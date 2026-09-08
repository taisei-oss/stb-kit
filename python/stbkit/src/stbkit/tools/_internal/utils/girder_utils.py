# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from typing import Protocol

from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_exceptions import SchemaError

from ..vectors import Vector3d
from .node_utils import get_node_coordinate


class GirderLike(Protocol):
    @property
    def id_node_start(self) -> int: ...
    @property
    def id_node_start_or_none(self) -> int | None: ...
    @property
    def id_node_end(self) -> int: ...
    @property
    def id_node_end_or_none(self) -> int | None: ...
    @property
    def offset_start_x_or_none(self) -> float | None: ...
    @property
    def offset_start_y_or_none(self) -> float | None: ...
    @property
    def offset_start_z_or_none(self) -> float | None: ...
    @property
    def offset_end_x_or_none(self) -> float | None: ...
    @property
    def offset_end_y_or_none(self) -> float | None: ...
    @property
    def offset_end_z_or_none(self) -> float | None: ...
    def _name_for_log(self) -> str: ...


def girder_offset_start(girder: GirderLike) -> Vector3d:
    return Vector3d(
        girder.offset_start_x_or_none or 0.0,
        girder.offset_start_y_or_none or 0.0,
        girder.offset_start_z_or_none or 0.0,
    )


def girder_offset_end(girder: GirderLike) -> Vector3d:
    return Vector3d(
        girder.offset_end_x_or_none or 0.0,
        girder.offset_end_y_or_none or 0.0,
        girder.offset_end_z_or_none or 0.0,
    )


@dataclass(slots=True)
class GirderLengthValue:
    length: float
    length_with_offset: float
    pos_control_point_start: float
    pos_control_point_end: float


def girder_length(
    stb_girder: GirderLike,
    stb: StBridgeRoot,
) -> GirderLengthValue:
    if (
        stb_girder.id_node_start_or_none is None
        or stb_girder.id_node_end_or_none is None
    ):
        raise SchemaError(f"{stb_girder._name_for_log()} 節点idがNoneです")
    coord_start: Vector3d = get_node_coordinate(stb, stb_girder.id_node_start)
    coord_end: Vector3d = get_node_coordinate(stb, stb_girder.id_node_end)
    offset_start: Vector3d = girder_offset_start(stb_girder)
    offset_end: Vector3d = girder_offset_end(stb_girder)
    vx: Vector3d = (coord_end - coord_start).normalize()
    length: float = coord_start.distance_to(coord_end)
    length_with_offset: float = (coord_start + offset_start).distance_to(
        coord_end + offset_end
    )
    pos_control_point_start: float = vx.dot(offset_start)
    pos_control_point_end: float = length - vx.dot(offset_end)

    return GirderLengthValue(
        length=length,
        length_with_offset=length_with_offset,
        pos_control_point_start=pos_control_point_start,
        pos_control_point_end=pos_control_point_end,
    )
