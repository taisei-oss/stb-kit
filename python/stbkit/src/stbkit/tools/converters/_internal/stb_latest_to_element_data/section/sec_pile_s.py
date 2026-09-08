# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import NoneAccessError

from stbkit.api.stb_latest import (
    StbSecFigurePileS,
    StbSecPileS,
    StbSecPileSRotational,
    StbSecPileSStraight,
    StbSecPileSTaper,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIRS_UNKNOWN,
    ShapePair,
    ShapePipe,
)
from ... import name_converter


def stb_sec_pile_s_to_shapes_and_length(
    stb_sec_pile_s: StbSecPileS,
) -> tuple[list[ShapePair], list[float]]:
    try:
        conventional: StbSecFigurePileS | None = (
            stb_sec_pile_s.stb_sec_pile_s_conventional.stb_sec_figure_pile_s
        )
    except NoneAccessError:
        conventional = None
    name: str = name_converter.stb_element_to_ifc_name(stb_sec_pile_s)
    if conventional is not None:
        piles: list[StbSecPileSStraight | StbSecPileSRotational | StbSecPileSTaper] = []
        piles.extend(conventional.stb_sec_pile_s_straight)
        piles.extend(conventional.stb_sec_pile_s_rotational)
        piles.extend(conventional.stb_sec_pile_s_taper)
        piles.sort(key=lambda p: -p.id_order)
        shapes: list[ShapePair] = []
        lengths: list[float] = []
        for i, pile in enumerate(piles):
            match pile:
                case StbSecPileSStraight() as straight:
                    shapes.append(
                        ShapePair(
                            ShapePipe(
                                name=f"{name}_{i}",
                                d=straight.d_or_none or 0.0,
                                t=straight.t_or_none or 0.0,
                            )
                        )
                    )
                    lengths.append(straight.length_pile_or_none or 0.0)
                case StbSecPileSRotational() as rotational:
                    shapes.append(
                        ShapePair(
                            ShapePipe(
                                name=f"{name}_{i}",
                                d=rotational.d2_or_none or 0.0,
                                t=(rotational.d2_or_none or 0.0) / 2.0,
                            )
                        )
                    )
                    lengths.append(rotational.t_or_none or 0.0)
                    shapes.append(
                        ShapePair(
                            ShapePipe(
                                name=f"{name}_{i}",
                                d=rotational.d1_or_none or 0.0,
                                t=rotational.t_or_none or 0.0,
                            )
                        )
                    )
                    lengths.append(
                        (rotational.length_pile_or_none or 0.0)
                        - (rotational.t_or_none or 0.0)
                    )
                case StbSecPileSTaper() as taper:
                    shapes.append(
                        ShapePair(
                            ShapePipe(
                                name=f"{name}_{i}",
                                d=taper.d2_or_none or 0.0,
                                t=taper.t_or_none or 0.0,
                            ),
                            ShapePipe(
                                name=f"{name}_{i}",
                                d=taper.d1_or_none or 0.0,
                                t=taper.t_or_none or 0.0,
                            ),
                        )
                    )
                    lengths.append(taper.length_pile_or_none or 0.0)
                case _:
                    raise AssertionError("想定外の杭断面です")
        return shapes, lengths

    return SHAPE_PAIRS_UNKNOWN, [0.0]
