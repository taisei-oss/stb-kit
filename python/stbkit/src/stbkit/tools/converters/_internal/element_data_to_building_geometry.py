# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid
from collections.abc import Sequence
from dataclasses import dataclass, field
from uuid import UUID

from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.tools._internal.vectors import Vector2d, Vector3d

from ..._internal.data_model.building_geometry import (
    BuildingGeometry,
    ElementFlags,
    ElementKind,
    SurfaceLoopType,
)
from ..._internal.data_model.element_data import (
    ElementData,
    ElementLine,
    ElementLineSrc,
    ElementPlane,
    ElementType,
    Node,
)
from ..._internal.data_model.shape_data import Shape, ShapePair, ShapePosition
from ..._internal.utils.mesh_utils import create_mesh
from .coord_converter import (
    axis_vector_plate,
    to_global_coord,
    to_global_coord_plate,
    to_plate_element_coord,
)


@dataclass
class _LocalMesh:
    vertices: list[Vector3d] = field(default_factory=list)
    faces: list[Sequence[int]] = field(default_factory=list)

    def add_vertices_and_faces(
        self, vertices: Sequence[Vector3d], faces: Sequence[Sequence[int]]
    ) -> None:
        offset: int = len(self.vertices)
        self.vertices.extend(vertices)
        for face in faces:
            self.faces.append([f + offset for f in face])


def create_local_line_meshes(
    shapes: Sequence[ShapePair],
    axis_position: ShapePosition,
    lengths: Sequence[float],
) -> list[_LocalMesh]:
    if not shapes:
        raise AssertionError("形状が設定されていません")
    if len(shapes) != len(lengths):
        raise AssertionError("形状と長さの数が異なります")

    meshes: list[_LocalMesh] = []
    start_length = 0.0
    for shape, length in zip(shapes, lengths, strict=True):
        shape_end: Shape = shape.end if shape.end else shape.start
        start_point2ds: list[Vector2d] = (
            shape.start.get_out_point2ds_with_rotate_and_offset()
        )
        end_point2ds: list[Vector2d] = (
            shape_end.get_out_point2ds_with_rotate_and_offset()
        )
        start_in_point2ds: list[Vector2d] | None = (
            shape.start.get_in_point2ds_with_rotate_and_offset()
        )
        end_in_point2ds: list[Vector2d] | None = (
            shape_end.get_in_point2ds_with_rotate_and_offset()
        )
        index_start: int = 0
        index_end: int = index_start + len(start_point2ds)
        if axis_position != ShapePosition.CENTER_CENTER:
            offset_start: Vector2d = shape.start.get_position_point(axis_position)
            start_point2ds = [point - offset_start for point in start_point2ds]
            offset_end: Vector2d = shape_end.get_position_point(axis_position)
            end_point2ds = [point - offset_end for point in end_point2ds]

        if len(start_point2ds) != len(end_point2ds):
            raise AssertionError("断面のStartとEndの頂点数が異なります")

        n: int = len(start_point2ds)
        vertices: list[Vector3d] = [
            point.to_vector3d(start_length) for point in start_point2ds
        ]
        vertices.extend(
            point.to_vector3d(start_length + length) for point in end_point2ds
        )
        faces: list[Sequence[int]] = []
        if (
            start_in_point2ds
            and end_in_point2ds
            and len(start_in_point2ds) == len(end_in_point2ds)
            and len(start_point2ds) == len(start_in_point2ds)
        ):
            vertices.extend(
                point.to_vector3d(start_length) for point in start_in_point2ds
            )
            vertices.extend(
                point.to_vector3d(start_length + length) for point in end_in_point2ds
            )
            index_in_start: int = index_end + len(end_point2ds)
            index_in_end: int = index_in_start + len(start_in_point2ds)
            for i in range(len(start_in_point2ds)):
                faces.append(
                    [
                        (i + 1) % n + index_in_start,
                        i + index_in_start,
                        i + index_in_end,
                        (i + 1) % n + index_in_end,
                    ]
                )
                faces.append(
                    [
                        i + index_start,
                        (i + 1) % n + index_start,
                        (i + 1) % n + index_in_start,
                        i + index_in_start,
                    ]
                )
                faces.append(
                    [
                        (i + 1) % n + index_end,
                        i + index_end,
                        i + index_in_end,
                        (i + 1) % n + index_in_end,
                    ]
                )
        else:
            faces.append(list(range(n)))
            faces.append(list(range(2 * n - 1, n - 1, -1)))

        for i in range(n):
            faces.append(
                [
                    i,
                    (i + 1) % n,
                    (i + 1) % n + n,
                    i + n,
                ]
            )

        meshes.append(_LocalMesh(vertices=vertices, faces=faces))
        start_length += length

    return meshes


def _triangulate_faces(mesh: _LocalMesh) -> _LocalMesh:
    result_vertices: list[Vector3d] = list(mesh.vertices)
    result_faces: list[Sequence[int]] = []

    for face in mesh.faces:
        match len(face):
            case 0 | 1 | 2:
                raise ValueError("頂点数が3未満の面は三角形分割できません")
            case 3:
                result_faces.append(list(face))
            case _:
                face_vertices: list[Vector3d] = [mesh.vertices[index] for index in face]
                face_vertices_element: list[Vector2d] = [
                    Vector2d(v.x, v.y) for v in to_plate_element_coord(face_vertices)
                ]
                _, new_faces, _, _ = create_mesh(face_vertices_element)
                result_faces.extend(new_faces)
    return _LocalMesh(vertices=result_vertices, faces=result_faces)


def element_line_to_element_mesh(
    element: ElementLine, *, allow_polygons: bool, reporter: Reporter
) -> _LocalMesh | None:
    if not element.shapes or not element.point_start or not element.point_end:
        reporter.error(
            "形状が設定されていません",
            code=Code.UNKNOWN_SHAPE,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return None
    if not element.element_type:
        reporter.error(
            "要素タイプが設定されていません",
            code=Code.UNKNOWN_SHAPE,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return None
    if len(element.shapes) != len(element.lengths):
        reporter.error(
            "形状と長さの数が異なります",
            code=Code.UNKNOWN_SHAPE,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return None
    local_meshes: list[_LocalMesh] = create_local_line_meshes(
        element.shapes,
        element.axis_position,
        element.lengths,
    )
    mesh: _LocalMesh = _LocalMesh()
    for local_mesh in local_meshes:
        global_vertices: list[Vector3d] = to_global_coord(
            local_mesh.vertices,
            element.point_start,
            element.point_end,
            element.angle,
            element.element_type,
        )
        mesh.add_vertices_and_faces(
            [point.mm_to_m() for point in global_vertices],
            local_mesh.faces,
        )
    if allow_polygons:
        return mesh

    try:
        return _triangulate_faces(mesh)
    except ValueError as e:
        reporter.error(
            f"線要素の多角形の三角形分割に失敗しました: {e}",
            code=Code.UNEXPECTED_ERROR,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return None


def element_line_src_to_element_meshes(
    element: ElementLineSrc, *, allow_polygons: bool, reporter: Reporter
) -> tuple[_LocalMesh | None, _LocalMesh | None]:
    if element.rc is None or element.steel is None:
        reporter.error(
            "RCまたはS形状が設定されていません",
            code=Code.UNKNOWN_SHAPE,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return None, None
    mesh_rc: _LocalMesh | None = element_line_to_element_mesh(
        element.rc, allow_polygons=allow_polygons, reporter=reporter
    )
    mesh_s: _LocalMesh | None = element_line_to_element_mesh(
        element.steel, allow_polygons=allow_polygons, reporter=reporter
    )
    return mesh_rc, mesh_s


def element_plane_to_element_mesh(
    element: ElementPlane, *, allow_polygons: bool, reporter: Reporter
) -> _LocalMesh | None:
    if not element.points:
        raise AssertionError("要素の頂点が設定されていません")
    thickness: float = element.thickness if element.thickness else 10
    # 表面
    out_points2d: list[Vector2d] = [
        Vector2d(v.x, v.y) for v in to_plate_element_coord(element.points)
    ]
    in_points2d: list[list[Vector2d]] = element.opens or []
    try:
        vertices2d, faces, new_out_points, new_in_points = create_mesh(
            out_points2d, in_points2d
        )
    except ValueError as e:
        reporter.error(
            f"平面要素のメッシュ化に失敗しました: {e}",
            code=Code.UNEXPECTED_ERROR,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return None
    mesh: _LocalMesh = _LocalMesh()
    vertices3d: list[Vector3d] = to_global_coord_plate(
        [v.to_vector3d(z=thickness) for v in vertices2d], element.points
    )
    mesh.add_vertices_and_faces([v.mm_to_m() for v in vertices3d], faces)
    # 裏面
    faces_rev = [list(reversed(face)) for face in faces]
    vertices3d_back: list[Vector3d] = to_global_coord_plate(
        [v.to_vector3d(z=0.0) for v in vertices2d], element.points
    )
    mesh.add_vertices_and_faces(
        [v.mm_to_m() for v in vertices3d_back],
        faces_rev,
    )

    _vx, _vy, _vz = axis_vector_plate(element.points)

    # 側面
    side_faces: list[list[int]] = (
        [[0, 1, 2, 3]] if allow_polygons else [[0, 1, 2], [0, 2, 3]]
    )

    if new_out_points is not None:
        if len(new_out_points) == 1:
            out_points2d = new_out_points[0]
        else:
            raise NotImplementedError("未実装です")
    if new_in_points is not None:
        in_points2d = new_in_points
    # 側面内側
    for tmp_in_point2ds in in_points2d:
        tmp_in_point2ds = tmp_in_point2ds + [tmp_in_point2ds[0]]
        for i in range(len(tmp_in_point2ds) - 1):
            p0 = tmp_in_point2ds[i]
            p1 = tmp_in_point2ds[i + 1]
            p0_3d_top = to_global_coord_plate(
                [p0.to_vector3d(z=thickness)], element.points
            )[0]
            p1_3d_top = to_global_coord_plate(
                [p1.to_vector3d(z=thickness)], element.points
            )[0]
            p0_3d_bottom = to_global_coord_plate(
                [p0.to_vector3d(z=0.0)], element.points
            )[0]
            p1_3d_bottom = to_global_coord_plate(
                [p1.to_vector3d(z=0.0)], element.points
            )[0]
            mesh.add_vertices_and_faces(
                [
                    p0_3d_top.mm_to_m(),
                    p1_3d_top.mm_to_m(),
                    p1_3d_bottom.mm_to_m(),
                    p0_3d_bottom.mm_to_m(),
                ],
                side_faces,
            )
    # 側面外側
    out_points2d = out_points2d + [out_points2d[0]]
    for i in range(len(out_points2d) - 1):
        p0 = out_points2d[i]
        p1 = out_points2d[i + 1]
        p0_3d_top = to_global_coord_plate(
            [p0.to_vector3d(z=thickness)], element.points
        )[0]
        p1_3d_top = to_global_coord_plate(
            [p1.to_vector3d(z=thickness)], element.points
        )[0]
        p0_3d_bottom = to_global_coord_plate([p0.to_vector3d(z=0.0)], element.points)[0]
        p1_3d_bottom = to_global_coord_plate([p1.to_vector3d(z=0.0)], element.points)[0]
        mesh.add_vertices_and_faces(
            [
                p0_3d_top.mm_to_m(),
                p1_3d_top.mm_to_m(),
                p1_3d_bottom.mm_to_m(),
                p0_3d_bottom.mm_to_m(),
            ],
            side_faces,
        )

    return mesh


def _get_element_source_type(
    element: ElementLine | ElementLineSrc | ElementPlane,
) -> str:
    path: str | None = element.path
    if path:
        source_type = path.rsplit("/", 1)[-1].partition("[")[0]
        if source_type:
            return source_type

    element_type: ElementType | None = element.element_type
    return element_type.value if element_type is not None else ""


def _element_kind_from_type(element_type: ElementType | None) -> ElementKind:
    if element_type is None:
        return ElementKind.OTHER
    return ElementKind[element_type.name]


_OFFSET_AXIS_TYPES: frozenset[ElementType] = frozenset(
    {
        ElementType.PILE,
        ElementType.FOUNDATION_COLUMN,
        ElementType.FOOTING,
        ElementType.PARAPET,
    }
)
"""Line描画の際にoffsetを考慮しないと見えない部材
- 杭は基準節点が1つのため、1つの柱に複数の杭がある場合offsetで表現しないと
  重なって見えない
- 基礎柱、フーチングは基準節点が1つであり、点になってしまうため、
  offsetした位置で表現する
- パラペットは基本的に梁と節点がかぶるため、重なってしまうのでoffsetで表現する
"""


def _line_points(
    element: ElementLine | ElementLineSrc,
    node_infos: dict[int, Node],
) -> tuple[Vector3d, Vector3d] | None:
    node_ids: list[int] = element.node_ids
    if element.element_type not in _OFFSET_AXIS_TYPES and len(node_ids) == 2:
        node_start: Node | None = node_infos.get(node_ids[0])
        node_end: Node | None = node_infos.get(node_ids[1])
        if node_start is not None and node_end is not None:
            return node_start.position, node_end.position
    line: ElementLine | None = (
        element
        if isinstance(element, ElementLine)
        else (element.rc if element.rc is not None else element.steel)
    )
    if line is None or line.point_start is None or line.point_end is None:
        return None
    return line.point_start, line.point_end


def _plane_points(
    element: ElementPlane,
) -> list[tuple[SurfaceLoopType, list[Vector3d]]] | None:
    node_points: list[Vector3d] | None = element.node_points
    if node_points is None or len(node_points) < 3:
        return None

    loops: list[tuple[SurfaceLoopType, list[Vector3d]]] = [
        (SurfaceLoopType.OUTER, [point.mm_to_m() for point in node_points])
    ]
    for open_point2ds in element.opens:
        if len(open_point2ds) < 3:
            continue
        open_point3ds: list[Vector3d] = to_global_coord_plate(
            [point.to_vector3d(z=0.0) for point in open_point2ds],
            node_points,
        )
        loops.append(
            (SurfaceLoopType.HOLE, [point.mm_to_m() for point in open_point3ds])
        )
    return loops


def _add_element_info(
    geom: BuildingGeometry,
    element_index: int,
    element: ElementLine | ElementLineSrc | ElementPlane,
    node_infos: dict[int, Node],
    node_indices: dict[int, int],
) -> None:
    node_relation: list[int] = [
        node_indices[node_id] for node_id in element.node_ids if node_id in node_indices
    ]
    if node_relation:
        geom.set_element_nodes(element_index, node_relation)

    if isinstance(element, ElementPlane):
        loops = _plane_points(element)
        if loops is not None:
            geom.add_element_plane_shape(element_index, loops)
        return

    axis_points = _line_points(element, node_infos)
    if axis_points is not None:
        point_start, point_end = axis_points
        geom.add_element_line_shape(
            element_index,
            start=point_start.mm_to_m(),
            end=point_end.mm_to_m(),
        )


def element_data_to_building_geometry(
    elements: ElementData,
    *,
    allow_polygons: bool,
    reporter: Reporter,
    node_infos: dict[int, Node] | None = None,
) -> BuildingGeometry:

    geom: BuildingGeometry = BuildingGeometry()
    node_indices: dict[int, int] = {}
    if node_infos is not None:
        node_indices = {
            node_id: geom.add_node(
                node.position.mm_to_m(),
                source_id=str(node_id),
                guid=node.guid,
                xpath=node.xpath,
            )
            for node_id, node in node_infos.items()
        }

    for element in elements:
        path: str | None = element.path
        guid: UUID = element.guid if element.guid else uuid.uuid4()
        element_kind: ElementKind = _element_kind_from_type(element.element_type)

        source_type: str = _get_element_source_type(element)
        # SRCのクリック検出は外側のRCで行う。そのためRCを先に登録する。
        is_composite: bool = isinstance(element, ElementLineSrc)
        index: int = geom.add_element(
            kind=element_kind,
            guid=guid,
            xpath=path,
            name=element.name,
            source_type=source_type,
            flags=(
                ElementFlags.IS_COMPOSITE_CONCRETE
                if is_composite
                else ElementFlags.NONE
            ),
        )
        if node_infos is not None:
            _add_element_info(
                geom,
                index,
                element,
                node_infos,
                node_indices,
            )
        match element:
            case ElementLineSrc():
                mesh_rc, mesh_s = element_line_src_to_element_meshes(
                    element,
                    allow_polygons=allow_polygons,
                    reporter=reporter,
                )
                if mesh_rc:
                    geom.add_element_mesh(index, mesh_rc.vertices, mesh_rc.faces)
                if mesh_s:
                    # SはRCと同じGUID・XPathを持つ別要素とする。
                    # 節点関連はRCにのみ持たせて二重描画を防ぐ
                    steel_index: int = geom.add_element(
                        kind=element_kind,
                        guid=guid,
                        xpath=path,
                        name=element.name,
                        source_type=source_type,
                        flags=ElementFlags.IS_COMPOSITE_STEEL,
                    )
                    geom.add_element_mesh(steel_index, mesh_s.vertices, mesh_s.faces)
            case ElementLine():
                mesh: _LocalMesh | None = element_line_to_element_mesh(
                    element,
                    allow_polygons=allow_polygons,
                    reporter=reporter,
                )
                if mesh:
                    geom.add_element_mesh(index, mesh.vertices, mesh.faces)
            case ElementPlane():
                mesh = element_plane_to_element_mesh(
                    element,
                    allow_polygons=allow_polygons,
                    reporter=reporter,
                )
                if mesh:
                    geom.add_element_mesh(index, mesh.vertices, mesh.faces)
    return geom
