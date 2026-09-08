# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import math
import sys
from argparse import ArgumentParser, Namespace, _SubParsersAction
from pathlib import Path
from typing import Any, Never

from stbkit.core._internal.io_text import load_text
from stbkit.core.stb_io._internal.loader import _detect_encoding
from stbkit.core.stb_io._internal.stream_reader import check_no_doctype

from stbkit.tools._internal.diff.diff_xml import (
    XmlCompareOption,
    compare_xml_str,
)

from . import common
from .constants_exit_code import (
    EXIT_EXECUTION_ERROR,
    EXIT_INVALID_ARGUMENT,
    EXIT_ISSUE_FOUND,
    EXIT_OK,
)
from .global_parent import get_max_size, make_global_parent


def register(subparsers: _SubParsersAction[Any]) -> None:
    parser = subparsers.add_parser(
        "diff",
        parents=[make_global_parent()],
        help="2つのモデルを比較します。",
    )
    diff_subparsers = parser.add_subparsers(
        dest="diff_command",
        title="比較方式",
    )
    _register_xml_command(diff_subparsers)

    # ``stbkit diff`` 単独では比較せず、利用可能な方式を表示する。
    parser.set_defaults(func=_show_diff_help, _parser=parser)


def _register_xml_command(subparsers: _SubParsersAction[Any]) -> None:
    parser = subparsers.add_parser(
        "xml",
        help="2つのST-Bridge XMLをXML構造として比較します。",
    )
    _use_common_arguments(parser)
    parser.add_argument(
        "--ignore-guid",
        action="store_true",
        help="guid属性を比較対象から除外します。",
    )
    parser.add_argument(
        "--compare-by-order",
        action="store_true",
        help=("guidやidで対応付けず、同じタグの子要素をタグ内の出現順で比較します。"),
    )
    parser.add_argument(
        "--compare-tag-order",
        action="store_true",
        help=("異なるタグを含む子要素のタグの並び順も差分として検出します。"),
    )
    parser.add_argument(
        "--combine-attribute-diffs",
        action="store_true",
        help="同じ要素の複数の属性差分を1行にまとめます。",
    )
    parser.set_defaults(func=_run_xml)


def _use_common_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "reference",
        type=Path,
        metavar="REFERENCE",
        help="基準、期待値、または変更前のファイルです。",
    )
    parser.add_argument(
        "candidate",
        type=Path,
        metavar="CANDIDATE",
        help="比較対象、実測値、または変更後のファイルです。",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="-",
        metavar="PATH",
        help="比較レポートの出力先です。省略時は標準出力へ出力します。",
    )
    parser.add_argument(
        "--exit-zero",
        action="store_true",
        help="差分が見つかった場合も終了コード0を返します。",
    )


def _show_diff_help(args: Namespace) -> Never:
    parser: ArgumentParser = args._parser
    parser.print_help()
    raise SystemExit(EXIT_OK)


def _run_xml(args: Namespace) -> None:
    reference: Path = args.reference
    candidate: Path = args.candidate

    try:
        max_size: int = get_max_size(args)
        _validate_output_path(args.output, reference, candidate)
        reference_xml = _read_xml(reference, max_size=max_size)
        candidate_xml = _read_xml(candidate, max_size=max_size)
        compare_option = XmlCompareOption()
        if args.ignore_guid:
            compare_option.filter_option.global_attribute_filter.exclude.append("guid")
        compare_option.ignore_order_children = not bool(args.compare_by_order)
        compare_option.compare_tag_order = bool(args.compare_tag_order)
        result = compare_xml_str(reference_xml, candidate_xml, compare_option)
        if args.combine_attribute_diffs:
            result = result.combine_attribute_diffs()
        report_text = result.to_reporting_result().to_text()
        _write_report(report_text, args.output)
    except FileNotFoundError as error:
        # 指定されたパスが誤っている場合。比較を始められていないため、
        # 比較中の失敗とは区別する。
        _exit_with_invalid_argument(error)
    except Exception as error:  # noqa: BLE001
        _exit_with_error("XML比較に失敗しました", error)

    _exit_for_result(equal=result.equal, exit_zero=bool(args.exit_zero))


def _read_xml(path: Path, *, max_size: int) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"入力ファイルが見つかりません: {path}")
    xml: str = load_text(path, encoding=_detect_encoding(path), max_size=max_size)
    check_no_doctype(xml)
    return xml


def _validate_geometry_inputs(reference: Path, candidate: Path) -> None:
    for path in (reference, candidate):
        if not path.is_file():
            raise FileNotFoundError(f"入力ファイルが見つかりません: {path}")

    suffixes = (reference.suffix.lower(), candidate.suffix.lower())
    supported = {
        (".stb", ".stb"),
        (".stb", ".ifc"),
        (".ifc", ".stb"),
    }
    if suffixes not in supported:
        raise ValueError(
            "対応している組合せはST-Bridge同士、またはST-BridgeとIFCです: "
            f"{reference.suffix or '(拡張子なし)'} / "
            f"{candidate.suffix or '(拡張子なし)'}"
        )


def _validate_distance_tolerance(value: float | None) -> float | None:
    if value is None:
        return None
    if not math.isfinite(value) or value < 0.0:
        raise ValueError("--distance-toleranceには0以上の有限値を指定してください。")
    return value


def _validate_output_path(output: str, reference: Path, candidate: Path) -> None:
    try:
        common.ensure_output_not_input(output, (reference, candidate))
    except ValueError as error:
        raise ValueError(f"比較レポートの{error}") from None


def _write_report(report_text: str, output: str) -> None:
    if output == "-":
        if report_text:
            sys.stdout.write(report_text)
            if not report_text.endswith("\n"):
                sys.stdout.write("\n")
            sys.stdout.flush()
        return

    common.write_text_via_temporary_file(
        output=output,
        text=report_text,
        encoding="utf-8",
    )


def _exit_for_result(*, equal: bool, exit_zero: bool) -> Never:
    exit_code = EXIT_OK if equal or exit_zero else EXIT_ISSUE_FOUND
    raise SystemExit(exit_code)


def _exit_with_error(message: str, error: Exception) -> Never:
    print(f"{message}: {error}", file=sys.stderr)
    raise SystemExit(EXIT_EXECUTION_ERROR) from None


def _exit_with_invalid_argument(error: Exception) -> Never:
    print(str(error), file=sys.stderr)
    raise SystemExit(EXIT_INVALID_ARGUMENT) from None


