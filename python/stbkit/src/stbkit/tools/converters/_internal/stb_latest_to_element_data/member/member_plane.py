# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

from typing import TYPE_CHECKING

from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api import stb_latest

from ....._internal.data_model.element_data import ElementPlane, ElementType
from ....._internal.vectors import Vector3d
from ... import coord_converter
from ..section import sec

if TYPE_CHECKING:
    from stbkit.api.experimental.repository import RepositoryLatest


def stb_wall_to_element_plane(
    stb_wall: stb_latest.StbWall,
    node_coords: dict[int, Vector3d],
    repo: RepositoryLatest,
    stb_id_to_planes: dict[
        tuple[stb_latest.StbOpenArrangementKindMember, int], ElementPlane
    ],
    reporter: Reporter,
) -> ElementPlane:
    points: list[Vector3d] = []
    node_ids: list[int] = list(stb_wall.stb_node_id_order.content)
    node_points: list[Vector3d] = [node_coords[id] for id in node_ids]
    for id in node_ids:
        point: Vector3d = node_coords[id]
        if stb_wall.stb_wall_offset_list_or_none is not None:
            for stb_offset in stb_wall.stb_wall_offset_list.stb_wall_offset:
                if stb_offset.id_node == id:
                    offset: Vector3d = Vector3d(
                        stb_offset.offset_x,
                        stb_offset.offset_y,
                        stb_offset.offset_z,
                    )
                    point += offset
                    break
        points.append(point)
    thickness: float = sec.get_wall_t(repo, stb_wall, reporter)
    (_vx, _vy, vz) = coord_converter.axis_vector_plate(points)
    points = [point - thickness / 2.0 * vz for point in points]
    name: str = str(stb_wall.id)

    if stb_wall.name:
        name += f"_{stb_wall.name}"
    plate: ElementPlane = ElementPlane(
        element_type=ElementType.WALL,
        name=name,
        guid=stb_wall.guid_or_none,
        points=points,
        thickness=thickness,
        path=stb_wall._path_xml(),
        node_ids=node_ids,
        node_points=node_points,
    )
    stb_id_to_planes[(stb_latest.StbOpenArrangementKindMember.WALL, stb_wall.id)] = (
        plate
    )
    return plate


def stb_slab_to_element_plane(
    stb_slab: stb_latest.StbSlab,
    node_coords: dict[int, Vector3d],
    repo: RepositoryLatest,
    stb_id_to_planes: dict[
        tuple[stb_latest.StbOpenArrangementKindMember, int], ElementPlane
    ],
    reporter: Reporter,
) -> ElementPlane | None:
    """ST-BridgeのスラブをElementPlaneに変換する

    Returns:
        ElementPlane | None: 変換されたElementPlane。変換に失敗した場合はNone。
    """
    try:
        points: list[Vector3d] = []
        node_ids: list[int] = list(stb_slab.stb_node_id_order.content)
        node_points: list[Vector3d] = [node_coords[id] for id in node_ids]
        for id in node_ids:
            point: Vector3d = node_coords[id]
            if stb_slab.stb_slab_offset_list_or_none:
                for stb_offset in stb_slab.stb_slab_offset_list.stb_slab_offset:
                    if stb_offset.id_node == id:
                        offset: Vector3d = Vector3d(
                            stb_offset.offset_x,
                            stb_offset.offset_y,
                            stb_offset.offset_z,
                        )
                        point += offset
                        break
            points.append(point)
        thickness: float = sec.get_slab_depth(repo, stb_slab, reporter)
        (_vx, _vy, vz) = coord_converter.axis_vector_plate(points)
        points = [point - thickness * vz for point in points]
        name: str = str(stb_slab.id)

        if stb_slab.name:
            name += f"_{stb_slab.name}"
        plate: ElementPlane = ElementPlane(
            element_type=ElementType.SLAB,
            name=name,
            guid=stb_slab.guid_or_none,
            points=points,
            thickness=thickness,
            path=stb_slab._path_xml(),
            node_ids=node_ids,
            node_points=node_points,
        )
        stb_id_to_planes[
            (stb_latest.StbOpenArrangementKindMember.SLAB, stb_slab.id)
        ] = plate
        return plate
    except ValueError as e:
        # 部材座標軸の変換時にpointsの数が3未満の場合や、
        # 始点の両側の節点が始点と同一の位置にある場合、
        # ValueErrorが発生するためここで処理する
        reporter.error(
            f"StbSlabのジオメトリ変換に失敗しました: {e}",
            code=Code.UNKNOWN,
            phase=Phase.CONVERT_GEOMETRY,
            stb_element=stb_slab,
        )
        return None
