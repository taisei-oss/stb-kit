# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid
from enum import Enum, IntEnum, StrEnum

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


class DataType(Enum):
    ANGLE = "Angle"
    BOOL = "bool"
    FLOAT = "float"
    INT = "int"
    INT_ENUM = "IntEnum"
    LENGTH = "Length"
    MONOLIST = "Monolist"
    MONOLIST_LENGTH = "MonolistLength"
    MONOLIST_ID = "MonolistId"
    NON_NEGATIVE_INTEGER = "NonNegativeInteger"
    NON_NEGATIVE_LENGTH = "NonNegativeLength"
    POSITIVE_INTEGER = "PositiveInteger"
    POSITIVE_INTEGER_LIST = "PositiveIntegerList"
    RATIO = "Ratio"
    STR = "str"
    STR_ENUM = "StrEnum"
    UUID = "UUID"

    def to_type(
        self,
    ) -> type[
        Angle
        | bool
        | float
        | int
        | IntEnum
        | Length
        | Monolist
        | MonolistLength
        | MonolistId
        | NonNegativeInteger
        | NonNegativeLength
        | PositiveInteger
        | PositiveIntegerList
        | Ratio
        | str
        | StrEnum
        | uuid.UUID
    ]:
        match self:
            case DataType.ANGLE:
                return Angle
            case DataType.BOOL:
                return bool
            case DataType.FLOAT:
                return float
            case DataType.INT:
                return int
            case DataType.INT_ENUM:
                return IntEnum
            case DataType.LENGTH:
                return Length
            case DataType.MONOLIST:
                return Monolist
            case DataType.MONOLIST_LENGTH:
                return MonolistLength
            case DataType.MONOLIST_ID:
                return MonolistId
            case DataType.NON_NEGATIVE_INTEGER:
                return NonNegativeInteger
            case DataType.NON_NEGATIVE_LENGTH:
                return NonNegativeLength
            case DataType.POSITIVE_INTEGER:
                return PositiveInteger
            case DataType.POSITIVE_INTEGER_LIST:
                return PositiveIntegerList
            case DataType.RATIO:
                return Ratio
            case DataType.STR:
                return str
            case DataType.STR_ENUM:
                return StrEnum
            case DataType.UUID:
                return uuid.UUID
