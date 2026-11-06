# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math

from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.stb_latest import StBridge

from ...._internal.data_model.ifc_data.entity_data import IfcGrid, IfcGridAxis, LineAxis
from ...._internal.vectors import Vector2d, Vector3d


def _divide_grid[T](
    items: list[tuple[float, T]], reporter: Reporter
) -> list[list[tuple[float, T]]]:
    if not items:
        return []
    sorted_items = sorted(items, key=lambda x: x[0] % 180)
    n: int = len(items)
    n_2: int = n // 2
    counter: dict[float, int] = {}
    for angle, _ in sorted_items:
        counter[angle % 180] = counter.get(angle % 180, 0) + 1
    if max(counter.values()) > n_2:
        reporter.warning(
            "同じ角度の軸が半数より多いため、"
            "グリッドのUAxes,VAxesの組み合わせを作成できません。",
            code=Code.SPECIFICATION_MISMATCH,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return []
    pairs = [[sorted_items[i], sorted_items[i + n_2]] for i in range(n_2)]
    if n % 2 > 0:
        last_item = sorted_items[-1]
        for pair in pairs:
            if (
                pair[0][0] % 180 != last_item[0] % 180
                and pair[1][0] % 180 != last_item[0] % 180
            ):
                pair.append(last_item)
                return pairs
        reporter.warning(
            "最後の軸を追加できるGridが見つからなかったため、"
            "グリッドのUAxes,VAxesの組み合わせを作成できません。",
            code=Code.SPECIFICATION_MISMATCH,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return []
    return pairs


def _get_axis_line(
    base_point: Vector2d,
    angle: float,
    distance: float,
    min_x: float,
    max_x: float,
    min_y: float,
    max_y: float,
) -> LineAxis | None:
    angle_rad: float = math.radians(angle)
    direction: Vector2d = Vector2d(math.cos(angle_rad), math.sin(angle_rad))
    normal: Vector2d = Vector2d(-direction.y, direction.x)
    point: Vector2d = Vector2d(
        base_point.x + distance * normal.x, base_point.y + distance * normal.y
    )
    start: float = -math.inf
    end: float = math.inf
    for point_xy, direction_xy, min_xy, max_xy in (
        (point.x, direction.x, min_x, max_x),
        (point.y, direction.y, min_y, max_y),
    ):
        if direction_xy == 0.0:
            if not min_xy <= point_xy <= max_xy:
                return None
            continue
        bound_1: float = (min_xy - point_xy) / direction_xy
        bound_2: float = (max_xy - point_xy) / direction_xy
        start = max(start, min(bound_1, bound_2))
        end = min(end, max(bound_1, bound_2))
    if start >= end:
        return None
    return LineAxis(
        p1=Vector3d(
            point.x + start * direction.x, point.y + start * direction.y, 0.0
        ).mm_to_m(),
        p2=Vector3d(
            point.x + end * direction.x, point.y + end * direction.y, 0.0
        ).mm_to_m(),
    )


def stb_axes_to_ifc_grid_data(stb: StBridge, reporter: Reporter) -> list[IfcGrid]:
    """通り心の変換

    現在は平行軸のみ
    IFCの仕様上、UAxes,VAxesが必須となる。
    通り心が1種類のみ等で、UAxes,VAxesの組み合わせを作成できない場合は、
    警告を記録して通り心の変換は省略する。
    TODO:その他の軸への対応"""
    result: list[IfcGrid] = []
    stb_axes = stb.stb_model.stb_axes_or_none
    if stb_axes is None:
        return result
    min_x: float = math.inf
    max_x: float = -math.inf
    min_y: float = math.inf
    max_y: float = -math.inf
    try:
        for stb_node in stb.stb_model.stb_nodes.stb_node:
            min_x = min(min_x, stb_node.x)
            max_x = max(max_x, stb_node.x)
            min_y = min(min_y, stb_node.y)
            max_y = max(max_y, stb_node.y)
    except NoneAccessError as e:
        reporter.error(
            f"StbNodeの座標取得ができなかったため、通り心の変換に失敗しました: {e}",
            code=Code.SCHEMA_ERROR,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return []
    dx: float = max_x - min_x
    dy: float = max_y - min_y
    margin: float = max(dx, dy) * 0.2
    max_x += margin
    min_x -= margin
    max_y += margin
    min_y -= margin
    ifc_grid_axes_list: list[tuple[float, tuple[str | None, list[IfcGridAxis]]]] = []
    for stb_parallel_axes in stb_axes.stb_parallel_axes:
        try:
            base_point: Vector2d = Vector2d(stb_parallel_axes.x, stb_parallel_axes.y)
            angle: float = stb_parallel_axes.angle
        except NoneAccessError as e:
            reporter.error(
                "StbParallelAxesの座標または角度が取得できなかったため"
                f"通り心の変換に失敗しました: {stb_parallel_axes} {e}",
                code=Code.SCHEMA_ERROR,
                phase=Phase.CONVERT_GEOMETRY,
            )
            continue
        ifc_grid_axes: list[IfcGridAxis] = []
        for stb_parallel_axis in stb_parallel_axes.stb_parallel_axis:
            try:
                distance: float = stb_parallel_axis.distance
            except NoneAccessError as e:
                reporter.error(
                    "StbParallelAxisの距離が取得できなかったため"
                    f"通り心の変換に失敗しました: {stb_parallel_axis} {e}",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.CONVERT_GEOMETRY,
                )
                continue
            axis_line: LineAxis | None = _get_axis_line(
                base_point, angle, distance, min_x, max_x, min_y, max_y
            )
            if axis_line is None:
                reporter.warning(
                    "通り心が節点の近くにないため、変換を省略しました:"
                    f" {stb_parallel_axis}",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.CONVERT_GEOMETRY,
                )
                continue
            ifc_grid_axes.append(
                IfcGridAxis(
                    axis_tag=stb_parallel_axis.name_or_none,
                    guid=stb_parallel_axis.guid_or_none,
                    axis_curve=axis_line,
                )
            )
        if ifc_grid_axes:
            ifc_grid_axes_list.append(
                (angle, (stb_parallel_axes.group_name_or_none, ifc_grid_axes))
            )
    divided_grids = _divide_grid(ifc_grid_axes_list, reporter)
    for divided_grid in divided_grids:
        name: str | None = None
        for _, (group_name_or_none, _) in divided_grid:
            if name is None:
                name = group_name_or_none
            elif group_name_or_none:
                name += f"+{group_name_or_none}"

        u_axes = divided_grid[0][1][1]
        v_axes = divided_grid[1][1][1]
        w_axes = divided_grid[2][1][1] if len(divided_grid) > 2 else []
        ifc_grid: IfcGrid = IfcGrid(
            name=name,
            u_axes=u_axes,
            v_axes=v_axes,
            w_axes=w_axes,
        )
        result.append(ifc_grid)
    return result
