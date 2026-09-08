# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.stb_latest import (
    StbSecFigureParapetRc,
    StbSecParapetRc,
    StbSecParapetRcTypeI,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIRS_UNKNOWN,
    Shape,
    ShapePair,
    ShapeRectangle,
)
from ... import name_converter


def stb_sec_parapet_rc_to_shapes(
    stb_sec_parapet_rc: StbSecParapetRc, reporter: Reporter
) -> list[ShapePair]:
    figure: StbSecFigureParapetRc | None = (
        stb_sec_parapet_rc.stb_sec_figure_parapet_rc_or_none
    )
    if figure is None:
        reporter.warning(
            "StbSecFigureParapet_RCが設定されていません。",
            code=Code.SCHEMA_ERROR,
            phase=Phase.CONVERT_IFC,
            stb_element=stb_sec_parapet_rc,
        )
        return SHAPE_PAIRS_UNKNOWN
    type_i: StbSecParapetRcTypeI | None = figure.stb_sec_parapet_rc_type_i_or_none
    if type_i is not None:
        shape: Shape = ShapeRectangle(
            name=name_converter.stb_element_to_ifc_name(stb_sec_parapet_rc),
            width_x=type_i.t_t_or_none or 0.0,
            width_y=type_i.depth_h_or_none or 0.0,
        )
        return [ShapePair(shape)]
    else:
        reporter.warning(
            "パラペットはI型以外の変換は対応していません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.CONVERT_IFC,
            stb_element=stb_sec_parapet_rc,
        )
        return SHAPE_PAIRS_UNKNOWN
