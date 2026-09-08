# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Reporter


def convert_sec_pile_rc(
    v202: stb_v2_0_2.StbSecPileRc, v210: stb_v2_1_0.StbSecPileRc
) -> None:
    v202_figure: stb_v2_0_2.StbSecFigurePileRc | None = (
        v202.stb_sec_figure_pile_rc_or_none
    )
    if v202_figure:
        v210_conventional: stb_v2_1_0.StbSecPileRcConventional = (
            stb_v2_1_0.StbSecPileRcConventional(
                strength_concrete=v202.strength_concrete_or_none
            )
        )
        v210.stb_sec_pile_rc_conventional = v210_conventional
        v210_figure: stb_v2_1_0.StbSecFigurePileRcConventional = (
            stb_v2_1_0.StbSecFigurePileRcConventional(
                length_pipe=v202_figure.length_pipe_or_none,
                t_pipe=v202_figure.t_pipe_or_none,
                strength_pipe=v202_figure.strength_pipe_or_none,
            )
        )
        v210_conventional.stb_sec_figure_pile_rc_conventional = v210_figure
        v202_straight: stb_v2_0_2.StbSecPileRcStraight | None = (
            v202_figure.stb_sec_pile_rc_straight_or_none
        )
        if v202_straight:
            v210_straight: stb_v2_1_0.StbSecPileRcConventionalStraight = (
                stb_v2_1_0.StbSecPileRcConventionalStraight(d=v202_straight.d)
            )
            v210_figure.stb_sec_pile_rc_conventional_straight = v210_straight
        v202_extend_foot: stb_v2_0_2.StbSecPileRcExtendedFoot | None = (
            v202_figure.stb_sec_pile_rc_extended_foot_or_none
        )
        if v202_extend_foot:
            v210_extend_foot: stb_v2_1_0.StbSecPileRcConventionalExtendedFoot = stb_v2_1_0.StbSecPileRcConventionalExtendedFoot(
                d_extended_foot=v202_extend_foot.d_extended_foot_or_none,
                d_axial=v202_extend_foot.d_axial_or_none,
                length_extended_foot=v202_extend_foot.length_extended_foot_or_none,
                angle_extended_foot_taper=v202_extend_foot.angle_extended_foot_taper_or_none,
            )
            v210_figure.stb_sec_pile_rc_conventional_extended_foot = v210_extend_foot
        v202_extend_top: stb_v2_0_2.StbSecPileRcExtendedTop | None = (
            v202_figure.stb_sec_pile_rc_extended_top_or_none
        )
        if v202_extend_top:
            v210_extend_top: stb_v2_1_0.StbSecPileRcConventionalExtendedTop = stb_v2_1_0.StbSecPileRcConventionalExtendedTop(
                d_extended_top=v202_extend_top.d_extended_top_or_none,
                d_axial=v202_extend_top.d_axial_or_none,
                angle_extended_top_taper=v202_extend_top.angle_extended_top_taper_or_none,
            )
            v210_figure.stb_sec_pile_rc_conventional_extended_top = v210_extend_top
        v202_extend_top_foot: stb_v2_0_2.StbSecPileRcExtendedTopFoot | None = (
            v202_figure.stb_sec_pile_rc_extended_top_foot_or_none
        )
        if v202_extend_top_foot:
            v210_extend_top_foot: stb_v2_1_0.StbSecPileRcConventionalExtendedTopFoot = stb_v2_1_0.StbSecPileRcConventionalExtendedTopFoot(
                d_extended_top=v202_extend_top_foot.d_extended_top_or_none,
                d_axial=v202_extend_top_foot.d_axial_or_none,
                d_extended_foot=v202_extend_top_foot.d_extended_foot_or_none,
                length_extended_foot=v202_extend_top_foot.length_extended_foot_or_none,
                angle_extended_foot_taper=v202_extend_top_foot.angle_extended_foot_taper_or_none,
                angle_extended_top_taper=v202_extend_top_foot.angle_extended_top_taper_or_none,
            )
            v210_figure.stb_sec_pile_rc_conventional_extended_top_foot = (
                v210_extend_top_foot
            )


def post_sec_pile_rc(v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge) -> None:
    try:
        v202_list: list[stb_v2_0_2.StbSecPileRc] = (
            v202.stb_model.stb_sections.stb_sec_pile_rc
        )
        v210_list: list[stb_v2_1_0.StbSecPileRc] = (
            v210.stb_model.stb_sections.stb_sec_pile_rc
        )
    except NoneAccessError:
        return
    for v202_sec_pile, v210_sec_pile in zip(v202_list, v210_list):
        convert_sec_pile_rc(v202_sec_pile, v210_sec_pile)


def sec_pile_rc(
    before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
) -> None:
    if not isinstance(before, stb_v2_0_2.StbSecPileRc) or not isinstance(
        after, stb_v2_1_0.StbSecPileRc
    ):
        return
    convert_sec_pile_rc(before, after)
