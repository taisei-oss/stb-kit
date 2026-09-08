# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""v2.0.2からv2.1.0への変換規則。

記載する名称は下記の規則で記載する:
- 要素を指すキー・値はXMLの要素名で書く。
- クラスの中の属性指す名前はPython属性名で書く。XMLでいう属性と子要素の両方を含む。
TODO: XML名またはPython名に統一するか検討中
"""

ignore_field: dict[str, list[str]] = {
    "StbMembers": ["stb_opens"],
    "StbWall": ["stb_open_id_list"],
    "StbSlab": ["stb_open_id_list"],
    "StbBeam": [
        "condition_start",
        "condition_end",
        "haunch_start",
        "haunch_end",
        "joint_start",
        "joint_end",
        "kind_haunch_start",
        "kind_haunch_end",
    ],
    "StbGirder": [
        "condition_start",
        "condition_end",
        "haunch_start",
        "haunch_end",
        "joint_start",
        "joint_end",
        "kind_haunch_start",
        "kind_haunch_end",
    ],
    "StbColumn": ["condition_bottom", "condition_top"],
    "StbPost": ["condition_bottom", "condition_top"],
    "StbApplyConditionsList": ["stb_column_rc_rebar_position_apply"],
    "StbSecBeam_S": ["stb_sec_steel_figure_beam_s"],
    "StbSecBeam_RC": ["stb_sec_figure_beam_rc", "stb_sec_bar_arrangement_beam_rc"],
    "StbSecBeam_SRC": [
        "stb_sec_figure_beam_src",
        "stb_sec_steel_figure_beam_src",
        "stb_sec_bar_arrangement_beam_src",
    ],
    "StbSecPile_RC": [
        "stb_sec_bar_arrangement_pile_rc",
        "stb_sec_figure_pile_rc",
        "strength_concrete",
    ],
    "StbSecPile_S": ["stb_sec_figure_pile_s"],
    "StbSecSlab_RC": ["stb_sec_figure_slab_rc"],
}
"""変換をスキップするフィールド。後処理(post_*)で作り直すものを列挙する。"""

class_name_table: dict[str, str] = {
    "StbSecColumn_RC_Circle": "StbSecColumnCircle",
    "StbSecColumn_RC_Rect": "StbSecColumnRect",
    "StbSecColumn_SRC_Circle": "StbSecColumnCircle",
    "StbSecColumn_SRC_Rect": "StbSecColumnRect",
    "StbSecColumn_SRC_SameShapeH": "StbSecSteelColumn_SRC_ShapeH",
    "StbSecColumn_SRC_SameShapeBox": "StbSecSteelColumn_SRC_ShapeBox",
    "StbSecColumn_SRC_SameShapePipe": "StbSecSteelColumn_SRC_ShapePipe",
    "StbSecColumn_SRC_SameShapeCross": "StbSecSteelColumn_SRC_ShapeCross1",
    "StbSecColumn_SRC_SameShapeT": "StbSecSteelColumn_SRC_ShapeT",
    "StbSecColumn_SRC_NotSameShapeH": "StbSecSteelColumn_SRC_ShapeH",
    "StbSecColumn_SRC_NotSameShapeBox": "StbSecSteelColumn_SRC_ShapeBox",
    "StbSecColumn_SRC_NotSameShapePipe": "StbSecSteelColumn_SRC_ShapePipe",
    "StbSecColumn_SRC_NotSameShapeCross": "StbSecSteelColumn_SRC_ShapeCross1",
    "StbSecColumn_SRC_NotSameShapeT": "StbSecSteelColumn_SRC_ShapeT",
    "StbSecColumn_SRC_ThreeTypesShapeH": "StbSecSteelColumn_SRC_ShapeH",
    "StbSecColumn_SRC_ThreeTypesShapeBox": "StbSecSteelColumn_SRC_ShapeBox",
    "StbSecColumn_SRC_ThreeTypesShapePipe": "StbSecSteelColumn_SRC_ShapePipe",
    "StbSecColumn_SRC_ThreeTypesShapeCross": "StbSecSteelColumn_SRC_ShapeCross1",
    "StbSecColumn_SRC_ThreeTypesShapeT": "StbSecSteelColumn_SRC_ShapeT",
    "StbSecPileProduct": "StbSecPilePrecast",
    "StbSecProductSlabDeck": "StbSecSlabDeckProduct",
}

attr_name_table: dict[str, dict[str, str]] = {
    "StbColumn": {
        "joint_top": "steel_switch_heigth_top",
        "joint_bottom": "steel_switch_height_bottom",
    },
    "StbBrace": {
        "offset_start_x": "aim_offset_start_x",
        "offset_start_y": "aim_offset_start_y",
        "offset_start_z": "aim_offset_start_z",
        "offset_end_x": "aim_offset_end_x",
        "offset_end_y": "aim_offset_end_y",
        "offset_end_z": "aim_offset_end_z",
    },
    "StbJointShapeH": {
        "strength_plate": "strength_plate_flange",
    },
}
