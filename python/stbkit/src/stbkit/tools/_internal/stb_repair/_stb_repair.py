# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Any, get_args

from stbkit.core._internal.name_converter import private_field_name
from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0, stb_v2_1_1
from stbkit.core.data_model._internal.stb_types import DataType
from stbkit.core.data_model.common import (
    StBridgeElement,
    StBridgeRoot,
    _FieldInfo,
    _FieldKind,
)
from stbkit.core.stb_reporting import Code, Phase, Reporter, get_reporter

from ..constants import REPAIR_DEFAULT_LENGTH_MM
from . import _stb_v2_0_2_repair, _stb_v2_1_0_repair, _stb_v2_1_1_repair
from ._common import Defaults, RepairContext


def _repair_required_length(
    element: StBridgeElement, *, context: RepairContext
) -> None:
    for key, field_info in element._fields.items():
        p_name: str = private_field_name(key)
        if field_info.required and field_info.data_type == DataType.LENGTH:
            value = getattr(element, p_name)
            if value is None or value <= 0:
                context.reporter.warning(
                    message=(
                        f"属性[{key}]の値[{value}]は不正な長さであるため、デフォルト値[{context.defaults.default_length}]に修復します"
                    ),
                    code=Code.REPAIR_LOG,
                    phase=Phase.REPAIR,
                    stb_element=element,
                    attr_name=key,
                )
                setattr(element, p_name, context.defaults.default_length)
        elif field_info.required and field_info.data_type == DataType.FLOAT:
            value = getattr(element, p_name)
            if value is None:
                context.reporter.warning(
                    message=(
                        f"属性[{key}]の値がNoneであるため、デフォルト値[{context.defaults.default_float}]に修復します"
                    ),
                    code=Code.REPAIR_LOG,
                    phase=Phase.REPAIR,
                    stb_element=element,
                    attr_name=key,
                )
                setattr(element, p_name, context.defaults.default_float)
        if field_info.kind == _FieldKind.ELEMENT:
            child = getattr(element, p_name)
            if isinstance(child, StBridgeElement):
                _repair_required_length(child, context=context)
            elif isinstance(child, list):
                for c in child:
                    if isinstance(c, StBridgeElement):
                        _repair_required_length(c, context=context)


def _default_value_for_field(
    field_info: _FieldInfo, *, defaults: Defaults
) -> Any | None:
    match field_info.data_type:
        case DataType.FLOAT:
            return defaults.default_float
        case DataType.LENGTH | DataType.NON_NEGATIVE_LENGTH:
            return defaults.default_length
        case DataType.STR:
            return defaults.default_string
        case _:
            return None


def _fill_required_attributes(
    element: StBridgeElement, *, context: RepairContext
) -> None:
    for key, field_info in element._fields.items():
        if field_info.kind not in (_FieldKind.ATTRIBUTE, _FieldKind.CONTENT):
            continue
        if not field_info.required:
            continue
        p_name: str = private_field_name(key)
        if getattr(element, p_name) is not None:
            continue
        default_value = _default_value_for_field(field_info, defaults=context.defaults)
        if default_value is None:
            continue
        context.reporter.warning(
            message=(
                f"属性[{key}]が存在しないため、デフォルト値[{default_value}]に修復します"
            ),
            code=Code.REPAIR_LOG,
            phase=Phase.REPAIR,
            stb_element=element,
            attr_name=key,
        )
        setattr(element, p_name, default_value)


def _instantiate_child(
    field_info: _FieldInfo, *, context: RepairContext
) -> StBridgeElement | None:
    element_cls = field_info.py_type
    if not isinstance(element_cls, type):
        args = get_args(element_cls)
        if not args or not isinstance(args[0], type):
            return None
        element_cls = args[0]
    if not issubclass(element_cls, StBridgeElement):
        return None
    instance: StBridgeElement = element_cls()
    _fill_required_attributes(instance, context=context)
    return instance


def _repair_occurs(element: StBridgeElement, *, context: RepairContext) -> None:
    for key, field_info in element._fields.items():
        if field_info.kind != _FieldKind.ELEMENT:
            continue
        p_name: str = private_field_name(key)
        value = getattr(element, p_name)
        if field_info.max_occurs == 1:
            if value is None and (field_info.min_occurs or 0) >= 1:
                new_child = _instantiate_child(field_info, context=context)
                if new_child is not None:
                    context.reporter.warning(
                        message=f"必須要素[{key}]が存在しないため追加しました",
                        code=Code.REPAIR_LOG,
                        phase=Phase.REPAIR,
                        stb_element=element,
                    )
                    setattr(element, key, new_child)
                    value = new_child
            if isinstance(value, StBridgeElement):
                _repair_occurs(value, context=context)
        elif isinstance(value, list):
            if field_info.max_occurs is not None and len(value) > field_info.max_occurs:
                del value[field_info.max_occurs :]
                context.reporter.warning(
                    message=(
                        f"要素[{key}]が最大回数[{field_info.max_occurs}]を"
                        "超過しているため削除しました"
                    ),
                    code=Code.REPAIR_LOG,
                    phase=Phase.REPAIR,
                    stb_element=element,
                )
            if field_info.min_occurs is not None and len(value) < field_info.min_occurs:
                while len(value) < field_info.min_occurs:
                    new_child = _instantiate_child(field_info, context=context)
                    if new_child is None:
                        break
                    value.append(new_child)
                context.reporter.warning(
                    message=(
                        f"要素[{key}]が最小回数[{field_info.min_occurs}]に"
                        "満たないため追加しました"
                    ),
                    code=Code.REPAIR_LOG,
                    phase=Phase.REPAIR,
                    stb_element=element,
                )
            for item in value:
                if isinstance(item, StBridgeElement):
                    _repair_occurs(item, context=context)


def repair_stb(
    stb: StBridgeRoot,
    *,
    reporter: Reporter | None = None,
    default_steel_strength: str = "SS400",
    default_length: float = REPAIR_DEFAULT_LENGTH_MM,
) -> None:
    if reporter is None:
        reporter = get_reporter()
    defaults: Defaults = Defaults(
        steel_strength=default_steel_strength, default_length=default_length
    )
    context: RepairContext = RepairContext(defaults=defaults, reporter=reporter)
    _repair_occurs(stb, context=context)
    _repair_required_length(stb, context=context)
    match stb:
        case stb_v2_1_1.StBridge():
            _stb_v2_1_1_repair.repair_stb(stb, context=context)
        case stb_v2_1_0.StBridge():
            _stb_v2_1_0_repair.repair_stb(stb, context=context)
        case stb_v2_0_2.StBridge():
            _stb_v2_0_2_repair.repair_stb(stb, context=context)
        case _:
            pass
