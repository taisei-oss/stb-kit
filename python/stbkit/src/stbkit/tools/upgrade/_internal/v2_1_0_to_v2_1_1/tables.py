# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

ignore_field: dict[str, list[str]] = {
    "StbSecDampingDeviceFriction": ["stb_sec_isolating_device_specification_change"]
}
"""変換をスキップするフィールド。後処理(post_*)で作り直すものを列挙する。"""

class_name_table: dict[str, str] = {
    "StbSecBuild-HAssymmetric": "StbSecBuild-HAsymmetric",
    "StbConnectionStiffner": "StbConnectionStiffener",
    "StbConnectionSpecStiffner": "StbConnectionSpecStiffener",
    "StbStiffner": "StbStiffener",
    "StbStiffners": "StbStiffeners",
}

attr_name_table: dict[str, dict[str, str]] = {
    "StbApply_RC_FoundationGirder": {"allocation_rule_stirrup": "allocation_rule_hoop"},
    "StbColumn": {
        "steel_switch_heigth_top": "steel_switch_height_top",
    },
    "StbPost": {
        "steel_switch_heigth_top": "steel_switch_height_top",
    },
    "StbConnectionSpecColumnH": {
        "stiffner_size_up_connected": "stiffener_size_up_connected",
        "stiffner_size_up_connecting": "stiffener_size_up_connecting",
    },
    "StbSecBarArrangementSlabDeck": {
        "d_refactory_bar": "d_refractory_bar",
        "strength_refactory_bar": "strength_refractory_bar",
    },
    "StbSecConnectionIsolatingDeviceSP": {
        "shape_plate_start": "shape_plate_bearingside"
    },
    "StbSecPenetration_S_HiringExtension": {"protruce_stick": "protrude_stick"},
    "StbSecPile_S_Connection": {
        "d_pile_band": "d_pile_head",
        "n_pile_band": "n_pile_head",
    },
    "StbSecSteelFigureDampingDeviceHistory": {
        "kind_section_stiffner": "kind_section_stiffener",
        "id_section_stiffner": "id_section_stiffener",
    },
    "StbWeldPartialPenetration": {
        "shape_bavel": "shape_bevel",
        "sid_bavel1": "side_bevel1",
        "sid_bavel2": "side_bevel2",
    },
    "StbConnectionStiffner": {
        "id_stiffner": "id_stiffener",
    },
}
