# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import StbError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbSecColumnS,
    StbSecSteelColumnSNotSame,
    StbSecSteelColumnSSame,
    StbSecSteelColumnSThreeTypes,
    StbSecSteelFigureColumnS,
)

from ....._internal.data_model.shape_data import SHAPE_PAIRS_UNKNOWN, Shape, ShapePair
from . import sec_steel


def stb_sec_column_s_to_shapes(
    repo: RepositoryLatest,
    sec_c: StbSecColumnS,
    reporter: Reporter,
) -> list[ShapePair]:
    result: list[ShapePair] = []
    figure: StbSecSteelFigureColumnS = sec_c.stb_sec_steel_figure_column_s
    try:
        same: StbSecSteelColumnSSame | None = figure.stb_sec_steel_column_s_same_or_none
        not_sames: list[StbSecSteelColumnSNotSame] = (
            figure.stb_sec_steel_column_s_not_same
        )
        three_types_list: list[StbSecSteelColumnSThreeTypes] = (
            figure.stb_sec_steel_column_s_three_types
        )

        if same is not None:
            shape_name: str | None = same.shape
            if shape_name:
                shape: Shape = sec_steel.stb_sec_steel_name_to_shape(
                    repo, shape_name, reporter=reporter
                )
                result = [ShapePair(shape)]
        elif not_sames:
            try:
                bottom: StbSecSteelColumnSNotSame = next(
                    not_same for not_same in not_sames if not_same.pos == "BOTTOM"
                )
                top: StbSecSteelColumnSNotSame = next(
                    not_same for not_same in not_sames if not_same.pos == "TOP"
                )
            except StopIteration:
                reporter.warning(
                    message="not_same断面にBOTTOM,TOPの両方が指定されていません",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.CONVERT_IFC,
                    stb_element=sec_c,
                )
                return SHAPE_PAIRS_UNKNOWN
            for not_same in (bottom, top):
                shape_name = not_same.shape
                if shape_name:
                    shape = sec_steel.stb_sec_steel_name_to_shape(
                        repo, shape_name, reporter
                    )
                    result.append(ShapePair(shape))
        elif three_types_list:
            try:
                three_types_bottom: StbSecSteelColumnSThreeTypes = next(
                    three_types
                    for three_types in three_types_list
                    if three_types.pos == "BOTTOM"
                )
                three_types_center: StbSecSteelColumnSThreeTypes = next(
                    three_types
                    for three_types in three_types_list
                    if three_types.pos == "CENTER"
                )
                three_types_top: StbSecSteelColumnSThreeTypes = next(
                    three_types
                    for three_types in three_types_list
                    if three_types.pos == "TOP"
                )
            except StopIteration:
                reporter.warning(
                    message="three_types断面にBOTTOM,CENTER,TOPの全てが指定されていません",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.CONVERT_IFC,
                    stb_element=sec_c,
                )
                return SHAPE_PAIRS_UNKNOWN
            for three_types in (
                three_types_bottom,
                three_types_center,
                three_types_top,
            ):
                shape_name = three_types.shape
                if shape_name:
                    shape = sec_steel.stb_sec_steel_name_to_shape(
                        repo, shape_name, reporter
                    )
                    result.append(ShapePair(shape))
        if (
            sec_c.is_reference_direction_or_none is not None
            and not sec_c.is_reference_direction_or_none
        ):
            for shape_pair in result:
                if shape_pair.start.rotate_degree:
                    shape_pair.start.rotate_degree += 90.0
                else:
                    shape_pair.start.rotate_degree = 90.0
                if shape_pair.end:
                    if shape_pair.end.rotate_degree:
                        shape_pair.end.rotate_degree += 90.0
                    else:
                        shape_pair.end.rotate_degree = 90.0
        return result
    except (StbError, RuntimeError, AssertionError, TypeError, ValueError):
        reporter.warning(
            message="断面形状が不明です",
            code=Code.SCHEMA_ERROR,
            phase=Phase.CONVERT_IFC,
            stb_element=sec_c,
        )
        return SHAPE_PAIRS_UNKNOWN
