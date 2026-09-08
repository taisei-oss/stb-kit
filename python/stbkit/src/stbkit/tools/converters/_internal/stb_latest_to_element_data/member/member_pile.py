# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math

from stbkit.core.stb_exceptions import NoneAccessError

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbPile,
    StbSecFigurePileRcConventional,
    StbSecPileRc,
    StbSecPileRcConventionalExtendedFoot,
    StbSecPileRcConventionalExtendedTop,
    StbSecPileRcConventionalExtendedTopFoot,
)

from ....._internal.utils.unit_utils import degree_to_radian


def stb_pile_get_length_rc(repo: RepositoryLatest, stb_pile: StbPile) -> list[float]:
    length: float = stb_pile.length_all_or_none or 0.0
    if length <= 0.0:
        return [0.0]
    src_rc: StbSecPileRc = repo.get(StbSecPileRc, stb_pile.id_section)
    try:
        conventional: StbSecFigurePileRcConventional | None = (
            src_rc.stb_sec_pile_rc_conventional.stb_sec_figure_pile_rc_conventional
        )
    except NoneAccessError:
        conventional = None
    if conventional is not None:
        if conventional.stb_sec_pile_rc_conventional_straight_or_none is not None:
            return [length]
        # ここから拡底、拡頭系の処理
        result: list[float] = []
        extend_foot: (
            StbSecPileRcConventionalExtendedFoot
            | StbSecPileRcConventionalExtendedTopFoot
            | None
        ) = (
            conventional.stb_sec_pile_rc_conventional_extended_foot_or_none
            or conventional.stb_sec_pile_rc_conventional_extended_top_foot_or_none
        )
        if extend_foot is not None:
            length_extend_foot: float = extend_foot.length_extended_foot_or_none or 0.0
            if length_extend_foot > 0.0:
                result.append(length_extend_foot)
            angle_extend_foot_taper_degree: float = (
                extend_foot.angle_extended_foot_taper_or_none or 0.0
            )
            if 0.0 < angle_extend_foot_taper_degree < 90.0:
                angle_extend_foot_taper_radian = degree_to_radian(
                    angle_extend_foot_taper_degree
                )
                length_taper = (
                    (
                        (extend_foot.d_extended_foot_or_none or 0.0)
                        - (extend_foot.d_axial_or_none or 0.0)
                    )
                    / 2.0
                    / math.tan(angle_extend_foot_taper_radian)
                )
                result.append(length_taper)
        center_idnex: int = len(result)
        result.append(0.0)  # 中間部
        extend_top: (
            StbSecPileRcConventionalExtendedTop
            | StbSecPileRcConventionalExtendedTopFoot
            | None
        ) = (
            conventional.stb_sec_pile_rc_conventional_extended_top_or_none
            or conventional.stb_sec_pile_rc_conventional_extended_top_foot_or_none
        )
        if extend_top is not None:
            angle_extend_top_taper_degree: float = (
                extend_top.angle_extended_top_taper_or_none or 0.0
            )

            if 0.0 < angle_extend_top_taper_degree < 90.0:
                angle_extend_top_taper_radian = degree_to_radian(
                    angle_extend_top_taper_degree
                )
                length_taper = (
                    (
                        (extend_top.d_extended_top_or_none or 0.0)
                        - (extend_top.d_axial_or_none or 0.0)
                    )
                    / 2.0
                    / math.tan(angle_extend_top_taper_radian)
                )
                result.append(length_taper)
            result.append(stb_pile.length_head_or_none or 0.0)
        result[center_idnex] = length - sum(result)
        return result
        # 拡底、拡頭系の処理ここまで
    return [length]
