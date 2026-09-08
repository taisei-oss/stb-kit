# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbSecColumnCft,
    StbSecSteelColumnCftNotSame,
    StbSecSteelColumnCftThreeTypes,
    StbSecSteelFigureColumnCft,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIRS_UNKNOWN,
    Shape,
    ShapeBox,
    ShapeBuildBox,
    ShapeCircle,
    ShapePair,
    ShapePipe,
    ShapeRectangle,
    ShapeUnknown,
)
from . import sec_steel


def _filled_concrete_shape(shape: Shape, report: Reporter) -> Shape:
    match shape:
        case ShapeBox():
            return ShapeRectangle(
                name=shape.name,
                width_x=shape.b - 2 * shape.t,
                width_y=shape.a - 2 * shape.t,
            )
        case ShapeBuildBox():
            return ShapeRectangle(
                name=shape.name,
                width_x=shape.b - 2 * shape.t1,
                width_y=shape.a - 2 * shape.t2,
            )
        case ShapePipe():
            return ShapeCircle(name=shape.name, d=shape.d - 2 * shape.t)
        case _:
            report.warning(
                message="充填できない形状の断面がCFTに使われています",
                code=Code.SCHEMA_ERROR,
                phase=Phase.CONVERT_IFC,
            )
            return ShapeUnknown()


def stb_sec_column_cft_to_shapes(
    repo: RepositoryLatest, sec_column_cft: StbSecColumnCft, reporter: Reporter
) -> list[ShapePair] | tuple[list[ShapePair], list[ShapePair]]:
    try:
        steel_figure: StbSecSteelFigureColumnCft = (
            sec_column_cft.stb_sec_steel_figure_column_cft
        )
    except NoneAccessError:
        reporter.warning(
            message="鉄骨形状が設定されていません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.CONVERT_IFC,
            stb_element=sec_column_cft,
        )
        return SHAPE_PAIRS_UNKNOWN
    try:
        shape: Shape = sec_steel.stb_sec_steel_name_to_shape(
            repo, steel_figure.stb_sec_steel_column_cft_same.shape, reporter=reporter
        )
        return (
            [ShapePair(_filled_concrete_shape(shape, reporter))],
            [ShapePair(shape)],
        )
    except NoneAccessError:
        pass
    not_same: list[StbSecSteelColumnCftNotSame] = (
        steel_figure.stb_sec_steel_column_cft_not_same
    )
    three_types: list[StbSecSteelColumnCftThreeTypes] = (
        steel_figure.stb_sec_steel_column_cft_three_types
    )
    if not_same:
        not_same_bottom: StbSecSteelColumnCftNotSame | None = next(
            (x for x in not_same if x.pos == "BOTTOM"), None
        )
        not_same_top: StbSecSteelColumnCftNotSame | None = next(
            (x for x in not_same if x.pos == "TOP"), None
        )
        if (
            not_same_bottom is None
            or not_same_top is None
            or not_same_bottom.shape_or_none is None
            or not_same_top.shape_or_none is None
        ):
            reporter.warning(
                message="TOP,BOTTOMがそろっていません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.CONVERT_IFC,
                stb_element=sec_column_cft,
            )
            return SHAPE_PAIRS_UNKNOWN
        return (
            [
                ShapePair(
                    _filled_concrete_shape(
                        sec_steel.stb_sec_steel_name_to_shape(
                            repo, not_same_bottom.shape, reporter
                        ),
                        reporter,
                    )
                ),
                ShapePair(
                    _filled_concrete_shape(
                        sec_steel.stb_sec_steel_name_to_shape(
                            repo, not_same_top.shape, reporter
                        ),
                        reporter,
                    ),
                ),
            ],
            [
                ShapePair(
                    sec_steel.stb_sec_steel_name_to_shape(
                        repo, not_same_bottom.shape, reporter
                    )
                ),
                ShapePair(
                    sec_steel.stb_sec_steel_name_to_shape(
                        repo, not_same_top.shape, reporter
                    ),
                ),
            ],
        )
    elif three_types:
        three_types_bottom: StbSecSteelColumnCftThreeTypes | None = next(
            (x for x in three_types if x.pos == "BOTTOM"), None
        )
        three_types_center: StbSecSteelColumnCftThreeTypes | None = next(
            (x for x in three_types if x.pos == "CENTER"), None
        )
        three_types_top: StbSecSteelColumnCftThreeTypes | None = next(
            (x for x in three_types if x.pos == "TOP"), None
        )
        if (
            three_types_bottom is None
            or three_types_center is None
            or three_types_top is None
            or three_types_bottom.shape_or_none is None
            or three_types_center.shape_or_none is None
            or three_types_top.shape_or_none is None
        ):
            reporter.warning(
                message="TOP,CENTER,BOTTOMがそろっていません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.CONVERT_IFC,
                stb_element=sec_column_cft,
            )
            return SHAPE_PAIRS_UNKNOWN
        return (
            [
                ShapePair(
                    _filled_concrete_shape(
                        sec_steel.stb_sec_steel_name_to_shape(
                            repo, three_types_bottom.shape, reporter
                        ),
                        reporter,
                    )
                ),
                ShapePair(
                    _filled_concrete_shape(
                        sec_steel.stb_sec_steel_name_to_shape(
                            repo, three_types_center.shape, reporter
                        ),
                        reporter,
                    )
                ),
                ShapePair(
                    _filled_concrete_shape(
                        sec_steel.stb_sec_steel_name_to_shape(
                            repo, three_types_top.shape, reporter
                        ),
                        reporter,
                    )
                ),
            ],
            [
                ShapePair(
                    sec_steel.stb_sec_steel_name_to_shape(
                        repo, three_types_bottom.shape, reporter
                    )
                ),
                ShapePair(
                    sec_steel.stb_sec_steel_name_to_shape(
                        repo, three_types_center.shape, reporter
                    ),
                ),
                ShapePair(
                    sec_steel.stb_sec_steel_name_to_shape(
                        repo, three_types_top.shape, reporter
                    ),
                ),
            ],
        )

    reporter.warning(
        message="鉄骨形状が設定されていません",
        code=Code.SCHEMA_ERROR,
        phase=Phase.CONVERT_IFC,
        stb_element=sec_column_cft,
    )
    return SHAPE_PAIRS_UNKNOWN
