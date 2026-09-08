# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import math
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from math import sqrt
from typing import TYPE_CHECKING, overload

from stbkit.core.stb_exceptions import SchemaError

from .utils.unit_utils import degree_to_radian, mm_to_m

if TYPE_CHECKING:
    from .utils.node_utils import HasXyz


@dataclass(frozen=True, slots=True)
class Vector2d(Sequence[float]):
    x: float = 0.0
    y: float = 0.0

    def mm_to_m(self) -> Vector2d:
        return Vector2d(mm_to_m(self.x), mm_to_m(self.y))

    def to_vector3d(self, z: float = 0.0) -> Vector3d:
        return Vector3d(self.x, self.y, z)

    @overload
    def __getitem__(self, index: int) -> float: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[float]: ...

    def __getitem__(self, index: int | slice) -> float | Sequence[float]:
        if isinstance(index, int):
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            else:
                raise IndexError("インデックスは0から1の範囲で指定してください")
        elif isinstance(index, slice):
            # スライスの場合はリストで返す
            return [self.x, self.y][index]
        else:
            raise TypeError("インデックスは整数またはスライスで指定してください")

    def __len__(self) -> int:
        return 2

    def __add__(self, other: Vector2d) -> Vector2d:
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2d) -> Vector2d:
        return Vector2d(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Vector2d:
        return Vector2d(-self.x, -self.y)

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y

    def clone(self) -> Vector2d:
        return Vector2d(self.x, self.y)

    def distance_to(self, other: Vector2d) -> float:
        return math.hypot(other.y - self.y, other.x - self.x)

    def rotate(self, angle_degree: float) -> Vector2d:
        if angle_degree == 0.0:
            return self.clone()
        theta: float = degree_to_radian(angle_degree)
        cos_theta: float = math.cos(theta)
        sin_theta: float = math.sin(theta)
        x_new: float = cos_theta * self.x - sin_theta * self.y
        y_new: float = sin_theta * self.x + cos_theta * self.y
        return Vector2d(x_new, y_new)

    @staticmethod
    def zero() -> Vector2d:
        return Vector2d(0.0, 0.0)


@dataclass(frozen=True, slots=True)
class Vector3d(Sequence[float]):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __add__(self, other: Vector3d) -> Vector3d:
        return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)

    @overload
    def __getitem__(self, index: int) -> float: ...

    @overload
    def __getitem__(self, index: slice) -> Sequence[float]: ...

    def __getitem__(self, index: int | slice) -> float | Sequence[float]:
        if isinstance(index, int):
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            elif index == 2:
                return self.z
            else:
                raise IndexError("インデックスは0から2の範囲で指定してください")
        elif isinstance(index, slice):
            # スライスの場合はリストで返す
            return [self.x, self.y, self.z][index]
        else:
            raise TypeError("インデックスは整数またはスライスで指定してください")

    def __len__(self) -> int:
        return 3

    def __rmul__(self, other: float) -> Vector3d:
        return Vector3d(other * self.x, other * self.y, other * self.z)

    def __sub__(self, other: Vector3d) -> Vector3d:
        return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self) -> Vector3d:
        return Vector3d(-self.x, -self.y, -self.z)

    def clone(self) -> Vector3d:
        return Vector3d(self.x, self.y, self.z)

    def cross(self, other: Vector3d) -> Vector3d:
        return Vector3d(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def distance_to(self, other: Vector3d) -> float:
        return sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    def dot(self, other: Vector3d) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def mm_to_m(self) -> Vector3d:
        return mm_to_m(1.0) * self

    def normalize(self) -> Vector3d:
        length = self.length()
        if length == 0:
            raise ValueError("零ベクトルは正規化できません")
        return Vector3d(self.x / length, self.y / length, self.z / length)

    def perpendicular_vector_on_plane(self, def_plane_vec: Vector3d) -> Vector3d:
        # vec1 を正規化
        vec1_normalized: Vector3d = self.normalize()

        # vec2 の vec1 への射影を計算
        projection_length: float = def_plane_vec.dot(vec1_normalized)
        projection_vector: Vector3d = projection_length * vec1_normalized

        # vec2 から射影ベクトルを引いて、vec1 に垂直なベクトルを得る
        result: Vector3d = def_plane_vec - projection_vector
        result = result.normalize()
        return result

    def rotate_around_axis(self, angle_degree: float, axis_vec: Vector3d) -> Vector3d:
        if angle_degree == 0.0:
            return self.clone()
        theta = degree_to_radian(angle_degree)
        a: Vector3d = axis_vec.normalize()
        vec1: Vector3d = math.cos(theta) * self
        vec2: Vector3d = (1.0 - math.cos(theta)) * (self.dot(a)) * a
        vec3: Vector3d = math.sin(theta) * a.cross(self)
        return vec1 + vec2 + vec3

    def to_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    @staticmethod
    def from_collection(
        collection: Sequence[float],
    ) -> Vector3d:
        if len(collection) != 3:
            raise ValueError("3次元のコレクションとしてください")
        return Vector3d(x=collection[0], y=collection[1], z=collection[2])

    @staticmethod
    def from_stb_node(
        stb_node: HasXyz,
    ) -> Vector3d:
        if stb_node.x is None or stb_node.y is None or stb_node.z is None:
            raise SchemaError(
                f"{stb_node._name_for_logger()} x,y,zの値が設定されていません"
            )
        return Vector3d(stb_node.x, stb_node.y, stb_node.z)

    @staticmethod
    def unit_x() -> Vector3d:
        return Vector3d(1.0, 0.0, 0.0)

    @staticmethod
    def unit_y() -> Vector3d:
        return Vector3d(0.0, 1.0, 0.0)

    @staticmethod
    def unit_z() -> Vector3d:
        return Vector3d(0.0, 0.0, 1.0)

    @staticmethod
    def zero() -> Vector3d:
        return Vector3d(0.0, 0.0, 0.0)
