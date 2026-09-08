# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from pathlib import Path
from typing import Any, ClassVar

from ..._internal import constants
from ..._internal.name_converter import private_field_name
from ..._internal.optional_dependencies.xmlschema_validator import (
    validate_by_xsd,
)
from ...data_model.common import StBridgeElement, _FieldKind
from ...stb_reporting import Code, Phase, Reporter
from .common import BaseValidator, CompositeValidator, ValidationContext


def _uses_xsd(*, xsd_path: Path | None, require_xsd: bool) -> bool:
    """XSDによるスキーマチェックを実行するかどうか。

    XSDを明示的に指定した場合は、require_xsdによらずXSDチェックを実施する。
    """
    return xsd_path is not None or require_xsd


class FieldValidator(BaseValidator):
    """field_infoによるチェック"""

    def validate(self, ctx: ValidationContext) -> bool:
        return self.validate_element(obj=ctx.obj(), reporter=ctx.reporter)

    def validate_element(self, obj: StBridgeElement, reporter: Reporter) -> bool:
        is_valid = True
        for field_name, field_info in obj._fields.items():
            p_field_name = private_field_name(field_name)
            value: Any = getattr(obj, p_field_name)
            match field_info.kind:
                case _FieldKind.ATTRIBUTE:
                    if value is None:
                        if field_info.required:
                            reporter.warning(
                                message=f"必須属性[{obj._xml_name(field_name)}]がnullです",
                                code=Code.SCHEMA_ERROR,
                                phase=Phase.VALIDATE,
                                stb_element=obj,
                                attr_name=field_name,
                            )
                            is_valid = False
                    else:
                        if field_info.choices and value not in field_info.choices:
                            reporter.warning(
                                message=(
                                    f"属性[{obj._xml_name(field_name)}]の値[{value}]が不正です。"
                                    f"許容値: {field_info.choices}"
                                ),
                                code=Code.SCHEMA_ERROR,
                                phase=Phase.VALIDATE,
                                stb_element=obj,
                                attr_name=field_name,
                                value=value,
                                ref_value=str(field_info.choices),
                            )
                            is_valid = False
                case _FieldKind.CONTENT:
                    if value is None or (isinstance(value, list) and not value):
                        reporter.warning(
                            message=f"要素[{obj._xml_name()}]の内容がありません",
                            code=Code.SCHEMA_ERROR,
                            phase=Phase.VALIDATE,
                            stb_element=obj,
                            attr_name=field_name,
                            value="",
                        )
                        is_valid = False
                case _FieldKind.ELEMENT:
                    if field_info.max_occurs == 1:
                        if value is None and field_info.min_occurs == 1:
                            reporter.warning(
                                message=f"必須要素[{obj._xml_name(field_name)}]の最小回数は1です",
                                code=Code.SCHEMA_ERROR,
                                phase=Phase.VALIDATE,
                                stb_element=obj,
                                attr_name=field_name,
                            )
                            is_valid = False
                        if isinstance(value, StBridgeElement):
                            is_valid &= self.validate_element(value, reporter)
                    else:
                        if not isinstance(value, list):
                            raise AssertionError(
                                f"{obj.__class__.__name__}の[{field_name}]の値がリストではありません"
                            )
                        else:
                            if (
                                field_info.min_occurs is not None
                                and len(value) < field_info.min_occurs
                            ):
                                reporter.warning(
                                    message=(f"最小回数は{field_info.min_occurs}です"),
                                    code=Code.SCHEMA_ERROR,
                                    phase=Phase.VALIDATE,
                                    stb_element=obj,
                                    attr_name=field_name,
                                    value=str(len(value)),
                                    ref_value=f">={field_info.min_occurs}",
                                )
                                is_valid = False
                            if (
                                field_info.max_occurs is not None
                                and len(value) > field_info.max_occurs
                            ):
                                reporter.warning(
                                    message=(f"最大回数は{field_info.max_occurs}です"),
                                    code=Code.SCHEMA_ERROR,
                                    phase=Phase.VALIDATE,
                                    stb_element=obj,
                                    attr_name=field_name,
                                    value=str(len(value)),
                                    ref_value=f"<={field_info.max_occurs}",
                                )
                                is_valid = False
                            for item in value:
                                if isinstance(item, StBridgeElement):
                                    is_valid &= self.validate_element(item, reporter)
                                else:
                                    raise TypeError(
                                        f"{obj.__class__.__name__}の[{field_name}]の要素がStBridgeElementではありません"
                                    )
        return is_valid


class EmptyValueValidator(BaseValidator):
    """空文字列のチェック。XSDチェックでは検出されないため別途実施する。"""

    def validate(self, ctx: ValidationContext) -> bool:
        return EmptyValueValidator.validate_element(
            obj=ctx.obj(), reporter=ctx.reporter
        )

    @staticmethod
    def validate_element(obj: StBridgeElement, reporter: Reporter) -> bool:
        result: bool = True
        for field_name, field_info in obj._fields.items():
            p_field_name = private_field_name(field_name)
            value: Any = getattr(obj, p_field_name)
            if (
                field_info.kind == _FieldKind.ATTRIBUTE
                and isinstance(value, str)
                and value == ""
            ):
                reporter.error(
                    message=f"要素[{obj._xml_name(field_name)}]の値がemptyです",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.VALIDATE,
                    stb_element=obj,
                    attr_name=field_name,
                )
                result = False
            elif field_info.kind == _FieldKind.ELEMENT and isinstance(
                value, StBridgeElement
            ):
                if not EmptyValueValidator.validate_element(value, reporter):
                    result = False
            elif field_info.kind == _FieldKind.ELEMENT and isinstance(value, list):
                for item in value:
                    if isinstance(
                        item, StBridgeElement
                    ) and not EmptyValueValidator.validate_element(item, reporter):
                        result = False
            elif (
                field_info.kind == _FieldKind.CONTENT
                and isinstance(value, str)
                and value == ""
            ):
                reporter.error(
                    message="要素の内容の値がemptyです",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.VALIDATE,
                    stb_element=obj,
                    attr_name=field_name,
                )
                result = False
        return result


class XsdSchemaValidator(BaseValidator):
    """XSDによるスキーマチェック"""

    _env_var_mapping: ClassVar[dict[str, str]] = {
        "2.0.0": constants.ENV_NAME_SCHEMA_PATH_STB_V2_0_0,
        "2.0.1": constants.ENV_NAME_SCHEMA_PATH_STB_V2_0_1,
        "2.0.2": constants.ENV_NAME_SCHEMA_PATH_STB_V2_0_2,
        "2.1.0": constants.ENV_NAME_SCHEMA_PATH_STB_V2_1_0,
        "2.1.1": constants.ENV_NAME_SCHEMA_PATH_STB_V2_1_1,
    }

    def __init__(
        self,
        *,
        xsd_path: Path | None = None,
        require_xsd: bool,
        exclude_legal_extensions: bool = False,
    ) -> None:
        self._xsd_path: Path | None = xsd_path
        self._require_xsd: bool = require_xsd
        self._exclude_legal_extensions: bool = exclude_legal_extensions

    def validate(self, ctx: ValidationContext) -> bool:
        if self._xsd_path is not None:
            return validate_by_xsd(
                self._xsd_path,
                ctx,
                require_xsd=self._require_xsd,
                exclude_legal_extensions=self._exclude_legal_extensions,
            )

        version: str
        if ctx._stb is not None:
            version = ctx._stb.version
        elif ctx._xml is not None:
            # 読み込み時の循環参照を避けるため、遅延インポートする。
            from ...stb_io._internal.loader import _detect_version

            version = _detect_version(ctx._xml)
        else:
            ctx.reporter.error(
                message="STBridgeオブジェクトもXML文字列も提供されていません。スキーマバリデーションを実行できません。",
                code=Code.SCHEMA_ERROR,
                phase=Phase.VALIDATE,
            )
            return False
        if version not in self._env_var_mapping:
            ctx.reporter.error(
                message=f"STBridgeバージョン[{version}]のxsdチェックは対応していません。",
                code=Code.SCHEMA_ERROR,
                phase=Phase.VALIDATE,
            )
            return not self._require_xsd
        xsd_path: Path | None = self.get_xsd_path_for_version(version)
        if xsd_path is None:
            ctx.reporter.error(
                message=(
                    f"STBridgeバージョン[{version}]に対応するXSDファイルが見つかりません。"
                    f"環境変数[{self._env_var_mapping[version]}]にXSDファイルのパスを設定してください。"
                ),
                code=Code.SCHEMA_ERROR,
                phase=Phase.VALIDATE,
            )
            return not self._require_xsd
        return validate_by_xsd(
            xsd_path,
            ctx,
            require_xsd=self._require_xsd,
            exclude_legal_extensions=self._exclude_legal_extensions,
        )

    @classmethod
    def get_xsd_path_for_version(cls, version: str) -> Path | None:
        env_var_name: str | None = cls._env_var_mapping.get(version)
        if env_var_name:
            xsd_path_str = os.getenv(env_var_name)
            if xsd_path_str:
                return Path(xsd_path_str)
        return None


class SchemaValidator(CompositeValidator):
    """総合的なスキーマチェックを行うためのばりでーたー。XSDで検出されないエラー検出も含む"""

    def __init__(
        self,
        *,
        xsd_path: Path | None = None,
        require_xsd: bool = False,
        exclude_legal_extensions: bool = False,
    ) -> None:
        validators: list[BaseValidator] = []
        # XSDチェックとかぶるバリデーター
        if _uses_xsd(xsd_path=xsd_path, require_xsd=require_xsd):
            validators.append(
                XsdSchemaValidator(
                    xsd_path=xsd_path,
                    require_xsd=require_xsd,
                    exclude_legal_extensions=exclude_legal_extensions,
                )
            )
        else:
            validators.append(FieldValidator())
        # XSDチェックとかぶらないバリデーター
        validators.append(EmptyValueValidator())
        super().__init__(validators)
