# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbSecBraceS,
    StbSecSteelBraceSSame,
    StbSecSteelFigureBraceS,
)

from ....._internal.data_model.shape_data import (
    Shape,
    ShapePair,
)
from .sec_steel import stb_sec_steel_name_to_shape


def stb_sec_brace_s_to_shapes(
    repo: RepositoryLatest,
    stb_sec_brace_s: StbSecBraceS,
    reporter: Reporter,
) -> list[ShapePair]:
    """
    TODO:
        - 2断面、3断面は非対応"""
    result: list[ShapePair] = []
    figure: StbSecSteelFigureBraceS | None = (
        stb_sec_brace_s.stb_sec_steel_figure_brace_s_or_none
    )
    if figure is None:
        reporter.warning(
            "StbSecSteelFigureBrace_Sが設定されていません。",
            code=Code.SCHEMA_ERROR,
            phase=Phase.CONVERT_IFC,
            stb_element=stb_sec_brace_s,
        )

        return result
    if figure.stb_sec_steel_brace_s_same_or_none is not None:
        same: StbSecSteelBraceSSame | None = figure.stb_sec_steel_brace_s_same_or_none
        if same:
            shape: Shape = stb_sec_steel_name_to_shape(repo, same.shape, reporter)
            result.append(ShapePair(shape))
    return result
