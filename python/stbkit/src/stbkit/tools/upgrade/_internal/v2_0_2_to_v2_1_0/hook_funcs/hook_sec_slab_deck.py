# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from ....._internal.constants import UNKNOWN_ELEMENT_SIZE_MM


def sec_slab_deck(
    before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
) -> None:
    if not isinstance(before, stb_v2_0_2.StbSecSlabDeck) or not isinstance(
        after, stb_v2_1_0.StbSecSlabDeck
    ):
        return
    use_default_length_by_can_not_calc_flag: bool = False
    use_default_length_by_error_calc_flag: bool = False
    try:
        top_concrete: float = (
            before.stb_sec_figure_slab_deck.stb_sec_slab_deck_straight.depth
        )
        top_concrete -= before.stb_sec_product_slab_deck.depth_deck
        if top_concrete <= 0:
            use_default_length_by_error_calc_flag = True
    except NoneAccessError:
        use_default_length_by_can_not_calc_flag = True

    for deck_product in after.stb_sec_slab_deck_product:
        deck_product.release_time = "Undefined"
        if use_default_length_by_can_not_calc_flag:
            reporter.warning(
                f"デッキスラブの厚みが算出できなかったため、デフォルト値{UNKNOWN_ELEMENT_SIZE_MM}mmを使用します",
                code=Code.REPAIR_LOG,
                phase=Phase.REPAIR,
                value=str(top_concrete),
                stb_element=deck_product,
            )
            deck_product.top_concrete = UNKNOWN_ELEMENT_SIZE_MM
        elif use_default_length_by_error_calc_flag:
            reporter.warning(
                f"デッキスラブの厚みが0以下となったため、デフォルト値{UNKNOWN_ELEMENT_SIZE_MM}mmを使用します",
                code=Code.REPAIR_LOG,
                phase=Phase.REPAIR,
                value=str(UNKNOWN_ELEMENT_SIZE_MM),
                ref_value=str(top_concrete),
                stb_element=after,
            )
            deck_product.top_concrete = UNKNOWN_ELEMENT_SIZE_MM
        else:
            deck_product.top_concrete = top_concrete
