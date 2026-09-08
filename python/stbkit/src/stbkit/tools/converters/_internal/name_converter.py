# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core._internal.name_converter import private_field_name
from stbkit.core.data_model.common import StBridgeElement


def stb_element_to_ifc_name(stb_element: StBridgeElement) -> str:
    result: list[str] = []
    p_name_id: str = private_field_name("id")
    if hasattr(stb_element, p_name_id):
        id = getattr(stb_element, p_name_id)
        if id:
            result.append(str(id))
    p_name_name: str = private_field_name("name")
    if hasattr(stb_element, p_name_name):
        name = getattr(stb_element, p_name_name)
        if name:
            result.append(str(name))
    return "_".join(result)
