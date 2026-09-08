# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Protocol

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter


class HasSize(Protocol):
    @property
    def width(self) -> float: ...
    @property
    def depth(self) -> float: ...


class HasPosAndSize(HasSize, Protocol):
    @property
    def pos(self) -> str: ...


@dataclass(frozen=True, kw_only=True, slots=True)
class ConcreteBeamKind[T: StBridgeElement]:
    """RCとSRCで分ける処理"""

    straight_figure: Callable[[int, stb_v2_1_0.StbSecBeamStraight], T]
    taper_figure: Callable[[int, stb_v2_1_0.StbSecBeamTaper], T]


BEAM_KIND_RC: ConcreteBeamKind[stb_v2_1_0.StbSecFigureBeamRc] = ConcreteBeamKind(
    straight_figure=lambda order, straight: stb_v2_1_0.StbSecFigureBeamRc(
        order=order, stb_sec_beam_straight=straight
    ),
    taper_figure=lambda order, taper: stb_v2_1_0.StbSecFigureBeamRc(
        order=order, stb_sec_beam_taper=taper
    ),
)

BEAM_KIND_SRC: ConcreteBeamKind[stb_v2_1_0.StbSecFigureBeamSrc] = ConcreteBeamKind(
    straight_figure=lambda order, straight: stb_v2_1_0.StbSecFigureBeamSrc(
        order=order, stb_sec_beam_straight=straight
    ),
    taper_figure=lambda order, taper: stb_v2_1_0.StbSecFigureBeamSrc(
        order=order, stb_sec_beam_taper=taper
    ),
)


def convert_figure[T: StBridgeElement](
    kind: ConcreteBeamKind[T],
    *,
    straight: HasSize | None,
    tapers: Sequence[HasPosAndSize],
    haunches: Sequence[HasPosAndSize],
    element: StBridgeElement,
    reporter: Reporter,
) -> list[T]:
    figures: list[T] = []
    if straight is not None:
        figures.append(
            kind.straight_figure(
                1,
                stb_v2_1_0.StbSecBeamStraight(
                    width=straight.width,
                    depth=straight.depth,
                ),
            )
        )
    if tapers:
        if len(tapers) != 2:
            reporter.warning(
                message="Taperの回数がスキーマ違反のため変換できません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=element,
            )
            return []
        try:
            taper_start: HasPosAndSize = next(
                segment for segment in tapers if segment.pos == "START"
            )
            taper_end: HasPosAndSize = next(
                segment for segment in tapers if segment.pos == "END"
            )
        except StopIteration:
            reporter.warning(
                message="TaperのSTART,ENDが1回ずつ使われていないため変換できません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=element,
            )
            return []
        figures.append(
            kind.taper_figure(
                1,
                stb_v2_1_0.StbSecBeamTaper(
                    start_width=taper_start.width,
                    start_depth=taper_start.depth,
                    end_width=taper_end.width,
                    end_depth=taper_end.depth,
                ),
            )
        )
    if haunches:
        if len(haunches) != 3:
            reporter.warning(
                message="Haunchの回数がスキーマ違反のため変換できません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=element,
            )
            return []
        try:
            haunch_start: HasPosAndSize = next(
                segment for segment in haunches if segment.pos == "START"
            )
            haunch_center: HasPosAndSize = next(
                segment for segment in haunches if segment.pos == "CENTER"
            )
            haunch_end: HasPosAndSize = next(
                segment for segment in haunches if segment.pos == "END"
            )
        except StopIteration:
            reporter.warning(
                message="HaunchのSTART,CENTER,ENDが1回ずつ使われていないため変換できません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=element,
            )
            return []
        figures.append(
            kind.taper_figure(
                1,
                stb_v2_1_0.StbSecBeamTaper(
                    start_width=haunch_start.width,
                    start_depth=haunch_start.depth,
                    end_width=haunch_center.width,
                    end_depth=haunch_center.depth,
                ),
            )
        )
        figures.append(
            kind.straight_figure(
                2,
                stb_v2_1_0.StbSecBeamStraight(
                    width=haunch_center.width,
                    depth=haunch_center.depth,
                ),
            )
        )
        figures.append(
            kind.taper_figure(
                3,
                stb_v2_1_0.StbSecBeamTaper(
                    start_width=haunch_center.width,
                    start_depth=haunch_center.depth,
                    end_width=haunch_end.width,
                    end_depth=haunch_end.depth,
                ),
            )
        )
    return figures


def post_sec_beam_rc(
    v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge, *, reporter: Reporter
) -> None:
    try:
        v202_sections: list[stb_v2_0_2.StbSecBeamRc] = (
            v202.stb_model.stb_sections.stb_sec_beam_rc
        )
        v210_sections: list[stb_v2_1_0.StbSecBeamRc] = (
            v210.stb_model.stb_sections.stb_sec_beam_rc
        )
        for v202_section, v210_section in zip(v202_sections, v210_sections):
            v202_figure: stb_v2_0_2.StbSecFigureBeamRc | None = (
                v202_section.stb_sec_figure_beam_rc_or_none
            )
            if v202_figure is None:
                v210_section.stb_sec_figure_beam_rc = []
                continue
            v210_section.stb_sec_figure_beam_rc = convert_figure(
                BEAM_KIND_RC,
                straight=v202_figure.stb_sec_beam_rc_straight_or_none,
                tapers=v202_figure.stb_sec_beam_rc_taper,
                haunches=v202_figure.stb_sec_beam_rc_haunch,
                element=v202_figure,
                reporter=reporter,
            )
    except NoneAccessError:
        return


def post_sec_beam_src_rc(
    v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge, *, reporter: Reporter
) -> None:
    try:
        v202_sections: list[stb_v2_0_2.StbSecBeamSrc] = (
            v202.stb_model.stb_sections.stb_sec_beam_src
        )
        v210_sections: list[stb_v2_1_0.StbSecBeamSrc] = (
            v210.stb_model.stb_sections.stb_sec_beam_src
        )
        for v202_section, v210_section in zip(v202_sections, v210_sections):
            v202_figure: stb_v2_0_2.StbSecFigureBeamSrc | None = (
                v202_section.stb_sec_figure_beam_src_or_none
            )
            if v202_figure is None:
                v210_section.stb_sec_figure_beam_src = []
                continue
            v210_section.stb_sec_figure_beam_src = convert_figure(
                BEAM_KIND_SRC,
                straight=v202_figure.stb_sec_beam_src_straight_or_none,
                tapers=v202_figure.stb_sec_beam_src_taper,
                haunches=v202_figure.stb_sec_beam_src_haunch,
                element=v202_figure,
                reporter=reporter,
            )
    except NoneAccessError:
        return
