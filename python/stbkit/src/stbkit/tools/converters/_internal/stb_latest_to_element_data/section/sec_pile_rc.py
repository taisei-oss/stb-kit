# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.stb_latest import (
    StbSecFigurePileRcConventional,
    StbSecPileRc,
    StbSecPileRcConventionalExtendedFoot,
    StbSecPileRcConventionalExtendedTop,
    StbSecPileRcConventionalExtendedTopFoot,
    StbSecPileRcConventionalStraight,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIRS_UNKNOWN,
    ShapeCircle,
    ShapePair,
)
from ... import name_converter


def stb_sec_pile_rc_to_shapes(
    stb_sec_pile_rc: StbSecPileRc, reporter: Reporter
) -> list[ShapePair]:
    try:
        conventional: StbSecFigurePileRcConventional | None = (
            stb_sec_pile_rc.stb_sec_pile_rc_conventional.stb_sec_figure_pile_rc_conventional
        )
    except NoneAccessError:
        conventional = None
    name: str = name_converter.stb_element_to_ifc_name(stb_sec_pile_rc)
    if conventional is not None:
        straight: StbSecPileRcConventionalStraight | None = (
            conventional.stb_sec_pile_rc_conventional_straight_or_none
        )
        if straight is not None:
            circle: ShapeCircle = ShapeCircle(name=stb_sec_pile_rc.name, d=straight.d)
            return [ShapePair(circle)]
        # ここから拡底、拡頭系の処理
        result: list[ShapePair] = []
        extend_foot: (
            StbSecPileRcConventionalExtendedFoot
            | StbSecPileRcConventionalExtendedTopFoot
            | None
        ) = (
            conventional.stb_sec_pile_rc_conventional_extended_foot_or_none
            or conventional.stb_sec_pile_rc_conventional_extended_top_foot_or_none
        )

        if extend_foot is not None:
            d_foot: float = extend_foot.d_extended_foot_or_none or 0.0
            d_axial: float = extend_foot.d_axial_or_none or 0.0
            length_extend_foot: float = extend_foot.length_extended_foot_or_none or 0.0
            angle_extend_foot_taper: float = (
                extend_foot.angle_extended_foot_taper_or_none or 0.0
            )
            if length_extend_foot > 0.0:
                result.append(ShapePair(ShapeCircle(name=name, d=d_foot)))
            if 0.0 < angle_extend_foot_taper < 90.0 and length_extend_foot > 0.0:
                result.append(
                    ShapePair(
                        ShapeCircle(name=name, d=d_foot),
                        ShapeCircle(name=name, d=d_axial),
                    )
                )
            result.append(ShapePair(ShapeCircle(name=name, d=d_axial)))
        extend_top: (
            StbSecPileRcConventionalExtendedTop
            | StbSecPileRcConventionalExtendedTopFoot
            | None
        ) = (
            conventional.stb_sec_pile_rc_conventional_extended_top_or_none
            or conventional.stb_sec_pile_rc_conventional_extended_top_foot_or_none
        )

        if extend_top is not None:
            d_top: float = extend_top.d_extended_top_or_none or 0.0
            d_axial = extend_top.d_axial_or_none or 0.0
            angle_extend_top_taper: float = (
                extend_top.angle_extended_top_taper_or_none or 0.0
            )
            if not isinstance(extend_top, StbSecPileRcConventionalExtendedTopFoot):
                result.append(ShapePair(ShapeCircle(name=name, d=d_axial)))
            if 0.0 < angle_extend_top_taper < 90.0:
                result.append(
                    ShapePair(
                        ShapeCircle(name=name, d=d_axial),
                        ShapeCircle(name=name, d=d_top),
                    )
                )
            result.append(ShapePair(ShapeCircle(name=name, d=d_top)))
        return result
        # 拡底、拡頭系の処理ここまで

    reporter.warning(
        "変換できない杭断面です",
        code=Code.SCHEMA_ERROR,
        phase=Phase.CONVERT_IFC,
        stb_element=stb_sec_pile_rc,
    )
    return SHAPE_PAIRS_UNKNOWN
