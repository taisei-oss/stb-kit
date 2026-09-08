# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass

from .vectors import Vector3d

type _Matrix4x4Tuple = tuple[
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
]


@dataclass(frozen=True, slots=True)
class RotationMatrix:
    """回転行列
    x_axis,y_axis,z_axisは正規直行基底"""

    origin: Vector3d
    x_axis: Vector3d
    y_axis: Vector3d
    z_axis: Vector3d

    def to_global_point(self, point: Vector3d) -> Vector3d:
        return (
            self.origin
            + point.x * self.x_axis
            + point.y * self.y_axis
            + point.z * self.z_axis
        )

    def to_local_point(self, point: Vector3d) -> Vector3d:
        delta: Vector3d = point - self.origin
        return Vector3d(
            delta.dot(self.x_axis),
            delta.dot(self.y_axis),
            delta.dot(self.z_axis),
        )

    def to_matrix_tuple(self) -> _Matrix4x4Tuple:
        return (
            (self.x_axis.x, self.y_axis.x, self.z_axis.x, self.origin.x),
            (self.x_axis.y, self.y_axis.y, self.z_axis.y, self.origin.y),
            (self.x_axis.z, self.y_axis.z, self.z_axis.z, self.origin.z),
            (0.0, 0.0, 0.0, 1.0),
        )
