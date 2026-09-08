# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

from collections.abc import Callable, Sequence
from enum import Enum
from typing import TYPE_CHECKING, Any
from uuid import UUID

from ..._internal.name_converter import private_field_name
from ...stb_exceptions import SchemaError, TypeMismatchError
from ...stb_typing import (
    Angle,
    Length,
    Monolist,
    MonolistId,
    MonolistLength,
    NonNegativeInteger,
    NonNegativeLength,
    PositiveInteger,
    PositiveIntegerList,
    Ratio,
)
from .stb_types import DataType

if TYPE_CHECKING:
    from ..common import StBridgeElement, _FieldInfo


def validate_angle(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, Angle):
        raise TypeMismatchError(
            expected_type=Angle,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if not (0 <= value < 360):
        raise SchemaError(
            f"angleが0以上360未満でない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def validate_bool(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, bool):
        raise TypeMismatchError(
            expected_type=bool,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def validate_enum(value: Any, element: StBridgeElement, attr_name: str) -> None:
    fi = element._field_info(attr_name)
    if not isinstance(fi.py_type, type):
        raise TypeError(f"{element.__class__}.{attr_name}のpy_typeが指定されていません")
    enum_type: type = fi.py_type
    enum_base_type: type
    if issubclass(enum_type, str):
        enum_base_type = str
    elif issubclass(enum_type, int):
        enum_base_type = int

    if isinstance(value, enum_type):
        return
    if isinstance(value, enum_base_type):
        if not fi.choices:
            raise RuntimeError(
                f"{element.__class__}.{attr_name}のchoicesが指定されていません"
            )
        if str(value) not in fi.choices:
            raise SchemaError(
                f"許容される値ではありません。値:{value} 候補:{fi.choices}",
                element=element,
                attr_name=attr_name,
            )
        else:
            return
    raise TypeMismatchError(
        expected_type=enum_base_type,
        actual_type=type(value),
        element=element,
        attr_name=attr_name,
    )


def validate_float(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, float):
        raise TypeMismatchError(
            expected_type=float,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def validate_int(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, int):
        raise TypeMismatchError(
            expected_type=int,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def validate_length(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, Length):
        raise TypeMismatchError(
            expected_type=Length,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if value <= 0:
        raise SchemaError(
            f"lengthが0以下です: {value}", element=element, attr_name=attr_name
        )


def validate_monolist(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, Sequence) or not all(
        isinstance(item, int) for item in value
    ):
        raise TypeMismatchError(
            expected_type=Monolist,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def validate_monolist_id(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, Sequence) or not all(
        isinstance(item, int) for item in value
    ):
        raise TypeMismatchError(
            expected_type=MonolistId,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if not all(item > 0 for item in value):
        raise SchemaError(
            f"monolist_idに0以下の値が含まれています: {value}",
            element=element,
            attr_name=attr_name,
        )


def validate_monolist_length(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, Sequence) or not all(
        isinstance(item, float) for item in value
    ):
        raise TypeMismatchError(
            expected_type=MonolistLength,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def validate_non_negative_integer(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, int):
        raise TypeMismatchError(
            expected_type=NonNegativeInteger,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if value < 0:
        raise SchemaError(
            f"non_negative_integerが負の値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def validate_non_negative_length(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, float):
        raise TypeMismatchError(
            expected_type=NonNegativeLength,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if value < 0:
        raise SchemaError(
            f"non_negative_lengthが負の値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def validate_positive_integer(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, int):
        raise TypeMismatchError(
            expected_type=PositiveInteger,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if value <= 0:
        raise SchemaError(
            f"positive_integerが0以下の値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def validate_positive_integer_list(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, Sequence) or not all(
        isinstance(item, int) for item in value
    ):
        raise TypeMismatchError(
            expected_type=PositiveIntegerList,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if not all(item > 0 for item in value):
        raise SchemaError(
            f"positive_integer_listに0以下の値が含まれています: {value}",
            element=element,
            attr_name=attr_name,
        )


def validate_ratio(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, float):
        raise TypeMismatchError(
            expected_type=Ratio,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )
    if not (0 < value < 1):
        raise SchemaError(
            f"ratioが0以上1以下でない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def validate_str(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, str):
        raise TypeMismatchError(
            expected_type=str,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def validate_uuid(
    value: Any, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> None:
    if not isinstance(value, UUID):
        raise TypeMismatchError(
            expected_type=UUID,
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def str_to_angle(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> Angle:
    try:
        result: Angle = float(value)
        validate_angle(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"angleに変換できない値です: {value}", element=element, attr_name=attr_name
        )


def str_to_bool(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> bool:
    match value.lower():
        case "true":
            return True
        case "false":
            return False
        case _:
            raise SchemaError(
                f"boolに変換できない値です: {value}",
                element=element,
                attr_name=attr_name,
            )


def str_to_enum(
    value: str, *, element: StBridgeElement | None, attr_name: str | None
) -> Enum:
    if element is None or attr_name is None:
        raise RuntimeError()
    fi = element._field_info(attr_name)
    enum_type = fi.py_type
    if isinstance(enum_type, str):
        raise TypeError()
    if not issubclass(enum_type, Enum):
        raise TypeError()
    try:
        return enum_type(value)
    except (TypeError, ValueError):
        raise SchemaError(
            f"{enum_type}に変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_float(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        raise SchemaError(
            f"floatに変換できない値です: {value}", element=element, attr_name=attr_name
        )


def str_to_int(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        raise SchemaError(
            f"intに変換できない値です: {value}", element=element, attr_name=attr_name
        )


def str_to_length(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> Length:
    try:
        result: Length = float(value)
        validate_length(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"lengthに変換できない値です: {value}", element=element, attr_name=attr_name
        )


def str_to_monolist(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> Monolist:
    try:
        items = value.split(" ")
        result: Monolist = [int(item.strip()) for item in items]
        validate_monolist(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"monolistに変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_monolist_id(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> MonolistId:
    try:
        items = value.split(" ")
        result: MonolistId = [int(item.strip()) for item in items]
        validate_monolist_id(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"monolist_idに変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_monolist_length(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> MonolistLength:
    try:
        items = value.split(" ")
        result: MonolistLength = [float(item.strip()) for item in items]
        validate_monolist_length(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"monolist_lengthに変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_non_negative_integer(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> NonNegativeInteger:
    try:
        result: NonNegativeInteger = int(value)
        validate_non_negative_integer(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"non_negative_integerに変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_non_negative_length(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> NonNegativeLength:
    try:
        result: NonNegativeLength = float(value)
        validate_non_negative_length(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"non_negative_lengthに変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_positive_integer(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> PositiveInteger:
    try:
        result: PositiveInteger = int(value)
        validate_positive_integer(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"positive_integerに変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_positive_integer_list(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> PositiveIntegerList:
    try:
        items = value.split(" ")
        result: PositiveIntegerList = [int(item.strip()) for item in items]
        validate_positive_integer_list(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"positive_integer_listに変換できない値です: {value}",
            element=element,
            attr_name=attr_name,
        )


def str_to_ratio(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> Ratio:
    try:
        result: Ratio = float(value)
        validate_ratio(result, element=element, attr_name=attr_name)
        return result
    except (TypeError, ValueError):
        raise SchemaError(
            f"ratioに変換できない値です: {value}", element=element, attr_name=attr_name
        )


def str_to_str(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> str:
    if not isinstance(value, str):
        raise SchemaError(
            f"strに変換できない値です: {value}", element=element, attr_name=attr_name
        )
    return value


def str_to_uuid(
    value: str, *, element: StBridgeElement | None = None, attr_name: str | None = None
) -> UUID:
    try:
        result: UUID = UUID(value)
        validate_uuid(result, element=element, attr_name=attr_name)
        return result
    except (ValueError, AttributeError):
        raise SchemaError(
            f"UUIDに変換できない値です: {value}", element=element, attr_name=attr_name
        )


def str_to_typed_value(
    value: str,
    data_type: DataType,
    *,
    element: StBridgeElement | None = None,
    attr_name: str | None = None,
) -> Any:
    match data_type:
        case DataType.ANGLE:
            return str_to_angle(value, element=element, attr_name=attr_name)
        case DataType.BOOL:
            return str_to_bool(value, element=element, attr_name=attr_name)
        case DataType.FLOAT:
            return str_to_float(value, element=element, attr_name=attr_name)
        case DataType.INT:
            return str_to_int(value, element=element, attr_name=attr_name)
        case DataType.LENGTH:
            return str_to_length(value, element=element, attr_name=attr_name)
        case DataType.MONOLIST:
            return str_to_monolist(value, element=element, attr_name=attr_name)
        case DataType.MONOLIST_LENGTH:
            return str_to_monolist_length(value, element=element, attr_name=attr_name)
        case DataType.MONOLIST_ID:
            return str_to_monolist_id(value, element=element, attr_name=attr_name)
        case DataType.NON_NEGATIVE_INTEGER:
            return str_to_non_negative_integer(
                value, element=element, attr_name=attr_name
            )
        case DataType.NON_NEGATIVE_LENGTH:
            return str_to_non_negative_length(
                value, element=element, attr_name=attr_name
            )
        case DataType.POSITIVE_INTEGER:
            return str_to_positive_integer(value, element=element, attr_name=attr_name)
        case DataType.POSITIVE_INTEGER_LIST:
            return str_to_positive_integer_list(
                value, element=element, attr_name=attr_name
            )
        case DataType.RATIO:
            return str_to_ratio(value, element=element, attr_name=attr_name)
        case DataType.STR:
            return str_to_str(value, element=element, attr_name=attr_name)
        case DataType.UUID:
            return str_to_uuid(value, element=element, attr_name=attr_name)
        case DataType.INT_ENUM | DataType.STR_ENUM:
            return str_to_enum(value, element=element, attr_name=attr_name)
        case _:
            raise NotImplementedError(f"未対応のDataTypeです: {data_type}")


def any_to_typed_value(
    value: Any,
    data_type: DataType,
    *,
    element: StBridgeElement | None = None,
    attr_name: str | None = None,
) -> Any:
    if data_type == DataType.MONOLIST:
        validate_monolist(value, element=element, attr_name=attr_name)
        return value
    elif data_type == DataType.MONOLIST_LENGTH:
        validate_monolist_length(value, element=element, attr_name=attr_name)
        return value
    elif data_type == DataType.MONOLIST_ID:
        validate_monolist_id(value, element=element, attr_name=attr_name)
        return value
    elif data_type == DataType.POSITIVE_INTEGER_LIST:
        validate_positive_integer_list(value, element=element, attr_name=attr_name)
        return value
    elif data_type in (DataType.INT_ENUM, DataType.STR_ENUM):
        if element is None or attr_name is None:
            raise RuntimeError("enum変換にはelementとattr_nameが必要です")
        fi: _FieldInfo = element._field_info(attr_name)
        enum_type = fi.py_type
        if not isinstance(enum_type, type) or not issubclass(enum_type, Enum):
            raise TypeError(
                f"{element.__class__.__name__}.{attr_name}のenum型情報が不正です"
            )
        validate_enum(value, element=element, attr_name=attr_name)
        if isinstance(value, enum_type):
            return value
        return enum_type(value)
    elif isinstance(value, data_type.to_type()):
        return value
    elif isinstance(value, str):
        return str_to_typed_value(
            value, data_type, element=element, attr_name=attr_name
        )
    else:
        raise TypeMismatchError(
            expected_type=data_type.to_type(),
            actual_type=type(value),
            element=element,
            attr_name=attr_name,
        )


def make_attribute_setter(
    key: str, data_type: DataType, has_choice: bool
) -> Callable[[StBridgeElement, Any], None]:
    p_name: str = private_field_name(key)

    def setter_angle(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_angle(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_bool(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_bool(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_enum(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_enum(value, element=self, attr_name=key)
            if isinstance(value, Enum):
                setattr(self, p_name, value)
            fi = self._field_info(key)
            if not isinstance(fi.py_type, type):
                raise RuntimeError()
            enum_type: type = fi.py_type
            value = enum_type(value)
        setattr(self, p_name, value)

    def setter_float(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_float(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_int(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_int(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_length(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_length(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_monolist(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_monolist(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_monolist_id(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_monolist_id(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_monolist_length(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_monolist_length(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_non_negative_integer(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_non_negative_integer(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_non_negative_length(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_non_negative_length(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_positive_integer(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_positive_integer(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_positive_integer_list(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_positive_integer_list(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_ratio(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_ratio(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_str(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_str(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    def setter_uuid(self: StBridgeElement, value: Any) -> None:
        if value is not None:
            validate_uuid(value, element=self, attr_name=key)
        setattr(self, p_name, value)

    if has_choice:
        return setter_enum
    match data_type:
        case DataType.ANGLE:
            return setter_angle
        case DataType.BOOL:
            return setter_bool
        case DataType.FLOAT:
            return setter_float
        case DataType.INT:
            return setter_int
        case DataType.LENGTH:
            return setter_length
        case DataType.MONOLIST:
            return setter_monolist
        case DataType.MONOLIST_LENGTH:
            return setter_monolist_length
        case DataType.MONOLIST_ID:
            return setter_monolist_id
        case DataType.NON_NEGATIVE_INTEGER:
            return setter_non_negative_integer
        case DataType.NON_NEGATIVE_LENGTH:
            return setter_non_negative_length
        case DataType.POSITIVE_INTEGER:
            return setter_positive_integer
        case DataType.POSITIVE_INTEGER_LIST:
            return setter_positive_integer_list
        case DataType.RATIO:
            return setter_ratio
        case DataType.STR:
            return setter_str
        case DataType.UUID:
            return setter_uuid
        case _:
            raise NotImplementedError(f"未対応のDataTypeです: {data_type}")
