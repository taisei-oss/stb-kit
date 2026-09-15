# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# 本ファイルはstbkit-codegenによって自動生成されました。
# このファイルを直接編集しないでください。

from collections.abc import Sequence
from enum import IntEnum, StrEnum
from typing import Literal, Protocol
from uuid import UUID

from stbkit.core.data_model.common import StBridgeElement, StBridgeRoot
from stbkit.core.data_model.common import _EnsureAccessorProtocol as _EAP
from stbkit.core.stb_typing import (
    Angle,
    Length,
    Monolist,
    NonNegativeInteger,
    NonNegativeLength,
    PositiveInteger,
)

VERSION: Literal["2.0.1"]

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

class StBridge(StBridgeRoot):
    def __init__(
        self,
        *,
        version: str | None = ...,
        stb_common: StbCommon | None = ...,
        stb_model: StbModel | None = ...,
        stb_extensions: StbExtensions | None = ...,
    ): ...
    version: str
    """属性(Noneの場合例外) ST-Bridgeのバージョン"""
    version_or_none: str | None
    """属性 ST-Bridgeのバージョン"""
    stb_common: StbCommon
    """子要素(Noneの場合例外)"""
    stb_common_or_none: StbCommon | None
    """子要素"""
    stb_model: StbModel
    """子要素(Noneの場合例外)"""
    stb_model_or_none: StbModel | None
    """子要素"""
    stb_extensions: StbExtensions
    """子要素(Noneの場合例外)"""
    stb_extensions_or_none: StbExtensions | None
    """子要素"""
    @property
    def ensure(self) -> _StBridgeEnsureAccessor: ...

class StbCommon(StBridgeElement):
    def __init__(
        self,
        *,
        guid: UUID | None = ...,
        project_name: str | None = ...,
        app_name: str | None = ...,
        strength_concrete: str | None = ...,
        stb_reinforcement_strength_list: StbReinforcementStrengthList | None = ...,
        stb_apply_conditions_list: StbApplyConditionsList | None = ...,
    ): ...
    guid: UUID
    """属性(Noneの場合例外) グローバルID"""
    guid_or_none: UUID | None
    """属性 グローバルID"""
    project_name: str
    """属性(Noneの場合例外) プロジェクト名"""
    project_name_or_none: str | None
    """属性 プロジェクト名"""
    app_name: str
    """属性(Noneの場合例外) アプリケーション名"""
    app_name_or_none: str | None
    """属性 アプリケーション名"""
    strength_concrete: str
    """属性(Noneの場合例外) 建物全体のコンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 建物全体のコンクリート強度"""
    stb_reinforcement_strength_list: StbReinforcementStrengthList
    """子要素(Noneの場合例外)"""
    stb_reinforcement_strength_list_or_none: StbReinforcementStrengthList | None
    """子要素"""
    stb_apply_conditions_list: StbApplyConditionsList
    """子要素(Noneの場合例外)"""
    stb_apply_conditions_list_or_none: StbApplyConditionsList | None
    """子要素"""
    @property
    def ensure(self) -> _StbCommonEnsureAccessor: ...

class StbReinforcementStrengthList(StBridgeElement):
    def __init__(
        self, *, stb_reinforcement_strength: Sequence[StbReinforcementStrength] = ...
    ): ...
    @property
    def stb_reinforcement_strength(self) -> list[StbReinforcementStrength]:
        """stb_reinforcement_strength (list[StbReinforcementStrength]): 子要素"""
    @stb_reinforcement_strength.setter
    def stb_reinforcement_strength(
        self, value: Sequence[StbReinforcementStrength]
    ) -> None: ...

class StbReinforcementStrength(StBridgeElement):
    def __init__(self, *, d: str | None = ..., strength: str | None = ...): ...
    d: str
    """属性(Noneの場合例外) 鉄筋径"""
    d_or_none: str | None
    """属性 鉄筋径"""
    strength: str
    """属性(Noneの場合例外) SD(鉄筋強度)"""
    strength_or_none: str | None
    """属性 SD(鉄筋強度)"""

class StbApplyConditionsList(StBridgeElement):
    def __init__(
        self,
        *,
        stb_column_rc_rebar_position_apply: StbColumnRcRebarPositionApply | None = ...,
        stb_column_rc_bar_spacing_apply: StbColumnRcBarSpacingApply | None = ...,
        stb_column_src_rebar_position_apply: StbColumnSrcRebarPositionApply
        | None = ...,
        stb_column_src_bar_spacing_apply: StbColumnSrcBarSpacingApply | None = ...,
        stb_beam_rc_rebar_position_apply: StbBeamRcRebarPositionApply | None = ...,
        stb_beam_rc_bar_web_apply: StbBeamRcBarWebApply | None = ...,
        stb_beam_rc_bar_spacing_apply: StbBeamRcBarSpacingApply | None = ...,
        stb_beam_src_rebar_position_apply: StbBeamSrcRebarPositionApply | None = ...,
        stb_beam_src_bar_web_apply: StbBeamSrcBarWebApply | None = ...,
        stb_beam_src_bar_spacing_apply: StbBeamSrcBarSpacingApply | None = ...,
        stb_slab_rc_bar_position_apply: StbSlabRcBarPositionApply | None = ...,
        stb_wall_rc_bar_position_apply: StbWallRcBarPositionApply | None = ...,
        stb_foundation_rc_bar_position_apply: StbFoundationRcBarPositionApply
        | None = ...,
        stb_pile_rc_bar_position_apply: StbPileRcBarPositionApply | None = ...,
        stb_parapet_rc_bar_position_apply: StbParapetRcBarPositionApply | None = ...,
    ): ...
    stb_column_rc_rebar_position_apply: StbColumnRcRebarPositionApply
    """子要素(Noneの場合例外)"""
    stb_column_rc_rebar_position_apply_or_none: StbColumnRcRebarPositionApply | None
    """子要素"""
    stb_column_rc_bar_spacing_apply: StbColumnRcBarSpacingApply
    """子要素(Noneの場合例外)"""
    stb_column_rc_bar_spacing_apply_or_none: StbColumnRcBarSpacingApply | None
    """子要素"""
    stb_column_src_rebar_position_apply: StbColumnSrcRebarPositionApply
    """子要素(Noneの場合例外)"""
    stb_column_src_rebar_position_apply_or_none: StbColumnSrcRebarPositionApply | None
    """子要素"""
    stb_column_src_bar_spacing_apply: StbColumnSrcBarSpacingApply
    """子要素(Noneの場合例外)"""
    stb_column_src_bar_spacing_apply_or_none: StbColumnSrcBarSpacingApply | None
    """子要素"""
    stb_beam_rc_rebar_position_apply: StbBeamRcRebarPositionApply
    """子要素(Noneの場合例外)"""
    stb_beam_rc_rebar_position_apply_or_none: StbBeamRcRebarPositionApply | None
    """子要素"""
    stb_beam_rc_bar_web_apply: StbBeamRcBarWebApply
    """子要素(Noneの場合例外)"""
    stb_beam_rc_bar_web_apply_or_none: StbBeamRcBarWebApply | None
    """子要素"""
    stb_beam_rc_bar_spacing_apply: StbBeamRcBarSpacingApply
    """子要素(Noneの場合例外)"""
    stb_beam_rc_bar_spacing_apply_or_none: StbBeamRcBarSpacingApply | None
    """子要素"""
    stb_beam_src_rebar_position_apply: StbBeamSrcRebarPositionApply
    """子要素(Noneの場合例外)"""
    stb_beam_src_rebar_position_apply_or_none: StbBeamSrcRebarPositionApply | None
    """子要素"""
    stb_beam_src_bar_web_apply: StbBeamSrcBarWebApply
    """子要素(Noneの場合例外)"""
    stb_beam_src_bar_web_apply_or_none: StbBeamSrcBarWebApply | None
    """子要素"""
    stb_beam_src_bar_spacing_apply: StbBeamSrcBarSpacingApply
    """子要素(Noneの場合例外)"""
    stb_beam_src_bar_spacing_apply_or_none: StbBeamSrcBarSpacingApply | None
    """子要素"""
    stb_slab_rc_bar_position_apply: StbSlabRcBarPositionApply
    """子要素(Noneの場合例外)"""
    stb_slab_rc_bar_position_apply_or_none: StbSlabRcBarPositionApply | None
    """子要素"""
    stb_wall_rc_bar_position_apply: StbWallRcBarPositionApply
    """子要素(Noneの場合例外)"""
    stb_wall_rc_bar_position_apply_or_none: StbWallRcBarPositionApply | None
    """子要素"""
    stb_foundation_rc_bar_position_apply: StbFoundationRcBarPositionApply
    """子要素(Noneの場合例外)"""
    stb_foundation_rc_bar_position_apply_or_none: StbFoundationRcBarPositionApply | None
    """子要素"""
    stb_pile_rc_bar_position_apply: StbPileRcBarPositionApply
    """子要素(Noneの場合例外)"""
    stb_pile_rc_bar_position_apply_or_none: StbPileRcBarPositionApply | None
    """子要素"""
    stb_parapet_rc_bar_position_apply: StbParapetRcBarPositionApply
    """子要素(Noneの場合例外)"""
    stb_parapet_rc_bar_position_apply_or_none: StbParapetRcBarPositionApply | None
    """子要素"""
    @property
    def ensure(self) -> _StbApplyConditionsListEnsureAccessor: ...

class StbColumnRcRebarPositionApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        depth_cover: Length | None = ...,
        interval: Length | None = ...,
        center: Length | None = ...,
        length_to_center: Length | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    center: Length
    """属性(Noneの場合例外)"""
    center_or_none: Length | None
    """属性"""
    length_to_center: Length
    """属性(Noneの場合例外)"""
    length_to_center_or_none: Length | None
    """属性"""

class StbColumnRcBarSpacingApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        d_bar_spacing: str | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbColumnSrcRebarPositionApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        depth_cover: Length | None = ...,
        interval: Length | None = ...,
        center: Length | None = ...,
        length_to_center: Length | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    center: Length
    """属性(Noneの場合例外)"""
    center_or_none: Length | None
    """属性"""
    length_to_center: Length
    """属性(Noneの場合例外)"""
    length_to_center_or_none: Length | None
    """属性"""

class StbColumnSrcBarSpacingApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        d_bar_spacing: str | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbBeamRcRebarPositionApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        depth_cover_side: Length | None = ...,
        depth_cover_top_bottom: Length | None = ...,
        interval: Length | None = ...,
        center_side: Length | None = ...,
        center_top_bottom: Length | None = ...,
        length_to_center: Length | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover_side: Length
    """属性(Noneの場合例外)"""
    depth_cover_side_or_none: Length | None
    """属性"""
    depth_cover_top_bottom: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_bottom_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    center_side: Length
    """属性(Noneの場合例外)"""
    center_side_or_none: Length | None
    """属性"""
    center_top_bottom: Length
    """属性(Noneの場合例外)"""
    center_top_bottom_or_none: Length | None
    """属性"""
    length_to_center: Length
    """属性(Noneの場合例外)"""
    length_to_center_or_none: Length | None
    """属性"""

class StbBeamRcBarWebApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        d_web: str | None = ...,
        n_web: PositiveInteger | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""

class StbBeamRcBarSpacingApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        d_bar_spacing: str | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""

class StbBeamSrcRebarPositionApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        depth_cover_side: Length | None = ...,
        depth_cover_top_bottom: Length | None = ...,
        interval: Length | None = ...,
        center_side: Length | None = ...,
        center_top_bottom: Length | None = ...,
        length_to_center: Length | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover_side: Length
    """属性(Noneの場合例外)"""
    depth_cover_side_or_none: Length | None
    """属性"""
    depth_cover_top_bottom: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_bottom_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    center_side: Length
    """属性(Noneの場合例外)"""
    center_side_or_none: Length | None
    """属性"""
    center_top_bottom: Length
    """属性(Noneの場合例外)"""
    center_top_bottom_or_none: Length | None
    """属性"""
    length_to_center: Length
    """属性(Noneの場合例外)"""
    length_to_center_or_none: Length | None
    """属性"""

class StbBeamSrcBarWebApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        d_web: str | None = ...,
        n_web: PositiveInteger | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""

class StbBeamSrcBarSpacingApply(StBridgeElement):
    def __init__(
        self,
        *,
        set_default: bool | None = ...,
        d_bar_spacing: str | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""

class StbSlabRcBarPositionApply(StBridgeElement):
    def __init__(
        self, *, set_default: bool | None = ..., depth_cover: Length | None = ...
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""

class StbWallRcBarPositionApply(StBridgeElement):
    def __init__(
        self, *, set_default: bool | None = ..., depth_cover: Length | None = ...
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""

class StbFoundationRcBarPositionApply(StBridgeElement):
    def __init__(
        self, *, set_default: bool | None = ..., depth_cover: Length | None = ...
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""

class StbPileRcBarPositionApply(StBridgeElement):
    def __init__(
        self, *, set_default: bool | None = ..., depth_cover: Length | None = ...
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""

class StbParapetRcBarPositionApply(StBridgeElement):
    def __init__(
        self, *, set_default: bool | None = ..., depth_cover: Length | None = ...
    ): ...
    set_default: bool
    """属性(Noneの場合例外)"""
    set_default_or_none: bool | None
    """属性"""
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""

class StbModel(StBridgeElement):
    def __init__(
        self,
        *,
        stb_nodes: StbNodes | None = ...,
        stb_axes: StbAxes | None = ...,
        stb_stories: StbStories | None = ...,
        stb_members: StbMembers | None = ...,
        stb_sections: StbSections | None = ...,
        stb_joints: StbJoints | None = ...,
    ): ...
    stb_nodes: StbNodes
    """子要素(Noneの場合例外)"""
    stb_nodes_or_none: StbNodes | None
    """子要素"""
    stb_axes: StbAxes
    """子要素(Noneの場合例外)"""
    stb_axes_or_none: StbAxes | None
    """子要素"""
    stb_stories: StbStories
    """子要素(Noneの場合例外)"""
    stb_stories_or_none: StbStories | None
    """子要素"""
    stb_members: StbMembers
    """子要素(Noneの場合例外)"""
    stb_members_or_none: StbMembers | None
    """子要素"""
    stb_sections: StbSections
    """子要素(Noneの場合例外)"""
    stb_sections_or_none: StbSections | None
    """子要素"""
    stb_joints: StbJoints
    """子要素(Noneの場合例外)"""
    stb_joints_or_none: StbJoints | None
    """子要素"""
    @property
    def ensure(self) -> _StbModelEnsureAccessor: ...

class StbNodes(StBridgeElement):
    def __init__(self, *, stb_node: Sequence[StbNode] = ...): ...
    @property
    def stb_node(self) -> list[StbNode]:
        """stb_node (list[StbNode]): 子要素"""
    @stb_node.setter
    def stb_node(self, value: Sequence[StbNode]) -> None: ...

class StbNode(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        x: float | None = ...,
        y: float | None = ...,
        z: float | None = ...,
        kind: StbNodeKind | str | None = ...,
        id_member: PositiveInteger | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    x: float
    """属性(Noneの場合例外) 全体座標系 """
    x_or_none: float | None
    """属性 全体座標系 """
    y: float
    """属性(Noneの場合例外) 全体座標系 """
    y_or_none: float | None
    """属性 全体座標系 """
    z: float
    """属性(Noneの場合例外) 全体座標系 """
    z_or_none: float | None
    """属性 全体座標系 """
    @property
    def kind(self) -> StbNodeKind:
        """属性(Noneの場合例外) 以下のいずれかの値をとるON_GIRDER：大梁上ON_BEAM：小梁上ON_COLUMN：柱上ON_POST：間柱上ON_GRID：グリッド上ON_CANTI：片持ち大梁先端ON_SLAB：スラブ上OTHER：その他"""
    @kind.setter
    def kind(self, value: StbNodeKind | str) -> None: ...
    @property
    def kind_or_none(self) -> StbNodeKind | None:
        """属性 以下のいずれかの値をとるON_GIRDER：大梁上ON_BEAM：小梁上ON_COLUMN：柱上ON_POST：間柱上ON_GRID：グリッド上ON_CANTI：片持ち大梁先端ON_SLAB：スラブ上OTHER：その他"""
    @kind_or_none.setter
    def kind_or_none(self, value: StbNodeKind | str | None) -> None: ...
    id_member: PositiveInteger
    """属性(Noneの場合例外) リンクする部材のID"""
    id_member_or_none: PositiveInteger | None
    """属性 リンクする部材のID"""

class StbNodeIdList(StBridgeElement):
    def __init__(self, *, stb_node_id: Sequence[StbNodeId] = ...): ...
    @property
    def stb_node_id(self) -> list[StbNodeId]:
        """stb_node_id (list[StbNodeId]): 子要素"""
    @stb_node_id.setter
    def stb_node_id(self, value: Sequence[StbNodeId]) -> None: ...

class StbNodeId(StBridgeElement):
    def __init__(self, *, id: PositiveInteger | None = ...): ...
    id: PositiveInteger
    """属性(Noneの場合例外) StbNodeのID"""
    id_or_none: PositiveInteger | None
    """属性 StbNodeのID"""

class StbNodeIdOrder(StBridgeElement):
    def __init__(self, *, content: Monolist = ...): ...
    content: Monolist
    """内容"""

class StbAxes(StBridgeElement):
    def __init__(
        self,
        *,
        stb_parallel_axes: Sequence[StbParallelAxes] = ...,
        stb_arc_axes: Sequence[StbArcAxes] = ...,
        stb_radial_axes: Sequence[StbRadialAxes] = ...,
        stb_drawing_axes: StbDrawingAxes | None = ...,
    ): ...
    @property
    def stb_parallel_axes(self) -> list[StbParallelAxes]:
        """stb_parallel_axes (list[StbParallelAxes]): 子要素"""
    @stb_parallel_axes.setter
    def stb_parallel_axes(self, value: Sequence[StbParallelAxes]) -> None: ...
    @property
    def stb_arc_axes(self) -> list[StbArcAxes]:
        """stb_arc_axes (list[StbArcAxes]): 子要素"""
    @stb_arc_axes.setter
    def stb_arc_axes(self, value: Sequence[StbArcAxes]) -> None: ...
    @property
    def stb_radial_axes(self) -> list[StbRadialAxes]:
        """stb_radial_axes (list[StbRadialAxes]): 子要素"""
    @stb_radial_axes.setter
    def stb_radial_axes(self, value: Sequence[StbRadialAxes]) -> None: ...
    stb_drawing_axes: StbDrawingAxes
    """子要素(Noneの場合例外)"""
    stb_drawing_axes_or_none: StbDrawingAxes | None
    """子要素"""
    @property
    def ensure(self) -> _StbAxesEnsureAccessor: ...

class StbParallelAxes(StBridgeElement):
    def __init__(
        self,
        *,
        group_name: str | None = ...,
        x: float | None = ...,
        y: float | None = ...,
        angle: Angle | None = ...,
        stb_parallel_axis: Sequence[StbParallelAxis] = ...,
    ): ...
    group_name: str
    """属性(Noneの場合例外) 平行軸グループの名称"""
    group_name_or_none: str | None
    """属性 平行軸グループの名称"""
    x: float
    """属性(Noneの場合例外) 基準座標 """
    x_or_none: float | None
    """属性 基準座標 """
    y: float
    """属性(Noneの場合例外) 基準座標 """
    y_or_none: float | None
    """属性 基準座標 """
    angle: Angle
    """属性(Noneの場合例外) 角度"""
    angle_or_none: Angle | None
    """属性 角度"""
    @property
    def stb_parallel_axis(self) -> list[StbParallelAxis]:
        """stb_parallel_axis (list[StbParallelAxis]): 子要素"""
    @stb_parallel_axis.setter
    def stb_parallel_axis(self, value: Sequence[StbParallelAxis]) -> None: ...

class StbParallelAxis(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        distance: float | None = ...,
        stb_node_id_list: StbNodeIdList | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    distance: float
    """属性(Noneの場合例外) 基準座標点からの距離"""
    distance_or_none: float | None
    """属性 基準座標点からの距離"""
    stb_node_id_list: StbNodeIdList
    """子要素(Noneの場合例外)"""
    stb_node_id_list_or_none: StbNodeIdList | None
    """子要素"""
    @property
    def ensure(self) -> _StbParallelAxisEnsureAccessor: ...

class StbArcAxes(StBridgeElement):
    def __init__(
        self,
        *,
        group_name: str | None = ...,
        x: float | None = ...,
        y: float | None = ...,
        start_angle: Angle | None = ...,
        end_angle: Angle | None = ...,
        stb_arc_axis: Sequence[StbArcAxis] = ...,
    ): ...
    group_name: str
    """属性(Noneの場合例外) 円弧軸グループの名称"""
    group_name_or_none: str | None
    """属性 円弧軸グループの名称"""
    x: float
    """属性(Noneの場合例外) 中心座標 """
    x_or_none: float | None
    """属性 中心座標 """
    y: float
    """属性(Noneの場合例外) 中心座標 """
    y_or_none: float | None
    """属性 中心座標 """
    start_angle: Angle
    """属性(Noneの場合例外) 開始角度"""
    start_angle_or_none: Angle | None
    """属性 開始角度"""
    end_angle: Angle
    """属性(Noneの場合例外) 終了角度"""
    end_angle_or_none: Angle | None
    """属性 終了角度"""
    @property
    def stb_arc_axis(self) -> list[StbArcAxis]:
        """stb_arc_axis (list[StbArcAxis]): 子要素"""
    @stb_arc_axis.setter
    def stb_arc_axis(self, value: Sequence[StbArcAxis]) -> None: ...

class StbArcAxis(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        radius: Length | None = ...,
        stb_node_id_list: StbNodeIdList | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    radius: Length
    """属性(Noneの場合例外) 中心座標からの半径距離"""
    radius_or_none: Length | None
    """属性 中心座標からの半径距離"""
    stb_node_id_list: StbNodeIdList
    """子要素(Noneの場合例外)"""
    stb_node_id_list_or_none: StbNodeIdList | None
    """子要素"""
    @property
    def ensure(self) -> _StbArcAxisEnsureAccessor: ...

class StbRadialAxes(StBridgeElement):
    def __init__(
        self,
        *,
        group_name: str | None = ...,
        x: float | None = ...,
        y: float | None = ...,
        stb_radial_axis: Sequence[StbRadialAxis] = ...,
    ): ...
    group_name: str
    """属性(Noneの場合例外) 放射軸グループの名称"""
    group_name_or_none: str | None
    """属性 放射軸グループの名称"""
    x: float
    """属性(Noneの場合例外) 中心座標 """
    x_or_none: float | None
    """属性 中心座標 """
    y: float
    """属性(Noneの場合例外) 中心座標 """
    y_or_none: float | None
    """属性 中心座標 """
    @property
    def stb_radial_axis(self) -> list[StbRadialAxis]:
        """stb_radial_axis (list[StbRadialAxis]): 子要素"""
    @stb_radial_axis.setter
    def stb_radial_axis(self, value: Sequence[StbRadialAxis]) -> None: ...

class StbRadialAxis(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        angle: Angle | None = ...,
        stb_node_id_list: StbNodeIdList | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    angle: Angle
    """属性(Noneの場合例外) 中心座標からの角度"""
    angle_or_none: Angle | None
    """属性 中心座標からの角度"""
    stb_node_id_list: StbNodeIdList
    """子要素(Noneの場合例外)"""
    stb_node_id_list_or_none: StbNodeIdList | None
    """子要素"""
    @property
    def ensure(self) -> _StbRadialAxisEnsureAccessor: ...

class StbDrawingAxes(StBridgeElement):
    def __init__(
        self,
        *,
        stb_drawing_line_axis: Sequence[StbDrawingLineAxis] = ...,
        stb_drawing_arc_axis: Sequence[StbDrawingArcAxis] = ...,
    ): ...
    @property
    def stb_drawing_line_axis(self) -> list[StbDrawingLineAxis]:
        """stb_drawing_line_axis (list[StbDrawingLineAxis]): 子要素"""
    @stb_drawing_line_axis.setter
    def stb_drawing_line_axis(self, value: Sequence[StbDrawingLineAxis]) -> None: ...
    @property
    def stb_drawing_arc_axis(self) -> list[StbDrawingArcAxis]:
        """stb_drawing_arc_axis (list[StbDrawingArcAxis]): 子要素"""
    @stb_drawing_arc_axis.setter
    def stb_drawing_arc_axis(self, value: Sequence[StbDrawingArcAxis]) -> None: ...

class StbDrawingLineAxis(StBridgeElement):
    def __init__(
        self,
        *,
        group_name: str | None = ...,
        name: str | None = ...,
        start_x: float | None = ...,
        start_y: float | None = ...,
        end_x: float | None = ...,
        end_y: float | None = ...,
    ): ...
    group_name: str
    """属性(Noneの場合例外) 軸グループ名称"""
    group_name_or_none: str | None
    """属性 軸グループ名称"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    start_x: float
    """属性(Noneの場合例外) 始点座標 """
    start_x_or_none: float | None
    """属性 始点座標 """
    start_y: float
    """属性(Noneの場合例外) 始点座標 """
    start_y_or_none: float | None
    """属性 始点座標 """
    end_x: float
    """属性(Noneの場合例外) 終点座標 """
    end_x_or_none: float | None
    """属性 終点座標 """
    end_y: float
    """属性(Noneの場合例外) 終点座標 """
    end_y_or_none: float | None
    """属性 終点座標 """

class StbDrawingArcAxis(StBridgeElement):
    def __init__(
        self,
        *,
        group_name: str | None = ...,
        name: str | None = ...,
        x: float | None = ...,
        y: float | None = ...,
        radius: Length | None = ...,
        start_angle: Angle | None = ...,
        end_angle: Angle | None = ...,
    ): ...
    group_name: str
    """属性(Noneの場合例外) 軸グループ名称"""
    group_name_or_none: str | None
    """属性 軸グループ名称"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    x: float
    """属性(Noneの場合例外) 中心座標 """
    x_or_none: float | None
    """属性 中心座標 """
    y: float
    """属性(Noneの場合例外) 中心座標 """
    y_or_none: float | None
    """属性 中心座標 """
    radius: Length
    """属性(Noneの場合例外) 半径"""
    radius_or_none: Length | None
    """属性 半径"""
    start_angle: Angle
    """属性(Noneの場合例外) 開始角度"""
    start_angle_or_none: Angle | None
    """属性 開始角度"""
    end_angle: Angle
    """属性(Noneの場合例外) 終了角度"""
    end_angle_or_none: Angle | None
    """属性 終了角度"""

class StbStories(StBridgeElement):
    def __init__(self, *, stb_story: Sequence[StbStory] = ...): ...
    @property
    def stb_story(self) -> list[StbStory]:
        """stb_story (list[StbStory]): 子要素"""
    @stb_story.setter
    def stb_story(self, value: Sequence[StbStory]) -> None: ...

class StbStory(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        height: float | None = ...,
        kind: StbStoryKind | str | None = ...,
        id_dependence: PositiveInteger | None = ...,
        strength_concrete: str | None = ...,
        stb_node_id_list: StbNodeIdList | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 階名称"""
    name_or_none: str | None
    """属性 階名称"""
    height: float
    """属性(Noneの場合例外) 代表高さ"""
    height_or_none: float | None
    """属性 代表高さ"""
    @property
    def kind(self) -> StbStoryKind:
        """属性(Noneの場合例外) 階属性以下のいずれかの値を取るGENERAL（一般階）BASEMENT（地下階）ROOF（屋上階）PENTHOUSE（塔屋階）ISOLATION（免震階）DEPENDENCE（従属階）"""
    @kind.setter
    def kind(self, value: StbStoryKind | str) -> None: ...
    @property
    def kind_or_none(self) -> StbStoryKind | None:
        """属性 階属性以下のいずれかの値を取るGENERAL（一般階）BASEMENT（地下階）ROOF（屋上階）PENTHOUSE（塔屋階）ISOLATION（免震階）DEPENDENCE（従属階）"""
    @kind_or_none.setter
    def kind_or_none(self, value: StbStoryKind | str | None) -> None: ...
    id_dependence: PositiveInteger
    """属性(Noneの場合例外) 従属する階のID"""
    id_dependence_or_none: PositiveInteger | None
    """属性 従属する階のID"""
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_node_id_list: StbNodeIdList
    """子要素(Noneの場合例外)"""
    stb_node_id_list_or_none: StbNodeIdList | None
    """子要素"""
    @property
    def ensure(self) -> _StbStoryEnsureAccessor: ...

class StbMembers(StBridgeElement):
    def __init__(
        self,
        *,
        stb_columns: StbColumns | None = ...,
        stb_posts: StbPosts | None = ...,
        stb_girders: StbGirders | None = ...,
        stb_beams: StbBeams | None = ...,
        stb_braces: StbBraces | None = ...,
        stb_slabs: StbSlabs | None = ...,
        stb_walls: StbWalls | None = ...,
        stb_footings: StbFootings | None = ...,
        stb_strip_footings: StbStripFootings | None = ...,
        stb_piles: StbPiles | None = ...,
        stb_foundation_columns: StbFoundationColumns | None = ...,
        stb_parapets: StbParapets | None = ...,
        stb_opens: StbOpens | None = ...,
    ): ...
    stb_columns: StbColumns
    """子要素(Noneの場合例外)"""
    stb_columns_or_none: StbColumns | None
    """子要素"""
    stb_posts: StbPosts
    """子要素(Noneの場合例外)"""
    stb_posts_or_none: StbPosts | None
    """子要素"""
    stb_girders: StbGirders
    """子要素(Noneの場合例外)"""
    stb_girders_or_none: StbGirders | None
    """子要素"""
    stb_beams: StbBeams
    """子要素(Noneの場合例外)"""
    stb_beams_or_none: StbBeams | None
    """子要素"""
    stb_braces: StbBraces
    """子要素(Noneの場合例外)"""
    stb_braces_or_none: StbBraces | None
    """子要素"""
    stb_slabs: StbSlabs
    """子要素(Noneの場合例外)"""
    stb_slabs_or_none: StbSlabs | None
    """子要素"""
    stb_walls: StbWalls
    """子要素(Noneの場合例外)"""
    stb_walls_or_none: StbWalls | None
    """子要素"""
    stb_footings: StbFootings
    """子要素(Noneの場合例外)"""
    stb_footings_or_none: StbFootings | None
    """子要素"""
    stb_strip_footings: StbStripFootings
    """子要素(Noneの場合例外)"""
    stb_strip_footings_or_none: StbStripFootings | None
    """子要素"""
    stb_piles: StbPiles
    """子要素(Noneの場合例外)"""
    stb_piles_or_none: StbPiles | None
    """子要素"""
    stb_foundation_columns: StbFoundationColumns
    """子要素(Noneの場合例外)"""
    stb_foundation_columns_or_none: StbFoundationColumns | None
    """子要素"""
    stb_parapets: StbParapets
    """子要素(Noneの場合例外)"""
    stb_parapets_or_none: StbParapets | None
    """子要素"""
    stb_opens: StbOpens
    """子要素(Noneの場合例外)"""
    stb_opens_or_none: StbOpens | None
    """子要素"""
    @property
    def ensure(self) -> _StbMembersEnsureAccessor: ...

class StbColumns(StBridgeElement):
    def __init__(self, *, stb_column: Sequence[StbColumn] = ...): ...
    @property
    def stb_column(self) -> list[StbColumn]:
        """stb_column (list[StbColumn]): 子要素"""
    @stb_column.setter
    def stb_column(self, value: Sequence[StbColumn]) -> None: ...

class StbColumn(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node_bottom: PositiveInteger | None = ...,
        id_node_top: PositiveInteger | None = ...,
        rotate: Angle | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: StbColumnKindStructure | str | None = ...,
        offset_bottom_x: float | None = ...,
        offset_bottom_y: float | None = ...,
        offset_bottom_z: float | None = ...,
        offset_top_x: float | None = ...,
        offset_top_y: float | None = ...,
        offset_top_z: float | None = ...,
        thickness_add_start_x: NonNegativeLength | None = ...,
        thickness_add_end_x: NonNegativeLength | None = ...,
        thickness_add_start_y: NonNegativeLength | None = ...,
        thickness_add_end_y: NonNegativeLength | None = ...,
        condition_bottom: StbColumnConditionBottom | str | None = ...,
        condition_top: StbColumnConditionTop | str | None = ...,
        joint_top: Length | None = ...,
        joint_bottom: Length | None = ...,
        kind_joint_top: StbColumnKindJointTop | str | None = ...,
        kind_joint_bottom: StbColumnKindJointBottom | str | None = ...,
        joint_id_top: PositiveInteger | None = ...,
        joint_id_bottom: PositiveInteger | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node_bottom: PositiveInteger
    """属性(Noneの場合例外) 始端節点ID"""
    id_node_bottom_or_none: PositiveInteger | None
    """属性 始端節点ID"""
    id_node_top: PositiveInteger
    """属性(Noneの場合例外) 終端節点ID"""
    id_node_top_or_none: PositiveInteger | None
    """属性 終端節点ID"""
    rotate: Angle
    """属性(Noneの場合例外) 回転角"""
    rotate_or_none: Angle | None
    """属性 回転角"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    @property
    def kind_structure(self) -> StbColumnKindStructure:
        """属性(Noneの場合例外) 構造種別以下のいずれかの値をとる。RC、S、SRC、CFT、UNDEFINED"""
    @kind_structure.setter
    def kind_structure(self, value: StbColumnKindStructure | str) -> None: ...
    @property
    def kind_structure_or_none(self) -> StbColumnKindStructure | None:
        """属性 構造種別以下のいずれかの値をとる。RC、S、SRC、CFT、UNDEFINED"""
    @kind_structure_or_none.setter
    def kind_structure_or_none(
        self, value: StbColumnKindStructure | str | None
    ) -> None: ...
    offset_bottom_x: float
    """属性(Noneの場合例外) 始端側オフセット（）"""
    offset_bottom_x_or_none: float | None
    """属性 始端側オフセット（）"""
    offset_bottom_y: float
    """属性(Noneの場合例外) 始端側オフセット（）"""
    offset_bottom_y_or_none: float | None
    """属性 始端側オフセット（）"""
    offset_bottom_z: float
    """属性(Noneの場合例外) 始端側オフセット（）"""
    offset_bottom_z_or_none: float | None
    """属性 始端側オフセット（）"""
    offset_top_x: float
    """属性(Noneの場合例外) 終端側オフセット（）"""
    offset_top_x_or_none: float | None
    """属性 終端側オフセット（）"""
    offset_top_y: float
    """属性(Noneの場合例外) 終端側オフセット（）"""
    offset_top_y_or_none: float | None
    """属性 終端側オフセット（）"""
    offset_top_z: float
    """属性(Noneの場合例外) 終端側オフセット（）"""
    offset_top_z_or_none: float | None
    """属性 終端側オフセット（）"""
    thickness_add_start_x: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（X始）"""
    thickness_add_start_x_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（X始）"""
    thickness_add_end_x: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（X終）"""
    thickness_add_end_x_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（X終）"""
    thickness_add_start_y: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（Y始）"""
    thickness_add_start_y_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（Y始）"""
    thickness_add_end_y: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（Y終）"""
    thickness_add_end_y_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（Y終）"""
    @property
    def condition_bottom(self) -> StbColumnConditionBottom:
        """属性(Noneの場合例外)"""
    @condition_bottom.setter
    def condition_bottom(self, value: StbColumnConditionBottom | str) -> None: ...
    @property
    def condition_bottom_or_none(self) -> StbColumnConditionBottom | None:
        """属性"""
    @condition_bottom_or_none.setter
    def condition_bottom_or_none(
        self, value: StbColumnConditionBottom | str | None
    ) -> None: ...
    @property
    def condition_top(self) -> StbColumnConditionTop:
        """属性(Noneの場合例外)"""
    @condition_top.setter
    def condition_top(self, value: StbColumnConditionTop | str) -> None: ...
    @property
    def condition_top_or_none(self) -> StbColumnConditionTop | None:
        """属性"""
    @condition_top_or_none.setter
    def condition_top_or_none(
        self, value: StbColumnConditionTop | str | None
    ) -> None: ...
    joint_top: Length
    """属性(Noneの場合例外)"""
    joint_top_or_none: Length | None
    """属性"""
    joint_bottom: Length
    """属性(Noneの場合例外)"""
    joint_bottom_or_none: Length | None
    """属性"""
    @property
    def kind_joint_top(self) -> StbColumnKindJointTop:
        """属性(Noneの場合例外)"""
    @kind_joint_top.setter
    def kind_joint_top(self, value: StbColumnKindJointTop | str) -> None: ...
    @property
    def kind_joint_top_or_none(self) -> StbColumnKindJointTop | None:
        """属性"""
    @kind_joint_top_or_none.setter
    def kind_joint_top_or_none(
        self, value: StbColumnKindJointTop | str | None
    ) -> None: ...
    @property
    def kind_joint_bottom(self) -> StbColumnKindJointBottom:
        """属性(Noneの場合例外)"""
    @kind_joint_bottom.setter
    def kind_joint_bottom(self, value: StbColumnKindJointBottom | str) -> None: ...
    @property
    def kind_joint_bottom_or_none(self) -> StbColumnKindJointBottom | None:
        """属性"""
    @kind_joint_bottom_or_none.setter
    def kind_joint_bottom_or_none(
        self, value: StbColumnKindJointBottom | str | None
    ) -> None: ...
    joint_id_top: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_top_or_none: PositiveInteger | None
    """属性"""
    joint_id_bottom: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_bottom_or_none: PositiveInteger | None
    """属性"""

class StbPosts(StBridgeElement):
    def __init__(self, *, stb_post: Sequence[StbPost] = ...): ...
    @property
    def stb_post(self) -> list[StbPost]:
        """stb_post (list[StbPost]): 子要素"""
    @stb_post.setter
    def stb_post(self, value: Sequence[StbPost]) -> None: ...

class StbPost(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node_bottom: PositiveInteger | None = ...,
        id_node_top: PositiveInteger | None = ...,
        rotate: Angle | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: StbPostKindStructure | str | None = ...,
        offset_bottom_x: float | None = ...,
        offset_bottom_y: float | None = ...,
        offset_bottom_z: float | None = ...,
        offset_top_x: float | None = ...,
        offset_top_y: float | None = ...,
        offset_top_z: float | None = ...,
        thickness_add_start_x: NonNegativeLength | None = ...,
        thickness_add_end_x: NonNegativeLength | None = ...,
        thickness_add_start_y: NonNegativeLength | None = ...,
        thickness_add_end_y: NonNegativeLength | None = ...,
        condition_bottom: StbPostConditionBottom | str | None = ...,
        condition_top: StbPostConditionTop | str | None = ...,
        joint_top: Length | None = ...,
        joint_bottom: Length | None = ...,
        kind_joint_top: StbPostKindJointTop | str | None = ...,
        kind_joint_bottom: StbPostKindJointBottom | str | None = ...,
        joint_id_top: PositiveInteger | None = ...,
        joint_id_bottom: PositiveInteger | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外)"""
    id_or_none: PositiveInteger | None
    """属性"""
    guid: UUID
    """属性(Noneの場合例外)"""
    guid_or_none: UUID | None
    """属性"""
    name: str
    """属性(Noneの場合例外)"""
    name_or_none: str | None
    """属性"""
    id_node_bottom: PositiveInteger
    """属性(Noneの場合例外)"""
    id_node_bottom_or_none: PositiveInteger | None
    """属性"""
    id_node_top: PositiveInteger
    """属性(Noneの場合例外)"""
    id_node_top_or_none: PositiveInteger | None
    """属性"""
    rotate: Angle
    """属性(Noneの場合例外)"""
    rotate_or_none: Angle | None
    """属性"""
    id_section: PositiveInteger
    """属性(Noneの場合例外)"""
    id_section_or_none: PositiveInteger | None
    """属性"""
    @property
    def kind_structure(self) -> StbPostKindStructure:
        """属性(Noneの場合例外)"""
    @kind_structure.setter
    def kind_structure(self, value: StbPostKindStructure | str) -> None: ...
    @property
    def kind_structure_or_none(self) -> StbPostKindStructure | None:
        """属性"""
    @kind_structure_or_none.setter
    def kind_structure_or_none(
        self, value: StbPostKindStructure | str | None
    ) -> None: ...
    offset_bottom_x: float
    """属性(Noneの場合例外)"""
    offset_bottom_x_or_none: float | None
    """属性"""
    offset_bottom_y: float
    """属性(Noneの場合例外)"""
    offset_bottom_y_or_none: float | None
    """属性"""
    offset_bottom_z: float
    """属性(Noneの場合例外)"""
    offset_bottom_z_or_none: float | None
    """属性"""
    offset_top_x: float
    """属性(Noneの場合例外)"""
    offset_top_x_or_none: float | None
    """属性"""
    offset_top_y: float
    """属性(Noneの場合例外)"""
    offset_top_y_or_none: float | None
    """属性"""
    offset_top_z: float
    """属性(Noneの場合例外)"""
    offset_top_z_or_none: float | None
    """属性"""
    thickness_add_start_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_start_x_or_none: NonNegativeLength | None
    """属性"""
    thickness_add_end_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_end_x_or_none: NonNegativeLength | None
    """属性"""
    thickness_add_start_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_start_y_or_none: NonNegativeLength | None
    """属性"""
    thickness_add_end_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_end_y_or_none: NonNegativeLength | None
    """属性"""
    @property
    def condition_bottom(self) -> StbPostConditionBottom:
        """属性(Noneの場合例外)"""
    @condition_bottom.setter
    def condition_bottom(self, value: StbPostConditionBottom | str) -> None: ...
    @property
    def condition_bottom_or_none(self) -> StbPostConditionBottom | None:
        """属性"""
    @condition_bottom_or_none.setter
    def condition_bottom_or_none(
        self, value: StbPostConditionBottom | str | None
    ) -> None: ...
    @property
    def condition_top(self) -> StbPostConditionTop:
        """属性(Noneの場合例外)"""
    @condition_top.setter
    def condition_top(self, value: StbPostConditionTop | str) -> None: ...
    @property
    def condition_top_or_none(self) -> StbPostConditionTop | None:
        """属性"""
    @condition_top_or_none.setter
    def condition_top_or_none(
        self, value: StbPostConditionTop | str | None
    ) -> None: ...
    joint_top: Length
    """属性(Noneの場合例外)"""
    joint_top_or_none: Length | None
    """属性"""
    joint_bottom: Length
    """属性(Noneの場合例外)"""
    joint_bottom_or_none: Length | None
    """属性"""
    @property
    def kind_joint_top(self) -> StbPostKindJointTop:
        """属性(Noneの場合例外)"""
    @kind_joint_top.setter
    def kind_joint_top(self, value: StbPostKindJointTop | str) -> None: ...
    @property
    def kind_joint_top_or_none(self) -> StbPostKindJointTop | None:
        """属性"""
    @kind_joint_top_or_none.setter
    def kind_joint_top_or_none(
        self, value: StbPostKindJointTop | str | None
    ) -> None: ...
    @property
    def kind_joint_bottom(self) -> StbPostKindJointBottom:
        """属性(Noneの場合例外)"""
    @kind_joint_bottom.setter
    def kind_joint_bottom(self, value: StbPostKindJointBottom | str) -> None: ...
    @property
    def kind_joint_bottom_or_none(self) -> StbPostKindJointBottom | None:
        """属性"""
    @kind_joint_bottom_or_none.setter
    def kind_joint_bottom_or_none(
        self, value: StbPostKindJointBottom | str | None
    ) -> None: ...
    joint_id_top: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_top_or_none: PositiveInteger | None
    """属性"""
    joint_id_bottom: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_bottom_or_none: PositiveInteger | None
    """属性"""

class StbGirders(StBridgeElement):
    def __init__(self, *, stb_girder: Sequence[StbGirder] = ...): ...
    @property
    def stb_girder(self) -> list[StbGirder]:
        """stb_girder (list[StbGirder]): 子要素"""
    @stb_girder.setter
    def stb_girder(self, value: Sequence[StbGirder]) -> None: ...

class StbGirder(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node_start: PositiveInteger | None = ...,
        id_node_end: PositiveInteger | None = ...,
        rotate: Angle | None = ...,
        id_section: PositiveInteger | None = ...,
        section_io_start: StbGirderSectionIoStart | str | None = ...,
        section_io_end: StbGirderSectionIoEnd | str | None = ...,
        kind_structure: StbGirderKindStructure | str | None = ...,
        is_foundation: bool | None = ...,
        offset_start_x: float | None = ...,
        offset_start_y: float | None = ...,
        offset_start_z: float | None = ...,
        offset_end_x: float | None = ...,
        offset_end_y: float | None = ...,
        offset_end_z: float | None = ...,
        thickness_add_top: NonNegativeLength | None = ...,
        thickness_add_bottom: NonNegativeLength | None = ...,
        thickness_add_right: NonNegativeLength | None = ...,
        thickness_add_left: NonNegativeLength | None = ...,
        condition_start: StbGirderConditionStart | str | None = ...,
        condition_end: StbGirderConditionEnd | str | None = ...,
        haunch_start: Length | None = ...,
        haunch_end: Length | None = ...,
        joint_start: Length | None = ...,
        joint_end: Length | None = ...,
        kind_haunch_start: StbGirderKindHaunchStart | str | None = ...,
        kind_haunch_end: StbGirderKindHaunchEnd | str | None = ...,
        type_haunch_h: StbGirderTypeHaunchH | str | None = ...,
        type_haunch_v: StbGirderTypeHaunchV | str | None = ...,
        kind_joint_start: StbGirderKindJointStart | str | None = ...,
        kind_joint_end: StbGirderKindJointEnd | str | None = ...,
        joint_id_start: PositiveInteger | None = ...,
        joint_id_end: PositiveInteger | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node_start: PositiveInteger
    """属性(Noneの場合例外) 始端節点ID"""
    id_node_start_or_none: PositiveInteger | None
    """属性 始端節点ID"""
    id_node_end: PositiveInteger
    """属性(Noneの場合例外) 終端節点ID"""
    id_node_end_or_none: PositiveInteger | None
    """属性 終端節点ID"""
    rotate: Angle
    """属性(Noneの場合例外) 回転角"""
    rotate_or_none: Angle | None
    """属性 回転角"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    @property
    def section_io_start(self) -> StbGirderSectionIoStart:
        """属性(Noneの場合例外) 断面の外端・内端指定以下のいずれかの値をとる。OUT、IN"""
    @section_io_start.setter
    def section_io_start(self, value: StbGirderSectionIoStart | str) -> None: ...
    @property
    def section_io_start_or_none(self) -> StbGirderSectionIoStart | None:
        """属性 断面の外端・内端指定以下のいずれかの値をとる。OUT、IN"""
    @section_io_start_or_none.setter
    def section_io_start_or_none(
        self, value: StbGirderSectionIoStart | str | None
    ) -> None: ...
    @property
    def section_io_end(self) -> StbGirderSectionIoEnd:
        """属性(Noneの場合例外) 断面の外端・内端指定以下のいずれかの値をとる。OUT、IN"""
    @section_io_end.setter
    def section_io_end(self, value: StbGirderSectionIoEnd | str) -> None: ...
    @property
    def section_io_end_or_none(self) -> StbGirderSectionIoEnd | None:
        """属性 断面の外端・内端指定以下のいずれかの値をとる。OUT、IN"""
    @section_io_end_or_none.setter
    def section_io_end_or_none(
        self, value: StbGirderSectionIoEnd | str | None
    ) -> None: ...
    @property
    def kind_structure(self) -> StbGirderKindStructure:
        """属性(Noneの場合例外) 構造種別以下のいずれかの値をとる。RC、S、SRC、UNDEFINED"""
    @kind_structure.setter
    def kind_structure(self, value: StbGirderKindStructure | str) -> None: ...
    @property
    def kind_structure_or_none(self) -> StbGirderKindStructure | None:
        """属性 構造種別以下のいずれかの値をとる。RC、S、SRC、UNDEFINED"""
    @kind_structure_or_none.setter
    def kind_structure_or_none(
        self, value: StbGirderKindStructure | str | None
    ) -> None: ...
    is_foundation: bool
    """属性(Noneの場合例外) 基礎か否か"""
    is_foundation_or_none: bool | None
    """属性 基礎か否か"""
    offset_start_x: float
    """属性(Noneの場合例外) 始端側オフセット（）"""
    offset_start_x_or_none: float | None
    """属性 始端側オフセット（）"""
    offset_start_y: float
    """属性(Noneの場合例外) 始端側オフセット（）"""
    offset_start_y_or_none: float | None
    """属性 始端側オフセット（）"""
    offset_start_z: float
    """属性(Noneの場合例外) 始端側オフセット（）"""
    offset_start_z_or_none: float | None
    """属性 始端側オフセット（）"""
    offset_end_x: float
    """属性(Noneの場合例外) 終端側オフセット（）"""
    offset_end_x_or_none: float | None
    """属性 終端側オフセット（）"""
    offset_end_y: float
    """属性(Noneの場合例外) 終端側オフセット（）"""
    offset_end_y_or_none: float | None
    """属性 終端側オフセット（）"""
    offset_end_z: float
    """属性(Noneの場合例外) 終端側オフセット（）"""
    offset_end_z_or_none: float | None
    """属性 終端側オフセット（）"""
    thickness_add_top: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（上）"""
    thickness_add_top_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（上）"""
    thickness_add_bottom: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（下）"""
    thickness_add_bottom_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（下）"""
    thickness_add_right: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（右）"""
    thickness_add_right_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（右）"""
    thickness_add_left: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（左）"""
    thickness_add_left_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（左）"""
    @property
    def condition_start(self) -> StbGirderConditionStart:
        """属性(Noneの場合例外)"""
    @condition_start.setter
    def condition_start(self, value: StbGirderConditionStart | str) -> None: ...
    @property
    def condition_start_or_none(self) -> StbGirderConditionStart | None:
        """属性"""
    @condition_start_or_none.setter
    def condition_start_or_none(
        self, value: StbGirderConditionStart | str | None
    ) -> None: ...
    @property
    def condition_end(self) -> StbGirderConditionEnd:
        """属性(Noneの場合例外)"""
    @condition_end.setter
    def condition_end(self, value: StbGirderConditionEnd | str) -> None: ...
    @property
    def condition_end_or_none(self) -> StbGirderConditionEnd | None:
        """属性"""
    @condition_end_or_none.setter
    def condition_end_or_none(
        self, value: StbGirderConditionEnd | str | None
    ) -> None: ...
    haunch_start: Length
    """属性(Noneの場合例外)"""
    haunch_start_or_none: Length | None
    """属性"""
    haunch_end: Length
    """属性(Noneの場合例外)"""
    haunch_end_or_none: Length | None
    """属性"""
    joint_start: Length
    """属性(Noneの場合例外)"""
    joint_start_or_none: Length | None
    """属性"""
    joint_end: Length
    """属性(Noneの場合例外)"""
    joint_end_or_none: Length | None
    """属性"""
    @property
    def kind_haunch_start(self) -> StbGirderKindHaunchStart:
        """属性(Noneの場合例外)"""
    @kind_haunch_start.setter
    def kind_haunch_start(self, value: StbGirderKindHaunchStart | str) -> None: ...
    @property
    def kind_haunch_start_or_none(self) -> StbGirderKindHaunchStart | None:
        """属性"""
    @kind_haunch_start_or_none.setter
    def kind_haunch_start_or_none(
        self, value: StbGirderKindHaunchStart | str | None
    ) -> None: ...
    @property
    def kind_haunch_end(self) -> StbGirderKindHaunchEnd:
        """属性(Noneの場合例外)"""
    @kind_haunch_end.setter
    def kind_haunch_end(self, value: StbGirderKindHaunchEnd | str) -> None: ...
    @property
    def kind_haunch_end_or_none(self) -> StbGirderKindHaunchEnd | None:
        """属性"""
    @kind_haunch_end_or_none.setter
    def kind_haunch_end_or_none(
        self, value: StbGirderKindHaunchEnd | str | None
    ) -> None: ...
    @property
    def type_haunch_h(self) -> StbGirderTypeHaunchH:
        """属性(Noneの場合例外)"""
    @type_haunch_h.setter
    def type_haunch_h(self, value: StbGirderTypeHaunchH | str) -> None: ...
    @property
    def type_haunch_h_or_none(self) -> StbGirderTypeHaunchH | None:
        """属性"""
    @type_haunch_h_or_none.setter
    def type_haunch_h_or_none(
        self, value: StbGirderTypeHaunchH | str | None
    ) -> None: ...
    @property
    def type_haunch_v(self) -> StbGirderTypeHaunchV:
        """属性(Noneの場合例外)"""
    @type_haunch_v.setter
    def type_haunch_v(self, value: StbGirderTypeHaunchV | str) -> None: ...
    @property
    def type_haunch_v_or_none(self) -> StbGirderTypeHaunchV | None:
        """属性"""
    @type_haunch_v_or_none.setter
    def type_haunch_v_or_none(
        self, value: StbGirderTypeHaunchV | str | None
    ) -> None: ...
    @property
    def kind_joint_start(self) -> StbGirderKindJointStart:
        """属性(Noneの場合例外)"""
    @kind_joint_start.setter
    def kind_joint_start(self, value: StbGirderKindJointStart | str) -> None: ...
    @property
    def kind_joint_start_or_none(self) -> StbGirderKindJointStart | None:
        """属性"""
    @kind_joint_start_or_none.setter
    def kind_joint_start_or_none(
        self, value: StbGirderKindJointStart | str | None
    ) -> None: ...
    @property
    def kind_joint_end(self) -> StbGirderKindJointEnd:
        """属性(Noneの場合例外)"""
    @kind_joint_end.setter
    def kind_joint_end(self, value: StbGirderKindJointEnd | str) -> None: ...
    @property
    def kind_joint_end_or_none(self) -> StbGirderKindJointEnd | None:
        """属性"""
    @kind_joint_end_or_none.setter
    def kind_joint_end_or_none(
        self, value: StbGirderKindJointEnd | str | None
    ) -> None: ...
    joint_id_start: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_start_or_none: PositiveInteger | None
    """属性"""
    joint_id_end: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_end_or_none: PositiveInteger | None
    """属性"""

class StbBeams(StBridgeElement):
    def __init__(self, *, stb_beam: Sequence[StbBeam] = ...): ...
    @property
    def stb_beam(self) -> list[StbBeam]:
        """stb_beam (list[StbBeam]): 子要素"""
    @stb_beam.setter
    def stb_beam(self, value: Sequence[StbBeam]) -> None: ...

class StbBeam(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node_start: PositiveInteger | None = ...,
        id_node_end: PositiveInteger | None = ...,
        rotate: Angle | None = ...,
        id_section: PositiveInteger | None = ...,
        section_io_start: StbBeamSectionIoStart | str | None = ...,
        section_io_end: StbBeamSectionIoEnd | str | None = ...,
        kind_structure: StbBeamKindStructure | str | None = ...,
        is_foundation: bool | None = ...,
        offset_start_x: float | None = ...,
        offset_start_y: float | None = ...,
        offset_start_z: float | None = ...,
        offset_end_x: float | None = ...,
        offset_end_y: float | None = ...,
        offset_end_z: float | None = ...,
        thickness_add_top: NonNegativeLength | None = ...,
        thickness_add_bottom: NonNegativeLength | None = ...,
        thickness_add_right: NonNegativeLength | None = ...,
        thickness_add_left: NonNegativeLength | None = ...,
        condition_start: StbBeamConditionStart | str | None = ...,
        condition_end: StbBeamConditionEnd | str | None = ...,
        haunch_start: Length | None = ...,
        haunch_end: Length | None = ...,
        joint_start: Length | None = ...,
        joint_end: Length | None = ...,
        kind_haunch_start: StbBeamKindHaunchStart | str | None = ...,
        kind_haunch_end: StbBeamKindHaunchEnd | str | None = ...,
        type_haunch_h: StbBeamTypeHaunchH | str | None = ...,
        type_haunch_v: StbBeamTypeHaunchV | str | None = ...,
        kind_joint_start: StbBeamKindJointStart | str | None = ...,
        kind_joint_end: StbBeamKindJointEnd | str | None = ...,
        joint_id_start: PositiveInteger | None = ...,
        joint_id_end: PositiveInteger | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外)"""
    id_or_none: PositiveInteger | None
    """属性"""
    guid: UUID
    """属性(Noneの場合例外)"""
    guid_or_none: UUID | None
    """属性"""
    name: str
    """属性(Noneの場合例外)"""
    name_or_none: str | None
    """属性"""
    id_node_start: PositiveInteger
    """属性(Noneの場合例外)"""
    id_node_start_or_none: PositiveInteger | None
    """属性"""
    id_node_end: PositiveInteger
    """属性(Noneの場合例外)"""
    id_node_end_or_none: PositiveInteger | None
    """属性"""
    rotate: Angle
    """属性(Noneの場合例外)"""
    rotate_or_none: Angle | None
    """属性"""
    id_section: PositiveInteger
    """属性(Noneの場合例外)"""
    id_section_or_none: PositiveInteger | None
    """属性"""
    @property
    def section_io_start(self) -> StbBeamSectionIoStart:
        """属性(Noneの場合例外)"""
    @section_io_start.setter
    def section_io_start(self, value: StbBeamSectionIoStart | str) -> None: ...
    @property
    def section_io_start_or_none(self) -> StbBeamSectionIoStart | None:
        """属性"""
    @section_io_start_or_none.setter
    def section_io_start_or_none(
        self, value: StbBeamSectionIoStart | str | None
    ) -> None: ...
    @property
    def section_io_end(self) -> StbBeamSectionIoEnd:
        """属性(Noneの場合例外)"""
    @section_io_end.setter
    def section_io_end(self, value: StbBeamSectionIoEnd | str) -> None: ...
    @property
    def section_io_end_or_none(self) -> StbBeamSectionIoEnd | None:
        """属性"""
    @section_io_end_or_none.setter
    def section_io_end_or_none(
        self, value: StbBeamSectionIoEnd | str | None
    ) -> None: ...
    @property
    def kind_structure(self) -> StbBeamKindStructure:
        """属性(Noneの場合例外)"""
    @kind_structure.setter
    def kind_structure(self, value: StbBeamKindStructure | str) -> None: ...
    @property
    def kind_structure_or_none(self) -> StbBeamKindStructure | None:
        """属性"""
    @kind_structure_or_none.setter
    def kind_structure_or_none(
        self, value: StbBeamKindStructure | str | None
    ) -> None: ...
    is_foundation: bool
    """属性(Noneの場合例外)"""
    is_foundation_or_none: bool | None
    """属性"""
    offset_start_x: float
    """属性(Noneの場合例外)"""
    offset_start_x_or_none: float | None
    """属性"""
    offset_start_y: float
    """属性(Noneの場合例外)"""
    offset_start_y_or_none: float | None
    """属性"""
    offset_start_z: float
    """属性(Noneの場合例外)"""
    offset_start_z_or_none: float | None
    """属性"""
    offset_end_x: float
    """属性(Noneの場合例外)"""
    offset_end_x_or_none: float | None
    """属性"""
    offset_end_y: float
    """属性(Noneの場合例外)"""
    offset_end_y_or_none: float | None
    """属性"""
    offset_end_z: float
    """属性(Noneの場合例外)"""
    offset_end_z_or_none: float | None
    """属性"""
    thickness_add_top: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_top_or_none: NonNegativeLength | None
    """属性"""
    thickness_add_bottom: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_bottom_or_none: NonNegativeLength | None
    """属性"""
    thickness_add_right: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_right_or_none: NonNegativeLength | None
    """属性"""
    thickness_add_left: NonNegativeLength
    """属性(Noneの場合例外)"""
    thickness_add_left_or_none: NonNegativeLength | None
    """属性"""
    @property
    def condition_start(self) -> StbBeamConditionStart:
        """属性(Noneの場合例外)"""
    @condition_start.setter
    def condition_start(self, value: StbBeamConditionStart | str) -> None: ...
    @property
    def condition_start_or_none(self) -> StbBeamConditionStart | None:
        """属性"""
    @condition_start_or_none.setter
    def condition_start_or_none(
        self, value: StbBeamConditionStart | str | None
    ) -> None: ...
    @property
    def condition_end(self) -> StbBeamConditionEnd:
        """属性(Noneの場合例外)"""
    @condition_end.setter
    def condition_end(self, value: StbBeamConditionEnd | str) -> None: ...
    @property
    def condition_end_or_none(self) -> StbBeamConditionEnd | None:
        """属性"""
    @condition_end_or_none.setter
    def condition_end_or_none(
        self, value: StbBeamConditionEnd | str | None
    ) -> None: ...
    haunch_start: Length
    """属性(Noneの場合例外)"""
    haunch_start_or_none: Length | None
    """属性"""
    haunch_end: Length
    """属性(Noneの場合例外)"""
    haunch_end_or_none: Length | None
    """属性"""
    joint_start: Length
    """属性(Noneの場合例外)"""
    joint_start_or_none: Length | None
    """属性"""
    joint_end: Length
    """属性(Noneの場合例外)"""
    joint_end_or_none: Length | None
    """属性"""
    @property
    def kind_haunch_start(self) -> StbBeamKindHaunchStart:
        """属性(Noneの場合例外)"""
    @kind_haunch_start.setter
    def kind_haunch_start(self, value: StbBeamKindHaunchStart | str) -> None: ...
    @property
    def kind_haunch_start_or_none(self) -> StbBeamKindHaunchStart | None:
        """属性"""
    @kind_haunch_start_or_none.setter
    def kind_haunch_start_or_none(
        self, value: StbBeamKindHaunchStart | str | None
    ) -> None: ...
    @property
    def kind_haunch_end(self) -> StbBeamKindHaunchEnd:
        """属性(Noneの場合例外)"""
    @kind_haunch_end.setter
    def kind_haunch_end(self, value: StbBeamKindHaunchEnd | str) -> None: ...
    @property
    def kind_haunch_end_or_none(self) -> StbBeamKindHaunchEnd | None:
        """属性"""
    @kind_haunch_end_or_none.setter
    def kind_haunch_end_or_none(
        self, value: StbBeamKindHaunchEnd | str | None
    ) -> None: ...
    @property
    def type_haunch_h(self) -> StbBeamTypeHaunchH:
        """属性(Noneの場合例外)"""
    @type_haunch_h.setter
    def type_haunch_h(self, value: StbBeamTypeHaunchH | str) -> None: ...
    @property
    def type_haunch_h_or_none(self) -> StbBeamTypeHaunchH | None:
        """属性"""
    @type_haunch_h_or_none.setter
    def type_haunch_h_or_none(self, value: StbBeamTypeHaunchH | str | None) -> None: ...
    @property
    def type_haunch_v(self) -> StbBeamTypeHaunchV:
        """属性(Noneの場合例外)"""
    @type_haunch_v.setter
    def type_haunch_v(self, value: StbBeamTypeHaunchV | str) -> None: ...
    @property
    def type_haunch_v_or_none(self) -> StbBeamTypeHaunchV | None:
        """属性"""
    @type_haunch_v_or_none.setter
    def type_haunch_v_or_none(self, value: StbBeamTypeHaunchV | str | None) -> None: ...
    @property
    def kind_joint_start(self) -> StbBeamKindJointStart:
        """属性(Noneの場合例外)"""
    @kind_joint_start.setter
    def kind_joint_start(self, value: StbBeamKindJointStart | str) -> None: ...
    @property
    def kind_joint_start_or_none(self) -> StbBeamKindJointStart | None:
        """属性"""
    @kind_joint_start_or_none.setter
    def kind_joint_start_or_none(
        self, value: StbBeamKindJointStart | str | None
    ) -> None: ...
    @property
    def kind_joint_end(self) -> StbBeamKindJointEnd:
        """属性(Noneの場合例外)"""
    @kind_joint_end.setter
    def kind_joint_end(self, value: StbBeamKindJointEnd | str) -> None: ...
    @property
    def kind_joint_end_or_none(self) -> StbBeamKindJointEnd | None:
        """属性"""
    @kind_joint_end_or_none.setter
    def kind_joint_end_or_none(
        self, value: StbBeamKindJointEnd | str | None
    ) -> None: ...
    joint_id_start: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_start_or_none: PositiveInteger | None
    """属性"""
    joint_id_end: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_end_or_none: PositiveInteger | None
    """属性"""

class StbBraces(StBridgeElement):
    def __init__(self, *, stb_brace: Sequence[StbBrace] = ...): ...
    @property
    def stb_brace(self) -> list[StbBrace]:
        """stb_brace (list[StbBrace]): 子要素"""
    @stb_brace.setter
    def stb_brace(self, value: Sequence[StbBrace]) -> None: ...

class StbBrace(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node_start: PositiveInteger | None = ...,
        id_node_end: PositiveInteger | None = ...,
        rotate: Angle | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: StbBraceKindStructure | str | None = ...,
        offset_start_x: float | None = ...,
        offset_start_y: float | None = ...,
        offset_start_z: float | None = ...,
        offset_end_x: float | None = ...,
        offset_end_y: float | None = ...,
        offset_end_z: float | None = ...,
        condition_start: StbBraceConditionStart | str | None = ...,
        condition_end: StbBraceConditionEnd | str | None = ...,
        feature_brace: StbBraceFeatureBrace | str | None = ...,
        joint_start: Length | None = ...,
        joint_end: Length | None = ...,
        kind_joint_start: StbBraceKindJointStart | str | None = ...,
        kind_joint_end: StbBraceKindJointEnd | str | None = ...,
        joint_id_start: PositiveInteger | None = ...,
        joint_id_end: PositiveInteger | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node_start: PositiveInteger
    """属性(Noneの場合例外) 始端節点ID"""
    id_node_start_or_none: PositiveInteger | None
    """属性 始端節点ID"""
    id_node_end: PositiveInteger
    """属性(Noneの場合例外) 終端節点ID"""
    id_node_end_or_none: PositiveInteger | None
    """属性 終端節点ID"""
    rotate: Angle
    """属性(Noneの場合例外) 回転角"""
    rotate_or_none: Angle | None
    """属性 回転角"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    @property
    def kind_structure(self) -> StbBraceKindStructure:
        """属性(Noneの場合例外) 構造種別RC、S、SRCのいずれかの値"""
    @kind_structure.setter
    def kind_structure(self, value: StbBraceKindStructure | str) -> None: ...
    @property
    def kind_structure_or_none(self) -> StbBraceKindStructure | None:
        """属性 構造種別RC、S、SRCのいずれかの値"""
    @kind_structure_or_none.setter
    def kind_structure_or_none(
        self, value: StbBraceKindStructure | str | None
    ) -> None: ...
    offset_start_x: float
    """属性(Noneの場合例外)"""
    offset_start_x_or_none: float | None
    """属性"""
    offset_start_y: float
    """属性(Noneの場合例外)"""
    offset_start_y_or_none: float | None
    """属性"""
    offset_start_z: float
    """属性(Noneの場合例外)"""
    offset_start_z_or_none: float | None
    """属性"""
    offset_end_x: float
    """属性(Noneの場合例外)"""
    offset_end_x_or_none: float | None
    """属性"""
    offset_end_y: float
    """属性(Noneの場合例外)"""
    offset_end_y_or_none: float | None
    """属性"""
    offset_end_z: float
    """属性(Noneの場合例外)"""
    offset_end_z_or_none: float | None
    """属性"""
    @property
    def condition_start(self) -> StbBraceConditionStart:
        """属性(Noneの場合例外)"""
    @condition_start.setter
    def condition_start(self, value: StbBraceConditionStart | str) -> None: ...
    @property
    def condition_start_or_none(self) -> StbBraceConditionStart | None:
        """属性"""
    @condition_start_or_none.setter
    def condition_start_or_none(
        self, value: StbBraceConditionStart | str | None
    ) -> None: ...
    @property
    def condition_end(self) -> StbBraceConditionEnd:
        """属性(Noneの場合例外)"""
    @condition_end.setter
    def condition_end(self, value: StbBraceConditionEnd | str) -> None: ...
    @property
    def condition_end_or_none(self) -> StbBraceConditionEnd | None:
        """属性"""
    @condition_end_or_none.setter
    def condition_end_or_none(
        self, value: StbBraceConditionEnd | str | None
    ) -> None: ...
    @property
    def feature_brace(self) -> StbBraceFeatureBrace:
        """属性(Noneの場合例外) ブレース特性引張り：TENSION、引張り圧縮：TENSIONANDCOMPRESSIONのいずれかの値"""
    @feature_brace.setter
    def feature_brace(self, value: StbBraceFeatureBrace | str) -> None: ...
    @property
    def feature_brace_or_none(self) -> StbBraceFeatureBrace | None:
        """属性 ブレース特性引張り：TENSION、引張り圧縮：TENSIONANDCOMPRESSIONのいずれかの値"""
    @feature_brace_or_none.setter
    def feature_brace_or_none(
        self, value: StbBraceFeatureBrace | str | None
    ) -> None: ...
    joint_start: Length
    """属性(Noneの場合例外)"""
    joint_start_or_none: Length | None
    """属性"""
    joint_end: Length
    """属性(Noneの場合例外)"""
    joint_end_or_none: Length | None
    """属性"""
    @property
    def kind_joint_start(self) -> StbBraceKindJointStart:
        """属性(Noneの場合例外)"""
    @kind_joint_start.setter
    def kind_joint_start(self, value: StbBraceKindJointStart | str) -> None: ...
    @property
    def kind_joint_start_or_none(self) -> StbBraceKindJointStart | None:
        """属性"""
    @kind_joint_start_or_none.setter
    def kind_joint_start_or_none(
        self, value: StbBraceKindJointStart | str | None
    ) -> None: ...
    @property
    def kind_joint_end(self) -> StbBraceKindJointEnd:
        """属性(Noneの場合例外)"""
    @kind_joint_end.setter
    def kind_joint_end(self, value: StbBraceKindJointEnd | str) -> None: ...
    @property
    def kind_joint_end_or_none(self) -> StbBraceKindJointEnd | None:
        """属性"""
    @kind_joint_end_or_none.setter
    def kind_joint_end_or_none(
        self, value: StbBraceKindJointEnd | str | None
    ) -> None: ...
    joint_id_start: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_start_or_none: PositiveInteger | None
    """属性"""
    joint_id_end: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_end_or_none: PositiveInteger | None
    """属性"""

class StbSlabs(StBridgeElement):
    def __init__(self, *, stb_slab: Sequence[StbSlab] = ...): ...
    @property
    def stb_slab(self) -> list[StbSlab]:
        """stb_slab (list[StbSlab]): 子要素"""
    @stb_slab.setter
    def stb_slab(self, value: Sequence[StbSlab]) -> None: ...

class StbSlab(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: StbSlabKindStructure | str | None = ...,
        kind_slab: StbSlabKindSlab | str | None = ...,
        thickness_add_top: NonNegativeLength | None = ...,
        thickness_add_bottom: NonNegativeLength | None = ...,
        direction_load: StbSlabDirectionLoad | str | None = ...,
        angle_load: Angle | None = ...,
        angle_main_bar_direction: Angle | None = ...,
        is_foundation: bool | None = ...,
        type_haunch: StbSlabTypeHaunch | str | None = ...,
        stb_node_id_order: StbNodeIdOrder | None = ...,
        stb_slab_offset_list: StbSlabOffsetList | None = ...,
        stb_open_id_list: StbOpenIdList | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    @property
    def kind_structure(self) -> StbSlabKindStructure:
        """属性(Noneの場合例外) 構造種別以下のいずれかの値をとる。RC（RCスラブ）DECK（デッキ合成スラブ）PRECAST（既製スラブ）LOAD(荷重のみ)"""
    @kind_structure.setter
    def kind_structure(self, value: StbSlabKindStructure | str) -> None: ...
    @property
    def kind_structure_or_none(self) -> StbSlabKindStructure | None:
        """属性 構造種別以下のいずれかの値をとる。RC（RCスラブ）DECK（デッキ合成スラブ）PRECAST（既製スラブ）LOAD(荷重のみ)"""
    @kind_structure_or_none.setter
    def kind_structure_or_none(
        self, value: StbSlabKindStructure | str | None
    ) -> None: ...
    @property
    def kind_slab(self) -> StbSlabKindSlab:
        """属性(Noneの場合例外) スラブ種類以下のいずれかの値をとる。NORMAL、CANTI"""
    @kind_slab.setter
    def kind_slab(self, value: StbSlabKindSlab | str) -> None: ...
    @property
    def kind_slab_or_none(self) -> StbSlabKindSlab | None:
        """属性 スラブ種類以下のいずれかの値をとる。NORMAL、CANTI"""
    @kind_slab_or_none.setter
    def kind_slab_or_none(self, value: StbSlabKindSlab | str | None) -> None: ...
    thickness_add_top: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（上）"""
    thickness_add_top_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（上）"""
    thickness_add_bottom: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（下）"""
    thickness_add_bottom_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（下）"""
    @property
    def direction_load(self) -> StbSlabDirectionLoad:
        """属性(Noneの場合例外) 荷重伝達方向以下のいずれかの値をとる。1WAY、2WAY"""
    @direction_load.setter
    def direction_load(self, value: StbSlabDirectionLoad | str) -> None: ...
    @property
    def direction_load_or_none(self) -> StbSlabDirectionLoad | None:
        """属性 荷重伝達方向以下のいずれかの値をとる。1WAY、2WAY"""
    @direction_load_or_none.setter
    def direction_load_or_none(
        self, value: StbSlabDirectionLoad | str | None
    ) -> None: ...
    angle_load: Angle
    """属性(Noneの場合例外) 荷重伝達方向「1WAY」の場合の角度"""
    angle_load_or_none: Angle | None
    """属性 荷重伝達方向「1WAY」の場合の角度"""
    angle_main_bar_direction: Angle
    """属性(Noneの場合例外) 主筋方向角度"""
    angle_main_bar_direction_or_none: Angle | None
    """属性 主筋方向角度"""
    is_foundation: bool
    """属性(Noneの場合例外) 基礎か否か"""
    is_foundation_or_none: bool | None
    """属性 基礎か否か"""
    @property
    def type_haunch(self) -> StbSlabTypeHaunch:
        """属性(Noneの場合例外)"""
    @type_haunch.setter
    def type_haunch(self, value: StbSlabTypeHaunch | str) -> None: ...
    @property
    def type_haunch_or_none(self) -> StbSlabTypeHaunch | None:
        """属性"""
    @type_haunch_or_none.setter
    def type_haunch_or_none(self, value: StbSlabTypeHaunch | str | None) -> None: ...
    stb_node_id_order: StbNodeIdOrder
    """子要素(Noneの場合例外)"""
    stb_node_id_order_or_none: StbNodeIdOrder | None
    """子要素"""
    stb_slab_offset_list: StbSlabOffsetList
    """子要素(Noneの場合例外)"""
    stb_slab_offset_list_or_none: StbSlabOffsetList | None
    """子要素"""
    stb_open_id_list: StbOpenIdList
    """子要素(Noneの場合例外)"""
    stb_open_id_list_or_none: StbOpenIdList | None
    """子要素"""
    @property
    def ensure(self) -> _StbSlabEnsureAccessor: ...

class StbSlabOffsetList(StBridgeElement):
    def __init__(self, *, stb_slab_offset: Sequence[StbSlabOffset] = ...): ...
    @property
    def stb_slab_offset(self) -> list[StbSlabOffset]:
        """stb_slab_offset (list[StbSlabOffset]): 子要素"""
    @stb_slab_offset.setter
    def stb_slab_offset(self, value: Sequence[StbSlabOffset]) -> None: ...

class StbSlabOffset(StBridgeElement):
    def __init__(
        self,
        *,
        id_node: PositiveInteger | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
        offset_z: float | None = ...,
    ): ...
    id_node: PositiveInteger
    """属性(Noneの場合例外) 節点ID"""
    id_node_or_none: PositiveInteger | None
    """属性 節点ID"""
    offset_x: float
    """属性(Noneの場合例外) 方向のオフセット"""
    offset_x_or_none: float | None
    """属性 方向のオフセット"""
    offset_y: float
    """属性(Noneの場合例外) 方向のオフセット"""
    offset_y_or_none: float | None
    """属性 方向のオフセット"""
    offset_z: float
    """属性(Noneの場合例外) 方向のオフセット"""
    offset_z_or_none: float | None
    """属性 方向のオフセット"""

class StbWalls(StBridgeElement):
    def __init__(self, *, stb_wall: Sequence[StbWall] = ...): ...
    @property
    def stb_wall(self) -> list[StbWall]:
        """stb_wall (list[StbWall]): 子要素"""
    @stb_wall.setter
    def stb_wall(self, value: Sequence[StbWall]) -> None: ...

class StbWall(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: str | None = ...,
        kind_layout: StbWallKindLayout | str | None = ...,
        thickness_add_right: NonNegativeLength | None = ...,
        thickness_add_left: NonNegativeLength | None = ...,
        kind_wall: StbWallKindWall | str | None = ...,
        slit_upper: Length | None = ...,
        slit_bottom: Length | None = ...,
        slit_right: Length | None = ...,
        slit_left: Length | None = ...,
        type_outside: StbWallTypeOutside | str | None = ...,
        is_press: bool | None = ...,
        stb_node_id_order: StbNodeIdOrder | None = ...,
        stb_wall_offset_list: StbWallOffsetList | None = ...,
        stb_open_id_list: StbOpenIdList | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    kind_structure: str
    """属性(Noneの場合例外) 構造種別以下のいずれかの値をとる。RC(RC壁)LOAD(荷重のみ)"""
    kind_structure_or_none: str | None
    """属性 構造種別以下のいずれかの値をとる。RC(RC壁)LOAD(荷重のみ)"""
    @property
    def kind_layout(self) -> StbWallKindLayout:
        """属性(Noneの場合例外) 壁種別以下のいずれかの値をとる。ON_GIRDER（大梁上）、ON_BEAM（小梁上）、ON_SLAB（スラブ上）"""
    @kind_layout.setter
    def kind_layout(self, value: StbWallKindLayout | str) -> None: ...
    @property
    def kind_layout_or_none(self) -> StbWallKindLayout | None:
        """属性 壁種別以下のいずれかの値をとる。ON_GIRDER（大梁上）、ON_BEAM（小梁上）、ON_SLAB（スラブ上）"""
    @kind_layout_or_none.setter
    def kind_layout_or_none(self, value: StbWallKindLayout | str | None) -> None: ...
    thickness_add_right: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（右）"""
    thickness_add_right_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（右）"""
    thickness_add_left: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（左）"""
    thickness_add_left_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（左）"""
    @property
    def kind_wall(self) -> StbWallKindWall:
        """属性(Noneの場合例外) 耐力区分以下のいずれかの値をとる。WALL_NORMAL（一般壁）、WALL_SHEAR（耐力壁）"""
    @kind_wall.setter
    def kind_wall(self, value: StbWallKindWall | str) -> None: ...
    @property
    def kind_wall_or_none(self) -> StbWallKindWall | None:
        """属性 耐力区分以下のいずれかの値をとる。WALL_NORMAL（一般壁）、WALL_SHEAR（耐力壁）"""
    @kind_wall_or_none.setter
    def kind_wall_or_none(self, value: StbWallKindWall | str | None) -> None: ...
    slit_upper: Length
    """属性(Noneの場合例外) 構造スリット（上）"""
    slit_upper_or_none: Length | None
    """属性 構造スリット（上）"""
    slit_bottom: Length
    """属性(Noneの場合例外) 構造スリット（下）"""
    slit_bottom_or_none: Length | None
    """属性 構造スリット（下）"""
    slit_right: Length
    """属性(Noneの場合例外) 構造スリット（右）"""
    slit_right_or_none: Length | None
    """属性 構造スリット（右）"""
    slit_left: Length
    """属性(Noneの場合例外) 構造スリット（左）"""
    slit_left_or_none: Length | None
    """属性 構造スリット（左）"""
    @property
    def type_outside(self) -> StbWallTypeOutside:
        """属性(Noneの場合例外)"""
    @type_outside.setter
    def type_outside(self, value: StbWallTypeOutside | str) -> None: ...
    @property
    def type_outside_or_none(self) -> StbWallTypeOutside | None:
        """属性"""
    @type_outside_or_none.setter
    def type_outside_or_none(self, value: StbWallTypeOutside | str | None) -> None: ...
    is_press: bool
    """属性(Noneの場合例外)"""
    is_press_or_none: bool | None
    """属性"""
    stb_node_id_order: StbNodeIdOrder
    """子要素(Noneの場合例外)"""
    stb_node_id_order_or_none: StbNodeIdOrder | None
    """子要素"""
    stb_wall_offset_list: StbWallOffsetList
    """子要素(Noneの場合例外)"""
    stb_wall_offset_list_or_none: StbWallOffsetList | None
    """子要素"""
    stb_open_id_list: StbOpenIdList
    """子要素(Noneの場合例外)"""
    stb_open_id_list_or_none: StbOpenIdList | None
    """子要素"""
    @property
    def ensure(self) -> _StbWallEnsureAccessor: ...

class StbWallOffsetList(StBridgeElement):
    def __init__(self, *, stb_wall_offset: Sequence[StbWallOffset] = ...): ...
    @property
    def stb_wall_offset(self) -> list[StbWallOffset]:
        """stb_wall_offset (list[StbWallOffset]): 子要素"""
    @stb_wall_offset.setter
    def stb_wall_offset(self, value: Sequence[StbWallOffset]) -> None: ...

class StbWallOffset(StBridgeElement):
    def __init__(
        self,
        *,
        id_node: PositiveInteger | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
        offset_z: float | None = ...,
    ): ...
    id_node: PositiveInteger
    """属性(Noneの場合例外) 節点ID"""
    id_node_or_none: PositiveInteger | None
    """属性 節点ID"""
    offset_x: float
    """属性(Noneの場合例外) 方向のオフセット"""
    offset_x_or_none: float | None
    """属性 方向のオフセット"""
    offset_y: float
    """属性(Noneの場合例外) 方向のオフセット"""
    offset_y_or_none: float | None
    """属性 方向のオフセット"""
    offset_z: float
    """属性(Noneの場合例外) 方向のオフセット"""
    offset_z_or_none: float | None
    """属性 方向のオフセット"""

class StbFootings(StBridgeElement):
    def __init__(self, *, stb_footing: Sequence[StbFooting] = ...): ...
    @property
    def stb_footing(self) -> list[StbFooting]:
        """stb_footing (list[StbFooting]): 子要素"""
    @stb_footing.setter
    def stb_footing(self, value: Sequence[StbFooting]) -> None: ...

class StbFooting(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node: PositiveInteger | None = ...,
        rotate: Angle | None = ...,
        id_section: PositiveInteger | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
        level_bottom: float | None = ...,
        thickness_add_start_x: NonNegativeLength | None = ...,
        thickness_add_end_x: NonNegativeLength | None = ...,
        thickness_add_start_y: NonNegativeLength | None = ...,
        thickness_add_end_y: NonNegativeLength | None = ...,
        thickness_add_top: NonNegativeLength | None = ...,
        thickness_add_bottom: NonNegativeLength | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node: PositiveInteger
    """属性(Noneの場合例外) 節点ID"""
    id_node_or_none: PositiveInteger | None
    """属性 節点ID"""
    rotate: Angle
    """属性(Noneの場合例外) 回転角"""
    rotate_or_none: Angle | None
    """属性 回転角"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    offset_x: float
    """属性(Noneの場合例外) オフセット（）"""
    offset_x_or_none: float | None
    """属性 オフセット（）"""
    offset_y: float
    """属性(Noneの場合例外) オフセット（）"""
    offset_y_or_none: float | None
    """属性 オフセット（）"""
    level_bottom: float
    """属性(Noneの場合例外) レベル（下）"""
    level_bottom_or_none: float | None
    """属性 レベル（下）"""
    thickness_add_start_x: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（X始）"""
    thickness_add_start_x_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（X始）"""
    thickness_add_end_x: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（X終）"""
    thickness_add_end_x_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（X終）"""
    thickness_add_start_y: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（Y始）"""
    thickness_add_start_y_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（Y始）"""
    thickness_add_end_y: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（Y終）"""
    thickness_add_end_y_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（Y終）"""
    thickness_add_top: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（上）"""
    thickness_add_top_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（上）"""
    thickness_add_bottom: NonNegativeLength
    """属性(Noneの場合例外) ふかし厚さ（下）"""
    thickness_add_bottom_or_none: NonNegativeLength | None
    """属性 ふかし厚さ（下）"""

class StbStripFootings(StBridgeElement):
    def __init__(self, *, stb_strip_footing: Sequence[StbStripFooting] = ...): ...
    @property
    def stb_strip_footing(self) -> list[StbStripFooting]:
        """stb_strip_footing (list[StbStripFooting]): 子要素"""
    @stb_strip_footing.setter
    def stb_strip_footing(self, value: Sequence[StbStripFooting]) -> None: ...

class StbStripFooting(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node_start: PositiveInteger | None = ...,
        id_node_end: PositiveInteger | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: str | None = ...,
        level: float | None = ...,
        offset: float | None = ...,
        length_ex_start: float | None = ...,
        length_ex_end: float | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node_start: PositiveInteger
    """属性(Noneの場合例外) 始端節点ID"""
    id_node_start_or_none: PositiveInteger | None
    """属性 始端節点ID"""
    id_node_end: PositiveInteger
    """属性(Noneの場合例外) 終端節点ID"""
    id_node_end_or_none: PositiveInteger | None
    """属性 終端節点ID"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    kind_structure: str
    """属性(Noneの場合例外) 構造種別"""
    kind_structure_or_none: str | None
    """属性 構造種別"""
    level: float
    """属性(Noneの場合例外) レベル"""
    level_or_none: float | None
    """属性 レベル"""
    offset: float
    """属性(Noneの場合例外) オフセット"""
    offset_or_none: float | None
    """属性 オフセット"""
    length_ex_start: float
    """属性(Noneの場合例外) 始点側余長"""
    length_ex_start_or_none: float | None
    """属性 始点側余長"""
    length_ex_end: float
    """属性(Noneの場合例外) 終点側余長"""
    length_ex_end_or_none: float | None
    """属性 終点側余長"""

class StbPiles(StBridgeElement):
    def __init__(self, *, stb_pile: Sequence[StbPile] = ...): ...
    @property
    def stb_pile(self) -> list[StbPile]:
        """stb_pile (list[StbPile]): 子要素"""
    @stb_pile.setter
    def stb_pile(self, value: Sequence[StbPile]) -> None: ...

class StbPile(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node: PositiveInteger | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: StbPileKindStructure | str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
        level_top: float | None = ...,
        length_all: Length | None = ...,
        length_head: Length | None = ...,
        length_foot: Length | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node: PositiveInteger
    """属性(Noneの場合例外) 節点ID"""
    id_node_or_none: PositiveInteger | None
    """属性 節点ID"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    @property
    def kind_structure(self) -> StbPileKindStructure:
        """属性(Noneの場合例外) 構造種別以下のいずれかの値をとる。RC、S、PC"""
    @kind_structure.setter
    def kind_structure(self, value: StbPileKindStructure | str) -> None: ...
    @property
    def kind_structure_or_none(self) -> StbPileKindStructure | None:
        """属性 構造種別以下のいずれかの値をとる。RC、S、PC"""
    @kind_structure_or_none.setter
    def kind_structure_or_none(
        self, value: StbPileKindStructure | str | None
    ) -> None: ...
    offset_x: float
    """属性(Noneの場合例外) オフセット（）"""
    offset_x_or_none: float | None
    """属性 オフセット（）"""
    offset_y: float
    """属性(Noneの場合例外) オフセット（）"""
    offset_y_or_none: float | None
    """属性 オフセット（）"""
    level_top: float
    """属性(Noneの場合例外) レベル（杭天）"""
    level_top_or_none: float | None
    """属性 レベル（杭天）"""
    length_all: Length
    """属性(Noneの場合例外) 杭全長"""
    length_all_or_none: Length | None
    """属性 杭全長"""
    length_head: Length
    """属性(Noneの場合例外) 杭頭（拡頭）長さ"""
    length_head_or_none: Length | None
    """属性 杭頭（拡頭）長さ"""
    length_foot: Length
    """属性(Noneの場合例外) 杭脚長さ"""
    length_foot_or_none: Length | None
    """属性 杭脚長さ"""

class StbFoundationColumns(StBridgeElement):
    def __init__(
        self, *, stb_foundation_column: Sequence[StbFoundationColumn] = ...
    ): ...
    @property
    def stb_foundation_column(self) -> list[StbFoundationColumn]:
        """stb_foundation_column (list[StbFoundationColumn]): 子要素"""
    @stb_foundation_column.setter
    def stb_foundation_column(self, value: Sequence[StbFoundationColumn]) -> None: ...

class StbFoundationColumn(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node: PositiveInteger | None = ...,
        rotate: Angle | None = ...,
        offset_z: float | None = ...,
        kind_structure: str | None = ...,
        id_section_fd: PositiveInteger | None = ...,
        length_fd: Length | None = ...,
        offset_fd_x: float | None = ...,
        offset_fd_y: float | None = ...,
        thickness_add_fd_start_x: NonNegativeLength | None = ...,
        thickness_add_fd_end_x: NonNegativeLength | None = ...,
        thickness_add_fd_start_y: NonNegativeLength | None = ...,
        thickness_add_fd_end_y: NonNegativeLength | None = ...,
        id_section_wr: PositiveInteger | None = ...,
        length_wr: Length | None = ...,
        offset_wr_x: float | None = ...,
        offset_wr_y: float | None = ...,
        thickness_add_wr_start_x: NonNegativeLength | None = ...,
        thickness_add_wr_end_x: NonNegativeLength | None = ...,
        thickness_add_wr_start_y: NonNegativeLength | None = ...,
        thickness_add_wr_end_y: NonNegativeLength | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node: PositiveInteger
    """属性(Noneの場合例外) 節点ID"""
    id_node_or_none: PositiveInteger | None
    """属性 節点ID"""
    rotate: Angle
    """属性(Noneの場合例外) 回転角"""
    rotate_or_none: Angle | None
    """属性 回転角"""
    offset_z: float
    """属性(Noneの場合例外) 基礎柱・根巻柱の基準点のオフセット（）"""
    offset_z_or_none: float | None
    """属性 基礎柱・根巻柱の基準点のオフセット（）"""
    kind_structure: str
    """属性(Noneの場合例外) 構造種別以下の値をとる。RC"""
    kind_structure_or_none: str | None
    """属性 構造種別以下の値をとる。RC"""
    id_section_fd: PositiveInteger
    """属性(Noneの場合例外) 基礎柱断面ＩＤ"""
    id_section_fd_or_none: PositiveInteger | None
    """属性 基礎柱断面ＩＤ"""
    length_fd: Length
    """属性(Noneの場合例外) 基礎柱高さ"""
    length_fd_or_none: Length | None
    """属性 基礎柱高さ"""
    offset_fd_x: float
    """属性(Noneの場合例外) 基礎柱オフセット（）"""
    offset_fd_x_or_none: float | None
    """属性 基礎柱オフセット（）"""
    offset_fd_y: float
    """属性(Noneの場合例外) 基礎柱オフセット（）"""
    offset_fd_y_or_none: float | None
    """属性 基礎柱オフセット（）"""
    thickness_add_fd_start_x: NonNegativeLength
    """属性(Noneの場合例外) 基礎柱ふかし厚さ（X始）"""
    thickness_add_fd_start_x_or_none: NonNegativeLength | None
    """属性 基礎柱ふかし厚さ（X始）"""
    thickness_add_fd_end_x: NonNegativeLength
    """属性(Noneの場合例外) 基礎柱ふかし厚さ（X終）"""
    thickness_add_fd_end_x_or_none: NonNegativeLength | None
    """属性 基礎柱ふかし厚さ（X終）"""
    thickness_add_fd_start_y: NonNegativeLength
    """属性(Noneの場合例外) 基礎柱ふかし厚さ（Y始）"""
    thickness_add_fd_start_y_or_none: NonNegativeLength | None
    """属性 基礎柱ふかし厚さ（Y始）"""
    thickness_add_fd_end_y: NonNegativeLength
    """属性(Noneの場合例外) 基礎柱ふかし厚さ（Y終）"""
    thickness_add_fd_end_y_or_none: NonNegativeLength | None
    """属性 基礎柱ふかし厚さ（Y終）"""
    id_section_wr: PositiveInteger
    """属性(Noneの場合例外) 根巻柱断面ＩＤ"""
    id_section_wr_or_none: PositiveInteger | None
    """属性 根巻柱断面ＩＤ"""
    length_wr: Length
    """属性(Noneの場合例外) 根巻柱高さ"""
    length_wr_or_none: Length | None
    """属性 根巻柱高さ"""
    offset_wr_x: float
    """属性(Noneの場合例外) 根巻柱オフセット（）"""
    offset_wr_x_or_none: float | None
    """属性 根巻柱オフセット（）"""
    offset_wr_y: float
    """属性(Noneの場合例外) 根巻柱オフセット（）"""
    offset_wr_y_or_none: float | None
    """属性 根巻柱オフセット（）"""
    thickness_add_wr_start_x: NonNegativeLength
    """属性(Noneの場合例外) 根巻柱ふかし厚さ（X始）"""
    thickness_add_wr_start_x_or_none: NonNegativeLength | None
    """属性 根巻柱ふかし厚さ（X始）"""
    thickness_add_wr_end_x: NonNegativeLength
    """属性(Noneの場合例外) 根巻柱ふかし厚さ（X終）"""
    thickness_add_wr_end_x_or_none: NonNegativeLength | None
    """属性 根巻柱ふかし厚さ（X終）"""
    thickness_add_wr_start_y: NonNegativeLength
    """属性(Noneの場合例外) 根巻柱ふかし厚さ（Y始）"""
    thickness_add_wr_start_y_or_none: NonNegativeLength | None
    """属性 根巻柱ふかし厚さ（Y始）"""
    thickness_add_wr_end_y: NonNegativeLength
    """属性(Noneの場合例外) 根巻柱ふかし厚さ（Y終）"""
    thickness_add_wr_end_y_or_none: NonNegativeLength | None
    """属性 根巻柱ふかし厚さ（Y終）"""

class StbParapets(StBridgeElement):
    def __init__(self, *, stb_parapet: Sequence[StbParapet] = ...): ...
    @property
    def stb_parapet(self) -> list[StbParapet]:
        """stb_parapet (list[StbParapet]): 子要素"""
    @stb_parapet.setter
    def stb_parapet(self, value: Sequence[StbParapet]) -> None: ...

class StbParapet(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_node_start: PositiveInteger | None = ...,
        id_node_end: PositiveInteger | None = ...,
        id_section: PositiveInteger | None = ...,
        kind_structure: str | None = ...,
        kind_layout: StbParapetKindLayout | str | None = ...,
        direction: StbParapetDirection | str | None = ...,
        offset: float | None = ...,
        level: float | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 名称"""
    name_or_none: str | None
    """属性 名称"""
    id_node_start: PositiveInteger
    """属性(Noneの場合例外) 始端節点ID"""
    id_node_start_or_none: PositiveInteger | None
    """属性 始端節点ID"""
    id_node_end: PositiveInteger
    """属性(Noneの場合例外) 終端節点ID"""
    id_node_end_or_none: PositiveInteger | None
    """属性 終端節点ID"""
    id_section: PositiveInteger
    """属性(Noneの場合例外) 断面ID"""
    id_section_or_none: PositiveInteger | None
    """属性 断面ID"""
    kind_structure: str
    """属性(Noneの場合例外) 構造種別"""
    kind_structure_or_none: str | None
    """属性 構造種別"""
    @property
    def kind_layout(self) -> StbParapetKindLayout:
        """属性(Noneの場合例外) 壁種別以下のいずれかの値をとる。ON_GIRDER（大梁上）、ON_BEAM（小梁上）、ON_SLAB（スラブ上）"""
    @kind_layout.setter
    def kind_layout(self, value: StbParapetKindLayout | str) -> None: ...
    @property
    def kind_layout_or_none(self) -> StbParapetKindLayout | None:
        """属性 壁種別以下のいずれかの値をとる。ON_GIRDER（大梁上）、ON_BEAM（小梁上）、ON_SLAB（スラブ上）"""
    @kind_layout_or_none.setter
    def kind_layout_or_none(self, value: StbParapetKindLayout | str | None) -> None: ...
    @property
    def direction(self) -> StbParapetDirection:
        """属性(Noneの場合例外) アゴの方向を示す(R/L)R（右側）L（左側）"""
    @direction.setter
    def direction(self, value: StbParapetDirection | str) -> None: ...
    @property
    def direction_or_none(self) -> StbParapetDirection | None:
        """属性 アゴの方向を示す(R/L)R（右側）L（左側）"""
    @direction_or_none.setter
    def direction_or_none(self, value: StbParapetDirection | str | None) -> None: ...
    offset: float
    """属性(Noneの場合例外) オフセット"""
    offset_or_none: float | None
    """属性 オフセット"""
    level: float
    """属性(Noneの場合例外) レベル"""
    level_or_none: float | None
    """属性 レベル"""

class StbOpens(StBridgeElement):
    def __init__(self, *, stb_open: Sequence[StbOpen] = ...): ...
    @property
    def stb_open(self) -> list[StbOpen]:
        """stb_open (list[StbOpen]): 子要素"""
    @stb_open.setter
    def stb_open(self, value: Sequence[StbOpen]) -> None: ...

class StbOpen(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        id_section: PositiveInteger | None = ...,
        position_x: float | None = ...,
        position_y: float | None = ...,
        length_x: Length | None = ...,
        length_y: Length | None = ...,
        rotate: Angle | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外)"""
    id_or_none: PositiveInteger | None
    """属性"""
    guid: UUID
    """属性(Noneの場合例外)"""
    guid_or_none: UUID | None
    """属性"""
    name: str
    """属性(Noneの場合例外)"""
    name_or_none: str | None
    """属性"""
    id_section: PositiveInteger
    """属性(Noneの場合例外)"""
    id_section_or_none: PositiveInteger | None
    """属性"""
    position_x: float
    """属性(Noneの場合例外)"""
    position_x_or_none: float | None
    """属性"""
    position_y: float
    """属性(Noneの場合例外)"""
    position_y_or_none: float | None
    """属性"""
    length_x: Length
    """属性(Noneの場合例外)"""
    length_x_or_none: Length | None
    """属性"""
    length_y: Length
    """属性(Noneの場合例外)"""
    length_y_or_none: Length | None
    """属性"""
    rotate: Angle
    """属性(Noneの場合例外)"""
    rotate_or_none: Angle | None
    """属性"""

class StbOpenIdList(StBridgeElement):
    def __init__(self, *, stb_open_id: Sequence[StbOpenId] = ...): ...
    @property
    def stb_open_id(self) -> list[StbOpenId]:
        """stb_open_id (list[StbOpenId]): 子要素"""
    @stb_open_id.setter
    def stb_open_id(self, value: Sequence[StbOpenId]) -> None: ...

class StbOpenId(StBridgeElement):
    def __init__(self, *, id: PositiveInteger | None = ...): ...
    id: PositiveInteger
    """属性(Noneの場合例外)"""
    id_or_none: PositiveInteger | None
    """属性"""

class StbSections(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_column_rc: Sequence[StbSecColumnRc] = ...,
        stb_sec_column_s: Sequence[StbSecColumnS] = ...,
        stb_sec_column_src: Sequence[StbSecColumnSrc] = ...,
        stb_sec_column_cft: Sequence[StbSecColumnCft] = ...,
        stb_sec_beam_rc: Sequence[StbSecBeamRc] = ...,
        stb_sec_beam_s: Sequence[StbSecBeamS] = ...,
        stb_sec_beam_src: Sequence[StbSecBeamSrc] = ...,
        stb_sec_brace_s: Sequence[StbSecBraceS] = ...,
        stb_sec_slab_rc: Sequence[StbSecSlabRc] = ...,
        stb_sec_slab_deck: Sequence[StbSecSlabDeck] = ...,
        stb_sec_slab_precast: Sequence[StbSecSlabPrecast] = ...,
        stb_sec_wall_rc: Sequence[StbSecWallRc] = ...,
        stb_sec_foundation_rc: Sequence[StbSecFoundationRc] = ...,
        stb_sec_pile_rc: Sequence[StbSecPileRc] = ...,
        stb_sec_pile_s: Sequence[StbSecPileS] = ...,
        stb_sec_pile_product: Sequence[StbSecPileProduct] = ...,
        stb_sec_open_rc: Sequence[StbSecOpenRc] = ...,
        stb_sec_parapet_rc: Sequence[StbSecParapetRc] = ...,
        stb_sec_steel: StbSecSteel | None = ...,
    ): ...
    @property
    def stb_sec_column_rc(self) -> list[StbSecColumnRc]:
        """stb_sec_column_rc (list[StbSecColumnRc]): 子要素"""
    @stb_sec_column_rc.setter
    def stb_sec_column_rc(self, value: Sequence[StbSecColumnRc]) -> None: ...
    @property
    def stb_sec_column_s(self) -> list[StbSecColumnS]:
        """stb_sec_column_s (list[StbSecColumnS]): 子要素"""
    @stb_sec_column_s.setter
    def stb_sec_column_s(self, value: Sequence[StbSecColumnS]) -> None: ...
    @property
    def stb_sec_column_src(self) -> list[StbSecColumnSrc]:
        """stb_sec_column_src (list[StbSecColumnSrc]): 子要素"""
    @stb_sec_column_src.setter
    def stb_sec_column_src(self, value: Sequence[StbSecColumnSrc]) -> None: ...
    @property
    def stb_sec_column_cft(self) -> list[StbSecColumnCft]:
        """stb_sec_column_cft (list[StbSecColumnCft]): 子要素"""
    @stb_sec_column_cft.setter
    def stb_sec_column_cft(self, value: Sequence[StbSecColumnCft]) -> None: ...
    @property
    def stb_sec_beam_rc(self) -> list[StbSecBeamRc]:
        """stb_sec_beam_rc (list[StbSecBeamRc]): 子要素"""
    @stb_sec_beam_rc.setter
    def stb_sec_beam_rc(self, value: Sequence[StbSecBeamRc]) -> None: ...
    @property
    def stb_sec_beam_s(self) -> list[StbSecBeamS]:
        """stb_sec_beam_s (list[StbSecBeamS]): 子要素"""
    @stb_sec_beam_s.setter
    def stb_sec_beam_s(self, value: Sequence[StbSecBeamS]) -> None: ...
    @property
    def stb_sec_beam_src(self) -> list[StbSecBeamSrc]:
        """stb_sec_beam_src (list[StbSecBeamSrc]): 子要素"""
    @stb_sec_beam_src.setter
    def stb_sec_beam_src(self, value: Sequence[StbSecBeamSrc]) -> None: ...
    @property
    def stb_sec_brace_s(self) -> list[StbSecBraceS]:
        """stb_sec_brace_s (list[StbSecBraceS]): 子要素"""
    @stb_sec_brace_s.setter
    def stb_sec_brace_s(self, value: Sequence[StbSecBraceS]) -> None: ...
    @property
    def stb_sec_slab_rc(self) -> list[StbSecSlabRc]:
        """stb_sec_slab_rc (list[StbSecSlabRc]): 子要素"""
    @stb_sec_slab_rc.setter
    def stb_sec_slab_rc(self, value: Sequence[StbSecSlabRc]) -> None: ...
    @property
    def stb_sec_slab_deck(self) -> list[StbSecSlabDeck]:
        """stb_sec_slab_deck (list[StbSecSlabDeck]): 子要素"""
    @stb_sec_slab_deck.setter
    def stb_sec_slab_deck(self, value: Sequence[StbSecSlabDeck]) -> None: ...
    @property
    def stb_sec_slab_precast(self) -> list[StbSecSlabPrecast]:
        """stb_sec_slab_precast (list[StbSecSlabPrecast]): 子要素"""
    @stb_sec_slab_precast.setter
    def stb_sec_slab_precast(self, value: Sequence[StbSecSlabPrecast]) -> None: ...
    @property
    def stb_sec_wall_rc(self) -> list[StbSecWallRc]:
        """stb_sec_wall_rc (list[StbSecWallRc]): 子要素"""
    @stb_sec_wall_rc.setter
    def stb_sec_wall_rc(self, value: Sequence[StbSecWallRc]) -> None: ...
    @property
    def stb_sec_foundation_rc(self) -> list[StbSecFoundationRc]:
        """stb_sec_foundation_rc (list[StbSecFoundationRc]): 子要素"""
    @stb_sec_foundation_rc.setter
    def stb_sec_foundation_rc(self, value: Sequence[StbSecFoundationRc]) -> None: ...
    @property
    def stb_sec_pile_rc(self) -> list[StbSecPileRc]:
        """stb_sec_pile_rc (list[StbSecPileRc]): 子要素"""
    @stb_sec_pile_rc.setter
    def stb_sec_pile_rc(self, value: Sequence[StbSecPileRc]) -> None: ...
    @property
    def stb_sec_pile_s(self) -> list[StbSecPileS]:
        """stb_sec_pile_s (list[StbSecPileS]): 子要素"""
    @stb_sec_pile_s.setter
    def stb_sec_pile_s(self, value: Sequence[StbSecPileS]) -> None: ...
    @property
    def stb_sec_pile_product(self) -> list[StbSecPileProduct]:
        """stb_sec_pile_product (list[StbSecPileProduct]): 子要素"""
    @stb_sec_pile_product.setter
    def stb_sec_pile_product(self, value: Sequence[StbSecPileProduct]) -> None: ...
    @property
    def stb_sec_open_rc(self) -> list[StbSecOpenRc]:
        """stb_sec_open_rc (list[StbSecOpenRc]): 子要素"""
    @stb_sec_open_rc.setter
    def stb_sec_open_rc(self, value: Sequence[StbSecOpenRc]) -> None: ...
    @property
    def stb_sec_parapet_rc(self) -> list[StbSecParapetRc]:
        """stb_sec_parapet_rc (list[StbSecParapetRc]): 子要素"""
    @stb_sec_parapet_rc.setter
    def stb_sec_parapet_rc(self, value: Sequence[StbSecParapetRc]) -> None: ...
    stb_sec_steel: StbSecSteel
    """子要素(Noneの場合例外)"""
    stb_sec_steel_or_none: StbSecSteel | None
    """子要素"""
    @property
    def ensure(self) -> _StbSectionsEnsureAccessor: ...

class StbSecColumnRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_column: StbSecColumnRcKindColumn | str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_column_rc: StbSecFigureColumnRc | None = ...,
        stb_sec_bar_arrangement_column_rc: StbSecBarArrangementColumnRc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_column(self) -> StbSecColumnRcKindColumn:
        """属性(Noneの場合例外) 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column.setter
    def kind_column(self, value: StbSecColumnRcKindColumn | str) -> None: ...
    @property
    def kind_column_or_none(self) -> StbSecColumnRcKindColumn | None:
        """属性 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column_or_none.setter
    def kind_column_or_none(
        self, value: StbSecColumnRcKindColumn | str | None
    ) -> None: ...
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_column_rc: StbSecFigureColumnRc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_column_rc_or_none: StbSecFigureColumnRc | None
    """子要素"""
    stb_sec_bar_arrangement_column_rc: StbSecBarArrangementColumnRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_column_rc_or_none: StbSecBarArrangementColumnRc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecColumnRcEnsureAccessor: ...

class StbSecFigureColumnRc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_column_rc_rect: StbSecColumnRcRect | None = ...,
        stb_sec_column_rc_circle: StbSecColumnRcCircle | None = ...,
    ): ...
    stb_sec_column_rc_rect: StbSecColumnRcRect
    """子要素(Noneの場合例外)"""
    stb_sec_column_rc_rect_or_none: StbSecColumnRcRect | None
    """子要素"""
    stb_sec_column_rc_circle: StbSecColumnRcCircle
    """子要素(Noneの場合例外)"""
    stb_sec_column_rc_circle_or_none: StbSecColumnRcCircle | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigureColumnRcEnsureAccessor: ...

class StbSecColumnRcRect(StBridgeElement):
    def __init__(
        self, *, width_x: Length | None = ..., width_y: Length | None = ...
    ): ...
    width_x: Length
    """属性(Noneの場合例外)"""
    width_x_or_none: Length | None
    """属性"""
    width_y: Length
    """属性(Noneの場合例外)"""
    width_y_or_none: Length | None
    """属性"""

class StbSecColumnRcCircle(StBridgeElement):
    def __init__(self, *, d: Length | None = ...): ...
    d: Length
    """属性(Noneの場合例外)"""
    d_or_none: Length | None
    """属性"""

class StbSecBarArrangementColumnRc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_start_x: Length | None = ...,
        depth_cover_end_x: Length | None = ...,
        depth_cover_start_y: Length | None = ...,
        depth_cover_end_y: Length | None = ...,
        interval: Length | None = ...,
        kind_corner: StbSecBarArrangementColumnRcKindCorner | str | None = ...,
        is_spiral: bool | None = ...,
        center_start_x: Length | None = ...,
        center_end_x: Length | None = ...,
        center_start_y: Length | None = ...,
        center_end_y: Length | None = ...,
        center_interval: Length | None = ...,
        stb_sec_bar_column_rc_rect_same: StbSecBarColumnRcRectSame | None = ...,
        stb_sec_bar_column_x_reinforced: StbSecBarColumnXReinforced | None = ...,
        stb_sec_bar_column_rc_rect_not_same: Sequence[
            StbSecBarColumnRcRectNotSame
        ] = ...,
        stb_sec_bar_column_rc_circle_same: StbSecBarColumnRcCircleSame | None = ...,
        stb_sec_bar_column_rc_circle_not_same: Sequence[
            StbSecBarColumnRcCircleNotSame
        ] = ...,
    ): ...
    depth_cover_start_x: Length
    """属性(Noneの場合例外)"""
    depth_cover_start_x_or_none: Length | None
    """属性"""
    depth_cover_end_x: Length
    """属性(Noneの場合例外)"""
    depth_cover_end_x_or_none: Length | None
    """属性"""
    depth_cover_start_y: Length
    """属性(Noneの場合例外)"""
    depth_cover_start_y_or_none: Length | None
    """属性"""
    depth_cover_end_y: Length
    """属性(Noneの場合例外)"""
    depth_cover_end_y_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    @property
    def kind_corner(self) -> StbSecBarArrangementColumnRcKindCorner:
        """属性(Noneの場合例外)"""
    @kind_corner.setter
    def kind_corner(
        self, value: StbSecBarArrangementColumnRcKindCorner | str
    ) -> None: ...
    @property
    def kind_corner_or_none(self) -> StbSecBarArrangementColumnRcKindCorner | None:
        """属性"""
    @kind_corner_or_none.setter
    def kind_corner_or_none(
        self, value: StbSecBarArrangementColumnRcKindCorner | str | None
    ) -> None: ...
    is_spiral: bool
    """属性(Noneの場合例外)"""
    is_spiral_or_none: bool | None
    """属性"""
    center_start_x: Length
    """属性(Noneの場合例外)"""
    center_start_x_or_none: Length | None
    """属性"""
    center_end_x: Length
    """属性(Noneの場合例外)"""
    center_end_x_or_none: Length | None
    """属性"""
    center_start_y: Length
    """属性(Noneの場合例外)"""
    center_start_y_or_none: Length | None
    """属性"""
    center_end_y: Length
    """属性(Noneの場合例外)"""
    center_end_y_or_none: Length | None
    """属性"""
    center_interval: Length
    """属性(Noneの場合例外)"""
    center_interval_or_none: Length | None
    """属性"""
    stb_sec_bar_column_rc_rect_same: StbSecBarColumnRcRectSame
    """子要素(Noneの場合例外)"""
    stb_sec_bar_column_rc_rect_same_or_none: StbSecBarColumnRcRectSame | None
    """子要素"""
    stb_sec_bar_column_x_reinforced: StbSecBarColumnXReinforced
    """子要素(Noneの場合例外)"""
    stb_sec_bar_column_x_reinforced_or_none: StbSecBarColumnXReinforced | None
    """子要素"""
    @property
    def stb_sec_bar_column_rc_rect_not_same(self) -> list[StbSecBarColumnRcRectNotSame]:
        """stb_sec_bar_column_rc_rect_not_same (list[StbSecBarColumnRcRectNotSame]): 子要素"""
    @stb_sec_bar_column_rc_rect_not_same.setter
    def stb_sec_bar_column_rc_rect_not_same(
        self, value: Sequence[StbSecBarColumnRcRectNotSame]
    ) -> None: ...
    stb_sec_bar_column_rc_circle_same: StbSecBarColumnRcCircleSame
    """子要素(Noneの場合例外)"""
    stb_sec_bar_column_rc_circle_same_or_none: StbSecBarColumnRcCircleSame | None
    """子要素"""
    @property
    def stb_sec_bar_column_rc_circle_not_same(
        self,
    ) -> list[StbSecBarColumnRcCircleNotSame]:
        """stb_sec_bar_column_rc_circle_not_same (list[StbSecBarColumnRcCircleNotSame]): 子要素"""
    @stb_sec_bar_column_rc_circle_not_same.setter
    def stb_sec_bar_column_rc_circle_not_same(
        self, value: Sequence[StbSecBarColumnRcCircleNotSame]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecBarArrangementColumnRcEnsureAccessor: ...

class StbSecBarColumnRcRectSame(StBridgeElement):
    def __init__(
        self,
        *,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_x_1st: PositiveInteger | None = ...,
        n_main_x_2nd: PositiveInteger | None = ...,
        n_main_y_1st: PositiveInteger | None = ...,
        n_main_y_2nd: PositiveInteger | None = ...,
        n_2nd_main_x_1st: PositiveInteger | None = ...,
        n_2nd_main_x_2nd: PositiveInteger | None = ...,
        n_2nd_main_y_1st: PositiveInteger | None = ...,
        n_2nd_main_y_2nd: PositiveInteger | None = ...,
        n_main_total: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        n_band_direction_x: PositiveInteger | None = ...,
        n_band_direction_y: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_total: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_total_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    n_band_direction_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_x_or_none: PositiveInteger | None
    """属性"""
    n_band_direction_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_y_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBarColumnRcRectNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarColumnRcRectNotSamePos | str | None = ...,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_x_1st: PositiveInteger | None = ...,
        n_main_x_2nd: PositiveInteger | None = ...,
        n_main_y_1st: PositiveInteger | None = ...,
        n_main_y_2nd: PositiveInteger | None = ...,
        n_2nd_main_x_1st: PositiveInteger | None = ...,
        n_2nd_main_x_2nd: PositiveInteger | None = ...,
        n_2nd_main_y_1st: PositiveInteger | None = ...,
        n_2nd_main_y_2nd: PositiveInteger | None = ...,
        n_main_total: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        n_band_direction_x: PositiveInteger | None = ...,
        n_band_direction_y: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarColumnRcRectNotSamePos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarColumnRcRectNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarColumnRcRectNotSamePos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarColumnRcRectNotSamePos | str | None
    ) -> None: ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_total: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_total_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    n_band_direction_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_x_or_none: PositiveInteger | None
    """属性"""
    n_band_direction_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_y_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBarColumnRcCircleSame(StBridgeElement):
    def __init__(
        self,
        *,
        d_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        n_band: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    n_band: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBarColumnRcCircleNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarColumnRcCircleNotSamePos | str | None = ...,
        d_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        n_band: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarColumnRcCircleNotSamePos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarColumnRcCircleNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarColumnRcCircleNotSamePos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarColumnRcCircleNotSamePos | str | None
    ) -> None: ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    n_band: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBarColumnXReinforced(StBridgeElement):
    def __init__(
        self,
        *,
        n_main_x: PositiveInteger | None = ...,
        n_main_y: PositiveInteger | None = ...,
        n_main_total: PositiveInteger | None = ...,
    ): ...
    n_main_x: PositiveInteger
    """属性(Noneの場合例外) 主筋：X方向本数"""
    n_main_x_or_none: PositiveInteger | None
    """属性 主筋：X方向本数"""
    n_main_y: PositiveInteger
    """属性(Noneの場合例外) 主筋：Y方向本数"""
    n_main_y_or_none: PositiveInteger | None
    """属性 主筋：Y方向本数"""
    n_main_total: PositiveInteger
    """属性(Noneの場合例外) 主筋：X形配筋の総本数"""
    n_main_total_or_none: PositiveInteger | None
    """属性 主筋：X形配筋の総本数"""

class StbSecColumnS(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_column: StbSecColumnSKindColumn | str | None = ...,
        is_reference_direction: bool | None = ...,
        stb_sec_steel_figure_column_s: StbSecSteelFigureColumnS | None = ...,
        stb_sec_base_product_s: StbSecBaseProductS | None = ...,
        stb_sec_base_conventional_s: StbSecBaseConventionalS | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_column(self) -> StbSecColumnSKindColumn:
        """属性(Noneの場合例外) 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column.setter
    def kind_column(self, value: StbSecColumnSKindColumn | str) -> None: ...
    @property
    def kind_column_or_none(self) -> StbSecColumnSKindColumn | None:
        """属性 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column_or_none.setter
    def kind_column_or_none(
        self, value: StbSecColumnSKindColumn | str | None
    ) -> None: ...
    is_reference_direction: bool
    """属性(Noneの場合例外) 鉄骨向き"""
    is_reference_direction_or_none: bool | None
    """属性 鉄骨向き"""
    stb_sec_steel_figure_column_s: StbSecSteelFigureColumnS
    """子要素(Noneの場合例外)"""
    stb_sec_steel_figure_column_s_or_none: StbSecSteelFigureColumnS | None
    """子要素"""
    stb_sec_base_product_s: StbSecBaseProductS
    """子要素(Noneの場合例外)"""
    stb_sec_base_product_s_or_none: StbSecBaseProductS | None
    """子要素"""
    stb_sec_base_conventional_s: StbSecBaseConventionalS
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_s_or_none: StbSecBaseConventionalS | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecColumnSEnsureAccessor: ...

class StbSecSteelFigureColumnS(StBridgeElement):
    def __init__(
        self,
        *,
        base_type: StbSecSteelFigureColumnSBaseType | str | None = ...,
        joint_id_top: PositiveInteger | None = ...,
        joint_id_bottom: PositiveInteger | None = ...,
        stb_sec_steel_column_s_same: StbSecSteelColumnSSame | None = ...,
        stb_sec_steel_column_s_not_same: Sequence[StbSecSteelColumnSNotSame] = ...,
        stb_sec_steel_column_s_three_types: Sequence[
            StbSecSteelColumnSThreeTypes
        ] = ...,
    ): ...
    @property
    def base_type(self) -> StbSecSteelFigureColumnSBaseType:
        """属性(Noneの場合例外) 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）EXPOSE（露出）EMBEDDED（埋込）WRAP（根巻）"""
    @base_type.setter
    def base_type(self, value: StbSecSteelFigureColumnSBaseType | str) -> None: ...
    @property
    def base_type_or_none(self) -> StbSecSteelFigureColumnSBaseType | None:
        """属性 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）EXPOSE（露出）EMBEDDED（埋込）WRAP（根巻）"""
    @base_type_or_none.setter
    def base_type_or_none(
        self, value: StbSecSteelFigureColumnSBaseType | str | None
    ) -> None: ...
    joint_id_top: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_top_or_none: PositiveInteger | None
    """属性"""
    joint_id_bottom: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_bottom_or_none: PositiveInteger | None
    """属性"""
    stb_sec_steel_column_s_same: StbSecSteelColumnSSame
    """子要素(Noneの場合例外)"""
    stb_sec_steel_column_s_same_or_none: StbSecSteelColumnSSame | None
    """子要素"""
    @property
    def stb_sec_steel_column_s_not_same(self) -> list[StbSecSteelColumnSNotSame]:
        """stb_sec_steel_column_s_not_same (list[StbSecSteelColumnSNotSame]): 子要素"""
    @stb_sec_steel_column_s_not_same.setter
    def stb_sec_steel_column_s_not_same(
        self, value: Sequence[StbSecSteelColumnSNotSame]
    ) -> None: ...
    @property
    def stb_sec_steel_column_s_three_types(self) -> list[StbSecSteelColumnSThreeTypes]:
        """stb_sec_steel_column_s_three_types (list[StbSecSteelColumnSThreeTypes]): 子要素"""
    @stb_sec_steel_column_s_three_types.setter
    def stb_sec_steel_column_s_three_types(
        self, value: Sequence[StbSecSteelColumnSThreeTypes]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecSteelFigureColumnSEnsureAccessor: ...

class StbSecSteelColumnSSame(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength_main: str
    """属性(Noneの場合例外) 鉄骨強度（主）"""
    strength_main_or_none: str | None
    """属性 鉄骨強度（主）"""
    strength_web: str
    """属性(Noneの場合例外) 鉄骨強度（ウェブ）"""
    strength_web_or_none: str | None
    """属性 鉄骨強度（ウェブ）"""

class StbSecSteelColumnSNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelColumnSNotSamePos | str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelColumnSNotSamePos:
        """属性(Noneの場合例外) 配置位置以下のいずれかBOTTOM（柱脚）TOP（柱頭）"""
    @pos.setter
    def pos(self, value: StbSecSteelColumnSNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelColumnSNotSamePos | None:
        """属性 配置位置以下のいずれかBOTTOM（柱脚）TOP（柱頭）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelColumnSNotSamePos | str | None) -> None: ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength_main: str
    """属性(Noneの場合例外) 鉄骨強度（主）"""
    strength_main_or_none: str | None
    """属性 鉄骨強度（主）"""
    strength_web: str
    """属性(Noneの場合例外) 鉄骨強度（ウェブ）"""
    strength_web_or_none: str | None
    """属性 鉄骨強度（ウェブ）"""

class StbSecSteelColumnSThreeTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelColumnSThreeTypesPos | str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelColumnSThreeTypesPos:
        """属性(Noneの場合例外) 配置位置以下のいずれかBOTTOM（柱脚）CENTER（中央）TOP（柱頭）"""
    @pos.setter
    def pos(self, value: StbSecSteelColumnSThreeTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelColumnSThreeTypesPos | None:
        """属性 配置位置以下のいずれかBOTTOM（柱脚）CENTER（中央）TOP（柱頭）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecSteelColumnSThreeTypesPos | str | None
    ) -> None: ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength_main: str
    """属性(Noneの場合例外) 鉄骨強度（主）"""
    strength_main_or_none: str | None
    """属性 鉄骨強度（主）"""
    strength_web: str
    """属性(Noneの場合例外) 鉄骨強度（ウェブ）"""
    strength_web_or_none: str | None
    """属性 鉄骨強度（ウェブ）"""

class StbSecBaseProductS(StBridgeElement):
    def __init__(
        self,
        *,
        product_company: str | None = ...,
        product_code: str | None = ...,
        direction_type: StbSecBaseProductSDirectionType | int | None = ...,
        height_mortar: NonNegativeLength | None = ...,
    ): ...
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    @property
    def direction_type(self) -> StbSecBaseProductSDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(self, value: StbSecBaseProductSDirectionType | int) -> None: ...
    @property
    def direction_type_or_none(self) -> StbSecBaseProductSDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecBaseProductSDirectionType | int | None
    ) -> None: ...
    height_mortar: NonNegativeLength
    """属性(Noneの場合例外)"""
    height_mortar_or_none: NonNegativeLength | None
    """属性"""

class StbSecBaseConventionalS(StBridgeElement):
    def __init__(
        self,
        *,
        height_mortar: NonNegativeLength | None = ...,
        stb_sec_base_conventional_s_plate: StbSecBaseConventionalSPlate | None = ...,
        stb_sec_base_conventional_s_anchor_bolt: StbSecBaseConventionalSAnchorBolt
        | None = ...,
        stb_sec_base_conventional_s_rib_plate: StbSecBaseConventionalSRibPlate
        | None = ...,
    ): ...
    height_mortar: NonNegativeLength
    """属性(Noneの場合例外)"""
    height_mortar_or_none: NonNegativeLength | None
    """属性"""
    stb_sec_base_conventional_s_plate: StbSecBaseConventionalSPlate
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_s_plate_or_none: StbSecBaseConventionalSPlate | None
    """子要素"""
    stb_sec_base_conventional_s_anchor_bolt: StbSecBaseConventionalSAnchorBolt
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_s_anchor_bolt_or_none: (
        StbSecBaseConventionalSAnchorBolt | None
    )
    """子要素"""
    stb_sec_base_conventional_s_rib_plate: StbSecBaseConventionalSRibPlate
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_s_rib_plate_or_none: (
        StbSecBaseConventionalSRibPlate | None
    )
    """子要素"""
    @property
    def ensure(self) -> _StbSecBaseConventionalSEnsureAccessor: ...

class StbSecBaseConventionalSPlate(StBridgeElement):
    def __init__(
        self,
        *,
        b_x: Length | None = ...,
        b_y: Length | None = ...,
        c1_x: NonNegativeLength | None = ...,
        c1_y: NonNegativeLength | None = ...,
        c2_x: NonNegativeLength | None = ...,
        c2_y: NonNegativeLength | None = ...,
        c3_x: NonNegativeLength | None = ...,
        c3_y: NonNegativeLength | None = ...,
        c4_x: NonNegativeLength | None = ...,
        c4_y: NonNegativeLength | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
        d_bolthole: Length | None = ...,
        offset_x: NonNegativeLength | None = ...,
        offset_y: NonNegativeLength | None = ...,
    ): ...
    b_x: Length
    """属性(Noneの場合例外)"""
    b_x_or_none: Length | None
    """属性"""
    b_y: Length
    """属性(Noneの場合例外)"""
    b_y_or_none: Length | None
    """属性"""
    c1_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c1_x_or_none: NonNegativeLength | None
    """属性"""
    c1_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c1_y_or_none: NonNegativeLength | None
    """属性"""
    c2_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c2_x_or_none: NonNegativeLength | None
    """属性"""
    c2_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c2_y_or_none: NonNegativeLength | None
    """属性"""
    c3_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c3_x_or_none: NonNegativeLength | None
    """属性"""
    c3_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c3_y_or_none: NonNegativeLength | None
    """属性"""
    c4_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c4_x_or_none: NonNegativeLength | None
    """属性"""
    c4_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c4_y_or_none: NonNegativeLength | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d_bolthole: Length
    """属性(Noneの場合例外)"""
    d_bolthole_or_none: Length | None
    """属性"""
    offset_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_x_or_none: NonNegativeLength | None
    """属性"""
    offset_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_y_or_none: NonNegativeLength | None
    """属性"""

class StbSecBaseConventionalSAnchorBolt(StBridgeElement):
    def __init__(
        self,
        *,
        kind_bolt: StbSecBaseConventionalSAnchorBoltKindBolt | str | None = ...,
        name_bolt: str | None = ...,
        length_bolt: Length | None = ...,
        strength_bolt: str | None = ...,
        arrangement_bolt: StbSecBaseConventionalSAnchorBoltArrangementBolt
        | str
        | None = ...,
        d1_x: Length | None = ...,
        d2_x: Length | None = ...,
        d1_y: Length | None = ...,
        d2_y: Length | None = ...,
        n_x: PositiveInteger | None = ...,
        n_y: PositiveInteger | None = ...,
    ): ...
    @property
    def kind_bolt(self) -> StbSecBaseConventionalSAnchorBoltKindBolt:
        """属性(Noneの場合例外)"""
    @kind_bolt.setter
    def kind_bolt(
        self, value: StbSecBaseConventionalSAnchorBoltKindBolt | str
    ) -> None: ...
    @property
    def kind_bolt_or_none(self) -> StbSecBaseConventionalSAnchorBoltKindBolt | None:
        """属性"""
    @kind_bolt_or_none.setter
    def kind_bolt_or_none(
        self, value: StbSecBaseConventionalSAnchorBoltKindBolt | str | None
    ) -> None: ...
    name_bolt: str
    """属性(Noneの場合例外)"""
    name_bolt_or_none: str | None
    """属性"""
    length_bolt: Length
    """属性(Noneの場合例外)"""
    length_bolt_or_none: Length | None
    """属性"""
    strength_bolt: str
    """属性(Noneの場合例外)"""
    strength_bolt_or_none: str | None
    """属性"""
    @property
    def arrangement_bolt(self) -> StbSecBaseConventionalSAnchorBoltArrangementBolt:
        """属性(Noneの場合例外)"""
    @arrangement_bolt.setter
    def arrangement_bolt(
        self, value: StbSecBaseConventionalSAnchorBoltArrangementBolt | str
    ) -> None: ...
    @property
    def arrangement_bolt_or_none(
        self,
    ) -> StbSecBaseConventionalSAnchorBoltArrangementBolt | None:
        """属性"""
    @arrangement_bolt_or_none.setter
    def arrangement_bolt_or_none(
        self, value: StbSecBaseConventionalSAnchorBoltArrangementBolt | str | None
    ) -> None: ...
    d1_x: Length
    """属性(Noneの場合例外)"""
    d1_x_or_none: Length | None
    """属性"""
    d2_x: Length
    """属性(Noneの場合例外)"""
    d2_x_or_none: Length | None
    """属性"""
    d1_y: Length
    """属性(Noneの場合例外)"""
    d1_y_or_none: Length | None
    """属性"""
    d2_y: Length
    """属性(Noneの場合例外)"""
    d2_y_or_none: Length | None
    """属性"""
    n_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_x_or_none: PositiveInteger | None
    """属性"""
    n_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBaseConventionalSRibPlate(StBridgeElement):
    def __init__(
        self,
        *,
        a1: Length | None = ...,
        a2: NonNegativeLength | None = ...,
        b1: Length | None = ...,
        b2: NonNegativeLength | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
        n_x: PositiveInteger | None = ...,
        n_y: PositiveInteger | None = ...,
        length_e_x: Length | None = ...,
        length_e_y: Length | None = ...,
    ): ...
    a1: Length
    """属性(Noneの場合例外)"""
    a1_or_none: Length | None
    """属性"""
    a2: NonNegativeLength
    """属性(Noneの場合例外)"""
    a2_or_none: NonNegativeLength | None
    """属性"""
    b1: Length
    """属性(Noneの場合例外)"""
    b1_or_none: Length | None
    """属性"""
    b2: NonNegativeLength
    """属性(Noneの場合例外)"""
    b2_or_none: NonNegativeLength | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    n_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_x_or_none: PositiveInteger | None
    """属性"""
    n_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_y_or_none: PositiveInteger | None
    """属性"""
    length_e_x: Length
    """属性(Noneの場合例外)"""
    length_e_x_or_none: Length | None
    """属性"""
    length_e_y: Length
    """属性(Noneの場合例外)"""
    length_e_y_or_none: Length | None
    """属性"""

class StbSecColumnSrc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_column: StbSecColumnSrcKindColumn | str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_column_src: StbSecFigureColumnSrc | None = ...,
        stb_sec_bar_arrangement_column_src: StbSecBarArrangementColumnSrc | None = ...,
        stb_sec_steel_figure_column_src: StbSecSteelFigureColumnSrc | None = ...,
        stb_sec_base_product_src: StbSecBaseProductSrc | None = ...,
        stb_sec_base_conventional_src: StbSecBaseConventionalSrc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_column(self) -> StbSecColumnSrcKindColumn:
        """属性(Noneの場合例外) 柱の種別 以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column.setter
    def kind_column(self, value: StbSecColumnSrcKindColumn | str) -> None: ...
    @property
    def kind_column_or_none(self) -> StbSecColumnSrcKindColumn | None:
        """属性 柱の種別 以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column_or_none.setter
    def kind_column_or_none(
        self, value: StbSecColumnSrcKindColumn | str | None
    ) -> None: ...
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_column_src: StbSecFigureColumnSrc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_column_src_or_none: StbSecFigureColumnSrc | None
    """子要素"""
    stb_sec_bar_arrangement_column_src: StbSecBarArrangementColumnSrc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_column_src_or_none: StbSecBarArrangementColumnSrc | None
    """子要素"""
    stb_sec_steel_figure_column_src: StbSecSteelFigureColumnSrc
    """子要素(Noneの場合例外)"""
    stb_sec_steel_figure_column_src_or_none: StbSecSteelFigureColumnSrc | None
    """子要素"""
    stb_sec_base_product_src: StbSecBaseProductSrc
    """子要素(Noneの場合例外)"""
    stb_sec_base_product_src_or_none: StbSecBaseProductSrc | None
    """子要素"""
    stb_sec_base_conventional_src: StbSecBaseConventionalSrc
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_src_or_none: StbSecBaseConventionalSrc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecColumnSrcEnsureAccessor: ...

class StbSecFigureColumnSrc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_column_src_rect: StbSecColumnSrcRect | None = ...,
        stb_sec_column_src_circle: StbSecColumnSrcCircle | None = ...,
    ): ...
    stb_sec_column_src_rect: StbSecColumnSrcRect
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_rect_or_none: StbSecColumnSrcRect | None
    """子要素"""
    stb_sec_column_src_circle: StbSecColumnSrcCircle
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_circle_or_none: StbSecColumnSrcCircle | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigureColumnSrcEnsureAccessor: ...

class StbSecColumnSrcRect(StBridgeElement):
    def __init__(
        self, *, width_x: Length | None = ..., width_y: Length | None = ...
    ): ...
    width_x: Length
    """属性(Noneの場合例外)"""
    width_x_or_none: Length | None
    """属性"""
    width_y: Length
    """属性(Noneの場合例外)"""
    width_y_or_none: Length | None
    """属性"""

class StbSecColumnSrcCircle(StBridgeElement):
    def __init__(self, *, d: Length | None = ...): ...
    d: Length
    """属性(Noneの場合例外)"""
    d_or_none: Length | None
    """属性"""

class StbSecBarArrangementColumnSrc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_start_x: Length | None = ...,
        depth_cover_end_x: Length | None = ...,
        depth_cover_start_y: Length | None = ...,
        depth_cover_end_y: Length | None = ...,
        interval: Length | None = ...,
        kind_corner: StbSecBarArrangementColumnSrcKindCorner | str | None = ...,
        is_spiral: bool | None = ...,
        center_start_x: Length | None = ...,
        center_end_x: Length | None = ...,
        center_start_y: Length | None = ...,
        center_end_y: Length | None = ...,
        center_interval: Length | None = ...,
        stb_sec_bar_column_src_rect_same: StbSecBarColumnSrcRectSame | None = ...,
        stb_sec_bar_column_src_rect_not_same: Sequence[
            StbSecBarColumnSrcRectNotSame
        ] = ...,
        stb_sec_bar_column_src_circle_same: StbSecBarColumnSrcCircleSame | None = ...,
        stb_sec_bar_column_src_circle_not_same: Sequence[
            StbSecBarColumnSrcCircleNotSame
        ] = ...,
    ): ...
    depth_cover_start_x: Length
    """属性(Noneの場合例外)"""
    depth_cover_start_x_or_none: Length | None
    """属性"""
    depth_cover_end_x: Length
    """属性(Noneの場合例外)"""
    depth_cover_end_x_or_none: Length | None
    """属性"""
    depth_cover_start_y: Length
    """属性(Noneの場合例外)"""
    depth_cover_start_y_or_none: Length | None
    """属性"""
    depth_cover_end_y: Length
    """属性(Noneの場合例外)"""
    depth_cover_end_y_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    @property
    def kind_corner(self) -> StbSecBarArrangementColumnSrcKindCorner:
        """属性(Noneの場合例外)"""
    @kind_corner.setter
    def kind_corner(
        self, value: StbSecBarArrangementColumnSrcKindCorner | str
    ) -> None: ...
    @property
    def kind_corner_or_none(self) -> StbSecBarArrangementColumnSrcKindCorner | None:
        """属性"""
    @kind_corner_or_none.setter
    def kind_corner_or_none(
        self, value: StbSecBarArrangementColumnSrcKindCorner | str | None
    ) -> None: ...
    is_spiral: bool
    """属性(Noneの場合例外)"""
    is_spiral_or_none: bool | None
    """属性"""
    center_start_x: Length
    """属性(Noneの場合例外)"""
    center_start_x_or_none: Length | None
    """属性"""
    center_end_x: Length
    """属性(Noneの場合例外)"""
    center_end_x_or_none: Length | None
    """属性"""
    center_start_y: Length
    """属性(Noneの場合例外)"""
    center_start_y_or_none: Length | None
    """属性"""
    center_end_y: Length
    """属性(Noneの場合例外)"""
    center_end_y_or_none: Length | None
    """属性"""
    center_interval: Length
    """属性(Noneの場合例外)"""
    center_interval_or_none: Length | None
    """属性"""
    stb_sec_bar_column_src_rect_same: StbSecBarColumnSrcRectSame
    """子要素(Noneの場合例外)"""
    stb_sec_bar_column_src_rect_same_or_none: StbSecBarColumnSrcRectSame | None
    """子要素"""
    @property
    def stb_sec_bar_column_src_rect_not_same(
        self,
    ) -> list[StbSecBarColumnSrcRectNotSame]:
        """stb_sec_bar_column_src_rect_not_same (list[StbSecBarColumnSrcRectNotSame]): 子要素"""
    @stb_sec_bar_column_src_rect_not_same.setter
    def stb_sec_bar_column_src_rect_not_same(
        self, value: Sequence[StbSecBarColumnSrcRectNotSame]
    ) -> None: ...
    stb_sec_bar_column_src_circle_same: StbSecBarColumnSrcCircleSame
    """子要素(Noneの場合例外)"""
    stb_sec_bar_column_src_circle_same_or_none: StbSecBarColumnSrcCircleSame | None
    """子要素"""
    @property
    def stb_sec_bar_column_src_circle_not_same(
        self,
    ) -> list[StbSecBarColumnSrcCircleNotSame]:
        """stb_sec_bar_column_src_circle_not_same (list[StbSecBarColumnSrcCircleNotSame]): 子要素"""
    @stb_sec_bar_column_src_circle_not_same.setter
    def stb_sec_bar_column_src_circle_not_same(
        self, value: Sequence[StbSecBarColumnSrcCircleNotSame]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecBarArrangementColumnSrcEnsureAccessor: ...

class StbSecBarColumnSrcRectSame(StBridgeElement):
    def __init__(
        self,
        *,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_x_1st: PositiveInteger | None = ...,
        n_main_x_2nd: PositiveInteger | None = ...,
        n_main_y_1st: PositiveInteger | None = ...,
        n_main_y_2nd: PositiveInteger | None = ...,
        n_2nd_main_x_1st: PositiveInteger | None = ...,
        n_2nd_main_x_2nd: PositiveInteger | None = ...,
        n_2nd_main_y_1st: PositiveInteger | None = ...,
        n_2nd_main_y_2nd: PositiveInteger | None = ...,
        n_main_total: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        n_band_direction_x: PositiveInteger | None = ...,
        n_band_direction_y: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_total: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_total_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    n_band_direction_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_x_or_none: PositiveInteger | None
    """属性"""
    n_band_direction_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_y_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBarColumnSrcRectNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarColumnSrcRectNotSamePos | str | None = ...,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_x_1st: PositiveInteger | None = ...,
        n_main_x_2nd: PositiveInteger | None = ...,
        n_main_y_1st: PositiveInteger | None = ...,
        n_main_y_2nd: PositiveInteger | None = ...,
        n_2nd_main_x_1st: PositiveInteger | None = ...,
        n_2nd_main_x_2nd: PositiveInteger | None = ...,
        n_2nd_main_y_1st: PositiveInteger | None = ...,
        n_2nd_main_y_2nd: PositiveInteger | None = ...,
        n_main_total: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        n_band_direction_x: PositiveInteger | None = ...,
        n_band_direction_y: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarColumnSrcRectNotSamePos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarColumnSrcRectNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarColumnSrcRectNotSamePos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarColumnSrcRectNotSamePos | str | None
    ) -> None: ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_x_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_x_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_y_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_y_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_total: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_total_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    n_band_direction_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_x_or_none: PositiveInteger | None
    """属性"""
    n_band_direction_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_direction_y_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBarColumnSrcCircleSame(StBridgeElement):
    def __init__(
        self,
        *,
        d_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        n_band: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    n_band: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBarColumnSrcCircleNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarColumnSrcCircleNotSamePos | str | None = ...,
        d_main: str | None = ...,
        d_axial: str | None = ...,
        d_band: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_axial: str | None = ...,
        strength_band: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main: PositiveInteger | None = ...,
        n_axial: PositiveInteger | None = ...,
        n_band: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        pitch_bar_spacing: Length | None = ...,
        n_bar_spacing_x: PositiveInteger | None = ...,
        n_bar_spacing_y: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarColumnSrcCircleNotSamePos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarColumnSrcCircleNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarColumnSrcCircleNotSamePos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarColumnSrcCircleNotSamePos | str | None
    ) -> None: ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_axial: str
    """属性(Noneの場合例外)"""
    d_axial_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_axial: str
    """属性(Noneの場合例外)"""
    strength_axial_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_or_none: PositiveInteger | None
    """属性"""
    n_axial: PositiveInteger
    """属性(Noneの場合例外)"""
    n_axial_or_none: PositiveInteger | None
    """属性"""
    n_band: PositiveInteger
    """属性(Noneの場合例外)"""
    n_band_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""
    n_bar_spacing_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_x_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_y_or_none: PositiveInteger | None
    """属性"""

class StbSecSteelFigureColumnSrc(StBridgeElement):
    def __init__(
        self,
        *,
        base_type: StbSecSteelFigureColumnSrcBaseType | str | None = ...,
        joint_id_top: PositiveInteger | None = ...,
        joint_id_bottom: PositiveInteger | None = ...,
        length_embedded: Length | None = ...,
        stb_sec_steel_column_src_same: StbSecSteelColumnSrcSame | None = ...,
        stb_sec_steel_column_src_not_same: Sequence[StbSecSteelColumnSrcNotSame] = ...,
        stb_sec_steel_column_src_three_types: Sequence[
            StbSecSteelColumnSrcThreeTypes
        ] = ...,
    ): ...
    @property
    def base_type(self) -> StbSecSteelFigureColumnSrcBaseType:
        """属性(Noneの場合例外) 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）UNEMBEDDED（非埋込）UNEMBEDDED2（非埋込）EMBEDDED（埋込）"""
    @base_type.setter
    def base_type(self, value: StbSecSteelFigureColumnSrcBaseType | str) -> None: ...
    @property
    def base_type_or_none(self) -> StbSecSteelFigureColumnSrcBaseType | None:
        """属性 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）UNEMBEDDED（非埋込）UNEMBEDDED2（非埋込）EMBEDDED（埋込）"""
    @base_type_or_none.setter
    def base_type_or_none(
        self, value: StbSecSteelFigureColumnSrcBaseType | str | None
    ) -> None: ...
    joint_id_top: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_top_or_none: PositiveInteger | None
    """属性"""
    joint_id_bottom: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_bottom_or_none: PositiveInteger | None
    """属性"""
    length_embedded: Length
    """属性(Noneの場合例外) 柱脚埋め込み長さ"""
    length_embedded_or_none: Length | None
    """属性 柱脚埋め込み長さ"""
    stb_sec_steel_column_src_same: StbSecSteelColumnSrcSame
    """子要素(Noneの場合例外)"""
    stb_sec_steel_column_src_same_or_none: StbSecSteelColumnSrcSame | None
    """子要素"""
    @property
    def stb_sec_steel_column_src_not_same(self) -> list[StbSecSteelColumnSrcNotSame]:
        """stb_sec_steel_column_src_not_same (list[StbSecSteelColumnSrcNotSame]): 子要素"""
    @stb_sec_steel_column_src_not_same.setter
    def stb_sec_steel_column_src_not_same(
        self, value: Sequence[StbSecSteelColumnSrcNotSame]
    ) -> None: ...
    @property
    def stb_sec_steel_column_src_three_types(
        self,
    ) -> list[StbSecSteelColumnSrcThreeTypes]:
        """stb_sec_steel_column_src_three_types (list[StbSecSteelColumnSrcThreeTypes]): 子要素"""
    @stb_sec_steel_column_src_three_types.setter
    def stb_sec_steel_column_src_three_types(
        self, value: Sequence[StbSecSteelColumnSrcThreeTypes]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecSteelFigureColumnSrcEnsureAccessor: ...

class StbSecSteelColumnSrcSame(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_column_src_same_shape_h: StbSecColumnSrcSameShapeH | None = ...,
        stb_sec_column_src_same_shape_box: StbSecColumnSrcSameShapeBox | None = ...,
        stb_sec_column_src_same_shape_pipe: StbSecColumnSrcSameShapePipe | None = ...,
        stb_sec_column_src_same_shape_cross: StbSecColumnSrcSameShapeCross | None = ...,
        stb_sec_column_src_same_shape_t: StbSecColumnSrcSameShapeT | None = ...,
    ): ...
    stb_sec_column_src_same_shape_h: StbSecColumnSrcSameShapeH
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_same_shape_h_or_none: StbSecColumnSrcSameShapeH | None
    """子要素"""
    stb_sec_column_src_same_shape_box: StbSecColumnSrcSameShapeBox
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_same_shape_box_or_none: StbSecColumnSrcSameShapeBox | None
    """子要素"""
    stb_sec_column_src_same_shape_pipe: StbSecColumnSrcSameShapePipe
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_same_shape_pipe_or_none: StbSecColumnSrcSameShapePipe | None
    """子要素"""
    stb_sec_column_src_same_shape_cross: StbSecColumnSrcSameShapeCross
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_same_shape_cross_or_none: StbSecColumnSrcSameShapeCross | None
    """子要素"""
    stb_sec_column_src_same_shape_t: StbSecColumnSrcSameShapeT
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_same_shape_t_or_none: StbSecColumnSrcSameShapeT | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecSteelColumnSrcSameEnsureAccessor: ...

class StbSecColumnSrcSameShapeH(StBridgeElement):
    def __init__(
        self,
        *,
        direction_type: StbSecColumnSrcSameShapeHDirectionType | str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    @property
    def direction_type(self) -> StbSecColumnSrcSameShapeHDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecColumnSrcSameShapeHDirectionType | str
    ) -> None: ...
    @property
    def direction_type_or_none(self) -> StbSecColumnSrcSameShapeHDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecColumnSrcSameShapeHDirectionType | str | None
    ) -> None: ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcSameShapeBox(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        encase_type: StbSecColumnSrcSameShapeBoxEncaseType | str | None = ...,
        strength: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    @property
    def encase_type(self) -> StbSecColumnSrcSameShapeBoxEncaseType:
        """属性(Noneの場合例外)"""
    @encase_type.setter
    def encase_type(
        self, value: StbSecColumnSrcSameShapeBoxEncaseType | str
    ) -> None: ...
    @property
    def encase_type_or_none(self) -> StbSecColumnSrcSameShapeBoxEncaseType | None:
        """属性"""
    @encase_type_or_none.setter
    def encase_type_or_none(
        self, value: StbSecColumnSrcSameShapeBoxEncaseType | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcSameShapePipe(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        encase_type: StbSecColumnSrcSameShapePipeEncaseType | str | None = ...,
        strength: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    @property
    def encase_type(self) -> StbSecColumnSrcSameShapePipeEncaseType:
        """属性(Noneの場合例外)"""
    @encase_type.setter
    def encase_type(
        self, value: StbSecColumnSrcSameShapePipeEncaseType | str
    ) -> None: ...
    @property
    def encase_type_or_none(self) -> StbSecColumnSrcSameShapePipeEncaseType | None:
        """属性"""
    @encase_type_or_none.setter
    def encase_type_or_none(
        self, value: StbSecColumnSrcSameShapePipeEncaseType | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcSameShapeCross(StBridgeElement):
    def __init__(
        self,
        *,
        shape_x: str | None = ...,
        shape_y: str | None = ...,
        strength_main_x: str | None = ...,
        strength_web_x: str | None = ...,
        strength_main_y: str | None = ...,
        strength_web_y: str | None = ...,
        offset_xx: float | None = ...,
        offset_xy: float | None = ...,
        offset_yx: float | None = ...,
        offset_yy: float | None = ...,
    ): ...
    shape_x: str
    """属性(Noneの場合例外)"""
    shape_x_or_none: str | None
    """属性"""
    shape_y: str
    """属性(Noneの場合例外)"""
    shape_y_or_none: str | None
    """属性"""
    strength_main_x: str
    """属性(Noneの場合例外)"""
    strength_main_x_or_none: str | None
    """属性"""
    strength_web_x: str
    """属性(Noneの場合例外)"""
    strength_web_x_or_none: str | None
    """属性"""
    strength_main_y: str
    """属性(Noneの場合例外)"""
    strength_main_y_or_none: str | None
    """属性"""
    strength_web_y: str
    """属性(Noneの場合例外)"""
    strength_web_y_or_none: str | None
    """属性"""
    offset_xx: float
    """属性(Noneの場合例外)"""
    offset_xx_or_none: float | None
    """属性"""
    offset_xy: float
    """属性(Noneの場合例外)"""
    offset_xy_or_none: float | None
    """属性"""
    offset_yx: float
    """属性(Noneの場合例外)"""
    offset_yx_or_none: float | None
    """属性"""
    offset_yy: float
    """属性(Noneの場合例外)"""
    offset_yy_or_none: float | None
    """属性"""

class StbSecColumnSrcSameShapeT(StBridgeElement):
    def __init__(
        self,
        *,
        direction_type: StbSecColumnSrcSameShapeTDirectionType | str | None = ...,
        shape_h: str | None = ...,
        shape_t: str | None = ...,
        strength_main_h: str | None = ...,
        strength_web_h: str | None = ...,
        strength_main_t: str | None = ...,
        strength_web_t: str | None = ...,
        offset_hx: float | None = ...,
        offset_hy: float | None = ...,
        offset_t: float | None = ...,
    ): ...
    @property
    def direction_type(self) -> StbSecColumnSrcSameShapeTDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecColumnSrcSameShapeTDirectionType | str
    ) -> None: ...
    @property
    def direction_type_or_none(self) -> StbSecColumnSrcSameShapeTDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecColumnSrcSameShapeTDirectionType | str | None
    ) -> None: ...
    shape_h: str
    """属性(Noneの場合例外)"""
    shape_h_or_none: str | None
    """属性"""
    shape_t: str
    """属性(Noneの場合例外)"""
    shape_t_or_none: str | None
    """属性"""
    strength_main_h: str
    """属性(Noneの場合例外)"""
    strength_main_h_or_none: str | None
    """属性"""
    strength_web_h: str
    """属性(Noneの場合例外)"""
    strength_web_h_or_none: str | None
    """属性"""
    strength_main_t: str
    """属性(Noneの場合例外)"""
    strength_main_t_or_none: str | None
    """属性"""
    strength_web_t: str
    """属性(Noneの場合例外)"""
    strength_web_t_or_none: str | None
    """属性"""
    offset_hx: float
    """属性(Noneの場合例外)"""
    offset_hx_or_none: float | None
    """属性"""
    offset_hy: float
    """属性(Noneの場合例外)"""
    offset_hy_or_none: float | None
    """属性"""
    offset_t: float
    """属性(Noneの場合例外)"""
    offset_t_or_none: float | None
    """属性"""

class StbSecSteelColumnSrcNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelColumnSrcNotSamePos | str | None = ...,
        stb_sec_column_src_not_same_shape_h: StbSecColumnSrcNotSameShapeH | None = ...,
        stb_sec_column_src_not_same_shape_box: StbSecColumnSrcNotSameShapeBox
        | None = ...,
        stb_sec_column_src_not_same_shape_pipe: StbSecColumnSrcNotSameShapePipe
        | None = ...,
        stb_sec_column_src_not_same_shape_cross: StbSecColumnSrcNotSameShapeCross
        | None = ...,
        stb_sec_column_src_not_same_shape_t: StbSecColumnSrcNotSameShapeT | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelColumnSrcNotSamePos:
        """属性(Noneの場合例外) 配置位置 以下のいずれかBOTTOM（柱脚）TOP（柱頭）"""
    @pos.setter
    def pos(self, value: StbSecSteelColumnSrcNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelColumnSrcNotSamePos | None:
        """属性 配置位置 以下のいずれかBOTTOM（柱脚）TOP（柱頭）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecSteelColumnSrcNotSamePos | str | None
    ) -> None: ...
    stb_sec_column_src_not_same_shape_h: StbSecColumnSrcNotSameShapeH
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_not_same_shape_h_or_none: StbSecColumnSrcNotSameShapeH | None
    """子要素"""
    stb_sec_column_src_not_same_shape_box: StbSecColumnSrcNotSameShapeBox
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_not_same_shape_box_or_none: StbSecColumnSrcNotSameShapeBox | None
    """子要素"""
    stb_sec_column_src_not_same_shape_pipe: StbSecColumnSrcNotSameShapePipe
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_not_same_shape_pipe_or_none: (
        StbSecColumnSrcNotSameShapePipe | None
    )
    """子要素"""
    stb_sec_column_src_not_same_shape_cross: StbSecColumnSrcNotSameShapeCross
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_not_same_shape_cross_or_none: (
        StbSecColumnSrcNotSameShapeCross | None
    )
    """子要素"""
    stb_sec_column_src_not_same_shape_t: StbSecColumnSrcNotSameShapeT
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_not_same_shape_t_or_none: StbSecColumnSrcNotSameShapeT | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecSteelColumnSrcNotSameEnsureAccessor: ...

class StbSecColumnSrcNotSameShapeH(StBridgeElement):
    def __init__(
        self,
        *,
        direction_type: StbSecColumnSrcNotSameShapeHDirectionType | str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    @property
    def direction_type(self) -> StbSecColumnSrcNotSameShapeHDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecColumnSrcNotSameShapeHDirectionType | str
    ) -> None: ...
    @property
    def direction_type_or_none(
        self,
    ) -> StbSecColumnSrcNotSameShapeHDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecColumnSrcNotSameShapeHDirectionType | str | None
    ) -> None: ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcNotSameShapeBox(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        encase_type: StbSecColumnSrcNotSameShapeBoxEncaseType | str | None = ...,
        strength: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    @property
    def encase_type(self) -> StbSecColumnSrcNotSameShapeBoxEncaseType:
        """属性(Noneの場合例外)"""
    @encase_type.setter
    def encase_type(
        self, value: StbSecColumnSrcNotSameShapeBoxEncaseType | str
    ) -> None: ...
    @property
    def encase_type_or_none(self) -> StbSecColumnSrcNotSameShapeBoxEncaseType | None:
        """属性"""
    @encase_type_or_none.setter
    def encase_type_or_none(
        self, value: StbSecColumnSrcNotSameShapeBoxEncaseType | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcNotSameShapePipe(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        encase_type: StbSecColumnSrcNotSameShapePipeEncaseType | str | None = ...,
        strength: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    @property
    def encase_type(self) -> StbSecColumnSrcNotSameShapePipeEncaseType:
        """属性(Noneの場合例外)"""
    @encase_type.setter
    def encase_type(
        self, value: StbSecColumnSrcNotSameShapePipeEncaseType | str
    ) -> None: ...
    @property
    def encase_type_or_none(self) -> StbSecColumnSrcNotSameShapePipeEncaseType | None:
        """属性"""
    @encase_type_or_none.setter
    def encase_type_or_none(
        self, value: StbSecColumnSrcNotSameShapePipeEncaseType | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcNotSameShapeCross(StBridgeElement):
    def __init__(
        self,
        *,
        shape_x: str | None = ...,
        shape_y: str | None = ...,
        strength_main_x: str | None = ...,
        strength_web_x: str | None = ...,
        strength_main_y: str | None = ...,
        strength_web_y: str | None = ...,
        offset_xx: float | None = ...,
        offset_xy: float | None = ...,
        offset_yx: float | None = ...,
        offset_yy: float | None = ...,
    ): ...
    shape_x: str
    """属性(Noneの場合例外)"""
    shape_x_or_none: str | None
    """属性"""
    shape_y: str
    """属性(Noneの場合例外)"""
    shape_y_or_none: str | None
    """属性"""
    strength_main_x: str
    """属性(Noneの場合例外)"""
    strength_main_x_or_none: str | None
    """属性"""
    strength_web_x: str
    """属性(Noneの場合例外)"""
    strength_web_x_or_none: str | None
    """属性"""
    strength_main_y: str
    """属性(Noneの場合例外)"""
    strength_main_y_or_none: str | None
    """属性"""
    strength_web_y: str
    """属性(Noneの場合例外)"""
    strength_web_y_or_none: str | None
    """属性"""
    offset_xx: float
    """属性(Noneの場合例外)"""
    offset_xx_or_none: float | None
    """属性"""
    offset_xy: float
    """属性(Noneの場合例外)"""
    offset_xy_or_none: float | None
    """属性"""
    offset_yx: float
    """属性(Noneの場合例外)"""
    offset_yx_or_none: float | None
    """属性"""
    offset_yy: float
    """属性(Noneの場合例外)"""
    offset_yy_or_none: float | None
    """属性"""

class StbSecColumnSrcNotSameShapeT(StBridgeElement):
    def __init__(
        self,
        *,
        direction_type: StbSecColumnSrcNotSameShapeTDirectionType | str | None = ...,
        shape_h: str | None = ...,
        shape_t: str | None = ...,
        strength_main_h: str | None = ...,
        strength_web_h: str | None = ...,
        strength_main_t: str | None = ...,
        strength_web_t: str | None = ...,
        offset_hx: float | None = ...,
        offset_hy: float | None = ...,
        offset_t: float | None = ...,
    ): ...
    @property
    def direction_type(self) -> StbSecColumnSrcNotSameShapeTDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecColumnSrcNotSameShapeTDirectionType | str
    ) -> None: ...
    @property
    def direction_type_or_none(
        self,
    ) -> StbSecColumnSrcNotSameShapeTDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecColumnSrcNotSameShapeTDirectionType | str | None
    ) -> None: ...
    shape_h: str
    """属性(Noneの場合例外)"""
    shape_h_or_none: str | None
    """属性"""
    shape_t: str
    """属性(Noneの場合例外)"""
    shape_t_or_none: str | None
    """属性"""
    strength_main_h: str
    """属性(Noneの場合例外)"""
    strength_main_h_or_none: str | None
    """属性"""
    strength_web_h: str
    """属性(Noneの場合例外)"""
    strength_web_h_or_none: str | None
    """属性"""
    strength_main_t: str
    """属性(Noneの場合例外)"""
    strength_main_t_or_none: str | None
    """属性"""
    strength_web_t: str
    """属性(Noneの場合例外)"""
    strength_web_t_or_none: str | None
    """属性"""
    offset_hx: float
    """属性(Noneの場合例外)"""
    offset_hx_or_none: float | None
    """属性"""
    offset_hy: float
    """属性(Noneの場合例外)"""
    offset_hy_or_none: float | None
    """属性"""
    offset_t: float
    """属性(Noneの場合例外)"""
    offset_t_or_none: float | None
    """属性"""

class StbSecSteelColumnSrcThreeTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelColumnSrcThreeTypesPos | str | None = ...,
        stb_sec_column_src_three_types_shape_h: StbSecColumnSrcThreeTypesShapeH
        | None = ...,
        stb_sec_column_src_three_types_shape_box: StbSecColumnSrcThreeTypesShapeBox
        | None = ...,
        stb_sec_column_src_three_types_shape_pipe: StbSecColumnSrcThreeTypesShapePipe
        | None = ...,
        stb_sec_column_src_three_types_shape_cross: StbSecColumnSrcThreeTypesShapeCross
        | None = ...,
        stb_sec_column_src_three_types_shape_t: StbSecColumnSrcThreeTypesShapeT
        | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelColumnSrcThreeTypesPos:
        """属性(Noneの場合例外) 配置位置 以下のいずれかBOTTOM（柱脚） CENTER（中央）TOP（柱頭）"""
    @pos.setter
    def pos(self, value: StbSecSteelColumnSrcThreeTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelColumnSrcThreeTypesPos | None:
        """属性 配置位置 以下のいずれかBOTTOM（柱脚） CENTER（中央）TOP（柱頭）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecSteelColumnSrcThreeTypesPos | str | None
    ) -> None: ...
    stb_sec_column_src_three_types_shape_h: StbSecColumnSrcThreeTypesShapeH
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_three_types_shape_h_or_none: (
        StbSecColumnSrcThreeTypesShapeH | None
    )
    """子要素"""
    stb_sec_column_src_three_types_shape_box: StbSecColumnSrcThreeTypesShapeBox
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_three_types_shape_box_or_none: (
        StbSecColumnSrcThreeTypesShapeBox | None
    )
    """子要素"""
    stb_sec_column_src_three_types_shape_pipe: StbSecColumnSrcThreeTypesShapePipe
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_three_types_shape_pipe_or_none: (
        StbSecColumnSrcThreeTypesShapePipe | None
    )
    """子要素"""
    stb_sec_column_src_three_types_shape_cross: StbSecColumnSrcThreeTypesShapeCross
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_three_types_shape_cross_or_none: (
        StbSecColumnSrcThreeTypesShapeCross | None
    )
    """子要素"""
    stb_sec_column_src_three_types_shape_t: StbSecColumnSrcThreeTypesShapeT
    """子要素(Noneの場合例外)"""
    stb_sec_column_src_three_types_shape_t_or_none: (
        StbSecColumnSrcThreeTypesShapeT | None
    )
    """子要素"""
    @property
    def ensure(self) -> _StbSecSteelColumnSrcThreeTypesEnsureAccessor: ...

class StbSecColumnSrcThreeTypesShapeH(StBridgeElement):
    def __init__(
        self,
        *,
        direction_type: StbSecColumnSrcThreeTypesShapeHDirectionType | str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    @property
    def direction_type(self) -> StbSecColumnSrcThreeTypesShapeHDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecColumnSrcThreeTypesShapeHDirectionType | str
    ) -> None: ...
    @property
    def direction_type_or_none(
        self,
    ) -> StbSecColumnSrcThreeTypesShapeHDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecColumnSrcThreeTypesShapeHDirectionType | str | None
    ) -> None: ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcThreeTypesShapeBox(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        encase_type: StbSecColumnSrcThreeTypesShapeBoxEncaseType | str | None = ...,
        strength: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    @property
    def encase_type(self) -> StbSecColumnSrcThreeTypesShapeBoxEncaseType:
        """属性(Noneの場合例外)"""
    @encase_type.setter
    def encase_type(
        self, value: StbSecColumnSrcThreeTypesShapeBoxEncaseType | str
    ) -> None: ...
    @property
    def encase_type_or_none(self) -> StbSecColumnSrcThreeTypesShapeBoxEncaseType | None:
        """属性"""
    @encase_type_or_none.setter
    def encase_type_or_none(
        self, value: StbSecColumnSrcThreeTypesShapeBoxEncaseType | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcThreeTypesShapePipe(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        encase_type: StbSecColumnSrcThreeTypesShapePipeEncaseType | str | None = ...,
        strength: str | None = ...,
        offset_x: float | None = ...,
        offset_y: float | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    @property
    def encase_type(self) -> StbSecColumnSrcThreeTypesShapePipeEncaseType:
        """属性(Noneの場合例外)"""
    @encase_type.setter
    def encase_type(
        self, value: StbSecColumnSrcThreeTypesShapePipeEncaseType | str
    ) -> None: ...
    @property
    def encase_type_or_none(
        self,
    ) -> StbSecColumnSrcThreeTypesShapePipeEncaseType | None:
        """属性"""
    @encase_type_or_none.setter
    def encase_type_or_none(
        self, value: StbSecColumnSrcThreeTypesShapePipeEncaseType | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    offset_x: float
    """属性(Noneの場合例外)"""
    offset_x_or_none: float | None
    """属性"""
    offset_y: float
    """属性(Noneの場合例外)"""
    offset_y_or_none: float | None
    """属性"""

class StbSecColumnSrcThreeTypesShapeCross(StBridgeElement):
    def __init__(
        self,
        *,
        shape_x: str | None = ...,
        shape_y: str | None = ...,
        strength_main_x: str | None = ...,
        strength_web_x: str | None = ...,
        strength_main_y: str | None = ...,
        strength_web_y: str | None = ...,
        offset_xx: float | None = ...,
        offset_xy: float | None = ...,
        offset_yx: float | None = ...,
        offset_yy: float | None = ...,
    ): ...
    shape_x: str
    """属性(Noneの場合例外)"""
    shape_x_or_none: str | None
    """属性"""
    shape_y: str
    """属性(Noneの場合例外)"""
    shape_y_or_none: str | None
    """属性"""
    strength_main_x: str
    """属性(Noneの場合例外)"""
    strength_main_x_or_none: str | None
    """属性"""
    strength_web_x: str
    """属性(Noneの場合例外)"""
    strength_web_x_or_none: str | None
    """属性"""
    strength_main_y: str
    """属性(Noneの場合例外)"""
    strength_main_y_or_none: str | None
    """属性"""
    strength_web_y: str
    """属性(Noneの場合例外)"""
    strength_web_y_or_none: str | None
    """属性"""
    offset_xx: float
    """属性(Noneの場合例外)"""
    offset_xx_or_none: float | None
    """属性"""
    offset_xy: float
    """属性(Noneの場合例外)"""
    offset_xy_or_none: float | None
    """属性"""
    offset_yx: float
    """属性(Noneの場合例外)"""
    offset_yx_or_none: float | None
    """属性"""
    offset_yy: float
    """属性(Noneの場合例外)"""
    offset_yy_or_none: float | None
    """属性"""

class StbSecColumnSrcThreeTypesShapeT(StBridgeElement):
    def __init__(
        self,
        *,
        direction_type: StbSecColumnSrcThreeTypesShapeTDirectionType | str | None = ...,
        shape_h: str | None = ...,
        shape_t: str | None = ...,
        strength_main_h: str | None = ...,
        strength_web_h: str | None = ...,
        strength_main_t: str | None = ...,
        strength_web_t: str | None = ...,
        offset_hx: float | None = ...,
        offset_hy: float | None = ...,
        offset_t: float | None = ...,
    ): ...
    @property
    def direction_type(self) -> StbSecColumnSrcThreeTypesShapeTDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecColumnSrcThreeTypesShapeTDirectionType | str
    ) -> None: ...
    @property
    def direction_type_or_none(
        self,
    ) -> StbSecColumnSrcThreeTypesShapeTDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecColumnSrcThreeTypesShapeTDirectionType | str | None
    ) -> None: ...
    shape_h: str
    """属性(Noneの場合例外)"""
    shape_h_or_none: str | None
    """属性"""
    shape_t: str
    """属性(Noneの場合例外)"""
    shape_t_or_none: str | None
    """属性"""
    strength_main_h: str
    """属性(Noneの場合例外)"""
    strength_main_h_or_none: str | None
    """属性"""
    strength_web_h: str
    """属性(Noneの場合例外)"""
    strength_web_h_or_none: str | None
    """属性"""
    strength_main_t: str
    """属性(Noneの場合例外)"""
    strength_main_t_or_none: str | None
    """属性"""
    strength_web_t: str
    """属性(Noneの場合例外)"""
    strength_web_t_or_none: str | None
    """属性"""
    offset_hx: float
    """属性(Noneの場合例外)"""
    offset_hx_or_none: float | None
    """属性"""
    offset_hy: float
    """属性(Noneの場合例外)"""
    offset_hy_or_none: float | None
    """属性"""
    offset_t: float
    """属性(Noneの場合例外)"""
    offset_t_or_none: float | None
    """属性"""

class StbSecBaseProductSrc(StBridgeElement):
    def __init__(
        self,
        *,
        product_company: str | None = ...,
        product_code: str | None = ...,
        direction_type: StbSecBaseProductSrcDirectionType | int | None = ...,
        height_mortar: NonNegativeLength | None = ...,
    ): ...
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    @property
    def direction_type(self) -> StbSecBaseProductSrcDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecBaseProductSrcDirectionType | int
    ) -> None: ...
    @property
    def direction_type_or_none(self) -> StbSecBaseProductSrcDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecBaseProductSrcDirectionType | int | None
    ) -> None: ...
    height_mortar: NonNegativeLength
    """属性(Noneの場合例外)"""
    height_mortar_or_none: NonNegativeLength | None
    """属性"""

class StbSecBaseConventionalSrc(StBridgeElement):
    def __init__(
        self,
        *,
        height_mortar: NonNegativeLength | None = ...,
        stb_sec_base_conventional_src_plate: StbSecBaseConventionalSrcPlate
        | None = ...,
        stb_sec_base_conventional_src_anchor_bolt: StbSecBaseConventionalSrcAnchorBolt
        | None = ...,
        stb_sec_base_conventional_src_rib_plate: StbSecBaseConventionalSrcRibPlate
        | None = ...,
    ): ...
    height_mortar: NonNegativeLength
    """属性(Noneの場合例外)"""
    height_mortar_or_none: NonNegativeLength | None
    """属性"""
    stb_sec_base_conventional_src_plate: StbSecBaseConventionalSrcPlate
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_src_plate_or_none: StbSecBaseConventionalSrcPlate | None
    """子要素"""
    stb_sec_base_conventional_src_anchor_bolt: StbSecBaseConventionalSrcAnchorBolt
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_src_anchor_bolt_or_none: (
        StbSecBaseConventionalSrcAnchorBolt | None
    )
    """子要素"""
    stb_sec_base_conventional_src_rib_plate: StbSecBaseConventionalSrcRibPlate
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_src_rib_plate_or_none: (
        StbSecBaseConventionalSrcRibPlate | None
    )
    """子要素"""
    @property
    def ensure(self) -> _StbSecBaseConventionalSrcEnsureAccessor: ...

class StbSecBaseConventionalSrcPlate(StBridgeElement):
    def __init__(
        self,
        *,
        b_x: Length | None = ...,
        b_y: Length | None = ...,
        c1_x: NonNegativeLength | None = ...,
        c1_y: NonNegativeLength | None = ...,
        c2_x: NonNegativeLength | None = ...,
        c2_y: NonNegativeLength | None = ...,
        c3_x: NonNegativeLength | None = ...,
        c3_y: NonNegativeLength | None = ...,
        c4_x: NonNegativeLength | None = ...,
        c4_y: NonNegativeLength | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
        d_bolthole: Length | None = ...,
        offset_x: NonNegativeLength | None = ...,
        offset_y: NonNegativeLength | None = ...,
    ): ...
    b_x: Length
    """属性(Noneの場合例外)"""
    b_x_or_none: Length | None
    """属性"""
    b_y: Length
    """属性(Noneの場合例外)"""
    b_y_or_none: Length | None
    """属性"""
    c1_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c1_x_or_none: NonNegativeLength | None
    """属性"""
    c1_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c1_y_or_none: NonNegativeLength | None
    """属性"""
    c2_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c2_x_or_none: NonNegativeLength | None
    """属性"""
    c2_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c2_y_or_none: NonNegativeLength | None
    """属性"""
    c3_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c3_x_or_none: NonNegativeLength | None
    """属性"""
    c3_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c3_y_or_none: NonNegativeLength | None
    """属性"""
    c4_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c4_x_or_none: NonNegativeLength | None
    """属性"""
    c4_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c4_y_or_none: NonNegativeLength | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d_bolthole: Length
    """属性(Noneの場合例外)"""
    d_bolthole_or_none: Length | None
    """属性"""
    offset_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_x_or_none: NonNegativeLength | None
    """属性"""
    offset_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_y_or_none: NonNegativeLength | None
    """属性"""

class StbSecBaseConventionalSrcAnchorBolt(StBridgeElement):
    def __init__(
        self,
        *,
        kind_bolt: StbSecBaseConventionalSrcAnchorBoltKindBolt | str | None = ...,
        name_bolt: str | None = ...,
        length_bolt: Length | None = ...,
        strength_bolt: str | None = ...,
        arrangement_bolt: StbSecBaseConventionalSrcAnchorBoltArrangementBolt
        | str
        | None = ...,
        d1_x: Length | None = ...,
        d2_x: Length | None = ...,
        d1_y: Length | None = ...,
        d2_y: Length | None = ...,
        n_x: PositiveInteger | None = ...,
        n_y: PositiveInteger | None = ...,
    ): ...
    @property
    def kind_bolt(self) -> StbSecBaseConventionalSrcAnchorBoltKindBolt:
        """属性(Noneの場合例外)"""
    @kind_bolt.setter
    def kind_bolt(
        self, value: StbSecBaseConventionalSrcAnchorBoltKindBolt | str
    ) -> None: ...
    @property
    def kind_bolt_or_none(self) -> StbSecBaseConventionalSrcAnchorBoltKindBolt | None:
        """属性"""
    @kind_bolt_or_none.setter
    def kind_bolt_or_none(
        self, value: StbSecBaseConventionalSrcAnchorBoltKindBolt | str | None
    ) -> None: ...
    name_bolt: str
    """属性(Noneの場合例外)"""
    name_bolt_or_none: str | None
    """属性"""
    length_bolt: Length
    """属性(Noneの場合例外)"""
    length_bolt_or_none: Length | None
    """属性"""
    strength_bolt: str
    """属性(Noneの場合例外)"""
    strength_bolt_or_none: str | None
    """属性"""
    @property
    def arrangement_bolt(self) -> StbSecBaseConventionalSrcAnchorBoltArrangementBolt:
        """属性(Noneの場合例外)"""
    @arrangement_bolt.setter
    def arrangement_bolt(
        self, value: StbSecBaseConventionalSrcAnchorBoltArrangementBolt | str
    ) -> None: ...
    @property
    def arrangement_bolt_or_none(
        self,
    ) -> StbSecBaseConventionalSrcAnchorBoltArrangementBolt | None:
        """属性"""
    @arrangement_bolt_or_none.setter
    def arrangement_bolt_or_none(
        self, value: StbSecBaseConventionalSrcAnchorBoltArrangementBolt | str | None
    ) -> None: ...
    d1_x: Length
    """属性(Noneの場合例外)"""
    d1_x_or_none: Length | None
    """属性"""
    d2_x: Length
    """属性(Noneの場合例外)"""
    d2_x_or_none: Length | None
    """属性"""
    d1_y: Length
    """属性(Noneの場合例外)"""
    d1_y_or_none: Length | None
    """属性"""
    d2_y: Length
    """属性(Noneの場合例外)"""
    d2_y_or_none: Length | None
    """属性"""
    n_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_x_or_none: PositiveInteger | None
    """属性"""
    n_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBaseConventionalSrcRibPlate(StBridgeElement):
    def __init__(
        self,
        *,
        a1: Length | None = ...,
        a2: NonNegativeLength | None = ...,
        b1: Length | None = ...,
        b2: NonNegativeLength | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
        n_x: PositiveInteger | None = ...,
        n_y: PositiveInteger | None = ...,
        length_e_x: Length | None = ...,
        length_e_y: Length | None = ...,
    ): ...
    a1: Length
    """属性(Noneの場合例外)"""
    a1_or_none: Length | None
    """属性"""
    a2: NonNegativeLength
    """属性(Noneの場合例外)"""
    a2_or_none: NonNegativeLength | None
    """属性"""
    b1: Length
    """属性(Noneの場合例外)"""
    b1_or_none: Length | None
    """属性"""
    b2: NonNegativeLength
    """属性(Noneの場合例外)"""
    b2_or_none: NonNegativeLength | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    n_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_x_or_none: PositiveInteger | None
    """属性"""
    n_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_y_or_none: PositiveInteger | None
    """属性"""
    length_e_x: Length
    """属性(Noneの場合例外)"""
    length_e_x_or_none: Length | None
    """属性"""
    length_e_y: Length
    """属性(Noneの場合例外)"""
    length_e_y_or_none: Length | None
    """属性"""

class StbSecColumnCft(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_column: StbSecColumnCftKindColumn | str | None = ...,
        strength_concrete: str | None = ...,
        is_reference_direction: bool | None = ...,
        stb_sec_steel_figure_column_cft: StbSecSteelFigureColumnCft | None = ...,
        stb_sec_base_product_cft: StbSecBaseProductCft | None = ...,
        stb_sec_base_conventional_cft: StbSecBaseConventionalCft | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_column(self) -> StbSecColumnCftKindColumn:
        """属性(Noneの場合例外) 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column.setter
    def kind_column(self, value: StbSecColumnCftKindColumn | str) -> None: ...
    @property
    def kind_column_or_none(self) -> StbSecColumnCftKindColumn | None:
        """属性 柱の種別以下のいずれかCOLUMN（柱）POST（間柱）"""
    @kind_column_or_none.setter
    def kind_column_or_none(
        self, value: StbSecColumnCftKindColumn | str | None
    ) -> None: ...
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    is_reference_direction: bool
    """属性(Noneの場合例外) 鉄骨向き"""
    is_reference_direction_or_none: bool | None
    """属性 鉄骨向き"""
    stb_sec_steel_figure_column_cft: StbSecSteelFigureColumnCft
    """子要素(Noneの場合例外)"""
    stb_sec_steel_figure_column_cft_or_none: StbSecSteelFigureColumnCft | None
    """子要素"""
    stb_sec_base_product_cft: StbSecBaseProductCft
    """子要素(Noneの場合例外)"""
    stb_sec_base_product_cft_or_none: StbSecBaseProductCft | None
    """子要素"""
    stb_sec_base_conventional_cft: StbSecBaseConventionalCft
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_cft_or_none: StbSecBaseConventionalCft | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecColumnCftEnsureAccessor: ...

class StbSecSteelFigureColumnCft(StBridgeElement):
    def __init__(
        self,
        *,
        base_type: StbSecSteelFigureColumnCftBaseType | str | None = ...,
        stb_sec_steel_column_cft_same: StbSecSteelColumnCftSame | None = ...,
        stb_sec_steel_column_cft_not_same: Sequence[StbSecSteelColumnCftNotSame] = ...,
        stb_sec_steel_column_cft_three_types: Sequence[
            StbSecSteelColumnCftThreeTypes
        ] = ...,
    ): ...
    @property
    def base_type(self) -> StbSecSteelFigureColumnCftBaseType:
        """属性(Noneの場合例外) 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）EXPOSE（露出）EMBEDDED（埋込）"""
    @base_type.setter
    def base_type(self, value: StbSecSteelFigureColumnCftBaseType | str) -> None: ...
    @property
    def base_type_or_none(self) -> StbSecSteelFigureColumnCftBaseType | None:
        """属性 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）EXPOSE（露出）EMBEDDED（埋込）"""
    @base_type_or_none.setter
    def base_type_or_none(
        self, value: StbSecSteelFigureColumnCftBaseType | str | None
    ) -> None: ...
    stb_sec_steel_column_cft_same: StbSecSteelColumnCftSame
    """子要素(Noneの場合例外)"""
    stb_sec_steel_column_cft_same_or_none: StbSecSteelColumnCftSame | None
    """子要素"""
    @property
    def stb_sec_steel_column_cft_not_same(self) -> list[StbSecSteelColumnCftNotSame]:
        """stb_sec_steel_column_cft_not_same (list[StbSecSteelColumnCftNotSame]): 子要素"""
    @stb_sec_steel_column_cft_not_same.setter
    def stb_sec_steel_column_cft_not_same(
        self, value: Sequence[StbSecSteelColumnCftNotSame]
    ) -> None: ...
    @property
    def stb_sec_steel_column_cft_three_types(
        self,
    ) -> list[StbSecSteelColumnCftThreeTypes]:
        """stb_sec_steel_column_cft_three_types (list[StbSecSteelColumnCftThreeTypes]): 子要素"""
    @stb_sec_steel_column_cft_three_types.setter
    def stb_sec_steel_column_cft_three_types(
        self, value: Sequence[StbSecSteelColumnCftThreeTypes]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecSteelFigureColumnCftEnsureAccessor: ...

class StbSecSteelColumnCftSame(StBridgeElement):
    def __init__(self, *, shape: str | None = ..., strength: str | None = ...): ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength: str
    """属性(Noneの場合例外) 鉄骨強度"""
    strength_or_none: str | None
    """属性 鉄骨強度"""

class StbSecSteelColumnCftNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelColumnCftNotSamePos | str | None = ...,
        shape: str | None = ...,
        strength: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelColumnCftNotSamePos:
        """属性(Noneの場合例外) 配置位置以下のいずれかBOTTOM（柱脚）TOP（柱頭）"""
    @pos.setter
    def pos(self, value: StbSecSteelColumnCftNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelColumnCftNotSamePos | None:
        """属性 配置位置以下のいずれかBOTTOM（柱脚）TOP（柱頭）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecSteelColumnCftNotSamePos | str | None
    ) -> None: ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength: str
    """属性(Noneの場合例外) 鉄骨強度"""
    strength_or_none: str | None
    """属性 鉄骨強度"""

class StbSecSteelColumnCftThreeTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelColumnCftThreeTypesPos | str | None = ...,
        shape: str | None = ...,
        strength: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelColumnCftThreeTypesPos:
        """属性(Noneの場合例外) 配置位置以下のいずれかBOTTOM（柱脚）CENTER（中央）TOP（柱頭）"""
    @pos.setter
    def pos(self, value: StbSecSteelColumnCftThreeTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelColumnCftThreeTypesPos | None:
        """属性 配置位置以下のいずれかBOTTOM（柱脚）CENTER（中央）TOP（柱頭）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecSteelColumnCftThreeTypesPos | str | None
    ) -> None: ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength: str
    """属性(Noneの場合例外) 鉄骨強度"""
    strength_or_none: str | None
    """属性 鉄骨強度"""

class StbSecBaseProductCft(StBridgeElement):
    def __init__(
        self,
        *,
        product_company: str | None = ...,
        product_code: str | None = ...,
        direction_type: StbSecBaseProductCftDirectionType | int | None = ...,
        height_mortar: NonNegativeLength | None = ...,
    ): ...
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    @property
    def direction_type(self) -> StbSecBaseProductCftDirectionType:
        """属性(Noneの場合例外)"""
    @direction_type.setter
    def direction_type(
        self, value: StbSecBaseProductCftDirectionType | int
    ) -> None: ...
    @property
    def direction_type_or_none(self) -> StbSecBaseProductCftDirectionType | None:
        """属性"""
    @direction_type_or_none.setter
    def direction_type_or_none(
        self, value: StbSecBaseProductCftDirectionType | int | None
    ) -> None: ...
    height_mortar: NonNegativeLength
    """属性(Noneの場合例外)"""
    height_mortar_or_none: NonNegativeLength | None
    """属性"""

class StbSecBaseConventionalCft(StBridgeElement):
    def __init__(
        self,
        *,
        height_mortar: NonNegativeLength | None = ...,
        stb_sec_base_conventional_cft_plate: StbSecBaseConventionalCftPlate
        | None = ...,
        stb_sec_base_conventional_cft_anchor_bolt: StbSecBaseConventionalCftAnchorBolt
        | None = ...,
        stb_sec_base_conventional_cft_rib_plate: StbSecBaseConventionalCftRibPlate
        | None = ...,
    ): ...
    height_mortar: NonNegativeLength
    """属性(Noneの場合例外)"""
    height_mortar_or_none: NonNegativeLength | None
    """属性"""
    stb_sec_base_conventional_cft_plate: StbSecBaseConventionalCftPlate
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_cft_plate_or_none: StbSecBaseConventionalCftPlate | None
    """子要素"""
    stb_sec_base_conventional_cft_anchor_bolt: StbSecBaseConventionalCftAnchorBolt
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_cft_anchor_bolt_or_none: (
        StbSecBaseConventionalCftAnchorBolt | None
    )
    """子要素"""
    stb_sec_base_conventional_cft_rib_plate: StbSecBaseConventionalCftRibPlate
    """子要素(Noneの場合例外)"""
    stb_sec_base_conventional_cft_rib_plate_or_none: (
        StbSecBaseConventionalCftRibPlate | None
    )
    """子要素"""
    @property
    def ensure(self) -> _StbSecBaseConventionalCftEnsureAccessor: ...

class StbSecBaseConventionalCftPlate(StBridgeElement):
    def __init__(
        self,
        *,
        b_x: Length | None = ...,
        b_y: Length | None = ...,
        c1_x: NonNegativeLength | None = ...,
        c1_y: NonNegativeLength | None = ...,
        c2_x: NonNegativeLength | None = ...,
        c2_y: NonNegativeLength | None = ...,
        c3_x: NonNegativeLength | None = ...,
        c3_y: NonNegativeLength | None = ...,
        c4_x: NonNegativeLength | None = ...,
        c4_y: NonNegativeLength | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
        d_bolthole: Length | None = ...,
        offset_x: NonNegativeLength | None = ...,
        offset_y: NonNegativeLength | None = ...,
    ): ...
    b_x: Length
    """属性(Noneの場合例外)"""
    b_x_or_none: Length | None
    """属性"""
    b_y: Length
    """属性(Noneの場合例外)"""
    b_y_or_none: Length | None
    """属性"""
    c1_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c1_x_or_none: NonNegativeLength | None
    """属性"""
    c1_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c1_y_or_none: NonNegativeLength | None
    """属性"""
    c2_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c2_x_or_none: NonNegativeLength | None
    """属性"""
    c2_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c2_y_or_none: NonNegativeLength | None
    """属性"""
    c3_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c3_x_or_none: NonNegativeLength | None
    """属性"""
    c3_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c3_y_or_none: NonNegativeLength | None
    """属性"""
    c4_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    c4_x_or_none: NonNegativeLength | None
    """属性"""
    c4_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    c4_y_or_none: NonNegativeLength | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d_bolthole: Length
    """属性(Noneの場合例外)"""
    d_bolthole_or_none: Length | None
    """属性"""
    offset_x: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_x_or_none: NonNegativeLength | None
    """属性"""
    offset_y: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_y_or_none: NonNegativeLength | None
    """属性"""

class StbSecBaseConventionalCftAnchorBolt(StBridgeElement):
    def __init__(
        self,
        *,
        kind_bolt: StbSecBaseConventionalCftAnchorBoltKindBolt | str | None = ...,
        name_bolt: str | None = ...,
        length_bolt: Length | None = ...,
        strength_bolt: str | None = ...,
        arrangement_bolt: StbSecBaseConventionalCftAnchorBoltArrangementBolt
        | str
        | None = ...,
        d1_x: Length | None = ...,
        d2_x: Length | None = ...,
        d1_y: Length | None = ...,
        d2_y: Length | None = ...,
        n_x: PositiveInteger | None = ...,
        n_y: PositiveInteger | None = ...,
    ): ...
    @property
    def kind_bolt(self) -> StbSecBaseConventionalCftAnchorBoltKindBolt:
        """属性(Noneの場合例外)"""
    @kind_bolt.setter
    def kind_bolt(
        self, value: StbSecBaseConventionalCftAnchorBoltKindBolt | str
    ) -> None: ...
    @property
    def kind_bolt_or_none(self) -> StbSecBaseConventionalCftAnchorBoltKindBolt | None:
        """属性"""
    @kind_bolt_or_none.setter
    def kind_bolt_or_none(
        self, value: StbSecBaseConventionalCftAnchorBoltKindBolt | str | None
    ) -> None: ...
    name_bolt: str
    """属性(Noneの場合例外)"""
    name_bolt_or_none: str | None
    """属性"""
    length_bolt: Length
    """属性(Noneの場合例外)"""
    length_bolt_or_none: Length | None
    """属性"""
    strength_bolt: str
    """属性(Noneの場合例外)"""
    strength_bolt_or_none: str | None
    """属性"""
    @property
    def arrangement_bolt(self) -> StbSecBaseConventionalCftAnchorBoltArrangementBolt:
        """属性(Noneの場合例外)"""
    @arrangement_bolt.setter
    def arrangement_bolt(
        self, value: StbSecBaseConventionalCftAnchorBoltArrangementBolt | str
    ) -> None: ...
    @property
    def arrangement_bolt_or_none(
        self,
    ) -> StbSecBaseConventionalCftAnchorBoltArrangementBolt | None:
        """属性"""
    @arrangement_bolt_or_none.setter
    def arrangement_bolt_or_none(
        self, value: StbSecBaseConventionalCftAnchorBoltArrangementBolt | str | None
    ) -> None: ...
    d1_x: Length
    """属性(Noneの場合例外)"""
    d1_x_or_none: Length | None
    """属性"""
    d2_x: Length
    """属性(Noneの場合例外)"""
    d2_x_or_none: Length | None
    """属性"""
    d1_y: Length
    """属性(Noneの場合例外)"""
    d1_y_or_none: Length | None
    """属性"""
    d2_y: Length
    """属性(Noneの場合例外)"""
    d2_y_or_none: Length | None
    """属性"""
    n_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_x_or_none: PositiveInteger | None
    """属性"""
    n_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_y_or_none: PositiveInteger | None
    """属性"""

class StbSecBaseConventionalCftRibPlate(StBridgeElement):
    def __init__(
        self,
        *,
        a1: Length | None = ...,
        a2: NonNegativeLength | None = ...,
        b1: Length | None = ...,
        b2: NonNegativeLength | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
        n_x: PositiveInteger | None = ...,
        n_y: PositiveInteger | None = ...,
        length_e_x: Length | None = ...,
        length_e_y: Length | None = ...,
    ): ...
    a1: Length
    """属性(Noneの場合例外)"""
    a1_or_none: Length | None
    """属性"""
    a2: NonNegativeLength
    """属性(Noneの場合例外)"""
    a2_or_none: NonNegativeLength | None
    """属性"""
    b1: Length
    """属性(Noneの場合例外)"""
    b1_or_none: Length | None
    """属性"""
    b2: NonNegativeLength
    """属性(Noneの場合例外)"""
    b2_or_none: NonNegativeLength | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    n_x: PositiveInteger
    """属性(Noneの場合例外)"""
    n_x_or_none: PositiveInteger | None
    """属性"""
    n_y: PositiveInteger
    """属性(Noneの場合例外)"""
    n_y_or_none: PositiveInteger | None
    """属性"""
    length_e_x: Length
    """属性(Noneの場合例外)"""
    length_e_x_or_none: Length | None
    """属性"""
    length_e_y: Length
    """属性(Noneの場合例外)"""
    length_e_y_or_none: Length | None
    """属性"""

class StbSecBeamRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_beam: StbSecBeamRcKindBeam | str | None = ...,
        is_foundation: bool | None = ...,
        is_canti: bool | None = ...,
        is_outin: bool | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_beam_rc: StbSecFigureBeamRc | None = ...,
        stb_sec_bar_arrangement_beam_rc: StbSecBarArrangementBeamRc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_beam(self) -> StbSecBeamRcKindBeam:
        """属性(Noneの場合例外) 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）"""
    @kind_beam.setter
    def kind_beam(self, value: StbSecBeamRcKindBeam | str) -> None: ...
    @property
    def kind_beam_or_none(self) -> StbSecBeamRcKindBeam | None:
        """属性 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）"""
    @kind_beam_or_none.setter
    def kind_beam_or_none(self, value: StbSecBeamRcKindBeam | str | None) -> None: ...
    is_foundation: bool
    """属性(Noneの場合例外) 基礎梁か否か"""
    is_foundation_or_none: bool | None
    """属性 基礎梁か否か"""
    is_canti: bool
    """属性(Noneの場合例外) 片持ち梁か否か"""
    is_canti_or_none: bool | None
    """属性 片持ち梁か否か"""
    is_outin: bool
    """属性(Noneの場合例外) 外端・内端指定"""
    is_outin_or_none: bool | None
    """属性 外端・内端指定"""
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_beam_rc: StbSecFigureBeamRc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_beam_rc_or_none: StbSecFigureBeamRc | None
    """子要素"""
    stb_sec_bar_arrangement_beam_rc: StbSecBarArrangementBeamRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_beam_rc_or_none: StbSecBarArrangementBeamRc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecBeamRcEnsureAccessor: ...

class StbSecFigureBeamRc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_beam_rc_straight: StbSecBeamRcStraight | None = ...,
        stb_sec_beam_rc_taper: Sequence[StbSecBeamRcTaper] = ...,
        stb_sec_beam_rc_haunch: Sequence[StbSecBeamRcHaunch] = ...,
    ): ...
    stb_sec_beam_rc_straight: StbSecBeamRcStraight
    """子要素(Noneの場合例外)"""
    stb_sec_beam_rc_straight_or_none: StbSecBeamRcStraight | None
    """子要素"""
    @property
    def stb_sec_beam_rc_taper(self) -> list[StbSecBeamRcTaper]:
        """stb_sec_beam_rc_taper (list[StbSecBeamRcTaper]): 子要素"""
    @stb_sec_beam_rc_taper.setter
    def stb_sec_beam_rc_taper(self, value: Sequence[StbSecBeamRcTaper]) -> None: ...
    @property
    def stb_sec_beam_rc_haunch(self) -> list[StbSecBeamRcHaunch]:
        """stb_sec_beam_rc_haunch (list[StbSecBeamRcHaunch]): 子要素"""
    @stb_sec_beam_rc_haunch.setter
    def stb_sec_beam_rc_haunch(self, value: Sequence[StbSecBeamRcHaunch]) -> None: ...
    @property
    def ensure(self) -> _StbSecFigureBeamRcEnsureAccessor: ...

class StbSecBeamRcStraight(StBridgeElement):
    def __init__(self, *, width: Length | None = ..., depth: Length | None = ...): ...
    width: Length
    """属性(Noneの場合例外)"""
    width_or_none: Length | None
    """属性"""
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBeamRcTaper(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBeamRcTaperPos | str | None = ...,
        width: Length | None = ...,
        depth: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBeamRcTaperPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBeamRcTaperPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBeamRcTaperPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBeamRcTaperPos | str | None) -> None: ...
    width: Length
    """属性(Noneの場合例外)"""
    width_or_none: Length | None
    """属性"""
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBeamRcHaunch(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBeamRcHaunchPos | str | None = ...,
        width: Length | None = ...,
        depth: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBeamRcHaunchPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBeamRcHaunchPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBeamRcHaunchPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBeamRcHaunchPos | str | None) -> None: ...
    width: Length
    """属性(Noneの場合例外)"""
    width_or_none: Length | None
    """属性"""
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBarArrangementBeamRc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_left: Length | None = ...,
        depth_cover_right: Length | None = ...,
        depth_cover_top: Length | None = ...,
        depth_cover_bottom: Length | None = ...,
        interval: Length | None = ...,
        center_top: Length | None = ...,
        center_bottom: Length | None = ...,
        center_side: Length | None = ...,
        center_interval: Length | None = ...,
        length_bar_start: Length | None = ...,
        length_bar_end: Length | None = ...,
        stb_sec_bar_beam_rc_same: StbSecBarBeamRcSame | None = ...,
        stb_sec_bar_beam_rc_three_types: Sequence[StbSecBarBeamRcThreeTypes] = ...,
        stb_sec_bar_beam_rc_start_end: Sequence[StbSecBarBeamRcStartEnd] = ...,
        stb_sec_bar_beam_x_reinforced: StbSecBarBeamXReinforced | None = ...,
    ): ...
    depth_cover_left: Length
    """属性(Noneの場合例外)"""
    depth_cover_left_or_none: Length | None
    """属性"""
    depth_cover_right: Length
    """属性(Noneの場合例外)"""
    depth_cover_right_or_none: Length | None
    """属性"""
    depth_cover_top: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_or_none: Length | None
    """属性"""
    depth_cover_bottom: Length
    """属性(Noneの場合例外)"""
    depth_cover_bottom_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    center_top: Length
    """属性(Noneの場合例外)"""
    center_top_or_none: Length | None
    """属性"""
    center_bottom: Length
    """属性(Noneの場合例外)"""
    center_bottom_or_none: Length | None
    """属性"""
    center_side: Length
    """属性(Noneの場合例外)"""
    center_side_or_none: Length | None
    """属性"""
    center_interval: Length
    """属性(Noneの場合例外)"""
    center_interval_or_none: Length | None
    """属性"""
    length_bar_start: Length
    """属性(Noneの場合例外)"""
    length_bar_start_or_none: Length | None
    """属性"""
    length_bar_end: Length
    """属性(Noneの場合例外)"""
    length_bar_end_or_none: Length | None
    """属性"""
    stb_sec_bar_beam_rc_same: StbSecBarBeamRcSame
    """子要素(Noneの場合例外)"""
    stb_sec_bar_beam_rc_same_or_none: StbSecBarBeamRcSame | None
    """子要素"""
    @property
    def stb_sec_bar_beam_rc_three_types(self) -> list[StbSecBarBeamRcThreeTypes]:
        """stb_sec_bar_beam_rc_three_types (list[StbSecBarBeamRcThreeTypes]): 子要素"""
    @stb_sec_bar_beam_rc_three_types.setter
    def stb_sec_bar_beam_rc_three_types(
        self, value: Sequence[StbSecBarBeamRcThreeTypes]
    ) -> None: ...
    @property
    def stb_sec_bar_beam_rc_start_end(self) -> list[StbSecBarBeamRcStartEnd]:
        """stb_sec_bar_beam_rc_start_end (list[StbSecBarBeamRcStartEnd]): 子要素"""
    @stb_sec_bar_beam_rc_start_end.setter
    def stb_sec_bar_beam_rc_start_end(
        self, value: Sequence[StbSecBarBeamRcStartEnd]
    ) -> None: ...
    stb_sec_bar_beam_x_reinforced: StbSecBarBeamXReinforced
    """子要素(Noneの場合例外)"""
    stb_sec_bar_beam_x_reinforced_or_none: StbSecBarBeamXReinforced | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecBarArrangementBeamRcEnsureAccessor: ...

class StbSecBarBeamRcSame(StBridgeElement):
    def __init__(
        self,
        *,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_stirrup: str | None = ...,
        d_web: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_stirrup: str | None = ...,
        strength_web: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_top_1st: PositiveInteger | None = ...,
        n_main_top_2nd: PositiveInteger | None = ...,
        n_main_top_3rd: PositiveInteger | None = ...,
        n_main_bottom_1st: PositiveInteger | None = ...,
        n_main_bottom_2nd: PositiveInteger | None = ...,
        n_main_bottom_3rd: PositiveInteger | None = ...,
        n_2nd_main_top_1st: PositiveInteger | None = ...,
        n_2nd_main_top_2nd: PositiveInteger | None = ...,
        n_2nd_main_top_3rd: PositiveInteger | None = ...,
        n_2nd_main_bottom_1st: PositiveInteger | None = ...,
        n_2nd_main_bottom_2nd: PositiveInteger | None = ...,
        n_2nd_main_bottom_3rd: PositiveInteger | None = ...,
        n_stirrup: PositiveInteger | None = ...,
        pitch_stirrup: Length | None = ...,
        n_web: PositiveInteger | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
    ): ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_stirrup: str
    """属性(Noneの場合例外)"""
    d_stirrup_or_none: str | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_stirrup: str
    """属性(Noneの場合例外)"""
    strength_stirrup_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_stirrup: PositiveInteger
    """属性(Noneの場合例外)"""
    n_stirrup_or_none: PositiveInteger | None
    """属性"""
    pitch_stirrup: Length
    """属性(Noneの場合例外)"""
    pitch_stirrup_or_none: Length | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""

class StbSecBarBeamRcThreeTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarBeamRcThreeTypesPos | str | None = ...,
        pos_name: str | None = ...,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_stirrup: str | None = ...,
        d_web: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_stirrup: str | None = ...,
        strength_web: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_top_1st: PositiveInteger | None = ...,
        n_main_top_2nd: PositiveInteger | None = ...,
        n_main_top_3rd: PositiveInteger | None = ...,
        n_main_bottom_1st: PositiveInteger | None = ...,
        n_main_bottom_2nd: PositiveInteger | None = ...,
        n_main_bottom_3rd: PositiveInteger | None = ...,
        n_2nd_main_top_1st: PositiveInteger | None = ...,
        n_2nd_main_top_2nd: PositiveInteger | None = ...,
        n_2nd_main_top_3rd: PositiveInteger | None = ...,
        n_2nd_main_bottom_1st: PositiveInteger | None = ...,
        n_2nd_main_bottom_2nd: PositiveInteger | None = ...,
        n_2nd_main_bottom_3rd: PositiveInteger | None = ...,
        n_stirrup: PositiveInteger | None = ...,
        pitch_stirrup: Length | None = ...,
        n_web: PositiveInteger | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarBeamRcThreeTypesPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarBeamRcThreeTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarBeamRcThreeTypesPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarBeamRcThreeTypesPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_stirrup: str
    """属性(Noneの場合例外)"""
    d_stirrup_or_none: str | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_stirrup: str
    """属性(Noneの場合例外)"""
    strength_stirrup_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_stirrup: PositiveInteger
    """属性(Noneの場合例外)"""
    n_stirrup_or_none: PositiveInteger | None
    """属性"""
    pitch_stirrup: Length
    """属性(Noneの場合例外)"""
    pitch_stirrup_or_none: Length | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""

class StbSecBarBeamRcStartEnd(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarBeamRcStartEndPos | str | None = ...,
        pos_name: str | None = ...,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_stirrup: str | None = ...,
        d_web: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_stirrup: str | None = ...,
        strength_web: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_top_1st: PositiveInteger | None = ...,
        n_main_top_2nd: PositiveInteger | None = ...,
        n_main_top_3rd: PositiveInteger | None = ...,
        n_main_bottom_1st: PositiveInteger | None = ...,
        n_main_bottom_2nd: PositiveInteger | None = ...,
        n_main_bottom_3rd: PositiveInteger | None = ...,
        n_2nd_main_top_1st: PositiveInteger | None = ...,
        n_2nd_main_top_2nd: PositiveInteger | None = ...,
        n_2nd_main_top_3rd: PositiveInteger | None = ...,
        n_2nd_main_bottom_1st: PositiveInteger | None = ...,
        n_2nd_main_bottom_2nd: PositiveInteger | None = ...,
        n_2nd_main_bottom_3rd: PositiveInteger | None = ...,
        n_stirrup: PositiveInteger | None = ...,
        pitch_stirrup: Length | None = ...,
        n_web: PositiveInteger | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarBeamRcStartEndPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarBeamRcStartEndPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarBeamRcStartEndPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarBeamRcStartEndPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_stirrup: str
    """属性(Noneの場合例外)"""
    d_stirrup_or_none: str | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_stirrup: str
    """属性(Noneの場合例外)"""
    strength_stirrup_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_stirrup: PositiveInteger
    """属性(Noneの場合例外)"""
    n_stirrup_or_none: PositiveInteger | None
    """属性"""
    pitch_stirrup: Length
    """属性(Noneの場合例外)"""
    pitch_stirrup_or_none: Length | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""

class StbSecBarBeamXReinforced(StBridgeElement):
    def __init__(
        self,
        *,
        n_main_top: NonNegativeInteger | None = ...,
        n_main_bottom: NonNegativeInteger | None = ...,
    ): ...
    n_main_top: NonNegativeInteger
    """属性(Noneの場合例外) 主筋：上端1段目"""
    n_main_top_or_none: NonNegativeInteger | None
    """属性 主筋：上端1段目"""
    n_main_bottom: NonNegativeInteger
    """属性(Noneの場合例外) 主筋：下端1段目"""
    n_main_bottom_or_none: NonNegativeInteger | None
    """属性 主筋：下端1段目"""

class StbSecBeamS(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_beam: StbSecBeamSKindBeam | str | None = ...,
        is_canti: bool | None = ...,
        is_outin: bool | None = ...,
        stb_sec_steel_figure_beam_s: StbSecSteelFigureBeamS | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_beam(self) -> StbSecBeamSKindBeam:
        """属性(Noneの場合例外) 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）"""
    @kind_beam.setter
    def kind_beam(self, value: StbSecBeamSKindBeam | str) -> None: ...
    @property
    def kind_beam_or_none(self) -> StbSecBeamSKindBeam | None:
        """属性 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）"""
    @kind_beam_or_none.setter
    def kind_beam_or_none(self, value: StbSecBeamSKindBeam | str | None) -> None: ...
    is_canti: bool
    """属性(Noneの場合例外) 片持ち梁か否か"""
    is_canti_or_none: bool | None
    """属性 片持ち梁か否か"""
    is_outin: bool
    """属性(Noneの場合例外) 外端・内端指定"""
    is_outin_or_none: bool | None
    """属性 外端・内端指定"""
    stb_sec_steel_figure_beam_s: StbSecSteelFigureBeamS
    """子要素(Noneの場合例外)"""
    stb_sec_steel_figure_beam_s_or_none: StbSecSteelFigureBeamS | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecBeamSEnsureAccessor: ...

class StbSecSteelFigureBeamS(StBridgeElement):
    def __init__(
        self,
        *,
        joint_id_start: PositiveInteger | None = ...,
        joint_id_end: PositiveInteger | None = ...,
        stb_sec_steel_beam_s_straight: StbSecSteelBeamSStraight | None = ...,
        stb_sec_steel_beam_s_taper: Sequence[StbSecSteelBeamSTaper] = ...,
        stb_sec_steel_beam_s_joint: Sequence[StbSecSteelBeamSJoint] = ...,
        stb_sec_steel_beam_s_haunch: Sequence[StbSecSteelBeamSHaunch] = ...,
        stb_sec_steel_beam_s_five_types: Sequence[StbSecSteelBeamSFiveTypes] = ...,
    ): ...
    joint_id_start: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_start_or_none: PositiveInteger | None
    """属性"""
    joint_id_end: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_end_or_none: PositiveInteger | None
    """属性"""
    stb_sec_steel_beam_s_straight: StbSecSteelBeamSStraight
    """子要素(Noneの場合例外)"""
    stb_sec_steel_beam_s_straight_or_none: StbSecSteelBeamSStraight | None
    """子要素"""
    @property
    def stb_sec_steel_beam_s_taper(self) -> list[StbSecSteelBeamSTaper]:
        """stb_sec_steel_beam_s_taper (list[StbSecSteelBeamSTaper]): 子要素"""
    @stb_sec_steel_beam_s_taper.setter
    def stb_sec_steel_beam_s_taper(
        self, value: Sequence[StbSecSteelBeamSTaper]
    ) -> None: ...
    @property
    def stb_sec_steel_beam_s_joint(self) -> list[StbSecSteelBeamSJoint]:
        """stb_sec_steel_beam_s_joint (list[StbSecSteelBeamSJoint]): 子要素"""
    @stb_sec_steel_beam_s_joint.setter
    def stb_sec_steel_beam_s_joint(
        self, value: Sequence[StbSecSteelBeamSJoint]
    ) -> None: ...
    @property
    def stb_sec_steel_beam_s_haunch(self) -> list[StbSecSteelBeamSHaunch]:
        """stb_sec_steel_beam_s_haunch (list[StbSecSteelBeamSHaunch]): 子要素"""
    @stb_sec_steel_beam_s_haunch.setter
    def stb_sec_steel_beam_s_haunch(
        self, value: Sequence[StbSecSteelBeamSHaunch]
    ) -> None: ...
    @property
    def stb_sec_steel_beam_s_five_types(self) -> list[StbSecSteelBeamSFiveTypes]:
        """stb_sec_steel_beam_s_five_types (list[StbSecSteelBeamSFiveTypes]): 子要素"""
    @stb_sec_steel_beam_s_five_types.setter
    def stb_sec_steel_beam_s_five_types(
        self, value: Sequence[StbSecSteelBeamSFiveTypes]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecSteelFigureBeamSEnsureAccessor: ...

class StbSecSteelBeamSStraight(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSTaper(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSTaperPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSTaperPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSTaperPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSTaperPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBeamSTaperPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSJoint(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSJointPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSJointPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSJointPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSJointPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBeamSJointPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSHaunch(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSHaunchPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSHaunchPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSHaunchPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSHaunchPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBeamSHaunchPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSFiveTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSFiveTypesPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSFiveTypesPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSFiveTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSFiveTypesPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBeamSFiveTypesPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecBeamSrc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_beam: StbSecBeamSrcKindBeam | str | None = ...,
        is_foundation: bool | None = ...,
        is_canti: bool | None = ...,
        is_outin: bool | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_beam_src: StbSecFigureBeamSrc | None = ...,
        stb_sec_bar_arrangement_beam_src: StbSecBarArrangementBeamSrc | None = ...,
        stb_sec_steel_figure_beam_src: StbSecSteelFigureBeamSrc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_beam(self) -> StbSecBeamSrcKindBeam:
        """属性(Noneの場合例外) 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）"""
    @kind_beam.setter
    def kind_beam(self, value: StbSecBeamSrcKindBeam | str) -> None: ...
    @property
    def kind_beam_or_none(self) -> StbSecBeamSrcKindBeam | None:
        """属性 梁の種別以下のいずれかGIRDER（大梁）BEAM（小梁）"""
    @kind_beam_or_none.setter
    def kind_beam_or_none(self, value: StbSecBeamSrcKindBeam | str | None) -> None: ...
    is_foundation: bool
    """属性(Noneの場合例外) 基礎梁か否か"""
    is_foundation_or_none: bool | None
    """属性 基礎梁か否か"""
    is_canti: bool
    """属性(Noneの場合例外) 片持ち梁か否か"""
    is_canti_or_none: bool | None
    """属性 片持ち梁か否か"""
    is_outin: bool
    """属性(Noneの場合例外) 外端・内端指定"""
    is_outin_or_none: bool | None
    """属性 外端・内端指定"""
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_beam_src: StbSecFigureBeamSrc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_beam_src_or_none: StbSecFigureBeamSrc | None
    """子要素"""
    stb_sec_bar_arrangement_beam_src: StbSecBarArrangementBeamSrc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_beam_src_or_none: StbSecBarArrangementBeamSrc | None
    """子要素"""
    stb_sec_steel_figure_beam_src: StbSecSteelFigureBeamSrc
    """子要素(Noneの場合例外)"""
    stb_sec_steel_figure_beam_src_or_none: StbSecSteelFigureBeamSrc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecBeamSrcEnsureAccessor: ...

class StbSecFigureBeamSrc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_beam_src_straight: StbSecBeamSrcStraight | None = ...,
        stb_sec_beam_src_taper: Sequence[StbSecBeamSrcTaper] = ...,
        stb_sec_beam_src_haunch: Sequence[StbSecBeamSrcHaunch] = ...,
    ): ...
    stb_sec_beam_src_straight: StbSecBeamSrcStraight
    """子要素(Noneの場合例外)"""
    stb_sec_beam_src_straight_or_none: StbSecBeamSrcStraight | None
    """子要素"""
    @property
    def stb_sec_beam_src_taper(self) -> list[StbSecBeamSrcTaper]:
        """stb_sec_beam_src_taper (list[StbSecBeamSrcTaper]): 子要素"""
    @stb_sec_beam_src_taper.setter
    def stb_sec_beam_src_taper(self, value: Sequence[StbSecBeamSrcTaper]) -> None: ...
    @property
    def stb_sec_beam_src_haunch(self) -> list[StbSecBeamSrcHaunch]:
        """stb_sec_beam_src_haunch (list[StbSecBeamSrcHaunch]): 子要素"""
    @stb_sec_beam_src_haunch.setter
    def stb_sec_beam_src_haunch(self, value: Sequence[StbSecBeamSrcHaunch]) -> None: ...
    @property
    def ensure(self) -> _StbSecFigureBeamSrcEnsureAccessor: ...

class StbSecBeamSrcStraight(StBridgeElement):
    def __init__(self, *, width: Length | None = ..., depth: Length | None = ...): ...
    width: Length
    """属性(Noneの場合例外)"""
    width_or_none: Length | None
    """属性"""
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBeamSrcTaper(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBeamSrcTaperPos | str | None = ...,
        width: Length | None = ...,
        depth: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBeamSrcTaperPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBeamSrcTaperPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBeamSrcTaperPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBeamSrcTaperPos | str | None) -> None: ...
    width: Length
    """属性(Noneの場合例外)"""
    width_or_none: Length | None
    """属性"""
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBeamSrcHaunch(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBeamSrcHaunchPos | str | None = ...,
        width: Length | None = ...,
        depth: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBeamSrcHaunchPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBeamSrcHaunchPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBeamSrcHaunchPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBeamSrcHaunchPos | str | None) -> None: ...
    width: Length
    """属性(Noneの場合例外)"""
    width_or_none: Length | None
    """属性"""
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBarArrangementBeamSrc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_left: Length | None = ...,
        depth_cover_right: Length | None = ...,
        depth_cover_top: Length | None = ...,
        depth_cover_bottom: Length | None = ...,
        interval: Length | None = ...,
        center_top: Length | None = ...,
        center_bottom: Length | None = ...,
        center_side: Length | None = ...,
        center_interval: Length | None = ...,
        bar_length_start: Length | None = ...,
        bar_length_end: Length | None = ...,
        stb_sec_bar_beam_src_same: StbSecBarBeamSrcSame | None = ...,
        stb_sec_bar_beam_src_three_types: Sequence[StbSecBarBeamSrcThreeTypes] = ...,
        stb_sec_bar_beam_src_start_end: Sequence[StbSecBarBeamSrcStartEnd] = ...,
    ): ...
    depth_cover_left: Length
    """属性(Noneの場合例外)"""
    depth_cover_left_or_none: Length | None
    """属性"""
    depth_cover_right: Length
    """属性(Noneの場合例外)"""
    depth_cover_right_or_none: Length | None
    """属性"""
    depth_cover_top: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_or_none: Length | None
    """属性"""
    depth_cover_bottom: Length
    """属性(Noneの場合例外)"""
    depth_cover_bottom_or_none: Length | None
    """属性"""
    interval: Length
    """属性(Noneの場合例外)"""
    interval_or_none: Length | None
    """属性"""
    center_top: Length
    """属性(Noneの場合例外)"""
    center_top_or_none: Length | None
    """属性"""
    center_bottom: Length
    """属性(Noneの場合例外)"""
    center_bottom_or_none: Length | None
    """属性"""
    center_side: Length
    """属性(Noneの場合例外)"""
    center_side_or_none: Length | None
    """属性"""
    center_interval: Length
    """属性(Noneの場合例外)"""
    center_interval_or_none: Length | None
    """属性"""
    bar_length_start: Length
    """属性(Noneの場合例外)"""
    bar_length_start_or_none: Length | None
    """属性"""
    bar_length_end: Length
    """属性(Noneの場合例外)"""
    bar_length_end_or_none: Length | None
    """属性"""
    stb_sec_bar_beam_src_same: StbSecBarBeamSrcSame
    """子要素(Noneの場合例外)"""
    stb_sec_bar_beam_src_same_or_none: StbSecBarBeamSrcSame | None
    """子要素"""
    @property
    def stb_sec_bar_beam_src_three_types(self) -> list[StbSecBarBeamSrcThreeTypes]:
        """stb_sec_bar_beam_src_three_types (list[StbSecBarBeamSrcThreeTypes]): 子要素"""
    @stb_sec_bar_beam_src_three_types.setter
    def stb_sec_bar_beam_src_three_types(
        self, value: Sequence[StbSecBarBeamSrcThreeTypes]
    ) -> None: ...
    @property
    def stb_sec_bar_beam_src_start_end(self) -> list[StbSecBarBeamSrcStartEnd]:
        """stb_sec_bar_beam_src_start_end (list[StbSecBarBeamSrcStartEnd]): 子要素"""
    @stb_sec_bar_beam_src_start_end.setter
    def stb_sec_bar_beam_src_start_end(
        self, value: Sequence[StbSecBarBeamSrcStartEnd]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecBarArrangementBeamSrcEnsureAccessor: ...

class StbSecBarBeamSrcSame(StBridgeElement):
    def __init__(
        self,
        *,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_stirrup: str | None = ...,
        d_web: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_stirrup: str | None = ...,
        strength_web: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_top_1st: PositiveInteger | None = ...,
        n_main_top_2nd: PositiveInteger | None = ...,
        n_main_top_3rd: PositiveInteger | None = ...,
        n_main_bottom_1st: PositiveInteger | None = ...,
        n_main_bottom_2nd: PositiveInteger | None = ...,
        n_main_bottom_3rd: PositiveInteger | None = ...,
        n_2nd_main_top_1st: PositiveInteger | None = ...,
        n_2nd_main_top_2nd: PositiveInteger | None = ...,
        n_2nd_main_top_3rd: PositiveInteger | None = ...,
        n_2nd_main_bottom_1st: PositiveInteger | None = ...,
        n_2nd_main_bottom_2nd: PositiveInteger | None = ...,
        n_2nd_main_bottom_3rd: PositiveInteger | None = ...,
        n_stirrup: PositiveInteger | None = ...,
        pitch_stirrup: Length | None = ...,
        n_web: PositiveInteger | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
    ): ...
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_stirrup: str
    """属性(Noneの場合例外)"""
    d_stirrup_or_none: str | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_stirrup: str
    """属性(Noneの場合例外)"""
    strength_stirrup_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_stirrup: PositiveInteger
    """属性(Noneの場合例外)"""
    n_stirrup_or_none: PositiveInteger | None
    """属性"""
    pitch_stirrup: Length
    """属性(Noneの場合例外)"""
    pitch_stirrup_or_none: Length | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""

class StbSecBarBeamSrcThreeTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarBeamSrcThreeTypesPos | str | None = ...,
        pos_name: str | None = ...,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_stirrup: str | None = ...,
        d_web: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_stirrup: str | None = ...,
        strength_web: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_top_1st: PositiveInteger | None = ...,
        n_main_top_2nd: PositiveInteger | None = ...,
        n_main_top_3rd: PositiveInteger | None = ...,
        n_main_bottom_1st: PositiveInteger | None = ...,
        n_main_bottom_2nd: PositiveInteger | None = ...,
        n_main_bottom_3rd: PositiveInteger | None = ...,
        n_2nd_main_top_1st: PositiveInteger | None = ...,
        n_2nd_main_top_2nd: PositiveInteger | None = ...,
        n_2nd_main_top_3rd: PositiveInteger | None = ...,
        n_2nd_main_bottom_1st: PositiveInteger | None = ...,
        n_2nd_main_bottom_2nd: PositiveInteger | None = ...,
        n_2nd_main_bottom_3rd: PositiveInteger | None = ...,
        n_stirrup: PositiveInteger | None = ...,
        pitch_stirrup: Length | None = ...,
        n_web: PositiveInteger | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarBeamSrcThreeTypesPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarBeamSrcThreeTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarBeamSrcThreeTypesPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarBeamSrcThreeTypesPos | str | None
    ) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_stirrup: str
    """属性(Noneの場合例外)"""
    d_stirrup_or_none: str | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_stirrup: str
    """属性(Noneの場合例外)"""
    strength_stirrup_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_stirrup: PositiveInteger
    """属性(Noneの場合例外)"""
    n_stirrup_or_none: PositiveInteger | None
    """属性"""
    pitch_stirrup: Length
    """属性(Noneの場合例外)"""
    pitch_stirrup_or_none: Length | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""

class StbSecBarBeamSrcStartEnd(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarBeamSrcStartEndPos | str | None = ...,
        pos_name: str | None = ...,
        d_main: str | None = ...,
        d_2nd_main: str | None = ...,
        d_stirrup: str | None = ...,
        d_web: str | None = ...,
        d_bar_spacing: str | None = ...,
        strength_main: str | None = ...,
        strength_2nd_main: str | None = ...,
        strength_stirrup: str | None = ...,
        strength_web: str | None = ...,
        strength_bar_spacing: str | None = ...,
        n_main_top_1st: PositiveInteger | None = ...,
        n_main_top_2nd: PositiveInteger | None = ...,
        n_main_top_3rd: PositiveInteger | None = ...,
        n_main_bottom_1st: PositiveInteger | None = ...,
        n_main_bottom_2nd: PositiveInteger | None = ...,
        n_main_bottom_3rd: PositiveInteger | None = ...,
        n_2nd_main_top_1st: PositiveInteger | None = ...,
        n_2nd_main_top_2nd: PositiveInteger | None = ...,
        n_2nd_main_top_3rd: PositiveInteger | None = ...,
        n_2nd_main_bottom_1st: PositiveInteger | None = ...,
        n_2nd_main_bottom_2nd: PositiveInteger | None = ...,
        n_2nd_main_bottom_3rd: PositiveInteger | None = ...,
        n_stirrup: PositiveInteger | None = ...,
        pitch_stirrup: Length | None = ...,
        n_web: PositiveInteger | None = ...,
        n_bar_spacing: PositiveInteger | None = ...,
        pitch_bar_spacing: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarBeamSrcStartEndPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarBeamSrcStartEndPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarBeamSrcStartEndPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarBeamSrcStartEndPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    d_main: str
    """属性(Noneの場合例外)"""
    d_main_or_none: str | None
    """属性"""
    d_2nd_main: str
    """属性(Noneの場合例外)"""
    d_2nd_main_or_none: str | None
    """属性"""
    d_stirrup: str
    """属性(Noneの場合例外)"""
    d_stirrup_or_none: str | None
    """属性"""
    d_web: str
    """属性(Noneの場合例外)"""
    d_web_or_none: str | None
    """属性"""
    d_bar_spacing: str
    """属性(Noneの場合例外)"""
    d_bar_spacing_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_2nd_main: str
    """属性(Noneの場合例外)"""
    strength_2nd_main_or_none: str | None
    """属性"""
    strength_stirrup: str
    """属性(Noneの場合例外)"""
    strength_stirrup_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""
    strength_bar_spacing: str
    """属性(Noneの場合例外)"""
    strength_bar_spacing_or_none: str | None
    """属性"""
    n_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_top_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_top_3rd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_1st_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_2nd_or_none: PositiveInteger | None
    """属性"""
    n_2nd_main_bottom_3rd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_2nd_main_bottom_3rd_or_none: PositiveInteger | None
    """属性"""
    n_stirrup: PositiveInteger
    """属性(Noneの場合例外)"""
    n_stirrup_or_none: PositiveInteger | None
    """属性"""
    pitch_stirrup: Length
    """属性(Noneの場合例外)"""
    pitch_stirrup_or_none: Length | None
    """属性"""
    n_web: PositiveInteger
    """属性(Noneの場合例外)"""
    n_web_or_none: PositiveInteger | None
    """属性"""
    n_bar_spacing: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_spacing_or_none: PositiveInteger | None
    """属性"""
    pitch_bar_spacing: Length
    """属性(Noneの場合例外)"""
    pitch_bar_spacing_or_none: Length | None
    """属性"""

class StbSecSteelFigureBeamSrc(StBridgeElement):
    def __init__(
        self,
        *,
        offset: float | None = ...,
        level: float | None = ...,
        joint_id_start: PositiveInteger | None = ...,
        joint_id_end: PositiveInteger | None = ...,
        stb_sec_steel_beam_src_straight: StbSecSteelBeamSrcStraight | None = ...,
        stb_sec_steel_beam_src_taper: Sequence[StbSecSteelBeamSrcTaper] = ...,
        stb_sec_steel_beam_src_joint: Sequence[StbSecSteelBeamSrcJoint] = ...,
        stb_sec_steel_beam_src_haunch: Sequence[StbSecSteelBeamSrcHaunch] = ...,
        stb_sec_steel_beam_src_five_types: Sequence[StbSecSteelBeamSrcFiveTypes] = ...,
    ): ...
    offset: float
    """属性(Noneの場合例外)"""
    offset_or_none: float | None
    """属性"""
    level: float
    """属性(Noneの場合例外)"""
    level_or_none: float | None
    """属性"""
    joint_id_start: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_start_or_none: PositiveInteger | None
    """属性"""
    joint_id_end: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_end_or_none: PositiveInteger | None
    """属性"""
    stb_sec_steel_beam_src_straight: StbSecSteelBeamSrcStraight
    """子要素(Noneの場合例外)"""
    stb_sec_steel_beam_src_straight_or_none: StbSecSteelBeamSrcStraight | None
    """子要素"""
    @property
    def stb_sec_steel_beam_src_taper(self) -> list[StbSecSteelBeamSrcTaper]:
        """stb_sec_steel_beam_src_taper (list[StbSecSteelBeamSrcTaper]): 子要素"""
    @stb_sec_steel_beam_src_taper.setter
    def stb_sec_steel_beam_src_taper(
        self, value: Sequence[StbSecSteelBeamSrcTaper]
    ) -> None: ...
    @property
    def stb_sec_steel_beam_src_joint(self) -> list[StbSecSteelBeamSrcJoint]:
        """stb_sec_steel_beam_src_joint (list[StbSecSteelBeamSrcJoint]): 子要素"""
    @stb_sec_steel_beam_src_joint.setter
    def stb_sec_steel_beam_src_joint(
        self, value: Sequence[StbSecSteelBeamSrcJoint]
    ) -> None: ...
    @property
    def stb_sec_steel_beam_src_haunch(self) -> list[StbSecSteelBeamSrcHaunch]:
        """stb_sec_steel_beam_src_haunch (list[StbSecSteelBeamSrcHaunch]): 子要素"""
    @stb_sec_steel_beam_src_haunch.setter
    def stb_sec_steel_beam_src_haunch(
        self, value: Sequence[StbSecSteelBeamSrcHaunch]
    ) -> None: ...
    @property
    def stb_sec_steel_beam_src_five_types(self) -> list[StbSecSteelBeamSrcFiveTypes]:
        """stb_sec_steel_beam_src_five_types (list[StbSecSteelBeamSrcFiveTypes]): 子要素"""
    @stb_sec_steel_beam_src_five_types.setter
    def stb_sec_steel_beam_src_five_types(
        self, value: Sequence[StbSecSteelBeamSrcFiveTypes]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecSteelFigureBeamSrcEnsureAccessor: ...

class StbSecSteelBeamSrcStraight(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSrcTaper(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSrcTaperPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSrcTaperPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSrcTaperPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSrcTaperPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBeamSrcTaperPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSrcJoint(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSrcJointPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSrcJointPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSrcJointPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSrcJointPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBeamSrcJointPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSrcHaunch(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSrcHaunchPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSrcHaunchPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSrcHaunchPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSrcHaunchPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBeamSrcHaunchPos | str | None) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecSteelBeamSrcFiveTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBeamSrcFiveTypesPos | str | None = ...,
        pos_name: str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBeamSrcFiveTypesPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSteelBeamSrcFiveTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBeamSrcFiveTypesPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecSteelBeamSrcFiveTypesPos | str | None
    ) -> None: ...
    pos_name: str
    """属性(Noneの場合例外)"""
    pos_name_or_none: str | None
    """属性"""
    shape: str
    """属性(Noneの場合例外)"""
    shape_or_none: str | None
    """属性"""
    strength_main: str
    """属性(Noneの場合例外)"""
    strength_main_or_none: str | None
    """属性"""
    strength_web: str
    """属性(Noneの場合例外)"""
    strength_web_or_none: str | None
    """属性"""

class StbSecBraceS(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        floor: str | None = ...,
        kind_brace: StbSecBraceSKindBrace | str | None = ...,
        stb_sec_steel_figure_brace_s: StbSecSteelFigureBraceS | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    floor: str
    """属性(Noneの場合例外) 所属階"""
    floor_or_none: str | None
    """属性 所属階"""
    @property
    def kind_brace(self) -> StbSecBraceSKindBrace:
        """属性(Noneの場合例外) ブレースの種別以下のいずれかVERTICAL（鉛直ブレース）HORIZONTAL（水平ブレース）"""
    @kind_brace.setter
    def kind_brace(self, value: StbSecBraceSKindBrace | str) -> None: ...
    @property
    def kind_brace_or_none(self) -> StbSecBraceSKindBrace | None:
        """属性 ブレースの種別以下のいずれかVERTICAL（鉛直ブレース）HORIZONTAL（水平ブレース）"""
    @kind_brace_or_none.setter
    def kind_brace_or_none(self, value: StbSecBraceSKindBrace | str | None) -> None: ...
    stb_sec_steel_figure_brace_s: StbSecSteelFigureBraceS
    """子要素(Noneの場合例外)"""
    stb_sec_steel_figure_brace_s_or_none: StbSecSteelFigureBraceS | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecBraceSEnsureAccessor: ...

class StbSecSteelFigureBraceS(StBridgeElement):
    def __init__(
        self,
        *,
        joint_id_start: PositiveInteger | None = ...,
        joint_id_end: PositiveInteger | None = ...,
        stb_sec_steel_brace_s_same: StbSecSteelBraceSSame | None = ...,
        stb_sec_steel_brace_s_not_same: Sequence[StbSecSteelBraceSNotSame] = ...,
        stb_sec_steel_brace_s_three_types: Sequence[StbSecSteelBraceSThreeTypes] = ...,
    ): ...
    joint_id_start: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_start_or_none: PositiveInteger | None
    """属性"""
    joint_id_end: PositiveInteger
    """属性(Noneの場合例外)"""
    joint_id_end_or_none: PositiveInteger | None
    """属性"""
    stb_sec_steel_brace_s_same: StbSecSteelBraceSSame
    """子要素(Noneの場合例外)"""
    stb_sec_steel_brace_s_same_or_none: StbSecSteelBraceSSame | None
    """子要素"""
    @property
    def stb_sec_steel_brace_s_not_same(self) -> list[StbSecSteelBraceSNotSame]:
        """stb_sec_steel_brace_s_not_same (list[StbSecSteelBraceSNotSame]): 子要素"""
    @stb_sec_steel_brace_s_not_same.setter
    def stb_sec_steel_brace_s_not_same(
        self, value: Sequence[StbSecSteelBraceSNotSame]
    ) -> None: ...
    @property
    def stb_sec_steel_brace_s_three_types(self) -> list[StbSecSteelBraceSThreeTypes]:
        """stb_sec_steel_brace_s_three_types (list[StbSecSteelBraceSThreeTypes]): 子要素"""
    @stb_sec_steel_brace_s_three_types.setter
    def stb_sec_steel_brace_s_three_types(
        self, value: Sequence[StbSecSteelBraceSThreeTypes]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecSteelFigureBraceSEnsureAccessor: ...

class StbSecSteelBraceSSame(StBridgeElement):
    def __init__(
        self,
        *,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength_main: str
    """属性(Noneの場合例外) 鉄骨強度（主）"""
    strength_main_or_none: str | None
    """属性 鉄骨強度（主）"""
    strength_web: str
    """属性(Noneの場合例外) 鉄骨強度（ウェブ）"""
    strength_web_or_none: str | None
    """属性 鉄骨強度（ウェブ）"""

class StbSecSteelBraceSNotSame(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBraceSNotSamePos | str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBraceSNotSamePos:
        """属性(Noneの場合例外) 配置位置以下のいずれかBOTTOM（脚部）TOP（頭部）"""
    @pos.setter
    def pos(self, value: StbSecSteelBraceSNotSamePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBraceSNotSamePos | None:
        """属性 配置位置以下のいずれかBOTTOM（脚部）TOP（頭部）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSteelBraceSNotSamePos | str | None) -> None: ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength_main: str
    """属性(Noneの場合例外) 鉄骨強度（主）"""
    strength_main_or_none: str | None
    """属性 鉄骨強度（主）"""
    strength_web: str
    """属性(Noneの場合例外) 鉄骨強度（ウェブ）"""
    strength_web_or_none: str | None
    """属性 鉄骨強度（ウェブ）"""

class StbSecSteelBraceSThreeTypes(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSteelBraceSThreeTypesPos | str | None = ...,
        shape: str | None = ...,
        strength_main: str | None = ...,
        strength_web: str | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSteelBraceSThreeTypesPos:
        """属性(Noneの場合例外) 配置位置以下のいずれかBOTTOM（脚部）CENTER（中央）TOP（頭部）"""
    @pos.setter
    def pos(self, value: StbSecSteelBraceSThreeTypesPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSteelBraceSThreeTypesPos | None:
        """属性 配置位置以下のいずれかBOTTOM（脚部）CENTER（中央）TOP（頭部）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecSteelBraceSThreeTypesPos | str | None
    ) -> None: ...
    shape: str
    """属性(Noneの場合例外) 鉄骨形状"""
    shape_or_none: str | None
    """属性 鉄骨形状"""
    strength_main: str
    """属性(Noneの場合例外) 鉄骨強度（主）"""
    strength_main_or_none: str | None
    """属性 鉄骨強度（主）"""
    strength_web: str
    """属性(Noneの場合例外) 鉄骨強度（ウェブ）"""
    strength_web_or_none: str | None
    """属性 鉄骨強度（ウェブ）"""

class StbSecSlabRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        is_foundation: bool | None = ...,
        is_earthen: bool | None = ...,
        is_canti: bool | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_slab_rc: StbSecFigureSlabRc | None = ...,
        stb_sec_bar_arrangement_slab_rc: StbSecBarArrangementSlabRc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    is_foundation: bool
    """属性(Noneの場合例外) 基礎スラブか否か"""
    is_foundation_or_none: bool | None
    """属性 基礎スラブか否か"""
    is_earthen: bool
    """属性(Noneの場合例外) 土間か否か"""
    is_earthen_or_none: bool | None
    """属性 土間か否か"""
    is_canti: bool
    """属性(Noneの場合例外) 片持ちスラブか否か"""
    is_canti_or_none: bool | None
    """属性 片持ちスラブか否か"""
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_slab_rc: StbSecFigureSlabRc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_slab_rc_or_none: StbSecFigureSlabRc | None
    """子要素"""
    stb_sec_bar_arrangement_slab_rc: StbSecBarArrangementSlabRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_slab_rc_or_none: StbSecBarArrangementSlabRc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecSlabRcEnsureAccessor: ...

class StbSecFigureSlabRc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_slab_rc_straight: StbSecSlabRcStraight | None = ...,
        stb_sec_slab_rc_taper: Sequence[StbSecSlabRcTaper] = ...,
        stb_sec_slab_rc_haunch: Sequence[StbSecSlabRcHaunch] = ...,
    ): ...
    stb_sec_slab_rc_straight: StbSecSlabRcStraight
    """子要素(Noneの場合例外)"""
    stb_sec_slab_rc_straight_or_none: StbSecSlabRcStraight | None
    """子要素"""
    @property
    def stb_sec_slab_rc_taper(self) -> list[StbSecSlabRcTaper]:
        """stb_sec_slab_rc_taper (list[StbSecSlabRcTaper]): 子要素"""
    @stb_sec_slab_rc_taper.setter
    def stb_sec_slab_rc_taper(self, value: Sequence[StbSecSlabRcTaper]) -> None: ...
    @property
    def stb_sec_slab_rc_haunch(self) -> list[StbSecSlabRcHaunch]:
        """stb_sec_slab_rc_haunch (list[StbSecSlabRcHaunch]): 子要素"""
    @stb_sec_slab_rc_haunch.setter
    def stb_sec_slab_rc_haunch(self, value: Sequence[StbSecSlabRcHaunch]) -> None: ...
    @property
    def ensure(self) -> _StbSecFigureSlabRcEnsureAccessor: ...

class StbSecSlabRcStraight(StBridgeElement):
    def __init__(self, *, depth: Length | None = ...): ...
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecSlabRcTaper(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSlabRcTaperPos | str | None = ...,
        depth: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSlabRcTaperPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSlabRcTaperPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSlabRcTaperPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSlabRcTaperPos | str | None) -> None: ...
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecSlabRcHaunch(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecSlabRcHaunchPos | str | None = ...,
        depth: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecSlabRcHaunchPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecSlabRcHaunchPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecSlabRcHaunchPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecSlabRcHaunchPos | str | None) -> None: ...
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBarArrangementSlabRc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_top: Length | None = ...,
        depth_cover_bottom: Length | None = ...,
        stb_sec_bar_slab_rc_standard: Sequence[StbSecBarSlabRcStandard] = ...,
        stb_sec_bar_slab_rc_2_way: Sequence[StbSecBarSlabRc2Way] = ...,
        stb_sec_bar_slab_rc_1_way1: Sequence[StbSecBarSlabRc1Way1] = ...,
        stb_sec_bar_slab_rc_1_way2: Sequence[StbSecBarSlabRc1Way2] = ...,
        stb_sec_bar_slab_rc_open: Sequence[StbSecBarSlabRcOpen] = ...,
    ): ...
    depth_cover_top: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_or_none: Length | None
    """属性"""
    depth_cover_bottom: Length
    """属性(Noneの場合例外)"""
    depth_cover_bottom_or_none: Length | None
    """属性"""
    @property
    def stb_sec_bar_slab_rc_standard(self) -> list[StbSecBarSlabRcStandard]:
        """stb_sec_bar_slab_rc_standard (list[StbSecBarSlabRcStandard]): 子要素"""
    @stb_sec_bar_slab_rc_standard.setter
    def stb_sec_bar_slab_rc_standard(
        self, value: Sequence[StbSecBarSlabRcStandard]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_rc_2_way(self) -> list[StbSecBarSlabRc2Way]:
        """stb_sec_bar_slab_rc_2_way (list[StbSecBarSlabRc2Way]): 子要素"""
    @stb_sec_bar_slab_rc_2_way.setter
    def stb_sec_bar_slab_rc_2_way(
        self, value: Sequence[StbSecBarSlabRc2Way]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_rc_1_way1(self) -> list[StbSecBarSlabRc1Way1]:
        """stb_sec_bar_slab_rc_1_way1 (list[StbSecBarSlabRc1Way1]): 子要素"""
    @stb_sec_bar_slab_rc_1_way1.setter
    def stb_sec_bar_slab_rc_1_way1(
        self, value: Sequence[StbSecBarSlabRc1Way1]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_rc_1_way2(self) -> list[StbSecBarSlabRc1Way2]:
        """stb_sec_bar_slab_rc_1_way2 (list[StbSecBarSlabRc1Way2]): 子要素"""
    @stb_sec_bar_slab_rc_1_way2.setter
    def stb_sec_bar_slab_rc_1_way2(
        self, value: Sequence[StbSecBarSlabRc1Way2]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_rc_open(self) -> list[StbSecBarSlabRcOpen]:
        """stb_sec_bar_slab_rc_open (list[StbSecBarSlabRcOpen]): 子要素"""
    @stb_sec_bar_slab_rc_open.setter
    def stb_sec_bar_slab_rc_open(
        self, value: Sequence[StbSecBarSlabRcOpen]
    ) -> None: ...

class StbSecBarSlabRcStandard(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabRcStandardPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabRcStandardPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabRcStandardPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabRcStandardPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabRcStandardPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabRc2Way(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabRc2WayPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabRc2WayPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabRc2WayPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabRc2WayPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabRc2WayPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabRc1Way1(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabRc1Way1Pos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabRc1Way1Pos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabRc1Way1Pos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabRc1Way1Pos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabRc1Way1Pos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabRc1Way2(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabRc1Way2Pos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabRc1Way2Pos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabRc1Way2Pos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabRc1Way2Pos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabRc1Way2Pos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabRcOpen(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabRcOpenPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
        length: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabRcOpenPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）DIAGONAL_TOP（斜め方向上端）DIAGONAL_BOTTOM（斜め方向下端）"""
    @pos.setter
    def pos(self, value: StbSecBarSlabRcOpenPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabRcOpenPos | None:
        """属性 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）DIAGONAL_TOP（斜め方向上端）DIAGONAL_BOTTOM（斜め方向下端）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabRcOpenPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""
    length: Length
    """属性(Noneの場合例外) 長さ"""
    length_or_none: Length | None
    """属性 長さ"""

class StbSecSlabDeck(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        product_type: StbSecSlabDeckProductType | str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_slab_deck: StbSecFigureSlabDeck | None = ...,
        stb_sec_bar_arrangement_slab_deck: StbSecBarArrangementSlabDeck | None = ...,
        stb_sec_product_slab_deck: StbSecProductSlabDeck | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    @property
    def product_type(self) -> StbSecSlabDeckProductType:
        """属性(Noneの場合例外)"""
    @product_type.setter
    def product_type(self, value: StbSecSlabDeckProductType | str) -> None: ...
    @property
    def product_type_or_none(self) -> StbSecSlabDeckProductType | None:
        """属性"""
    @product_type_or_none.setter
    def product_type_or_none(
        self, value: StbSecSlabDeckProductType | str | None
    ) -> None: ...
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_slab_deck: StbSecFigureSlabDeck
    """子要素(Noneの場合例外)"""
    stb_sec_figure_slab_deck_or_none: StbSecFigureSlabDeck | None
    """子要素"""
    stb_sec_bar_arrangement_slab_deck: StbSecBarArrangementSlabDeck
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_slab_deck_or_none: StbSecBarArrangementSlabDeck | None
    """子要素"""
    stb_sec_product_slab_deck: StbSecProductSlabDeck
    """子要素(Noneの場合例外)"""
    stb_sec_product_slab_deck_or_none: StbSecProductSlabDeck | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecSlabDeckEnsureAccessor: ...

class StbSecFigureSlabDeck(StBridgeElement):
    def __init__(
        self, *, stb_sec_slab_deck_straight: StbSecSlabDeckStraight | None = ...
    ): ...
    stb_sec_slab_deck_straight: StbSecSlabDeckStraight
    """子要素(Noneの場合例外)"""
    stb_sec_slab_deck_straight_or_none: StbSecSlabDeckStraight | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigureSlabDeckEnsureAccessor: ...

class StbSecSlabDeckStraight(StBridgeElement):
    def __init__(self, *, depth: Length | None = ...): ...
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecBarArrangementSlabDeck(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_top: Length | None = ...,
        depth_cover_bottom: Length | None = ...,
        stb_sec_bar_slab_deck_standard: Sequence[StbSecBarSlabDeckStandard] = ...,
        stb_sec_bar_slab_deck2_way: Sequence[StbSecBarSlabDeck2Way] = ...,
        stb_sec_bar_slab_deck1_way: Sequence[StbSecBarSlabDeck1Way] = ...,
    ): ...
    depth_cover_top: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_or_none: Length | None
    """属性"""
    depth_cover_bottom: Length
    """属性(Noneの場合例外)"""
    depth_cover_bottom_or_none: Length | None
    """属性"""
    @property
    def stb_sec_bar_slab_deck_standard(self) -> list[StbSecBarSlabDeckStandard]:
        """stb_sec_bar_slab_deck_standard (list[StbSecBarSlabDeckStandard]): 子要素"""
    @stb_sec_bar_slab_deck_standard.setter
    def stb_sec_bar_slab_deck_standard(
        self, value: Sequence[StbSecBarSlabDeckStandard]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_deck2_way(self) -> list[StbSecBarSlabDeck2Way]:
        """stb_sec_bar_slab_deck2_way (list[StbSecBarSlabDeck2Way]): 子要素"""
    @stb_sec_bar_slab_deck2_way.setter
    def stb_sec_bar_slab_deck2_way(
        self, value: Sequence[StbSecBarSlabDeck2Way]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_deck1_way(self) -> list[StbSecBarSlabDeck1Way]:
        """stb_sec_bar_slab_deck1_way (list[StbSecBarSlabDeck1Way]): 子要素"""
    @stb_sec_bar_slab_deck1_way.setter
    def stb_sec_bar_slab_deck1_way(
        self, value: Sequence[StbSecBarSlabDeck1Way]
    ) -> None: ...

class StbSecBarSlabDeckStandard(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabDeckStandardPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabDeckStandardPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabDeckStandardPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabDeckStandardPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabDeckStandardPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabDeck2Way(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabDeck2WayPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabDeck2WayPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabDeck2WayPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabDeck2WayPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabDeck2WayPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabDeck1Way(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabDeck1WayPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabDeck1WayPos:
        """属性(Noneの場合例外) 配筋位置以下のいずれかMAIN_TOP（①主筋方向上端）TRANSVERSE_TOP（②配力筋方向上端）MESH（③溶接金網）"""
    @pos.setter
    def pos(self, value: StbSecBarSlabDeck1WayPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabDeck1WayPos | None:
        """属性 配筋位置以下のいずれかMAIN_TOP（①主筋方向上端）TRANSVERSE_TOP（②配力筋方向上端）MESH（③溶接金網）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabDeck1WayPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecProductSlabDeck(StBridgeElement):
    def __init__(
        self,
        *,
        product_company: str | None = ...,
        product_code: str | None = ...,
        depth_deck: Length | None = ...,
    ): ...
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    depth_deck: Length
    """属性(Noneの場合例外)"""
    depth_deck_or_none: Length | None
    """属性"""

class StbSecSlabPrecast(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        precast_type: StbSecSlabPrecastPrecastType | str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_slab_precast: StbSecFigureSlabPrecast | None = ...,
        stb_sec_bar_arrangement_slab_precast: StbSecBarArrangementSlabPrecast
        | None = ...,
        stb_sec_product_slab_precast: StbSecProductSlabPrecast | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    @property
    def precast_type(self) -> StbSecSlabPrecastPrecastType:
        """属性(Noneの場合例外) 工法種別 以下のいずれかFULL（フルPC工法）HALF（ハーフPC工法）FORM（型枠利用）"""
    @precast_type.setter
    def precast_type(self, value: StbSecSlabPrecastPrecastType | str) -> None: ...
    @property
    def precast_type_or_none(self) -> StbSecSlabPrecastPrecastType | None:
        """属性 工法種別 以下のいずれかFULL（フルPC工法）HALF（ハーフPC工法）FORM（型枠利用）"""
    @precast_type_or_none.setter
    def precast_type_or_none(
        self, value: StbSecSlabPrecastPrecastType | str | None
    ) -> None: ...
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    stb_sec_figure_slab_precast: StbSecFigureSlabPrecast
    """子要素(Noneの場合例外)"""
    stb_sec_figure_slab_precast_or_none: StbSecFigureSlabPrecast | None
    """子要素"""
    stb_sec_bar_arrangement_slab_precast: StbSecBarArrangementSlabPrecast
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_slab_precast_or_none: StbSecBarArrangementSlabPrecast | None
    """子要素"""
    stb_sec_product_slab_precast: StbSecProductSlabPrecast
    """子要素(Noneの場合例外)"""
    stb_sec_product_slab_precast_or_none: StbSecProductSlabPrecast | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecSlabPrecastEnsureAccessor: ...

class StbSecFigureSlabPrecast(StBridgeElement):
    def __init__(
        self, *, stb_sec_slab_precast_straight: StbSecSlabPrecastStraight | None = ...
    ): ...
    stb_sec_slab_precast_straight: StbSecSlabPrecastStraight
    """子要素(Noneの場合例外)"""
    stb_sec_slab_precast_straight_or_none: StbSecSlabPrecastStraight | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigureSlabPrecastEnsureAccessor: ...

class StbSecSlabPrecastStraight(StBridgeElement):
    def __init__(self, *, depth_concrete: Length | None = ...): ...
    depth_concrete: Length
    """属性(Noneの場合例外)"""
    depth_concrete_or_none: Length | None
    """属性"""

class StbSecBarArrangementSlabPrecast(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_top: Length | None = ...,
        stb_sec_bar_slab_precast_standard: Sequence[StbSecBarSlabPrecastStandard] = ...,
        stb_sec_bar_slab_precast2_way: Sequence[StbSecBarSlabPrecast2Way] = ...,
        stb_sec_bar_slab_precast1_way: Sequence[StbSecBarSlabPrecast1Way] = ...,
    ): ...
    depth_cover_top: Length
    """属性(Noneの場合例外) かぶり厚さ（上）"""
    depth_cover_top_or_none: Length | None
    """属性 かぶり厚さ（上）"""
    @property
    def stb_sec_bar_slab_precast_standard(self) -> list[StbSecBarSlabPrecastStandard]:
        """stb_sec_bar_slab_precast_standard (list[StbSecBarSlabPrecastStandard]): 子要素"""
    @stb_sec_bar_slab_precast_standard.setter
    def stb_sec_bar_slab_precast_standard(
        self, value: Sequence[StbSecBarSlabPrecastStandard]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_precast2_way(self) -> list[StbSecBarSlabPrecast2Way]:
        """stb_sec_bar_slab_precast2_way (list[StbSecBarSlabPrecast2Way]): 子要素"""
    @stb_sec_bar_slab_precast2_way.setter
    def stb_sec_bar_slab_precast2_way(
        self, value: Sequence[StbSecBarSlabPrecast2Way]
    ) -> None: ...
    @property
    def stb_sec_bar_slab_precast1_way(self) -> list[StbSecBarSlabPrecast1Way]:
        """stb_sec_bar_slab_precast1_way (list[StbSecBarSlabPrecast1Way]): 子要素"""
    @stb_sec_bar_slab_precast1_way.setter
    def stb_sec_bar_slab_precast1_way(
        self, value: Sequence[StbSecBarSlabPrecast1Way]
    ) -> None: ...

class StbSecBarSlabPrecastStandard(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabPrecastStandardPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabPrecastStandardPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabPrecastStandardPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabPrecastStandardPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarSlabPrecastStandardPos | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabPrecast2Way(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabPrecast2WayPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabPrecast2WayPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabPrecast2WayPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabPrecast2WayPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabPrecast2WayPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarSlabPrecast1Way(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarSlabPrecast1WayPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarSlabPrecast1WayPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarSlabPrecast1WayPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarSlabPrecast1WayPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarSlabPrecast1WayPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecProductSlabPrecast(StBridgeElement):
    def __init__(
        self,
        *,
        product_company: str | None = ...,
        product_name: str | None = ...,
        product_code: str | None = ...,
        depth: Length | None = ...,
    ): ...
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_name: str
    """属性(Noneの場合例外)"""
    product_name_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外) 製品型番"""
    product_code_or_none: str | None
    """属性 製品型番"""
    depth: Length
    """属性(Noneの場合例外)"""
    depth_or_none: Length | None
    """属性"""

class StbSecWallRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_wall_rc: StbSecFigureWallRc | None = ...,
        stb_sec_bar_arrangement_wall_rc: StbSecBarArrangementWallRc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_wall_rc: StbSecFigureWallRc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_wall_rc_or_none: StbSecFigureWallRc | None
    """子要素"""
    stb_sec_bar_arrangement_wall_rc: StbSecBarArrangementWallRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_wall_rc_or_none: StbSecBarArrangementWallRc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecWallRcEnsureAccessor: ...

class StbSecFigureWallRc(StBridgeElement):
    def __init__(
        self, *, stb_sec_wall_rc_straight: StbSecWallRcStraight | None = ...
    ): ...
    stb_sec_wall_rc_straight: StbSecWallRcStraight
    """子要素(Noneの場合例外)"""
    stb_sec_wall_rc_straight_or_none: StbSecWallRcStraight | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigureWallRcEnsureAccessor: ...

class StbSecWallRcStraight(StBridgeElement):
    def __init__(self, *, t: Length | None = ...): ...
    t: Length
    """属性(Noneの場合例外) 厚さ"""
    t_or_none: Length | None
    """属性 厚さ"""

class StbSecBarArrangementWallRc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_outside: Length | None = ...,
        depth_cover_inside: Length | None = ...,
        stb_sec_bar_wall_rc_single: Sequence[StbSecBarWallRcSingle] = ...,
        stb_sec_bar_wall_rc_zigzag: Sequence[StbSecBarWallRcZigzag] = ...,
        stb_sec_bar_wall_rc_double_net: Sequence[StbSecBarWallRcDoubleNet] = ...,
        stb_sec_bar_wall_rc_inside_and_outside: Sequence[
            StbSecBarWallRcInsideAndOutside
        ] = ...,
        stb_sec_bar_wall_rc_edge: Sequence[StbSecBarWallRcEdge] = ...,
        stb_sec_bar_wall_rc_open: Sequence[StbSecBarWallRcOpen] = ...,
    ): ...
    depth_cover_outside: Length
    """属性(Noneの場合例外)"""
    depth_cover_outside_or_none: Length | None
    """属性"""
    depth_cover_inside: Length
    """属性(Noneの場合例外)"""
    depth_cover_inside_or_none: Length | None
    """属性"""
    @property
    def stb_sec_bar_wall_rc_single(self) -> list[StbSecBarWallRcSingle]:
        """stb_sec_bar_wall_rc_single (list[StbSecBarWallRcSingle]): 子要素"""
    @stb_sec_bar_wall_rc_single.setter
    def stb_sec_bar_wall_rc_single(
        self, value: Sequence[StbSecBarWallRcSingle]
    ) -> None: ...
    @property
    def stb_sec_bar_wall_rc_zigzag(self) -> list[StbSecBarWallRcZigzag]:
        """stb_sec_bar_wall_rc_zigzag (list[StbSecBarWallRcZigzag]): 子要素"""
    @stb_sec_bar_wall_rc_zigzag.setter
    def stb_sec_bar_wall_rc_zigzag(
        self, value: Sequence[StbSecBarWallRcZigzag]
    ) -> None: ...
    @property
    def stb_sec_bar_wall_rc_double_net(self) -> list[StbSecBarWallRcDoubleNet]:
        """stb_sec_bar_wall_rc_double_net (list[StbSecBarWallRcDoubleNet]): 子要素"""
    @stb_sec_bar_wall_rc_double_net.setter
    def stb_sec_bar_wall_rc_double_net(
        self, value: Sequence[StbSecBarWallRcDoubleNet]
    ) -> None: ...
    @property
    def stb_sec_bar_wall_rc_inside_and_outside(
        self,
    ) -> list[StbSecBarWallRcInsideAndOutside]:
        """stb_sec_bar_wall_rc_inside_and_outside (list[StbSecBarWallRcInsideAndOutside]): 子要素"""
    @stb_sec_bar_wall_rc_inside_and_outside.setter
    def stb_sec_bar_wall_rc_inside_and_outside(
        self, value: Sequence[StbSecBarWallRcInsideAndOutside]
    ) -> None: ...
    @property
    def stb_sec_bar_wall_rc_edge(self) -> list[StbSecBarWallRcEdge]:
        """stb_sec_bar_wall_rc_edge (list[StbSecBarWallRcEdge]): 子要素"""
    @stb_sec_bar_wall_rc_edge.setter
    def stb_sec_bar_wall_rc_edge(
        self, value: Sequence[StbSecBarWallRcEdge]
    ) -> None: ...
    @property
    def stb_sec_bar_wall_rc_open(self) -> list[StbSecBarWallRcOpen]:
        """stb_sec_bar_wall_rc_open (list[StbSecBarWallRcOpen]): 子要素"""
    @stb_sec_bar_wall_rc_open.setter
    def stb_sec_bar_wall_rc_open(
        self, value: Sequence[StbSecBarWallRcOpen]
    ) -> None: ...

class StbSecBarWallRcSingle(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarWallRcSinglePos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarWallRcSinglePos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos.setter
    def pos(self, value: StbSecBarWallRcSinglePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarWallRcSinglePos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarWallRcSinglePos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecBarWallRcZigzag(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarWallRcZigzagPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarWallRcZigzagPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos.setter
    def pos(self, value: StbSecBarWallRcZigzagPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarWallRcZigzagPos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarWallRcZigzagPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecBarWallRcDoubleNet(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarWallRcDoubleNetPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarWallRcDoubleNetPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos.setter
    def pos(self, value: StbSecBarWallRcDoubleNetPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarWallRcDoubleNetPos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarWallRcDoubleNetPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecBarWallRcInsideAndOutside(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarWallRcInsideAndOutsidePos | str | None = ...,
        pos2: StbSecBarWallRcInsideAndOutsidePos2 | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarWallRcInsideAndOutsidePos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL_OUTSIDE（縦筋外側）VERTICAL_INSIDE（縦筋内側）HORIZONTAL_OUTSIDE（横筋外側）HORIZONTAL_INSIDE（横筋内側）"""
    @pos.setter
    def pos(self, value: StbSecBarWallRcInsideAndOutsidePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarWallRcInsideAndOutsidePos | None:
        """属性 配筋位置 以下のいずれかVERTICAL_OUTSIDE（縦筋外側）VERTICAL_INSIDE（縦筋内側）HORIZONTAL_OUTSIDE（横筋外側）HORIZONTAL_INSIDE（横筋内側）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarWallRcInsideAndOutsidePos | str | None
    ) -> None: ...
    @property
    def pos2(self) -> StbSecBarWallRcInsideAndOutsidePos2:
        """属性(Noneの場合例外) 鉄筋の段位置"""
    @pos2.setter
    def pos2(self, value: StbSecBarWallRcInsideAndOutsidePos2 | str) -> None: ...
    @property
    def pos2_or_none(self) -> StbSecBarWallRcInsideAndOutsidePos2 | None:
        """属性 鉄筋の段位置"""
    @pos2_or_none.setter
    def pos2_or_none(
        self, value: StbSecBarWallRcInsideAndOutsidePos2 | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外)"""
    strength_or_none: str | None
    """属性"""
    d: str
    """属性(Noneの場合例外)"""
    d_or_none: str | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""

class StbSecBarWallRcEdge(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarWallRcEdgePos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarWallRcEdgePos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL_START（袖壁始端）VERTICAL_END（袖壁終端）HORIZONTAL_BOTTOM（たれ壁下端）HORIZONTAL_TOP（腰壁上端）"""
    @pos.setter
    def pos(self, value: StbSecBarWallRcEdgePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarWallRcEdgePos | None:
        """属性 配筋位置 以下のいずれかVERTICAL_START（袖壁始端）VERTICAL_END（袖壁終端）HORIZONTAL_BOTTOM（たれ壁下端）HORIZONTAL_TOP（腰壁上端）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarWallRcEdgePos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外)"""
    n_or_none: PositiveInteger | None
    """属性"""

class StbSecBarWallRcOpen(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarWallRcOpenPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
        length: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarWallRcOpenPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）DIAGONAL（斜め筋）"""
    @pos.setter
    def pos(self, value: StbSecBarWallRcOpenPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarWallRcOpenPos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）DIAGONAL（斜め筋）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarWallRcOpenPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""
    length: Length
    """属性(Noneの場合例外) 長さ"""
    length_or_none: Length | None
    """属性 長さ"""

class StbSecFoundationRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_foundation_rc: StbSecFigureFoundationRc | None = ...,
        stb_sec_bar_arrangement_foundation_rc: StbSecBarArrangementFoundationRc
        | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_foundation_rc: StbSecFigureFoundationRc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_foundation_rc_or_none: StbSecFigureFoundationRc | None
    """子要素"""
    stb_sec_bar_arrangement_foundation_rc: StbSecBarArrangementFoundationRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_foundation_rc_or_none: (
        StbSecBarArrangementFoundationRc | None
    )
    """子要素"""
    @property
    def ensure(self) -> _StbSecFoundationRcEnsureAccessor: ...

class StbSecFigureFoundationRc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_foundation_rc_rect: StbSecFoundationRcRect | None = ...,
        stb_sec_foundation_rc_tapered_rect: StbSecFoundationRcTaperedRect | None = ...,
        stb_sec_foundation_rc_triangle: StbSecFoundationRcTriangle | None = ...,
        stb_sec_foundation_rc_equi_triangle: StbSecFoundationRcEquiTriangle
        | None = ...,
        stb_sec_foundation_rc_octagon: StbSecFoundationRcOctagon | None = ...,
        stb_sec_foundation_rc_continuous: StbSecFoundationRcContinuous | None = ...,
    ): ...
    stb_sec_foundation_rc_rect: StbSecFoundationRcRect
    """子要素(Noneの場合例外)"""
    stb_sec_foundation_rc_rect_or_none: StbSecFoundationRcRect | None
    """子要素"""
    stb_sec_foundation_rc_tapered_rect: StbSecFoundationRcTaperedRect
    """子要素(Noneの場合例外)"""
    stb_sec_foundation_rc_tapered_rect_or_none: StbSecFoundationRcTaperedRect | None
    """子要素"""
    stb_sec_foundation_rc_triangle: StbSecFoundationRcTriangle
    """子要素(Noneの場合例外)"""
    stb_sec_foundation_rc_triangle_or_none: StbSecFoundationRcTriangle | None
    """子要素"""
    stb_sec_foundation_rc_equi_triangle: StbSecFoundationRcEquiTriangle
    """子要素(Noneの場合例外)"""
    stb_sec_foundation_rc_equi_triangle_or_none: StbSecFoundationRcEquiTriangle | None
    """子要素"""
    stb_sec_foundation_rc_octagon: StbSecFoundationRcOctagon
    """子要素(Noneの場合例外)"""
    stb_sec_foundation_rc_octagon_or_none: StbSecFoundationRcOctagon | None
    """子要素"""
    stb_sec_foundation_rc_continuous: StbSecFoundationRcContinuous
    """子要素(Noneの場合例外)"""
    stb_sec_foundation_rc_continuous_or_none: StbSecFoundationRcContinuous | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigureFoundationRcEnsureAccessor: ...

class StbSecFoundationRcRect(StBridgeElement):
    def __init__(
        self,
        *,
        width_x: Length | None = ...,
        width_y: Length | None = ...,
        depth: Length | None = ...,
    ): ...
    width_x: Length
    """属性(Noneの場合例外) Ｘ幅"""
    width_x_or_none: Length | None
    """属性 Ｘ幅"""
    width_y: Length
    """属性(Noneの場合例外) Ｙ幅"""
    width_y_or_none: Length | None
    """属性 Ｙ幅"""
    depth: Length
    """属性(Noneの場合例外) 厚さ"""
    depth_or_none: Length | None
    """属性 厚さ"""

class StbSecFoundationRcTaperedRect(StBridgeElement):
    def __init__(
        self,
        *,
        width_x: Length | None = ...,
        width_y: Length | None = ...,
        depth_base: Length | None = ...,
        depth_tip: Length | None = ...,
    ): ...
    width_x: Length
    """属性(Noneの場合例外) Ｘ幅"""
    width_x_or_none: Length | None
    """属性 Ｘ幅"""
    width_y: Length
    """属性(Noneの場合例外) Ｙ幅"""
    width_y_or_none: Length | None
    """属性 Ｙ幅"""
    depth_base: Length
    """属性(Noneの場合例外) 根元厚さ"""
    depth_base_or_none: Length | None
    """属性 根元厚さ"""
    depth_tip: Length
    """属性(Noneの場合例外) 先端厚さ"""
    depth_tip_or_none: Length | None
    """属性 先端厚さ"""

class StbSecFoundationRcTriangle(StBridgeElement):
    def __init__(
        self,
        *,
        width_x: Length | None = ...,
        width_y: Length | None = ...,
        depth: Length | None = ...,
    ): ...
    width_x: Length
    """属性(Noneの場合例外) Ｘ幅"""
    width_x_or_none: Length | None
    """属性 Ｘ幅"""
    width_y: Length
    """属性(Noneの場合例外) Ｙ幅"""
    width_y_or_none: Length | None
    """属性 Ｙ幅"""
    depth: Length
    """属性(Noneの場合例外) 厚さ"""
    depth_or_none: Length | None
    """属性 厚さ"""

class StbSecFoundationRcEquiTriangle(StBridgeElement):
    def __init__(
        self,
        *,
        width_base: Length | None = ...,
        width_chamfer: Length | None = ...,
        depth: Length | None = ...,
    ): ...
    width_base: Length
    """属性(Noneの場合例外) 底辺幅"""
    width_base_or_none: Length | None
    """属性 底辺幅"""
    width_chamfer: Length
    """属性(Noneの場合例外) 面取り幅"""
    width_chamfer_or_none: Length | None
    """属性 面取り幅"""
    depth: Length
    """属性(Noneの場合例外) 厚さ"""
    depth_or_none: Length | None
    """属性 厚さ"""

class StbSecFoundationRcOctagon(StBridgeElement):
    def __init__(
        self,
        *,
        width_x: Length | None = ...,
        width_y: Length | None = ...,
        width_chamfer1_x: NonNegativeLength | None = ...,
        width_chamfer1_y: NonNegativeLength | None = ...,
        width_chamfer2_x: NonNegativeLength | None = ...,
        width_chamfer2_y: NonNegativeLength | None = ...,
        width_chamfer3_x: NonNegativeLength | None = ...,
        width_chamfer3_y: NonNegativeLength | None = ...,
        width_chamfer4_x: NonNegativeLength | None = ...,
        width_chamfer4_y: NonNegativeLength | None = ...,
        depth: Length | None = ...,
    ): ...
    width_x: Length
    """属性(Noneの場合例外) X幅"""
    width_x_or_none: Length | None
    """属性 X幅"""
    width_y: Length
    """属性(Noneの場合例外) Y幅"""
    width_y_or_none: Length | None
    """属性 Y幅"""
    width_chamfer1_x: NonNegativeLength
    """属性(Noneの場合例外) 面取りX幅(1)"""
    width_chamfer1_x_or_none: NonNegativeLength | None
    """属性 面取りX幅(1)"""
    width_chamfer1_y: NonNegativeLength
    """属性(Noneの場合例外) 面取りY幅(1)"""
    width_chamfer1_y_or_none: NonNegativeLength | None
    """属性 面取りY幅(1)"""
    width_chamfer2_x: NonNegativeLength
    """属性(Noneの場合例外) 面取りX幅(2)"""
    width_chamfer2_x_or_none: NonNegativeLength | None
    """属性 面取りX幅(2)"""
    width_chamfer2_y: NonNegativeLength
    """属性(Noneの場合例外) 面取りY幅(2)"""
    width_chamfer2_y_or_none: NonNegativeLength | None
    """属性 面取りY幅(2)"""
    width_chamfer3_x: NonNegativeLength
    """属性(Noneの場合例外) 面取りX幅(3)"""
    width_chamfer3_x_or_none: NonNegativeLength | None
    """属性 面取りX幅(3)"""
    width_chamfer3_y: NonNegativeLength
    """属性(Noneの場合例外) 面取りY幅(3)"""
    width_chamfer3_y_or_none: NonNegativeLength | None
    """属性 面取りY幅(3)"""
    width_chamfer4_x: NonNegativeLength
    """属性(Noneの場合例外) 面取りX幅(4)"""
    width_chamfer4_x_or_none: NonNegativeLength | None
    """属性 面取りX幅(4)"""
    width_chamfer4_y: NonNegativeLength
    """属性(Noneの場合例外) 面取りY幅(4)"""
    width_chamfer4_y_or_none: NonNegativeLength | None
    """属性 面取りY幅(4)"""
    depth: Length
    """属性(Noneの場合例外) 厚さ"""
    depth_or_none: Length | None
    """属性 厚さ"""

class StbSecFoundationRcContinuous(StBridgeElement):
    def __init__(
        self,
        *,
        width: Length | None = ...,
        depth_base: Length | None = ...,
        depth_tip: Length | None = ...,
        type: StbSecFoundationRcContinuousType | str | None = ...,
    ): ...
    width: Length
    """属性(Noneの場合例外) 幅"""
    width_or_none: Length | None
    """属性 幅"""
    depth_base: Length
    """属性(Noneの場合例外) 根元厚さ"""
    depth_base_or_none: Length | None
    """属性 根元厚さ"""
    depth_tip: Length
    """属性(Noneの場合例外) 先端厚さ"""
    depth_tip_or_none: Length | None
    """属性 先端厚さ"""
    @property
    def type(self) -> StbSecFoundationRcContinuousType:
        """属性(Noneの場合例外) タイプ 以下のいずれかRIGHT_LLEFT_LREVERSE_T"""
    @type.setter
    def type(self, value: StbSecFoundationRcContinuousType | str) -> None: ...
    @property
    def type_or_none(self) -> StbSecFoundationRcContinuousType | None:
        """属性 タイプ 以下のいずれかRIGHT_LLEFT_LREVERSE_T"""
    @type_or_none.setter
    def type_or_none(
        self, value: StbSecFoundationRcContinuousType | str | None
    ) -> None: ...

class StbSecBarArrangementFoundationRc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_top: Length | None = ...,
        depth_cover_bottom: Length | None = ...,
        depth_cover_side: Length | None = ...,
        stb_sec_bar_foundation_rc_rect: Sequence[StbSecBarFoundationRcRect] = ...,
        stb_sec_bar_foundation_rc_triangle: Sequence[
            StbSecBarFoundationRcTriangle
        ] = ...,
        stb_sec_bar_foundation_rc_three_way: Sequence[
            StbSecBarFoundationRcThreeWay
        ] = ...,
        stb_sec_bar_foundation_rc_continuous: Sequence[
            StbSecBarFoundationRcContinuous
        ] = ...,
    ): ...
    depth_cover_top: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_or_none: Length | None
    """属性"""
    depth_cover_bottom: Length
    """属性(Noneの場合例外)"""
    depth_cover_bottom_or_none: Length | None
    """属性"""
    depth_cover_side: Length
    """属性(Noneの場合例外)"""
    depth_cover_side_or_none: Length | None
    """属性"""
    @property
    def stb_sec_bar_foundation_rc_rect(self) -> list[StbSecBarFoundationRcRect]:
        """stb_sec_bar_foundation_rc_rect (list[StbSecBarFoundationRcRect]): 子要素"""
    @stb_sec_bar_foundation_rc_rect.setter
    def stb_sec_bar_foundation_rc_rect(
        self, value: Sequence[StbSecBarFoundationRcRect]
    ) -> None: ...
    @property
    def stb_sec_bar_foundation_rc_triangle(self) -> list[StbSecBarFoundationRcTriangle]:
        """stb_sec_bar_foundation_rc_triangle (list[StbSecBarFoundationRcTriangle]): 子要素"""
    @stb_sec_bar_foundation_rc_triangle.setter
    def stb_sec_bar_foundation_rc_triangle(
        self, value: Sequence[StbSecBarFoundationRcTriangle]
    ) -> None: ...
    @property
    def stb_sec_bar_foundation_rc_three_way(
        self,
    ) -> list[StbSecBarFoundationRcThreeWay]:
        """stb_sec_bar_foundation_rc_three_way (list[StbSecBarFoundationRcThreeWay]): 子要素"""
    @stb_sec_bar_foundation_rc_three_way.setter
    def stb_sec_bar_foundation_rc_three_way(
        self, value: Sequence[StbSecBarFoundationRcThreeWay]
    ) -> None: ...
    @property
    def stb_sec_bar_foundation_rc_continuous(
        self,
    ) -> list[StbSecBarFoundationRcContinuous]:
        """stb_sec_bar_foundation_rc_continuous (list[StbSecBarFoundationRcContinuous]): 子要素"""
    @stb_sec_bar_foundation_rc_continuous.setter
    def stb_sec_bar_foundation_rc_continuous(
        self, value: Sequence[StbSecBarFoundationRcContinuous]
    ) -> None: ...

class StbSecBarFoundationRcRect(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarFoundationRcRectPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarFoundationRcRectPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）HORIZONTAL（横）"""
    @pos.setter
    def pos(self, value: StbSecBarFoundationRcRectPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarFoundationRcRectPos | None:
        """属性 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）HORIZONTAL（横）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarFoundationRcRectPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""

class StbSecBarFoundationRcTriangle(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarFoundationRcTrianglePos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarFoundationRcTrianglePos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）TRANSVERSE_TOP（配力筋方向上端）TRANSVERSE_BOTTOM（配力筋方向下端）HORIZONTAL（横）"""
    @pos.setter
    def pos(self, value: StbSecBarFoundationRcTrianglePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarFoundationRcTrianglePos | None:
        """属性 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）TRANSVERSE_TOP（配力筋方向上端）TRANSVERSE_BOTTOM（配力筋方向下端）HORIZONTAL（横）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarFoundationRcTrianglePos | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""

class StbSecBarFoundationRcThreeWay(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarFoundationRcThreeWayPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarFoundationRcThreeWayPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）OUTSIDE_TOP（外周上端）OUTSIDE_BOTTOM（外周下端）HORIZONTAL（横）"""
    @pos.setter
    def pos(self, value: StbSecBarFoundationRcThreeWayPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarFoundationRcThreeWayPos | None:
        """属性 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）OUTSIDE_TOP（外周上端）OUTSIDE_BOTTOM（外周下端）HORIZONTAL（横）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarFoundationRcThreeWayPos | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""

class StbSecBarFoundationRcContinuous(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarFoundationRcContinuousPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarFoundationRcContinuousPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかMAIN_BASE_TOP（主筋方向元端上端筋）MAIN_BASE_BOTTOM（主筋方向元端下端筋）MAIN_TIP_TOP（主筋方向先端上端筋）MAIN_TIP_BOTTOM（主筋方向先端下端筋）TRANSVERSE_TOP（配力筋方向上端筋）TRANSVERSE_BOTTOM（配力筋方向下端筋）HORIZONTAL（横筋）"""
    @pos.setter
    def pos(self, value: StbSecBarFoundationRcContinuousPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarFoundationRcContinuousPos | None:
        """属性 配筋位置 以下のいずれかMAIN_BASE_TOP（主筋方向元端上端筋）MAIN_BASE_BOTTOM（主筋方向元端下端筋）MAIN_TIP_TOP（主筋方向先端上端筋）MAIN_TIP_BOTTOM（主筋方向先端下端筋）TRANSVERSE_TOP（配力筋方向上端筋）TRANSVERSE_BOTTOM（配力筋方向下端筋）HORIZONTAL（横筋）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarFoundationRcContinuousPos | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecPileRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_pile_rc: StbSecFigurePileRc | None = ...,
        stb_sec_bar_arrangement_pile_rc: StbSecBarArrangementPileRc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    stb_sec_figure_pile_rc: StbSecFigurePileRc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_pile_rc_or_none: StbSecFigurePileRc | None
    """子要素"""
    stb_sec_bar_arrangement_pile_rc: StbSecBarArrangementPileRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_pile_rc_or_none: StbSecBarArrangementPileRc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecPileRcEnsureAccessor: ...

class StbSecFigurePileRc(StBridgeElement):
    def __init__(
        self,
        *,
        length_pipe: Length | None = ...,
        t_pipe: Length | None = ...,
        strength_pipe: str | None = ...,
        stb_sec_pile_rc_straight: StbSecPileRcStraight | None = ...,
        stb_sec_pile_rc_extended_foot: StbSecPileRcExtendedFoot | None = ...,
        stb_sec_pile_rc_extended_top: StbSecPileRcExtendedTop | None = ...,
        stb_sec_pile_rc_extended_top_foot: StbSecPileRcExtendedTopFoot | None = ...,
    ): ...
    length_pipe: Length
    """属性(Noneの場合例外)"""
    length_pipe_or_none: Length | None
    """属性"""
    t_pipe: Length
    """属性(Noneの場合例外)"""
    t_pipe_or_none: Length | None
    """属性"""
    strength_pipe: str
    """属性(Noneの場合例外)"""
    strength_pipe_or_none: str | None
    """属性"""
    stb_sec_pile_rc_straight: StbSecPileRcStraight
    """子要素(Noneの場合例外)"""
    stb_sec_pile_rc_straight_or_none: StbSecPileRcStraight | None
    """子要素"""
    stb_sec_pile_rc_extended_foot: StbSecPileRcExtendedFoot
    """子要素(Noneの場合例外)"""
    stb_sec_pile_rc_extended_foot_or_none: StbSecPileRcExtendedFoot | None
    """子要素"""
    stb_sec_pile_rc_extended_top: StbSecPileRcExtendedTop
    """子要素(Noneの場合例外)"""
    stb_sec_pile_rc_extended_top_or_none: StbSecPileRcExtendedTop | None
    """子要素"""
    stb_sec_pile_rc_extended_top_foot: StbSecPileRcExtendedTopFoot
    """子要素(Noneの場合例外)"""
    stb_sec_pile_rc_extended_top_foot_or_none: StbSecPileRcExtendedTopFoot | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigurePileRcEnsureAccessor: ...

class StbSecPileRcStraight(StBridgeElement):
    def __init__(self, *, d: Length | None = ...): ...
    d: Length
    """属性(Noneの場合例外)"""
    d_or_none: Length | None
    """属性"""

class StbSecPileRcExtendedFoot(StBridgeElement):
    def __init__(
        self,
        *,
        d_axial: Length | None = ...,
        d_extended_foot: Length | None = ...,
        length_extended_foot: Length | None = ...,
        angle_extended_foot_taper: Angle | None = ...,
    ): ...
    d_axial: Length
    """属性(Noneの場合例外)"""
    d_axial_or_none: Length | None
    """属性"""
    d_extended_foot: Length
    """属性(Noneの場合例外)"""
    d_extended_foot_or_none: Length | None
    """属性"""
    length_extended_foot: Length
    """属性(Noneの場合例外)"""
    length_extended_foot_or_none: Length | None
    """属性"""
    angle_extended_foot_taper: Angle
    """属性(Noneの場合例外)"""
    angle_extended_foot_taper_or_none: Angle | None
    """属性"""

class StbSecPileRcExtendedTop(StBridgeElement):
    def __init__(
        self,
        *,
        d_extended_top: Length | None = ...,
        d_axial: Length | None = ...,
        angle_extended_top_taper: Angle | None = ...,
    ): ...
    d_extended_top: Length
    """属性(Noneの場合例外)"""
    d_extended_top_or_none: Length | None
    """属性"""
    d_axial: Length
    """属性(Noneの場合例外)"""
    d_axial_or_none: Length | None
    """属性"""
    angle_extended_top_taper: Angle
    """属性(Noneの場合例外)"""
    angle_extended_top_taper_or_none: Angle | None
    """属性"""

class StbSecPileRcExtendedTopFoot(StBridgeElement):
    def __init__(
        self,
        *,
        d_extended_top: Length | None = ...,
        d_axial: Length | None = ...,
        d_extended_foot: Length | None = ...,
        angle_extended_top_taper: Angle | None = ...,
        length_extended_foot: Length | None = ...,
        angle_extended_foot_taper: Angle | None = ...,
    ): ...
    d_extended_top: Length
    """属性(Noneの場合例外)"""
    d_extended_top_or_none: Length | None
    """属性"""
    d_axial: Length
    """属性(Noneの場合例外)"""
    d_axial_or_none: Length | None
    """属性"""
    d_extended_foot: Length
    """属性(Noneの場合例外)"""
    d_extended_foot_or_none: Length | None
    """属性"""
    angle_extended_top_taper: Angle
    """属性(Noneの場合例外)"""
    angle_extended_top_taper_or_none: Angle | None
    """属性"""
    length_extended_foot: Length
    """属性(Noneの場合例外)"""
    length_extended_foot_or_none: Length | None
    """属性"""
    angle_extended_foot_taper: Angle
    """属性(Noneの場合例外)"""
    angle_extended_foot_taper_or_none: Angle | None
    """属性"""

class StbSecBarArrangementPileRc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover: Length | None = ...,
        depth_cover_top: Length | None = ...,
        is_spiral: bool | None = ...,
        stb_sec_bar_pile_rc_same: StbSecBarPileRcSame | None = ...,
        stb_sec_bar_pile_rc_top_bottom: Sequence[StbSecBarPileRcTopBottom] = ...,
        stb_sec_bar_pile_rc_top_center_bottom: Sequence[
            StbSecBarPileRcTopCenterBottom
        ] = ...,
    ): ...
    depth_cover: Length
    """属性(Noneの場合例外)"""
    depth_cover_or_none: Length | None
    """属性"""
    depth_cover_top: Length
    """属性(Noneの場合例外)"""
    depth_cover_top_or_none: Length | None
    """属性"""
    is_spiral: bool
    """属性(Noneの場合例外)"""
    is_spiral_or_none: bool | None
    """属性"""
    stb_sec_bar_pile_rc_same: StbSecBarPileRcSame
    """子要素(Noneの場合例外)"""
    stb_sec_bar_pile_rc_same_or_none: StbSecBarPileRcSame | None
    """子要素"""
    @property
    def stb_sec_bar_pile_rc_top_bottom(self) -> list[StbSecBarPileRcTopBottom]:
        """stb_sec_bar_pile_rc_top_bottom (list[StbSecBarPileRcTopBottom]): 子要素"""
    @stb_sec_bar_pile_rc_top_bottom.setter
    def stb_sec_bar_pile_rc_top_bottom(
        self, value: Sequence[StbSecBarPileRcTopBottom]
    ) -> None: ...
    @property
    def stb_sec_bar_pile_rc_top_center_bottom(
        self,
    ) -> list[StbSecBarPileRcTopCenterBottom]:
        """stb_sec_bar_pile_rc_top_center_bottom (list[StbSecBarPileRcTopCenterBottom]): 子要素"""
    @stb_sec_bar_pile_rc_top_center_bottom.setter
    def stb_sec_bar_pile_rc_top_center_bottom(
        self, value: Sequence[StbSecBarPileRcTopCenterBottom]
    ) -> None: ...
    @property
    def ensure(self) -> _StbSecBarArrangementPileRcEnsureAccessor: ...

class StbSecBarPileRcSame(StBridgeElement):
    def __init__(
        self,
        *,
        d_main_circumference_1st: str | None = ...,
        d_main_circumference_2nd: str | None = ...,
        d_main_core: str | None = ...,
        d_band: str | None = ...,
        strength_main_circumference_1st: str | None = ...,
        strength_main_circumference_2nd: str | None = ...,
        strength_main_core: str | None = ...,
        strength_band: str | None = ...,
        n_main_circumference_1st: PositiveInteger | None = ...,
        n_main_circumference_2nd: PositiveInteger | None = ...,
        n_main_core: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
    ): ...
    d_main_circumference_1st: str
    """属性(Noneの場合例外)"""
    d_main_circumference_1st_or_none: str | None
    """属性"""
    d_main_circumference_2nd: str
    """属性(Noneの場合例外)"""
    d_main_circumference_2nd_or_none: str | None
    """属性"""
    d_main_core: str
    """属性(Noneの場合例外)"""
    d_main_core_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    strength_main_circumference_1st: str
    """属性(Noneの場合例外)"""
    strength_main_circumference_1st_or_none: str | None
    """属性"""
    strength_main_circumference_2nd: str
    """属性(Noneの場合例外)"""
    strength_main_circumference_2nd_or_none: str | None
    """属性"""
    strength_main_core: str
    """属性(Noneの場合例外)"""
    strength_main_core_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    n_main_circumference_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_circumference_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_circumference_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_circumference_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_core: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_core_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""

class StbSecBarPileRcTopBottom(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarPileRcTopBottomPos | str | None = ...,
        d_main_circumference_1st: str | None = ...,
        d_main_circumference_2nd: str | None = ...,
        d_main_core: str | None = ...,
        d_band: str | None = ...,
        strength_main_circumference_1st: str | None = ...,
        strength_main_circumference_2nd: str | None = ...,
        strength_main_core: str | None = ...,
        strength_band: str | None = ...,
        n_main_circumference_1st: PositiveInteger | None = ...,
        n_main_circumference_2nd: PositiveInteger | None = ...,
        n_main_core: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        length_bar: Length | None = ...,
        length_lap_bar: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarPileRcTopBottomPos:
        """属性(Noneの場合例外) 配筋位置以下のいずれかTOP（杭頭）BOTTOM（杭脚）"""
    @pos.setter
    def pos(self, value: StbSecBarPileRcTopBottomPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarPileRcTopBottomPos | None:
        """属性 配筋位置以下のいずれかTOP（杭頭）BOTTOM（杭脚）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarPileRcTopBottomPos | str | None) -> None: ...
    d_main_circumference_1st: str
    """属性(Noneの場合例外)"""
    d_main_circumference_1st_or_none: str | None
    """属性"""
    d_main_circumference_2nd: str
    """属性(Noneの場合例外)"""
    d_main_circumference_2nd_or_none: str | None
    """属性"""
    d_main_core: str
    """属性(Noneの場合例外)"""
    d_main_core_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外) 帯筋：径"""
    d_band_or_none: str | None
    """属性 帯筋：径"""
    strength_main_circumference_1st: str
    """属性(Noneの場合例外)"""
    strength_main_circumference_1st_or_none: str | None
    """属性"""
    strength_main_circumference_2nd: str
    """属性(Noneの場合例外)"""
    strength_main_circumference_2nd_or_none: str | None
    """属性"""
    strength_main_core: str
    """属性(Noneの場合例外)"""
    strength_main_core_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外) 帯筋：鉄筋強度"""
    strength_band_or_none: str | None
    """属性 帯筋：鉄筋強度"""
    n_main_circumference_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_circumference_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_circumference_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_circumference_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_core: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_core_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外) 帯筋：ピッチ"""
    pitch_band_or_none: Length | None
    """属性 帯筋：ピッチ"""
    length_bar: Length
    """属性(Noneの場合例外) 配筋長さ"""
    length_bar_or_none: Length | None
    """属性 配筋長さ"""
    length_lap_bar: Length
    """属性(Noneの場合例外) 重ね継手長さ"""
    length_lap_bar_or_none: Length | None
    """属性 重ね継手長さ"""

class StbSecBarPileRcTopCenterBottom(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarPileRcTopCenterBottomPos | str | None = ...,
        d_main_circumference_1st: str | None = ...,
        d_main_circumference_2nd: str | None = ...,
        d_main_core: str | None = ...,
        d_band: str | None = ...,
        strength_main_circumference_1st: str | None = ...,
        strength_main_circumference_2nd: str | None = ...,
        strength_main_core: str | None = ...,
        strength_band: str | None = ...,
        n_main_circumference_1st: PositiveInteger | None = ...,
        n_main_circumference_2nd: PositiveInteger | None = ...,
        n_main_core: PositiveInteger | None = ...,
        pitch_band: Length | None = ...,
        length_bar: Length | None = ...,
        length_lap_bar: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarPileRcTopCenterBottomPos:
        """属性(Noneの場合例外)"""
    @pos.setter
    def pos(self, value: StbSecBarPileRcTopCenterBottomPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarPileRcTopCenterBottomPos | None:
        """属性"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarPileRcTopCenterBottomPos | str | None
    ) -> None: ...
    d_main_circumference_1st: str
    """属性(Noneの場合例外)"""
    d_main_circumference_1st_or_none: str | None
    """属性"""
    d_main_circumference_2nd: str
    """属性(Noneの場合例外)"""
    d_main_circumference_2nd_or_none: str | None
    """属性"""
    d_main_core: str
    """属性(Noneの場合例外)"""
    d_main_core_or_none: str | None
    """属性"""
    d_band: str
    """属性(Noneの場合例外)"""
    d_band_or_none: str | None
    """属性"""
    strength_main_circumference_1st: str
    """属性(Noneの場合例外)"""
    strength_main_circumference_1st_or_none: str | None
    """属性"""
    strength_main_circumference_2nd: str
    """属性(Noneの場合例外)"""
    strength_main_circumference_2nd_or_none: str | None
    """属性"""
    strength_main_core: str
    """属性(Noneの場合例外)"""
    strength_main_core_or_none: str | None
    """属性"""
    strength_band: str
    """属性(Noneの場合例外)"""
    strength_band_or_none: str | None
    """属性"""
    n_main_circumference_1st: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_circumference_1st_or_none: PositiveInteger | None
    """属性"""
    n_main_circumference_2nd: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_circumference_2nd_or_none: PositiveInteger | None
    """属性"""
    n_main_core: PositiveInteger
    """属性(Noneの場合例外)"""
    n_main_core_or_none: PositiveInteger | None
    """属性"""
    pitch_band: Length
    """属性(Noneの場合例外)"""
    pitch_band_or_none: Length | None
    """属性"""
    length_bar: Length
    """属性(Noneの場合例外)"""
    length_bar_or_none: Length | None
    """属性"""
    length_lap_bar: Length
    """属性(Noneの場合例外)"""
    length_lap_bar_or_none: Length | None
    """属性"""

class StbSecPileS(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        stb_sec_figure_pile_s: StbSecFigurePileS | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    stb_sec_figure_pile_s: StbSecFigurePileS
    """子要素(Noneの場合例外)"""
    stb_sec_figure_pile_s_or_none: StbSecFigurePileS | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecPileSEnsureAccessor: ...

class StbSecFigurePileS(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_pile_s_straight: Sequence[StbSecPileSStraight] = ...,
        stb_sec_pile_s_rotational: Sequence[StbSecPileSRotational] = ...,
        stb_sec_pile_s_taper: Sequence[StbSecPileSTaper] = ...,
    ): ...
    @property
    def stb_sec_pile_s_straight(self) -> list[StbSecPileSStraight]:
        """stb_sec_pile_s_straight (list[StbSecPileSStraight]): 子要素"""
    @stb_sec_pile_s_straight.setter
    def stb_sec_pile_s_straight(self, value: Sequence[StbSecPileSStraight]) -> None: ...
    @property
    def stb_sec_pile_s_rotational(self) -> list[StbSecPileSRotational]:
        """stb_sec_pile_s_rotational (list[StbSecPileSRotational]): 子要素"""
    @stb_sec_pile_s_rotational.setter
    def stb_sec_pile_s_rotational(
        self, value: Sequence[StbSecPileSRotational]
    ) -> None: ...
    @property
    def stb_sec_pile_s_taper(self) -> list[StbSecPileSTaper]:
        """stb_sec_pile_s_taper (list[StbSecPileSTaper]): 子要素"""
    @stb_sec_pile_s_taper.setter
    def stb_sec_pile_s_taper(self, value: Sequence[StbSecPileSTaper]) -> None: ...

class StbSecPileSStraight(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        d: Length | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外) 継杭の位置"""
    id_order_or_none: PositiveInteger | None
    """属性 継杭の位置"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外) 杭の長さ"""
    length_pile_or_none: Length | None
    """属性 杭の長さ"""
    d: Length
    """属性(Noneの場合例外) 軸部径"""
    d_or_none: Length | None
    """属性 軸部径"""
    t: Length
    """属性(Noneの場合例外) 鋼管の厚さ"""
    t_or_none: Length | None
    """属性 鋼管の厚さ"""
    strength: str
    """属性(Noneの場合例外) 鋼管の鉄骨強度"""
    strength_or_none: str | None
    """属性 鋼管の鉄骨強度"""

class StbSecPileSRotational(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        d1: Length | None = ...,
        d2: Length | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外) 継杭の位置"""
    id_order_or_none: PositiveInteger | None
    """属性 継杭の位置"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外) 杭の長さ"""
    length_pile_or_none: Length | None
    """属性 杭の長さ"""
    d1: Length
    """属性(Noneの場合例外) 軸部径"""
    d1_or_none: Length | None
    """属性 軸部径"""
    d2: Length
    """属性(Noneの場合例外) 先端拡翼径"""
    d2_or_none: Length | None
    """属性 先端拡翼径"""
    t: Length
    """属性(Noneの場合例外) 鋼管の厚さ"""
    t_or_none: Length | None
    """属性 鋼管の厚さ"""
    strength: str
    """属性(Noneの場合例外) 鋼管の鉄骨強度"""
    strength_or_none: str | None
    """属性 鋼管の鉄骨強度"""

class StbSecPileSTaper(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        d1: Length | None = ...,
        d2: Length | None = ...,
        t: Length | None = ...,
        strength: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外) 継杭の位置"""
    id_order_or_none: PositiveInteger | None
    """属性 継杭の位置"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外) 杭の長さ"""
    length_pile_or_none: Length | None
    """属性 杭の長さ"""
    d1: Length
    """属性(Noneの場合例外) 上部径"""
    d1_or_none: Length | None
    """属性 上部径"""
    d2: Length
    """属性(Noneの場合例外) 下部径"""
    d2_or_none: Length | None
    """属性 下部径"""
    t: Length
    """属性(Noneの場合例外) 鋼管の厚さ"""
    t_or_none: Length | None
    """属性 鋼管の厚さ"""
    strength: str
    """属性(Noneの場合例外) 鋼管の鉄骨強度"""
    strength_or_none: str | None
    """属性 鋼管の鉄骨強度"""

class StbSecPileProduct(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        stb_sec_figure_pile_product: StbSecFigurePileProduct | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外)"""
    id_or_none: PositiveInteger | None
    """属性"""
    guid: UUID
    """属性(Noneの場合例外)"""
    guid_or_none: UUID | None
    """属性"""
    name: str
    """属性(Noneの場合例外)"""
    name_or_none: str | None
    """属性"""
    stb_sec_figure_pile_product: StbSecFigurePileProduct
    """子要素(Noneの場合例外)"""
    stb_sec_figure_pile_product_or_none: StbSecFigurePileProduct | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecPileProductEnsureAccessor: ...

class StbSecFigurePileProduct(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_pile_product_phc: Sequence[StbSecPileProductPhc] = ...,
        stb_sec_pile_product_st: Sequence[StbSecPileProductSt] = ...,
        stb_sec_pile_product_sc: Sequence[StbSecPileProductSc] = ...,
        stb_sec_pile_product_prc: Sequence[StbSecPileProductPrc] = ...,
        stb_sec_pile_product_cprc: Sequence[StbSecPileProductCprc] = ...,
        stb_sec_pile_product_nodular_phc: Sequence[StbSecPileProductNodularPhc] = ...,
        stb_sec_pile_product_nodular_prc: Sequence[StbSecPileProductNodularPrc] = ...,
        stb_sec_pile_product_nodular_cprc: Sequence[StbSecPileProductNodularCprc] = ...,
    ): ...
    @property
    def stb_sec_pile_product_phc(self) -> list[StbSecPileProductPhc]:
        """stb_sec_pile_product_phc (list[StbSecPileProductPhc]): 子要素"""
    @stb_sec_pile_product_phc.setter
    def stb_sec_pile_product_phc(
        self, value: Sequence[StbSecPileProductPhc]
    ) -> None: ...
    @property
    def stb_sec_pile_product_st(self) -> list[StbSecPileProductSt]:
        """stb_sec_pile_product_st (list[StbSecPileProductSt]): 子要素"""
    @stb_sec_pile_product_st.setter
    def stb_sec_pile_product_st(self, value: Sequence[StbSecPileProductSt]) -> None: ...
    @property
    def stb_sec_pile_product_sc(self) -> list[StbSecPileProductSc]:
        """stb_sec_pile_product_sc (list[StbSecPileProductSc]): 子要素"""
    @stb_sec_pile_product_sc.setter
    def stb_sec_pile_product_sc(self, value: Sequence[StbSecPileProductSc]) -> None: ...
    @property
    def stb_sec_pile_product_prc(self) -> list[StbSecPileProductPrc]:
        """stb_sec_pile_product_prc (list[StbSecPileProductPrc]): 子要素"""
    @stb_sec_pile_product_prc.setter
    def stb_sec_pile_product_prc(
        self, value: Sequence[StbSecPileProductPrc]
    ) -> None: ...
    @property
    def stb_sec_pile_product_cprc(self) -> list[StbSecPileProductCprc]:
        """stb_sec_pile_product_cprc (list[StbSecPileProductCprc]): 子要素"""
    @stb_sec_pile_product_cprc.setter
    def stb_sec_pile_product_cprc(
        self, value: Sequence[StbSecPileProductCprc]
    ) -> None: ...
    @property
    def stb_sec_pile_product_nodular_phc(self) -> list[StbSecPileProductNodularPhc]:
        """stb_sec_pile_product_nodular_phc (list[StbSecPileProductNodularPhc]): 子要素"""
    @stb_sec_pile_product_nodular_phc.setter
    def stb_sec_pile_product_nodular_phc(
        self, value: Sequence[StbSecPileProductNodularPhc]
    ) -> None: ...
    @property
    def stb_sec_pile_product_nodular_prc(self) -> list[StbSecPileProductNodularPrc]:
        """stb_sec_pile_product_nodular_prc (list[StbSecPileProductNodularPrc]): 子要素"""
    @stb_sec_pile_product_nodular_prc.setter
    def stb_sec_pile_product_nodular_prc(
        self, value: Sequence[StbSecPileProductNodularPrc]
    ) -> None: ...
    @property
    def stb_sec_pile_product_nodular_cprc(self) -> list[StbSecPileProductNodularCprc]:
        """stb_sec_pile_product_nodular_cprc (list[StbSecPileProductNodularCprc]): 子要素"""
    @stb_sec_pile_product_nodular_cprc.setter
    def stb_sec_pile_product_nodular_cprc(
        self, value: Sequence[StbSecPileProductNodularCprc]
    ) -> None: ...

class StbSecPileProductPhc(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d: Length | None = ...,
        t: Length | None = ...,
        strength_concrete: str | None = ...,
        d_pc: Length | None = ...,
        n_pc: PositiveInteger | None = ...,
        strength_pc: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d: Length
    """属性(Noneの場合例外)"""
    d_or_none: Length | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    d_pc: Length
    """属性(Noneの場合例外)"""
    d_pc_or_none: Length | None
    """属性"""
    n_pc: PositiveInteger
    """属性(Noneの場合例外)"""
    n_pc_or_none: PositiveInteger | None
    """属性"""
    strength_pc: str
    """属性(Noneの場合例外)"""
    strength_pc_or_none: str | None
    """属性"""

class StbSecPileProductSt(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d1: Length | None = ...,
        d2: Length | None = ...,
        t1: Length | None = ...,
        t2: Length | None = ...,
        strength_concrete: str | None = ...,
        d_pc: Length | None = ...,
        n_pc: PositiveInteger | None = ...,
        strength_pc: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d1: Length
    """属性(Noneの場合例外)"""
    d1_or_none: Length | None
    """属性"""
    d2: Length
    """属性(Noneの場合例外)"""
    d2_or_none: Length | None
    """属性"""
    t1: Length
    """属性(Noneの場合例外)"""
    t1_or_none: Length | None
    """属性"""
    t2: Length
    """属性(Noneの場合例外)"""
    t2_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    d_pc: Length
    """属性(Noneの場合例外)"""
    d_pc_or_none: Length | None
    """属性"""
    n_pc: PositiveInteger
    """属性(Noneの場合例外)"""
    n_pc_or_none: PositiveInteger | None
    """属性"""
    strength_pc: str
    """属性(Noneの場合例外)"""
    strength_pc_or_none: str | None
    """属性"""

class StbSecPileProductSc(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d: Length | None = ...,
        tc: Length | None = ...,
        ts: Length | None = ...,
        strength_concrete: str | None = ...,
        strength_pipe: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d: Length
    """属性(Noneの場合例外)"""
    d_or_none: Length | None
    """属性"""
    tc: Length
    """属性(Noneの場合例外)"""
    tc_or_none: Length | None
    """属性"""
    ts: Length
    """属性(Noneの場合例外)"""
    ts_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    strength_pipe: str
    """属性(Noneの場合例外)"""
    strength_pipe_or_none: str | None
    """属性"""

class StbSecPileProductPrc(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d: Length | None = ...,
        tc: Length | None = ...,
        strength_concrete: str | None = ...,
        d_pc: Length | None = ...,
        n_pc: PositiveInteger | None = ...,
        strength_pc: str | None = ...,
        d_bar: str | None = ...,
        n_bar: PositiveInteger | None = ...,
        strength_bar: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d: Length
    """属性(Noneの場合例外)"""
    d_or_none: Length | None
    """属性"""
    tc: Length
    """属性(Noneの場合例外)"""
    tc_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    d_pc: Length
    """属性(Noneの場合例外)"""
    d_pc_or_none: Length | None
    """属性"""
    n_pc: PositiveInteger
    """属性(Noneの場合例外)"""
    n_pc_or_none: PositiveInteger | None
    """属性"""
    strength_pc: str
    """属性(Noneの場合例外)"""
    strength_pc_or_none: str | None
    """属性"""
    d_bar: str
    """属性(Noneの場合例外)"""
    d_bar_or_none: str | None
    """属性"""
    n_bar: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_or_none: PositiveInteger | None
    """属性"""
    strength_bar: str
    """属性(Noneの場合例外)"""
    strength_bar_or_none: str | None
    """属性"""

class StbSecPileProductCprc(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d: Length | None = ...,
        tc: Length | None = ...,
        strength_concrete: str | None = ...,
        d_pc: Length | None = ...,
        n_pc: PositiveInteger | None = ...,
        strength_pc: str | None = ...,
        d_bar: str | None = ...,
        n_bar: PositiveInteger | None = ...,
        strength_bar: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d: Length
    """属性(Noneの場合例外)"""
    d_or_none: Length | None
    """属性"""
    tc: Length
    """属性(Noneの場合例外)"""
    tc_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    d_pc: Length
    """属性(Noneの場合例外)"""
    d_pc_or_none: Length | None
    """属性"""
    n_pc: PositiveInteger
    """属性(Noneの場合例外)"""
    n_pc_or_none: PositiveInteger | None
    """属性"""
    strength_pc: str
    """属性(Noneの場合例外)"""
    strength_pc_or_none: str | None
    """属性"""
    d_bar: str
    """属性(Noneの場合例外)"""
    d_bar_or_none: str | None
    """属性"""
    n_bar: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_or_none: PositiveInteger | None
    """属性"""
    strength_bar: str
    """属性(Noneの場合例外)"""
    strength_bar_or_none: str | None
    """属性"""

class StbSecPileProductNodularPhc(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d1: Length | None = ...,
        d2: Length | None = ...,
        t: Length | None = ...,
        strength_concrete: str | None = ...,
        d_pc: Length | None = ...,
        n_pc: PositiveInteger | None = ...,
        strength_pc: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d1: Length
    """属性(Noneの場合例外)"""
    d1_or_none: Length | None
    """属性"""
    d2: Length
    """属性(Noneの場合例外)"""
    d2_or_none: Length | None
    """属性"""
    t: Length
    """属性(Noneの場合例外)"""
    t_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    d_pc: Length
    """属性(Noneの場合例外)"""
    d_pc_or_none: Length | None
    """属性"""
    n_pc: PositiveInteger
    """属性(Noneの場合例外)"""
    n_pc_or_none: PositiveInteger | None
    """属性"""
    strength_pc: str
    """属性(Noneの場合例外)"""
    strength_pc_or_none: str | None
    """属性"""

class StbSecPileProductNodularPrc(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d1: Length | None = ...,
        d2: Length | None = ...,
        tc: Length | None = ...,
        strength_concrete: str | None = ...,
        d_pc: Length | None = ...,
        n_pc: PositiveInteger | None = ...,
        strength_pc: str | None = ...,
        d_bar: str | None = ...,
        n_bar: PositiveInteger | None = ...,
        strength_bar: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d1: Length
    """属性(Noneの場合例外)"""
    d1_or_none: Length | None
    """属性"""
    d2: Length
    """属性(Noneの場合例外)"""
    d2_or_none: Length | None
    """属性"""
    tc: Length
    """属性(Noneの場合例外)"""
    tc_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    d_pc: Length
    """属性(Noneの場合例外)"""
    d_pc_or_none: Length | None
    """属性"""
    n_pc: PositiveInteger
    """属性(Noneの場合例外)"""
    n_pc_or_none: PositiveInteger | None
    """属性"""
    strength_pc: str
    """属性(Noneの場合例外)"""
    strength_pc_or_none: str | None
    """属性"""
    d_bar: str
    """属性(Noneの場合例外)"""
    d_bar_or_none: str | None
    """属性"""
    n_bar: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_or_none: PositiveInteger | None
    """属性"""
    strength_bar: str
    """属性(Noneの場合例外)"""
    strength_bar_or_none: str | None
    """属性"""

class StbSecPileProductNodularCprc(StBridgeElement):
    def __init__(
        self,
        *,
        id_order: PositiveInteger | None = ...,
        product_company: str | None = ...,
        product_code: str | None = ...,
        length_pile: Length | None = ...,
        kind: str | None = ...,
        d1: Length | None = ...,
        d2: Length | None = ...,
        tc: Length | None = ...,
        strength_concrete: str | None = ...,
        d_pc: Length | None = ...,
        n_pc: PositiveInteger | None = ...,
        strength_pc: str | None = ...,
        d_bar: str | None = ...,
        n_bar: PositiveInteger | None = ...,
        strength_bar: str | None = ...,
    ): ...
    id_order: PositiveInteger
    """属性(Noneの場合例外)"""
    id_order_or_none: PositiveInteger | None
    """属性"""
    product_company: str
    """属性(Noneの場合例外)"""
    product_company_or_none: str | None
    """属性"""
    product_code: str
    """属性(Noneの場合例外)"""
    product_code_or_none: str | None
    """属性"""
    length_pile: Length
    """属性(Noneの場合例外)"""
    length_pile_or_none: Length | None
    """属性"""
    kind: str
    """属性(Noneの場合例外)"""
    kind_or_none: str | None
    """属性"""
    d1: Length
    """属性(Noneの場合例外)"""
    d1_or_none: Length | None
    """属性"""
    d2: Length
    """属性(Noneの場合例外)"""
    d2_or_none: Length | None
    """属性"""
    tc: Length
    """属性(Noneの場合例外)"""
    tc_or_none: Length | None
    """属性"""
    strength_concrete: str
    """属性(Noneの場合例外)"""
    strength_concrete_or_none: str | None
    """属性"""
    d_pc: Length
    """属性(Noneの場合例外)"""
    d_pc_or_none: Length | None
    """属性"""
    n_pc: PositiveInteger
    """属性(Noneの場合例外)"""
    n_pc_or_none: PositiveInteger | None
    """属性"""
    strength_pc: str
    """属性(Noneの場合例外)"""
    strength_pc_or_none: str | None
    """属性"""
    d_bar: str
    """属性(Noneの場合例外)"""
    d_bar_or_none: str | None
    """属性"""
    n_bar: PositiveInteger
    """属性(Noneの場合例外)"""
    n_bar_or_none: PositiveInteger | None
    """属性"""
    strength_bar: str
    """属性(Noneの場合例外)"""
    strength_bar_or_none: str | None
    """属性"""

class StbSecOpenRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        stb_sec_bar_arrangement_open_rc: StbSecBarArrangementOpenRc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    stb_sec_bar_arrangement_open_rc: StbSecBarArrangementOpenRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_open_rc_or_none: StbSecBarArrangementOpenRc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecOpenRcEnsureAccessor: ...

class StbSecBarArrangementOpenRc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_bar_open_rc_slab: Sequence[StbSecBarOpenRcSlab] = ...,
        stb_sec_bar_open_rc_wall: Sequence[StbSecBarOpenRcWall] = ...,
    ): ...
    @property
    def stb_sec_bar_open_rc_slab(self) -> list[StbSecBarOpenRcSlab]:
        """stb_sec_bar_open_rc_slab (list[StbSecBarOpenRcSlab]): 子要素"""
    @stb_sec_bar_open_rc_slab.setter
    def stb_sec_bar_open_rc_slab(
        self, value: Sequence[StbSecBarOpenRcSlab]
    ) -> None: ...
    @property
    def stb_sec_bar_open_rc_wall(self) -> list[StbSecBarOpenRcWall]:
        """stb_sec_bar_open_rc_wall (list[StbSecBarOpenRcWall]): 子要素"""
    @stb_sec_bar_open_rc_wall.setter
    def stb_sec_bar_open_rc_wall(
        self, value: Sequence[StbSecBarOpenRcWall]
    ) -> None: ...

class StbSecBarOpenRcSlab(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarOpenRcSlabPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
        length: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarOpenRcSlabPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）DIAGONAL_TOP（斜め方向上端）DIAGONAL_BOTTOM（斜め方向下端）"""
    @pos.setter
    def pos(self, value: StbSecBarOpenRcSlabPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarOpenRcSlabPos | None:
        """属性 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）DIAGONAL_TOP（斜め方向上端）DIAGONAL_BOTTOM（斜め方向下端）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarOpenRcSlabPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""
    length: Length
    """属性(Noneの場合例外) 長さ"""
    length_or_none: Length | None
    """属性 長さ"""

class StbSecBarOpenRcWall(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarOpenRcWallPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
        length: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarOpenRcWallPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）DIAGONAL（斜め筋）"""
    @pos.setter
    def pos(self, value: StbSecBarOpenRcWallPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarOpenRcWallPos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）DIAGONAL（斜め筋）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarOpenRcWallPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""
    length: Length
    """属性(Noneの場合例外) 長さ"""
    length_or_none: Length | None
    """属性 長さ"""

class StbSecParapetRc(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        guid: UUID | None = ...,
        name: str | None = ...,
        strength_concrete: str | None = ...,
        stb_sec_figure_parapet_rc: StbSecFigureParapetRc | None = ...,
        stb_sec_bar_arrangement_parapet_rc: StbSecBarArrangementParapetRc | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    guid: UUID
    """属性(Noneの場合例外) GUID"""
    guid_or_none: UUID | None
    """属性 GUID"""
    name: str
    """属性(Noneの場合例外) 断面名称"""
    name_or_none: str | None
    """属性 断面名称"""
    strength_concrete: str
    """属性(Noneの場合例外) コンクリート強度"""
    strength_concrete_or_none: str | None
    """属性 コンクリート強度"""
    stb_sec_figure_parapet_rc: StbSecFigureParapetRc
    """子要素(Noneの場合例外)"""
    stb_sec_figure_parapet_rc_or_none: StbSecFigureParapetRc | None
    """子要素"""
    stb_sec_bar_arrangement_parapet_rc: StbSecBarArrangementParapetRc
    """子要素(Noneの場合例外)"""
    stb_sec_bar_arrangement_parapet_rc_or_none: StbSecBarArrangementParapetRc | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecParapetRcEnsureAccessor: ...

class StbSecFigureParapetRc(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_parapet_rc_type_l: StbSecParapetRcTypeL | None = ...,
        stb_sec_parapet_rc_type_t: StbSecParapetRcTypeT | None = ...,
        stb_sec_parapet_rc_type_i: StbSecParapetRcTypeI | None = ...,
    ): ...
    stb_sec_parapet_rc_type_l: StbSecParapetRcTypeL
    """子要素(Noneの場合例外)"""
    stb_sec_parapet_rc_type_l_or_none: StbSecParapetRcTypeL | None
    """子要素"""
    stb_sec_parapet_rc_type_t: StbSecParapetRcTypeT
    """子要素(Noneの場合例外)"""
    stb_sec_parapet_rc_type_t_or_none: StbSecParapetRcTypeT | None
    """子要素"""
    stb_sec_parapet_rc_type_i: StbSecParapetRcTypeI
    """子要素(Noneの場合例外)"""
    stb_sec_parapet_rc_type_i_or_none: StbSecParapetRcTypeI | None
    """子要素"""
    @property
    def ensure(self) -> _StbSecFigureParapetRcEnsureAccessor: ...

class StbSecParapetRcTypeL(StBridgeElement):
    def __init__(
        self,
        *,
        t_t: Length | None = ...,
        depth_h: Length | None = ...,
        t_t1: Length | None = ...,
        depth_h1: Length | None = ...,
        depth_h2: Length | None = ...,
    ): ...
    t_t: Length
    """属性(Noneの場合例外) 厚さT"""
    t_t_or_none: Length | None
    """属性 厚さT"""
    depth_h: Length
    """属性(Noneの場合例外) 高さH"""
    depth_h_or_none: Length | None
    """属性 高さH"""
    t_t1: Length
    """属性(Noneの場合例外) 寸法T1"""
    t_t1_or_none: Length | None
    """属性 寸法T1"""
    depth_h1: Length
    """属性(Noneの場合例外) 寸法H1"""
    depth_h1_or_none: Length | None
    """属性 寸法H1"""
    depth_h2: Length
    """属性(Noneの場合例外) 寸法H2"""
    depth_h2_or_none: Length | None
    """属性 寸法H2"""

class StbSecParapetRcTypeT(StBridgeElement):
    def __init__(
        self,
        *,
        t_t: Length | None = ...,
        depth_h: Length | None = ...,
        t_t1: Length | None = ...,
        depth_h1: Length | None = ...,
        depth_h2: Length | None = ...,
        depth_h3: Length | None = ...,
    ): ...
    t_t: Length
    """属性(Noneの場合例外) 厚さT"""
    t_t_or_none: Length | None
    """属性 厚さT"""
    depth_h: Length
    """属性(Noneの場合例外) 高さH"""
    depth_h_or_none: Length | None
    """属性 高さH"""
    t_t1: Length
    """属性(Noneの場合例外) 寸法T1"""
    t_t1_or_none: Length | None
    """属性 寸法T1"""
    depth_h1: Length
    """属性(Noneの場合例外) 寸法H1"""
    depth_h1_or_none: Length | None
    """属性 寸法H1"""
    depth_h2: Length
    """属性(Noneの場合例外) 寸法H2"""
    depth_h2_or_none: Length | None
    """属性 寸法H2"""
    depth_h3: Length
    """属性(Noneの場合例外) 寸法H3"""
    depth_h3_or_none: Length | None
    """属性 寸法H3"""

class StbSecParapetRcTypeI(StBridgeElement):
    def __init__(self, *, t_t: Length | None = ..., depth_h: Length | None = ...): ...
    t_t: Length
    """属性(Noneの場合例外) 厚さT"""
    t_t_or_none: Length | None
    """属性 厚さT"""
    depth_h: Length
    """属性(Noneの場合例外) 高さH"""
    depth_h_or_none: Length | None
    """属性 高さH"""

class StbSecBarArrangementParapetRc(StBridgeElement):
    def __init__(
        self,
        *,
        depth_cover_outside: Length | None = ...,
        depth_cover_inside: Length | None = ...,
        is_tipline: bool | None = ...,
        stb_sec_bar_parapet_rc_single: Sequence[StbSecBarParapetRcSingle] = ...,
        stb_sec_bar_parapet_rc_zigzag: Sequence[StbSecBarParapetRcZigzag] = ...,
        stb_sec_bar_parapet_rc_double_net: Sequence[StbSecBarParapetRcDoubleNet] = ...,
        stb_sec_bar_parapet_rc_tip: Sequence[StbSecBarParapetRcTip] = ...,
        stb_sec_bar_parapet_rc_edge: Sequence[StbSecBarParapetRcEdge] = ...,
    ): ...
    depth_cover_outside: Length
    """属性(Noneの場合例外)"""
    depth_cover_outside_or_none: Length | None
    """属性"""
    depth_cover_inside: Length
    """属性(Noneの場合例外)"""
    depth_cover_inside_or_none: Length | None
    """属性"""
    is_tipline: bool
    """属性(Noneの場合例外)"""
    is_tipline_or_none: bool | None
    """属性"""
    @property
    def stb_sec_bar_parapet_rc_single(self) -> list[StbSecBarParapetRcSingle]:
        """stb_sec_bar_parapet_rc_single (list[StbSecBarParapetRcSingle]): 子要素"""
    @stb_sec_bar_parapet_rc_single.setter
    def stb_sec_bar_parapet_rc_single(
        self, value: Sequence[StbSecBarParapetRcSingle]
    ) -> None: ...
    @property
    def stb_sec_bar_parapet_rc_zigzag(self) -> list[StbSecBarParapetRcZigzag]:
        """stb_sec_bar_parapet_rc_zigzag (list[StbSecBarParapetRcZigzag]): 子要素"""
    @stb_sec_bar_parapet_rc_zigzag.setter
    def stb_sec_bar_parapet_rc_zigzag(
        self, value: Sequence[StbSecBarParapetRcZigzag]
    ) -> None: ...
    @property
    def stb_sec_bar_parapet_rc_double_net(self) -> list[StbSecBarParapetRcDoubleNet]:
        """stb_sec_bar_parapet_rc_double_net (list[StbSecBarParapetRcDoubleNet]): 子要素"""
    @stb_sec_bar_parapet_rc_double_net.setter
    def stb_sec_bar_parapet_rc_double_net(
        self, value: Sequence[StbSecBarParapetRcDoubleNet]
    ) -> None: ...
    @property
    def stb_sec_bar_parapet_rc_tip(self) -> list[StbSecBarParapetRcTip]:
        """stb_sec_bar_parapet_rc_tip (list[StbSecBarParapetRcTip]): 子要素"""
    @stb_sec_bar_parapet_rc_tip.setter
    def stb_sec_bar_parapet_rc_tip(
        self, value: Sequence[StbSecBarParapetRcTip]
    ) -> None: ...
    @property
    def stb_sec_bar_parapet_rc_edge(self) -> list[StbSecBarParapetRcEdge]:
        """stb_sec_bar_parapet_rc_edge (list[StbSecBarParapetRcEdge]): 子要素"""
    @stb_sec_bar_parapet_rc_edge.setter
    def stb_sec_bar_parapet_rc_edge(
        self, value: Sequence[StbSecBarParapetRcEdge]
    ) -> None: ...

class StbSecBarParapetRcSingle(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarParapetRcSinglePos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarParapetRcSinglePos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos.setter
    def pos(self, value: StbSecBarParapetRcSinglePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarParapetRcSinglePos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarParapetRcSinglePos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecBarParapetRcZigzag(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarParapetRcZigzagPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarParapetRcZigzagPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos.setter
    def pos(self, value: StbSecBarParapetRcZigzagPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarParapetRcZigzagPos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarParapetRcZigzagPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecBarParapetRcDoubleNet(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarParapetRcDoubleNetPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarParapetRcDoubleNetPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos.setter
    def pos(self, value: StbSecBarParapetRcDoubleNetPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarParapetRcDoubleNetPos | None:
        """属性 配筋位置 以下のいずれかVERTICAL（縦筋）HORIZONTAL（横筋）"""
    @pos_or_none.setter
    def pos_or_none(
        self, value: StbSecBarParapetRcDoubleNetPos | str | None
    ) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""

class StbSecBarParapetRcTip(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarParapetRcTipPos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        pitch: Length | None = ...,
        n: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarParapetRcTipPos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかSHORT_SIDE（短辺方向）LONG_SIDE（長辺方向）"""
    @pos.setter
    def pos(self, value: StbSecBarParapetRcTipPos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarParapetRcTipPos | None:
        """属性 配筋位置 以下のいずれかSHORT_SIDE（短辺方向）LONG_SIDE（長辺方向）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarParapetRcTipPos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    pitch: Length
    """属性(Noneの場合例外) ピッチ"""
    pitch_or_none: Length | None
    """属性 ピッチ"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""

class StbSecBarParapetRcEdge(StBridgeElement):
    def __init__(
        self,
        *,
        pos: StbSecBarParapetRcEdgePos | str | None = ...,
        strength: str | None = ...,
        d: str | None = ...,
        n: PositiveInteger | None = ...,
    ): ...
    @property
    def pos(self) -> StbSecBarParapetRcEdgePos:
        """属性(Noneの場合例外) 配筋位置 以下のいずれかVERTICAL_START（パラペット始端）VERTICAL_END（パラペット終端）HORIZONTAL_TOP（パラペット上端）HORIZONTAL_BOTTOM（パラペット下端）"""
    @pos.setter
    def pos(self, value: StbSecBarParapetRcEdgePos | str) -> None: ...
    @property
    def pos_or_none(self) -> StbSecBarParapetRcEdgePos | None:
        """属性 配筋位置 以下のいずれかVERTICAL_START（パラペット始端）VERTICAL_END（パラペット終端）HORIZONTAL_TOP（パラペット上端）HORIZONTAL_BOTTOM（パラペット下端）"""
    @pos_or_none.setter
    def pos_or_none(self, value: StbSecBarParapetRcEdgePos | str | None) -> None: ...
    strength: str
    """属性(Noneの場合例外) 鉄筋強度"""
    strength_or_none: str | None
    """属性 鉄筋強度"""
    d: str
    """属性(Noneの場合例外) 径"""
    d_or_none: str | None
    """属性 径"""
    n: PositiveInteger
    """属性(Noneの場合例外) 本数"""
    n_or_none: PositiveInteger | None
    """属性 本数"""

class StbSecSteel(StBridgeElement):
    def __init__(
        self,
        *,
        stb_sec_roll_h: Sequence[StbSecRollH] = ...,
        stb_sec_build_h: Sequence[StbSecBuildH] = ...,
        stb_sec_roll_box: Sequence[StbSecRollBox] = ...,
        stb_sec_build_box: Sequence[StbSecBuildBox] = ...,
        stb_sec_pipe: Sequence[StbSecPipe] = ...,
        stb_sec_roll_t: Sequence[StbSecRollT] = ...,
        stb_sec_roll_c: Sequence[StbSecRollC] = ...,
        stb_sec_roll_l: Sequence[StbSecRollL] = ...,
        stb_sec_lip_c: Sequence[StbSecLipC] = ...,
        stb_sec_flat_bar: Sequence[StbSecFlatBar] = ...,
        stb_sec_round_bar: Sequence[StbSecRoundBar] = ...,
    ): ...
    @property
    def stb_sec_roll_h(self) -> list[StbSecRollH]:
        """stb_sec_roll_h (list[StbSecRollH]): 子要素"""
    @stb_sec_roll_h.setter
    def stb_sec_roll_h(self, value: Sequence[StbSecRollH]) -> None: ...
    @property
    def stb_sec_build_h(self) -> list[StbSecBuildH]:
        """stb_sec_build_h (list[StbSecBuildH]): 子要素"""
    @stb_sec_build_h.setter
    def stb_sec_build_h(self, value: Sequence[StbSecBuildH]) -> None: ...
    @property
    def stb_sec_roll_box(self) -> list[StbSecRollBox]:
        """stb_sec_roll_box (list[StbSecRollBox]): 子要素"""
    @stb_sec_roll_box.setter
    def stb_sec_roll_box(self, value: Sequence[StbSecRollBox]) -> None: ...
    @property
    def stb_sec_build_box(self) -> list[StbSecBuildBox]:
        """stb_sec_build_box (list[StbSecBuildBox]): 子要素"""
    @stb_sec_build_box.setter
    def stb_sec_build_box(self, value: Sequence[StbSecBuildBox]) -> None: ...
    @property
    def stb_sec_pipe(self) -> list[StbSecPipe]:
        """stb_sec_pipe (list[StbSecPipe]): 子要素"""
    @stb_sec_pipe.setter
    def stb_sec_pipe(self, value: Sequence[StbSecPipe]) -> None: ...
    @property
    def stb_sec_roll_t(self) -> list[StbSecRollT]:
        """stb_sec_roll_t (list[StbSecRollT]): 子要素"""
    @stb_sec_roll_t.setter
    def stb_sec_roll_t(self, value: Sequence[StbSecRollT]) -> None: ...
    @property
    def stb_sec_roll_c(self) -> list[StbSecRollC]:
        """stb_sec_roll_c (list[StbSecRollC]): 子要素"""
    @stb_sec_roll_c.setter
    def stb_sec_roll_c(self, value: Sequence[StbSecRollC]) -> None: ...
    @property
    def stb_sec_roll_l(self) -> list[StbSecRollL]:
        """stb_sec_roll_l (list[StbSecRollL]): 子要素"""
    @stb_sec_roll_l.setter
    def stb_sec_roll_l(self, value: Sequence[StbSecRollL]) -> None: ...
    @property
    def stb_sec_lip_c(self) -> list[StbSecLipC]:
        """stb_sec_lip_c (list[StbSecLipC]): 子要素"""
    @stb_sec_lip_c.setter
    def stb_sec_lip_c(self, value: Sequence[StbSecLipC]) -> None: ...
    @property
    def stb_sec_flat_bar(self) -> list[StbSecFlatBar]:
        """stb_sec_flat_bar (list[StbSecFlatBar]): 子要素"""
    @stb_sec_flat_bar.setter
    def stb_sec_flat_bar(self, value: Sequence[StbSecFlatBar]) -> None: ...
    @property
    def stb_sec_round_bar(self) -> list[StbSecRoundBar]:
        """stb_sec_round_bar (list[StbSecRoundBar]): 子要素"""
    @stb_sec_round_bar.setter
    def stb_sec_round_bar(self, value: Sequence[StbSecRoundBar]) -> None: ...

class StbSecRollH(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        type: StbSecRollHType | str | None = ...,
        a: Length | None = ...,
        b: Length | None = ...,
        t1: Length | None = ...,
        t2: Length | None = ...,
        r: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    @property
    def type(self) -> StbSecRollHType:
        """属性(Noneの場合例外) 形状タイプ以下のいずれかH（一般H形鋼）SH（外法一定H形鋼）"""
    @type.setter
    def type(self, value: StbSecRollHType | str) -> None: ...
    @property
    def type_or_none(self) -> StbSecRollHType | None:
        """属性 形状タイプ以下のいずれかH（一般H形鋼）SH（外法一定H形鋼）"""
    @type_or_none.setter
    def type_or_none(self, value: StbSecRollHType | str | None) -> None: ...
    a: Length
    """属性(Noneの場合例外) 成"""
    a_or_none: Length | None
    """属性 成"""
    b: Length
    """属性(Noneの場合例外) フランジ幅"""
    b_or_none: Length | None
    """属性 フランジ幅"""
    t1: Length
    """属性(Noneの場合例外) ウェブ厚"""
    t1_or_none: Length | None
    """属性 ウェブ厚"""
    t2: Length
    """属性(Noneの場合例外) フランジ厚"""
    t2_or_none: Length | None
    """属性 フランジ厚"""
    r: Length
    """属性(Noneの場合例外) フィレット半径"""
    r_or_none: Length | None
    """属性 フィレット半径"""

class StbSecBuildH(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        a: Length | None = ...,
        b: Length | None = ...,
        t1: Length | None = ...,
        t2: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    a: Length
    """属性(Noneの場合例外) 成"""
    a_or_none: Length | None
    """属性 成"""
    b: Length
    """属性(Noneの場合例外) フランジ幅"""
    b_or_none: Length | None
    """属性 フランジ幅"""
    t1: Length
    """属性(Noneの場合例外) ウェブ厚"""
    t1_or_none: Length | None
    """属性 ウェブ厚"""
    t2: Length
    """属性(Noneの場合例外) フランジ厚"""
    t2_or_none: Length | None
    """属性 フランジ厚"""

class StbSecRollBox(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        type: StbSecRollBoxType | str | None = ...,
        a: Length | None = ...,
        b: Length | None = ...,
        t: Length | None = ...,
        r: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    @property
    def type(self) -> StbSecRollBoxType:
        """属性(Noneの場合例外) 形状タイプ以下のいずれかBCP、BCR、STKR、ELSE"""
    @type.setter
    def type(self, value: StbSecRollBoxType | str) -> None: ...
    @property
    def type_or_none(self) -> StbSecRollBoxType | None:
        """属性 形状タイプ以下のいずれかBCP、BCR、STKR、ELSE"""
    @type_or_none.setter
    def type_or_none(self, value: StbSecRollBoxType | str | None) -> None: ...
    a: Length
    """属性(Noneの場合例外) 成"""
    a_or_none: Length | None
    """属性 成"""
    b: Length
    """属性(Noneの場合例外) 幅"""
    b_or_none: Length | None
    """属性 幅"""
    t: Length
    """属性(Noneの場合例外) 板厚"""
    t_or_none: Length | None
    """属性 板厚"""
    r: Length
    """属性(Noneの場合例外) コーナー半径(R)"""
    r_or_none: Length | None
    """属性 コーナー半径(R)"""

class StbSecBuildBox(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        a: Length | None = ...,
        b: Length | None = ...,
        t1: Length | None = ...,
        t2: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    a: Length
    """属性(Noneの場合例外) 成"""
    a_or_none: Length | None
    """属性 成"""
    b: Length
    """属性(Noneの場合例外) 幅"""
    b_or_none: Length | None
    """属性 幅"""
    t1: Length
    """属性(Noneの場合例外) 成方向の板厚"""
    t1_or_none: Length | None
    """属性 成方向の板厚"""
    t2: Length
    """属性(Noneの場合例外) 幅方向の板厚"""
    t2_or_none: Length | None
    """属性 幅方向の板厚"""

class StbSecPipe(StBridgeElement):
    def __init__(
        self, *, name: str | None = ..., d: Length | None = ..., t: Length | None = ...
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    d: Length
    """属性(Noneの場合例外) 直径"""
    d_or_none: Length | None
    """属性 直径"""
    t: Length
    """属性(Noneの場合例外) 板厚"""
    t_or_none: Length | None
    """属性 板厚"""

class StbSecRollT(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        type: StbSecRollTType | str | None = ...,
        a: Length | None = ...,
        b: Length | None = ...,
        t1: Length | None = ...,
        t2: Length | None = ...,
        r: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    @property
    def type(self) -> StbSecRollTType:
        """属性(Noneの場合例外) 形状タイプ以下のいずれかT（一般T形鋼）ST（外法一定T形鋼）"""
    @type.setter
    def type(self, value: StbSecRollTType | str) -> None: ...
    @property
    def type_or_none(self) -> StbSecRollTType | None:
        """属性 形状タイプ以下のいずれかT（一般T形鋼）ST（外法一定T形鋼）"""
    @type_or_none.setter
    def type_or_none(self, value: StbSecRollTType | str | None) -> None: ...
    a: Length
    """属性(Noneの場合例外) 成"""
    a_or_none: Length | None
    """属性 成"""
    b: Length
    """属性(Noneの場合例外) フランジ幅"""
    b_or_none: Length | None
    """属性 フランジ幅"""
    t1: Length
    """属性(Noneの場合例外) ウェブ厚"""
    t1_or_none: Length | None
    """属性 ウェブ厚"""
    t2: Length
    """属性(Noneの場合例外) フランジ厚"""
    t2_or_none: Length | None
    """属性 フランジ厚"""
    r: Length
    """属性(Noneの場合例外) フィレット半径"""
    r_or_none: Length | None
    """属性 フィレット半径"""

class StbSecRollC(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        type: StbSecRollCType | str | None = ...,
        a: Length | None = ...,
        b: Length | None = ...,
        t1: Length | None = ...,
        t2: Length | None = ...,
        r1: Length | None = ...,
        r2: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    @property
    def type(self) -> StbSecRollCType:
        """属性(Noneの場合例外)"""
    @type.setter
    def type(self, value: StbSecRollCType | str) -> None: ...
    @property
    def type_or_none(self) -> StbSecRollCType | None:
        """属性"""
    @type_or_none.setter
    def type_or_none(self, value: StbSecRollCType | str | None) -> None: ...
    a: Length
    """属性(Noneの場合例外) 成"""
    a_or_none: Length | None
    """属性 成"""
    b: Length
    """属性(Noneの場合例外) フランジ幅"""
    b_or_none: Length | None
    """属性 フランジ幅"""
    t1: Length
    """属性(Noneの場合例外) ウェブ厚"""
    t1_or_none: Length | None
    """属性 ウェブ厚"""
    t2: Length
    """属性(Noneの場合例外) フランジ厚"""
    t2_or_none: Length | None
    """属性 フランジ厚"""
    r1: Length
    """属性(Noneの場合例外) フィレット半径"""
    r1_or_none: Length | None
    """属性 フィレット半径"""
    r2: Length
    """属性(Noneの場合例外) フランジ先端半径"""
    r2_or_none: Length | None
    """属性 フランジ先端半径"""

class StbSecRollL(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        type: StbSecRollLType | str | None = ...,
        a: Length | None = ...,
        b: Length | None = ...,
        t1: Length | None = ...,
        t2: Length | None = ...,
        r1: Length | None = ...,
        r2: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    @property
    def type(self) -> StbSecRollLType:
        """属性(Noneの場合例外)"""
    @type.setter
    def type(self, value: StbSecRollLType | str) -> None: ...
    @property
    def type_or_none(self) -> StbSecRollLType | None:
        """属性"""
    @type_or_none.setter
    def type_or_none(self, value: StbSecRollLType | str | None) -> None: ...
    a: Length
    """属性(Noneの場合例外) 成"""
    a_or_none: Length | None
    """属性 成"""
    b: Length
    """属性(Noneの場合例外) 幅"""
    b_or_none: Length | None
    """属性 幅"""
    t1: Length
    """属性(Noneの場合例外) 成方向の板厚"""
    t1_or_none: Length | None
    """属性 成方向の板厚"""
    t2: Length
    """属性(Noneの場合例外) 幅方向の板厚"""
    t2_or_none: Length | None
    """属性 幅方向の板厚"""
    r1: Length
    """属性(Noneの場合例外) フィレット半径"""
    r1_or_none: Length | None
    """属性 フィレット半径"""
    r2: Length
    """属性(Noneの場合例外) 先端半径"""
    r2_or_none: Length | None
    """属性 先端半径"""

class StbSecLipC(StBridgeElement):
    def __init__(
        self,
        *,
        name: str | None = ...,
        type: StbSecLipCType | str | None = ...,
        h: Length | None = ...,
        a: Length | None = ...,
        c: Length | None = ...,
        t: Length | None = ...,
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    @property
    def type(self) -> StbSecLipCType:
        """属性(Noneの場合例外)"""
    @type.setter
    def type(self, value: StbSecLipCType | str) -> None: ...
    @property
    def type_or_none(self) -> StbSecLipCType | None:
        """属性"""
    @type_or_none.setter
    def type_or_none(self, value: StbSecLipCType | str | None) -> None: ...
    h: Length
    """属性(Noneの場合例外) 成"""
    h_or_none: Length | None
    """属性 成"""
    a: Length
    """属性(Noneの場合例外) 幅"""
    a_or_none: Length | None
    """属性 幅"""
    c: Length
    """属性(Noneの場合例外) リップ長"""
    c_or_none: Length | None
    """属性 リップ長"""
    t: Length
    """属性(Noneの場合例外) 板厚"""
    t_or_none: Length | None
    """属性 板厚"""

class StbSecFlatBar(StBridgeElement):
    def __init__(
        self, *, name: str | None = ..., b: Length | None = ..., t: Length | None = ...
    ): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    b: Length
    """属性(Noneの場合例外) 幅"""
    b_or_none: Length | None
    """属性 幅"""
    t: Length
    """属性(Noneの場合例外) 板厚"""
    t_or_none: Length | None
    """属性 板厚"""

class StbSecRoundBar(StBridgeElement):
    def __init__(self, *, name: str | None = ..., r: Length | None = ...): ...
    name: str
    """属性(Noneの場合例外) 形状名"""
    name_or_none: str | None
    """属性 形状名"""
    r: Length
    """属性(Noneの場合例外) 直径"""
    r_or_none: Length | None
    """属性 直径"""

class StbJoints(StBridgeElement):
    def __init__(
        self,
        *,
        stb_joint_beam_shape_h: Sequence[StbJointBeamShapeH] = ...,
        stb_joint_column_shape_h: Sequence[StbJointColumnShapeH] = ...,
        stb_joint_column_shape_t: Sequence[StbJointColumnShapeT] = ...,
        stb_joint_column_shape_cross: Sequence[StbJointColumnShapeCross] = ...,
    ): ...
    @property
    def stb_joint_beam_shape_h(self) -> list[StbJointBeamShapeH]:
        """stb_joint_beam_shape_h (list[StbJointBeamShapeH]): 子要素"""
    @stb_joint_beam_shape_h.setter
    def stb_joint_beam_shape_h(self, value: Sequence[StbJointBeamShapeH]) -> None: ...
    @property
    def stb_joint_column_shape_h(self) -> list[StbJointColumnShapeH]:
        """stb_joint_column_shape_h (list[StbJointColumnShapeH]): 子要素"""
    @stb_joint_column_shape_h.setter
    def stb_joint_column_shape_h(
        self, value: Sequence[StbJointColumnShapeH]
    ) -> None: ...
    @property
    def stb_joint_column_shape_t(self) -> list[StbJointColumnShapeT]:
        """stb_joint_column_shape_t (list[StbJointColumnShapeT]): 子要素"""
    @stb_joint_column_shape_t.setter
    def stb_joint_column_shape_t(
        self, value: Sequence[StbJointColumnShapeT]
    ) -> None: ...
    @property
    def stb_joint_column_shape_cross(self) -> list[StbJointColumnShapeCross]:
        """stb_joint_column_shape_cross (list[StbJointColumnShapeCross]): 子要素"""
    @stb_joint_column_shape_cross.setter
    def stb_joint_column_shape_cross(
        self, value: Sequence[StbJointColumnShapeCross]
    ) -> None: ...

class StbJointBeamShapeH(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        joint_name: str | None = ...,
        joint_mark: str | None = ...,
        stb_joint_shape_h: StbJointShapeH | None = ...,
        stb_joint_shape_h_flange: StbJointShapeHFlange | None = ...,
        stb_joint_shape_h_web: StbJointShapeHWeb | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    joint_name: str
    """属性(Noneの場合例外) 継手呼称"""
    joint_name_or_none: str | None
    """属性 継手呼称"""
    joint_mark: str
    """属性(Noneの場合例外) 継手符号"""
    joint_mark_or_none: str | None
    """属性 継手符号"""
    stb_joint_shape_h: StbJointShapeH
    """子要素(Noneの場合例外)"""
    stb_joint_shape_h_or_none: StbJointShapeH | None
    """子要素"""
    stb_joint_shape_h_flange: StbJointShapeHFlange
    """子要素(Noneの場合例外)"""
    stb_joint_shape_h_flange_or_none: StbJointShapeHFlange | None
    """子要素"""
    stb_joint_shape_h_web: StbJointShapeHWeb
    """子要素(Noneの場合例外)"""
    stb_joint_shape_h_web_or_none: StbJointShapeHWeb | None
    """子要素"""
    @property
    def ensure(self) -> _StbJointBeamShapeHEnsureAccessor: ...

class StbJointShapeH(StBridgeElement):
    def __init__(
        self,
        *,
        strength_plate: str | None = ...,
        strength_bolt: str | None = ...,
        name_bolt: str | None = ...,
        clearance: NonNegativeLength | None = ...,
    ): ...
    strength_plate: str
    """属性(Noneの場合例外)"""
    strength_plate_or_none: str | None
    """属性"""
    strength_bolt: str
    """属性(Noneの場合例外) ボルト材種"""
    strength_bolt_or_none: str | None
    """属性 ボルト材種"""
    name_bolt: str
    """属性(Noneの場合例外) ボルト径（呼び名）"""
    name_bolt_or_none: str | None
    """属性 ボルト径（呼び名）"""
    clearance: NonNegativeLength
    """属性(Noneの場合例外) 部材の母材間隔"""
    clearance_or_none: NonNegativeLength | None
    """属性 部材の母材間隔"""

class StbJointShapeHFlange(StBridgeElement):
    def __init__(
        self,
        *,
        is_zigzag: bool | None = ...,
        nf: PositiveInteger | None = ...,
        mf: PositiveInteger | None = ...,
        g1: Length | None = ...,
        g2: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        outside_thickness: Length | None = ...,
        outside_width: Length | None = ...,
        outside_length: Length | None = ...,
        inside_thickness: Length | None = ...,
        inside_width: Length | None = ...,
        inside_length: Length | None = ...,
    ): ...
    is_zigzag: bool
    """属性(Noneの場合例外) 千鳥配置か否か"""
    is_zigzag_or_none: bool | None
    """属性 千鳥配置か否か"""
    nf: PositiveInteger
    """属性(Noneの場合例外)"""
    nf_or_none: PositiveInteger | None
    """属性"""
    mf: PositiveInteger
    """属性(Noneの場合例外)"""
    mf_or_none: PositiveInteger | None
    """属性"""
    g1: Length
    """属性(Noneの場合例外) ゲージ寸法1 (g1)"""
    g1_or_none: Length | None
    """属性 ゲージ寸法1 (g1)"""
    g2: Length
    """属性(Noneの場合例外) ゲージ寸法2 (g2)"""
    g2_or_none: Length | None
    """属性 ゲージ寸法2 (g2)"""
    pitch: Length
    """属性(Noneの場合例外) 長手方向のボルトピッチ (P)"""
    pitch_or_none: Length | None
    """属性 長手方向のボルトピッチ (P)"""
    e1: Length
    """属性(Noneの場合例外) 縁端距離1 (e1)"""
    e1_or_none: Length | None
    """属性 縁端距離1 (e1)"""
    e2: Length
    """属性(Noneの場合例外) 縁端距離2 (e2)"""
    e2_or_none: Length | None
    """属性 縁端距離2 (e2)"""
    outside_thickness: Length
    """属性(Noneの場合例外) 外添え板 厚さ"""
    outside_thickness_or_none: Length | None
    """属性 外添え板 厚さ"""
    outside_width: Length
    """属性(Noneの場合例外) 外添え板 幅(B)"""
    outside_width_or_none: Length | None
    """属性 外添え板 幅(B)"""
    outside_length: Length
    """属性(Noneの場合例外) 外添え板 長さ(L)"""
    outside_length_or_none: Length | None
    """属性 外添え板 長さ(L)"""
    inside_thickness: Length
    """属性(Noneの場合例外) 内添え板 厚さ"""
    inside_thickness_or_none: Length | None
    """属性 内添え板 厚さ"""
    inside_width: Length
    """属性(Noneの場合例外) 内添え板 幅"""
    inside_width_or_none: Length | None
    """属性 内添え板 幅"""
    inside_length: Length
    """属性(Noneの場合例外) 内添え板 長さ"""
    inside_length_or_none: Length | None
    """属性 内添え板 長さ"""

class StbJointShapeHWeb(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外) 部材成方向のボルトピッチ (pC)"""
    pitch_depth_or_none: Length | None
    """属性 部材成方向のボルトピッチ (pC)"""
    pitch: Length
    """属性(Noneの場合例外) 部材長手方向のボルトピッチ(pL)"""
    pitch_or_none: Length | None
    """属性 部材長手方向のボルトピッチ(pL)"""
    e1: Length
    """属性(Noneの場合例外) 縁端距離1 (e1)"""
    e1_or_none: Length | None
    """属性 縁端距離1 (e1)"""
    e2: Length
    """属性(Noneの場合例外) 縁端距離2 (e2)"""
    e2_or_none: Length | None
    """属性 縁端距離2 (e2)"""
    plate_thickness: Length
    """属性(Noneの場合例外) 添え板 厚さ"""
    plate_thickness_or_none: Length | None
    """属性 添え板 厚さ"""
    plate_width: Length
    """属性(Noneの場合例外) 添え板 幅(B)"""
    plate_width_or_none: Length | None
    """属性 添え板 幅(B)"""
    plate_length: Length
    """属性(Noneの場合例外) 添え板 長さ(L)"""
    plate_length_or_none: Length | None
    """属性 添え板 長さ(L)"""

class StbJointColumnShapeH(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        joint_name: str | None = ...,
        joint_mark: str | None = ...,
        stb_joint_shape_h: StbJointShapeH | None = ...,
        stb_joint_shape_h_flange: StbJointShapeHFlange | None = ...,
        stb_joint_shape_h_web: StbJointShapeHWeb | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    joint_name: str
    """属性(Noneの場合例外) 継手呼称"""
    joint_name_or_none: str | None
    """属性 継手呼称"""
    joint_mark: str
    """属性(Noneの場合例外) 継手符号"""
    joint_mark_or_none: str | None
    """属性 継手符号"""
    stb_joint_shape_h: StbJointShapeH
    """子要素(Noneの場合例外)"""
    stb_joint_shape_h_or_none: StbJointShapeH | None
    """子要素"""
    stb_joint_shape_h_flange: StbJointShapeHFlange
    """子要素(Noneの場合例外)"""
    stb_joint_shape_h_flange_or_none: StbJointShapeHFlange | None
    """子要素"""
    stb_joint_shape_h_web: StbJointShapeHWeb
    """子要素(Noneの場合例外)"""
    stb_joint_shape_h_web_or_none: StbJointShapeHWeb | None
    """子要素"""
    @property
    def ensure(self) -> _StbJointColumnShapeHEnsureAccessor: ...

class StbJointColumnShapeT(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        joint_name: str | None = ...,
        joint_mark: str | None = ...,
        stb_joint_shape_t: StbJointShapeT | None = ...,
        stb_joint_shape_t_flange_h: StbJointShapeTFlangeH | None = ...,
        stb_joint_shape_t_web_h_long: StbJointShapeTWebHLong | None = ...,
        stb_joint_shape_t_web_h_short: StbJointShapeTWebHShort | None = ...,
        stb_joint_shape_t_flange_t: StbJointShapeTFlangeT | None = ...,
        stb_joint_shape_t_web_t: StbJointShapeTWebT | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    joint_name: str
    """属性(Noneの場合例外) 継手呼称"""
    joint_name_or_none: str | None
    """属性 継手呼称"""
    joint_mark: str
    """属性(Noneの場合例外) 継手符号"""
    joint_mark_or_none: str | None
    """属性 継手符号"""
    stb_joint_shape_t: StbJointShapeT
    """子要素(Noneの場合例外)"""
    stb_joint_shape_t_or_none: StbJointShapeT | None
    """子要素"""
    stb_joint_shape_t_flange_h: StbJointShapeTFlangeH
    """子要素(Noneの場合例外)"""
    stb_joint_shape_t_flange_h_or_none: StbJointShapeTFlangeH | None
    """子要素"""
    stb_joint_shape_t_web_h_long: StbJointShapeTWebHLong
    """子要素(Noneの場合例外)"""
    stb_joint_shape_t_web_h_long_or_none: StbJointShapeTWebHLong | None
    """子要素"""
    stb_joint_shape_t_web_h_short: StbJointShapeTWebHShort
    """子要素(Noneの場合例外)"""
    stb_joint_shape_t_web_h_short_or_none: StbJointShapeTWebHShort | None
    """子要素"""
    stb_joint_shape_t_flange_t: StbJointShapeTFlangeT
    """子要素(Noneの場合例外)"""
    stb_joint_shape_t_flange_t_or_none: StbJointShapeTFlangeT | None
    """子要素"""
    stb_joint_shape_t_web_t: StbJointShapeTWebT
    """子要素(Noneの場合例外)"""
    stb_joint_shape_t_web_t_or_none: StbJointShapeTWebT | None
    """子要素"""
    @property
    def ensure(self) -> _StbJointColumnShapeTEnsureAccessor: ...

class StbJointShapeT(StBridgeElement):
    def __init__(
        self,
        *,
        strength_plate: str | None = ...,
        strength_bolt: str | None = ...,
        name_bolt: str | None = ...,
        offset_t: NonNegativeLength | None = ...,
        clearance: NonNegativeLength | None = ...,
    ): ...
    strength_plate: str
    """属性(Noneの場合例外)"""
    strength_plate_or_none: str | None
    """属性"""
    strength_bolt: str
    """属性(Noneの場合例外) ボルト材種"""
    strength_bolt_or_none: str | None
    """属性 ボルト材種"""
    name_bolt: str
    """属性(Noneの場合例外) ボルト径（呼名）"""
    name_bolt_or_none: str | None
    """属性 ボルト径（呼名）"""
    offset_t: NonNegativeLength
    """属性(Noneの場合例外) Ｔ形鋼の偏心（Ｈ形鋼の成の中心からの距離）"""
    offset_t_or_none: NonNegativeLength | None
    """属性 Ｔ形鋼の偏心（Ｈ形鋼の成の中心からの距離）"""
    clearance: NonNegativeLength
    """属性(Noneの場合例外) 部材の母材間隔"""
    clearance_or_none: NonNegativeLength | None
    """属性 部材の母材間隔"""

class StbJointShapeTFlangeH(StBridgeElement):
    def __init__(
        self,
        *,
        is_zigzag: bool | None = ...,
        nf: PositiveInteger | None = ...,
        mf: PositiveInteger | None = ...,
        g1: Length | None = ...,
        g2: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        outside_thickness: Length | None = ...,
        outside_width: Length | None = ...,
        outside_length: Length | None = ...,
        inside_thickness: Length | None = ...,
        inside_width: Length | None = ...,
        inside_length: Length | None = ...,
    ): ...
    is_zigzag: bool
    """属性(Noneの場合例外) 千鳥配置か否か"""
    is_zigzag_or_none: bool | None
    """属性 千鳥配置か否か"""
    nf: PositiveInteger
    """属性(Noneの場合例外)"""
    nf_or_none: PositiveInteger | None
    """属性"""
    mf: PositiveInteger
    """属性(Noneの場合例外)"""
    mf_or_none: PositiveInteger | None
    """属性"""
    g1: Length
    """属性(Noneの場合例外) ゲージ寸法1 (g1)"""
    g1_or_none: Length | None
    """属性 ゲージ寸法1 (g1)"""
    g2: Length
    """属性(Noneの場合例外) ゲージ寸法2 (g2)"""
    g2_or_none: Length | None
    """属性 ゲージ寸法2 (g2)"""
    pitch: Length
    """属性(Noneの場合例外) 長手方向のボルトピッチ(P)"""
    pitch_or_none: Length | None
    """属性 長手方向のボルトピッチ(P)"""
    e1: Length
    """属性(Noneの場合例外) 縁端距離1 (e1)"""
    e1_or_none: Length | None
    """属性 縁端距離1 (e1)"""
    e2: Length
    """属性(Noneの場合例外) 縁端距離2 (e2)"""
    e2_or_none: Length | None
    """属性 縁端距離2 (e2)"""
    outside_thickness: Length
    """属性(Noneの場合例外) 外添え板 厚さ"""
    outside_thickness_or_none: Length | None
    """属性 外添え板 厚さ"""
    outside_width: Length
    """属性(Noneの場合例外) 外添え板 幅(B)"""
    outside_width_or_none: Length | None
    """属性 外添え板 幅(B)"""
    outside_length: Length
    """属性(Noneの場合例外) 外添え板 長さ(L)"""
    outside_length_or_none: Length | None
    """属性 外添え板 長さ(L)"""
    inside_thickness: Length
    """属性(Noneの場合例外) 内添え板 厚さ"""
    inside_thickness_or_none: Length | None
    """属性 内添え板 厚さ"""
    inside_width: Length
    """属性(Noneの場合例外) 内添え板 幅"""
    inside_width_or_none: Length | None
    """属性 内添え板 幅"""
    inside_length: Length
    """属性(Noneの場合例外) 内添え板 長さ"""
    inside_length_or_none: Length | None
    """属性 内添え板 長さ"""

class StbJointShapeTWebHLong(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外) 部材成方向のボルトピッチ (pC)"""
    pitch_depth_or_none: Length | None
    """属性 部材成方向のボルトピッチ (pC)"""
    pitch: Length
    """属性(Noneの場合例外) 部材長手方向のボルトピッチ(pL)"""
    pitch_or_none: Length | None
    """属性 部材長手方向のボルトピッチ(pL)"""
    e1: Length
    """属性(Noneの場合例外) 縁端距離1 (e1)"""
    e1_or_none: Length | None
    """属性 縁端距離1 (e1)"""
    e2: Length
    """属性(Noneの場合例外) 縁端距離2 (e2)"""
    e2_or_none: Length | None
    """属性 縁端距離2 (e2)"""
    plate_thickness: Length
    """属性(Noneの場合例外) 添え板 厚さ"""
    plate_thickness_or_none: Length | None
    """属性 添え板 厚さ"""
    plate_width: Length
    """属性(Noneの場合例外) 添え板 幅(B)"""
    plate_width_or_none: Length | None
    """属性 添え板 幅(B)"""
    plate_length: Length
    """属性(Noneの場合例外) 添え板 長さ(L)"""
    plate_length_or_none: Length | None
    """属性 添え板 長さ(L)"""

class StbJointShapeTWebHShort(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外) 部材成方向のボルトピッチ (pC)"""
    pitch_depth_or_none: Length | None
    """属性 部材成方向のボルトピッチ (pC)"""
    pitch: Length
    """属性(Noneの場合例外) 部材長手方向のボルトピッチ(pL)"""
    pitch_or_none: Length | None
    """属性 部材長手方向のボルトピッチ(pL)"""
    e1: Length
    """属性(Noneの場合例外) 縁端距離1 (e1)"""
    e1_or_none: Length | None
    """属性 縁端距離1 (e1)"""
    e2: Length
    """属性(Noneの場合例外) 縁端距離2 (e2)"""
    e2_or_none: Length | None
    """属性 縁端距離2 (e2)"""
    plate_thickness: Length
    """属性(Noneの場合例外) 添え板 厚さ"""
    plate_thickness_or_none: Length | None
    """属性 添え板 厚さ"""
    plate_width: Length
    """属性(Noneの場合例外) 添え板 幅(B)"""
    plate_width_or_none: Length | None
    """属性 添え板 幅(B)"""
    plate_length: Length
    """属性(Noneの場合例外) 添え板 長さ(L)"""
    plate_length_or_none: Length | None
    """属性 添え板 長さ(L)"""

class StbJointShapeTFlangeT(StBridgeElement):
    def __init__(
        self,
        *,
        is_zigzag: bool | None = ...,
        nf: PositiveInteger | None = ...,
        mf: PositiveInteger | None = ...,
        g1: Length | None = ...,
        g2: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        outside_thickness: Length | None = ...,
        outside_width: Length | None = ...,
        outside_length: Length | None = ...,
        inside_thickness: Length | None = ...,
        inside_width: Length | None = ...,
        inside_length: Length | None = ...,
    ): ...
    is_zigzag: bool
    """属性(Noneの場合例外) 千鳥配置か否か"""
    is_zigzag_or_none: bool | None
    """属性 千鳥配置か否か"""
    nf: PositiveInteger
    """属性(Noneの場合例外)"""
    nf_or_none: PositiveInteger | None
    """属性"""
    mf: PositiveInteger
    """属性(Noneの場合例外)"""
    mf_or_none: PositiveInteger | None
    """属性"""
    g1: Length
    """属性(Noneの場合例外) ゲージ寸法1 (g1)"""
    g1_or_none: Length | None
    """属性 ゲージ寸法1 (g1)"""
    g2: Length
    """属性(Noneの場合例外) ゲージ寸法2 (g2)"""
    g2_or_none: Length | None
    """属性 ゲージ寸法2 (g2)"""
    pitch: Length
    """属性(Noneの場合例外) 長手方向のボルトピッチ(P)"""
    pitch_or_none: Length | None
    """属性 長手方向のボルトピッチ(P)"""
    e1: Length
    """属性(Noneの場合例外) 縁端距離1 (e1)"""
    e1_or_none: Length | None
    """属性 縁端距離1 (e1)"""
    e2: Length
    """属性(Noneの場合例外) 縁端距離2 (e2)"""
    e2_or_none: Length | None
    """属性 縁端距離2 (e2)"""
    outside_thickness: Length
    """属性(Noneの場合例外) 外添え板 厚さ"""
    outside_thickness_or_none: Length | None
    """属性 外添え板 厚さ"""
    outside_width: Length
    """属性(Noneの場合例外) 外添え板 幅(B)"""
    outside_width_or_none: Length | None
    """属性 外添え板 幅(B)"""
    outside_length: Length
    """属性(Noneの場合例外) 外添え板 長さ(L)"""
    outside_length_or_none: Length | None
    """属性 外添え板 長さ(L)"""
    inside_thickness: Length
    """属性(Noneの場合例外) 内添え板 厚さ"""
    inside_thickness_or_none: Length | None
    """属性 内添え板 厚さ"""
    inside_width: Length
    """属性(Noneの場合例外) 内添え板 幅"""
    inside_width_or_none: Length | None
    """属性 内添え板 幅"""
    inside_length: Length
    """属性(Noneの場合例外) 内添え板 長さ"""
    inside_length_or_none: Length | None
    """属性 内添え板 長さ"""

class StbJointShapeTWebT(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外) 部材成方向のボルトピッチ (pC)"""
    pitch_depth_or_none: Length | None
    """属性 部材成方向のボルトピッチ (pC)"""
    pitch: Length
    """属性(Noneの場合例外) 部材長手方向のボルトピッチ(pL)"""
    pitch_or_none: Length | None
    """属性 部材長手方向のボルトピッチ(pL)"""
    e1: Length
    """属性(Noneの場合例外) 縁端距離1 (e1)"""
    e1_or_none: Length | None
    """属性 縁端距離1 (e1)"""
    e2: Length
    """属性(Noneの場合例外) 縁端距離2 (e2)"""
    e2_or_none: Length | None
    """属性 縁端距離2 (e2)"""
    plate_thickness: Length
    """属性(Noneの場合例外) 添え板 厚さ"""
    plate_thickness_or_none: Length | None
    """属性 添え板 厚さ"""
    plate_width: Length
    """属性(Noneの場合例外) 添え板 幅(B)"""
    plate_width_or_none: Length | None
    """属性 添え板 幅(B)"""
    plate_length: Length
    """属性(Noneの場合例外) 添え板 長さ(L)"""
    plate_length_or_none: Length | None
    """属性 添え板 長さ(L)"""

class StbJointColumnShapeCross(StBridgeElement):
    def __init__(
        self,
        *,
        id: PositiveInteger | None = ...,
        joint_name: str | None = ...,
        joint_mark: str | None = ...,
        stb_joint_shape_cross: StbJointShapeCross | None = ...,
        stb_joint_shape_cross_x_flange: StbJointShapeCrossXFlange | None = ...,
        stb_joint_shape_cross_x_web_long: StbJointShapeCrossXWebLong | None = ...,
        stb_joint_shape_cross_x_web_short: StbJointShapeCrossXWebShort | None = ...,
        stb_joint_shape_cross_y_flange: StbJointShapeCrossYFlange | None = ...,
        stb_joint_shape_cross_y_web_long: StbJointShapeCrossYWebLong | None = ...,
        stb_joint_shape_cross_y_web_short: StbJointShapeCrossYWebShort | None = ...,
    ): ...
    id: PositiveInteger
    """属性(Noneの場合例外) ID"""
    id_or_none: PositiveInteger | None
    """属性 ID"""
    joint_name: str
    """属性(Noneの場合例外) 継手呼称"""
    joint_name_or_none: str | None
    """属性 継手呼称"""
    joint_mark: str
    """属性(Noneの場合例外) 継手符号"""
    joint_mark_or_none: str | None
    """属性 継手符号"""
    stb_joint_shape_cross: StbJointShapeCross
    """子要素(Noneの場合例外)"""
    stb_joint_shape_cross_or_none: StbJointShapeCross | None
    """子要素"""
    stb_joint_shape_cross_x_flange: StbJointShapeCrossXFlange
    """子要素(Noneの場合例外)"""
    stb_joint_shape_cross_x_flange_or_none: StbJointShapeCrossXFlange | None
    """子要素"""
    stb_joint_shape_cross_x_web_long: StbJointShapeCrossXWebLong
    """子要素(Noneの場合例外)"""
    stb_joint_shape_cross_x_web_long_or_none: StbJointShapeCrossXWebLong | None
    """子要素"""
    stb_joint_shape_cross_x_web_short: StbJointShapeCrossXWebShort
    """子要素(Noneの場合例外)"""
    stb_joint_shape_cross_x_web_short_or_none: StbJointShapeCrossXWebShort | None
    """子要素"""
    stb_joint_shape_cross_y_flange: StbJointShapeCrossYFlange
    """子要素(Noneの場合例外)"""
    stb_joint_shape_cross_y_flange_or_none: StbJointShapeCrossYFlange | None
    """子要素"""
    stb_joint_shape_cross_y_web_long: StbJointShapeCrossYWebLong
    """子要素(Noneの場合例外)"""
    stb_joint_shape_cross_y_web_long_or_none: StbJointShapeCrossYWebLong | None
    """子要素"""
    stb_joint_shape_cross_y_web_short: StbJointShapeCrossYWebShort
    """子要素(Noneの場合例外)"""
    stb_joint_shape_cross_y_web_short_or_none: StbJointShapeCrossYWebShort | None
    """子要素"""
    @property
    def ensure(self) -> _StbJointColumnShapeCrossEnsureAccessor: ...

class StbJointShapeCross(StBridgeElement):
    def __init__(
        self,
        *,
        strength_plate: str | None = ...,
        strength_bolt: str | None = ...,
        name_bolt: str | None = ...,
        offset_hy: NonNegativeLength | None = ...,
        offset_hx: NonNegativeLength | None = ...,
        clearance: NonNegativeLength | None = ...,
    ): ...
    strength_plate: str
    """属性(Noneの場合例外)"""
    strength_plate_or_none: str | None
    """属性"""
    strength_bolt: str
    """属性(Noneの場合例外) ボルト材種"""
    strength_bolt_or_none: str | None
    """属性 ボルト材種"""
    name_bolt: str
    """属性(Noneの場合例外) ボルト径（呼名）"""
    name_bolt_or_none: str | None
    """属性 ボルト径（呼名）"""
    offset_hy: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_hy_or_none: NonNegativeLength | None
    """属性"""
    offset_hx: NonNegativeLength
    """属性(Noneの場合例外)"""
    offset_hx_or_none: NonNegativeLength | None
    """属性"""
    clearance: NonNegativeLength
    """属性(Noneの場合例外) 部材の母材間隔"""
    clearance_or_none: NonNegativeLength | None
    """属性 部材の母材間隔"""

class StbJointShapeCrossXFlange(StBridgeElement):
    def __init__(
        self,
        *,
        is_zigzag: bool | None = ...,
        nf: PositiveInteger | None = ...,
        mf: PositiveInteger | None = ...,
        g1: Length | None = ...,
        g2: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        outside_thickness: Length | None = ...,
        outside_width: Length | None = ...,
        outside_length: Length | None = ...,
        inside_thickness: Length | None = ...,
        inside_width: Length | None = ...,
        inside_length: Length | None = ...,
    ): ...
    is_zigzag: bool
    """属性(Noneの場合例外)"""
    is_zigzag_or_none: bool | None
    """属性"""
    nf: PositiveInteger
    """属性(Noneの場合例外)"""
    nf_or_none: PositiveInteger | None
    """属性"""
    mf: PositiveInteger
    """属性(Noneの場合例外)"""
    mf_or_none: PositiveInteger | None
    """属性"""
    g1: Length
    """属性(Noneの場合例外)"""
    g1_or_none: Length | None
    """属性"""
    g2: Length
    """属性(Noneの場合例外)"""
    g2_or_none: Length | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""
    e1: Length
    """属性(Noneの場合例外)"""
    e1_or_none: Length | None
    """属性"""
    e2: Length
    """属性(Noneの場合例外)"""
    e2_or_none: Length | None
    """属性"""
    outside_thickness: Length
    """属性(Noneの場合例外)"""
    outside_thickness_or_none: Length | None
    """属性"""
    outside_width: Length
    """属性(Noneの場合例外)"""
    outside_width_or_none: Length | None
    """属性"""
    outside_length: Length
    """属性(Noneの場合例外)"""
    outside_length_or_none: Length | None
    """属性"""
    inside_thickness: Length
    """属性(Noneの場合例外)"""
    inside_thickness_or_none: Length | None
    """属性"""
    inside_width: Length
    """属性(Noneの場合例外)"""
    inside_width_or_none: Length | None
    """属性"""
    inside_length: Length
    """属性(Noneの場合例外)"""
    inside_length_or_none: Length | None
    """属性"""

class StbJointShapeCrossXWebLong(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外)"""
    pitch_depth_or_none: Length | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""
    e1: Length
    """属性(Noneの場合例外)"""
    e1_or_none: Length | None
    """属性"""
    e2: Length
    """属性(Noneの場合例外)"""
    e2_or_none: Length | None
    """属性"""
    plate_thickness: Length
    """属性(Noneの場合例外)"""
    plate_thickness_or_none: Length | None
    """属性"""
    plate_width: Length
    """属性(Noneの場合例外)"""
    plate_width_or_none: Length | None
    """属性"""
    plate_length: Length
    """属性(Noneの場合例外)"""
    plate_length_or_none: Length | None
    """属性"""

class StbJointShapeCrossXWebShort(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外)"""
    pitch_depth_or_none: Length | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""
    e1: Length
    """属性(Noneの場合例外)"""
    e1_or_none: Length | None
    """属性"""
    e2: Length
    """属性(Noneの場合例外)"""
    e2_or_none: Length | None
    """属性"""
    plate_thickness: Length
    """属性(Noneの場合例外)"""
    plate_thickness_or_none: Length | None
    """属性"""
    plate_width: Length
    """属性(Noneの場合例外)"""
    plate_width_or_none: Length | None
    """属性"""
    plate_length: Length
    """属性(Noneの場合例外)"""
    plate_length_or_none: Length | None
    """属性"""

class StbJointShapeCrossYFlange(StBridgeElement):
    def __init__(
        self,
        *,
        is_zigzag: bool | None = ...,
        nf: PositiveInteger | None = ...,
        mf: PositiveInteger | None = ...,
        g1: Length | None = ...,
        g2: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        outside_thickness: Length | None = ...,
        outside_width: Length | None = ...,
        outside_length: Length | None = ...,
        inside_thickness: Length | None = ...,
        inside_width: Length | None = ...,
        inside_length: Length | None = ...,
    ): ...
    is_zigzag: bool
    """属性(Noneの場合例外)"""
    is_zigzag_or_none: bool | None
    """属性"""
    nf: PositiveInteger
    """属性(Noneの場合例外)"""
    nf_or_none: PositiveInteger | None
    """属性"""
    mf: PositiveInteger
    """属性(Noneの場合例外)"""
    mf_or_none: PositiveInteger | None
    """属性"""
    g1: Length
    """属性(Noneの場合例外)"""
    g1_or_none: Length | None
    """属性"""
    g2: Length
    """属性(Noneの場合例外)"""
    g2_or_none: Length | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""
    e1: Length
    """属性(Noneの場合例外)"""
    e1_or_none: Length | None
    """属性"""
    e2: Length
    """属性(Noneの場合例外)"""
    e2_or_none: Length | None
    """属性"""
    outside_thickness: Length
    """属性(Noneの場合例外)"""
    outside_thickness_or_none: Length | None
    """属性"""
    outside_width: Length
    """属性(Noneの場合例外)"""
    outside_width_or_none: Length | None
    """属性"""
    outside_length: Length
    """属性(Noneの場合例外)"""
    outside_length_or_none: Length | None
    """属性"""
    inside_thickness: Length
    """属性(Noneの場合例外)"""
    inside_thickness_or_none: Length | None
    """属性"""
    inside_width: Length
    """属性(Noneの場合例外)"""
    inside_width_or_none: Length | None
    """属性"""
    inside_length: Length
    """属性(Noneの場合例外)"""
    inside_length_or_none: Length | None
    """属性"""

class StbJointShapeCrossYWebLong(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外)"""
    pitch_depth_or_none: Length | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""
    e1: Length
    """属性(Noneの場合例外)"""
    e1_or_none: Length | None
    """属性"""
    e2: Length
    """属性(Noneの場合例外)"""
    e2_or_none: Length | None
    """属性"""
    plate_thickness: Length
    """属性(Noneの場合例外)"""
    plate_thickness_or_none: Length | None
    """属性"""
    plate_width: Length
    """属性(Noneの場合例外)"""
    plate_width_or_none: Length | None
    """属性"""
    plate_length: Length
    """属性(Noneの場合例外)"""
    plate_length_or_none: Length | None
    """属性"""

class StbJointShapeCrossYWebShort(StBridgeElement):
    def __init__(
        self,
        *,
        mw: PositiveInteger | None = ...,
        nw: PositiveInteger | None = ...,
        pitch_depth: Length | None = ...,
        pitch: Length | None = ...,
        e1: Length | None = ...,
        e2: Length | None = ...,
        plate_thickness: Length | None = ...,
        plate_width: Length | None = ...,
        plate_length: Length | None = ...,
    ): ...
    mw: PositiveInteger
    """属性(Noneの場合例外)"""
    mw_or_none: PositiveInteger | None
    """属性"""
    nw: PositiveInteger
    """属性(Noneの場合例外)"""
    nw_or_none: PositiveInteger | None
    """属性"""
    pitch_depth: Length
    """属性(Noneの場合例外)"""
    pitch_depth_or_none: Length | None
    """属性"""
    pitch: Length
    """属性(Noneの場合例外)"""
    pitch_or_none: Length | None
    """属性"""
    e1: Length
    """属性(Noneの場合例外)"""
    e1_or_none: Length | None
    """属性"""
    e2: Length
    """属性(Noneの場合例外)"""
    e2_or_none: Length | None
    """属性"""
    plate_thickness: Length
    """属性(Noneの場合例外)"""
    plate_thickness_or_none: Length | None
    """属性"""
    plate_width: Length
    """属性(Noneの場合例外)"""
    plate_width_or_none: Length | None
    """属性"""
    plate_length: Length
    """属性(Noneの場合例外)"""
    plate_length_or_none: Length | None
    """属性"""

class StbExtensions(StBridgeElement):
    def __init__(self, *, stb_extension: Sequence[StbExtension] = ...): ...
    @property
    def stb_extension(self) -> list[StbExtension]:
        """stb_extension (list[StbExtension]): 子要素"""
    @stb_extension.setter
    def stb_extension(self, value: Sequence[StbExtension]) -> None: ...

class StbExtension(StBridgeElement):
    def __init__(
        self,
        *,
        identifier: str | None = ...,
        description: str | None = ...,
        stb_ext_object: Sequence[StbExtObject] = ...,
        stb_ext_element: Sequence[StbExtElement] = ...,
    ): ...
    identifier: str
    """属性(Noneの場合例外) 拡張情報の識別子"""
    identifier_or_none: str | None
    """属性 拡張情報の識別子"""
    description: str
    """属性(Noneの場合例外) 拡張情報の説明"""
    description_or_none: str | None
    """属性 拡張情報の説明"""
    @property
    def stb_ext_object(self) -> list[StbExtObject]:
        """stb_ext_object (list[StbExtObject]): 子要素"""
    @stb_ext_object.setter
    def stb_ext_object(self, value: Sequence[StbExtObject]) -> None: ...
    @property
    def stb_ext_element(self) -> list[StbExtElement]:
        """stb_ext_element (list[StbExtElement]): 子要素"""
    @stb_ext_element.setter
    def stb_ext_element(self, value: Sequence[StbExtElement]) -> None: ...

class StbExtObject(StBridgeElement):
    def __init__(
        self,
        *,
        object_name: str | None = ...,
        id_object: NonNegativeInteger | None = ...,
        stb_ext_property: Sequence[StbExtProperty] = ...,
    ): ...
    object_name: str
    """属性(Noneの場合例外) ST-Bridgeの要素名"""
    object_name_or_none: str | None
    """属性 ST-Bridgeの要素名"""
    id_object: NonNegativeInteger
    """属性(Noneの場合例外) 要素のID"""
    id_object_or_none: NonNegativeInteger | None
    """属性 要素のID"""
    @property
    def stb_ext_property(self) -> list[StbExtProperty]:
        """stb_ext_property (list[StbExtProperty]): 子要素"""
    @stb_ext_property.setter
    def stb_ext_property(self, value: Sequence[StbExtProperty]) -> None: ...

class StbExtProperty(StBridgeElement):
    def __init__(
        self,
        *,
        key: str | None = ...,
        type: StbExtPropertyType | str | None = ...,
        value: str | None = ...,
    ): ...
    key: str
    """属性(Noneの場合例外) 変数名"""
    key_or_none: str | None
    """属性 変数名"""
    @property
    def type(self) -> StbExtPropertyType:
        """属性(Noneの場合例外) 変数型で以下のいずれかの値をとるstring：文字型integer：整数型double：実数型boolean：論理型"""
    @type.setter
    def type(self, value: StbExtPropertyType | str) -> None: ...
    @property
    def type_or_none(self) -> StbExtPropertyType | None:
        """属性 変数型で以下のいずれかの値をとるstring：文字型integer：整数型double：実数型boolean：論理型"""
    @type_or_none.setter
    def type_or_none(self, value: StbExtPropertyType | str | None) -> None: ...
    value: str
    """属性(Noneの場合例外) 値"""
    value_or_none: str | None
    """属性 値"""

class StbExtElement(StBridgeElement):
    def __init__(
        self,
        *,
        object_name: str | None = ...,
        element_name: str | None = ...,
        stb_ext_property_def: Sequence[StbExtPropertyDef] = ...,
    ): ...
    object_name: str
    """属性(Noneの場合例外) ST-Bridgeの要素名"""
    object_name_or_none: str | None
    """属性 ST-Bridgeの要素名"""
    element_name: str
    """属性(Noneの場合例外) 拡張する子要素の名前"""
    element_name_or_none: str | None
    """属性 拡張する子要素の名前"""
    @property
    def stb_ext_property_def(self) -> list[StbExtPropertyDef]:
        """stb_ext_property_def (list[StbExtPropertyDef]): 子要素"""
    @stb_ext_property_def.setter
    def stb_ext_property_def(self, value: Sequence[StbExtPropertyDef]) -> None: ...

class StbExtPropertyDef(StBridgeElement):
    def __init__(
        self,
        *,
        key: str | None = ...,
        type: StbExtPropertyDefType | str | None = ...,
        default: str | None = ...,
    ): ...
    key: str
    """属性(Noneの場合例外) 変数名"""
    key_or_none: str | None
    """属性 変数名"""
    @property
    def type(self) -> StbExtPropertyDefType:
        """属性(Noneの場合例外) 変数型で以下のいずれかの値をとるstring：文字型integer：整数型double：実数型boolean：論理型"""
    @type.setter
    def type(self, value: StbExtPropertyDefType | str) -> None: ...
    @property
    def type_or_none(self) -> StbExtPropertyDefType | None:
        """属性 変数型で以下のいずれかの値をとるstring：文字型integer：整数型double：実数型boolean：論理型"""
    @type_or_none.setter
    def type_or_none(self, value: StbExtPropertyDefType | str | None) -> None: ...
    default: str
    """属性(Noneの場合例外) 省略値"""
    default_or_none: str | None
    """属性 省略値"""

class _StBridgeEnsureAccessor(_EAP, Protocol):
    def stb_common(self) -> StbCommon: ...
    def stb_model(self) -> StbModel: ...
    def stb_extensions(self) -> StbExtensions: ...

class _StbCommonEnsureAccessor(_EAP, Protocol):
    def stb_reinforcement_strength_list(self) -> StbReinforcementStrengthList: ...
    def stb_apply_conditions_list(self) -> StbApplyConditionsList: ...

class _StbApplyConditionsListEnsureAccessor(_EAP, Protocol):
    def stb_column_rc_rebar_position_apply(self) -> StbColumnRcRebarPositionApply: ...
    def stb_column_rc_bar_spacing_apply(self) -> StbColumnRcBarSpacingApply: ...
    def stb_column_src_rebar_position_apply(self) -> StbColumnSrcRebarPositionApply: ...
    def stb_column_src_bar_spacing_apply(self) -> StbColumnSrcBarSpacingApply: ...
    def stb_beam_rc_rebar_position_apply(self) -> StbBeamRcRebarPositionApply: ...
    def stb_beam_rc_bar_web_apply(self) -> StbBeamRcBarWebApply: ...
    def stb_beam_rc_bar_spacing_apply(self) -> StbBeamRcBarSpacingApply: ...
    def stb_beam_src_rebar_position_apply(self) -> StbBeamSrcRebarPositionApply: ...
    def stb_beam_src_bar_web_apply(self) -> StbBeamSrcBarWebApply: ...
    def stb_beam_src_bar_spacing_apply(self) -> StbBeamSrcBarSpacingApply: ...
    def stb_slab_rc_bar_position_apply(self) -> StbSlabRcBarPositionApply: ...
    def stb_wall_rc_bar_position_apply(self) -> StbWallRcBarPositionApply: ...
    def stb_foundation_rc_bar_position_apply(
        self,
    ) -> StbFoundationRcBarPositionApply: ...
    def stb_pile_rc_bar_position_apply(self) -> StbPileRcBarPositionApply: ...
    def stb_parapet_rc_bar_position_apply(self) -> StbParapetRcBarPositionApply: ...

class _StbModelEnsureAccessor(_EAP, Protocol):
    def stb_nodes(self) -> StbNodes: ...
    def stb_axes(self) -> StbAxes: ...
    def stb_stories(self) -> StbStories: ...
    def stb_members(self) -> StbMembers: ...
    def stb_sections(self) -> StbSections: ...
    def stb_joints(self) -> StbJoints: ...

class _StbAxesEnsureAccessor(_EAP, Protocol):
    def stb_drawing_axes(self) -> StbDrawingAxes: ...

class _StbParallelAxisEnsureAccessor(_EAP, Protocol):
    def stb_node_id_list(self) -> StbNodeIdList: ...

class _StbArcAxisEnsureAccessor(_EAP, Protocol):
    def stb_node_id_list(self) -> StbNodeIdList: ...

class _StbRadialAxisEnsureAccessor(_EAP, Protocol):
    def stb_node_id_list(self) -> StbNodeIdList: ...

class _StbStoryEnsureAccessor(_EAP, Protocol):
    def stb_node_id_list(self) -> StbNodeIdList: ...

class _StbMembersEnsureAccessor(_EAP, Protocol):
    def stb_columns(self) -> StbColumns: ...
    def stb_posts(self) -> StbPosts: ...
    def stb_girders(self) -> StbGirders: ...
    def stb_beams(self) -> StbBeams: ...
    def stb_braces(self) -> StbBraces: ...
    def stb_slabs(self) -> StbSlabs: ...
    def stb_walls(self) -> StbWalls: ...
    def stb_footings(self) -> StbFootings: ...
    def stb_strip_footings(self) -> StbStripFootings: ...
    def stb_piles(self) -> StbPiles: ...
    def stb_foundation_columns(self) -> StbFoundationColumns: ...
    def stb_parapets(self) -> StbParapets: ...
    def stb_opens(self) -> StbOpens: ...

class _StbSlabEnsureAccessor(_EAP, Protocol):
    def stb_node_id_order(self) -> StbNodeIdOrder: ...
    def stb_slab_offset_list(self) -> StbSlabOffsetList: ...
    def stb_open_id_list(self) -> StbOpenIdList: ...

class _StbWallEnsureAccessor(_EAP, Protocol):
    def stb_node_id_order(self) -> StbNodeIdOrder: ...
    def stb_wall_offset_list(self) -> StbWallOffsetList: ...
    def stb_open_id_list(self) -> StbOpenIdList: ...

class _StbSectionsEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel(self) -> StbSecSteel: ...

class _StbSecColumnRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_column_rc(self) -> StbSecFigureColumnRc: ...
    def stb_sec_bar_arrangement_column_rc(self) -> StbSecBarArrangementColumnRc: ...

class _StbSecFigureColumnRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_column_rc_rect(self) -> StbSecColumnRcRect: ...
    def stb_sec_column_rc_circle(self) -> StbSecColumnRcCircle: ...

class _StbSecBarArrangementColumnRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_bar_column_rc_rect_same(self) -> StbSecBarColumnRcRectSame: ...
    def stb_sec_bar_column_x_reinforced(self) -> StbSecBarColumnXReinforced: ...
    def stb_sec_bar_column_rc_circle_same(self) -> StbSecBarColumnRcCircleSame: ...

class _StbSecColumnSEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_figure_column_s(self) -> StbSecSteelFigureColumnS: ...
    def stb_sec_base_product_s(self) -> StbSecBaseProductS: ...
    def stb_sec_base_conventional_s(self) -> StbSecBaseConventionalS: ...

class _StbSecSteelFigureColumnSEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_column_s_same(self) -> StbSecSteelColumnSSame: ...

class _StbSecBaseConventionalSEnsureAccessor(_EAP, Protocol):
    def stb_sec_base_conventional_s_plate(self) -> StbSecBaseConventionalSPlate: ...
    def stb_sec_base_conventional_s_anchor_bolt(
        self,
    ) -> StbSecBaseConventionalSAnchorBolt: ...
    def stb_sec_base_conventional_s_rib_plate(
        self,
    ) -> StbSecBaseConventionalSRibPlate: ...

class _StbSecColumnSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_column_src(self) -> StbSecFigureColumnSrc: ...
    def stb_sec_bar_arrangement_column_src(self) -> StbSecBarArrangementColumnSrc: ...
    def stb_sec_steel_figure_column_src(self) -> StbSecSteelFigureColumnSrc: ...
    def stb_sec_base_product_src(self) -> StbSecBaseProductSrc: ...
    def stb_sec_base_conventional_src(self) -> StbSecBaseConventionalSrc: ...

class _StbSecFigureColumnSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_column_src_rect(self) -> StbSecColumnSrcRect: ...
    def stb_sec_column_src_circle(self) -> StbSecColumnSrcCircle: ...

class _StbSecBarArrangementColumnSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_bar_column_src_rect_same(self) -> StbSecBarColumnSrcRectSame: ...
    def stb_sec_bar_column_src_circle_same(self) -> StbSecBarColumnSrcCircleSame: ...

class _StbSecSteelFigureColumnSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_column_src_same(self) -> StbSecSteelColumnSrcSame: ...

class _StbSecSteelColumnSrcSameEnsureAccessor(_EAP, Protocol):
    def stb_sec_column_src_same_shape_h(self) -> StbSecColumnSrcSameShapeH: ...
    def stb_sec_column_src_same_shape_box(self) -> StbSecColumnSrcSameShapeBox: ...
    def stb_sec_column_src_same_shape_pipe(self) -> StbSecColumnSrcSameShapePipe: ...
    def stb_sec_column_src_same_shape_cross(self) -> StbSecColumnSrcSameShapeCross: ...
    def stb_sec_column_src_same_shape_t(self) -> StbSecColumnSrcSameShapeT: ...

class _StbSecSteelColumnSrcNotSameEnsureAccessor(_EAP, Protocol):
    def stb_sec_column_src_not_same_shape_h(self) -> StbSecColumnSrcNotSameShapeH: ...
    def stb_sec_column_src_not_same_shape_box(
        self,
    ) -> StbSecColumnSrcNotSameShapeBox: ...
    def stb_sec_column_src_not_same_shape_pipe(
        self,
    ) -> StbSecColumnSrcNotSameShapePipe: ...
    def stb_sec_column_src_not_same_shape_cross(
        self,
    ) -> StbSecColumnSrcNotSameShapeCross: ...
    def stb_sec_column_src_not_same_shape_t(self) -> StbSecColumnSrcNotSameShapeT: ...

class _StbSecSteelColumnSrcThreeTypesEnsureAccessor(_EAP, Protocol):
    def stb_sec_column_src_three_types_shape_h(
        self,
    ) -> StbSecColumnSrcThreeTypesShapeH: ...
    def stb_sec_column_src_three_types_shape_box(
        self,
    ) -> StbSecColumnSrcThreeTypesShapeBox: ...
    def stb_sec_column_src_three_types_shape_pipe(
        self,
    ) -> StbSecColumnSrcThreeTypesShapePipe: ...
    def stb_sec_column_src_three_types_shape_cross(
        self,
    ) -> StbSecColumnSrcThreeTypesShapeCross: ...
    def stb_sec_column_src_three_types_shape_t(
        self,
    ) -> StbSecColumnSrcThreeTypesShapeT: ...

class _StbSecBaseConventionalSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_base_conventional_src_plate(self) -> StbSecBaseConventionalSrcPlate: ...
    def stb_sec_base_conventional_src_anchor_bolt(
        self,
    ) -> StbSecBaseConventionalSrcAnchorBolt: ...
    def stb_sec_base_conventional_src_rib_plate(
        self,
    ) -> StbSecBaseConventionalSrcRibPlate: ...

class _StbSecColumnCftEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_figure_column_cft(self) -> StbSecSteelFigureColumnCft: ...
    def stb_sec_base_product_cft(self) -> StbSecBaseProductCft: ...
    def stb_sec_base_conventional_cft(self) -> StbSecBaseConventionalCft: ...

class _StbSecSteelFigureColumnCftEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_column_cft_same(self) -> StbSecSteelColumnCftSame: ...

class _StbSecBaseConventionalCftEnsureAccessor(_EAP, Protocol):
    def stb_sec_base_conventional_cft_plate(self) -> StbSecBaseConventionalCftPlate: ...
    def stb_sec_base_conventional_cft_anchor_bolt(
        self,
    ) -> StbSecBaseConventionalCftAnchorBolt: ...
    def stb_sec_base_conventional_cft_rib_plate(
        self,
    ) -> StbSecBaseConventionalCftRibPlate: ...

class _StbSecBeamRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_beam_rc(self) -> StbSecFigureBeamRc: ...
    def stb_sec_bar_arrangement_beam_rc(self) -> StbSecBarArrangementBeamRc: ...

class _StbSecFigureBeamRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_beam_rc_straight(self) -> StbSecBeamRcStraight: ...

class _StbSecBarArrangementBeamRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_bar_beam_rc_same(self) -> StbSecBarBeamRcSame: ...
    def stb_sec_bar_beam_x_reinforced(self) -> StbSecBarBeamXReinforced: ...

class _StbSecBeamSEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_figure_beam_s(self) -> StbSecSteelFigureBeamS: ...

class _StbSecSteelFigureBeamSEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_beam_s_straight(self) -> StbSecSteelBeamSStraight: ...

class _StbSecBeamSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_beam_src(self) -> StbSecFigureBeamSrc: ...
    def stb_sec_bar_arrangement_beam_src(self) -> StbSecBarArrangementBeamSrc: ...
    def stb_sec_steel_figure_beam_src(self) -> StbSecSteelFigureBeamSrc: ...

class _StbSecFigureBeamSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_beam_src_straight(self) -> StbSecBeamSrcStraight: ...

class _StbSecBarArrangementBeamSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_bar_beam_src_same(self) -> StbSecBarBeamSrcSame: ...

class _StbSecSteelFigureBeamSrcEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_beam_src_straight(self) -> StbSecSteelBeamSrcStraight: ...

class _StbSecBraceSEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_figure_brace_s(self) -> StbSecSteelFigureBraceS: ...

class _StbSecSteelFigureBraceSEnsureAccessor(_EAP, Protocol):
    def stb_sec_steel_brace_s_same(self) -> StbSecSteelBraceSSame: ...

class _StbSecSlabRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_slab_rc(self) -> StbSecFigureSlabRc: ...
    def stb_sec_bar_arrangement_slab_rc(self) -> StbSecBarArrangementSlabRc: ...

class _StbSecFigureSlabRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_slab_rc_straight(self) -> StbSecSlabRcStraight: ...

class _StbSecSlabDeckEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_slab_deck(self) -> StbSecFigureSlabDeck: ...
    def stb_sec_bar_arrangement_slab_deck(self) -> StbSecBarArrangementSlabDeck: ...
    def stb_sec_product_slab_deck(self) -> StbSecProductSlabDeck: ...

class _StbSecFigureSlabDeckEnsureAccessor(_EAP, Protocol):
    def stb_sec_slab_deck_straight(self) -> StbSecSlabDeckStraight: ...

class _StbSecSlabPrecastEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_slab_precast(self) -> StbSecFigureSlabPrecast: ...
    def stb_sec_bar_arrangement_slab_precast(
        self,
    ) -> StbSecBarArrangementSlabPrecast: ...
    def stb_sec_product_slab_precast(self) -> StbSecProductSlabPrecast: ...

class _StbSecFigureSlabPrecastEnsureAccessor(_EAP, Protocol):
    def stb_sec_slab_precast_straight(self) -> StbSecSlabPrecastStraight: ...

class _StbSecWallRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_wall_rc(self) -> StbSecFigureWallRc: ...
    def stb_sec_bar_arrangement_wall_rc(self) -> StbSecBarArrangementWallRc: ...

class _StbSecFigureWallRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_wall_rc_straight(self) -> StbSecWallRcStraight: ...

class _StbSecFoundationRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_foundation_rc(self) -> StbSecFigureFoundationRc: ...
    def stb_sec_bar_arrangement_foundation_rc(
        self,
    ) -> StbSecBarArrangementFoundationRc: ...

class _StbSecFigureFoundationRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_foundation_rc_rect(self) -> StbSecFoundationRcRect: ...
    def stb_sec_foundation_rc_tapered_rect(self) -> StbSecFoundationRcTaperedRect: ...
    def stb_sec_foundation_rc_triangle(self) -> StbSecFoundationRcTriangle: ...
    def stb_sec_foundation_rc_equi_triangle(self) -> StbSecFoundationRcEquiTriangle: ...
    def stb_sec_foundation_rc_octagon(self) -> StbSecFoundationRcOctagon: ...
    def stb_sec_foundation_rc_continuous(self) -> StbSecFoundationRcContinuous: ...

class _StbSecPileRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_pile_rc(self) -> StbSecFigurePileRc: ...
    def stb_sec_bar_arrangement_pile_rc(self) -> StbSecBarArrangementPileRc: ...

class _StbSecFigurePileRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_pile_rc_straight(self) -> StbSecPileRcStraight: ...
    def stb_sec_pile_rc_extended_foot(self) -> StbSecPileRcExtendedFoot: ...
    def stb_sec_pile_rc_extended_top(self) -> StbSecPileRcExtendedTop: ...
    def stb_sec_pile_rc_extended_top_foot(self) -> StbSecPileRcExtendedTopFoot: ...

class _StbSecBarArrangementPileRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_bar_pile_rc_same(self) -> StbSecBarPileRcSame: ...

class _StbSecPileSEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_pile_s(self) -> StbSecFigurePileS: ...

class _StbSecPileProductEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_pile_product(self) -> StbSecFigurePileProduct: ...

class _StbSecOpenRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_bar_arrangement_open_rc(self) -> StbSecBarArrangementOpenRc: ...

class _StbSecParapetRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_figure_parapet_rc(self) -> StbSecFigureParapetRc: ...
    def stb_sec_bar_arrangement_parapet_rc(self) -> StbSecBarArrangementParapetRc: ...

class _StbSecFigureParapetRcEnsureAccessor(_EAP, Protocol):
    def stb_sec_parapet_rc_type_l(self) -> StbSecParapetRcTypeL: ...
    def stb_sec_parapet_rc_type_t(self) -> StbSecParapetRcTypeT: ...
    def stb_sec_parapet_rc_type_i(self) -> StbSecParapetRcTypeI: ...

class _StbJointBeamShapeHEnsureAccessor(_EAP, Protocol):
    def stb_joint_shape_h(self) -> StbJointShapeH: ...
    def stb_joint_shape_h_flange(self) -> StbJointShapeHFlange: ...
    def stb_joint_shape_h_web(self) -> StbJointShapeHWeb: ...

class _StbJointColumnShapeHEnsureAccessor(_EAP, Protocol):
    def stb_joint_shape_h(self) -> StbJointShapeH: ...
    def stb_joint_shape_h_flange(self) -> StbJointShapeHFlange: ...
    def stb_joint_shape_h_web(self) -> StbJointShapeHWeb: ...

class _StbJointColumnShapeTEnsureAccessor(_EAP, Protocol):
    def stb_joint_shape_t(self) -> StbJointShapeT: ...
    def stb_joint_shape_t_flange_h(self) -> StbJointShapeTFlangeH: ...
    def stb_joint_shape_t_web_h_long(self) -> StbJointShapeTWebHLong: ...
    def stb_joint_shape_t_web_h_short(self) -> StbJointShapeTWebHShort: ...
    def stb_joint_shape_t_flange_t(self) -> StbJointShapeTFlangeT: ...
    def stb_joint_shape_t_web_t(self) -> StbJointShapeTWebT: ...

class _StbJointColumnShapeCrossEnsureAccessor(_EAP, Protocol):
    def stb_joint_shape_cross(self) -> StbJointShapeCross: ...
    def stb_joint_shape_cross_x_flange(self) -> StbJointShapeCrossXFlange: ...
    def stb_joint_shape_cross_x_web_long(self) -> StbJointShapeCrossXWebLong: ...
    def stb_joint_shape_cross_x_web_short(self) -> StbJointShapeCrossXWebShort: ...
    def stb_joint_shape_cross_y_flange(self) -> StbJointShapeCrossYFlange: ...
    def stb_joint_shape_cross_y_web_long(self) -> StbJointShapeCrossYWebLong: ...
    def stb_joint_shape_cross_y_web_short(self) -> StbJointShapeCrossYWebShort: ...
