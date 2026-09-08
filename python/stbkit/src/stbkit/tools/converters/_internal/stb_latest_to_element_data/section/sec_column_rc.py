# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.api.stb_latest import (
    StbSecColumnCircle,
    StbSecColumnRc,
    StbSecColumnRect,
    StbSecFigureColumnRc,
)

from ....._internal.data_model.shape_data import (
    ShapeCircle,
    ShapePair,
    ShapeRectangle,
)


def stb_sec_column_rc_to_shapes(
    stb_sec_column_rc: StbSecColumnRc,
) -> list[ShapePair]:
    figure: StbSecFigureColumnRc | None = stb_sec_column_rc.stb_sec_figure_column_rc
    if not figure:
        return []
    rect: StbSecColumnRect | None = figure.stb_sec_column_rect_or_none
    if rect:
        return [
            ShapePair(
                ShapeRectangle(
                    name=stb_sec_column_rc.name,
                    width_x=rect.width_x,
                    width_y=rect.width_y,
                )
            )
        ]
    circle: StbSecColumnCircle | None = figure.stb_sec_column_circle_or_none
    if circle:
        return [ShapePair(ShapeCircle(name=stb_sec_column_rc.name, d=circle.d))]
    return []
