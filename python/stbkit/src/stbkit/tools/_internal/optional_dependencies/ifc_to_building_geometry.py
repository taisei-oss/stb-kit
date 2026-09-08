# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Sequence
from typing import TYPE_CHECKING
from uuid import UUID

from ..data_model.building_geometry import BuildingGeometry
from ..utils.guid_utils import from_ifc_guid
from .ifc_common import ensure_ifcopenshell

if TYPE_CHECKING:
    import ifcopenshell.file


def ifc_to_building_geometry(ifc_file: "ifcopenshell.file") -> BuildingGeometry:
    ensure_ifcopenshell()
    import ifcopenshell
    import ifcopenshell.geom
    import ifcopenshell.util.shape
    from ifcopenshell.ifcopenshell_wrapper import (
        BRep,
        Serialization,
        Triangulation,
    )

    # ジオメトリの設定
    settings = ifcopenshell.geom.settings()  # type: ignore
    settings.set("use-world-coords", True)
    building_geometry: BuildingGeometry = BuildingGeometry()

    for element in ifc_file.by_type("IfcProduct"):
        if element.is_a("IfcOpeningElement"):
            continue
        try:
            shape = ifcopenshell.geom.create_shape(settings, element)
        except RuntimeError:
            continue
        if not hasattr(shape, "geometry"):
            continue
        geometry = shape.geometry
        vertices: list[Sequence[float]] = []

        if isinstance(geometry, (BRep, Triangulation, Serialization)):
            global_id: str | None = (
                element.GlobalId if hasattr(element, "GlobalId") else None
            )
            guid: UUID | None = from_ifc_guid(global_id) if global_id else None
            index: int = building_geometry.add_element(
                guid=guid,
                source_type=str(element.is_a()),
                source_id=str(element.id()),
                name=getattr(element, "Name", None),
            )
            vertices.extend(ifcopenshell.util.shape.get_vertices(geometry))  # type:ignore
            tmp_faces: list[Sequence[int]] = [
                item
                for item in ifcopenshell.util.shape.get_faces(geometry)  # type: ignore
            ]
            building_geometry.add_element_mesh(index, vertices, tmp_faces)
    return building_geometry
