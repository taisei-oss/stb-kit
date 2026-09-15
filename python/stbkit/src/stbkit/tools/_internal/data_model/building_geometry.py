# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from array import array
from collections.abc import Iterable, Sequence, Sized
from dataclasses import dataclass, field
from enum import IntEnum, IntFlag
from math import isfinite
from uuid import UUID

from ..vectors import Vector3d

UINT32_NONE = 0xFFFF_FFFF
"""u32列で参照なし表す値。Rustのu32::MAXと一致させる。"""

_GUID_SIZE = 16

# 処理系依存対策
if array("f").itemsize != 4:
    raise RuntimeError("array('f')のサイズが32bitになっていません")
if array("d").itemsize != 8:
    raise RuntimeError("array('d')のサイズが64bitになっていません")
if array("I").itemsize != 4:
    raise RuntimeError("array('I')のサイズが32bitになっていません")


def _new_f32_array() -> array[float]:
    # GPU描画用
    return array("f")


def _new_f64_array() -> array[float]:
    return array("d")


def _new_u32_array() -> array[int]:
    # id用
    return array("I")


def _new_offsets_array() -> array[int]:
    # データの範囲をoffsets[i]:offsets[i + 1] で求めるため、
    # 要素が0個でも先頭の0を作っておく。
    return array("I", [0])


def _vector3(value: Sequence[float], *, name: str) -> Vector3d:
    """任意コレクションのVector3dへの変換。
    NaNや無限大のチェックも行うことで、rustへ渡る前に不整値を排除する。
    """
    if len(value) != 3:
        raise ValueError(f"{name}のlenは3である必要があります")

    vec: Vector3d = Vector3d(float(value[0]), float(value[1]), float(value[2]))
    if not all(isfinite(component) for component in vec):
        raise ValueError(f"{name}の全ての要素は有限値である必要があります")
    return vec


class ElementKind(IntEnum):
    UNKNOWN = 0
    COLUMN = 1
    POST = 2
    GIRDER = 3
    BEAM = 4
    BRACE = 5
    SLAB = 6
    WALL = 7
    ISOLATING_DEVICE = 8
    DAMPING_DEVICE = 9
    FRAME_DAMPING_DEVICE = 10
    FOOTING = 11
    STRIP_FOOTING = 12
    PILE = 13
    FOUNDATION_COLUMN = 14
    PARAPET = 15
    OPEN = 16
    PENETRATION = 17
    JOINT = 18
    PANEL_ZONE = 19
    CONNECTION = 20
    OTHER = 21


class ElementFlags(IntFlag):
    NONE = 0
    HAS_MESH = 1 << 0
    HAS_LINE_SHAPE = 1 << 1
    HAS_PLANE_SHAPE = 1 << 2
    HAS_NODE_RELATION = 1 << 3
    HAS_STORY_RELATION = 1 << 4

    # 合成構造断面（SRC・CFT）を、RCとSの2要素へ分けたときの部位。
    # 単一断面の要素はどちらのビットも立たない。また、両方が同時に立つこともない。
    IS_COMPOSITE_CONCRETE = 1 << 5
    IS_COMPOSITE_STEEL = 1 << 6


class SurfaceLoopType(IntEnum):
    # 1つの面につきOUTERは1つ、HOLEは0個以上
    OUTER = 0
    HOLE = 1


@dataclass(slots=True)
class OptionalUuidColumn:
    """UUID | Noneを、固定長bytearrayと有効フラグで保持する"""

    data: bytearray = field(default_factory=bytearray, repr=False)
    """要素[i]のUUIDをdata[i * 16:(i + 1) * 16]に格納"""
    valid: bytearray = field(default_factory=bytearray, repr=False)
    """0:None, 1:UUIDあり"""

    def __len__(self) -> int:
        return len(self.valid)

    def append(self, value: UUID | str | None) -> None:
        if value is None:
            # 固定長を維持するため、Noneでもメモリを確保する
            self.data.extend(b"\x00" * _GUID_SIZE)
            self.valid.append(0)
            return
        uuid_value: UUID = value if isinstance(value, UUID) else UUID(value)
        self.data.extend(uuid_value.bytes)
        self.valid.append(1)

    def get(self, index: int) -> UUID | None:
        if not 0 <= index < len(self):
            raise IndexError(index)
        if self.valid[index] == 0:
            return None
        start: int = index * _GUID_SIZE
        return UUID(bytes=bytes(self.data[start : start + _GUID_SIZE]))

    def validate(self, expected_count: int | None = None) -> None:
        if len(self.data) != len(self.valid) * _GUID_SIZE:
            raise ValueError(
                "UUIDを格納推している配列サイズが不正です: "
                f"{len(self.data)} != {len(self.valid) * _GUID_SIZE}"
            )
        if expected_count is not None and len(self) != expected_count:
            raise ValueError(
                f"UUIDの数が不正です: expect={expected_count}, actual={len(self)}"
            )
        if any(value not in (0, 1) for value in self.valid):
            raise ValueError("UUID valid フラグは0か1でなければなりません")


@dataclass(frozen=True, slots=True)
class MeshRange:
    # PolygonMesh.positions上のvertex開始位置と長さ
    vertex_start: int
    vertex_count: int

    # PolygonMesh.face_offsets上のface開始位置と長さ
    face_start: int
    face_count: int


@dataclass(slots=True)
class PolygonMesh:
    positions: array[float] = field(default_factory=_new_f32_array, repr=False)
    """x, y, z, x, y, z, ...。BuildingGeometry.origin_xyzからの相対座標。"""

    face_vertex_indices: array[int] = field(
        default_factory=_new_u32_array,
        repr=False,
    )
    """面の頂点。

    例えば面が(0, 1, 2, 3),(4, 5, 6)なら、 [0, 1, 2, 3, 4, 5, 6]のように格納する"""

    face_offsets: array[int] = field(
        default_factory=_new_offsets_array,
        repr=False,
    )
    """面の頂点のオフセット開始位置。

    例えば面が(0, 1, 2, 3),(4, 5, 6)なら、 [0, 4, 7]のように格納する。
    面iはface_offsets[i]:face_offsets[i + 1]を参照する。"""

    @property
    def vertex_count(self) -> int:
        return len(self.positions) // 3

    @property
    def face_count(self) -> int:
        return len(self.face_offsets) - 1

    def validate(self) -> None:
        if len(self.positions) % 3 != 0:
            raise ValueError("len(mesh.positions)が3の倍数ではありません")
        if not self.face_offsets:
            raise ValueError("mesh.face_offsetsが空です")
        if self.face_offsets[0] != 0:
            raise ValueError("mesh.face_offsetsの先頭は0でなければなりません")
        if self.face_offsets[-1] != len(self.face_vertex_indices):
            raise ValueError(
                "最後のface offsetはface vertex indexの数と一致しなければなりません"
            )

        previous: int = 0
        for face_index in range(self.face_count):
            start: int = self.face_offsets[face_index]
            end: int = self.face_offsets[face_index + 1]
            if start < previous or end < start:
                raise ValueError("mesh.face_offsetsは単調増加でなければなりません")
            if end - start < 3:
                raise ValueError(f"mesh face {face_index}は最低3つの頂点が必要です")
            previous = end

        vertex_count: int = self.vertex_count
        for index in self.face_vertex_indices:
            if index >= vertex_count:
                raise ValueError(
                    f"mesh vertex index {index} は {vertex_count} 頂点の範囲外です"
                )


@dataclass(frozen=True, slots=True)
class LineShape:
    start: Vector3d
    end: Vector3d

    reference_y: Vector3d | None


@dataclass(slots=True)
class LineShapeTable:
    start_end_xyz: array[float] = field(default_factory=_new_f64_array, repr=False)
    """1要素につき start xyz + end xyz の6値。"""

    reference_y_xyz: array[float] = field(default_factory=_new_f64_array, repr=False)
    """1要素につき reference_y xyz の3値。"""
    reference_y_valid: bytearray = field(default_factory=bytearray, repr=False)
    """1要素につき1値。0:None, 1:設定済み。"""

    def __len__(self) -> int:
        return len(self.reference_y_valid)

    def add(
        self,
        start: Sequence[float],
        end: Sequence[float],
        reference_y: Sequence[float] | None = None,
    ) -> int:
        start_value: Vector3d = _vector3(start, name="start")
        end_value: Vector3d = _vector3(end, name="end")

        index: int = len(self)
        self.start_end_xyz.extend((*start_value, *end_value))

        if reference_y is None:
            # 固定長を維持するため、Noneでもメモリを確保する。
            self.reference_y_xyz.extend((0.0, 0.0, 0.0))
            self.reference_y_valid.append(0)
        else:
            reference_y_value: Vector3d = _vector3(reference_y, name="reference_y")
            self.reference_y_xyz.extend(reference_y_value)
            self.reference_y_valid.append(1)

        return index

    def get(self, index: int) -> LineShape:
        if not 0 <= index < len(self):
            raise IndexError(index)

        start_offset: int = index * 6
        reference_offset: int = index * 3
        start: tuple[float, ...] = tuple(
            self.start_end_xyz[start_offset : start_offset + 3]
        )
        end: tuple[float, ...] = tuple(
            self.start_end_xyz[start_offset + 3 : start_offset + 6]
        )
        reference_y: tuple[float, ...] | None = None
        if self.reference_y_valid[index]:
            reference_y = tuple(
                self.reference_y_xyz[reference_offset : reference_offset + 3]
            )

        return LineShape(
            start=Vector3d(float(start[0]), float(start[1]), float(start[2])),
            end=Vector3d(float(end[0]), float(end[1]), float(end[2])),
            reference_y=(
                None
                if reference_y is None
                else Vector3d(
                    float(reference_y[0]),
                    float(reference_y[1]),
                    float(reference_y[2]),
                )
            ),
        )

    def validate(self) -> None:
        count = len(self)
        if len(self.start_end_xyz) != count * 6:
            raise ValueError(
                "line start_end_xyzの長さは count * 6 である必要があります"
            )
        if len(self.reference_y_xyz) != count * 3:
            raise ValueError(
                "line reference_y_xyzの長さは count * 3 である必要があります"
            )
        if any(value not in (0, 1) for value in self.reference_y_valid):
            raise ValueError(
                "line reference_y_valid の値は 0 または 1 である必要があります"
            )


@dataclass(frozen=True, slots=True)
class PlaneLoop:
    role: SurfaceLoopType
    points: tuple[Vector3d, ...]


@dataclass(frozen=True, slots=True)
class PlaneShape:
    loops: tuple[PlaneLoop, ...]


@dataclass(slots=True)
class PlaneShapeTable:
    points_xyz: array[float] = field(default_factory=_new_f64_array, repr=False)
    """全ループの頂点。x, y, z の順で1点につき3値。
    ループの順序はplane_loop_offsetsで表す。"""
    loop_point_offsets: array[int] = field(
        default_factory=_new_offsets_array,
        repr=False,
    )
    """ループiが使用する頂点の範囲は
    loop_point_offsets[i]:loop_point_offsets[i + 1]。"""

    plane_loop_offsets: array[int] = field(
        default_factory=_new_offsets_array,
        repr=False,
    )
    """面iが使用するループ範囲は
    plane_loop_offsets[i]:plane_loop_offsets[i + 1]。
    """

    loop_types: bytearray = field(default_factory=bytearray, repr=False)
    """loop_point_offsetsで表される各ループと同じ順序でOUTER/HOLEを保持する。"""

    @property
    def loop_count(self) -> int:
        return len(self.loop_point_offsets) - 1

    @property
    def plane_count(self) -> int:
        return len(self.plane_loop_offsets) - 1

    def add(
        self,
        loops: Sequence[tuple[SurfaceLoopType | int, Sequence[Sequence[float]]]],
    ) -> int:
        if not loops:
            raise ValueError("planeには少なくとも1つのループが必要です")

        plane_index: int = self.plane_count
        outer_count: int = 0

        for raw_role, raw_points in loops:
            role: SurfaceLoopType = SurfaceLoopType(raw_role)
            if role is SurfaceLoopType.OUTER:
                outer_count += 1

            if len(raw_points) < 3:
                raise ValueError("planeの各ループには少なくとも3点が必要です")

            for point_index, point in enumerate(raw_points):
                self.points_xyz.extend(
                    _vector3(point, name=f"plane point {point_index}")
                )

            self.loop_point_offsets.append(len(self.points_xyz) // 3)
            self.loop_types.append(int(role))

        if outer_count != 1:
            raise ValueError("planeにはOUTERループが1つである必要があります")

        self.plane_loop_offsets.append(self.loop_count)
        return plane_index

    def get(self, index: int) -> PlaneShape:
        if not 0 <= index < self.plane_count:
            raise IndexError(index)

        loop_start: int = self.plane_loop_offsets[index]
        loop_end: int = self.plane_loop_offsets[index + 1]
        loops: list[PlaneLoop] = []

        for loop_index in range(loop_start, loop_end):
            point_start: int = self.loop_point_offsets[loop_index]
            point_end: int = self.loop_point_offsets[loop_index + 1]
            points: list[Vector3d] = []
            for point_index in range(point_start, point_end):
                offset = point_index * 3
                points.append(
                    Vector3d(
                        float(self.points_xyz[offset]),
                        float(self.points_xyz[offset + 1]),
                        float(self.points_xyz[offset + 2]),
                    )
                )
            loops.append(
                PlaneLoop(
                    role=SurfaceLoopType(self.loop_types[loop_index]),
                    points=tuple(points),
                )
            )

        return PlaneShape(loops=tuple(loops))

    def validate(self) -> None:
        if len(self.points_xyz) % 3 != 0:
            raise ValueError("plane points_xyzの長さは3の倍数である必要があります")
        if not self.loop_point_offsets or self.loop_point_offsets[0] != 0:
            raise ValueError("plane loop_point_offsetsは0で開始する必要があります")
        if not self.plane_loop_offsets or self.plane_loop_offsets[0] != 0:
            raise ValueError("plane plane_loop_offsetsは0で開始する必要があります")
        if self.loop_point_offsets[-1] != len(self.points_xyz) // 3:
            raise ValueError("最後のloop point offsetは点数と一致する必要があります")
        if self.plane_loop_offsets[-1] != self.loop_count:
            raise ValueError(
                "最後のplane loop offsetはループ数と一致する必要があります"
            )
        if len(self.loop_types) != self.loop_count:
            raise ValueError("plane loop type数はループ数と一致する必要があります")

        for loop_index in range(self.loop_count):
            start: int = self.loop_point_offsets[loop_index]
            end: int = self.loop_point_offsets[loop_index + 1]
            if end < start or end - start < 3:
                raise ValueError(f"plane loop {loop_index}には少なくとも3点が必要です")
            SurfaceLoopType(self.loop_types[loop_index])

        for plane_index in range(self.plane_count):
            plane_start: int = self.plane_loop_offsets[plane_index]
            plane_end: int = self.plane_loop_offsets[plane_index + 1]
            if plane_end <= plane_start:
                raise ValueError(
                    f"plane {plane_index}には少なくとも1つのループが必要です"
                )
            outer_count: int = sum(
                self.loop_types[loop_index] == SurfaceLoopType.OUTER
                for loop_index in range(plane_start, plane_end)
            )
            if outer_count != 1:
                raise ValueError(
                    f"plane {plane_index}にはouter loopが1つである必要があります"
                )


@dataclass(frozen=True, slots=True)
class Node:
    position: Vector3d
    source_id: str
    guid: UUID | None
    story_index: int | None
    xpath: str | None


@dataclass(slots=True)
class NodeTable:
    positions_xyz: array[float] = field(default_factory=_new_f64_array, repr=False)
    source_id: list[str] = field(default_factory=list, repr=False)
    guid: OptionalUuidColumn = field(default_factory=OptionalUuidColumn)
    story_index: array[int] = field(default_factory=_new_u32_array, repr=False)
    xpath: list[str | None] = field(default_factory=list, repr=False)

    def __len__(self) -> int:
        return len(self.source_id)

    def add(
        self,
        position: Sequence[float],
        *,
        source_id: str,
        guid: UUID | str | None = None,
        story_index: int | None = None,
        xpath: str | None = None,
    ) -> int:
        index: int = len(self)
        self.positions_xyz.extend(_vector3(position, name="node position"))
        self.source_id.append(source_id)
        self.guid.append(guid)
        # u32列ではNone直接保持できないため、UINT32_NONEとして持たせる。
        self.story_index.append(
            UINT32_NONE if story_index is None else int(story_index)
        )
        self.xpath.append(xpath)
        return index

    def get(self, index: int) -> Node:
        if not 0 <= index < len(self):
            raise IndexError(index)
        offset: int = index * 3
        raw_story: int = self.story_index[index]
        return Node(
            position=Vector3d(
                float(self.positions_xyz[offset]),
                float(self.positions_xyz[offset + 1]),
                float(self.positions_xyz[offset + 2]),
            ),
            source_id=self.source_id[index],
            guid=self.guid.get(index),
            story_index=None if raw_story == UINT32_NONE else int(raw_story),
            xpath=self.xpath[index],
        )

    def validate(self, story_count: int) -> None:
        count: int = len(self)
        if len(self.positions_xyz) != count * 3:
            raise ValueError("node positionsの長さはnode数 * 3と一致する必要があります")
        self.guid.validate(count)
        if len(self.story_index) != count:
            raise ValueError("node story_index数はnode数と一致する必要があります")
        if len(self.xpath) != count:
            raise ValueError("node xpath数はnode数と一致する必要があります")
        for index in self.story_index:
            if index != UINT32_NONE and index >= story_count:
                raise ValueError(f"node story index {index} は範囲外です")


@dataclass(frozen=True, slots=True)
class Story:
    source_id: str
    name: str | None
    elevation: float


@dataclass(slots=True)
class StoryTable:
    source_id: list[str] = field(default_factory=list, repr=False)
    name: list[str | None] = field(default_factory=list, repr=False)
    elevations: array[float] = field(default_factory=_new_f64_array, repr=False)

    def __len__(self) -> int:
        return len(self.source_id)

    def add(
        self,
        *,
        source_id: str,
        elevation: float,
        name: str | None = None,
    ) -> int:
        elevation_value: float = float(elevation)
        if not isfinite(elevation_value):
            raise ValueError("story elevationは有限値である必要があります")
        index: int = len(self)
        self.source_id.append(source_id)
        self.name.append(name)
        self.elevations.append(elevation_value)
        return index

    def get(self, index: int) -> Story:
        if not 0 <= index < len(self):
            raise IndexError(index)
        return Story(
            source_id=self.source_id[index],
            name=self.name[index],
            elevation=float(self.elevations[index]),
        )

    def validate(self) -> None:
        count: int = len(self)
        if len(self.name) != count or len(self.elevations) != count:
            raise ValueError("storyの各列は同じ長さである必要があります")


@dataclass(frozen=True, slots=True)
class Axis:
    source_id: str
    name: str | None
    points: tuple[Vector3d, ...]


@dataclass(slots=True)
class AxisTable:
    points_xyz: array[float] = field(default_factory=_new_f64_array, repr=False)
    """全通り芯の点をx, y, zで連続格納する。"""
    point_start: array[int] = field(default_factory=_new_u32_array, repr=False)
    """各通り芯がpoints_xyz中で使用する点単位の開始位置。"""
    point_count: array[int] = field(default_factory=_new_u32_array, repr=False)
    """各通り芯がpoints_xyz中で使用する点単位の長さ。"""
    source_id: list[str] = field(default_factory=list, repr=False)
    name: list[str | None] = field(default_factory=list, repr=False)

    def __len__(self) -> int:
        return len(self.source_id)

    def add(
        self,
        points: Sequence[Sequence[float]],
        *,
        source_id: str,
        name: str | None = None,
    ) -> int:
        if len(points) < 2:
            raise ValueError("axisには少なくとも2点が必要です")
        index: int = len(self)
        start: int = len(self.points_xyz) // 3
        for point_index, point in enumerate(points):
            self.points_xyz.extend(_vector3(point, name=f"axis point {point_index}"))
        self.point_start.append(start)
        self.point_count.append(len(points))
        self.source_id.append(source_id)
        self.name.append(name)
        return index

    def get(self, index: int) -> Axis:
        if not 0 <= index < len(self):
            raise IndexError(index)
        start: int = self.point_start[index]
        end: int = start + self.point_count[index]
        points: list[Vector3d] = []
        for point_index in range(start, end):
            offset: int = point_index * 3
            points.append(
                Vector3d(
                    float(self.points_xyz[offset]),
                    float(self.points_xyz[offset + 1]),
                    float(self.points_xyz[offset + 2]),
                )
            )
        return Axis(
            source_id=self.source_id[index],
            name=self.name[index],
            points=tuple(points),
        )

    def validate(self) -> None:
        count: int = len(self)
        if len(self.points_xyz) % 3 != 0:
            raise ValueError("axis pointsの長さは3の倍数である必要があります")
        if not (
            len(self.point_start) == len(self.point_count) == len(self.name) == count
        ):
            raise ValueError("axisの各列は同じ長さである必要があります")
        total_points: int = len(self.points_xyz) // 3
        for axis_index in range(count):
            start: int = self.point_start[axis_index]
            point_count: int = self.point_count[axis_index]
            if point_count < 2 or start + point_count > total_points:
                raise ValueError(f"axis {axis_index} の点範囲が不正です")


@dataclass(slots=True)
class ElementTable:
    kind: array[int] = field(default_factory=_new_u32_array, repr=False)
    flags: array[int] = field(default_factory=_new_u32_array, repr=False)

    # PolygonMesh中でこの要素が占有する頂点・面の連続範囲。
    # メッシュ未設定時はstartをUINT32_NONE、countを0とする。
    vertex_start: array[int] = field(default_factory=_new_u32_array, repr=False)
    vertex_count: array[int] = field(default_factory=_new_u32_array, repr=False)
    face_start: array[int] = field(default_factory=_new_u32_array, repr=False)
    face_count: array[int] = field(default_factory=_new_u32_array, repr=False)

    # 軸・面テーブルの参照。存在しなければUINT32_NONE。
    line_shape_index: array[int] = field(default_factory=_new_u32_array, repr=False)
    plane_shape_index: array[int] = field(default_factory=_new_u32_array, repr=False)

    # BuildingGeometry.element_node_indices / element_story_indices中の可変長範囲。
    node_start: array[int] = field(default_factory=_new_u32_array, repr=False)
    node_count: array[int] = field(default_factory=_new_u32_array, repr=False)
    story_start: array[int] = field(default_factory=_new_u32_array, repr=False)
    story_count: array[int] = field(default_factory=_new_u32_array, repr=False)

    guid: OptionalUuidColumn = field(default_factory=OptionalUuidColumn)
    xpath: list[str | None] = field(default_factory=list, repr=False)
    name: list[str | None] = field(default_factory=list, repr=False)
    source_type: list[str] = field(default_factory=list, repr=False)
    source_id: list[str | None] = field(default_factory=list, repr=False)

    def __len__(self) -> int:
        return len(self.kind)

    def add(
        self,
        *,
        kind: ElementKind | int,
        guid: UUID | str | None,
        xpath: str | None,
        source_type: str,
        source_id: str | None = None,
        name: str | None = None,
        flags: ElementFlags = ElementFlags.NONE,
    ) -> int:
        # flagsはメッシュや関連の有無から導けない属性だけを渡す。
        # HAS_*は対応するデータを追加するメソッドがORするため、ここで渡してはいけない。

        index: int = len(self)
        self.kind.append(int(ElementKind(kind)))
        self.flags.append(int(ElementFlags(flags)))

        # メッシュや関連は後から追加するため、最初は未設定で初期化する。
        self.vertex_start.append(UINT32_NONE)
        self.vertex_count.append(0)
        self.face_start.append(UINT32_NONE)
        self.face_count.append(0)

        self.line_shape_index.append(UINT32_NONE)
        self.plane_shape_index.append(UINT32_NONE)
        self.node_start.append(UINT32_NONE)
        self.node_count.append(0)
        self.story_start.append(UINT32_NONE)
        self.story_count.append(0)

        self.guid.append(guid)
        self.xpath.append(xpath)
        self.name.append(name)
        self.source_type.append(source_type)
        self.source_id.append(source_id)
        return index

    def mesh_range(self, element_index: int) -> MeshRange | None:
        if not 0 <= element_index < len(self):
            raise IndexError(element_index)
        vertex_start: int = self.vertex_start[element_index]
        if vertex_start == UINT32_NONE:
            return None
        return MeshRange(
            vertex_start=int(vertex_start),
            vertex_count=int(self.vertex_count[element_index]),
            face_start=int(self.face_start[element_index]),
            face_count=int(self.face_count[element_index]),
        )

    def validate(self) -> None:
        count: int = len(self)
        columns: dict[str, Sized] = {
            "flags": self.flags,
            "vertex_start": self.vertex_start,
            "vertex_count": self.vertex_count,
            "face_start": self.face_start,
            "face_count": self.face_count,
            "line_shape_index": self.line_shape_index,
            "plane_shape_index": self.plane_shape_index,
            "node_start": self.node_start,
            "node_count": self.node_count,
            "story_start": self.story_start,
            "story_count": self.story_count,
            "xpath": self.xpath,
            "name": self.name,
            "source_type": self.source_type,
            "source_id": self.source_id,
        }
        for name, column in columns.items():
            if len(column) != count:
                raise ValueError(
                    f"element列 {name!r} の長さは {count} である必要があります: "
                    f"actual={len(column)}"
                )
        self.guid.validate(count)
        for value in self.kind:
            ElementKind(value)


@dataclass(slots=True)
class BuildingGeometry:
    """ST-Bridge 3D描画中間データ。

    長さの単位はm。ST-Bridgeの長さ単位はmmであるので注意。

    構築中は各add_*/set_*メソッドで追記し、完成後にfreeze()を呼び出す。
    凍結時に全参照を検証し、その後のPyO3転送やmemoryviewによるゼロコピー参照問題が生じないようにする。
    """

    origin_xyz: Vector3d = field(default_factory=Vector3d)
    """原点"""
    mesh: PolygonMesh = field(default_factory=PolygonMesh)
    elements: ElementTable = field(default_factory=ElementTable)
    line_shapes: LineShapeTable = field(default_factory=LineShapeTable)
    plane_shapes: PlaneShapeTable = field(default_factory=PlaneShapeTable)
    nodes: NodeTable = field(default_factory=NodeTable)
    stories: StoryTable = field(default_factory=StoryTable)
    axes: AxisTable = field(default_factory=AxisTable)
    element_node_indices: array[int] = field(
        default_factory=_new_u32_array,
        repr=False,
    )
    element_story_indices: array[int] = field(
        default_factory=_new_u32_array,
        repr=False,
    )
    _frozen: bool = field(default=False, init=False, repr=False)

    def __post_init__(self) -> None:
        self.origin_xyz = _vector3(self.origin_xyz, name="origin_xyz")

    @property
    def frozen(self) -> bool:
        return self._frozen

    def _ensure_mutable(self) -> None:
        if self._frozen:
            raise RuntimeError("BuildingGeometryは凍結済みです")

    def _check_element_index(self, element_index: int) -> None:
        if not 0 <= element_index < len(self.elements):
            raise IndexError(element_index)

    def add_element(
        self,
        *,
        guid: UUID | str | None = None,
        xpath: str | None = None,
        source_type: str = "",
        kind: ElementKind | int = ElementKind.OTHER,
        source_id: str | None = None,
        name: str | None = None,
        flags: ElementFlags = ElementFlags.NONE,
    ) -> int:
        """ST-Bridge要素の行を追加し、indexを返す。

        この時点ではメッシュや節点関連を持たなくてもよい。
        返されたindexをadd_element_meshやset_element_nodesへ渡して情報を追加する。

        flagsにはSRC断面の部位のように、他の列から導けない属性だけを渡す。
        """

        self._ensure_mutable()
        return self.elements.add(
            kind=kind,
            guid=guid,
            xpath=xpath,
            source_type=source_type,
            source_id=source_id,
            name=name,
            flags=flags,
        )

    def add_story(
        self,
        *,
        source_id: str,
        elevation: float,
        name: str | None = None,
    ) -> int:
        self._ensure_mutable()
        return self.stories.add(
            source_id=source_id,
            elevation=elevation,
            name=name,
        )

    def add_node(
        self,
        position: Sequence[float],
        *,
        source_id: str,
        guid: UUID | str | None = None,
        story_index: int | None = None,
        xpath: str | None = None,
    ) -> int:
        self._ensure_mutable()
        if story_index is not None and not 0 <= story_index < len(self.stories):
            raise IndexError(f"story_indexが範囲外です: {story_index}")
        return self.nodes.add(
            position,
            source_id=source_id,
            guid=guid,
            story_index=story_index,
            xpath=xpath,
        )

    def add_axis(
        self,
        points: Sequence[Sequence[float]],
        *,
        source_id: str,
        name: str | None = None,
    ) -> int:
        self._ensure_mutable()
        return self.axes.add(points, source_id=source_id, name=name)

    def add_element_mesh(
        self,
        element_index: int,
        vertices: Iterable[Sequence[float]],
        faces: Iterable[Sequence[int]],
    ) -> MeshRange:
        """要素単位の頂点と面を追加する。

        verticesとfacesは通常のタプルやリストで渡せる簡易版API。
        """

        positions: array[float] = array("f")
        for vertex_index, vertex in enumerate(vertices):
            positions.extend(_vector3(vertex, name=f"vertex {vertex_index}"))

        face_vertex_indices: array[int] = array("I")
        face_offsets: array[int] = array("I", [0])
        for face_index, face in enumerate(faces):
            face_values: tuple[int, ...] = tuple(int(index) for index in face)
            if len(face_values) < 3:
                raise ValueError(
                    f"face {face_index} には少なくとも3つのindexが必要です"
                )
            if any(index < 0 for index in face_values):
                raise ValueError(f"face {face_index} に負のindexが含まれています")
            face_vertex_indices.extend(face_values)
            face_offsets.append(len(face_vertex_indices))

        return self.add_element_mesh_flat(
            element_index,
            positions,
            face_vertex_indices,
            face_offsets,
        )

    def add_element_mesh_flat(
        self,
        element_index: int,
        positions: array[float],
        local_face_vertex_indices: array[int],
        local_face_offsets: array[int],
    ) -> MeshRange:
        """配列から要素メッシュを追加する。

        入力頂点番号は要素の先頭頂点を0とする。
        追加時に全体頂点配列の開始番号を加え、モデル全体に対する絶対頂点番号へ変換する。
        """

        self._ensure_mutable()
        self._check_element_index(element_index)

        if self.elements.vertex_start[element_index] != UINT32_NONE:
            raise ValueError(f"element {element_index} には既にmeshが設定されています")
        if positions.typecode != "f":
            raise TypeError("positionsはarray('f')である必要があります")
        if local_face_vertex_indices.typecode != "I":
            raise TypeError("local_face_vertex_indicesはarray('I')である必要があります")
        if local_face_offsets.typecode != "I":
            raise TypeError("local_face_offsetsはarray('I')である必要があります")
        if len(positions) % 3 != 0:
            raise ValueError("positionsの長さは3の倍数である必要があります")
        if not local_face_offsets or local_face_offsets[0] != 0:
            raise ValueError("local_face_offsetsは0で開始する必要があります")
        if local_face_offsets[-1] != len(local_face_vertex_indices):
            raise ValueError(
                "最後のlocal face offsetはlocal face index数と一致する必要があります"
            )

        local_vertex_count: int = len(positions) // 3
        local_face_count: int = len(local_face_offsets) - 1
        if local_vertex_count == 0 or local_face_count == 0:
            raise ValueError("element meshには頂点と面の両方が必要です")

        for face_index in range(local_face_count):
            start: int = local_face_offsets[face_index]
            end: int = local_face_offsets[face_index + 1]
            if end < start or end - start < 3:
                raise ValueError(
                    f"face {face_index} には少なくとも3つのindexが必要です"
                )

        for index in local_face_vertex_indices:
            if index >= local_vertex_count:
                raise ValueError(
                    f"local vertex index {index} は "
                    f"{local_vertex_count} 頂点の範囲外です"
                )

        vertex_start: int = self.mesh.vertex_count
        face_start: int = self.mesh.face_count
        index_base: int = len(self.mesh.face_vertex_indices)

        self.mesh.positions.extend(positions)
        self.mesh.face_vertex_indices.extend(
            vertex_start + index for index in local_face_vertex_indices
        )

        self.mesh.face_offsets.extend(
            index_base + offset for offset in local_face_offsets[1:]
        )

        self.elements.vertex_start[element_index] = vertex_start
        self.elements.vertex_count[element_index] = local_vertex_count
        self.elements.face_start[element_index] = face_start
        self.elements.face_count[element_index] = local_face_count
        self.elements.flags[element_index] |= int(ElementFlags.HAS_MESH)

        return MeshRange(
            vertex_start=vertex_start,
            vertex_count=local_vertex_count,
            face_start=face_start,
            face_count=local_face_count,
        )

    def set_element_nodes(
        self,
        element_index: int,
        node_indices: Iterable[int],
    ) -> None:

        self._ensure_mutable()
        self._check_element_index(element_index)
        if self.elements.node_start[element_index] != UINT32_NONE:
            raise ValueError(f"element {element_index} のnodesは既に設定済みです")

        values: tuple[int, ...] = tuple(int(index) for index in node_indices)
        for index in values:
            if not 0 <= index < len(self.nodes):
                raise IndexError(f"node indexが範囲外です: {index}")

        self.elements.node_start[element_index] = len(self.element_node_indices)
        self.elements.node_count[element_index] = len(values)
        self.element_node_indices.extend(values)
        self.elements.flags[element_index] |= int(ElementFlags.HAS_NODE_RELATION)

    def get_element_node_indices(self, element_index: int) -> tuple[int, ...]:
        self._check_element_index(element_index)
        start: int = self.elements.node_start[element_index]
        if start == UINT32_NONE:
            return ()
        count: int = self.elements.node_count[element_index]
        return tuple(
            int(value) for value in self.element_node_indices[start : start + count]
        )

    def set_element_stories(
        self,
        element_index: int,
        story_indices: Iterable[int],
    ) -> None:

        self._ensure_mutable()
        self._check_element_index(element_index)
        if self.elements.story_start[element_index] != UINT32_NONE:
            raise ValueError(f"element {element_index} のlevelsは既に設定済みです")

        values: tuple[int, ...] = tuple(int(index) for index in story_indices)
        for index in values:
            if not 0 <= index < len(self.stories):
                raise IndexError(f"story indexが範囲外です: {index}")

        self.elements.story_start[element_index] = len(self.element_story_indices)
        self.elements.story_count[element_index] = len(values)
        self.element_story_indices.extend(values)
        self.elements.flags[element_index] |= int(ElementFlags.HAS_STORY_RELATION)

    def add_element_line_shape(
        self,
        element_index: int,
        *,
        start: Sequence[float],
        end: Sequence[float],
        reference_y: Sequence[float] | None = None,
    ) -> int:

        self._ensure_mutable()
        self._check_element_index(element_index)
        if self.elements.line_shape_index[element_index] != UINT32_NONE:
            raise ValueError(
                f"element {element_index} には既にline shapeが設定されています"
            )

        shape_index: int = self.line_shapes.add(start, end, reference_y)
        self.elements.line_shape_index[element_index] = shape_index
        self.elements.flags[element_index] |= int(ElementFlags.HAS_LINE_SHAPE)
        return shape_index

    def get_element_line_shape(self, element_index: int) -> LineShape | None:

        self._check_element_index(element_index)
        shape_index: int = self.elements.line_shape_index[element_index]
        if shape_index == UINT32_NONE:
            return None
        return self.line_shapes.get(shape_index)

    def add_element_plane_shape(
        self,
        element_index: int,
        loops: Sequence[tuple[SurfaceLoopType | int, Sequence[Sequence[float]]]],
    ) -> int:

        self._ensure_mutable()
        self._check_element_index(element_index)
        if self.elements.plane_shape_index[element_index] != UINT32_NONE:
            raise ValueError(
                f"element {element_index} には既にplane shapeが設定されています"
            )

        shape_index: int = self.plane_shapes.add(loops)
        self.elements.plane_shape_index[element_index] = shape_index
        self.elements.flags[element_index] |= int(ElementFlags.HAS_PLANE_SHAPE)
        return shape_index

    def get_element_plane_shape(
        self,
        element_index: int,
    ) -> PlaneShape | None:

        self._check_element_index(element_index)
        shape_index: int = self.elements.plane_shape_index[element_index]
        if shape_index == UINT32_NONE:
            return None
        return self.plane_shapes.get(shape_index)

    def validate(self) -> None:
        self.mesh.validate()
        self.elements.validate()
        self.line_shapes.validate()
        self.plane_shapes.validate()
        self.stories.validate()
        self.nodes.validate(len(self.stories))
        self.axes.validate()

        vertex_count: int = self.mesh.vertex_count
        face_count: int = self.mesh.face_count

        for element_index in range(len(self.elements)):
            span: MeshRange | None = self.elements.mesh_range(element_index)
            flags: ElementFlags = ElementFlags(self.elements.flags[element_index])

            composite_part: ElementFlags = flags & (
                ElementFlags.IS_COMPOSITE_CONCRETE | ElementFlags.IS_COMPOSITE_STEEL
            )
            if composite_part == (
                ElementFlags.IS_COMPOSITE_CONCRETE | ElementFlags.IS_COMPOSITE_STEEL
            ):
                raise ValueError(f"element {element_index} はconcreteとsteelの両方です")

            if span is None:
                if flags & ElementFlags.HAS_MESH:
                    raise ValueError(
                        f"element {element_index} はHAS_MESHですがmesh spanがありません"
                    )
            else:
                if not flags & ElementFlags.HAS_MESH:
                    raise ValueError(
                        f"element {element_index} はmesh spanがありますが"
                        "HAS_MESHではありません"
                    )
                if span.vertex_start + span.vertex_count > vertex_count:
                    raise ValueError(
                        f"element {element_index} のvertex spanは範囲外です"
                    )
                if span.face_start + span.face_count > face_count:
                    raise ValueError(f"element {element_index} のface spanは範囲外です")

                face_end: int = span.face_start + span.face_count
                vertex_end: int = span.vertex_start + span.vertex_count
                for face_index in range(span.face_start, face_end):
                    start: int = self.mesh.face_offsets[face_index]
                    end: int = self.mesh.face_offsets[face_index + 1]
                    for vertex_index in self.mesh.face_vertex_indices[start:end]:
                        if not span.vertex_start <= vertex_index < vertex_end:
                            raise ValueError(
                                f"element {element_index} face {face_index} "
                                "が他のelementの頂点を参照しています"
                            )

            line_index: int = self.elements.line_shape_index[element_index]
            if line_index != UINT32_NONE and line_index >= len(self.line_shapes):
                raise ValueError(
                    f"element {element_index} のline shape indexは範囲外です"
                )
            plane_index: int = self.elements.plane_shape_index[element_index]
            if (
                plane_index != UINT32_NONE
                and plane_index >= self.plane_shapes.plane_count
            ):
                raise ValueError(
                    f"element {element_index} のplane shape indexは範囲外です"
                )

            node_start: int = self.elements.node_start[element_index]
            node_count: int = self.elements.node_count[element_index]
            if node_start != UINT32_NONE:
                if node_start + node_count > len(self.element_node_indices):
                    raise ValueError(f"element {element_index} のnode関連は範囲外です")
                for node_index in self.element_node_indices[
                    node_start : node_start + node_count
                ]:
                    if node_index >= len(self.nodes):
                        raise ValueError(
                            f"element {element_index} のnode indexは範囲外です"
                        )

            story_start: int = self.elements.story_start[element_index]
            story_count: int = self.elements.story_count[element_index]
            if story_start != UINT32_NONE:
                if story_start + story_count > len(self.element_story_indices):
                    raise ValueError(f"element {element_index} のstory関連は範囲外です")
                for story_index in self.element_story_indices[
                    story_start : story_start + story_count
                ]:
                    if story_index >= len(self.stories):
                        raise ValueError(
                            f"element {element_index} のstory indexは範囲外です"
                        )

    def freeze(self) -> None:
        """全体をチェックし、Rust転送やmemoryview参照を行える状態にする。

        凍結後は追加系メソッドがRuntimeErrorをなげる。
        PyO3転送はRust所有のVecへコピーするため凍結後もPythonオブジェクトを保持し続ける必要はない。
        """
        if self._frozen:
            return
        self.validate()
        self._frozen = True
