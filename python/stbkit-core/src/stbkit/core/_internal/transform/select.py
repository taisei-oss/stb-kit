# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""要素の抜粋を行う処理。

TODO:モジュール名や関数名を検討中。filterやextract等。
    また、inputを編集するか、コピーしてreturnするか
"""

from ...data_model._internal.filter_option import FilterOption, NameFilter
from ...data_model.common import (
    StBridgeElement,
    StBridgeRoot,
    _FieldKind,
    _StBridgeElementList,
)
from ...stb_reporting import Reporter
from ..name_converter import private_field_name


def select_elements(
    stb: StBridgeRoot,
    option: FilterOption,
    *,
    reporter: Reporter,
) -> None:
    """SelectOptionで指定した要素のみが残るようにStBridgeRootを編集する。"""

    def _traverse(element: StBridgeElement) -> bool:
        """再帰的に要素をたどり、選択オプションに基づいて要素や属性を削除する。
        RETURN: 要素がinclude指定で残る場合True、そうでない場合False"""
        has_include_element: bool = False
        for key, field in element._fields.items():
            child_has_include_element: bool = False
            # 要素の場合
            if field.kind == _FieldKind.ELEMENT:
                value = getattr(element, private_field_name(key), None)
                if not value:
                    continue
                if isinstance(value, list) and len(value) > 0:
                    xml_name: str = value[0]._xml_name()
                    for item in value:
                        if isinstance(item, StBridgeElement):
                            child_has_include_element = (
                                child_has_include_element or _traverse(item)
                            )
                elif isinstance(value, StBridgeElement):
                    xml_name = value._xml_name()
                    child_has_include_element = child_has_include_element or _traverse(
                        value
                    )
                else:
                    continue
                # include指定がある場合はそれ以外は除外
                if child_has_include_element or (
                    option.global_element_filter.include
                    and xml_name in option.global_element_filter.include
                ):
                    has_include_element = True
                elif (
                    option.global_element_filter.include
                    and xml_name not in option.global_element_filter.include
                ):
                    if field.max_occurs == 1:
                        setattr(element, private_field_name(key), None)
                    else:
                        setattr(
                            element,
                            private_field_name(key),
                            _StBridgeElementList(parent=element),
                        )
                    continue
                # exclude指定がある場合は除外
                if xml_name in option.global_element_filter.exclude:
                    if field.max_occurs == 1:
                        setattr(element, private_field_name(key), None)
                    else:
                        setattr(
                            element,
                            private_field_name(key),
                            _StBridgeElementList(parent=element),
                        )
                    continue

            # 属性の場合
            elif field.kind == _FieldKind.ATTRIBUTE:
                xml_name = element._xml_name(key)
                # 属性抽出オプション
                attrs_opt: NameFilter = option.element_attribute_filters.get(
                    element._xml_name(), NameFilter()
                )
                if attrs_opt and xml_name in attrs_opt.exclude:
                    setattr(element, private_field_name(key), None)
                    continue
                if (
                    attrs_opt
                    and attrs_opt.include
                    and xml_name not in attrs_opt.include
                ):
                    setattr(element, private_field_name(key), None)
                    continue
                # グローバル除外
                if (
                    option.global_attribute_filter
                    and xml_name in option.global_attribute_filter.exclude
                ):
                    setattr(element, private_field_name(key), None)
                    continue
        return has_include_element

    _traverse(stb)
