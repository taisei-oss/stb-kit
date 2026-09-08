# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from copy import deepcopy
from typing import TypedDict

from stbkit.core.data_model._internal.filter_option import FilterOption, NameFilter
from stbkit.tools._internal.diff.diff_xml import (
    XmlCompareOption,
    XmlCompareResult,
    compare_xml_str,
)

from .text_comparator import CompareResult, TextComparator


class _XmlAssertEqualOptions(TypedDict, total=False):
    ignore_empty_element: bool
    ignore_application_information: bool
    ignore_empty_attributes: bool
    filter_option: FilterOption | None
    sort_elements: bool


def _add_ignore_application_info_to_filter_option(
    filter_option: FilterOption | None, ignore_application_information: bool
) -> FilterOption:
    result: FilterOption = deepcopy(filter_option) if filter_option else FilterOption()
    if ignore_application_information:
        stb_common_filter = result.element_attribute_filters.get(
            "StbCommon", NameFilter()
        )
        if "app_name" not in stb_common_filter.exclude:
            stb_common_filter.exclude.append("app_name")
        if "app_version" not in stb_common_filter.exclude:
            stb_common_filter.exclude.append("app_version")
        if "convert_app_name" not in stb_common_filter.exclude:
            stb_common_filter.exclude.append("convert_app_name")
        if "convert_app_version" not in stb_common_filter.exclude:
            stb_common_filter.exclude.append("convert_app_version")
        result.element_attribute_filters["StbCommon"] = stb_common_filter
    return result


class XmlComparator(TextComparator):
    def __init__(
        self,
        ignore_empty_element: bool = False,
        ignore_application_information: bool = False,
        ignore_empty_attributes: bool = False,
        filter_option: FilterOption | None = None,
        sort_elements: bool = False,
    ):
        self.ignore_empty_element = ignore_empty_element
        self.ignore_application_information = ignore_application_information
        self.ignore_empty_attributes = ignore_empty_attributes
        self.filter_option = filter_option
        self.sort_elements = sort_elements

    def compare(
        self,
        expected: str,
        actual: str,
    ) -> CompareResult:
        filter_option = _add_ignore_application_info_to_filter_option(
            self.filter_option, self.ignore_application_information
        )

        xml_result: XmlCompareResult = compare_xml_str(
            expected,
            actual,
            XmlCompareOption(
                ignore_order_children=self.sort_elements,
                ignore_empty_attributes=self.ignore_empty_attributes,
                ignore_empty_elements=self.ignore_empty_element,
                numeric_equivalent_attributes=True,
                filter_option=filter_option,
            ),
        )
        return CompareResult(
            equal=xml_result.equal,
            diff=xml_result.to_reason() if xml_result.equal is False else None,
        )
