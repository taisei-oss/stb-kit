# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_reporting import Code, Phase, Reporter


def convert_sec_figure_slab_rc(
    v202: stb_v2_0_2.StbSecFigureSlabRc, *, reporter: Reporter
) -> stb_v2_1_0.StbSecFigureSlabRcConventional | None:
    v210: stb_v2_1_0.StbSecFigureSlabRcConventional = (
        stb_v2_1_0.StbSecFigureSlabRcConventional()
    )
    if v202.stb_sec_slab_rc_straight:
        v202_straight: stb_v2_0_2.StbSecSlabRcStraight = v202.stb_sec_slab_rc_straight
        v210_straight: stb_v2_1_0.StbSecSlabRcConventionalStraight = (
            stb_v2_1_0.StbSecSlabRcConventionalStraight(depth=v202_straight.depth)
        )
        v210.stb_sec_slab_rc_conventional_straight = v210_straight
    elif v202.stb_sec_slab_rc_taper:
        v202_tapers: list[stb_v2_0_2.StbSecSlabRcTaper] = v202.stb_sec_slab_rc_taper
        try:
            taper_base = next(
                v202_taper for v202_taper in v202_tapers if v202_taper.pos == "BASE"
            )
            taper_tip = next(
                v202_taper for v202_taper in v202_tapers if v202_taper.pos == "TIP"
            )
        except StopIteration:
            reporter.warning(
                message="TaperのBASE,TIPが1回ずつ使われていないため変換できません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=v202,
            )
            return None

        v210_taper: stb_v2_1_0.StbSecSlabRcConventionalTaper = (
            stb_v2_1_0.StbSecSlabRcConventionalTaper(
                base_depth=taper_base.depth, tip_depth=taper_tip.depth
            )
        )
        v210.stb_sec_slab_rc_conventional_taper = v210_taper
    elif v202.stb_sec_slab_rc_haunch:
        v202_haunches: list[stb_v2_0_2.StbSecSlabRcHaunch] = v202.stb_sec_slab_rc_haunch
        try:
            haunch_base = next(
                v202_haunch
                for v202_haunch in v202_haunches
                if v202_haunch.pos == "BASE"
            )
            haunch_center = next(
                v202_haunch
                for v202_haunch in v202_haunches
                if v202_haunch.pos == "CENTER"
            )
            haunch_haunch = next(
                v202_haunch
                for v202_haunch in v202_haunches
                if v202_haunch.pos == "HAUNCH"
            )

        except StopIteration:
            reporter.warning(
                message=(
                    "HaunchのBASE,CENTER,HAUNCHが1回ずつ使われていないため変換できません"
                ),
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=v202,
            )
            return None

        v210_haunch: stb_v2_1_0.StbSecSlabRcConventionalHaunch = (
            stb_v2_1_0.StbSecSlabRcConventionalHaunch(
                base_depth=haunch_base.depth,
                tip_depth=haunch_center.depth,
                haunch_length=haunch_haunch.depth,
            )
        )
        v210.stb_sec_slab_rc_conventional_haunch = v210_haunch
    else:
        reporter.warning(
            message="必要な子要素がないため変換できません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.UPGRADE,
            stb_element=v202,
        )
        return None
    return v210


def convert_sec_slab_rc(
    v202: stb_v2_0_2.StbSecSlabRc,
    v210: stb_v2_1_0.StbSecSlabRc,
    *,
    reporter: Reporter,
) -> None:
    if not v202.stb_sec_figure_slab_rc:
        reporter.warning(
            message="必要な子要素がないため変換できません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.UPGRADE,
            stb_element=v202,
        )
        return
    v210_fig_conventional: stb_v2_1_0.StbSecFigureSlabRcConventional | None = (
        convert_sec_figure_slab_rc(v202.stb_sec_figure_slab_rc, reporter=reporter)
    )
    if v210_fig_conventional is None:
        return
    v210.stb_sec_slab_rc_conventional = stb_v2_1_0.StbSecSlabRcConventional(
        stb_sec_figure_slab_rc_conventional=v210_fig_conventional
    )


def sec_slab_rc(
    before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
) -> None:
    if not isinstance(before, stb_v2_0_2.StbSecSlabRc) or not isinstance(
        after, stb_v2_1_0.StbSecSlabRc
    ):
        return
    convert_sec_slab_rc(before, after, reporter=reporter)
