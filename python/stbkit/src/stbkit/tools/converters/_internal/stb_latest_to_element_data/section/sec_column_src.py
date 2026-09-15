# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import contextlib

from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbSecColumnRect,
    StbSecColumnSrc,
    StbSecFigureColumnSrc,
    StbSecSteelColumnSrcNotSame,
    StbSecSteelColumnSrcSame,
    StbSecSteelColumnSrcThreeTypes,
    StbSecSteelFigureColumnSrc,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIR_UNDEFINED,
    ShapeCircle,
    ShapePair,
    ShapeRectangle,
)
from . import sec_steel


def stb_sec_column_src_to_shapes(
    repo: RepositoryLatest, sec_column_src: StbSecColumnSrc, reporter: Reporter
) -> list[ShapePair] | tuple[list[ShapePair], list[ShapePair]] | None:
    shapes_rc: list[ShapePair] = []
    shapes_s: list[ShapePair] = []

    # RC断面
    sec_figure_column_src: StbSecFigureColumnSrc | None = (
        sec_column_src.stb_sec_figure_column_src_or_none
    )
    if sec_figure_column_src:
        name_rc: str = f"{sec_column_src.name_or_none}_RC"
        with contextlib.suppress(NoneAccessError):
            shapes_rc.append(
                ShapePair(
                    ShapeCircle(
                        name=name_rc,
                        d=sec_figure_column_src.stb_sec_column_circle.d,
                    ),
                )
            )
        try:
            sec_column_rect: StbSecColumnRect = (
                sec_figure_column_src.stb_sec_column_rect
            )
            shapes_rc.append(
                ShapePair(
                    ShapeRectangle(
                        name=name_rc,
                        width_x=sec_column_rect.width_x,
                        width_y=sec_column_rect.width_y,
                    ),
                )
            )
        except NoneAccessError:
            pass
        if not shapes_rc:
            reporter.warning(
                message="RC断面の形状が取得できません",
                code=Code.MISSING_ATTRIBUTE,
                phase=Phase.CONVERT_IFC,
                stb_element=sec_figure_column_src,
            )
    # S断面
    sec_steel_figure_column_src: StbSecSteelFigureColumnSrc | None = (
        sec_column_src.stb_sec_steel_figure_column_src_or_none
    )
    if sec_steel_figure_column_src:
        sec_steel_column_src_same: StbSecSteelColumnSrcSame | None = (
            sec_steel_figure_column_src.stb_sec_steel_column_src_same_or_none
        )
        src_not_same_list: list[StbSecSteelColumnSrcNotSame] = (
            sec_steel_figure_column_src.stb_sec_steel_column_src_not_same
        )
        src_three_types_list: list[StbSecSteelColumnSrcThreeTypes] = (
            sec_steel_figure_column_src.stb_sec_steel_column_src_three_types
        )
        if sec_steel_column_src_same:
            shapes_s.append(
                sec_steel.stb_sec_steel_column_src_shape_to_shape_pair(
                    repo,
                    sec_steel_column_src_same,
                    reporter,
                )
            )
        elif src_not_same_list:
            try:
                bottom: StbSecSteelColumnSrcNotSame = next(
                    not_same
                    for not_same in src_not_same_list
                    if not_same.pos == "BOTTOM"
                )
                shapes_s.append(
                    sec_steel.stb_sec_steel_column_src_shape_to_shape_pair(
                        repo,
                        bottom,
                        reporter,
                    )
                )
            except StopIteration:
                shapes_s.append(SHAPE_PAIR_UNDEFINED)
            try:
                top: StbSecSteelColumnSrcNotSame = next(
                    not_same for not_same in src_not_same_list if not_same.pos == "TOP"
                )
                shapes_s.append(
                    sec_steel.stb_sec_steel_column_src_shape_to_shape_pair(
                        repo,
                        top,
                        reporter,
                    )
                )
            except StopIteration:
                shapes_s.append(SHAPE_PAIR_UNDEFINED)
        elif src_three_types_list:
            try:
                bottom_three: StbSecSteelColumnSrcThreeTypes = next(
                    three_types
                    for three_types in src_three_types_list
                    if three_types.pos == "BOTTOM"
                )
                shapes_s.append(
                    sec_steel.stb_sec_steel_column_src_shape_to_shape_pair(
                        repo,
                        bottom_three,
                        reporter,
                    )
                )
            except StopIteration:
                shapes_s.append(SHAPE_PAIR_UNDEFINED)
            try:
                center_three: StbSecSteelColumnSrcThreeTypes = next(
                    three_types
                    for three_types in src_three_types_list
                    if three_types.pos == "CENTER"
                )
                shapes_s.append(
                    sec_steel.stb_sec_steel_column_src_shape_to_shape_pair(
                        repo,
                        center_three,
                        reporter,
                    )
                )
            except StopIteration:
                shapes_s.append(SHAPE_PAIR_UNDEFINED)
            try:
                top_three: StbSecSteelColumnSrcThreeTypes = next(
                    three_types
                    for three_types in src_three_types_list
                    if three_types.pos == "TOP"
                )
                shapes_s.append(
                    sec_steel.stb_sec_steel_column_src_shape_to_shape_pair(
                        repo,
                        top_three,
                        reporter,
                    )
                )
            except StopIteration:
                shapes_s.append(SHAPE_PAIR_UNDEFINED)

    return (shapes_rc, shapes_s)
