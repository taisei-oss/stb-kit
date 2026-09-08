# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""変換テーブルに書かれた名前が正しいかのテスト"""

from dataclasses import dataclass
from functools import cache
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest
from stbkit.core._internal.name_converter import xml_element_name_to_python_class_name
from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0, stb_v2_1_1
from stbkit.core.data_model.common import StBridgeElement

from stbkit.api import (
    upgrade_to_latest,  # noqa: F401  循環インポートを避けるため先に読み込む
)
from stbkit.tools.upgrade import _internal as upgrade_package
from stbkit.tools.upgrade._internal.v2_0_2_to_v2_1_0 import (
    hooks as hooks_v2_0_2_to_v2_1_0,
)
from stbkit.tools.upgrade._internal.v2_0_2_to_v2_1_0 import (
    tables as tables_v2_0_2_to_v2_1_0,
)
from stbkit.tools.upgrade._internal.v2_1_0_to_v2_1_1 import (
    tables as tables_v2_1_0_to_v2_1_1,
)


@dataclass(frozen=True, kw_only=True, slots=True)
class Conversion:
    """検証対象の変換"""

    package: str
    module_from: ModuleType
    module_to: ModuleType
    tables: ModuleType
    hooks: ModuleType | None = None

    @property
    def label(self) -> str:
        return self.package.removeprefix("upgrade_")

    @property
    def hook_keys(self) -> list[str]:
        if self.hooks is None:
            return []
        return sorted(getattr(self.hooks, "HOOKS", {}))

    @property
    def ignore_field(self) -> dict[str, list[str]]:
        return getattr(self.tables, "ignore_field", {})

    @property
    def class_name_table(self) -> dict[str, str]:
        return getattr(self.tables, "class_name_table", {})

    @property
    def attr_name_table(self) -> dict[str, dict[str, str]]:
        return getattr(self.tables, "attr_name_table", {})


_CONVERSIONS: list[Conversion] = [
    Conversion(
        package="v2_0_2_to_v2_1_0",
        module_from=stb_v2_0_2,
        module_to=stb_v2_1_0,
        tables=tables_v2_0_2_to_v2_1_0,
        hooks=hooks_v2_0_2_to_v2_1_0,
    ),
    Conversion(
        package="v2_1_0_to_v2_1_1",
        module_from=stb_v2_1_0,
        module_to=stb_v2_1_1,
        tables=tables_v2_1_0_to_v2_1_1,
    ),
]


@cache
def _class_dict_by_xml_name(module: ModuleType) -> dict[str, type[StBridgeElement]]:
    result: dict[str, type[StBridgeElement]] = {}
    for name in dir(module):
        obj: Any = getattr(module, name)
        if (
            isinstance(obj, type)
            and issubclass(obj, StBridgeElement)
            and obj.__module__ == module.__name__
        ):
            result[obj._xml_class_name()] = obj
    return result


def _target_class(
    conversion: Conversion, element_name: str
) -> type[StBridgeElement] | None:
    """convert_elementと同じ規則で、変換後のクラスを求める。

    class_name_tableに載っていなければ、同じPythonクラス名のまま変換される。
    """
    source: type[StBridgeElement] = _class_dict_by_xml_name(conversion.module_from)[
        element_name
    ]
    if element_name in conversion.class_name_table:
        target_name: str = xml_element_name_to_python_class_name(
            conversion.class_name_table[element_name]
        )
    else:
        target_name = source.__name__
    target = getattr(conversion.module_to, target_name, None)
    if isinstance(target, type) and issubclass(target, StBridgeElement):
        return target
    return None


def _conversion_id(value: object) -> str | None:
    if isinstance(value, Conversion):
        return value.label
    return None


def _element_params(table_name: str) -> list[tuple[Conversion, str]]:
    return [
        (conversion, element_name)
        for conversion in _CONVERSIONS
        for element_name in sorted(getattr(conversion, table_name))
    ]


def _field_params(table_name: str) -> list[tuple[Conversion, str, str]]:
    return [
        (conversion, element_name, field_name)
        for conversion in _CONVERSIONS
        for element_name, field_names in sorted(getattr(conversion, table_name).items())
        for field_name in field_names
    ]


def _rename_params(table_name: str) -> list[tuple[Conversion, str, str, str]]:
    return [
        (conversion, element_name, source_name, target_name)
        for conversion in _CONVERSIONS
        for element_name, mapping in sorted(getattr(conversion, table_name).items())
        for source_name, target_name in mapping.items()
    ]


def _pair_params(table_name: str) -> list[tuple[Conversion, str, str]]:
    return [
        (conversion, source_name, target_name)
        for conversion in _CONVERSIONS
        for source_name, target_name in sorted(getattr(conversion, table_name).items())
    ]


def test_every_conversion_package_is_registered() -> None:
    """tablesを持つ変換パッケージは、すべてCONVERSIONSに登録する。"""
    package_dir = Path(str(upgrade_package.__file__)).parent
    found = {
        entry.name
        for entry in package_dir.iterdir()
        if entry.is_dir() and (entry / "tables.py").exists()
    }
    assert found == {conversion.package for conversion in _CONVERSIONS}


def test_conversions_are_not_empty() -> None:
    assert _CONVERSIONS


@pytest.mark.parametrize(
    ("conversion", "element_name"), _element_params("ignore_field"), ids=_conversion_id
)
def test_ignore_field_keys_are_element_names(
    conversion: Conversion, element_name: str
) -> None:
    assert element_name in _class_dict_by_xml_name(conversion.module_from)


@pytest.mark.parametrize(
    ("conversion", "element_name", "field_name"),
    _field_params("ignore_field"),
    ids=_conversion_id,
)
def test_ignore_field_values_are_field_names(
    conversion: Conversion, element_name: str, field_name: str
) -> None:
    source = _class_dict_by_xml_name(conversion.module_from)[element_name]
    assert field_name in source._fields


@pytest.mark.parametrize(
    ("conversion", "element_name"),
    _element_params("class_name_table"),
    ids=_conversion_id,
)
def test_class_name_table_keys_are_element_names(
    conversion: Conversion, element_name: str
) -> None:
    assert element_name in _class_dict_by_xml_name(conversion.module_from)


@pytest.mark.parametrize(
    ("conversion", "element_name", "target_name"),
    _pair_params("class_name_table"),
    ids=_conversion_id,
)
def test_class_name_table_values_are_element_names(
    conversion: Conversion, element_name: str, target_name: str
) -> None:
    assert target_name in _class_dict_by_xml_name(conversion.module_to)


@pytest.mark.parametrize(
    ("conversion", "element_name", "target_name"),
    _pair_params("class_name_table"),
    ids=_conversion_id,
)
def test_class_name_table_has_no_identity_rename(
    conversion: Conversion, element_name: str, target_name: str
) -> None:
    assert element_name != target_name


@pytest.mark.parametrize(
    ("conversion", "element_name"),
    _element_params("attr_name_table"),
    ids=_conversion_id,
)
def test_attr_name_table_keys_are_element_names(
    conversion: Conversion, element_name: str
) -> None:
    assert element_name in _class_dict_by_xml_name(conversion.module_from)


@pytest.mark.parametrize(
    ("conversion", "element_name", "source_name", "target_name"),
    _rename_params("attr_name_table"),
    ids=_conversion_id,
)
def test_attr_name_table_values_are_existing_fields(
    conversion: Conversion, element_name: str, source_name: str, target_name: str
) -> None:
    source = _class_dict_by_xml_name(conversion.module_from)[element_name]
    assert source_name in source._fields
    target = _target_class(conversion, element_name)
    assert target is not None, f"{element_name}に対応するクラスが変換先にありません"
    assert target_name in target._fields


@pytest.mark.parametrize(
    ("conversion", "element_name", "source_name", "target_name"),
    _rename_params("attr_name_table"),
    ids=_conversion_id,
)
def test_attr_name_table_has_no_identity_rename(
    conversion: Conversion, element_name: str, source_name: str, target_name: str
) -> None:
    assert source_name != target_name


@pytest.mark.parametrize(
    ("conversion", "element_name"),
    [
        (conversion, element_name)
        for conversion in _CONVERSIONS
        for element_name in conversion.hook_keys
    ],
    ids=_conversion_id,
)
def test_hook_keys_are_element_names(conversion: Conversion, element_name: str) -> None:
    assert element_name in _class_dict_by_xml_name(conversion.module_from)
