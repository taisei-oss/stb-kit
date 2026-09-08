# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Reporter


def column_rc_rebar_position_apply_to_stb_apply_column(
    v202: stb_v2_0_2.StbColumnRcRebarPositionApply,
) -> stb_v2_1_0.StbApplyRcColumn:
    v210: stb_v2_1_0.StbApplyRcColumn = stb_v2_1_0.StbApplyRcColumn()
    v210.depth_cover_start_x_or_none = v202.depth_cover_or_none
    v210.depth_cover_start_y_or_none = v202.depth_cover_or_none
    v210.depth_cover_end_x_or_none = v202.depth_cover_or_none
    v210.depth_cover_end_y_or_none = v202.depth_cover_or_none
    v210.interval_or_none = v202.interval_or_none
    v210.center_start_x_or_none = v202.center_or_none
    v210.center_start_y_or_none = v202.center_or_none
    v210.center_end_x_or_none = v202.center_or_none
    v210.center_end_y_or_none = v202.center_or_none
    v210.center_interval_or_none = v202.length_to_center_or_none
    # set_defaultは無視
    return v210


def post_common(v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge) -> None:
    """TODO:作成中。要対応"""
    try:
        v202_c_r_r_p_a = (
            v202.stb_common.stb_apply_conditions_list.stb_column_rc_rebar_position_apply
        )
    except NoneAccessError:
        return
    v210_a_c_l_r: stb_v2_1_0.StbApplyConditionListRc = (
        v210.ensure.stb_common()
        .ensure.stb_apply_conditions_list()
        .ensure.stb_apply_condition_list_rc()
    )
    v210_a_c_l_r.stb_apply_rc_column = (
        column_rc_rebar_position_apply_to_stb_apply_column(v202_c_r_r_p_a)
    )


def hook_apply_conditions_list(
    before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
) -> None:
    if not isinstance(before, stb_v2_0_2.StbApplyConditionsList) or not isinstance(
        after, stb_v2_1_0.StbApplyConditionsList
    ):
        return
    try:
        v202_apply = before.stb_column_rc_rebar_position_apply
    except NoneAccessError:
        return
    after.ensure.stb_apply_condition_list_rc().stb_apply_rc_column = (
        column_rc_rebar_position_apply_to_stb_apply_column(v202_apply)
    )
