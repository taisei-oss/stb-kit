# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.stb_latest import (
    StbSecFigureFoundationRc,
    StbSecFoundationRc,
    StbSecFoundationRcContinuous,
    StbSecFoundationRcEquiTriangle,
    StbSecFoundationRcOctagon,
    StbSecFoundationRcRect,
    StbSecFoundationRcTaperedRect,
    StbSecFoundationRcTriangle,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIRS_UNDEFINED,
    ShapeEquilateralTriangle,
    ShapeOctagon,
    ShapePair,
    ShapeRectangle,
    ShapeRightTriangle,
)


def stb_sec_foundation_rc_to_shapes_and_depth(
    stb_sec_foundation_rc: StbSecFoundationRc,
    reporter: Reporter,
    *,
    column_width_x: float | None = None,
    column_width_y: float | None = None,
    girder_width: float | None = None,
) -> tuple[list[ShapePair], list[float]]:
    figure: StbSecFigureFoundationRc | None = (
        stb_sec_foundation_rc.stb_sec_figure_foundation_rc
    )
    if not figure:
        return ([], [])
    rect: StbSecFoundationRcRect | None = figure.stb_sec_foundation_rc_rect_or_none
    if rect is not None:
        return (
            [
                ShapePair(
                    ShapeRectangle(
                        name=stb_sec_foundation_rc.name,
                        width_x=rect.width_x,
                        width_y=rect.width_y,
                    )
                )
            ],
            [rect.depth],
        )
    tapered_rect: StbSecFoundationRcTaperedRect | None = (
        figure.stb_sec_foundation_rc_tapered_rect_or_none
    )
    if tapered_rect is not None:
        depth_tip: float = tapered_rect.depth_tip_or_none or 0.0
        depth_base: float = tapered_rect.depth_base_or_none or 0.0
        top_width_x: float | None = column_width_x
        top_width_y: float | None = column_width_y
        if top_width_x is None or top_width_y is None:
            reporter.warning(
                "TaperedRectの上側のサイズが不明なため、底面の1/2のサイズで出力します。",
                code=Code.UNEXPECTED_ERROR,
                phase=Phase.CONVERT_IFC,
            )
            top_width_x = top_width_x or tapered_rect.width_x / 2.0
            top_width_y = top_width_y or tapered_rect.width_y / 2.0
        return [
            ShapePair(
                ShapeRectangle(
                    name=f"{stb_sec_foundation_rc.name}_bottom",
                    width_x=tapered_rect.width_x,
                    width_y=tapered_rect.width_y,
                )
            ),
            ShapePair(
                ShapeRectangle(
                    name=f"{stb_sec_foundation_rc.name}_switch",
                    width_x=tapered_rect.width_x,
                    width_y=tapered_rect.width_y,
                ),
                ShapeRectangle(
                    name=f"{stb_sec_foundation_rc.name}_top",
                    width_x=top_width_x,
                    width_y=top_width_y,
                ),
            ),
        ], [depth_tip, depth_base - depth_tip]
    triangle: StbSecFoundationRcTriangle | None = (
        figure.stb_sec_foundation_rc_triangle_or_none
    )
    if triangle is not None:
        return [
            ShapePair(
                ShapeRightTriangle(
                    name=stb_sec_foundation_rc.name,
                    width_x=triangle.width_x_or_none or 0.0,
                    width_y=triangle.width_y_or_none or 0.0,
                    chamfer_x=triangle.width_chamfer_x_or_none or 0.0,
                    chamfer_y=triangle.width_chamfer_y_or_none or 0.0,
                )
            )
        ], [triangle.depth_or_none or 0.0]
    equi_triangle: StbSecFoundationRcEquiTriangle | None = (
        figure.stb_sec_foundation_rc_equi_triangle_or_none
    )
    if equi_triangle is not None:
        return [
            ShapePair(
                ShapeEquilateralTriangle(
                    name=stb_sec_foundation_rc.name,
                    width_base=equi_triangle.width_base_or_none or 0.0,
                    width_chamfer=equi_triangle.width_chamfer_or_none or 0.0,
                )
            )
        ], [equi_triangle.depth_or_none or 0.0]
    octagon: StbSecFoundationRcOctagon | None = (
        figure.stb_sec_foundation_rc_octagon_or_none
    )
    if octagon is not None:
        return [
            ShapePair(
                ShapeOctagon(
                    name=stb_sec_foundation_rc.name,
                    width_x=octagon.width_x_or_none or 0.0,
                    width_y=octagon.width_y_or_none or 0.0,
                    width_chamfer_bottom_left_x=octagon.width_chamfer1_x_or_none or 0.0,
                    width_chamfer_bottom_left_y=octagon.width_chamfer1_y_or_none or 0.0,
                    width_chamfer_bottom_right_x=octagon.width_chamfer2_x_or_none
                    or 0.0,
                    width_chamfer_bottom_right_y=octagon.width_chamfer2_y_or_none
                    or 0.0,
                    width_chamfer_top_right_x=octagon.width_chamfer3_x_or_none or 0.0,
                    width_chamfer_top_right_y=octagon.width_chamfer3_y_or_none or 0.0,
                    width_chamfer_top_left_x=octagon.width_chamfer4_x_or_none or 0.0,
                    width_chamfer_top_left_y=octagon.width_chamfer4_y_or_none or 0.0,
                )
            )
        ], [octagon.depth]

    continuous: StbSecFoundationRcContinuous | None = (
        figure.stb_sec_foundation_rc_continuous_or_none
    )
    if continuous is not None:
        width_x: float = continuous.width_or_none or 0.0
        width_y: float = continuous.depth_base_or_none or 0.0
        width_top_x: float | None = girder_width
        if width_top_x is None:
            reporter.warning(
                "連続基礎の上側の幅が不明なため、底面の1/2のサイズで出力します。",
                code=Code.UNEXPECTED_ERROR,
                phase=Phase.CONVERT_IFC,
            )
            width_top_x = width_x / 2.0
        match continuous.type_or_none:
            case "RIGHT_L" | "LEFT_L":
                chamfer_x: float = width_x - width_top_x
            case "REVERSE_T":
                chamfer_x = (width_x - width_top_x) / 2.0
            case _:
                reporter.warning(
                    f"連続基礎のタイプ '{continuous.type_or_none}' はスキーマ違反です",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.CONVERT_IFC,
                    stb_element=continuous,
                )
                return (SHAPE_PAIRS_UNDEFINED, [])
        chamfer_y: float = width_y - (continuous.depth_tip_or_none or 0.0)
        if chamfer_x == 0.0 or chamfer_y == 0.0:
            return [
                ShapePair(
                    ShapeRectangle(
                        name=stb_sec_foundation_rc.name,
                        width_x=width_x,
                        width_y=width_y,
                    )
                )
            ], []
        match continuous.type_or_none:
            case "RIGHT_L":
                return [
                    ShapePair(
                        ShapeOctagon(
                            name=stb_sec_foundation_rc.name,
                            width_x=width_x,
                            width_y=width_y,
                            width_chamfer_top_right_x=chamfer_x,
                            width_chamfer_top_right_y=chamfer_y,
                        )
                    )
                ], []
            case "LEFT_L":
                return [
                    ShapePair(
                        ShapeOctagon(
                            name=stb_sec_foundation_rc.name,
                            width_x=width_x,
                            width_y=width_y,
                            width_chamfer_top_left_x=chamfer_x,
                            width_chamfer_top_left_y=chamfer_y,
                        )
                    )
                ], []

            case "REVERSE_T":
                return [
                    ShapePair(
                        ShapeOctagon(
                            name=stb_sec_foundation_rc.name,
                            width_x=width_x,
                            width_y=width_y,
                            width_chamfer_top_right_x=chamfer_x,
                            width_chamfer_top_right_y=chamfer_y,
                            width_chamfer_top_left_x=chamfer_x,
                            width_chamfer_top_left_y=chamfer_y,
                        )
                    )
                ], []

    return ([], [])
