# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Mapping
from types import ModuleType
from typing import Any, Protocol

from stbkit.core._internal.name_converter import (
    xml_element_name_to_key,
    xml_element_name_to_python_class_name,
)
from stbkit.core.data_model.common import (
    StBridgeElement,
    StBridgeRoot,
    _StBridgeExtensionElement,
)
from stbkit.core.stb_reporting import Code, Phase, Reporter


class ElementHook(Protocol):
    """変換が終わった後に呼ばれる後処理"""

    def __call__(
        self, before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
    ) -> None: ...


def _clone_extension_element(element: StBridgeElement) -> _StBridgeExtensionElement:
    clone = _StBridgeExtensionElement(element._xml_name())
    _copy_extension(element, clone)
    return clone


def _copy_extension(source: StBridgeElement, new_element: StBridgeElement) -> None:
    extension = source._extension
    if extension is None:
        return
    if extension._attributes:
        for name, value in extension._attributes.items():
            new_element._ensure_extension._set_attribute(name, value)
    if extension._children:
        for child in extension._children:
            new_element._ensure_extension._set_child(_clone_extension_element(child))


def _resolve_renamed_child_attr_name(
    element: StBridgeElement,
    attr_name: str,
    class_name_table: dict[str, str],
) -> str | None:
    if not element._is_child(attr_name):
        return None
    source_child_xml_name: str = element._xml_name(attr_name)
    target_child_xml_name: str | None = class_name_table.get(source_child_xml_name)
    if target_child_xml_name is None:
        return None

    source_child_key: str = xml_element_name_to_key(source_child_xml_name)
    if attr_name == source_child_key:
        return xml_element_name_to_key(target_child_xml_name)
    return None


def convert_element(
    element: StBridgeElement,
    module_to: ModuleType,
    *,
    ignore_field: dict[str, list[str]] | None = None,
    class_name_table: dict[str, str] | None = None,
    attr_name_table: dict[str, dict[str, str]] | None = None,
    hooks: Mapping[str, ElementHook] | None = None,
    post: ElementHook | None = None,
    reporter: Reporter,
) -> StBridgeElement | None:
    """要素を変換後バージョンのモジュールの同等クラスへ複製する。

    変換後のバージョンに対応するクラスが無い場合はNoneを返す。
    """
    if ignore_field is None:
        ignore_field = {}
    old_class_name: str = element.__class__.__name__
    old_element_name: str = element._xml_name()
    new_class_name: str = old_class_name
    if class_name_table and old_element_name in class_name_table:
        new_class_name = xml_element_name_to_python_class_name(
            class_name_table[old_element_name]
        )
    NewClass: type[StBridgeElement] | None = getattr(module_to, new_class_name, None)
    if NewClass is None:
        reporter.warning(
            message=(
                f"変換後のバージョンにクラス[{new_class_name}]がないためスキップします"
            ),
            code=Code.NOT_IMPLEMENTED,
            phase=Phase.UPGRADE,
            stb_element=element,
        )
        return None
    new_element: StBridgeElement = NewClass()
    for key in element._fields:
        attr_name: str = key
        if attr_name.startswith("_"):
            continue
        new_attr_name: str = attr_name
        if attr_name in ignore_field.get(old_element_name, []):
            continue
        if (
            attr_name_table
            and old_element_name in attr_name_table
            and attr_name in attr_name_table[old_element_name]
        ):
            new_attr_name = attr_name_table[old_element_name][attr_name]
        elif class_name_table:
            auto_renamed_attr_name = _resolve_renamed_child_attr_name(
                element,
                attr_name,
                class_name_table,
            )
            if auto_renamed_attr_name is not None:
                new_attr_name = auto_renamed_attr_name
        value: Any = getattr(element, f"_{attr_name}")
        if not hasattr(new_element, f"_{new_attr_name}"):
            if value is not None:
                reporter.warning(
                    message=(f"変換後のバージョンに属性[{new_attr_name}]がありません"),
                    code=Code.NOT_IMPLEMENTED,
                    phase=Phase.UPGRADE,
                    stb_element=element,
                    attr_name=attr_name,
                )
                continue
            else:
                continue
        elif element._is_child(attr_name) and new_element._is_child(new_attr_name):
            source_is_children: bool = element._is_children(attr_name)
            target_is_children: bool = new_element._is_children(new_attr_name)
            if source_is_children and target_is_children:
                new_items: list[StBridgeElement] = []
                for item in getattr(element, attr_name):
                    new_item: StBridgeElement | None = convert_element(
                        item,
                        module_to,
                        ignore_field=ignore_field,
                        class_name_table=class_name_table,
                        attr_name_table=attr_name_table,
                        hooks=hooks,
                        reporter=reporter,
                    )
                    if new_item is not None:
                        new_items.append(new_item)
                setattr(new_element, new_attr_name, new_items)
            elif not source_is_children and not target_is_children:
                if value:
                    new_child: StBridgeElement | None = convert_element(
                        value,
                        module_to,
                        ignore_field=ignore_field,
                        class_name_table=class_name_table,
                        attr_name_table=attr_name_table,
                        hooks=hooks,
                        reporter=reporter,
                    )
                    if new_child is not None:
                        setattr(new_element, new_attr_name, new_child)
            elif not source_is_children and target_is_children:
                if value:
                    new_child = convert_element(
                        value,
                        module_to,
                        ignore_field=ignore_field,
                        class_name_table=class_name_table,
                        attr_name_table=attr_name_table,
                        hooks=hooks,
                        reporter=reporter,
                    )
                    if new_child is not None:
                        setattr(new_element, new_attr_name, [new_child])
            else:
                reporter.warning(
                    message=("子要素の最大回数が異なります"),
                    code=Code.SCHEMA_VERSION_MISMATCH,
                    phase=Phase.UPGRADE,
                    stb_element=element,
                    attr_name=attr_name,
                )
        else:
            if value is not None:
                new_element._set_attribute_by_any(new_attr_name, value)
    _copy_extension(element, new_element)
    if hooks is not None:
        hook: ElementHook | None = hooks.get(old_element_name)
        if hook is not None:
            hook(element, new_element, reporter=reporter)
    if post is not None:
        post(
            element,
            new_element,
            reporter=reporter,
        )
    if isinstance(new_element, StBridgeRoot):
        new_element._set_version(reporter=reporter, phase=Phase.UPGRADE)
    return new_element
