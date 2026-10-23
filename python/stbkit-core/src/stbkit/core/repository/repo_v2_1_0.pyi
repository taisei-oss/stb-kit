# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# 本ファイルはstbkit-codegenによって自動生成されました。
# このファイルを直接編集しないでください。

from typing import ClassVar, overload

from ..data_model.common import StBridgeElement
from ..data_model.stb_v2_1_0 import (
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
    StbConnectionSpecStiffner,
    StbConnectionStiffner,
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
    StbParapet,
    StbPenetrationArrangement,
    StbPile,
    StbPost,
    StbRibPlate,
    StbSecBeamRc,
    StbSecBeamS,
    StbSecBeamSrc,
    StbSecBraceS,
    StbSecBuildBox,
    StbSecBuildH,
    StbSecBuildHAssymmetric,
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
    StbStiffner,
    StbStory,
    StbStripFooting,
    StbWall,
    StbWallOffset,
    StbWeldFillet,
    StbWeldFlare,
    StbWeldFullPenetration,
    StbWeldPartialPenetration,
)
from .repo_common import RepositoryBase, _DerefAccessor, _RefMap

type _StbNodeIdMember = StbGirder | StbBeam | StbColumn | StbPost | StbSlab
type _StbColumnIdSection = (
    StbSecColumnRc | StbSecColumnS | StbSecColumnSrc | StbSecColumnCft | StbSecUndefined
)
type _StbGirderIdSection = StbSecBeamRc | StbSecBeamS | StbSecBeamSrc | StbSecUndefined
type _StbSlabIdSection = (
    StbSecSlabRc | StbSecSlabDeck | StbSecSlabPrecast | StbSecSlabLoad
)
type _StbWallIdSection = StbSecWallRc | StbSecWallLoad
type _StbDampingDeviceIdSectionStart = (
    StbSecColumnRc
    | StbSecColumnS
    | StbSecColumnSrc
    | StbSecColumnCft
    | StbSecUndefined
    | StbSecBeamRc
    | StbSecBeamS
    | StbSecBeamSrc
)
type _StbFrameDampingDeviceConnectionIdMember = StbBrace | StbPost | StbGirder
type _StbPileIdSection = StbSecPileRc | StbSecPileS | StbSecPilePrecast
type _StbOpenArrangementIdMember = StbWall | StbSlab
type _StbPenetrationArrangementIdMember = StbGirder | StbBeam
type _StbJointArrangementIdSection = (
    StbJointColumnShapeH
    | StbJointColumnShapeT
    | StbJointColumnShapeCross
    | StbJointBeamShapeH
)
type _StbJointArrangementIdMember = StbColumn | StbPost | StbGirder | StbBeam | StbBrace
type _StbGussetPlateIdWeld = (
    StbWeldFullPenetration | StbWeldPartialPenetration | StbWeldFillet | StbWeldFlare
)
type _StbSecSteelColumnSSameShape = (
    StbSecRollH
    | StbSecBuildH
    | StbSecBuildHAssymmetric
    | StbSecRollBox
    | StbSecBuildBox
    | StbSecPipe
    | StbSecRollT
    | StbSecBuildT
    | StbSecRollC
    | StbSecRoll2c
    | StbSecRollL
    | StbSecRoll2l
    | StbSecLipC
    | StbSecLip2c
    | StbSecFlatBar
    | StbSecRoundBar
    | StbSecSteelProduct
    | StbSecSteelUndefined
)
type _StbSecSteelFigureDampingDeviceHistoryIdSectionStiffner = (
    StbSecColumnRc | StbSecColumnS | StbSecColumnSrc | StbSecColumnCft
)

class _StbNodeDeref(_DerefAccessor):
    @property
    def id_member(self) -> _StbNodeIdMember: ...
    @property
    def id_member_or_none(self) -> _StbNodeIdMember | None: ...

class _StbNodeIdDeref(_DerefAccessor):
    @property
    def id(self) -> StbNode: ...
    @property
    def id_or_none(self) -> StbNode | None: ...

class _StbStoryDeref(_DerefAccessor):
    @property
    def id_dependence(self) -> StbStory: ...
    @property
    def id_dependence_or_none(self) -> StbStory | None: ...

class _StbColumnDeref(_DerefAccessor):
    @property
    def id_node_bottom(self) -> StbNode: ...
    @property
    def id_node_bottom_or_none(self) -> StbNode | None: ...
    @property
    def id_node_top(self) -> StbNode: ...
    @property
    def id_node_top_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbColumnIdSection: ...
    @property
    def id_section_or_none(self) -> _StbColumnIdSection | None: ...

class _StbPostDeref(_DerefAccessor):
    @property
    def id_node_bottom(self) -> StbNode: ...
    @property
    def id_node_bottom_or_none(self) -> StbNode | None: ...
    @property
    def id_node_top(self) -> StbNode: ...
    @property
    def id_node_top_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbColumnIdSection: ...
    @property
    def id_section_or_none(self) -> _StbColumnIdSection | None: ...

class _StbGirderDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbGirderIdSection: ...
    @property
    def id_section_or_none(self) -> _StbGirderIdSection | None: ...

class _StbBeamDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbGirderIdSection: ...
    @property
    def id_section_or_none(self) -> _StbGirderIdSection | None: ...

class _StbBraceDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecBraceS: ...
    @property
    def id_section_or_none(self) -> StbSecBraceS | None: ...

class _StbSlabDeref(_DerefAccessor):
    @property
    def id_section(self) -> _StbSlabIdSection: ...
    @property
    def id_section_or_none(self) -> _StbSlabIdSection | None: ...

class _StbWallDeref(_DerefAccessor):
    @property
    def id_section(self) -> _StbWallIdSection: ...
    @property
    def id_section_or_none(self) -> _StbWallIdSection | None: ...

class _StbMemberOffsetListDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...

class _StbSlabOffsetDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...

class _StbWallOffsetDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...

class _StbIsolatingDeviceDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecIsolatingDevice: ...
    @property
    def id_section_or_none(self) -> StbSecIsolatingDevice | None: ...
    @property
    def id_section_start(self) -> _StbColumnIdSection: ...
    @property
    def id_section_start_or_none(self) -> _StbColumnIdSection | None: ...
    @property
    def id_section_end(self) -> _StbColumnIdSection: ...
    @property
    def id_section_end_or_none(self) -> _StbColumnIdSection | None: ...

class _StbDampingDeviceDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecDampingDevice: ...
    @property
    def id_section_or_none(self) -> StbSecDampingDevice | None: ...
    @property
    def id_section_start(self) -> _StbDampingDeviceIdSectionStart: ...
    @property
    def id_section_start_or_none(self) -> _StbDampingDeviceIdSectionStart | None: ...
    @property
    def id_section_end(self) -> _StbDampingDeviceIdSectionStart: ...
    @property
    def id_section_end_or_none(self) -> _StbDampingDeviceIdSectionStart | None: ...

class _StbFrameDampingDeviceDeref(_DerefAccessor):
    @property
    def id_section(self) -> StbSecDampingDevice: ...
    @property
    def id_section_or_none(self) -> StbSecDampingDevice | None: ...

class _StbFrameDampingDeviceOffsetDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...

class _StbFrameDampingDeviceMemberDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...

class _StbFrameDampingDeviceConnectionDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_member(self) -> _StbFrameDampingDeviceConnectionIdMember: ...
    @property
    def id_member_or_none(self) -> _StbFrameDampingDeviceConnectionIdMember | None: ...

class _StbFootingDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecFoundationRc: ...
    @property
    def id_section_or_none(self) -> StbSecFoundationRc | None: ...

class _StbStripFootingDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecFoundationRc: ...
    @property
    def id_section_or_none(self) -> StbSecFoundationRc | None: ...

class _StbPileDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbPileIdSection: ...
    @property
    def id_section_or_none(self) -> _StbPileIdSection | None: ...

class _StbFoundationColumnDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...
    @property
    def id_section_fd(self) -> StbSecColumnRc: ...
    @property
    def id_section_fd_or_none(self) -> StbSecColumnRc | None: ...
    @property
    def id_section_wr(self) -> StbSecFoundationRc: ...
    @property
    def id_section_wr_or_none(self) -> StbSecFoundationRc | None: ...

class _StbParapetDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecParapetRc: ...
    @property
    def id_section_or_none(self) -> StbSecParapetRc | None: ...

class _StbOpenArrangementDeref(_DerefAccessor):
    @property
    def id_section(self) -> StbSecOpenRc: ...
    @property
    def id_section_or_none(self) -> StbSecOpenRc | None: ...
    @property
    def id_member(self) -> _StbOpenArrangementIdMember: ...
    @property
    def id_member_or_none(self) -> _StbOpenArrangementIdMember | None: ...

class _StbPenetrationArrangementDeref(_DerefAccessor):
    @property
    def id_section(self) -> StbSecPenetrationS: ...
    @property
    def id_section_or_none(self) -> StbSecPenetrationS | None: ...
    @property
    def id_member(self) -> _StbPenetrationArrangementIdMember: ...
    @property
    def id_member_or_none(self) -> _StbPenetrationArrangementIdMember | None: ...

class _StbJointArrangementDeref(_DerefAccessor):
    @property
    def id_section(self) -> _StbJointArrangementIdSection: ...
    @property
    def id_section_or_none(self) -> _StbJointArrangementIdSection | None: ...
    @property
    def id_member(self) -> _StbJointArrangementIdMember: ...
    @property
    def id_member_or_none(self) -> _StbJointArrangementIdMember | None: ...

class _StbPanelZoneArrangementDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...

class _StbConnectionArrangementDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...

class _StbConnectedColumnDeref(_DerefAccessor):
    @property
    def id(self) -> StbColumn: ...
    @property
    def id_or_none(self) -> StbColumn | None: ...

class _StbConnectedPostDeref(_DerefAccessor):
    @property
    def id(self) -> StbPost: ...
    @property
    def id_or_none(self) -> StbPost | None: ...

class _StbConnectedGirderDeref(_DerefAccessor):
    @property
    def id(self) -> StbGirder: ...
    @property
    def id_or_none(self) -> StbGirder | None: ...

class _StbConnectedBeamDeref(_DerefAccessor):
    @property
    def id(self) -> StbBeam: ...
    @property
    def id_or_none(self) -> StbBeam | None: ...

class _StbConnectedBraceDeref(_DerefAccessor):
    @property
    def id(self) -> StbBrace: ...
    @property
    def id_or_none(self) -> StbBrace | None: ...

class _StbConnectingPostDeref(_DerefAccessor):
    @property
    def id(self) -> StbPost: ...
    @property
    def id_or_none(self) -> StbPost | None: ...

class _StbConnectingGirderDeref(_DerefAccessor):
    @property
    def id(self) -> StbGirder: ...
    @property
    def id_or_none(self) -> StbGirder | None: ...

class _StbConnectingBeamDeref(_DerefAccessor):
    @property
    def id(self) -> StbBeam: ...
    @property
    def id_or_none(self) -> StbBeam | None: ...

class _StbConnectingBraceDeref(_DerefAccessor):
    @property
    def id(self) -> StbBrace: ...
    @property
    def id_or_none(self) -> StbBrace | None: ...

class _StbConnectionGussetPlateDeref(_DerefAccessor):
    @property
    def id_gusset_plate(self) -> StbGussetPlate: ...
    @property
    def id_gusset_plate_or_none(self) -> StbGussetPlate | None: ...

class _StbConnectionRibPlateDeref(_DerefAccessor):
    @property
    def id_rib_plate(self) -> StbRibPlate: ...
    @property
    def id_rib_plate_or_none(self) -> StbRibPlate | None: ...

class _StbConnectionDiaphragmDeref(_DerefAccessor):
    @property
    def id_diaphragm(self) -> StbDiaphragm: ...
    @property
    def id_diaphragm_or_none(self) -> StbDiaphragm | None: ...

class _StbConnectionStiffnerDeref(_DerefAccessor):
    @property
    def id_stiffner(self) -> StbStiffner: ...
    @property
    def id_stiffner_or_none(self) -> StbStiffner | None: ...

class _StbGussetPlateDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbRibPlateDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbDiaphragmDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbStiffnerDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbConnectionSpecGussetPlateDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbConnectionSpecRibPlateDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbConnectionSpecDiaphragmDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbConnectionSpecStiffnerDeref(_DerefAccessor):
    @property
    def id_weld(self) -> _StbGussetPlateIdWeld: ...
    @property
    def id_weld_or_none(self) -> _StbGussetPlateIdWeld | None: ...

class _StbSecSteelColumnSSameDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSNotSameDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSThreeTypesDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSrcShapeHDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSrcShapeBoxDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSrcShapePipeDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSrcShapeCross1Deref(_DerefAccessor):
    @property
    def shape_x(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_x_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_y(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_y_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSrcShapeCross2Deref(_DerefAccessor):
    @property
    def shape_h(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_h_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_t1(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_t1_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_t2(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_t2_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnSrcShapeTDeref(_DerefAccessor):
    @property
    def shape_h(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_h_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_t(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_t_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnCftSameDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnCftNotSameDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelColumnCftThreeTypesDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamStraightDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamTaperDeref(_DerefAccessor):
    @property
    def start_shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def start_shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def end_shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def end_shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBraceSSameDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBraceSNotSameDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBraceSThreeTypesDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelFigureDampingDeviceHistoryDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_sub(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_sub_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def id_section_stiffner(
        self,
    ) -> _StbSecSteelFigureDampingDeviceHistoryIdSectionStiffner: ...
    @property
    def id_section_stiffner_or_none(
        self,
    ) -> _StbSecSteelFigureDampingDeviceHistoryIdSectionStiffner | None: ...

class RepositoryV2_1_0(RepositoryBase):
    _key_field_names: ClassVar[dict[type[StBridgeElement], str]]
    _ref_map: ClassVar[_RefMap]

    @overload
    def deref(self, element: StbNode) -> _StbNodeDeref: ...
    @overload
    def deref(self, element: StbNodeId) -> _StbNodeIdDeref: ...
    @overload
    def deref(self, element: StbStory) -> _StbStoryDeref: ...
    @overload
    def deref(self, element: StbColumn) -> _StbColumnDeref: ...
    @overload
    def deref(self, element: StbPost) -> _StbPostDeref: ...
    @overload
    def deref(self, element: StbGirder) -> _StbGirderDeref: ...
    @overload
    def deref(self, element: StbBeam) -> _StbBeamDeref: ...
    @overload
    def deref(self, element: StbBrace) -> _StbBraceDeref: ...
    @overload
    def deref(self, element: StbSlab) -> _StbSlabDeref: ...
    @overload
    def deref(self, element: StbWall) -> _StbWallDeref: ...
    @overload
    def deref(self, element: StbMemberOffsetList) -> _StbMemberOffsetListDeref: ...
    @overload
    def deref(self, element: StbSlabOffset) -> _StbSlabOffsetDeref: ...
    @overload
    def deref(self, element: StbWallOffset) -> _StbWallOffsetDeref: ...
    @overload
    def deref(self, element: StbIsolatingDevice) -> _StbIsolatingDeviceDeref: ...
    @overload
    def deref(self, element: StbDampingDevice) -> _StbDampingDeviceDeref: ...
    @overload
    def deref(self, element: StbFrameDampingDevice) -> _StbFrameDampingDeviceDeref: ...
    @overload
    def deref(
        self, element: StbFrameDampingDeviceOffset
    ) -> _StbFrameDampingDeviceOffsetDeref: ...
    @overload
    def deref(
        self, element: StbFrameDampingDeviceMember
    ) -> _StbFrameDampingDeviceMemberDeref: ...
    @overload
    def deref(
        self, element: StbFrameDampingDeviceConnection
    ) -> _StbFrameDampingDeviceConnectionDeref: ...
    @overload
    def deref(self, element: StbFooting) -> _StbFootingDeref: ...
    @overload
    def deref(self, element: StbStripFooting) -> _StbStripFootingDeref: ...
    @overload
    def deref(self, element: StbPile) -> _StbPileDeref: ...
    @overload
    def deref(self, element: StbFoundationColumn) -> _StbFoundationColumnDeref: ...
    @overload
    def deref(self, element: StbParapet) -> _StbParapetDeref: ...
    @overload
    def deref(self, element: StbOpenArrangement) -> _StbOpenArrangementDeref: ...
    @overload
    def deref(
        self, element: StbPenetrationArrangement
    ) -> _StbPenetrationArrangementDeref: ...
    @overload
    def deref(self, element: StbJointArrangement) -> _StbJointArrangementDeref: ...
    @overload
    def deref(
        self, element: StbPanelZoneArrangement
    ) -> _StbPanelZoneArrangementDeref: ...
    @overload
    def deref(
        self, element: StbConnectionArrangement
    ) -> _StbConnectionArrangementDeref: ...
    @overload
    def deref(self, element: StbConnectedColumn) -> _StbConnectedColumnDeref: ...
    @overload
    def deref(self, element: StbConnectedPost) -> _StbConnectedPostDeref: ...
    @overload
    def deref(self, element: StbConnectedGirder) -> _StbConnectedGirderDeref: ...
    @overload
    def deref(self, element: StbConnectedBeam) -> _StbConnectedBeamDeref: ...
    @overload
    def deref(self, element: StbConnectedBrace) -> _StbConnectedBraceDeref: ...
    @overload
    def deref(self, element: StbConnectingPost) -> _StbConnectingPostDeref: ...
    @overload
    def deref(self, element: StbConnectingGirder) -> _StbConnectingGirderDeref: ...
    @overload
    def deref(self, element: StbConnectingBeam) -> _StbConnectingBeamDeref: ...
    @overload
    def deref(self, element: StbConnectingBrace) -> _StbConnectingBraceDeref: ...
    @overload
    def deref(
        self, element: StbConnectionGussetPlate
    ) -> _StbConnectionGussetPlateDeref: ...
    @overload
    def deref(self, element: StbConnectionRibPlate) -> _StbConnectionRibPlateDeref: ...
    @overload
    def deref(
        self, element: StbConnectionDiaphragm
    ) -> _StbConnectionDiaphragmDeref: ...
    @overload
    def deref(self, element: StbConnectionStiffner) -> _StbConnectionStiffnerDeref: ...
    @overload
    def deref(self, element: StbGussetPlate) -> _StbGussetPlateDeref: ...
    @overload
    def deref(self, element: StbRibPlate) -> _StbRibPlateDeref: ...
    @overload
    def deref(self, element: StbDiaphragm) -> _StbDiaphragmDeref: ...
    @overload
    def deref(self, element: StbStiffner) -> _StbStiffnerDeref: ...
    @overload
    def deref(
        self, element: StbConnectionSpecGussetPlate
    ) -> _StbConnectionSpecGussetPlateDeref: ...
    @overload
    def deref(
        self, element: StbConnectionSpecRibPlate
    ) -> _StbConnectionSpecRibPlateDeref: ...
    @overload
    def deref(
        self, element: StbConnectionSpecDiaphragm
    ) -> _StbConnectionSpecDiaphragmDeref: ...
    @overload
    def deref(
        self, element: StbConnectionSpecStiffner
    ) -> _StbConnectionSpecStiffnerDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSSame
    ) -> _StbSecSteelColumnSSameDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSNotSame
    ) -> _StbSecSteelColumnSNotSameDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSThreeTypes
    ) -> _StbSecSteelColumnSThreeTypesDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSrcShapeH
    ) -> _StbSecSteelColumnSrcShapeHDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSrcShapeBox
    ) -> _StbSecSteelColumnSrcShapeBoxDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSrcShapePipe
    ) -> _StbSecSteelColumnSrcShapePipeDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSrcShapeCross1
    ) -> _StbSecSteelColumnSrcShapeCross1Deref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSrcShapeCross2
    ) -> _StbSecSteelColumnSrcShapeCross2Deref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnSrcShapeT
    ) -> _StbSecSteelColumnSrcShapeTDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnCftSame
    ) -> _StbSecSteelColumnCftSameDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnCftNotSame
    ) -> _StbSecSteelColumnCftNotSameDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelColumnCftThreeTypes
    ) -> _StbSecSteelColumnCftThreeTypesDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamStraight
    ) -> _StbSecSteelBeamStraightDeref: ...
    @overload
    def deref(self, element: StbSecSteelBeamTaper) -> _StbSecSteelBeamTaperDeref: ...
    @overload
    def deref(self, element: StbSecSteelBraceSSame) -> _StbSecSteelBraceSSameDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBraceSNotSame
    ) -> _StbSecSteelBraceSNotSameDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBraceSThreeTypes
    ) -> _StbSecSteelBraceSThreeTypesDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelFigureDampingDeviceHistory
    ) -> _StbSecSteelFigureDampingDeviceHistoryDeref: ...
    def get_steel(
        self,
        name: str,
    ) -> (
        StbSecRollH
        | StbSecBuildH
        | StbSecBuildHAssymmetric
        | StbSecRollBox
        | StbSecBuildBox
        | StbSecPipe
        | StbSecRollT
        | StbSecBuildT
        | StbSecRollC
        | StbSecRoll2c
        | StbSecRollL
        | StbSecRoll2l
        | StbSecLipC
        | StbSecLip2c
        | StbSecFlatBar
        | StbSecRoundBar
        | StbSecSteelProduct
        | StbSecSteelUndefined
    ): ...
