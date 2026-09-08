# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any

import yaml
from stbkit.core import stb_exceptions
from stbkit.core.data_model._internal.filter_option import FilterOption, NameFilter
from stbkit.tools.converters._internal.pipeline.data import (
    _DataFormat,
    _DataFormatSet,
    _DataKind,
    _get_extension,
    _StbVersion,
)


class FixtureFormat(StrEnum):
    STB_V2_0_1 = "stb_v2_0_1"
    STB_V2_0_2 = "stb_v2_0_2"
    STB_V2_1_0 = "stb_v2_1_0"
    STB_V2_1_1 = "stb_v2_1_1"
    IFC4 = "ifc4"
    PLY = "ply"

    def to_data_format_set(self) -> _DataFormatSet:
        match self:
            case FixtureFormat.STB_V2_0_1:
                return _DataFormatSet(
                    format=_DataFormat.STB,
                    kind=_DataKind.FILE,
                    stb_version=_StbVersion.V2_0_1,
                )
            case FixtureFormat.STB_V2_0_2:
                return _DataFormatSet(
                    format=_DataFormat.STB,
                    kind=_DataKind.FILE,
                    stb_version=_StbVersion.V2_0_2,
                )
            case FixtureFormat.STB_V2_1_0:
                return _DataFormatSet(
                    format=_DataFormat.STB,
                    kind=_DataKind.FILE,
                    stb_version=_StbVersion.V2_1_0,
                )
            case FixtureFormat.STB_V2_1_1:
                return _DataFormatSet(
                    format=_DataFormat.STB,
                    kind=_DataKind.FILE,
                    stb_version=_StbVersion.V2_1_1,
                )
            case FixtureFormat.IFC4:
                return _DataFormatSet(
                    format=_DataFormat.IFC,
                    kind=_DataKind.FILE,
                )
            case FixtureFormat.PLY:
                return _DataFormatSet(
                    format=_DataFormat.PLY,
                    kind=_DataKind.FILE,
                )
            case _:
                raise ValueError(f"Unsupported fixture format: {self}")


SUPPORTED_CONVERSIONS: set[tuple[FixtureFormat, FixtureFormat]] = {
    (FixtureFormat.STB_V2_0_1, FixtureFormat.STB_V2_1_0),
    (FixtureFormat.STB_V2_0_1, FixtureFormat.STB_V2_1_1),
    (FixtureFormat.STB_V2_0_2, FixtureFormat.STB_V2_1_0),
    (FixtureFormat.STB_V2_0_2, FixtureFormat.STB_V2_1_1),
    (FixtureFormat.STB_V2_1_0, FixtureFormat.STB_V2_1_1),
    (FixtureFormat.STB_V2_1_0, FixtureFormat.IFC4),
    (FixtureFormat.STB_V2_1_0, FixtureFormat.PLY),
    (FixtureFormat.STB_V2_1_1, FixtureFormat.IFC4),
    (FixtureFormat.STB_V2_1_1, FixtureFormat.PLY),
    (FixtureFormat.IFC4, FixtureFormat.PLY),
}


def _is_stb(fmt: FixtureFormat) -> bool:
    return fmt.to_data_format_set().format is _DataFormat.STB


def _next_stem_parts(
    stem_parts: tuple[str, ...],
    *,
    src_format: FixtureFormat,
    dst_format: FixtureFormat,
) -> tuple[str, ...]:
    if _is_stb(src_format) and _is_stb(dst_format):
        return (*stem_parts[:-1], dst_format.value)
    return (*stem_parts, dst_format.value)


def _resolve_error_type(name: str, *, case_id: str) -> type[Exception]:
    error_type: Any = getattr(stb_exceptions, name, None)
    if not isinstance(error_type, type) or not issubclass(error_type, Exception):
        raise ValueError(
            f"case[{case_id}]のexpect-error[{name}]は"
            "stbkit.core.stb_exceptionsの例外クラス名である必要があります"
        )
    return error_type


@dataclass(frozen=True, kw_only=True)
class CompareOptions:
    filter: FilterOption | None = None
    ignore_application_information: bool = False
    ignore_empty_attributes: bool = False
    ignore_empty_elements: bool = False
    sort_elements: bool = False


@dataclass(frozen=True, kw_only=True)
class InputSpec:
    format: FixtureFormat
    path: Path
    compare_options: CompareOptions
    enable_repair: bool = False
    expect_error: type[Exception] | None = None
    schema_check_line_count_diff: int = 0


@dataclass(frozen=True, kw_only=True)
class ConversionNodeSpec:
    case_id: str
    route_formats: tuple[FixtureFormat, ...]
    src_format: FixtureFormat
    dst_format: FixtureFormat
    input_path: Path
    golden_output_path: Path
    golden_log_path: Path
    compare_options: CompareOptions
    enable_repair: bool = False
    input_enable_repair: bool = False
    schema_check_line_count_diff: int = 0


@dataclass(frozen=True, kw_only=True)
class RoundTripSpec:
    case_id: str
    format: FixtureFormat
    source_path: Path
    compare_options: CompareOptions
    enable_repair: bool = False
    expect_error: type[Exception] | None = None
    schema_check_line_count_diff: int = 0

    @property
    def schema_check_path(self) -> Path:
        return self.source_path.parent / f"schema_check.{self.source_path.name}.txt"

    @property
    def schema_check_no_xsd_path(self) -> Path:
        return (
            self.source_path.parent / f"schema_check_no_xsd.{self.source_path.name}.txt"
        )


class FixtureCase:
    def __init__(self, case_dir: Path) -> None:
        self.case_dir: Path = case_dir
        self.meta: dict[str, Any] = self._load_yaml(case_dir / "case.yml")
        self.case_id: str = str(self.meta["id"])

    @staticmethod
    def _load_yaml(path: Path) -> dict[str, Any]:
        with path.open("r", encoding="utf-8") as f:
            data: Any = yaml.safe_load(f)
        if not isinstance(data, dict):
            raise ValueError(f"YAMLのルートが無効です: {path}")
        return data

    def _input_path_for_format(self, fmt: FixtureFormat) -> Path:
        ext: str = _get_extension(fmt.to_data_format_set().format)
        return self.case_dir / f"{self.case_id}.{fmt.value}{ext}"

    def _output_path_for_stem_parts(
        self, stem_parts: tuple[str, ...], dst_format: FixtureFormat
    ) -> Path:
        ext: str = _get_extension(dst_format.to_data_format_set().format)
        return self.case_dir / f"{'.'.join(stem_parts)}{ext}"

    def _log_path_for_output(self, output_path: Path) -> Path:
        return output_path.parent / f"convert_log.{output_path.name}.txt"

    def _parse_compare_options(self, item: dict[str, Any]) -> CompareOptions:
        if "compare-options" in item:
            compare_options_dict: Any = item["compare-options"]
            if "filter" in compare_options_dict:
                filter_dict: Any = compare_options_dict["filter"]
                filter_option = FilterOption(
                    global_element_filter=NameFilter(
                        include=filter_dict.get("include-elements", []),
                        exclude=filter_dict.get("exclude-elements", []),
                    ),
                    element_attribute_filters={
                        elem: NameFilter(
                            include=attr_filter.get("include-attributes", []),
                            exclude=attr_filter.get("exclude-attributes", []),
                        )
                        for elem, attr_filter in filter_dict.get(
                            "element-attribute-filters", {}
                        ).items()
                    },
                    global_attribute_filter=NameFilter(
                        include=filter_dict.get("global-include-attributes", []),
                        exclude=filter_dict.get("global-exclude-attributes", []),
                    )
                    if filter_dict.get("global-include-attributes")
                    or filter_dict.get("global-exclude-attributes")
                    else NameFilter(),
                )
            sort_elements: bool = compare_options_dict.get("sort-elements", False)
            return CompareOptions(
                ignore_application_information=compare_options_dict.get(
                    "ignore-application-information", False
                ),
                ignore_empty_elements=compare_options_dict.get(
                    "ignore-empty-elements", False
                ),
                ignore_empty_attributes=compare_options_dict.get(
                    "ignore-empty-attributes", False
                ),
                filter=filter_option if "filter" in compare_options_dict else None,
                sort_elements=sort_elements,
            )
        else:
            return CompareOptions()

    def _parse_schema_check_line_count_diff_from_item(
        self, item: dict[str, Any], *, item_label: str, default: int
    ) -> int:
        """スキーマ検査のゴールデンで想定する行数差（XSD版-非XSD版）を読む。"""
        schema_check: Any = item.get("schema-check")
        if schema_check is None:
            return default
        if not isinstance(schema_check, dict):
            raise ValueError(
                f"case[{self.case_id}]の{item_label}.schema-checkは"
                " dictである必要があります"
            )

        value: Any = schema_check.get("line-count-diff", default)
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(
                f"case[{self.case_id}]の{item_label}.schema-check.line-count-diffは"
                "intである必要があります"
            )
        return value

    def input_spec(self) -> InputSpec:
        item: Any = self.meta.get("input")
        if not isinstance(item, dict):
            raise ValueError(f"case[{self.case_id}]のinputはdictである必要があります")

        try:
            fmt = FixtureFormat(item["format"])
        except KeyError as e:
            raise ValueError(
                f"case[{self.case_id}]のinput定義に必須項目が不足しています: {e}"
            ) from e

        compare_options: CompareOptions = self._parse_compare_options(item)
        line_count_diff: int = self._parse_schema_check_line_count_diff_from_item(
            item, item_label="input", default=0
        )

        input_path: Path | None = None
        if "filename" in item:
            file_name: Any = item["filename"]
            if not isinstance(file_name, str):
                raise ValueError(
                    f"case[{self.case_id}]のinput.filenameは文字列である必要があります"
                )
            input_path = self.case_dir / file_name
        else:
            input_path = self._input_path_for_format(fmt)
        enable_repair: bool = False
        if "enable-repair" in item:
            if not isinstance(item["enable-repair"], bool):
                raise ValueError(
                    f"case[{self.case_id}]のinput.enable-repairは"
                    "boolである必要があります"
                )
            enable_repair = item["enable-repair"]
        expect_error: type[Exception] | None = None
        if "expect-error" in item:
            if not isinstance(item["expect-error"], str):
                raise ValueError(
                    f"case[{self.case_id}]のinput.expect-errorは文字列である必要があります"
                )
            expect_error = _resolve_error_type(
                item["expect-error"], case_id=self.case_id
            )

        return InputSpec(
            format=fmt,
            path=input_path,
            compare_options=compare_options,
            enable_repair=enable_repair,
            expect_error=expect_error,
            schema_check_line_count_diff=line_count_diff,
        )

    def _parse_tree_node(
        self,
        *,
        parent_format: FixtureFormat,
        parent_input_path: Path,
        parent_route: tuple[FixtureFormat, ...],
        parent_stem_parts: tuple[str, ...],
        node: Any,
        result: list[ConversionNodeSpec],
        input_enable_repair: bool = False,
        inherited_schema_check_line_count_diff: int = 0,
    ) -> None:
        if not isinstance(node, dict):
            raise ValueError(
                f"case[{self.case_id}]のtree nodeはdictである必要があります"
            )

        try:
            dst_format: FixtureFormat = FixtureFormat(node["to"])
        except KeyError as e:
            raise ValueError(
                f"case[{self.case_id}]のtree nodeに必須項目が不足しています: {e}"
            ) from e
        enable_repair: bool = False
        if "enable-repair" in node:
            if not isinstance(node["enable-repair"], bool):
                raise ValueError(
                    f"case[{self.case_id}]のtree nodeのenable-repairは"
                    "boolである必要があります"
                )
            enable_repair = node["enable-repair"]

        edge: tuple[FixtureFormat, FixtureFormat] = (parent_format, dst_format)
        if edge not in SUPPORTED_CONVERSIONS:
            raise ValueError(
                f"case[{self.case_id}]の変換は未対応です: "
                f"{parent_format.value} -> {dst_format.value}"
            )

        route_formats: tuple[FixtureFormat, ...] = (*parent_route, dst_format)
        stem_parts: tuple[str, ...] = _next_stem_parts(
            parent_stem_parts, src_format=parent_format, dst_format=dst_format
        )
        output_path: Path = self._output_path_for_stem_parts(stem_parts, dst_format)
        log_path: Path = self._log_path_for_output(output_path)
        compare_options: CompareOptions = self._parse_compare_options(node)
        line_count_diff: int = self._parse_schema_check_line_count_diff_from_item(
            node,
            item_label="tree node",
            default=inherited_schema_check_line_count_diff,
        )

        spec = ConversionNodeSpec(
            case_id=self.case_id,
            route_formats=route_formats,
            src_format=parent_format,
            dst_format=dst_format,
            input_path=parent_input_path,
            golden_output_path=output_path,
            golden_log_path=log_path,
            compare_options=compare_options,
            enable_repair=enable_repair,
            input_enable_repair=input_enable_repair,
            schema_check_line_count_diff=line_count_diff,
        )
        result.append(spec)

        children = node.get("children", [])
        if children is None:
            children = []
        if not isinstance(children, list):
            raise ValueError(
                f"case[{self.case_id}]のchildrenはlistである必要があります"
            )

        for child in children:
            self._parse_tree_node(
                parent_format=dst_format,
                parent_input_path=output_path,
                parent_route=route_formats,
                parent_stem_parts=stem_parts,
                node=child,
                result=result,
                inherited_schema_check_line_count_diff=line_count_diff,
            )

    def conversion_node_specs(self) -> list[ConversionNodeSpec]:
        input_spec: InputSpec = self.input_spec()
        tree = self.meta.get("tree")
        if tree is None:
            return []

        result: list[ConversionNodeSpec] = []
        self._parse_tree_node(
            parent_format=input_spec.format,
            parent_input_path=input_spec.path,
            parent_route=(input_spec.format,),
            parent_stem_parts=(self.case_id, input_spec.format.value),
            node=tree,
            result=result,
            input_enable_repair=input_spec.enable_repair,
            inherited_schema_check_line_count_diff=0,
        )
        return result

    def iter_roundtrip_specs(
        self,
        *,
        fmt: FixtureFormat,
        include_input: bool = True,
        include_conversion_outputs: bool = True,
    ) -> list[RoundTripSpec]:
        result: list[RoundTripSpec] = []
        input_spec: InputSpec = self.input_spec()

        if include_input and input_spec.format == fmt:
            result.append(
                RoundTripSpec(
                    case_id=self.case_id,
                    format=fmt,
                    source_path=input_spec.path,
                    compare_options=input_spec.compare_options,
                    enable_repair=input_spec.enable_repair,
                    expect_error=input_spec.expect_error,
                    schema_check_line_count_diff=input_spec.schema_check_line_count_diff,
                )
            )

        if include_conversion_outputs:
            for spec in self.conversion_node_specs():
                if spec.dst_format == fmt:
                    result.append(
                        RoundTripSpec(
                            case_id=self.case_id,
                            format=fmt,
                            source_path=spec.golden_output_path,
                            compare_options=spec.compare_options,
                            enable_repair=spec.enable_repair,
                            schema_check_line_count_diff=spec.schema_check_line_count_diff,
                        )
                    )

        return result


class FixtureRepository:
    def __init__(self, fixtures_root: Path) -> None:
        self.fixtures_root: Path = fixtures_root
        self.cases_dir: Path = fixtures_root / "cases"

    def list_case_ids(self) -> list[str]:
        if not self.cases_dir.exists():
            return []
        return sorted(
            p.name
            for p in self.cases_dir.iterdir()
            if p.is_dir() and (p / "case.yml").exists()
        )

    def get_case(self, case_id: str) -> FixtureCase:
        case_dir = self.cases_dir / case_id
        if not case_dir.exists():
            raise FileNotFoundError(f"Case not found: {case_id}")
        return FixtureCase(case_dir)

    def iter_conversion_node_specs(self) -> list[ConversionNodeSpec]:
        result: list[ConversionNodeSpec] = []
        for case_id in self.list_case_ids():
            result.extend(self.get_case(case_id).conversion_node_specs())
        return result

    def iter_roundtrip_specs(
        self,
        *,
        fmt: FixtureFormat,
        include_input: bool = True,
        include_conversion_outputs: bool = True,
    ) -> list[RoundTripSpec]:
        result: list[RoundTripSpec] = []
        for case_id in self.list_case_ids():
            result.extend(
                self.get_case(case_id).iter_roundtrip_specs(
                    fmt=fmt,
                    include_input=include_input,
                    include_conversion_outputs=include_conversion_outputs,
                )
            )
        return result
