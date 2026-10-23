# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# 本ファイルはstbkit-codegenによって自動生成されました。
# このファイルを直接編集しないでください。

from typing import ClassVar, overload

from ..data_model.common import StBridgeElement
from ..data_model.stb_v2_0_2 import (
    StbBeam,
    StbBrace,
    StbColumn,
    StbFooting,
    StbFoundationColumn,
    StbGirder,
    StbJointBeamShapeH,
    StbJointColumnShapeCross,
    StbJointColumnShapeH,
    StbJointColumnShapeT,
    StbMemberOffsetList,
    StbNode,
    StbNodeId,
    StbOpen,
    StbOpenId,
    StbParapet,
    StbPile,
    StbPost,
    StbSecBeamRc,
    StbSecBeamS,
    StbSecBeamSrc,
    StbSecBraceS,
    StbSecBuildBox,
    StbSecBuildH,
    StbSecColumnCft,
    StbSecColumnRc,
    StbSecColumnS,
    StbSecColumnSrc,
    StbSecColumnSrcNotSameShapeBox,
    StbSecColumnSrcNotSameShapeCross,
    StbSecColumnSrcNotSameShapeH,
    StbSecColumnSrcNotSameShapePipe,
    StbSecColumnSrcNotSameShapeT,
    StbSecColumnSrcSameShapeBox,
    StbSecColumnSrcSameShapeCross,
    StbSecColumnSrcSameShapeH,
    StbSecColumnSrcSameShapePipe,
    StbSecColumnSrcSameShapeT,
    StbSecColumnSrcThreeTypesShapeBox,
    StbSecColumnSrcThreeTypesShapeCross,
    StbSecColumnSrcThreeTypesShapeH,
    StbSecColumnSrcThreeTypesShapePipe,
    StbSecColumnSrcThreeTypesShapeT,
    StbSecFlatBar,
    StbSecFoundationRc,
    StbSecLipC,
    StbSecOpenRc,
    StbSecParapetRc,
    StbSecPileProduct,
    StbSecPileRc,
    StbSecPileS,
    StbSecPipe,
    StbSecRollBox,
    StbSecRollC,
    StbSecRollH,
    StbSecRollL,
    StbSecRollT,
    StbSecRoundBar,
    StbSecSlabDeck,
    StbSecSlabPrecast,
    StbSecSlabRc,
    StbSecSteelBeamSFiveTypes,
    StbSecSteelBeamSHaunch,
    StbSecSteelBeamSJoint,
    StbSecSteelBeamSrcFiveTypes,
    StbSecSteelBeamSrcHaunch,
    StbSecSteelBeamSrcJoint,
    StbSecSteelBeamSrcStraight,
    StbSecSteelBeamSrcTaper,
    StbSecSteelBeamSStraight,
    StbSecSteelBeamSTaper,
    StbSecSteelBraceSNotSame,
    StbSecSteelBraceSSame,
    StbSecSteelBraceSThreeTypes,
    StbSecSteelColumnCftNotSame,
    StbSecSteelColumnCftSame,
    StbSecSteelColumnCftThreeTypes,
    StbSecSteelColumnSNotSame,
    StbSecSteelColumnSSame,
    StbSecSteelColumnSThreeTypes,
    StbSecSteelFigureBeamS,
    StbSecSteelFigureBeamSrc,
    StbSecSteelFigureBraceS,
    StbSecSteelFigureColumnS,
    StbSecSteelFigureColumnSrc,
    StbSecSteelProduct,
    StbSecSteelUndefined,
    StbSecUndefined,
    StbSecWallRc,
    StbSlab,
    StbSlabOffset,
    StbStory,
    StbStripFooting,
    StbWall,
    StbWallOffset,
)
from .repo_common import RepositoryBase, _DerefAccessor, _RefMap

type _StbNodeIdMember = StbGirder | StbBeam | StbColumn | StbPost | StbSlab
type _StbColumnIdSection = (
    StbSecColumnRc | StbSecColumnS | StbSecColumnSrc | StbSecColumnCft | StbSecUndefined
)
type _StbColumnJointIdTop = (
    StbJointColumnShapeH | StbJointColumnShapeT | StbJointColumnShapeCross
)
type _StbGirderIdSection = StbSecBeamRc | StbSecBeamS | StbSecBeamSrc | StbSecUndefined
type _StbSlabIdSection = StbSecSlabRc | StbSecSlabDeck | StbSecSlabPrecast
type _StbPileIdSection = StbSecPileRc | StbSecPileS | StbSecPileProduct
type _StbSecSteelColumnSSameShape = (
    StbSecRollH
    | StbSecBuildH
    | StbSecRollBox
    | StbSecBuildBox
    | StbSecPipe
    | StbSecRollT
    | StbSecRollC
    | StbSecRollL
    | StbSecLipC
    | StbSecFlatBar
    | StbSecRoundBar
    | StbSecSteelProduct
    | StbSecSteelUndefined
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
    @property
    def joint_id_top(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_top_or_none(self) -> _StbColumnJointIdTop | None: ...
    @property
    def joint_id_bottom(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_bottom_or_none(self) -> _StbColumnJointIdTop | None: ...

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
    @property
    def joint_id_top(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_top_or_none(self) -> _StbColumnJointIdTop | None: ...
    @property
    def joint_id_bottom(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_bottom_or_none(self) -> _StbColumnJointIdTop | None: ...

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
    @property
    def joint_id_start(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_start_or_none(self) -> StbJointBeamShapeH | None: ...
    @property
    def joint_id_end(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_end_or_none(self) -> StbJointBeamShapeH | None: ...

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
    @property
    def joint_id_start(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_start_or_none(self) -> StbJointBeamShapeH | None: ...
    @property
    def joint_id_end(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_end_or_none(self) -> StbJointBeamShapeH | None: ...

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
    @property
    def joint_id_start(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_start_or_none(self) -> StbJointBeamShapeH | None: ...
    @property
    def joint_id_end(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_end_or_none(self) -> StbJointBeamShapeH | None: ...

class _StbSlabDeref(_DerefAccessor):
    @property
    def id_section(self) -> _StbSlabIdSection: ...
    @property
    def id_section_or_none(self) -> _StbSlabIdSection | None: ...

class _StbWallDeref(_DerefAccessor):
    @property
    def id_section(self) -> StbSecWallRc: ...
    @property
    def id_section_or_none(self) -> StbSecWallRc | None: ...

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

class _StbOpenDeref(_DerefAccessor):
    @property
    def id_section(self) -> StbSecOpenRc: ...
    @property
    def id_section_or_none(self) -> StbSecOpenRc | None: ...

class _StbOpenIdDeref(_DerefAccessor):
    @property
    def id(self) -> StbOpen: ...
    @property
    def id_or_none(self) -> StbOpen | None: ...

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

class _StbSecSteelFigureColumnSDeref(_DerefAccessor):
    @property
    def joint_id_top(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_top_or_none(self) -> _StbColumnJointIdTop | None: ...
    @property
    def joint_id_bottom(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_bottom_or_none(self) -> _StbColumnJointIdTop | None: ...

class _StbSecSteelFigureColumnSrcDeref(_DerefAccessor):
    @property
    def joint_id_top(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_top_or_none(self) -> _StbColumnJointIdTop | None: ...
    @property
    def joint_id_bottom(self) -> _StbColumnJointIdTop: ...
    @property
    def joint_id_bottom_or_none(self) -> _StbColumnJointIdTop | None: ...

class _StbSecSteelFigureBeamSDeref(_DerefAccessor):
    @property
    def joint_id_start(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_start_or_none(self) -> StbJointBeamShapeH | None: ...
    @property
    def joint_id_end(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_end_or_none(self) -> StbJointBeamShapeH | None: ...

class _StbSecSteelFigureBeamSrcDeref(_DerefAccessor):
    @property
    def joint_id_start(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_start_or_none(self) -> StbJointBeamShapeH | None: ...
    @property
    def joint_id_end(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_end_or_none(self) -> StbJointBeamShapeH | None: ...

class _StbSecSteelFigureBraceSDeref(_DerefAccessor):
    @property
    def joint_id_start(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_start_or_none(self) -> StbJointBeamShapeH | None: ...
    @property
    def joint_id_end(self) -> StbJointBeamShapeH: ...
    @property
    def joint_id_end_or_none(self) -> StbJointBeamShapeH | None: ...

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

class _StbSecColumnSrcSameShapeHDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcSameShapeBoxDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcSameShapePipeDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcSameShapeCrossDeref(_DerefAccessor):
    @property
    def shape_x(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_x_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_y(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_y_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcSameShapeTDeref(_DerefAccessor):
    @property
    def shape_h(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_h_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_t(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_t_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcNotSameShapeHDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcNotSameShapeBoxDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcNotSameShapePipeDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcNotSameShapeCrossDeref(_DerefAccessor):
    @property
    def shape_x(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_x_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_y(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_y_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcNotSameShapeTDeref(_DerefAccessor):
    @property
    def shape_h(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_h_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_t(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_t_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcThreeTypesShapeHDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcThreeTypesShapeBoxDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcThreeTypesShapePipeDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcThreeTypesShapeCrossDeref(_DerefAccessor):
    @property
    def shape_x(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_x_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...
    @property
    def shape_y(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_y_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecColumnSrcThreeTypesShapeTDeref(_DerefAccessor):
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

class _StbSecSteelBeamSStraightDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSTaperDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSJointDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSHaunchDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSFiveTypesDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSrcStraightDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSrcTaperDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSrcJointDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSrcHaunchDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

class _StbSecSteelBeamSrcFiveTypesDeref(_DerefAccessor):
    @property
    def shape(self) -> _StbSecSteelColumnSSameShape: ...
    @property
    def shape_or_none(self) -> _StbSecSteelColumnSSameShape | None: ...

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

class RepositoryV2_0_2(RepositoryBase):
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
    def deref(self, element: StbOpen) -> _StbOpenDeref: ...
    @overload
    def deref(self, element: StbOpenId) -> _StbOpenIdDeref: ...
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
    def deref(
        self, element: StbSecSteelFigureColumnS
    ) -> _StbSecSteelFigureColumnSDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelFigureColumnSrc
    ) -> _StbSecSteelFigureColumnSrcDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelFigureBeamS
    ) -> _StbSecSteelFigureBeamSDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelFigureBeamSrc
    ) -> _StbSecSteelFigureBeamSrcDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelFigureBraceS
    ) -> _StbSecSteelFigureBraceSDeref: ...
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
        self, element: StbSecColumnSrcSameShapeH
    ) -> _StbSecColumnSrcSameShapeHDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcSameShapeBox
    ) -> _StbSecColumnSrcSameShapeBoxDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcSameShapePipe
    ) -> _StbSecColumnSrcSameShapePipeDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcSameShapeCross
    ) -> _StbSecColumnSrcSameShapeCrossDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcSameShapeT
    ) -> _StbSecColumnSrcSameShapeTDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcNotSameShapeH
    ) -> _StbSecColumnSrcNotSameShapeHDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcNotSameShapeBox
    ) -> _StbSecColumnSrcNotSameShapeBoxDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcNotSameShapePipe
    ) -> _StbSecColumnSrcNotSameShapePipeDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcNotSameShapeCross
    ) -> _StbSecColumnSrcNotSameShapeCrossDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcNotSameShapeT
    ) -> _StbSecColumnSrcNotSameShapeTDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcThreeTypesShapeH
    ) -> _StbSecColumnSrcThreeTypesShapeHDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcThreeTypesShapeBox
    ) -> _StbSecColumnSrcThreeTypesShapeBoxDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcThreeTypesShapePipe
    ) -> _StbSecColumnSrcThreeTypesShapePipeDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcThreeTypesShapeCross
    ) -> _StbSecColumnSrcThreeTypesShapeCrossDeref: ...
    @overload
    def deref(
        self, element: StbSecColumnSrcThreeTypesShapeT
    ) -> _StbSecColumnSrcThreeTypesShapeTDeref: ...
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
        self, element: StbSecSteelBeamSStraight
    ) -> _StbSecSteelBeamSStraightDeref: ...
    @overload
    def deref(self, element: StbSecSteelBeamSTaper) -> _StbSecSteelBeamSTaperDeref: ...
    @overload
    def deref(self, element: StbSecSteelBeamSJoint) -> _StbSecSteelBeamSJointDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamSHaunch
    ) -> _StbSecSteelBeamSHaunchDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamSFiveTypes
    ) -> _StbSecSteelBeamSFiveTypesDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamSrcStraight
    ) -> _StbSecSteelBeamSrcStraightDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamSrcTaper
    ) -> _StbSecSteelBeamSrcTaperDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamSrcJoint
    ) -> _StbSecSteelBeamSrcJointDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamSrcHaunch
    ) -> _StbSecSteelBeamSrcHaunchDeref: ...
    @overload
    def deref(
        self, element: StbSecSteelBeamSrcFiveTypes
    ) -> _StbSecSteelBeamSrcFiveTypesDeref: ...
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
    def get_steel(
        self,
        name: str,
    ) -> (
        StbSecRollH
        | StbSecBuildH
        | StbSecRollBox
        | StbSecBuildBox
        | StbSecPipe
        | StbSecRollT
        | StbSecRollC
        | StbSecRollL
        | StbSecLipC
        | StbSecFlatBar
        | StbSecRoundBar
        | StbSecSteelProduct
        | StbSecSteelUndefined
    ): ...
