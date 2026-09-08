# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid
from collections.abc import Callable
from enum import Enum
from uuid import UUID

from ...data_model.common import StBridgeElement, _FieldKind
from ..name_converter import private_field_name


class UuidGenerateType(Enum):
    AUTO = "auto"
    UUID4 = "uuid4"
    UUID7 = "uuid7"


_uuid7: Callable[[], UUID] | None = getattr(uuid, "uuid7", None)


def generate_uuid(generate_type: UuidGenerateType = UuidGenerateType.AUTO) -> UUID:
    match generate_type:
        case UuidGenerateType.AUTO:
            if callable(_uuid7):
                return _uuid7()
            return uuid.uuid4()
        case UuidGenerateType.UUID7:
            if callable(_uuid7):
                return _uuid7()
            raise RuntimeError("UUID7の利用はPython 3.14以降である必要があります")
        case UuidGenerateType.UUID4:
            return uuid.uuid4()


def assign_guid_all(stb_element: StBridgeElement) -> None:
    """子要素も含めたすべての要素にguidを割り当てる。"""
    for field_key, field_info in stb_element._fields.items():
        p_name: str = private_field_name(field_key)
        if field_info.py_type == UUID or field_info.py_type == "UUID":
            current_guid = getattr(stb_element, p_name)
            if current_guid is None:
                setattr(stb_element, p_name, uuid.uuid4())
        elif field_info.kind == _FieldKind.ELEMENT:
            child = getattr(stb_element, p_name)
            if isinstance(child, list):
                for c in child:
                    if isinstance(c, StBridgeElement):
                        assign_guid_all(c)
            elif isinstance(child, StBridgeElement):
                assign_guid_all(child)


def is_guid_assigned_all(stb_element: StBridgeElement) -> bool:
    """全要素にguidが割り当てられているかを確認する。"""
    for field_key, field_info in stb_element._fields.items():
        p_name: str = private_field_name(field_key)
        if field_info.py_type == UUID or field_info.py_type == "UUID":
            current_guid = getattr(stb_element, p_name)
            if current_guid is None:
                return False
        elif field_info.kind == _FieldKind.ELEMENT:
            child = getattr(stb_element, p_name)
            if isinstance(child, list):
                for c in child:
                    if isinstance(c, StBridgeElement) and not is_guid_assigned_all(c):
                        return False
            elif isinstance(child, StBridgeElement) and not is_guid_assigned_all(child):
                return False
    return True
