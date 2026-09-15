# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Reporter


def convert_sec_pile_s(
    v202: stb_v2_0_2.StbSecPileS, v210: stb_v2_1_0.StbSecPileS
) -> None:
    v202_figure: stb_v2_0_2.StbSecFigurePileS | None = (
        v202.stb_sec_figure_pile_s_or_none
    )
    if v202_figure:
        v210_conventional: stb_v2_1_0.StbSecPileSConventional = (
            stb_v2_1_0.StbSecPileSConventional()
        )
        v210.stb_sec_pile_s_conventional = v210_conventional
        v210_figure: stb_v2_1_0.StbSecFigurePileS = stb_v2_1_0.StbSecFigurePileS()
        v210_conventional.stb_sec_figure_pile_s = v210_figure
        for v202_straight in v202_figure.stb_sec_pile_s_straight:
            v210_straight = stb_v2_1_0.StbSecPileSStraight(
                id_order=v202_straight.id_order,
                length_pile=v202_straight.length_pile_or_none,
                d=v202_straight.d_or_none,
                t=v202_straight.t_or_none,
                strength=v202_straight.strength_or_none,
            )
            v210_figure.stb_sec_pile_s_straight.append(v210_straight)
        for v202_rotational in v202_figure.stb_sec_pile_s_rotational:
            v210_rotational = stb_v2_1_0.StbSecPileSRotational(
                id_order=v202_rotational.id_order,
                length_pile=v202_rotational.length_pile_or_none,
                d1=v202_rotational.d1_or_none,
                d2=v202_rotational.d2_or_none,
                t=v202_rotational.t_or_none,
                strength=v202_rotational.strength_or_none,
            )
            v210_figure.stb_sec_pile_s_rotational.append(v210_rotational)
        for v202_taper in v202_figure.stb_sec_pile_s_taper:
            v210_taper = stb_v2_1_0.StbSecPileSTaper(
                id_order=v202_taper.id_order,
                length_pile=v202_taper.length_pile_or_none,
                d1=v202_taper.d1_or_none,
                d2=v202_taper.d2_or_none,
                t=v202_taper.t_or_none,
                strength=v202_taper.strength_or_none,
            )
            v210_figure.stb_sec_pile_s_taper.append(v210_taper)


def post_sec_pile_s(v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge) -> None:
    try:
        v202_list: list[stb_v2_0_2.StbSecPileS] = (
            v202.stb_model.stb_sections.stb_sec_pile_s
        )
        v210_list: list[stb_v2_1_0.StbSecPileS] = (
            v210.stb_model.stb_sections.stb_sec_pile_s
        )
    except NoneAccessError:
        return
    for v202_sec_pile, v210_sec_pile in zip(v202_list, v210_list, strict=False):
        convert_sec_pile_s(v202_sec_pile, v210_sec_pile)


def sec_pile_s(
    before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
) -> None:
    if not isinstance(before, stb_v2_0_2.StbSecPileS) or not isinstance(
        after, stb_v2_1_0.StbSecPileS
    ):
        return
    convert_sec_pile_s(before, after)
