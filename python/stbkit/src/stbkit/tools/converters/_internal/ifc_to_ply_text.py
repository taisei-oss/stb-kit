# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import TYPE_CHECKING

from ..._internal.data_model.building_geometry import BuildingGeometry
from ..._internal.optional_dependencies.ifc_to_building_geometry import (
    ifc_to_building_geometry,
)
from .building_geometry_to_ply_text import building_geometry_to_ply_text

if TYPE_CHECKING:
    import ifcopenshell.file


def ifc_to_ply_text(ifc_file: "ifcopenshell.file") -> str:
    geom: BuildingGeometry = ifc_to_building_geometry(ifc_file)
    return building_geometry_to_ply_text(geom)
