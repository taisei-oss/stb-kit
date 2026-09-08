# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
from collections.abc import Mapping
from functools import cache
from pathlib import Path
from typing import Any

from ...stb_reporting import Code, NullReporter, Phase
from ...validation._internal.common import ValidationContext
from ..extension_utils import ExtensionInfoRepository


def _print_import_error() -> None:
    import sys

    print(
        "xmlschemaがインストールされていません。下記コマンドでインストールしてください。\n"
        "pip install xmlschema\n"
        "または\n"
        "pip install stbkit[xsd]\n",
        file=sys.stderr,
    )


@cache
def _load_xmlschema(xsd_path: Path) -> Any:
    import xmlschema

    xsd_str: str = xsd_path.read_text(encoding="utf-8")
    # 公式スキーマのファイル頭に余計な文字が入っているのを取り除く処理
    while xsd_str and xsd_str[0] != "<":
        xsd_str = xsd_str[1:]

    return xmlschema.XMLSchema(xsd_str)


# 定義に無い属性のエラーメッセージを検出する正規表現。
_ATTRIBUTE_NOT_ALLOWED_RE = re.compile(
    r"^'(?P<name>[^']+)' attribute not allowed for element$"
)


def _is_legal_extension_error(error: Any, *, ext_repo: ExtensionInfoRepository) -> bool:
    """XSDのエラーが、ST-Bridge仕様で認められる拡張かを返す

    判断できないエラーはFalse
    """
    from xmlschema.validators import XMLSchemaChildrenValidationError

    from ...stb_io._internal.stream_reader import _delete_namespace

    elem: Any = getattr(error, "elem", None)
    if elem is None:
        return False
    element_name: str = _delete_namespace(str(elem.tag))

    if isinstance(error, XMLSchemaChildrenValidationError):
        if error.invalid_tag is None:
            return False
        return ext_repo._is_allowed_child_name(
            child_name=_delete_namespace(str(error.invalid_tag)),
            parent_name=element_name,
        )

    matched = _ATTRIBUTE_NOT_ALLOWED_RE.match(str(getattr(error, "reason", None) or ""))
    if matched is None:
        return False
    attribute_name: str = matched.group("name")
    # 解釈が適切か、要素が実際にその属性を持つかで確認する
    attributes: Any = getattr(error, "obj", None)
    if not isinstance(attributes, Mapping) or attribute_name not in attributes:
        return False
    return attribute_name in ext_repo._allowed_attribute_names_by_element_name(
        element_name
    )


def validate_by_xsd(
    xsd_path: Path | None,
    ctx: ValidationContext,
    *,
    require_xsd: bool = False,
    use_cache: bool = True,
    exclude_legal_extensions: bool = False,
) -> bool:
    try:
        if xsd_path is None:
            ctx.reporter.error(
                message="xsd:XSDファイルのパスが指定されていません。XSDによるスキーマチェックはスキップします。",
                code=Code.SCHEMA_ERROR,
                phase=Phase.VALIDATE,
            )
            return not require_xsd
        import xmlschema
        from xmlschema import XMLSchemaException

        try:
            resolved_xsd_path: Path = xsd_path.resolve()
            if use_cache:
                schema = _load_xmlschema(resolved_xsd_path)
            else:
                schema = xmlschema.XMLSchema(resolved_xsd_path)
        except XMLSchemaException as e:
            ctx.reporter.error(
                message=f"xsd:XSDファイルの読み込みに失敗しました: {e}。詳細スキーマチェックはスキップします。",
                code=Code.UNEXPECTED_ERROR,
                phase=Phase.VALIDATE,
            )
            return not require_xsd
        ext_repo: ExtensionInfoRepository | None = None
        if exclude_legal_extensions:
            ext_repo = ExtensionInfoRepository()
            # 拡張定義のエラーメッセージはload時に出力しているため、ここでは出力しない
            ext_repo.register(ctx.obj(), reporter=NullReporter())
        errors = []
        xpaths = []
        for error in schema.iter_errors(ctx.xml()):
            if ext_repo is not None and _is_legal_extension_error(
                error, ext_repo=ext_repo
            ):
                continue
            line = getattr(error, "line", None)
            xpath = error.path
            raw_msg = (
                getattr(error, "reason", None)
                or getattr(error, "message", None)
                or str(error)
            )
            msg = str(raw_msg).strip()
            info = []
            if line is not None:
                info.append(f"line-{line}")
            info_str = " / ".join(info)
            if info_str:
                errors.append(f"{info_str}: {msg}")
            else:
                errors.append(f"{msg}")
            xpaths.append(xpath)

        if not errors:
            return True
        else:
            for err, xpath in zip(errors, xpaths):
                ctx.reporter.error(
                    message=f"xsd:{err}",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.VALIDATE,
                    xpath=xpath,
                )
            return False
    except ImportError:
        ctx.reporter.warning(
            message="xmlschemaパッケージがインストールされていません。XSDによるスキーマチェックはスキップします。",
            code=Code.OPTIONAL_DEPENDENCY_MISSING,
            phase=Phase.VALIDATE,
        )
        _print_import_error()
        return not require_xsd
