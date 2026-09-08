# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from contextlib import AbstractContextManager, nullcontext
from dataclasses import dataclass
from pathlib import Path
from typing import Final

import pytest
from stbkit.core.stb_io._internal.loader import _detect_encoding
from stbkit.core.stb_reporting import CollectingReporter
from stbkit.core.validation import validate_schema
from stbkit.tools.converters._internal.pipeline.data import (
    _DataFormat,
    _DataFormatSet,
)
from stbkit.tools.converters._internal.pipeline.execution import (
    ConvertResultFormat,
    convert,
)

from .comparators import PlyComparator, TextComparator, XmlComparator
from .fixture_repository import (
    CompareOptions,
    ConversionNodeSpec,
    FixtureFormat,
    RoundTripSpec,
)
from .roundtrip import roundtrip_dict, roundtrip_stb

_STB_FORMATS: Final[tuple[FixtureFormat, ...]] = (
    FixtureFormat.STB_V2_0_2,
    FixtureFormat.STB_V2_1_0,
    FixtureFormat.STB_V2_1_1,
)

_IFC_TIME_OFFSET_FROM: Final[str] = "00:00+09:00"
_IFC_TIME_OFFSET_TO: Final[str] = "00:00+00:00"


@dataclass(frozen=True)
class RunContext:
    create_golden: bool = False
    ifc_round_digits: int | None = None
    ifc_round_digits_mm: int | None = None


def _write_golden(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _normalize_ifc_time_offset(text: str) -> str:
    """IFCのタイムゾーン補正"""
    return text.replace(_IFC_TIME_OFFSET_FROM, _IFC_TIME_OFFSET_TO)


def _get_reporter_log_text(reporter: CollectingReporter) -> str | None:
    if reporter.is_valid():
        return None
    return reporter.report.to_text(
        has_timestamp=False, has_code=True, has_phase=True, has_path=True
    )


def compare_text(actual_text: str, golden_path: Path, fmt: FixtureFormat) -> None:
    expected_text: str = golden_path.read_text(encoding="utf-8")
    message: str = f"出力が期待値と異なります: {golden_path}"
    if fmt in _STB_FORMATS:
        # ST-Bridgeは差分を見やすいようにXmlComparatorを使う。
        xml_comparator: XmlComparator = XmlComparator()
        xml_comparator.assert_equal(
            expected=expected_text,
            actual=actual_text,
            message=message,
        )
    elif fmt == FixtureFormat.IFC4:
        # IFCは単純なテキスト比較とする
        text_comparator: TextComparator = TextComparator()
        text_comparator.assert_equal(
            expected=expected_text,
            actual=actual_text,
            message=message,
        )
    elif fmt == FixtureFormat.PLY:
        # PLY出力は、WindowsとLinuxでメッシュの順序が変わってしまうため、形状比較を行う
        ply_comparator: PlyComparator = PlyComparator()
        ply_comparator.assert_equal(
            expected=expected_text,
            actual=actual_text,
            message=message,
        )
    else:
        raise NotImplementedError(f"比較に未対応の形式です: {fmt}")


def verify_or_create_log_golden(
    *,
    actual_log: str | None,
    golden_log_path: Path,
    context: RunContext,
) -> None:
    """ログのゴールデンをチェックする。--create-golden時は生成か削除を行う"""
    if context.create_golden:
        if actual_log is None:
            golden_log_path.unlink(missing_ok=True)
        else:
            _write_golden(golden_log_path, actual_log)
        return

    if not golden_log_path.exists():
        if actual_log is None:
            return
        raise AssertionError(
            f"Logファイルが存在しませんが、ログが生成されました: {golden_log_path}"
        )

    if actual_log is None:
        raise AssertionError(
            f"Logファイルが存在しますが、ログは生成されませんでした: {golden_log_path}"
        )
    text_comparator: TextComparator = TextComparator()
    text_comparator.assert_equal(
        expected=golden_log_path.read_text(encoding="utf-8"),
        actual=actual_log,
        message=f"ログが期待値と異なります: {golden_log_path}",
    )


def run_conversion_node_spec(
    spec: ConversionNodeSpec,
    *,
    context: RunContext,
) -> None:
    reporter: CollectingReporter = CollectingReporter()
    dst_format: _DataFormatSet = spec.dst_format.to_data_format_set()
    output: str | Path = convert(
        spec.input_path,
        input_format=spec.src_format.to_data_format_set().format,
        output_format=dst_format.format,
        result_format=ConvertResultFormat.TEXT,
        reporter=reporter,
        output_stb_version=dst_format.stb_version,
        input_enable_repair=spec.input_enable_repair,
        output_enable_repair=spec.enable_repair,
        ifc_round_digits=context.ifc_round_digits,
        ifc_round_digits_mm=context.ifc_round_digits_mm,
    )
    assert isinstance(output, str)

    if spec.dst_format == FixtureFormat.IFC4:
        output = _normalize_ifc_time_offset(output)

    if context.create_golden:
        _write_golden(spec.golden_output_path, output)
    else:
        compare_text(output, spec.golden_output_path, spec.dst_format)

    verify_or_create_log_golden(
        actual_log=_get_reporter_log_text(reporter),
        golden_log_path=spec.golden_log_path,
        context=context,
    )


def run_roundtrip_spec(spec: RoundTripSpec) -> None:
    if spec.format not in _STB_FORMATS:
        raise NotImplementedError(f"ラウンドトリップに未対応の形式です: {spec.format}")

    expectation: AbstractContextManager[object] = (
        pytest.raises(spec.expect_error)
        if spec.expect_error is not None
        else nullcontext()
    )
    options: CompareOptions = spec.compare_options
    with expectation:
        roundtrip_stb(
            spec.source_path,
            enable_repair=spec.enable_repair,
            filter_option=options.filter,
            ignore_application_information=options.ignore_application_information,
            ignore_empty_attributes=options.ignore_empty_attributes,
            ignore_empty_element=options.ignore_empty_elements,
            sort_elements=options.sort_elements,
        )


def run_roundtrip_dict_spec(spec: RoundTripSpec) -> None:
    if spec.format not in _STB_FORMATS:
        raise NotImplementedError(f"ラウンドトリップに未対応の形式です: {spec.format}")
    roundtrip_dict(spec.source_path)


def run_schema_check_spec(
    spec: RoundTripSpec, *, context: RunContext, use_xsd: bool
) -> None:
    if spec.format.to_data_format_set().format != _DataFormat.STB:
        raise NotImplementedError("スキーマチェックはST-Bridge形式のみ行います。")

    reporter: CollectingReporter = CollectingReporter()
    xml: str = spec.source_path.read_text(encoding=_detect_encoding(spec.source_path))
    validate_schema(
        xml, reporter=reporter, require_xsd=use_xsd, exclude_legal_extensions=True
    )
    verify_or_create_log_golden(
        actual_log=_get_reporter_log_text(reporter),
        golden_log_path=spec.schema_check_path
        if use_xsd
        else spec.schema_check_no_xsd_path,
        context=context,
    )


def _count_golden_lines(path: Path) -> int:
    if not path.exists():
        return 0
    return len(path.read_text(encoding="utf-8").splitlines())


def run_schema_check_line_count_spec(spec: RoundTripSpec) -> None:
    """XSD有無でゴールデンの行数差が想定通りかを確認する

    Raises:
        AssertionError: 行数差が想定と異なる場合。
    """
    xsd_line_count: int = _count_golden_lines(spec.schema_check_path)
    no_xsd_line_count: int = _count_golden_lines(spec.schema_check_no_xsd_path)
    actual_diff: int = xsd_line_count - no_xsd_line_count
    if actual_diff != spec.schema_check_line_count_diff:
        raise AssertionError(
            "スキーマ検査のゴールデンの行数差が想定と異なります: "
            f"{spec.schema_check_path.name}={xsd_line_count}行, "
            f"{spec.schema_check_no_xsd_path.name}={no_xsd_line_count}行, "
            f"差={actual_diff} (想定 {spec.schema_check_line_count_diff})"
        )
