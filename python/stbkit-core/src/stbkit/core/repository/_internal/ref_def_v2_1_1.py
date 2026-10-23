# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""
ST-Bridge v2.1.1の参照定義

公式スキーマでは表現されないため、仕様書に基づいて手書きで記述する。
内容にidを列挙するものは現状対象外

※id_orderは位置で参照ではないため除外
※出力ログのid_objectはST-Bridge内の参照ではないため除外
TODO: 計算編の対応、StbExtObject.id_object対応
"""

from ...data_model.common import StBridgeElement
from ...data_model.stb_v2_1_1 import (
    StbArcAxis,
    StbBeam,
    StbBrace,
    StbColumn,
    StbConnectedBeam,
    StbConnectedBrace,
    StbConnectedColumn,
    StbConnectedGirder,
    StbConnectedPost,
    StbConnectingBeam,
    StbConnectingBrace,
    StbConnectingGirder,
    StbConnectingPost,
    StbConnectionArrangement,
    StbConnectionDiaphragm,
    StbConnectionGussetPlate,
    StbConnectionRibPlate,
    StbConnectionSpecDiaphragm,
    StbConnectionSpecGussetPlate,
    StbConnectionSpecRibPlate,
    StbConnectionSpecStiffener,
    StbConnectionStiffener,
    StbDampingDevice,
    StbDiaphragm,
    StbFooting,
    StbFoundationColumn,
    StbFrameDampingDevice,
    StbFrameDampingDeviceConnection,
    StbFrameDampingDeviceMember,
    StbFrameDampingDeviceOffset,
    StbGirder,
    StbGussetPlate,
    StbIsolatingDevice,
    StbJointArrangement,
    StbJointBeamShapeH,
    StbJointColumnShapeCross,
    StbJointColumnShapeH,
    StbJointColumnShapeT,
    StbMemberOffsetList,
    StbNode,
    StbNodeId,
    StbOpenArrangement,
    StbPanelZoneArrangement,
    StbParallelAxis,
    StbParapet,
    StbPenetrationArrangement,
    StbPile,
    StbPost,
    StbRadialAxis,
    StbRibPlate,
    StbSecBeamRc,
    StbSecBeamS,
    StbSecBeamSrc,
    StbSecBraceS,
    StbSecBuildBox,
    StbSecBuildH,
    StbSecBuildHAsymmetric,
    StbSecBuildT,
    StbSecColumnCft,
    StbSecColumnRc,
    StbSecColumnS,
    StbSecColumnSrc,
    StbSecDampingDevice,
    StbSecFlatBar,
    StbSecFoundationRc,
    StbSecIsolatingDevice,
    StbSecLip2c,
    StbSecLipC,
    StbSecOpenRc,
    StbSecPanelZone,
    StbSecParapetRc,
    StbSecPenetrationS,
    StbSecPilePrecast,
    StbSecPileRc,
    StbSecPileS,
    StbSecPipe,
    StbSecRoll2c,
    StbSecRoll2l,
    StbSecRollBox,
    StbSecRollC,
    StbSecRollH,
    StbSecRollL,
    StbSecRollT,
    StbSecRoundBar,
    StbSecSlabDeck,
    StbSecSlabLoad,
    StbSecSlabPrecast,
    StbSecSlabRc,
    StbSecSteelBeamStraight,
    StbSecSteelBeamTaper,
    StbSecSteelBraceSNotSame,
    StbSecSteelBraceSSame,
    StbSecSteelBraceSThreeTypes,
    StbSecSteelColumnCftNotSame,
    StbSecSteelColumnCftSame,
    StbSecSteelColumnCftThreeTypes,
    StbSecSteelColumnSNotSame,
    StbSecSteelColumnSrcShapeBox,
    StbSecSteelColumnSrcShapeCross1,
    StbSecSteelColumnSrcShapeCross2,
    StbSecSteelColumnSrcShapeH,
    StbSecSteelColumnSrcShapePipe,
    StbSecSteelColumnSrcShapeT,
    StbSecSteelColumnSSame,
    StbSecSteelColumnSThreeTypes,
    StbSecSteelFigureDampingDeviceHistory,
    StbSecSteelProduct,
    StbSecSteelUndefined,
    StbSecUndefined,
    StbSecWallLoad,
    StbSecWallRc,
    StbSlab,
    StbSlabOffset,
    StbStiffener,
    StbStory,
    StbStripFooting,
    StbWall,
    StbWallOffset,
    StbWeldFillet,
    StbWeldFlare,
    StbWeldFullPenetration,
    StbWeldPartialPenetration,
)
from ..repo_common import _ByKind, _RefMap

_COLUMN_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecColumnRc,
        "S": StbSecColumnS,
        "SRC": StbSecColumnSrc,
        "CFT": StbSecColumnCft,
        "UNDEFINED": StbSecUndefined,
    },
)
_BEAM_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecBeamRc,
        "S": StbSecBeamS,
        "SRC": StbSecBeamSrc,
        "UNDEFINED": StbSecUndefined,
    },
)
_PILE_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecPileRc,
        "S": StbSecPileS,
        "PC": StbSecPilePrecast,
    },
)

_SLAB_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecSlabRc,
        "DECK": StbSecSlabDeck,
        "PRECAST": StbSecSlabPrecast,
        "LOAD": StbSecSlabLoad,
    },
)
_WALL_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecWallRc,
        "LOAD": StbSecWallLoad,
    },
)

_DAMPING_SECTION_START = _ByKind(
    "type_shape",
    {
        "BRACE": _ByKind("kind_structure_start", _COLUMN_SECTION.targets),
        "POST": _ByKind("kind_structure_start", _COLUMN_SECTION.targets),
        "GIRDER": _ByKind("kind_structure_start", _BEAM_SECTION.targets),
    },
)
_DAMPING_SECTION_END = _ByKind(
    "type_shape",
    {
        "BRACE": _ByKind("kind_structure_end", _COLUMN_SECTION.targets),
        "POST": _ByKind("kind_structure_end", _COLUMN_SECTION.targets),
        "GIRDER": _ByKind("kind_structure_end", _BEAM_SECTION.targets),
    },
)
_WELD = (
    StbWeldFullPenetration,
    StbWeldPartialPenetration,
    StbWeldFillet,
    StbWeldFlare,
)
_COLUMN_JOINT = (
    StbJointColumnShapeH,
    StbJointColumnShapeT,
    StbJointColumnShapeCross,
)
_STEEL_SECTION = (
    StbSecRollH,
    StbSecBuildH,
    StbSecBuildHAsymmetric,
    StbSecRollBox,
    StbSecBuildBox,
    StbSecPipe,
    StbSecRollT,
    StbSecBuildT,
    StbSecRollC,
    StbSecRoll2c,
    StbSecRollL,
    StbSecRoll2l,
    StbSecLipC,
    StbSecLip2c,
    StbSecFlatBar,
    StbSecRoundBar,
    StbSecSteelProduct,
    StbSecSteelUndefined,
)

_ref_map_v2_1_1: _RefMap = _RefMap(
    references={
        StbNode: {
            # ON_GRID、OTHERはリンクする部材はない（仕様書4-3～4-5）。
            "id_member": _ByKind(
                "kind",
                {
                    "ON_GIRDER": StbGirder,
                    "ON_BEAM": StbBeam,
                    "ON_COLUMN": StbColumn,
                    "ON_POST": StbPost,
                    "ON_CANTI": StbGirder,
                    "ON_SLAB": StbSlab,
                },
            ),
        },
        StbNodeId: {"id": StbNode},
        StbStory: {"id_dependence": StbStory},
        StbColumn: {
            "id_node_bottom": StbNode,
            "id_node_top": StbNode,
            "id_section": _COLUMN_SECTION,
        },
        StbPost: {
            "id_node_bottom": StbNode,
            "id_node_top": StbNode,
            "id_section": _COLUMN_SECTION,
        },
        StbGirder: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_section": _BEAM_SECTION,
        },
        StbBeam: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_section": _BEAM_SECTION,
        },
        StbBrace: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_section": StbSecBraceS,
        },
        StbSlab: {
            "id_section": _SLAB_SECTION,
        },
        StbWall: {
            "id_section": _WALL_SECTION,
        },
        StbMemberOffsetList: {"id_node": StbNode},
        StbSlabOffset: {"id_node": StbNode},
        StbWallOffset: {"id_node": StbNode},
        StbIsolatingDevice: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_section": StbSecIsolatingDevice,
            "id_section_start": _ByKind(
                "kind_structure_start", _COLUMN_SECTION.targets
            ),
            "id_section_end": _ByKind("kind_structure_end", _COLUMN_SECTION.targets),
        },
        StbDampingDevice: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_section": StbSecDampingDevice,
            # 梁タイプは梁断面、ブレースタイプ・間柱タイプは柱断面を参照する
            # （仕様書5-49）
            "id_section_start": _DAMPING_SECTION_START,
            "id_section_end": _DAMPING_SECTION_END,
        },
        StbFrameDampingDevice: {"id_section": StbSecDampingDevice},
        StbFrameDampingDeviceOffset: {"id_node": StbNode},
        StbFrameDampingDeviceMember: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
        },
        StbFrameDampingDeviceConnection: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_member": _ByKind(
                "kind_structure",
                {"BRACE": StbBrace, "POST": StbPost, "GIRDER": StbGirder},
            ),
        },
        StbFooting: {
            "id_node": StbNode,
            "id_section": StbSecFoundationRc,
        },
        StbStripFooting: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_section": StbSecFoundationRc,
        },
        StbPile: {
            "id_node": StbNode,
            "id_section": _PILE_SECTION,
        },
        StbFoundationColumn: {
            "id_node": StbNode,
            "id_section_fd": StbSecColumnRc,
            "id_section_wr": StbSecColumnRc,
        },
        StbParapet: {
            "id_node_start": StbNode,
            "id_node_end": StbNode,
            "id_section": StbSecParapetRc,
        },
        StbOpenArrangement: {
            "id_section": StbSecOpenRc,
            "id_member": _ByKind("kind_member", {"WALL": StbWall, "SLAB": StbSlab}),
        },
        StbPenetrationArrangement: {
            "id_section": StbSecPenetrationS,
            # 省略された場合はGIRDER（仕様書p.5-84）
            "id_member": _ByKind(
                "kind_member", {"GIRDER": StbGirder, "BEAM": StbBeam}, default="GIRDER"
            ),
        },
        StbJointArrangement: {
            "id_section": _ByKind(
                "kind_member",
                {
                    "COLUMN": _COLUMN_JOINT,
                    "POST": _COLUMN_JOINT,
                    "GIRDER": StbJointBeamShapeH,
                    "BEAM": StbJointBeamShapeH,
                    "BRACE": StbJointBeamShapeH,
                },
            ),
            "id_member": _ByKind(
                "kind_member",
                {
                    "COLUMN": StbColumn,
                    "POST": StbPost,
                    "GIRDER": StbGirder,
                    "BEAM": StbBeam,
                    "BRACE": StbBrace,
                },
            ),
        },
        StbPanelZoneArrangement: {"id_node": StbNode},
        StbConnectionArrangement: {"id_node": StbNode},
        StbConnectedColumn: {"id": StbColumn},
        StbConnectedPost: {"id": StbPost},
        StbConnectedGirder: {"id": StbGirder},
        StbConnectedBeam: {"id": StbBeam},
        StbConnectedBrace: {"id": StbBrace},
        StbConnectingPost: {"id": StbPost},
        StbConnectingGirder: {"id": StbGirder},
        StbConnectingBeam: {"id": StbBeam},
        StbConnectingBrace: {"id": StbBrace},
        StbConnectionGussetPlate: {"id_gusset_plate": StbGussetPlate},
        StbConnectionRibPlate: {"id_rib_plate": StbRibPlate},
        StbConnectionDiaphragm: {"id_diaphragm": StbDiaphragm},
        StbConnectionStiffener: {"id_stiffener": StbStiffener},
        StbGussetPlate: {"id_weld": _WELD},
        StbRibPlate: {"id_weld": _WELD},
        StbDiaphragm: {"id_weld": _WELD},
        StbStiffener: {"id_weld": _WELD},
        StbConnectionSpecGussetPlate: {"id_weld": _WELD},
        StbConnectionSpecRibPlate: {"id_weld": _WELD},
        StbConnectionSpecDiaphragm: {"id_weld": _WELD},
        StbConnectionSpecStiffener: {"id_weld": _WELD},
        StbSecSteelColumnSSame: {"shape": _STEEL_SECTION},
        StbSecSteelColumnSNotSame: {"shape": _STEEL_SECTION},
        StbSecSteelColumnSThreeTypes: {"shape": _STEEL_SECTION},
        StbSecSteelColumnSrcShapeH: {"shape": _STEEL_SECTION},
        StbSecSteelColumnSrcShapeBox: {"shape": _STEEL_SECTION},
        StbSecSteelColumnSrcShapePipe: {"shape": _STEEL_SECTION},
        StbSecSteelColumnSrcShapeCross1: {
            "shape_x": _STEEL_SECTION,
            "shape_y": _STEEL_SECTION,
        },
        StbSecSteelColumnSrcShapeCross2: {
            "shape_h": _STEEL_SECTION,
            "shape_t1": _STEEL_SECTION,
            "shape_t2": _STEEL_SECTION,
        },
        StbSecSteelColumnSrcShapeT: {
            "shape_h": _STEEL_SECTION,
            "shape_t": _STEEL_SECTION,
        },
        StbSecSteelColumnCftSame: {"shape": _STEEL_SECTION},
        StbSecSteelColumnCftNotSame: {"shape": _STEEL_SECTION},
        StbSecSteelColumnCftThreeTypes: {"shape": _STEEL_SECTION},
        StbSecSteelBeamStraight: {"shape": _STEEL_SECTION},
        StbSecSteelBeamTaper: {
            "start_shape": _STEEL_SECTION,
            "end_shape": _STEEL_SECTION,
        },
        StbSecSteelBraceSSame: {"shape": _STEEL_SECTION},
        StbSecSteelBraceSNotSame: {"shape": _STEEL_SECTION},
        StbSecSteelBraceSThreeTypes: {"shape": _STEEL_SECTION},
        StbSecSteelFigureDampingDeviceHistory: {
            "shape": _STEEL_SECTION,
            "shape_sub": _STEEL_SECTION,
            "id_section_stiffener": _ByKind(
                "kind_section_stiffener",
                {
                    "RC": StbSecColumnRc,
                    "S": StbSecColumnS,
                    "SRC": StbSecColumnSrc,
                    "CFT": StbSecColumnCft,
                },
            ),
        },
    },
    unique_key_groups=(frozenset(_STEEL_SECTION),),
)

_key_field_names_v2_1_1: dict[type[StBridgeElement], str] = {
    # id: ST-Bridgeにはキーではないid属性も存在するため、明示的に指定する。
    # 仕様書2-3,2-4ページに基づき記載
    StbNode: "id",
    StbParallelAxis: "id",
    StbArcAxis: "id",
    StbRadialAxis: "id",
    StbStory: "id",
    StbColumn: "id",
    StbPost: "id",
    StbGirder: "id",
    StbBeam: "id",
    StbBrace: "id",
    StbSlab: "id",
    StbWall: "id",
    StbIsolatingDevice: "id",
    StbDampingDevice: "id",
    StbFrameDampingDevice: "id",
    StbFooting: "id",
    StbStripFooting: "id",
    StbPile: "id",
    StbFoundationColumn: "id",
    StbParapet: "id",
    StbOpenArrangement: "id",  # 仕様書はStbOpenArrangementsと記載
    StbPenetrationArrangement: "id",  # 仕様書はStbPenetrationArrangementsと記載
    StbJointArrangement: "id",  # 仕様書はStbJointArrangementsと記載
    StbConnectionArrangement: "id",  # 仕様書はStbConnectionArrangementsと記載
    StbSecColumnRc: "id",
    StbSecColumnS: "id",
    StbSecColumnSrc: "id",
    StbSecColumnCft: "id",
    StbSecBeamRc: "id",
    StbSecBeamS: "id",
    StbSecBeamSrc: "id",
    StbSecBraceS: "id",
    StbSecSlabRc: "id",
    StbSecSlabDeck: "id",
    StbSecSlabPrecast: "id",
    StbSecSlabLoad: "id",
    StbSecWallRc: "id",
    StbSecWallLoad: "id",
    StbSecIsolatingDevice: "id",
    StbSecDampingDevice: "id",
    StbSecFoundationRc: "id",
    StbSecPileRc: "id",
    StbSecPileS: "id",
    StbSecPilePrecast: "id",
    StbSecParapetRc: "id",
    StbSecOpenRc: "id",
    StbSecPenetrationS: "id",
    StbSecPanelZone: "id",
    StbJointBeamShapeH: "id",
    StbJointColumnShapeH: "id",
    StbJointColumnShapeT: "id",
    StbJointColumnShapeCross: "id",
    StbSecUndefined: "id",
    # 仕様書はStbConnectionsと記載があるが、StbConnections自体はIDを持たないため、
    # 中身を登録
    StbGussetPlate: "id",
    StbRibPlate: "id",
    StbDiaphragm: "id",
    StbStiffener: "id",
    # 仕様書はStbWeldと記載があるが、StbWeld自体はIDを持たないため、中身を登録
    StbWeldFullPenetration: "id",
    StbWeldPartialPenetration: "id",
    StbWeldFillet: "id",
    StbWeldFlare: "id",
    # name: get_steel()で名前引きする鋼材断面。
    # 仕様書p6.26-1のStbSecSteelの子要素をもとに記載
    StbSecRollH: "name",
    StbSecBuildH: "name",
    StbSecBuildHAsymmetric: "name",
    StbSecRollBox: "name",
    StbSecBuildBox: "name",
    StbSecPipe: "name",
    StbSecRollT: "name",
    StbSecBuildT: "name",
    StbSecRollC: "name",
    StbSecRoll2c: "name",
    StbSecRollL: "name",
    StbSecRoll2l: "name",
    StbSecLipC: "name",
    StbSecLip2c: "name",
    StbSecFlatBar: "name",
    StbSecRoundBar: "name",
    StbSecSteelProduct: "name",
    StbSecSteelUndefined: "name",
}
