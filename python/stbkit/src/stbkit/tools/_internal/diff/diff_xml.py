# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from enum import StrEnum
from typing import Any

from stbkit.core.data_model._internal.filter_option import FilterOption, NameFilter
from stbkit.core.stb_io._internal.stream_reader import check_no_doctype

from .common import CompareOption, CompareResult, DiffItem


@dataclass(kw_only=True)
class XmlCompareOption(CompareOption):
    """
    XML比較オプション

    Attribute:
        ignore_order_children(bool): 同一タグの子要素の順序を無視するか
        compare_tag_order(bool): 異なるタグを含む子要素のタグの並び順を
          差分として検出するか
        ignore_empty_attributes(bool): 値が空の属性を無視するか
        ignore_empty_elements(bool): 属性も子要素も内容もない要素を無視するか
        numeric_equivalent_attributes(bool): 数値として等価な属性値を同一とみなすか
         (例: True の場合、"1" と "1.0" を同一とみなす。
           Falseの場合は文字列として異なるため、差分となる)
        filter_option(FilterOption): 比較対象の要素や属性を絞り込むための
          フィルターオプション
    """

    ignore_order_children: bool = True
    compare_tag_order: bool = False
    ignore_empty_attributes: bool = False
    ignore_empty_elements: bool = False
    ignore_name_space: bool = True
    numeric_equivalent_attributes: bool = True
    filter_option: FilterOption = field(default_factory=FilterOption)


@dataclass(frozen=True, kw_only=True)
class XmlCompareResult(CompareResult):
    def to_reason(self) -> str:
        if self.equal:
            return "XMLは等価です"
        return "\n".join(
            f"{diff.path}: {diff.display_message}\n  "
            f"{_Side.LEFT.print()}: {diff.left}\n  {_Side.RIGHT.print()}: {diff.right}"
            for diff in self.diffs
        )

    def combine_attribute_diffs(self) -> XmlCompareResult:
        """同じ要素の複数属性の差分を、1件へ集約する"""

        combined_diffs: list[DiffItem] = _combine_attribute_diffs(self.diffs)
        return XmlCompareResult(equal=self.equal, diffs=combined_diffs)


class _Side(StrEnum):
    LEFT = "left"
    RIGHT = "right"

    def print(self) -> str:
        match self:
            case _Side.LEFT:
                return "左"
            case _Side.RIGHT:
                return "右"


def _try_parse_decimal(value: str) -> Decimal | None:
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError):
        return None


def _delete_namespace(tag: str) -> str:
    return tag.split("}")[-1] if "}" in tag else tag


def _name_for_compare(
    name: str,
    option: XmlCompareOption,
) -> str:
    if option.ignore_name_space:
        return _delete_namespace(name)
    return name


def _normalize_content(text: str | None) -> str:
    if text is None:
        return ""
    return " ".join(text.strip().split())


def _apply_filter(name: str, name_filter: NameFilter | None) -> bool:
    if name_filter is None:
        return True

    # exclude 優先
    if name in name_filter.exclude:
        return False

    if name_filter.include:
        return name in name_filter.include

    return True


def _is_empty_element(
    element: ET.Element,
    compare_option: XmlCompareOption,
) -> bool:
    if _normalize_content(element.text) != "":
        return False

    for value in element.attrib.values():
        if not compare_option.ignore_empty_attributes or value.strip() != "":
            return False

    return all(_is_empty_element(child, compare_option) for child in element)


def _is_child_target(
    parent_tag: str,
    child: ET.Element,
    compare_option: XmlCompareOption,
) -> bool:
    filter_option: FilterOption = compare_option.filter_option

    child_tag_name: str = (
        _delete_namespace(child.tag) if compare_option.ignore_name_space else child.tag
    )

    if not _apply_filter(
        child_tag_name,
        filter_option.global_element_filter,
    ):
        return False

    parent_tag_name: str = (
        _delete_namespace(parent_tag)
        if compare_option.ignore_name_space
        else parent_tag
    )
    child_filter: NameFilter | None = filter_option.element_child_filters.get(
        parent_tag_name
    )

    if not _apply_filter(child_tag_name, child_filter):
        return False

    return not (
        compare_option.ignore_empty_elements
        and _is_empty_element(child, compare_option)
    )


def _filtered_children(
    element: ET.Element,
    compare_option: XmlCompareOption,
) -> list[ET.Element]:
    return [
        child
        for child in element
        if _is_child_target(element.tag, child, compare_option)
    ]


def _filtered_attributes(
    element: ET.Element,
    compare_option: XmlCompareOption,
) -> dict[str, list[str]]:
    filter_option: FilterOption = compare_option.filter_option
    tag_name: str = _name_for_compare(element.tag, compare_option)

    per_element_filter: NameFilter | None = filter_option.element_attribute_filters.get(
        tag_name
    )

    result: dict[str, list[str]] = defaultdict(list)

    for raw_name, value in element.attrib.items():
        attr_name: str = _name_for_compare(raw_name, compare_option)

        if compare_option.ignore_empty_attributes and value == "":
            continue

        if not _apply_filter(
            attr_name,
            filter_option.global_attribute_filter,
        ):
            continue

        if not _apply_filter(attr_name, per_element_filter):
            continue

        result[attr_name].append(value)

    return dict(result)


def _matching_key(
    element: ET.Element,
    compare_option: XmlCompareOption,
) -> tuple[str, str] | None:
    """
    順序無視時に比較対象を探すキー。

    比較対象の属性からguid、idの順に選ぶ。
    """
    global_attribute_filter: NameFilter | None = (
        compare_option.filter_option.global_attribute_filter
    )

    for key_name in ("guid", "id"):
        if not _apply_filter(key_name, global_attribute_filter):
            continue

        values: list[str] = [
            value.strip()
            for attr_name, value in element.attrib.items()
            if _name_for_compare(attr_name, compare_option) == key_name
            and value.strip() != ""
        ]

        # 同じキーが複数ある場合は曖昧なので使わない
        if len(values) == 1:
            return key_name, values[0]

    return None


def _group_by_tag(
    children: list[ET.Element],
    compare_option: XmlCompareOption,
) -> dict[str, list[ET.Element]]:
    grouped: dict[str, list[ET.Element]] = defaultdict(list)

    for child in children:
        tag: str = _name_for_compare(child.tag, compare_option)
        grouped[tag].append(child)

    return dict(grouped)


def _attribute_values_equal(
    left_value: str,
    right_value: str,
    compare_option: XmlCompareOption,
) -> bool:
    if left_value == right_value:
        return True

    if not compare_option.numeric_equivalent_attributes:
        return False

    left_number: Decimal | None = _try_parse_decimal(left_value)
    right_number: Decimal | None = _try_parse_decimal(right_value)

    if left_number is not None and right_number is not None:
        return left_number == right_number

    return False


def _attribute_value_groups_equal(
    left_values: list[str],
    right_values: list[str],
    compare_option: XmlCompareOption,
) -> bool:
    if len(left_values) != len(right_values):
        return False

    unmatched: list[str] = list(right_values)

    for left_value in left_values:
        for index, right_value in enumerate(unmatched):
            if _attribute_values_equal(
                left_value,
                right_value,
                compare_option,
            ):
                unmatched.pop(index)
                break
        else:
            return False

    return True


def _build_xpath(
    root_element: ET.Element,
    compare_option: XmlCompareOption,
) -> dict[ET.Element, str]:
    paths: dict[ET.Element, str] = {
        root_element: f"/{_name_for_compare(root_element.tag, compare_option)}"
    }

    def _step(parent: ET.Element) -> None:
        counts: dict[str, int] = defaultdict(int)
        parent_path = paths[parent]

        for child in parent:
            tag_name = _name_for_compare(child.tag, compare_option)
            counts[tag_name] += 1
            paths[child] = f"{parent_path}/{tag_name}[{counts[tag_name]}]"
            _step(child)

    _step(root_element)
    return paths


@dataclass(frozen=True, kw_only=True)
class _CompareContext:
    option: XmlCompareOption
    left_paths: dict[ET.Element, str]
    right_paths: dict[ET.Element, str]


def _clean_linebreaks(element: ET.Element) -> str:
    xml: str = ET.tostring(element, encoding="unicode")
    return re.sub(r">\s+<", "><", xml).strip()


def _compare_attributes(
    left: ET.Element,
    right: ET.Element,
    path: str,
    compare_option: XmlCompareOption,
    diffs: list[DiffItem],
    *,
    match_reason: str | None,
) -> None:
    left_attrs: dict[str, list[str]] = _filtered_attributes(left, compare_option)
    right_attrs: dict[str, list[str]] = _filtered_attributes(right, compare_option)

    for attr_name in sorted(set(left_attrs) | set(right_attrs)):
        if attr_name not in left_attrs:
            diffs.append(
                DiffItem(
                    path=path,
                    message=(f"属性[{attr_name}]が{_Side.LEFT.print()}に存在しません"),
                    left=None,
                    right=right_attrs[attr_name],
                    attribute_name=attr_name,
                    match_reason=match_reason,
                )
            )
        elif attr_name not in right_attrs:
            diffs.append(
                DiffItem(
                    path=path,
                    message=(f"属性[{attr_name}]が{_Side.RIGHT.print()}に存在しません"),
                    left=left_attrs[attr_name],
                    right=None,
                    attribute_name=attr_name,
                    match_reason=match_reason,
                )
            )
        elif not _attribute_value_groups_equal(
            left_attrs[attr_name], right_attrs[attr_name], compare_option
        ):
            diffs.append(
                DiffItem(
                    path=path,
                    message=f"属性[{attr_name}]の値が異なります",
                    left=left_attrs[attr_name],
                    right=right_attrs[attr_name],
                    attribute_name=attr_name,
                    match_reason=match_reason,
                )
            )


def _compare_content(
    left: ET.Element,
    right: ET.Element,
    path: str,
    diffs: list[DiffItem],
    *,
    match_reason: str | None,
) -> None:
    left_text: str = _normalize_content(left.text)
    right_text: str = _normalize_content(right.text)

    if left_text != right_text:
        diffs.append(
            DiffItem(
                path=path,
                message="内容が異なります",
                left=left_text,
                right=right_text,
                match_reason=match_reason,
            )
        )


def _append_missing_elements(
    *,
    missing_side: _Side,
    elements: list[ET.Element],
    context: _CompareContext,
    diffs: list[DiffItem],
    match_reason: str | None,
) -> None:
    for elem in elements:
        if missing_side == _Side.LEFT:
            path: str = context.right_paths[elem]
            left: str | None = None
            right: str | None = _clean_linebreaks(elem)
        else:
            path = context.left_paths[elem]
            left = _clean_linebreaks(elem)
            right = None

        diffs.append(
            DiffItem(
                path=path,
                message=f"{missing_side.print()}に対応要素が存在しません",
                left=left,
                right=right,
                match_reason=match_reason,
            )
        )


def _append_tag_order_diff(
    left: ET.Element,
    left_children: list[ET.Element],
    right_children: list[ET.Element],
    context: _CompareContext,
    diffs: list[DiffItem],
    *,
    match_reason: str | None,
) -> None:
    option: XmlCompareOption = context.option
    left_tags: list[str] = [
        _name_for_compare(child.tag, option) for child in left_children
    ]
    right_tags: list[str] = [
        _name_for_compare(child.tag, option) for child in right_children
    ]

    # 要素の追加・削除は別の差分で示すため、タグ数が同じ場合だけ差分とする。
    if left_tags == right_tags or sorted(left_tags) != sorted(right_tags):
        return

    diffs.append(
        DiffItem(
            path=context.left_paths[left],
            message="子要素のタグの並び順が異なります",
            left=", ".join(left_tags),
            right=", ".join(right_tags),
            match_reason=match_reason,
        )
    )


def _compare_same_tag_ordered(
    left_list: list[ET.Element],
    right_list: list[ET.Element],
    context: _CompareContext,
    diffs: list[DiffItem],
    *,
    match_reason: str | None,
) -> None:
    common_count: int = min(len(left_list), len(right_list))

    for index in range(common_count):
        _compare_element(
            left_list[index],
            right_list[index],
            context,
            diffs,
            match_reason=match_reason,
        )

    _append_missing_elements(
        missing_side=_Side.RIGHT,
        elements=left_list[common_count:],
        context=context,
        diffs=diffs,
        match_reason=match_reason,
    )
    _append_missing_elements(
        missing_side=_Side.LEFT,
        elements=right_list[common_count:],
        context=context,
        diffs=diffs,
        match_reason=match_reason,
    )


def _group_same_tag_by_match_key(
    children: list[ET.Element],
    compare_option: XmlCompareOption,
) -> tuple[dict[tuple[str, str], list[ET.Element]], list[ET.Element]]:
    keyed: dict[tuple[str, str], list[ET.Element]] = defaultdict(list)
    unkeyed: list[ET.Element] = []

    for child in children:
        key: tuple[str, str] | None = _matching_key(child, compare_option)
        if key is None:
            unkeyed.append(child)
        else:
            keyed[key].append(child)

    return dict(keyed), unkeyed


def _match_reason_for_pair(
    *,
    key_name: str,
    left: ET.Element,
    right: ET.Element,
    context: _CompareContext,
    inherited_reason: str | None,
) -> str | None:
    if context.left_paths[left] == context.right_paths[right]:
        return inherited_reason
    return f"{key_name}一致で対応付け"


def _compare_same_tag_unordered(
    left_list: list[ET.Element],
    right_list: list[ET.Element],
    context: _CompareContext,
    diffs: list[DiffItem],
    *,
    match_reason: str | None,
) -> None:
    option: XmlCompareOption = context.option
    left_keyed, left_unkeyed = _group_same_tag_by_match_key(left_list, option)
    right_keyed, right_unkeyed = _group_same_tag_by_match_key(right_list, option)

    # guid,idを持つ要素はキーで対応付ける
    for key_name, key_value in sorted(set(left_keyed) | set(right_keyed)):
        left_group: list[ET.Element[str]] = left_keyed.get((key_name, key_value), [])
        right_group: list[ET.Element[str]] = right_keyed.get((key_name, key_value), [])
        common_count: int = min(len(left_group), len(right_group))

        for index in range(common_count):
            left_elem: ET.Element[str] = left_group[index]
            right_elem: ET.Element[str] = right_group[index]
            pair_reason: str | None = _match_reason_for_pair(
                key_name=key_name,
                left=left_elem,
                right=right_elem,
                context=context,
                inherited_reason=match_reason,
            )
            _compare_element(
                left_elem,
                right_elem,
                context,
                diffs,
                match_reason=pair_reason,
            )

        _append_missing_elements(
            missing_side=_Side.RIGHT,
            elements=left_group[common_count:],
            context=context,
            diffs=diffs,
            match_reason=match_reason,
        )
        _append_missing_elements(
            missing_side=_Side.LEFT,
            elements=right_group[common_count:],
            context=context,
            diffs=diffs,
            match_reason=match_reason,
        )

    # キーを持たない要素は、出現順で比較する。
    _compare_same_tag_ordered(
        left_unkeyed,
        right_unkeyed,
        context,
        diffs,
        match_reason=match_reason,
    )


def _compare_children(
    left: ET.Element,
    right: ET.Element,
    context: _CompareContext,
    diffs: list[DiffItem],
    *,
    match_reason: str | None,
) -> None:
    compare_option: XmlCompareOption = context.option
    left_children: list[ET.Element[str]] = _filtered_children(left, compare_option)
    right_children: list[ET.Element[str]] = _filtered_children(right, compare_option)

    if compare_option.compare_tag_order:
        _append_tag_order_diff(
            left,
            left_children,
            right_children,
            context,
            diffs,
            match_reason=match_reason,
        )

    left_grouped: dict[str, list[ET.Element[str]]] = _group_by_tag(
        left_children, compare_option
    )
    right_grouped: dict[str, list[ET.Element[str]]] = _group_by_tag(
        right_children, compare_option
    )

    for tag in sorted(set(left_grouped) | set(right_grouped)):
        left_list: list[ET.Element[str]] = left_grouped.get(tag, [])
        right_list: list[ET.Element[str]] = right_grouped.get(tag, [])

        if compare_option.ignore_order_children:
            _compare_same_tag_unordered(
                left_list,
                right_list,
                context,
                diffs,
                match_reason=match_reason,
            )
        else:
            _compare_same_tag_ordered(
                left_list,
                right_list,
                context,
                diffs,
                match_reason=match_reason,
            )


def _compare_element(
    left: ET.Element,
    right: ET.Element,
    context: _CompareContext,
    diffs: list[DiffItem],
    *,
    match_reason: str | None = None,
) -> None:
    compare_option: XmlCompareOption = context.option
    path: str = context.left_paths[left]
    left_tag: str = _name_for_compare(left.tag, compare_option)
    right_tag: str = _name_for_compare(right.tag, compare_option)

    if left_tag != right_tag:
        diffs.append(
            DiffItem(
                path=path,
                message="タグ名が異なります",
                left=left_tag,
                right=right_tag,
                match_reason=match_reason,
            )
        )

    _compare_attributes(
        left,
        right,
        path,
        compare_option,
        diffs,
        match_reason=match_reason,
    )
    _compare_content(
        left,
        right,
        path,
        diffs,
        match_reason=match_reason,
    )
    _compare_children(
        left,
        right,
        context,
        diffs,
        match_reason=match_reason,
    )


def _format_attribute_value(value: Any) -> str:
    if value is None:
        return "(なし)"
    if isinstance(value, list):
        values: list[str] = [" ".join(str(item).split()) for item in value]
        if len(values) == 1:
            return values[0]
        return f"[{', '.join(values)}]"
    return " ".join(str(value).split())


def _format_combined_attribute_values(
    diffs: list[DiffItem],
    *,
    use_left: bool,
) -> str:
    values: list[str] = []

    for diff in diffs:
        if diff.attribute_name is None:
            continue
        value = diff.left if use_left else diff.right
        values.append(f"{diff.attribute_name}={_format_attribute_value(value)}")

    return ", ".join(values)


def _make_combined_attribute_diff(diffs: list[DiffItem]) -> DiffItem:
    first: DiffItem = diffs[0]
    attribute_names: list[str] = [
        f"'{diff.attribute_name}'" for diff in diffs if diff.attribute_name is not None
    ]
    return DiffItem(
        path=first.path,
        message=f"属性に差異があります: {', '.join(attribute_names)}",
        left=_format_combined_attribute_values(diffs, use_left=True),
        right=_format_combined_attribute_values(diffs, use_left=False),
        match_reason=first.match_reason,
    )


def _combine_attribute_diffs(diffs: list[DiffItem]) -> list[DiffItem]:
    """比較済みの差分から、同じ要素の複数属性の結果を集約する"""

    group_map: dict[tuple[str, str | None], list[DiffItem]] = defaultdict(list)
    for diff in diffs:
        if diff.attribute_name is not None:
            group_map[(diff.path, diff.match_reason)].append(diff)

    combined_keys: set[tuple[str, str | None]] = {
        key for key, group in group_map.items() if len(group) >= 2
    }
    emitted_keys: set[tuple[str, str | None]] = set()
    result: list[DiffItem] = []

    for diff in diffs:
        if diff.attribute_name is None:
            result.append(diff)
            continue

        key: tuple[str, str | None] = (diff.path, diff.match_reason)
        if key not in combined_keys:
            result.append(diff)
            continue
        if key in emitted_keys:
            continue

        result.append(_make_combined_attribute_diff(group_map[key]))
        emitted_keys.add(key)

    return result


def compare_xml_str(
    left_xml: str,
    right_xml: str,
    compare_option: XmlCompareOption | None = None,
) -> XmlCompareResult:
    """2つのXML文字列を比較します。

    Raises:
        UnsafeXmlError: いずれかにDOCTYPE宣言が含まれる場合。
        xml.etree.ElementTree.ParseError: XMLとして解析できない場合。
    """
    compare_option = compare_option or XmlCompareOption()

    # 危険なXMLのチェック
    check_no_doctype(left_xml)
    check_no_doctype(right_xml)

    left_root: ET.Element = ET.fromstring(left_xml)
    right_root: ET.Element = ET.fromstring(right_xml)
    context: _CompareContext = _CompareContext(
        option=compare_option,
        left_paths=_build_xpath(left_root, compare_option),
        right_paths=_build_xpath(right_root, compare_option),
    )

    diffs: list[DiffItem] = []
    _compare_element(left_root, right_root, context, diffs)
    return XmlCompareResult(equal=(len(diffs) == 0), diffs=diffs)
