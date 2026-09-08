# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import (
    ZeroLengthMemberError,
)

from ..._internal.data_model.element_data import ElementType
from ..._internal.matrix import RotationMatrix
from ..._internal.vectors import Vector3d


def rotation_matrix(
    point: Vector3d, vx: Vector3d, vy: Vector3d, vz: Vector3d
) -> RotationMatrix:
    return RotationMatrix(point, vx, vy, vz)


def rotation_matrix_by_element_type(
    point_start: Vector3d, point_end: Vector3d, angle: float, element_type: ElementType
) -> RotationMatrix:
    match element_type:
        case (
            ElementType.GIRDER
            | ElementType.BEAM
            | ElementType.BRACE
            | ElementType.STRIP_FOOTING
            | ElementType.PARAPET
        ):
            return rotation_matrix_beam(point_start, point_end, angle)
        case (
            ElementType.COLUMN
            | ElementType.POST
            | ElementType.FOOTING
            | ElementType.PILE
            | ElementType.FOUNDATION_COLUMN
        ):
            return rotation_matrix_column(point_start, point_end, angle)
        case _:
            raise NotImplementedError(f"要素タイプ{element_type}の回転行列は未実装です")


def axis_vector_by_element_type(
    point_start: Vector3d, point_end: Vector3d, angle: float, element_type: ElementType
) -> tuple[Vector3d, Vector3d, Vector3d]:
    match element_type:
        case (
            ElementType.GIRDER
            | ElementType.BEAM
            | ElementType.BRACE
            | ElementType.STRIP_FOOTING
            | ElementType.PARAPET
        ):
            return axis_vector_beam(point_start, point_end, angle)
        case (
            ElementType.COLUMN
            | ElementType.POST
            | ElementType.FOOTING
            | ElementType.PILE
            | ElementType.FOUNDATION_COLUMN
        ):
            return axis_vector_column(point_start, point_end, angle)
        case _:
            raise NotImplementedError(
                f"要素タイプ{element_type}の軸ベクトルは未実装です"
            )


def axis_vector_beam(
    point_start: Vector3d, point_end: Vector3d, angle: float
) -> tuple[Vector3d, Vector3d, Vector3d]:
    vx: Vector3d = (point_end - point_start).normalize()
    pv: Vector3d = vx.perpendicular_vector_on_plane(Vector3d.unit_z())
    vz: Vector3d = pv.rotate_around_axis(angle, vx).normalize()
    vy: Vector3d = vz.cross(vx)
    return (vx, vy, vz)


def rotation_matrix_beam(
    point_start: Vector3d,
    point_end: Vector3d,
    angle: float,
) -> RotationMatrix:
    (vx, vy, vz) = axis_vector_beam(point_start, point_end, angle)
    return rotation_matrix(point_start, vy, vz, vx)


def axis_vector_column(
    point_start: Vector3d, point_end: Vector3d, angle: float
) -> tuple[Vector3d, Vector3d, Vector3d]:
    vx: Vector3d = point_end - point_start
    if vx.length() == 0:
        raise ZeroLengthMemberError("柱の始点と終点が同じ位置です")
    vx = vx.normalize()
    pv: Vector3d = vx.perpendicular_vector_on_plane(Vector3d.unit_x())
    vy: Vector3d = pv.rotate_around_axis(angle, vx).normalize()
    vz: Vector3d = vx.cross(vy)
    return (vx, vy, vz)


def rotation_matrix_column(
    point_start: Vector3d,
    point_end: Vector3d,
    angle: float,
) -> RotationMatrix:
    (vx, vy, vz) = axis_vector_column(point_start, point_end, angle)
    return rotation_matrix(point_start, vy, vz, vx)


def axis_vector_plate(
    points: list[Vector3d],
) -> tuple[Vector3d, Vector3d, Vector3d]:
    if len(points) < 3:
        raise AssertionError("pointsの数が3以下です")
    vx: Vector3d = (points[1] - points[0]).normalize()
    vy: Vector3d = vx.perpendicular_vector_on_plane(points[-1] - points[0]).normalize()
    vz = vx.cross(vy)
    return (vx, vy, vz)


def rotation_matrix_plate(points: list[Vector3d]) -> RotationMatrix:
    vx, vy, vz = axis_vector_plate(points)
    return rotation_matrix(points[0], vx, vy, vz)


def to_plate_element_coord(points: list[Vector3d]) -> list[Vector3d]:
    matrix = rotation_matrix_plate(points)
    return [matrix.to_local_point(point) for point in points]


def to_global_coord_plate(
    points: list[Vector3d], out_points: list[Vector3d]
) -> list[Vector3d]:
    matrix = rotation_matrix_plate(out_points)
    return [matrix.to_global_point(point) for point in points]


def to_global_coord(
    points: list[Vector3d],
    point_start: Vector3d,
    point_end: Vector3d,
    angle: float,
    element_type: ElementType,
) -> list[Vector3d]:
    matrix = rotation_matrix_by_element_type(
        point_start, point_end, angle, element_type
    )
    return [matrix.to_global_point(point) for point in points]
