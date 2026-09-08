# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# 本ファイルはstbkit-codegenによって自動生成されました。
# このファイルを直接編集しないでください。

# 本ファイルには、大成建設株式会社がbuildingSMART Japanとの間の
# 利⽤許諾契約に基づき、buildingSMART Japanが権利を保有するST-Bridge仕様書の記述を
# 参照・転記等のうえST-Bridge仕様書に基づく実装をしている部分が含まれます。

# ST-Bridgeの権利は buildingSMART Japan に帰属します。
# 詳細な出典情報および権利関係についてはREADME.md を参照してください。
# 引用仕様書
#  - ST-Bridge XMLファイル仕様書（ver.2.0）
#     （2020.12.16 、buildingSMART Japan 構造設計小委員会）
from __future__ import annotations

from enum import IntEnum, StrEnum
from typing import ClassVar, Final
from uuid import UUID

from stbkit.core.data_model._internal.stb_types import DataType as _DT
from stbkit.core.data_model.common import StBridgeElement, StBridgeRoot
from stbkit.core.data_model.common import _FieldInfo as _FI
from stbkit.core.data_model.common import _FieldKind as _FK

VERSION: Final[str] = "2.0.2"


class StbNodeKind(StrEnum):
    """StbNode.kind で使用できる値。"""

    ON_GIRDER = "ON_GIRDER"
    ON_BEAM = "ON_BEAM"
    ON_COLUMN = "ON_COLUMN"
    ON_POST = "ON_POST"
    ON_GRID = "ON_GRID"
    ON_CANTI = "ON_CANTI"
    ON_SLAB = "ON_SLAB"
    OTHER = "OTHER"


class StbStoryKind(StrEnum):
    """StbStory.kind で使用できる値。"""

    GENERAL = "GENERAL"
    BASEMENT = "BASEMENT"
    ROOF = "ROOF"
    PENTHOUSE = "PENTHOUSE"
    ISOLATION = "ISOLATION"
    DEPENDENCE = "DEPENDENCE"


class StbColumnKindStructure(StrEnum):
    """StbColumn.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbColumnConditionBottom(StrEnum):
    """StbColumn.condition_bottom で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbColumnConditionTop(StrEnum):
    """StbColumn.condition_top で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbColumnKindJointTop(StrEnum):
    """StbColumn.kind_joint_top で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbColumnKindJointBottom(StrEnum):
    """StbColumn.kind_joint_bottom で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbPostKindStructure(StrEnum):
    """StbPost.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbPostConditionBottom(StrEnum):
    """StbPost.condition_bottom で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbPostConditionTop(StrEnum):
    """StbPost.condition_top で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbPostKindJointTop(StrEnum):
    """StbPost.kind_joint_top で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbPostKindJointBottom(StrEnum):
    """StbPost.kind_joint_bottom で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbGirderSectionIoStart(StrEnum):
    """StbGirder.section_io_start で使用できる値。"""

    OUT = "OUT"
    IN = "IN"


class StbGirderSectionIoEnd(StrEnum):
    """StbGirder.section_io_end で使用できる値。"""

    OUT = "OUT"
    IN = "IN"


class StbGirderKindStructure(StrEnum):
    """StbGirder.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    UNDEFINED = "UNDEFINED"


class StbGirderConditionStart(StrEnum):
    """StbGirder.condition_start で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbGirderConditionEnd(StrEnum):
    """StbGirder.condition_end で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbGirderKindHaunchStart(StrEnum):
    """StbGirder.kind_haunch_start で使用できる値。"""

    SLOPE = "SLOPE"
    DROP = "DROP"


class StbGirderKindHaunchEnd(StrEnum):
    """StbGirder.kind_haunch_end で使用できる値。"""

    SLOPE = "SLOPE"
    DROP = "DROP"


class StbGirderTypeHaunchH(StrEnum):
    """StbGirder.type_haunch_h で使用できる値。"""

    BOTH = "BOTH"
    RIGHT = "RIGHT"
    LEFT = "LEFT"


class StbGirderTypeHaunchV(StrEnum):
    """StbGirder.type_haunch_v で使用できる値。"""

    BOTH = "BOTH"
    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbGirderKindJointStart(StrEnum):
    """StbGirder.kind_joint_start で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbGirderKindJointEnd(StrEnum):
    """StbGirder.kind_joint_end で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbBeamSectionIoStart(StrEnum):
    """StbBeam.section_io_start で使用できる値。"""

    OUT = "OUT"
    IN = "IN"


class StbBeamSectionIoEnd(StrEnum):
    """StbBeam.section_io_end で使用できる値。"""

    OUT = "OUT"
    IN = "IN"


class StbBeamKindStructure(StrEnum):
    """StbBeam.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    UNDEFINED = "UNDEFINED"


class StbBeamConditionStart(StrEnum):
    """StbBeam.condition_start で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbBeamConditionEnd(StrEnum):
    """StbBeam.condition_end で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbBeamKindHaunchStart(StrEnum):
    """StbBeam.kind_haunch_start で使用できる値。"""

    SLOPE = "SLOPE"
    DROP = "DROP"


class StbBeamKindHaunchEnd(StrEnum):
    """StbBeam.kind_haunch_end で使用できる値。"""

    SLOPE = "SLOPE"
    DROP = "DROP"


class StbBeamTypeHaunchH(StrEnum):
    """StbBeam.type_haunch_h で使用できる値。"""

    BOTH = "BOTH"
    RIGHT = "RIGHT"
    LEFT = "LEFT"


class StbBeamTypeHaunchV(StrEnum):
    """StbBeam.type_haunch_v で使用できる値。"""

    BOTH = "BOTH"
    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbBeamKindJointStart(StrEnum):
    """StbBeam.kind_joint_start で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbBeamKindJointEnd(StrEnum):
    """StbBeam.kind_joint_end で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbBraceKindStructure(StrEnum):
    """StbBrace.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"


class StbBraceConditionStart(StrEnum):
    """StbBrace.condition_start で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbBraceConditionEnd(StrEnum):
    """StbBrace.condition_end で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"


class StbBraceFeatureBrace(StrEnum):
    """StbBrace.feature_brace で使用できる値。"""

    TENSION = "TENSION"
    TENSIONANDCOMPRESSION = "TENSIONANDCOMPRESSION"


class StbBraceKindJointStart(StrEnum):
    """StbBrace.kind_joint_start で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbBraceKindJointEnd(StrEnum):
    """StbBrace.kind_joint_end で使用できる値。"""

    BOLT = "BOLT"
    WBOLT = "WBOLT"
    WELD = "WELD"


class StbSlabKindStructure(StrEnum):
    """StbSlab.kind_structure で使用できる値。"""

    RC = "RC"
    DECK = "DECK"
    PRECAST = "PRECAST"


class StbSlabKindSlab(StrEnum):
    """StbSlab.kind_slab で使用できる値。"""

    NORMAL = "NORMAL"
    CANTI = "CANTI"


class StbSlabDirectionLoad(StrEnum):
    """StbSlab.direction_load で使用できる値。"""

    VALUE_1_WAY = "1WAY"
    VALUE_2_WAY = "2WAY"


class StbSlabTypeHaunch(StrEnum):
    """StbSlab.type_haunch で使用できる値。"""

    BOTH = "BOTH"
    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbWallKindLayout(StrEnum):
    """StbWall.kind_layout で使用できる値。"""

    ON_GIRDER = "ON_GIRDER"
    ON_BEAM = "ON_BEAM"
    ON_SLAB = "ON_SLAB"


class StbWallKindWall(StrEnum):
    """StbWall.kind_wall で使用できる値。"""

    WALL_NORMAL = "WALL_NORMAL"
    WALL_SHEAR = "WALL_SHEAR"


class StbWallTypeOutside(StrEnum):
    """StbWall.type_outside で使用できる値。"""

    TYPE_PLUS = "TYPE_PLUS"
    TYPE_MINUS = "TYPE_MINUS"


class StbPileKindStructure(StrEnum):
    """StbPile.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    PC = "PC"


class StbParapetKindLayout(StrEnum):
    """StbParapet.kind_layout で使用できる値。"""

    ON_GIRDER = "ON_GIRDER"
    ON_BEAM = "ON_BEAM"
    ON_SLAB = "ON_SLAB"


class StbParapetDirection(StrEnum):
    """StbParapet.direction で使用できる値。"""

    R = "R"
    L = "L"


class StbSecColumnRcKindColumn(StrEnum):
    """StbSecColumnRc.kind_column で使用できる値。"""

    COLUMN = "COLUMN"
    POST = "POST"


class StbSecBarArrangementColumnRcKindCorner(StrEnum):
    """StbSecBarArrangementColumnRc.kind_corner で使用できる値。"""

    NONE = "NONE"
    DIR_X = "DIR_X"
    DIR_Y = "DIR_Y"
    DIR_XY = "DIR_XY"


class StbSecBarColumnRcRectNotSamePos(StrEnum):
    """StbSecBarColumnRcRectNotSame.pos で使用できる値。"""

    BASE = "BASE"
    TOP = "TOP"


class StbSecBarColumnRcCircleNotSamePos(StrEnum):
    """StbSecBarColumnRcCircleNotSame.pos で使用できる値。"""

    BASE = "BASE"
    TOP = "TOP"


class StbSecColumnSKindColumn(StrEnum):
    """StbSecColumnS.kind_column で使用できる値。"""

    COLUMN = "COLUMN"
    POST = "POST"


class StbSecSteelFigureColumnSBaseType(StrEnum):
    """StbSecSteelFigureColumnS.base_type で使用できる値。"""

    NONE = "NONE"
    EXPOSE = "EXPOSE"
    EMBEDDED = "EMBEDDED"
    WRAP = "WRAP"


class StbSecSteelColumnSNotSamePos(StrEnum):
    """StbSecSteelColumnSNotSame.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecSteelColumnSThreeTypesPos(StrEnum):
    """StbSecSteelColumnSThreeTypes.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    CENTER = "CENTER"
    TOP = "TOP"


class StbSecBaseProductSDirectionType(IntEnum):
    """StbSecBaseProductS.direction_type で使用できる値。"""

    VALUE_0 = 0
    VALUE_90 = 90
    VALUE_180 = 180
    VALUE_270 = 270


class StbSecBaseConventionalSAnchorBoltKindBolt(StrEnum):
    """StbSecBaseConventionalSAnchorBolt.kind_bolt で使用できる値。"""

    STD = "STD"
    ABR = "ABR"
    ABM = "ABM"


class StbSecBaseConventionalSAnchorBoltArrangementBolt(StrEnum):
    """StbSecBaseConventionalSAnchorBolt.arrangement_bolt で使用できる値。"""

    STD = "STD"
    CUT = "CUT"


class StbSecColumnSrcKindColumn(StrEnum):
    """StbSecColumnSrc.kind_column で使用できる値。"""

    COLUMN = "COLUMN"
    POST = "POST"


class StbSecBarArrangementColumnSrcKindCorner(StrEnum):
    """StbSecBarArrangementColumnSrc.kind_corner で使用できる値。"""

    NONE = "NONE"
    DIR_X = "DIR_X"
    DIR_Y = "DIR_Y"
    DIR_XY = "DIR_XY"


class StbSecBarColumnSrcRectNotSamePos(StrEnum):
    """StbSecBarColumnSrcRectNotSame.pos で使用できる値。"""

    BASE = "BASE"
    TOP = "TOP"


class StbSecBarColumnSrcCircleNotSamePos(StrEnum):
    """StbSecBarColumnSrcCircleNotSame.pos で使用できる値。"""

    BASE = "BASE"
    TOP = "TOP"


class StbSecSteelFigureColumnSrcBaseType(StrEnum):
    """StbSecSteelFigureColumnSrc.base_type で使用できる値。"""

    NONE = "NONE"
    UNEMBEDDED = "UNEMBEDDED"
    UNEMBEDDED2 = "UNEMBEDDED2"
    EMBEDDED = "EMBEDDED"


class StbSecColumnSrcSameShapeHDirectionType(StrEnum):
    """StbSecColumnSrcSameShapeH.direction_type で使用できる値。"""

    H = "H"
    I = "I"


class StbSecColumnSrcSameShapeBoxEncaseType(StrEnum):
    """StbSecColumnSrcSameShapeBox.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecColumnSrcSameShapePipeEncaseType(StrEnum):
    """StbSecColumnSrcSameShapePipe.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecColumnSrcSameShapeTDirectionType(StrEnum):
    """StbSecColumnSrcSameShapeT.direction_type で使用できる値。"""

    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4 = "T4"


class StbSecSteelColumnSrcNotSamePos(StrEnum):
    """StbSecSteelColumnSrcNotSame.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecColumnSrcNotSameShapeHDirectionType(StrEnum):
    """StbSecColumnSrcNotSameShapeH.direction_type で使用できる値。"""

    H = "H"
    I = "I"


class StbSecColumnSrcNotSameShapeBoxEncaseType(StrEnum):
    """StbSecColumnSrcNotSameShapeBox.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecColumnSrcNotSameShapePipeEncaseType(StrEnum):
    """StbSecColumnSrcNotSameShapePipe.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecColumnSrcNotSameShapeTDirectionType(StrEnum):
    """StbSecColumnSrcNotSameShapeT.direction_type で使用できる値。"""

    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4 = "T4"


class StbSecSteelColumnSrcThreeTypesPos(StrEnum):
    """StbSecSteelColumnSrcThreeTypes.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    CENTER = "CENTER"
    TOP = "TOP"


class StbSecColumnSrcThreeTypesShapeHDirectionType(StrEnum):
    """StbSecColumnSrcThreeTypesShapeH.direction_type で使用できる値。"""

    H = "H"
    I = "I"


class StbSecColumnSrcThreeTypesShapeBoxEncaseType(StrEnum):
    """StbSecColumnSrcThreeTypesShapeBox.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecColumnSrcThreeTypesShapePipeEncaseType(StrEnum):
    """StbSecColumnSrcThreeTypesShapePipe.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecColumnSrcThreeTypesShapeTDirectionType(StrEnum):
    """StbSecColumnSrcThreeTypesShapeT.direction_type で使用できる値。"""

    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4 = "T4"


class StbSecBaseProductSrcDirectionType(IntEnum):
    """StbSecBaseProductSrc.direction_type で使用できる値。"""

    VALUE_0 = 0
    VALUE_90 = 90
    VALUE_180 = 180
    VALUE_270 = 270


class StbSecBaseConventionalSrcAnchorBoltKindBolt(StrEnum):
    """StbSecBaseConventionalSrcAnchorBolt.kind_bolt で使用できる値。"""

    STD = "STD"
    ABR = "ABR"
    ABM = "ABM"


class StbSecBaseConventionalSrcAnchorBoltArrangementBolt(StrEnum):
    """StbSecBaseConventionalSrcAnchorBolt.arrangement_bolt で使用できる値。"""

    STD = "STD"
    CUT = "CUT"


class StbSecColumnCftKindColumn(StrEnum):
    """StbSecColumnCft.kind_column で使用できる値。"""

    COLUMN = "COLUMN"
    POST = "POST"


class StbSecSteelFigureColumnCftBaseType(StrEnum):
    """StbSecSteelFigureColumnCft.base_type で使用できる値。"""

    NONE = "NONE"
    EXPOSE = "EXPOSE"
    EMBEDDED = "EMBEDDED"


class StbSecSteelColumnCftNotSamePos(StrEnum):
    """StbSecSteelColumnCftNotSame.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecSteelColumnCftThreeTypesPos(StrEnum):
    """StbSecSteelColumnCftThreeTypes.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    CENTER = "CENTER"
    TOP = "TOP"


class StbSecBaseProductCftDirectionType(IntEnum):
    """StbSecBaseProductCft.direction_type で使用できる値。"""

    VALUE_0 = 0
    VALUE_90 = 90
    VALUE_180 = 180
    VALUE_270 = 270


class StbSecBaseConventionalCftAnchorBoltKindBolt(StrEnum):
    """StbSecBaseConventionalCftAnchorBolt.kind_bolt で使用できる値。"""

    STD = "STD"
    ABR = "ABR"
    ABM = "ABM"


class StbSecBaseConventionalCftAnchorBoltArrangementBolt(StrEnum):
    """StbSecBaseConventionalCftAnchorBolt.arrangement_bolt で使用できる値。"""

    STD = "STD"
    CUT = "CUT"


class StbSecBeamRcKindBeam(StrEnum):
    """StbSecBeamRc.kind_beam で使用できる値。"""

    GIRDER = "GIRDER"
    BEAM = "BEAM"


class StbSecBeamRcTaperPos(StrEnum):
    """StbSecBeamRcTaper.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbSecBeamRcHaunchPos(StrEnum):
    """StbSecBeamRcHaunch.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecBarBeamRcThreeTypesPos(StrEnum):
    """StbSecBarBeamRcThreeTypes.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecBarBeamRcStartEndPos(StrEnum):
    """StbSecBarBeamRcStartEnd.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbSecBeamSKindBeam(StrEnum):
    """StbSecBeamS.kind_beam で使用できる値。"""

    GIRDER = "GIRDER"
    BEAM = "BEAM"


class StbSecSteelBeamSTaperPos(StrEnum):
    """StbSecSteelBeamSTaper.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbSecSteelBeamSJointPos(StrEnum):
    """StbSecSteelBeamSJoint.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecSteelBeamSHaunchPos(StrEnum):
    """StbSecSteelBeamSHaunch.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecSteelBeamSFiveTypesPos(StrEnum):
    """StbSecSteelBeamSFiveTypes.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"
    HAUNCH_S = "HAUNCH_S"
    HAUNCH_E = "HAUNCH_E"


class StbSecBeamSrcKindBeam(StrEnum):
    """StbSecBeamSrc.kind_beam で使用できる値。"""

    GIRDER = "GIRDER"
    BEAM = "BEAM"


class StbSecBeamSrcTaperPos(StrEnum):
    """StbSecBeamSrcTaper.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbSecBeamSrcHaunchPos(StrEnum):
    """StbSecBeamSrcHaunch.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecBarBeamSrcThreeTypesPos(StrEnum):
    """StbSecBarBeamSrcThreeTypes.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecBarBeamSrcStartEndPos(StrEnum):
    """StbSecBarBeamSrcStartEnd.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbSecSteelBeamSrcTaperPos(StrEnum):
    """StbSecSteelBeamSrcTaper.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbSecSteelBeamSrcJointPos(StrEnum):
    """StbSecSteelBeamSrcJoint.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecSteelBeamSrcHaunchPos(StrEnum):
    """StbSecSteelBeamSrcHaunch.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"


class StbSecSteelBeamSrcFiveTypesPos(StrEnum):
    """StbSecSteelBeamSrcFiveTypes.pos で使用できる値。"""

    START = "START"
    CENTER = "CENTER"
    END = "END"
    HAUNCH_S = "HAUNCH_S"
    HAUNCH_E = "HAUNCH_E"


class StbSecBraceSKindBrace(StrEnum):
    """StbSecBraceS.kind_brace で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class StbSecSteelBraceSNotSamePos(StrEnum):
    """StbSecSteelBraceSNotSame.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecSteelBraceSThreeTypesPos(StrEnum):
    """StbSecSteelBraceSThreeTypes.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    CENTER = "CENTER"
    TOP = "TOP"


class StbSecSlabRcTaperPos(StrEnum):
    """StbSecSlabRcTaper.pos で使用できる値。"""

    BASE = "BASE"
    TIP = "TIP"


class StbSecSlabRcHaunchPos(StrEnum):
    """StbSecSlabRcHaunch.pos で使用できる値。"""

    BASE = "BASE"
    CENTER = "CENTER"
    HAUNCH = "HAUNCH"


class StbSecBarSlabRcStandardPos(StrEnum):
    """StbSecBarSlabRcStandard.pos で使用できる値。"""

    SHORT_TOP_COLUMN = "SHORT_TOP_COLUMN"
    SHORT_TOP_MID_END = "SHORT_TOP_MID_END"
    SHORT_TOP_MID_CENTER = "SHORT_TOP_MID_CENTER"
    SHORT_BOTTOM_COLUMN = "SHORT_BOTTOM_COLUMN"
    SHORT_BOTTOM_MID_END = "SHORT_BOTTOM_MID_END"
    SHORT_BOTTOM_MID_CENTER = "SHORT_BOTTOM_MID_CENTER"
    LONG_TOP_COLUMN = "LONG_TOP_COLUMN"
    LONG_TOP_MID_END = "LONG_TOP_MID_END"
    LONG_TOP_MID_CENTER = "LONG_TOP_MID_CENTER"
    LONG_BOTTOM_COLUMN = "LONG_BOTTOM_COLUMN"
    LONG_BOTTOM_MID_END = "LONG_BOTTOM_MID_END"
    LONG_BOTTOM_MID_CENTER = "LONG_BOTTOM_MID_CENTER"


class StbSecBarSlabRc2WayPos(StrEnum):
    """StbSecBarSlabRc2Way.pos で使用できる値。"""

    SHORT_TOP = "SHORT_TOP"
    SHORT_BOTTOM = "SHORT_BOTTOM"
    LONG_TOP = "LONG_TOP"
    LONG_BOTTOM = "LONG_BOTTOM"


class StbSecBarSlabRc1Way1Pos(StrEnum):
    """StbSecBarSlabRc1Way1.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"


class StbSecBarSlabRc1Way2Pos(StrEnum):
    """StbSecBarSlabRc1Way2.pos で使用できる値。"""

    MAIN_BASE_TOP = "MAIN_BASE_TOP"
    MAIN_BASE_BOTTOM = "MAIN_BASE_BOTTOM"
    MAIN_TIP_TOP = "MAIN_TIP_TOP"
    MAIN_TIP_BOTTOM = "MAIN_TIP_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"


class StbSecBarSlabRcOpenPos(StrEnum):
    """StbSecBarSlabRcOpen.pos で使用できる値。"""

    X_TOP = "X_TOP"
    X_BOTTOM = "X_BOTTOM"
    Y_TOP = "Y_TOP"
    Y_BOTTOM = "Y_BOTTOM"
    DIAGONAL_TOP = "DIAGONAL_TOP"
    DIAGONAL_BOTTOM = "DIAGONAL_BOTTOM"


class StbSecSlabDeckProductType(StrEnum):
    """StbSecSlabDeck.product_type で使用できる値。"""

    FLAT = "FLAT"
    COMPOSITE = "COMPOSITE"


class StbSecBarSlabDeckStandardPos(StrEnum):
    """StbSecBarSlabDeckStandard.pos で使用できる値。"""

    SHORT_TOP_COLUMN = "SHORT_TOP_COLUMN"
    SHORT_TOP_MID_END = "SHORT_TOP_MID_END"
    SHORT_TOP_MID_CENTER = "SHORT_TOP_MID_CENTER"
    SHORT_BOTTOM_COLUMN = "SHORT_BOTTOM_COLUMN"
    SHORT_BOTTOM_MID_END = "SHORT_BOTTOM_MID_END"
    SHORT_BOTTOM_MID_CENTER = "SHORT_BOTTOM_MID_CENTER"
    LONG_TOP_COLUMN = "LONG_TOP_COLUMN"
    LONG_TOP_MID_END = "LONG_TOP_MID_END"
    LONG_TOP_MID_CENTER = "LONG_TOP_MID_CENTER"
    LONG_BOTTOM_COLUMN = "LONG_BOTTOM_COLUMN"
    LONG_BOTTOM_MID_END = "LONG_BOTTOM_MID_END"
    LONG_BOTTOM_MID_CENTER = "LONG_BOTTOM_MID_CENTER"


class StbSecBarSlabDeck2WayPos(StrEnum):
    """StbSecBarSlabDeck2Way.pos で使用できる値。"""

    SHORT_TOP = "SHORT_TOP"
    SHORT_BOTTOM = "SHORT_BOTTOM"
    LONG_TOP = "LONG_TOP"
    LONG_BOTTOM = "LONG_BOTTOM"


class StbSecBarSlabDeck1WayPos(StrEnum):
    """StbSecBarSlabDeck1Way.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"
    REFRACTORY = "REFRACTORY"


class StbSecSlabPrecastPrecastType(StrEnum):
    """StbSecSlabPrecast.precast_type で使用できる値。"""

    FULL = "FULL"
    HALF = "HALF"
    FORM = "FORM"


class StbSecBarSlabPrecastStandardPos(StrEnum):
    """StbSecBarSlabPrecastStandard.pos で使用できる値。"""

    SHORT_TOP_COLUMN = "SHORT_TOP_COLUMN"
    SHORT_TOP_MID_END = "SHORT_TOP_MID_END"
    SHORT_TOP_MID_CENTER = "SHORT_TOP_MID_CENTER"
    SHORT_BOTTOM_COLUMN = "SHORT_BOTTOM_COLUMN"
    SHORT_BOTTOM_MID_END = "SHORT_BOTTOM_MID_END"
    SHORT_BOTTOM_MID_CENTER = "SHORT_BOTTOM_MID_CENTER"
    LONG_TOP_COLUMN = "LONG_TOP_COLUMN"
    LONG_TOP_MID_END = "LONG_TOP_MID_END"
    LONG_TOP_MID_CENTER = "LONG_TOP_MID_CENTER"
    LONG_BOTTOM_COLUMN = "LONG_BOTTOM_COLUMN"
    LONG_BOTTOM_MID_END = "LONG_BOTTOM_MID_END"
    LONG_BOTTOM_MID_CENTER = "LONG_BOTTOM_MID_CENTER"


class StbSecBarSlabPrecast2WayPos(StrEnum):
    """StbSecBarSlabPrecast2Way.pos で使用できる値。"""

    SHORT_TOP = "SHORT_TOP"
    SHORT_BOTTOM = "SHORT_BOTTOM"
    LONG_TOP = "LONG_TOP"
    LONG_BOTTOM = "LONG_BOTTOM"


class StbSecBarSlabPrecast1WayPos(StrEnum):
    """StbSecBarSlabPrecast1Way.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"
    REFRACTORY = "REFRACTORY"


class StbSecBarWallRcSinglePos(StrEnum):
    """StbSecBarWallRcSingle.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarWallRcZigzagPos(StrEnum):
    """StbSecBarWallRcZigzag.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarWallRcDoubleNetPos(StrEnum):
    """StbSecBarWallRcDoubleNet.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarWallRcInsideAndOutsidePos(StrEnum):
    """StbSecBarWallRcInsideAndOutside.pos で使用できる値。"""

    VERTICAL_OUTSIDE = "VERTICAL_OUTSIDE"
    VERTICAL_INSIDE = "VERTICAL_INSIDE"
    HORIZONTAL_OUTSIDE = "HORIZONTAL_OUTSIDE"
    HORIZONTAL_INSIDE = "HORIZONTAL_INSIDE"


class StbSecBarWallRcInsideAndOutsidePos2(StrEnum):
    """StbSecBarWallRcInsideAndOutside.pos2 で使用できる値。"""

    ALL = "ALL"
    TOP_START = "TOP_START"
    MIDDLE = "MIDDLE"
    BOTTOM_END = "BOTTOM_END"


class StbSecBarWallRcEdgePos(StrEnum):
    """StbSecBarWallRcEdge.pos で使用できる値。"""

    VERTICAL_START = "VERTICAL_START"
    VERTICAL_END = "VERTICAL_END"
    HORIZONTAL_BOTTOM = "HORIZONTAL_BOTTOM"
    HORIZONTAL_TOP = "HORIZONTAL_TOP"


class StbSecBarWallRcOpenPos(StrEnum):
    """StbSecBarWallRcOpen.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    DIAGONAL = "DIAGONAL"


class StbSecFoundationRcContinuousType(StrEnum):
    """StbSecFoundationRcContinuous.type で使用できる値。"""

    RIGHT_L = "RIGHT_L"
    LEFT_L = "LEFT_L"
    REVERSE_T = "REVERSE_T"


class StbSecBarFoundationRcRectPos(StrEnum):
    """StbSecBarFoundationRcRect.pos で使用できる値。"""

    X_TOP = "X_TOP"
    X_BOTTOM = "X_BOTTOM"
    Y_TOP = "Y_TOP"
    Y_BOTTOM = "Y_BOTTOM"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarFoundationRcTrianglePos(StrEnum):
    """StbSecBarFoundationRcTriangle.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarFoundationRcThreeWayPos(StrEnum):
    """StbSecBarFoundationRcThreeWay.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    OUTSIDE_TOP = "OUTSIDE_TOP"
    OUTSIDE_BOTTOM = "OUTSIDE_BOTTOM"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarFoundationRcContinuousPos(StrEnum):
    """StbSecBarFoundationRcContinuous.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarPileRcTopBottomPos(StrEnum):
    """StbSecBarPileRcTopBottom.pos で使用できる値。"""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbSecBarPileRcTopCenterBottomPos(StrEnum):
    """StbSecBarPileRcTopCenterBottom.pos で使用できる値。"""

    TOP = "TOP"
    CENTER = "CENTER"
    BOTTOM = "BOTTOM"


class StbSecBarOpenRcSlabPos(StrEnum):
    """StbSecBarOpenRcSlab.pos で使用できる値。"""

    X_TOP = "X_TOP"
    X_BOTTOM = "X_BOTTOM"
    Y_TOP = "Y_TOP"
    Y_BOTTOM = "Y_BOTTOM"
    DIAGONAL_TOP = "DIAGONAL_TOP"
    DIAGONAL_BOTTOM = "DIAGONAL_BOTTOM"


class StbSecBarOpenRcWallPos(StrEnum):
    """StbSecBarOpenRcWall.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    DIAGONAL = "DIAGONAL"


class StbSecBarParapetRcSinglePos(StrEnum):
    """StbSecBarParapetRcSingle.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarParapetRcZigzagPos(StrEnum):
    """StbSecBarParapetRcZigzag.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarParapetRcDoubleNetPos(StrEnum):
    """StbSecBarParapetRcDoubleNet.pos で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarParapetRcTipPos(StrEnum):
    """StbSecBarParapetRcTip.pos で使用できる値。"""

    SHORT_SIDE = "SHORT_SIDE"
    LONG_SIDE = "LONG_SIDE"


class StbSecBarParapetRcEdgePos(StrEnum):
    """StbSecBarParapetRcEdge.pos で使用できる値。"""

    VERTICAL_START = "VERTICAL_START"
    VERTICAL_END = "VERTICAL_END"
    HORIZONTAL_TOP = "HORIZONTAL_TOP"
    HORIZONTAL_BOTTOM = "HORIZONTAL_BOTTOM"


class StbSecRollHType(StrEnum):
    """StbSecRollH.type で使用できる値。"""

    H = "H"
    SH = "SH"


class StbSecRollBoxType(StrEnum):
    """StbSecRollBox.type で使用できる値。"""

    BCP = "BCP"
    BCR = "BCR"
    STKR = "STKR"
    ELSE = "ELSE"


class StbSecRollTType(StrEnum):
    """StbSecRollT.type で使用できる値。"""

    T = "T"
    ST = "ST"


class StbSecRollCType(StrEnum):
    """StbSecRollC.type で使用できる値。"""

    SINGLE = "SINGLE"
    BACKTOBACK = "BACKTOBACK"
    FACETOFACE = "FACETOFACE"


class StbSecRollLType(StrEnum):
    """StbSecRollL.type で使用できる値。"""

    SINGLE = "SINGLE"
    BACKTOBACK = "BACKTOBACK"
    FACETOFACE = "FACETOFACE"


class StbSecLipCType(StrEnum):
    """StbSecLipC.type で使用できる値。"""

    SINGLE = "SINGLE"
    BACKTOBACK = "BACKTOBACK"
    FACETOFACE = "FACETOFACE"


class StbExtPropertyType(StrEnum):
    """StbExtProperty.type で使用できる値。"""

    STRING = "string"
    INTEGER = "integer"
    DOUBLE = "double"
    BOOLEAN = "boolean"


class StbExtPropertyDefType(StrEnum):
    """StbExtPropertyDef.type で使用できる値。"""

    STRING = "string"
    INTEGER = "integer"
    DOUBLE = "double"
    BOOLEAN = "boolean"


class StbCalSeismicConditionSoil(IntEnum):
    """StbCalSeismicCondition.soil で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalWindConditionRoughness(IntEnum):
    """StbCalWindCondition.roughness で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class StbCalLiveloadType(IntEnum):
    """StbCalLiveload.type で使用できる値。"""

    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7


class StbCalColumnKindStructure(StrEnum):
    """StbCalColumn.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbCalGirderSectionIoStart(StrEnum):
    """StbCalGirder.section_io_start で使用できる値。"""

    OUT = "OUT"
    IN = "IN"
    CENTER = "CENTER"


class StbCalGirderSectionIoEnd(StrEnum):
    """StbCalGirder.section_io_end で使用できる値。"""

    OUT = "OUT"
    IN = "IN"
    CENTER = "CENTER"


class StbCalGirderKindStructure(StrEnum):
    """StbCalGirder.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    UNDEFINED = "UNDEFINED"


class StbCalGirderKindHaunchStart(StrEnum):
    """StbCalGirder.kind_haunch_start で使用できる値。"""

    SLOPE = "SLOPE"
    DROP = "DROP"


class StbCalGirderKindHaunchEnd(StrEnum):
    """StbCalGirder.kind_haunch_end で使用できる値。"""

    SLOPE = "SLOPE"
    DROP = "DROP"


class StbCalGirderTypeHaunchH(StrEnum):
    """StbCalGirder.type_haunch_h で使用できる値。"""

    BOTH = "BOTH"
    RIGHT = "RIGHT"
    LEFT = "LEFT"


class StbCalGirderTypeHaunchV(StrEnum):
    """StbCalGirder.type_haunch_v で使用できる値。"""

    BOTH = "BOTH"
    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbCalFinishRcTypeGirder(IntEnum):
    """StbCalFinishRc.type_girder で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFinishRcTypeColumn(IntEnum):
    """StbCalFinishRc.type_column で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFinishRcTypeBeam(IntEnum):
    """StbCalFinishRc.type_beam で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFinishRcTypeCanti(IntEnum):
    """StbCalFinishRc.type_canti で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFinishRcTypeWall(IntEnum):
    """StbCalFinishRc.type_wall で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFinishSMemberMemberType(StrEnum):
    """StbCalFinishSMember.member_type で使用できる値。"""

    COLUMN = "COLUMN"
    GIRDER = "GIRDER"
    BEAM = "BEAM"
    CANTI = "CANTI"
    BRACE = "BRACE"


class StbCalFinishSMemberCoveringType(StrEnum):
    """StbCalFinishSMember.covering_type で使用できる値。"""

    A = "A"
    B = "B"
    C = "C"
    D = "D"


class StbCalFloorFinishRcTypeGirder(IntEnum):
    """StbCalFloorFinishRc.type_girder で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFloorFinishRcTypeColumn(IntEnum):
    """StbCalFloorFinishRc.type_column で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFloorFinishRcTypeBeam(IntEnum):
    """StbCalFloorFinishRc.type_beam で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFloorFinishRcTypeCanti(IntEnum):
    """StbCalFloorFinishRc.type_canti で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFloorFinishRcTypeWall(IntEnum):
    """StbCalFloorFinishRc.type_wall で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalFloorFinishSMemberMemberType(StrEnum):
    """StbCalFloorFinishSMember.member_type で使用できる値。"""

    COLUMN = "COLUMN"
    GIRDER = "GIRDER"
    BEAM = "BEAM"
    CANTI = "CANTI"
    BRACE = "BRACE"


class StbCalFloorFinishSMemberCoveringType(StrEnum):
    """StbCalFloorFinishSMember.covering_type で使用できる値。"""

    A = "A"
    B = "B"
    C = "C"
    D = "D"


class StbCalColumnFinishRcType(IntEnum):
    """StbCalColumnFinishRc.type で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalGirderFinishRcType(IntEnum):
    """StbCalGirderFinishRc.type で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalWallFinishRcType(IntEnum):
    """StbCalWallFinishRc.type で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalColumnFinishSType(IntEnum):
    """StbCalColumnFinishS.type で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalColumnFinishSCoveringType(StrEnum):
    """StbCalColumnFinishS.covering_type で使用できる値。"""

    A = "A"
    B = "B"
    C = "C"
    D = "D"


class StbCalGirderFinishSType(IntEnum):
    """StbCalGirderFinishS.type で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalGirderFinishSCoveringType(StrEnum):
    """StbCalGirderFinishS.covering_type で使用できる値。"""

    A = "A"
    B = "B"
    C = "C"
    D = "D"


class StbCalBraceFinishSType(IntEnum):
    """StbCalBraceFinishS.type で使用できる値。"""

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class StbCalBraceFinishSCoveringType(StrEnum):
    """StbCalBraceFinishS.covering_type で使用できる値。"""

    A = "A"
    B = "B"
    C = "C"
    D = "D"


class StbCalLoadCaseCategory(StrEnum):
    """StbCalLoadCase.category で使用できる値。"""

    STANDARD = "STANDARD"
    ANALYSIS = "ANALYSIS"


class StbCalLoadCaseKind(StrEnum):
    """StbCalLoadCase.kind で使用できる値。"""

    DL = "DL"
    LL_F = "LLf"
    LL_E = "LLe"
    TL = "TL"
    S = "S"
    K = "K"
    W = "W"
    OTHER = "OTHER"


class StbCalMemberLoadCoordinateLoad(StrEnum):
    """StbCalMemberLoad.coordinate_load で使用できる値。"""

    LOCAL = "LOCAL"
    GLOBAL = "GLOBAL"
    PROJECTION = "PROJECTION"


class StbCalMemberLoadDirectionLoad(StrEnum):
    """StbCalMemberLoad.direction_load で使用できる値。"""

    X = "X"
    Y = "Y"


class StbCalAreaLoadType(IntEnum):
    """StbCalAreaLoad.type で使用できる値。"""

    VALUE_51 = 51
    VALUE_52 = 52


class StbCalAreaLoadCoordinateLoad(StrEnum):
    """StbCalAreaLoad.coordinate_load で使用できる値。"""

    LOCAL = "LOCAL"
    GLOBAL = "GLOBAL"
    PROJECTION = "PROJECTION"


class StbCalEarthHydrostaticPressureLoadCoordinateLoad(StrEnum):
    """StbCalEarthHydrostaticPressureLoad.coordinate_load で使用できる値。"""

    PLUS = "plus"
    MINUS = "minus"


class StbCalColumnConditionBottomX(StrEnum):
    """StbCalColumnCondition.bottom_x で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalColumnConditionBottomY(StrEnum):
    """StbCalColumnCondition.bottom_y で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalColumnConditionTopX(StrEnum):
    """StbCalColumnCondition.top_x で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalColumnConditionTopY(StrEnum):
    """StbCalColumnCondition.top_y で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalGirderConditionStart(StrEnum):
    """StbCalGirderCondition.start で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalGirderConditionEnd(StrEnum):
    """StbCalGirderCondition.end で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalNodeRestrictionEX(StrEnum):
    """StbCalNodeRestriction.e_x で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"
    SPRING = "SPRING"


class StbCalNodeRestrictionEY(StrEnum):
    """StbCalNodeRestriction.e_y で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"
    SPRING = "SPRING"


class StbCalNodeRestrictionEZ(StrEnum):
    """StbCalNodeRestriction.e_z で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"
    SPRING = "SPRING"


class StbCalNodeRestrictionRX(StrEnum):
    """StbCalNodeRestriction.r_x で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"
    SPRING = "SPRING"


class StbCalNodeRestrictionRY(StrEnum):
    """StbCalNodeRestriction.r_y で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"
    SPRING = "SPRING"


class StbCalNodeRestrictionRZ(StrEnum):
    """StbCalNodeRestriction.r_z で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"
    SPRING = "SPRING"


class StbAnaBoundaryX(StrEnum):
    """StbAnaBoundary.x で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"


class StbAnaBoundaryY(StrEnum):
    """StbAnaBoundary.y で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"


class StbAnaBoundaryZ(StrEnum):
    """StbAnaBoundary.z で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"


class StbAnaBoundaryTx(StrEnum):
    """StbAnaBoundary.tx で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"


class StbAnaBoundaryTy(StrEnum):
    """StbAnaBoundary.ty で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"


class StbAnaBoundaryTz(StrEnum):
    """StbAnaBoundary.tz で使用できる値。"""

    FIX = "FIX"
    FREE = "FREE"


class StbAnaMemberidKind(StrEnum):
    """StbAnaMemberid.kind で使用できる値。"""

    STB_ANA_BEAM = "StbAnaBeam"
    STB_ANA_TRUSS = "StbAnaTruss"
    STB_ANA_SUPPORT = "StbAnaSupport"
    STB_ANA_SPRING = "StbAnaSpring"
    STB_ANA_WALL = "StbAnaWall"
    STB_ANA_PLANE_TRIANGLE = "StbAnaPlaneTriangle"
    STB_ANA_PLANE_RECTANGLE = "StbAnaPlaneRectangle"
    STB_ANA_NODE_PANEL = "StbAnaNodePanel"


class StbAnaSupportDirection(StrEnum):
    """StbAnaSupport.direction で使用できる値。"""

    UX = "UX"
    UY = "UY"
    UZ = "UZ"
    TX = "TX"
    TY = "TY"
    TZ = "TZ"


class StbAnaSpringDirection(StrEnum):
    """StbAnaSpring.direction で使用できる値。"""

    UX = "UX"
    UY = "UY"
    UZ = "UZ"
    TX = "TX"
    TY = "TY"
    TZ = "TZ"
    AXIAL = "AXIAL"


class StbAnaPlanePropertyElementType(StrEnum):
    """StbAnaPlaneProperty.element_type で使用できる値。"""

    PLANE_STRESS = "PLANE_STRESS"
    PLANE_STRAIN = "PLANE_STRAIN"


class StbAnaMemberRelMemberKind(StrEnum):
    """StbAnaMemberRel.member_kind で使用できる値。"""

    STB_COLUMN = "StbColumn"
    STB_POST = "StbPost"
    STB_GIRDER = "StbGirder"
    STB_BEAM = "StbBeam"
    STB_BRACE = "StbBrace"
    STB_SLAB = "StbSlab"
    STB_WALL = "StbWall"


class StbAnaCalMemberRelMemberKind(StrEnum):
    """StbAnaCalMemberRel.member_kind で使用できる値。"""

    STB_CAL_COLUMN = "StbCalColumn"
    STB_CAL_GIRDER = "StbCalGirder"


class StbAnaPropertyRelSectionKind(StrEnum):
    """StbAnaPropertyRel.section_kind で使用できる値。"""

    STB_SEC_COLUMN_RC = "StbSecColumn_RC"
    STB_SEC_COLUMN_S = "StbSecColumn_S"
    STB_SEC_COLUMN_SRC = "StbSecColumn_SRC"
    STB_SEC_COLUMN_CFT = "StbSecColumn_CFT"
    STB_SEC_BEAM_RC = "StbSecBeam_RC"
    STB_SEC_BEAM_S = "StbSecBeam_S"
    STB_SEC_BEAM_SRC = "StbSecBeam_SRC"
    STB_SEC_BRACE_S = "StbSecBrace_S"
    STB_SEC_SLAB_RC = "StbSecSlab_RC"
    STB_SEC_SLAB_DECK = "StbSecSlabDeck"
    STB_SEC_SLAB_PRECAST = "StbSecSlabPrecast"
    STB_SEC_WALL_RC = "StbSecWall_RC"


class StbAnaPropertyRel(StBridgeElement):
    """StbAnaPropertyRel

    Attributes:
        id_ana_property (int): 属性
        section_kind (StbAnaPropertyRelSectionKind): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_kind": _FI(
            py_type=StbAnaPropertyRelSectionKind,
            data_type=_DT.STR_ENUM,
            choices=(
                "StbSecColumn_RC",
                "StbSecColumn_S",
                "StbSecColumn_SRC",
                "StbSecColumn_CFT",
                "StbSecBeam_RC",
                "StbSecBeam_S",
                "StbSecBeam_SRC",
                "StbSecBrace_S",
                "StbSecSlab_RC",
                "StbSecSlabDeck",
                "StbSecSlabPrecast",
                "StbSecWall_RC",
            ),
        ),
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbAnaCalMemberRel(StBridgeElement):
    """StbAnaCalMemberRel

    Attributes:
        id_ana_member (int): 属性
        member_kind (StbAnaCalMemberRelMemberKind): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(
            py_type=StbAnaCalMemberRelMemberKind,
            data_type=_DT.STR_ENUM,
            choices=("StbCalColumn", "StbCalGirder"),
        ),
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbAnaMemberRel(StBridgeElement):
    """StbAnaMemberRel

    Attributes:
        id_ana_member (int): 属性
        member_kind (StbAnaMemberRelMemberKind): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(
            py_type=StbAnaMemberRelMemberKind,
            data_type=_DT.STR_ENUM,
            choices=(
                "StbColumn",
                "StbPost",
                "StbGirder",
                "StbBeam",
                "StbBrace",
                "StbSlab",
                "StbWall",
            ),
        ),
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbAnaStoryRel(StBridgeElement):
    """StbAnaStoryRel

    Attributes:
        id_ana_story (int): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbAnaNodeRel(StBridgeElement):
    """StbAnaNodeRel

    Attributes:
        id_ana_node (int): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbAnaRelations(StBridgeElement):
    """StbAnaRelations

    Attributes:
        stb_ana_node_rel (list[StbAnaNodeRel]): 子要素
        stb_ana_story_rel (list[StbAnaStoryRel]): 子要素
        stb_ana_member_rel (list[StbAnaMemberRel]): 子要素
        stb_ana_cal_member_rel (list[StbAnaCalMemberRel]): 子要素
        stb_ana_property_rel (list[StbAnaPropertyRel]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_node_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaNodeRel]),
        "stb_ana_story_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaStoryRel]),
        "stb_ana_member_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaMemberRel]),
        "stb_ana_cal_member_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaCalMemberRel]
        ),
        "stb_ana_property_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaPropertyRel]),
    }


class StbAnaAnalysisStaticLinear(StBridgeElement):
    """StbAnaAnalysisStaticLinear

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_initial_stress_load_case (int): 属性
        id_load_case (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_initial_stress_load_case": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "id_load_case": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaAnalyses(StBridgeElement):
    """StbAnaAnalyses

    Attributes:
        stb_ana_analysis_static_linear (list[StbAnaAnalysisStaticLinear]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_analysis_static_linear": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaAnalysisStaticLinear]
        ),
    }


class StbAnaLoadSpringInitialStress(StBridgeElement):
    """StbAnaLoadSpringInitialStress

    Attributes:
        force (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "force": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbAnaLoadSpring(StBridgeElement):
    """StbAnaLoadSpring

    Attributes:
        id_member (int): 属性
        stb_ana_load_spring_initial_stress (list[StbAnaLoadSpringInitialStress]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_ana_load_spring_initial_stress": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaLoadSpringInitialStress]
        ),
    }


class StbAnaLoadWallInitialStress(StBridgeElement):
    """StbAnaLoadWallInitialStress

    Attributes:
        n (float): 属性
        q (float): 属性
        bottom_m (float): 属性
        top_m (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "n": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="N"),
        "q": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Q"),
        "bottom_m": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="bottom_M"),
        "top_m": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="top_M"),
    }


class StbAnaLoadWall(StBridgeElement):
    """StbAnaLoadWall

    Attributes:
        id_member (int): 属性
        stb_ana_load_wall_initial_stress (list[StbAnaLoadWallInitialStress]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_ana_load_wall_initial_stress": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaLoadWallInitialStress]
        ),
    }


class StbAnaLoadTrussInitialStress(StBridgeElement):
    """StbAnaLoadTrussInitialStress

    Attributes:
        n (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "n": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="N"),
    }


class StbAnaLoadTruss(StBridgeElement):
    """StbAnaLoadTruss

    Attributes:
        id_member (int): 属性
        stb_ana_load_truss_initial_stress (list[StbAnaLoadTrussInitialStress]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_ana_load_truss_initial_stress": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaLoadTrussInitialStress]
        ),
    }


class StbAnaLoadBeamInitialStress(StBridgeElement):
    """StbAnaLoadBeamInitialStress

    Attributes:
        n (float): 属性
        start_qy (float): 属性
        start_qz (float): 属性
        start_my (float): 属性
        start_mz (float): 属性
        end_qy (float): 属性
        end_qz (float): 属性
        end_my (float): 属性
        end_mz (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "n": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="N"),
        "start_qy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Qy"),
        "start_qz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Qz"),
        "start_my": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_My"),
        "start_mz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Mz"),
        "end_qy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Qy"),
        "end_qz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Qz"),
        "end_my": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_My"),
        "end_mz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Mz"),
    }


class StbAnaLoadBeamCmq(StBridgeElement):
    """StbAnaLoadBeamCmq：StbAnaLoadBeamCMQ

    Attributes:
        start_n (float): 属性
        start_qy (float): 属性
        start_qz (float): 属性
        start_t (float): 属性
        start_cy (float): 属性
        start_cz (float): 属性
        end_n (float): 属性
        end_qy (float): 属性
        end_qz (float): 属性
        end_t (float): 属性
        end_cy (float): 属性
        end_cz (float): 属性
        center_t (float): 属性
        center_m0y (float): 属性
        center_m0z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "start_n": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_N"),
        "start_qy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Qy"),
        "start_qz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Qz"),
        "start_t": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_T"),
        "start_cy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Cy"),
        "start_cz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Cz"),
        "end_n": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_N"),
        "end_qy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Qy"),
        "end_qz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Qz"),
        "end_t": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_T"),
        "end_cy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Cy"),
        "end_cz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Cz"),
        "center_t": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="center_T"),
        "center_m0y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="center_M0y"),
        "center_m0z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="center_M0z"),
    }
    _xml_element_name: ClassVar[str] = "StbAnaLoadBeamCMQ"


class StbAnaLoadBeam(StBridgeElement):
    """StbAnaLoadBeam

    Attributes:
        id_member (int): 属性
        stb_ana_load_beam_cmq (list[StbAnaLoadBeamCmq]): 子要素
        stb_ana_load_beam_initial_stress (list[StbAnaLoadBeamInitialStress]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_ana_load_beam_cmq": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadBeamCmq]),
        "stb_ana_load_beam_initial_stress": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaLoadBeamInitialStress]
        ),
    }


class StbAnaLoadNode(StBridgeElement):
    """StbAnaLoadNode

    Attributes:
        id_node (int): 属性
        ux (float): 属性
        uy (float): 属性
        uz (float): 属性
        tx (float): 属性
        ty (float): 属性
        tz (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "ux": _FI(py_type=float, data_type=_DT.FLOAT),
        "uy": _FI(py_type=float, data_type=_DT.FLOAT),
        "uz": _FI(py_type=float, data_type=_DT.FLOAT),
        "tx": _FI(py_type=float, data_type=_DT.FLOAT),
        "ty": _FI(py_type=float, data_type=_DT.FLOAT),
        "tz": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbAnaLoadCase(StBridgeElement):
    """StbAnaLoadCase

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        stb_ana_load_node (list[StbAnaLoadNode]): 子要素
        stb_ana_load_beam (list[StbAnaLoadBeam]): 子要素
        stb_ana_load_truss (list[StbAnaLoadTruss]): 子要素
        stb_ana_load_wall (list[StbAnaLoadWall]): 子要素
        stb_ana_load_spring (list[StbAnaLoadSpring]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "stb_ana_load_node": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadNode]),
        "stb_ana_load_beam": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadBeam]),
        "stb_ana_load_truss": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadTruss]),
        "stb_ana_load_wall": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadWall]),
        "stb_ana_load_spring": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadSpring]),
    }


class StbAnaLoadCases(StBridgeElement):
    """StbAnaLoadCases

    Attributes:
        stb_ana_load_case (list[StbAnaLoadCase]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_load_case": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadCase]),
    }


class StbAnaSection(StBridgeElement):
    """StbAnaSection

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        ax (float): 属性
        ay (float): 属性
        az (float): 属性
        ix (float): 属性
        iy (float): 属性
        iz (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "ax": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Ax"),
        "ay": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Ay"),
        "az": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Az"),
        "ix": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Ix"),
        "iy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Iy"),
        "iz": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Iz"),
    }


class StbAnaSections(StBridgeElement):
    """StbAnaSections

    Attributes:
        stb_ana_section (list[StbAnaSection]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_section": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaSection]),
    }


class StbAnaMaterial(StBridgeElement):
    """StbAnaMaterial

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        e (float): 属性
        g (float): 属性
        poisson (float): 属性
        thermal (float): 属性
        density (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "e": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="E"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="G"),
        "poisson": _FI(py_type=float, data_type=_DT.FLOAT),
        "thermal": _FI(py_type=float, data_type=_DT.FLOAT),
        "density": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbAnaMaterials(StBridgeElement):
    """StbAnaMaterials

    Attributes:
        stb_ana_material (list[StbAnaMaterial]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_material": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaMaterial]),
    }


class StbAnaNodeid(StBridgeElement):
    """StbAnaNodeid

    Attributes:
        id (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaNodeid_List(StBridgeElement):
    """StbAnaNodeid_List

    Attributes:
        stb_ana_nodeid (list[StbAnaNodeid]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_nodeid": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaNodeid]),
    }


class StbAnaFloorDiaphragm(StBridgeElement):
    """StbAnaFloorDiaphragm

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_representative_node (int): 属性
        stb_ana_nodeid_list (StbAnaNodeid_List): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_representative_node": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_ana_nodeid_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbAnaNodeid_List
        ),
    }


class StbAnaFloorDiaphragms(StBridgeElement):
    """StbAnaFloorDiaphragms

    Attributes:
        stb_ana_floor_diaphragm (list[StbAnaFloorDiaphragm]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_floor_diaphragm": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaFloorDiaphragm]
        ),
    }


class StbAnaNodePanelProperty(StBridgeElement):
    """StbAnaNodePanelProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_material (int): 属性
        b_x (float): 属性
        b_y (float): 属性
        b_z (float): 属性
        t_x (float): 属性
        t_y (float): 属性
        t_z (float): 属性
        d_x (float): 属性
        d_y (float): 属性
        d_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_material": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "b_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="B_x"),
        "b_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="B_y"),
        "b_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="B_z"),
        "t_x": _FI(py_type=float, data_type=_DT.FLOAT),
        "t_y": _FI(py_type=float, data_type=_DT.FLOAT),
        "t_z": _FI(py_type=float, data_type=_DT.FLOAT),
        "d_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="D_x"),
        "d_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="D_y"),
        "d_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="D_z"),
    }


class StbAnaNodePanelProperties(StBridgeElement):
    """StbAnaNodePanelProperties

    Attributes:
        stb_ana_node_panel_property (list[StbAnaNodePanelProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_node_panel_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaNodePanelProperty]
        ),
    }


class StbAnaPlaneProperty(StBridgeElement):
    """StbAnaPlaneProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_material (int): 属性
        element_type (StbAnaPlanePropertyElementType): 属性
        thickness (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_material": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "element_type": _FI(
            py_type=StbAnaPlanePropertyElementType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("PLANE_STRESS", "PLANE_STRAIN"),
        ),
        "thickness": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbAnaPlaneProperties(StBridgeElement):
    """StbAnaPlaneProperties

    Attributes:
        stb_ana_plane_property (list[StbAnaPlaneProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_plane_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaPlaneProperty]
        ),
    }


class StbAnaWallProperty(StBridgeElement):
    """StbAnaWallProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_material (int): 属性
        id_section (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_material": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaWallProperties(StBridgeElement):
    """StbAnaWallProperties

    Attributes:
        stb_ana_wall_property (list[StbAnaWallProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_wall_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaWallProperty]
        ),
    }


class StbAnaSpringProperty(StBridgeElement):
    """StbAnaSpringProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        spring (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "spring": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbAnaSpringProperties(StBridgeElement):
    """StbAnaSpringProperties

    Attributes:
        stb_ana_spring_property (list[StbAnaSpringProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_spring_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaSpringProperty]
        ),
    }


class StbAnaTrussProperty(StBridgeElement):
    """StbAnaTrussProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_material (int): 属性
        id_section (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_material": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaTrussProperties(StBridgeElement):
    """StbAnaTrussProperties

    Attributes:
        stb_ana_truss_property (list[StbAnaTrussProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_truss_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaTrussProperty]
        ),
    }


class StbAnaBeamProperty(StBridgeElement):
    """StbAnaBeamProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_material (int): 属性
        id_section (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_material": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaBeamProperties(StBridgeElement):
    """StbAnaBeamProperties

    Attributes:
        stb_ana_beam_property (list[StbAnaBeamProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_beam_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaBeamProperty]
        ),
    }


class StbAnaProperties(StBridgeElement):
    """StbAnaProperties

    Attributes:
        stb_ana_beam_properties (StbAnaBeamProperties): 子要素
        stb_ana_truss_properties (StbAnaTrussProperties): 子要素
        stb_ana_spring_properties (StbAnaSpringProperties): 子要素
        stb_ana_wall_properties (StbAnaWallProperties): 子要素
        stb_ana_plane_properties (StbAnaPlaneProperties): 子要素
        stb_ana_node_panel_properties (StbAnaNodePanelProperties): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_beam_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaBeamProperties
        ),
        "stb_ana_truss_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaTrussProperties
        ),
        "stb_ana_spring_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaSpringProperties
        ),
        "stb_ana_wall_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaWallProperties
        ),
        "stb_ana_plane_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaPlaneProperties
        ),
        "stb_ana_node_panel_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaNodePanelProperties
        ),
    }


class StbAnaNodePanel(StBridgeElement):
    """StbAnaNodePanel

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        angle (float): 属性
        id_property (int): 属性
        id_node (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaNodePanels(StBridgeElement):
    """StbAnaNodePanels

    Attributes:
        stb_ana_node_panel (list[StbAnaNodePanel]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_node_panel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaNodePanel]),
    }


class StbAnaPlaneRectangle(StBridgeElement):
    """StbAnaPlaneRectangle

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_property (int): 属性
        id_node1 (int): 属性
        id_node2 (int): 属性
        id_node3 (int): 属性
        id_node4 (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node1": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node2": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node3": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node4": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaPlaneRectangles(StBridgeElement):
    """StbAnaPlaneRectangles

    Attributes:
        stb_ana_plane_rectangle (list[StbAnaPlaneRectangle]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_plane_rectangle": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaPlaneRectangle]
        ),
    }


class StbAnaPlaneTriangle(StBridgeElement):
    """StbAnaPlaneTriangle

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_property (int): 属性
        id_node1 (int): 属性
        id_node2 (int): 属性
        id_node3 (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node1": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node2": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node3": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaPlaneTriangles(StBridgeElement):
    """StbAnaPlaneTriangles

    Attributes:
        stb_ana_plane_triangle (list[StbAnaPlaneTriangle]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_plane_triangle": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaPlaneTriangle]
        ),
    }


class StbAnaWall(StBridgeElement):
    """StbAnaWall

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_property (int): 属性
        id_node_start_bottom (int): 属性
        id_node_end_bottom (int): 属性
        id_node_start_top (int): 属性
        id_node_end_top (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_start_bottom": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end_bottom": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_start_top": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end_top": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaWalls(StBridgeElement):
    """StbAnaWalls

    Attributes:
        stb_ana_wall (list[StbAnaWall]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_wall": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaWall]),
    }


class StbAnaSpring(StBridgeElement):
    """StbAnaSpring

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_property (int): 属性
        id_node_start (int): 属性
        id_node_end (int): 属性
        direction (StbAnaSpringDirection): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "direction": _FI(
            py_type=StbAnaSpringDirection,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("UX", "UY", "UZ", "TX", "TY", "TZ", "AXIAL"),
        ),
    }


class StbAnaSprings(StBridgeElement):
    """StbAnaSprings

    Attributes:
        stb_ana_spring (list[StbAnaSpring]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_spring": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaSpring]),
    }


class StbAnaSupport(StBridgeElement):
    """StbAnaSupport

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_property (int): 属性
        id_node (int): 属性
        direction (StbAnaSupportDirection): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "direction": _FI(
            py_type=StbAnaSupportDirection,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("UX", "UY", "UZ", "TX", "TY", "TZ"),
        ),
    }


class StbAnaSupports(StBridgeElement):
    """StbAnaSupports

    Attributes:
        stb_ana_support (list[StbAnaSupport]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_support": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaSupport]),
    }


class StbAnaTruss(StBridgeElement):
    """StbAnaTruss

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_property (int): 属性
        id_node_start (int): 属性
        id_node_end (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbAnaTrusses(StBridgeElement):
    """StbAnaTrusses

    Attributes:
        stb_ana_truss (list[StbAnaTruss]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_truss": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaTruss]),
    }


class StbAnaBeamEndSpring(StBridgeElement):
    """StbAnaBeamEndSpring

    Attributes:
        id_property_start_y (int): 属性
        id_property_start_z (int): 属性
        id_property_end_y (int): 属性
        id_property_end_z (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_property_start_y": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "id_property_start_z": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "id_property_end_y": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "id_property_end_z": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbAnaBeamCriticalPosition(StBridgeElement):
    """StbAnaBeamCriticalPosition

    Attributes:
        start_x (float): 属性
        start_y (float): 属性
        start_z (float): 属性
        end_x (float): 属性
        end_y (float): 属性
        end_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "start_x": _FI(py_type=float, data_type=_DT.FLOAT),
        "start_y": _FI(py_type=float, data_type=_DT.FLOAT),
        "start_z": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_x": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_y": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_z": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbAnaBeamRigidzone(StBridgeElement):
    """StbAnaBeamRigidzone

    Attributes:
        start_x (float): 属性
        start_y (float): 属性
        start_z (float): 属性
        end_x (float): 属性
        end_y (float): 属性
        end_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "start_x": _FI(py_type=float, data_type=_DT.FLOAT),
        "start_y": _FI(py_type=float, data_type=_DT.FLOAT),
        "start_z": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_x": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_y": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_z": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbAnaBeam(StBridgeElement):
    """StbAnaBeam

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_property (int): 属性
        id_node_start (int): 属性
        id_node_end (int): 属性
        coord_angle (float): 属性
        stb_ana_beam_rigidzone (StbAnaBeamRigidzone): 子要素
        stb_ana_beam_critical_position (StbAnaBeamCriticalPosition): 子要素
        stb_ana_beam_end_spring (StbAnaBeamEndSpring): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "coord_angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "stb_ana_beam_rigidzone": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaBeamRigidzone
        ),
        "stb_ana_beam_critical_position": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaBeamCriticalPosition
        ),
        "stb_ana_beam_end_spring": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaBeamEndSpring
        ),
    }


class StbAnaBeams(StBridgeElement):
    """StbAnaBeams

    Attributes:
        stb_ana_beam (list[StbAnaBeam]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_beam": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaBeam]),
    }


class StbAnaMembers(StBridgeElement):
    """StbAnaMembers

    Attributes:
        stb_ana_beams (StbAnaBeams): 子要素
        stb_ana_trusses (StbAnaTrusses): 子要素
        stb_ana_supports (StbAnaSupports): 子要素
        stb_ana_springs (StbAnaSprings): 子要素
        stb_ana_walls (StbAnaWalls): 子要素
        stb_ana_plane_triangles (StbAnaPlaneTriangles): 子要素
        stb_ana_plane_rectangles (StbAnaPlaneRectangles): 子要素
        stb_ana_node_panels (StbAnaNodePanels): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_beams": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaBeams),
        "stb_ana_trusses": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaTrusses),
        "stb_ana_supports": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaSupports),
        "stb_ana_springs": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaSprings),
        "stb_ana_walls": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaWalls),
        "stb_ana_plane_triangles": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaPlaneTriangles
        ),
        "stb_ana_plane_rectangles": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaPlaneRectangles
        ),
        "stb_ana_node_panels": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaNodePanels
        ),
    }


class StbAnaMemberid(StBridgeElement):
    """StbAnaMemberid

    Attributes:
        id (int): 属性
        kind (StbAnaMemberidKind): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind": _FI(
            py_type=StbAnaMemberidKind,
            data_type=_DT.STR_ENUM,
            choices=(
                "StbAnaBeam",
                "StbAnaTruss",
                "StbAnaSupport",
                "StbAnaSpring",
                "StbAnaWall",
                "StbAnaPlaneTriangle",
                "StbAnaPlaneRectangle",
                "StbAnaNodePanel",
            ),
        ),
    }


class StbAnaMemberid_List(StBridgeElement):
    """StbAnaMemberid_List

    Attributes:
        stb_ana_memberid (list[StbAnaMemberid]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_memberid": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaMemberid]),
    }


class StbAnaStory(StBridgeElement):
    """StbAnaStory

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_node_lower (int): 属性
        id_node_upper (int): 属性
        height (float): 属性
        sum_weight (float): 属性
        stb_ana_memberid_list (StbAnaMemberid_List): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_node_lower": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "id_node_upper": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "height": _FI(py_type=float, data_type=_DT.FLOAT),
        "sum_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "stb_ana_memberid_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbAnaMemberid_List
        ),
    }


class StbAnaStories(StBridgeElement):
    """StbAnaStories

    Attributes:
        stb_ana_story (list[StbAnaStory]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_story": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaStory]),
    }


class StbAnaBoundary(StBridgeElement):
    """StbAnaBoundary

    Attributes:
        x (StbAnaBoundaryX): 属性
        y (StbAnaBoundaryY): 属性
        z (StbAnaBoundaryZ): 属性
        tx (StbAnaBoundaryTx): 属性
        ty (StbAnaBoundaryTy): 属性
        tz (StbAnaBoundaryTz): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "x": _FI(
            py_type=StbAnaBoundaryX, data_type=_DT.STR_ENUM, choices=("FIX", "FREE")
        ),
        "y": _FI(
            py_type=StbAnaBoundaryY, data_type=_DT.STR_ENUM, choices=("FIX", "FREE")
        ),
        "z": _FI(
            py_type=StbAnaBoundaryZ, data_type=_DT.STR_ENUM, choices=("FIX", "FREE")
        ),
        "tx": _FI(
            py_type=StbAnaBoundaryTx, data_type=_DT.STR_ENUM, choices=("FIX", "FREE")
        ),
        "ty": _FI(
            py_type=StbAnaBoundaryTy, data_type=_DT.STR_ENUM, choices=("FIX", "FREE")
        ),
        "tz": _FI(
            py_type=StbAnaBoundaryTz, data_type=_DT.STR_ENUM, choices=("FIX", "FREE")
        ),
    }


class StbAnaNode(StBridgeElement):
    """StbAnaNode

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        x (float): 属性
        y (float): 属性
        z (float): 属性
        stb_ana_boundary (StbAnaBoundary): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "z": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stb_ana_boundary": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaBoundary),
    }


class StbAnaNodes(StBridgeElement):
    """StbAnaNodes

    Attributes:
        stb_ana_node (list[StbAnaNode]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_node": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaNode]),
    }


class StbAnaModel(StBridgeElement):
    """StbAnaModel

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        stb_ana_nodes (StbAnaNodes): 子要素
        stb_ana_stories (StbAnaStories): 子要素
        stb_ana_members (StbAnaMembers): 子要素
        stb_ana_properties (StbAnaProperties): 子要素
        stb_ana_floor_diaphragms (StbAnaFloorDiaphragms): 子要素
        stb_ana_materials (StbAnaMaterials): 子要素
        stb_ana_sections (StbAnaSections): 子要素
        stb_ana_load_cases (StbAnaLoadCases): 子要素
        stb_ana_analyses (StbAnaAnalyses): 子要素
        stb_ana_relations (StbAnaRelations): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "stb_ana_nodes": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaNodes),
        "stb_ana_stories": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaStories),
        "stb_ana_members": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaMembers),
        "stb_ana_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaProperties
        ),
        "stb_ana_floor_diaphragms": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaFloorDiaphragms
        ),
        "stb_ana_materials": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaMaterials
        ),
        "stb_ana_sections": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaSections),
        "stb_ana_load_cases": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaLoadCases
        ),
        "stb_ana_analyses": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaAnalyses),
        "stb_ana_relations": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaRelations
        ),
    }


class StbAnaModels(StBridgeElement):
    """StbAnaModels

    Attributes:
        stb_ana_model (list[StbAnaModel]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_model": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaModel]),
    }


class StbCalWallSecPropertyRcList(StBridgeElement):
    """StbCalWallSecPropertyRcList：StbCalWallSecProperty_RC_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalWallSecProperty_RC_List"


class StbCalWallSecPropertyList(StBridgeElement):
    """StbCalWallSecPropertyList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalWallSecPropertyArr(StBridgeElement):
    """StbCalWallSecPropertyArr

    Attributes:
        stb_cal_wall_sec_property_list (StbCalWallSecPropertyList): 子要素
        stb_cal_wall_sec_property_rc_list (StbCalWallSecPropertyRcList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_wall_sec_property_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallSecPropertyList,
        ),
        "stb_cal_wall_sec_property_rc_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallSecPropertyRcList,
        ),
    }


class StbCalSlabSecPropertyPrecastList(StBridgeElement):
    """StbCalSlabSecPropertyPrecastList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabSecPropertyDeckList(StBridgeElement):
    """StbCalSlabSecPropertyDeckList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabSecPropertyRcList(StBridgeElement):
    """StbCalSlabSecPropertyRcList：StbCalSlabSecProperty_RC_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalSlabSecProperty_RC_List"


class StbCalSlabSecPropertyList(StBridgeElement):
    """StbCalSlabSecPropertyList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabSecPropertyArr(StBridgeElement):
    """StbCalSlabSecPropertyArr

    Attributes:
        stb_cal_slab_sec_property_list (StbCalSlabSecPropertyList): 子要素
        stb_cal_slab_sec_property_rc_list (StbCalSlabSecPropertyRcList): 子要素
        stb_cal_slab_sec_property_deck_list (StbCalSlabSecPropertyDeckList): 子要素
        stb_cal_slab_sec_property_precast_list (StbCalSlabSecPropertyPrecastList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_slab_sec_property_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSlabSecPropertyList,
        ),
        "stb_cal_slab_sec_property_rc_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSlabSecPropertyRcList
        ),
        "stb_cal_slab_sec_property_deck_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSlabSecPropertyDeckList
        ),
        "stb_cal_slab_sec_property_precast_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSlabSecPropertyPrecastList
        ),
    }


class StbCalBraceSecPropertySList(StBridgeElement):
    """StbCalBraceSecPropertySList：StbCalBraceSecProperty_S_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBraceSecProperty_S_List"


class StbCalBraceSecPropertyList(StBridgeElement):
    """StbCalBraceSecPropertyList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalBraceSecPropertyArr(StBridgeElement):
    """StbCalBraceSecPropertyArr

    Attributes:
        stb_cal_brace_sec_property_list (StbCalBraceSecPropertyList): 子要素
        stb_cal_brace_sec_property_s_list (StbCalBraceSecPropertySList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_brace_sec_property_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceSecPropertyList,
        ),
        "stb_cal_brace_sec_property_s_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceSecPropertySList,
        ),
    }


class StbCalGirderSecPropertySrcList(StBridgeElement):
    """StbCalGirderSecPropertySrcList：StbCalGirderSecProperty_SRC_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderSecProperty_SRC_List"


class StbCalGirderSecPropertySList(StBridgeElement):
    """StbCalGirderSecPropertySList：StbCalGirderSecProperty_S_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderSecProperty_S_List"


class StbCalGirderSecPropertyRcList(StBridgeElement):
    """StbCalGirderSecPropertyRcList：StbCalGirderSecProperty_RC_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderSecProperty_RC_List"


class StbCalGirderSecPropertyList(StBridgeElement):
    """StbCalGirderSecPropertyList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderSecPropertyArr(StBridgeElement):
    """StbCalGirderSecPropertyArr

    Attributes:
        stb_cal_girder_sec_property_list (StbCalGirderSecPropertyList): 子要素
        stb_cal_girder_sec_property_rc_list (StbCalGirderSecPropertyRcList): 子要素
        stb_cal_girder_sec_property_s_list (StbCalGirderSecPropertySList): 子要素
        stb_cal_girder_sec_property_src_list (StbCalGirderSecPropertySrcList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_sec_property_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderSecPropertyList,
        ),
        "stb_cal_girder_sec_property_rc_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderSecPropertyRcList
        ),
        "stb_cal_girder_sec_property_s_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderSecPropertySList
        ),
        "stb_cal_girder_sec_property_src_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderSecPropertySrcList
        ),
    }


class StbCalColumnSecPropertyCftList(StBridgeElement):
    """StbCalColumnSecPropertyCftList：StbCalColumnSecProperty_CFT_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnSecProperty_CFT_List"


class StbCalColumnSecPropertySrcList(StBridgeElement):
    """StbCalColumnSecPropertySrcList：StbCalColumnSecProperty_SRC_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnSecProperty_SRC_List"


class StbCalColumnSecPropertySList(StBridgeElement):
    """StbCalColumnSecPropertySList：StbCalColumnSecProperty_S_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnSecProperty_S_List"


class StbCalColumnSecPropertyRcList(StBridgeElement):
    """StbCalColumnSecPropertyRcList：StbCalColumnSecProperty_RC_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnSecProperty_RC_List"


class StbCalColumnSecPropertyList(StBridgeElement):
    """StbCalColumnSecPropertyList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnSecPropertyArr(StBridgeElement):
    """StbCalColumnSecPropertyArr

    Attributes:
        stb_cal_column_sec_property_list (StbCalColumnSecPropertyList): 子要素
        stb_cal_column_sec_property_rc_list (StbCalColumnSecPropertyRcList): 子要素
        stb_cal_column_sec_property_s_list (StbCalColumnSecPropertySList): 子要素
        stb_cal_column_sec_property_src_list (StbCalColumnSecPropertySrcList): 子要素
        stb_cal_column_sec_property_cft_list (StbCalColumnSecPropertyCftList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_sec_property_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnSecPropertyList,
        ),
        "stb_cal_column_sec_property_rc_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnSecPropertyRcList
        ),
        "stb_cal_column_sec_property_s_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnSecPropertySList
        ),
        "stb_cal_column_sec_property_src_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnSecPropertySrcList
        ),
        "stb_cal_column_sec_property_cft_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnSecPropertyCftList
        ),
    }


class StbCalNodePanelNodeList(StBridgeElement):
    """StbCalNodePanelNodeList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodePanelList(StBridgeElement):
    """StbCalNodePanelList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodePanelArr(StBridgeElement):
    """StbCalNodePanelArr

    Attributes:
        stb_cal_node_panel_list (StbCalNodePanelList): 子要素
        stb_cal_node_panel_node_list (StbCalNodePanelNodeList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_node_panel_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbCalNodePanelList
        ),
        "stb_cal_node_panel_node_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalNodePanelNodeList,
        ),
    }


class StbCalNodeRestrictionNodeList(StBridgeElement):
    """StbCalNodeRestrictionNodeList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodeRestrictionList(StBridgeElement):
    """StbCalNodeRestrictionList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodeRestrictionArr(StBridgeElement):
    """StbCalNodeRestrictionArr

    Attributes:
        stb_cal_node_restriction_list (StbCalNodeRestrictionList): 子要素
        stb_cal_node_restriction_node_list (StbCalNodeRestrictionNodeList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_node_restriction_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalNodeRestrictionList,
        ),
        "stb_cal_node_restriction_node_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalNodeRestrictionNodeList,
        ),
    }


class StbCalWallStiffnessMemList(StBridgeElement):
    """StbCalWallStiffnessMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalWallStiffnessList(StBridgeElement):
    """StbCalWallStiffnessList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalWallStiffnessArr(StBridgeElement):
    """StbCalWallStiffnessArr

    Attributes:
        stb_cal_wall_stiffness_list (StbCalWallStiffnessList): 子要素
        stb_cal_wall_stiffness_mem_list (StbCalWallStiffnessMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_wall_stiffness_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallStiffnessList,
        ),
        "stb_cal_wall_stiffness_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallStiffnessMemList,
        ),
    }


class StbCalBraceStiffnessMemList(StBridgeElement):
    """StbCalBraceStiffnessMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalBraceStiffnessList(StBridgeElement):
    """StbCalBraceStiffnessList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalBraceStiffnessArr(StBridgeElement):
    """StbCalBraceStiffnessArr

    Attributes:
        stb_cal_brace_stiffness_list (StbCalBraceStiffnessList): 子要素
        stb_cal_brace_stiffness_mem_list (StbCalBraceStiffnessMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_brace_stiffness_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceStiffnessList,
        ),
        "stb_cal_brace_stiffness_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceStiffnessMemList,
        ),
    }


class StbCalGirderStiffnessCalMemList(StBridgeElement):
    """StbCalGirderStiffnessCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderStiffnessMemList(StBridgeElement):
    """StbCalGirderStiffnessMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderStiffnessList(StBridgeElement):
    """StbCalGirderStiffnessList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderStiffnessArr(StBridgeElement):
    """StbCalGirderStiffnessArr

    Attributes:
        stb_cal_girder_stiffness_list (StbCalGirderStiffnessList): 子要素
        stb_cal_girder_stiffness_mem_list (StbCalGirderStiffnessMemList): 子要素
        stb_cal_girder_stiffness_cal_mem_list (StbCalGirderStiffnessCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_stiffness_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderStiffnessList,
        ),
        "stb_cal_girder_stiffness_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderStiffnessMemList
        ),
        "stb_cal_girder_stiffness_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderStiffnessCalMemList
        ),
    }


class StbCalGirderCriticalPositionCalMemList(StBridgeElement):
    """StbCalGirderCriticalPositionCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderCriticalPositionMemList(StBridgeElement):
    """StbCalGirderCriticalPositionMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderCriticalPositionList(StBridgeElement):
    """StbCalGirderCriticalPositionList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderCriticalPositionArr(StBridgeElement):
    """StbCalGirderCriticalPositionArr

    Attributes:
        stb_cal_girder_critical_position_list (StbCalGirderCriticalPositionList): 子要素
        stb_cal_girder_critical_position_mem_list (StbCalGirderCriticalPositionMemList): 子要素
        stb_cal_girder_critical_position_cal_mem_list (StbCalGirderCriticalPositionCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_critical_position_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderCriticalPositionList,
        ),
        "stb_cal_girder_critical_position_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderCriticalPositionMemList
        ),
        "stb_cal_girder_critical_position_cal_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbCalGirderCriticalPositionCalMemList,
        ),
    }


class StbCalGirderRigidzoneCalMemList(StBridgeElement):
    """StbCalGirderRigidzoneCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderRigidzoneMemList(StBridgeElement):
    """StbCalGirderRigidzoneMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderRigidzoneList(StBridgeElement):
    """StbCalGirderRigidzoneList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderRigidzoneArr(StBridgeElement):
    """StbCalGirderRigidzoneArr

    Attributes:
        stb_cal_girder_rigidzone_list (StbCalGirderRigidzoneList): 子要素
        stb_cal_girder_rigidzone_mem_list (StbCalGirderRigidzoneMemList): 子要素
        stb_cal_girder_rigidzone_cal_mem_list (StbCalGirderRigidzoneCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_rigidzone_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderRigidzoneList,
        ),
        "stb_cal_girder_rigidzone_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderRigidzoneMemList
        ),
        "stb_cal_girder_rigidzone_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderRigidzoneCalMemList
        ),
    }


class StbCalGirderConditionCalMemList(StBridgeElement):
    """StbCalGirderConditionCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderConditionMemList(StBridgeElement):
    """StbCalGirderConditionMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderConditionList(StBridgeElement):
    """StbCalGirderConditionList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderConditionArr(StBridgeElement):
    """StbCalGirderConditionArr

    Attributes:
        stb_cal_girder_condition_list (StbCalGirderConditionList): 子要素
        stb_cal_girder_condition_mem_list (StbCalGirderConditionMemList): 子要素
        stb_cal_girder_condition_cal_mem_list (StbCalGirderConditionCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_condition_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderConditionList,
        ),
        "stb_cal_girder_condition_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderConditionMemList
        ),
        "stb_cal_girder_condition_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderConditionCalMemList
        ),
    }


class StbCalColumnStiffnessCalMemList(StBridgeElement):
    """StbCalColumnStiffnessCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnStiffnessMemList(StBridgeElement):
    """StbCalColumnStiffnessMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnStiffnessList(StBridgeElement):
    """StbCalColumnStiffnessList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnStiffnessArr(StBridgeElement):
    """StbCalColumnStiffnessArr

    Attributes:
        stb_cal_column_stiffness_list (StbCalColumnStiffnessList): 子要素
        stb_cal_column_stiffness_mem_list (StbCalColumnStiffnessMemList): 子要素
        stb_cal_column_stiffness_cal_mem_list (StbCalColumnStiffnessCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_stiffness_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnStiffnessList,
        ),
        "stb_cal_column_stiffness_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnStiffnessMemList
        ),
        "stb_cal_column_stiffness_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnStiffnessCalMemList
        ),
    }


class StbCalColumnCriticalPositionCalMemList(StBridgeElement):
    """StbCalColumnCriticalPositionCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnCriticalPositionMemList(StBridgeElement):
    """StbCalColumnCriticalPositionMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnCriticalPositionList(StBridgeElement):
    """StbCalColumnCriticalPositionList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnCriticalPositionArr(StBridgeElement):
    """StbCalColumnCriticalPositionArr

    Attributes:
        stb_cal_column_critical_position_list (StbCalColumnCriticalPositionList): 子要素
        stb_cal_column_critical_position_mem_list (StbCalColumnCriticalPositionMemList): 子要素
        stb_cal_column_critical_position_cal_mem_list (StbCalColumnCriticalPositionCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_critical_position_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnCriticalPositionList,
        ),
        "stb_cal_column_critical_position_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnCriticalPositionMemList
        ),
        "stb_cal_column_critical_position_cal_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbCalColumnCriticalPositionCalMemList,
        ),
    }


class StbCalColumnRigidzoneCalMemList(StBridgeElement):
    """StbCalColumnRigidzoneCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnRigidzoneMemList(StBridgeElement):
    """StbCalColumnRigidzoneMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnRigidzoneList(StBridgeElement):
    """StbCalColumnRigidzoneList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnRigidzoneArr(StBridgeElement):
    """StbCalColumnRigidzoneArr

    Attributes:
        stb_cal_column_rigidzone_list (StbCalColumnRigidzoneList): 子要素
        stb_cal_column_rigidzone_mem_list (StbCalColumnRigidzoneMemList): 子要素
        stb_cal_column_rigidzone_cal_mem_list (StbCalColumnRigidzoneCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_rigidzone_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnRigidzoneList,
        ),
        "stb_cal_column_rigidzone_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnRigidzoneMemList
        ),
        "stb_cal_column_rigidzone_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnRigidzoneCalMemList
        ),
    }


class StbCalColumnConditionCalMemList(StBridgeElement):
    """StbCalColumnConditionCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnConditionMemList(StBridgeElement):
    """StbCalColumnConditionMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnConditionList(StBridgeElement):
    """StbCalColumnConditionList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnConditionArr(StBridgeElement):
    """StbCalColumnConditionArr

    Attributes:
        stb_cal_column_condition_list (StbCalColumnConditionList): 子要素
        stb_cal_column_condition_mem_list (StbCalColumnConditionMemList): 子要素
        stb_cal_column_condition_cal_mem_list (StbCalColumnConditionCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_condition_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnConditionList,
        ),
        "stb_cal_column_condition_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnConditionMemList
        ),
        "stb_cal_column_condition_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnConditionCalMemList
        ),
    }


class StbCalConditionArrangements(StBridgeElement):
    """StbCalConditionArrangements

    Attributes:
        stb_cal_column_condition_arr (list[StbCalColumnConditionArr]): 子要素
        stb_cal_column_rigidzone_arr (list[StbCalColumnRigidzoneArr]): 子要素
        stb_cal_column_critical_position_arr (list[StbCalColumnCriticalPositionArr]): 子要素
        stb_cal_column_stiffness_arr (list[StbCalColumnStiffnessArr]): 子要素
        stb_cal_girder_condition_arr (list[StbCalGirderConditionArr]): 子要素
        stb_cal_girder_rigidzone_arr (list[StbCalGirderRigidzoneArr]): 子要素
        stb_cal_girder_critical_position_arr (list[StbCalGirderCriticalPositionArr]): 子要素
        stb_cal_girder_stiffness_arr (list[StbCalGirderStiffnessArr]): 子要素
        stb_cal_brace_stiffness_arr (list[StbCalBraceStiffnessArr]): 子要素
        stb_cal_wall_stiffness_arr (list[StbCalWallStiffnessArr]): 子要素
        stb_cal_node_restriction_arr (list[StbCalNodeRestrictionArr]): 子要素
        stb_cal_node_panel_arr (list[StbCalNodePanelArr]): 子要素
        stb_cal_column_sec_property_arr (list[StbCalColumnSecPropertyArr]): 子要素
        stb_cal_girder_sec_property_arr (list[StbCalGirderSecPropertyArr]): 子要素
        stb_cal_brace_sec_property_arr (list[StbCalBraceSecPropertyArr]): 子要素
        stb_cal_slab_sec_property_arr (list[StbCalSlabSecPropertyArr]): 子要素
        stb_cal_wall_sec_property_arr (list[StbCalWallSecPropertyArr]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_condition_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnConditionArr]
        ),
        "stb_cal_column_rigidzone_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnRigidzoneArr]
        ),
        "stb_cal_column_critical_position_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnCriticalPositionArr]
        ),
        "stb_cal_column_stiffness_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnStiffnessArr]
        ),
        "stb_cal_girder_condition_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderConditionArr]
        ),
        "stb_cal_girder_rigidzone_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderRigidzoneArr]
        ),
        "stb_cal_girder_critical_position_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderCriticalPositionArr]
        ),
        "stb_cal_girder_stiffness_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderStiffnessArr]
        ),
        "stb_cal_brace_stiffness_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceStiffnessArr]
        ),
        "stb_cal_wall_stiffness_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallStiffnessArr]
        ),
        "stb_cal_node_restriction_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalNodeRestrictionArr]
        ),
        "stb_cal_node_panel_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalNodePanelArr]
        ),
        "stb_cal_column_sec_property_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnSecPropertyArr]
        ),
        "stb_cal_girder_sec_property_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderSecPropertyArr]
        ),
        "stb_cal_brace_sec_property_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceSecPropertyArr]
        ),
        "stb_cal_slab_sec_property_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSlabSecPropertyArr]
        ),
        "stb_cal_wall_sec_property_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallSecPropertyArr]
        ),
    }


class StbCalNodePointLoadNodeList(StBridgeElement):
    """StbCalNodePointLoadNodeList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodePointLoadList(StBridgeElement):
    """StbCalNodePointLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodePointLoadArr(StBridgeElement):
    """StbCalNodePointLoadArr

    Attributes:
        stb_cal_node_point_load_list (StbCalNodePointLoadList): 子要素
        stb_cal_node_point_load_node_list (StbCalNodePointLoadNodeList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_node_point_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalNodePointLoadList,
        ),
        "stb_cal_node_point_load_node_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalNodePointLoadNodeList,
        ),
    }


class StbCalNodeWeightNodeList(StBridgeElement):
    """StbCalNodeWeightNodeList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodeWeightLoadList(StBridgeElement):
    """StbCalNodeWeightLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalNodeWeightArr(StBridgeElement):
    """StbCalNodeWeightArr

    Attributes:
        stb_cal_node_weight_load_list (StbCalNodeWeightLoadList): 子要素
        stb_cal_node_weight_node_list (StbCalNodeWeightNodeList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_node_weight_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalNodeWeightLoadList,
        ),
        "stb_cal_node_weight_node_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalNodeWeightNodeList,
        ),
    }


class StbCalWallPressureLoadMemList(StBridgeElement):
    """StbCalWallPressureLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalWallPressureLoadList(StBridgeElement):
    """StbCalWallPressureLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalWallPressureLoadArr(StBridgeElement):
    """StbCalWallPressureLoadArr

    Attributes:
        stb_cal_wall_pressure_load_list (StbCalWallPressureLoadList): 子要素
        stb_cal_wall_pressure_load_mem_list (StbCalWallPressureLoadMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_wall_pressure_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallPressureLoadList,
        ),
        "stb_cal_wall_pressure_load_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallPressureLoadMemList,
        ),
    }


class StbCalWallAreaLoadMemList(StBridgeElement):
    """StbCalWallAreaLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalWallAreaLoadList(StBridgeElement):
    """StbCalWallAreaLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalWallAreaLoadArr(StBridgeElement):
    """StbCalWallAreaLoadArr

    Attributes:
        stb_cal_wall_area_load_list (StbCalWallAreaLoadList): 子要素
        stb_cal_wall_area_load_mem_list (StbCalWallAreaLoadMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_wall_area_load_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbCalWallAreaLoadList
        ),
        "stb_cal_wall_area_load_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallAreaLoadMemList,
        ),
    }


class StbCalWallFinishRcMemList(StBridgeElement):
    """StbCalWallFinishRcMemList：StbCalWallFinish_RC_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalWallFinish_RC_MemList"


class StbCalWallFinishRcLoadList(StBridgeElement):
    """StbCalWallFinishRcLoadList：StbCalWallFinish_RC_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalWallFinish_RC_LoadList"


class StbCalWallFinishRcArr(StBridgeElement):
    """StbCalWallFinishRcArr：StbCalWallFinish_RC_Arr

    Attributes:
        stb_cal_wall_finish_rc_load_list (StbCalWallFinishRcLoadList): 子要素
        stb_cal_wall_finish_rc_mem_list (StbCalWallFinishRcMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_wall_finish_rc_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallFinishRcLoadList,
        ),
        "stb_cal_wall_finish_rc_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalWallFinishRcMemList,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalWallFinish_RC_Arr"


class StbCalSlabPressureLoadMemList(StBridgeElement):
    """StbCalSlabPressureLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabPressureLoadList(StBridgeElement):
    """StbCalSlabPressureLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabPressureLoadArr(StBridgeElement):
    """StbCalSlabPressureLoadArr

    Attributes:
        stb_cal_slab_pressure_load_list (StbCalSlabPressureLoadList): 子要素
        stb_cal_slab_pressure_load_mem_list (StbCalSlabPressureLoadMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_slab_pressure_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSlabPressureLoadList,
        ),
        "stb_cal_slab_pressure_load_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSlabPressureLoadMemList,
        ),
    }


class StbCalSlabAreaLoadMemList(StBridgeElement):
    """StbCalSlabAreaLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabAreaLoadList(StBridgeElement):
    """StbCalSlabAreaLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabAreaLoadArr(StBridgeElement):
    """StbCalSlabAreaLoadArr

    Attributes:
        stb_cal_slab_area_load_list (StbCalSlabAreaLoadList): 子要素
        stb_cal_slab_area_load_mem_list (StbCalSlabAreaLoadMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_slab_area_load_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbCalSlabAreaLoadList
        ),
        "stb_cal_slab_area_load_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSlabAreaLoadMemList,
        ),
    }


class StbCalSlabFinishRcMemList(StBridgeElement):
    """StbCalSlabFinishRcMemList：StbCalSlabFinish_RC_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalSlabFinish_RC_MemList"


class StbCalSlabFinishRcLoadList(StBridgeElement):
    """StbCalSlabFinishRcLoadList：StbCalSlabFinish_RC_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalSlabFinish_RC_LoadList"


class StbCalSlabFinishRcArr(StBridgeElement):
    """StbCalSlabFinishRcArr：StbCalSlabFinish_RC_Arr

    Attributes:
        stb_cal_slab_finish_rc_load_list (StbCalSlabFinishRcLoadList): 子要素
        stb_cal_slab_finish_rc_mem_list (StbCalSlabFinishRcMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_slab_finish_rc_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSlabFinishRcLoadList,
        ),
        "stb_cal_slab_finish_rc_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSlabFinishRcMemList,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalSlabFinish_RC_Arr"


class StbCalSlabLiveLoadMemList(StBridgeElement):
    """StbCalSlabLiveLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabLiveLoadList(StBridgeElement):
    """StbCalSlabLiveLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalSlabLiveLoadArr(StBridgeElement):
    """StbCalSlabLiveLoadArr

    Attributes:
        stb_cal_slab_live_load_list (StbCalSlabLiveLoadList): 子要素
        stb_cal_slab_live_load_mem_list (StbCalSlabLiveLoadMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_slab_live_load_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbCalSlabLiveLoadList
        ),
        "stb_cal_slab_live_load_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSlabLiveLoadMemList,
        ),
    }


class StbCalBraceFinishSMemList(StBridgeElement):
    """StbCalBraceFinishSMemList：StbCalBraceFinish_S_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBraceFinish_S_MemList"


class StbCalBraceFinishSLoadList(StBridgeElement):
    """StbCalBraceFinishSLoadList：StbCalBraceFinish_S_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBraceFinish_S_LoadList"


class StbCalBraceFinishSArr(StBridgeElement):
    """StbCalBraceFinishSArr：StbCalBraceFinish_S_Arr

    Attributes:
        stb_cal_brace_finish_s_load_list (StbCalBraceFinishSLoadList): 子要素
        stb_cal_brace_finish_s_mem_list (StbCalBraceFinishSMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_brace_finish_s_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceFinishSLoadList,
        ),
        "stb_cal_brace_finish_s_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceFinishSMemList,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBraceFinish_S_Arr"


class StbCalBeamMemberLoadMemList(StBridgeElement):
    """StbCalBeamMemberLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalBeamMemberLoadList(StBridgeElement):
    """StbCalBeamMemberLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalBeamMemberLoadArr(StBridgeElement):
    """StbCalBeamMemberLoadArr

    Attributes:
        stb_cal_beam_member_load_list (StbCalBeamMemberLoadList): 子要素
        stb_cal_beam_member_load_mem_list (StbCalBeamMemberLoadMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_beam_member_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamMemberLoadList,
        ),
        "stb_cal_beam_member_load_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamMemberLoadMemList,
        ),
    }


class StbCalBeamFinishSMemList(StBridgeElement):
    """StbCalBeamFinishSMemList：StbCalBeamFinish_S_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBeamFinish_S_MemList"


class StbCalBeamFinishSLoadList(StBridgeElement):
    """StbCalBeamFinishSLoadList：StbCalBeamFinish_S_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBeamFinish_S_LoadList"


class StbCalBeamFinishSArr(StBridgeElement):
    """StbCalBeamFinishSArr：StbCalBeamFinish_S_Arr

    Attributes:
        stb_cal_beam_finish_s_load_list (StbCalBeamFinishSLoadList): 子要素
        stb_cal_beam_finish_s_mem_list (StbCalBeamFinishSMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_beam_finish_s_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamFinishSLoadList,
        ),
        "stb_cal_beam_finish_s_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamFinishSMemList,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBeamFinish_S_Arr"


class StbCalBeamFinishRcMemList(StBridgeElement):
    """StbCalBeamFinishRcMemList：StbCalBeamFinish_RC_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBeamFinish_RC_MemList"


class StbCalBeamFinishRcLoadList(StBridgeElement):
    """StbCalBeamFinishRcLoadList：StbCalBeamFinish_RC_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBeamFinish_RC_LoadList"


class StbCalBeamFinishRcArr(StBridgeElement):
    """StbCalBeamFinishRcArr：StbCalBeamFinish_RC_Arr

    Attributes:
        stb_cal_beam_finish_rc_load_list (StbCalBeamFinishRcLoadList): 子要素
        stb_cal_beam_finish_rc_mem_list (StbCalBeamFinishRcMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_beam_finish_rc_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamFinishRcLoadList,
        ),
        "stb_cal_beam_finish_rc_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamFinishRcMemList,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBeamFinish_RC_Arr"


class StbCalGirderMemberLoadCalMemList(StBridgeElement):
    """StbCalGirderMemberLoadCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderMemberLoadMemList(StBridgeElement):
    """StbCalGirderMemberLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderMemberLoadList(StBridgeElement):
    """StbCalGirderMemberLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalGirderMemberLoadArr(StBridgeElement):
    """StbCalGirderMemberLoadArr

    Attributes:
        stb_cal_girder_member_load_list (StbCalGirderMemberLoadList): 子要素
        stb_cal_girder_member_load_mem_list (StbCalGirderMemberLoadMemList): 子要素
        stb_cal_girder_member_load_cal_mem_list (StbCalGirderMemberLoadCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_member_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderMemberLoadList,
        ),
        "stb_cal_girder_member_load_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderMemberLoadMemList
        ),
        "stb_cal_girder_member_load_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderMemberLoadCalMemList
        ),
    }


class StbCalGirderFinishSCalMemList(StBridgeElement):
    """StbCalGirderFinishSCalMemList：StbCalGirderFinish_S_CalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_S_CalMemList"


class StbCalGirderFinishSMemList(StBridgeElement):
    """StbCalGirderFinishSMemList：StbCalGirderFinish_S_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_S_MemList"


class StbCalGirderFinishSLoadList(StBridgeElement):
    """StbCalGirderFinishSLoadList：StbCalGirderFinish_S_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_S_LoadList"


class StbCalGirderFinishSArr(StBridgeElement):
    """StbCalGirderFinishSArr：StbCalGirderFinish_S_Arr

    Attributes:
        stb_cal_girder_finish_s_load_list (StbCalGirderFinishSLoadList): 子要素
        stb_cal_girder_finish_s_mem_list (StbCalGirderFinishSMemList): 子要素
        stb_cal_girder_finish_s_cal_mem_list (StbCalGirderFinishSCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_finish_s_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderFinishSLoadList,
        ),
        "stb_cal_girder_finish_s_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderFinishSMemList
        ),
        "stb_cal_girder_finish_s_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderFinishSCalMemList
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_S_Arr"


class StbCalGirderFinishRcCalMemList(StBridgeElement):
    """StbCalGirderFinishRcCalMemList：StbCalGirderFinish_RC_CalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_RC_CalMemList"


class StbCalGirderFinishRcMemList(StBridgeElement):
    """StbCalGirderFinishRcMemList：StbCalGirderFinish_RC_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_RC_MemList"


class StbCalGirderFinishRcLoadList(StBridgeElement):
    """StbCalGirderFinishRcLoadList：StbCalGirderFinish_RC_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_RC_LoadList"


class StbCalGirderFinishRcArr(StBridgeElement):
    """StbCalGirderFinishRcArr：StbCalGirderFinish_RC_Arr

    Attributes:
        stb_cal_girder_finish_rc_load_list (StbCalGirderFinishRcLoadList): 子要素
        stb_cal_girder_finish_rc_mem_list (StbCalGirderFinishRcMemList): 子要素
        stb_cal_girder_finish_rc_cal_mem_list (StbCalGirderFinishRcCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_finish_rc_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderFinishRcLoadList,
        ),
        "stb_cal_girder_finish_rc_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderFinishRcMemList
        ),
        "stb_cal_girder_finish_rc_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderFinishRcCalMemList
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_RC_Arr"


class StbCalColumnMemberLoadCalMemList(StBridgeElement):
    """StbCalColumnMemberLoadCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnMemberLoadMemList(StBridgeElement):
    """StbCalColumnMemberLoadMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnMemberLoadList(StBridgeElement):
    """StbCalColumnMemberLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalColumnMemberLoadArr(StBridgeElement):
    """StbCalColumnMemberLoadArr

    Attributes:
        stb_cal_column_member_load_list (StbCalColumnMemberLoadList): 子要素
        stb_cal_column_member_load_mem_list (StbCalColumnMemberLoadMemList): 子要素
        stb_cal_column_member_load_cal_mem_list (StbCalColumnMemberLoadCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_member_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnMemberLoadList,
        ),
        "stb_cal_column_member_load_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnMemberLoadMemList
        ),
        "stb_cal_column_member_load_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnMemberLoadCalMemList
        ),
    }


class StbCalColumnFinishSCalMemList(StBridgeElement):
    """StbCalColumnFinishSCalMemList：StbCalColumnFinish_S_CalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_S_CalMemList"


class StbCalColumnFinishSMemList(StBridgeElement):
    """StbCalColumnFinishSMemList：StbCalColumnFinish_S_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_S_MemList"


class StbCalColumnFinishSLoadList(StBridgeElement):
    """StbCalColumnFinishSLoadList：StbCalColumnFinish_S_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_S_LoadList"


class StbCalColumnFinishSArr(StBridgeElement):
    """StbCalColumnFinishSArr：StbCalColumnFinish_S_Arr

    Attributes:
        stb_cal_column_finish_s_load_list (StbCalColumnFinishSLoadList): 子要素
        stb_cal_column_finish_s_mem_list (StbCalColumnFinishSMemList): 子要素
        stb_cal_column_finish_s_cal_mem_list (StbCalColumnFinishSCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_finish_s_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnFinishSLoadList,
        ),
        "stb_cal_column_finish_s_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnFinishSMemList
        ),
        "stb_cal_column_finish_s_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnFinishSCalMemList
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_S_Arr"


class StbCalColumnFinishRcCalMemList(StBridgeElement):
    """StbCalColumnFinishRcCalMemList：StbCalColumnFinish_RC_CalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_RC_CalMemList"


class StbCalColumnFinishRcMemList(StBridgeElement):
    """StbCalColumnFinishRcMemList：StbCalColumnFinish_RC_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_RC_MemList"


class StbCalColumnFinishRcLoadList(StBridgeElement):
    """StbCalColumnFinishRcLoadList：StbCalColumnFinish_RC_LoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_RC_LoadList"


class StbCalColumnFinishRcArr(StBridgeElement):
    """StbCalColumnFinishRcArr：StbCalColumnFinish_RC_Arr

    Attributes:
        stb_cal_column_finish_rc_load_list (StbCalColumnFinishRcLoadList): 子要素
        stb_cal_column_finish_rc_mem_list (StbCalColumnFinishRcMemList): 子要素
        stb_cal_column_finish_rc_cal_mem_list (StbCalColumnFinishRcCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_finish_rc_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnFinishRcLoadList,
        ),
        "stb_cal_column_finish_rc_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnFinishRcMemList
        ),
        "stb_cal_column_finish_rc_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnFinishRcCalMemList
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_RC_Arr"


class StbCalLoadArrangements(StBridgeElement):
    """StbCalLoadArrangements

    Attributes:
        stb_cal_column_finish_rc_arr (list[StbCalColumnFinishRcArr]): 子要素
        stb_cal_column_finish_s_arr (list[StbCalColumnFinishSArr]): 子要素
        stb_cal_column_member_load_arr (list[StbCalColumnMemberLoadArr]): 子要素
        stb_cal_girder_finish_rc_arr (list[StbCalGirderFinishRcArr]): 子要素
        stb_cal_girder_finish_s_arr (list[StbCalGirderFinishSArr]): 子要素
        stb_cal_girder_member_load_arr (list[StbCalGirderMemberLoadArr]): 子要素
        stb_cal_beam_finish_rc_arr (list[StbCalBeamFinishRcArr]): 子要素
        stb_cal_beam_finish_s_arr (list[StbCalBeamFinishSArr]): 子要素
        stb_cal_beam_member_load_arr (list[StbCalBeamMemberLoadArr]): 子要素
        stb_cal_brace_finish_s_arr (list[StbCalBraceFinishSArr]): 子要素
        stb_cal_slab_live_load_arr (list[StbCalSlabLiveLoadArr]): 子要素
        stb_cal_slab_finish_rc_arr (list[StbCalSlabFinishRcArr]): 子要素
        stb_cal_slab_area_load_arr (list[StbCalSlabAreaLoadArr]): 子要素
        stb_cal_slab_pressure_load_arr (list[StbCalSlabPressureLoadArr]): 子要素
        stb_cal_wall_finish_rc_arr (list[StbCalWallFinishRcArr]): 子要素
        stb_cal_wall_area_load_arr (list[StbCalWallAreaLoadArr]): 子要素
        stb_cal_wall_pressure_load_arr (list[StbCalWallPressureLoadArr]): 子要素
        stb_cal_node_weight_arr (list[StbCalNodeWeightArr]): 子要素
        stb_cal_node_point_load_arr (list[StbCalNodePointLoadArr]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_finish_rc_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnFinishRcArr]
        ),
        "stb_cal_column_finish_s_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnFinishSArr]
        ),
        "stb_cal_column_member_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnMemberLoadArr]
        ),
        "stb_cal_girder_finish_rc_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderFinishRcArr]
        ),
        "stb_cal_girder_finish_s_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderFinishSArr]
        ),
        "stb_cal_girder_member_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderMemberLoadArr]
        ),
        "stb_cal_beam_finish_rc_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBeamFinishRcArr]
        ),
        "stb_cal_beam_finish_s_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBeamFinishSArr]
        ),
        "stb_cal_beam_member_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBeamMemberLoadArr]
        ),
        "stb_cal_brace_finish_s_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceFinishSArr]
        ),
        "stb_cal_slab_live_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSlabLiveLoadArr]
        ),
        "stb_cal_slab_finish_rc_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSlabFinishRcArr]
        ),
        "stb_cal_slab_area_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSlabAreaLoadArr]
        ),
        "stb_cal_slab_pressure_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSlabPressureLoadArr]
        ),
        "stb_cal_wall_finish_rc_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallFinishRcArr]
        ),
        "stb_cal_wall_area_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallAreaLoadArr]
        ),
        "stb_cal_wall_pressure_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallPressureLoadArr]
        ),
        "stb_cal_node_weight_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalNodeWeightArr]
        ),
        "stb_cal_node_point_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalNodePointLoadArr]
        ),
    }


class StbCalFloorDiaphragm(StBridgeElement):
    """StbCalFloorDiaphragm

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_floor_divided_area (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_floor_divided_area": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbCalFloorDiaphragms(StBridgeElement):
    """StbCalFloorDiaphragms

    Attributes:
        stb_cal_floor_diaphragm (list[StbCalFloorDiaphragm]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_floor_diaphragm": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalFloorDiaphragm]
        ),
    }


class StbCalNodePanel(StBridgeElement):
    """StbCalNodePanel

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        b_x (float): 属性
        d_x (float): 属性
        t_x (float): 属性
        b_y (float): 属性
        d_y (float): 属性
        t_y (float): 属性
        g (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "b_x": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="B_X"
        ),
        "d_x": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_X"
        ),
        "t_x": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="t_X"
        ),
        "b_y": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="B_Y"
        ),
        "d_y": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_Y"
        ),
        "t_y": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="t_Y"
        ),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="G"),
    }


class StbCalNodePanels(StBridgeElement):
    """StbCalNodePanels

    Attributes:
        stb_cal_node_panel (list[StbCalNodePanel]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_node_panel": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalNodePanel]
        ),
    }


class StbCalNodeRestriction(StBridgeElement):
    """StbCalNodeRestriction

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        e_x (StbCalNodeRestrictionEX): 属性
        e_y (StbCalNodeRestrictionEY): 属性
        e_z (StbCalNodeRestrictionEZ): 属性
        r_x (StbCalNodeRestrictionRX): 属性
        r_y (StbCalNodeRestrictionRY): 属性
        r_z (StbCalNodeRestrictionRZ): 属性
        e_spring_x (float): 属性
        e_spring_y (float): 属性
        e_spring_z (float): 属性
        r_spring_x (float): 属性
        r_spring_y (float): 属性
        r_spring_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "e_x": _FI(
            py_type=StbCalNodeRestrictionEX,
            data_type=_DT.STR_ENUM,
            xml_name="e_X",
            choices=("FIX", "FREE", "SPRING"),
        ),
        "e_y": _FI(
            py_type=StbCalNodeRestrictionEY,
            data_type=_DT.STR_ENUM,
            xml_name="e_Y",
            choices=("FIX", "FREE", "SPRING"),
        ),
        "e_z": _FI(
            py_type=StbCalNodeRestrictionEZ,
            data_type=_DT.STR_ENUM,
            xml_name="e_Z",
            choices=("FIX", "FREE", "SPRING"),
        ),
        "r_x": _FI(
            py_type=StbCalNodeRestrictionRX,
            data_type=_DT.STR_ENUM,
            xml_name="r_X",
            choices=("FIX", "FREE", "SPRING"),
        ),
        "r_y": _FI(
            py_type=StbCalNodeRestrictionRY,
            data_type=_DT.STR_ENUM,
            xml_name="r_Y",
            choices=("FIX", "FREE", "SPRING"),
        ),
        "r_z": _FI(
            py_type=StbCalNodeRestrictionRZ,
            data_type=_DT.STR_ENUM,
            xml_name="r_Z",
            choices=("FIX", "FREE", "SPRING"),
        ),
        "e_spring_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="e_spring_X"),
        "e_spring_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="e_spring_Y"),
        "e_spring_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="e_spring_Z"),
        "r_spring_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="r_spring_X"),
        "r_spring_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="r_spring_Y"),
        "r_spring_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="r_spring_Z"),
    }


class StbCalNodeRestrictions(StBridgeElement):
    """StbCalNodeRestrictions

    Attributes:
        stb_cal_node_restriction (list[StbCalNodeRestriction]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_node_restriction": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalNodeRestriction]
        ),
    }


class StbCalBraceStiffness(StBridgeElement):
    """StbCalBraceStiffness

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        ratio_axial (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "ratio_axial": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalWallStiffness(StBridgeElement):
    """StbCalWallStiffness

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        ratio_axial (float): 属性
        ratio_shear (float): 属性
        ratio_bending (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "ratio_axial": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_shear": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_bending": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalGirderStiffness(StBridgeElement):
    """StbCalGirderStiffness

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        ratio_shear_y (float): 属性
        ratio_shear_z (float): 属性
        ratio_bending_y (float): 属性
        ratio_bending_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "ratio_shear_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_shear_Y"
        ),
        "ratio_shear_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_shear_Z"
        ),
        "ratio_bending_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_bending_Y"
        ),
        "ratio_bending_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_bending_Z"
        ),
    }


class StbCalColumnStiffness(StBridgeElement):
    """StbCalColumnStiffness

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        ratio_axial_x (float): 属性
        ratio_axial_y (float): 属性
        ratio_shear_x (float): 属性
        ratio_shear_y (float): 属性
        ratio_bending_x (float): 属性
        ratio_bending_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "ratio_axial_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_axial_X"
        ),
        "ratio_axial_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_axial_Y"
        ),
        "ratio_shear_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_shear_X"
        ),
        "ratio_shear_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_shear_Y"
        ),
        "ratio_bending_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_bending_X"
        ),
        "ratio_bending_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="ratio_bending_Y"
        ),
    }


class StbCalMemberStiffnesses(StBridgeElement):
    """StbCalMemberStiffnesses

    Attributes:
        stb_cal_column_stiffness (list[StbCalColumnStiffness]): 子要素
        stb_cal_girder_stiffness (list[StbCalGirderStiffness]): 子要素
        stb_cal_wall_stiffness (list[StbCalWallStiffness]): 子要素
        stb_cal_brace_stiffness (list[StbCalBraceStiffness]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_stiffness": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnStiffness]
        ),
        "stb_cal_girder_stiffness": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderStiffness]
        ),
        "stb_cal_wall_stiffness": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallStiffness]
        ),
        "stb_cal_brace_stiffness": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceStiffness]
        ),
    }


class StbCalSlabSectionProperty(StBridgeElement):
    """StbCalSlabSectionProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        t (float): 属性
        e (float): 属性
        g (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "t": _FI(py_type=float, data_type=_DT.FLOAT),
        "e": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="E"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="G"),
    }


class StbCalBraceSectionProperty(StBridgeElement):
    """StbCalBraceSectionProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        a (float): 属性
        i (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "a": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="A"),
        "i": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalWallSectionProperty(StBridgeElement):
    """StbCalWallSectionProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        a (float): 属性
        as_ (float): 属性
        i (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "a": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="A"),
        "as_": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="As"),
        "i": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="I"),
    }


class StbCalGirderSectionProperty(StBridgeElement):
    """StbCalGirderSectionProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        a (float): 属性
        as_y (float): 属性
        as_z (float): 属性
        i_y (float): 属性
        i_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "a": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="A"),
        "as_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="As_Y"),
        "as_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="As_Z"),
        "i_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="I_Y"),
        "i_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="I_Z"),
    }


class StbCalColumnSectionProperty(StBridgeElement):
    """StbCalColumnSectionProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        a (float): 属性
        as_x (float): 属性
        as_y (float): 属性
        i_x (float): 属性
        i_y (float): 属性
        j (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "a": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="A"),
        "as_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="As_X"),
        "as_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="As_Y"),
        "i_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="I_X"),
        "i_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="I_Y"),
        "j": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="J"),
    }


class StbCalSectionProperties(StBridgeElement):
    """StbCalSectionProperties

    Attributes:
        stb_cal_column_section_property (list[StbCalColumnSectionProperty]): 子要素
        stb_cal_girder_section_property (list[StbCalGirderSectionProperty]): 子要素
        stb_cal_wall_section_property (list[StbCalWallSectionProperty]): 子要素
        stb_cal_brace_section_property (list[StbCalBraceSectionProperty]): 子要素
        stb_cal_slab_section_property (list[StbCalSlabSectionProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_section_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnSectionProperty]
        ),
        "stb_cal_girder_section_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderSectionProperty]
        ),
        "stb_cal_wall_section_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallSectionProperty]
        ),
        "stb_cal_brace_section_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceSectionProperty]
        ),
        "stb_cal_slab_section_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSlabSectionProperty]
        ),
    }


class StbCalGirderCriticalPosition(StBridgeElement):
    """StbCalGirderCriticalPosition

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        start (float): 属性
        end (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "start": _FI(py_type=float, data_type=_DT.FLOAT),
        "end": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalColumnCriticalPosition(StBridgeElement):
    """StbCalColumnCriticalPosition

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        bottom_x (float): 属性
        bottom_y (float): 属性
        top_x (float): 属性
        top_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "bottom_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="bottom_X"),
        "bottom_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="bottom_Y"),
        "top_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="top_X"),
        "top_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="top_Y"),
    }


class StbCalMemberCriticalPositions(StBridgeElement):
    """StbCalMemberCriticalPositions

    Attributes:
        stb_cal_column_critical_position (list[StbCalColumnCriticalPosition]): 子要素
        stb_cal_girder_critical_position (list[StbCalGirderCriticalPosition]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_critical_position": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnCriticalPosition]
        ),
        "stb_cal_girder_critical_position": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderCriticalPosition]
        ),
    }


class StbCalGirderRigidzone(StBridgeElement):
    """StbCalGirderRigidzone

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        start (float): 属性
        end (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "start": _FI(py_type=float, data_type=_DT.FLOAT),
        "end": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalColumnRigidzone(StBridgeElement):
    """StbCalColumnRigidzone

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        bottom_x (float): 属性
        bottom_y (float): 属性
        top_x (float): 属性
        top_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "bottom_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="bottom_X"),
        "bottom_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="bottom_Y"),
        "top_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="top_X"),
        "top_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="top_Y"),
    }


class StbCalMemberRigidzones(StBridgeElement):
    """StbCalMemberRigidzones

    Attributes:
        stb_cal_column_rigidzone (list[StbCalColumnRigidzone]): 子要素
        stb_cal_girder_rigidzone (list[StbCalGirderRigidzone]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_rigidzone": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnRigidzone]
        ),
        "stb_cal_girder_rigidzone": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderRigidzone]
        ),
    }


class StbCalGirderCondition(StBridgeElement):
    """StbCalGirderCondition

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        start (StbCalGirderConditionStart): 属性
        end (StbCalGirderConditionEnd): 属性
        start_spring (float): 属性
        end_spring (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "start": _FI(
            py_type=StbCalGirderConditionStart,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN", "SPRING"),
        ),
        "end": _FI(
            py_type=StbCalGirderConditionEnd,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN", "SPRING"),
        ),
        "start_spring": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_spring": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalColumnCondition(StBridgeElement):
    """StbCalColumnCondition

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        bottom_x (StbCalColumnConditionBottomX): 属性
        bottom_y (StbCalColumnConditionBottomY): 属性
        top_x (StbCalColumnConditionTopX): 属性
        top_y (StbCalColumnConditionTopY): 属性
        bottom_spring_x (float): 属性
        bottom_spring_y (float): 属性
        top_spring_x (float): 属性
        top_spring_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "bottom_x": _FI(
            py_type=StbCalColumnConditionBottomX,
            data_type=_DT.STR_ENUM,
            xml_name="bottom_X",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "bottom_y": _FI(
            py_type=StbCalColumnConditionBottomY,
            data_type=_DT.STR_ENUM,
            xml_name="bottom_Y",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "top_x": _FI(
            py_type=StbCalColumnConditionTopX,
            data_type=_DT.STR_ENUM,
            xml_name="top_X",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "top_y": _FI(
            py_type=StbCalColumnConditionTopY,
            data_type=_DT.STR_ENUM,
            xml_name="top_Y",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "bottom_spring_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="bottom_spring_X"
        ),
        "bottom_spring_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="bottom_spring_Y"
        ),
        "top_spring_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="top_spring_X"
        ),
        "top_spring_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="top_spring_Y"
        ),
    }


class StbCalMemberConditions(StBridgeElement):
    """StbCalMemberConditions

    Attributes:
        stb_cal_column_condition (list[StbCalColumnCondition]): 子要素
        stb_cal_girder_condition (list[StbCalGirderCondition]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_condition": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnCondition]
        ),
        "stb_cal_girder_condition": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderCondition]
        ),
    }


class StbCalCondition(StBridgeElement):
    """StbCalCondition

    Attributes:
        stb_cal_member_conditions (StbCalMemberConditions): 子要素
        stb_cal_member_rigidzones (StbCalMemberRigidzones): 子要素
        stb_cal_member_critical_positions (StbCalMemberCriticalPositions): 子要素
        stb_cal_section_properties (StbCalSectionProperties): 子要素
        stb_cal_member_stiffnesses (StbCalMemberStiffnesses): 子要素
        stb_cal_node_restrictions (StbCalNodeRestrictions): 子要素
        stb_cal_node_panels (StbCalNodePanels): 子要素
        stb_cal_floor_diaphragms (StbCalFloorDiaphragms): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_member_conditions": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberConditions
        ),
        "stb_cal_member_rigidzones": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberRigidzones
        ),
        "stb_cal_member_critical_positions": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberCriticalPositions
        ),
        "stb_cal_section_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSectionProperties
        ),
        "stb_cal_member_stiffnesses": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberStiffnesses
        ),
        "stb_cal_node_restrictions": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalNodeRestrictions
        ),
        "stb_cal_node_panels": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalNodePanels
        ),
        "stb_cal_floor_diaphragms": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFloorDiaphragms
        ),
    }


class StbCalEarthquakeforce(StBridgeElement):
    """StbCalEarthquakeforce

    Attributes:
        id_story (int): 属性
        id_seismic_condition (int): 属性
        force (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_seismic_condition": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "force": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbCalEarthquakeforces(StBridgeElement):
    """StbCalEarthquakeforces

    Attributes:
        id_loadcase (int): 属性
        stb_cal_earthquakeforce (list[StbCalEarthquakeforce]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_cal_earthquakeforce": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalEarthquakeforce]
        ),
    }


class StbCalShearforce(StBridgeElement):
    """StbCalShearforce

    Attributes:
        id_story (int): 属性
        id_seismic_condition (int): 属性
        force (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_seismic_condition": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "force": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbCalShearforces(StBridgeElement):
    """StbCalShearforces

    Attributes:
        id_loadcase (int): 属性
        stb_cal_shearforce (list[StbCalShearforce]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_cal_shearforce": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalShearforce]
        ),
    }


class StbCalShearcoefficient(StBridgeElement):
    """StbCalShearcoefficient

    Attributes:
        id_story (int): 属性
        id_seismic_condition (int): 属性
        coefficient (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_seismic_condition": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "coefficient": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbCalShearcoefficients(StBridgeElement):
    """StbCalShearcoefficients

    Attributes:
        id_loadcase (int): 属性
        stb_cal_shearcoefficient (list[StbCalShearcoefficient]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_cal_shearcoefficient": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalShearcoefficient]
        ),
    }


class StbCalGravityPointWeight(StBridgeElement):
    """StbCalGravityPointWeight

    Attributes:
        weight (float): 属性
        id_story (int): 属性
        id_seismic_condition (int): 属性
        x (float): 属性
        y (float): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_seismic_condition": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalGravityPointWeights(StBridgeElement):
    """StbCalGravityPointWeights

    Attributes:
        stb_cal_gravity_point_weight (list[StbCalGravityPointWeight]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_gravity_point_weight": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalGravityPointWeight]
        ),
    }


class StbCalSeismicWeight(StBridgeElement):
    """StbCalSeismicWeight

    Attributes:
        id_story (int): 属性
        id_seismic_condition (int): 属性
        weight (float): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_seismic_condition": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalSeismicWeights(StBridgeElement):
    """StbCalSeismicWeights

    Attributes:
        stb_cal_seismic_weight (list[StbCalSeismicWeight]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_seismic_weight": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalSeismicWeight]
        ),
    }


class StbCalSeismicDirection(StBridgeElement):
    """StbCalSeismicDirection

    Attributes:
        id_loadcase (int): 属性
        baseshear_coefficient1 (float): 属性
        baseshear_coefficient2 (float): 属性
        lateral_coefficient (float): 属性
        height (float): 属性
        natural_period (float): 属性
        id_seismic_condition (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "baseshear_coefficient1": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True
        ),
        "baseshear_coefficient2": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True
        ),
        "lateral_coefficient": _FI(py_type=float, data_type=_DT.FLOAT),
        "height": _FI(py_type=float, data_type=_DT.FLOAT),
        "natural_period": _FI(py_type=float, data_type=_DT.FLOAT),
        "id_seismic_condition": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbCalSeismicDirections(StBridgeElement):
    """StbCalSeismicDirections

    Attributes:
        stb_cal_seismic_direction (list[StbCalSeismicDirection]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_seismic_direction": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalSeismicDirection]
        ),
    }


class StbCalSeismicConditionGroup(StBridgeElement):
    """StbCalSeismicConditionGroup

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_floor_divided_area (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_floor_divided_area": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbCalSeismicConditionGroups(StBridgeElement):
    """StbCalSeismicConditionGroups

    Attributes:
        stb_cal_seismic_condition_group (list[StbCalSeismicConditionGroup]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_seismic_condition_group": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalSeismicConditionGroup]
        ),
    }


class StbCalSeismic(StBridgeElement):
    """StbCalSeismic

    Attributes:
        stb_cal_seismic_condition_groups (StbCalSeismicConditionGroups): 子要素
        stb_cal_seismic_directions (StbCalSeismicDirections): 子要素
        stb_cal_seismic_weights (StbCalSeismicWeights): 子要素
        stb_cal_gravity_point_weights (StbCalGravityPointWeights): 子要素
        stb_cal_shearcoefficients (list[StbCalShearcoefficients]): 子要素
        stb_cal_shearforces (list[StbCalShearforces]): 子要素
        stb_cal_earthquakeforces (list[StbCalEarthquakeforces]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_seismic_condition_groups": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalSeismicConditionGroups,
        ),
        "stb_cal_seismic_directions": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSeismicDirections
        ),
        "stb_cal_seismic_weights": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSeismicWeights
        ),
        "stb_cal_gravity_point_weights": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGravityPointWeights
        ),
        "stb_cal_shearcoefficients": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalShearcoefficients]
        ),
        "stb_cal_shearforces": _FI(kind=_FK.ELEMENT, py_type=list[StbCalShearforces]),
        "stb_cal_earthquakeforces": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalEarthquakeforces]
        ),
    }


class StbCalSelectedNodeAddedWeight(StBridgeElement):
    """StbCalSelectedNodeAddedWeight

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        id_loadcase (int): 属性
        loadcase (str): 属性
        id_story (int): 属性
        id_seismic_condition (int): 属性
        x (float): 属性
        y (float): 属性
        weight (float): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "loadcase": _FI(py_type=str, data_type=_DT.STR),
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_seismic_condition": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalNodeAddedWeight(StBridgeElement):
    """StbCalNodeAddedWeight

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        id_loadcase (int): 属性
        loadcase (str): 属性
        weight (float): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "loadcase": _FI(py_type=str, data_type=_DT.STR),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalAddedWeights(StBridgeElement):
    """StbCalAddedWeights

    Attributes:
        stb_cal_node_added_weight (list[StbCalNodeAddedWeight]): 子要素
        stb_cal_selected_node_added_weight (list[StbCalSelectedNodeAddedWeight]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_node_added_weight": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalNodeAddedWeight]
        ),
        "stb_cal_selected_node_added_weight": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSelectedNodeAddedWeight]
        ),
    }


class StbCalEarthHydrostaticPressureLoad(StBridgeElement):
    """StbCalEarthHydrostaticPressureLoad

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        id_loadcase (int): 属性
        loadcase (str): 属性
        p1 (float): 属性
        p2 (float): 属性
        p3 (float): 属性
        p4 (float): 属性
        coordinate_load (StbCalEarthHydrostaticPressureLoadCoordinateLoad): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "loadcase": _FI(py_type=str, data_type=_DT.STR),
        "p1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P1"),
        "p2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P2"),
        "p3": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P3"),
        "p4": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P4"),
        "coordinate_load": _FI(
            py_type=StbCalEarthHydrostaticPressureLoadCoordinateLoad,
            data_type=_DT.STR_ENUM,
            choices=("plus", "minus"),
        ),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalSelectedPointLoad(StBridgeElement):
    """StbCalSelectedPointLoad

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        id_loadcase (int): 属性
        loadcase (str): 属性
        id_story (int): 属性
        id_seismic_condition (int): 属性
        x (float): 属性
        y (float): 属性
        p1 (float): 属性
        p2 (float): 属性
        p3 (float): 属性
        p4 (float): 属性
        p5 (float): 属性
        p6 (float): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "loadcase": _FI(py_type=str, data_type=_DT.STR),
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_seismic_condition": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "p1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P1"),
        "p2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P2"),
        "p3": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P3"),
        "p4": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P4"),
        "p5": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P5"),
        "p6": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P6"),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalPointLoad(StBridgeElement):
    """StbCalPointLoad

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        id_loadcase (int): 属性
        loadcase (str): 属性
        p1 (float): 属性
        p2 (float): 属性
        p3 (float): 属性
        p4 (float): 属性
        p5 (float): 属性
        p6 (float): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "loadcase": _FI(py_type=str, data_type=_DT.STR),
        "p1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P1"),
        "p2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P2"),
        "p3": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P3"),
        "p4": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P4"),
        "p5": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P5"),
        "p6": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P6"),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalAreaLoad(StBridgeElement):
    """StbCalAreaLoad

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        id_loadcase (int): 属性
        loadcase (str): 属性
        type (StbCalAreaLoadType): 属性
        p1 (float): 属性
        coordinate_load (StbCalAreaLoadCoordinateLoad): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "loadcase": _FI(py_type=str, data_type=_DT.STR),
        "type": _FI(
            py_type=StbCalAreaLoadType,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("51", "52"),
        ),
        "p1": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="P1"),
        "coordinate_load": _FI(
            py_type=StbCalAreaLoadCoordinateLoad,
            data_type=_DT.STR_ENUM,
            choices=("LOCAL", "GLOBAL", "PROJECTION"),
        ),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalMemberLoad(StBridgeElement):
    """StbCalMemberLoad

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        id_loadcase (int): 属性
        loadcase (str): 属性
        type (int): 属性
        p1 (float): 属性
        p2 (float): 属性
        p3 (float): 属性
        p4 (float): 属性
        p5 (float): 属性
        p6 (float): 属性
        coordinate_load (StbCalMemberLoadCoordinateLoad): 属性
        direction_load (StbCalMemberLoadDirectionLoad): 属性
        description (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "id_loadcase": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "loadcase": _FI(py_type=str, data_type=_DT.STR),
        "type": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "p1": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="P1"),
        "p2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P2"),
        "p3": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P3"),
        "p4": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P4"),
        "p5": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P5"),
        "p6": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P6"),
        "coordinate_load": _FI(
            py_type=StbCalMemberLoadCoordinateLoad,
            data_type=_DT.STR_ENUM,
            choices=("LOCAL", "GLOBAL", "PROJECTION"),
        ),
        "direction_load": _FI(
            py_type=StbCalMemberLoadDirectionLoad,
            data_type=_DT.STR_ENUM,
            choices=("X", "Y"),
        ),
        "description": _FI(py_type=str, data_type=_DT.STR),
    }


class StbCalAdditionalLoads(StBridgeElement):
    """StbCalAdditionalLoads

    Attributes:
        stb_cal_member_load (list[StbCalMemberLoad]): 子要素
        stb_cal_area_load (list[StbCalAreaLoad]): 子要素
        stb_cal_point_load (list[StbCalPointLoad]): 子要素
        stb_cal_selected_point_load (list[StbCalSelectedPointLoad]): 子要素
        stb_cal_earth_hydrostatic_pressure_load (list[StbCalEarthHydrostaticPressureLoad]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_member_load": _FI(kind=_FK.ELEMENT, py_type=list[StbCalMemberLoad]),
        "stb_cal_area_load": _FI(kind=_FK.ELEMENT, py_type=list[StbCalAreaLoad]),
        "stb_cal_point_load": _FI(kind=_FK.ELEMENT, py_type=list[StbCalPointLoad]),
        "stb_cal_selected_point_load": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSelectedPointLoad]
        ),
        "stb_cal_earth_hydrostatic_pressure_load": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalEarthHydrostaticPressureLoad]
        ),
    }


class StbCalLoadCase(StBridgeElement):
    """StbCalLoadCase

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        category (StbCalLoadCaseCategory): 属性
        kind (StbCalLoadCaseKind): 属性
        name (str): 属性
        direction (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "category": _FI(
            py_type=StbCalLoadCaseCategory,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STANDARD", "ANALYSIS"),
        ),
        "kind": _FI(
            py_type=StbCalLoadCaseKind,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("DL", "LLf", "LLe", "TL", "S", "K", "W", "OTHER"),
        ),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "direction": _FI(py_type=int, data_type=_DT.INT),
    }


class StbCalLoadCases(StBridgeElement):
    """StbCalLoadCases

    Attributes:
        stb_cal_load_case (list[StbCalLoadCase]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_load_case": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalLoadCase]
        ),
    }


class StbCalBraceFinishS(StBridgeElement):
    """StbCalBraceFinishS：StbCalBraceFinish_S

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        type (StbCalBraceFinishSType): 属性
        weight (float): 属性
        covering_unit_weight (float): 属性
        covering_size (float): 属性
        covering_type (StbCalBraceFinishSCoveringType): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "type": _FI(
            py_type=StbCalBraceFinishSType,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3"),
        ),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_type": _FI(
            py_type=StbCalBraceFinishSCoveringType,
            data_type=_DT.STR_ENUM,
            choices=("A", "B", "C", "D"),
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalBraceFinish_S"


class StbCalGirderFinishS(StBridgeElement):
    """StbCalGirderFinishS：StbCalGirderFinish_S

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        type (StbCalGirderFinishSType): 属性
        weight (float): 属性
        covering_unit_weight (float): 属性
        covering_size (float): 属性
        covering_type (StbCalGirderFinishSCoveringType): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "type": _FI(
            py_type=StbCalGirderFinishSType,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3"),
        ),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_type": _FI(
            py_type=StbCalGirderFinishSCoveringType,
            data_type=_DT.STR_ENUM,
            choices=("A", "B", "C", "D"),
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_S"


class StbCalColumnFinishS(StBridgeElement):
    """StbCalColumnFinishS：StbCalColumnFinish_S

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        type (StbCalColumnFinishSType): 属性
        weight (float): 属性
        covering_unit_weight (float): 属性
        covering_size (float): 属性
        covering_type (StbCalColumnFinishSCoveringType): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "type": _FI(
            py_type=StbCalColumnFinishSType,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3"),
        ),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_type": _FI(
            py_type=StbCalColumnFinishSCoveringType,
            data_type=_DT.STR_ENUM,
            choices=("A", "B", "C", "D"),
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_S"


class StbCalMemberFinishesS(StBridgeElement):
    """StbCalMemberFinishesS：StbCalMemberFinishes_S

    Attributes:
        stb_cal_column_finish_s (list[StbCalColumnFinishS]): 子要素
        stb_cal_girder_finish_s (list[StbCalGirderFinishS]): 子要素
        stb_cal_brace_finish_s (list[StbCalBraceFinishS]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_finish_s": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnFinishS]
        ),
        "stb_cal_girder_finish_s": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderFinishS]
        ),
        "stb_cal_brace_finish_s": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceFinishS]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalMemberFinishes_S"


class StbCalWallFinishRc(StBridgeElement):
    """StbCalWallFinishRc：StbCalWallFinish_RC

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        type (StbCalWallFinishRcType): 属性
        weight (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "type": _FI(
            py_type=StbCalWallFinishRcType,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3"),
        ),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalWallFinish_RC"


class StbCalSlabFinishRc(StBridgeElement):
    """StbCalSlabFinishRc：StbCalSlabFinish_RC

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        weight (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalSlabFinish_RC"


class StbCalGirderFinishRc(StBridgeElement):
    """StbCalGirderFinishRc：StbCalGirderFinish_RC

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        type (StbCalGirderFinishRcType): 属性
        weight (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "type": _FI(
            py_type=StbCalGirderFinishRcType,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3"),
        ),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_RC"


class StbCalColumnFinishRc(StBridgeElement):
    """StbCalColumnFinishRc：StbCalColumnFinish_RC

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        type (StbCalColumnFinishRcType): 属性
        weight (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "type": _FI(
            py_type=StbCalColumnFinishRcType,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3"),
        ),
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalColumnFinish_RC"


class StbCalMemberFinishesRc(StBridgeElement):
    """StbCalMemberFinishesRc：StbCalMemberFinishes_RC

    Attributes:
        stb_cal_column_finish_rc (list[StbCalColumnFinishRc]): 子要素
        stb_cal_girder_finish_rc (list[StbCalGirderFinishRc]): 子要素
        stb_cal_slab_finish_rc (list[StbCalSlabFinishRc]): 子要素
        stb_cal_wall_finish_rc (list[StbCalWallFinishRc]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_finish_rc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnFinishRc]
        ),
        "stb_cal_girder_finish_rc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderFinishRc]
        ),
        "stb_cal_slab_finish_rc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalSlabFinishRc]
        ),
        "stb_cal_wall_finish_rc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalWallFinishRc]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalMemberFinishes_RC"


class StbCalFloorFinishSMember(StBridgeElement):
    """StbCalFloorFinishSMember：StbCalFloorFinish_S_member

    Attributes:
        member_type (StbCalFloorFinishSMemberMemberType): 属性
        finishing_weight (float): 属性
        covering_type (StbCalFloorFinishSMemberCoveringType): 属性
        covering_size (float): 属性
        covering_unit_weight (float): 属性
        load_ratio (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "member_type": _FI(
            py_type=StbCalFloorFinishSMemberMemberType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("COLUMN", "GIRDER", "BEAM", "CANTI", "BRACE"),
        ),
        "finishing_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_type": _FI(
            py_type=StbCalFloorFinishSMemberCoveringType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("A", "B", "C", "D"),
        ),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "load_ratio": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalFloorFinish_S_member"


class StbCalFloorFinishS(StBridgeElement):
    """StbCalFloorFinishS：StbCalFloorFinish_S

    Attributes:
        stb_cal_floor_finish_s_member (list[StbCalFloorFinishSMember]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_floor_finish_s_member": _FI(
            kind=_FK.ELEMENT,
            max_occurs=5,
            min_occurs=1,
            py_type=list[StbCalFloorFinishSMember],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalFloorFinish_S"


class StbCalFloorFinishRc(StBridgeElement):
    """StbCalFloorFinishRc：StbCalFloorFinish_RC

    Attributes:
        weight_girder (float): 属性
        type_girder (StbCalFloorFinishRcTypeGirder): 属性
        weight_column (float): 属性
        type_column (StbCalFloorFinishRcTypeColumn): 属性
        weight_beam (float): 属性
        type_beam (StbCalFloorFinishRcTypeBeam): 属性
        weight_canti (float): 属性
        type_canti (StbCalFloorFinishRcTypeCanti): 属性
        weight_wall (float): 属性
        type_wall (StbCalFloorFinishRcTypeWall): 属性
        weight_slab (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "weight_girder": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_girder": _FI(
            py_type=StbCalFloorFinishRcTypeGirder,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_column": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_column": _FI(
            py_type=StbCalFloorFinishRcTypeColumn,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_beam": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_beam": _FI(
            py_type=StbCalFloorFinishRcTypeBeam,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_canti": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_canti": _FI(
            py_type=StbCalFloorFinishRcTypeCanti,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_wall": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_wall": _FI(
            py_type=StbCalFloorFinishRcTypeWall,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_slab": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalFloorFinish_RC"


class StbCalFloorFinish(StBridgeElement):
    """StbCalFloorFinish

    Attributes:
        id_story (int): 属性
        stb_cal_floor_finish_rc (StbCalFloorFinishRc): 子要素
        stb_cal_floor_finish_s (StbCalFloorFinishS): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_cal_floor_finish_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFloorFinishRc
        ),
        "stb_cal_floor_finish_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFloorFinishS
        ),
    }


class StbCalFloorFinishes(StBridgeElement):
    """StbCalFloorFinishes

    Attributes:
        stb_cal_floor_finish (list[StbCalFloorFinish]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_floor_finish": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalFloorFinish]
        ),
    }


class StbCalFinishSMember(StBridgeElement):
    """StbCalFinishSMember：StbCalFinish_S_member

    Attributes:
        member_type (StbCalFinishSMemberMemberType): 属性
        finishing_weight (float): 属性
        covering_type (StbCalFinishSMemberCoveringType): 属性
        covering_size (float): 属性
        covering_unit_weight (float): 属性
        load_ratio (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "member_type": _FI(
            py_type=StbCalFinishSMemberMemberType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("COLUMN", "GIRDER", "BEAM", "CANTI", "BRACE"),
        ),
        "finishing_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_type": _FI(
            py_type=StbCalFinishSMemberCoveringType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("A", "B", "C", "D"),
        ),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "load_ratio": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalFinish_S_member"


class StbCalFinishS(StBridgeElement):
    """StbCalFinishS：StbCalFinish_S

    Attributes:
        stb_cal_finish_s_member (list[StbCalFinishSMember]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_finish_s_member": _FI(
            kind=_FK.ELEMENT,
            max_occurs=5,
            min_occurs=1,
            py_type=list[StbCalFinishSMember],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalFinish_S"


class StbCalFinishRc(StBridgeElement):
    """StbCalFinishRc：StbCalFinish_RC

    Attributes:
        weight_girder (float): 属性
        type_girder (StbCalFinishRcTypeGirder): 属性
        weight_column (float): 属性
        type_column (StbCalFinishRcTypeColumn): 属性
        weight_beam (float): 属性
        type_beam (StbCalFinishRcTypeBeam): 属性
        weight_canti (float): 属性
        type_canti (StbCalFinishRcTypeCanti): 属性
        weight_wall (float): 属性
        type_wall (StbCalFinishRcTypeWall): 属性
        weight_slab (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "weight_girder": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_girder": _FI(
            py_type=StbCalFinishRcTypeGirder,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_column": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_column": _FI(
            py_type=StbCalFinishRcTypeColumn,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_beam": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_beam": _FI(
            py_type=StbCalFinishRcTypeBeam,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_canti": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_canti": _FI(
            py_type=StbCalFinishRcTypeCanti,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_wall": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_wall": _FI(
            py_type=StbCalFinishRcTypeWall,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            choices=("1", "2", "3"),
        ),
        "weight_slab": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalFinish_RC"


class StbCalFinish(StBridgeElement):
    """StbCalFinish

    Attributes:
        stb_cal_finish_rc (StbCalFinishRc): 子要素
        stb_cal_finish_s (StbCalFinishS): 子要素
        stb_cal_floor_finishes (StbCalFloorFinishes): 子要素
        stb_cal_member_finishes_rc (StbCalMemberFinishesRc): 子要素
        stb_cal_member_finishes_s (StbCalMemberFinishesS): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_finish_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFinishRc
        ),
        "stb_cal_finish_s": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFinishS),
        "stb_cal_floor_finishes": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFloorFinishes
        ),
        "stb_cal_member_finishes_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberFinishesRc
        ),
        "stb_cal_member_finishes_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberFinishesS
        ),
    }


class StbCalLoad(StBridgeElement):
    """StbCalLoad

    Attributes:
        stb_cal_finish (StbCalFinish): 子要素
        stb_cal_load_cases (StbCalLoadCases): 子要素
        stb_cal_additional_loads (StbCalAdditionalLoads): 子要素
        stb_cal_added_weights (StbCalAddedWeights): 子要素
        stb_cal_seismic (StbCalSeismic): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_finish": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFinish),
        "stb_cal_load_cases": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalLoadCases
        ),
        "stb_cal_additional_loads": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalAdditionalLoads
        ),
        "stb_cal_added_weights": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalAddedWeights
        ),
        "stb_cal_seismic": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSeismic),
    }


class StbCalGirder(StBridgeElement):
    """StbCalGirder

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_parent (int): 属性
        id_node_start (int): 属性
        id_node_end (int): 属性
        rotate (float): 属性
        id_section (int): 属性
        section_io_start (StbCalGirderSectionIoStart): 属性
        section_io_end (StbCalGirderSectionIoEnd): 属性
        kind_structure (StbCalGirderKindStructure): 属性
        is_foundation (bool): 属性
        strength_concrete (str): 属性
        offset_start_x (float): 属性
        offset_start_y (float): 属性
        offset_start_z (float): 属性
        offset_end_x (float): 属性
        offset_end_y (float): 属性
        offset_end_z (float): 属性
        thickness_add_top (float): 属性
        thickness_add_bottom (float): 属性
        thickness_add_right (float): 属性
        thickness_add_left (float): 属性
        haunch_start (float): 属性
        haunch_end (float): 属性
        kind_haunch_start (StbCalGirderKindHaunchStart): 属性
        kind_haunch_end (StbCalGirderKindHaunchEnd): 属性
        type_haunch_h (StbCalGirderTypeHaunchH): 属性
        type_haunch_v (StbCalGirderTypeHaunchV): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_parent": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_io_start": _FI(
            py_type=StbCalGirderSectionIoStart,
            data_type=_DT.STR_ENUM,
            choices=("OUT", "IN", "CENTER"),
        ),
        "section_io_end": _FI(
            py_type=StbCalGirderSectionIoEnd,
            data_type=_DT.STR_ENUM,
            choices=("OUT", "IN", "CENTER"),
        ),
        "kind_structure": _FI(
            py_type=StbCalGirderKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "SRC", "UNDEFINED"),
        ),
        "is_foundation": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isFoundation"
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "offset_start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_X"
        ),
        "offset_start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Y"
        ),
        "offset_start_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Z"
        ),
        "offset_end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_X"
        ),
        "offset_end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Y"
        ),
        "offset_end_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Z"
        ),
        "thickness_add_top": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_bottom": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_right": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_left": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "haunch_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "haunch_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_haunch_start": _FI(
            py_type=StbCalGirderKindHaunchStart,
            data_type=_DT.STR_ENUM,
            choices=("SLOPE", "DROP"),
        ),
        "kind_haunch_end": _FI(
            py_type=StbCalGirderKindHaunchEnd,
            data_type=_DT.STR_ENUM,
            choices=("SLOPE", "DROP"),
        ),
        "type_haunch_h": _FI(
            py_type=StbCalGirderTypeHaunchH,
            data_type=_DT.STR_ENUM,
            xml_name="type_haunch_H",
            choices=("BOTH", "RIGHT", "LEFT"),
        ),
        "type_haunch_v": _FI(
            py_type=StbCalGirderTypeHaunchV,
            data_type=_DT.STR_ENUM,
            xml_name="type_haunch_V",
            choices=("BOTH", "TOP", "BOTTOM"),
        ),
    }


class StbCalGirders(StBridgeElement):
    """StbCalGirders

    Attributes:
        stb_cal_girder (list[StbCalGirder]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalGirder]
        ),
    }


class StbCalColumn(StBridgeElement):
    """StbCalColumn

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_parent (int): 属性
        id_node_bottom (int): 属性
        id_node_top (int): 属性
        rotate (float): 属性
        id_section (int): 属性
        kind_structure (StbCalColumnKindStructure): 属性
        strength_concrete (str): 属性
        offset_bottom_x (float): 属性
        offset_bottom_y (float): 属性
        offset_bottom_z (float): 属性
        offset_top_x (float): 属性
        offset_top_y (float): 属性
        offset_top_z (float): 属性
        thickness_add_start_x (float): 属性
        thickness_add_end_x (float): 属性
        thickness_add_start_y (float): 属性
        thickness_add_end_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_parent": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_bottom": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_top": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbCalColumnKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "SRC", "CFT", "UNDEFINED"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "offset_bottom_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_X"
        ),
        "offset_bottom_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_Y"
        ),
        "offset_bottom_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_Z"
        ),
        "offset_top_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_X"
        ),
        "offset_top_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_Y"
        ),
        "offset_top_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_Z"
        ),
        "thickness_add_start_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_X",
        ),
        "thickness_add_end_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_X",
        ),
        "thickness_add_start_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_Y",
        ),
        "thickness_add_end_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_Y",
        ),
    }


class StbCalColumns(StBridgeElement):
    """StbCalColumns

    Attributes:
        stb_cal_column (list[StbCalColumn]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalColumn]
        ),
    }


class StbCalStoryDivided(StBridgeElement):
    """StbCalStoryDivided

    Attributes:
        id_story (int): 属性
        name_floor (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_story": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "name_floor": _FI(py_type=str, data_type=_DT.STR),
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbCalFloorDividedArea(StBridgeElement):
    """StbCalFloorDividedArea

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        is_include (bool): 属性
        stb_cal_story_divided (list[StbCalStoryDivided]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "is_include": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isInclude"),
        "stb_cal_story_divided": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalStoryDivided]
        ),
    }


class StbCalFloorDividedAreas(StBridgeElement):
    """StbCalFloorDividedAreas

    Attributes:
        stb_cal_floor_divided_area (list[StbCalFloorDividedArea]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_floor_divided_area": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalFloorDividedArea]
        ),
    }


class StbCalLiveload(StBridgeElement):
    """StbCalLiveload

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        type (StbCalLiveloadType): 属性
        liveload_slab (float): 属性
        liveload_beam (float): 属性
        liveload_frame (float): 属性
        liveload_seismic (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbCalLiveloadType,
            data_type=_DT.INT_ENUM,
            xml_type="nonNegativeInteger",
            required=True,
            choices=("0", "1", "2", "3", "4", "5", "6", "7"),
        ),
        "liveload_slab": _FI(py_type=float, data_type=_DT.FLOAT),
        "liveload_beam": _FI(py_type=float, data_type=_DT.FLOAT),
        "liveload_frame": _FI(py_type=float, data_type=_DT.FLOAT),
        "liveload_seismic": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalLiveloads(StBridgeElement):
    """StbCalLiveloads

    Attributes:
        stb_cal_liveload (list[StbCalLiveload]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_liveload": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbCalLiveload]
        ),
    }


class StbCalSnowCondition(StBridgeElement):
    """StbCalSnowCondition

    Attributes:
        unit_weight (float): 属性
        snow_depth (float): 属性
        region (int): 属性
        altitude (float): 属性
        sea_coverage (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "unit_weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "snow_depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "region": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "altitude": _FI(py_type=float, data_type=_DT.FLOAT),
        "sea_coverage": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalWindCondition(StBridgeElement):
    """StbCalWindCondition

    Attributes:
        roughness (StbCalWindConditionRoughness): 属性
        wind_speed (float): 属性
        height (float): 属性
        reduction_coefficient (float): 属性
        velocity_pressure (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "roughness": _FI(
            py_type=StbCalWindConditionRoughness,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3", "4"),
        ),
        "wind_speed": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "height": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "reduction_coefficient": _FI(py_type=float, data_type=_DT.FLOAT),
        "velocity_pressure": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalSeismicCondition(StBridgeElement):
    """StbCalSeismicCondition

    Attributes:
        zone (float): 属性
        importance (float): 属性
        soil (StbCalSeismicConditionSoil): 属性
        tc (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "zone": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "importance": _FI(py_type=float, data_type=_DT.FLOAT),
        "soil": _FI(
            py_type=StbCalSeismicConditionSoil,
            data_type=_DT.INT_ENUM,
            xml_type="positiveInteger",
            required=True,
            choices=("1", "2", "3"),
        ),
        "tc": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Tc"),
    }


class StbCalLoadCondition(StBridgeElement):
    """StbCalLoadCondition

    Attributes:
        stb_cal_seismic_condition (StbCalSeismicCondition): 子要素
        stb_cal_wind_condition (StbCalWindCondition): 子要素
        stb_cal_snow_condition (StbCalSnowCondition): 子要素
        stb_cal_liveloads (StbCalLiveloads): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_seismic_condition": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSeismicCondition
        ),
        "stb_cal_wind_condition": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalWindCondition
        ),
        "stb_cal_snow_condition": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSnowCondition
        ),
        "stb_cal_liveloads": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalLiveloads
        ),
    }


class StbCalCommon(StBridgeElement):
    """StbCalCommon

    Attributes:
        stb_cal_load_condition (StbCalLoadCondition): 子要素
        stb_cal_floor_divided_areas (StbCalFloorDividedAreas): 子要素
        stb_cal_columns (StbCalColumns): 子要素
        stb_cal_girders (StbCalGirders): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_load_condition": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbCalLoadCondition
        ),
        "stb_cal_floor_divided_areas": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFloorDividedAreas
        ),
        "stb_cal_columns": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumns),
        "stb_cal_girders": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirders),
    }


class StbCalData(StBridgeElement):
    """StbCalData

    Attributes:
        stb_cal_common (StbCalCommon): 子要素
        stb_cal_load (StbCalLoad): 子要素
        stb_cal_condition (StbCalCondition): 子要素
        stb_cal_load_arrangements (StbCalLoadArrangements): 子要素
        stb_cal_condition_arrangements (StbCalConditionArrangements): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_common": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalCommon),
        "stb_cal_load": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalLoad),
        "stb_cal_condition": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalCondition
        ),
        "stb_cal_load_arrangements": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalLoadArrangements
        ),
        "stb_cal_condition_arrangements": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalConditionArrangements
        ),
    }


class StbExtPropertyDef(StBridgeElement):
    """拡張属性定義：StbExtPropertyDef

    Attributes:
        key (str): 属性 変数名
        type (StbExtPropertyDefType): 属性 変数型で以下のいずれかの値をとるstring：文字型integer：整数型double：実数型boolean：論理型
        default (str): 属性 省略値
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "key": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbExtPropertyDefType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("string", "integer", "double", "boolean"),
        ),
        "default": _FI(py_type=str, data_type=_DT.STR),
    }


class StbExtElement(StBridgeElement):
    """拡張子要素：StbExtElement

    Attributes:
        object_name (str): 属性 ST-Bridgeの要素名
        element_name (str): 属性 拡張する子要素の名前
        stb_ext_property_def (list[StbExtPropertyDef]): 子要素 StbExtPropertyDef(拡張属性定義)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "object_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "element_name": _FI(py_type=str, data_type=_DT.STR),
        "stb_ext_property_def": _FI(kind=_FK.ELEMENT, py_type=list[StbExtPropertyDef]),
    }


class StbExtProperty(StBridgeElement):
    """拡張属性：StbExtProperty

    Attributes:
        key (str): 属性 変数名
        type (StbExtPropertyType): 属性 変数型で以下のいずれかの値をとるstring：文字型integer：整数型double：実数型boolean：論理型
        value (str): 属性 値
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "key": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbExtPropertyType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("string", "integer", "double", "boolean"),
        ),
        "value": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbExtObject(StBridgeElement):
    """対象オブジェクト：StbExtObject

    Attributes:
        object_name (str): 属性 ST-Bridgeの要素名
        id_object (int): 属性 要素のID
        stb_ext_property (list[StbExtProperty]): 子要素 StbExtProperty(拡張属性)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "object_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_object": _FI(
            py_type=int,
            data_type=_DT.NON_NEGATIVE_INTEGER,
            xml_type="nonNegativeInteger",
            required=True,
        ),
        "stb_ext_property": _FI(kind=_FK.ELEMENT, py_type=list[StbExtProperty]),
    }


class StbExtension(StBridgeElement):
    """拡張情報：StbExtension

    Attributes:
        identifier (str): 属性 拡張情報の識別子
        description (str): 属性 拡張情報の説明
        stb_ext_object (list[StbExtObject]): 子要素 StbExtObject(対象オブジェクト)
        stb_ext_element (list[StbExtElement]): 子要素 StbExtElement(拡張子要素)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "identifier": _FI(py_type=str, data_type=_DT.STR, required=True),
        "description": _FI(py_type=str, data_type=_DT.STR),
        "stb_ext_object": _FI(kind=_FK.ELEMENT, py_type=list[StbExtObject]),
        "stb_ext_element": _FI(kind=_FK.ELEMENT, py_type=list[StbExtElement]),
    }


class StbExtensions(StBridgeElement):
    """拡張情報（複数）：StbExtensions

    Attributes:
        stb_extension (list[StbExtension]): 子要素 StbExtension(拡張情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_extension": _FI(kind=_FK.ELEMENT, py_type=list[StbExtension]),
    }


class StbJointShapeCrossYWebShort(StBridgeElement):
    """StbJointShapeCrossYWebShort

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性
        pitch (float): 属性
        e1 (float): 属性
        e2 (float): 属性
        plate_thickness (float): 属性
        plate_width (float): 属性
        plate_length (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeCrossYWebLong(StBridgeElement):
    """StbJointShapeCrossYWebLong

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性
        pitch (float): 属性
        e1 (float): 属性
        e2 (float): 属性
        plate_thickness (float): 属性
        plate_width (float): 属性
        plate_length (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeCrossYFlange(StBridgeElement):
    """StbJointShapeCrossYFlange

    Attributes:
        is_zigzag (bool): 属性
        nf (int): 属性
        mf (int): 属性
        g1 (float): 属性
        g2 (float): 属性
        pitch (float): 属性
        e1 (float): 属性
        e2 (float): 属性
        outside_thickness (float): 属性
        outside_width (float): 属性
        outside_length (float): 属性
        inside_thickness (float): 属性
        inside_width (float): 属性
        inside_length (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
        "nf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "g1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "g2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "outside_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_thickness": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_width": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeCrossXWebShort(StBridgeElement):
    """StbJointShapeCrossXWebShort

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性
        pitch (float): 属性
        e1 (float): 属性
        e2 (float): 属性
        plate_thickness (float): 属性
        plate_width (float): 属性
        plate_length (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeCrossXWebLong(StBridgeElement):
    """StbJointShapeCrossXWebLong

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性
        pitch (float): 属性
        e1 (float): 属性
        e2 (float): 属性
        plate_thickness (float): 属性
        plate_width (float): 属性
        plate_length (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeCrossXFlange(StBridgeElement):
    """StbJointShapeCrossXFlange

    Attributes:
        is_zigzag (bool): 属性
        nf (int): 属性
        mf (int): 属性
        g1 (float): 属性
        g2 (float): 属性
        pitch (float): 属性
        e1 (float): 属性
        e2 (float): 属性
        outside_thickness (float): 属性
        outside_width (float): 属性
        outside_length (float): 属性
        inside_thickness (float): 属性
        inside_width (float): 属性
        inside_length (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
        "nf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "g1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "g2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "outside_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_thickness": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_width": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeCross(StBridgeElement):
    """＋形継手詳細：StbJointShapeCross

    Attributes:
        strength_plate (str): 属性
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼名）
        offset_hy (float): 属性
        offset_hx (float): 属性
        clearance (float): 属性 部材の母材間隔
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_hy": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_HY",
        ),
        "offset_hx": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_HX",
        ),
        "clearance": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
    }


class StbJointColumnShapeCross(StBridgeElement):
    """Ｓ柱継手・＋形：StbJointColumnShapeCross

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        joint_name (str): 属性 継手呼称
        joint_mark (str): 属性 継手符号
        stb_joint_shape_cross (StbJointShapeCross): 子要素 StbJointShapeCross(＋形継手詳細)
        stb_joint_shape_cross_x_flange (StbJointShapeCrossXFlange): 子要素
        stb_joint_shape_cross_x_web_long (StbJointShapeCrossXWebLong): 子要素
        stb_joint_shape_cross_x_web_short (StbJointShapeCrossXWebShort): 子要素
        stb_joint_shape_cross_y_flange (StbJointShapeCrossYFlange): 子要素
        stb_joint_shape_cross_y_web_long (StbJointShapeCrossYWebLong): 子要素
        stb_joint_shape_cross_y_web_short (StbJointShapeCrossYWebShort): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "joint_name": _FI(py_type=str, data_type=_DT.STR),
        "joint_mark": _FI(py_type=str, data_type=_DT.STR),
        "stb_joint_shape_cross": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbJointShapeCross
        ),
        "stb_joint_shape_cross_x_flange": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeCrossXFlange
        ),
        "stb_joint_shape_cross_x_web_long": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossXWebLong,
        ),
        "stb_joint_shape_cross_x_web_short": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossXWebShort,
        ),
        "stb_joint_shape_cross_y_flange": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeCrossYFlange
        ),
        "stb_joint_shape_cross_y_web_long": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossYWebLong,
        ),
        "stb_joint_shape_cross_y_web_short": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossYWebShort,
        ),
    }


class StbJointShapeTWebT(StBridgeElement):
    """Ｔ形継手詳細・Ｔ部分ウェブ：StbJointShapeTWebT

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeTFlangeT(StBridgeElement):
    """Ｔ形継手詳細・Ｔ部分フランジ：StbJointShapeTFlangeT

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        nf (int): 属性
        mf (int): 属性
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ(P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
        "nf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "g1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "g2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "outside_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_thickness": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_width": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeTWebHShort(StBridgeElement):
    """Ｔ形継手詳細・Ｈ部分ウェブ(短)：StbJointShapeTWebHShort

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeTWebHLong(StBridgeElement):
    """Ｔ形継手詳細・Ｈ部分ウェブ(長)：StbJointShapeTWebHLong

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeTFlangeH(StBridgeElement):
    """Ｔ形継手詳細・Ｈ部分フランジ：StbJointShapeTFlangeH

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        nf (int): 属性
        mf (int): 属性
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ(P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
        "nf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "g1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "g2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "outside_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_thickness": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_width": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeT(StBridgeElement):
    """Ｔ形継手詳細：StbJointShapeT

    Attributes:
        strength_plate (str): 属性
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼名）
        offset_t (float): 属性 Ｔ形鋼の偏心（Ｈ形鋼の成の中心からの距離）
        clearance (float): 属性 部材の母材間隔
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_t": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_T",
        ),
        "clearance": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
    }


class StbJointColumnShapeT(StBridgeElement):
    """Ｓ柱継手・Ｔ形：StbJointColumnShapeT

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        joint_name (str): 属性 継手呼称
        joint_mark (str): 属性 継手符号
        stb_joint_shape_t (StbJointShapeT): 子要素 StbJointShapeT(Ｔ形継手詳細)
        stb_joint_shape_t_flange_h (StbJointShapeTFlangeH): 子要素 StbJointShapeTFlangeH(Ｔ形継手詳細・Ｈ部分フランジ)
        stb_joint_shape_t_web_h_long (StbJointShapeTWebHLong): 子要素 StbJointShapeTWebHLong(Ｔ形継手詳細・Ｈ部分ウェブ(長))
        stb_joint_shape_t_web_h_short (StbJointShapeTWebHShort): 子要素 StbJointShapeTWebHShort(Ｔ形継手詳細・Ｈ部分ウェブ(短))
        stb_joint_shape_t_flange_t (StbJointShapeTFlangeT): 子要素 StbJointShapeTFlangeT(Ｔ形継手詳細・Ｔ部分フランジ)
        stb_joint_shape_t_web_t (StbJointShapeTWebT): 子要素 StbJointShapeTWebT(Ｔ形継手詳細・Ｔ部分ウェブ)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "joint_name": _FI(py_type=str, data_type=_DT.STR),
        "joint_mark": _FI(py_type=str, data_type=_DT.STR),
        "stb_joint_shape_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbJointShapeT
        ),
        "stb_joint_shape_t_flange_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeTFlangeH
        ),
        "stb_joint_shape_t_web_h_long": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbJointShapeTWebHLong
        ),
        "stb_joint_shape_t_web_h_short": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeTWebHShort,
        ),
        "stb_joint_shape_t_flange_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeTFlangeT
        ),
        "stb_joint_shape_t_web_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbJointShapeTWebT
        ),
    }


class StbJointColumnShapeH(StBridgeElement):
    """Ｓ柱継手・Ｈ形：StbJointColumnShapeH

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        joint_name (str): 属性 継手呼称
        joint_mark (str): 属性 継手符号
        stb_joint_shape_h (StbJointShapeH): 子要素 StbJointShapeH(Ｈ形継手詳細)
        stb_joint_shape_h_flange (StbJointShapeHFlange): 子要素 StbJointShapeHFlange(Ｈ形継手詳細・フランジ)
        stb_joint_shape_h_web (StbJointShapeHWeb): 子要素 StbJointShapeHWeb(Ｈ形継手詳細・ウェブ)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "joint_name": _FI(py_type=str, data_type=_DT.STR),
        "joint_mark": _FI(py_type=str, data_type=_DT.STR),
        "stb_joint_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbJointShapeH"
        ),
        "stb_joint_shape_h_flange": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbJointShapeHFlange"
        ),
        "stb_joint_shape_h_web": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbJointShapeHWeb"
        ),
    }


class StbJointShapeHWeb(StBridgeElement):
    """Ｈ形継手詳細・ウェブ：StbJointShapeHWeb

    Attributes:
        mw (int): 属性
        nw (int): 属性
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "nw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeHFlange(StBridgeElement):
    """Ｈ形継手詳細・フランジ：StbJointShapeHFlange

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        nf (int): 属性
        mf (int): 属性
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ (P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
        "nf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mf": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "g1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "g2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "outside_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "outside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_thickness": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_width": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "inside_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbJointShapeH(StBridgeElement):
    """Ｈ形継手詳細：StbJointShapeH

    Attributes:
        strength_plate (str): 属性
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼び名）
        clearance (float): 属性 部材の母材間隔
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "clearance": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
    }


class StbJointBeamShapeH(StBridgeElement):
    """Ｓ梁継手・Ｈ形：StbJointBeamShapeH

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        joint_name (str): 属性 継手呼称
        joint_mark (str): 属性 継手符号
        stb_joint_shape_h (StbJointShapeH): 子要素 StbJointShapeH(Ｈ形継手詳細)
        stb_joint_shape_h_flange (StbJointShapeHFlange): 子要素 StbJointShapeHFlange(Ｈ形継手詳細・フランジ)
        stb_joint_shape_h_web (StbJointShapeHWeb): 子要素 StbJointShapeHWeb(Ｈ形継手詳細・ウェブ)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "joint_name": _FI(py_type=str, data_type=_DT.STR),
        "joint_mark": _FI(py_type=str, data_type=_DT.STR),
        "stb_joint_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbJointShapeH
        ),
        "stb_joint_shape_h_flange": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeHFlange
        ),
        "stb_joint_shape_h_web": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbJointShapeHWeb
        ),
    }


class StbJoints(StBridgeElement):
    """継手情報：StbJoints

    Attributes:
        stb_joint_beam_shape_h (list[StbJointBeamShapeH]): 子要素 StbJointBeamShapeH(Ｓ梁継手・Ｈ形)
        stb_joint_column_shape_h (list[StbJointColumnShapeH]): 子要素 StbJointColumnShapeH(Ｓ柱継手・Ｈ形)
        stb_joint_column_shape_t (list[StbJointColumnShapeT]): 子要素 StbJointColumnShapeT(Ｓ柱継手・Ｔ形)
        stb_joint_column_shape_cross (list[StbJointColumnShapeCross]): 子要素 StbJointColumnShapeCross(Ｓ柱継手・＋形)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_joint_beam_shape_h": _FI(
            kind=_FK.ELEMENT, py_type=list[StbJointBeamShapeH]
        ),
        "stb_joint_column_shape_h": _FI(
            kind=_FK.ELEMENT, py_type=list[StbJointColumnShapeH]
        ),
        "stb_joint_column_shape_t": _FI(
            kind=_FK.ELEMENT, py_type=list[StbJointColumnShapeT]
        ),
        "stb_joint_column_shape_cross": _FI(
            kind=_FK.ELEMENT, py_type=list[StbJointColumnShapeCross]
        ),
    }


class StbSecUndefined(StBridgeElement):
    """構造種別に依存しない断面：StbSecUndefined

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbSecSteelUndefined(StBridgeElement):
    """未定義鉄骨断面：StbSecSteelUndefined

    Attributes:
        name (str): 属性 形状名
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbSecSteelProduct(StBridgeElement):
    """鉄骨製品：StbSecSteelProduct

    Attributes:
        name (str): 属性 形状名
        product_company (str): 属性 メーカー名
        product_name (str): 属性 製品名または種類
        product_code (str): 属性 製品型番
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_name": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbSecRoundBar(StBridgeElement):
    """丸鋼：StbSecRoundBar

    Attributes:
        name (str): 属性 形状名
        r (float): 属性 直径
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "r": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="R",
        ),
    }


class StbSecFlatBar(StBridgeElement):
    """フラットバー：StbSecFlatBar

    Attributes:
        name (str): 属性 形状名
        b (float): 属性 幅
        t (float): 属性 板厚
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
    }


class StbSecLipC(StBridgeElement):
    """リップ溝形鋼：StbSecLipC

    Attributes:
        name (str): 属性 形状名
        type (StbSecLipCType): 属性
        h (float): 属性 成
        a (float): 属性 幅
        c (float): 属性 リップ長
        t (float): 属性 板厚
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecLipCType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("SINGLE", "BACKTOBACK", "FACETOFACE"),
        ),
        "h": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="H",
        ),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "c": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="C",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
    }


class StbSecRollL(StBridgeElement):
    """山形鋼：StbSecRoll-L

    Attributes:
        name (str): 属性 形状名
        type (StbSecRollLType): 属性
        a (float): 属性 成
        b (float): 属性 幅
        t1 (float): 属性 成方向の板厚
        t2 (float): 属性 幅方向の板厚
        r1 (float): 属性 フィレット半径
        r2 (float): 属性 先端半径
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecRollLType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("SINGLE", "BACKTOBACK", "FACETOFACE"),
        ),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-L"


class StbSecRollC(StBridgeElement):
    """溝形鋼：StbSecRoll-C

    Attributes:
        name (str): 属性 形状名
        type (StbSecRollCType): 属性
        a (float): 属性 成
        b (float): 属性 フランジ幅
        t1 (float): 属性 ウェブ厚
        t2 (float): 属性 フランジ厚
        r1 (float): 属性 フィレット半径
        r2 (float): 属性 フランジ先端半径
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecRollCType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("SINGLE", "BACKTOBACK", "FACETOFACE"),
        ),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-C"


class StbSecRollT(StBridgeElement):
    """T形鋼：StbSecRoll-T

    Attributes:
        name (str): 属性 形状名
        type (StbSecRollTType): 属性 形状タイプ以下のいずれかT（一般T形鋼）ST（外法一定T形鋼）
        a (float): 属性 成
        b (float): 属性 フランジ幅
        t1 (float): 属性 ウェブ厚
        t2 (float): 属性 フランジ厚
        r (float): 属性 フィレット半径
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecRollTType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("T", "ST"),
        ),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-T"


class StbSecPipe(StBridgeElement):
    """円形鋼管：StbSecPipe

    Attributes:
        name (str): 属性 形状名
        d (float): 属性 直径
        t (float): 属性 板厚
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
    }


class StbSecBuildBox(StBridgeElement):
    """組立角形鋼管：StbSecBuild-BOX

    Attributes:
        name (str): 属性 形状名
        a (float): 属性 成
        b (float): 属性 幅
        t1 (float): 属性 成方向の板厚
        t2 (float): 属性 幅方向の板厚
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBuild-BOX"


class StbSecRollBox(StBridgeElement):
    """角形鋼管：StbSecRoll-BOX

    Attributes:
        name (str): 属性 形状名
        type (StbSecRollBoxType): 属性 形状タイプ以下のいずれかBCP、BCR、STKR、ELSE
        a (float): 属性 成
        b (float): 属性 幅
        t (float): 属性 板厚
        r (float): 属性 コーナー半径(R)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecRollBoxType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BCP", "BCR", "STKR", "ELSE"),
        ),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-BOX"


class StbSecBuildH(StBridgeElement):
    """組立H形鋼：StbSecBuild-H

    Attributes:
        name (str): 属性 形状名
        a (float): 属性 成
        b (float): 属性 フランジ幅
        t1 (float): 属性 ウェブ厚
        t2 (float): 属性 フランジ厚
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBuild-H"


class StbSecRollH(StBridgeElement):
    """H形鋼：StbSecRoll-H

    Attributes:
        name (str): 属性 形状名
        type (StbSecRollHType): 属性 形状タイプ以下のいずれかH（一般H形鋼）SH（外法一定H形鋼）
        a (float): 属性 成
        b (float): 属性 フランジ幅
        t1 (float): 属性 ウェブ厚
        t2 (float): 属性 フランジ厚
        r (float): 属性 フィレット半径
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecRollHType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("H", "SH"),
        ),
        "a": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A",
        ),
        "b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-H"


class StbSecSteel(StBridgeElement):
    """鉄骨断面：StbSecSteel

    Attributes:
        stb_sec_roll_h (list[StbSecRollH]): 子要素 StbSecRoll-H(H形鋼)
        stb_sec_build_h (list[StbSecBuildH]): 子要素 StbSecBuild-H(組立H形鋼)
        stb_sec_roll_box (list[StbSecRollBox]): 子要素 StbSecRoll-BOX(角形鋼管)
        stb_sec_build_box (list[StbSecBuildBox]): 子要素 StbSecBuild-BOX(組立角形鋼管)
        stb_sec_pipe (list[StbSecPipe]): 子要素 StbSecPipe(円形鋼管)
        stb_sec_roll_t (list[StbSecRollT]): 子要素 StbSecRoll-T(T形鋼)
        stb_sec_roll_c (list[StbSecRollC]): 子要素 StbSecRoll-C(溝形鋼)
        stb_sec_roll_l (list[StbSecRollL]): 子要素 StbSecRoll-L(山形鋼)
        stb_sec_lip_c (list[StbSecLipC]): 子要素 StbSecLipC(リップ溝形鋼)
        stb_sec_flat_bar (list[StbSecFlatBar]): 子要素 StbSecFlatBar(フラットバー)
        stb_sec_round_bar (list[StbSecRoundBar]): 子要素 StbSecRoundBar(丸鋼)
        stb_sec_steel_product (list[StbSecSteelProduct]): 子要素 StbSecSteelProduct(鉄骨製品)
        stb_sec_steel_undefined (list[StbSecSteelUndefined]): 子要素 StbSecSteelUndefined(未定義鉄骨断面)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_roll_h": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollH]),
        "stb_sec_build_h": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBuildH]),
        "stb_sec_roll_box": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollBox]),
        "stb_sec_build_box": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBuildBox]),
        "stb_sec_pipe": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPipe]),
        "stb_sec_roll_t": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollT]),
        "stb_sec_roll_c": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollC]),
        "stb_sec_roll_l": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollL]),
        "stb_sec_lip_c": _FI(kind=_FK.ELEMENT, py_type=list[StbSecLipC]),
        "stb_sec_flat_bar": _FI(kind=_FK.ELEMENT, py_type=list[StbSecFlatBar]),
        "stb_sec_round_bar": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRoundBar]),
        "stb_sec_steel_product": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecSteelProduct]
        ),
        "stb_sec_steel_undefined": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecSteelUndefined]
        ),
    }


class StbSecBarParapetRcEdge(StBridgeElement):
    """端部補強筋：StbSecBarParapet_RC_Edge

    Attributes:
        pos (StbSecBarParapetRcEdgePos): 属性 配筋位置 以下のいずれかVERTICAL_START（パラペット始端）VERTICAL_END（パラペット終端）HORIZONTAL_TOP（パラペット上端）HORIZONTAL_BOTTOM（パラペット下端）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarParapetRcEdgePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "VERTICAL_START",
                "VERTICAL_END",
                "HORIZONTAL_TOP",
                "HORIZONTAL_BOTTOM",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarParapet_RC_Edge"


class StbSecBarParapetRcTip(StBridgeElement):
    """パラペット先端補強筋（アゴ筋）：StbSecBarParapet_RC_Tip

    Attributes:
        pos (StbSecBarParapetRcTipPos): 属性 配筋位置 以下のいずれかSHORT_SIDE（短辺方向）LONG_SIDE（長辺方向）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
        n (int): 属性 本数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarParapetRcTipPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("SHORT_SIDE", "LONG_SIDE"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarParapet_RC_Tip"


class StbSecBarParapetRcDoubleNet(StBridgeElement):
    """ＲＣパラペット断面配筋・ダブル：StbSecBarParapet_RC_DoubleNet

    Attributes:
        pos (StbSecBarParapetRcDoubleNetPos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarParapetRcDoubleNetPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarParapet_RC_DoubleNet"


class StbSecBarParapetRcZigzag(StBridgeElement):
    """ＲＣパラペット断面配筋・千鳥：StbSecBarParapet_RC_Zigzag

    Attributes:
        pos (StbSecBarParapetRcZigzagPos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarParapetRcZigzagPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarParapet_RC_Zigzag"


class StbSecBarParapetRcSingle(StBridgeElement):
    """ＲＣパラペット断面配筋・シングル：StbSecBarParapet_RC_Single

    Attributes:
        pos (StbSecBarParapetRcSinglePos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarParapetRcSinglePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarParapet_RC_Single"


class StbSecBarArrangementParapetRc(StBridgeElement):
    """ＲＣパラペット断面配筋：StbSecBarArrangementParapet_RC

    Attributes:
        depth_cover_outside (float): 属性
        depth_cover_inside (float): 属性
        is_tipline (bool): 属性
        stb_sec_bar_parapet_rc_single (list[StbSecBarParapetRcSingle]): 子要素 StbSecBarParapet_RC_Single(ＲＣパラペット断面配筋・シングル)
        stb_sec_bar_parapet_rc_zigzag (list[StbSecBarParapetRcZigzag]): 子要素 StbSecBarParapet_RC_Zigzag(ＲＣパラペット断面配筋・千鳥)
        stb_sec_bar_parapet_rc_double_net (list[StbSecBarParapetRcDoubleNet]): 子要素 StbSecBarParapet_RC_DoubleNet(ＲＣパラペット断面配筋・ダブル)
        stb_sec_bar_parapet_rc_tip (list[StbSecBarParapetRcTip]): 子要素 StbSecBarParapet_RC_Tip(パラペット先端補強筋（アゴ筋）)
        stb_sec_bar_parapet_rc_edge (list[StbSecBarParapetRcEdge]): 子要素 StbSecBarParapet_RC_Edge(端部補強筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_outside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "depth_cover_inside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "is_tipline": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isTipline"),
        "stb_sec_bar_parapet_rc_single": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarParapetRcSingle]
        ),
        "stb_sec_bar_parapet_rc_zigzag": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarParapetRcZigzag]
        ),
        "stb_sec_bar_parapet_rc_double_net": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarParapetRcDoubleNet]
        ),
        "stb_sec_bar_parapet_rc_tip": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarParapetRcTip]
        ),
        "stb_sec_bar_parapet_rc_edge": _FI(
            kind=_FK.ELEMENT, max_occurs=4, py_type=list[StbSecBarParapetRcEdge]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementParapet_RC"


class StbSecParapetRcTypeI(StBridgeElement):
    """ＲＣパラペット断面形状・I型：StbSecParapet_RC_TypeI

    Attributes:
        t_t (float): 属性 厚さT
        depth_h (float): 属性 高さH
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "t_t": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="t_T",
        ),
        "depth_h": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecParapet_RC_TypeI"


class StbSecParapetRcTypeT(StBridgeElement):
    """ＲＣパラペット断面形状・T型：StbSecParapet_RC_TypeT

    Attributes:
        t_t (float): 属性 厚さT
        depth_h (float): 属性 高さH
        t_t1 (float): 属性 寸法T1
        depth_h1 (float): 属性 寸法H1
        depth_h2 (float): 属性 寸法H2
        depth_h3 (float): 属性 寸法H3
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "t_t": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="t_T",
        ),
        "depth_h": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H",
        ),
        "t_t1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="t_T1",
        ),
        "depth_h1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H1",
        ),
        "depth_h2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H2",
        ),
        "depth_h3": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H3",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecParapet_RC_TypeT"


class StbSecParapetRcTypeL(StBridgeElement):
    """ＲＣパラペット断面形状・L型：StbSecParapet_RC_TypeL

    Attributes:
        t_t (float): 属性 厚さT
        depth_h (float): 属性 高さH
        t_t1 (float): 属性 寸法T1
        depth_h1 (float): 属性 寸法H1
        depth_h2 (float): 属性 寸法H2
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "t_t": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="t_T",
        ),
        "depth_h": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H",
        ),
        "t_t1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="t_T1",
        ),
        "depth_h1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H1",
        ),
        "depth_h2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="depth_H2",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecParapet_RC_TypeL"


class StbSecFigureParapetRc(StBridgeElement):
    """ＲＣパラペット断面形状：StbSecFigureParapet_RC

    Attributes:
        stb_sec_parapet_rc_type_l (StbSecParapetRcTypeL): 子要素 StbSecParapet_RC_TypeL(ＲＣパラペット断面形状・L型)
        stb_sec_parapet_rc_type_t (StbSecParapetRcTypeT): 子要素 StbSecParapet_RC_TypeT(ＲＣパラペット断面形状・T型)
        stb_sec_parapet_rc_type_i (StbSecParapetRcTypeI): 子要素 StbSecParapet_RC_TypeI(ＲＣパラペット断面形状・I型)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_parapet_rc_type_l": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecParapetRcTypeL
        ),
        "stb_sec_parapet_rc_type_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecParapetRcTypeT
        ),
        "stb_sec_parapet_rc_type_i": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecParapetRcTypeI
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureParapet_RC"


class StbSecParapetRc(StBridgeElement):
    """ＲＣパラペット断面：StbSecParapet_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_parapet_rc (StbSecFigureParapetRc): 子要素 StbSecFigureParapet_RC(ＲＣパラペット断面形状)
        stb_sec_bar_arrangement_parapet_rc (StbSecBarArrangementParapetRc): 子要素 StbSecBarArrangementParapet_RC(ＲＣパラペット断面配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_parapet_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigureParapetRc
        ),
        "stb_sec_bar_arrangement_parapet_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementParapetRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecParapet_RC"


class StbSecBarOpenRcWall(StBridgeElement):
    """ＲＣ壁開口配筋：StbSecBarOpen_RC_Wall

    Attributes:
        pos (StbSecBarOpenRcWallPos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）DIAGONAL（斜め筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        length (float): 属性 長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarOpenRcWallPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL", "DIAGONAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
        "length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarOpen_RC_Wall"


class StbSecBarOpenRcSlab(StBridgeElement):
    """ＲＣスラブ開口配筋：StbSecBarOpen_RC_Slab

    Attributes:
        pos (StbSecBarOpenRcSlabPos): 属性 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）DIAGONAL_TOP（斜め方向上端）DIAGONAL_BOTTOM（斜め方向下端）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        length (float): 属性 長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarOpenRcSlabPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "X_TOP",
                "X_BOTTOM",
                "Y_TOP",
                "Y_BOTTOM",
                "DIAGONAL_TOP",
                "DIAGONAL_BOTTOM",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
        "length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarOpen_RC_Slab"


class StbSecBarArrangementOpenRc(StBridgeElement):
    """ＲＣ開口断面配筋：StbSecBarArrangementOpen_RC

    Attributes:
        stb_sec_bar_open_rc_slab (list[StbSecBarOpenRcSlab]): 子要素 StbSecBarOpen_RC_Slab(ＲＣスラブ開口配筋)
        stb_sec_bar_open_rc_wall (list[StbSecBarOpenRcWall]): 子要素 StbSecBarOpen_RC_Wall(ＲＣ壁開口配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_bar_open_rc_slab": _FI(
            kind=_FK.ELEMENT, max_occurs=6, py_type=list[StbSecBarOpenRcSlab]
        ),
        "stb_sec_bar_open_rc_wall": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBarOpenRcWall]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementOpen_RC"


class StbSecOpenRc(StBridgeElement):
    """ＲＣ開口断面：StbSecOpen_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        stb_sec_bar_arrangement_open_rc (StbSecBarArrangementOpenRc): 子要素 StbSecBarArrangementOpen_RC(ＲＣ開口断面配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_arrangement_open_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementOpenRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecOpen_RC"


class StbSecPileProductNodularCprc(StBridgeElement):
    """StbSecPileProductNodularCprc：StbSecPileProductNodular_CPRC

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d1 (float): 属性
        d2 (float): 属性
        tc (float): 属性
        strength_concrete (str): 属性
        d_pc (float): 属性
        n_pc (int): 属性
        strength_pc (str): 属性
        d_bar (str): 属性
        n_bar (int): 属性
        strength_bar (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR),
        "d1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1",
        ),
        "d2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2",
        ),
        "tc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "d_pc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_PC"
        ),
        "n_pc": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_PC",
        ),
        "strength_pc": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_PC"),
        "d_bar": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar"),
        "n_bar": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar",
        ),
        "strength_bar": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProductNodular_CPRC"


class StbSecPileProductNodularPrc(StBridgeElement):
    """StbSecPileProductNodularPrc：StbSecPileProductNodular_PRC

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d1 (float): 属性
        d2 (float): 属性
        tc (float): 属性
        strength_concrete (str): 属性
        d_pc (float): 属性
        n_pc (int): 属性
        strength_pc (str): 属性
        d_bar (str): 属性
        n_bar (int): 属性
        strength_bar (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR),
        "d1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1",
        ),
        "d2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2",
        ),
        "tc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "d_pc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_PC"
        ),
        "n_pc": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_PC",
        ),
        "strength_pc": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_PC"),
        "d_bar": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar"),
        "n_bar": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar",
        ),
        "strength_bar": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProductNodular_PRC"


class StbSecPileProductNodularPhc(StBridgeElement):
    """StbSecPileProductNodularPhc：StbSecPileProductNodular_PHC

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d1 (float): 属性
        d2 (float): 属性
        t (float): 属性
        strength_concrete (str): 属性
        d_pc (float): 属性
        n_pc (int): 属性
        strength_pc (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR),
        "d1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1",
        ),
        "d2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "d_pc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_PC"
        ),
        "n_pc": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_PC",
        ),
        "strength_pc": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_PC"),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProductNodular_PHC"


class StbSecPileProductCprc(StBridgeElement):
    """StbSecPileProductCprc：StbSecPileProduct_CPRC

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d (float): 属性
        tc (float): 属性
        strength_concrete (str): 属性
        d_pc (float): 属性
        n_pc (int): 属性
        strength_pc (str): 属性
        d_bar (str): 属性
        n_bar (int): 属性
        strength_bar (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
        "tc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "d_pc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_PC"
        ),
        "n_pc": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_PC",
        ),
        "strength_pc": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_PC"),
        "d_bar": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar"),
        "n_bar": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar",
        ),
        "strength_bar": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProduct_CPRC"


class StbSecPileProductPrc(StBridgeElement):
    """StbSecPileProductPrc：StbSecPileProduct_PRC

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d (float): 属性
        tc (float): 属性
        strength_concrete (str): 属性
        d_pc (float): 属性
        n_pc (int): 属性
        strength_pc (str): 属性
        d_bar (str): 属性
        n_bar (int): 属性
        strength_bar (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
        "tc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "d_pc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_PC"
        ),
        "n_pc": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_PC",
        ),
        "strength_pc": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_PC"),
        "d_bar": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar"),
        "n_bar": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar",
        ),
        "strength_bar": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProduct_PRC"


class StbSecPileProductSc(StBridgeElement):
    """StbSecPileProductSc：StbSecPileProduct_SC

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d (float): 属性
        tc (float): 属性
        ts (float): 属性
        strength_concrete (str): 属性
        strength_pipe (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
        "tc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "ts": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "strength_pipe": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProduct_SC"


class StbSecPileProductSt(StBridgeElement):
    """StbSecPileProductSt：StbSecPileProduct_ST

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d1 (float): 属性
        d2 (float): 属性
        t1 (float): 属性
        t2 (float): 属性
        strength_concrete (str): 属性
        d_pc (float): 属性
        n_pc (int): 属性
        strength_pc (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "d1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1",
        ),
        "d2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "d_pc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_PC"
        ),
        "n_pc": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_PC",
        ),
        "strength_pc": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_PC"),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProduct_ST"


class StbSecPileProductPhc(StBridgeElement):
    """StbSecPileProductPhc：StbSecPileProduct_PHC

    Attributes:
        id_order (int): 属性
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性
        kind (str): 属性
        d (float): 属性
        t (float): 属性
        strength_concrete (str): 属性
        d_pc (float): 属性
        n_pc (int): 属性
        strength_pc (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "d_pc": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_PC"
        ),
        "n_pc": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_PC",
        ),
        "strength_pc": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_PC"),
    }
    _xml_element_name: ClassVar[str] = "StbSecPileProduct_PHC"


class StbSecFigurePileProduct(StBridgeElement):
    """StbSecFigurePileProduct

    Attributes:
        stb_sec_pile_product_phc (list[StbSecPileProductPhc]): 子要素
        stb_sec_pile_product_st (list[StbSecPileProductSt]): 子要素
        stb_sec_pile_product_sc (list[StbSecPileProductSc]): 子要素
        stb_sec_pile_product_prc (list[StbSecPileProductPrc]): 子要素
        stb_sec_pile_product_cprc (list[StbSecPileProductCprc]): 子要素
        stb_sec_pile_product_nodular_phc (list[StbSecPileProductNodularPhc]): 子要素
        stb_sec_pile_product_nodular_prc (list[StbSecPileProductNodularPrc]): 子要素
        stb_sec_pile_product_nodular_cprc (list[StbSecPileProductNodularCprc]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_pile_product_phc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductPhc]
        ),
        "stb_sec_pile_product_st": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductSt]
        ),
        "stb_sec_pile_product_sc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductSc]
        ),
        "stb_sec_pile_product_prc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductPrc]
        ),
        "stb_sec_pile_product_cprc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductCprc]
        ),
        "stb_sec_pile_product_nodular_phc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductNodularPhc]
        ),
        "stb_sec_pile_product_nodular_prc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductNodularPrc]
        ),
        "stb_sec_pile_product_nodular_cprc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileProductNodularCprc]
        ),
    }


class StbSecPileProduct(StBridgeElement):
    """StbSecPileProduct

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        stb_sec_figure_pile_product (StbSecFigurePileProduct): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_figure_pile_product": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecFigurePileProduct,
        ),
    }


class StbSecPileSTaper(StBridgeElement):
    """鋼管杭断面形状・テーパー管杭：StbSecPile_S_Taper

    Attributes:
        id_order (int): 属性 継杭の位置
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性 杭の長さ
        d1 (float): 属性 上部径
        d2 (float): 属性 下部径
        t (float): 属性 鋼管の厚さ
        strength (str): 属性 鋼管の鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1",
        ),
        "d2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Taper"


class StbSecPileSRotational(StBridgeElement):
    """鋼管杭断面形状・回転貫入杭（先端拡翼杭）：StbSecPile_S_Rotational

    Attributes:
        id_order (int): 属性 継杭の位置
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性 杭の長さ
        d1 (float): 属性 軸部径
        d2 (float): 属性 先端拡翼径
        t (float): 属性 鋼管の厚さ
        strength (str): 属性 鋼管の鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1",
        ),
        "d2": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Rotational"


class StbSecPileSStraight(StBridgeElement):
    """鋼管杭断面形状・ストレート：StbSecPile_S_Straight

    Attributes:
        id_order (int): 属性 継杭の位置
        product_company (str): 属性
        product_code (str): 属性
        length_pile (float): 属性 杭の長さ
        d (float): 属性 軸部径
        t (float): 属性 鋼管の厚さ
        strength (str): 属性 鋼管の鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Straight"


class StbSecFigurePileS(StBridgeElement):
    """鋼管杭断面形状：StbSecFigurePile_S

    Attributes:
        stb_sec_pile_s_straight (list[StbSecPileSStraight]): 子要素 StbSecPile_S_Straight(鋼管杭断面形状・ストレート)
        stb_sec_pile_s_rotational (list[StbSecPileSRotational]): 子要素 StbSecPile_S_Rotational(鋼管杭断面形状・回転貫入杭（先端拡翼杭）)
        stb_sec_pile_s_taper (list[StbSecPileSTaper]): 子要素 StbSecPile_S_Taper(鋼管杭断面形状・テーパー管杭)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_pile_s_straight": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileSStraight]
        ),
        "stb_sec_pile_s_rotational": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileSRotational]
        ),
        "stb_sec_pile_s_taper": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileSTaper]),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigurePile_S"


class StbSecPileS(StBridgeElement):
    """鋼管杭断面：StbSecPile_S

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        stb_sec_figure_pile_s (StbSecFigurePileS): 子要素 StbSecFigurePile_S(鋼管杭断面形状)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_figure_pile_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigurePileS
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S"


class StbSecBarPileRcTopCenterBottom(StBridgeElement):
    """ＲＣ杭断面配筋・杭頭軸部杭脚：StbSecBarPile_RC_TopCenterBottom

    Attributes:
        pos (StbSecBarPileRcTopCenterBottomPos): 属性
        d_main_circumference_1st (str): 属性
        d_main_circumference_2nd (str): 属性
        d_main_core (str): 属性
        d_band (str): 属性
        strength_main_circumference_1st (str): 属性
        strength_main_circumference_2nd (str): 属性
        strength_main_core (str): 属性
        strength_band (str): 属性
        n_main_circumference_1st (int): 属性
        n_main_circumference_2nd (int): 属性
        n_main_core (int): 属性
        pitch_band (float): 属性
        length_bar (float): 属性
        length_lap_bar (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarPileRcTopCenterBottomPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("TOP", "CENTER", "BOTTOM"),
        ),
        "d_main_circumference_1st": _FI(
            py_type=str,
            data_type=_DT.STR,
            required=True,
            xml_name="D_main_circumference_1st",
        ),
        "d_main_circumference_2nd": _FI(
            py_type=str, data_type=_DT.STR, xml_name="D_main_circumference_2nd"
        ),
        "d_main_core": _FI(py_type=str, data_type=_DT.STR, xml_name="D_main_core"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "strength_main_circumference_1st": _FI(py_type=str, data_type=_DT.STR),
        "strength_main_circumference_2nd": _FI(py_type=str, data_type=_DT.STR),
        "strength_main_core": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "n_main_circumference_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_circumference_1st",
        ),
        "n_main_circumference_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_circumference_2nd",
        ),
        "n_main_core": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_core",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "length_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_lap_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarPile_RC_TopCenterBottom"


class StbSecBarPileRcTopBottom(StBridgeElement):
    """ＲＣ杭断面配筋・杭頭脚別：StbSecBarPile_RC_TopBottom

    Attributes:
        pos (StbSecBarPileRcTopBottomPos): 属性 配筋位置以下のいずれかTOP（杭頭）BOTTOM（杭脚）
        d_main_circumference_1st (str): 属性
        d_main_circumference_2nd (str): 属性
        d_main_core (str): 属性
        d_band (str): 属性 帯筋：径
        strength_main_circumference_1st (str): 属性
        strength_main_circumference_2nd (str): 属性
        strength_main_core (str): 属性
        strength_band (str): 属性 帯筋：鉄筋強度
        n_main_circumference_1st (int): 属性
        n_main_circumference_2nd (int): 属性
        n_main_core (int): 属性
        pitch_band (float): 属性 帯筋：ピッチ
        length_bar (float): 属性 配筋長さ
        length_lap_bar (float): 属性 重ね継手長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarPileRcTopBottomPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("TOP", "BOTTOM"),
        ),
        "d_main_circumference_1st": _FI(
            py_type=str,
            data_type=_DT.STR,
            required=True,
            xml_name="D_main_circumference_1st",
        ),
        "d_main_circumference_2nd": _FI(
            py_type=str, data_type=_DT.STR, xml_name="D_main_circumference_2nd"
        ),
        "d_main_core": _FI(py_type=str, data_type=_DT.STR, xml_name="D_main_core"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "strength_main_circumference_1st": _FI(py_type=str, data_type=_DT.STR),
        "strength_main_circumference_2nd": _FI(py_type=str, data_type=_DT.STR),
        "strength_main_core": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "n_main_circumference_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_circumference_1st",
        ),
        "n_main_circumference_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_circumference_2nd",
        ),
        "n_main_core": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_core",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "length_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_lap_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarPile_RC_TopBottom"


class StbSecBarPileRcSame(StBridgeElement):
    """ＲＣ杭断面配筋・全断面：StbSecBarPile_RC_Same

    Attributes:
        d_main_circumference_1st (str): 属性
        d_main_circumference_2nd (str): 属性
        d_main_core (str): 属性
        d_band (str): 属性
        strength_main_circumference_1st (str): 属性
        strength_main_circumference_2nd (str): 属性
        strength_main_core (str): 属性
        strength_band (str): 属性
        n_main_circumference_1st (int): 属性
        n_main_circumference_2nd (int): 属性
        n_main_core (int): 属性
        pitch_band (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main_circumference_1st": _FI(
            py_type=str,
            data_type=_DT.STR,
            required=True,
            xml_name="D_main_circumference_1st",
        ),
        "d_main_circumference_2nd": _FI(
            py_type=str, data_type=_DT.STR, xml_name="D_main_circumference_2nd"
        ),
        "d_main_core": _FI(py_type=str, data_type=_DT.STR, xml_name="D_main_core"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "strength_main_circumference_1st": _FI(py_type=str, data_type=_DT.STR),
        "strength_main_circumference_2nd": _FI(py_type=str, data_type=_DT.STR),
        "strength_main_core": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "n_main_circumference_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_circumference_1st",
        ),
        "n_main_circumference_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_circumference_2nd",
        ),
        "n_main_core": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_core",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarPile_RC_Same"


class StbSecBarArrangementPileRc(StBridgeElement):
    """StbSecBarArrangementPileRc：StbSecBarArrangementPile_RC

    Attributes:
        depth_cover (float): 属性
        depth_cover_top (float): 属性
        is_spiral (bool): 属性
        stb_sec_bar_pile_rc_same (StbSecBarPileRcSame): 子要素 StbSecBarPile_RC_Same(ＲＣ杭断面配筋・全断面)
        stb_sec_bar_pile_rc_top_bottom (list[StbSecBarPileRcTopBottom]): 子要素 StbSecBarPile_RC_TopBottom(ＲＣ杭断面配筋・杭頭脚別)
        stb_sec_bar_pile_rc_top_center_bottom (list[StbSecBarPileRcTopCenterBottom]): 子要素 StbSecBarPile_RC_TopCenterBottom(ＲＣ杭断面配筋・杭頭軸部杭脚)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "is_spiral": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isSpiral"),
        "stb_sec_bar_pile_rc_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarPileRcSame
        ),
        "stb_sec_bar_pile_rc_top_bottom": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarPileRcTopBottom]
        ),
        "stb_sec_bar_pile_rc_top_center_bottom": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBarPileRcTopCenterBottom]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementPile_RC"


class StbSecPileRcExtendedTopFoot(StBridgeElement):
    """StbSecPileRcExtendedTopFoot：StbSecPile_RC_ExtendedTopFoot

    Attributes:
        d_extended_top (float): 属性
        d_axial (float): 属性
        d_extended_foot (float): 属性
        angle_extended_top_taper (float): 属性
        length_extended_foot (float): 属性
        angle_extended_foot_taper (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_extended_top": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_extended_top",
        ),
        "d_axial": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_axial",
        ),
        "d_extended_foot": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_extended_foot",
        ),
        "angle_extended_top_taper": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "length_extended_foot": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "angle_extended_foot_taper": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ExtendedTopFoot"


class StbSecPileRcExtendedTop(StBridgeElement):
    """StbSecPileRcExtendedTop：StbSecPile_RC_ExtendedTop

    Attributes:
        d_extended_top (float): 属性
        d_axial (float): 属性
        angle_extended_top_taper (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_extended_top": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_extended_top",
        ),
        "d_axial": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_axial",
        ),
        "angle_extended_top_taper": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ExtendedTop"


class StbSecPileRcExtendedFoot(StBridgeElement):
    """StbSecPileRcExtendedFoot：StbSecPile_RC_ExtendedFoot

    Attributes:
        d_axial (float): 属性
        d_extended_foot (float): 属性
        length_extended_foot (float): 属性
        angle_extended_foot_taper (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_axial": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_axial",
        ),
        "d_extended_foot": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_extended_foot",
        ),
        "length_extended_foot": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "angle_extended_foot_taper": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ExtendedFoot"


class StbSecPileRcStraight(StBridgeElement):
    """StbSecPileRcStraight：StbSecPile_RC_Straight

    Attributes:
        d (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_Straight"


class StbSecFigurePileRc(StBridgeElement):
    """StbSecFigurePileRc：StbSecFigurePile_RC

    Attributes:
        length_pipe (float): 属性
        t_pipe (float): 属性
        strength_pipe (str): 属性
        stb_sec_pile_rc_straight (StbSecPileRcStraight): 子要素
        stb_sec_pile_rc_extended_foot (StbSecPileRcExtendedFoot): 子要素
        stb_sec_pile_rc_extended_top (StbSecPileRcExtendedTop): 子要素
        stb_sec_pile_rc_extended_top_foot (StbSecPileRcExtendedTopFoot): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "length_pipe": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "t_pipe": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_pipe": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_pile_rc_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcStraight
        ),
        "stb_sec_pile_rc_extended_foot": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcExtendedFoot
        ),
        "stb_sec_pile_rc_extended_top": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcExtendedTop
        ),
        "stb_sec_pile_rc_extended_top_foot": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcExtendedTopFoot
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigurePile_RC"


class StbSecPileRc(StBridgeElement):
    """ＲＣ杭断面：StbSecPile_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        strength_concrete (str): 属性
        stb_sec_figure_pile_rc (StbSecFigurePileRc): 子要素
        stb_sec_bar_arrangement_pile_rc (StbSecBarArrangementPileRc): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_pile_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigurePileRc
        ),
        "stb_sec_bar_arrangement_pile_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementPileRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC"


class StbSecBarFoundationRcContinuous(StBridgeElement):
    """ＲＣ基礎断面配筋・連続：StbSecBarFoundation_RC_Continuous

    Attributes:
        pos (StbSecBarFoundationRcContinuousPos): 属性 配筋位置 以下のいずれかMAIN_BASE_TOP（主筋方向元端上端筋）MAIN_BASE_BOTTOM（主筋方向元端下端筋）MAIN_TIP_TOP（主筋方向先端上端筋）MAIN_TIP_BOTTOM（主筋方向先端下端筋）TRANSVERSE_TOP（配力筋方向上端筋）TRANSVERSE_BOTTOM（配力筋方向下端筋）HORIZONTAL（横筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarFoundationRcContinuousPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "MAIN_TOP",
                "MAIN_BOTTOM",
                "TRANSVERSE_TOP",
                "TRANSVERSE_BOTTOM",
                "HORIZONTAL",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N",
        ),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarFoundation_RC_Continuous"


class StbSecBarFoundationRcThreeWay(StBridgeElement):
    """ＲＣ基礎断面配筋・三方：StbSecBarFoundation_RC_ThreeWay

    Attributes:
        pos (StbSecBarFoundationRcThreeWayPos): 属性 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）OUTSIDE_TOP（外周上端）OUTSIDE_BOTTOM（外周下端）HORIZONTAL（横）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarFoundationRcThreeWayPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "MAIN_TOP",
                "MAIN_BOTTOM",
                "OUTSIDE_TOP",
                "OUTSIDE_BOTTOM",
                "HORIZONTAL",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarFoundation_RC_ThreeWay"


class StbSecBarFoundationRcTriangle(StBridgeElement):
    """ＲＣ基礎断面配筋・三角：StbSecBarFoundation_RC_Triangle

    Attributes:
        pos (StbSecBarFoundationRcTrianglePos): 属性 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）TRANSVERSE_TOP（配力筋方向上端）TRANSVERSE_BOTTOM（配力筋方向下端）HORIZONTAL（横）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarFoundationRcTrianglePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "MAIN_TOP",
                "MAIN_BOTTOM",
                "TRANSVERSE_TOP",
                "TRANSVERSE_BOTTOM",
                "HORIZONTAL",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarFoundation_RC_Triangle"


class StbSecBarFoundationRcRect(StBridgeElement):
    """ＲＣ基礎断面配筋・矩形：StbSecBarFoundation_RC_Rect

    Attributes:
        pos (StbSecBarFoundationRcRectPos): 属性 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）HORIZONTAL（横）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarFoundationRcRectPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("X_TOP", "X_BOTTOM", "Y_TOP", "Y_BOTTOM", "HORIZONTAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarFoundation_RC_Rect"


class StbSecBarArrangementFoundationRc(StBridgeElement):
    """ＲＣ基礎断面配筋：StbSecBarArrangementFoundation_RC

    Attributes:
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        depth_cover_side (float): 属性
        stb_sec_bar_foundation_rc_rect (list[StbSecBarFoundationRcRect]): 子要素 StbSecBarFoundation_RC_Rect(ＲＣ基礎断面配筋・矩形)
        stb_sec_bar_foundation_rc_triangle (list[StbSecBarFoundationRcTriangle]): 子要素 StbSecBarFoundation_RC_Triangle(ＲＣ基礎断面配筋・三角)
        stb_sec_bar_foundation_rc_three_way (list[StbSecBarFoundationRcThreeWay]): 子要素 StbSecBarFoundation_RC_ThreeWay(ＲＣ基礎断面配筋・三方)
        stb_sec_bar_foundation_rc_continuous (list[StbSecBarFoundationRcContinuous]): 子要素 StbSecBarFoundation_RC_Continuous(ＲＣ基礎断面配筋・連続)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "depth_cover_side": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_bar_foundation_rc_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=5, py_type=list[StbSecBarFoundationRcRect]
        ),
        "stb_sec_bar_foundation_rc_triangle": _FI(
            kind=_FK.ELEMENT, max_occurs=5, py_type=list[StbSecBarFoundationRcTriangle]
        ),
        "stb_sec_bar_foundation_rc_three_way": _FI(
            kind=_FK.ELEMENT, max_occurs=5, py_type=list[StbSecBarFoundationRcThreeWay]
        ),
        "stb_sec_bar_foundation_rc_continuous": _FI(
            kind=_FK.ELEMENT,
            max_occurs=5,
            py_type=list[StbSecBarFoundationRcContinuous],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementFoundation_RC"


class StbSecFoundationRcContinuous(StBridgeElement):
    """ＲＣ連続基礎断面形状：StbSecFoundation_RC_Continuous

    Attributes:
        width (float): 属性 幅
        depth_base (float): 属性 根元厚さ
        depth_tip (float): 属性 先端厚さ
        type (StbSecFoundationRcContinuousType): 属性 タイプ 以下のいずれかRIGHT_LLEFT_LREVERSE_T
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth_base": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth_tip": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "type": _FI(
            py_type=StbSecFoundationRcContinuousType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RIGHT_L", "LEFT_L", "REVERSE_T"),
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFoundation_RC_Continuous"


class StbSecFoundationRcOctagon(StBridgeElement):
    """ＲＣ基礎断面形状・八角形：StbSecFoundation_RC_Octagon

    Attributes:
        width_x (float): 属性 X幅
        width_y (float): 属性 Y幅
        width_chamfer1_x (float): 属性 面取りX幅(1)
        width_chamfer1_y (float): 属性 面取りY幅(1)
        width_chamfer2_x (float): 属性 面取りX幅(2)
        width_chamfer2_y (float): 属性 面取りY幅(2)
        width_chamfer3_x (float): 属性 面取りX幅(3)
        width_chamfer3_y (float): 属性 面取りY幅(3)
        width_chamfer4_x (float): 属性 面取りX幅(4)
        width_chamfer4_y (float): 属性 面取りY幅(4)
        depth (float): 属性 厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_X",
        ),
        "width_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_Y",
        ),
        "width_chamfer1_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer1_X",
        ),
        "width_chamfer1_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer1_Y",
        ),
        "width_chamfer2_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer2_X",
        ),
        "width_chamfer2_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer2_Y",
        ),
        "width_chamfer3_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer3_X",
        ),
        "width_chamfer3_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer3_Y",
        ),
        "width_chamfer4_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer4_X",
        ),
        "width_chamfer4_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
            xml_name="width_chamfer4_Y",
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFoundation_RC_Octagon"


class StbSecFoundationRcEquiTriangle(StBridgeElement):
    """ＲＣ基礎断面形状・正三角形：StbSecFoundation_RC_EquiTriangle

    Attributes:
        width_base (float): 属性 底辺幅
        width_chamfer (float): 属性 面取り幅
        depth (float): 属性 厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width_base": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "width_chamfer": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFoundation_RC_EquiTriangle"


class StbSecFoundationRcTriangle(StBridgeElement):
    """ＲＣ基礎断面形状・直角三角形：StbSecFoundation_RC_Triangle

    Attributes:
        width_x (float): 属性 Ｘ幅
        width_y (float): 属性 Ｙ幅
        depth (float): 属性 厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_X",
        ),
        "width_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_Y",
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFoundation_RC_Triangle"


class StbSecFoundationRcTaperedRect(StBridgeElement):
    """ＲＣ基礎断面形状・矩形テーパー：StbSecFoundation_RC_TaperedRect

    Attributes:
        width_x (float): 属性 Ｘ幅
        width_y (float): 属性 Ｙ幅
        depth_base (float): 属性 根元厚さ
        depth_tip (float): 属性 先端厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_X",
        ),
        "width_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_Y",
        ),
        "depth_base": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth_tip": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFoundation_RC_TaperedRect"


class StbSecFoundationRcRect(StBridgeElement):
    """ＲＣ基礎断面形状・矩形：StbSecFoundation_RC_Rect

    Attributes:
        width_x (float): 属性 Ｘ幅
        width_y (float): 属性 Ｙ幅
        depth (float): 属性 厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_X",
        ),
        "width_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_Y",
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFoundation_RC_Rect"


class StbSecFigureFoundationRc(StBridgeElement):
    """ＲＣ基礎断面形状：StbSecFigureFoundation_RC

    Attributes:
        stb_sec_foundation_rc_rect (StbSecFoundationRcRect): 子要素 StbSecFoundation_RC_Rect(ＲＣ基礎断面形状・矩形)
        stb_sec_foundation_rc_tapered_rect (StbSecFoundationRcTaperedRect): 子要素 StbSecFoundation_RC_TaperedRect(ＲＣ基礎断面形状・矩形テーパー)
        stb_sec_foundation_rc_triangle (StbSecFoundationRcTriangle): 子要素 StbSecFoundation_RC_Triangle(ＲＣ基礎断面形状・直角三角形)
        stb_sec_foundation_rc_equi_triangle (StbSecFoundationRcEquiTriangle): 子要素 StbSecFoundation_RC_EquiTriangle(ＲＣ基礎断面形状・正三角形)
        stb_sec_foundation_rc_octagon (StbSecFoundationRcOctagon): 子要素 StbSecFoundation_RC_Octagon(ＲＣ基礎断面形状・八角形)
        stb_sec_foundation_rc_continuous (StbSecFoundationRcContinuous): 子要素 StbSecFoundation_RC_Continuous(ＲＣ連続基礎断面形状)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_foundation_rc_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFoundationRcRect
        ),
        "stb_sec_foundation_rc_tapered_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFoundationRcTaperedRect
        ),
        "stb_sec_foundation_rc_triangle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFoundationRcTriangle
        ),
        "stb_sec_foundation_rc_equi_triangle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFoundationRcEquiTriangle
        ),
        "stb_sec_foundation_rc_octagon": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFoundationRcOctagon
        ),
        "stb_sec_foundation_rc_continuous": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFoundationRcContinuous
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureFoundation_RC"


class StbSecFoundationRc(StBridgeElement):
    """ＲＣ基礎断面：StbSecFoundation_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_foundation_rc (StbSecFigureFoundationRc): 子要素 StbSecFigureFoundation_RC(ＲＣ基礎断面形状)
        stb_sec_bar_arrangement_foundation_rc (StbSecBarArrangementFoundationRc): 子要素 StbSecBarArrangementFoundation_RC(ＲＣ基礎断面配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_foundation_rc": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecFigureFoundationRc,
        ),
        "stb_sec_bar_arrangement_foundation_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementFoundationRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFoundation_RC"


class StbSecBarWallRcOpen(StBridgeElement):
    """壁開口配筋：StbSecBarWall_RC_Open

    Attributes:
        pos (StbSecBarWallRcOpenPos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）DIAGONAL（斜め筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        length (float): 属性 長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarWallRcOpenPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL", "DIAGONAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
        "length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_Open"


class StbSecBarWallRcEdge(StBridgeElement):
    """端部補強筋（コ型補強筋）：StbSecBarWall_RC_Edge

    Attributes:
        pos (StbSecBarWallRcEdgePos): 属性 配筋位置 以下のいずれかVERTICAL_START（袖壁始端）VERTICAL_END（袖壁終端）HORIZONTAL_BOTTOM（たれ壁下端）HORIZONTAL_TOP（腰壁上端）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarWallRcEdgePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "VERTICAL_START",
                "VERTICAL_END",
                "HORIZONTAL_BOTTOM",
                "HORIZONTAL_TOP",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_Edge"


class StbSecBarWallRcInsideAndOutside(StBridgeElement):
    """ＲＣ壁断面配筋（内外異なる）：StbSecBarWall_RC_InsideAndOutside

    Attributes:
        pos (StbSecBarWallRcInsideAndOutsidePos): 属性 配筋位置 以下のいずれかVERTICAL_OUTSIDE（縦筋外側）VERTICAL_INSIDE（縦筋内側）HORIZONTAL_OUTSIDE（横筋外側）HORIZONTAL_INSIDE（横筋内側）
        pos2 (StbSecBarWallRcInsideAndOutsidePos2): 属性 鉄筋の段位置
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarWallRcInsideAndOutsidePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "VERTICAL_OUTSIDE",
                "VERTICAL_INSIDE",
                "HORIZONTAL_OUTSIDE",
                "HORIZONTAL_INSIDE",
            ),
        ),
        "pos2": _FI(
            py_type=StbSecBarWallRcInsideAndOutsidePos2,
            data_type=_DT.STR_ENUM,
            choices=("ALL", "TOP_START", "MIDDLE", "BOTTOM_END"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_InsideAndOutside"


class StbSecBarWallRcDoubleNet(StBridgeElement):
    """ＲＣ壁断面配筋・ダブル：StbSecBarWall_RC_DoubleNet

    Attributes:
        pos (StbSecBarWallRcDoubleNetPos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarWallRcDoubleNetPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_DoubleNet"


class StbSecBarWallRcZigzag(StBridgeElement):
    """ＲＣ壁断面配筋・千鳥：StbSecBarWall_RC_Zigzag

    Attributes:
        pos (StbSecBarWallRcZigzagPos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarWallRcZigzagPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_Zigzag"


class StbSecBarWallRcSingle(StBridgeElement):
    """ＲＣ壁断面配筋・シングル：StbSecBarWall_RC_Single

    Attributes:
        pos (StbSecBarWallRcSinglePos): 属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarWallRcSinglePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_Single"


class StbSecBarArrangementWallRc(StBridgeElement):
    """ＲＣ壁断面配筋：StbSecBarArrangementWall_RC

    Attributes:
        depth_cover_outside (float): 属性
        depth_cover_inside (float): 属性
        stb_sec_bar_wall_rc_single (list[StbSecBarWallRcSingle]): 子要素 StbSecBarWall_RC_Single(ＲＣ壁断面配筋・シングル)
        stb_sec_bar_wall_rc_zigzag (list[StbSecBarWallRcZigzag]): 子要素 StbSecBarWall_RC_Zigzag(ＲＣ壁断面配筋・千鳥)
        stb_sec_bar_wall_rc_double_net (list[StbSecBarWallRcDoubleNet]): 子要素 StbSecBarWall_RC_DoubleNet(ＲＣ壁断面配筋・ダブル)
        stb_sec_bar_wall_rc_inside_and_outside (list[StbSecBarWallRcInsideAndOutside]): 子要素 StbSecBarWall_RC_InsideAndOutside(ＲＣ壁断面配筋（内外異なる）)
        stb_sec_bar_wall_rc_edge (list[StbSecBarWallRcEdge]): 子要素 StbSecBarWall_RC_Edge(端部補強筋（コ型補強筋）)
        stb_sec_bar_wall_rc_open (list[StbSecBarWallRcOpen]): 子要素 StbSecBarWall_RC_Open(壁開口配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_outside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "depth_cover_inside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_wall_rc_single": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarWallRcSingle]
        ),
        "stb_sec_bar_wall_rc_zigzag": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarWallRcZigzag]
        ),
        "stb_sec_bar_wall_rc_double_net": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarWallRcDoubleNet]
        ),
        "stb_sec_bar_wall_rc_inside_and_outside": _FI(
            kind=_FK.ELEMENT,
            max_occurs=12,
            py_type=list[StbSecBarWallRcInsideAndOutside],
        ),
        "stb_sec_bar_wall_rc_edge": _FI(
            kind=_FK.ELEMENT, max_occurs=4, py_type=list[StbSecBarWallRcEdge]
        ),
        "stb_sec_bar_wall_rc_open": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBarWallRcOpen]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementWall_RC"


class StbSecWallRcStraight(StBridgeElement):
    """ＲＣ壁断面形状・ストレート：StbSecWall_RC_Straight

    Attributes:
        t (float): 属性 厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecWall_RC_Straight"


class StbSecFigureWallRc(StBridgeElement):
    """ＲＣ壁断面形状：StbSecFigureWall_RC

    Attributes:
        stb_sec_wall_rc_straight (StbSecWallRcStraight): 子要素 StbSecWall_RC_Straight(ＲＣ壁断面形状・ストレート)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_wall_rc_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecWallRcStraight
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureWall_RC"


class StbSecWallRc(StBridgeElement):
    """ＲＣ壁断面：StbSecWall_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_wall_rc (StbSecFigureWallRc): 子要素 StbSecFigureWall_RC(ＲＣ壁断面形状)
        stb_sec_bar_arrangement_wall_rc (StbSecBarArrangementWallRc): 子要素 StbSecBarArrangementWall_RC(ＲＣ壁断面配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_wall_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigureWallRc
        ),
        "stb_sec_bar_arrangement_wall_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementWallRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecWall_RC"


class StbSecProductSlabPrecast(StBridgeElement):
    """既製スラブ製品：StbSecProductSlabPrecast

    Attributes:
        product_company (str): 属性
        product_name (str): 属性
        product_code (str): 属性 製品型番
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_name": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarSlabPrecast1Way(StBridgeElement):
    """既製スラブ断面配筋・１方向：StbSecBarSlabPrecast1Way

    Attributes:
        pos (StbSecBarSlabPrecast1WayPos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabPrecast1WayPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "MAIN_TOP",
                "MAIN_BOTTOM",
                "TRANSVERSE_TOP",
                "TRANSVERSE_BOTTOM",
                "REFRACTORY",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarSlabPrecast2Way(StBridgeElement):
    """既製スラブ断面配筋・２方向：StbSecBarSlabPrecast2Way

    Attributes:
        pos (StbSecBarSlabPrecast2WayPos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabPrecast2WayPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("SHORT_TOP", "SHORT_BOTTOM", "LONG_TOP", "LONG_BOTTOM"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarSlabPrecastStandard(StBridgeElement):
    """既製スラブ断面配筋・標準：StbSecBarSlabPrecastStandard

    Attributes:
        pos (StbSecBarSlabPrecastStandardPos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabPrecastStandardPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "SHORT_TOP_COLUMN",
                "SHORT_TOP_MID_END",
                "SHORT_TOP_MID_CENTER",
                "SHORT_BOTTOM_COLUMN",
                "SHORT_BOTTOM_MID_END",
                "SHORT_BOTTOM_MID_CENTER",
                "LONG_TOP_COLUMN",
                "LONG_TOP_MID_END",
                "LONG_TOP_MID_CENTER",
                "LONG_BOTTOM_COLUMN",
                "LONG_BOTTOM_MID_END",
                "LONG_BOTTOM_MID_CENTER",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarArrangementSlabPrecast(StBridgeElement):
    """既製スラブトップ部分断面配筋：StbSecBarArrangementSlabPrecast

    Attributes:
        depth_cover_top (float): 属性 かぶり厚さ（上）
        stb_sec_bar_slab_precast_standard (list[StbSecBarSlabPrecastStandard]): 子要素 StbSecBarSlabPrecastStandard(既製スラブ断面配筋・標準)
        stb_sec_bar_slab_precast2_way (list[StbSecBarSlabPrecast2Way]): 子要素 StbSecBarSlabPrecast2Way(既製スラブ断面配筋・２方向)
        stb_sec_bar_slab_precast1_way (list[StbSecBarSlabPrecast1Way]): 子要素 StbSecBarSlabPrecast1Way(既製スラブ断面配筋・１方向)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_bar_slab_precast_standard": _FI(
            kind=_FK.ELEMENT, max_occurs=12, py_type=list[StbSecBarSlabPrecastStandard]
        ),
        "stb_sec_bar_slab_precast2_way": _FI(
            kind=_FK.ELEMENT, max_occurs=4, py_type=list[StbSecBarSlabPrecast2Way]
        ),
        "stb_sec_bar_slab_precast1_way": _FI(
            kind=_FK.ELEMENT, max_occurs=5, py_type=list[StbSecBarSlabPrecast1Way]
        ),
    }


class StbSecSlabPrecastStraight(StBridgeElement):
    """既製スラブトップ部分断面形状・ストレート：StbSecSlabPrecastStraight

    Attributes:
        depth_concrete (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_concrete": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecFigureSlabPrecast(StBridgeElement):
    """既製スラブトップ部分断面形状：StbSecFigureSlabPrecast

    Attributes:
        stb_sec_slab_precast_straight (StbSecSlabPrecastStraight): 子要素 StbSecSlabPrecastStraight(既製スラブトップ部分断面形状・ストレート)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_slab_precast_straight": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecSlabPrecastStraight,
        ),
    }


class StbSecSlabPrecast(StBridgeElement):
    """既製スラブ断面：StbSecSlabPrecast

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        precast_type (StbSecSlabPrecastPrecastType): 属性 工法種別 以下のいずれかFULL（フルPC工法）HALF（ハーフPC工法）FORM（型枠利用）
        strength_concrete (str): 属性
        stb_sec_figure_slab_precast (StbSecFigureSlabPrecast): 子要素 StbSecFigureSlabPrecast(既製スラブトップ部分断面形状)
        stb_sec_bar_arrangement_slab_precast (StbSecBarArrangementSlabPrecast): 子要素 StbSecBarArrangementSlabPrecast(既製スラブトップ部分断面配筋)
        stb_sec_product_slab_precast (StbSecProductSlabPrecast): 子要素 StbSecProductSlabPrecast(既製スラブ製品)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "precast_type": _FI(
            py_type=StbSecSlabPrecastPrecastType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("FULL", "HALF", "FORM"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_slab_precast": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFigureSlabPrecast
        ),
        "stb_sec_bar_arrangement_slab_precast": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementSlabPrecast
        ),
        "stb_sec_product_slab_precast": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecProductSlabPrecast,
        ),
    }


class StbSecProductSlabDeck(StBridgeElement):
    """StbSecProductSlabDeck

    Attributes:
        product_company (str): 属性
        product_code (str): 属性
        depth_deck (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "depth_deck": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbSecBarSlabDeck1Way(StBridgeElement):
    """デッキ合成スラブ断面配筋・１方向：StbSecBarSlabDeck1Way

    Attributes:
        pos (StbSecBarSlabDeck1WayPos): 属性 配筋位置以下のいずれかMAIN_TOP（①主筋方向上端）TRANSVERSE_TOP（②配力筋方向上端）MESH（③溶接金網）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabDeck1WayPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "MAIN_TOP",
                "MAIN_BOTTOM",
                "TRANSVERSE_TOP",
                "TRANSVERSE_BOTTOM",
                "REFRACTORY",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarSlabDeck2Way(StBridgeElement):
    """StbSecBarSlabDeck2Way

    Attributes:
        pos (StbSecBarSlabDeck2WayPos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabDeck2WayPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("SHORT_TOP", "SHORT_BOTTOM", "LONG_TOP", "LONG_BOTTOM"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarSlabDeckStandard(StBridgeElement):
    """StbSecBarSlabDeckStandard

    Attributes:
        pos (StbSecBarSlabDeckStandardPos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabDeckStandardPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "SHORT_TOP_COLUMN",
                "SHORT_TOP_MID_END",
                "SHORT_TOP_MID_CENTER",
                "SHORT_BOTTOM_COLUMN",
                "SHORT_BOTTOM_MID_END",
                "SHORT_BOTTOM_MID_CENTER",
                "LONG_TOP_COLUMN",
                "LONG_TOP_MID_END",
                "LONG_TOP_MID_CENTER",
                "LONG_BOTTOM_COLUMN",
                "LONG_BOTTOM_MID_END",
                "LONG_BOTTOM_MID_CENTER",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarArrangementSlabDeck(StBridgeElement):
    """デッキ合成スラブ断面配筋：StbSecBarArrangementSlabDeck

    Attributes:
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        stb_sec_bar_slab_deck_standard (list[StbSecBarSlabDeckStandard]): 子要素
        stb_sec_bar_slab_deck2_way (list[StbSecBarSlabDeck2Way]): 子要素
        stb_sec_bar_slab_deck1_way (list[StbSecBarSlabDeck1Way]): 子要素 StbSecBarSlabDeck1Way(デッキ合成スラブ断面配筋・１方向)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_slab_deck_standard": _FI(
            kind=_FK.ELEMENT, max_occurs=12, py_type=list[StbSecBarSlabDeckStandard]
        ),
        "stb_sec_bar_slab_deck2_way": _FI(
            kind=_FK.ELEMENT, max_occurs=4, py_type=list[StbSecBarSlabDeck2Way]
        ),
        "stb_sec_bar_slab_deck1_way": _FI(
            kind=_FK.ELEMENT, max_occurs=5, py_type=list[StbSecBarSlabDeck1Way]
        ),
    }


class StbSecSlabDeckStraight(StBridgeElement):
    """StbSecSlabDeckStraight

    Attributes:
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecFigureSlabDeck(StBridgeElement):
    """StbSecFigureSlabDeck

    Attributes:
        stb_sec_slab_deck_straight (StbSecSlabDeckStraight): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_slab_deck_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecSlabDeckStraight
        ),
    }


class StbSecSlabDeck(StBridgeElement):
    """デッキ合成スラブ断面：StbSecSlabDeck

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        product_type (StbSecSlabDeckProductType): 属性
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_slab_deck (StbSecFigureSlabDeck): 子要素
        stb_sec_bar_arrangement_slab_deck (StbSecBarArrangementSlabDeck): 子要素 StbSecBarArrangementSlabDeck(デッキ合成スラブ断面配筋)
        stb_sec_product_slab_deck (StbSecProductSlabDeck): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "product_type": _FI(
            py_type=StbSecSlabDeckProductType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("FLAT", "COMPOSITE"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_slab_deck": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigureSlabDeck
        ),
        "stb_sec_bar_arrangement_slab_deck": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementSlabDeck
        ),
        "stb_sec_product_slab_deck": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecProductSlabDeck
        ),
    }


class StbSecBarSlabRcOpen(StBridgeElement):
    """スラブ開口配筋：StbSecBarSlab_RC_Open

    Attributes:
        pos (StbSecBarSlabRcOpenPos): 属性 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）DIAGONAL_TOP（斜め方向上端）DIAGONAL_BOTTOM（斜め方向下端）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        length (float): 属性 長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRcOpenPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "X_TOP",
                "X_BOTTOM",
                "Y_TOP",
                "Y_BOTTOM",
                "DIAGONAL_TOP",
                "DIAGONAL_BOTTOM",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
        "length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_Open"


class StbSecBarSlabRc1Way2(StBridgeElement):
    """StbSecBarSlabRc1Way2：StbSecBarSlab_RC_1Way2

    Attributes:
        pos (StbSecBarSlabRc1Way2Pos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRc1Way2Pos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "MAIN_BASE_TOP",
                "MAIN_BASE_BOTTOM",
                "MAIN_TIP_TOP",
                "MAIN_TIP_BOTTOM",
                "TRANSVERSE_TOP",
                "TRANSVERSE_BOTTOM",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_1Way2"


class StbSecBarSlabRc1Way1(StBridgeElement):
    """StbSecBarSlabRc1Way1：StbSecBarSlab_RC_1Way1

    Attributes:
        pos (StbSecBarSlabRc1Way1Pos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRc1Way1Pos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("MAIN_TOP", "MAIN_BOTTOM", "TRANSVERSE_TOP", "TRANSVERSE_BOTTOM"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_1Way1"


class StbSecBarSlabRc2Way(StBridgeElement):
    """StbSecBarSlabRc2Way：StbSecBarSlab_RC_2Way

    Attributes:
        pos (StbSecBarSlabRc2WayPos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRc2WayPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("SHORT_TOP", "SHORT_BOTTOM", "LONG_TOP", "LONG_BOTTOM"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_2Way"


class StbSecBarSlabRcStandard(StBridgeElement):
    """StbSecBarSlabRcStandard：StbSecBarSlab_RC_Standard

    Attributes:
        pos (StbSecBarSlabRcStandardPos): 属性
        strength (str): 属性
        d (str): 属性
        pitch (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRcStandardPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "SHORT_TOP_COLUMN",
                "SHORT_TOP_MID_END",
                "SHORT_TOP_MID_CENTER",
                "SHORT_BOTTOM_COLUMN",
                "SHORT_BOTTOM_MID_END",
                "SHORT_BOTTOM_MID_CENTER",
                "LONG_TOP_COLUMN",
                "LONG_TOP_MID_END",
                "LONG_TOP_MID_CENTER",
                "LONG_BOTTOM_COLUMN",
                "LONG_BOTTOM_MID_END",
                "LONG_BOTTOM_MID_CENTER",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_Standard"


class StbSecBarArrangementSlabRc(StBridgeElement):
    """StbSecBarArrangementSlabRc：StbSecBarArrangementSlab_RC

    Attributes:
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        stb_sec_bar_slab_rc_standard (list[StbSecBarSlabRcStandard]): 子要素
        stb_sec_bar_slab_rc_2_way (list[StbSecBarSlabRc2Way]): 子要素
        stb_sec_bar_slab_rc_1_way1 (list[StbSecBarSlabRc1Way1]): 子要素
        stb_sec_bar_slab_rc_1_way2 (list[StbSecBarSlabRc1Way2]): 子要素
        stb_sec_bar_slab_rc_open (list[StbSecBarSlabRcOpen]): 子要素 StbSecBarSlab_RC_Open(スラブ開口配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_slab_rc_standard": _FI(
            kind=_FK.ELEMENT, max_occurs=12, py_type=list[StbSecBarSlabRcStandard]
        ),
        "stb_sec_bar_slab_rc_2_way": _FI(
            kind=_FK.ELEMENT, max_occurs=4, py_type=list[StbSecBarSlabRc2Way]
        ),
        "stb_sec_bar_slab_rc_1_way1": _FI(
            kind=_FK.ELEMENT, max_occurs=4, py_type=list[StbSecBarSlabRc1Way1]
        ),
        "stb_sec_bar_slab_rc_1_way2": _FI(
            kind=_FK.ELEMENT, max_occurs=6, py_type=list[StbSecBarSlabRc1Way2]
        ),
        "stb_sec_bar_slab_rc_open": _FI(
            kind=_FK.ELEMENT, max_occurs=6, py_type=list[StbSecBarSlabRcOpen]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementSlab_RC"


class StbSecSlabRcHaunch(StBridgeElement):
    """StbSecSlabRcHaunch：StbSecSlab_RC_Haunch

    Attributes:
        pos (StbSecSlabRcHaunchPos): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSlabRcHaunchPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASE", "CENTER", "HAUNCH"),
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_Haunch"


class StbSecSlabRcTaper(StBridgeElement):
    """StbSecSlabRcTaper：StbSecSlab_RC_Taper

    Attributes:
        pos (StbSecSlabRcTaperPos): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSlabRcTaperPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASE", "TIP"),
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_Taper"


class StbSecSlabRcStraight(StBridgeElement):
    """StbSecSlabRcStraight：StbSecSlab_RC_Straight

    Attributes:
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_Straight"


class StbSecFigureSlabRc(StBridgeElement):
    """StbSecFigureSlabRc：StbSecFigureSlab_RC

    Attributes:
        stb_sec_slab_rc_straight (StbSecSlabRcStraight): 子要素
        stb_sec_slab_rc_taper (list[StbSecSlabRcTaper]): 子要素
        stb_sec_slab_rc_haunch (list[StbSecSlabRcHaunch]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_slab_rc_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSlabRcStraight
        ),
        "stb_sec_slab_rc_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSlabRcTaper]
        ),
        "stb_sec_slab_rc_haunch": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSlabRcHaunch]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureSlab_RC"


class StbSecSlabRc(StBridgeElement):
    """ＲＣスラブ断面：StbSecSlab_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        is_foundation (bool): 属性 基礎スラブか否か
        is_earthen (bool): 属性 土間か否か
        is_canti (bool): 属性 片持ちスラブか否か
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_slab_rc (StbSecFigureSlabRc): 子要素
        stb_sec_bar_arrangement_slab_rc (StbSecBarArrangementSlabRc): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "is_foundation": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isFoundation"),
        "is_earthen": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isEarthen"),
        "is_canti": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isCanti"),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_slab_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigureSlabRc
        ),
        "stb_sec_bar_arrangement_slab_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementSlabRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC"


class StbSecSteelBraceSThreeTypes(StBridgeElement):
    """Ｓブレース断面鉄骨形状・３種類：StbSecSteelBrace_S_ThreeTypes

    Attributes:
        pos (StbSecSteelBraceSThreeTypesPos): 属性 配置位置以下のいずれかBOTTOM（脚部）CENTER（中央）TOP（頭部）
        shape (str): 属性 鉄骨形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBraceSThreeTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "CENTER", "TOP"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBrace_S_ThreeTypes"


class StbSecSteelBraceSNotSame(StBridgeElement):
    """Ｓブレース断面鉄骨形状・頭脚部別：StbSecSteelBrace_S_NotSame

    Attributes:
        pos (StbSecSteelBraceSNotSamePos): 属性 配置位置以下のいずれかBOTTOM（脚部）TOP（頭部）
        shape (str): 属性 鉄骨形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBraceSNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBrace_S_NotSame"


class StbSecSteelBraceSSame(StBridgeElement):
    """Ｓブレース断面鉄骨形状・同一：StbSecSteelBrace_S_Same

    Attributes:
        shape (str): 属性 鉄骨形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBrace_S_Same"


class StbSecSteelFigureBraceS(StBridgeElement):
    """Ｓブレース断面鉄骨形状：StbSecSteelFigureBrace_S

    Attributes:
        joint_id_start (int): 属性
        joint_id_end (int): 属性
        stb_sec_steel_brace_s_same (StbSecSteelBraceSSame): 子要素 StbSecSteelBrace_S_Same(Ｓブレース断面鉄骨形状・同一)
        stb_sec_steel_brace_s_not_same (list[StbSecSteelBraceSNotSame]): 子要素 StbSecSteelBrace_S_NotSame(Ｓブレース断面鉄骨形状・頭脚部別)
        stb_sec_steel_brace_s_three_types (list[StbSecSteelBraceSThreeTypes]): 子要素 StbSecSteelBrace_S_ThreeTypes(Ｓブレース断面鉄骨形状・３種類)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "joint_id_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_sec_steel_brace_s_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelBraceSSame
        ),
        "stb_sec_steel_brace_s_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSteelBraceSNotSame]
        ),
        "stb_sec_steel_brace_s_three_types": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelBraceSThreeTypes]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelFigureBrace_S"


class StbSecBraceS(StBridgeElement):
    """Ｓブレース断面：StbSecBrace_S

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_brace (StbSecBraceSKindBrace): 属性 ブレースの種別以下のいずれかVERTICAL（鉛直ブレース）HORIZONTAL（水平ブレース）
        stb_sec_steel_figure_brace_s (StbSecSteelFigureBraceS): 子要素 StbSecSteelFigureBrace_S(Ｓブレース断面鉄骨形状)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_brace": _FI(
            py_type=StbSecBraceSKindBrace,
            data_type=_DT.STR_ENUM,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "stb_sec_steel_figure_brace_s": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecSteelFigureBraceS,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBrace_S"


class StbSecSteelBeamSrcFiveTypes(StBridgeElement):
    """StbSecSteelBeamSrcFiveTypes：StbSecSteelBeam_SRC_FiveTypes

    Attributes:
        pos (StbSecSteelBeamSrcFiveTypesPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSrcFiveTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END", "HAUNCH_S", "HAUNCH_E"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_SRC_FiveTypes"


class StbSecSteelBeamSrcHaunch(StBridgeElement):
    """StbSecSteelBeamSrcHaunch：StbSecSteelBeam_SRC_Haunch

    Attributes:
        pos (StbSecSteelBeamSrcHaunchPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSrcHaunchPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_SRC_Haunch"


class StbSecSteelBeamSrcJoint(StBridgeElement):
    """StbSecSteelBeamSrcJoint：StbSecSteelBeam_SRC_Joint

    Attributes:
        pos (StbSecSteelBeamSrcJointPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSrcJointPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_SRC_Joint"


class StbSecSteelBeamSrcTaper(StBridgeElement):
    """StbSecSteelBeamSrcTaper：StbSecSteelBeam_SRC_Taper

    Attributes:
        pos (StbSecSteelBeamSrcTaperPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSrcTaperPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_SRC_Taper"


class StbSecSteelBeamSrcStraight(StBridgeElement):
    """StbSecSteelBeamSrcStraight：StbSecSteelBeam_SRC_Straight

    Attributes:
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_SRC_Straight"


class StbSecSteelFigureBeamSrc(StBridgeElement):
    """ＳＲＣ梁断面鉄骨形状：StbSecSteelFigureBeam_SRC

    Attributes:
        offset (float): 属性
        level (float): 属性
        joint_id_start (int): 属性
        joint_id_end (int): 属性
        stb_sec_steel_beam_src_straight (StbSecSteelBeamSrcStraight): 子要素
        stb_sec_steel_beam_src_taper (list[StbSecSteelBeamSrcTaper]): 子要素
        stb_sec_steel_beam_src_joint (list[StbSecSteelBeamSrcJoint]): 子要素
        stb_sec_steel_beam_src_haunch (list[StbSecSteelBeamSrcHaunch]): 子要素
        stb_sec_steel_beam_src_five_types (list[StbSecSteelBeamSrcFiveTypes]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "level": _FI(py_type=float, data_type=_DT.FLOAT),
        "joint_id_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_sec_steel_beam_src_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelBeamSrcStraight
        ),
        "stb_sec_steel_beam_src_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSteelBeamSrcTaper]
        ),
        "stb_sec_steel_beam_src_joint": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelBeamSrcJoint]
        ),
        "stb_sec_steel_beam_src_haunch": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelBeamSrcHaunch]
        ),
        "stb_sec_steel_beam_src_five_types": _FI(
            kind=_FK.ELEMENT, max_occurs=5, py_type=list[StbSecSteelBeamSrcFiveTypes]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelFigureBeam_SRC"


class StbSecBarBeamSrcStartEnd(StBridgeElement):
    """StbSecBarBeamSrcStartEnd：StbSecBarBeam_SRC_StartEnd

    Attributes:
        pos (StbSecBarBeamSrcStartEndPos): 属性
        pos_name (str): 属性
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_stirrup (str): 属性
        d_web (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_stirrup (str): 属性
        strength_web (str): 属性
        strength_bar_spacing (str): 属性
        n_main_top_1st (int): 属性
        n_main_top_2nd (int): 属性
        n_main_top_3rd (int): 属性
        n_main_bottom_1st (int): 属性
        n_main_bottom_2nd (int): 属性
        n_main_bottom_3rd (int): 属性
        n_2nd_main_top_1st (int): 属性
        n_2nd_main_top_2nd (int): 属性
        n_2nd_main_top_3rd (int): 属性
        n_2nd_main_bottom_1st (int): 属性
        n_2nd_main_bottom_2nd (int): 属性
        n_2nd_main_bottom_3rd (int): 属性
        n_stirrup (int): 属性
        pitch_stirrup (float): 属性
        n_web (int): 属性
        n_bar_spacing (int): 属性
        pitch_bar_spacing (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarBeamSrcStartEndPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_stirrup": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_stirrup"
        ),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_top_1st",
        ),
        "n_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_2nd",
        ),
        "n_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_3rd",
        ),
        "n_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_bottom_1st",
        ),
        "n_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_2nd",
        ),
        "n_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_3rd",
        ),
        "n_2nd_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_1st",
        ),
        "n_2nd_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_2nd",
        ),
        "n_2nd_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_3rd",
        ),
        "n_2nd_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_1st",
        ),
        "n_2nd_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_2nd",
        ),
        "n_2nd_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_3rd",
        ),
        "n_stirrup": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_stirrup",
        ),
        "pitch_stirrup": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarBeam_SRC_StartEnd"


class StbSecBarBeamSrcThreeTypes(StBridgeElement):
    """StbSecBarBeamSrcThreeTypes：StbSecBarBeam_SRC_ThreeTypes

    Attributes:
        pos (StbSecBarBeamSrcThreeTypesPos): 属性
        pos_name (str): 属性
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_stirrup (str): 属性
        d_web (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_stirrup (str): 属性
        strength_web (str): 属性
        strength_bar_spacing (str): 属性
        n_main_top_1st (int): 属性
        n_main_top_2nd (int): 属性
        n_main_top_3rd (int): 属性
        n_main_bottom_1st (int): 属性
        n_main_bottom_2nd (int): 属性
        n_main_bottom_3rd (int): 属性
        n_2nd_main_top_1st (int): 属性
        n_2nd_main_top_2nd (int): 属性
        n_2nd_main_top_3rd (int): 属性
        n_2nd_main_bottom_1st (int): 属性
        n_2nd_main_bottom_2nd (int): 属性
        n_2nd_main_bottom_3rd (int): 属性
        n_stirrup (int): 属性
        pitch_stirrup (float): 属性
        n_web (int): 属性
        n_bar_spacing (int): 属性
        pitch_bar_spacing (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarBeamSrcThreeTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_stirrup": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_stirrup"
        ),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_top_1st",
        ),
        "n_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_2nd",
        ),
        "n_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_3rd",
        ),
        "n_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_bottom_1st",
        ),
        "n_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_2nd",
        ),
        "n_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_3rd",
        ),
        "n_2nd_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_1st",
        ),
        "n_2nd_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_2nd",
        ),
        "n_2nd_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_3rd",
        ),
        "n_2nd_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_1st",
        ),
        "n_2nd_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_2nd",
        ),
        "n_2nd_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_3rd",
        ),
        "n_stirrup": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_stirrup",
        ),
        "pitch_stirrup": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarBeam_SRC_ThreeTypes"


class StbSecBarBeamSrcSame(StBridgeElement):
    """StbSecBarBeamSrcSame：StbSecBarBeam_SRC_Same

    Attributes:
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_stirrup (str): 属性
        d_web (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_stirrup (str): 属性
        strength_web (str): 属性
        strength_bar_spacing (str): 属性
        n_main_top_1st (int): 属性
        n_main_top_2nd (int): 属性
        n_main_top_3rd (int): 属性
        n_main_bottom_1st (int): 属性
        n_main_bottom_2nd (int): 属性
        n_main_bottom_3rd (int): 属性
        n_2nd_main_top_1st (int): 属性
        n_2nd_main_top_2nd (int): 属性
        n_2nd_main_top_3rd (int): 属性
        n_2nd_main_bottom_1st (int): 属性
        n_2nd_main_bottom_2nd (int): 属性
        n_2nd_main_bottom_3rd (int): 属性
        n_stirrup (int): 属性
        pitch_stirrup (float): 属性
        n_web (int): 属性
        n_bar_spacing (int): 属性
        pitch_bar_spacing (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_stirrup": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_stirrup"
        ),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_top_1st",
        ),
        "n_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_2nd",
        ),
        "n_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_3rd",
        ),
        "n_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_bottom_1st",
        ),
        "n_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_2nd",
        ),
        "n_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_3rd",
        ),
        "n_2nd_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_1st",
        ),
        "n_2nd_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_2nd",
        ),
        "n_2nd_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_3rd",
        ),
        "n_2nd_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_1st",
        ),
        "n_2nd_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_2nd",
        ),
        "n_2nd_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_3rd",
        ),
        "n_stirrup": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_stirrup",
        ),
        "pitch_stirrup": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarBeam_SRC_Same"


class StbSecBarArrangementBeamSrc(StBridgeElement):
    """ＳＲＣ梁断面配筋：StbSecBarArrangementBeam_SRC

    Attributes:
        depth_cover_left (float): 属性
        depth_cover_right (float): 属性
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        interval (float): 属性
        center_top (float): 属性
        center_bottom (float): 属性
        center_side (float): 属性
        center_interval (float): 属性
        length_bar_start (float): 属性
        length_bar_end (float): 属性
        stb_sec_bar_beam_src_same (StbSecBarBeamSrcSame): 子要素
        stb_sec_bar_beam_src_three_types (list[StbSecBarBeamSrcThreeTypes]): 子要素
        stb_sec_bar_beam_src_start_end (list[StbSecBarBeamSrcStartEnd]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_left": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_right": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_bottom": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_side": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_bar_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_bar_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_bar_beam_src_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarBeamSrcSame
        ),
        "stb_sec_bar_beam_src_three_types": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBarBeamSrcThreeTypes]
        ),
        "stb_sec_bar_beam_src_start_end": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarBeamSrcStartEnd]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementBeam_SRC"


class StbSecBeamSrcHaunch(StBridgeElement):
    """StbSecBeamSrcHaunch：StbSecBeam_SRC_Haunch

    Attributes:
        pos (StbSecBeamSrcHaunchPos): 属性
        width (float): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBeamSrcHaunchPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_SRC_Haunch"


class StbSecBeamSrcTaper(StBridgeElement):
    """StbSecBeamSrcTaper：StbSecBeam_SRC_Taper

    Attributes:
        pos (StbSecBeamSrcTaperPos): 属性
        width (float): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBeamSrcTaperPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_SRC_Taper"


class StbSecBeamSrcStraight(StBridgeElement):
    """StbSecBeamSrcStraight：StbSecBeam_SRC_Straight

    Attributes:
        width (float): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_SRC_Straight"


class StbSecFigureBeamSrc(StBridgeElement):
    """ＳＲＣ梁断面形状：StbSecFigureBeam_SRC

    Attributes:
        stb_sec_beam_src_straight (StbSecBeamSrcStraight): 子要素
        stb_sec_beam_src_taper (list[StbSecBeamSrcTaper]): 子要素
        stb_sec_beam_src_haunch (list[StbSecBeamSrcHaunch]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_beam_src_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBeamSrcStraight
        ),
        "stb_sec_beam_src_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBeamSrcTaper]
        ),
        "stb_sec_beam_src_haunch": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBeamSrcHaunch]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureBeam_SRC"


class StbSecBeamSrc(StBridgeElement):
    """ＳＲＣ梁断面：StbSecBeam_SRC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_beam (StbSecBeamSrcKindBeam): 属性 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）
        is_foundation (bool): 属性 基礎梁か否か
        is_canti (bool): 属性 片持ち梁か否か
        is_outin (bool): 属性 外端・内端指定
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_beam_src (StbSecFigureBeamSrc): 子要素 StbSecFigureBeam_SRC(ＳＲＣ梁断面形状)
        stb_sec_bar_arrangement_beam_src (StbSecBarArrangementBeamSrc): 子要素 StbSecBarArrangementBeam_SRC(ＳＲＣ梁断面配筋)
        stb_sec_steel_figure_beam_src (StbSecSteelFigureBeamSrc): 子要素 StbSecSteelFigureBeam_SRC(ＳＲＣ梁断面鉄骨形状)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_beam": _FI(
            py_type=StbSecBeamSrcKindBeam,
            data_type=_DT.STR_ENUM,
            choices=("GIRDER", "BEAM"),
        ),
        "is_foundation": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isFoundation"),
        "is_canti": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isCanti"),
        "is_outin": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOutin"),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_beam_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFigureBeamSrc
        ),
        "stb_sec_bar_arrangement_beam_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementBeamSrc
        ),
        "stb_sec_steel_figure_beam_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelFigureBeamSrc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_SRC"


class StbSecSteelBeamSFiveTypes(StBridgeElement):
    """StbSecSteelBeamSFiveTypes：StbSecSteelBeam_S_FiveTypes

    Attributes:
        pos (StbSecSteelBeamSFiveTypesPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSFiveTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END", "HAUNCH_S", "HAUNCH_E"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_S_FiveTypes"


class StbSecSteelBeamSHaunch(StBridgeElement):
    """StbSecSteelBeamSHaunch：StbSecSteelBeam_S_Haunch

    Attributes:
        pos (StbSecSteelBeamSHaunchPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSHaunchPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_S_Haunch"


class StbSecSteelBeamSJoint(StBridgeElement):
    """StbSecSteelBeamSJoint：StbSecSteelBeam_S_Joint

    Attributes:
        pos (StbSecSteelBeamSJointPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSJointPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_S_Joint"


class StbSecSteelBeamSTaper(StBridgeElement):
    """StbSecSteelBeamSTaper：StbSecSteelBeam_S_Taper

    Attributes:
        pos (StbSecSteelBeamSTaperPos): 属性
        pos_name (str): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamSTaperPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_S_Taper"


class StbSecSteelBeamSStraight(StBridgeElement):
    """StbSecSteelBeamSStraight：StbSecSteelBeam_S_Straight

    Attributes:
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_S_Straight"


class StbSecSteelFigureBeamS(StBridgeElement):
    """Ｓ梁断面鉄骨形状：StbSecSteelFigureBeam_S

    Attributes:
        joint_id_start (int): 属性
        joint_id_end (int): 属性
        stb_sec_steel_beam_s_straight (StbSecSteelBeamSStraight): 子要素
        stb_sec_steel_beam_s_taper (list[StbSecSteelBeamSTaper]): 子要素
        stb_sec_steel_beam_s_joint (list[StbSecSteelBeamSJoint]): 子要素
        stb_sec_steel_beam_s_haunch (list[StbSecSteelBeamSHaunch]): 子要素
        stb_sec_steel_beam_s_five_types (list[StbSecSteelBeamSFiveTypes]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "joint_id_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_sec_steel_beam_s_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelBeamSStraight
        ),
        "stb_sec_steel_beam_s_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSteelBeamSTaper]
        ),
        "stb_sec_steel_beam_s_joint": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelBeamSJoint]
        ),
        "stb_sec_steel_beam_s_haunch": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelBeamSHaunch]
        ),
        "stb_sec_steel_beam_s_five_types": _FI(
            kind=_FK.ELEMENT, max_occurs=5, py_type=list[StbSecSteelBeamSFiveTypes]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelFigureBeam_S"


class StbSecBeamS(StBridgeElement):
    """Ｓ梁断面：StbSecBeam_S

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_beam (StbSecBeamSKindBeam): 属性 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）
        is_canti (bool): 属性 片持ち梁か否か
        is_outin (bool): 属性 外端・内端指定
        stb_sec_steel_figure_beam_s (StbSecSteelFigureBeamS): 子要素 StbSecSteelFigureBeam_S(Ｓ梁断面鉄骨形状)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_beam": _FI(
            py_type=StbSecBeamSKindBeam,
            data_type=_DT.STR_ENUM,
            choices=("GIRDER", "BEAM"),
        ),
        "is_canti": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isCanti"),
        "is_outin": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOutin"),
        "stb_sec_steel_figure_beam_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecSteelFigureBeamS
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_S"


class StbSecBarBeamXReinforced(StBridgeElement):
    """コンクリート梁 Ｘ形配筋：StbSecBarBeamXReinforced

    Attributes:
        n_main_top (int): 属性 主筋：上端1段目
        n_main_bottom (int): 属性 主筋：下端1段目
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "n_main_top": _FI(
            py_type=int,
            data_type=_DT.NON_NEGATIVE_INTEGER,
            xml_type="nonNegativeInteger",
            required=True,
            xml_name="N_main_top",
        ),
        "n_main_bottom": _FI(
            py_type=int,
            data_type=_DT.NON_NEGATIVE_INTEGER,
            xml_type="nonNegativeInteger",
            required=True,
            xml_name="N_main_bottom",
        ),
    }


class StbSecBarBeamRcStartEnd(StBridgeElement):
    """StbSecBarBeamRcStartEnd：StbSecBarBeam_RC_StartEnd

    Attributes:
        pos (StbSecBarBeamRcStartEndPos): 属性
        pos_name (str): 属性
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_stirrup (str): 属性
        d_web (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_stirrup (str): 属性
        strength_web (str): 属性
        strength_bar_spacing (str): 属性
        n_main_top_1st (int): 属性
        n_main_top_2nd (int): 属性
        n_main_top_3rd (int): 属性
        n_main_bottom_1st (int): 属性
        n_main_bottom_2nd (int): 属性
        n_main_bottom_3rd (int): 属性
        n_2nd_main_top_1st (int): 属性
        n_2nd_main_top_2nd (int): 属性
        n_2nd_main_top_3rd (int): 属性
        n_2nd_main_bottom_1st (int): 属性
        n_2nd_main_bottom_2nd (int): 属性
        n_2nd_main_bottom_3rd (int): 属性
        n_stirrup (int): 属性
        pitch_stirrup (float): 属性
        n_web (int): 属性
        n_bar_spacing (int): 属性
        pitch_bar_spacing (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarBeamRcStartEndPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_stirrup": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_stirrup"
        ),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_top_1st",
        ),
        "n_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_2nd",
        ),
        "n_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_3rd",
        ),
        "n_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_bottom_1st",
        ),
        "n_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_2nd",
        ),
        "n_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_3rd",
        ),
        "n_2nd_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_1st",
        ),
        "n_2nd_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_2nd",
        ),
        "n_2nd_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_3rd",
        ),
        "n_2nd_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_1st",
        ),
        "n_2nd_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_2nd",
        ),
        "n_2nd_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_3rd",
        ),
        "n_stirrup": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_stirrup",
        ),
        "pitch_stirrup": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarBeam_RC_StartEnd"


class StbSecBarBeamRcThreeTypes(StBridgeElement):
    """StbSecBarBeamRcThreeTypes：StbSecBarBeam_RC_ThreeTypes

    Attributes:
        pos (StbSecBarBeamRcThreeTypesPos): 属性
        pos_name (str): 属性
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_stirrup (str): 属性
        d_web (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_stirrup (str): 属性
        strength_web (str): 属性
        strength_bar_spacing (str): 属性
        n_main_top_1st (int): 属性
        n_main_top_2nd (int): 属性
        n_main_top_3rd (int): 属性
        n_main_bottom_1st (int): 属性
        n_main_bottom_2nd (int): 属性
        n_main_bottom_3rd (int): 属性
        n_2nd_main_top_1st (int): 属性
        n_2nd_main_top_2nd (int): 属性
        n_2nd_main_top_3rd (int): 属性
        n_2nd_main_bottom_1st (int): 属性
        n_2nd_main_bottom_2nd (int): 属性
        n_2nd_main_bottom_3rd (int): 属性
        n_stirrup (int): 属性
        pitch_stirrup (float): 属性
        n_web (int): 属性
        n_bar_spacing (int): 属性
        pitch_bar_spacing (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarBeamRcThreeTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "pos_name": _FI(py_type=str, data_type=_DT.STR),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_stirrup": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_stirrup"
        ),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_top_1st",
        ),
        "n_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_2nd",
        ),
        "n_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_3rd",
        ),
        "n_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_bottom_1st",
        ),
        "n_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_2nd",
        ),
        "n_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_3rd",
        ),
        "n_2nd_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_1st",
        ),
        "n_2nd_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_2nd",
        ),
        "n_2nd_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_3rd",
        ),
        "n_2nd_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_1st",
        ),
        "n_2nd_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_2nd",
        ),
        "n_2nd_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_3rd",
        ),
        "n_stirrup": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_stirrup",
        ),
        "pitch_stirrup": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarBeam_RC_ThreeTypes"


class StbSecBarBeamRcSame(StBridgeElement):
    """StbSecBarBeamRcSame：StbSecBarBeam_RC_Same

    Attributes:
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_stirrup (str): 属性
        d_web (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_stirrup (str): 属性
        strength_web (str): 属性
        strength_bar_spacing (str): 属性
        n_main_top_1st (int): 属性
        n_main_top_2nd (int): 属性
        n_main_top_3rd (int): 属性
        n_main_bottom_1st (int): 属性
        n_main_bottom_2nd (int): 属性
        n_main_bottom_3rd (int): 属性
        n_2nd_main_top_1st (int): 属性
        n_2nd_main_top_2nd (int): 属性
        n_2nd_main_top_3rd (int): 属性
        n_2nd_main_bottom_1st (int): 属性
        n_2nd_main_bottom_2nd (int): 属性
        n_2nd_main_bottom_3rd (int): 属性
        n_stirrup (int): 属性
        pitch_stirrup (float): 属性
        n_web (int): 属性
        n_bar_spacing (int): 属性
        pitch_bar_spacing (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_stirrup": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_stirrup"
        ),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_top_1st",
        ),
        "n_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_2nd",
        ),
        "n_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_top_3rd",
        ),
        "n_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_bottom_1st",
        ),
        "n_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_2nd",
        ),
        "n_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_bottom_3rd",
        ),
        "n_2nd_main_top_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_1st",
        ),
        "n_2nd_main_top_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_2nd",
        ),
        "n_2nd_main_top_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_top_3rd",
        ),
        "n_2nd_main_bottom_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_1st",
        ),
        "n_2nd_main_bottom_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_2nd",
        ),
        "n_2nd_main_bottom_3rd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_bottom_3rd",
        ),
        "n_stirrup": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_stirrup",
        ),
        "pitch_stirrup": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarBeam_RC_Same"


class StbSecBarArrangementBeamRc(StBridgeElement):
    """ＲＣ梁断面配筋：StbSecBarArrangementBeam_RC

    Attributes:
        depth_cover_left (float): 属性
        depth_cover_right (float): 属性
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        interval (float): 属性
        center_top (float): 属性
        center_bottom (float): 属性
        center_side (float): 属性
        center_interval (float): 属性
        length_bar_start (float): 属性
        length_bar_end (float): 属性
        stb_sec_bar_beam_rc_same (StbSecBarBeamRcSame): 子要素
        stb_sec_bar_beam_rc_three_types (list[StbSecBarBeamRcThreeTypes]): 子要素
        stb_sec_bar_beam_rc_start_end (list[StbSecBarBeamRcStartEnd]): 子要素
        stb_sec_bar_beam_x_reinforced (StbSecBarBeamXReinforced): 子要素 StbSecBarBeamXReinforced(コンクリート梁 Ｘ形配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_left": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_right": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_bottom": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_side": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_bar_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_bar_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_bar_beam_rc_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarBeamRcSame
        ),
        "stb_sec_bar_beam_rc_three_types": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBarBeamRcThreeTypes]
        ),
        "stb_sec_bar_beam_rc_start_end": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarBeamRcStartEnd]
        ),
        "stb_sec_bar_beam_x_reinforced": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarBeamXReinforced
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementBeam_RC"


class StbSecBeamRcHaunch(StBridgeElement):
    """StbSecBeamRcHaunch：StbSecBeam_RC_Haunch

    Attributes:
        pos (StbSecBeamRcHaunchPos): 属性
        width (float): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBeamRcHaunchPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "CENTER", "END"),
        ),
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_RC_Haunch"


class StbSecBeamRcTaper(StBridgeElement):
    """StbSecBeamRcTaper：StbSecBeam_RC_Taper

    Attributes:
        pos (StbSecBeamRcTaperPos): 属性
        width (float): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBeamRcTaperPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_RC_Taper"


class StbSecBeamRcStraight(StBridgeElement):
    """StbSecBeamRcStraight：StbSecBeam_RC_Straight

    Attributes:
        width (float): 属性
        depth (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_RC_Straight"


class StbSecFigureBeamRc(StBridgeElement):
    """ＲＣ梁断面形状：StbSecFigureBeam_RC

    Attributes:
        stb_sec_beam_rc_straight (StbSecBeamRcStraight): 子要素
        stb_sec_beam_rc_taper (list[StbSecBeamRcTaper]): 子要素
        stb_sec_beam_rc_haunch (list[StbSecBeamRcHaunch]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_beam_rc_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBeamRcStraight
        ),
        "stb_sec_beam_rc_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBeamRcTaper]
        ),
        "stb_sec_beam_rc_haunch": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBeamRcHaunch]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureBeam_RC"


class StbSecBeamRc(StBridgeElement):
    """ＲＣ梁断面：StbSecBeam_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_beam (StbSecBeamRcKindBeam): 属性 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）
        is_foundation (bool): 属性 基礎梁か否か
        is_canti (bool): 属性 片持ち梁か否か
        is_outin (bool): 属性 外端・内端指定
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_beam_rc (StbSecFigureBeamRc): 子要素 StbSecFigureBeam_RC(ＲＣ梁断面形状)
        stb_sec_bar_arrangement_beam_rc (StbSecBarArrangementBeamRc): 子要素 StbSecBarArrangementBeam_RC(ＲＣ梁断面配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_beam": _FI(
            py_type=StbSecBeamRcKindBeam,
            data_type=_DT.STR_ENUM,
            choices=("GIRDER", "BEAM"),
        ),
        "is_foundation": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isFoundation"),
        "is_canti": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isCanti"),
        "is_outin": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOutin"),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_beam_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFigureBeamRc
        ),
        "stb_sec_bar_arrangement_beam_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementBeamRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_RC"


class StbSecBaseConventionalCftRibPlate(StBridgeElement):
    """StbSecBaseConventionalCftRibPlate：StbSecBaseConventional_CFT_RibPlate

    Attributes:
        a1 (float): 属性
        a2 (float): 属性
        b1 (float): 属性
        b2 (float): 属性
        t (float): 属性
        strength (str): 属性
        n_x (int): 属性
        n_y (int): 属性
        length_e_x (float): 属性
        length_e_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "a1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A1",
        ),
        "a2": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="A2",
        ),
        "b1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B1",
        ),
        "b2": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="B2",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
        "length_e_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_e_X",
        ),
        "length_e_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_e_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_CFT_RibPlate"


class StbSecBaseConventionalCftAnchorBolt(StBridgeElement):
    """StbSecBaseConventionalCftAnchorBolt：StbSecBaseConventional_CFT_AnchorBolt

    Attributes:
        kind_bolt (StbSecBaseConventionalCftAnchorBoltKindBolt): 属性
        name_bolt (str): 属性
        length_bolt (float): 属性
        strength_bolt (str): 属性
        arrangement_bolt (StbSecBaseConventionalCftAnchorBoltArrangementBolt): 属性
        d1_x (float): 属性
        d2_x (float): 属性
        d1_y (float): 属性
        d2_y (float): 属性
        n_x (int): 属性
        n_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "kind_bolt": _FI(
            py_type=StbSecBaseConventionalCftAnchorBoltKindBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STD", "ABR", "ABM"),
        ),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "length_bolt": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "arrangement_bolt": _FI(
            py_type=StbSecBaseConventionalCftAnchorBoltArrangementBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STD", "CUT"),
        ),
        "d1_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1_X",
        ),
        "d2_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2_X",
        ),
        "d1_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1_Y",
        ),
        "d2_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2_Y",
        ),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_CFT_AnchorBolt"


class StbSecBaseConventionalCftPlate(StBridgeElement):
    """StbSecBaseConventionalCftPlate：StbSecBaseConventional_CFT_Plate

    Attributes:
        b_x (float): 属性
        b_y (float): 属性
        c1_x (float): 属性
        c1_y (float): 属性
        c2_x (float): 属性
        c2_y (float): 属性
        c3_x (float): 属性
        c3_y (float): 属性
        c4_x (float): 属性
        c4_y (float): 属性
        t (float): 属性
        strength (str): 属性
        d_bolthole (float): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "b_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_X",
        ),
        "b_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_Y",
        ),
        "c1_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C1_X",
        ),
        "c1_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C1_Y",
        ),
        "c2_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C2_X",
        ),
        "c2_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C2_Y",
        ),
        "c3_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C3_X",
        ),
        "c3_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C3_Y",
        ),
        "c4_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C4_X",
        ),
        "c4_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C4_Y",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "d_bolthole": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_bolthole",
        ),
        "offset_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_X",
        ),
        "offset_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_CFT_Plate"


class StbSecBaseConventionalCft(StBridgeElement):
    """StbSecBaseConventionalCft：StbSecBaseConventional_CFT

    Attributes:
        height_mortar (float): 属性
        stb_sec_base_conventional_cft_plate (StbSecBaseConventionalCftPlate): 子要素
        stb_sec_base_conventional_cft_anchor_bolt (StbSecBaseConventionalCftAnchorBolt): 子要素
        stb_sec_base_conventional_cft_rib_plate (StbSecBaseConventionalCftRibPlate): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
        "stb_sec_base_conventional_cft_plate": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalCftPlate,
        ),
        "stb_sec_base_conventional_cft_anchor_bolt": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalCftAnchorBolt,
        ),
        "stb_sec_base_conventional_cft_rib_plate": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseConventionalCftRibPlate
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_CFT"


class StbSecBaseProductCft(StBridgeElement):
    """StbSecBaseProductCft：StbSecBaseProduct_CFT

    Attributes:
        product_company (str): 属性
        product_code (str): 属性
        direction_type (StbSecBaseProductCftDirectionType): 属性
        height_mortar (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "direction_type": _FI(
            py_type=StbSecBaseProductCftDirectionType,
            data_type=_DT.INT_ENUM,
            xml_type="nonNegativeInteger",
            choices=("0", "90", "180", "270"),
        ),
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseProduct_CFT"


class StbSecSteelColumnCftThreeTypes(StBridgeElement):
    """ＣＦＴ柱断面鉄骨形状・３種類：StbSecSteelColumn_CFT_ThreeTypes

    Attributes:
        pos (StbSecSteelColumnCftThreeTypesPos): 属性 配置位置以下のいずれかBOTTOM（柱脚）CENTER（中央）TOP（柱頭）
        shape (str): 属性 鉄骨形状
        strength (str): 属性 鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnCftThreeTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "CENTER", "TOP"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_CFT_ThreeTypes"


class StbSecSteelColumnCftNotSame(StBridgeElement):
    """ＣＦＴ柱断面鉄骨形状・柱頭脚別：StbSecSteelColumn_CFT_NotSame

    Attributes:
        pos (StbSecSteelColumnCftNotSamePos): 属性 配置位置以下のいずれかBOTTOM（柱脚）TOP（柱頭）
        shape (str): 属性 鉄骨形状
        strength (str): 属性 鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnCftNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_CFT_NotSame"


class StbSecSteelColumnCftSame(StBridgeElement):
    """ＣＦＴ柱断面鉄骨形状・同一：StbSecSteelColumn_CFT_Same

    Attributes:
        shape (str): 属性 鉄骨形状
        strength (str): 属性 鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_CFT_Same"


class StbSecSteelFigureColumnCft(StBridgeElement):
    """ＣＦＴ柱断面鉄骨形状：StbSecSteelFigureColumn_CFT

    Attributes:
        base_type (StbSecSteelFigureColumnCftBaseType): 属性 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）EXPOSE（露出）EMBEDDED（埋込）
        stb_sec_steel_column_cft_same (StbSecSteelColumnCftSame): 子要素 StbSecSteelColumn_CFT_Same(ＣＦＴ柱断面鉄骨形状・同一)
        stb_sec_steel_column_cft_not_same (list[StbSecSteelColumnCftNotSame]): 子要素 StbSecSteelColumn_CFT_NotSame(ＣＦＴ柱断面鉄骨形状・柱頭脚別)
        stb_sec_steel_column_cft_three_types (list[StbSecSteelColumnCftThreeTypes]): 子要素 StbSecSteelColumn_CFT_ThreeTypes(ＣＦＴ柱断面鉄骨形状・３種類)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "base_type": _FI(
            py_type=StbSecSteelFigureColumnCftBaseType,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "EXPOSE", "EMBEDDED"),
        ),
        "stb_sec_steel_column_cft_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnCftSame
        ),
        "stb_sec_steel_column_cft_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSteelColumnCftNotSame]
        ),
        "stb_sec_steel_column_cft_three_types": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelColumnCftThreeTypes]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelFigureColumn_CFT"


class StbSecColumnCft(StBridgeElement):
    """ＣＦＴ柱断面：StbSecColumn_CFT

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_column (StbSecColumnCftKindColumn): 属性 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）
        strength_concrete (str): 属性 コンクリート強度
        is_reference_direction (bool): 属性 鉄骨向き
        stb_sec_steel_figure_column_cft (StbSecSteelFigureColumnCft): 子要素 StbSecSteelFigureColumn_CFT(ＣＦＴ柱断面鉄骨形状)
        stb_sec_base_product_cft (StbSecBaseProductCft): 子要素
        stb_sec_base_conventional_cft (StbSecBaseConventionalCft): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_column": _FI(
            py_type=StbSecColumnCftKindColumn,
            data_type=_DT.STR_ENUM,
            choices=("COLUMN", "POST"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "is_reference_direction": _FI(
            py_type=bool, data_type=_DT.BOOL, xml_name="isReferenceDirection"
        ),
        "stb_sec_steel_figure_column_cft": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecSteelFigureColumnCft,
        ),
        "stb_sec_base_product_cft": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseProductCft
        ),
        "stb_sec_base_conventional_cft": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseConventionalCft
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_CFT"


class StbSecBaseConventionalSrcRibPlate(StBridgeElement):
    """StbSecBaseConventionalSrcRibPlate：StbSecBaseConventional_SRC_RibPlate

    Attributes:
        a1 (float): 属性
        a2 (float): 属性
        b1 (float): 属性
        b2 (float): 属性
        t (float): 属性
        strength (str): 属性
        n_x (int): 属性
        n_y (int): 属性
        length_e_x (float): 属性
        length_e_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "a1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A1",
        ),
        "a2": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="A2",
        ),
        "b1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B1",
        ),
        "b2": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="B2",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
        "length_e_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_e_X",
        ),
        "length_e_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_e_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_SRC_RibPlate"


class StbSecBaseConventionalSrcAnchorBolt(StBridgeElement):
    """StbSecBaseConventionalSrcAnchorBolt：StbSecBaseConventional_SRC_AnchorBolt

    Attributes:
        kind_bolt (StbSecBaseConventionalSrcAnchorBoltKindBolt): 属性
        name_bolt (str): 属性
        length_bolt (float): 属性
        strength_bolt (str): 属性
        arrangement_bolt (StbSecBaseConventionalSrcAnchorBoltArrangementBolt): 属性
        d1_x (float): 属性
        d2_x (float): 属性
        d1_y (float): 属性
        d2_y (float): 属性
        n_x (int): 属性
        n_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "kind_bolt": _FI(
            py_type=StbSecBaseConventionalSrcAnchorBoltKindBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STD", "ABR", "ABM"),
        ),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "length_bolt": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "arrangement_bolt": _FI(
            py_type=StbSecBaseConventionalSrcAnchorBoltArrangementBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STD", "CUT"),
        ),
        "d1_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1_X",
        ),
        "d2_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2_X",
        ),
        "d1_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1_Y",
        ),
        "d2_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2_Y",
        ),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_SRC_AnchorBolt"


class StbSecBaseConventionalSrcPlate(StBridgeElement):
    """StbSecBaseConventionalSrcPlate：StbSecBaseConventional_SRC_Plate

    Attributes:
        b_x (float): 属性
        b_y (float): 属性
        c1_x (float): 属性
        c1_y (float): 属性
        c2_x (float): 属性
        c2_y (float): 属性
        c3_x (float): 属性
        c3_y (float): 属性
        c4_x (float): 属性
        c4_y (float): 属性
        t (float): 属性
        strength (str): 属性
        d_bolthole (float): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "b_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_X",
        ),
        "b_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_Y",
        ),
        "c1_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C1_X",
        ),
        "c1_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C1_Y",
        ),
        "c2_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C2_X",
        ),
        "c2_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C2_Y",
        ),
        "c3_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C3_X",
        ),
        "c3_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C3_Y",
        ),
        "c4_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C4_X",
        ),
        "c4_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C4_Y",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "d_bolthole": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_bolthole",
        ),
        "offset_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_X",
        ),
        "offset_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_SRC_Plate"


class StbSecBaseConventionalSrc(StBridgeElement):
    """StbSecBaseConventionalSrc：StbSecBaseConventional_SRC

    Attributes:
        height_mortar (float): 属性
        stb_sec_base_conventional_src_plate (StbSecBaseConventionalSrcPlate): 子要素
        stb_sec_base_conventional_src_anchor_bolt (StbSecBaseConventionalSrcAnchorBolt): 子要素
        stb_sec_base_conventional_src_rib_plate (StbSecBaseConventionalSrcRibPlate): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
        "stb_sec_base_conventional_src_plate": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalSrcPlate,
        ),
        "stb_sec_base_conventional_src_anchor_bolt": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalSrcAnchorBolt,
        ),
        "stb_sec_base_conventional_src_rib_plate": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseConventionalSrcRibPlate
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_SRC"


class StbSecBaseProductSrc(StBridgeElement):
    """StbSecBaseProductSrc：StbSecBaseProduct_SRC

    Attributes:
        product_company (str): 属性
        product_code (str): 属性
        direction_type (StbSecBaseProductSrcDirectionType): 属性
        height_mortar (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "direction_type": _FI(
            py_type=StbSecBaseProductSrcDirectionType,
            data_type=_DT.INT_ENUM,
            xml_type="nonNegativeInteger",
            choices=("0", "90", "180", "270"),
        ),
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseProduct_SRC"


class StbSecColumnSrcThreeTypesShapeT(StBridgeElement):
    """StbSecColumnSrcThreeTypesShapeT：StbSecColumn_SRC_ThreeTypesShapeT

    Attributes:
        direction_type (StbSecColumnSrcThreeTypesShapeTDirectionType): 属性
        shape_h (str): 属性
        shape_t (str): 属性
        strength_main_h (str): 属性
        strength_web_h (str): 属性
        strength_main_t (str): 属性
        strength_web_t (str): 属性
        offset_hx (float): 属性
        offset_hy (float): 属性
        offset_t (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecColumnSrcThreeTypesShapeTDirectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("T1", "T2", "T3", "T4"),
        ),
        "shape_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_H"
        ),
        "shape_t": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_T"
        ),
        "strength_main_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_H"
        ),
        "strength_web_h": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_H"
        ),
        "strength_main_t": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_T"
        ),
        "strength_web_t": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_T"
        ),
        "offset_hx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HX"),
        "offset_hy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HY"),
        "offset_t": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_T"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_ThreeTypesShapeT"


class StbSecColumnSrcThreeTypesShapeCross(StBridgeElement):
    """StbSecColumnSrcThreeTypesShapeCross：StbSecColumn_SRC_ThreeTypesShapeCross

    Attributes:
        shape_x (str): 属性
        shape_y (str): 属性
        strength_main_x (str): 属性
        strength_web_x (str): 属性
        strength_main_y (str): 属性
        strength_web_y (str): 属性
        offset_xx (float): 属性
        offset_xy (float): 属性
        offset_yx (float): 属性
        offset_yy (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape_x": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_X"
        ),
        "shape_y": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_Y"
        ),
        "strength_main_x": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_X"
        ),
        "strength_web_x": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_X"
        ),
        "strength_main_y": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_main_Y"
        ),
        "strength_web_y": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_Y"
        ),
        "offset_xx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_XX"),
        "offset_xy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_XY"),
        "offset_yx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_YX"),
        "offset_yy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_YY"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_ThreeTypesShapeCross"


class StbSecColumnSrcThreeTypesShapePipe(StBridgeElement):
    """StbSecColumnSrcThreeTypesShapePipe：StbSecColumn_SRC_ThreeTypesShapePipe

    Attributes:
        shape (str): 属性
        encase_type (StbSecColumnSrcThreeTypesShapePipeEncaseType): 属性
        strength (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecColumnSrcThreeTypesShapePipeEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_ThreeTypesShapePipe"


class StbSecColumnSrcThreeTypesShapeBox(StBridgeElement):
    """StbSecColumnSrcThreeTypesShapeBox：StbSecColumn_SRC_ThreeTypesShapeBox

    Attributes:
        shape (str): 属性
        encase_type (StbSecColumnSrcThreeTypesShapeBoxEncaseType): 属性
        strength (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecColumnSrcThreeTypesShapeBoxEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_ThreeTypesShapeBox"


class StbSecColumnSrcThreeTypesShapeH(StBridgeElement):
    """StbSecColumnSrcThreeTypesShapeH：StbSecColumn_SRC_ThreeTypesShapeH

    Attributes:
        direction_type (StbSecColumnSrcThreeTypesShapeHDirectionType): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecColumnSrcThreeTypesShapeHDirectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("H", "I"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_ThreeTypesShapeH"


class StbSecSteelColumnSrcThreeTypes(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・３種類：StbSecSteelColumn_SRC_ThreeTypes

    Attributes:
        pos (StbSecSteelColumnSrcThreeTypesPos): 属性 配置位置 以下のいずれかBOTTOM（柱脚） CENTER（中央）TOP（柱頭）
        stb_sec_column_src_three_types_shape_h (StbSecColumnSrcThreeTypesShapeH): 子要素
        stb_sec_column_src_three_types_shape_box (StbSecColumnSrcThreeTypesShapeBox): 子要素
        stb_sec_column_src_three_types_shape_pipe (StbSecColumnSrcThreeTypesShapePipe): 子要素
        stb_sec_column_src_three_types_shape_cross (StbSecColumnSrcThreeTypesShapeCross): 子要素
        stb_sec_column_src_three_types_shape_t (StbSecColumnSrcThreeTypesShapeT): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnSrcThreeTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "CENTER", "TOP"),
        ),
        "stb_sec_column_src_three_types_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcThreeTypesShapeH
        ),
        "stb_sec_column_src_three_types_shape_box": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcThreeTypesShapeBox
        ),
        "stb_sec_column_src_three_types_shape_pipe": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcThreeTypesShapePipe
        ),
        "stb_sec_column_src_three_types_shape_cross": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcThreeTypesShapeCross
        ),
        "stb_sec_column_src_three_types_shape_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcThreeTypesShapeT
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ThreeTypes"


class StbSecColumnSrcNotSameShapeT(StBridgeElement):
    """StbSecColumnSrcNotSameShapeT：StbSecColumn_SRC_NotSameShapeT

    Attributes:
        direction_type (StbSecColumnSrcNotSameShapeTDirectionType): 属性
        shape_h (str): 属性
        shape_t (str): 属性
        strength_main_h (str): 属性
        strength_web_h (str): 属性
        strength_main_t (str): 属性
        strength_web_t (str): 属性
        offset_hx (float): 属性
        offset_hy (float): 属性
        offset_t (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecColumnSrcNotSameShapeTDirectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("T1", "T2", "T3", "T4"),
        ),
        "shape_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_H"
        ),
        "shape_t": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_T"
        ),
        "strength_main_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_H"
        ),
        "strength_web_h": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_H"
        ),
        "strength_main_t": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_T"
        ),
        "strength_web_t": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_T"
        ),
        "offset_hx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HX"),
        "offset_hy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HY"),
        "offset_t": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_T"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_NotSameShapeT"


class StbSecColumnSrcNotSameShapeCross(StBridgeElement):
    """StbSecColumnSrcNotSameShapeCross：StbSecColumn_SRC_NotSameShapeCross

    Attributes:
        shape_x (str): 属性
        shape_y (str): 属性
        strength_main_x (str): 属性
        strength_web_x (str): 属性
        strength_main_y (str): 属性
        strength_web_y (str): 属性
        offset_xx (float): 属性
        offset_xy (float): 属性
        offset_yx (float): 属性
        offset_yy (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape_x": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_X"
        ),
        "shape_y": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_Y"
        ),
        "strength_main_x": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_X"
        ),
        "strength_web_x": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_X"
        ),
        "strength_main_y": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_main_Y"
        ),
        "strength_web_y": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_Y"
        ),
        "offset_xx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_XX"),
        "offset_xy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_XY"),
        "offset_yx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_YX"),
        "offset_yy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_YY"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_NotSameShapeCross"


class StbSecColumnSrcNotSameShapePipe(StBridgeElement):
    """StbSecColumnSrcNotSameShapePipe：StbSecColumn_SRC_NotSameShapePipe

    Attributes:
        shape (str): 属性
        encase_type (StbSecColumnSrcNotSameShapePipeEncaseType): 属性
        strength (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecColumnSrcNotSameShapePipeEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_NotSameShapePipe"


class StbSecColumnSrcNotSameShapeBox(StBridgeElement):
    """StbSecColumnSrcNotSameShapeBox：StbSecColumn_SRC_NotSameShapeBox

    Attributes:
        shape (str): 属性
        encase_type (StbSecColumnSrcNotSameShapeBoxEncaseType): 属性
        strength (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecColumnSrcNotSameShapeBoxEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_NotSameShapeBox"


class StbSecColumnSrcNotSameShapeH(StBridgeElement):
    """StbSecColumnSrcNotSameShapeH：StbSecColumn_SRC_NotSameShapeH

    Attributes:
        direction_type (StbSecColumnSrcNotSameShapeHDirectionType): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecColumnSrcNotSameShapeHDirectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("H", "I"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_NotSameShapeH"


class StbSecSteelColumnSrcNotSame(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・柱頭脚別：StbSecSteelColumn_SRC_NotSame

    Attributes:
        pos (StbSecSteelColumnSrcNotSamePos): 属性 配置位置 以下のいずれかBOTTOM（柱脚）TOP（柱頭）
        stb_sec_column_src_not_same_shape_h (StbSecColumnSrcNotSameShapeH): 子要素
        stb_sec_column_src_not_same_shape_box (StbSecColumnSrcNotSameShapeBox): 子要素
        stb_sec_column_src_not_same_shape_pipe (StbSecColumnSrcNotSameShapePipe): 子要素
        stb_sec_column_src_not_same_shape_cross (StbSecColumnSrcNotSameShapeCross): 子要素
        stb_sec_column_src_not_same_shape_t (StbSecColumnSrcNotSameShapeT): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnSrcNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "stb_sec_column_src_not_same_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcNotSameShapeH
        ),
        "stb_sec_column_src_not_same_shape_box": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcNotSameShapeBox
        ),
        "stb_sec_column_src_not_same_shape_pipe": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcNotSameShapePipe
        ),
        "stb_sec_column_src_not_same_shape_cross": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcNotSameShapeCross
        ),
        "stb_sec_column_src_not_same_shape_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcNotSameShapeT
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_NotSame"


class StbSecColumnSrcSameShapeT(StBridgeElement):
    """StbSecColumnSrcSameShapeT：StbSecColumn_SRC_SameShapeT

    Attributes:
        direction_type (StbSecColumnSrcSameShapeTDirectionType): 属性
        shape_h (str): 属性
        shape_t (str): 属性
        strength_main_h (str): 属性
        strength_web_h (str): 属性
        strength_main_t (str): 属性
        strength_web_t (str): 属性
        offset_hx (float): 属性
        offset_hy (float): 属性
        offset_t (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecColumnSrcSameShapeTDirectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("T1", "T2", "T3", "T4"),
        ),
        "shape_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_H"
        ),
        "shape_t": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_T"
        ),
        "strength_main_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_H"
        ),
        "strength_web_h": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_H"
        ),
        "strength_main_t": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_T"
        ),
        "strength_web_t": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_T"
        ),
        "offset_hx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HX"),
        "offset_hy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HY"),
        "offset_t": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_T"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_SameShapeT"


class StbSecColumnSrcSameShapeCross(StBridgeElement):
    """StbSecColumnSrcSameShapeCross：StbSecColumn_SRC_SameShapeCross

    Attributes:
        shape_x (str): 属性
        shape_y (str): 属性
        strength_main_x (str): 属性
        strength_web_x (str): 属性
        strength_main_y (str): 属性
        strength_web_y (str): 属性
        offset_xx (float): 属性
        offset_xy (float): 属性
        offset_yx (float): 属性
        offset_yy (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape_x": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_X"
        ),
        "shape_y": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_Y"
        ),
        "strength_main_x": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_X"
        ),
        "strength_web_x": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_X"
        ),
        "strength_main_y": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_main_Y"
        ),
        "strength_web_y": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_Y"
        ),
        "offset_xx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_XX"),
        "offset_xy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_XY"),
        "offset_yx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_YX"),
        "offset_yy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_YY"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_SameShapeCross"


class StbSecColumnSrcSameShapePipe(StBridgeElement):
    """StbSecColumnSrcSameShapePipe：StbSecColumn_SRC_SameShapePipe

    Attributes:
        shape (str): 属性
        encase_type (StbSecColumnSrcSameShapePipeEncaseType): 属性
        strength (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecColumnSrcSameShapePipeEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_SameShapePipe"


class StbSecColumnSrcSameShapeBox(StBridgeElement):
    """StbSecColumnSrcSameShapeBox：StbSecColumn_SRC_SameShapeBox

    Attributes:
        shape (str): 属性
        encase_type (StbSecColumnSrcSameShapeBoxEncaseType): 属性
        strength (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecColumnSrcSameShapeBoxEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_SameShapeBox"


class StbSecColumnSrcSameShapeH(StBridgeElement):
    """StbSecColumnSrcSameShapeH：StbSecColumn_SRC_SameShapeH

    Attributes:
        direction_type (StbSecColumnSrcSameShapeHDirectionType): 属性
        shape (str): 属性
        strength_main (str): 属性
        strength_web (str): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecColumnSrcSameShapeHDirectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("H", "I"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_SameShapeH"


class StbSecSteelColumnSrcSame(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・同一：StbSecSteelColumn_SRC_Same

    Attributes:
        stb_sec_column_src_same_shape_h (StbSecColumnSrcSameShapeH): 子要素
        stb_sec_column_src_same_shape_box (StbSecColumnSrcSameShapeBox): 子要素
        stb_sec_column_src_same_shape_pipe (StbSecColumnSrcSameShapePipe): 子要素
        stb_sec_column_src_same_shape_cross (StbSecColumnSrcSameShapeCross): 子要素
        stb_sec_column_src_same_shape_t (StbSecColumnSrcSameShapeT): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_column_src_same_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcSameShapeH
        ),
        "stb_sec_column_src_same_shape_box": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcSameShapeBox
        ),
        "stb_sec_column_src_same_shape_pipe": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcSameShapePipe
        ),
        "stb_sec_column_src_same_shape_cross": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcSameShapeCross
        ),
        "stb_sec_column_src_same_shape_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcSameShapeT
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_Same"


class StbSecSteelFigureColumnSrc(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状：StbSecSteelFigureColumn_SRC

    Attributes:
        base_type (StbSecSteelFigureColumnSrcBaseType): 属性 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）UNEMBEDDED（非埋込）UNEMBEDDED2（非埋込）EMBEDDED（埋込）
        joint_id_top (int): 属性
        joint_id_bottom (int): 属性
        length_embedded (float): 属性 柱脚埋め込み長さ
        stb_sec_steel_column_src_same (StbSecSteelColumnSrcSame): 子要素 StbSecSteelColumn_SRC_Same(ＳＲＣ柱断面鉄骨形状・同一)
        stb_sec_steel_column_src_not_same (list[StbSecSteelColumnSrcNotSame]): 子要素 StbSecSteelColumn_SRC_NotSame(ＳＲＣ柱断面鉄骨形状・柱頭脚別)
        stb_sec_steel_column_src_three_types (list[StbSecSteelColumnSrcThreeTypes]): 子要素 StbSecSteelColumn_SRC_ThreeTypes(ＳＲＣ柱断面鉄骨形状・３種類)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "base_type": _FI(
            py_type=StbSecSteelFigureColumnSrcBaseType,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "UNEMBEDDED", "UNEMBEDDED2", "EMBEDDED"),
        ),
        "joint_id_top": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_bottom": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "length_embedded": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_steel_column_src_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSrcSame
        ),
        "stb_sec_steel_column_src_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSteelColumnSrcNotSame]
        ),
        "stb_sec_steel_column_src_three_types": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelColumnSrcThreeTypes]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelFigureColumn_SRC"


class StbSecBarColumnSrcCircleNotSame(StBridgeElement):
    """StbSecBarColumnSrcCircleNotSame：StbSecBarColumn_SRC_CircleNotSame

    Attributes:
        pos (StbSecBarColumnSrcCircleNotSamePos): 属性
        d_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main (int): 属性
        n_axial (int): 属性
        n_band (int): 属性
        pitch_band (float): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnSrcCircleNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASE", "TOP"),
        ),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "n_band": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_SRC_CircleNotSame"


class StbSecBarColumnSrcCircleSame(StBridgeElement):
    """StbSecBarColumnSrcCircleSame：StbSecBarColumn_SRC_CircleSame

    Attributes:
        d_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main (int): 属性
        n_axial (int): 属性
        n_band (int): 属性
        pitch_band (float): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "n_band": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_SRC_CircleSame"


class StbSecBarColumnSrcRectNotSame(StBridgeElement):
    """StbSecBarColumnSrcRectNotSame：StbSecBarColumn_SRC_RectNotSame

    Attributes:
        pos (StbSecBarColumnSrcRectNotSamePos): 属性
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main_x_1st (int): 属性
        n_main_x_2nd (int): 属性
        n_main_y_1st (int): 属性
        n_main_y_2nd (int): 属性
        n_2nd_main_x_1st (int): 属性
        n_2nd_main_x_2nd (int): 属性
        n_2nd_main_y_1st (int): 属性
        n_2nd_main_y_2nd (int): 属性
        n_main_total (int): 属性
        n_axial (int): 属性
        pitch_band (float): 属性
        n_band_direction_x (int): 属性
        n_band_direction_y (int): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnSrcRectNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASE", "TOP"),
        ),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_X_1st",
        ),
        "n_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_X_2nd",
        ),
        "n_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_Y_1st",
        ),
        "n_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_Y_2nd",
        ),
        "n_2nd_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_1st",
        ),
        "n_2nd_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_2nd",
        ),
        "n_2nd_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_1st",
        ),
        "n_2nd_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_2nd",
        ),
        "n_main_total": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_total",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_band_direction_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_X",
        ),
        "n_band_direction_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_Y",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_SRC_RectNotSame"


class StbSecBarColumnSrcRectSame(StBridgeElement):
    """StbSecBarColumnSrcRectSame：StbSecBarColumn_SRC_RectSame

    Attributes:
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main_x_1st (int): 属性
        n_main_x_2nd (int): 属性
        n_main_y_1st (int): 属性
        n_main_y_2nd (int): 属性
        n_2nd_main_x_1st (int): 属性
        n_2nd_main_x_2nd (int): 属性
        n_2nd_main_y_1st (int): 属性
        n_2nd_main_y_2nd (int): 属性
        n_main_total (int): 属性
        n_axial (int): 属性
        pitch_band (float): 属性
        n_band_direction_x (int): 属性
        n_band_direction_y (int): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_X_1st",
        ),
        "n_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_X_2nd",
        ),
        "n_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_Y_1st",
        ),
        "n_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_Y_2nd",
        ),
        "n_2nd_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_1st",
        ),
        "n_2nd_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_2nd",
        ),
        "n_2nd_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_1st",
        ),
        "n_2nd_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_2nd",
        ),
        "n_main_total": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_total",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_band_direction_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_X",
        ),
        "n_band_direction_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_Y",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_SRC_RectSame"


class StbSecBarArrangementColumnSrc(StBridgeElement):
    """ＳＲＣ柱断面配筋：StbSecBarArrangementColumn_SRC

    Attributes:
        depth_cover_start_x (float): 属性
        depth_cover_end_x (float): 属性
        depth_cover_start_y (float): 属性
        depth_cover_end_y (float): 属性
        interval (float): 属性
        kind_corner (StbSecBarArrangementColumnSrcKindCorner): 属性
        is_spiral (bool): 属性
        center_start_x (float): 属性
        center_end_x (float): 属性
        center_start_y (float): 属性
        center_end_y (float): 属性
        center_interval (float): 属性
        stb_sec_bar_column_src_rect_same (StbSecBarColumnSrcRectSame): 子要素
        stb_sec_bar_column_src_rect_not_same (list[StbSecBarColumnSrcRectNotSame]): 子要素
        stb_sec_bar_column_src_circle_same (StbSecBarColumnSrcCircleSame): 子要素
        stb_sec_bar_column_src_circle_not_same (list[StbSecBarColumnSrcCircleNotSame]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_start_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_start_X",
        ),
        "depth_cover_end_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_end_X",
        ),
        "depth_cover_start_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_start_Y",
        ),
        "depth_cover_end_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_end_Y",
        ),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_corner": _FI(
            py_type=StbSecBarArrangementColumnSrcKindCorner,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "DIR_X", "DIR_Y", "DIR_XY"),
        ),
        "is_spiral": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isSpiral"),
        "center_start_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_X",
        ),
        "center_end_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_X",
        ),
        "center_start_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_Y",
        ),
        "center_end_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_Y",
        ),
        "center_interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_bar_column_src_rect_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnSrcRectSame
        ),
        "stb_sec_bar_column_src_rect_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarColumnSrcRectNotSame]
        ),
        "stb_sec_bar_column_src_circle_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnSrcCircleSame
        ),
        "stb_sec_bar_column_src_circle_not_same": _FI(
            kind=_FK.ELEMENT,
            max_occurs=2,
            py_type=list[StbSecBarColumnSrcCircleNotSame],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementColumn_SRC"


class StbSecColumnSrcCircle(StBridgeElement):
    """StbSecColumnSrcCircle：StbSecColumn_SRC_Circle

    Attributes:
        d (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_Circle"


class StbSecColumnSrcRect(StBridgeElement):
    """StbSecColumnSrcRect：StbSecColumn_SRC_Rect

    Attributes:
        width_x (float): 属性
        width_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_X",
        ),
        "width_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC_Rect"


class StbSecFigureColumnSrc(StBridgeElement):
    """ＳＲＣ柱断面形状：StbSecFigureColumn_SRC

    Attributes:
        stb_sec_column_src_rect (StbSecColumnSrcRect): 子要素
        stb_sec_column_src_circle (StbSecColumnSrcCircle): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_column_src_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcRect
        ),
        "stb_sec_column_src_circle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnSrcCircle
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureColumn_SRC"


class StbSecColumnSrc(StBridgeElement):
    """ＳＲＣ柱断面：StbSecColumn_SRC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_column (StbSecColumnSrcKindColumn): 属性 柱の種別 以下のいずれかCOLUMN（柱）POST（間柱）
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_column_src (StbSecFigureColumnSrc): 子要素 StbSecFigureColumn_SRC(ＳＲＣ柱断面形状)
        stb_sec_bar_arrangement_column_src (StbSecBarArrangementColumnSrc): 子要素 StbSecBarArrangementColumn_SRC(ＳＲＣ柱断面配筋)
        stb_sec_steel_figure_column_src (StbSecSteelFigureColumnSrc): 子要素 StbSecSteelFigureColumn_SRC(ＳＲＣ柱断面鉄骨形状)
        stb_sec_base_product_src (StbSecBaseProductSrc): 子要素
        stb_sec_base_conventional_src (StbSecBaseConventionalSrc): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_column": _FI(
            py_type=StbSecColumnSrcKindColumn,
            data_type=_DT.STR_ENUM,
            choices=("COLUMN", "POST"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_column_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFigureColumnSrc
        ),
        "stb_sec_bar_arrangement_column_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementColumnSrc
        ),
        "stb_sec_steel_figure_column_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelFigureColumnSrc
        ),
        "stb_sec_base_product_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseProductSrc
        ),
        "stb_sec_base_conventional_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseConventionalSrc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC"


class StbSecBaseConventionalSRibPlate(StBridgeElement):
    """StbSecBaseConventionalSRibPlate：StbSecBaseConventional_S_RibPlate

    Attributes:
        a1 (float): 属性
        a2 (float): 属性
        b1 (float): 属性
        b2 (float): 属性
        t (float): 属性
        strength (str): 属性
        n_x (int): 属性
        n_y (int): 属性
        length_e_x (float): 属性
        length_e_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "a1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="A1",
        ),
        "a2": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="A2",
        ),
        "b1": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B1",
        ),
        "b2": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="B2",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
        "length_e_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_e_X",
        ),
        "length_e_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_e_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_S_RibPlate"


class StbSecBaseConventionalSAnchorBolt(StBridgeElement):
    """StbSecBaseConventionalSAnchorBolt：StbSecBaseConventional_S_AnchorBolt

    Attributes:
        kind_bolt (StbSecBaseConventionalSAnchorBoltKindBolt): 属性
        name_bolt (str): 属性
        length_bolt (float): 属性
        strength_bolt (str): 属性
        arrangement_bolt (StbSecBaseConventionalSAnchorBoltArrangementBolt): 属性
        d1_x (float): 属性
        d2_x (float): 属性
        d1_y (float): 属性
        d2_y (float): 属性
        n_x (int): 属性
        n_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "kind_bolt": _FI(
            py_type=StbSecBaseConventionalSAnchorBoltKindBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STD", "ABR", "ABM"),
        ),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "length_bolt": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "arrangement_bolt": _FI(
            py_type=StbSecBaseConventionalSAnchorBoltArrangementBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STD", "CUT"),
        ),
        "d1_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1_X",
        ),
        "d2_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2_X",
        ),
        "d1_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D1_Y",
        ),
        "d2_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D2_Y",
        ),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_S_AnchorBolt"


class StbSecBaseConventionalSPlate(StBridgeElement):
    """StbSecBaseConventionalSPlate：StbSecBaseConventional_S_Plate

    Attributes:
        b_x (float): 属性
        b_y (float): 属性
        c1_x (float): 属性
        c1_y (float): 属性
        c2_x (float): 属性
        c2_y (float): 属性
        c3_x (float): 属性
        c3_y (float): 属性
        c4_x (float): 属性
        c4_y (float): 属性
        t (float): 属性
        strength (str): 属性
        d_bolthole (float): 属性
        offset_x (float): 属性
        offset_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "b_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_X",
        ),
        "b_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_Y",
        ),
        "c1_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C1_X",
        ),
        "c1_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C1_Y",
        ),
        "c2_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C2_X",
        ),
        "c2_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C2_Y",
        ),
        "c3_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C3_X",
        ),
        "c3_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C3_Y",
        ),
        "c4_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C4_X",
        ),
        "c4_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="C4_Y",
        ),
        "t": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "d_bolthole": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D_bolthole",
        ),
        "offset_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_X",
        ),
        "offset_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_S_Plate"


class StbSecBaseConventionalS(StBridgeElement):
    """StbSecBaseConventionalS：StbSecBaseConventional_S

    Attributes:
        height_mortar (float): 属性
        stb_sec_base_conventional_s_plate (StbSecBaseConventionalSPlate): 子要素
        stb_sec_base_conventional_s_anchor_bolt (StbSecBaseConventionalSAnchorBolt): 子要素
        stb_sec_base_conventional_s_rib_plate (StbSecBaseConventionalSRibPlate): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
        "stb_sec_base_conventional_s_plate": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalSPlate,
        ),
        "stb_sec_base_conventional_s_anchor_bolt": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalSAnchorBolt,
        ),
        "stb_sec_base_conventional_s_rib_plate": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseConventionalSRibPlate
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseConventional_S"


class StbSecBaseProductS(StBridgeElement):
    """StbSecBaseProductS：StbSecBaseProduct_S

    Attributes:
        product_company (str): 属性
        product_code (str): 属性
        direction_type (StbSecBaseProductSDirectionType): 属性
        height_mortar (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_company": _FI(py_type=str, data_type=_DT.STR),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "direction_type": _FI(
            py_type=StbSecBaseProductSDirectionType,
            data_type=_DT.INT_ENUM,
            xml_type="nonNegativeInteger",
            choices=("0", "90", "180", "270"),
        ),
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBaseProduct_S"


class StbSecSteelColumnSThreeTypes(StBridgeElement):
    """Ｓ柱断面鉄骨形状・３種類：StbSecSteelColumn_S_ThreeTypes

    Attributes:
        pos (StbSecSteelColumnSThreeTypesPos): 属性 配置位置以下のいずれかBOTTOM（柱脚）CENTER（中央）TOP（柱頭）
        shape (str): 属性 鉄骨形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnSThreeTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "CENTER", "TOP"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_S_ThreeTypes"


class StbSecSteelColumnSNotSame(StBridgeElement):
    """Ｓ柱断面鉄骨形状・柱頭脚別：StbSecSteelColumn_S_NotSame

    Attributes:
        pos (StbSecSteelColumnSNotSamePos): 属性 配置位置以下のいずれかBOTTOM（柱脚）TOP（柱頭）
        shape (str): 属性 鉄骨形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnSNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_S_NotSame"


class StbSecSteelColumnSSame(StBridgeElement):
    """Ｓ柱断面鉄骨形状・同一：StbSecSteelColumn_S_Same

    Attributes:
        shape (str): 属性 鉄骨形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_S_Same"


class StbSecSteelFigureColumnS(StBridgeElement):
    """Ｓ柱断面鉄骨形状：StbSecSteelFigureColumn_S

    Attributes:
        base_type (StbSecSteelFigureColumnSBaseType): 属性 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）EXPOSE（露出）EMBEDDED（埋込）WRAP（根巻）
        joint_id_top (int): 属性
        joint_id_bottom (int): 属性
        stb_sec_steel_column_s_same (StbSecSteelColumnSSame): 子要素 StbSecSteelColumn_S_Same(Ｓ柱断面鉄骨形状・同一)
        stb_sec_steel_column_s_not_same (list[StbSecSteelColumnSNotSame]): 子要素 StbSecSteelColumn_S_NotSame(Ｓ柱断面鉄骨形状・柱頭脚別)
        stb_sec_steel_column_s_three_types (list[StbSecSteelColumnSThreeTypes]): 子要素 StbSecSteelColumn_S_ThreeTypes(Ｓ柱断面鉄骨形状・３種類)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "base_type": _FI(
            py_type=StbSecSteelFigureColumnSBaseType,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "EXPOSE", "EMBEDDED", "WRAP"),
        ),
        "joint_id_top": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_bottom": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_sec_steel_column_s_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSSame
        ),
        "stb_sec_steel_column_s_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSteelColumnSNotSame]
        ),
        "stb_sec_steel_column_s_three_types": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecSteelColumnSThreeTypes]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelFigureColumn_S"


class StbSecColumnS(StBridgeElement):
    """Ｓ柱断面：StbSecColumn_S

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_column (StbSecColumnSKindColumn): 属性 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）
        is_reference_direction (bool): 属性 鉄骨向き
        stb_sec_steel_figure_column_s (StbSecSteelFigureColumnS): 子要素 StbSecSteelFigureColumn_S(Ｓ柱断面鉄骨形状)
        stb_sec_base_product_s (StbSecBaseProductS): 子要素
        stb_sec_base_conventional_s (StbSecBaseConventionalS): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_column": _FI(
            py_type=StbSecColumnSKindColumn,
            data_type=_DT.STR_ENUM,
            choices=("COLUMN", "POST"),
        ),
        "is_reference_direction": _FI(
            py_type=bool, data_type=_DT.BOOL, xml_name="isReferenceDirection"
        ),
        "stb_sec_steel_figure_column_s": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecSteelFigureColumnS,
        ),
        "stb_sec_base_product_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseProductS
        ),
        "stb_sec_base_conventional_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseConventionalS
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_S"


class StbSecBarColumnXReinforced(StBridgeElement):
    """コンクリート矩形柱 Ｘ形配筋：StbSecBarColumnXReinforced

    Attributes:
        n_main_x (int): 属性 主筋：X方向本数
        n_main_y (int): 属性 主筋：Y方向本数
        n_main_total (int): 属性 主筋：X形配筋の総本数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "n_main_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_X",
        ),
        "n_main_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_Y",
        ),
        "n_main_total": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_total",
        ),
    }


class StbSecBarColumnRcCircleNotSame(StBridgeElement):
    """StbSecBarColumnRcCircleNotSame：StbSecBarColumn_RC_CircleNotSame

    Attributes:
        pos (StbSecBarColumnRcCircleNotSamePos): 属性
        d_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main (int): 属性
        n_axial (int): 属性
        n_band (int): 属性
        pitch_band (float): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnRcCircleNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASE", "TOP"),
        ),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "n_band": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_RC_CircleNotSame"


class StbSecBarColumnRcCircleSame(StBridgeElement):
    """StbSecBarColumnRcCircleSame：StbSecBarColumn_RC_CircleSame

    Attributes:
        d_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main (int): 属性
        n_axial (int): 属性
        n_band (int): 属性
        pitch_band (float): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "n_band": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_RC_CircleSame"


class StbSecBarColumnRcRectNotSame(StBridgeElement):
    """StbSecBarColumnRcRectNotSame：StbSecBarColumn_RC_RectNotSame

    Attributes:
        pos (StbSecBarColumnRcRectNotSamePos): 属性
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main_x_1st (int): 属性
        n_main_x_2nd (int): 属性
        n_main_y_1st (int): 属性
        n_main_y_2nd (int): 属性
        n_2nd_main_x_1st (int): 属性
        n_2nd_main_x_2nd (int): 属性
        n_2nd_main_y_1st (int): 属性
        n_2nd_main_y_2nd (int): 属性
        n_main_total (int): 属性
        n_axial (int): 属性
        pitch_band (float): 属性
        n_band_direction_x (int): 属性
        n_band_direction_y (int): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnRcRectNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASE", "TOP"),
        ),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_X_1st",
        ),
        "n_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_X_2nd",
        ),
        "n_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_Y_1st",
        ),
        "n_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_Y_2nd",
        ),
        "n_2nd_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_1st",
        ),
        "n_2nd_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_2nd",
        ),
        "n_2nd_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_1st",
        ),
        "n_2nd_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_2nd",
        ),
        "n_main_total": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_total",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_band_direction_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_X",
        ),
        "n_band_direction_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_Y",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_RC_RectNotSame"


class StbSecBarColumnRcRectSame(StBridgeElement):
    """StbSecBarColumnRcRectSame：StbSecBarColumn_RC_RectSame

    Attributes:
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_axial (str): 属性
        d_band (str): 属性
        d_bar_spacing (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_axial (str): 属性
        strength_band (str): 属性
        strength_bar_spacing (str): 属性
        n_main_x_1st (int): 属性
        n_main_x_2nd (int): 属性
        n_main_y_1st (int): 属性
        n_main_y_2nd (int): 属性
        n_2nd_main_x_1st (int): 属性
        n_2nd_main_x_2nd (int): 属性
        n_2nd_main_y_1st (int): 属性
        n_2nd_main_y_2nd (int): 属性
        n_main_total (int): 属性
        n_axial (int): 属性
        pitch_band (float): 属性
        n_band_direction_x (int): 属性
        n_band_direction_y (int): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "n_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_X_1st",
        ),
        "n_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_X_2nd",
        ),
        "n_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_Y_1st",
        ),
        "n_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_main_Y_2nd",
        ),
        "n_2nd_main_x_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_1st",
        ),
        "n_2nd_main_x_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_X_2nd",
        ),
        "n_2nd_main_y_1st": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_1st",
        ),
        "n_2nd_main_y_2nd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main_Y_2nd",
        ),
        "n_main_total": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main_total",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "n_band_direction_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_X",
        ),
        "n_band_direction_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_band_direction_Y",
        ),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarColumn_RC_RectSame"


class StbSecBarArrangementColumnRc(StBridgeElement):
    """ＲＣ柱断面配筋：StbSecBarArrangementColumn_RC

    Attributes:
        depth_cover_start_x (float): 属性
        depth_cover_end_x (float): 属性
        depth_cover_start_y (float): 属性
        depth_cover_end_y (float): 属性
        interval (float): 属性
        kind_corner (StbSecBarArrangementColumnRcKindCorner): 属性
        is_spiral (bool): 属性
        center_start_x (float): 属性
        center_end_x (float): 属性
        center_start_y (float): 属性
        center_end_y (float): 属性
        center_interval (float): 属性
        stb_sec_bar_column_rc_rect_same (StbSecBarColumnRcRectSame): 子要素
        stb_sec_bar_column_x_reinforced (StbSecBarColumnXReinforced): 子要素 StbSecBarColumnXReinforced(コンクリート矩形柱 Ｘ形配筋)
        stb_sec_bar_column_rc_rect_not_same (list[StbSecBarColumnRcRectNotSame]): 子要素
        stb_sec_bar_column_rc_circle_same (StbSecBarColumnRcCircleSame): 子要素
        stb_sec_bar_column_rc_circle_not_same (list[StbSecBarColumnRcCircleNotSame]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_start_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_start_X",
        ),
        "depth_cover_end_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_end_X",
        ),
        "depth_cover_start_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_start_Y",
        ),
        "depth_cover_end_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="depth_cover_end_Y",
        ),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_corner": _FI(
            py_type=StbSecBarArrangementColumnRcKindCorner,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "DIR_X", "DIR_Y", "DIR_XY"),
        ),
        "is_spiral": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isSpiral"),
        "center_start_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_X",
        ),
        "center_end_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_X",
        ),
        "center_start_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_Y",
        ),
        "center_end_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_Y",
        ),
        "center_interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_bar_column_rc_rect_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnRcRectSame
        ),
        "stb_sec_bar_column_x_reinforced": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnXReinforced
        ),
        "stb_sec_bar_column_rc_rect_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarColumnRcRectNotSame]
        ),
        "stb_sec_bar_column_rc_circle_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnRcCircleSame
        ),
        "stb_sec_bar_column_rc_circle_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarColumnRcCircleNotSame]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementColumn_RC"


class StbSecColumnRcCircle(StBridgeElement):
    """StbSecColumnRcCircle：StbSecColumn_RC_Circle

    Attributes:
        d (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="D",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_RC_Circle"


class StbSecColumnRcRect(StBridgeElement):
    """StbSecColumnRcRect：StbSecColumn_RC_Rect

    Attributes:
        width_x (float): 属性
        width_y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_X",
        ),
        "width_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="width_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_RC_Rect"


class StbSecFigureColumnRc(StBridgeElement):
    """ＲＣ柱断面形状：StbSecFigureColumn_RC

    Attributes:
        stb_sec_column_rc_rect (StbSecColumnRcRect): 子要素
        stb_sec_column_rc_circle (StbSecColumnRcCircle): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_column_rc_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnRcRect
        ),
        "stb_sec_column_rc_circle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnRcCircle
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureColumn_RC"


class StbSecColumnRc(StBridgeElement):
    """ＲＣ柱断面：StbSecColumn_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        floor (str): 属性 所属階
        kind_column (StbSecColumnRcKindColumn): 属性 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_column_rc (StbSecFigureColumnRc): 子要素 StbSecFigureColumn_RC(ＲＣ柱断面形状)
        stb_sec_bar_arrangement_column_rc (StbSecBarArrangementColumnRc): 子要素 StbSecBarArrangementColumn_RC(ＲＣ柱断面配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "floor": _FI(py_type=str, data_type=_DT.STR),
        "kind_column": _FI(
            py_type=StbSecColumnRcKindColumn,
            data_type=_DT.STR_ENUM,
            choices=("COLUMN", "POST"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_column_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFigureColumnRc
        ),
        "stb_sec_bar_arrangement_column_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementColumnRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_RC"


class StbSections(StBridgeElement):
    """断面情報：StbSections

    Attributes:
        stb_sec_column_rc (list[StbSecColumnRc]): 子要素 StbSecColumn_RC(ＲＣ柱断面)
        stb_sec_column_s (list[StbSecColumnS]): 子要素 StbSecColumn_S(Ｓ柱断面)
        stb_sec_column_src (list[StbSecColumnSrc]): 子要素 StbSecColumn_SRC(ＳＲＣ柱断面)
        stb_sec_column_cft (list[StbSecColumnCft]): 子要素 StbSecColumn_CFT(ＣＦＴ柱断面)
        stb_sec_beam_rc (list[StbSecBeamRc]): 子要素 StbSecBeam_RC(ＲＣ梁断面)
        stb_sec_beam_s (list[StbSecBeamS]): 子要素 StbSecBeam_S(Ｓ梁断面)
        stb_sec_beam_src (list[StbSecBeamSrc]): 子要素 StbSecBeam_SRC(ＳＲＣ梁断面)
        stb_sec_brace_s (list[StbSecBraceS]): 子要素 StbSecBrace_S(Ｓブレース断面)
        stb_sec_slab_rc (list[StbSecSlabRc]): 子要素 StbSecSlab_RC(ＲＣスラブ断面)
        stb_sec_slab_deck (list[StbSecSlabDeck]): 子要素 StbSecSlabDeck(デッキ合成スラブ断面)
        stb_sec_slab_precast (list[StbSecSlabPrecast]): 子要素 StbSecSlabPrecast(既製スラブ断面)
        stb_sec_wall_rc (list[StbSecWallRc]): 子要素 StbSecWall_RC(ＲＣ壁断面)
        stb_sec_foundation_rc (list[StbSecFoundationRc]): 子要素 StbSecFoundation_RC(ＲＣ基礎断面)
        stb_sec_pile_rc (list[StbSecPileRc]): 子要素 StbSecPile_RC(ＲＣ杭断面)
        stb_sec_pile_s (list[StbSecPileS]): 子要素 StbSecPile_S(鋼管杭断面)
        stb_sec_pile_product (list[StbSecPileProduct]): 子要素
        stb_sec_open_rc (list[StbSecOpenRc]): 子要素 StbSecOpen_RC(ＲＣ開口断面)
        stb_sec_parapet_rc (list[StbSecParapetRc]): 子要素 StbSecParapet_RC(ＲＣパラペット断面)
        stb_sec_steel (StbSecSteel): 子要素 StbSecSteel(鉄骨断面)
        stb_sec_undefined (list[StbSecUndefined]): 子要素 StbSecUndefined(構造種別に依存しない断面)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_column_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecColumnRc]),
        "stb_sec_column_s": _FI(kind=_FK.ELEMENT, py_type=list[StbSecColumnS]),
        "stb_sec_column_src": _FI(kind=_FK.ELEMENT, py_type=list[StbSecColumnSrc]),
        "stb_sec_column_cft": _FI(kind=_FK.ELEMENT, py_type=list[StbSecColumnCft]),
        "stb_sec_beam_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBeamRc]),
        "stb_sec_beam_s": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBeamS]),
        "stb_sec_beam_src": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBeamSrc]),
        "stb_sec_brace_s": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBraceS]),
        "stb_sec_slab_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecSlabRc]),
        "stb_sec_slab_deck": _FI(kind=_FK.ELEMENT, py_type=list[StbSecSlabDeck]),
        "stb_sec_slab_precast": _FI(kind=_FK.ELEMENT, py_type=list[StbSecSlabPrecast]),
        "stb_sec_wall_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecWallRc]),
        "stb_sec_foundation_rc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecFoundationRc]
        ),
        "stb_sec_pile_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileRc]),
        "stb_sec_pile_s": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileS]),
        "stb_sec_pile_product": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileProduct]),
        "stb_sec_open_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecOpenRc]),
        "stb_sec_parapet_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecParapetRc]),
        "stb_sec_steel": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteel),
        "stb_sec_undefined": _FI(kind=_FK.ELEMENT, py_type=list[StbSecUndefined]),
    }


class StbOpenId(StBridgeElement):
    """StbOpenId

    Attributes:
        id (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbOpenIdList(StBridgeElement):
    """StbOpenIdList

    Attributes:
        stb_open_id (list[StbOpenId]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_open_id": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbOpenId]),
    }


class StbOpen(StBridgeElement):
    """StbOpen

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_section (int): 属性
        position_x (float): 属性
        position_y (float): 属性
        length_x (float): 属性
        length_y (float): 属性
        rotate (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_section": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "position_x": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="position_X"
        ),
        "position_y": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="position_Y"
        ),
        "length_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_X",
        ),
        "length_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="length_Y",
        ),
        "rotate": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
    }


class StbOpens(StBridgeElement):
    """StbOpens

    Attributes:
        stb_open (list[StbOpen]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_open": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbOpen]),
    }


class StbParapet(StBridgeElement):
    """パラペット：StbParapet

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node_start (int): 属性 始端節点ID
        id_node_end (int): 属性 終端節点ID
        id_section (int): 属性 断面ID
        kind_structure (str): 属性 構造種別
        kind_layout (StbParapetKindLayout): 属性 壁種別以下のいずれかの値をとる。ON_GIRDER（大梁上）、ON_BEAM（小梁上）、ON_SLAB（スラブ上）
        direction (StbParapetDirection): 属性 アゴの方向を示す(R/L)R（右側）L（左側）
        offset (float): 属性 オフセット
        level (float): 属性 レベル
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(py_type=str, data_type=_DT.STR, required=True),
        "kind_layout": _FI(
            py_type=StbParapetKindLayout,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ON_GIRDER", "ON_BEAM", "ON_SLAB"),
        ),
        "direction": _FI(
            py_type=StbParapetDirection, data_type=_DT.STR_ENUM, choices=("R", "L")
        ),
        "offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "level": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbParapets(StBridgeElement):
    """パラペット（複数）：StbParapets

    Attributes:
        stb_parapet (list[StbParapet]): 子要素 StbParapet(パラペット)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_parapet": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbParapet]),
    }


class StbFoundationColumn(StBridgeElement):
    """基礎柱：StbFoundationColumn

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node (int): 属性 節点ID
        rotate (float): 属性 回転角
        offset_z (float): 属性 基礎柱・根巻柱の基準点のオフセット（）
        kind_structure (str): 属性 構造種別以下の値をとる。RC
        id_section_fd (int): 属性 基礎柱断面ＩＤ
        length_fd (float): 属性 基礎柱高さ
        offset_fd_x (float): 属性 基礎柱オフセット（）
        offset_fd_y (float): 属性 基礎柱オフセット（）
        thickness_add_fd_start_x (float): 属性 基礎柱ふかし厚さ（X始）
        thickness_add_fd_end_x (float): 属性 基礎柱ふかし厚さ（X終）
        thickness_add_fd_start_y (float): 属性 基礎柱ふかし厚さ（Y始）
        thickness_add_fd_end_y (float): 属性 基礎柱ふかし厚さ（Y終）
        id_section_wr (int): 属性 根巻柱断面ＩＤ
        length_wr (float): 属性 根巻柱高さ
        offset_wr_x (float): 属性 根巻柱オフセット（）
        offset_wr_y (float): 属性 根巻柱オフセット（）
        thickness_add_wr_start_x (float): 属性 根巻柱ふかし厚さ（X始）
        thickness_add_wr_end_x (float): 属性 根巻柱ふかし厚さ（X終）
        thickness_add_wr_start_y (float): 属性 根巻柱ふかし厚さ（Y始）
        thickness_add_wr_end_y (float): 属性 根巻柱ふかし厚さ（Y終）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "offset_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Z"),
        "kind_structure": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_section_fd": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="id_section_FD",
        ),
        "length_fd": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="length_FD"
        ),
        "offset_fd_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_FD_X"),
        "offset_fd_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_FD_Y"),
        "thickness_add_fd_start_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_FD_start_X",
        ),
        "thickness_add_fd_end_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_FD_end_X",
        ),
        "thickness_add_fd_start_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_FD_start_Y",
        ),
        "thickness_add_fd_end_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_FD_end_Y",
        ),
        "id_section_wr": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="id_section_WR",
        ),
        "length_wr": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="length_WR"
        ),
        "offset_wr_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_WR_X"),
        "offset_wr_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_WR_Y"),
        "thickness_add_wr_start_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_WR_start_X",
        ),
        "thickness_add_wr_end_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_WR_end_X",
        ),
        "thickness_add_wr_start_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_WR_start_Y",
        ),
        "thickness_add_wr_end_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_WR_end_Y",
        ),
    }


class StbFoundationColumns(StBridgeElement):
    """基礎柱（複数）：StbFoundationColumns

    Attributes:
        stb_foundation_column (list[StbFoundationColumn]): 子要素 StbFoundationColumn(基礎柱)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_foundation_column": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbFoundationColumn]
        ),
    }


class StbPile(StBridgeElement):
    """杭基礎：StbPile

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node (int): 属性 節点ID
        id_section (int): 属性 断面ID
        kind_structure (StbPileKindStructure): 属性 構造種別以下のいずれかの値をとる。RC、S、PC
        offset_x (float): 属性 オフセット（）
        offset_y (float): 属性 オフセット（）
        level_top (float): 属性 レベル（杭天）
        length_all (float): 属性 杭全長
        length_head (float): 属性 杭頭（拡頭）長さ
        length_foot (float): 属性 杭脚長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbPileKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "PC"),
        ),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
        "level_top": _FI(py_type=float, data_type=_DT.FLOAT),
        "length_all": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_head": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_foot": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbPiles(StBridgeElement):
    """杭基礎（複数）：StbPiles

    Attributes:
        stb_pile (list[StbPile]): 子要素 StbPile(杭基礎)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_pile": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbPile]),
    }


class StbStripFooting(StBridgeElement):
    """布基礎：StbStripFooting

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node_start (int): 属性 始端節点ID
        id_node_end (int): 属性 終端節点ID
        id_section (int): 属性 断面ID
        kind_structure (str): 属性 構造種別
        level (float): 属性 レベル
        offset (float): 属性 オフセット
        length_ex_start (float): 属性 始点側余長
        length_ex_end (float): 属性 終点側余長
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(py_type=str, data_type=_DT.STR, required=True),
        "level": _FI(py_type=float, data_type=_DT.FLOAT),
        "offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "length_ex_start": _FI(py_type=float, data_type=_DT.FLOAT),
        "length_ex_end": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbStripFootings(StBridgeElement):
    """布基礎（複数）：StbStripFootings

    Attributes:
        stb_strip_footing (list[StbStripFooting]): 子要素 StbStripFooting(布基礎)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_strip_footing": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbStripFooting]
        ),
    }


class StbFooting(StBridgeElement):
    """フーチング：StbFooting

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node (int): 属性 節点ID
        rotate (float): 属性 回転角
        id_section (int): 属性 断面ID
        offset_x (float): 属性 オフセット（）
        offset_y (float): 属性 オフセット（）
        level_bottom (float): 属性 レベル（下）
        thickness_add_start_x (float): 属性 ふかし厚さ（X始）
        thickness_add_end_x (float): 属性 ふかし厚さ（X終）
        thickness_add_start_y (float): 属性 ふかし厚さ（Y始）
        thickness_add_end_y (float): 属性 ふかし厚さ（Y終）
        thickness_add_top (float): 属性 ふかし厚さ（上）
        thickness_add_bottom (float): 属性 ふかし厚さ（下）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
        "level_bottom": _FI(py_type=float, data_type=_DT.FLOAT),
        "thickness_add_start_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_X",
        ),
        "thickness_add_end_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_X",
        ),
        "thickness_add_start_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_Y",
        ),
        "thickness_add_end_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_Y",
        ),
        "thickness_add_top": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_bottom": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
    }


class StbFootings(StBridgeElement):
    """フーチング（複数）：StbFootings

    Attributes:
        stb_footing (list[StbFooting]): 子要素 StbFooting(フーチング)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_footing": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbFooting]),
    }


class StbWallOffset(StBridgeElement):
    """壁オフセット：StbWallOffset

    Attributes:
        id_node (int): 属性 節点ID
        offset_x (float): 属性 方向のオフセット
        offset_y (float): 属性 方向のオフセット
        offset_z (float): 属性 方向のオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset_x": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_X"
        ),
        "offset_y": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_Y"
        ),
        "offset_z": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_Z"
        ),
    }


class StbWallOffsetList(StBridgeElement):
    """壁オフセットリスト：StbWallOffsetList

    Attributes:
        stb_wall_offset (list[StbWallOffset]): 子要素 StbWallOffset(壁オフセット)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_wall_offset": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbWallOffset]
        ),
    }


class StbWall(StBridgeElement):
    """壁：StbWall

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_section (int): 属性 断面ID
        kind_structure (str): 属性 構造種別以下のいずれかの値をとる。RC(RC壁)LOAD(荷重のみ)
        kind_layout (StbWallKindLayout): 属性 壁種別以下のいずれかの値をとる。ON_GIRDER（大梁上）、ON_BEAM（小梁上）、ON_SLAB（スラブ上）
        strength_concrete (str): 属性 コンクリート強度
        thickness_add_right (float): 属性 ふかし厚さ（右）
        thickness_add_left (float): 属性 ふかし厚さ（左）
        kind_wall (StbWallKindWall): 属性 耐力区分以下のいずれかの値をとる。WALL_NORMAL（一般壁）、WALL_SHEAR（耐力壁）
        slit_upper (float): 属性 構造スリット（上）
        slit_bottom (float): 属性 構造スリット（下）
        slit_right (float): 属性 構造スリット（右）
        slit_left (float): 属性 構造スリット（左）
        type_outside (StbWallTypeOutside): 属性
        is_press (bool): 属性
        stb_node_id_order (StbNodeIdOrder): 子要素 StbNodeIdOrder(順序のある節点ID)
        stb_wall_offset_list (StbWallOffsetList): 子要素 StbWallOffsetList(壁オフセットリスト)
        stb_open_id_list (StbOpenIdList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(py_type=str, data_type=_DT.STR, required=True),
        "kind_layout": _FI(
            py_type=StbWallKindLayout,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ON_GIRDER", "ON_BEAM", "ON_SLAB"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "thickness_add_right": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_left": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "kind_wall": _FI(
            py_type=StbWallKindWall,
            data_type=_DT.STR_ENUM,
            choices=("WALL_NORMAL", "WALL_SHEAR"),
        ),
        "slit_upper": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "slit_bottom": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "slit_right": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "slit_left": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "type_outside": _FI(
            py_type=StbWallTypeOutside,
            data_type=_DT.STR_ENUM,
            choices=("TYPE_PLUS", "TYPE_MINUS"),
        ),
        "is_press": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isPress"),
        "stb_node_id_order": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbNodeIdOrder"
        ),
        "stb_wall_offset_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbWallOffsetList
        ),
        "stb_open_id_list": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbOpenIdList),
    }


class StbWalls(StBridgeElement):
    """壁（複数）：StbWalls

    Attributes:
        stb_wall (list[StbWall]): 子要素 StbWall(壁)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_wall": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbWall]),
    }


class StbSlabOffset(StBridgeElement):
    """スラブオフセット：StbSlabOffset

    Attributes:
        id_node (int): 属性 節点ID
        offset_x (float): 属性 方向のオフセット
        offset_y (float): 属性 方向のオフセット
        offset_z (float): 属性 方向のオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset_x": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_X"
        ),
        "offset_y": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_Y"
        ),
        "offset_z": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_Z"
        ),
    }


class StbSlabOffsetList(StBridgeElement):
    """スラブオフセットリスト：StbSlabOffsetList

    Attributes:
        stb_slab_offset (list[StbSlabOffset]): 子要素 StbSlabOffset(スラブオフセット)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_slab_offset": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSlabOffset]
        ),
    }


class StbSlab(StBridgeElement):
    """スラブ：StbSlab

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_section (int): 属性 断面ID
        kind_structure (StbSlabKindStructure): 属性 構造種別以下のいずれかの値をとる。RC（RCスラブ）DECK（デッキ合成スラブ）PRECAST（既製スラブ）LOAD(荷重のみ)
        kind_slab (StbSlabKindSlab): 属性 スラブ種類以下のいずれかの値をとる。NORMAL、CANTI
        strength_concrete (str): 属性 コンクリート強度
        thickness_add_top (float): 属性 ふかし厚さ（上）
        thickness_add_bottom (float): 属性 ふかし厚さ（下）
        direction_load (StbSlabDirectionLoad): 属性 荷重伝達方向以下のいずれかの値をとる。1WAY、2WAY
        angle_load (float): 属性 荷重伝達方向「1WAY」の場合の角度
        angle_main_bar_direction (float): 属性 主筋方向角度
        is_foundation (bool): 属性 基礎か否か
        type_haunch (StbSlabTypeHaunch): 属性
        stb_node_id_order (StbNodeIdOrder): 子要素 StbNodeIdOrder(順序のある節点ID)
        stb_slab_offset_list (StbSlabOffsetList): 子要素 StbSlabOffsetList(スラブオフセットリスト)
        stb_open_id_list (StbOpenIdList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbSlabKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "DECK", "PRECAST"),
        ),
        "kind_slab": _FI(
            py_type=StbSlabKindSlab,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("NORMAL", "CANTI"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "thickness_add_top": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_bottom": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "direction_load": _FI(
            py_type=StbSlabDirectionLoad,
            data_type=_DT.STR_ENUM,
            choices=("1WAY", "2WAY"),
        ),
        "angle_load": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "angle_main_bar_direction": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle"
        ),
        "is_foundation": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isFoundation"
        ),
        "type_haunch": _FI(
            py_type=StbSlabTypeHaunch,
            data_type=_DT.STR_ENUM,
            choices=("BOTH", "TOP", "BOTTOM"),
        ),
        "stb_node_id_order": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbNodeIdOrder"
        ),
        "stb_slab_offset_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSlabOffsetList
        ),
        "stb_open_id_list": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbOpenIdList),
    }


class StbSlabs(StBridgeElement):
    """スラブ（複数）：StbSlabs

    Attributes:
        stb_slab (list[StbSlab]): 子要素 StbSlab(スラブ)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_slab": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSlab]),
    }


class StbBrace(StBridgeElement):
    """ブレース：StbBrace

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node_start (int): 属性 始端節点ID
        id_node_end (int): 属性 終端節点ID
        rotate (float): 属性 回転角
        id_section (int): 属性 断面ID
        kind_structure (StbBraceKindStructure): 属性 構造種別RC、S、SRCのいずれかの値
        offset_start_x (float): 属性
        offset_start_y (float): 属性
        offset_start_z (float): 属性
        offset_end_x (float): 属性
        offset_end_y (float): 属性
        offset_end_z (float): 属性
        condition_start (StbBraceConditionStart): 属性
        condition_end (StbBraceConditionEnd): 属性
        feature_brace (StbBraceFeatureBrace): 属性 ブレース特性引張り：TENSION、引張り圧縮：TENSIONANDCOMPRESSIONのいずれかの値
        joint_start (float): 属性
        joint_end (float): 属性
        kind_joint_start (StbBraceKindJointStart): 属性
        kind_joint_end (StbBraceKindJointEnd): 属性
        joint_id_start (int): 属性
        joint_id_end (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbBraceKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "SRC"),
        ),
        "offset_start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_X"
        ),
        "offset_start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Y"
        ),
        "offset_start_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Z"
        ),
        "offset_end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_X"
        ),
        "offset_end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Y"
        ),
        "offset_end_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Z"
        ),
        "condition_start": _FI(
            py_type=StbBraceConditionStart,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN"),
        ),
        "condition_end": _FI(
            py_type=StbBraceConditionEnd, data_type=_DT.STR_ENUM, choices=("FIX", "PIN")
        ),
        "feature_brace": _FI(
            py_type=StbBraceFeatureBrace,
            data_type=_DT.STR_ENUM,
            choices=("TENSION", "TENSIONANDCOMPRESSION"),
        ),
        "joint_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "joint_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_joint_start": _FI(
            py_type=StbBraceKindJointStart,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "kind_joint_end": _FI(
            py_type=StbBraceKindJointEnd,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "joint_id_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbBraces(StBridgeElement):
    """ブレース（複数）：StbBraces

    Attributes:
        stb_brace (list[StbBrace]): 子要素 StbBrace(ブレース)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_brace": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbBrace]),
    }


class StbBeam(StBridgeElement):
    """小梁：StbBeam

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_node_start (int): 属性
        id_node_end (int): 属性
        rotate (float): 属性
        id_section (int): 属性
        section_io_start (StbBeamSectionIoStart): 属性
        section_io_end (StbBeamSectionIoEnd): 属性
        kind_structure (StbBeamKindStructure): 属性
        is_foundation (bool): 属性
        strength_concrete (str): 属性
        offset_start_x (float): 属性
        offset_start_y (float): 属性
        offset_start_z (float): 属性
        offset_end_x (float): 属性
        offset_end_y (float): 属性
        offset_end_z (float): 属性
        thickness_add_top (float): 属性
        thickness_add_bottom (float): 属性
        thickness_add_right (float): 属性
        thickness_add_left (float): 属性
        condition_start (StbBeamConditionStart): 属性
        condition_end (StbBeamConditionEnd): 属性
        haunch_start (float): 属性
        haunch_end (float): 属性
        joint_start (float): 属性
        joint_end (float): 属性
        kind_haunch_start (StbBeamKindHaunchStart): 属性
        kind_haunch_end (StbBeamKindHaunchEnd): 属性
        type_haunch_h (StbBeamTypeHaunchH): 属性
        type_haunch_v (StbBeamTypeHaunchV): 属性
        kind_joint_start (StbBeamKindJointStart): 属性
        kind_joint_end (StbBeamKindJointEnd): 属性
        joint_id_start (int): 属性
        joint_id_end (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_io_start": _FI(
            py_type=StbBeamSectionIoStart, data_type=_DT.STR_ENUM, choices=("OUT", "IN")
        ),
        "section_io_end": _FI(
            py_type=StbBeamSectionIoEnd, data_type=_DT.STR_ENUM, choices=("OUT", "IN")
        ),
        "kind_structure": _FI(
            py_type=StbBeamKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "SRC", "UNDEFINED"),
        ),
        "is_foundation": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isFoundation"
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "offset_start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_X"
        ),
        "offset_start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Y"
        ),
        "offset_start_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Z"
        ),
        "offset_end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_X"
        ),
        "offset_end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Y"
        ),
        "offset_end_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Z"
        ),
        "thickness_add_top": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_bottom": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_right": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_left": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "condition_start": _FI(
            py_type=StbBeamConditionStart,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN"),
        ),
        "condition_end": _FI(
            py_type=StbBeamConditionEnd, data_type=_DT.STR_ENUM, choices=("FIX", "PIN")
        ),
        "haunch_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "haunch_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "joint_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "joint_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_haunch_start": _FI(
            py_type=StbBeamKindHaunchStart,
            data_type=_DT.STR_ENUM,
            choices=("SLOPE", "DROP"),
        ),
        "kind_haunch_end": _FI(
            py_type=StbBeamKindHaunchEnd,
            data_type=_DT.STR_ENUM,
            choices=("SLOPE", "DROP"),
        ),
        "type_haunch_h": _FI(
            py_type=StbBeamTypeHaunchH,
            data_type=_DT.STR_ENUM,
            xml_name="type_haunch_H",
            choices=("BOTH", "RIGHT", "LEFT"),
        ),
        "type_haunch_v": _FI(
            py_type=StbBeamTypeHaunchV,
            data_type=_DT.STR_ENUM,
            xml_name="type_haunch_V",
            choices=("BOTH", "TOP", "BOTTOM"),
        ),
        "kind_joint_start": _FI(
            py_type=StbBeamKindJointStart,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "kind_joint_end": _FI(
            py_type=StbBeamKindJointEnd,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "joint_id_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbBeams(StBridgeElement):
    """小梁（複数）：StbBeams

    Attributes:
        stb_beam (list[StbBeam]): 子要素 StbBeam(小梁)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_beam": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbBeam]),
    }


class StbGirderViaNode(StBridgeElement):
    """大梁中間節点：StbGirderViaNode

    Attributes:
        stb_node_id_order (StbNodeIdOrder): 子要素 StbNodeIdOrder(順序のある節点ID)
        stb_member_offset_list (list[StbMemberOffsetList]): 子要素 StbMemberOffsetList(中間節点オフセットリスト)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_node_id_order": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbNodeIdOrder"
        ),
        "stb_member_offset_list": _FI(
            kind=_FK.ELEMENT, py_type="list[StbMemberOffsetList]"
        ),
    }


class StbGirder(StBridgeElement):
    """大梁：StbGirder

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node_start (int): 属性 始端節点ID
        id_node_end (int): 属性 終端節点ID
        rotate (float): 属性 回転角
        id_section (int): 属性 断面ID
        section_io_start (StbGirderSectionIoStart): 属性 断面の外端・内端指定以下のいずれかの値をとる。OUT、IN
        section_io_end (StbGirderSectionIoEnd): 属性 断面の外端・内端指定以下のいずれかの値をとる。OUT、IN
        kind_structure (StbGirderKindStructure): 属性 構造種別以下のいずれかの値をとる。RC、S、SRC、UNDEFINED
        is_foundation (bool): 属性 基礎か否か
        strength_concrete (str): 属性 コンクリート強度
        offset_start_x (float): 属性 始端側オフセット（）
        offset_start_y (float): 属性 始端側オフセット（）
        offset_start_z (float): 属性 始端側オフセット（）
        offset_end_x (float): 属性 終端側オフセット（）
        offset_end_y (float): 属性 終端側オフセット（）
        offset_end_z (float): 属性 終端側オフセット（）
        thickness_add_top (float): 属性 ふかし厚さ（上）
        thickness_add_bottom (float): 属性 ふかし厚さ（下）
        thickness_add_right (float): 属性 ふかし厚さ（右）
        thickness_add_left (float): 属性 ふかし厚さ（左）
        condition_start (StbGirderConditionStart): 属性
        condition_end (StbGirderConditionEnd): 属性
        haunch_start (float): 属性
        haunch_end (float): 属性
        joint_start (float): 属性
        joint_end (float): 属性
        kind_haunch_start (StbGirderKindHaunchStart): 属性
        kind_haunch_end (StbGirderKindHaunchEnd): 属性
        type_haunch_h (StbGirderTypeHaunchH): 属性
        type_haunch_v (StbGirderTypeHaunchV): 属性
        kind_joint_start (StbGirderKindJointStart): 属性
        kind_joint_end (StbGirderKindJointEnd): 属性
        joint_id_start (int): 属性
        joint_id_end (int): 属性
        stb_girder_via_node (StbGirderViaNode): 子要素 StbGirderViaNode(大梁中間節点)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node_start": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_end": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_io_start": _FI(
            py_type=StbGirderSectionIoStart,
            data_type=_DT.STR_ENUM,
            choices=("OUT", "IN"),
        ),
        "section_io_end": _FI(
            py_type=StbGirderSectionIoEnd, data_type=_DT.STR_ENUM, choices=("OUT", "IN")
        ),
        "kind_structure": _FI(
            py_type=StbGirderKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "SRC", "UNDEFINED"),
        ),
        "is_foundation": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isFoundation"
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "offset_start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_X"
        ),
        "offset_start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Y"
        ),
        "offset_start_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Z"
        ),
        "offset_end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_X"
        ),
        "offset_end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Y"
        ),
        "offset_end_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Z"
        ),
        "thickness_add_top": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_bottom": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_right": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "thickness_add_left": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "condition_start": _FI(
            py_type=StbGirderConditionStart,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN"),
        ),
        "condition_end": _FI(
            py_type=StbGirderConditionEnd,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN"),
        ),
        "haunch_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "haunch_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "joint_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "joint_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_haunch_start": _FI(
            py_type=StbGirderKindHaunchStart,
            data_type=_DT.STR_ENUM,
            choices=("SLOPE", "DROP"),
        ),
        "kind_haunch_end": _FI(
            py_type=StbGirderKindHaunchEnd,
            data_type=_DT.STR_ENUM,
            choices=("SLOPE", "DROP"),
        ),
        "type_haunch_h": _FI(
            py_type=StbGirderTypeHaunchH,
            data_type=_DT.STR_ENUM,
            xml_name="type_haunch_H",
            choices=("BOTH", "RIGHT", "LEFT"),
        ),
        "type_haunch_v": _FI(
            py_type=StbGirderTypeHaunchV,
            data_type=_DT.STR_ENUM,
            xml_name="type_haunch_V",
            choices=("BOTH", "TOP", "BOTTOM"),
        ),
        "kind_joint_start": _FI(
            py_type=StbGirderKindJointStart,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "kind_joint_end": _FI(
            py_type=StbGirderKindJointEnd,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "joint_id_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_girder_via_node": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbGirderViaNode
        ),
    }


class StbGirders(StBridgeElement):
    """大梁（複数）：StbGirders

    Attributes:
        stb_girder (list[StbGirder]): 子要素 StbGirder(大梁)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_girder": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbGirder]),
    }


class StbPost(StBridgeElement):
    """間柱：StbPost

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        id_node_bottom (int): 属性
        id_node_top (int): 属性
        rotate (float): 属性
        id_section (int): 属性
        kind_structure (StbPostKindStructure): 属性
        strength_concrete (str): 属性
        offset_bottom_x (float): 属性
        offset_bottom_y (float): 属性
        offset_bottom_z (float): 属性
        offset_top_x (float): 属性
        offset_top_y (float): 属性
        offset_top_z (float): 属性
        thickness_add_start_x (float): 属性
        thickness_add_end_x (float): 属性
        thickness_add_start_y (float): 属性
        thickness_add_end_y (float): 属性
        condition_bottom (StbPostConditionBottom): 属性
        condition_top (StbPostConditionTop): 属性
        joint_top (float): 属性
        joint_bottom (float): 属性
        kind_joint_top (StbPostKindJointTop): 属性
        kind_joint_bottom (StbPostKindJointBottom): 属性
        joint_id_top (int): 属性
        joint_id_bottom (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node_bottom": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_top": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbPostKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "SRC", "CFT", "UNDEFINED"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "offset_bottom_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_X"
        ),
        "offset_bottom_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_Y"
        ),
        "offset_bottom_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_Z"
        ),
        "offset_top_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_X"
        ),
        "offset_top_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_Y"
        ),
        "offset_top_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_Z"
        ),
        "thickness_add_start_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_X",
        ),
        "thickness_add_end_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_X",
        ),
        "thickness_add_start_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_Y",
        ),
        "thickness_add_end_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_Y",
        ),
        "condition_bottom": _FI(
            py_type=StbPostConditionBottom,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN"),
        ),
        "condition_top": _FI(
            py_type=StbPostConditionTop, data_type=_DT.STR_ENUM, choices=("FIX", "PIN")
        ),
        "joint_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "joint_bottom": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_joint_top": _FI(
            py_type=StbPostKindJointTop,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "kind_joint_bottom": _FI(
            py_type=StbPostKindJointBottom,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "joint_id_top": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_bottom": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbPosts(StBridgeElement):
    """間柱（複数）：StbPosts

    Attributes:
        stb_post (list[StbPost]): 子要素 StbPost(間柱)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_post": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbPost]),
    }


class StbMemberOffsetList(StBridgeElement):
    """中間節点オフセットリスト：StbMemberOffsetList

    Attributes:
        id_node (int): 属性 <StbNodeIdOrder>の中間節点ID
        offset_x (float): 属性 方向のオフセット
        offset_y (float): 属性 方向のオフセット
        offset_z (float): 属性 方向のオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset_x": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_X"
        ),
        "offset_y": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_Y"
        ),
        "offset_z": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="offset_Z"
        ),
    }


class StbColumnViaNode(StBridgeElement):
    """柱中間節点：StbColumnViaNode

    Attributes:
        stb_node_id_order (StbNodeIdOrder): 子要素 StbNodeIdOrder(順序のある節点ID)
        stb_member_offset_list (list[StbMemberOffsetList]): 子要素 StbMemberOffsetList(中間節点オフセットリスト)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_node_id_order": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbNodeIdOrder"
        ),
        "stb_member_offset_list": _FI(
            kind=_FK.ELEMENT, py_type=list[StbMemberOffsetList]
        ),
    }


class StbColumn(StBridgeElement):
    """柱：StbColumn

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node_bottom (int): 属性 始端節点ID
        id_node_top (int): 属性 終端節点ID
        rotate (float): 属性 回転角
        id_section (int): 属性 断面ID
        kind_structure (StbColumnKindStructure): 属性 構造種別以下のいずれかの値をとる。RC、S、SRC、CFT、UNDEFINED
        strength_concrete (str): 属性 コンクリート強度
        offset_bottom_x (float): 属性 始端側オフセット（）
        offset_bottom_y (float): 属性 始端側オフセット（）
        offset_bottom_z (float): 属性 始端側オフセット（）
        offset_top_x (float): 属性 終端側オフセット（）
        offset_top_y (float): 属性 終端側オフセット（）
        offset_top_z (float): 属性 終端側オフセット（）
        thickness_add_start_x (float): 属性 ふかし厚さ（X始）
        thickness_add_end_x (float): 属性 ふかし厚さ（X終）
        thickness_add_start_y (float): 属性 ふかし厚さ（Y始）
        thickness_add_end_y (float): 属性 ふかし厚さ（Y終）
        condition_bottom (StbColumnConditionBottom): 属性
        condition_top (StbColumnConditionTop): 属性
        joint_top (float): 属性
        joint_bottom (float): 属性
        kind_joint_top (StbColumnKindJointTop): 属性
        kind_joint_bottom (StbColumnKindJointBottom): 属性
        joint_id_top (int): 属性
        joint_id_bottom (int): 属性
        stb_column_via_node (StbColumnViaNode): 子要素 StbColumnViaNode(柱中間節点)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_node_bottom": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "id_node_top": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "id_section": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbColumnKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "S", "SRC", "CFT", "UNDEFINED"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "offset_bottom_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_X"
        ),
        "offset_bottom_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_Y"
        ),
        "offset_bottom_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_bottom_Z"
        ),
        "offset_top_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_X"
        ),
        "offset_top_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_Y"
        ),
        "offset_top_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_top_Z"
        ),
        "thickness_add_start_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_X",
        ),
        "thickness_add_end_x": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_X",
        ),
        "thickness_add_start_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_start_Y",
        ),
        "thickness_add_end_y": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="thickness_add_end_Y",
        ),
        "condition_bottom": _FI(
            py_type=StbColumnConditionBottom,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN"),
        ),
        "condition_top": _FI(
            py_type=StbColumnConditionTop,
            data_type=_DT.STR_ENUM,
            choices=("FIX", "PIN"),
        ),
        "joint_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "joint_bottom": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "kind_joint_top": _FI(
            py_type=StbColumnKindJointTop,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "kind_joint_bottom": _FI(
            py_type=StbColumnKindJointBottom,
            data_type=_DT.STR_ENUM,
            choices=("BOLT", "WBOLT", "WELD"),
        ),
        "joint_id_top": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "joint_id_bottom": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_column_via_node": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbColumnViaNode
        ),
    }


class StbColumns(StBridgeElement):
    """柱（複数）：StbColumns

    Attributes:
        stb_column (list[StbColumn]): 子要素 StbColumn(柱)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_column": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbColumn]),
    }


class StbMembers(StBridgeElement):
    """部材情報：StbMembers

    Attributes:
        stb_columns (StbColumns): 子要素 StbColumns(柱（複数）)
        stb_posts (StbPosts): 子要素 StbPosts(間柱（複数）)
        stb_girders (StbGirders): 子要素 StbGirders(大梁（複数）)
        stb_beams (StbBeams): 子要素 StbBeams(小梁（複数）)
        stb_braces (StbBraces): 子要素 StbBraces(ブレース（複数）)
        stb_slabs (StbSlabs): 子要素 StbSlabs(スラブ（複数）)
        stb_walls (StbWalls): 子要素 StbWalls(壁（複数）)
        stb_footings (StbFootings): 子要素 StbFootings(フーチング（複数）)
        stb_strip_footings (StbStripFootings): 子要素 StbStripFootings(布基礎（複数）)
        stb_piles (StbPiles): 子要素 StbPiles(杭基礎（複数）)
        stb_foundation_columns (StbFoundationColumns): 子要素 StbFoundationColumns(基礎柱（複数）)
        stb_parapets (StbParapets): 子要素 StbParapets(パラペット（複数）)
        stb_opens (StbOpens): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_columns": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbColumns),
        "stb_posts": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbPosts),
        "stb_girders": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbGirders),
        "stb_beams": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeams),
        "stb_braces": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbBraces),
        "stb_slabs": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbSlabs),
        "stb_walls": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbWalls),
        "stb_footings": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbFootings),
        "stb_strip_footings": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbStripFootings
        ),
        "stb_piles": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbPiles),
        "stb_foundation_columns": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbFoundationColumns
        ),
        "stb_parapets": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbParapets),
        "stb_opens": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbOpens),
    }


class StbStory(StBridgeElement):
    """階：StbStory

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 階名称
        height (float): 属性 代表高さ
        kind (StbStoryKind): 属性 階属性以下のいずれかの値を取るGENERAL（一般階）BASEMENT（地下階）ROOF（屋上階）PENTHOUSE（塔屋階）ISOLATION（免震階）DEPENDENCE（従属階）
        id_dependence (int): 属性 従属する階のID
        strength_concrete (str): 属性 コンクリート強度
        stb_node_id_list (StbNodeIdList): 子要素 StbNodeIdList(節点IDリスト)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "height": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "kind": _FI(
            py_type=StbStoryKind,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "GENERAL",
                "BASEMENT",
                "ROOF",
                "PENTHOUSE",
                "ISOLATION",
                "DEPENDENCE",
            ),
        ),
        "id_dependence": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_node_id_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbNodeIdList"
        ),
    }


class StbStories(StBridgeElement):
    """階（複数）：StbStories

    Attributes:
        stb_story (list[StbStory]): 子要素 StbStory(階)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_story": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbStory]),
    }


class StbDrawingArcAxis(StBridgeElement):
    """作図用円弧軸：StbDrawingArcAxis

    Attributes:
        group_name (str): 属性 軸グループ名称
        name (str): 属性 名称
        x (float): 属性 中心座標
        y (float): 属性 中心座標
        radius (float): 属性 半径
        start_angle (float): 属性 開始角度
        end_angle (float): 属性 終了角度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "group_name": _FI(py_type=str, data_type=_DT.STR),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "radius": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "start_angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "end_angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
    }


class StbDrawingLineAxis(StBridgeElement):
    """作図用直線軸：StbDrawingLineAxis

    Attributes:
        group_name (str): 属性 軸グループ名称
        name (str): 属性 名称
        start_x (float): 属性 始点座標
        start_y (float): 属性 始点座標
        end_x (float): 属性 終点座標
        end_y (float): 属性 終点座標
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "group_name": _FI(py_type=str, data_type=_DT.STR),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="start_X"
        ),
        "start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="start_Y"
        ),
        "end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="end_X"
        ),
        "end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="end_Y"
        ),
    }


class StbDrawingAxes(StBridgeElement):
    """作図用軸(複数)：StbDrawingAxes

    Attributes:
        stb_drawing_line_axis (list[StbDrawingLineAxis]): 子要素 StbDrawingLineAxis(作図用直線軸)
        stb_drawing_arc_axis (list[StbDrawingArcAxis]): 子要素 StbDrawingArcAxis(作図用円弧軸)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_drawing_line_axis": _FI(
            kind=_FK.ELEMENT, py_type=list[StbDrawingLineAxis]
        ),
        "stb_drawing_arc_axis": _FI(kind=_FK.ELEMENT, py_type=list[StbDrawingArcAxis]),
    }


class StbRadialAxis(StBridgeElement):
    """放射軸：StbRadialAxis

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        angle (float): 属性 中心座標からの角度
        stb_node_id_list (StbNodeIdList): 子要素 StbNodeIdList(節点IDリスト)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "stb_node_id_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbNodeIdList"
        ),
    }


class StbRadialAxes(StBridgeElement):
    """放射軸(複数)：StbRadialAxes

    Attributes:
        group_name (str): 属性 放射軸グループの名称
        x (float): 属性 中心座標
        y (float): 属性 中心座標
        stb_radial_axis (list[StbRadialAxis]): 子要素 StbRadialAxis(放射軸)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "group_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "stb_radial_axis": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbRadialAxis]
        ),
    }


class StbArcAxis(StBridgeElement):
    """円弧軸：StbArcAxis

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        radius (float): 属性 中心座標からの半径距離
        stb_node_id_list (StbNodeIdList): 子要素 StbNodeIdList(節点IDリスト)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "radius": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "stb_node_id_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbNodeIdList"
        ),
    }


class StbArcAxes(StBridgeElement):
    """円弧軸(複数)：StbArcAxes

    Attributes:
        group_name (str): 属性 円弧軸グループの名称
        x (float): 属性 中心座標
        y (float): 属性 中心座標
        start_angle (float): 属性 開始角度
        end_angle (float): 属性 終了角度
        stb_arc_axis (list[StbArcAxis]): 子要素 StbArcAxis(円弧軸)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "group_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "start_angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "end_angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "stb_arc_axis": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbArcAxis]),
    }


class StbParallelAxis(StBridgeElement):
    """平行軸：StbParallelAxis

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        distance (float): 属性 基準座標点からの距離
        stb_node_id_list (StbNodeIdList): 子要素 StbNodeIdList(節点IDリスト)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "distance": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stb_node_id_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbNodeIdList"
        ),
    }


class StbParallelAxes(StBridgeElement):
    """平行軸(複数)：StbParallelAxes

    Attributes:
        group_name (str): 属性 平行軸グループの名称
        x (float): 属性 基準座標
        y (float): 属性 基準座標
        angle (float): 属性 角度
        stb_parallel_axis (list[StbParallelAxis]): 子要素 StbParallelAxis(平行軸)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "group_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "stb_parallel_axis": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbParallelAxis]
        ),
    }


class StbAxes(StBridgeElement):
    """軸（複数）：StbAxes

    Attributes:
        stb_parallel_axes (list[StbParallelAxes]): 子要素 StbParallelAxes(平行軸(複数))
        stb_arc_axes (list[StbArcAxes]): 子要素 StbArcAxes(円弧軸(複数))
        stb_radial_axes (list[StbRadialAxes]): 子要素 StbRadialAxes(放射軸(複数))
        stb_drawing_axes (StbDrawingAxes): 子要素 StbDrawingAxes(作図用軸(複数))
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_parallel_axes": _FI(kind=_FK.ELEMENT, py_type=list[StbParallelAxes]),
        "stb_arc_axes": _FI(kind=_FK.ELEMENT, py_type=list[StbArcAxes]),
        "stb_radial_axes": _FI(kind=_FK.ELEMENT, py_type=list[StbRadialAxes]),
        "stb_drawing_axes": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbDrawingAxes),
    }


class StbNodeIdOrder(StBridgeElement):
    """順序のある節点ID：StbNodeIdOrder

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST,
            py_type=list[int],
        ),
    }


class StbNodeId(StBridgeElement):
    """節点ID：StbNodeId

    Attributes:
        id (int): 属性 StbNodeのID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbNodeIdList(StBridgeElement):
    """節点IDリスト：StbNodeIdList

    Attributes:
        stb_node_id (list[StbNodeId]): 子要素 StbNodeId(節点ID)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_node_id": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbNodeId]),
    }


class StbNode(StBridgeElement):
    """節点：StbNode

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        x (float): 属性 全体座標系
        y (float): 属性 全体座標系
        z (float): 属性 全体座標系
        kind (StbNodeKind): 属性 以下のいずれかの値をとるON_GIRDER：大梁上ON_BEAM：小梁上ON_COLUMN：柱上ON_POST：間柱上ON_GRID：グリッド上ON_CANTI：片持ち大梁先端ON_SLAB：スラブ上OTHER：その他
        id_member (int): 属性 リンクする部材のID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "z": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Z"),
        "kind": _FI(
            py_type=StbNodeKind,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "ON_GIRDER",
                "ON_BEAM",
                "ON_COLUMN",
                "ON_POST",
                "ON_GRID",
                "ON_CANTI",
                "ON_SLAB",
                "OTHER",
            ),
        ),
        "id_member": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbNodes(StBridgeElement):
    """節点（複数）：StbNodes

    Attributes:
        stb_node (list[StbNode]): 子要素 StbNode(節点)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_node": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbNode]),
    }


class StbModel(StBridgeElement):
    """位置・断面情報：StbModel

    Attributes:
        stb_nodes (StbNodes): 子要素 StbNodes(節点（複数）)
        stb_axes (StbAxes): 子要素 StbAxes(軸（複数）)
        stb_stories (StbStories): 子要素 StbStories(階（複数）)
        stb_members (StbMembers): 子要素 StbMembers(部材情報)
        stb_sections (StbSections): 子要素 StbSections(断面情報)
        stb_joints (StbJoints): 子要素 StbJoints(継手情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_nodes": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbNodes),
        "stb_axes": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAxes),
        "stb_stories": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbStories),
        "stb_members": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbMembers),
        "stb_sections": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbSections),
        "stb_joints": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbJoints),
    }


class StbParapetRcBarPositionApply(StBridgeElement):
    """StbParapetRcBarPositionApply：StbParapet_RC_BarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbParapet_RC_BarPositionApply"


class StbPileRcBarPositionApply(StBridgeElement):
    """StbPileRcBarPositionApply：StbPile_RC_BarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbPile_RC_BarPositionApply"


class StbFoundationRcBarPositionApply(StBridgeElement):
    """StbFoundationRcBarPositionApply：StbFoundation_RC_BarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbFoundation_RC_BarPositionApply"


class StbWallRcBarPositionApply(StBridgeElement):
    """StbWallRcBarPositionApply：StbWall_RC_BarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbWall_RC_BarPositionApply"


class StbSlabRcBarPositionApply(StBridgeElement):
    """StbSlabRcBarPositionApply：StbSlab_RC_BarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSlab_RC_BarPositionApply"


class StbBeamSrcBarSpacingApply(StBridgeElement):
    """StbBeamSrcBarSpacingApply：StbBeam_SRC_BarSpacingApply

    Attributes:
        set_default (bool): 属性
        d_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbBeam_SRC_BarSpacingApply"


class StbBeamSrcBarWebApply(StBridgeElement):
    """StbBeamSrcBarWebApply：StbBeam_SRC_BarWebApply

    Attributes:
        set_default (bool): 属性
        d_web (str): 属性
        n_web (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbBeam_SRC_BarWebApply"


class StbBeamSrcRebarPositionApply(StBridgeElement):
    """StbBeamSrcRebarPositionApply：StbBeam_SRC_RebarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover_side (float): 属性
        depth_cover_top_bottom (float): 属性
        interval (float): 属性
        center_side (float): 属性
        center_top_bottom (float): 属性
        length_to_center (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover_side": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_top_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_side": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_top_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "length_to_center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbBeam_SRC_RebarPositionApply"


class StbBeamRcBarSpacingApply(StBridgeElement):
    """StbBeamRcBarSpacingApply：StbBeam_RC_BarSpacingApply

    Attributes:
        set_default (bool): 属性
        d_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbBeam_RC_BarSpacingApply"


class StbBeamRcBarWebApply(StBridgeElement):
    """StbBeamRcBarWebApply：StbBeam_RC_BarWebApply

    Attributes:
        set_default (bool): 属性
        d_web (str): 属性
        n_web (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "n_web": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_web",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbBeam_RC_BarWebApply"


class StbBeamRcRebarPositionApply(StBridgeElement):
    """StbBeamRcRebarPositionApply：StbBeam_RC_RebarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover_side (float): 属性
        depth_cover_top_bottom (float): 属性
        interval (float): 属性
        center_side (float): 属性
        center_top_bottom (float): 属性
        length_to_center (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover_side": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_top_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_side": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center_top_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "length_to_center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbBeam_RC_RebarPositionApply"


class StbColumnSrcBarSpacingApply(StBridgeElement):
    """StbColumnSrcBarSpacingApply：StbColumn_SRC_BarSpacingApply

    Attributes:
        set_default (bool): 属性
        d_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbColumn_SRC_BarSpacingApply"


class StbColumnSrcRebarPositionApply(StBridgeElement):
    """StbColumnSrcRebarPositionApply：StbColumn_SRC_RebarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover (float): 属性
        interval (float): 属性
        center (float): 属性
        length_to_center (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_to_center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbColumn_SRC_RebarPositionApply"


class StbColumnRcBarSpacingApply(StBridgeElement):
    """StbColumnRcBarSpacingApply：StbColumn_RC_BarSpacingApply

    Attributes:
        set_default (bool): 属性
        d_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        n_bar_spacing_x (int): 属性
        n_bar_spacing_y (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "n_bar_spacing_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_X",
        ),
        "n_bar_spacing_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_bar_spacing_Y",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbColumn_RC_BarSpacingApply"


class StbColumnRcRebarPositionApply(StBridgeElement):
    """StbColumnRcRebarPositionApply：StbColumn_RC_RebarPositionApply

    Attributes:
        set_default (bool): 属性
        depth_cover (float): 属性
        interval (float): 属性
        center (float): 属性
        length_to_center (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "set_default": _FI(py_type=bool, data_type=_DT.BOOL, required=True),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_to_center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbColumn_RC_RebarPositionApply"


class StbApplyConditionsList(StBridgeElement):
    """属性・条件適用リスト：StbApplyConditionsList

    Attributes:
        stb_column_rc_rebar_position_apply (StbColumnRcRebarPositionApply): 子要素
        stb_column_rc_bar_spacing_apply (StbColumnRcBarSpacingApply): 子要素
        stb_column_src_rebar_position_apply (StbColumnSrcRebarPositionApply): 子要素
        stb_column_src_bar_spacing_apply (StbColumnSrcBarSpacingApply): 子要素
        stb_beam_rc_rebar_position_apply (StbBeamRcRebarPositionApply): 子要素
        stb_beam_rc_bar_web_apply (StbBeamRcBarWebApply): 子要素
        stb_beam_rc_bar_spacing_apply (StbBeamRcBarSpacingApply): 子要素
        stb_beam_src_rebar_position_apply (StbBeamSrcRebarPositionApply): 子要素
        stb_beam_src_bar_web_apply (StbBeamSrcBarWebApply): 子要素
        stb_beam_src_bar_spacing_apply (StbBeamSrcBarSpacingApply): 子要素
        stb_slab_rc_bar_position_apply (StbSlabRcBarPositionApply): 子要素
        stb_wall_rc_bar_position_apply (StbWallRcBarPositionApply): 子要素
        stb_foundation_rc_bar_position_apply (StbFoundationRcBarPositionApply): 子要素
        stb_pile_rc_bar_position_apply (StbPileRcBarPositionApply): 子要素
        stb_parapet_rc_bar_position_apply (StbParapetRcBarPositionApply): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_column_rc_rebar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbColumnRcRebarPositionApply
        ),
        "stb_column_rc_bar_spacing_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbColumnRcBarSpacingApply
        ),
        "stb_column_src_rebar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbColumnSrcRebarPositionApply
        ),
        "stb_column_src_bar_spacing_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbColumnSrcBarSpacingApply
        ),
        "stb_beam_rc_rebar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeamRcRebarPositionApply
        ),
        "stb_beam_rc_bar_web_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeamRcBarWebApply
        ),
        "stb_beam_rc_bar_spacing_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeamRcBarSpacingApply
        ),
        "stb_beam_src_rebar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeamSrcRebarPositionApply
        ),
        "stb_beam_src_bar_web_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeamSrcBarWebApply
        ),
        "stb_beam_src_bar_spacing_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeamSrcBarSpacingApply
        ),
        "stb_slab_rc_bar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSlabRcBarPositionApply
        ),
        "stb_wall_rc_bar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbWallRcBarPositionApply
        ),
        "stb_foundation_rc_bar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbFoundationRcBarPositionApply
        ),
        "stb_pile_rc_bar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbPileRcBarPositionApply
        ),
        "stb_parapet_rc_bar_position_apply": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbParapetRcBarPositionApply
        ),
    }


class StbReinforcementStrength(StBridgeElement):
    """径別鉄筋強度情報：StbReinforcementStrength

    Attributes:
        d (str): 属性 鉄筋径
        strength (str): 属性 SD(鉄筋強度)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbReinforcementStrengthList(StBridgeElement):
    """径別鉄筋強度情報リスト：StbReinforcementStrengthList

    Attributes:
        stb_reinforcement_strength (list[StbReinforcementStrength]): 子要素 StbReinforcementStrength(径別鉄筋強度情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_reinforcement_strength": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbReinforcementStrength]
        ),
    }


class StbCommon(StBridgeElement):
    """共通情報：StbCommon

    Attributes:
        guid (UUID): 属性 グローバルID
        project_name (str): 属性 プロジェクト名
        app_name (str): 属性 アプリケーション名
        app_version (str): 属性 アプリケーションのバージョン
        convert_app_name (str): 属性 変換プログラム名
        convert_app_version (str): 属性 変換プログラムのバージョン
        strength_concrete (str): 属性 建物全体のコンクリート強度
        global_offset_x (float): 属性 グローバル座標系とのずれ（ΔX）
        global_offset_y (float): 属性 グローバル座標系とのずれ（ΔY）
        global_offset_z (float): 属性 グローバル座標系とのずれ（ΔZ）
        global_rotation (float): 属性 グローバル座標系との回転角度（θ）
        stb_reinforcement_strength_list (StbReinforcementStrengthList): 子要素 StbReinforcementStrengthList(径別鉄筋強度情報リスト)
        stb_apply_conditions_list (StbApplyConditionsList): 子要素 StbApplyConditionsList(属性・条件適用リスト)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "project_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "app_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "app_version": _FI(py_type=str, data_type=_DT.STR, required=True),
        "convert_app_name": _FI(py_type=str, data_type=_DT.STR),
        "convert_app_version": _FI(py_type=str, data_type=_DT.STR),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "global_offset_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="global_offset_X"
        ),
        "global_offset_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="global_offset_Y"
        ),
        "global_offset_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="global_offset_Z"
        ),
        "global_rotation": _FI(py_type=float, data_type=_DT.FLOAT),
        "stb_reinforcement_strength_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbReinforcementStrengthList
        ),
        "stb_apply_conditions_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyConditionsList
        ),
    }


class StBridge(StBridgeRoot):
    """ST-Bridge：ST_BRIDGE

    Attributes:
        version (str): 属性 ST-Bridgeのバージョン
        stb_common (StbCommon): 子要素 StbCommon(共通情報)
        stb_model (StbModel): 子要素 StbModel(位置・断面情報)
        stb_extensions (StbExtensions): 子要素 StbExtensions(拡張情報（複数）)
        stb_cal_data (StbCalData): 子要素
        stb_ana_models (StbAnaModels): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "version": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_common": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbCommon
        ),
        "stb_model": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbModel
        ),
        "stb_extensions": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbExtensions),
        "stb_cal_data": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalData),
        "stb_ana_models": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaModels),
    }
    _xml_element_name: ClassVar[str] = "ST_BRIDGE"
