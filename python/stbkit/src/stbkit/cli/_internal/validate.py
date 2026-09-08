# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import sys
from argparse import Namespace, _SubParsersAction
from pathlib import Path
from typing import Any, Never
from xml.etree.ElementTree import ParseError

from stbkit.core._internal.io_text import load_text
from stbkit.core.stb_exceptions import DeveloperError, StbError
from stbkit.core.stb_io._internal.loader import _detect_encoding
from stbkit.core.stb_reporting import (
    Code,
    CollectingReporter,
    Phase,
    Severity,
)
from stbkit.core.validation._internal.validator import validate_schema

from . import common
from .constants_exit_code import (
    EXIT_EXECUTION_ERROR,
    EXIT_INVALID_ARGUMENT,
    EXIT_ISSUE_FOUND,
    EXIT_OK,
    EXIT_OPTIONAL_DEPENDENCY_MISSING,
)
from .global_parent import get_interactive, get_max_size, make_global_parent


def _check_optional_dependency(reporter: CollectingReporter) -> bool:
    return any(
        item.code == Code.OPTIONAL_DEPENDENCY_MISSING.value for item in reporter.report
    )


def _try_validate_report(
    input_path: str,
    *,
    schema_path: str | None,
    max_size: int,
    require_xsd: bool,
    exclude_legal_extensions: bool,
) -> tuple[CollectingReporter | None, str]:
    # XMLとして読み込めなかった場合は、チェック結果ではなく実行の失敗なので(None, エラーメッセージ)を返す。
    # ST-Bridgeとしての不正はチェック結果であるため、エラーとしない。
    try:
        reporter: CollectingReporter = _validate_report(
            input_path,
            schema_path=schema_path,
            max_size=max_size,
            require_xsd=require_xsd,
            exclude_legal_extensions=exclude_legal_extensions,
        )
    except DeveloperError:
        raise
    except (StbError, ParseError, UnicodeDecodeError) as error:
        return None, f"入力ファイルを処理できません: {error}"
    return reporter, ""


def _has_error(reporter: CollectingReporter) -> bool:
    # 任意依存の不足以外
    return any(
        item.severity >= Severity.WARNING.value
        and item.code != Code.OPTIONAL_DEPENDENCY_MISSING.value
        for item in reporter.report
    )


def register(subparsers: _SubParsersAction[Any]) -> None:
    parser = subparsers.add_parser(
        "validate",
        parents=[make_global_parent()],
        help=(
            "ST-Bridgeのバリデーションを行います。\n"
            "--schemaを指定すると、指定されたXSDスキーマでの検査を行います。\n"
            "XSDスキーマの指定は環境変数でも可能です\n"
            "XSDスキーマの指定を行わない場合は、stbkit-coreのデータモデルが持つ情報でチェックを行います。"
        ),
    )
    common.use_input(parser)
    common.use_output(parser)
    common.use_yes(parser)
    parser.add_argument(
        "--schema",
        help="チェックに利用するXSDスキーマファイルのパス",
    )
    parser.add_argument(
        "--require-xsd",
        action="store_true",
        help="XSDスキーマによる検査を必須にします",
    )
    parser.add_argument(
        "--exclude-legal-extensions",
        action="store_true",
        help="StbExtensionsで定義された拡張に由来するXSDスキーマチェック時のエラーをXSD結果から除外します。\n"
        "XSDを利用しない場合はこのオプションは不要です。",
    )
    common.use_quiet(parser)

    parser.set_defaults(func=_run, _parser=parser)


def _run(args: Namespace) -> None:
    input_path_str: str = common.get_input(args)
    output_path: str = common.get_output(args)
    yes: bool = common.get_yes(args)
    quiet: bool = common.get_quiet(args)
    interactive: bool = get_interactive(args)
    schema: str | None = args.schema
    require_xsd: bool = bool(args.require_xsd)
    exclude_legal_extensions: bool = bool(args.exclude_legal_extensions)
    max_size: int = get_max_size(args)

    if schema:
        schema_path = Path(schema)
        if not schema_path.is_file():
            _exit_with_error(
                f"指定されたXSDスキーマファイルが存在しません: {schema_path}"
            )

    is_valid: bool = True
    from_stdin: bool = input_path_str == "-"
    input_path: Path = Path(input_path_str)

    if not from_stdin:
        try:
            common.ensure_output_not_input(output_path, (input_path,))
        except ValueError as error:
            _exit_with_error(f"バリデーション結果の{error}")

    if not common.confirm_overwrite(
        output=output_path,
        yes=yes,
        interactive=interactive,
    ):
        _exit_with_error(
            "出力先ファイルが既に存在します。上書きするには-y/--yesを指定してください。"
        )

    result: list[str] = []
    lacks_optional_dependency = False
    has_target_issue = False
    has_unreadable_input = False

    if from_stdin or input_path.is_file():
        result.append("入力： 標準入力" if from_stdin else f"ファイル： {input_path}")
        reporter, read_error = _try_validate_report(
            input_path_str,
            schema_path=schema,
            max_size=max_size,
            require_xsd=require_xsd,
            exclude_legal_extensions=exclude_legal_extensions,
        )
        if reporter is None:
            print(read_error, file=sys.stderr)
            sys.exit(EXIT_EXECUTION_ERROR)
        result.extend(_output_report(reporter, quiet=quiet))
        is_valid = reporter.is_valid()
        lacks_optional_dependency = _check_optional_dependency(reporter)
        has_target_issue = _has_error(reporter)
    elif input_path.is_dir():
        result.append(f"ディレクトリ: {input_path}")
        result.append("ディレクトリ内のST-Bridgeファイルを再帰的に検査します。")
        xml_files: list[Path] = list(input_path.rglob("*.stb"))
        try:
            common.ensure_output_not_input(output_path, xml_files)
        except ValueError as error:
            _exit_with_error(f"バリデーション結果の{error}")
        if not xml_files:
            result.append("ディレクトリ内にST-Bridgeファイルが見つかりませんでした。")
            is_valid = False
        else:
            result_files: list[str] = []
            error_file_count: list[tuple[str, int]] = []
            for xml_file in xml_files:
                reporter, read_error = _try_validate_report(
                    str(xml_file),
                    schema_path=schema,
                    max_size=max_size,
                    require_xsd=require_xsd,
                    exclude_legal_extensions=exclude_legal_extensions,
                )
                if reporter is None:
                    # 1つのファイルが読めなくても残りのバリデーションは続ける
                    result_files.append("-" * 3)
                    result_files.append(f"ファイル: {xml_file}")
                    result_files.append(read_error)
                    has_unreadable_input = True
                    is_valid = False
                    continue
                file_result = _output_report(reporter, quiet=quiet)
                result_files.append("-" * 3)
                result_files.append(f"ファイル: {xml_file}")
                result_files.extend(file_result)
                if _check_optional_dependency(reporter):
                    lacks_optional_dependency = True
                if _has_error(reporter):
                    has_target_issue = True
                if not reporter.is_valid():
                    error_file_count.append((str(xml_file), len(reporter.report)))
                    is_valid = False
            result.append(f"{len(xml_files)}ファイルが見つかりました。")
            if is_valid:
                result.append("すべてのファイルがOKです。")
            else:
                result.append(
                    f"{len(error_file_count)}ファイルにエラーが見つかりました。"
                )
                for file, count in error_file_count:
                    result.append(f"  {file}: {count}件のエラー")
                result.extend(result_files)
    else:
        _exit_with_error(
            f"入力パスはファイルまたはディレクトリである必要があります: {input_path}"
        )

    if is_valid:
        if not quiet:
            if output_path == "-":
                print("\n".join(result))
            else:
                common.write_text_via_temporary_file(
                    output=output_path,
                    text="\n".join(result),
                    encoding="utf-8",
                )
        sys.exit(EXIT_OK)
    else:
        error_text: str = "\n".join(result)
        if output_path == "-":
            print(error_text, file=sys.stderr)
        else:
            common.write_text_via_temporary_file(
                output=output_path,
                text=error_text,
                encoding="utf-8",
            )
            print(error_text, file=sys.stderr)
        # 検査が実行できた場合は、検査のエラーを優先する。
        # 検査で問題を見つけられなかった場合は、実行できなかった原因を返す。
        if not has_target_issue:
            if has_unreadable_input:
                sys.exit(EXIT_EXECUTION_ERROR)
            if lacks_optional_dependency:
                sys.exit(EXIT_OPTIONAL_DEPENDENCY_MISSING)
        sys.exit(EXIT_ISSUE_FOUND)


def _output_report(reporter: CollectingReporter, quiet: bool) -> list[str]:
    result: list[str] = []
    if reporter.is_valid():
        result.append("結果: OK")
    else:
        result.append("結果: NG")
        result.append("エラー数: " + str(len(reporter.report)))
        result.append("エラー詳細:")
        result.append(reporter.report.to_text())
    return result


def _validate_report(
    input_path: str,
    schema_path: str | None,
    *,
    max_size: int,
    require_xsd: bool,
    exclude_legal_extensions: bool,
) -> CollectingReporter:
    xsd_path: Path | None = Path(schema_path) if schema_path else None

    reporter: CollectingReporter = CollectingReporter(
        default_code=Code.SCHEMA_ERROR, default_phase=Phase.VALIDATE
    )

    if xsd_path is not None and not xsd_path.is_file():
        reporter.error(f"指定されたXSDスキーマファイルが存在しません: {xsd_path}")
        return reporter

    xml_text: str
    if input_path == "-":
        xml_text = common.read_stdin_xml(max_size=max_size)
    else:
        xml_path: Path = Path(input_path)
        if not xml_path.is_file():
            reporter.error(f"指定されたST-Bridgeファイルが存在しません: {xml_path}")
            return reporter
        encoding: str = _detect_encoding(xml_path)
        xml_text = load_text(xml_path, encoding=encoding, max_size=max_size)

    validate_schema(
        xml_text,
        reporter=reporter,
        xsd_path=xsd_path,
        require_xsd=require_xsd,
        exclude_legal_extensions=exclude_legal_extensions,
    )
    return reporter


def _exit_with_error(message: str) -> Never:
    print(message, file=sys.stderr)
    sys.exit(EXIT_INVALID_ARGUMENT)
