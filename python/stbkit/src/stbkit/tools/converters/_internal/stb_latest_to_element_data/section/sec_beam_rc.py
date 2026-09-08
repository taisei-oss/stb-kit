# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.api.stb_latest import (
    StbSecBeamRc,
    StbSecBeamSrc,
    StbSecBeamStraight,
    StbSecBeamTaper,
    StbSecFigureBeamRc,
    StbSecFigureBeamSrc,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIR_UNKNOWN,
    ShapePair,
    ShapeRectangle,
)


def stb_figure_beam_rc_to_shapes(
    figure: StbSecFigureBeamRc | StbSecFigureBeamSrc, name: str
) -> ShapePair:
    if figure.stb_sec_beam_straight_or_none:
        straight: StbSecBeamStraight = figure.stb_sec_beam_straight
        return ShapePair(
            ShapeRectangle(
                name=name,
                width_x=straight.width,
                width_y=straight.depth,
            )
        )
    elif figure.stb_sec_beam_taper_or_none:
        taper: StbSecBeamTaper = figure.stb_sec_beam_taper
        shape_start: ShapeRectangle = ShapeRectangle(
            name=name + "_start",
            width_x=taper.start_width,
            width_y=taper.start_depth,
        )
        shape_end: ShapeRectangle = ShapeRectangle(
            name=name + "_end",
            width_x=taper.end_width,
            width_y=taper.end_depth,
        )
        return ShapePair(shape_start, shape_end)
    else:
        return SHAPE_PAIR_UNKNOWN


def stb_sec_beam_rc_to_shapes(
    stb_sec_beam_rc: StbSecBeamRc,
) -> list[ShapePair]:
    result: list[ShapePair] = []
    for figure in stb_sec_beam_rc.stb_sec_figure_beam_rc:
        result.append(stb_figure_beam_rc_to_shapes(figure, stb_sec_beam_rc.name))
    return result


def stb_sec_beam_src_to_shapes_rc(
    stb_sec_beam_src: StbSecBeamSrc,
) -> list[ShapePair]:
    result: list[ShapePair] = []
    for figure in stb_sec_beam_src.stb_sec_figure_beam_src:
        result.append(stb_figure_beam_rc_to_shapes(figure, stb_sec_beam_src.name))
    return result
