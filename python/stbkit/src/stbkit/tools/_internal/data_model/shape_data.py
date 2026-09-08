# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Final, Self

from ..._internal.constants import UNKNOWN_ELEMENT_SIZE_MM
from ..utils.unit_utils import degree_to_radian
from ..vectors import Vector2d


def rotate_and_offset_points(
    points: list[Vector2d], angle_degree: float | None, offset: Vector2d | None
) -> list[Vector2d]:
    if angle_degree is None and offset is None:
        return points
    angle_degree = angle_degree or 0.0
    offset = offset or Vector2d.zero()
    angle: float = degree_to_radian(angle_degree)
    cos_a: float = math.cos(angle)
    sin_a: float = math.sin(angle)
    rotated_and_offset_points = [
        Vector2d(x * cos_a - y * sin_a + offset.x, x * sin_a + y * cos_a + offset.y)
        for x, y in points
    ]
    return rotated_and_offset_points


def diagram_core(points: list[Vector2d]) -> Vector2d:
    """図心を計算する（多角形の重心）"""
    if not points or len(points) < 3:
        raise ValueError("3点以上の多角形が必要です")
    area: float = 0.0
    cx: float = 0.0
    cy: float = 0.0
    n: int = len(points)
    for i in range(n):
        x0, y0 = points[i].x, points[i].y
        x1, y1 = points[(i + 1) % n].x, points[(i + 1) % n].y
        cross: float = x0 * y1 - x1 * y0
        area += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    area *= 0.5
    if abs(area) < 1e-12:
        raise ValueError("面積がゼロです")
    cx /= 6.0 * area
    cy /= 6.0 * area
    return Vector2d(cx, cy)


class ShapePosition(Enum):
    BOTTOM_CENTER = "中央下"
    BOTTOM_LEFT = "左下"
    BOTTOM_RIGHT = "右下"
    CENTER_CENTER = "中央"
    CENTER_LEFT = "左中央"
    CENTER_RIGHT = "右中央"
    TOP_CENTER = "中央上"
    TOP_LEFT = "左上"
    TOP_RIGHT = "右上"
    DIAGRAM_CORE = "図心"


class SlotsMergeMeta(ABCMeta):
    def __new__(
        mcs,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **kwargs: Any,
    ) -> Any:
        # クラス生成
        cls = super().__new__(mcs, name, bases, namespace)
        # すべての親クラスの __slots__ を集める
        slots: list[str] = []
        for base in bases:
            base_slots = getattr(base, "__slots__", ())
            if isinstance(base_slots, str):
                base_slots = (base_slots,)
            slots.extend(base_slots)
        # dataclassのフィールド名を取得
        if hasattr(cls, "__annotations__"):
            dataclass_fields = cls.__annotations__.keys()
            slots.extend(dataclass_fields)
        # 重複を除去し、tupleに変換
        slots_tuple: tuple[str, ...] = tuple(dict.fromkeys(slots))
        # __slots__をクラスに設定
        cls.__slots__ = slots_tuple  # type: ignore
        return cls


@dataclass(eq=False, order=False, kw_only=True)
class Shape(metaclass=SlotsMergeMeta):
    rotate_degree: float | None = None
    offset: Vector2d | None = None

    # オーバーロード必須メソッド

    @abstractmethod
    def get_out_point2ds(self) -> list[Vector2d]:
        """座標は形状に外接する長方形の中心点を原点とする"""

    # 任意でオーバーロードするメソッド

    def get_in_point2ds(self) -> list[Vector2d] | None:
        """座標は形状に外接する長方形の中心点を原点とする"""
        return None

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.TOP_LEFT:
                return Vector2d(self._x_min, self._y_max)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self._x_max, self._y_max)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(self._x_min, self._y_min)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self._x_max, self._y_min)
            case ShapePosition.TOP_CENTER:
                return Vector2d(self._x_center, self._y_max)
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(self._x_center, self._y_min)
            case ShapePosition.CENTER_LEFT:
                return Vector2d(self._x_min, self._y_center)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self._x_max, self._y_center)
            case ShapePosition.CENTER_CENTER:
                return Vector2d(self._x_center, self._y_center)
            case ShapePosition.DIAGRAM_CORE:
                core_point: Vector2d = diagram_core(self.get_out_point2ds())
                in_point_2ds: list[Vector2d] | None = self.get_in_point2ds()
                if in_point_2ds:
                    core_point -= diagram_core(in_point_2ds)
                return core_point
            case _:
                raise AssertionError(f"{position}:不明な位置指定です")

    # 基本的にオーバーロード不要メソッド

    def get_out_point2ds_with_rotate_and_offset(self) -> list[Vector2d]:
        return rotate_and_offset_points(
            self.get_out_point2ds(), self.rotate_degree, self.offset
        )

    def get_in_point2ds_with_rotate_and_offset(self) -> list[Vector2d] | None:
        in_points = self.get_in_point2ds()
        if in_points is None:
            return None
        return rotate_and_offset_points(in_points, self.rotate_degree, self.offset)

    # プライベートプロパティ

    @property
    def _x_min(self) -> float:
        return min(point.x for point in self.get_out_point2ds())

    @property
    def _x_max(self) -> float:
        return max(point.x for point in self.get_out_point2ds())

    @property
    def _y_min(self) -> float:
        return min(point.y for point in self.get_out_point2ds())

    @property
    def _y_max(self) -> float:
        return max(point.y for point in self.get_out_point2ds())

    @property
    def _x_center(self) -> float:
        return (self._x_min + self._x_max) / 2.0

    @property
    def _y_center(self) -> float:
        return (self._y_min + self._y_max) / 2.0


@dataclass(repr=False, eq=False, order=False)
class ShapePair:
    start: Shape
    end: Shape | None = None


@dataclass(eq=False, order=False, kw_only=True)
class ShapeAngle(Shape):
    name: str
    a: float
    b: float
    t1: float
    t2: float
    r1: float = 0.0
    r2: float = 0.0

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.b / 2.0, -self.a / 2.0),
            Vector2d(-self.b / 2.0 + self.t1, -self.a / 2.0),
            Vector2d(-self.b / 2.0 + self.t1, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        if self.rotate_degree is None and self.offset is None:
            match position:
                case ShapePosition.BOTTOM_CENTER:
                    return Vector2d(0.0, -self.a / 2.0)
                case ShapePosition.BOTTOM_LEFT:
                    return Vector2d(-self.b / 2.0, -self.a / 2.0)
                case ShapePosition.BOTTOM_RIGHT:
                    return Vector2d(self.b / 2.0, -self.a / 2.0)
                case ShapePosition.CENTER_CENTER:
                    return Vector2d.zero()
                case ShapePosition.CENTER_LEFT:
                    return Vector2d(-self.b / 2.0, 0.0)
                case ShapePosition.CENTER_RIGHT:
                    return Vector2d(self.b / 2.0, 0.0)
                case ShapePosition.TOP_CENTER:
                    return Vector2d(0.0, self.a / 2.0)
                case ShapePosition.TOP_LEFT:
                    return Vector2d(-self.b / 2.0, self.a / 2.0)
                case ShapePosition.TOP_RIGHT:
                    return Vector2d(self.b / 2.0, self.a / 2.0)
                case ShapePosition.DIAGRAM_CORE:
                    raise NotImplementedError(
                        "Angleの図心の計算はサポートされていません"
                    )
        else:
            return super().get_position_point(position)


@dataclass(eq=False, order=False, kw_only=True)
class ShapeArbitrary(Shape):
    out_points: list[Vector2d] = field(default_factory=list)
    in_points: list[list[Vector2d]] = field(default_factory=list)

    def get_out_point2ds(self) -> list[Vector2d]:
        return self.out_points

    def get_in_point2ds(self) -> list[Vector2d] | None:
        if self.in_points:
            return self.in_points[0]
        else:
            return None

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        if position == ShapePosition.DIAGRAM_CORE:
            core_point: Vector2d = diagram_core(self.out_points)
            for in_point_2ds in self.in_points:
                core_point -= diagram_core(in_point_2ds)
            return core_point
        return super().get_position_point(position)


@dataclass(eq=False, order=False, kw_only=True)
class ShapeBox(Shape):
    name: str
    a: float
    b: float
    t: float
    r: float

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(0.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(-self.b / 2.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self.b / 2.0, -self.a / 2.0)
            case ShapePosition.CENTER_LEFT:
                return Vector2d(-self.b / 2.0, 0.0)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self.b / 2.0, 0.0)
            case ShapePosition.TOP_CENTER:
                return Vector2d(0.0, self.a / 2.0)
            case ShapePosition.TOP_LEFT:
                return Vector2d(-self.b / 2.0, self.a / 2.0)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self.b / 2.0, self.a / 2.0)
            case ShapePosition.CENTER_CENTER | ShapePosition.DIAGRAM_CORE:
                return Vector2d.zero()


@dataclass(eq=False, order=False, kw_only=True)
class ShapeBuildBox(Shape):
    name: str
    a: float
    b: float
    t1: float
    t2: float

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0),
        ]
        return result

    def get_in_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.b / 2.0 + self.t1, -self.a / 2.0 + self.t2),
            Vector2d(self.b / 2.0 - self.t1, -self.a / 2.0 + self.t2),
            Vector2d(self.b / 2.0 - self.t1, self.a / 2.0 - self.t2),
            Vector2d(-self.b / 2.0 + self.t1, self.a / 2.0 - self.t2),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(0.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(-self.b / 2.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self.b / 2.0, -self.a / 2.0)
            case ShapePosition.CENTER_LEFT:
                return Vector2d(-self.b / 2.0, 0.0)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self.b / 2.0, 0.0)
            case ShapePosition.TOP_CENTER:
                return Vector2d(0.0, self.a / 2.0)
            case ShapePosition.TOP_LEFT:
                return Vector2d(-self.b / 2.0, self.a / 2.0)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self.b / 2.0, self.a / 2.0)
            case ShapePosition.CENTER_CENTER | ShapePosition.DIAGRAM_CORE:
                return Vector2d.zero()


@dataclass(eq=False, order=False, kw_only=True)
class ShapeChannel(Shape):
    name: str
    a: float
    b: float
    t1: float
    t2: float
    r1: float = 0.0
    r2: float = 0.0

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, -self.a / 2.0 + self.t2),
            Vector2d(-self.b / 2.0 + self.t1, -self.a / 2.0 + self.t2),
            Vector2d(-self.b / 2.0 + self.t1, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(0.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(-self.b / 2.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self.b / 2.0, -self.a / 2.0)
            case ShapePosition.CENTER_CENTER:
                return Vector2d.zero()
            case ShapePosition.CENTER_LEFT:
                return Vector2d(-self.b / 2.0, 0.0)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self.b / 2.0, 0.0)
            case ShapePosition.TOP_CENTER:
                return Vector2d(0.0, self.a / 2.0)
            case ShapePosition.TOP_LEFT:
                return Vector2d(-self.b / 2.0, self.a / 2.0)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self.b / 2.0, self.a / 2.0)
            case ShapePosition.DIAGRAM_CORE:
                raise NotImplementedError("Channelの図心の計算はサポートされていません")


@dataclass(eq=False, order=False, kw_only=True)
class ShapeCircle(Shape):
    name: str
    d: float
    number_of_divisions: int = 12

    def get_out_point2ds(self) -> list[Vector2d]:
        n_div: int = max(self.number_of_divisions, 3)
        unit_angle: float = math.pi * 2.0 / n_div
        r: float = self.d / 2.0
        result: list[Vector2d] = [
            Vector2d(
                r * math.cos(i * unit_angle),
                r * math.sin(i * unit_angle),
            )
            for i in range(n_div)
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        i: int
        match position:
            case ShapePosition.CENTER_CENTER | ShapePosition.DIAGRAM_CORE:
                return Vector2d.zero()
            case ShapePosition.BOTTOM_CENTER:
                i = 6
            case ShapePosition.BOTTOM_LEFT:
                i = 5
            case ShapePosition.BOTTOM_RIGHT:
                i = 7
            case ShapePosition.CENTER_LEFT:
                i = 4
            case ShapePosition.CENTER_RIGHT:
                i = 0
            case ShapePosition.TOP_CENTER:
                i = 2
            case ShapePosition.TOP_LEFT:
                i = 1
            case ShapePosition.TOP_RIGHT:
                i = 3
        unit_angle: float = math.pi * 2.0 / 8.0
        r: float = self.d / 2.0
        return Vector2d(
            r * math.cos(i * unit_angle),
            r * math.sin(i * unit_angle),
        )


@dataclass(eq=False, order=False, kw_only=True)
class ShapeCrossH(Shape):
    name: str
    h_h: float
    h_b: float
    h_tw: float
    h_tf: float
    i_h: float
    i_b: float
    i_tw: float
    i_tf: float
    i_offset_x: float = 0.0
    h_offset_y: float = 0.0

    @property
    def _x_max(self) -> float:
        return self.h_h / 2.0

    @property
    def _x_min(self) -> float:
        return -self.h_h / 2.0

    @property
    def _x_center(self) -> float:
        return 0.0

    @property
    def _y_max(self) -> float:
        return self.i_h / 2.0

    @property
    def _y_min(self) -> float:
        return -self.i_h / 2.0

    @property
    def _y_center(self) -> float:
        return 0.0

    def get_out_point2ds(self) -> list[Vector2d]:
        return [
            Vector2d(-self.i_b / 2.0 + self.i_offset_x, self._y_min),
            Vector2d(self.i_b / 2.0 + self.i_offset_x, self._y_min),
            Vector2d(self.i_b / 2.0 + self.i_offset_x, self._y_min + self.i_tf),
            Vector2d(self.i_tw / 2.0 + self.i_offset_x, self._y_min + self.i_tf),
            Vector2d(
                self.i_tw / 2.0 + self.i_offset_x, -self.h_tw / 2.0 + self.h_offset_y
            ),
            Vector2d(self._x_max - self.h_tf, -self.h_tw / 2.0 + self.h_offset_y),
            Vector2d(self._x_max - self.h_tf, -self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_max, -self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_max, self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_max - self.h_tf, self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_max - self.h_tf, self.h_tw / 2.0 + self.h_offset_y),
            Vector2d(
                self.i_tw / 2.0 + self.i_offset_x, self.h_tw / 2.0 + self.h_offset_y
            ),
            Vector2d(self.i_tw / 2.0 + self.i_offset_x, self._y_max - self.i_tf),
            Vector2d(self.i_b / 2.0 + self.i_offset_x, self._y_max - self.i_tf),
            Vector2d(self.i_b / 2.0 + self.i_offset_x, self._y_max),
            Vector2d(-self.i_b / 2.0 + self.i_offset_x, self._y_max),
            Vector2d(-self.i_b / 2.0 + self.i_offset_x, self._y_max - self.i_tf),
            Vector2d(-self.i_tw / 2.0 + self.i_offset_x, self._y_max - self.i_tf),
            Vector2d(
                -self.i_tw / 2.0 + self.i_offset_x, self.h_tw / 2.0 + self.h_offset_y
            ),
            Vector2d(self._x_min + self.h_tf, self.h_tw / 2.0 + self.h_offset_y),
            Vector2d(self._x_min + self.h_tf, self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_min, self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_min, -self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_min + self.h_tf, -self.h_b / 2.0 + self.h_offset_y),
            Vector2d(self._x_min + self.h_tf, -self.h_tw / 2.0 + self.h_offset_y),
            Vector2d(
                -self.i_tw / 2.0 + self.i_offset_x, -self.h_tw / 2.0 + self.h_offset_y
            ),
            Vector2d(-self.i_tw / 2.0 + self.i_offset_x, self._y_min + self.i_tf),
            Vector2d(-self.i_b / 2.0 + self.i_offset_x, self._y_min + self.i_tf),
        ]


@dataclass(eq=False, order=False, kw_only=True)
class ShapeEquilateralTriangle(Shape):
    name: str
    width_base: float
    width_chamfer: float = 0.0

    def get_out_point2ds(self) -> list[Vector2d]:
        if self.width_chamfer == 0.0:
            return [
                Vector2d(self._x_min, self._y_min),
                Vector2d(self._x_max, self._y_min),
                Vector2d(self._x_center, self._y_max),
            ]
        else:
            height_chamfer: float = (math.sqrt(3.0) / 2.0) * self.width_chamfer
            return [
                Vector2d(-self.width_base / 2.0, self._y_min),
                Vector2d(self.width_base / 2.0, self._y_min),
                Vector2d(
                    self._x_max,
                    self._y_min + height_chamfer,
                ),
                Vector2d(self.width_chamfer / 2.0, self._y_max),
                Vector2d(-self.width_chamfer / 2.0, self._y_max),
                Vector2d(
                    self._x_min,
                    self._y_min + height_chamfer,
                ),
            ]

    @property
    def _x_max(self) -> float:
        if self.width_chamfer == 0.0:
            return self.width_base / 2.0
        else:
            return self.width_base / 2.0 + self.width_chamfer / 2.0

    @property
    def _x_min(self) -> float:
        return -self._x_max

    @property
    def _x_center(self) -> float:
        return 0.0

    @property
    def _y_max(self) -> float:
        return math.sqrt(3.0) / 2.0 * (self.width_base + self.width_chamfer) / 2.0

    @property
    def _y_min(self) -> float:
        return -self._y_max

    @property
    def _y_center(self) -> float:
        return 0.0


@dataclass(eq=False, order=False, kw_only=True)
class ShapeH(Shape):
    name: str
    a: float
    b: float
    t1: float
    t2: float
    r: float

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, -self.a / 2.0),
            Vector2d(self.b / 2.0, -self.a / 2.0 + self.t2),
            Vector2d(self.t1 / 2.0, -self.a / 2.0 + self.t2),
            Vector2d(self.t1 / 2.0, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0 - self.t2),
            Vector2d(-self.t1 / 2.0, self.a / 2.0 - self.t2),
            Vector2d(-self.t1 / 2.0, -self.a / 2.0 + self.t2),
            Vector2d(-self.b / 2.0, -self.a / 2.0 + self.t2),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.CENTER_CENTER | ShapePosition.DIAGRAM_CORE:
                return Vector2d.zero()
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(0.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(-self.b / 2.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self.b / 2.0, -self.a / 2.0)
            case ShapePosition.CENTER_LEFT:
                return Vector2d(-self.b / 2.0, 0.0)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self.b / 2.0, 0.0)
            case ShapePosition.TOP_CENTER:
                return Vector2d(0.0, self.a / 2.0)
            case ShapePosition.TOP_LEFT:
                return Vector2d(-self.b / 2.0, self.a / 2.0)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self.b / 2.0, self.a / 2.0)


@dataclass(eq=False, order=False, kw_only=True)
class ShapeLipC(Shape):
    name: str
    h: float
    a: float
    c: float
    t: float

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.a / 2.0, -self.h / 2.0),
            Vector2d(self.a / 2.0, -self.h / 2.0),
            Vector2d(self.a / 2.0, -self.h / 2.0 + self.c),
            Vector2d(self.a / 2.0 - self.t, -self.h / 2.0 + self.c),
            Vector2d(self.a / 2.0 - self.t, -self.h / 2.0 + self.t),
            Vector2d(-self.a / 2.0 + self.t, -self.h / 2.0 + self.t),
            Vector2d(-self.a / 2.0 + self.t, self.h / 2.0 - self.t),
            Vector2d(self.a / 2.0 - self.t, self.h / 2.0 - self.t),
            Vector2d(self.a / 2.0 - self.t, self.h / 2.0 - self.c),
            Vector2d(self.a / 2.0, self.h / 2.0 - self.c),
            Vector2d(self.a / 2.0, self.h / 2.0),
            Vector2d(-self.a / 2.0, self.h / 2.0),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(0.0, -self.h / 2.0)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(-self.a / 2.0, -self.h / 2.0)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self.a / 2.0, -self.h / 2.0)
            case ShapePosition.CENTER_CENTER:
                return Vector2d.zero()
            case ShapePosition.CENTER_LEFT:
                return Vector2d(-self.a / 2.0, 0.0)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self.a / 2.0, 0.0)
            case ShapePosition.TOP_CENTER:
                return Vector2d(0.0, self.h / 2.0)
            case ShapePosition.TOP_LEFT:
                return Vector2d(-self.a / 2.0, self.h / 2.0)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self.a / 2.0, self.h / 2.0)
            case ShapePosition.DIAGRAM_CORE:
                raise NotImplementedError("LipCの図心の計算はサポートされていません")


@dataclass(eq=False, order=False, kw_only=True)
class ShapeOctagon(Shape):
    name: str
    width_x: float
    width_y: float
    width_chamfer_bottom_left_x: float = 0.0
    width_chamfer_bottom_left_y: float = 0.0
    width_chamfer_bottom_right_x: float = 0.0
    width_chamfer_bottom_right_y: float = 0.0
    width_chamfer_top_right_x: float = 0.0
    width_chamfer_top_right_y: float = 0.0
    width_chamfer_top_left_x: float = 0.0
    width_chamfer_top_left_y: float = 0.0

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = []
        if (
            self.width_chamfer_bottom_left_x == 0.0
            or self.width_chamfer_bottom_left_y == 0.0
        ):
            result.append(Vector2d(self._x_min, self._y_min))
        else:
            result.append(
                Vector2d(self._x_min + self.width_chamfer_bottom_left_x, self._y_min)
            )
        if (
            self.width_chamfer_bottom_right_x == 0.0
            or self.width_chamfer_bottom_right_y == 0.0
        ):
            result.append(Vector2d(self._x_max, self._y_min))
        else:
            result.append(
                Vector2d(self._x_max - self.width_chamfer_bottom_right_x, self._y_min)
            )
            result.append(
                Vector2d(self._x_max, self._y_min + self.width_chamfer_bottom_right_y)
            )
        if (
            self.width_chamfer_top_right_x == 0.0
            or self.width_chamfer_top_right_y == 0.0
        ):
            result.append(Vector2d(self._x_max, self._y_max))
        else:
            result.append(
                Vector2d(self._x_max, self._y_max - self.width_chamfer_top_right_y)
            )
            result.append(
                Vector2d(self._x_max - self.width_chamfer_top_right_x, self._y_max)
            )
        if self.width_chamfer_top_left_x == 0.0 or self.width_chamfer_top_left_y == 0.0:
            result.append(Vector2d(self._x_min, self._y_max))
        else:
            result.append(
                Vector2d(self._x_min + self.width_chamfer_top_left_x, self._y_max)
            )
            result.append(
                Vector2d(self._x_min, self._y_max - self.width_chamfer_top_left_y)
            )
        if (
            self.width_chamfer_bottom_left_x == 0.0
            or self.width_chamfer_bottom_left_y == 0.0
        ):
            pass
        else:
            result.append(
                Vector2d(self._x_min, self._y_min + self.width_chamfer_bottom_left_y)
            )
        return result

    @property
    def _x_min(self) -> float:
        return -self.width_x / 2.0

    @property
    def _x_max(self) -> float:
        return self.width_x / 2.0

    @property
    def _x_center(self) -> float:
        return 0.0

    @property
    def _y_min(self) -> float:
        return -self.width_y / 2.0

    @property
    def _y_max(self) -> float:
        return self.width_y / 2.0

    @property
    def _y_center(self) -> float:
        return 0.0


@dataclass(eq=False, order=False, kw_only=True)
class ShapePipe(Shape):
    name: str
    d: float
    t: float
    number_of_divisions: int = 12

    def get_out_point2ds(self) -> list[Vector2d]:
        n_div: int = max(self.number_of_divisions, 3)
        unit_angle: float = math.pi * 2.0 / n_div
        r: float = self.d / 2.0
        result: list[Vector2d] = [
            Vector2d(
                r * math.cos(i * unit_angle),
                r * math.sin(i * unit_angle),
            )
            for i in range(n_div)
        ]
        return result

    def get_in_point2ds(self) -> list[Vector2d]:
        n_div: int = max(self.number_of_divisions, 3)
        unit_angle: float = math.pi * 2.0 / n_div
        r = self.d / 2.0 - self.t
        result: list[Vector2d] = [
            Vector2d(
                r * math.cos(i * unit_angle),
                r * math.sin(i * unit_angle),
            )
            for i in range(n_div)
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        i: int
        match position:
            case ShapePosition.CENTER_CENTER | ShapePosition.DIAGRAM_CORE:
                return Vector2d.zero()
            case ShapePosition.BOTTOM_CENTER:
                i = 6
            case ShapePosition.BOTTOM_LEFT:
                i = 5
            case ShapePosition.BOTTOM_RIGHT:
                i = 7
            case ShapePosition.CENTER_LEFT:
                i = 4
            case ShapePosition.CENTER_RIGHT:
                i = 0
            case ShapePosition.TOP_CENTER:
                i = 2
            case ShapePosition.TOP_LEFT:
                i = 1
            case ShapePosition.TOP_RIGHT:
                i = 3
        unit_angle: float = math.pi * 2.0 / 8.0
        r: float = self.d / 2.0
        return Vector2d(
            r * math.cos(i * unit_angle),
            r * math.sin(i * unit_angle),
        )


@dataclass(eq=False, order=False, kw_only=True)
class ShapeRectangle(Shape):
    name: str
    width_x: float
    width_y: float

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.width_x / 2.0, -self.width_y / 2.0),
            Vector2d(self.width_x / 2.0, -self.width_y / 2.0),
            Vector2d(self.width_x / 2.0, self.width_y / 2.0),
            Vector2d(-self.width_x / 2.0, self.width_y / 2.0),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.CENTER_CENTER | ShapePosition.DIAGRAM_CORE:
                return Vector2d.zero()
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(0.0, -self.width_y / 2.0)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(-self.width_x / 2.0, -self.width_y / 2.0)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self.width_x / 2.0, -self.width_y / 2.0)
            case ShapePosition.CENTER_LEFT:
                return Vector2d(-self.width_x / 2.0, 0.0)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self.width_x / 2.0, 0.0)
            case ShapePosition.TOP_CENTER:
                return Vector2d(0.0, self.width_y / 2.0)
            case ShapePosition.TOP_LEFT:
                return Vector2d(-self.width_x / 2.0, self.width_y / 2.0)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self.width_x / 2.0, self.width_y / 2.0)


@dataclass(eq=False, order=False, kw_only=True)
class ShapeRightTriangle(Shape):
    """直角三角形

    左下が直角とする"""

    name: str
    width_x: float
    width_y: float
    chamfer_x: float = 0.0
    chamfer_y: float = 0.0

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.width_x / 2.0, -self.width_y / 2.0),
            Vector2d(self.width_x / 2.0, -self.width_y / 2.0),
        ]
        if self.chamfer_y > 0.0:
            result.append(
                Vector2d(self.width_x / 2.0, -self.width_y / 2.0 + self.chamfer_y)
            )
        if self.chamfer_x > 0.0:
            result.append(
                Vector2d(-self.width_x / 2.0 + self.chamfer_x, self.width_y / 2.0)
            )
        result.append(
            Vector2d(-self.width_x / 2.0, self.width_y / 2.0),
        )
        return result

    @property
    def _x_max(self) -> float:
        return self.width_x / 2.0

    @property
    def _x_min(self) -> float:
        return -self.width_x / 2.0

    @property
    def _x_center(self) -> float:
        return 0.0

    @property
    def _y_max(self) -> float:
        return self.width_y / 2.0

    @property
    def _y_min(self) -> float:
        return -self.width_y / 2.0

    @property
    def _y_center(self) -> float:
        return 0.0


@dataclass(eq=False, order=False, kw_only=True)
class ShapeT(Shape):
    name: str
    a: float
    b: float
    t1: float
    t2: float
    r: float

    def get_out_point2ds(self) -> list[Vector2d]:
        result: list[Vector2d] = [
            Vector2d(-self.t1 / 2.0, -self.a / 2.0),
            Vector2d(self.t1 / 2.0, -self.a / 2.0),
            Vector2d(self.t1 / 2.0, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0 - self.t2),
            Vector2d(self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0),
            Vector2d(-self.b / 2.0, self.a / 2.0 - self.t2),
            Vector2d(-self.t1 / 2.0, self.a / 2.0 - self.t2),
        ]
        return result

    def get_position_point(self, position: ShapePosition) -> Vector2d:
        match position:
            case ShapePosition.BOTTOM_CENTER:
                return Vector2d(0.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_LEFT:
                return Vector2d(-self.b / 2.0, -self.a / 2.0)
            case ShapePosition.BOTTOM_RIGHT:
                return Vector2d(self.b / 2.0, -self.a / 2.0)
            case ShapePosition.CENTER_CENTER:
                return Vector2d.zero()
            case ShapePosition.CENTER_LEFT:
                return Vector2d(-self.b / 2.0, 0.0)
            case ShapePosition.CENTER_RIGHT:
                return Vector2d(self.b / 2.0, 0.0)
            case ShapePosition.TOP_CENTER:
                return Vector2d(0.0, self.a / 2.0)
            case ShapePosition.TOP_LEFT:
                return Vector2d(-self.b / 2.0, self.a / 2.0)
            case ShapePosition.TOP_RIGHT:
                return Vector2d(self.b / 2.0, self.a / 2.0)
            case ShapePosition.DIAGRAM_CORE:
                raise NotImplementedError("T形鋼の図心の計算はサポートされていません")


@dataclass(eq=False, order=False, kw_only=True)
class ShapeTSrc(Shape):
    name: str
    h_h: float
    h_b: float
    h_tw: float
    h_tf: float
    t_h: float
    t_b: float
    t_tw: float
    t_tf: float
    t_offset_x: float = 0.0

    @property
    def _x_max(self) -> float:
        return self.h_h / 2.0

    @property
    def _x_min(self) -> float:
        return -self.h_h / 2.0

    @property
    def _x_center(self) -> float:
        return 0.0

    @property
    def _y_max(self) -> float:
        return (self.t_h + self.h_b / 2.0) / 2.0

    @property
    def _y_min(self) -> float:
        return -self._y_max

    @property
    def _y_center(self) -> float:
        return 0.0

    def get_out_point2ds(self) -> list[Vector2d]:
        return [
            Vector2d(-self.t_b / 2.0 + self.t_offset_x, self._y_min),
            Vector2d(self.t_b / 2.0 + self.t_offset_x, self._y_min),
            Vector2d(self.t_b / 2.0 + self.t_offset_x, self._y_min + self.t_tf),
            Vector2d(self.t_tw / 2.0 + self.t_offset_x, self._y_min + self.t_tf),
            Vector2d(
                self.t_tw / 2.0 + self.t_offset_x,
                self._y_max - self.h_b / 2.0 - self.h_tw / 2.0,
            ),
            Vector2d(
                self._x_max - self.h_tf, self._y_max - self.h_b / 2.0 - self.h_tw / 2.0
            ),
            Vector2d(self._x_max - self.h_tf, self._y_max - self.h_b),
            Vector2d(self._x_max, self._y_max - self.h_b),
            Vector2d(self._x_max, self._y_max),
            Vector2d(self._x_max - self.h_tf, self._y_max),
            Vector2d(
                self._x_max - self.h_tf, self._y_max - self.h_b / 2.0 + self.h_tw / 2.0
            ),
            Vector2d(
                self._x_min + self.h_tf, self._y_max - self.h_b / 2.0 + self.h_tw / 2.0
            ),
            Vector2d(self._x_min + self.h_tf, self._y_max),
            Vector2d(self._x_min, self._y_max),
            Vector2d(self._x_min, self._y_max - self.h_b),
            Vector2d(self._x_min + self.h_tf, self._y_max - self.h_b),
            Vector2d(
                self._x_min + self.h_tf, self._y_max - self.h_b / 2.0 - self.h_tw / 2.0
            ),
            Vector2d(
                -self.t_tw / 2.0 + self.t_offset_x,
                self._y_max - self.h_b / 2.0 - self.h_tw / 2.0,
            ),
            Vector2d(-self.t_tw / 2.0 + self.t_offset_x, self._y_min + self.t_tf),
            Vector2d(-self.t_b / 2.0 + self.t_offset_x, self._y_min + self.t_tf),
        ]


class ShapeUnknown(Shape):
    _instance: Shape | None = None

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = ShapeRectangle(
                name="Unknown",
                width_x=UNKNOWN_ELEMENT_SIZE_MM,
                width_y=UNKNOWN_ELEMENT_SIZE_MM,
            )
        return cls._instance  # type:ignore[return-value]

    def get_out_point2ds(self) -> list[Vector2d]:
        if self._instance is None:
            raise RuntimeError("UnknownShape instance is not initialized.")
        return self._instance.get_out_point2ds()


class ShapeUndefined(Shape):
    _instance: Shape | None = None

    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = ShapeRectangle(
                name="Undefined",
                width_x=UNKNOWN_ELEMENT_SIZE_MM,
                width_y=UNKNOWN_ELEMENT_SIZE_MM,
            )
        return cls._instance

    def get_out_point2ds(self) -> list[Vector2d]:
        if self._instance is None:
            raise RuntimeError("UndefinedShape instance is not initialized.")
        return self._instance.get_out_point2ds()


SHAPE_PAIR_UNKNOWN: Final[ShapePair] = ShapePair(start=ShapeUnknown(), end=None)
SHAPE_PAIRS_UNKNOWN: Final[list[ShapePair]] = [SHAPE_PAIR_UNKNOWN]
SHAPE_PAIR_UNDEFINED: Final[ShapePair] = ShapePair(start=ShapeUndefined(), end=None)
SHAPE_PAIRS_UNDEFINED: Final[list[ShapePair]] = [SHAPE_PAIR_UNDEFINED]
