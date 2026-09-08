# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from uuid import UUID

from ..optional_dependencies.ifc_common import ensure_ifcopenshell


def to_ifc_guid(guid: UUID) -> str:
    """UUIDをIFCのGlobalId形式に変換する

    TODO:ifcopenshell無しで変換できるようにする"""
    ensure_ifcopenshell()
    import ifcopenshell

    return ifcopenshell.guid.compress(str(guid))


def from_ifc_guid(ifc_guid: str) -> UUID:
    """IFCのGlobalId形式をUUIDに変換する

    TODO:ifcopenshell無しで変換できるようにする"""
    ensure_ifcopenshell()
    import ifcopenshell

    decompressed = ifcopenshell.guid.expand(ifc_guid)
    return UUID(decompressed)
