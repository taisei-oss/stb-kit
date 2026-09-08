# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import StbFooting, StbSecFoundationRc

from ....._internal.data_model.element_data import ElementLine, ElementType
from ....._internal.data_model.shape_data import ShapePosition
from ....._internal.vectors import Vector3d
from ..section.sec_foundation import stb_sec_foundation_rc_to_shapes_and_depth


def stb_footing_to_line_element(
    repo: RepositoryLatest,
    stb_footing: StbFooting,
    node_coords: dict[int, Vector3d],
    reporter: Reporter,
) -> ElementLine:
    point: Vector3d = node_coords[stb_footing.id_node]
    offset: Vector3d = Vector3d(
        stb_footing.offset_x if stb_footing.offset_x_or_none else 0.0,
        stb_footing.offset_y if stb_footing.offset_y_or_none else 0.0,
        stb_footing.level_bottom if stb_footing.level_bottom_or_none else 0.0,
    )
    angle: float = stb_footing.rotate if stb_footing.rotate_or_none else 0.0
    point_bottom: Vector3d = point + offset
    stb_sec_foundation_rc: StbSecFoundationRc = repo.deref(stb_footing).id_section
    shapes, lengths = stb_sec_foundation_rc_to_shapes_and_depth(
        stb_sec_foundation_rc, reporter
    )
    point_top: Vector3d = point_bottom + sum(lengths) * Vector3d.unit_z()
    return ElementLine(
        element_type=ElementType.FOOTING,
        name=stb_footing.name_or_none,
        guid=stb_footing.guid_or_none,
        lengths=lengths,
        point_start=point_bottom,
        point_end=point_top,
        angle=angle,
        shapes=shapes,
        axis_position=ShapePosition.DIAGRAM_CORE,
        path=stb_footing._path_xml(),
        node_ids=[stb_footing.id_node],
    )
