# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import StbError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbSecBeamS,
    StbSecBeamSrc,
    StbSecSteelFigureBeamS,
    StbSecSteelFigureBeamSrc,
)

from ....._internal.data_model.shape_data import (
    Shape,
    ShapePair,
)
from ....._internal.vectors import Vector2d
from . import sec_steel


def stb_sec_beam_s_to_shapes(
    repo: RepositoryLatest,
    sec_b_s: StbSecBeamS | StbSecBeamSrc,
    reporter: Reporter,
) -> list[ShapePair]:
    result: list[ShapePair] = []
    try:
        figure_b: StbSecSteelFigureBeamS | StbSecSteelFigureBeamSrc = (
            sec_b_s.stb_sec_steel_figure_beam_s
            if isinstance(sec_b_s, StbSecBeamS)
            else sec_b_s.stb_sec_steel_figure_beam_src
        )
        for s_s_b_s_shape in (
            figure_b.stb_sec_steel_beam_s_shape
            if isinstance(figure_b, StbSecSteelFigureBeamS)
            else figure_b.stb_sec_steel_beam_src_shape
        ):
            straight = s_s_b_s_shape.stb_sec_steel_beam_straight_or_none
            taper = s_s_b_s_shape.stb_sec_steel_beam_taper_or_none
            if straight:
                shape: Shape = sec_steel.stb_sec_steel_name_to_shape(
                    repo, straight.shape, reporter
                )
                if (
                    straight.vertical_offset_or_none
                    or straight.horizontal_offset_or_none
                ):
                    offset: Vector2d = Vector2d(
                        straight.horizontal_offset_or_none or 0.0,
                        straight.vertical_offset_or_none or 0.0,
                    )
                    shape.offset = offset
                if not shape:
                    return []
                result.append(ShapePair(shape))
            elif taper:
                shape_start: Shape = sec_steel.stb_sec_steel_name_to_shape(
                    repo, taper.start_shape, reporter
                )
                if (
                    taper.start_horizontal_offset_or_none
                    or taper.start_vertical_offset_or_none
                ):
                    offset_start: Vector2d = Vector2d(
                        taper.start_horizontal_offset_or_none or 0.0,
                        taper.start_vertical_offset_or_none or 0.0,
                    )
                    shape_start.offset = offset_start
                shape_end: Shape = sec_steel.stb_sec_steel_name_to_shape(
                    repo, taper.end_shape, reporter
                )
                if (
                    taper.end_horizontal_offset_or_none
                    or taper.end_vertical_offset_or_none
                ):
                    offset_end: Vector2d = Vector2d(
                        taper.end_horizontal_offset_or_none or 0.0,
                        taper.end_vertical_offset_or_none or 0.0,
                    )
                    shape_end.offset = offset_end
                result.append(
                    ShapePair(
                        shape_start,
                        shape_end,
                    )
                )
        return result
    except (StbError, RuntimeError, AssertionError, TypeError, ValueError) as e:
        reporter.warning(
            message=str(e), code=Code.UNEXPECTED_ERROR, phase=Phase.CONVERT_IFC
        )
        return result
