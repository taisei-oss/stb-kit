# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import os
import sys
from argparse import Namespace, _SubParsersAction
from dataclasses import dataclass
from logging import Logger
from pathlib import Path
from typing import Any
from xml.etree.ElementTree import ParseError

from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_exceptions import DeveloperError, StbError
from stbkit.core.stb_reporting import (
    CollectingReporter,
    Reporter,
    Severity,
    get_reporter,
)

from stbkit.tools.converters._internal.pipeline.data import (
    _Data,
    _DataFormat,
    _DataFormatSet,
    _DataKind,
    _get_extension,
    _StbVersion,
)
from stbkit.tools.converters._internal.pipeline.execution import (
    _UnsupportedConversionError,
    cleanup_paths,
    execute_conversion,
    get_step,
    open_data,
    open_text_data,
    save_data,
    to_text,
)
from stbkit.tools.converters._internal.pipeline.stb_pipeline import StbData
from stbkit.tools.converters._internal.pipeline.step import _ExecutionResult

from . import common
from .constants_exit_code import (
    EXIT_EXECUTION_ERROR,
    EXIT_INVALID_ARGUMENT,
    EXIT_ISSUE_FOUND,
    EXIT_OK,
    EXIT_OPTIONAL_DEPENDENCY_MISSING,
)
from .global_parent import (
    get_interactive,
    get_logger,
    get_max_size,
    make_global_parent,
)


@dataclass(kw_only=True)
class ConverterArgs:
    input: str
    output: str
    from_format: str
    to_format: str
    yes: bool
    interactive: bool
    input_encoding: str | None
    via: str | None
    save_intermediate: dict[str, str | None]
    max_size: int
    logger: Logger
    reporter: Reporter

    def print_stb_info(self, stb: StBridgeRoot) -> None:
        logger = self.logger
        logger.info("ST-Bridgeモデル情報:")
        model = stb.stb_model_or_none  # type: ignore[attr-defined]
        if model is None:
            return
        if model.stb_nodes_or_none:
            logger.info(f" node数:{len(model.stb_nodes.stb_node)}")
        members = model.stb_members_or_none
        if members is None:
            return
        member_types = [
            "column",
            "girder",
            "post",
            "beam",
            "brace",
            "wall",
            "slab",
        ]
        for member_type in member_types:
            member_group = getattr(
                members,
                f"stb_{member_type}s_or_none",
                None,
            )
            if member_group is None:
                continue
            member_list = getattr(
                member_group,
                f"stb_{member_type}",
                None,
            )
            if member_list:
                logger.info(f" {member_type}数:{len(member_list)}")


@dataclass(frozen=True)
class _CliFormatSpec:
    data_format: _DataFormat
    label: str
    aliases: tuple[str, ...]
    description: tuple[str, ...] = ()


@dataclass(frozen=True)
class _CliRouteSpec:
    title: str
    from_format: str
    to_format: str
    via: tuple[str, ...] = ()
    note: str | None = None

    @property
    def command_example(self) -> str:
        command = f"--from {self.from_format} --to {self.to_format}"
        if self.via:
            command += f" --via {','.join(self.via)}"
        return command


_CLI_FORMAT_SPECS: tuple[_CliFormatSpec, ...] = (
    _CliFormatSpec(
        data_format=_DataFormat.STB,
        label="ST-Bridge",
        aliases=("stb",),
        description=(
            "拡張子.stbはST-Bridgeファイルと判定します。",
            (
                "バージョンの指定は stb-2.0.1 / stb-2.0.2 / stb-2.1.0 / stb-2.1.1 / "
                "stb-latest で指定できます。"
            ),
            "指定がない場合入力のST-Bridgeはバージョンを自動検出します。",
            "指定がない場合出力のST-Bridgeは最新版を使用します。",
        ),
    ),
    _CliFormatSpec(
        data_format=_DataFormat.IFC,
        label="IFC",
        aliases=("ifc", "ifc4"),
        description=("拡張子.ifcはIFCファイルと判定します。",),
    ),
    _CliFormatSpec(
        data_format=_DataFormat.PLY,
        label="PLY",
        aliases=("ply",),
        description=("拡張子.plyはPLYファイルと判定します。",),
    ),
)

_CLI_ROUTE_SPECS: tuple[_CliRouteSpec, ...] = (
    _CliRouteSpec(
        title="ST-Bridgeのバージョンアップ",
        from_format="stb-2.0.2",
        to_format="stb-latest",
        note="バージョンダウンはサポートしていません。",
    ),
    _CliRouteSpec(
        title="ST-BridgeからIFCへの変換",
        from_format="stb",
        to_format="ifc",
    ),
    _CliRouteSpec(
        title="ST-BridgeからPLYへの直接変換",
        from_format="stb",
        to_format="ply",
    ),
    _CliRouteSpec(
        title="ST-BridgeからIFCを経由したPLYへの変換",
        from_format="stb",
        to_format="ply",
        via=("ifc",),
    ),
)

_STB_VERSION_ALIASES: dict[str, _StbVersion] = {
    "stb-latest": _StbVersion.LATEST,
    "stb-2.0.1": _StbVersion.V2_0_1,
    "stb-2.0.2": _StbVersion.V2_0_2,
    "stb-2.1.0": _StbVersion.V2_1_0,
    "stb-2.1.1": _StbVersion.V2_1_1,
}


def _get_format_spec(data_format: _DataFormat) -> _CliFormatSpec:
    for spec in _CLI_FORMAT_SPECS:
        if spec.data_format == data_format:
            return spec
    raise ValueError(f"CLIで対応していないデータ形式です: {data_format}")


def _get_stb_version(
    normalized_format: str,
    *,
    for_output: bool,
) -> _StbVersion:
    if normalized_format == "stb":
        return _StbVersion.LATEST if for_output else _StbVersion.UNSPECIFIED

    version: _StbVersion | None = _STB_VERSION_ALIASES.get(normalized_format)
    if version is None:
        return _StbVersion.LATEST if for_output else _StbVersion.UNSPECIFIED
    return version


def _guess_format(path: str) -> str | None:
    if path == "-" or not path:
        return None
    return os.path.splitext(path)[1].lower().lstrip(".")


def _get_pipeline_format(
    format_name: str,
    *,
    for_output: bool,
) -> _DataFormatSet | None:
    """CLIのフォーマット指定をパイプラインのデータ形式へ変換する。"""
    normalized_format = format_name.strip().casefold().replace("_", "-")

    if normalized_format == "stb" or normalized_format in _STB_VERSION_ALIASES:
        return _DataFormatSet(
            _DataFormat.STB,
            _DataKind.OBJECT,
            stb_version=_get_stb_version(
                normalized_format,
                for_output=for_output,
            ),
        )

    for spec in _CLI_FORMAT_SPECS:
        if spec.data_format == _DataFormat.STB:
            continue
        if normalized_format in spec.aliases:
            return _DataFormatSet(spec.data_format, _DataKind.OBJECT)
    return None


def _require_pipeline_format(
    format_name: str,
    *,
    for_output: bool,
    role: str,
) -> _DataFormatSet:
    format_set: _DataFormatSet | None = _get_pipeline_format(
        format_name,
        for_output=for_output,
    )
    if format_set is None:
        raise _UnsupportedConversionError(f"{role}形式が不正です: {format_name}")
    return format_set


def _get_route_formats(via: str | None) -> list[_DataFormatSet]:
    if not via:
        return []
    result: list[_DataFormatSet] = []
    for item in via.split(","):
        format_name = item.strip()
        if not format_name:
            raise _UnsupportedConversionError("--via に空の文字列が指定されています")
        result.append(
            _require_pipeline_format(
                format_name,
                for_output=True,
                role="中間",
            )
        )
    return result


class _OverwriteDeniedError(Exception):
    """既存出力の上書きが許可されていないことを表す。"""


class _OutputPathConflictError(Exception):
    """入力・出力・中間出力のパスが衝突していることを表す。"""


def _confirm_overwrite(path: Path, *, yes: bool, interactive: bool) -> bool:
    if not path.exists() or yes:
        return True
    if not interactive:
        return False
    response: str = input(f"{path}は既に存在します。上書きしますか？(y/N):")
    return response.strip().casefold() in {"y", "yes"}


def _paths_conflict(path_a: Path, path_b: Path) -> bool:
    resolved_a: Path = path_a.resolve()
    resolved_b: Path = path_b.resolve()
    if resolved_a == resolved_b:
        return True

    if path_a.exists() and path_b.exists():
        try:
            return path_a.samefile(path_b)
        except OSError:
            return False
    return False


def _get_intermediate_paths(
    args: ConverterArgs,
    *,
    output_format: _DataFormat,
) -> list[tuple[str, Path]]:
    destinations: list[tuple[str, Path]] = []
    for format_name, specified_path in args.save_intermediate.items():
        format_set = _get_pipeline_format(format_name, for_output=True)
        if format_set is None:
            args.logger.warning("中間形式が不正です: %s", format_name)
            continue
        data_format = format_set.format
        if data_format == output_format:
            args.logger.info(
                "中間出力[%s]は最終出力と同じであるため省略します。",
                data_format.value,
            )
            continue

        path_text = specified_path
        if not path_text and args.output and args.output != "-":
            path_text = f"{args.output}{_get_extension(data_format)}"
        if not path_text:
            args.logger.warning(
                "中間形式[%s]の保存先を決定できません。"
                "標準出力を使う場合はpathを明示してください。",
                data_format.value,
            )
            continue
        destinations.append((f"中間出力({format_name})", Path(path_text)))
    return destinations


def _validate_path_collisions(
    args: ConverterArgs,
    *,
    output_path: Path | None,
    output_format: _DataFormat,
) -> list[tuple[str, Path]]:
    destinations = _get_intermediate_paths(args, output_format=output_format)
    targets: list[tuple[str, Path]] = []
    if args.input != "-":
        targets.append(("入力", Path(args.input)))
    if output_path is not None:
        targets.append(("最終出力", output_path))
    targets.extend(destinations)

    for index, (left_name, left_path) in enumerate(targets):
        for right_name, right_path in targets[index + 1 :]:
            if _paths_conflict(left_path, right_path):
                raise _OutputPathConflictError(
                    "入力ファイル・最終出力・中間出力の保存先は重複できません: "
                    f"{left_name}={left_path} / {right_name}={right_path}"
                )
    return destinations


def _save_intermediate_data(
    args: ConverterArgs,
    destinations: list[tuple[str, Path]],
    observed_data: dict[_DataFormat, _Data],
    output_format: _DataFormat,
) -> None:
    """各ステップで最後に得られたデータを保存する。"""
    destination_map: dict[str, Path] = {
        label.removeprefix("中間出力(").removesuffix(")"): path
        for label, path in destinations
    }
    for format_name in args.save_intermediate:
        path = destination_map.get(format_name)
        if path is None:
            continue

        format_set = _get_pipeline_format(format_name, for_output=True)
        if format_set is None:
            continue
        data_format = format_set.format
        data = observed_data.get(data_format)
        if data is None:
            args.logger.warning(
                "変換ルート上に中間形式[%s]がありません。",
                data_format.value,
            )
            continue
        if not _confirm_overwrite(path, yes=args.yes, interactive=args.interactive):
            args.logger.info(
                "中間ファイルの保存を省略しました: %s",
                path,
            )
            continue
        save_data(data, path, args.reporter)
        args.logger.info("中間ファイルを保存しました: %s", path)


def _pipeline_convert(args: ConverterArgs) -> None:
    input_format: _DataFormatSet = _require_pipeline_format(
        args.from_format,
        for_output=False,
        role="入力",
    )
    output_format: _DataFormatSet = _require_pipeline_format(
        args.to_format,
        for_output=True,
        role="出力",
    )
    route_formats: list[_DataFormatSet] = _get_route_formats(args.via)

    get_step(
        input_format,
        output_format,
        route_formats=route_formats,
        assign_guids=False,
    )

    output_path: Path | None = (
        None if not args.output or args.output == "-" else Path(args.output)
    )
    intermediate_paths: list[tuple[str, Path]] = _validate_path_collisions(
        args,
        output_path=output_path,
        output_format=output_format.format,
    )
    if (
        output_path is not None
        and output_path.exists()
        and not args.yes
        and args.input == "-"
    ):
        raise _OverwriteDeniedError(
            "標準入力を入力に使う場合、既存出力を上書きするには-y/--yesの指定が必要です。"
        )
    if output_path is not None and not _confirm_overwrite(
        output_path,
        yes=args.yes,
        interactive=args.interactive,
    ):
        raise _OverwriteDeniedError(
            "出力先ファイルが既に存在します。上書きするには-y/--yesの指定が必要です。"
        )

    if not args.input or args.input == "-":
        input_data: _Data = open_text_data(
            common.read_stdin_xml(max_size=args.max_size, encoding=args.input_encoding),
            input_format,
            args.reporter,
            max_size=args.max_size,
        )
    else:
        input_data = open_data(
            Path(args.input),
            input_format,
            args.reporter,
            encoding=args.input_encoding,
            max_size=args.max_size,
        )

    if isinstance(input_data, StbData):
        args.print_stb_info(input_data.value)

    observed_data: dict[_DataFormat, _Data] = {
        input_data.format: input_data,
    }

    def on_step_completed(step_name: str, data: _Data) -> None:
        args.logger.debug(
            "変換ステップ完了: %s (%s)",
            step_name,
            data.format_set,
        )
        observed_data[data.format] = data

    result: _ExecutionResult[_Data] = execute_conversion(
        input_data,
        output_format,
        route_formats=route_formats,
        reporter=args.reporter,
        assign_guids=False,
        on_step_completed=on_step_completed,
    )
    try:
        if output_path is None:
            sys.stdout.write(
                to_text(
                    result.output,
                    args.reporter,
                )
            )
            sys.stdout.flush()
        else:
            save_data(result.output, output_path, args.reporter)
        _save_intermediate_data(
            args,
            intermediate_paths,
            observed_data,
            output_format.format,
        )
    finally:
        cleanup_paths(result.cleanup_paths)


def register(subparsers: _SubParsersAction[Any]) -> None:
    parser = subparsers.add_parser(
        "convert",
        parents=[make_global_parent()],
        help=("ファイルフォーマット変換ツール。入出力形式を指定して変換します。"),
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="入力ファイルのパス。-で標準入力を使用します。",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="-",
        help="出力ファイルのパス。-で標準出力を使用します。",
    )
    parser.add_argument(
        "-f",
        "--from",
        dest="from_format",
        help="入力ファイル形式。省略時は拡張子から推測します。",
    )
    parser.add_argument(
        "-t",
        "--to",
        dest="to_format",
        help="出力ファイル形式。省略時は拡張子から推測します。",
    )
    parser.add_argument(
        "-y", "--yes", action="store_true", help="確認なしで上書きします。"
    )
    parser.add_argument(
        "--input-encoding",
        help="入力ファイルのエンコーディングを指定します。"
        "省略時は自動検出またはutf-8を使用します。",
    )
    parser.add_argument(
        "--via",
        help=("中間形式を指定します。複数指定する場合はカンマで区切ります。"),
    )
    parser.add_argument(
        "--save-intermediate",
        help="中間ファイルを保存します。例: stb,ifc=result.ifc",
    )
    parser.add_argument(
        "--list-formats",
        action="store_true",
        help="対応しているファイル形式を表示します。",
    )

    parser.set_defaults(func=_run, _parser=parser)


def _print_list_formats() -> None:
    print("対応しているファイル形式")
    for spec in _CLI_FORMAT_SPECS:
        print(f"- {spec.label}: {'/'.join(spec.aliases)}")
        for line in spec.description:
            print(f"    {line}")

    print("対応している変換形式の組み合わせ")
    for route in _CLI_ROUTE_SPECS:
        print(f"- {route.title}")
        print(f"    {route.command_example}")
        if route.note:
            print(f"    {route.note}")


def _get_save_intermediate(value: str | None) -> dict[str, str | None]:
    result: dict[str, str | None] = {}
    if not value:
        return result
    for raw_item in value.split(","):
        item: str = raw_item.strip()
        if not item:
            continue
        key, separator, path = item.partition("=")
        key = key.strip()
        if not key:
            continue
        result[key] = path.strip() if separator and path.strip() else None
    return result


def _run(args: Namespace) -> None:
    logger: Logger = get_logger(args)
    logger.info("---変換処理開始---")
    if args.list_formats:
        _print_list_formats()
        raise SystemExit(EXIT_OK)

    interactive: bool = get_interactive(args)
    input_path: str = args.input or ""
    if not input_path:
        if interactive:
            print("入力ファイルパスを入力してください: ")
            input_path = input().strip()
        else:
            input_path = "-"

    output_path: str = args.output or ""
    if not output_path:
        if interactive:
            print("出力ファイルパスを入力してください: ")
            output_path = input().strip()
        else:
            output_path = "-"

    from_format: str | None = args.from_format or _guess_format(input_path)
    if not from_format and interactive:
        print("入力ファイル形式を指定してください: ")
        from_format = input().strip()
    if not from_format:
        args._parser.error("入力ファイル形式が不明です")
        raise AssertionError("到達しない場所: ArgumentParser.error() must not return")

    to_format: str | None = args.to_format or _guess_format(output_path)
    if not to_format and interactive:
        print("出力ファイル形式を指定してください: ")
        to_format = input().strip()
    if not to_format:
        args._parser.error("出力ファイル形式が不明です")
        raise AssertionError("到達しない場所: ArgumentParser.error() must not return")

    collecting_reporter: CollectingReporter = CollectingReporter()
    reporter: Reporter = get_reporter(logger=logger, reporter=collecting_reporter)
    converter_args: ConverterArgs = ConverterArgs(
        input=input_path,
        output=output_path,
        from_format=from_format,
        to_format=to_format,
        yes=bool(args.yes),
        interactive=interactive,
        input_encoding=args.input_encoding,
        via=args.via,
        save_intermediate=_get_save_intermediate(args.save_intermediate),
        max_size=get_max_size(args),
        logger=logger,
        reporter=reporter,
    )

    try:
        _pipeline_convert(converter_args)
    except _UnsupportedConversionError as error:
        logger.error(
            "サポートされない変換です。\n"
            f"  入力 format: {from_format} path:{input_path}\n"
            f"  出力 format: {to_format} path:{output_path}\n"
            f"  詳細: {error}"
        )
        raise SystemExit(EXIT_INVALID_ARGUMENT) from None
    except _OverwriteDeniedError as error:
        logger.error(str(error))
        raise SystemExit(EXIT_INVALID_ARGUMENT) from None
    except _OutputPathConflictError as error:
        logger.error(str(error))
        raise SystemExit(EXIT_INVALID_ARGUMENT) from None
    except FileNotFoundError as error:
        logger.error(f"入力ファイルが見つかりません: {error.filename or input_path}")
        raise SystemExit(EXIT_INVALID_ARGUMENT) from None
    except ImportError as error:
        logger.error(str(error))
        raise SystemExit(EXIT_OPTIONAL_DEPENDENCY_MISSING) from None
    except DeveloperError:
        raise
    except (StbError, ParseError, UnicodeDecodeError) as error:
        logger.error(f"入力ファイルを処理できません: {error}")
        raise SystemExit(EXIT_EXECUTION_ERROR) from None

    logger.info("---変換完了---")
    if not collecting_reporter.is_valid(min_level=Severity.ERROR):
        raise SystemExit(EXIT_ISSUE_FOUND)
    raise SystemExit(EXIT_OK)
