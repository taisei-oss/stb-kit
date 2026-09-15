# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import itertools
import math
import warnings
from dataclasses import dataclass

from ..vectors import Vector2d

__all__ = ["MeshTriangulationWarning", "create_mesh"]


class MeshTriangulationWarning(UserWarning):
    """開口を含んだ三角形分割に失敗し、開口を考慮しないことを示す警告。"""


class _TriangulationError(RuntimeError):
    """内部処理が継続できない場合に投げる例外。"""


@dataclass(frozen=True, slots=True)
class _Edge:
    """開口の辺"""

    a: Vector2d
    b: Vector2d
    ring_index: int
    edge_index: int

    def is_intersecting(self, y: float) -> bool:
        """水平線が辺とぶつかる場合にTrueを返す。"""
        return min(self.a.y, self.b.y) < y < max(self.a.y, self.b.y)

    def intersection_x(self, y: float, eps: float) -> float:
        """辺と水平線との交点X座標"""
        if abs(y - self.a.y) <= eps:
            return self.a.x
        if abs(y - self.b.y) <= eps:
            return self.b.x

        dy: float = self.b.y - self.a.y
        if abs(dy) <= eps:
            raise _TriangulationError("水平辺の交点X座標は計算不可")

        t: float = (y - self.a.y) / dy
        parameter_tolerance: float = eps / max(abs(dy), eps)
        if t < -parameter_tolerance or t > 1.0 + parameter_tolerance:
            raise _TriangulationError("交点が編の範囲外")

        t = min(1.0, max(0.0, t))
        return self.a.x + t * (self.b.x - self.a.x)


@dataclass(frozen=True, slots=True)
class _BandInterval:
    """水平帯中央の、左右の辺を持つX区間。"""

    left_edge: _Edge
    right_edge: _Edge
    left_x: float
    right_x: float


class _VertexPool:
    """許容誤差内の点を同じ頂点インデックスへまとめるクラス。"""

    def __init__(self, eps: float) -> None:
        self._eps: float = max(eps / 2.0, 1.0e-13)
        self.points: list[Vector2d] = []
        self._bins: dict[tuple[int, int], list[int]] = {}

    def add(self, point: Vector2d) -> int:
        """頂点を追加し、既存頂点と一致する場合は既存番号を返す。"""
        size: float = self._eps
        key: tuple[int, int] = (math.floor(point.x / size), math.floor(point.y / size))
        limit: float = size * size

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nearby = self._bins.get((key[0] + dx, key[1] + dy), ())
                for index in nearby:
                    if _distance_2(self.points[index], point) <= limit:
                        return index

        index = len(self.points)
        self.points.append(point)
        self._bins.setdefault(key, []).append(index)
        return index


def create_mesh(
    out_points: list[Vector2d],
    in_points: list[list[Vector2d]] | None = None,
    *,
    merge_tolerance: float | None = None,
) -> tuple[
    list[Vector2d],
    list[tuple[int, int, int]],
    list[list[Vector2d]] | None,
    list[list[Vector2d]] | None,
]:
    """開口付きの形状を三角形分割する。

    外形と各開口を水平帯に分割し、帯ごとに集合演算を行う。

    外形のX区間 - 全開口X区間の和集合

    開口が外形からはみ出す場合、外形内部にある部分のみ差し引く。
    外形に接触する開口は切り欠きとなり、重なる複数開口は一つの開口領域として処理する。

    今回の分割用途は描画用でありFEMモデル作成用ではないため、メッシュ品質にはこだわらない。
    処理も効率的なものではないが、今回対象としているものは断面の多角形や
    床や壁の開口など、頂点数は多くても2桁のオーダーであるため、そこまでの負荷にはならなと考える。

    Args:
        out_points: 外形
        in_points: 開口の一覧
        merge_tolerance: 同じ頂点として扱う許容誤差。
            連続する近接点の除去、頂点の共有、接触判定に使用する。
            省略時は、外形の幅と高さの大きい方x1e-10。

    Returns:
        次の4要素のtupleを返す。

        vertices: 分割した頂点。
        faces: 分割した三角形の頂点インデックス一覧。
        new_out_points:
            開口が外形へ統合されるなどが生じて、外形が変化した場合の外形。
            変化がなければNone。
            開口が外形を横断して領域が分断された場合は、複数返す。
            外形全体が開口で除去された場合は空リスト[]。
        new_in_points:
            クリップ、結合、外形への統合、完全な外側開口の除外などにより
            開口が変化した場合の新しい開口一覧。
            変化がなければNone。
            開口が残らない場合は空リスト[]。

    警告:
        MeshTriangulationWarning: 開口処理に失敗した場合に投げる。
            開口を無視し、外形だけを分割する。この場合new_in_pointsは空リスト[]になる。

    Raises:
        ValueError:
            外形だけの分割にも失敗した場合、またはmerge_toleranceがおかしい場合に投げる
    """
    try:
        return _run(out_points, in_points or [], merge_tolerance)
    except _TriangulationError as error:
        if not in_points:
            raise ValueError(f"外形の三角形分割に失敗しました: {error}") from error

        warnings.warn(
            "開口を含む三角形分割に失敗したため、開口を無視して外形のみ分割します。"
            f" {error}",
            MeshTriangulationWarning,
            stacklevel=2,
        )

    try:
        vertices, faces, new_outer, _ = _run(
            out_points,
            [],
            merge_tolerance,
        )
    except _TriangulationError as error:
        raise ValueError(f"外形の三角形分割も失敗しました: {error}") from error

    # 入力された開口除外されたため、[]を返して変更を明示。
    return vertices, faces, new_outer, []


def _run(
    out_points: list[Vector2d],
    in_points: list[list[Vector2d]],
    merge_tolerance: float | None,
) -> tuple[
    list[Vector2d],
    list[tuple[int, int, int]],
    list[list[Vector2d]] | None,
    list[list[Vector2d]] | None,
]:
    if len(out_points) < 3:
        raise _TriangulationError("外形の頂点数が3点未満です")

    min_x: float = min(point.x for point in out_points)
    max_x: float = max(point.x for point in out_points)
    min_y: float = min(point.y for point in out_points)
    max_y: float = max(point.y for point in out_points)
    scale: float = max(max_x - min_x, max_y - min_y)
    if scale <= 0.0 or not math.isfinite(scale):
        raise _TriangulationError("外形の大きさが0です")

    center_x: float = (min_x + max_x) / 2.0
    center_y: float = (min_y + max_y) / 2.0

    if merge_tolerance is None:
        eps: float = 1.0e-10
    else:
        if merge_tolerance <= 0.0 or not math.isfinite(merge_tolerance):
            raise ValueError("merge_toleranceは正の有限値で指定してください")
        eps = max(merge_tolerance / scale, 1.0e-14)

    def normalize(ring: list[Vector2d]) -> list[Vector2d]:
        return [
            Vector2d(
                (point.x - center_x) / scale,
                (point.y - center_y) / scale,
            )
            for point in ring
        ]

    outer: list[Vector2d] = _clean_ring(normalize(out_points), eps, "外形")
    holes: list[list[Vector2d]] = [
        _clean_ring(
            normalize(ring),
            eps,
            f"開口{index}",
        )
        for index, ring in enumerate(in_points, start=1)
    ]

    # ほぼ同じY座標を共通値にする。
    # 同じ高さの異なるリングの頂点が、誤差で薄い水平帯が生じることを防ぐ。
    snapped: list[list[Vector2d]] = _snap_near_y([outer, *holes], eps)
    outer = _clean_ring(snapped[0], eps, "外形")
    holes = [
        _clean_ring(ring, eps, f"開口{index}")
        for index, ring in enumerate(snapped[1:], start=1)
    ]

    _validate_simple_ring(outer, eps, "外形")
    for index, hole in enumerate(holes, start=1):
        _validate_simple_ring(hole, eps, f"開口{index}")

    normalized_vertices, faces = _triangulate(outer, holes, eps)
    if faces:
        boundary_loops = _extract_boundary_loops(
            normalized_vertices,
            faces,
            eps,
        )
        output_outers, output_holes = _classify_boundary_loops(
            boundary_loops,
            eps,
        )
    else:
        # 外形全体が開口の和集合で覆われた正常な空結果。
        output_outers = []
        output_holes = []

    comparison_eps: float = max(eps * 8.0, 1.0e-12)
    outer_changed: bool = not _ring_sets_equivalent(
        [_simplify_loop(outer, comparison_eps)],
        output_outers,
        comparison_eps,
    )
    holes_changed = not _ring_sets_equivalent(
        [_simplify_loop(hole, comparison_eps) for hole in holes],
        output_holes,
        comparison_eps,
    )

    def denormalize(point: Vector2d) -> Vector2d:
        return Vector2d(
            point.x * scale + center_x,
            point.y * scale + center_y,
        )

    vertices: list[Vector2d] = [denormalize(point) for point in normalized_vertices]
    new_outer: list[list[Vector2d]] | None = (
        [[denormalize(point) for point in outer_loop] for outer_loop in output_outers]
        if outer_changed
        else None
    )
    new_holes: list[list[Vector2d]] | None = (
        [[denormalize(point) for point in hole] for hole in output_holes]
        if holes_changed
        else None
    )
    return vertices, faces, new_outer, new_holes


def _clean_ring(ring: list[Vector2d], eps: float, label: str) -> list[Vector2d]:
    if not ring:
        raise _TriangulationError(f"{label}に頂点がありません")

    points: list[Vector2d] = list(ring)
    limit: float = eps * eps

    if len(points) > 1 and _distance_2(points[0], points[-1]) <= limit:
        points.pop()

    cleaned: list[Vector2d] = []
    for point in points:
        if not cleaned or _distance_2(cleaned[-1], point) > limit:
            cleaned.append(point)

    if len(cleaned) > 1 and _distance_2(cleaned[0], cleaned[-1]) <= limit:
        cleaned.pop()

    if len(cleaned) < 3:
        raise _TriangulationError(f"{label}の有効な頂点が3点未満です")

    for _ in range(len(cleaned) + 2):
        result: list[Vector2d] = []
        changed: bool = False
        count: int = len(cleaned)

        for index, point in enumerate(cleaned):
            previous: Vector2d = cleaned[(index - 1) % count]
            following: Vector2d = cleaned[(index + 1) % count]
            local_scale: float = (
                previous.distance_to(point) + point.distance_to(following) + 1.0
            )

            if abs(_cross(previous, point, following)) <= eps * local_scale:
                if _on_segment(point, previous, following, eps):
                    changed = True
                    continue
                if _on_segment(previous, point, following, eps) or _on_segment(
                    following, previous, point, eps
                ):
                    raise _TriangulationError(
                        f"{label}に折り返しまたは重複する辺があります"
                    )
            result.append(point)

        cleaned = result
        if len(cleaned) < 3:
            raise _TriangulationError(f"{label}の有効な頂点が3点未満です")
        if not changed:
            break

    area: float = abs(_signed_area(cleaned))
    if area <= max(1.0e-16, eps * _perimeter(cleaned) * 2.0):
        raise _TriangulationError(f"{label}の面積が小さすぎます")
    return cleaned


def _snap_near_y(rings: list[list[Vector2d]], eps: float) -> list[list[Vector2d]]:
    """許容誤差内にある頂点Y座標を同じ値へまとめる"""
    values: list[float] = sorted({point.y for ring in rings for point in ring})
    if not values:
        return rings

    replacement: dict[float, float] = {}
    cluster: list[float] = [values[0]]
    cluster_start: float = values[0]

    for value in values[1:]:
        if value - cluster_start <= eps:
            cluster.append(value)
            continue

        representative: float = math.fsum(cluster) / len(cluster)
        replacement.update((item, representative) for item in cluster)
        cluster = [value]
        cluster_start = value

    representative = math.fsum(cluster) / len(cluster)
    replacement.update((item, representative) for item in cluster)

    return [
        [Vector2d(point.x, replacement[point.y]) for point in ring] for ring in rings
    ]


def _validate_simple_ring(
    ring: list[Vector2d],
    eps: float,
    label: str,
) -> None:
    """リングが自己交差せず、非隣接辺が近すぎないことを確認する。"""
    edges: list[tuple[Vector2d, Vector2d]] = _edge_pairs(ring)
    count: int = len(edges)

    for first_index, first in enumerate(edges):
        if _distance_2(*first) <= eps * eps:
            raise _TriangulationError(f"{label}に短すぎる辺があります")

        for second_index in range(first_index + 1, count):
            # 隣接辺は共有端点を持つため、非隣接辺だけ検査する。
            if (
                second_index == (first_index + 1) % count
                or first_index == (second_index + 1) % count
            ):
                continue

            if _segments_too_close(*first, *edges[second_index], eps):
                raise _TriangulationError(
                    f"{label}が自己交差しているか、非隣接辺が近すぎます"
                )


def _triangulate(
    outer: list[Vector2d],
    holes: list[list[Vector2d]],
    eps: float,
) -> tuple[list[Vector2d], list[tuple[int, int, int]]]:
    """水平帯ごとの区間差を台形分割し、三角形メッシュを生成する。"""
    rings: list[list[Vector2d]] = [outer, *holes]
    ring_edges: list[list[_Edge]] = [
        _make_edges(ring, ring_index) for ring_index, ring in enumerate(rings)
    ]
    all_edges: list[_Edge] = [edge for edges in ring_edges for edge in edges]

    # 外形辺と開口辺、または異なる開口辺が交差する高さでは、水平帯の境界を追加する。
    # これにより、帯の途中で左右境界が入れ替わらない。
    intersection_points: list[Vector2d] = _collect_cross_ring_intersections(
        all_edges, eps
    )
    event_points: list[Vector2d] = [
        point for ring in rings for point in ring
    ] + intersection_points

    levels: list[float] = _unique(
        [point.y for point in event_points],
        eps / 2.0,
    )
    if len(levels) < 2:
        raise _TriangulationError("Y方向の広がりがありません")

    events: dict[float, list[float]] = {level: [] for level in levels}
    for point in event_points:
        level: float = _nearest_value(levels, point.y)
        if abs(level - point.y) <= eps * 2.0:
            events[level].append(point.x)
    events = {level: _unique(values, eps / 2.0) for level, values in events.items()}

    pool: _VertexPool = _VertexPool(eps)
    faces: list[tuple[int, int, int]] = []
    expected_area: float = 0.0
    area_eps: float = max(1.0e-16, eps * eps)

    for y0, y1 in itertools.pairwise(levels):
        if y1 - y0 <= eps:
            continue

        middle_y: float = (y0 + y1) / 2.0
        outer_intervals: list[_BandInterval] = _ring_intervals_at_y(
            ring_edges[0],
            middle_y,
            eps,
            "外形",
        )

        opening_intervals: list[_BandInterval] = []
        for index, edges in enumerate(ring_edges[1:], start=1):
            opening_intervals.extend(
                _ring_intervals_at_y(
                    edges,
                    middle_y,
                    eps,
                    f"開口{index}",
                )
            )

        opening_union: list[_BandInterval] = _merge_intervals(opening_intervals, eps)
        solid_intervals: list[_BandInterval] = []
        for outer_interval in outer_intervals:
            solid_intervals.extend(
                _subtract_intervals(
                    outer_interval,
                    opening_union,
                    eps,
                )
            )

        for interval in solid_intervals:
            left0: float = interval.left_edge.intersection_x(y0, eps)
            right0: float = interval.right_edge.intersection_x(y0, eps)
            left1: float = interval.left_edge.intersection_x(y1, eps)
            right1: float = interval.right_edge.intersection_x(y1, eps)

            width0: float = right0 - left0
            width1: float = right1 - left1
            if width0 < -eps or width1 < -eps:
                raise _TriangulationError(
                    "水平帯の途中で左右境界が逆転しました。"
                    "交点高さの計算に失敗している可能性があります"
                )

            if abs(width0) <= eps:
                width0 = 0.0
            if abs(width1) <= eps:
                width1 = 0.0

            cell_area: float = (width0 + width1) * (y1 - y0) / 2.0
            if cell_area <= area_eps:
                continue

            expected_area += cell_area
            _triangulate_cell(
                pool,
                faces,
                y0,
                y1,
                left0,
                right0,
                left1,
                right1,
                events[y0],
                events[y1],
                eps,
                area_eps,
            )

    if expected_area <= area_eps:
        # 開口の和集合が外形全体を覆う場合は、空メッシュを正常結果とする。
        return [], []
    if not faces:
        raise _TriangulationError("三角形を生成できませんでした")

    actual_area: float = math.fsum(
        abs(_cross(pool.points[a], pool.points[b], pool.points[c])) / 2.0
        for a, b, c in faces
    )
    tolerance: float = max(expected_area * 1.0e-8, eps * 16.0, 1.0e-12)
    if abs(actual_area - expected_area) > tolerance:
        raise _TriangulationError(
            "面積検証に失敗しました "
            f"(水平帯={expected_area:.12g}, 三角形={actual_area:.12g})"
        )

    return pool.points, faces


def _make_edges(ring: list[Vector2d], ring_index: int) -> list[_Edge]:
    return [
        _Edge(a, b, ring_index, edge_index)
        for edge_index, (a, b) in enumerate(_edge_pairs(ring))
    ]


def _collect_cross_ring_intersections(
    edges: list[_Edge],
    eps: float,
) -> list[Vector2d]:
    result: list[Vector2d] = []

    for first_index, first in enumerate(edges):
        for second in edges[first_index + 1 :]:
            if first.ring_index == second.ring_index:
                continue
            result.extend(
                _segment_intersection_points(
                    first.a,
                    first.b,
                    second.a,
                    second.b,
                    eps,
                )
            )

    return _unique_points(result, eps)


def _ring_intervals_at_y(
    edges: list[_Edge],
    y: float,
    eps: float,
    label: str,
) -> list[_BandInterval]:
    """単純リングが水平線上で占めるX区間を返す。"""
    crossings: list[tuple[float, _Edge]] = sorted(
        (
            (edge.intersection_x(y, eps), edge)
            for edge in edges
            if edge.is_intersecting(y)
        ),
        key=lambda item: (
            item[0],
            item[1].ring_index,
            item[1].edge_index,
        ),
    )

    if len(crossings) % 2:
        raise _TriangulationError(f"高さ{y:g}で{label}の境界交点数が奇数です")

    result: list[_BandInterval] = []
    for index in range(0, len(crossings), 2):
        left_x, left_edge = crossings[index]
        right_x, right_edge = crossings[index + 1]
        if right_x - left_x <= eps:
            raise _TriangulationError(f"高さ{y:g}で{label}の幅が許容誤差以下です")
        result.append(
            _BandInterval(
                left_edge,
                right_edge,
                left_x,
                right_x,
            )
        )
    return result


def _merge_intervals(
    intervals: list[_BandInterval],
    eps: float,
) -> list[_BandInterval]:
    """開口区間を重なりと接触を含めて和集合へまとめる。"""
    if not intervals:
        return []

    ordered: list[_BandInterval] = sorted(
        intervals,
        key=lambda interval: (
            interval.left_x,
            interval.right_x,
            interval.left_edge.ring_index,
            interval.left_edge.edge_index,
        ),
    )
    merged: list[_BandInterval] = [ordered[0]]

    for interval in ordered[1:]:
        current: _BandInterval = merged[-1]
        if interval.left_x > current.right_x + eps:
            merged.append(interval)
            continue

        # 区間が重なる場合、左端は並び順の先頭を維持し、
        # 右端だけをより遠くまで伸びる境界へ更新する。
        if interval.right_x > current.right_x + eps:
            merged[-1] = _BandInterval(
                current.left_edge,
                interval.right_edge,
                current.left_x,
                interval.right_x,
            )

    return merged


def _subtract_intervals(
    outer: _BandInterval,
    openings: list[_BandInterval],
    eps: float,
) -> list[_BandInterval]:
    """一つの外形区間から開口区間の和集合を差し引く。"""
    result: list[_BandInterval] = []
    cursor_x: float = outer.left_x
    cursor_edge: _Edge = outer.left_edge
    outer_right: float = outer.right_x

    for opening in openings:
        if opening.right_x <= cursor_x + eps:
            continue
        if opening.left_x >= outer_right - eps:
            break

        if opening.left_x > cursor_x + eps:
            segment_right: float = min(opening.left_x, outer_right)
            segment_right_edge: _Edge = (
                opening.left_edge
                if opening.left_x < outer_right - eps
                else outer.right_edge
            )
            if segment_right - cursor_x > eps:
                result.append(
                    _BandInterval(
                        cursor_edge,
                        segment_right_edge,
                        cursor_x,
                        segment_right,
                    )
                )

        if opening.right_x >= outer_right - eps:
            cursor_x = outer_right
            cursor_edge = outer.right_edge
            break

        if opening.right_x > cursor_x + eps:
            cursor_x = opening.right_x
            cursor_edge = opening.right_edge

    if outer_right - cursor_x > eps:
        result.append(
            _BandInterval(
                cursor_edge,
                outer.right_edge,
                cursor_x,
                outer_right,
            )
        )

    return result


def _triangulate_cell(
    pool: _VertexPool,
    faces: list[tuple[int, int, int]],
    y0: float,
    y1: float,
    left0: float,
    right0: float,
    left1: float,
    right1: float,
    events0: list[float],
    events1: list[float],
    eps: float,
    area_eps: float,
) -> None:
    """一つの台形を、境界イベントを共有する三角形へ分割する。"""
    width0: float = right0 - left0
    width1: float = right1 - left1

    if width0 < -eps or width1 < -eps:
        raise _TriangulationError("水平帯の左右境界が逆転しました")

    if abs(width0) <= eps:
        left0 = right0 = (left0 + right0) / 2.0
        width0 = 0.0
    if abs(width1) <= eps:
        left1 = right1 = (left1 + right1) / 2.0
        width1 = 0.0
    if width0 == 0.0 and width1 == 0.0:
        return

    bottom: list[Vector2d] = _chain(y0, left0, right0, events0, eps)
    top: list[Vector2d] = _chain(y1, left1, right1, events1, eps)

    if width0 == 0.0:
        for index in range(len(top) - 1):
            _add_triangle(
                pool,
                faces,
                bottom[0],
                top[index + 1],
                top[index],
                area_eps,
            )
        return

    if width1 == 0.0:
        for index in range(len(bottom) - 1):
            _add_triangle(
                pool,
                faces,
                top[0],
                bottom[index],
                bottom[index + 1],
                area_eps,
            )
        return

    # 凸セルを左上から右下へ向かう対角線で二つの扇形に分ける。
    for index in range(len(bottom) - 1):
        _add_triangle(
            pool,
            faces,
            top[0],
            bottom[index],
            bottom[index + 1],
            area_eps,
        )
    for index in range(len(top) - 1):
        _add_triangle(
            pool,
            faces,
            bottom[-1],
            top[index + 1],
            top[index],
            area_eps,
        )


def _chain(
    y: float,
    first: float,
    last: float,
    events: list[float],
    eps: float,
) -> list[Vector2d]:
    """水平セル辺を、同じ高さにある境界イベント位置で分割する。"""
    if last < first:
        first, last = last, first

    values: list[float] = [first, last]
    values.extend(x for x in events if first + eps < x < last - eps)
    return [Vector2d(x, y) for x in _unique(values, eps / 2.0)]


def _add_triangle(
    pool: _VertexPool,
    faces: list[tuple[int, int, int]],
    a: Vector2d,
    b: Vector2d,
    c: Vector2d,
    area_eps: float,
) -> None:
    area2: float = _cross(a, b, c)
    if abs(area2) <= 2.0 * area_eps:
        return
    if area2 < 0.0:
        b, c = c, b

    indices: tuple[int, int, int] = (pool.add(a), pool.add(b), pool.add(c))
    if len(set(indices)) == 3:
        faces.append(indices)


def _extract_boundary_loops(
    points: list[Vector2d],
    faces: list[tuple[int, int, int]],
    eps: float,
) -> list[list[Vector2d]]:
    """三角形の境界半辺をたどり、外周と内周のループを復元する。

    頂点だけで接触する複数開口では、一つの頂点に複数の境界が集まる。
    単純な頂点隣接表では経路を一意に決められないため、三角形の隣接面を回りながら次の境界半辺を探す。
    これにより接触点でも各ループを分離する。
    """
    owner: dict[tuple[int, int], tuple[int, int]] = {}
    face_edges: list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]] = []
    undirected_count: dict[tuple[int, ...], int] = {}

    for face_index, (a, b, c) in enumerate(faces):
        edges: tuple[tuple[int, int], tuple[int, int], tuple[int, int]] = (
            (a, b),
            (b, c),
            (c, a),
        )
        face_edges.append(edges)

        for local_index, edge in enumerate(edges):
            if edge in owner:
                raise _TriangulationError(
                    "同じ向きの半辺を複数の三角形が共有しています"
                )
            owner[edge] = (face_index, local_index)
            key: tuple[int, ...] = tuple(sorted(edge))
            undirected_count[key] = undirected_count.get(key, 0) + 1

    if any(count > 2 for count in undirected_count.values()):
        raise _TriangulationError("三角形メッシュに非多様体辺があります")

    boundary_edges: set[tuple[int, int]] = {
        edge for edge in owner if (edge[1], edge[0]) not in owner
    }
    if not boundary_edges:
        raise _TriangulationError("メッシュ境界を復元できませんでした")

    next_boundary: dict[tuple[int, int], tuple[int, int]] = {}
    maximum_steps: int = len(owner) + 1

    for start_edge in boundary_edges:
        current: tuple[int, int] = start_edge
        for _ in range(maximum_steps):
            face_index, local_index = owner[current]
            candidate: tuple[int, int] = face_edges[face_index][(local_index + 1) % 3]
            reverse: tuple[int, int] = (candidate[1], candidate[0])

            if reverse not in owner:
                if candidate not in boundary_edges:
                    raise _TriangulationError("境界半辺の隣接関係が矛盾しています")
                next_boundary[start_edge] = candidate
                break

            # 内部辺を反対側の三角形へ渡り、同じ頂点の周囲を回る。
            current = reverse
        else:
            raise _TriangulationError("境界半辺の次辺探索が収束しませんでした")

    loops: list[list[Vector2d]] = []
    used: set[tuple[int, int]] = set()

    for start_edge in sorted(boundary_edges):
        if start_edge in used:
            continue

        loop_indices: list[int] = []
        current = start_edge

        for _ in range(len(boundary_edges) + 1):
            if current in used:
                if current != start_edge:
                    raise _TriangulationError(
                        "境界ループが別のループへ途中接続しています"
                    )
                break

            used.add(current)
            loop_indices.append(current[0])
            current = next_boundary[current]

            if current == start_edge:
                break
        else:
            raise _TriangulationError("境界ループの追跡が収束しませんでした")

        if current != start_edge:
            raise _TriangulationError("閉じていないメッシュ境界があります")

        # 点接触する複数境界は、一つの閉路内で同じ頂点を複数回通る場合がある。
        # その閉路を共有頂点ごとの単純ループへ分解する。
        for simple_indices in _split_repeated_vertex_walk(loop_indices):
            loop = _simplify_loop(
                [points[index] for index in simple_indices],
                eps * 4.0,
            )
            if len(loop) < 3:
                raise _TriangulationError("境界ループの頂点が3点未満です")
            loops.append(loop)

    if used != boundary_edges:
        raise _TriangulationError("一部の境界半辺をループへ復元できませんでした")
    return loops


def _split_repeated_vertex_walk(
    walk: list[int],
) -> list[list[int]]:
    """同じ頂点を複数回通る閉路を、単純な閉路へ再帰的に分解する。

    開口同士が一点で接触する場合、境界半辺の追跡結果が8の字状の一つの閉路になることがある。
    共有頂点の二つの出現位置で閉路を切り分けると、元の二つの単純な境界ループを復元できる。
    """
    pending: list[list[int]] = [walk]
    result: list[list[int]] = []

    while pending:
        current = pending.pop()
        first_position: dict[int, int] = {}
        split_pair: tuple[int, int] | None = None

        for index, vertex in enumerate(current):
            previous = first_position.get(vertex)
            if previous is not None:
                split_pair = (previous, index)
                break
            first_position[vertex] = index

        if split_pair is None:
            result.append(current)
            continue

        first, second = split_pair
        first_loop = current[first:second]
        second_loop = current[:first] + current[second:]

        if len(first_loop) < 3 or len(second_loop) < 3:
            raise _TriangulationError("共有頂点で分解した境界ループの頂点が3点未満です")

        pending.append(second_loop)
        pending.append(first_loop)

    return result


def _classify_boundary_loops(
    loops: list[list[Vector2d]],
    eps: float,
) -> tuple[list[list[Vector2d]], list[list[Vector2d]]]:
    """符号付き面積で外周と内周を分類し、向きと順序を正規化する。

    三角形面は反時計回りで生成されるため、材料領域を左側に見てたどる
    境界の外周は反時計回り、内周は時計回りになる。
    開口が外形を横断して材料領域が分断された場合は、複数の外周ループをそのまま返す。
    """
    area_tolerance: float = max(eps * eps * 4.0, 1.0e-16)
    outer_loops: list[list[Vector2d]] = []
    hole_loops: list[list[Vector2d]] = []

    for loop in loops:
        area: float = _signed_area(loop)
        if area > area_tolerance:
            outer_loops.append(_rotate_loop_to_stable_start(loop))
        elif area < -area_tolerance:
            hole_loops.append(_rotate_loop_to_stable_start(loop))
        else:
            raise _TriangulationError("面積が小さすぎる境界ループがあります")

    if not outer_loops:
        raise _TriangulationError("処理後の外形ループを取得できませんでした")

    outer_loops.sort(key=_loop_sort_key)
    hole_loops.sort(key=_loop_sort_key)
    return outer_loops, hole_loops


def _simplify_loop(loop: list[Vector2d], eps: float) -> list[Vector2d]:
    """境界ループから連続重複点と一直線上の中間点を除去する。"""
    if not loop:
        return []

    limit: float = eps * eps
    cleaned: list[Vector2d] = []
    for point in loop:
        if not cleaned or _distance_2(cleaned[-1], point) > limit:
            cleaned.append(point)

    if len(cleaned) > 1 and _distance_2(cleaned[0], cleaned[-1]) <= limit:
        cleaned.pop()

    for _ in range(len(cleaned) + 2):
        if len(cleaned) < 3:
            break

        result: list[Vector2d] = []
        changed: bool = False
        count: int = len(cleaned)

        for index, point in enumerate(cleaned):
            previous: Vector2d = cleaned[(index - 1) % count]
            following: Vector2d = cleaned[(index + 1) % count]
            local_scale: float = (
                previous.distance_to(point) + point.distance_to(following) + 1.0
            )
            if abs(
                _cross(previous, point, following)
            ) <= eps * local_scale and _on_segment(point, previous, following, eps):
                changed = True
                continue
            result.append(point)

        cleaned = result
        if not changed:
            break

    return cleaned


def _rings_equivalent(
    first: list[Vector2d],
    second: list[Vector2d],
    eps: float,
) -> bool:
    if len(first) != len(second):
        return False
    if not first:
        return True

    limit: float = eps * eps
    candidates: list[int] = [
        index
        for index, point in enumerate(second)
        if _distance_2(first[0], point) <= limit
    ]

    for start in candidates:
        forward: bool = all(
            _distance_2(first[index], second[(start + index) % len(second)]) <= limit
            for index in range(len(first))
        )
        if forward:
            return True

        backward: bool = all(
            _distance_2(first[index], second[(start - index) % len(second)]) <= limit
            for index in range(len(first))
        )
        if backward:
            return True

    return False


def _ring_sets_equivalent(
    first: list[list[Vector2d]],
    second: list[list[Vector2d]],
    eps: float,
) -> bool:
    if len(first) != len(second):
        return False

    unmatched: list[int] = list(range(len(second)))
    for first_ring in first:
        matched_index: int | None = None
        for second_index in unmatched:
            if _rings_equivalent(first_ring, second[second_index], eps):
                matched_index = second_index
                break
        if matched_index is None:
            return False
        unmatched.remove(matched_index)

    return not unmatched


def _rotate_loop_to_stable_start(loop: list[Vector2d]) -> list[Vector2d]:
    """最小のY、次に最小のXとなる頂点をリング先頭へ移動する。"""
    if not loop:
        return []
    start: int = min(
        range(len(loop)),
        key=lambda index: (loop[index].y, loop[index].x),
    )
    return loop[start:] + loop[:start]


def _loop_sort_key(loop: list[Vector2d]) -> tuple[float, float, float, int]:
    """開口リングを決定的な順序へ並べるためのキー"""
    min_y = min(point.y for point in loop)
    min_x = min(point.x for point in loop)
    return (min_y, min_x, -abs(_signed_area(loop)), len(loop))


def _segment_intersection_points(
    a: Vector2d,
    b: Vector2d,
    c: Vector2d,
    d: Vector2d,
    eps: float,
) -> list[Vector2d]:
    """2線分の交点。共線重複時は重複区間の端点。"""
    if not _segments_intersect(a, b, c, d, eps):
        return []

    rx: float = b.x - a.x
    ry: float = b.y - a.y
    sx: float = d.x - c.x
    sy: float = d.y - c.y
    denominator: float = rx * sy - ry * sx
    scale: float = math.hypot(rx, ry) * math.hypot(sx, sy) + 1.0

    if abs(denominator) > eps * scale:
        qpx: float = c.x - a.x
        qpy: float = c.y - a.y
        t: float = (qpx * sy - qpy * sx) / denominator
        u: float = (qpx * ry - qpy * rx) / denominator

        parameter_tolerance: float = eps / max(
            math.hypot(rx, ry),
            math.hypot(sx, sy),
            eps,
        )
        if (
            -parameter_tolerance <= t <= 1.0 + parameter_tolerance
            and -parameter_tolerance <= u <= 1.0 + parameter_tolerance
        ):
            t = min(1.0, max(0.0, t))
            u = min(1.0, max(0.0, u))
            first_point: Vector2d = Vector2d(a.x + t * rx, a.y + t * ry)
            second_point: Vector2d = Vector2d(c.x + u * sx, c.y + u * sy)
            return [
                Vector2d(
                    (first_point.x + second_point.x) / 2.0,
                    (first_point.y + second_point.y) / 2.0,
                )
            ]
        return []

    # 平行線分の場合は、両方の線分上にある端点を集める。
    candidates: list[Vector2d] = [
        point
        for point in (a, b, c, d)
        if _on_segment(point, a, b, eps) and _on_segment(point, c, d, eps)
    ]
    return _unique_points(candidates, eps)


def _unique_points(points: list[Vector2d], eps: float) -> list[Vector2d]:
    """許容誤差内で一致する点を一つへまとめる。"""
    result: list[Vector2d] = []
    limit: float = eps * eps

    for point in sorted(points, key=lambda item: (item.y, item.x)):
        if any(_distance_2(point, existing) <= limit for existing in result):
            continue
        result.append(point)
    return result


def _nearest_value(values: list[float], target: float) -> float:
    return min(values, key=lambda value: abs(value - target))


def _unique(values: list[float], eps: float) -> list[float]:
    """近接する数値を平均値へまとめ、昇順で返す。"""
    result: list[float] = []
    for value in sorted(values):
        if not result or value - result[-1] > eps:
            result.append(value)
        else:
            result[-1] = (result[-1] + value) / 2.0
    return result


def _edge_pairs(ring: list[Vector2d]) -> list[tuple[Vector2d, Vector2d]]:
    return list(zip(ring, ring[1:] + ring[:1], strict=False))


def _distance_2(a: Vector2d, b: Vector2d) -> float:
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2


def _cross(a: Vector2d, b: Vector2d, c: Vector2d) -> float:
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def _signed_area(ring: list[Vector2d]) -> float:
    return math.fsum(a.x * b.y - b.x * a.y for a, b in _edge_pairs(ring)) / 2.0


def _perimeter(ring: list[Vector2d]) -> float:
    return math.fsum(a.distance_to(b) for a, b in _edge_pairs(ring))


def _point_segment_distance_2(
    point: Vector2d,
    a: Vector2d,
    b: Vector2d,
) -> float:
    dx: float = b.x - a.x
    dy: float = b.y - a.y
    length2: float = dx * dx + dy * dy

    if length2 == 0.0:
        return _distance_2(point, a)

    t: float = ((point.x - a.x) * dx + (point.y - a.y) * dy) / length2
    t = min(1.0, max(0.0, t))
    nearest: Vector2d = Vector2d(a.x + t * dx, a.y + t * dy)
    return _distance_2(point, nearest)


def _on_segment(
    point: Vector2d,
    a: Vector2d,
    b: Vector2d,
    eps: float,
) -> bool:
    """点が許容誤差内で線分上にあるかの判定"""
    return (
        min(a.x, b.x) - eps <= point.x <= max(a.x, b.x) + eps
        and min(a.y, b.y) - eps <= point.y <= max(a.y, b.y) + eps
        and _point_segment_distance_2(point, a, b) <= eps * eps
    )


def _orientation(
    a: Vector2d,
    b: Vector2d,
    c: Vector2d,
    eps: float,
) -> int:
    """3点の向きを反時計回り1、時計回り-1、共線0で返す。"""
    value: float = _cross(a, b, c)
    tolerance: float = eps * (a.distance_to(b) + a.distance_to(c) + 1.0)
    if value > tolerance:
        return 1
    if value < -tolerance:
        return -1
    return 0


def _segments_intersect(
    a: Vector2d,
    b: Vector2d,
    c: Vector2d,
    d: Vector2d,
    eps: float,
) -> bool:
    """2線分が許容誤差内で交差または接触するかの判定"""
    if (
        max(a.x, b.x) + eps < min(c.x, d.x)
        or max(c.x, d.x) + eps < min(a.x, b.x)
        or max(a.y, b.y) + eps < min(c.y, d.y)
        or max(c.y, d.y) + eps < min(a.y, b.y)
    ):
        return False

    o1: int = _orientation(a, b, c, eps)
    o2: int = _orientation(a, b, d, eps)
    o3: int = _orientation(c, d, a, eps)
    o4: int = _orientation(c, d, b, eps)

    if o1 * o2 < 0 and o3 * o4 < 0:
        return True

    return (
        (o1 == 0 and _on_segment(c, a, b, eps))
        or (o2 == 0 and _on_segment(d, a, b, eps))
        or (o3 == 0 and _on_segment(a, c, d, eps))
        or (o4 == 0 and _on_segment(b, c, d, eps))
    )


def _segments_too_close(
    a: Vector2d,
    b: Vector2d,
    c: Vector2d,
    d: Vector2d,
    eps: float,
) -> bool:
    """2線分が交差するか、許容距離以内まで近接するかの判定"""
    if _segments_intersect(a, b, c, d, eps):
        return True

    limit: float = eps * eps
    return (
        min(
            _point_segment_distance_2(a, c, d),
            _point_segment_distance_2(b, c, d),
            _point_segment_distance_2(c, a, b),
            _point_segment_distance_2(d, a, b),
        )
        <= limit
    )
