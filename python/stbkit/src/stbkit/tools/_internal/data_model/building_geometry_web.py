# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_io import loads
from stbkit.core.stb_reporting import Reporter, get_reporter

from stbkit.api import upgrade_to_latest
from stbkit.api.stb_latest import StBridge
from stbkit.tools.converters._internal.stb_to_building_geometry import (
    stb_to_building_geometry,
)

from .building_geometry import BuildingGeometry, OptionalUuidColumn


def _uuid_strings(column: OptionalUuidColumn) -> list[str | None]:
    def _get_string(index: int) -> str | None:
        value = column.get(index)
        return None if value is None else str(value)

    return [_get_string(index) for index in range(len(column))]


def building_geometry_to_web_payload(
    geometry: BuildingGeometry,
) -> dict[str, object]:
    geometry.freeze()

    return {
        "origin_xyz": list(geometry.origin_xyz),
        "mesh": {
            "positions": list(geometry.mesh.positions),
            "face_vertex_indices": list(geometry.mesh.face_vertex_indices),
            "face_offsets": list(geometry.mesh.face_offsets),
        },
        "elements": {
            "kind": list(geometry.elements.kind),
            "flags": list(geometry.elements.flags),
            "vertex_start": list(geometry.elements.vertex_start),
            "vertex_count": list(geometry.elements.vertex_count),
            "face_start": list(geometry.elements.face_start),
            "face_count": list(geometry.elements.face_count),
            "line_shape_index": list(geometry.elements.line_shape_index),
            "plane_shape_index": list(geometry.elements.plane_shape_index),
            "node_start": list(geometry.elements.node_start),
            "node_count": list(geometry.elements.node_count),
            "story_start": list(geometry.elements.story_start),
            "story_count": list(geometry.elements.story_count),
            "guid": _uuid_strings(geometry.elements.guid),
            "xpath": list(geometry.elements.xpath),
            "name": list(geometry.elements.name),
            "source_type": list(geometry.elements.source_type),
            "source_id": list(geometry.elements.source_id),
        },
        "line_shapes": {
            "start_end_xyz": list(geometry.line_shapes.start_end_xyz),
            "reference_y_xyz": list(geometry.line_shapes.reference_y_xyz),
            "reference_y_valid": list(geometry.line_shapes.reference_y_valid),
        },
        "plane_shapes": {
            "points_xyz": list(geometry.plane_shapes.points_xyz),
            "loop_point_offsets": list(geometry.plane_shapes.loop_point_offsets),
            "plane_loop_offsets": list(geometry.plane_shapes.plane_loop_offsets),
            "loop_types": list(geometry.plane_shapes.loop_types),
        },
        "nodes": {
            "positions_xyz": list(geometry.nodes.positions_xyz),
            "source_id": list(geometry.nodes.source_id),
            "guid": _uuid_strings(geometry.nodes.guid),
            "story_index": list(geometry.nodes.story_index),
            "xpath": list(geometry.nodes.xpath),
        },
        "stories": {
            "source_id": list(geometry.stories.source_id),
            "name": list(geometry.stories.name),
            "elevations": list(geometry.stories.elevations),
        },
        "axes": {
            "points_xyz": list(geometry.axes.points_xyz),
            "point_start": list(geometry.axes.point_start),
            "point_count": list(geometry.axes.point_count),
            "source_id": list(geometry.axes.source_id),
            "name": list(geometry.axes.name),
        },
        "element_node_indices": list(geometry.element_node_indices),
        "element_story_indices": list(geometry.element_story_indices),
    }


def stb_xml_to_web_payload(
    xml: str,
    *,
    reporter: Reporter | None = None,
) -> dict[str, object]:
    actual_reporter: Reporter = reporter or get_reporter()
    root: StBridgeRoot = loads(xml, reporter=actual_reporter)
    stb: StBridge = upgrade_to_latest(root, reporter=actual_reporter)
    geometry: BuildingGeometry = stb_to_building_geometry(
        stb,
        reporter=actual_reporter,
    )
    return building_geometry_to_web_payload(geometry)
