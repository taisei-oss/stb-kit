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
#  - ST-Bridge XMLファイル仕様書（ver.2.1）
#     （2023.03.31、buildingSMART Japan 構造設計小委員会）
#  - ST-Bridge XMLファイル仕様書 計算データ編（ver.2.1）
#     （2023.03.31、buildingSMART Japan 構造設計小委員会）
#  - ST-Bridge XMLファイル仕様書（ver.2.1.1）
#     （2026.04.15、buildingSMART Japan 構造設計小委員会）
from __future__ import annotations

from enum import IntEnum, StrEnum
from typing import ClassVar, Final
from uuid import UUID

from stbkit.core.data_model._internal.stb_types import DataType as _DT
from stbkit.core.data_model.common import StBridgeElement, StBridgeRoot
from stbkit.core.data_model.common import _FieldInfo as _FI
from stbkit.core.data_model.common import _FieldKind as _FK

VERSION: Final[str] = "2.1.1"


class StbConnectionSpecGussetPlateConnectionType(StrEnum):
    """StbConnectionSpecGussetPlate.connection_type で使用できる値。"""

    GAP = "gap"
    WEB = "web"
    SPLICE = "splice"


class StbConnectionSpecGussetPlateFlangeType(StrEnum):
    """StbConnectionSpecGussetPlate.flange_type で使用できる値。"""

    NONE = "none"
    ONE_SIDE = "one_side"
    BOTH_SIDES = "both_sides"


class StbConnectionSpecDiaphragmLocation(StrEnum):
    """StbConnectionSpecDiaphragm.location で使用できる値。"""

    OUTER = "Outer"
    INNER = "Inner"


class StbConnectionSpecDiaphragmType(StrEnum):
    """StbConnectionSpecDiaphragm.type で使用できる値。"""

    THROUGH = "Through"
    INTERNAL = "Internal"
    EXTERNAL = "External"


class StbConnectionSpecPanelPanelType(StrEnum):
    """StbConnectionSpecPanel.panel_type で使用できる値。"""

    SAME = "Same"
    PRODUCT = "Product"
    PLATE = "Plate"


class StbConnectionSpecPanelStrengthStrength(StrEnum):
    """StbConnectionSpecPanelStrength.strength で使用できる値。"""

    SAME = "Same"
    CLASS_C = "Class_C"


class StbConnectionSpecPanelStrengthStrengthInternal(StrEnum):
    """StbConnectionSpecPanelStrength.strength_internal で使用できる値。"""

    SAME = "Same"
    CLASS_C = "Class_C"


class StbWeldCommonKindEndTab(StrEnum):
    """StbWeldCommon.kind_end_tab で使用できる値。"""

    STEEL = "Steel"
    FLUX = "Flux"


class StbWeldCommonShapeBackup(StrEnum):
    """StbWeldCommon.shape_backup で使用できる値。"""

    PL = "PL"
    FB = "FB"


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


class StbColumnSeam(StrEnum):
    """StbColumn.seam で使用できる値。"""

    X_P = "X_P"
    X_N = "X_N"
    Y_P = "Y_P"
    Y_N = "Y_N"
    X = "X"
    Y = "Y"


class StbPostKindStructure(StrEnum):
    """StbPost.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbPostSeam(StrEnum):
    """StbPost.seam で使用できる値。"""

    X_P = "X_P"
    X_N = "X_N"
    Y_P = "Y_P"
    Y_N = "Y_N"
    X = "X"
    Y = "Y"


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


class StbGirderCompositeBeam(StrEnum):
    """StbGirder.composite_beam で使用できる値。"""

    NONE = "NONE"
    INCOMPLETE = "INCOMPLETE"
    COMPLETE = "COMPLETE"


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


class StbBeamCompositeBeam(StrEnum):
    """StbBeam.composite_beam で使用できる値。"""

    NONE = "NONE"
    INCOMPLETE = "INCOMPLETE"
    COMPLETE = "COMPLETE"


class StbBraceKindStructure(StrEnum):
    """StbBrace.kind_structure で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"


class StbBraceFeatureBrace(StrEnum):
    """StbBrace.feature_brace で使用できる値。"""

    TENSION = "TENSION"
    TENSIONANDCOMPRESSION = "TENSIONANDCOMPRESSION"


class StbSlabKindStructure(StrEnum):
    """StbSlab.kind_structure で使用できる値。"""

    RC = "RC"
    DECK = "DECK"
    PRECAST = "PRECAST"
    LOAD = "LOAD"


class StbSlabKindSlab(StrEnum):
    """StbSlab.kind_slab で使用できる値。"""

    NORMAL = "NORMAL"
    CANTI = "CANTI"


class StbSlabDirectionLoad(StrEnum):
    """StbSlab.direction_load で使用できる値。"""

    VALUE_1_WAY = "1WAY"
    VALUE_2_WAY = "2WAY"


class StbWallKindStructure(StrEnum):
    """StbWall.kind_structure で使用できる値。"""

    RC = "RC"
    LOAD = "LOAD"


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


class StbWallTypePress(StrEnum):
    """StbWall.type_press で使用できる値。"""

    NONE = "NONE"
    ONESIDE = "ONESIDE"
    BOTH = "BOTH"


class StbIsolatingDeviceKindStructureStart(StrEnum):
    """StbIsolatingDevice.kind_structure_start で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbIsolatingDeviceKindStructureEnd(StrEnum):
    """StbIsolatingDevice.kind_structure_end で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbDampingDeviceTypeShape(StrEnum):
    """StbDampingDevice.type_shape で使用できる値。"""

    BRACE = "BRACE"
    POST = "POST"
    GIRDER = "GIRDER"


class StbDampingDeviceKindStructureStart(StrEnum):
    """StbDampingDevice.kind_structure_start で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbDampingDeviceKindStructureEnd(StrEnum):
    """StbDampingDevice.kind_structure_end で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"
    UNDEFINED = "UNDEFINED"


class StbFrameDampingDeviceTypeShape(StrEnum):
    """StbFrameDampingDevice.type_shape で使用できる値。"""

    WALL = "WALL"
    BRACES = "BRACES"
    POSTS = "POSTS"
    SHEARLINK = "SHEARLINK"
    HORIZONTALLY_SI_LAYER = "HORIZONTALLY_SI_LAYER"


class StbFrameDampingDeviceMinorTypeShape(StrEnum):
    """StbFrameDampingDevice.minor_type_shape で使用できる値。"""

    NORMAL_V = "NORMAL_V"
    INVERTED_V = "INVERTED_V"
    SEPARATED_V = "SEPARATED_V"
    INVERTED_SEPARATED_V = "INVERTED_SEPARATED_V"
    LOWER_BOTH = "LOWER_BOTH"
    LOWER_2_ND_SIDE = "LOWER_2ND_SIDE"
    LOWER_1_ST_SIDE = "LOWER_1ST_SIDE"
    UPPER_BOTH = "UPPER_BOTH"
    UPPER_3_RD_SIDE = "UPPER_3RD_SIDE"
    UPPER_4_TH_SIDE = "UPPER_4TH_SIDE"
    LOWER_VERTICAL = "LOWER_VERTICAL"
    UPPER_VERTICAL = "UPPER_VERTICAL"


class StbFrameDampingDeviceConnectionKindStructure(StrEnum):
    """StbFrameDampingDeviceConnection.kind_structure で使用できる値。"""

    BRACE = "BRACE"
    POST = "POST"
    GIRDER = "GIRDER"


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


class StbOpenArrangementKindMember(StrEnum):
    """StbOpenArrangement.kind_member で使用できる値。"""

    WALL = "WALL"
    SLAB = "SLAB"


class StbPenetrationArrangementKindMember(StrEnum):
    """StbPenetrationArrangement.kind_member で使用できる値。"""

    GIRDER = "GIRDER"
    BEAM = "BEAM"


class StbJointArrangementKindMember(StrEnum):
    """StbJointArrangement.kind_member で使用できる値。"""

    COLUMN = "COLUMN"
    POST = "POST"
    GIRDER = "GIRDER"
    BEAM = "BEAM"
    BRACE = "BRACE"


class StbJointArrangementStartingPoint(StrEnum):
    """StbJointArrangement.starting_point で使用できる値。"""

    START = "START"
    END = "END"


class StbConnectionGussetPlateSide(StrEnum):
    """StbConnectionGussetPlate.side で使用できる値。"""

    FRONT = "front"
    BACK = "back"


class StbConnectingPostPos(StrEnum):
    """StbConnectingPost.pos で使用できる値。"""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbConnectingGirderPos(StrEnum):
    """StbConnectingGirder.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbConnectingBeamPos(StrEnum):
    """StbConnectingBeam.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbConnectingBracePos(StrEnum):
    """StbConnectingBrace.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbConnectionRibPlateMountingAngle(StrEnum):
    """StbConnectionRibPlate.mounting_angle で使用できる値。"""

    PARALLEL = "Parallel"
    RIGHT_ANGLED = "Right-angled"


class StbSecColumnRcKindColumn(StrEnum):
    """StbSecColumnRc.kind_column で使用できる値。"""

    COLUMN = "COLUMN"
    POST = "POST"


class StbSecBarColumnRectSameSimpleMainDirection(StrEnum):
    """StbSecBarColumnRectSameSimple.main_direction で使用できる値。"""

    X = "X"
    Y = "Y"


class StbSecBarColumnRectSameSimpleHoopType(StrEnum):
    """StbSecBarColumnRectSameSimple.hoop_type で使用できる値。"""

    NORMAL = "NORMAL"
    WELD = "WELD"
    SPIRAL = "SPIRAL"


class StbSecBarColumnRectComplexMainPos(StrEnum):
    """StbSecBarColumnRectComplexMain.pos で使用できる値。"""

    STARTX = "STARTX"
    ENDX = "ENDX"
    STARTY = "STARTY"
    ENDY = "ENDY"


class StbSecBarColumnRectComplexHoopHoopType(StrEnum):
    """StbSecBarColumnRectComplexHoop.hoop_type で使用できる値。"""

    NORMAL = "NORMAL"
    WELD = "WELD"
    SPIRAL = "SPIRAL"


class StbSecBarColumnRectNotSameSimplePos(StrEnum):
    """StbSecBarColumnRectNotSameSimple.pos で使用できる値。"""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbSecBarColumnRectNotSameSimpleMainDirection(StrEnum):
    """StbSecBarColumnRectNotSameSimple.main_direction で使用できる値。"""

    X = "X"
    Y = "Y"


class StbSecBarColumnRectNotSameSimpleHoopType(StrEnum):
    """StbSecBarColumnRectNotSameSimple.hoop_type で使用できる値。"""

    NORMAL = "NORMAL"
    WELD = "WELD"
    SPIRAL = "SPIRAL"


class StbSecBarColumnRectNotSameComplexPos(StrEnum):
    """StbSecBarColumnRectNotSameComplex.pos で使用できる値。"""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbSecBarColumnCircleSameSimpleHoopType(StrEnum):
    """StbSecBarColumnCircleSameSimple.hoop_type で使用できる値。"""

    NORMAL = "NORMAL"
    WELD = "WELD"
    SPIRAL = "SPIRAL"


class StbSecBarColumnCircleComplexHoopHoopType(StrEnum):
    """StbSecBarColumnCircleComplexHoop.hoop_type で使用できる値。"""

    NORMAL = "NORMAL"
    WELD = "WELD"
    SPIRAL = "SPIRAL"


class StbSecBarColumnCircleNotSameSimplePos(StrEnum):
    """StbSecBarColumnCircleNotSameSimple.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecBarColumnCircleNotSameSimpleHoopType(StrEnum):
    """StbSecBarColumnCircleNotSameSimple.hoop_type で使用できる値。"""

    NORMAL = "NORMAL"
    WELD = "WELD"
    SPIRAL = "SPIRAL"


class StbSecBarColumnCircleNotSameComplexPos(StrEnum):
    """StbSecBarColumnCircleNotSameComplex.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
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


class StbSecBaseProductDirectionType(IntEnum):
    """StbSecBaseProduct.direction_type で使用できる値。"""

    VALUE_0 = 0
    VALUE_90 = 90
    VALUE_180 = 180
    VALUE_270 = 270


class StbSecBaseConventionalAnchorBoltsKindBolt(StrEnum):
    """StbSecBaseConventionalAnchorBolts.kind_bolt で使用できる値。"""

    STD = "STD"
    ABR = "ABR"
    ABM = "ABM"


class StbSecBaseConventionalAnchorBoltsTypeBolt(StrEnum):
    """StbSecBaseConventionalAnchorBolts.type_bolt で使用できる値。"""

    I = "I"
    J = "J"
    L = "L"
    LHOOK = "LHOOK"
    HOLEIN = "HOLEIN"


class StbSecColumnSrcKindColumn(StrEnum):
    """StbSecColumnSrc.kind_column で使用できる値。"""

    COLUMN = "COLUMN"
    POST = "POST"


class StbSecSteelFigureColumnSrcBaseType(StrEnum):
    """StbSecSteelFigureColumnSrc.base_type で使用できる値。"""

    NONE = "NONE"
    UNEMBEDDED = "UNEMBEDDED"
    UNEMBEDDED2 = "UNEMBEDDED2"
    EMBEDDED = "EMBEDDED"


class StbSecSteelColumnSrcShapeHDirectionType(StrEnum):
    """StbSecSteelColumnSrcShapeH.direction_type で使用できる値。"""

    H = "H"
    I = "I"


class StbSecSteelColumnSrcShapeBoxEncaseType(StrEnum):
    """StbSecSteelColumnSrcShapeBox.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecSteelColumnSrcShapePipeEncaseType(StrEnum):
    """StbSecSteelColumnSrcShapePipe.encase_type で使用できる値。"""

    ENCASED = "ENCASED"
    ENCASEDANDINFILLED = "ENCASEDANDINFILLED"


class StbSecSteelColumnSrcShapeCross2DirectionType(StrEnum):
    """StbSecSteelColumnSrcShapeCross2.direction_type で使用できる値。"""

    H = "H"
    I = "I"


class StbSecSteelColumnSrcShapeTDirectionType(StrEnum):
    """StbSecSteelColumnSrcShapeT.direction_type で使用できる値。"""

    T1 = "T1"
    T2 = "T2"
    T3 = "T3"
    T4 = "T4"


class StbSecSteelColumnSrcNotSamePos(StrEnum):
    """StbSecSteelColumnSrcNotSame.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecSteelColumnSrcThreeTypesPos(StrEnum):
    """StbSecSteelColumnSrcThreeTypes.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    CENTER = "CENTER"
    TOP = "TOP"


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


class StbSecBeamRcKindBeam(StrEnum):
    """StbSecBeamRc.kind_beam で使用できる値。"""

    GIRDER = "GIRDER"
    BEAM = "BEAM"


class StbSecBarBeamSimpleMainPos(StrEnum):
    """StbSecBarBeamSimpleMain.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecBarBeamComplexMainPos(StrEnum):
    """StbSecBarBeamComplexMain.pos で使用できる値。"""

    BOTTOM = "BOTTOM"
    TOP = "TOP"


class StbSecBeamSKindBeam(StrEnum):
    """StbSecBeamS.kind_beam で使用できる値。"""

    GIRDER = "GIRDER"
    BEAM = "BEAM"


class StbSecSteelBeamWideningPos(StrEnum):
    """StbSecSteelBeamWidening.pos で使用できる値。"""

    START = "START"
    END = "END"


class StbSecBeamSrcKindBeam(StrEnum):
    """StbSecBeamSrc.kind_beam で使用できる値。"""

    GIRDER = "GIRDER"
    BEAM = "BEAM"


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


class StbSecBarSlabRcConventionalStandardPos(StrEnum):
    """StbSecBarSlabRcConventionalStandard.pos で使用できる値。"""

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


class StbSecBarSlabRcConventional2WayPos(StrEnum):
    """StbSecBarSlabRcConventional2Way.pos で使用できる値。"""

    SHORT_TOP_END = "SHORT_TOP_END"
    SHORT_BOTTOM_END = "SHORT_BOTTOM_END"
    SHORT_TOP_CENTER = "SHORT_TOP_CENTER"
    SHORT_BOTTOM_CENTER = "SHORT_BOTTOM_CENTER"
    LONG_TOP_END = "LONG_TOP_END"
    LONG_BOTTOM_END = "LONG_BOTTOM_END"
    LONG_TOP_CENTER = "LONG_TOP_CENTER"
    LONG_BOTTOM_CENTER = "LONG_BOTTOM_CENTER"


class StbSecBarSlabRcConventional1Way1Pos(StrEnum):
    """StbSecBarSlabRcConventional1Way1.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"


class StbSecBarSlabRcConventional1Way2Pos(StrEnum):
    """StbSecBarSlabRcConventional1Way2.pos で使用できる値。"""

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


class StbSecFormworkSlabWoodType(StrEnum):
    """StbSecFormworkSlabWood.type で使用できる値。"""

    A = "A"
    B = "B"
    C = "C"


class StbSecBarSlabRcTruss1WayPos(StrEnum):
    """StbSecBarSlabRcTruss1Way.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    MAIN_BOTTOM = "MAIN_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"


class StbSecBarSlabDeck1WayPos(StrEnum):
    """StbSecBarSlabDeck1Way.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    MESH = "MESH"


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

    SHORT_TOP_END = "SHORT_TOP_END"
    SHORT_BOTTOM_END = "SHORT_BOTTOM_END"
    SHORT_TOP_CENTER = "SHORT_TOP_CENTER"
    SHORT_BOTTOM_CENTER = "SHORT_BOTTOM_CENTER"
    LONG_TOP_END = "LONG_TOP_END"
    LONG_BOTTOM_END = "LONG_BOTTOM_END"
    LONG_TOP_CENTER = "LONG_TOP_CENTER"
    LONG_BOTTOM_CENTER = "LONG_BOTTOM_CENTER"


class StbSecBarSlabPrecast1WayPos(StrEnum):
    """StbSecBarSlabPrecast1Way.pos で使用できる値。"""

    MAIN_TOP = "MAIN_TOP"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    MESH = "MESH"


class StbSecWallRcTaperTypeStraight(StrEnum):
    """StbSecWallRcTaper.type_straight で使用できる値。"""

    OUTSIDE = "OUTSIDE"
    INSIDE = "INSIDE"


class StbSecBarArrangementWallRcOuterBarDirection(StrEnum):
    """StbSecBarArrangementWallRc.outer_bar_direction で使用できる値。"""

    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"


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


class StbSecIsolatingDeviceSpecificationChangeSpecificationChangeable(StrEnum):
    """StbSecIsolatingDeviceSpecificationChange.specification_changeable で使用できる値。"""

    SIZE_FRANGE = "SIZE_FRANGE"
    LENGTH_FRANGE = "LENGTH_FRANGE"
    T_FRANGE = "T_FRANGE"
    PCD_BOLT = "PCD_BOLT"
    N_BOLT = "N_BOLT"
    HOLE_BOLT = "HOLE_BOLT"
    NAME_BOLT = "NAME_BOLT"
    HEIGHT = "HEIGHT"
    SIZE_SLIDEPLATE = "SIZE_SLIDEPLATE"
    T_SLIDEPLATE = "T_SLIDEPLATE"
    PCD_BOLT_SLIDEPLATE = "PCD_BOLT_SLIDEPLATE"
    N_BOLT_SLIDEPLATE = "N_BOLT_SLIDEPLATE"
    NAME_BOLT_SLIDEPLATE = "NAME_BOLT_SLIDEPLATE"


class StbSecIsolatingDeviceEsbPos(StrEnum):
    """StbSecIsolatingDeviceEsb.pos で使用できる値。"""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbSecIsolatingDeviceRsbPos(StrEnum):
    """StbSecIsolatingDeviceRsb.pos で使用できる値。"""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbSecConnectionIsolatingDeviceRbMethodStart(StrEnum):
    """StbSecConnectionIsolatingDeviceRb.method_start で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"


class StbSecConnectionIsolatingDeviceRbShapePlateStart(StrEnum):
    """StbSecConnectionIsolatingDeviceRb.shape_plate_start で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbSecConnectionIsolatingDeviceRbMethodEnd(StrEnum):
    """StbSecConnectionIsolatingDeviceRb.method_end で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"


class StbSecConnectionIsolatingDeviceRbShapePlateEnd(StrEnum):
    """StbSecConnectionIsolatingDeviceRb.shape_plate_end で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbSecConnectionIsolatingDeviceSpMethodBearingside(StrEnum):
    """StbSecConnectionIsolatingDeviceSp.method_bearingside で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"


class StbSecConnectionIsolatingDeviceSpShapePlateBearingside(StrEnum):
    """StbSecConnectionIsolatingDeviceSp.shape_plate_bearingside で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbSecConnectionIsolatingDeviceSpMethodPlateside(StrEnum):
    """StbSecConnectionIsolatingDeviceSp.method_plateside で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"


class StbSecConnectionIsolatingDeviceSpShapePlatePlateside(StrEnum):
    """StbSecConnectionIsolatingDeviceSp.shape_plate_plateside で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbSecConnectionIsolatingDeviceLbMethodStart(StrEnum):
    """StbSecConnectionIsolatingDeviceLb.method_start で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"
    WELDING = "WELDING"


class StbSecConnectionIsolatingDeviceLbMethodEnd(StrEnum):
    """StbSecConnectionIsolatingDeviceLb.method_end で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"
    WELDING = "WELDING"


class StbSecDampingDeviceSpecificationChangeSpecificationChangeable(StrEnum):
    """StbSecDampingDeviceSpecificationChange.specification_changeable で使用できる値。"""

    WIDTH_MOUNTPLATE = "WIDTH_MOUNTPLATE"
    LENGTH_MOUNTPLATE = "LENGTH_MOUNTPLATE"
    T_MOUNTPLATE = "T_MOUNTPLATE"
    NAME_MOUNTPLATE = "NAME_MOUNTPLATE"
    WIDTH_SPLICEPLATE = "WIDTH_SPLICEPLATE"
    LENGTH_SPLICEPLATE = "LENGTH_SPLICEPLATE"
    T_SPLICEPLATE = "T_SPLICEPLATE"
    NAME_SPLICEPLATE = "NAME_SPLICEPLATE"
    PITCH_BOLT = "PITCH_BOLT"
    N_BOLT = "N_BOLT"
    HOLE_BOLT = "HOLE_BOLT"
    NAME_BOLT = "NAME_BOLT"
    LENGTH = "LENGTH"


class StbSecSteelFigureDampingDeviceHistoryKindSectionStiffener(StrEnum):
    """StbSecSteelFigureDampingDeviceHistory.kind_section_stiffener で使用できる値。"""

    RC = "RC"
    S = "S"
    SRC = "SRC"
    CFT = "CFT"


class StbSecConnectionDampingDeviceHorizontalMethodStart(StrEnum):
    """StbSecConnectionDampingDeviceHorizontal.method_start で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"
    THROUGH_BOLT = "THROUGH_BOLT"
    WELDING = "WELDING"


class StbSecConnectionDampingDeviceHorizontalMethodEnd(StrEnum):
    """StbSecConnectionDampingDeviceHorizontal.method_end で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"
    THROUGH_BOLT = "THROUGH_BOLT"
    WELDING = "WELDING"


class StbSecConnectionDampingDeviceVerticalMethodStart(StrEnum):
    """StbSecConnectionDampingDeviceVertical.method_start で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"
    WELDING = "WELDING"


class StbSecConnectionDampingDeviceVerticalMethodEnd(StrEnum):
    """StbSecConnectionDampingDeviceVertical.method_end で使用できる値。"""

    BASEPLATE = "BASEPLATE"
    BOLT = "BOLT"
    WELDING = "WELDING"


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

    MAIN_BASE_TOP = "MAIN_BASE_TOP"
    MAIN_BASE_BOTTOM = "MAIN_BASE_BOTTOM"
    MAIN_TIP_TOP = "MAIN_TIP_TOP"
    MAIN_TIP_BOTTOM = "MAIN_TIP_BOTTOM"
    TRANSVERSE_TOP = "TRANSVERSE_TOP"
    TRANSVERSE_BOTTOM = "TRANSVERSE_BOTTOM"
    HORIZONTAL = "HORIZONTAL"


class StbSecBarFoundationRcContinuousMainType(StrEnum):
    """StbSecBarFoundationRcContinuous.main_type で使用できる値。"""

    SYMMETRICAL = "SYMMETRICAL"
    ASYMMETRICAL = "ASYMMETRICAL"


class StbSecPileRcConventionalConstructionMethod(StrEnum):
    """StbSecPileRcConventional.construction_method で使用できる値。"""

    EARTHDRILL = "EARTHDRILL"
    REVERSE = "REVERSE"
    ALLCASING = "ALLCASING"
    BH = "BH"
    SHINSO = "SHINSO"


class StbSecBarPileRcTopBottomPos(StrEnum):
    """StbSecBarPileRcTopBottom.pos で使用できる値。"""

    TOP = "TOP"
    BOTTOM = "BOTTOM"


class StbSecBarPileRcTopCenterBottomPos(StrEnum):
    """StbSecBarPileRcTopCenterBottom.pos で使用できる値。"""

    TOP = "TOP"
    CENTER = "CENTER"
    BOTTOM = "BOTTOM"


class StbSecPileSConventionalConstructionMethod(StrEnum):
    """StbSecPileSConventional.construction_method で使用できる値。"""

    DRIVING = "DRIVING"
    BURIED = "BURIED"


class StbSecPilePrecastConventionalConstructionMethod(StrEnum):
    """StbSecPilePrecastConventional.construction_method で使用できる値。"""

    DRIVING = "DRIVING"
    BURIED = "BURIED"


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


class StbSecPenetrationSType(StrEnum):
    """StbSecPenetrationS.type で使用できる値。"""

    EG = "EG"
    FR = "FR"
    HI = "HI"
    OS = "OS"
    NO = "NO"
    CO = "CO"


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


class StbSecRoll2cType(StrEnum):
    """StbSecRoll2c.type で使用できる値。"""

    BACKTOBACK = "BACKTOBACK"
    FACETOFACE = "FACETOFACE"


class StbSecRoll2lType(StrEnum):
    """StbSecRoll2l.type で使用できる値。"""

    BACKTOBACK = "BACKTOBACK"
    FACETOFACE = "FACETOFACE"


class StbSecLip2cType(StrEnum):
    """StbSecLip2c.type で使用できる値。"""

    BACKTOBACK = "BACKTOBACK"
    FACETOFACE = "FACETOFACE"


class StbGussetPlateConnectionType(StrEnum):
    """StbGussetPlate.connection_type で使用できる値。"""

    GAP = "gap"
    WEB = "web"
    SPLICE = "splice"


class StbGussetPlateFlangeType(StrEnum):
    """StbGussetPlate.flange_type で使用できる値。"""

    NONE = "none"
    ONE_SIDE = "one_side"
    BOTH_SIDES = "both_sides"


class StbDiaphragmType(StrEnum):
    """StbDiaphragm.type で使用できる値。"""

    THROUGH = "Through"
    INTERNAL = "Internal"
    EXTERNAL = "External"


class StbWeldFullPenetrationTypeWeld(StrEnum):
    """StbWeldFullPenetration.type_weld で使用できる値。"""

    B = "B"
    T = "T"
    C = "C"
    E = "E"


class StbWeldFullPenetrationTypeBackup(StrEnum):
    """StbWeldFullPenetration.type_backup で使用できる値。"""

    U = "U"
    H = "H"


class StbWeldFullPenetrationShapeBevel(StrEnum):
    """StbWeldFullPenetration.shape_bevel で使用できる値。"""

    L = "L"
    V = "V"
    K = "K"
    X = "X"
    I = "I"


class StbWeldFullPenetrationSideBevel1(StrEnum):
    """StbWeldFullPenetration.side_bevel1 で使用できる値。"""

    FRONT = "Front"
    REVERSE = "Reverse"
    BOTH = "Both"


class StbWeldFullPenetrationSideBevel2(StrEnum):
    """StbWeldFullPenetration.side_bevel2 で使用できる値。"""

    RIGHT = "Right"
    LEFT = "Left"


class StbWeldFullPenetrationMethod(StrEnum):
    """StbWeldFullPenetration.method で使用できる値。"""

    G = "G"
    S = "S"
    E = "E"


class StbWeldFullPenetrationLocation(StrEnum):
    """StbWeldFullPenetration.location で使用できる値。"""

    FACTORY = "Factory"
    SITE = "Site"


class StbWeldFullPenetrationKindEndTab(StrEnum):
    """StbWeldFullPenetration.kind_end_tab で使用できる値。"""

    STEEL = "Steel"
    FLUX = "Flux"


class StbWeldFullPenetrationShapeBackup1(StrEnum):
    """StbWeldFullPenetration.shape_backup1 で使用できる値。"""

    PL = "PL"
    FB = "FB"


class StbWeldFullPenetrationShapeBackup2(StrEnum):
    """StbWeldFullPenetration.shape_backup2 で使用できる値。"""

    PL = "PL"
    FB = "FB"


class StbWeldPartialPenetrationTypeWeld(StrEnum):
    """StbWeldPartialPenetration.type_weld で使用できる値。"""

    B = "B"
    T = "T"
    C = "C"


class StbWeldPartialPenetrationTypeBackup(StrEnum):
    """StbWeldPartialPenetration.type_backup で使用できる値。"""

    U = "U"


class StbWeldPartialPenetrationShapeBevel(StrEnum):
    """StbWeldPartialPenetration.shape_bevel で使用できる値。"""

    L = "L"
    V = "V"
    K = "K"


class StbWeldPartialPenetrationSideBevel1(StrEnum):
    """StbWeldPartialPenetration.side_bevel1 で使用できる値。"""

    FRONT = "Front"
    REVERSE = "Reverse"
    BOTH = "Both"


class StbWeldPartialPenetrationSideBevel2(StrEnum):
    """StbWeldPartialPenetration.side_bevel2 で使用できる値。"""

    RIGHT = "Right"
    LEFT = "Left"


class StbWeldPartialPenetrationMethod(StrEnum):
    """StbWeldPartialPenetration.method で使用できる値。"""

    G = "G"
    S = "S"


class StbWeldPartialPenetrationLocation(StrEnum):
    """StbWeldPartialPenetration.location で使用できる値。"""

    FACTORY = "Factory"
    SITE = "Site"


class StbWeldPartialPenetrationShapeBackup(StrEnum):
    """StbWeldPartialPenetration.shape_backup で使用できる値。"""

    PL = "PL"
    FB = "FB"


class StbWeldFilletTypeWeld(StrEnum):
    """StbWeldFillet.type_weld で使用できる値。"""

    B = "B"
    T = "T"
    L = "L"


class StbWeldFilletShapeBevel(StrEnum):
    """StbWeldFillet.shape_bevel で使用できる値。"""

    L = "L"
    K = "K"


class StbWeldFilletSideBevel1(StrEnum):
    """StbWeldFillet.side_bevel1 で使用できる値。"""

    FRONT = "Front"
    REVERSE = "Reverse"


class StbWeldFilletSideBevel2(StrEnum):
    """StbWeldFillet.side_bevel2 で使用できる値。"""

    RIGHT = "Right"
    LEFT = "Left"


class StbWeldFilletLocation(StrEnum):
    """StbWeldFillet.location で使用できる値。"""

    FACTORY = "Factory"
    SITE = "Site"


class StbWeldFlareTypeWeld(StrEnum):
    """StbWeldFlare.type_weld で使用できる値。"""

    RR = "RR"
    RP = "RP"
    CC = "CC"
    CP = "CP"


class StbWeldFlareLocation(StrEnum):
    """StbWeldFlare.location で使用できる値。"""

    FACTORY = "Factory"
    SITE = "Site"


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


class StbCalSeismicConditionSoil(StrEnum):
    """StbCalSeismicCondition.soil で使用できる値。"""

    CLASS1 = "CLASS1"
    CLASS2 = "CLASS2"
    CLASS3 = "CLASS3"


class StbCalWindConditionRoughness(StrEnum):
    """StbCalWindCondition.roughness で使用できる値。"""

    DIVISION1 = "DIVISION1"
    DIVISION2 = "DIVISION2"
    DIVISION3 = "DIVISION3"
    DIVISION4 = "DIVISION4"


class StbCalLiveloadType(StrEnum):
    """StbCalLiveload.type で使用できる値。"""

    HABITABLEROOMS = "HABITABLEROOMS"
    OFFICES = "OFFICES"
    CLASSROOMS = "CLASSROOMS"
    STORES = "STORES"
    MEETINGROOMS_FIXEDSEATING = "MEETINGROOMS_FIXEDSEATING"
    MEETINGROOMS_OTHERSEATS = "MEETINGROOMS_OTHERSEATS"
    AUTOMOBILEGARAGES = "AUTOMOBILEGARAGES"
    INPUT_VALUES = "INPUT_VALUES"


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


class StbCalFinishRcTypeGirder(StrEnum):
    """StbCalFinishRc.type_girder で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    BOTHSIDE_BOTTOM = "BOTHSIDE_BOTTOM"
    ONESIDE_HALFBOTTOM = "ONESIDE_HALFBOTTOM"
    NONE = "NONE"


class StbCalFinishRcTypeColumn(StrEnum):
    """StbCalFinishRc.type_column で使用できる値。"""

    VALUE_4_SIDES = "4SIDES"
    VALUE_2_SIDES = "2SIDES"
    NONE = "NONE"


class StbCalFinishRcTypeBeam(StrEnum):
    """StbCalFinishRc.type_beam で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    BOTHSIDE_BOTTOM = "BOTHSIDE_BOTTOM"
    ONESIDE_HALFBOTTOM = "ONESIDE_HALFBOTTOM"
    NONE = "NONE"


class StbCalFinishRcTypeCanti(StrEnum):
    """StbCalFinishRc.type_canti で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    BOTHSIDE_BOTTOM = "BOTHSIDE_BOTTOM"
    ONESIDE_HALFBOTTOM = "ONESIDE_HALFBOTTOM"
    NONE = "NONE"


class StbCalFinishRcTypeWall(StrEnum):
    """StbCalFinishRc.type_wall で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    NONE = "NONE"


class StbCalFinishSMemberMemberType(StrEnum):
    """StbCalFinishSMember.member_type で使用できる値。"""

    COLUMN = "COLUMN"
    GIRDER = "GIRDER"
    BEAM = "BEAM"
    CANTI = "CANTI"
    BRACE = "BRACE"


class StbCalFinishSMemberCoveringType(StrEnum):
    """StbCalFinishSMember.covering_type で使用できる値。"""

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C = "C"
    D = "D"


class StbCalFloorFinishRcTypeGirder(StrEnum):
    """StbCalFloorFinishRc.type_girder で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    BOTHSIDE_BOTTOM = "BOTHSIDE_BOTTOM"
    ONESIDE_HALFBOTTOM = "ONESIDE_HALFBOTTOM"
    NONE = "NONE"


class StbCalFloorFinishRcTypeColumn(StrEnum):
    """StbCalFloorFinishRc.type_column で使用できる値。"""

    VALUE_4_SIDES = "4SIDES"
    VALUE_2_SIDES = "2SIDES"
    NONE = "NONE"


class StbCalFloorFinishRcTypeBeam(StrEnum):
    """StbCalFloorFinishRc.type_beam で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    BOTHSIDE_BOTTOM = "BOTHSIDE_BOTTOM"
    ONESIDE_HALFBOTTOM = "ONESIDE_HALFBOTTOM"
    NONE = "NONE"


class StbCalFloorFinishRcTypeCanti(StrEnum):
    """StbCalFloorFinishRc.type_canti で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    BOTHSIDE_BOTTOM = "BOTHSIDE_BOTTOM"
    ONESIDE_HALFBOTTOM = "ONESIDE_HALFBOTTOM"
    NONE = "NONE"


class StbCalFloorFinishRcTypeWall(StrEnum):
    """StbCalFloorFinishRc.type_wall で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    NONE = "NONE"


class StbCalFloorFinishSMemberMemberType(StrEnum):
    """StbCalFloorFinishSMember.member_type で使用できる値。"""

    COLUMN = "COLUMN"
    GIRDER = "GIRDER"
    BEAM = "BEAM"
    CANTI = "CANTI"
    BRACE = "BRACE"


class StbCalFloorFinishSMemberCoveringType(StrEnum):
    """StbCalFloorFinishSMember.covering_type で使用できる値。"""

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C = "C"
    D = "D"


class StbCalColumnFinishRcType(StrEnum):
    """StbCalColumnFinishRc.type で使用できる値。"""

    VALUE_4_SIDES = "4SIDES"
    VALUE_2_SIDES = "2SIDES"
    NONE = "NONE"


class StbCalGirderFinishRcType(StrEnum):
    """StbCalGirderFinishRc.type で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    BOTHSIDE_BOTTOM = "BOTHSIDE_BOTTOM"
    ONESIDE_HALFBOTTOM = "ONESIDE_HALFBOTTOM"
    NONE = "NONE"


class StbCalWallFinishRcType(StrEnum):
    """StbCalWallFinishRc.type で使用できる値。"""

    BOTHSIDE = "BOTHSIDE"
    ONESIDE = "ONESIDE"
    NONE = "NONE"


class StbCalColumnFinishSCoveringType(StrEnum):
    """StbCalColumnFinishS.covering_type で使用できる値。"""

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C = "C"
    D = "D"


class StbCalGirderFinishSCoveringType(StrEnum):
    """StbCalGirderFinishS.covering_type で使用できる値。"""

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C = "C"
    D = "D"


class StbCalBraceFinishSCoveringType(StrEnum):
    """StbCalBraceFinishS.covering_type で使用できる値。"""

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C = "C"
    D = "D"


class StbCalLoadCaseCategory(StrEnum):
    """StbCalLoadCase.category で使用できる値。"""

    STANDARD = "STANDARD"
    ANALYSIS = "ANALYSIS"


class StbCalLoadCaseKind(StrEnum):
    """StbCalLoadCase.kind で使用できる値。"""

    DEADLOAD = "DEADLOAD"
    LIVELOAD_FRAME = "LIVELOAD_FRAME"
    LIVELOAD_SEISMIC = "LIVELOAD_SEISMIC"
    TOTALLOAD = "TOTALLOAD"
    SNOWLOAD = "SNOWLOAD"
    SEISMICLOAD = "SEISMICLOAD"
    WINDLOAD = "WINDLOAD"
    OTHER = "OTHER"


class StbCalMemberLoadType(StrEnum):
    """StbCalMemberLoad.type で使用できる値。"""

    CONCENTRATED = "CONCENTRATED"
    MOMENT = "MOMENT"
    CONCENTRATED_BYNUMBER = "CONCENTRATED_BYNUMBER"
    DISTRIBUTED_UNIFORM = "DISTRIBUTED_UNIFORM"
    DISTRIBUTED_TRIANGLE = "DISTRIBUTED_TRIANGLE"
    DISTRIBUTED_ISOSCELESTRIANGLE = "DISTRIBUTED_ISOSCELESTRIANGLE"
    DISTRIBUTED_QUADRILATERAL1 = "DISTRIBUTED_QUADRILATERAL1"
    DISTRIBUTED_QUADRILATERAL2 = "DISTRIBUTED_QUADRILATERAL2"
    DISTRIBUTED_3_POINT_SPECIFY1 = "DISTRIBUTED_3POINT_SPECIFY1"
    DISTRIBUTED_3_POINT_SPECIFY2 = "DISTRIBUTED_3POINT_SPECIFY2"
    INPUT_CMQ = "INPUT_CMQ"
    TORTOISE_SHELL1 = "TORTOISE_SHELL1"
    TORTOISE_SHELL2 = "TORTOISE_SHELL2"
    TORTOISE_SHELL3 = "TORTOISE_SHELL3"
    TORTOISE_SHELL4 = "TORTOISE_SHELL4"


class StbCalMemberLoadDirectionLoad(StrEnum):
    """StbCalMemberLoad.direction_load で使用できる値。"""

    LOCAL = "LOCAL"
    GLOBAL = "GLOBAL"
    PROJECTION = "PROJECTION"


class StbCalMemberLoadCoordinateLoad(StrEnum):
    """StbCalMemberLoad.coordinate_load で使用できる値。"""

    X = "X"
    Y = "Y"


class StbCalAreaLoadType(StrEnum):
    """StbCalAreaLoad.type で使用できる値。"""

    UNIFORM = "UNIFORM"
    TOTALWEIGHT = "TOTALWEIGHT"


class StbCalAreaLoadCoordinateLoad(StrEnum):
    """StbCalAreaLoad.coordinate_load で使用できる値。"""

    LOCAL = "LOCAL"
    GLOBAL = "GLOBAL"
    PROJECTION = "PROJECTION"


class StbCalEarthHydrostaticPressureLoadCoordinateLoad(StrEnum):
    """StbCalEarthHydrostaticPressureLoad.coordinate_load で使用できる値。"""

    TYPE_PLUS = "TYPE_PLUS"
    TYPE_MINUS = "TYPE_MINUS"


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


class StbCalGirderConditionStartY(StrEnum):
    """StbCalGirderCondition.start_y で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalGirderConditionStartZ(StrEnum):
    """StbCalGirderCondition.start_z で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalGirderConditionEndY(StrEnum):
    """StbCalGirderCondition.end_y で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalGirderConditionEndZ(StrEnum):
    """StbCalGirderCondition.end_z で使用できる値。"""

    FIX = "FIX"
    PIN = "PIN"
    SPRING = "SPRING"


class StbCalNrbPropertyShape(StrEnum):
    """StbCalNrbProperty.shape で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbCalLrbPropertyShape(StrEnum):
    """StbCalLrbProperty.shape で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbCalEsbPropertyShape(StrEnum):
    """StbCalEsbProperty.shape で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbCalEsbPropertyShapeSlipmetal(StrEnum):
    """StbCalEsbProperty.shape_slipmetal で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbCalRsbPropertyShapeSlipmetal(StrEnum):
    """StbCalRsbProperty.shape_slipmetal で使用できる値。"""

    CIRCLE = "CIRCLE"
    SQUARE = "SQUARE"


class StbCalOilDampingDevicePropertyAttributeDamping(StrEnum):
    """StbCalOilDampingDeviceProperty.attribute_damping で使用できる値。"""

    LINEAR = "LINEAR"
    BILINEAR = "BILINEAR"
    TRILINEAR = "TRILINEAR"


class StbCalHistoryDampingDevicePropertyModelRestoring(StrEnum):
    """StbCalHistoryDampingDeviceProperty.model_restoring で使用できる値。"""

    NORMALBI = "NORMALBI"
    NORMALTRI = "NORMALTRI"
    MODEIFIED_RO = "MODEIFIED_RO"
    ISOTROPIC = "ISOTROPIC"


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


class StbAnaBeamRelMemberKind(StrEnum):
    """StbAnaBeamRel.member_kind で使用できる値。"""

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


class StbAnaBeamPropertyRelSectionKind(StrEnum):
    """StbAnaBeamPropertyRel.section_kind で使用できる値。"""

    STB_SEC_COLUMN_RC = "StbSecColumn_RC"
    STB_SEC_COLUMN_S = "StbSecColumn_S"
    STB_SEC_COLUMN_SRC = "StbSecColumn_SRC"
    STB_SEC_COLUMN_CFT = "StbSecColumn_CFT"
    STB_SEC_BEAM_RC = "StbSecBeam_RC"
    STB_SEC_BEAM_S = "StbSecBeam_S"
    STB_SEC_BEAM_SRC = "StbSecBeam_SRC"
    STB_SEC_BRACE_S = "StbSecBrace_S"


class StbAnaPlanePropertyRelSectionKind(StrEnum):
    """StbAnaPlanePropertyRel.section_kind で使用できる値。"""

    STB_SEC_SLAB_RC = "StbSecSlab_RC"
    STB_SEC_SLAB_DECK = "StbSecSlabDeck"
    STB_SEC_SLAB_PRECAST = "StbSecSlabPrecast"


class StbAnaPlanePropertyRel(StBridgeElement):
    """StbAnaPlanePropertyRel

    Attributes:
        id_ana_slab_property (int): 属性
        section_kind (StbAnaPlanePropertyRelSectionKind): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_slab_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_kind": _FI(
            py_type=StbAnaPlanePropertyRelSectionKind,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("StbSecSlab_RC", "StbSecSlabDeck", "StbSecSlabPrecast"),
        ),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaWallPropertyRel(StBridgeElement):
    """StbAnaWallPropertyRel

    Attributes:
        id_ana_wall_property (int): 属性
        section_kind (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_wall_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaTrussPropertyRel(StBridgeElement):
    """StbAnaTrussPropertyRel

    Attributes:
        id_ana_truss_property (int): 属性
        section_kind (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_truss_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaBeamPropertyRel(StBridgeElement):
    """StbAnaBeamPropertyRel

    Attributes:
        id_ana_beam_property (int): 属性
        section_kind (StbAnaBeamPropertyRelSectionKind): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_beam_property": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "section_kind": _FI(
            py_type=StbAnaBeamPropertyRelSectionKind,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "StbSecColumn_RC",
                "StbSecColumn_S",
                "StbSecColumn_SRC",
                "StbSecColumn_CFT",
                "StbSecBeam_RC",
                "StbSecBeam_S",
                "StbSecBeam_SRC",
                "StbSecBrace_S",
            ),
        ),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaCalMemberRel(StBridgeElement):
    """StbAnaCalMemberRel

    Attributes:
        id_ana_beam (int): 属性
        member_kind (StbAnaCalMemberRelMemberKind): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_beam": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(
            py_type=StbAnaCalMemberRelMemberKind,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("StbCalColumn", "StbCalGirder"),
        ),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaFloorDiaphragmRel(StBridgeElement):
    """StbAnaFloorDiaphragmRel

    Attributes:
        id_ana_floordiaphragm (int): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_floordiaphragm": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaNodePanelRel(StBridgeElement):
    """StbAnaNodePanelRel

    Attributes:
        id_ana_nodepanel (int): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_nodepanel": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaPlaneRectangleRel(StBridgeElement):
    """StbAnaPlaneRectangleRel

    Attributes:
        id_ana_slab (int): 属性
        member_kind (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_slab": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaPlaneTriangleRel(StBridgeElement):
    """StbAnaPlaneTriangleRel

    Attributes:
        id_ana_slab (int): 属性
        member_kind (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_slab": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaWallRel(StBridgeElement):
    """StbAnaWallRel

    Attributes:
        id_ana_wall (int): 属性
        member_kind (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_wall": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaSupportRel(StBridgeElement):
    """StbAnaSupportRel

    Attributes:
        id_ana_support (int): 属性
        member_kind (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_support": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaTrussRel(StBridgeElement):
    """StbAnaTrussRel

    Attributes:
        id_ana_truss (int): 属性
        member_kind (str): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_truss": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(py_type=str, data_type=_DT.STR, required=True),
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaBeamRel(StBridgeElement):
    """StbAnaBeamRel

    Attributes:
        id_ana_beam (int): 属性
        member_kind (StbAnaBeamRelMemberKind): 属性
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_ana_beam": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "member_kind": _FI(
            py_type=StbAnaBeamRelMemberKind,
            data_type=_DT.STR_ENUM,
            required=True,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbAnaRelations(StBridgeElement):
    """StbAnaRelations

    Attributes:
        stb_ana_node_rel (list[StbAnaNodeRel]): 子要素
        stb_ana_story_rel (list[StbAnaStoryRel]): 子要素
        stb_ana_beam_rel (list[StbAnaBeamRel]): 子要素
        stb_ana_truss_rel (list[StbAnaTrussRel]): 子要素
        stb_ana_support_rel (list[StbAnaSupportRel]): 子要素
        stb_ana_wall_rel (list[StbAnaWallRel]): 子要素
        stb_ana_plane_triangle_rel (list[StbAnaPlaneTriangleRel]): 子要素
        stb_ana_plane_rectangle_rel (list[StbAnaPlaneRectangleRel]): 子要素
        stb_ana_node_panel_rel (list[StbAnaNodePanelRel]): 子要素
        stb_ana_floor_diaphragm_rel (list[StbAnaFloorDiaphragmRel]): 子要素
        stb_ana_cal_member_rel (list[StbAnaCalMemberRel]): 子要素
        stb_ana_beam_property_rel (list[StbAnaBeamPropertyRel]): 子要素
        stb_ana_truss_property_rel (list[StbAnaTrussPropertyRel]): 子要素
        stb_ana_wall_property_rel (list[StbAnaWallPropertyRel]): 子要素
        stb_ana_plane_property_rel (list[StbAnaPlanePropertyRel]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_ana_node_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaNodeRel]),
        "stb_ana_story_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaStoryRel]),
        "stb_ana_beam_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaBeamRel]),
        "stb_ana_truss_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaTrussRel]),
        "stb_ana_support_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaSupportRel]),
        "stb_ana_wall_rel": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaWallRel]),
        "stb_ana_plane_triangle_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaPlaneTriangleRel]
        ),
        "stb_ana_plane_rectangle_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaPlaneRectangleRel]
        ),
        "stb_ana_node_panel_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaNodePanelRel]
        ),
        "stb_ana_floor_diaphragm_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaFloorDiaphragmRel]
        ),
        "stb_ana_cal_member_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaCalMemberRel]
        ),
        "stb_ana_beam_property_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaBeamPropertyRel]
        ),
        "stb_ana_truss_property_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaTrussPropertyRel]
        ),
        "stb_ana_wall_property_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaWallPropertyRel]
        ),
        "stb_ana_plane_property_rel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaPlanePropertyRel]
        ),
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


class StbAnaLoadNodePanelInitialStress(StBridgeElement):
    """StbAnaLoadNodePanelInitialStress

    Attributes:
        x_tau (float): 属性
        y_tau (float): 属性
        z_tau (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "x_tau": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="X_tau"),
        "y_tau": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Y_tau"),
        "z_tau": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="Z_tau"),
    }


class StbAnaLoadNodePanel(StBridgeElement):
    """StbAnaLoadNodePanel

    Attributes:
        id_member (int): 属性
        stb_ana_load_node_panel_initial_stress (list[StbAnaLoadNodePanelInitialStress]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_ana_load_node_panel_initial_stress": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaLoadNodePanelInitialStress]
        ),
    }


class StbAnaLoadSupportInitialStress(StBridgeElement):
    """StbAnaLoadSupportInitialStress

    Attributes:
        force (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "force": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbAnaLoadSupport(StBridgeElement):
    """StbAnaLoadSupport

    Attributes:
        id_member (int): 属性
        stb_ana_load_support_initial_stress (list[StbAnaLoadSupportInitialStress]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_ana_load_support_initial_stress": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaLoadSupportInitialStress]
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
        stb_ana_load_support (list[StbAnaLoadSupport]): 子要素
        stb_ana_load_node_panel (list[StbAnaLoadNodePanel]): 子要素
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
        "stb_ana_load_support": _FI(kind=_FK.ELEMENT, py_type=list[StbAnaLoadSupport]),
        "stb_ana_load_node_panel": _FI(
            kind=_FK.ELEMENT, py_type=list[StbAnaLoadNodePanel]
        ),
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


class StbAnaNodeidList(StBridgeElement):
    """StbAnaNodeidList

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
        stb_ana_nodeid_list (StbAnaNodeidList): 子要素
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
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbAnaNodeidList
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
        "b_x": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="B_x"
        ),
        "b_y": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="B_y"
        ),
        "b_z": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="B_z"
        ),
        "t_x": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "t_y": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "t_z": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "d_x": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_x"
        ),
        "d_y": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_y"
        ),
        "d_z": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D_z"
        ),
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
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
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
            required=True,
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


class StbAnaMemberidList(StBridgeElement):
    """StbAnaMemberidList

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
        represent_height (float): 属性
        id_node_lower (int): 属性
        id_node_upper (int): 属性
        drift_angle_height (float): 属性
        sum_weight (float): 属性
        stb_ana_memberid_list (StbAnaMemberidList): 子要素
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
        "represent_height": _FI(py_type=float, data_type=_DT.FLOAT),
        "id_node_lower": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "id_node_upper": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "drift_angle_height": _FI(py_type=float, data_type=_DT.FLOAT),
        "sum_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "stb_ana_memberid_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbAnaMemberidList
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
        name (str): 属性
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
        "name": _FI(py_type=str, data_type=_DT.STR),
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


class StbCalDampingDevicePropertyRatioMemFrameList(StBridgeElement):
    """StbCalDampingDevicePropertyRatioMemFrameList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalDampingDevicePropertyRatioMemList(StBridgeElement):
    """StbCalDampingDevicePropertyRatioMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalDampingDevicePropertyRatioList(StBridgeElement):
    """StbCalDampingDevicePropertyRatioList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalDampingDevicePropertyRatioArr(StBridgeElement):
    """StbCalDampingDevicePropertyRatioArr

    Attributes:
        stb_cal_damping_device_property_ratio_list (StbCalDampingDevicePropertyRatioList): 子要素
        stb_cal_damping_device_property_ratio_mem_list (StbCalDampingDevicePropertyRatioMemList): 子要素
        stb_cal_damping_device_property_ratio_mem_frame_list (StbCalDampingDevicePropertyRatioMemFrameList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_damping_device_property_ratio_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalDampingDevicePropertyRatioList,
        ),
        "stb_cal_damping_device_property_ratio_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalDampingDevicePropertyRatioMemList,
        ),
        "stb_cal_damping_device_property_ratio_mem_frame_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalDampingDevicePropertyRatioMemFrameList,
        ),
    }


class StbCalDampingDevicePropertySecList(StBridgeElement):
    """StbCalDampingDevicePropertySecList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalDampingDevicePropertyList(StBridgeElement):
    """StbCalDampingDevicePropertyList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalDampingDevicePropertyArr(StBridgeElement):
    """StbCalDampingDevicePropertyArr

    Attributes:
        stb_cal_damping_device_property_list (StbCalDampingDevicePropertyList): 子要素
        stb_cal_damping_device_property_sec_list (StbCalDampingDevicePropertySecList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_damping_device_property_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalDampingDevicePropertyList,
        ),
        "stb_cal_damping_device_property_sec_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalDampingDevicePropertySecList,
        ),
    }


class StbCalIsolatingDevicePropertyRatioMemList(StBridgeElement):
    """StbCalIsolatingDevicePropertyRatioMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalIsolatingDevicePropertyRatioList(StBridgeElement):
    """StbCalIsolatingDevicePropertyRatioList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalIsolatingDevicePropertyRatioArr(StBridgeElement):
    """StbCalIsolatingDevicePropertyRatioArr

    Attributes:
        stb_cal_isolating_device_property_ratio_list (StbCalIsolatingDevicePropertyRatioList): 子要素
        stb_cal_isolating_device_property_ratio_mem_list (StbCalIsolatingDevicePropertyRatioMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_isolating_device_property_ratio_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalIsolatingDevicePropertyRatioList,
        ),
        "stb_cal_isolating_device_property_ratio_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalIsolatingDevicePropertyRatioMemList,
        ),
    }


class StbCalIsolatingDevicePropertySecList(StBridgeElement):
    """StbCalIsolatingDevicePropertySecList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalIsolatingDevicePropertyList(StBridgeElement):
    """StbCalIsolatingDevicePropertyList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalIsolatingDevicePropertyArr(StBridgeElement):
    """StbCalIsolatingDevicePropertyArr

    Attributes:
        stb_cal_isolating_device_property_list (StbCalIsolatingDevicePropertyList): 子要素
        stb_cal_isolating_device_property_sec_list (StbCalIsolatingDevicePropertySecList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_isolating_device_property_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalIsolatingDevicePropertyList,
        ),
        "stb_cal_isolating_device_property_sec_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalIsolatingDevicePropertySecList,
        ),
    }


class StbCalWallSecPropertyRcList(StBridgeElement):
    """StbCalWallSecPropertyRcList：StbCalWallSecProperty_RC_List

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
        stb_cal_isolating_device_property_arr (list[StbCalIsolatingDevicePropertyArr]): 子要素
        stb_cal_isolating_device_property_ratio_arr (list[StbCalIsolatingDevicePropertyRatioArr]): 子要素
        stb_cal_damping_device_property_arr (list[StbCalDampingDevicePropertyArr]): 子要素
        stb_cal_damping_device_property_ratio_arr (list[StbCalDampingDevicePropertyRatioArr]): 子要素
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
        "stb_cal_isolating_device_property_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalIsolatingDevicePropertyArr]
        ),
        "stb_cal_isolating_device_property_ratio_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalIsolatingDevicePropertyRatioArr]
        ),
        "stb_cal_damping_device_property_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalDampingDevicePropertyArr]
        ),
        "stb_cal_damping_device_property_ratio_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalDampingDevicePropertyRatioArr]
        ),
    }


class StbCalNodePointLoadNodeList(StBridgeElement):
    """StbCalNodePointLoadNodeList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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


class StbCalBraceFinishValueMemList(StBridgeElement):
    """StbCalBraceFinishValueMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalBraceFinishValueLoadList(StBridgeElement):
    """StbCalBraceFinishValueLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalBraceFinishValueArr(StBridgeElement):
    """StbCalBraceFinishValueArr

    Attributes:
        stb_cal_brace_finish_value_load_list (StbCalBraceFinishValueLoadList): 子要素
        stb_cal_brace_finish_value_mem_list (StbCalBraceFinishValueMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_brace_finish_value_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceFinishValueLoadList,
        ),
        "stb_cal_brace_finish_value_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBraceFinishValueMemList,
        ),
    }


class StbCalBraceFinishSMemList(StBridgeElement):
    """StbCalBraceFinishSMemList：StbCalBraceFinish_S_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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


class StbCalBeamFinishValueMemList(StBridgeElement):
    """StbCalBeamFinishValueMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalBeamFinishValueLoadList(StBridgeElement):
    """StbCalBeamFinishValueLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalBeamFinishValueArr(StBridgeElement):
    """StbCalBeamFinishValueArr

    Attributes:
        stb_cal_beam_finish_value_load_list (StbCalBeamFinishValueLoadList): 子要素
        stb_cal_beam_finish_value_mem_list (StbCalBeamFinishValueMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_beam_finish_value_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamFinishValueLoadList,
        ),
        "stb_cal_beam_finish_value_mem_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalBeamFinishValueMemList,
        ),
    }


class StbCalBeamFinishSMemList(StBridgeElement):
    """StbCalBeamFinishSMemList：StbCalBeamFinish_S_MemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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


class StbCalGirderFinishValueCalMemList(StBridgeElement):
    """StbCalGirderFinishValueCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalGirderFinishValueMemList(StBridgeElement):
    """StbCalGirderFinishValueMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalGirderFinishValueLoadList(StBridgeElement):
    """StbCalGirderFinishValueLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalGirderFinishValueArr(StBridgeElement):
    """StbCalGirderFinishValueArr

    Attributes:
        stb_cal_girder_finish_value_load_list (StbCalGirderFinishValueLoadList): 子要素
        stb_cal_girder_finish_value_mem_list (StbCalGirderFinishValueMemList): 子要素
        stb_cal_girder_finish_value_cal_mem_list (StbCalGirderFinishValueCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_girder_finish_value_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalGirderFinishValueLoadList,
        ),
        "stb_cal_girder_finish_value_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderFinishValueMemList
        ),
        "stb_cal_girder_finish_value_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalGirderFinishValueCalMemList
        ),
    }


class StbCalGirderFinishSCalMemList(StBridgeElement):
    """StbCalGirderFinishSCalMemList：StbCalGirderFinish_S_CalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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


class StbCalColumnFinishValueCalMemList(StBridgeElement):
    """StbCalColumnFinishValueCalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalColumnFinishValueMemList(StBridgeElement):
    """StbCalColumnFinishValueMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalColumnFinishValueLoadList(StBridgeElement):
    """StbCalColumnFinishValueLoadList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
            py_type=list[int],
        ),
    }


class StbCalColumnFinishValueArr(StBridgeElement):
    """StbCalColumnFinishValueArr

    Attributes:
        stb_cal_column_finish_value_load_list (StbCalColumnFinishValueLoadList): 子要素
        stb_cal_column_finish_value_mem_list (StbCalColumnFinishValueMemList): 子要素
        stb_cal_column_finish_value_cal_mem_list (StbCalColumnFinishValueCalMemList): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_finish_value_load_list": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbCalColumnFinishValueLoadList,
        ),
        "stb_cal_column_finish_value_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnFinishValueMemList
        ),
        "stb_cal_column_finish_value_cal_mem_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalColumnFinishValueCalMemList
        ),
    }


class StbCalColumnFinishSCalMemList(StBridgeElement):
    """StbCalColumnFinishSCalMemList：StbCalColumnFinish_S_CalMemList

    Attributes:
        content (list[int]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
        stb_cal_column_finish_value_arr (list[StbCalColumnFinishValueArr]): 子要素
        stb_cal_column_member_load_arr (list[StbCalColumnMemberLoadArr]): 子要素
        stb_cal_girder_finish_rc_arr (list[StbCalGirderFinishRcArr]): 子要素
        stb_cal_girder_finish_s_arr (list[StbCalGirderFinishSArr]): 子要素
        stb_cal_girder_finish_value_arr (list[StbCalGirderFinishValueArr]): 子要素
        stb_cal_girder_member_load_arr (list[StbCalGirderMemberLoadArr]): 子要素
        stb_cal_beam_finish_rc_arr (list[StbCalBeamFinishRcArr]): 子要素
        stb_cal_beam_finish_s_arr (list[StbCalBeamFinishSArr]): 子要素
        stb_cal_beam_finish_value_arr (list[StbCalBeamFinishValueArr]): 子要素
        stb_cal_beam_member_load_arr (list[StbCalBeamMemberLoadArr]): 子要素
        stb_cal_brace_finish_s_arr (list[StbCalBraceFinishSArr]): 子要素
        stb_cal_brace_finish_value_arr (list[StbCalBraceFinishValueArr]): 子要素
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
        "stb_cal_column_finish_value_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnFinishValueArr]
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
        "stb_cal_girder_finish_value_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderFinishValueArr]
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
        "stb_cal_beam_finish_value_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBeamFinishValueArr]
        ),
        "stb_cal_beam_member_load_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBeamMemberLoadArr]
        ),
        "stb_cal_brace_finish_s_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceFinishSArr]
        ),
        "stb_cal_brace_finish_value_arr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceFinishValueArr]
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
        "g": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="G"),
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


class StbCalDampingDevicePropertyRatio(StBridgeElement):
    """StbCalDampingDevicePropertyRatio

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        ratio_stiffness (float): 属性
        ratio_damping_coefficient (float): 属性
        ratio_yield_strength (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "ratio_stiffness": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_damping_coefficient": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_yield_strength": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalIsolatingDevicePropertyRatio(StBridgeElement):
    """StbCalIsolatingDevicePropertyRatio

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        ratio_stiffness (float): 属性
        ratio_damping_coefficient (float): 属性
        ratio_friction_coefficient (float): 属性
        ratio_yield_strength (float): 属性
        ratio_stiffness_damping (float): 属性
        ratio_yield_strength_damping (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "ratio_stiffness": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_damping_coefficient": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_friction_coefficient": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_yield_strength": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_stiffness_damping": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_yield_strength_damping": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalDevicePropertyRatios(StBridgeElement):
    """StbCalDevicePropertyRatios

    Attributes:
        stb_cal_isolating_device_property_ratio (list[StbCalIsolatingDevicePropertyRatio]): 子要素
        stb_cal_damping_device_property_ratio (list[StbCalDampingDevicePropertyRatio]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_isolating_device_property_ratio": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalIsolatingDevicePropertyRatio]
        ),
        "stb_cal_damping_device_property_ratio": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalDampingDevicePropertyRatio]
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
        ratio_axial (float): 属性
        ratio_torsion (float): 属性
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
        "ratio_axial": _FI(py_type=float, data_type=_DT.FLOAT),
        "ratio_torsion": _FI(py_type=float, data_type=_DT.FLOAT),
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
        ratio_torsion (float): 属性
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
        "ratio_torsion": _FI(py_type=float, data_type=_DT.FLOAT),
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


class StbCalMassDampingDeviceProperty(StBridgeElement):
    """StbCalMassDampingDeviceProperty

    Attributes:
        type_specification (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_specification": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbCalFrictionDampingDeviceProperty(StBridgeElement):
    """StbCalFrictionDampingDeviceProperty

    Attributes:
        stiffness (float): 属性
        load_friction (float): 属性
        gradient (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stiffness": _FI(py_type=float, data_type=_DT.FLOAT),
        "load_friction": _FI(py_type=float, data_type=_DT.FLOAT),
        "gradient": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalHistoryDampingDeviceProperty(StBridgeElement):
    """StbCalHistoryDampingDeviceProperty

    Attributes:
        type_specification (str): 属性
        model_restoring (StbCalHistoryDampingDevicePropertyModelRestoring): 属性
        strength (str): 属性
        stiffness (float): 属性
        strength_yield (float): 属性
        gradient (float): 属性
        strength_final (float): 属性
        gradient_final (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_specification": _FI(py_type=str, data_type=_DT.STR, required=True),
        "model_restoring": _FI(
            py_type=StbCalHistoryDampingDevicePropertyModelRestoring,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("NORMALBI", "NORMALTRI", "MODEIFIED_RO", "ISOTROPIC"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stiffness": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "strength_yield": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "gradient": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "strength_final": _FI(py_type=float, data_type=_DT.FLOAT),
        "gradient_final": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalViscoelasticDampingDeviceProperty(StBridgeElement):
    """StbCalViscoelasticDampingDeviceProperty

    Attributes:
        type_specification (str): 属性
        area (float): 属性
        d (float): 属性
        temperature (float): 属性
        frequency (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_specification": _FI(py_type=str, data_type=_DT.STR, required=True),
        "area": _FI(py_type=float, data_type=_DT.FLOAT),
        "d": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "temperature": _FI(py_type=float, data_type=_DT.FLOAT),
        "frequency": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbCalViscousDampingDeviceProperty(StBridgeElement):
    """StbCalViscousDampingDeviceProperty

    Attributes:
        type_specification (str): 属性
        coefficient_damping (float): 属性
        exponential_damping (float): 属性
        velocity_linear (float): 属性
        area (float): 属性
        d (float): 属性
        temperature (float): 属性
        length_stroke (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_specification": _FI(py_type=str, data_type=_DT.STR, required=True),
        "coefficient_damping": _FI(py_type=float, data_type=_DT.FLOAT),
        "exponential_damping": _FI(py_type=float, data_type=_DT.FLOAT),
        "velocity_linear": _FI(py_type=float, data_type=_DT.FLOAT),
        "area": _FI(py_type=float, data_type=_DT.FLOAT),
        "d": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "temperature": _FI(py_type=float, data_type=_DT.FLOAT),
        "length_stroke": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbCalOilDampingDeviceProperty(StBridgeElement):
    """StbCalOilDampingDeviceProperty

    Attributes:
        type_specification (str): 属性
        attribute_damping (StbCalOilDampingDevicePropertyAttributeDamping): 属性
        coefficient_damping (float): 属性
        is_relief (bool): 属性
        load_relief (float): 属性
        gradient_final (float): 属性
        load_first_relief (float): 属性
        gradient_second (float): 属性
        length_stroke (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_specification": _FI(py_type=str, data_type=_DT.STR, required=True),
        "attribute_damping": _FI(
            py_type=StbCalOilDampingDevicePropertyAttributeDamping,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("LINEAR", "BILINEAR", "TRILINEAR"),
        ),
        "coefficient_damping": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "is_relief": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isRelief"
        ),
        "load_relief": _FI(py_type=float, data_type=_DT.FLOAT),
        "gradient_final": _FI(py_type=float, data_type=_DT.FLOAT),
        "load_first_relief": _FI(py_type=float, data_type=_DT.FLOAT),
        "gradient_second": _FI(py_type=float, data_type=_DT.FLOAT),
        "length_stroke": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbCalDampingDeviceProperty(StBridgeElement):
    """StbCalDampingDeviceProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        weight (float): 属性
        unit_weight (float): 属性
        stiffness_series_spring_device (float): 属性
        stiffness_series_spring_connect (float): 属性
        deformation_limit (float): 属性
        velocity_limit (float): 属性
        stb_cal_oil_damping_device_property (StbCalOilDampingDeviceProperty): 子要素
        stb_cal_viscous_damping_device_property (StbCalViscousDampingDeviceProperty): 子要素
        stb_cal_viscoelastic_damping_device_property (StbCalViscoelasticDampingDeviceProperty): 子要素
        stb_cal_history_damping_device_property (StbCalHistoryDampingDeviceProperty): 子要素
        stb_cal_friction_damping_device_property (StbCalFrictionDampingDeviceProperty): 子要素
        stb_cal_mass_damping_device_property (StbCalMassDampingDeviceProperty): 子要素
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
        "weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "stiffness_series_spring_device": _FI(py_type=float, data_type=_DT.FLOAT),
        "stiffness_series_spring_connect": _FI(py_type=float, data_type=_DT.FLOAT),
        "deformation_limit": _FI(py_type=float, data_type=_DT.FLOAT),
        "velocity_limit": _FI(py_type=float, data_type=_DT.FLOAT),
        "stb_cal_oil_damping_device_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalOilDampingDeviceProperty
        ),
        "stb_cal_viscous_damping_device_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalViscousDampingDeviceProperty
        ),
        "stb_cal_viscoelastic_damping_device_property": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbCalViscoelasticDampingDeviceProperty,
        ),
        "stb_cal_history_damping_device_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalHistoryDampingDeviceProperty
        ),
        "stb_cal_friction_damping_device_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalFrictionDampingDeviceProperty
        ),
        "stb_cal_mass_damping_device_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMassDampingDeviceProperty
        ),
    }


class StbCalClbProperty(StBridgeElement):
    """StbCalClbProperty：StbCalCLBProperty

    Attributes:
        length_rail (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "length_rail": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalCLBProperty"


class StbCalCslbProperty(StBridgeElement):
    """StbCalCslbProperty：StbCalCSLBProperty

    Attributes:
        length_rail (float): 属性
        friction_coefficient (float): 属性
        friction_specification (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "length_rail": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "friction_coefficient": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "friction_specification": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbCalCSLBProperty"


class StbCalCsbProperty(StBridgeElement):
    """StbCalCsbProperty：StbCalCSBProperty

    Attributes:
        friction_coefficient (float): 属性
        friction_specification (str): 属性
        diameter_slipmetal (float): 属性
        spherical_radius_slipmetal (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "friction_coefficient": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "friction_specification": _FI(py_type=str, data_type=_DT.STR),
        "diameter_slipmetal": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "spherical_radius_slipmetal": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbCalCSBProperty"


class StbCalRsbProperty(StBridgeElement):
    """StbCalRsbProperty：StbCalRSBProperty

    Attributes:
        friction_coefficient (float): 属性
        friction_specification (str): 属性
        area_slipmetal (float): 属性
        shape_slipmetal (StbCalRsbPropertyShapeSlipmetal): 属性
        diameter_slipmetal (float): 属性
        length_slipmetal (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "friction_coefficient": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "friction_specification": _FI(py_type=str, data_type=_DT.STR),
        "area_slipmetal": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "shape_slipmetal": _FI(
            py_type=StbCalRsbPropertyShapeSlipmetal,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "diameter_slipmetal": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "length_slipmetal": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbCalRSBProperty"


class StbCalEsbProperty(StBridgeElement):
    """StbCalEsbProperty：StbCalESBProperty

    Attributes:
        area (float): 属性
        shape (StbCalEsbPropertyShape): 属性
        diameter_outer (float): 属性
        chamfer (float): 属性
        diameter_inner (float): 属性
        g (float): 属性
        thickness (float): 属性
        thickness_one (float): 属性
        number_laminate (int): 属性
        s1 (float): 属性
        s2 (float): 属性
        pressure_reference (float): 属性
        stiffness_tensile (float): 属性
        strength_limit_tensile (float): 属性
        friction_coefficient (float): 属性
        friction_specification (str): 属性
        area_slipmetal (float): 属性
        shape_slipmetal (StbCalEsbPropertyShapeSlipmetal): 属性
        diameter_slipmetal (float): 属性
        length_slipmetal (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "area": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "shape": _FI(
            py_type=StbCalEsbPropertyShape,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "diameter_outer": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "chamfer": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "diameter_inner": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="G"),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "thickness_one": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "number_laminate": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "s1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S1"),
        "s2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S2"),
        "pressure_reference": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stiffness_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "strength_limit_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "friction_coefficient": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "friction_specification": _FI(py_type=str, data_type=_DT.STR),
        "area_slipmetal": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "shape_slipmetal": _FI(
            py_type=StbCalEsbPropertyShapeSlipmetal,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "diameter_slipmetal": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "length_slipmetal": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbCalESBProperty"


class StbCalSdrbProperty(StBridgeElement):
    """StbCalSdrbProperty：StbCalSDRBProperty

    Attributes:
        area (float): 属性
        diameter_outer (float): 属性
        diameter_inner (float): 属性
        g (float): 属性
        thickness (float): 属性
        thickness_one (float): 属性
        number_laminate (int): 属性
        s1 (float): 属性
        s2 (float): 属性
        pressure_reference (float): 属性
        stiffness_tensile (float): 属性
        strength_limit_tensile (float): 属性
        strength (str): 属性
        stiffness_damper (float): 属性
        strength_yield_damper (float): 属性
        gradient_damper (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "area": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "diameter_outer": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "diameter_inner": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="G"),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "thickness_one": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "number_laminate": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "s1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S1"),
        "s2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S2"),
        "pressure_reference": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stiffness_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "strength_limit_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stiffness_damper": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "strength_yield_damper": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "gradient_damper": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbCalSDRBProperty"


class StbCalTrbProperty(StBridgeElement):
    """StbCalTrbProperty：StbCalTRBProperty

    Attributes:
        type_performance (str): 属性
        area (float): 属性
        diameter_outer (float): 属性
        diameter_inner (float): 属性
        g (float): 属性
        thickness (float): 属性
        thickness_one (float): 属性
        number_laminate (int): 属性
        s1 (float): 属性
        s2 (float): 属性
        tin_plug_area (float): 属性
        tin_plug_area_one_piece (float): 属性
        tin_plug_number (int): 属性
        pressure_reference (float): 属性
        stiffness_tensile (float): 属性
        strength_limit_tensile (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_performance": _FI(py_type=str, data_type=_DT.STR, required=True),
        "area": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "diameter_outer": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "diameter_inner": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="G"),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "thickness_one": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "number_laminate": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "s1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S1"),
        "s2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S2"),
        "tin_plug_area": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "tin_plug_area_one_piece": _FI(py_type=float, data_type=_DT.FLOAT),
        "tin_plug_number": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "pressure_reference": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stiffness_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "strength_limit_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalTRBProperty"


class StbCalLrbProperty(StBridgeElement):
    """StbCalLrbProperty：StbCalLRBProperty

    Attributes:
        type_performance (str): 属性
        area (float): 属性
        shape (StbCalLrbPropertyShape): 属性
        diameter_outer (float): 属性
        chamfer (float): 属性
        diameter_inner (float): 属性
        g (float): 属性
        thickness (float): 属性
        thickness_one (float): 属性
        number_laminate (int): 属性
        s1 (float): 属性
        s2 (float): 属性
        area_plug (float): 属性
        area_plug_one (float): 属性
        number_plug (int): 属性
        pressure_reference (float): 属性
        stiffness_tensile (float): 属性
        strength_limit_tensile (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_performance": _FI(py_type=str, data_type=_DT.STR, required=True),
        "area": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "shape": _FI(
            py_type=StbCalLrbPropertyShape,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "diameter_outer": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "chamfer": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "diameter_inner": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="G"),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "thickness_one": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "number_laminate": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "s1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S1"),
        "s2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S2"),
        "area_plug": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "area_plug_one": _FI(py_type=float, data_type=_DT.FLOAT),
        "number_plug": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "pressure_reference": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stiffness_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "strength_limit_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalLRBProperty"


class StbCalHdrProperty(StBridgeElement):
    """StbCalHdrProperty：StbCalHDRProperty

    Attributes:
        type_performance (str): 属性
        area (float): 属性
        diameter_outer (float): 属性
        diameter_inner (float): 属性
        g (float): 属性
        thickness (float): 属性
        thickness_one (float): 属性
        number_laminate (int): 属性
        s1 (float): 属性
        s2 (float): 属性
        pressure_reference (float): 属性
        stiffness_tensile (float): 属性
        strength_limit_tensile (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "type_performance": _FI(py_type=str, data_type=_DT.STR, required=True),
        "area": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "diameter_outer": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "diameter_inner": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="G"),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "thickness_one": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "number_laminate": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "s1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S1"),
        "s2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S2"),
        "pressure_reference": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stiffness_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "strength_limit_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalHDRProperty"


class StbCalNrbProperty(StBridgeElement):
    """StbCalNrbProperty：StbCalNRBProperty

    Attributes:
        area (float): 属性
        shape (StbCalNrbPropertyShape): 属性
        diameter_outer (float): 属性
        chamfer (float): 属性
        diameter_inner (float): 属性
        g (float): 属性
        thickness (float): 属性
        thickness_one (float): 属性
        number_laminate (int): 属性
        s1 (float): 属性
        s2 (float): 属性
        pressure_reference (float): 属性
        stiffness_tensile (float): 属性
        strength_limit_tensile (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "area": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "shape": _FI(
            py_type=StbCalNrbPropertyShape,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "diameter_outer": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "chamfer": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "diameter_inner": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "g": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="G"),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "thickness_one": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "number_laminate": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "s1": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S1"),
        "s2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="S2"),
        "pressure_reference": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stiffness_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
        "strength_limit_tensile": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalNRBProperty"


class StbCalIsolatingDeviceProperty(StBridgeElement):
    """StbCalIsolatingDeviceProperty

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        weight (float): 属性
        stiffness_vertical (float): 属性
        limit_deformation (float): 属性
        stiffness_equivalent (float): 属性
        stiffness_1st (float): 属性
        stiffness_2nd (float): 属性
        intercept_load (float): 属性
        stb_cal_nrb_property (StbCalNrbProperty): 子要素
        stb_cal_hdr_property (StbCalHdrProperty): 子要素
        stb_cal_lrb_property (StbCalLrbProperty): 子要素
        stb_cal_trb_property (StbCalTrbProperty): 子要素
        stb_cal_sdrb_property (StbCalSdrbProperty): 子要素
        stb_cal_esb_property (StbCalEsbProperty): 子要素
        stb_cal_rsb_property (StbCalRsbProperty): 子要素
        stb_cal_csb_property (StbCalCsbProperty): 子要素
        stb_cal_cslb_property (StbCalCslbProperty): 子要素
        stb_cal_clb_property (StbCalClbProperty): 子要素
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
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
        "stiffness_vertical": _FI(py_type=float, data_type=_DT.FLOAT),
        "limit_deformation": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stiffness_equivalent": _FI(py_type=float, data_type=_DT.FLOAT),
        "stiffness_1st": _FI(py_type=float, data_type=_DT.FLOAT),
        "stiffness_2nd": _FI(py_type=float, data_type=_DT.FLOAT),
        "intercept_load": _FI(py_type=float, data_type=_DT.FLOAT),
        "stb_cal_nrb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalNrbProperty
        ),
        "stb_cal_hdr_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalHdrProperty
        ),
        "stb_cal_lrb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalLrbProperty
        ),
        "stb_cal_trb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalTrbProperty
        ),
        "stb_cal_sdrb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalSdrbProperty
        ),
        "stb_cal_esb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalEsbProperty
        ),
        "stb_cal_rsb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalRsbProperty
        ),
        "stb_cal_csb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalCsbProperty
        ),
        "stb_cal_cslb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalCslbProperty
        ),
        "stb_cal_clb_property": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalClbProperty
        ),
    }


class StbCalDeviceProperties(StBridgeElement):
    """StbCalDeviceProperties

    Attributes:
        stb_cal_isolating_device_property (list[StbCalIsolatingDeviceProperty]): 子要素
        stb_cal_damping_device_property (list[StbCalDampingDeviceProperty]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_isolating_device_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalIsolatingDeviceProperty]
        ),
        "stb_cal_damping_device_property": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalDampingDeviceProperty]
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
        start_y (float): 属性
        start_z (float): 属性
        end_y (float): 属性
        end_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "start_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Y"),
        "start_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Z"),
        "end_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Y"),
        "end_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Z"),
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
        start_y (float): 属性
        start_z (float): 属性
        end_y (float): 属性
        end_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "start_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Y"),
        "start_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="start_Z"),
        "end_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Y"),
        "end_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="end_Z"),
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
        start_y (StbCalGirderConditionStartY): 属性
        start_z (StbCalGirderConditionStartZ): 属性
        end_y (StbCalGirderConditionEndY): 属性
        end_z (StbCalGirderConditionEndZ): 属性
        start_spring_y (float): 属性
        start_spring_z (float): 属性
        end_spring_y (float): 属性
        end_spring_z (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "start_y": _FI(
            py_type=StbCalGirderConditionStartY,
            data_type=_DT.STR_ENUM,
            xml_name="start_Y",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "start_z": _FI(
            py_type=StbCalGirderConditionStartZ,
            data_type=_DT.STR_ENUM,
            xml_name="start_Z",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "end_y": _FI(
            py_type=StbCalGirderConditionEndY,
            data_type=_DT.STR_ENUM,
            xml_name="end_Y",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "end_z": _FI(
            py_type=StbCalGirderConditionEndZ,
            data_type=_DT.STR_ENUM,
            xml_name="end_Z",
            choices=("FIX", "PIN", "SPRING"),
        ),
        "start_spring_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="start_spring_Y"
        ),
        "start_spring_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="start_spring_Z"
        ),
        "end_spring_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="end_spring_Y"
        ),
        "end_spring_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="end_spring_Z"
        ),
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
        stb_cal_device_properties (StbCalDeviceProperties): 子要素
        stb_cal_member_stiffnesses (StbCalMemberStiffnesses): 子要素
        stb_cal_device_property_ratios (StbCalDevicePropertyRatios): 子要素
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
        "stb_cal_device_properties": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalDeviceProperties
        ),
        "stb_cal_member_stiffnesses": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberStiffnesses
        ),
        "stb_cal_device_property_ratios": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalDevicePropertyRatios
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
        alpha (float): 属性
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
        "alpha": _FI(py_type=float, data_type=_DT.FLOAT),
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
            choices=("TYPE_PLUS", "TYPE_MINUS"),
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
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("UNIFORM", "TOTALWEIGHT"),
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
        type (StbCalMemberLoadType): 属性
        p1 (float): 属性
        p2 (float): 属性
        p3 (float): 属性
        p4 (float): 属性
        p5 (float): 属性
        p6 (float): 属性
        direction_load (StbCalMemberLoadDirectionLoad): 属性
        coordinate_load (StbCalMemberLoadCoordinateLoad): 属性
        is_addnode (bool): 属性
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
            py_type=StbCalMemberLoadType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "CONCENTRATED",
                "MOMENT",
                "CONCENTRATED_BYNUMBER",
                "DISTRIBUTED_UNIFORM",
                "DISTRIBUTED_TRIANGLE",
                "DISTRIBUTED_ISOSCELESTRIANGLE",
                "DISTRIBUTED_QUADRILATERAL1",
                "DISTRIBUTED_QUADRILATERAL2",
                "DISTRIBUTED_3POINT_SPECIFY1",
                "DISTRIBUTED_3POINT_SPECIFY2",
                "INPUT_CMQ",
                "TORTOISE_SHELL1",
                "TORTOISE_SHELL2",
                "TORTOISE_SHELL3",
                "TORTOISE_SHELL4",
            ),
        ),
        "p1": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="P1"),
        "p2": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P2"),
        "p3": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P3"),
        "p4": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P4"),
        "p5": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P5"),
        "p6": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="P6"),
        "direction_load": _FI(
            py_type=StbCalMemberLoadDirectionLoad,
            data_type=_DT.STR_ENUM,
            choices=("LOCAL", "GLOBAL", "PROJECTION"),
        ),
        "coordinate_load": _FI(
            py_type=StbCalMemberLoadCoordinateLoad,
            data_type=_DT.STR_ENUM,
            choices=("X", "Y"),
        ),
        "is_addnode": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isAddnode"),
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
            choices=(
                "DEADLOAD",
                "LIVELOAD_FRAME",
                "LIVELOAD_SEISMIC",
                "TOTALLOAD",
                "SNOWLOAD",
                "SEISMICLOAD",
                "WINDLOAD",
                "OTHER",
            ),
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


class StbCalBraceFinishValue(StBridgeElement):
    """StbCalBraceFinishValue

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
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbCalGirderFinishValue(StBridgeElement):
    """StbCalGirderFinishValue

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
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbCalColumnFinishValue(StBridgeElement):
    """StbCalColumnFinishValue

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
        "weight": _FI(py_type=float, data_type=_DT.FLOAT, required=True),
    }


class StbCalMemberFinishValues(StBridgeElement):
    """StbCalMemberFinishValues

    Attributes:
        stb_cal_column_finish_value (list[StbCalColumnFinishValue]): 子要素
        stb_cal_girder_finish_value (list[StbCalGirderFinishValue]): 子要素
        stb_cal_brace_finish_value (list[StbCalBraceFinishValue]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_cal_column_finish_value": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalColumnFinishValue]
        ),
        "stb_cal_girder_finish_value": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalGirderFinishValue]
        ),
        "stb_cal_brace_finish_value": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCalBraceFinishValue]
        ),
    }


class StbCalBraceFinishS(StBridgeElement):
    """StbCalBraceFinishS：StbCalBraceFinish_S

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        weight (float): 属性
        covering_unit_weight (float): 属性
        covering_size (float): 属性
        covering_type (StbCalBraceFinishSCoveringType): 属性
        load_ratio (float): 属性
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
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_type": _FI(
            py_type=StbCalBraceFinishSCoveringType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("A1", "A2", "B1", "B2", "C", "D"),
        ),
        "load_ratio": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalBraceFinish_S"


class StbCalGirderFinishS(StBridgeElement):
    """StbCalGirderFinishS：StbCalGirderFinish_S

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        weight (float): 属性
        covering_unit_weight (float): 属性
        covering_size (float): 属性
        covering_type (StbCalGirderFinishSCoveringType): 属性
        load_ratio (float): 属性
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
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_type": _FI(
            py_type=StbCalGirderFinishSCoveringType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("A1", "A2", "B1", "B2", "C", "D"),
        ),
        "load_ratio": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbCalGirderFinish_S"


class StbCalColumnFinishS(StBridgeElement):
    """StbCalColumnFinishS：StbCalColumnFinish_S

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        weight (float): 属性
        covering_unit_weight (float): 属性
        covering_size (float): 属性
        covering_type (StbCalColumnFinishSCoveringType): 属性
        load_ratio (float): 属性
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
        "covering_unit_weight": _FI(py_type=float, data_type=_DT.FLOAT),
        "covering_size": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "covering_type": _FI(
            py_type=StbCalColumnFinishSCoveringType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("A1", "A2", "B1", "B2", "C", "D"),
        ),
        "load_ratio": _FI(py_type=float, data_type=_DT.FLOAT),
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
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTHSIDE", "ONESIDE", "NONE"),
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
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "BOTHSIDE",
                "ONESIDE",
                "BOTHSIDE_BOTTOM",
                "ONESIDE_HALFBOTTOM",
                "NONE",
            ),
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
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("4SIDES", "2SIDES", "NONE"),
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
            choices=("A1", "A2", "B1", "B2", "C", "D"),
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
            data_type=_DT.STR_ENUM,
            choices=(
                "BOTHSIDE",
                "ONESIDE",
                "BOTHSIDE_BOTTOM",
                "ONESIDE_HALFBOTTOM",
                "NONE",
            ),
        ),
        "weight_column": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_column": _FI(
            py_type=StbCalFloorFinishRcTypeColumn,
            data_type=_DT.STR_ENUM,
            choices=("4SIDES", "2SIDES", "NONE"),
        ),
        "weight_beam": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_beam": _FI(
            py_type=StbCalFloorFinishRcTypeBeam,
            data_type=_DT.STR_ENUM,
            choices=(
                "BOTHSIDE",
                "ONESIDE",
                "BOTHSIDE_BOTTOM",
                "ONESIDE_HALFBOTTOM",
                "NONE",
            ),
        ),
        "weight_canti": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_canti": _FI(
            py_type=StbCalFloorFinishRcTypeCanti,
            data_type=_DT.STR_ENUM,
            choices=(
                "BOTHSIDE",
                "ONESIDE",
                "BOTHSIDE_BOTTOM",
                "ONESIDE_HALFBOTTOM",
                "NONE",
            ),
        ),
        "weight_wall": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_wall": _FI(
            py_type=StbCalFloorFinishRcTypeWall,
            data_type=_DT.STR_ENUM,
            choices=("BOTHSIDE", "ONESIDE", "NONE"),
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
            choices=("A1", "A2", "B1", "B2", "C", "D"),
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
            data_type=_DT.STR_ENUM,
            choices=(
                "BOTHSIDE",
                "ONESIDE",
                "BOTHSIDE_BOTTOM",
                "ONESIDE_HALFBOTTOM",
                "NONE",
            ),
        ),
        "weight_column": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_column": _FI(
            py_type=StbCalFinishRcTypeColumn,
            data_type=_DT.STR_ENUM,
            choices=("4SIDES", "2SIDES", "NONE"),
        ),
        "weight_beam": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_beam": _FI(
            py_type=StbCalFinishRcTypeBeam,
            data_type=_DT.STR_ENUM,
            choices=(
                "BOTHSIDE",
                "ONESIDE",
                "BOTHSIDE_BOTTOM",
                "ONESIDE_HALFBOTTOM",
                "NONE",
            ),
        ),
        "weight_canti": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_canti": _FI(
            py_type=StbCalFinishRcTypeCanti,
            data_type=_DT.STR_ENUM,
            choices=(
                "BOTHSIDE",
                "ONESIDE",
                "BOTHSIDE_BOTTOM",
                "ONESIDE_HALFBOTTOM",
                "NONE",
            ),
        ),
        "weight_wall": _FI(py_type=float, data_type=_DT.FLOAT),
        "type_wall": _FI(
            py_type=StbCalFinishRcTypeWall,
            data_type=_DT.STR_ENUM,
            choices=("BOTHSIDE", "ONESIDE", "NONE"),
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
        stb_cal_member_finish_values (StbCalMemberFinishValues): 子要素
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
        "stb_cal_member_finish_values": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalMemberFinishValues
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
            xml_type="positiveIntegerList",
            kind=_FK.CONTENT,
            data_type=_DT.POSITIVE_INTEGER_LIST,
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
        code (str): 属性
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
        "code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "type": _FI(
            py_type=StbCalLiveloadType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "HABITABLEROOMS",
                "OFFICES",
                "CLASSROOMS",
                "STORES",
                "MEETINGROOMS_FIXEDSEATING",
                "MEETINGROOMS_OTHERSEATS",
                "AUTOMOBILEGARAGES",
                "INPUT_VALUES",
            ),
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
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("DIVISION1", "DIVISION2", "DIVISION3", "DIVISION4"),
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
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("CLASS1", "CLASS2", "CLASS3"),
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


class StbExportNotice(StBridgeElement):
    """通知ログ：StbExportNotice

    Attributes:
        id (int): 属性 通知ID
        object_name (str): 属性 ST-Bridgeの要素名
        id_object (int): 属性 object_nameに該当する要素のID
        comment (str): 属性 説明
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "object_name": _FI(py_type=str, data_type=_DT.STR),
        "id_object": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbExportWarning(StBridgeElement):
    """通知ログ：StbExportWarning

    Attributes:
        id (int): 属性 ワーニングID
        object_name (str): 属性 ST-Bridgeの要素名
        id_object (int): 属性 object_nameに該当するのID
        comment (str): 属性 説明
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "object_name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_object": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbExportError(StBridgeElement):
    """エラーログ：StbExportError

    Attributes:
        id (int): 属性 エラーID
        object_name (str): 属性 出力アプリケーションでの名前
        id_object (int): 属性 出力アプリケーションでのID
        comment (str): 属性 説明
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "object_name": _FI(py_type=str, data_type=_DT.STR),
        "id_object": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbExportLog(StBridgeElement):
    """変換ログ：StbExportLog

    Attributes:
        stb_export_error (list[StbExportError]): 子要素 StbExportError(エラーログ)
        stb_export_warning (list[StbExportWarning]): 子要素 StbExportWarning(通知ログ)
        stb_export_notice (list[StbExportNotice]): 子要素 StbExportNotice(通知ログ)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_export_error": _FI(kind=_FK.ELEMENT, py_type=list[StbExportError]),
        "stb_export_warning": _FI(kind=_FK.ELEMENT, py_type=list[StbExportWarning]),
        "stb_export_notice": _FI(kind=_FK.ELEMENT, py_type=list[StbExportNotice]),
    }


class StbExportPolicy(StBridgeElement):
    """変換方針：StbExportPolicy

    Attributes:
        comment (str): 属性 変換方針説明
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbExportInformation(StBridgeElement):
    """出力情報：StbExportInformation

    Attributes:
        stb_export_policy (list[StbExportPolicy]): 子要素 StbExportPolicy(変換方針)
        stb_export_log (StbExportLog): 子要素 StbExportLog(変換ログ)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_export_policy": _FI(kind=_FK.ELEMENT, py_type=list[StbExportPolicy]),
        "stb_export_log": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbExportLog),
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
        "stb_ext_property": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbExtProperty]
        ),
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
        "stb_extension": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbExtension]
        ),
    }


class StbWeldFlare(StBridgeElement):
    """フレア溶接：StbWeldFlare

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        mark (str): 属性 識別マーク
        name (str): 属性 略称
        type_weld (StbWeldFlareTypeWeld): 属性 継手形式以下のいずれかの値をとる。RR（丸鋼―丸鋼）、RP（丸鋼―板）、CC（角形鋼管―角形鋼管）CP（角形鋼管―板）
        min_t (float): 属性 板厚の下限
        max_t (float): 属性 板厚の上限
        continuous (bool): 属性 まわし溶接の有無
        location (StbWeldFlareLocation): 属性 溶接場所以下のいずれかの値をとる。Factory（工場溶接）、Site（現場溶接）
        stb_weld_spec (list[StbWeldSpec]): 子要素 StbWeldSpec(溶接仕様詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "mark": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type_weld": _FI(
            py_type=StbWeldFlareTypeWeld,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RR", "RP", "CC", "CP"),
        ),
        "min_t": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "max_t": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "continuous": _FI(py_type=bool, data_type=_DT.BOOL),
        "location": _FI(
            py_type=StbWeldFlareLocation,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Factory", "Site"),
        ),
        "stb_weld_spec": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbWeldSpec]"
        ),
    }


class StbWeldFillet(StBridgeElement):
    """隅肉溶接：StbWeldFillet

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        mark (str): 属性 識別マーク
        name (str): 属性 略称
        type_weld (StbWeldFilletTypeWeld): 属性 継手形式以下のいずれかの値をとる。B（突合せ溶接）、T（T形溶接）、L（重ね溶接）
        shape_bevel (StbWeldFilletShapeBevel): 属性 開先形状以下のいずれかの値をとる。L（レ形開先）、K（K形開先）
        side_bevel1 (StbWeldFilletSideBevel1): 属性 開先の方向以下のいずれかの値をとる。Front（表面）Reverse（裏面）
        side_bevel2 (StbWeldFilletSideBevel2): 属性 開先の方向（左右）以下のいずれかの値をとる。Right（右側）Left（左側）
        min_t1 (float): 属性 板厚の下限
        max_t1 (float): 属性 板厚の上限
        g (float): 属性 ルート間隔
        r (float): 属性 ルート面
        alfa1 (float): 属性 開先角度1（表面）
        alfa2 (float): 属性 開先角度2（裏面）
        continuous (bool): 属性 まわし溶接の有無
        location (StbWeldFilletLocation): 属性 溶接場所以下のいずれかの値をとる。Factory（工場溶接）、Site（現場溶接）
        robots (str): 属性 ロボット溶接の対応
        stb_weld_spec (list[StbWeldSpec]): 子要素 StbWeldSpec(溶接仕様詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "mark": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type_weld": _FI(
            py_type=StbWeldFilletTypeWeld,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("B", "T", "L"),
        ),
        "shape_bevel": _FI(
            py_type=StbWeldFilletShapeBevel, data_type=_DT.STR_ENUM, choices=("L", "K")
        ),
        "side_bevel1": _FI(
            py_type=StbWeldFilletSideBevel1,
            data_type=_DT.STR_ENUM,
            choices=("Front", "Reverse"),
        ),
        "side_bevel2": _FI(
            py_type=StbWeldFilletSideBevel2,
            data_type=_DT.STR_ENUM,
            choices=("Right", "Left"),
        ),
        "min_t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "max_t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "g": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="G"),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="R"),
        "alfa1": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "alfa2": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "continuous": _FI(py_type=bool, data_type=_DT.BOOL),
        "location": _FI(
            py_type=StbWeldFilletLocation,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Factory", "Site"),
        ),
        "robots": _FI(py_type=str, data_type=_DT.STR),
        "stb_weld_spec": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbWeldSpec]"
        ),
    }


class StbWeldPartialPenetration(StBridgeElement):
    """部分溶け込み溶接：StbWeldPartialPenetration

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        mark (str): 属性 識別マーク
        name (str): 属性 略称
        type_weld (StbWeldPartialPenetrationTypeWeld): 属性 継手形式以下のいずれかの値をとる。B（突合せ溶接）、T（T形溶接）、C（角溶接）
        type_backup (StbWeldPartialPenetrationTypeBackup): 属性 バックアップ材の種類角溶接で必要な場合以下の値をとる。U（裏当金）
        shape_bevel (StbWeldPartialPenetrationShapeBevel): 属性 開先加工の形状以下のいずれかの値をとる。L（レ形開先）、V（V形開先）、K（K形開先）
        side_bevel1 (StbWeldPartialPenetrationSideBevel1): 属性 開先の方向（表裏）以下のいずれかの値をとる。Front（表面）Reverse（裏面）Both（両面）
        side_bevel2 (StbWeldPartialPenetrationSideBevel2): 属性 開先の方向（左右）以下のいずれかの値をとる。Right（右側）Left（左側）
        min_t1 (float): 属性 板厚の下限
        max_t1 (float): 属性 板厚の上限
        r (float): 属性 ルート面
        alfa1 (float): 属性 開先角度1
        alfa2 (float): 属性 開先角度2
        continuous (bool): 属性 まわし溶接の有無
        method (StbWeldPartialPenetrationMethod): 属性 溶接方法以下のいずれかの値をとる。G（GMAW-ガスシールドアーク溶接、SMAW-被覆アーク溶接）、S（SAW-サブマージアーク溶接）
        location (StbWeldPartialPenetrationLocation): 属性 溶接場所以下のいずれかの値をとる。Factory（工場溶接）、Site（現場溶接）
        robots (str): 属性 ロボット溶接の対応
        strength_backup (str): 属性 裏当て金の材質
        shape_backup (StbWeldPartialPenetrationShapeBackup): 属性 裏当て金の材種以下の値をとる。PL（プレート）、FB（フラットバー）
        stb_weld_spec (list[StbWeldSpec]): 子要素 StbWeldSpec(溶接仕様詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "mark": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type_weld": _FI(
            py_type=StbWeldPartialPenetrationTypeWeld,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("B", "T", "C"),
        ),
        "type_backup": _FI(
            py_type=StbWeldPartialPenetrationTypeBackup,
            data_type=_DT.STR_ENUM,
            choices=("U",),
        ),
        "shape_bevel": _FI(
            py_type=StbWeldPartialPenetrationShapeBevel,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("L", "V", "K"),
        ),
        "side_bevel1": _FI(
            py_type=StbWeldPartialPenetrationSideBevel1,
            data_type=_DT.STR_ENUM,
            choices=("Front", "Reverse", "Both"),
        ),
        "side_bevel2": _FI(
            py_type=StbWeldPartialPenetrationSideBevel2,
            data_type=_DT.STR_ENUM,
            choices=("Right", "Left"),
        ),
        "min_t1": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "max_t1": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="R"),
        "alfa1": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "alfa2": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "continuous": _FI(py_type=bool, data_type=_DT.BOOL),
        "method": _FI(
            py_type=StbWeldPartialPenetrationMethod,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("G", "S"),
        ),
        "location": _FI(
            py_type=StbWeldPartialPenetrationLocation,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Factory", "Site"),
        ),
        "robots": _FI(py_type=str, data_type=_DT.STR),
        "strength_backup": _FI(py_type=str, data_type=_DT.STR),
        "shape_backup": _FI(
            py_type=StbWeldPartialPenetrationShapeBackup,
            data_type=_DT.STR_ENUM,
            choices=("PL", "FB"),
        ),
        "stb_weld_spec": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbWeldSpec]"
        ),
    }


class StbWeldSpec(StBridgeElement):
    """溶接仕様詳細：StbWeldSpec

    Attributes:
        t1 (float): 属性 板厚
        d (float): 属性 直径
        d1 (float): 属性 開先深さ1（表面）
        d2 (float): 属性 開先深さ2（裏面）
        s1 (float): 属性 隅肉サイズ（表面）
        s2 (float): 属性 隅肉サイズ（裏面）
        h1 (float): 属性 余盛高さ1（表面）
        h2 (float): 属性 余盛高さ2（裏面）
        area (float): 属性 断面積
        length (float): 属性 溶接実長
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "d1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D1"
        ),
        "d2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="D2"
        ),
        "s1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="S1"
        ),
        "s2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="S2"
        ),
        "h1": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "h2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "area": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbWeldFullPenetration(StBridgeElement):
    """完全溶込み溶接：StbWeldFullPenetration

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        mark (str): 属性 識別マーク
        name (str): 属性 略称
        type_weld (StbWeldFullPenetrationTypeWeld): 属性 継手形式以下のいずれかの値をとる。B（突合せ溶接）、T（T形溶接）、C（角溶接）E（エレクトロスラグ溶接）
        type_backup (StbWeldFullPenetrationTypeBackup): 属性 バックアップ材の種類以下のいずれかの値をとる。U（裏当金）、H（裏はつり）
        shape_bevel (StbWeldFullPenetrationShapeBevel): 属性 開先加工の形状以下のいずれかの値をとる。L（レ形開先）、V（V形開先）、K（K形開先）、X（X形開先）I（I形開先）
        side_bevel1 (StbWeldFullPenetrationSideBevel1): 属性 開先の方向（表裏）以下のいずれかの値をとる。Front（表面）Reverse（裏面）Both（両面）
        side_bevel2 (StbWeldFullPenetrationSideBevel2): 属性 開先の方向（左右）以下のいずれかの値をとる。Right（右側）Left（左側）
        min_t1 (float): 属性 板厚の下限
        max_t1 (float): 属性 板厚の上限
        g (float): 属性 ルート間隔
        r (float): 属性 ルート面
        alfa1 (float): 属性 開先角度1（表面）
        alfa2 (float): 属性 開先角度2（裏面）
        method (StbWeldFullPenetrationMethod): 属性 溶接方法以下のいずれかの値をとる。G（GMAW-ガスシールドアーク溶接、SMAW-被覆アーク溶接）、S（SAW-サブマージアーク溶接）、E（ESW-エレクトロスラグ溶接）
        location (StbWeldFullPenetrationLocation): 属性 溶接場所以下のいずれかの値をとる。Factory（工場溶接）、Site（現場溶接）
        robots (str): 属性 ロボット溶接の対応
        kind_end_tab (StbWeldFullPenetrationKindEndTab): 属性 エンドタブの種類以下のいずれかの値をとる。Steel（鋼製エンドタブ）、Flux（固形エンドタブ）
        strength_backup (str): 属性 裏当て金の材質
        shape_backup1 (StbWeldFullPenetrationShapeBackup1): 属性 裏当て金の材種1以下の値をとる。PL（プレート）、FB（フラットバー）
        size_backup1 (str): 属性 裏当て金のサイズ1
        shape_backup2 (StbWeldFullPenetrationShapeBackup2): 属性 裏当て金の材種2以下の値をとる。PL（プレート）、FB（フラットバー）
        size_backup2 (str): 属性 裏当て金のサイズ2
        taper_processing (bool): 属性 テーパー加工
        facing_processing (bool): 属性 フェーシング加工
        stb_weld_spec (list[StbWeldSpec]): 子要素 StbWeldSpec(溶接仕様詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "mark": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "type_weld": _FI(
            py_type=StbWeldFullPenetrationTypeWeld,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("B", "T", "C", "E"),
        ),
        "type_backup": _FI(
            py_type=StbWeldFullPenetrationTypeBackup,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("U", "H"),
        ),
        "shape_bevel": _FI(
            py_type=StbWeldFullPenetrationShapeBevel,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("L", "V", "K", "X", "I"),
        ),
        "side_bevel1": _FI(
            py_type=StbWeldFullPenetrationSideBevel1,
            data_type=_DT.STR_ENUM,
            choices=("Front", "Reverse", "Both"),
        ),
        "side_bevel2": _FI(
            py_type=StbWeldFullPenetrationSideBevel2,
            data_type=_DT.STR_ENUM,
            choices=("Right", "Left"),
        ),
        "min_t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "max_t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "g": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="G"),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="R"),
        "alfa1": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "alfa2": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "method": _FI(
            py_type=StbWeldFullPenetrationMethod,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("G", "S", "E"),
        ),
        "location": _FI(
            py_type=StbWeldFullPenetrationLocation,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Factory", "Site"),
        ),
        "robots": _FI(py_type=str, data_type=_DT.STR),
        "kind_end_tab": _FI(
            py_type=StbWeldFullPenetrationKindEndTab,
            data_type=_DT.STR_ENUM,
            choices=("Steel", "Flux"),
        ),
        "strength_backup": _FI(py_type=str, data_type=_DT.STR),
        "shape_backup1": _FI(
            py_type=StbWeldFullPenetrationShapeBackup1,
            data_type=_DT.STR_ENUM,
            choices=("PL", "FB"),
        ),
        "size_backup1": _FI(py_type=str, data_type=_DT.STR),
        "shape_backup2": _FI(
            py_type=StbWeldFullPenetrationShapeBackup2,
            data_type=_DT.STR_ENUM,
            choices=("PL", "FB"),
        ),
        "size_backup2": _FI(py_type=str, data_type=_DT.STR),
        "taper_processing": _FI(py_type=bool, data_type=_DT.BOOL),
        "facing_processing": _FI(py_type=bool, data_type=_DT.BOOL),
        "stb_weld_spec": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbWeldSpec]),
    }


class StbWeld(StBridgeElement):
    """溶接：StbWeld

    Attributes:
        stb_weld_full_penetration (list[StbWeldFullPenetration]): 子要素 StbWeldFullPenetration(完全溶込み溶接)
        stb_weld_partial_penetration (list[StbWeldPartialPenetration]): 子要素 StbWeldPartialPenetration(部分溶け込み溶接)
        stb_weld_fillet (list[StbWeldFillet]): 子要素 StbWeldFillet(隅肉溶接)
        stb_weld_flare (list[StbWeldFlare]): 子要素 StbWeldFlare(フレア溶接)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_weld_full_penetration": _FI(
            kind=_FK.ELEMENT, py_type=list[StbWeldFullPenetration]
        ),
        "stb_weld_partial_penetration": _FI(
            kind=_FK.ELEMENT, py_type=list[StbWeldPartialPenetration]
        ),
        "stb_weld_fillet": _FI(kind=_FK.ELEMENT, py_type=list[StbWeldFillet]),
        "stb_weld_flare": _FI(kind=_FK.ELEMENT, py_type=list[StbWeldFlare]),
    }


class StbStiffener(StBridgeElement):
    """StbStiffener

    Attributes:
        id (int): 属性
        guid (UUID): 属性
        name (str): 属性
        strength_plate (str): 属性
        thickness (float): 属性
        b_x (float): 属性
        b_y (float): 属性
        id_weld (int): 属性
        cutback (int): 属性
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
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
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
        "id_weld": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "cutback": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbStiffeners(StBridgeElement):
    """StbStiffeners

    Attributes:
        stb_stiffener (list[StbStiffener]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_stiffener": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbStiffener]
        ),
    }


class StbDiaphragm(StBridgeElement):
    """ダイアフラム詳細：StbDiaphragm

    Attributes:
        id (int): 属性 ID
        guid (str): 属性 GUID
        name (str): 属性 符号
        strength_plate (str): 属性 ダイアフラムの材種
        thickness (float): 属性 ダイアフラムの厚さ
        b_x (float): 属性 ダイアフラムの寸法(Bx)
        b_y (float): 属性 ダイアフラムの寸法(By)
        type (StbDiaphragmType): 属性 ダイアフラム形式以下のいずれかの値をとる。Through（通しダイア）、Internal（内ダイア）、External（外ダイア）
        id_weld (int): 属性 溶接ID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=str, data_type=_DT.STR),
        "name": _FI(py_type=str, data_type=_DT.STR),
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "b_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_X",
        ),
        "b_y": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="B_Y"
        ),
        "type": _FI(
            py_type=StbDiaphragmType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Through", "Internal", "External"),
        ),
        "id_weld": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbDiaphragms(StBridgeElement):
    """ダイアフラム詳細（複数）：StbDiaphragms

    Attributes:
        stb_diaphragm (list[StbDiaphragm]): 子要素 StbDiaphragm(ダイアフラム詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_diaphragm": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbDiaphragm]
        ),
    }


class StbRibPlate(StBridgeElement):
    """リブプレート詳細：StbRibPlate

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 符号
        strength_plate (str): 属性 リブプレートの材種
        thickness (float): 属性 リブプレートの厚さ
        id_weld (int): 属性 溶接ID
        cutback (int): 属性 溶接控え
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
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "id_weld": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "cutback": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbRibPlates(StBridgeElement):
    """リブプレート詳細（複数）：StbRibPlates

    Attributes:
        stb_rib_plate (list[StbRibPlate]): 子要素 StbRibPlate(リブプレート詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_rib_plate": _FI(kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbRibPlate]),
    }


class StbGussetPlateSplice(StBridgeElement):
    """スプライスプレート詳細：StbGussetPlateSplice

    Attributes:
        strength_plate (str): 属性 添え板の材種
        plate_thickness (float): 属性 添え板の厚さ
        strength_filler (str): 属性 フィラープレートの材種
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_filler": _FI(py_type=str, data_type=_DT.STR),
    }


class StbGussetPlateBoltArray(StBridgeElement):
    """ボルト詳細：StbGussetPlateBoltArray

    Attributes:
        id_order (int): 属性 ボルトの列数
        mw (int): 属性 ボルトの数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbGussetPlate(StBridgeElement):
    """ガセットプレート詳細：StbGussetPlate

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 符号
        connection_type (StbGussetPlateConnectionType): 属性 仕口タイプgap、web、splice
        flange_type (StbGussetPlateFlangeType): 属性 フランジ刃落としタイプnone、one_side、both_sides
        strength_plate (str): 属性 ガセットプレートの材種
        thickness (float): 属性 ガセットプレートの厚さ
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼び名）
        clearance (float): 属性 母材と接続部材の間隔
        flange_cut (float): 属性 フランジ刃落としの長さ
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ (pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        h1 (float): 属性 ガセットプレートのあき1 (h1)
        h2 (float): 属性 ガセットプレートのあき2 (h2)
        ey (float): 属性 嵩上げ点の幅方向の距離
        ez (float): 属性 嵩上げ点の高さ方向の距離
        r (float): 属性 入隅半径 (R)
        id_weld (int): 属性 溶接ID
        cutback (int): 属性 溶接控え
        stb_gusset_plate_bolt_array (list[StbGussetPlateBoltArray]): 子要素 StbGussetPlateBoltArray(ボルト詳細)
        stb_gusset_plate_splice (StbGussetPlateSplice): 子要素 StbGussetPlateSplice(スプライスプレート詳細)
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
        "connection_type": _FI(
            py_type=StbGussetPlateConnectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("gap", "web", "splice"),
        ),
        "flange_type": _FI(
            py_type=StbGussetPlateFlangeType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("none", "one_side", "both_sides"),
        ),
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "clearance": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "flange_cut": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "h1": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "h2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "ey": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "ez": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="R"),
        "id_weld": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "cutback": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_gusset_plate_bolt_array": _FI(
            kind=_FK.ELEMENT, py_type=list[StbGussetPlateBoltArray]
        ),
        "stb_gusset_plate_splice": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbGussetPlateSplice
        ),
    }


class StbGussetPlates(StBridgeElement):
    """ガセットプレート詳細（複数）：StbGussetPlates

    Attributes:
        stb_gusset_plate (list[StbGussetPlate]): 子要素 StbGussetPlate(ガセットプレート詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_gusset_plate": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbGussetPlate]
        ),
    }


class StbConnections(StBridgeElement):
    """コネクション情報：StbConnections

    Attributes:
        stb_gusset_plates (StbGussetPlates): 子要素 StbGussetPlates(ガセットプレート詳細（複数）)
        stb_rib_plates (StbRibPlates): 子要素 StbRibPlates(リブプレート詳細（複数）)
        stb_diaphragms (StbDiaphragms): 子要素 StbDiaphragms(ダイアフラム詳細（複数）)
        stb_stiffeners (StbStiffeners): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_gusset_plates": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbGussetPlates
        ),
        "stb_rib_plates": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbRibPlates),
        "stb_diaphragms": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbDiaphragms),
        "stb_stiffeners": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbStiffeners),
    }


class StbJointShapeCrossHWebShort(StBridgeElement):
    """＋形継手詳細・H部分ウェブ(短)：StbJointShapeCrossHWebShort

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        e5 (float): 属性 縁端距離5 (e5)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_cross_web_bolt (list[StbJointShapeCrossWebBolt]): 子要素 StbJointShapeCrossWebBolt(＋形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e5": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_cross_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeCrossWebBolt]"
        ),
    }


class StbJointShapeCrossHWebLong(StBridgeElement):
    """＋形継手詳細・H部分ウェブ(長)：StbJointShapeCrossHWebLong

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        e5 (float): 属性 縁端距離5 (e5)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_cross_web_bolt (list[StbJointShapeCrossWebBolt]): 子要素 StbJointShapeCrossWebBolt(＋形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e5": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_cross_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeCrossWebBolt]"
        ),
    }


class StbJointShapeCrossHFlange(StBridgeElement):
    """＋形継手詳細・H部分フランジ：StbJointShapeCrossHFlange

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ(P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
        stb_joint_shape_cross_flange_bolt (list[StbJointShapeCrossFlangeBolt]): 子要素 StbJointShapeCrossFlangeBolt(＋形継手詳細・フランジボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
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
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
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
        "stb_joint_shape_cross_flange_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeCrossFlangeBolt]"
        ),
    }


class StbJointShapeCrossTWebShort(StBridgeElement):
    """＋形継手詳細・T部分ウェブ(短)：StbJointShapeCrossTWebShort

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        e5 (float): 属性 縁端距離5 (e5)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_cross_web_bolt (list[StbJointShapeCrossWebBolt]): 子要素 StbJointShapeCrossWebBolt(＋形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e5": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_cross_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeCrossWebBolt]"
        ),
    }


class StbJointShapeCrossWebBolt(StBridgeElement):
    """＋形継手詳細・ウェブボルト詳細：StbJointShapeCrossWebBolt

    Attributes:
        id_order (int): 属性 ボルトの列数
        mw (int): 属性 ボルトの数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbJointShapeCrossTWebLong(StBridgeElement):
    """＋形継手詳細・T部分ウェブ(長)：StbJointShapeCrossTWebLong

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        e5 (float): 属性 縁端距離5 (e5)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_cross_web_bolt (list[StbJointShapeCrossWebBolt]): 子要素 StbJointShapeCrossWebBolt(＋形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e5": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_cross_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbJointShapeCrossWebBolt]
        ),
    }


class StbJointShapeCrossTFlangeShort(StBridgeElement):
    """＋形継手詳細・T部分フランジ（短）：StbJointShapeCrossTFlangeShort

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ(P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
        stb_joint_shape_cross_flange_bolt (list[StbJointShapeCrossFlangeBolt]): 子要素 StbJointShapeCrossFlangeBolt(＋形継手詳細・フランジボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
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
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
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
        "stb_joint_shape_cross_flange_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeCrossFlangeBolt]"
        ),
    }


class StbJointShapeCrossFlangeBolt(StBridgeElement):
    """＋形継手詳細・フランジボルト詳細：StbJointShapeCrossFlangeBolt

    Attributes:
        id_order (int): 属性 ボルトの列数
        mf (int): 属性 ボルトの数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
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
    }


class StbJointShapeCrossTFlangeLong(StBridgeElement):
    """＋形継手詳細・T部分フランジ（長）：StbJointShapeCrossTFlangeLong

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ(P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
        stb_joint_shape_cross_flange_bolt (list[StbJointShapeCrossFlangeBolt]): 子要素 StbJointShapeCrossFlangeBolt(＋形継手詳細・フランジボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
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
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
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
        "stb_joint_shape_cross_flange_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbJointShapeCrossFlangeBolt]
        ),
    }


class StbJointShapeCross(StBridgeElement):
    """＋形継手詳細：StbJointShapeCross

    Attributes:
        strength_plate_flange (str): 属性 添え板の材種（フランジ）
        strength_plate_web (str): 属性 添え板の材種（ウェブ）
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼名）
        offset_h (float): 属性 Ｈ形鋼の偏心（T形鋼部分の成の中心からの距離）
        offset_t (float): 属性 T形鋼部分の偏心（Ｈ形鋼の成の中心からの距離）
        clearance (float): 属性 部材の母材間隔
        strength_filler (str): 属性 フィラープレートの材種（共通）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate_flange": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_plate_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_h": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="offset_H",
        ),
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
        "strength_filler": _FI(py_type=str, data_type=_DT.STR),
    }


class StbJointColumnShapeCross(StBridgeElement):
    """Ｓ柱継手・＋形：StbJointColumnShapeCross

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        joint_name (str): 属性 継手呼称
        joint_mark (str): 属性 継手符号
        stb_joint_shape_cross (StbJointShapeCross): 子要素 StbJointShapeCross(＋形継手詳細)
        stb_joint_shape_cross_t_flange_long (StbJointShapeCrossTFlangeLong): 子要素 StbJointShapeCrossTFlangeLong(＋形継手詳細・T部分フランジ（長）)
        stb_joint_shape_cross_t_flange_short (StbJointShapeCrossTFlangeShort): 子要素 StbJointShapeCrossTFlangeShort(＋形継手詳細・T部分フランジ（短）)
        stb_joint_shape_cross_t_web_long (StbJointShapeCrossTWebLong): 子要素 StbJointShapeCrossTWebLong(＋形継手詳細・T部分ウェブ(長))
        stb_joint_shape_cross_t_web_short (StbJointShapeCrossTWebShort): 子要素 StbJointShapeCrossTWebShort(＋形継手詳細・T部分ウェブ(短))
        stb_joint_shape_cross_h_flange (StbJointShapeCrossHFlange): 子要素 StbJointShapeCrossHFlange(＋形継手詳細・H部分フランジ)
        stb_joint_shape_cross_h_web_long (StbJointShapeCrossHWebLong): 子要素 StbJointShapeCrossHWebLong(＋形継手詳細・H部分ウェブ(長))
        stb_joint_shape_cross_h_web_short (StbJointShapeCrossHWebShort): 子要素 StbJointShapeCrossHWebShort(＋形継手詳細・H部分ウェブ(短))
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
        "stb_joint_shape_cross_t_flange_long": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeCrossTFlangeLong
        ),
        "stb_joint_shape_cross_t_flange_short": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeCrossTFlangeShort
        ),
        "stb_joint_shape_cross_t_web_long": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossTWebLong,
        ),
        "stb_joint_shape_cross_t_web_short": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossTWebShort,
        ),
        "stb_joint_shape_cross_h_flange": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointShapeCrossHFlange
        ),
        "stb_joint_shape_cross_h_web_long": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossHWebLong,
        ),
        "stb_joint_shape_cross_h_web_short": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbJointShapeCrossHWebShort,
        ),
    }


class StbJointShapeTWebT(StBridgeElement):
    """Ｔ形継手詳細・Ｔ部分ウェブ：StbJointShapeTWebT

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        e5 (float): 属性 縁端距離5 (e5)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_t_web_bolt (list[StbJointShapeTWebBolt]): 子要素 StbJointShapeTWebBolt(Ｔ形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e5": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_t_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeTWebBolt]"
        ),
    }


class StbJointShapeTFlangeT(StBridgeElement):
    """Ｔ形継手詳細・Ｔ部分フランジ：StbJointShapeTFlangeT

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ(P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
        stb_joint_shape_t_flange_bolt (list[StbJointShapeTFlangeBolt]): 子要素 StbJointShapeTFlangeBolt(Ｔ形継手詳細・フランジボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
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
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
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
        "stb_joint_shape_t_flange_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeTFlangeBolt]"
        ),
    }


class StbJointShapeTWebHShort(StBridgeElement):
    """Ｔ形継手詳細・Ｈ部分ウェブ(短)：StbJointShapeTWebHShort

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        e5 (float): 属性 縁端距離5 (e5)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_t_web_bolt (list[StbJointShapeTWebBolt]): 子要素 StbJointShapeTWebBolt(Ｔ形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e5": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_t_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbJointShapeTWebBolt]"
        ),
    }


class StbJointShapeTWebBolt(StBridgeElement):
    """Ｔ形継手詳細・ウェブボルト詳細：StbJointShapeTWebBolt

    Attributes:
        id_order (int): 属性 ボルトの列数
        mw (int): 属性 ボルトの数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbJointShapeTWebHLong(StBridgeElement):
    """Ｔ形継手詳細・Ｈ部分ウェブ(長)：StbJointShapeTWebHLong

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        e5 (float): 属性 縁端距離5 (e5)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_t_web_bolt (list[StbJointShapeTWebBolt]): 子要素 StbJointShapeTWebBolt(Ｔ形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e5": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_t_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbJointShapeTWebBolt]
        ),
    }


class StbJointShapeTFlangeBolt(StBridgeElement):
    """Ｔ形継手詳細・フランジボルト詳細：StbJointShapeTFlangeBolt

    Attributes:
        id_order (int): 属性 ボルトの列数
        mf (int): 属性 ボルトの数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
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
    }


class StbJointShapeTFlangeH(StBridgeElement):
    """Ｔ形継手詳細・Ｈ部分フランジ：StbJointShapeTFlangeH

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ(P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
        stb_joint_shape_t_flange_bolt (list[StbJointShapeTFlangeBolt]): 子要素 StbJointShapeTFlangeBolt(Ｔ形継手詳細・フランジボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
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
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
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
        "stb_joint_shape_t_flange_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbJointShapeTFlangeBolt]
        ),
    }


class StbJointShapeT(StBridgeElement):
    """Ｔ形継手詳細：StbJointShapeT

    Attributes:
        strength_plate_flange (str): 属性 添え板の材種（フランジ）
        strength_plate_web (str): 属性 添え板の材種（ウェブ）
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼名）
        offset_t (float): 属性 Ｔ形鋼の偏心（Ｈ形鋼の成の中心からの距離）
        clearance (float): 属性 部材の母材間隔
        strength_filler (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate_flange": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_plate_web": _FI(py_type=str, data_type=_DT.STR),
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
        "strength_filler": _FI(py_type=str, data_type=_DT.STR),
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


class StbJointShapeHWebBolt(StBridgeElement):
    """Ｈ形継手詳細・ウェブボルト詳細：StbJointShapeHWebBolt

    Attributes:
        id_order (int): 属性 ボルトの列数
        mw (int): 属性 ボルトの数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mw": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }


class StbJointShapeHWeb(StBridgeElement):
    """Ｈ形継手詳細・ウェブ：StbJointShapeHWeb

    Attributes:
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ(pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        plate_thickness (float): 属性 添え板 厚さ
        plate_width (float): 属性 添え板 幅(B)
        plate_length (float): 属性 添え板 長さ(L)
        stb_joint_shape_h_web_bolt (list[StbJointShapeHWebBolt]): 子要素 StbJointShapeHWebBolt(Ｈ形継手詳細・ウェブボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "plate_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_joint_shape_h_web_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbJointShapeHWebBolt]
        ),
    }


class StbJointShapeHFlangeBolt(StBridgeElement):
    """Ｈ形継手詳細・フランジボルト詳細：StbJointShapeHFlangeBolt

    Attributes:
        id_order (int): 属性 ボルトの列数
        mf (int): 属性 ボルトの数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
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
    }


class StbJointShapeHFlange(StBridgeElement):
    """Ｈ形継手詳細・フランジ：StbJointShapeHFlange

    Attributes:
        is_zigzag (bool): 属性 千鳥配置か否か
        g1 (float): 属性 ゲージ寸法1 (g1)
        g2 (float): 属性 ゲージ寸法2 (g2)
        pitch (float): 属性 長手方向のボルトピッチ (P)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        outside_thickness (float): 属性 外添え板 厚さ
        outside_width (float): 属性 外添え板 幅(B)
        outside_length (float): 属性 外添え板 長さ(L)
        inside_thickness (float): 属性 内添え板 厚さ
        inside_width (float): 属性 内添え板 幅
        inside_length (float): 属性 内添え板 長さ
        stb_joint_shape_h_flange_bolt (list[StbJointShapeHFlangeBolt]): 子要素 StbJointShapeHFlangeBolt(Ｈ形継手詳細・フランジボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_zigzag": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isZigzag"),
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
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
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
        "stb_joint_shape_h_flange_bolt": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbJointShapeHFlangeBolt]
        ),
    }


class StbJointShapeH(StBridgeElement):
    """Ｈ形継手詳細：StbJointShapeH

    Attributes:
        strength_plate_flange (str): 属性 添え板の材種（フランジ）
        strength_plate_web (str): 属性 添え板の材種（ウェブ）
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼び名）
        clearance (float): 属性 部材の母材間隔
        strength_filler (str): 属性 フィラープレートの材種（共通）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate_flange": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_plate_web": _FI(py_type=str, data_type=_DT.STR),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "clearance": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "strength_filler": _FI(py_type=str, data_type=_DT.STR),
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


class StbSecLip2c(StBridgeElement):
    """リップ溝形鋼(2丁)：StbSecLip2C

    Attributes:
        name (str): 属性 形状名
        type (StbSecLip2cType): 属性 形状タイプ以下のいずれか背中合わせ：BACKTOBACK表合わせ：FACETOFACE
        h (float): 属性 成
        a (float): 属性 幅
        c (float): 属性 リップ長
        t (float): 属性 板厚
        gap (float): 属性 ギャップ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecLip2cType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BACKTOBACK", "FACETOFACE"),
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
        "gap": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecLip2C"


class StbSecLipC(StBridgeElement):
    """リップ溝形鋼：StbSecLipC

    Attributes:
        name (str): 属性 形状名
        h (float): 属性 成
        a (float): 属性 幅
        c (float): 属性 リップ長
        t (float): 属性 板厚
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
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


class StbSecRoll2l(StBridgeElement):
    """山形鋼(2丁)：StbSecRoll-2L

    Attributes:
        name (str): 属性 形状名
        type (StbSecRoll2lType): 属性 形状タイプ以下のいずれかの値をとる。背中合わせ：BACKTOBACK表合わせ：FACETOFACE
        a (float): 属性 成
        b (float): 属性 幅
        t1 (float): 属性 成方向の板厚
        t2 (float): 属性 幅方向の板厚
        r1 (float): 属性 フィレット半径
        r2 (float): 属性 先端半径
        gap (float): 属性 ギャップ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecRoll2lType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BACKTOBACK", "FACETOFACE"),
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
        "gap": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-2L"


class StbSecRollL(StBridgeElement):
    """山形鋼：StbSecRoll-L

    Attributes:
        name (str): 属性 形状名
        a (float): 属性 成
        b (float): 属性 幅
        t1 (float): 属性 成方向の板厚
        t2 (float): 属性 幅方向の板厚
        r1 (float): 属性 フィレット半径
        r2 (float): 属性 先端半径
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
        "r1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-L"


class StbSecRoll2c(StBridgeElement):
    """溝形鋼(2丁)：StbSecRoll-2C

    Attributes:
        name (str): 属性 形状名
        type (StbSecRoll2cType): 属性 形状タイプ以下のいずれか背中合わせ：BACKTOBACK表合わせ：FACETOFACE
        a (float): 属性 成
        b (float): 属性 フランジ幅
        t1 (float): 属性 ウェブ厚
        t2 (float): 属性 フランジ厚
        r1 (float): 属性 フィレット半径
        r2 (float): 属性 フランジ先端半径
        gap (float): 属性 ギャップ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type": _FI(
            py_type=StbSecRoll2cType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BACKTOBACK", "FACETOFACE"),
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
        "gap": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-2C"


class StbSecRollC(StBridgeElement):
    """溝形鋼：StbSecRoll-C

    Attributes:
        name (str): 属性 形状名
        a (float): 属性 成
        b (float): 属性 フランジ幅
        t1 (float): 属性 ウェブ厚
        t2 (float): 属性 フランジ厚
        r1 (float): 属性 フィレット半径
        r2 (float): 属性 フランジ先端半径
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
        "r1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "r2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecRoll-C"


class StbSecBuildT(StBridgeElement):
    """組立T形鋼：StbSecBuild-T

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
    _xml_element_name: ClassVar[str] = "StbSecBuild-T"


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


class StbSecBuildHAsymmetric(StBridgeElement):
    """StbSecBuildHAsymmetric：StbSecBuild-HAsymmetric

    Attributes:
        name (str): 属性
        a (float): 属性
        b_t (float): 属性
        b_b (float): 属性
        t1 (float): 属性
        t2_t (float): 属性
        t2_b (float): 属性
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
        "b_t": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_T",
        ),
        "b_b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="B_B",
        ),
        "t1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t2_t": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="t2_T",
        ),
        "t2_b": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="t2_B",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBuild-HAsymmetric"


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
        stb_sec_build_h_asymmetric (list[StbSecBuildHAsymmetric]): 子要素
        stb_sec_roll_box (list[StbSecRollBox]): 子要素 StbSecRoll-BOX(角形鋼管)
        stb_sec_build_box (list[StbSecBuildBox]): 子要素 StbSecBuild-BOX(組立角形鋼管)
        stb_sec_pipe (list[StbSecPipe]): 子要素 StbSecPipe(円形鋼管)
        stb_sec_roll_t (list[StbSecRollT]): 子要素 StbSecRoll-T(T形鋼)
        stb_sec_build_t (list[StbSecBuildT]): 子要素 StbSecBuild-T(組立T形鋼)
        stb_sec_roll_c (list[StbSecRollC]): 子要素 StbSecRoll-C(溝形鋼)
        stb_sec_roll_2c (list[StbSecRoll2c]): 子要素 StbSecRoll-2C(溝形鋼(2丁))
        stb_sec_roll_l (list[StbSecRollL]): 子要素 StbSecRoll-L(山形鋼)
        stb_sec_roll_2l (list[StbSecRoll2l]): 子要素 StbSecRoll-2L(山形鋼(2丁))
        stb_sec_lip_c (list[StbSecLipC]): 子要素 StbSecLipC(リップ溝形鋼)
        stb_sec_lip_2c (list[StbSecLip2c]): 子要素 StbSecLip2C(リップ溝形鋼(2丁))
        stb_sec_flat_bar (list[StbSecFlatBar]): 子要素 StbSecFlatBar(フラットバー)
        stb_sec_round_bar (list[StbSecRoundBar]): 子要素 StbSecRoundBar(丸鋼)
        stb_sec_steel_product (list[StbSecSteelProduct]): 子要素 StbSecSteelProduct(鉄骨製品)
        stb_sec_steel_undefined (list[StbSecSteelUndefined]): 子要素 StbSecSteelUndefined(未定義鉄骨断面)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_roll_h": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollH]),
        "stb_sec_build_h": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBuildH]),
        "stb_sec_build_h_asymmetric": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecBuildHAsymmetric]
        ),
        "stb_sec_roll_box": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollBox]),
        "stb_sec_build_box": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBuildBox]),
        "stb_sec_pipe": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPipe]),
        "stb_sec_roll_t": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollT]),
        "stb_sec_build_t": _FI(kind=_FK.ELEMENT, py_type=list[StbSecBuildT]),
        "stb_sec_roll_c": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollC]),
        "stb_sec_roll_2c": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRoll2c]),
        "stb_sec_roll_l": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRollL]),
        "stb_sec_roll_2l": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRoll2l]),
        "stb_sec_lip_c": _FI(kind=_FK.ELEMENT, py_type=list[StbSecLipC]),
        "stb_sec_lip_2c": _FI(kind=_FK.ELEMENT, py_type=list[StbSecLip2c]),
        "stb_sec_flat_bar": _FI(kind=_FK.ELEMENT, py_type=list[StbSecFlatBar]),
        "stb_sec_round_bar": _FI(kind=_FK.ELEMENT, py_type=list[StbSecRoundBar]),
        "stb_sec_steel_product": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecSteelProduct]
        ),
        "stb_sec_steel_undefined": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecSteelUndefined]
        ),
    }


class StbSecPanelZoneCircle(StBridgeElement):
    """柱梁接合部断面形状・円形：StbSecPanelZoneCircle

    Attributes:
        d (float): 属性 直径
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


class StbSecPanelZoneRect(StBridgeElement):
    """柱梁接合部断面形状・矩形：StbSecPanelZoneRect

    Attributes:
        width_x (float): 属性 Ｘ幅
        width_y (float): 属性 Ｙ幅
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


class StbSecFigurePanelZone(StBridgeElement):
    """柱梁接合部断面形状：StbSecFigurePanelZone

    Attributes:
        stb_sec_panel_zone_rect (StbSecPanelZoneRect): 子要素 StbSecPanelZoneRect(柱梁接合部断面形状・矩形)
        stb_sec_panel_zone_circle (StbSecPanelZoneCircle): 子要素 StbSecPanelZoneCircle(柱梁接合部断面形状・円形)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_panel_zone_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPanelZoneRect
        ),
        "stb_sec_panel_zone_circle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPanelZoneCircle
        ),
    }


class StbSecPanelZone(StBridgeElement):
    """柱梁接合部断面：StbSecPanelZone

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        n_hoop_x (int): 属性 帯筋：X方向本数
        d_hoop_x (str): 属性 帯筋：X方向径
        strength_x (str): 属性 帯筋：X方向強度
        n_hoop_y (int): 属性 帯筋：Y方向本数
        d_hoop_y (str): 属性 帯筋：Y方向径
        strength_y (str): 属性 帯筋：Y方向強度
        pitch_hoop (float): 属性 帯筋：ピッチ
        stb_sec_figure_panel_zone (StbSecFigurePanelZone): 子要素 StbSecFigurePanelZone(柱梁接合部断面形状)
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
        "n_hoop_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_X",
        ),
        "d_hoop_x": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_hoop_X"
        ),
        "strength_x": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_X"),
        "n_hoop_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_Y",
        ),
        "d_hoop_y": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_hoop_Y"
        ),
        "strength_y": _FI(py_type=str, data_type=_DT.STR, xml_name="strength_Y"),
        "pitch_hoop": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "stb_sec_figure_panel_zone": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigurePanelZone
        ),
    }


class StbSecPenetrationSOsringExtension(StBridgeElement):
    """OSリング拡張情報：StbSecPenetration_S_OSringExtension

    Attributes:
        clear_splice (float): 属性 リング縁からウェブスプライス端までの必要クリアランス
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "clear_splice": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPenetration_S_OSringExtension"


class StbSecPenetrationSFrringExtension(StBridgeElement):
    """フリードーナツ拡張情報：StbSecPenetration_S_FRringExtension

    Attributes:
        phi_bottom (float): 属性 下孔径
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "phi_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPenetration_S_FRringExtension"


class StbSecPenetrationSEgringExtension(StBridgeElement):
    """EGリング拡張情報：StbSecPenetration_S_EGringExtension

    Attributes:
        phi_bottom (float): 属性 下孔径
        installation (int): 属性 設置段
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "phi_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "installation": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPenetration_S_EGringExtension"


class StbSecPenetrationSHiringExtension(StBridgeElement):
    """ハイリング拡張情報：StbSecPenetration_S_HiringExtension

    Attributes:
        length_stick (float): 属性 スティック長さ
        wide_stick (float): 属性 スティックの幅
        protrude_stick (float): 属性
        lh_stick (float): 属性 スティック取り付け寸法
        clear_stick (float): 属性 スティック端からフランジスプライス端までの必要クリアランス
        phi_bottom (float): 属性 下孔径
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "length_stick": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "wide_stick": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "protrude_stick": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "lh_stick": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="Lh_stick"
        ),
        "clear_stick": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "phi_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPenetration_S_HiringExtension"


class StbSecPenetrationS(StBridgeElement):
    """S梁貫通孔補強仕様：StbSecPenetration_S

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        phi (float): 属性 貫通孔径
        type (StbSecPenetrationSType): 属性 補強工法以下のいずれかEG（EGリング）FR（フリードーナツ）HI（ハイリング）OS（OSリング）NO（無補強）CO（在来補強）
        model (str): 属性 リング型式名
        phi_ring (float): 属性 リング外径
        protrude (float): 属性 リングのWeb面からの突出寸法
        clear (float): 属性 リング縁からの必要クリアランス
        stb_sec_penetration_s_hiring_extension (StbSecPenetrationSHiringExtension): 子要素 StbSecPenetration_S_HiringExtension(ハイリング拡張情報)
        stb_sec_penetration_s_egring_extension (StbSecPenetrationSEgringExtension): 子要素 StbSecPenetration_S_EGringExtension(EGリング拡張情報)
        stb_sec_penetration_s_frring_extension (StbSecPenetrationSFrringExtension): 子要素 StbSecPenetration_S_FRringExtension(フリードーナツ拡張情報)
        stb_sec_penetration_s_osring_extension (StbSecPenetrationSOsringExtension): 子要素 StbSecPenetration_S_OSringExtension(OSリング拡張情報)
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
        "phi": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "type": _FI(
            py_type=StbSecPenetrationSType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("EG", "FR", "HI", "OS", "NO", "CO"),
        ),
        "model": _FI(py_type=str, data_type=_DT.STR),
        "phi_ring": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "protrude": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "clear": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_penetration_s_hiring_extension": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPenetrationSHiringExtension
        ),
        "stb_sec_penetration_s_egring_extension": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPenetrationSEgringExtension
        ),
        "stb_sec_penetration_s_frring_extension": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPenetrationSFrringExtension
        ),
        "stb_sec_penetration_s_osring_extension": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPenetrationSOsringExtension
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPenetration_S"


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
        length_x (float): 属性 開口寸法(X)
        length_y (float): 属性 開口寸法(Y)
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
        "stb_sec_bar_arrangement_open_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementOpenRc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecOpen_RC"


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


class StbSecPilePrecastCertified(StBridgeElement):
    """既製コンクリート杭 認定工法：StbSecPilePrecastCertified

    Attributes:
        name (str): 属性 認定工法
        stb_sec_figure_pile_precast (StbSecFigurePilePrecast): 子要素 StbSecFigurePilePrecast(既成コンクリート杭断面形状)
        stb_certified_method_key_value (list[StbCertifiedMethodKeyValue]): 子要素 StbCertifiedMethodKeyValue(認定工法特有の属性と値)
        stb_certification_number (list[StbCertificationNumber]): 子要素 StbCertificationNumber(認定番号)
        stb_sec_pile_precast_joint (list[StbSecPilePrecastJoint]): 子要素 StbSecPilePrecastJoint(継手)
        stb_sec_pile_precast_connection (StbSecPilePrecastConnection): 子要素 StbSecPilePrecastConnection(既製杭 杭頭接合)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_figure_pile_precast": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type="StbSecFigurePilePrecast",
        ),
        "stb_certified_method_key_value": _FI(
            kind=_FK.ELEMENT, py_type="list[StbCertifiedMethodKeyValue]"
        ),
        "stb_certification_number": _FI(
            kind=_FK.ELEMENT, py_type="list[StbCertificationNumber]"
        ),
        "stb_sec_pile_precast_joint": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecPilePrecastJoint]"
        ),
        "stb_sec_pile_precast_connection": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecPilePrecastConnection"
        ),
    }


class StbSecPilePrecastConnectionCertified(StBridgeElement):
    """既製杭 杭頭接合 認定工法：StbSecPilePrecastConnectionCertified

    Attributes:
        name (str): 属性 杭頭接合 工法名
        stb_certified_method_key_value (list[StbCertifiedMethodKeyValue]): 子要素 StbCertifiedMethodKeyValue(認定工法特有の属性と値)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_certified_method_key_value": _FI(
            kind=_FK.ELEMENT, py_type="list[StbCertifiedMethodKeyValue]"
        ),
    }


class StbSecPilePrecastConnectionConventional(StBridgeElement):
    """既製杭 杭頭接合 在来工法：StbSecPilePrecastConnectionConventional

    Attributes:
        d_pile_head (str): 属性 杭頭補強筋の径
        n_pile_head (int): 属性 杭頭補強筋の本数
        strength_pile_head (str): 属性
        d_inner (str): 属性 中詰めの鉄筋径
        n_inner (int): 属性 中詰めの鉄筋本数
        strength_inner (str): 属性 中詰めの鉄筋強度
        strength_inner_concrete (str): 属性 中詰めコンクリート
        concrete_depth (float): 属性 中詰めコンクリート深さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_pile_head": _FI(py_type=str, data_type=_DT.STR, xml_name="D_pile_head"),
        "n_pile_head": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_pile_head",
        ),
        "strength_pile_head": _FI(py_type=str, data_type=_DT.STR),
        "d_inner": _FI(py_type=str, data_type=_DT.STR, xml_name="D_inner"),
        "n_inner": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_inner",
        ),
        "strength_inner": _FI(py_type=str, data_type=_DT.STR),
        "strength_inner_concrete": _FI(py_type=str, data_type=_DT.STR),
        "concrete_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbSecPilePrecastConnection(StBridgeElement):
    """既製杭 杭頭接合：StbSecPilePrecastConnection

    Attributes:
        stb_sec_pile_precast_connection_conventional (StbSecPilePrecastConnectionConventional): 子要素 StbSecPilePrecastConnectionConventional(既製杭 杭頭接合 在来工法)
        stb_sec_pile_precast_connection_certified (StbSecPilePrecastConnectionCertified): 子要素 StbSecPilePrecastConnectionCertified(既製杭 杭頭接合 認定工法)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_pile_precast_connection_conventional": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbSecPilePrecastConnectionConventional,
        ),
        "stb_sec_pile_precast_connection_certified": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPilePrecastConnectionCertified
        ),
    }


class StbSecPilePrecastJointMechanical(StBridgeElement):
    """StbSecPilePrecastJointMechanical

    Attributes:
        product_code (str): 属性
        release_time (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbSecPilePrecastJointWeld(StBridgeElement):
    """溶接継手：StbSecPilePrecastJointWeld

    Attributes:
        name (str): 属性 溶接工法名
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR),
    }


class StbSecPilePrecastJoint(StBridgeElement):
    """継手：StbSecPilePrecastJoint

    Attributes:
        id_order (int): 属性
        stb_sec_pile_precast_joint_weld (StbSecPilePrecastJointWeld): 子要素 StbSecPilePrecastJointWeld(溶接継手)
        stb_sec_pile_precast_joint_mechanical (StbSecPilePrecastJointMechanical): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_sec_pile_precast_joint_weld": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPilePrecastJointWeld
        ),
        "stb_sec_pile_precast_joint_mechanical": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPilePrecastJointMechanical
        ),
    }


class StbSecPilePrecastProduct(StBridgeElement):
    """StbSecPilePrecastProduct

    Attributes:
        id_order (int): 属性
        product_code (str): 属性
        release_time (str): 属性
        length_pile (float): 属性
        top_length (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "top_length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbSecPilePrecastNodularCprc(StBridgeElement):
    """既製コンクリート杭断面形状・節付CPRC杭：StbSecPilePrecastNodular_CPRC

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d1 (float): 属性 外径（軸部）
        d2 (float): 属性 外形（節部）
        tc (float): 属性 厚さ
        strength_concrete (str): 属性 コンクリート強度
        d_pc (float): 属性 PC鋼棒径
        n_pc (int): 属性 PC鋼棒本数
        strength_pc (str): 属性 PC鋼棒強度
        d_bar (str): 属性 異形棒鋼径
        n_bar (int): 属性 異形棒鋼本数
        strength_bar (str): 属性 異形棒鋼強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecastNodular_CPRC"


class StbSecPilePrecastNodularPrc(StBridgeElement):
    """既製コンクリート杭断面形状・節付PRC杭：StbSecPilePrecastNodular_PRC

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d1 (float): 属性 外径（軸部）
        d2 (float): 属性 外形（節部）
        tc (float): 属性 厚さ
        strength_concrete (str): 属性 コンクリート強度
        d_pc (float): 属性 PC鋼棒径
        n_pc (int): 属性 PC鋼棒本数
        strength_pc (str): 属性 PC鋼棒強度
        d_bar (str): 属性 異形棒鋼径
        n_bar (int): 属性 異形棒鋼本数
        strength_bar (str): 属性 異形棒鋼強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecastNodular_PRC"


class StbSecPilePrecastNodularPhc(StBridgeElement):
    """既製コンクリート杭断面形状・節付PHC杭：StbSecPilePrecastNodular_PHC

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d1 (float): 属性 外径（軸部）
        d2 (float): 属性 外形（節部）
        t (float): 属性 厚さ
        strength_concrete (str): 属性 コンクリート強度
        d_pc (float): 属性 PC鋼棒径
        n_pc (int): 属性 PC鋼棒本数
        strength_pc (str): 属性 PC鋼棒強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecastNodular_PHC"


class StbSecPilePrecastCprc(StBridgeElement):
    """既製コンクリート杭断面形状・CPRC杭：StbSecPilePrecast_CPRC

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d (float): 属性 外径
        tc (float): 属性 厚さ
        strength_concrete (str): 属性 コンクリート強度
        d_pc (float): 属性 PC鋼棒径
        n_pc (int): 属性 PC鋼棒本数
        strength_pc (str): 属性 PC鋼棒強度
        d_bar (str): 属性 異形棒鋼径
        n_bar (int): 属性 異形棒鋼本数
        strength_bar (str): 属性 異形棒鋼強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecast_CPRC"


class StbSecPilePrecastPrc(StBridgeElement):
    """既製コンクリート杭断面形状・PRC杭：StbSecPilePrecast_PRC

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d (float): 属性 外径
        tc (float): 属性 厚さ
        strength_concrete (str): 属性 コンクリート強度
        d_pc (float): 属性 PC鋼棒径
        n_pc (int): 属性 PC鋼棒本数
        strength_pc (str): 属性 PC鋼棒強度
        d_bar (str): 属性 異形棒鋼径
        n_bar (int): 属性 異形棒鋼本数
        strength_bar (str): 属性 異形棒鋼強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecast_PRC"


class StbSecPilePrecastSc(StBridgeElement):
    """既製コンクリート杭断面形状・SC杭：StbSecPilePrecast_SC

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d (float): 属性 外径
        tc (float): 属性 肉厚(含鋼管)
        ts (float): 属性 鋼管の板厚
        strength_concrete (str): 属性 コンクリート強度
        strength_pipe (str): 属性 鋼管の鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecast_SC"


class StbSecPilePrecastSt(StBridgeElement):
    """既製コンクリート杭断面形状・ST杭：StbSecPilePrecast_ST

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d1 (float): 属性 外径（本体部）
        d2 (float): 属性 外径（拡径部）
        t1 (float): 属性 厚さ（本体部）
        t2 (float): 属性 厚さ（拡径部）
        strength_concrete (str): 属性 コンクリート強度
        d_pc (float): 属性 PC鋼棒径
        n_pc (int): 属性 PC鋼棒本数
        strength_pc (str): 属性 PC鋼棒強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecast_ST"


class StbSecPilePrecastPhc(StBridgeElement):
    """既製コンクリート杭断面形状・PHC杭：StbSecPilePrecast_PHC

    Attributes:
        id_order (int): 属性 継杭の位置
        length_pile (float): 属性 杭の長さ
        kind (str): 属性 種類
        d (float): 属性 外径
        t (float): 属性 厚さ
        strength_concrete (str): 属性 コンクリート強度
        d_pc (float): 属性 PC鋼棒径
        n_pc (int): 属性 PC鋼棒本数
        strength_pc (str): 属性 PC鋼棒強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
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
    _xml_element_name: ClassVar[str] = "StbSecPilePrecast_PHC"


class StbSecFigurePilePrecast(StBridgeElement):
    """既成コンクリート杭断面形状：StbSecFigurePilePrecast

    Attributes:
        stb_sec_pile_precast_phc (list[StbSecPilePrecastPhc]): 子要素 StbSecPilePrecast_PHC(既製コンクリート杭断面形状・PHC杭)
        stb_sec_pile_precast_st (list[StbSecPilePrecastSt]): 子要素 StbSecPilePrecast_ST(既製コンクリート杭断面形状・ST杭)
        stb_sec_pile_precast_sc (list[StbSecPilePrecastSc]): 子要素 StbSecPilePrecast_SC(既製コンクリート杭断面形状・SC杭)
        stb_sec_pile_precast_prc (list[StbSecPilePrecastPrc]): 子要素 StbSecPilePrecast_PRC(既製コンクリート杭断面形状・PRC杭)
        stb_sec_pile_precast_cprc (list[StbSecPilePrecastCprc]): 子要素 StbSecPilePrecast_CPRC(既製コンクリート杭断面形状・CPRC杭)
        stb_sec_pile_precast_nodular_phc (list[StbSecPilePrecastNodularPhc]): 子要素 StbSecPilePrecastNodular_PHC(既製コンクリート杭断面形状・節付PHC杭)
        stb_sec_pile_precast_nodular_prc (list[StbSecPilePrecastNodularPrc]): 子要素 StbSecPilePrecastNodular_PRC(既製コンクリート杭断面形状・節付PRC杭)
        stb_sec_pile_precast_nodular_cprc (list[StbSecPilePrecastNodularCprc]): 子要素 StbSecPilePrecastNodular_CPRC(既製コンクリート杭断面形状・節付CPRC杭)
        stb_sec_pile_precast_product (list[StbSecPilePrecastProduct]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_pile_precast_phc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastPhc]
        ),
        "stb_sec_pile_precast_st": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastSt]
        ),
        "stb_sec_pile_precast_sc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastSc]
        ),
        "stb_sec_pile_precast_prc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastPrc]
        ),
        "stb_sec_pile_precast_cprc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastCprc]
        ),
        "stb_sec_pile_precast_nodular_phc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastNodularPhc]
        ),
        "stb_sec_pile_precast_nodular_prc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastNodularPrc]
        ),
        "stb_sec_pile_precast_nodular_cprc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastNodularCprc]
        ),
        "stb_sec_pile_precast_product": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastProduct]
        ),
    }


class StbSecPilePrecastConventional(StBridgeElement):
    """既製コンクリート 一般工法：StbSecPilePrecastConventional

    Attributes:
        construction_method (StbSecPilePrecastConventionalConstructionMethod): 属性 工法 以下のいずれかDRIVING(打ち込み杭)BURIED(埋込杭)
        stb_sec_figure_pile_precast (StbSecFigurePilePrecast): 子要素 StbSecFigurePilePrecast(既成コンクリート杭断面形状)
        stb_sec_pile_precast_joint (list[StbSecPilePrecastJoint]): 子要素 StbSecPilePrecastJoint(継手)
        stb_sec_pile_precast_connection (StbSecPilePrecastConnection): 子要素 StbSecPilePrecastConnection(既製杭 杭頭接合)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "construction_method": _FI(
            py_type=StbSecPilePrecastConventionalConstructionMethod,
            data_type=_DT.STR_ENUM,
            choices=("DRIVING", "BURIED"),
        ),
        "stb_sec_figure_pile_precast": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecFigurePilePrecast,
        ),
        "stb_sec_pile_precast_joint": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastJoint]
        ),
        "stb_sec_pile_precast_connection": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPilePrecastConnection
        ),
    }


class StbSecPilePrecast(StBridgeElement):
    """既製コンクリート杭断面：StbSecPilePrecast

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        stb_sec_pile_precast_conventional (StbSecPilePrecastConventional): 子要素 StbSecPilePrecastConventional(既製コンクリート 一般工法)
        stb_sec_pile_precast_certified (list[StbSecPilePrecastCertified]): 子要素 StbSecPilePrecastCertified(既製コンクリート杭 認定工法)
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
        "stb_sec_pile_precast_conventional": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPilePrecastConventional
        ),
        "stb_sec_pile_precast_certified": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPilePrecastCertified]
        ),
    }


class StbSecPileSCertified(StBridgeElement):
    """鋼管杭 認定工法：StbSecPile_S_Certified

    Attributes:
        name (str): 属性 認定工法名
        stb_sec_figure_pile_s (StbSecFigurePileS): 子要素 StbSecFigurePile_S(鋼管杭断面形状)
        stb_certified_method_key_value (list[StbCertifiedMethodKeyValue]): 子要素 StbCertifiedMethodKeyValue(認定工法特有の属性と値)
        stb_certification_number (list[StbCertificationNumber]): 子要素 StbCertificationNumber(認定番号)
        stb_sec_pile_s_joint (list[StbSecPileSJoint]): 子要素 StbSecPile_S_Joint(鋼管杭継手)
        stb_sec_pile_s_connection (StbSecPileSConnection): 子要素 StbSecPile_S_Connection(鋼管杭杭頭接合)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_figure_pile_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbSecFigurePileS"
        ),
        "stb_certified_method_key_value": _FI(
            kind=_FK.ELEMENT, py_type="list[StbCertifiedMethodKeyValue]"
        ),
        "stb_certification_number": _FI(
            kind=_FK.ELEMENT, py_type="list[StbCertificationNumber]"
        ),
        "stb_sec_pile_s_joint": _FI(kind=_FK.ELEMENT, py_type="list[StbSecPileSJoint]"),
        "stb_sec_pile_s_connection": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecPileSConnection"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Certified"


class StbSecPileSConnection(StBridgeElement):
    """鋼管杭杭頭接合：StbSecPile_S_Connection

    Attributes:
        d_pile_head (str): 属性 杭頭補強筋の径
        n_pile_head (int): 属性 杭頭補強筋の本数
        strength_pile_head (str): 属性
        d_inner (str): 属性 中詰め鉄筋径
        n_inner (int): 属性 中詰め鉄筋本数
        strength_inner (str): 属性 中詰め鉄筋強度
        strength_inner_concrete (str): 属性 中詰めコンクリート
        concrete_depth (float): 属性 中詰めコンクリート深さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_pile_head": _FI(py_type=str, data_type=_DT.STR, xml_name="D_pile_head"),
        "n_pile_head": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_pile_head",
        ),
        "strength_pile_head": _FI(py_type=str, data_type=_DT.STR),
        "d_inner": _FI(py_type=str, data_type=_DT.STR, xml_name="D_inner"),
        "n_inner": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_inner",
        ),
        "strength_inner": _FI(py_type=str, data_type=_DT.STR),
        "strength_inner_concrete": _FI(py_type=str, data_type=_DT.STR),
        "concrete_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Connection"


class StbSecPileSJointMechanical(StBridgeElement):
    """StbSecPileSJointMechanical：StbSecPile_S_JointMechanical

    Attributes:
        product_code (str): 属性
        release_time (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_JointMechanical"


class StbSecPileSJointWeld(StBridgeElement):
    """鋼管杭溶接継手：StbSecPile_S_JointWeld

    Attributes:
        name (str): 属性 溶接工法名
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_JointWeld"


class StbSecPileSJoint(StBridgeElement):
    """鋼管杭継手：StbSecPile_S_Joint

    Attributes:
        id_order (int): 属性 継手位置
        stb_sec_pile_s_joint_weld (StbSecPileSJointWeld): 子要素 StbSecPile_S_JointWeld(鋼管杭溶接継手)
        stb_sec_pile_s_joint_mechanical (StbSecPileSJointMechanical): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_sec_pile_s_joint_weld": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileSJointWeld
        ),
        "stb_sec_pile_s_joint_mechanical": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileSJointMechanical
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Joint"


class StbSecPileSProduct(StBridgeElement):
    """鋼管杭断面形状・製品指定：StbSecPile_S_Product

    Attributes:
        id_order (int): 属性 継杭の位置
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        length_pile (float): 属性 杭の長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "length_pile": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Product"


class StbSecPileSTaper(StBridgeElement):
    """鋼管杭断面形状・テーパー管杭：StbSecPile_S_Taper

    Attributes:
        id_order (int): 属性 継杭の位置
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
        stb_sec_pile_s_product (list[StbSecPileSProduct]): 子要素 StbSecPile_S_Product(鋼管杭断面形状・製品指定)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_pile_s_straight": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileSStraight]
        ),
        "stb_sec_pile_s_rotational": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileSRotational]
        ),
        "stb_sec_pile_s_taper": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileSTaper]),
        "stb_sec_pile_s_product": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileSProduct]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigurePile_S"


class StbSecPileSConventional(StBridgeElement):
    """鋼管杭 一般工法：StbSecPile_S_Conventional

    Attributes:
        construction_method (StbSecPileSConventionalConstructionMethod): 属性 工法 以下のいずれかDRIVING(打ち込み杭)BURIED(埋込杭)
        stb_sec_figure_pile_s (StbSecFigurePileS): 子要素 StbSecFigurePile_S(鋼管杭断面形状)
        stb_sec_pile_s_joint (list[StbSecPileSJoint]): 子要素 StbSecPile_S_Joint(鋼管杭継手)
        stb_sec_pile_s_connection (StbSecPileSConnection): 子要素 StbSecPile_S_Connection(鋼管杭杭頭接合)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "construction_method": _FI(
            py_type=StbSecPileSConventionalConstructionMethod,
            data_type=_DT.STR_ENUM,
            choices=("DRIVING", "BURIED"),
        ),
        "stb_sec_figure_pile_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type=StbSecFigurePileS
        ),
        "stb_sec_pile_s_joint": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileSJoint]),
        "stb_sec_pile_s_connection": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileSConnection
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S_Conventional"


class StbSecPileS(StBridgeElement):
    """鋼管杭断面：StbSecPile_S

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        stb_sec_pile_s_conventional (StbSecPileSConventional): 子要素 StbSecPile_S_Conventional(鋼管杭 一般工法)
        stb_sec_pile_s_certified (list[StbSecPileSCertified]): 子要素 StbSecPile_S_Certified(鋼管杭 認定工法)
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
        "stb_sec_pile_s_conventional": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileSConventional
        ),
        "stb_sec_pile_s_certified": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileSCertified]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_S"


class StbSecBarArrangementPileRcCertified(StBridgeElement):
    """ＲＣ杭断面配筋：StbSecBarArrangementPile_RC_Certified

    Attributes:
        depth_cover (float): 属性 かぶり厚さ
        is_spiral (bool): 属性 帯筋がスパイラルか否か
        stb_sec_bar_pile_rc_same (StbSecBarPileRcSame): 子要素 StbSecBarPile_RC_Same(ＲＣ杭断面配筋・全断面)
        stb_sec_bar_pile_rc_top_bottom (list[StbSecBarPileRcTopBottom]): 子要素 StbSecBarPile_RC_TopBottom(ＲＣ杭断面配筋・杭頭脚別)
        stb_sec_bar_pile_rc_top_center_bottom (list[StbSecBarPileRcTopCenterBottom]): 子要素 StbSecBarPile_RC_TopCenterBottom(ＲＣ杭断面配筋・杭頭軸部杭脚)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "is_spiral": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isSpiral"),
        "stb_sec_bar_pile_rc_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBarPileRcSame"
        ),
        "stb_sec_bar_pile_rc_top_bottom": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type="list[StbSecBarPileRcTopBottom]"
        ),
        "stb_sec_bar_pile_rc_top_center_bottom": _FI(
            kind=_FK.ELEMENT,
            max_occurs=3,
            py_type="list[StbSecBarPileRcTopCenterBottom]",
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementPile_RC_Certified"


class StbSecFigurePileRcCertified(StBridgeElement):
    """ＲＣ杭断面形状 認定工法：StbSecFigurePile_RC_Certified

    Attributes:
        d (float): 属性 杭径
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
    _xml_element_name: ClassVar[str] = "StbSecFigurePile_RC_Certified"


class StbSecPileRcCertified(StBridgeElement):
    """RC杭断面 認定工法：StbSecPile_RC_Certified

    Attributes:
        name (str): 属性 認定工法名
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_pile_rc_certified (StbSecFigurePileRcCertified): 子要素 StbSecFigurePile_RC_Certified(ＲＣ杭断面形状 認定工法)
        stb_sec_bar_arrangement_pile_rc_certified (StbSecBarArrangementPileRcCertified): 子要素 StbSecBarArrangementPile_RC_Certified(ＲＣ杭断面配筋)
        stb_certified_method_key_value (list[StbCertifiedMethodKeyValue]): 子要素 StbCertifiedMethodKeyValue(認定工法特有の属性と値)
        stb_certification_number (list[StbCertificationNumber]): 子要素 StbCertificationNumber(認定番号)
        stb_sec_pile_rc_connection (StbSecPileRcConnection): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_pile_rc_certified": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecFigurePileRcCertified,
        ),
        "stb_sec_bar_arrangement_pile_rc_certified": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementPileRcCertified
        ),
        "stb_certified_method_key_value": _FI(
            kind=_FK.ELEMENT, py_type="list[StbCertifiedMethodKeyValue]"
        ),
        "stb_certification_number": _FI(
            kind=_FK.ELEMENT, py_type="list[StbCertificationNumber]"
        ),
        "stb_sec_pile_rc_connection": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecPileRcConnection"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_Certified"


class StbCertifiedMethodKeyValue(StBridgeElement):
    """認定工法特有の属性と値：StbCertifiedMethodKeyValue

    Attributes:
        key (str): 属性
        value (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "key": _FI(py_type=str, data_type=_DT.STR, required=True),
        "value": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbSecPileRcConnectionCertified(StBridgeElement):
    """StbSecPileRcConnectionCertified：StbSecPile_RC_ConnectionCertified

    Attributes:
        name (str): 属性
        stb_certified_method_key_value (list[StbCertifiedMethodKeyValue]): 子要素 StbCertifiedMethodKeyValue(認定工法特有の属性と値)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_certified_method_key_value": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCertifiedMethodKeyValue]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ConnectionCertified"


class StbSecPileRcConnection(StBridgeElement):
    """StbSecPileRcConnection：StbSecPile_RC_Connection

    Attributes:
        stb_sec_pile_rc_connection_certified (StbSecPileRcConnectionCertified): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_pile_rc_connection_certified": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecPileRcConnectionCertified,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_Connection"


class StbSecBarPileRcTopCenterBottom(StBridgeElement):
    """ＲＣ杭断面配筋・杭頭軸部杭脚：StbSecBarPile_RC_TopCenterBottom

    Attributes:
        pos (StbSecBarPileRcTopCenterBottomPos): 属性
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_core (str): 属性
        d_band (str): 属性
        d_core_band (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_core (str): 属性
        strength_band (str): 属性
        strength_core_band (str): 属性
        n_main (int): 属性
        n_2nd_main (int): 属性
        n_core (int): 属性
        pitch_band (float): 属性
        pitch_core_band (float): 属性
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
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_core": _FI(py_type=str, data_type=_DT.STR, xml_name="D_core"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_core_band": _FI(py_type=str, data_type=_DT.STR, xml_name="D_core_band"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_core": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_core_band": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_2nd_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main",
        ),
        "n_core": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_core",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "pitch_core_band": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_lap_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarPile_RC_TopCenterBottom"


class StbSecBarPileRcTopBottom(StBridgeElement):
    """ＲＣ杭断面配筋・杭頭脚別：StbSecBarPile_RC_TopBottom

    Attributes:
        pos (StbSecBarPileRcTopBottomPos): 属性 配筋位置以下のいずれかTOP（杭頭）BOTTOM（杭脚）
        d_main (str): 属性 主筋：径
        d_2nd_main (str): 属性 束ね筋：径
        d_core (str): 属性 芯筋：径
        d_band (str): 属性 帯筋：径
        d_core_band (str): 属性 芯帯筋：径
        strength_main (str): 属性 主筋：鉄筋強度
        strength_2nd_main (str): 属性 束ね筋：鉄筋強度
        strength_core (str): 属性 芯筋：鉄筋強度
        strength_band (str): 属性 帯筋：鉄筋強度
        strength_core_band (str): 属性 芯帯筋：径
        n_main (int): 属性 主筋：本数
        n_2nd_main (int): 属性 束ね筋：本数
        n_core (int): 属性 芯筋：本数
        pitch_band (float): 属性 帯筋：ピッチ
        pitch_core_band (float): 属性 芯帯筋：ピッチ
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
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_core": _FI(py_type=str, data_type=_DT.STR, xml_name="D_core"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_core_band": _FI(py_type=str, data_type=_DT.STR, xml_name="D_core_band"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_core": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_core_band": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_2nd_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main",
        ),
        "n_core": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_core",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "pitch_core_band": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length_lap_bar": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarPile_RC_TopBottom"


class StbSecBarPileRcSame(StBridgeElement):
    """ＲＣ杭断面配筋・全断面：StbSecBarPile_RC_Same

    Attributes:
        d_main (str): 属性
        d_2nd_main (str): 属性
        d_core (str): 属性
        d_band (str): 属性
        d_core_band (str): 属性
        strength_main (str): 属性
        strength_2nd_main (str): 属性
        strength_core (str): 属性
        strength_band (str): 属性
        strength_core_band (str): 属性
        n_main (int): 属性
        n_2nd_main (int): 属性
        n_core (int): 属性
        pitch_band (float): 属性
        pitch_core_band (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_2nd_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_2nd_main"),
        "d_core": _FI(py_type=str, data_type=_DT.STR, xml_name="D_core"),
        "d_band": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_band"),
        "d_core_band": _FI(py_type=str, data_type=_DT.STR, xml_name="D_core_band"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_2nd_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_core": _FI(py_type=str, data_type=_DT.STR),
        "strength_band": _FI(py_type=str, data_type=_DT.STR),
        "strength_core_band": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_2nd_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_2nd_main",
        ),
        "n_core": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_core",
        ),
        "pitch_band": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "pitch_core_band": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarPile_RC_Same"


class StbSecBarArrangementPileRcConventional(StBridgeElement):
    """ＲＣ杭断面配筋：StbSecBarArrangementPile_RC_Conventional

    Attributes:
        depth_cover (float): 属性 かぶり厚さ
        depth_cover_top (float): 属性 拡頭部かぶり厚さ
        is_spiral (bool): 属性 帯筋がスパイラルか否か
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
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementPile_RC_Conventional"


class StbSecPileRcConventionalExtendedTopFoot(StBridgeElement):
    """ＲＣ杭断面形状・頂部脚部拡大：StbSecPile_RC_ConventionalExtendedTopFoot

    Attributes:
        d_extended_top (float): 属性 拡頭径
        d_axial (float): 属性 軸径
        d_extended_foot (float): 属性 拡底径
        angle_extended_top_taper (float): 属性 拡頭部のテーパー角度
        length_extended_foot (float): 属性 拡底部の立ち上がり長さ
        angle_extended_foot_taper (float): 属性 拡底部の傾斜角度
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
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ConventionalExtendedTopFoot"


class StbSecPileRcConventionalExtendedTop(StBridgeElement):
    """ＲＣ杭断面形状・頂部拡大：StbSecPile_RC_ConventionalExtendedTop

    Attributes:
        d_extended_top (float): 属性 拡頭径
        d_axial (float): 属性 軸径
        angle_extended_top_taper (float): 属性 拡頭部のテーパー角度
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
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ConventionalExtendedTop"


class StbSecPileRcConventionalExtendedFoot(StBridgeElement):
    """ＲＣ杭断面形状・脚部拡大：StbSecPile_RC_ConventionalExtendedFoot

    Attributes:
        d_axial (float): 属性 軸径
        d_extended_foot (float): 属性 拡底径
        length_extended_foot (float): 属性 拡底部の立ち上がり長さ
        angle_extended_foot_taper (float): 属性 拡底部の傾斜角度
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
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ConventionalExtendedFoot"


class StbSecPileRcConventionalStraight(StBridgeElement):
    """ＲＣ杭断面形状・ストレート：StbSecPile_RC_ConventionalStraight

    Attributes:
        d (float): 属性 杭径
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
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_ConventionalStraight"


class StbSecFigurePileRcConventional(StBridgeElement):
    """ＲＣ杭断面形状 一般工法：StbSecFigurePile_RC_Conventional

    Attributes:
        length_pipe (float): 属性 鋼管部長さ
        t_pipe (float): 属性 鋼管の厚さ
        strength_pipe (str): 属性 鋼管の鉄骨強度
        stb_sec_pile_rc_conventional_straight (StbSecPileRcConventionalStraight): 子要素 StbSecPile_RC_ConventionalStraight(ＲＣ杭断面形状・ストレート)
        stb_sec_pile_rc_conventional_extended_foot (StbSecPileRcConventionalExtendedFoot): 子要素 StbSecPile_RC_ConventionalExtendedFoot(ＲＣ杭断面形状・脚部拡大)
        stb_sec_pile_rc_conventional_extended_top (StbSecPileRcConventionalExtendedTop): 子要素 StbSecPile_RC_ConventionalExtendedTop(ＲＣ杭断面形状・頂部拡大)
        stb_sec_pile_rc_conventional_extended_top_foot (StbSecPileRcConventionalExtendedTopFoot): 子要素 StbSecPile_RC_ConventionalExtendedTopFoot(ＲＣ杭断面形状・頂部脚部拡大)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "length_pipe": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "t_pipe": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_pipe": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_pile_rc_conventional_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcConventionalStraight
        ),
        "stb_sec_pile_rc_conventional_extended_foot": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcConventionalExtendedFoot
        ),
        "stb_sec_pile_rc_conventional_extended_top": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcConventionalExtendedTop
        ),
        "stb_sec_pile_rc_conventional_extended_top_foot": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbSecPileRcConventionalExtendedTopFoot,
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigurePile_RC_Conventional"


class StbSecPileRcConventional(StBridgeElement):
    """ＲＣ杭断面 一般工法：StbSecPile_RC_Conventional

    Attributes:
        construction_method (StbSecPileRcConventionalConstructionMethod): 属性 工法 以下のいずれかEARTHDRILL(アースドリル工法)REVERSE(リバース工法)ALLCASING(オールケーシング工法)BH(BH工法)SHINSO(深礎工法)
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_figure_pile_rc_conventional (StbSecFigurePileRcConventional): 子要素 StbSecFigurePile_RC_Conventional(ＲＣ杭断面形状 一般工法)
        stb_sec_bar_arrangement_pile_rc_conventional (StbSecBarArrangementPileRcConventional): 子要素 StbSecBarArrangementPile_RC_Conventional(ＲＣ杭断面配筋)
        stb_sec_pile_rc_connection (StbSecPileRcConnection): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "construction_method": _FI(
            py_type=StbSecPileRcConventionalConstructionMethod,
            data_type=_DT.STR_ENUM,
            choices=("EARTHDRILL", "REVERSE", "ALLCASING", "BH", "SHINSO"),
        ),
        "strength_concrete": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_figure_pile_rc_conventional": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecFigurePileRcConventional,
        ),
        "stb_sec_bar_arrangement_pile_rc_conventional": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbSecBarArrangementPileRcConventional,
        ),
        "stb_sec_pile_rc_connection": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcConnection
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecPile_RC_Conventional"


class StbSecPileRc(StBridgeElement):
    """ＲＣ杭断面：StbSecPile_RC

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        stb_sec_pile_rc_conventional (StbSecPileRcConventional): 子要素 StbSecPile_RC_Conventional(ＲＣ杭断面 一般工法)
        stb_sec_pile_rc_certified (list[StbSecPileRcCertified]): 子要素 StbSecPile_RC_Certified(RC杭断面 認定工法)
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
        "stb_sec_pile_rc_conventional": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecPileRcConventional
        ),
        "stb_sec_pile_rc_certified": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPileRcCertified]
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
        length (float): 属性 主筋の鉄筋切替位置
        main_type (StbSecBarFoundationRcContinuousMainType): 属性 主筋方向元端先端で配筋を切り替える場合の配筋パターンを示す以下のいずれかの値をとるSYMMETRICALASYMMETRICAL
        is_vertical (bool): 属性 外周の縦筋の扱い上端筋の場合は立ち下げるか否か下端筋の場合は立ち上げるか否か
        length_vertical (float): 属性 上端筋の場合は立ち下げ長さ下端筋の場合は立ち上げ長さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarFoundationRcContinuousPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "MAIN_BASE_TOP",
                "MAIN_BASE_BOTTOM",
                "MAIN_TIP_TOP",
                "MAIN_TIP_BOTTOM",
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
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "main_type": _FI(
            py_type=StbSecBarFoundationRcContinuousMainType,
            data_type=_DT.STR_ENUM,
            choices=("SYMMETRICAL", "ASYMMETRICAL"),
        ),
        "is_vertical": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isVertical"),
        "length_vertical": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarFoundation_RC_Continuous"


class StbSecBarFoundationRcThreeWay(StBridgeElement):
    """ＲＣ基礎断面配筋・三方：StbSecBarFoundation_RC_ThreeWay

    Attributes:
        pos (StbSecBarFoundationRcThreeWayPos): 属性 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）OUTSIDE_TOP（外周上端）OUTSIDE_BOTTOM（外周下端）HORIZONTAL（横）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        is_vertical (bool): 属性 外周の縦筋の扱い上端筋の場合は立ち下げるか否か下端筋の場合は立ち上げるか否か
        length_vertical (float): 属性 上端筋の場合は立ち下げ長さ下端筋の場合は立ち上げ長さ
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
        "is_vertical": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isVertical"),
        "length_vertical": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarFoundation_RC_ThreeWay"


class StbSecBarFoundationRcTriangle(StBridgeElement):
    """ＲＣ基礎断面配筋・三角：StbSecBarFoundation_RC_Triangle

    Attributes:
        pos (StbSecBarFoundationRcTrianglePos): 属性 配筋位置 以下のいずれかMAIN_TOP（主筋方向上端）MAIN_BOTTOM（主筋方向下端）TRANSVERSE_TOP（配力筋方向上端）TRANSVERSE_BOTTOM（配力筋方向下端）HORIZONTAL（横）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        is_vertical (bool): 属性 外周の縦筋の扱い上端筋の場合は立ち下げるか否か下端筋の場合は立ち上げるか否か
        length_vertical (float): 属性 上端筋の場合は立ち下げ長さ下端筋の場合は立ち上げ長さ
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
        "is_vertical": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isVertical"),
        "length_vertical": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarFoundation_RC_Triangle"


class StbSecBarFoundationRcRect(StBridgeElement):
    """ＲＣ基礎断面配筋・矩形：StbSecBarFoundation_RC_Rect

    Attributes:
        pos (StbSecBarFoundationRcRectPos): 属性 配筋位置 以下のいずれかX_TOP（X方向上端）X_BOTTOM（X方向下端）Y_TOP（Y方向上端）Y_BOTTOM（Y方向下端）HORIZONTAL（横）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        n (int): 属性 本数
        is_vertical (bool): 属性 外周の縦筋の扱い上端筋の場合は立ち下げるか否か下端筋の場合は立ち上げるか否か
        length_vertical (float): 属性 上端筋の場合は立ち下げ長さ下端筋の場合は立ち上げ長さ
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
        "is_vertical": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isVertical"),
        "length_vertical": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
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
            max_occurs=7,
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
        width_chamfer_x (float): 属性 面取りＸ幅
        width_chamfer_y (float): 属性 面取りＹ幅
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
        "width_chamfer_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="width_chamfer_X",
        ),
        "width_chamfer_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="width_chamfer_Y",
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


class StbSecConnectionDampingDeviceVertical(StBridgeElement):
    """層上下接合型接合部：StbSecConnectionDampingDeviceVertical

    Attributes:
        method_start (StbSecConnectionDampingDeviceVerticalMethodStart): 属性 始端（下部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）、WELDING（溶接接合）
        t_plate_start (float): 属性 始端（下部）ベースプレート・厚さ
        strength_plate_start (str): 属性 同・鉄骨強度
        number_anchorbolt_start (int): 属性 始端（下部）アンカーボルト類・全本数
        name_anchorbolt_start (str): 属性 同・材料名称
        strength_anchorbolt_start (str): 属性 同・鉄骨強度
        method_end (StbSecConnectionDampingDeviceVerticalMethodEnd): 属性 終端（上部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）、WELDING（溶接接合）
        t_plate_end (float): 属性 終端（上部）ベースプレート・厚さ
        strength_plate_end (str): 属性 同・鉄骨強度
        number_anchorbolt_end (int): 属性 終端（上部）アンカーボルト類・全本数
        name_anchorbolt_end (str): 属性 同・材料名称
        strength_anchorbolt_end (str): 属性 同・鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "method_start": _FI(
            py_type=StbSecConnectionDampingDeviceVerticalMethodStart,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT", "WELDING"),
        ),
        "t_plate_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_start": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_start": _FI(
            py_type=int,
            data_type=_DT.NON_NEGATIVE_INTEGER,
            xml_type="nonNegativeInteger",
        ),
        "name_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "method_end": _FI(
            py_type=StbSecConnectionDampingDeviceVerticalMethodEnd,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT", "WELDING"),
        ),
        "t_plate_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_end": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_end": _FI(
            py_type=int,
            data_type=_DT.NON_NEGATIVE_INTEGER,
            xml_type="nonNegativeInteger",
        ),
        "name_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
    }


class StbSecConnectionDampingDeviceHorizontal(StBridgeElement):
    """水平方向接合型接合部：StbSecConnectionDampingDeviceHorizontal

    Attributes:
        method_start (StbSecConnectionDampingDeviceHorizontalMethodStart): 属性 始端（下部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）、THROUGH_BOLT（通しボルト接合）、WELDING（溶接接合）
        t_plate_start (float): 属性 始端（下部）ベースプレート・厚さ
        strength_plate_start (str): 属性 同・鉄骨強度
        number_anchorbolt_start (int): 属性 始端（下部）アンカーボルト類・全本数
        name_anchorbolt_start (str): 属性 同・材料名称
        strength_anchorbolt_start (str): 属性 同・鉄骨強度
        method_end (StbSecConnectionDampingDeviceHorizontalMethodEnd): 属性 終端（上部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）、THROUGH_BOLT（通しボルト接合）、WELDING（溶接接合）
        t_plate_end (float): 属性 終端（上部）ベースプレート・厚さ
        strength_plate_end (str): 属性 同・鉄骨強度
        number_anchorbolt_end (int): 属性 終端（上部）アンカーボルト類・全本数
        name_anchorbolt_end (str): 属性 同・材料名称
        strength_anchorbolt_end (str): 属性 同・鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "method_start": _FI(
            py_type=StbSecConnectionDampingDeviceHorizontalMethodStart,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT", "THROUGH_BOLT", "WELDING"),
        ),
        "t_plate_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_start": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_start": _FI(
            py_type=int,
            data_type=_DT.NON_NEGATIVE_INTEGER,
            xml_type="nonNegativeInteger",
        ),
        "name_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "method_end": _FI(
            py_type=StbSecConnectionDampingDeviceHorizontalMethodEnd,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT", "THROUGH_BOLT", "WELDING"),
        ),
        "t_plate_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_end": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_end": _FI(
            py_type=int,
            data_type=_DT.NON_NEGATIVE_INTEGER,
            xml_type="nonNegativeInteger",
        ),
        "name_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
    }


class StbSecConnectionDampingDevice(StBridgeElement):
    """制振装置断面・接合部：StbSecConnectionDampingDevice

    Attributes:
        stb_sec_connection_damping_device_horizontal (StbSecConnectionDampingDeviceHorizontal): 子要素 StbSecConnectionDampingDeviceHorizontal(水平方向接合型接合部)
        stb_sec_connection_damping_device_vertical (StbSecConnectionDampingDeviceVertical): 子要素 StbSecConnectionDampingDeviceVertical(層上下接合型接合部)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_connection_damping_device_horizontal": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbSecConnectionDampingDeviceHorizontal,
        ),
        "stb_sec_connection_damping_device_vertical": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbSecConnectionDampingDeviceVertical,
        ),
    }


class StbSecSpecificationDampingDevice(StBridgeElement):
    """制振装置断面・仕様指定：StbSecSpecificationDampingDevice

    Attributes:
    """

    _fields: ClassVar[dict[str, _FI]] = {}


class StbSecSteelFigureDampingDeviceHistory(StBridgeElement):
    """履歴系ダンパー・鉄骨断面形状：StbSecSteelFigureDampingDeviceHistory

    Attributes:
        shape (str): 属性 芯材鉄骨形状
        shape_sub (str): 属性 芯材鉄骨形状（副）
        strength (str): 属性 芯材鉄骨強度
        kind_section_stiffener (StbSecSteelFigureDampingDeviceHistoryKindSectionStiffener): 属性 補剛材・構造種別
        id_section_stiffener (int): 属性 補剛材・断面ID
        length (float): 属性 装置部分の長さ、または高さ(mm)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "shape_sub": _FI(py_type=str, data_type=_DT.STR),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "kind_section_stiffener": _FI(
            py_type=StbSecSteelFigureDampingDeviceHistoryKindSectionStiffener,
            data_type=_DT.STR_ENUM,
            choices=("RC", "S", "SRC", "CFT"),
        ),
        "id_section_stiffener": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "length": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbSecSteelFigureDampingDevice(StBridgeElement):
    """制振装置断面・鉄骨断面形状：StbSecSteelFigureDampingDevice

    Attributes:
        stb_sec_steel_figure_damping_device_history (list[StbSecSteelFigureDampingDeviceHistory]): 子要素 StbSecSteelFigureDampingDeviceHistory(履歴系ダンパー・鉄骨断面形状)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_steel_figure_damping_device_history": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecSteelFigureDampingDeviceHistory],
        ),
    }


class StbSecDampingDeviceMass(StBridgeElement):
    """質量系ダンパー：StbSecDampingDeviceMass

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_damping_device_specification_change (list[StbSecDampingDeviceSpecificationChange]): 子要素 StbSecDampingDeviceSpecificationChange(制振装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_damping_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecDampingDeviceSpecificationChange]"
        ),
    }


class StbSecDampingDeviceFriction(StBridgeElement):
    """摩擦ダンパー：StbSecDampingDeviceFriction

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_damping_device_specification_change (list[StbSecDampingDeviceSpecificationChange]): 子要素 StbSecDampingDeviceSpecificationChange(制振装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_damping_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecDampingDeviceSpecificationChange]"
        ),
    }


class StbSecDampingDeviceHistory(StBridgeElement):
    """履歴系ダンパー：StbSecDampingDeviceHistory

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_damping_device_specification_change (list[StbSecDampingDeviceSpecificationChange]): 子要素 StbSecDampingDeviceSpecificationChange(制振装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_damping_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecDampingDeviceSpecificationChange]"
        ),
    }


class StbSecDampingDeviceViscoelastic(StBridgeElement):
    """粘弾性体ダンパー：StbSecDampingDeviceViscoelastic

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_damping_device_specification_change (list[StbSecDampingDeviceSpecificationChange]): 子要素 StbSecDampingDeviceSpecificationChange(制振装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_damping_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecDampingDeviceSpecificationChange]"
        ),
    }


class StbSecDampingDeviceViscous(StBridgeElement):
    """粘性体ダンパー：StbSecDampingDeviceViscous

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_damping_device_specification_change (list[StbSecDampingDeviceSpecificationChange]): 子要素 StbSecDampingDeviceSpecificationChange(制振装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_damping_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecDampingDeviceSpecificationChange]"
        ),
    }


class StbSecDampingDeviceSpecificationChange(StBridgeElement):
    """制振装置・規定仕様の変更：StbSecDampingDeviceSpecificationChange

    Attributes:
        specification_changeable (StbSecDampingDeviceSpecificationChangeSpecificationChangeable): 属性 変更する仕様の名称
        value (str): 属性 変更する値
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "specification_changeable": _FI(
            py_type=StbSecDampingDeviceSpecificationChangeSpecificationChangeable,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "WIDTH_MOUNTPLATE",
                "LENGTH_MOUNTPLATE",
                "T_MOUNTPLATE",
                "NAME_MOUNTPLATE",
                "WIDTH_SPLICEPLATE",
                "LENGTH_SPLICEPLATE",
                "T_SPLICEPLATE",
                "NAME_SPLICEPLATE",
                "PITCH_BOLT",
                "N_BOLT",
                "HOLE_BOLT",
                "NAME_BOLT",
                "LENGTH",
            ),
        ),
        "value": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbSecDampingDeviceOil(StBridgeElement):
    """流体系ダンパー：StbSecDampingDeviceOil

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_damping_device_specification_change (list[StbSecDampingDeviceSpecificationChange]): 子要素 StbSecDampingDeviceSpecificationChange(制振装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_damping_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDeviceSpecificationChange]
        ),
    }


class StbSecProductDampingDevice(StBridgeElement):
    """制振装置断面・製品：StbSecProductDampingDevice

    Attributes:
        stb_sec_damping_device_oil (list[StbSecDampingDeviceOil]): 子要素 StbSecDampingDeviceOil(流体系ダンパー)
        stb_sec_damping_device_viscous (list[StbSecDampingDeviceViscous]): 子要素 StbSecDampingDeviceViscous(粘性体ダンパー)
        stb_sec_damping_device_viscoelastic (list[StbSecDampingDeviceViscoelastic]): 子要素 StbSecDampingDeviceViscoelastic(粘弾性体ダンパー)
        stb_sec_damping_device_history (list[StbSecDampingDeviceHistory]): 子要素 StbSecDampingDeviceHistory(履歴系ダンパー)
        stb_sec_damping_device_friction (list[StbSecDampingDeviceFriction]): 子要素 StbSecDampingDeviceFriction(摩擦ダンパー)
        stb_sec_damping_device_mass (list[StbSecDampingDeviceMass]): 子要素 StbSecDampingDeviceMass(質量系ダンパー)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_damping_device_oil": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDeviceOil]
        ),
        "stb_sec_damping_device_viscous": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDeviceViscous]
        ),
        "stb_sec_damping_device_viscoelastic": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDeviceViscoelastic]
        ),
        "stb_sec_damping_device_history": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDeviceHistory]
        ),
        "stb_sec_damping_device_friction": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDeviceFriction]
        ),
        "stb_sec_damping_device_mass": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDeviceMass]
        ),
    }


class StbSecDampingDevice(StBridgeElement):
    """制振装置断面：StbSecDampingDevice

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        stb_sec_product_damping_device (StbSecProductDampingDevice): 子要素 StbSecProductDampingDevice(制振装置断面・製品)
        stb_sec_steel_figure_damping_device (StbSecSteelFigureDampingDevice): 子要素 StbSecSteelFigureDampingDevice(制振装置断面・鉄骨断面形状)
        stb_sec_specification_damping_device (StbSecSpecificationDampingDevice): 子要素 StbSecSpecificationDampingDevice(制振装置断面・仕様指定)
        stb_sec_connection_damping_device (StbSecConnectionDampingDevice): 子要素 StbSecConnectionDampingDevice(制振装置断面・接合部)
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
        "stb_sec_product_damping_device": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecProductDampingDevice
        ),
        "stb_sec_steel_figure_damping_device": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelFigureDampingDevice
        ),
        "stb_sec_specification_damping_device": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSpecificationDampingDevice
        ),
        "stb_sec_connection_damping_device": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecConnectionDampingDevice
        ),
    }


class StbSecConnectionIsolatingDeviceLb(StBridgeElement):
    """免震層上下接合型支承接合部：StbSecConnectionIsolatingDeviceLB

    Attributes:
        method_start (StbSecConnectionIsolatingDeviceLbMethodStart): 属性 始端（下部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）、WELDING（溶接接合）
        t_plate_start (float): 属性 始端（下部）ベースプレート・厚さ
        strength_plate_start (str): 属性 同・鉄骨強度
        number_studbolt_start (int): 属性 始端（下部）スタッドボルト・全本数
        name_studbolt_start (str): 属性 同・鉄骨強度
        strength_studbolt_start (str): 属性 同・材料名称
        number_anchorbolt_start (int): 属性 始端（下部）アンカーボルト類・全本数
        name_anchorbolt_start (str): 属性 同・材料名称
        strength_anchorbolt_start (str): 属性 同・鉄骨強度
        method_end (StbSecConnectionIsolatingDeviceLbMethodEnd): 属性 終端（上部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）、WELDING（溶接接合）
        t_plate_end (float): 属性 終端（上部）ベースプレート・厚さ
        strength_plate_end (str): 属性 同・鉄骨強度
        number_studbolt_end (int): 属性 終端（上部）スタッドボルト・全本数
        name_studbolt_end (str): 属性 同・鉄骨強度
        strength_studbolt_end (str): 属性 同・材料名称
        number_anchorbolt_end (int): 属性 終端（上部）アンカーボルト類・全本数
        name_anchorbolt_end (str): 属性 同・材料名称
        strength_anchorbolt_end (str): 属性 同・鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "method_start": _FI(
            py_type=StbSecConnectionIsolatingDeviceLbMethodStart,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT", "WELDING"),
        ),
        "t_plate_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_start": _FI(py_type=str, data_type=_DT.STR),
        "number_studbolt_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_studbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "strength_studbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "method_end": _FI(
            py_type=StbSecConnectionIsolatingDeviceLbMethodEnd,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT", "WELDING"),
        ),
        "t_plate_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_end": _FI(py_type=str, data_type=_DT.STR),
        "number_studbolt_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_studbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "strength_studbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecConnectionIsolatingDeviceLB"


class StbSecConnectionIsolatingDeviceSp(StBridgeElement):
    """すべり板設置型支承接合部：StbSecConnectionIsolatingDeviceSP

    Attributes:
        method_bearingside (StbSecConnectionIsolatingDeviceSpMethodBearingside): 属性 支承側接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）
        shape_plate_bearingside (StbSecConnectionIsolatingDeviceSpShapePlateBearingside): 属性 支承側ベースプレート・形状以下のいずれかCIRCLE（円形）、SQUARE（正方形）
        size_plate_bearingside (float): 属性 同・外径
        t_plate_bearingside (float): 属性 同・厚さ
        strength_plate_bearingside (str): 属性 同・鉄骨強度
        number_studbolt_bearingside (int): 属性 支承側スタッドボルト・全本数
        name_studbolt_bearingside (str): 属性 同・鉄骨強度
        strength_studbolt_bearingside (str): 属性 同・材料名称
        number_anchorbolt_bearingside (int): 属性 支承側アンカーボルト類・全本数
        pitch_anchorbolt_bearingside (float): 属性 同・穴PCD
        name_anchorbolt_bearingside (str): 属性 同・材料名称
        strength_anchorbolt_bearingside (str): 属性 同・鉄骨強度
        method_plateside (StbSecConnectionIsolatingDeviceSpMethodPlateside): 属性 すべり板側接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）
        shape_plate_plateside (StbSecConnectionIsolatingDeviceSpShapePlatePlateside): 属性 すべり板側ベースプレート・形状以下のいずれかCIRCLE（円形）、SQUARE（正方形）
        size_plate_plateside (float): 属性 同・外径
        t_plate_plateside (float): 属性 同・厚さ
        strength_plate_plateside (str): 属性 同・鉄骨強度
        number_studbolt_plateside (int): 属性 すべり板側スタッドボルト・全本数
        name_studbolt_plateside (str): 属性 同・鉄骨強度
        strength_studbolt_plateside (str): 属性 同・材料名称
        number_anchorbolt_plateside (int): 属性 すべり板側アンカーボルト類・全本数
        pitch_anchorbolt_plateside (float): 属性 同・穴PCD
        name_anchorbolt_plateside (str): 属性 同・材料名称
        strength_anchorbolt_plateside (str): 属性 同・鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "method_bearingside": _FI(
            py_type=StbSecConnectionIsolatingDeviceSpMethodBearingside,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT"),
        ),
        "shape_plate_bearingside": _FI(
            py_type=StbSecConnectionIsolatingDeviceSpShapePlateBearingside,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "size_plate_bearingside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "t_plate_bearingside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "strength_plate_bearingside": _FI(py_type=str, data_type=_DT.STR),
        "number_studbolt_bearingside": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_studbolt_bearingside": _FI(py_type=str, data_type=_DT.STR),
        "strength_studbolt_bearingside": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_bearingside": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "pitch_anchorbolt_bearingside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "name_anchorbolt_bearingside": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_bearingside": _FI(py_type=str, data_type=_DT.STR),
        "method_plateside": _FI(
            py_type=StbSecConnectionIsolatingDeviceSpMethodPlateside,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT"),
        ),
        "shape_plate_plateside": _FI(
            py_type=StbSecConnectionIsolatingDeviceSpShapePlatePlateside,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "size_plate_plateside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "t_plate_plateside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "strength_plate_plateside": _FI(py_type=str, data_type=_DT.STR),
        "number_studbolt_plateside": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_studbolt_plateside": _FI(py_type=str, data_type=_DT.STR),
        "strength_studbolt_plateside": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_plateside": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "pitch_anchorbolt_plateside": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "name_anchorbolt_plateside": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_plateside": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecConnectionIsolatingDeviceSP"


class StbSecConnectionIsolatingDeviceRb(StBridgeElement):
    """積層ゴム支承接合部：StbSecConnectionIsolatingDeviceRB

    Attributes:
        method_start (StbSecConnectionIsolatingDeviceRbMethodStart): 属性 始端（下部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）
        shape_plate_start (StbSecConnectionIsolatingDeviceRbShapePlateStart): 属性 始端（下部）ベースプレート・形状以下のいずれかCIRCLE（円形）、SQUARE（正方形）
        size_plate_start (float): 属性 始端（下部）ベースプレート・外径
        t_plate_start (float): 属性 始端（下部）ベースプレート・厚さ
        strength_plate_start (str): 属性 始端（下部）ベースプレート・鉄骨強度
        number_studbolt_start (int): 属性 始端（下部）スタッドボルト・全本数
        name_studbolt_start (str): 属性 始端（下部）スタッドボルト・鉄骨強度
        strength_studbolt_start (str): 属性 始端（下部）スタッドボルト・材料名称
        number_anchorbolt_start (int): 属性 始端（下部）アンカーボルト類・全本数
        pitch_anchorbolt_start (float): 属性 始端（下部）アンカーボルト類・穴PCD
        name_anchorbolt_start (str): 属性 始端（下部）アンカーボルト類・材料名称
        strength_anchorbolt_start (str): 属性 始端（下部）アンカーボルト類・鉄骨強度
        method_end (StbSecConnectionIsolatingDeviceRbMethodEnd): 属性 終端（上部）接合方法以下のいずれかBASEPLATE（ベースプレート接合）、BOLT（ボルト接合）
        shape_plate_end (StbSecConnectionIsolatingDeviceRbShapePlateEnd): 属性 終端（上部）ベースプレート・形状以下のいずれかCIRCLE（円形）、SQUARE（正方形）
        size_plate_end (float): 属性 終端（上部）ベースプレート・外径
        t_plate_end (float): 属性 終端（上部）ベースプレート・厚さ
        strength_plate_end (str): 属性 終端（上部）ベースプレート・鉄骨強度
        number_studbolt_end (int): 属性 終端（上部）スタッドボルト・全本数
        name_studbolt_end (str): 属性 終端（上部）スタッドボルト・鉄骨強度
        strength_studbolt_end (str): 属性 終端（上部）スタッドボルト・材料名称
        number_anchorbolt_end (int): 属性 終端（上部）アンカーボルト類・全本数
        pitch_anchorbolt_end (float): 属性 終端（上部）アンカーボルト類・穴PCD
        name_anchorbolt_end (str): 属性 終端（上部）アンカーボルト類・材料名称
        strength_anchorbolt_end (str): 属性 終端（上部）アンカーボルト類・鉄骨強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "method_start": _FI(
            py_type=StbSecConnectionIsolatingDeviceRbMethodStart,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT"),
        ),
        "shape_plate_start": _FI(
            py_type=StbSecConnectionIsolatingDeviceRbShapePlateStart,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "size_plate_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "t_plate_start": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_start": _FI(py_type=str, data_type=_DT.STR),
        "number_studbolt_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_studbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "strength_studbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "pitch_anchorbolt_start": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "name_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_start": _FI(py_type=str, data_type=_DT.STR),
        "method_end": _FI(
            py_type=StbSecConnectionIsolatingDeviceRbMethodEnd,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BASEPLATE", "BOLT"),
        ),
        "shape_plate_end": _FI(
            py_type=StbSecConnectionIsolatingDeviceRbShapePlateEnd,
            data_type=_DT.STR_ENUM,
            choices=("CIRCLE", "SQUARE"),
        ),
        "size_plate_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "t_plate_end": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "strength_plate_end": _FI(py_type=str, data_type=_DT.STR),
        "number_studbolt_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "name_studbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "strength_studbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "number_anchorbolt_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "pitch_anchorbolt_end": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "name_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
        "strength_anchorbolt_end": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecConnectionIsolatingDeviceRB"


class StbSecConnectionIsolatingDevice(StBridgeElement):
    """免震装置断面・接合部：StbSecConnectionIsolatingDevice

    Attributes:
        stb_sec_connection_isolating_device_rb (StbSecConnectionIsolatingDeviceRb): 子要素 StbSecConnectionIsolatingDeviceRB(積層ゴム支承接合部)
        stb_sec_connection_isolating_device_sp (StbSecConnectionIsolatingDeviceSp): 子要素 StbSecConnectionIsolatingDeviceSP(すべり板設置型支承接合部)
        stb_sec_connection_isolating_device_lb (StbSecConnectionIsolatingDeviceLb): 子要素 StbSecConnectionIsolatingDeviceLB(免震層上下接合型支承接合部)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_connection_isolating_device_rb": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecConnectionIsolatingDeviceRb
        ),
        "stb_sec_connection_isolating_device_sp": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecConnectionIsolatingDeviceSp
        ),
        "stb_sec_connection_isolating_device_lb": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecConnectionIsolatingDeviceLb
        ),
    }


class StbSecSpecificationIsolatingDevice(StBridgeElement):
    """免震装置断面・仕様指定：StbSecSpecificationIsolatingDevice

    Attributes:
    """

    _fields: ClassVar[dict[str, _FI]] = {}


class StbSecIsolatingDeviceClb(StBridgeElement):
    """レール式転がり支承：StbSecIsolatingDeviceCLB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        is_used_upside_down (bool): 属性 true：キ型(下２列、上1列)を上下反転して設置
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "is_used_upside_down": _FI(
            py_type=bool, data_type=_DT.BOOL, xml_name="isUsedUpsideDown"
        ),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceCLB"


class StbSecIsolatingDeviceClsb(StBridgeElement):
    """レール式すべり支承：StbSecIsolatingDeviceCLSB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceCLSB"


class StbSecIsolatingDeviceCsb(StBridgeElement):
    """曲面すべり支承：StbSecIsolatingDeviceCSB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceCSB"


class StbSecIsolatingDeviceRsb(StBridgeElement):
    """剛すべり支承：StbSecIsolatingDeviceRSB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        pos (StbSecIsolatingDeviceRsbPos): 属性 すべり板設置 以下のいずれかTOP（支承上側）BOTTOM（支承下側）
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "pos": _FI(
            py_type=StbSecIsolatingDeviceRsbPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("TOP", "BOTTOM"),
        ),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceRSB"


class StbSecIsolatingDeviceEsb(StBridgeElement):
    """弾性すべり支承：StbSecIsolatingDeviceESB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        pos (StbSecIsolatingDeviceEsbPos): 属性 すべり板設置 以下のいずれかTOP（支承上側）BOTTOM（支承下側）
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "pos": _FI(
            py_type=StbSecIsolatingDeviceEsbPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("TOP", "BOTTOM"),
        ),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceESB"


class StbSecIsolatingDeviceSdrb(StBridgeElement):
    """ダンパー一体型積層ゴム支承：StbSecIsolatingDeviceSDRB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceSDRB"


class StbSecIsolatingDeviceTrb(StBridgeElement):
    """錫プラグ入り積層ゴム支承：StbSecIsolatingDeviceTRB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceTRB"


class StbSecIsolatingDeviceLrb(StBridgeElement):
    """鉛プラグ入り積層ゴム支承：StbSecIsolatingDeviceLRB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceLRB"


class StbSecIsolatingDeviceHdr(StBridgeElement):
    """高減衰ゴム系積層ゴム支承：StbSecIsolatingDeviceHDR

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecIsolatingDeviceSpecificationChange]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceHDR"


class StbSecIsolatingDeviceSpecificationChange(StBridgeElement):
    """免震装置・規定仕様の変更：StbSecIsolatingDeviceSpecificationChange

    Attributes:
        specification_changeable (StbSecIsolatingDeviceSpecificationChangeSpecificationChangeable): 属性 変更する仕様の名称
        value (str): 属性 変更する値
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "specification_changeable": _FI(
            py_type=StbSecIsolatingDeviceSpecificationChangeSpecificationChangeable,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "SIZE_FRANGE",
                "LENGTH_FRANGE",
                "T_FRANGE",
                "PCD_BOLT",
                "N_BOLT",
                "HOLE_BOLT",
                "NAME_BOLT",
                "HEIGHT",
                "SIZE_SLIDEPLATE",
                "T_SLIDEPLATE",
                "PCD_BOLT_SLIDEPLATE",
                "N_BOLT_SLIDEPLATE",
                "NAME_BOLT_SLIDEPLATE",
            ),
        ),
        "value": _FI(py_type=str, data_type=_DT.STR, required=True),
    }


class StbSecIsolatingDeviceNrb(StBridgeElement):
    """天然ゴム系積層ゴム支承：StbSecIsolatingDeviceNRB

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        stb_sec_isolating_device_specification_change (list[StbSecIsolatingDeviceSpecificationChange]): 子要素 StbSecIsolatingDeviceSpecificationChange(免震装置・規定仕様の変更)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "stb_sec_isolating_device_specification_change": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceSpecificationChange]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecIsolatingDeviceNRB"


class StbSecProductIsolatingDevice(StBridgeElement):
    """免震装置断面・製品：StbSecProductIsolatingDevice

    Attributes:
        stb_sec_isolating_device_nrb (list[StbSecIsolatingDeviceNrb]): 子要素 StbSecIsolatingDeviceNRB(天然ゴム系積層ゴム支承)
        stb_sec_isolating_device_hdr (list[StbSecIsolatingDeviceHdr]): 子要素 StbSecIsolatingDeviceHDR(高減衰ゴム系積層ゴム支承)
        stb_sec_isolating_device_lrb (list[StbSecIsolatingDeviceLrb]): 子要素 StbSecIsolatingDeviceLRB(鉛プラグ入り積層ゴム支承)
        stb_sec_isolating_device_trb (list[StbSecIsolatingDeviceTrb]): 子要素 StbSecIsolatingDeviceTRB(錫プラグ入り積層ゴム支承)
        stb_sec_isolating_device_sdrb (list[StbSecIsolatingDeviceSdrb]): 子要素 StbSecIsolatingDeviceSDRB(ダンパー一体型積層ゴム支承)
        stb_sec_isolating_device_esb (list[StbSecIsolatingDeviceEsb]): 子要素 StbSecIsolatingDeviceESB(弾性すべり支承)
        stb_sec_isolating_device_rsb (list[StbSecIsolatingDeviceRsb]): 子要素 StbSecIsolatingDeviceRSB(剛すべり支承)
        stb_sec_isolating_device_csb (list[StbSecIsolatingDeviceCsb]): 子要素 StbSecIsolatingDeviceCSB(曲面すべり支承)
        stb_sec_isolating_device_clsb (list[StbSecIsolatingDeviceClsb]): 子要素 StbSecIsolatingDeviceCLSB(レール式すべり支承)
        stb_sec_isolating_device_clb (list[StbSecIsolatingDeviceClb]): 子要素 StbSecIsolatingDeviceCLB(レール式転がり支承)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_isolating_device_nrb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceNrb]
        ),
        "stb_sec_isolating_device_hdr": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceHdr]
        ),
        "stb_sec_isolating_device_lrb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceLrb]
        ),
        "stb_sec_isolating_device_trb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceTrb]
        ),
        "stb_sec_isolating_device_sdrb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceSdrb]
        ),
        "stb_sec_isolating_device_esb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceEsb]
        ),
        "stb_sec_isolating_device_rsb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceRsb]
        ),
        "stb_sec_isolating_device_csb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceCsb]
        ),
        "stb_sec_isolating_device_clsb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceClsb]
        ),
        "stb_sec_isolating_device_clb": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDeviceClb]
        ),
    }


class StbSecIsolatingDevice(StBridgeElement):
    """免震装置断面：StbSecIsolatingDevice

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        stb_sec_product_isolating_device (StbSecProductIsolatingDevice): 子要素 StbSecProductIsolatingDevice(免震装置断面・製品)
        stb_sec_specification_isolating_device (StbSecSpecificationIsolatingDevice): 子要素 StbSecSpecificationIsolatingDevice(免震装置断面・仕様指定)
        stb_sec_connection_isolating_device (StbSecConnectionIsolatingDevice): 子要素 StbSecConnectionIsolatingDevice(免震装置断面・接合部)
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
        "stb_sec_product_isolating_device": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecProductIsolatingDevice
        ),
        "stb_sec_specification_isolating_device": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSpecificationIsolatingDevice
        ),
        "stb_sec_connection_isolating_device": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecConnectionIsolatingDevice
        ),
    }


class StbSecWallLoad(StBridgeElement):
    """荷重用壁断面：StbSecWallLoad

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


class StbSecBarWallRcBottomEnd(StBridgeElement):
    """ＲＣ壁断面配筋（内外異なる）縦筋下端・横筋終端：StbSecBarWall_RC_BottomEnd

    Attributes:
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_BottomEnd"


class StbSecBarWallRcMiddle(StBridgeElement):
    """ＲＣ壁断面配筋（内外異なる）縦筋中央・横筋中央：StbSecBarWall_RC_Middle

    Attributes:
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_Middle"


class StbSecBarWallRcTopStart(StBridgeElement):
    """ＲＣ壁断面配筋（内外異なる）縦筋上端・横筋始端：StbSecBarWall_RC_TopStart

    Attributes:
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_TopStart"


class StbSecBarWallRcAll(StBridgeElement):
    """ＲＣ壁断面配筋（内外異なる）全断面一様な配筋：StbSecBarWall_RC_All

    Attributes:
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarWall_RC_All"


class StbSecBarWallRcInsideAndOutside(StBridgeElement):
    """ＲＣ壁断面配筋（内外異なる）：StbSecBarWall_RC_InsideAndOutside

    Attributes:
        pos (StbSecBarWallRcInsideAndOutsidePos): 属性 配筋位置 以下のいずれかVERTICAL_OUTSIDE（縦筋外側）VERTICAL_INSIDE（縦筋内側）HORIZONTAL_OUTSIDE（横筋外側）HORIZONTAL_INSIDE（横筋内側）
        pos2 (int): 属性 鉄筋の段位置
        length1 (float): 属性 縦筋上端・横筋始端側の鉄筋切替位置
        length1_ex (float): 属性 縦筋上端・横筋始端側の余長
        length2 (float): 属性 縦筋下端・横筋終端側の鉄筋切替位置
        length2_ex (float): 属性 縦筋下端・横筋終端側の余長
        stb_sec_bar_wall_rc_all (StbSecBarWallRcAll): 子要素 StbSecBarWall_RC_All(ＲＣ壁断面配筋（内外異なる）全断面一様な配筋)
        stb_sec_bar_wall_rc_top_start (StbSecBarWallRcTopStart): 子要素 StbSecBarWall_RC_TopStart(ＲＣ壁断面配筋（内外異なる）縦筋上端・横筋始端)
        stb_sec_bar_wall_rc_middle (StbSecBarWallRcMiddle): 子要素 StbSecBarWall_RC_Middle(ＲＣ壁断面配筋（内外異なる）縦筋中央・横筋中央)
        stb_sec_bar_wall_rc_bottom_end (StbSecBarWallRcBottomEnd): 子要素 StbSecBarWall_RC_BottomEnd(ＲＣ壁断面配筋（内外異なる）縦筋下端・横筋終端)
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
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "length1": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length1_ex": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "length2_ex": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_bar_wall_rc_all": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarWallRcAll
        ),
        "stb_sec_bar_wall_rc_top_start": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarWallRcTopStart
        ),
        "stb_sec_bar_wall_rc_middle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarWallRcMiddle
        ),
        "stb_sec_bar_wall_rc_bottom_end": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarWallRcBottomEnd
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
        outer_bar_direction (StbSecBarArrangementWallRcOuterBarDirection): 属性
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
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
        "outer_bar_direction": _FI(
            py_type=StbSecBarArrangementWallRcOuterBarDirection,
            data_type=_DT.STR_ENUM,
            choices=("VERTICAL", "HORIZONTAL"),
        ),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
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
            kind=_FK.ELEMENT, py_type=list[StbSecBarWallRcInsideAndOutside]
        ),
        "stb_sec_bar_wall_rc_edge": _FI(
            kind=_FK.ELEMENT, max_occurs=4, py_type=list[StbSecBarWallRcEdge]
        ),
        "stb_sec_bar_wall_rc_open": _FI(
            kind=_FK.ELEMENT, max_occurs=3, py_type=list[StbSecBarWallRcOpen]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementWall_RC"


class StbSecWallRcTaper(StBridgeElement):
    """ＲＣ壁断面形状・テーパー：StbSecWall_RC_Taper

    Attributes:
        t_bottom (float): 属性 RC壁下端の厚さTb
        t_top (float): 属性 RC壁上端の厚さTt
        depth_hb (float): 属性 形状の切り替え位置Hb
        depth_ht (float): 属性 形状の切り替え位置Ht
        type_straight (StbSecWallRcTaperTypeStraight): 属性 ストレートな面以下のいずれかの値をとる。OUTSIDE（外側）INSIDE（内側）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "t_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "t_top": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth_hb": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="depth_Hb",
        ),
        "depth_ht": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            xml_name="depth_Ht",
        ),
        "type_straight": _FI(
            py_type=StbSecWallRcTaperTypeStraight,
            data_type=_DT.STR_ENUM,
            choices=("OUTSIDE", "INSIDE"),
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecWall_RC_Taper"


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
        stb_sec_wall_rc_taper (StbSecWallRcTaper): 子要素 StbSecWall_RC_Taper(ＲＣ壁断面形状・テーパー)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_wall_rc_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecWallRcStraight
        ),
        "stb_sec_wall_rc_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecWallRcTaper
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


class StbSecSlabLoad(StBridgeElement):
    """荷重用スラブ断面：StbSecSlabLoad

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


class StbSecProductSlabPrecast(StBridgeElement):
    """既製スラブ製品：StbSecProductSlabPrecast

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
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
            choices=("MAIN_TOP", "TRANSVERSE_TOP", "MESH"),
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
            choices=(
                "SHORT_TOP_END",
                "SHORT_BOTTOM_END",
                "SHORT_TOP_CENTER",
                "SHORT_BOTTOM_CENTER",
                "LONG_TOP_END",
                "LONG_BOTTOM_END",
                "LONG_TOP_CENTER",
                "LONG_BOTTOM_CENTER",
            ),
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
            kind=_FK.ELEMENT, max_occurs=8, py_type=list[StbSecBarSlabPrecast2Way]
        ),
        "stb_sec_bar_slab_precast1_way": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarSlabPrecast1Way]
        ),
    }


class StbSecSlabPrecastStraight(StBridgeElement):
    """既製スラブトップ部分断面形状・ストレート：StbSecSlabPrecastStraight

    Attributes:
        depth_top_concrete (float): 属性 トップコンクリート厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_top_concrete": _FI(
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
        strength_top_concrete (str): 属性 トップ部分コンクリート強度
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
        "strength_top_concrete": _FI(py_type=str, data_type=_DT.STR),
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


class StbCertificationNumber(StBridgeElement):
    """認定番号：StbCertificationNumber

    Attributes:
        certification_number (str): 属性 認定番号
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "certification_number": _FI(py_type=str, data_type=_DT.STR, required=True),
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
            choices=("MAIN_TOP", "TRANSVERSE_TOP", "MESH"),
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
        d_refractory_bar (str): 属性
        strength_refractory_bar (str): 属性
        stb_sec_bar_slab_deck1_way (list[StbSecBarSlabDeck1Way]): 子要素 StbSecBarSlabDeck1Way(デッキ合成スラブ断面配筋・１方向)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "d_refractory_bar": _FI(
            py_type=str, data_type=_DT.STR, xml_name="D_refractory_bar"
        ),
        "strength_refractory_bar": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_slab_deck1_way": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecBarSlabDeck1Way]
        ),
    }


class StbSecSlabDeckProduct(StBridgeElement):
    """合成デッキ製品：StbSecSlabDeckProduct

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        top_concrete (float): 属性 トップコンクリート
        surface_finishing (str): 属性 表面処理(Z12など)
        stb_sec_bar_arrangement_slab_deck (StbSecBarArrangementSlabDeck): 子要素 StbSecBarArrangementSlabDeck(デッキ合成スラブ断面配筋)
        stb_certification_number (list[StbCertificationNumber]): 子要素 StbCertificationNumber(認定番号)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "top_concrete": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "surface_finishing": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_arrangement_slab_deck": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementSlabDeck
        ),
        "stb_certification_number": _FI(
            kind=_FK.ELEMENT, py_type=list[StbCertificationNumber]
        ),
    }


class StbSecSlabDeck(StBridgeElement):
    """デッキ合成スラブ断面：StbSecSlabDeck

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 断面名称
        strength_concrete (str): 属性 コンクリート強度
        stb_sec_slab_deck_product (list[StbSecSlabDeckProduct]): 子要素 StbSecSlabDeckProduct(合成デッキ製品)
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
        "stb_sec_slab_deck_product": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecSlabDeckProduct]
        ),
    }


class StbSecBarSlabRcTruss1Way(StBridgeElement):
    """トラス筋付きデッキスラブ断面配筋・１方向：StbSecBarSlab_RC_Truss1Way

    Attributes:
        pos (StbSecBarSlabRcTruss1WayPos): 属性 配筋位置以下のいずれかMAIN_TOP（①主筋方向上端）MAIN_BOTTOM（②主筋方向下端）TRANSVERSE_TOP（③配力筋方向上端）TRANSVERSE_BOTTOM（④配力筋方向下端）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRcTruss1WayPos,
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
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_Truss1Way"


class StbSecBarArrangementSlabRcTruss(StBridgeElement):
    """トラス筋付きデッキスラブ断面配筋：StbSecBarArrangementSlab_RC_Truss

    Attributes:
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        stb_sec_bar_slab_rc_truss1_way (list[StbSecBarSlabRcTruss1Way]): 子要素 StbSecBarSlab_RC_Truss1Way(トラス筋付きデッキスラブ断面配筋・１方向)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_slab_rc_truss1_way": _FI(
            kind=_FK.ELEMENT,
            max_occurs=4,
            min_occurs=2,
            py_type=list[StbSecBarSlabRcTruss1Way],
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementSlab_RC_Truss"


class StbSecSlabRcTrussProduct(StBridgeElement):
    """トラス筋付きデッキスラブ製品：StbSecSlab_RC_TrussProduct

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        thickness (float): 属性 コンクリート厚
        surface_finishing (str): 属性 表面処理(Z12など)
        stb_sec_bar_arrangement_slab_rc_truss (StbSecBarArrangementSlabRcTruss): 子要素 StbSecBarArrangementSlab_RC_Truss(トラス筋付きデッキスラブ断面配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "surface_finishing": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_arrangement_slab_rc_truss": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarArrangementSlabRcTruss
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_TrussProduct"


class StbSecSlabRcTruss(StBridgeElement):
    """ＲＣスラブトラス断面：StbSecSlab_RC_Truss

    Attributes:
        stb_sec_slab_rc_truss_product (list[StbSecSlabRcTrussProduct]): 子要素 StbSecSlab_RC_TrussProduct(トラス筋付きデッキスラブ製品)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_slab_rc_truss_product": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecSlabRcTrussProduct]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_Truss"


class StbSecFormworkSlabFlatDeckProduct(StBridgeElement):
    """フラットデッキ型番指定：StbSecFormworkSlabFlatDeckProduct

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        surface_finishing (str): 属性 表面処理(Z12など)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "surface_finishing": _FI(py_type=str, data_type=_DT.STR),
    }


class StbSecFormworkSlabFlatDeckSpec(StBridgeElement):
    """フラットデッキ型枠仕様指定：StbSecFormworkSlabFlatDeckSpec

    Attributes:
        depth (float): 属性 デッキ厚
        surface_finishing (str): 属性 表面処理(Z12など)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "surface_finishing": _FI(py_type=str, data_type=_DT.STR),
    }


class StbSecFormworkSlabFlatDeck(StBridgeElement):
    """フラットデッキ型枠：StbSecFormworkSlabFlatDeck

    Attributes:
        stb_sec_formwork_slab_flat_deck_spec (StbSecFormworkSlabFlatDeckSpec): 子要素 StbSecFormworkSlabFlatDeckSpec(フラットデッキ型枠仕様指定)
        stb_sec_formwork_slab_flat_deck_product (StbSecFormworkSlabFlatDeckProduct): 子要素 StbSecFormworkSlabFlatDeckProduct(フラットデッキ型番指定)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_formwork_slab_flat_deck_spec": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFormworkSlabFlatDeckSpec
        ),
        "stb_sec_formwork_slab_flat_deck_product": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFormworkSlabFlatDeckProduct
        ),
    }


class StbSecFormworkSlabWood(StBridgeElement):
    """在来型枠：StbSecFormworkSlabWood

    Attributes:
        thickness (float): 属性 木の厚さ
        type (StbSecFormworkSlabWoodType): 属性 せき板以下のいずれかの値をとるA：A種B：B種C：C種
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "thickness": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "type": _FI(
            py_type=StbSecFormworkSlabWoodType,
            data_type=_DT.STR_ENUM,
            choices=("A", "B", "C"),
        ),
    }


class StbSecFormworkSlab(StBridgeElement):
    """型枠要素：StbSecFormworkSlab

    Attributes:
        stb_sec_formwork_slab_wood (StbSecFormworkSlabWood): 子要素 StbSecFormworkSlabWood(在来型枠)
        stb_sec_formwork_slab_flat_deck (StbSecFormworkSlabFlatDeck): 子要素 StbSecFormworkSlabFlatDeck(フラットデッキ型枠)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_formwork_slab_wood": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFormworkSlabWood
        ),
        "stb_sec_formwork_slab_flat_deck": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFormworkSlabFlatDeck
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


class StbSecBarSlabRcConventional1Way2(StBridgeElement):
    """ＲＣ在来スラブ断面配筋・１方向２：StbSecBarSlab_RC_Conventional1Way2

    Attributes:
        pos (StbSecBarSlabRcConventional1Way2Pos): 属性 配筋位置以下のいずれかMAIN_BASE_TOP（①主筋方向根元上端）MAIN_BASE_BOTTOM（②主筋方向根元下端）MAIN_TIP_TOP（③主筋方向先端上端）MAIN_TIP_BOTTOM（④主筋方向先端下端）TRANSVERSE_TOP（⑤配力筋方向上端）TRANSVERSE_BOTTOM（⑥配力筋方向下端）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRcConventional1Way2Pos,
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
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_Conventional1Way2"


class StbSecBarSlabRcConventional1Way1(StBridgeElement):
    """ＲＣ在来スラブ断面配筋・１方向１：StbSecBarSlab_RC_Conventional1Way1

    Attributes:
        pos (StbSecBarSlabRcConventional1Way1Pos): 属性 配筋位置以下のいずれかMAIN_TOP（①主筋方向上端）MAIN_BOTTOM（②主筋方向下端）TRANSVERSE_TOP（③配力筋方向上端）TRANSVERSE_BOTTOM（④配力筋方向下端）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRcConventional1Way1Pos,
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
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_Conventional1Way1"


class StbSecBarSlabRcConventional2Way(StBridgeElement):
    """ＲＣ在来スラブ断面配筋・２方向：StbSecBarSlab_RC_Conventional2Way

    Attributes:
        pos (StbSecBarSlabRcConventional2WayPos): 属性 配筋位置以下のいずれかSHORT_TOP_END短辺上端端部）SHORT_BOTTOM_END短辺下端端部）SHORT_TOP_CENTER短辺上端中央）SHORT_BOTTOM_CENTER短辺下端中央）LONG_TOP_END長辺上端端部）LONG _BOTTOM_END長辺下端端部）LONG_TOP_CENTER長辺上端中央）LONG_BOTTOM_CENTER長辺下端中央）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRcConventional2WayPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=(
                "SHORT_TOP_END",
                "SHORT_BOTTOM_END",
                "SHORT_TOP_CENTER",
                "SHORT_BOTTOM_CENTER",
                "LONG_TOP_END",
                "LONG_BOTTOM_END",
                "LONG_TOP_CENTER",
                "LONG_BOTTOM_CENTER",
            ),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_Conventional2Way"


class StbSecBarSlabRcConventionalStandard(StBridgeElement):
    """ＲＣ在来スラブ断面配筋・標準：StbSecBarSlab_RC_ConventionalStandard

    Attributes:
        pos (StbSecBarSlabRcConventionalStandardPos): 属性 配筋位置以下のいずれかSHORT_TOP_COLUMN短辺上端柱列帯）SHORT_TOP_MID_END（②短辺上端柱間帯端部）SHORT_TOP_MID_CENTER（③短辺上端柱間帯中央）SHORT_BOTTOM_COLUMN（④短辺下端柱列帯）SHORT_BOTTOM_MID_END（⑤短辺下端柱間帯端部）SHORT_BOTTOM_MID_CENTER（⑥短辺下端柱間帯中央）LONG_TOP_COLUMN（⑦長辺上端柱列帯）LONG_TOP_MID_END（⑧長辺上端柱間帯端部）LONG_TOP_MID_CENTER（⑨長辺上端柱間帯中央）LONG_BOTTOM_COLUMN（⑩長辺下端柱列帯）LONG_BOTTOM_MID_END（⑪長辺下端柱間帯端部）LONG_BOTTOM_MID_CENTER（⑫長辺下端柱間帯中央）
        strength (str): 属性 鉄筋強度
        d (str): 属性 径
        pitch (float): 属性 ピッチ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarSlabRcConventionalStandardPos,
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
    _xml_element_name: ClassVar[str] = "StbSecBarSlab_RC_ConventionalStandard"


class StbSecBarArrangementSlabRcConventional(StBridgeElement):
    """ＲＣ在来スラブ断面配筋：StbSecBarArrangementSlab_RC_Conventional

    Attributes:
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        stb_sec_bar_slab_rc_conventional_standard (list[StbSecBarSlabRcConventionalStandard]): 子要素 StbSecBarSlab_RC_ConventionalStandard(ＲＣ在来スラブ断面配筋・標準)
        stb_sec_bar_slab_rc_conventional2_way (list[StbSecBarSlabRcConventional2Way]): 子要素 StbSecBarSlab_RC_Conventional2Way(ＲＣ在来スラブ断面配筋・２方向)
        stb_sec_bar_slab_rc_conventional1_way1 (list[StbSecBarSlabRcConventional1Way1]): 子要素 StbSecBarSlab_RC_Conventional1Way1(ＲＣ在来スラブ断面配筋・１方向１)
        stb_sec_bar_slab_rc_conventional1_way2 (list[StbSecBarSlabRcConventional1Way2]): 子要素 StbSecBarSlab_RC_Conventional1Way2(ＲＣ在来スラブ断面配筋・１方向２)
        stb_sec_bar_slab_rc_open (list[StbSecBarSlabRcOpen]): 子要素 StbSecBarSlab_RC_Open(スラブ開口配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover_top": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "depth_cover_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_slab_rc_conventional_standard": _FI(
            kind=_FK.ELEMENT,
            max_occurs=12,
            py_type=list[StbSecBarSlabRcConventionalStandard],
        ),
        "stb_sec_bar_slab_rc_conventional2_way": _FI(
            kind=_FK.ELEMENT,
            max_occurs=8,
            py_type=list[StbSecBarSlabRcConventional2Way],
        ),
        "stb_sec_bar_slab_rc_conventional1_way1": _FI(
            kind=_FK.ELEMENT,
            max_occurs=4,
            py_type=list[StbSecBarSlabRcConventional1Way1],
        ),
        "stb_sec_bar_slab_rc_conventional1_way2": _FI(
            kind=_FK.ELEMENT,
            max_occurs=6,
            py_type=list[StbSecBarSlabRcConventional1Way2],
        ),
        "stb_sec_bar_slab_rc_open": _FI(
            kind=_FK.ELEMENT, max_occurs=6, py_type=list[StbSecBarSlabRcOpen]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementSlab_RC_Conventional"


class StbSecSlabRcConventionalHaunch(StBridgeElement):
    """ＲＣ在来スラブ断面形状・ハンチ：StbSecSlab_RC_ConventionalHaunch

    Attributes:
        base_depth (float): 属性 根元厚さ
        tip_depth (float): 属性 中央厚さ
        haunch_length (float): 属性 ハンチ長さ
        tip_offset (float): 属性 オフセット平面からの下がり寸法
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "base_depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "tip_depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "haunch_length": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "tip_offset": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_ConventionalHaunch"


class StbSecSlabRcConventionalTaper(StBridgeElement):
    """ＲＣ在来スラブ断面形状・テーパー：StbSecSlab_RC_ConventionalTaper

    Attributes:
        base_depth (float): 属性 根元厚さ
        tip_depth (float): 属性 先端厚さ
        tip_offset (float): 属性 オフセット平面からの下がり寸法
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "base_depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "tip_depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "tip_offset": _FI(py_type=float, data_type=_DT.FLOAT),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_ConventionalTaper"


class StbSecSlabRcConventionalStraight(StBridgeElement):
    """ＲＣ在来スラブ断面形状・ストレート：StbSecSlab_RC_ConventionalStraight

    Attributes:
        depth (float): 属性 厚さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_ConventionalStraight"


class StbSecFigureSlabRcConventional(StBridgeElement):
    """ＲＣ在来スラブ断面形状：StbSecFigureSlab_RC_Conventional

    Attributes:
        stb_sec_slab_rc_conventional_straight (StbSecSlabRcConventionalStraight): 子要素 StbSecSlab_RC_ConventionalStraight(ＲＣ在来スラブ断面形状・ストレート)
        stb_sec_slab_rc_conventional_taper (StbSecSlabRcConventionalTaper): 子要素 StbSecSlab_RC_ConventionalTaper(ＲＣ在来スラブ断面形状・テーパー)
        stb_sec_slab_rc_conventional_haunch (StbSecSlabRcConventionalHaunch): 子要素 StbSecSlab_RC_ConventionalHaunch(ＲＣ在来スラブ断面形状・ハンチ)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_slab_rc_conventional_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSlabRcConventionalStraight
        ),
        "stb_sec_slab_rc_conventional_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSlabRcConventionalTaper
        ),
        "stb_sec_slab_rc_conventional_haunch": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSlabRcConventionalHaunch
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecFigureSlab_RC_Conventional"


class StbSecSlabRcConventional(StBridgeElement):
    """ＲＣスラブ在来断面：StbSecSlab_RC_Conventional

    Attributes:
        stb_sec_figure_slab_rc_conventional (StbSecFigureSlabRcConventional): 子要素 StbSecFigureSlab_RC_Conventional(ＲＣ在来スラブ断面形状)
        stb_sec_bar_arrangement_slab_rc_conventional (StbSecBarArrangementSlabRcConventional): 子要素 StbSecBarArrangementSlab_RC_Conventional(ＲＣ在来スラブ断面配筋)
        stb_sec_formwork_slab (StbSecFormworkSlab): 子要素 StbSecFormworkSlab(型枠要素)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_figure_slab_rc_conventional": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecFigureSlabRcConventional,
        ),
        "stb_sec_bar_arrangement_slab_rc_conventional": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            py_type=StbSecBarArrangementSlabRcConventional,
        ),
        "stb_sec_formwork_slab": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecFormworkSlab
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSlab_RC_Conventional"


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
        stb_sec_slab_rc_conventional (StbSecSlabRcConventional): 子要素 StbSecSlab_RC_Conventional(ＲＣスラブ在来断面)
        stb_sec_slab_rc_truss (StbSecSlabRcTruss): 子要素 StbSecSlab_RC_Truss(ＲＣスラブトラス断面)
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
        "stb_sec_slab_rc_conventional": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSlabRcConventional
        ),
        "stb_sec_slab_rc_truss": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSlabRcTruss
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
        stb_sec_steel_brace_s_same (StbSecSteelBraceSSame): 子要素 StbSecSteelBrace_S_Same(Ｓブレース断面鉄骨形状・同一)
        stb_sec_steel_brace_s_not_same (list[StbSecSteelBraceSNotSame]): 子要素 StbSecSteelBrace_S_NotSame(Ｓブレース断面鉄骨形状・頭脚部別)
        stb_sec_steel_brace_s_three_types (list[StbSecSteelBraceSThreeTypes]): 子要素 StbSecSteelBrace_S_ThreeTypes(Ｓブレース断面鉄骨形状・３種類)
    """

    _fields: ClassVar[dict[str, _FI]] = {
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


class StbSecSteelBeamSrcShape(StBridgeElement):
    """SRC梁断面任意鉄骨形状：StbSecSteelBeam_SRC_Shape

    Attributes:
        order (int): 属性 左端からの順番
        stb_sec_steel_beam_straight (StbSecSteelBeamStraight): 子要素 StbSecSteelBeamStraight(ストレート要素)
        stb_sec_steel_beam_taper (StbSecSteelBeamTaper): 子要素 StbSecSteelBeamTaper(テーパー要素)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_sec_steel_beam_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelBeamStraight"
        ),
        "stb_sec_steel_beam_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelBeamTaper"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_SRC_Shape"


class StbSecSteelFigureBeamSrc(StBridgeElement):
    """ＳＲＣ梁断面鉄骨形状：StbSecSteelFigureBeam_SRC

    Attributes:
        stb_sec_steel_beam_src_shape (list[StbSecSteelBeamSrcShape]): 子要素 StbSecSteelBeam_SRC_Shape(SRC梁断面任意鉄骨形状)
        stb_sec_steel_beam_widening (list[StbSecSteelBeamWidening]): 子要素 StbSecSteelBeamWidening(拡幅要素)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_steel_beam_src_shape": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecSteelBeamSrcShape]
        ),
        "stb_sec_steel_beam_widening": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type="list[StbSecSteelBeamWidening]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelFigureBeam_SRC"


class StbSecBarArrangementBeamSrc(StBridgeElement):
    """ＳＲＣ梁断面配筋：StbSecBarArrangementBeam_SRC

    Attributes:
        order (int): 属性 始端からの順番
        d_bar_spacing (str): 属性 巾止筋：径
        strength_bar_spacing (str): 属性 巾止筋：鉄筋強度
        pitch_bar_spacing (float): 属性 巾止筋：ピッチ
        d_catch_bar (str): 属性 段取り筋
        strength_catch_bar (str): 属性 段取り筋強度
        stb_sec_bar_beam_simple (StbSecBarBeamSimple): 子要素 StbSecBarBeamSimple(コンクリート梁断面配筋・簡易)
        stb_sec_bar_beam_complex (StbSecBarBeamComplex): 子要素 StbSecBarBeamComplex(コンクリート梁断面配筋・３種類・詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "d_catch_bar": _FI(py_type=str, data_type=_DT.STR, xml_name="D_catch_bar"),
        "strength_catch_bar": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_beam_simple": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBarBeamSimple"
        ),
        "stb_sec_bar_beam_complex": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBarBeamComplex"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementBeam_SRC"


class StbSecFigureBeamSrc(StBridgeElement):
    """ＳＲＣ梁断面形状：StbSecFigureBeam_SRC

    Attributes:
        order (int): 属性 始端からの順番
        stb_sec_beam_straight (StbSecBeamStraight): 子要素 StbSecBeamStraight(コンクリート梁断面形状・ストレート)
        stb_sec_beam_taper (StbSecBeamTaper): 子要素 StbSecBeamTaper(コンクリート梁断面形状・テーパー)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_sec_beam_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBeamStraight"
        ),
        "stb_sec_beam_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBeamTaper"
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
        stb_sec_figure_beam_src (list[StbSecFigureBeamSrc]): 子要素 StbSecFigureBeam_SRC(ＳＲＣ梁断面形状)
        stb_sec_bar_arrangement_beam_src (list[StbSecBarArrangementBeamSrc]): 子要素 StbSecBarArrangementBeam_SRC(ＳＲＣ梁断面配筋)
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
            kind=_FK.ELEMENT, py_type=list[StbSecFigureBeamSrc]
        ),
        "stb_sec_bar_arrangement_beam_src": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecBarArrangementBeamSrc]
        ),
        "stb_sec_steel_figure_beam_src": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelFigureBeamSrc
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_SRC"


class StbSecSteelBeamWidening(StBridgeElement):
    """拡幅要素：StbSecSteelBeamWidening

    Attributes:
        pos (StbSecSteelBeamWideningPos): 属性 形状位置以下のいずれかSTART（始端）END（終端）
        l1 (float): 属性 水平部長さ
        l2 (float): 属性 サイドPL長さ
        l3 (float): 属性 サイドPL水平長さ
        l4 (float): 属性 サイドPL先端立ち上がり長さ
        is_weld (bool): 属性 溶接する／一枚板
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelBeamWideningPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "l1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "l2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "l3": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "l4": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "is_weld": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isWeld"),
    }


class StbSecSteelBeamTaper(StBridgeElement):
    """テーパー要素：StbSecSteelBeamTaper

    Attributes:
        start_shape (str): 属性 始端側形状
        end_shape (str): 属性 終端側形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
        start_horizontal_offset (float): 属性 始端側の左右方向のオフセット
        start_vertical_offset (float): 属性 始端側の上下方向のオフセット
        end_horizontal_offset (float): 属性 終端側の左右方向のオフセット
        end_vertical_offset (float): 属性 終端側の上下方向のオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "start_shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "end_shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "start_horizontal_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "start_vertical_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_horizontal_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_vertical_offset": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbSecSteelBeamStraight(StBridgeElement):
    """ストレート要素：StbSecSteelBeamStraight

    Attributes:
        shape (str): 属性 形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
        horizontal_offset (float): 属性 左右方向のオフセット
        vertical_offset (float): 属性 上下方向のオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_main": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "horizontal_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "vertical_offset": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbSecSteelBeamSShape(StBridgeElement):
    """Ｓ梁断面任意鉄骨形状：StbSecSteelBeam_S_Shape

    Attributes:
        order (int): 属性 順番
        stb_sec_steel_beam_straight (StbSecSteelBeamStraight): 子要素 StbSecSteelBeamStraight(ストレート要素)
        stb_sec_steel_beam_taper (StbSecSteelBeamTaper): 子要素 StbSecSteelBeamTaper(テーパー要素)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_sec_steel_beam_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelBeamStraight
        ),
        "stb_sec_steel_beam_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelBeamTaper
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelBeam_S_Shape"


class StbSecSteelFigureBeamS(StBridgeElement):
    """Ｓ梁断面鉄骨形状：StbSecSteelFigureBeam_S

    Attributes:
        stb_sec_steel_beam_s_shape (list[StbSecSteelBeamSShape]): 子要素 StbSecSteelBeam_S_Shape(Ｓ梁断面任意鉄骨形状)
        stb_sec_steel_beam_widening (list[StbSecSteelBeamWidening]): 子要素 StbSecSteelBeamWidening(拡幅要素)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_steel_beam_s_shape": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecSteelBeamSShape]
        ),
        "stb_sec_steel_beam_widening": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbSecSteelBeamWidening]
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
        d_main (str): 属性 主筋径
        n_main_top (int): 属性 主筋：上端1段目
        n_main_bottom (int): 属性 主筋：下端1段目
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
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


class StbSecBarBeamComplexWebLoc(StBridgeElement):
    """コンクリート梁断面配筋・詳細・腹筋位置：StbSecBarBeamComplexWebLoc

    Attributes:
        distance (float): 属性 コンクリート上端から鉄筋芯までの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarBeamComplexWeb(StBridgeElement):
    """コンクリート梁断面配筋・詳細・腹筋：StbSecBarBeamComplexWeb

    Attributes:
        d (str): 属性 鉄筋筋径
        strength (str): 属性 鉄筋強度
        stb_sec_bar_beam_complex_web_loc (list[StbSecBarBeamComplexWebLoc]): 子要素 StbSecBarBeamComplexWebLoc(コンクリート梁断面配筋・詳細・腹筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_beam_complex_web_loc": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecBarBeamComplexWebLoc]
        ),
    }


class StbSecBarBeamComplexStirrupLoc(StBridgeElement):
    """コンクリート梁断面配筋・詳細・あばら筋位置：StbSecBarBeamComplexStirrupLoc

    Attributes:
        distance (float): 属性 コンクリート左端から鉄筋芯までの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarBeamComplexStirrup(StBridgeElement):
    """コンクリート梁断面配筋・詳細・あばら筋：StbSecBarBeamComplexStirrup

    Attributes:
        d (str): 属性 鉄筋径
        strength (str): 属性 鉄筋強度
        pitch (float): 属性 ピッチ
        stb_sec_bar_beam_complex_stirrup_loc (list[StbSecBarBeamComplexStirrupLoc]): 子要素 StbSecBarBeamComplexStirrupLoc(コンクリート梁断面配筋・詳細・あばら筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "stb_sec_bar_beam_complex_stirrup_loc": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecBarBeamComplexStirrupLoc]
        ),
    }


class StbSecBarBeamComplexMainLoc(StBridgeElement):
    """コンクリート梁断面配筋・詳細・主筋位置：StbSecBarBeamComplexMainLoc

    Attributes:
        distance (float): 属性 コンクリート左端から鉄筋芯までの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarBeamComplexMainLine(StBridgeElement):
    """コンクリート梁断面配筋・詳細・主筋・各行：StbSecBarBeamComplexMainLine

    Attributes:
        step (int): 属性 段数
        depth (float): 属性 コンクリート端（上端の場合は上面、下端の場合は下面）から鉄筋芯までの距離
        d (str): 属性 主筋径
        strength (str): 属性 主筋強度
        stb_sec_bar_beam_complex_main_loc (list[StbSecBarBeamComplexMainLoc]): 子要素 StbSecBarBeamComplexMainLoc(コンクリート梁断面配筋・詳細・主筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "step": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_beam_complex_main_loc": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecBarBeamComplexMainLoc]
        ),
    }


class StbSecBarBeamComplexMain(StBridgeElement):
    """コンクリート梁断面配筋・詳細・主筋：StbSecBarBeamComplexMain

    Attributes:
        pos (StbSecBarBeamComplexMainPos): 属性 配置位置以下のいずれかBOTTOM：下端TOP：上端
        stb_sec_bar_beam_complex_main_line (list[StbSecBarBeamComplexMainLine]): 子要素 StbSecBarBeamComplexMainLine(コンクリート梁断面配筋・詳細・主筋・各行)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarBeamComplexMainPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "stb_sec_bar_beam_complex_main_line": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecBarBeamComplexMainLine]
        ),
    }


class StbSecBarBeamComplex(StBridgeElement):
    """コンクリート梁断面配筋・３種類・詳細：StbSecBarBeamComplex

    Attributes:
        stb_sec_bar_beam_complex_main (list[StbSecBarBeamComplexMain]): 子要素 StbSecBarBeamComplexMain(コンクリート梁断面配筋・詳細・主筋)
        stb_sec_bar_beam_complex_stirrup (StbSecBarBeamComplexStirrup): 子要素 StbSecBarBeamComplexStirrup(コンクリート梁断面配筋・詳細・あばら筋)
        stb_sec_bar_beam_complex_web (StbSecBarBeamComplexWeb): 子要素 StbSecBarBeamComplexWeb(コンクリート梁断面配筋・詳細・腹筋)
        stb_sec_bar_beam_additional (list[StbSecBarBeamAdditional]): 子要素 StbSecBarBeamAdditional(コンクリート梁断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_bar_beam_complex_main": _FI(
            kind=_FK.ELEMENT,
            max_occurs=2,
            min_occurs=2,
            py_type=list[StbSecBarBeamComplexMain],
        ),
        "stb_sec_bar_beam_complex_stirrup": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBarBeamComplexStirrup,
        ),
        "stb_sec_bar_beam_complex_web": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarBeamComplexWeb
        ),
        "stb_sec_bar_beam_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarBeamAdditional]"
        ),
    }


class StbSecBarBeamAdditional(StBridgeElement):
    """コンクリート梁断面配筋・追加鉄筋：StbSecBarBeamAdditional

    Attributes:
        d (str): 属性 径
        strength (str): 属性 強度
        y (float): 属性 Y座標
        z (float): 属性 Z座標
        is_structural (bool): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "z": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Z"),
        "is_structural": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isStructural"),
    }


class StbSecBarBeamSimpleMain(StBridgeElement):
    """コンクリート梁断面配筋・簡易主筋：StbSecBarBeamSimpleMain

    Attributes:
        pos (StbSecBarBeamSimpleMainPos): 属性 配置位置以下のいずれかBOTTOM：下端TOP：上端
        step (int): 属性 段数
        d (str): 属性 主筋径
        strength (str): 属性 主筋強度
        n (int): 属性 主筋本数
        n_left (int): 属性 左側に寄せて配置する本数
        n_right (int): 属性 右側に寄せて配置する本数
        interval (float): 属性 寄せ筋間隔
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarBeamSimpleMainPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "step": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "n": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N",
        ),
        "n_left": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_left",
        ),
        "n_right": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_right",
        ),
        "interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
    }


class StbSecBarBeamSimple(StBridgeElement):
    """コンクリート梁断面配筋・簡易：StbSecBarBeamSimple

    Attributes:
        depth_cover_left (float): 属性 かぶり厚さ（左）
        depth_cover_right (float): 属性 かぶり厚さ（右）
        depth_cover_top (float): 属性 かぶり厚さ（上）
        depth_cover_bottom (float): 属性 かぶり厚さ（下）
        interval (float): 属性 ２段筋のあき
        center_top (float): 属性 主筋重心位置（上）
        center_bottom (float): 属性 主筋重心位置（下）
        center_side (float): 属性 主筋重心位置（側）
        center_interval (float): 属性 ２段筋重心間距離
        d_stirrup (str): 属性 あばら筋：径
        n_stirrup (int): 属性 あばら筋：本数
        strength_stirrup (str): 属性 あばら筋：鉄筋強度
        pitch_stirrup (float): 属性 あばら筋：ピッチ
        d_web (str): 属性 腹筋：径
        n_web (int): 属性 腹筋：本数
        strength_web (str): 属性 腹筋：鉄筋強度
        stb_sec_bar_beam_simple_main (list[StbSecBarBeamSimpleMain]): 子要素 StbSecBarBeamSimpleMain(コンクリート梁断面配筋・簡易主筋)
        stb_sec_bar_beam_additional (list[StbSecBarBeamAdditional]): 子要素 StbSecBarBeamAdditional(コンクリート梁断面配筋・追加鉄筋)
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
        "d_stirrup": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="D_stirrup"
        ),
        "n_stirrup": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_stirrup",
        ),
        "strength_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "pitch_stirrup": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d_web": _FI(py_type=str, data_type=_DT.STR, xml_name="D_web"),
        "n_web": _FI(py_type=int, data_type=_DT.INT, xml_name="N_web"),
        "strength_web": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_beam_simple_main": _FI(
            kind=_FK.ELEMENT, min_occurs=2, py_type=list[StbSecBarBeamSimpleMain]
        ),
        "stb_sec_bar_beam_additional": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecBarBeamAdditional]
        ),
    }


class StbSecBarArrangementBeamRc(StBridgeElement):
    """ＲＣ梁断面配筋：StbSecBarArrangementBeam_RC

    Attributes:
        order (int): 属性 配筋位置始端からの番号
        d_bar_spacing (str): 属性 巾止筋：径
        strength_bar_spacing (str): 属性 巾止筋：鉄筋強度
        pitch_bar_spacing (float): 属性 巾止筋：ピッチ
        d_catch_bar (str): 属性 段取り筋
        strength_catch_bar (str): 属性 段取り筋強度
        stb_sec_bar_beam_simple (StbSecBarBeamSimple): 子要素 StbSecBarBeamSimple(コンクリート梁断面配筋・簡易)
        stb_sec_bar_beam_complex (StbSecBarBeamComplex): 子要素 StbSecBarBeamComplex(コンクリート梁断面配筋・３種類・詳細)
        stb_sec_bar_beam_x_reinforced (StbSecBarBeamXReinforced): 子要素 StbSecBarBeamXReinforced(コンクリート梁 Ｘ形配筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "d_catch_bar": _FI(py_type=str, data_type=_DT.STR, xml_name="D_catch_bar"),
        "strength_catch_bar": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_beam_simple": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarBeamSimple
        ),
        "stb_sec_bar_beam_complex": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarBeamComplex
        ),
        "stb_sec_bar_beam_x_reinforced": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarBeamXReinforced
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementBeam_RC"


class StbSecBeamTaper(StBridgeElement):
    """コンクリート梁断面形状・テーパー：StbSecBeamTaper

    Attributes:
        start_width (float): 属性 始端側の幅
        start_depth (float): 属性 始端側の成
        end_width (float): 属性 終端側の幅
        end_depth (float): 属性 終端側の成
        start_horizontal_offset (float): 属性 始端側の水平方向のオフセット
        start_vertical_offset (float): 属性
        end_horizontal_offset (float): 属性 終端側の水平方向のオフセット
        end_vertical_offset (float): 属性 終端側の鉛直方向のオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "start_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "start_depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "end_width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "end_depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "start_horizontal_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "start_vertical_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_horizontal_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "end_vertical_offset": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbSecBeamStraight(StBridgeElement):
    """コンクリート梁断面形状・ストレート：StbSecBeamStraight

    Attributes:
        width (float): 属性 幅
        depth (float): 属性 成
        horizontal_offset (float): 属性 水平方向のオフセット
        vertical_offset (float): 属性 鉛直方向のオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "width": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "depth": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "horizontal_offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "vertical_offset": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbSecFigureBeamRc(StBridgeElement):
    """ＲＣ梁断面形状：StbSecFigureBeam_RC

    Attributes:
        order (int): 属性 始端からの順番
        stb_sec_beam_straight (StbSecBeamStraight): 子要素 StbSecBeamStraight(コンクリート梁断面形状・ストレート)
        stb_sec_beam_taper (StbSecBeamTaper): 子要素 StbSecBeamTaper(コンクリート梁断面形状・テーパー)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_sec_beam_straight": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBeamStraight
        ),
        "stb_sec_beam_taper": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBeamTaper
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
        stb_sec_figure_beam_rc (list[StbSecFigureBeamRc]): 子要素 StbSecFigureBeam_RC(ＲＣ梁断面形状)
        stb_sec_bar_arrangement_beam_rc (list[StbSecBarArrangementBeamRc]): 子要素 StbSecBarArrangementBeam_RC(ＲＣ梁断面配筋)
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
            kind=_FK.ELEMENT, py_type=list[StbSecFigureBeamRc]
        ),
        "stb_sec_bar_arrangement_beam_rc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecBarArrangementBeamRc]
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBeam_RC"


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
        stb_sec_base_product (StbSecBaseProduct): 子要素 StbSecBaseProduct(鉄骨断面柱脚製品)
        stb_sec_base_conventional (StbSecBaseConventional): 子要素 StbSecBaseConventional(鉄骨断面柱脚在来工法)
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
        "stb_sec_base_product": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBaseProduct"
        ),
        "stb_sec_base_conventional": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBaseConventional"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_CFT"


class StbSecSteelColumnSrcThreeTypes(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・３種類：StbSecSteelColumn_SRC_ThreeTypes

    Attributes:
        pos (StbSecSteelColumnSrcThreeTypesPos): 属性 配置位置 以下のいずれかBOTTOM（柱脚） CENTER（中央）TOP（柱頭）
        stb_sec_steel_column_src_shape_h (StbSecSteelColumnSrcShapeH): 子要素 StbSecSteelColumn_SRC_ShapeH(ＳＲＣ柱断面鉄骨形状・Ｈ形)
        stb_sec_steel_column_src_shape_box (StbSecSteelColumnSrcShapeBox): 子要素 StbSecSteelColumn_SRC_ShapeBox(ＳＲＣ柱断面鉄骨形状・□形)
        stb_sec_steel_column_src_shape_pipe (StbSecSteelColumnSrcShapePipe): 子要素 StbSecSteelColumn_SRC_ShapePipe(ＳＲＣ柱断面鉄骨形状・○形)
        stb_sec_steel_column_src_shape_cross1 (StbSecSteelColumnSrcShapeCross1): 子要素 StbSecSteelColumn_SRC_ShapeCross1(ＳＲＣ柱断面鉄骨形状・＋形（H+H）)
        stb_sec_steel_column_src_shape_cross2 (StbSecSteelColumnSrcShapeCross2): 子要素 StbSecSteelColumn_SRC_ShapeCross2(ＳＲＣ柱断面鉄骨形状・＋形（H+T+T）)
        stb_sec_steel_column_src_shape_t (StbSecSteelColumnSrcShapeT): 子要素 StbSecSteelColumn_SRC_ShapeT(ＳＲＣ柱断面鉄骨形状・Ｔ形)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnSrcThreeTypesPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "CENTER", "TOP"),
        ),
        "stb_sec_steel_column_src_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeH"
        ),
        "stb_sec_steel_column_src_shape_box": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeBox"
        ),
        "stb_sec_steel_column_src_shape_pipe": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapePipe"
        ),
        "stb_sec_steel_column_src_shape_cross1": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeCross1"
        ),
        "stb_sec_steel_column_src_shape_cross2": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeCross2"
        ),
        "stb_sec_steel_column_src_shape_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeT"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ThreeTypes"


class StbSecSteelColumnSrcNotSame(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・柱頭脚別：StbSecSteelColumn_SRC_NotSame

    Attributes:
        pos (StbSecSteelColumnSrcNotSamePos): 属性 配置位置 以下のいずれかBOTTOM（柱脚）TOP（柱頭）
        stb_sec_steel_column_src_shape_h (StbSecSteelColumnSrcShapeH): 子要素 StbSecSteelColumn_SRC_ShapeH(ＳＲＣ柱断面鉄骨形状・Ｈ形)
        stb_sec_steel_column_src_shape_box (StbSecSteelColumnSrcShapeBox): 子要素 StbSecSteelColumn_SRC_ShapeBox(ＳＲＣ柱断面鉄骨形状・□形)
        stb_sec_steel_column_src_shape_pipe (StbSecSteelColumnSrcShapePipe): 子要素 StbSecSteelColumn_SRC_ShapePipe(ＳＲＣ柱断面鉄骨形状・○形)
        stb_sec_steel_column_src_shape_cross1 (StbSecSteelColumnSrcShapeCross1): 子要素 StbSecSteelColumn_SRC_ShapeCross1(ＳＲＣ柱断面鉄骨形状・＋形（H+H）)
        stb_sec_steel_column_src_shape_cross2 (StbSecSteelColumnSrcShapeCross2): 子要素 StbSecSteelColumn_SRC_ShapeCross2(ＳＲＣ柱断面鉄骨形状・＋形（H+T+T）)
        stb_sec_steel_column_src_shape_t (StbSecSteelColumnSrcShapeT): 子要素 StbSecSteelColumn_SRC_ShapeT(ＳＲＣ柱断面鉄骨形状・Ｔ形)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecSteelColumnSrcNotSamePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "stb_sec_steel_column_src_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeH"
        ),
        "stb_sec_steel_column_src_shape_box": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeBox"
        ),
        "stb_sec_steel_column_src_shape_pipe": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapePipe"
        ),
        "stb_sec_steel_column_src_shape_cross1": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeCross1"
        ),
        "stb_sec_steel_column_src_shape_cross2": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeCross2"
        ),
        "stb_sec_steel_column_src_shape_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecSteelColumnSrcShapeT"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_NotSame"


class StbSecSteelColumnSrcShapeT(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・Ｔ形：StbSecSteelColumn_SRC_ShapeT

    Attributes:
        direction_type (StbSecSteelColumnSrcShapeTDirectionType): 属性 鉄骨の向き 以下のいずれかT1：┬、T2：┤、T3：┴、T4：├
        shape_h (str): 属性 H形鋼鉄骨形状
        shape_t (str): 属性 T形鋼鉄骨形状
        strength_main_h (str): 属性 H形鋼鉄骨強度（主）
        strength_web_h (str): 属性 H形鋼鉄骨強度（ウェブ）
        strength_main_t (str): 属性 T形鋼鉄骨強度（主）
        strength_web_t (str): 属性 T形鋼鉄骨強度（ウェブ）
        offset_hx (float): 属性 H形鋼鉄骨の偏心（X方向）
        offset_hy (float): 属性 H形鋼鉄骨の偏心（Y方向）
        offset_t (float): 属性 T形鋼鉄骨の偏心（Y方向）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecSteelColumnSrcShapeTDirectionType,
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
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ShapeT"


class StbSecSteelColumnSrcShapeCross2(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・＋形（H+T+T）：StbSecSteelColumn_SRC_ShapeCross2

    Attributes:
        direction_type (StbSecSteelColumnSrcShapeCross2DirectionType): 属性 H形鋼鉄骨の向き 以下のいずれかH（同方向）、I（直交）
        shape_h (str): 属性 H形鋼鉄骨形状
        shape_t1 (str): 属性 T形鋼鉄骨形状1
        shape_t2 (str): 属性 T形鋼鉄骨形状2
        strength_main_h (str): 属性 H形鋼鉄骨強度（主）
        strength_web_h (str): 属性 H形鋼鉄骨強度（ウェブ）
        strength_main_t (str): 属性 T形鋼鉄骨強度（主）
        strength_web_t (str): 属性 T形鋼鉄骨強度（ウェブ）
        offset_hx (float): 属性 H形鋼鉄骨の偏心（X方向）
        offset_hy (float): 属性 H形鋼鉄骨の偏心（Y方向）
        offset_t (float): 属性 T形鋼鉄骨の偏心
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecSteelColumnSrcShapeCross2DirectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("H", "I"),
        ),
        "shape_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_H"
        ),
        "shape_t1": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_T1"
        ),
        "shape_t2": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="shape_T2"
        ),
        "strength_main_h": _FI(
            py_type=str, data_type=_DT.STR, required=True, xml_name="strength_main_H"
        ),
        "strength_web_h": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_H"
        ),
        "strength_main_t": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_main_T"
        ),
        "strength_web_t": _FI(
            py_type=str, data_type=_DT.STR, xml_name="strength_web_T"
        ),
        "offset_hx": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HX"),
        "offset_hy": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_HY"),
        "offset_t": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_T"),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ShapeCross2"


class StbSecSteelColumnSrcShapeCross1(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・＋形（H+H）：StbSecSteelColumn_SRC_ShapeCross1

    Attributes:
        shape_x (str): 属性 X方向鉄骨形状
        shape_y (str): 属性 Y方向鉄骨形状
        strength_main_x (str): 属性 X方向鉄骨強度（主）
        strength_web_x (str): 属性 X方向鉄骨強度（ウェブ）
        strength_main_y (str): 属性 Y方向鉄骨強度（主）
        strength_web_y (str): 属性 Y方向鉄骨強度（ウェブ）
        offset_xx (float): 属性 X方向鉄骨の偏心（X方向）
        offset_xy (float): 属性 X方向鉄骨の偏心（Y方向）
        offset_yx (float): 属性 Y方向鉄骨の偏心（X方向）
        offset_yy (float): 属性 Y方向鉄骨の偏心（Y方向）
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
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ShapeCross1"


class StbSecSteelColumnSrcShapePipe(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・○形：StbSecSteelColumn_SRC_ShapePipe

    Attributes:
        shape (str): 属性 鋼管形状
        encase_type (StbSecSteelColumnSrcShapePipeEncaseType): 属性 鋼管コンクリートのタイプ以下のいずれかENCASED（被覆形）ENCASEDANDINFILLED（充填被覆形）
        strength (str): 属性 鉄骨強度
        offset_x (float): 属性 鉄骨の偏心（X方向）
        offset_y (float): 属性 鉄骨の偏心（Y方向）
        strength_inner_concrete (str): 属性 充填コンクリート強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecSteelColumnSrcShapePipeEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
        "strength_inner_concrete": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ShapePipe"


class StbSecSteelColumnSrcShapeBox(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・□形：StbSecSteelColumn_SRC_ShapeBox

    Attributes:
        shape (str): 属性 角形鋼管形状
        encase_type (StbSecSteelColumnSrcShapeBoxEncaseType): 属性 鋼管コンクリートのタイプ以下のいずれかENCASED（被覆形）ENCASEDANDINFILLED（充填被覆形）
        strength (str): 属性 鉄骨強度
        offset_x (float): 属性 鉄骨の偏心（X方向）
        offset_y (float): 属性 鉄骨の偏心（Y方向）
        strength_inner_concrete (str): 属性 充填コンクリート強度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "shape": _FI(py_type=str, data_type=_DT.STR, required=True),
        "encase_type": _FI(
            py_type=StbSecSteelColumnSrcShapeBoxEncaseType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("ENCASED", "ENCASEDANDINFILLED"),
        ),
        "strength": _FI(py_type=str, data_type=_DT.STR, required=True),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
        "strength_inner_concrete": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ShapeBox"


class StbSecSteelColumnSrcShapeH(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・Ｈ形：StbSecSteelColumn_SRC_ShapeH

    Attributes:
        direction_type (StbSecSteelColumnSrcShapeHDirectionType): 属性 鉄骨の向き 以下のいずれかH（同方向）、I（直交）
        shape (str): 属性 鉄骨形状
        strength_main (str): 属性 鉄骨強度（主）
        strength_web (str): 属性 鉄骨強度（ウェブ）
        offset_x (float): 属性 鉄骨の偏心（X方向）
        offset_y (float): 属性 鉄骨の偏心（Y方向）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "direction_type": _FI(
            py_type=StbSecSteelColumnSrcShapeHDirectionType,
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
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_ShapeH"


class StbSecSteelColumnSrcSame(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状・同一：StbSecSteelColumn_SRC_Same

    Attributes:
        stb_sec_steel_column_src_shape_h (StbSecSteelColumnSrcShapeH): 子要素 StbSecSteelColumn_SRC_ShapeH(ＳＲＣ柱断面鉄骨形状・Ｈ形)
        stb_sec_steel_column_src_shape_box (StbSecSteelColumnSrcShapeBox): 子要素 StbSecSteelColumn_SRC_ShapeBox(ＳＲＣ柱断面鉄骨形状・□形)
        stb_sec_steel_column_src_shape_pipe (StbSecSteelColumnSrcShapePipe): 子要素 StbSecSteelColumn_SRC_ShapePipe(ＳＲＣ柱断面鉄骨形状・○形)
        stb_sec_steel_column_src_shape_cross1 (StbSecSteelColumnSrcShapeCross1): 子要素 StbSecSteelColumn_SRC_ShapeCross1(ＳＲＣ柱断面鉄骨形状・＋形（H+H）)
        stb_sec_steel_column_src_shape_cross2 (StbSecSteelColumnSrcShapeCross2): 子要素 StbSecSteelColumn_SRC_ShapeCross2(ＳＲＣ柱断面鉄骨形状・＋形（H+T+T）)
        stb_sec_steel_column_src_shape_t (StbSecSteelColumnSrcShapeT): 子要素 StbSecSteelColumn_SRC_ShapeT(ＳＲＣ柱断面鉄骨形状・Ｔ形)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_steel_column_src_shape_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSrcShapeH
        ),
        "stb_sec_steel_column_src_shape_box": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSrcShapeBox
        ),
        "stb_sec_steel_column_src_shape_pipe": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSrcShapePipe
        ),
        "stb_sec_steel_column_src_shape_cross1": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSrcShapeCross1
        ),
        "stb_sec_steel_column_src_shape_cross2": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSrcShapeCross2
        ),
        "stb_sec_steel_column_src_shape_t": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteelColumnSrcShapeT
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecSteelColumn_SRC_Same"


class StbSecSteelFigureColumnSrc(StBridgeElement):
    """ＳＲＣ柱断面鉄骨形状：StbSecSteelFigureColumn_SRC

    Attributes:
        base_type (StbSecSteelFigureColumnSrcBaseType): 属性 柱脚形式 以下のいずれかNONE（鉄骨柱脚なし）UNEMBEDDED（非埋込）UNEMBEDDED2（非埋込）EMBEDDED（埋込）
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


class StbSecBarArrangementColumnSrc(StBridgeElement):
    """ＳＲＣ柱断面配筋：StbSecBarArrangementColumn_SRC

    Attributes:
        stb_sec_bar_column_rect_same (StbSecBarColumnRectSame): 子要素 StbSecBarColumnRectSame(コンクリート柱断面配筋・矩形・同一)
        stb_sec_bar_column_rect_not_same (list[StbSecBarColumnRectNotSame]): 子要素 StbSecBarColumnRectNotSame(コンクリート柱断面配筋・矩形・柱頭脚別)
        stb_sec_bar_column_circle_same (StbSecBarColumnCircleSame): 子要素 StbSecBarColumnCircleSame(コンクリート柱断面配筋・円形・同一)
        stb_sec_bar_column_circle_not_same (list[StbSecBarColumnCircleNotSame]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_bar_column_rect_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBarColumnRectSame"
        ),
        "stb_sec_bar_column_rect_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type="list[StbSecBarColumnRectNotSame]"
        ),
        "stb_sec_bar_column_circle_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBarColumnCircleSame"
        ),
        "stb_sec_bar_column_circle_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type="list[StbSecBarColumnCircleNotSame]"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementColumn_SRC"


class StbSecFigureColumnSrc(StBridgeElement):
    """ＳＲＣ柱断面形状：StbSecFigureColumn_SRC

    Attributes:
        stb_sec_column_rect (StbSecColumnRect): 子要素 StbSecColumnRect(コンクリート柱断面形状・矩形)
        stb_sec_column_circle (StbSecColumnCircle): 子要素 StbSecColumnCircle(コンクリート柱断面形状・円形)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_column_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecColumnRect"
        ),
        "stb_sec_column_circle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecColumnCircle"
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
        stb_sec_base_product (StbSecBaseProduct): 子要素 StbSecBaseProduct(鉄骨断面柱脚製品)
        stb_sec_base_conventional (StbSecBaseConventional): 子要素 StbSecBaseConventional(鉄骨断面柱脚在来工法)
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
        "stb_sec_base_product": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBaseProduct"
        ),
        "stb_sec_base_conventional": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBaseConventional"
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_SRC"


class StbSecBaseConventionalRibPlate(StBridgeElement):
    """鉄骨断面柱脚在来工法・リブプレート：StbSecBaseConventionalRibPlate

    Attributes:
        id_order (int): 属性 リブプレートの番号
        offset_x (float): 属性 オフセット(X)
        offset_y (float): 属性 オフセット(Y)
        angle (float): 属性 角度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
        "angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
    }


class StbSecBaseConventionalRibPlates(StBridgeElement):
    """鉄骨断面柱脚在来工法・リブプレート：StbSecBaseConventionalRibPlates

    Attributes:
        a1 (float): 属性 リブプレートの長さ
        a2 (float): 属性 リブプレートの長さ
        b1 (float): 属性 リブプレートの高さ
        b2 (float): 属性 リブプレートの高さ
        t (float): 属性 リブプレートの厚さ
        strength (str): 属性 リブプレート鉄骨強度
        stb_sec_base_conventional_rib_plate (list[StbSecBaseConventionalRibPlate]): 子要素 StbSecBaseConventionalRibPlate(鉄骨断面柱脚在来工法・リブプレート)
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
        "stb_sec_base_conventional_rib_plate": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbSecBaseConventionalRibPlate]
        ),
    }


class StbSecBaseConventionalAnchorBolt(StBridgeElement):
    """鉄骨断面柱脚在来工法・アンカーボルト詳細：StbSecBaseConventionalAnchorBolt

    Attributes:
        id_order (int): 属性 ボルトの番号
        offset_x (float): 属性 オフセット(X)
        offset_y (float): 属性 オフセット(Y)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
    }


class StbSecBaseConventionalAnchorBolts(StBridgeElement):
    """鉄骨断面柱脚在来工法・アンカーボルト：StbSecBaseConventionalAnchorBolts

    Attributes:
        kind_bolt (StbSecBaseConventionalAnchorBoltsKindBolt): 属性 アンカーボルト種別で以下のいずれかSTD（建方用アンカーボルト）ABR（JIS B 1220 ABRアンカーボルト[転造ねじ]）ABM（JIS B 1221 ABMアンカーボルト[切削ねじ]）
        name_bolt (str): 属性 アンカーボルト径（ねじの呼びd）
        l (float): 属性 アンカーボルト定着長
        strength_bolt (str): 属性 アンカーボルト強度
        type_bolt (StbSecBaseConventionalAnchorBoltsTypeBolt): 属性 アンカーボルト形状で以下のいずれかI：I型J：J型L：L型LHOOK：L型フックHOLEIN：ホールインアンカー
        r1 (float): 属性 アンカーボルト曲げ半径
        r2 (float): 属性 アンカーボルト曲げ半径2
        lt (float): 属性 アンカーボルト全長
        s1 (float): 属性 アンカーボルト余長（上）
        s2 (float): 属性 アンカーボルト余長（下）
        l1 (float): 属性 埋め込み長さ1
        l2 (float): 属性 埋め込み長さ2
        type_flame (str): 属性 アンカーフレーム形状
        stb_sec_base_conventional_anchor_bolt (list[StbSecBaseConventionalAnchorBolt]): 子要素 StbSecBaseConventionalAnchorBolt(鉄骨断面柱脚在来工法・アンカーボルト詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "kind_bolt": _FI(
            py_type=StbSecBaseConventionalAnchorBoltsKindBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STD", "ABR", "ABM"),
        ),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "l": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="L",
        ),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "type_bolt": _FI(
            py_type=StbSecBaseConventionalAnchorBoltsTypeBolt,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("I", "J", "L", "LHOOK", "HOLEIN"),
        ),
        "r1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="R1"
        ),
        "r2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="R2"
        ),
        "lt": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="Lt"
        ),
        "s1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="S1"
        ),
        "s2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="S2"
        ),
        "l1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="L1"
        ),
        "l2": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="L2"
        ),
        "type_flame": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_base_conventional_anchor_bolt": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBaseConventionalAnchorBolt],
        ),
    }


class StbSecBaseConventionalPlate(StBridgeElement):
    """鉄骨断面柱脚在来工法・ベースプレート：StbSecBaseConventionalPlate

    Attributes:
        b_x (float): 属性 ベースプレートの寸法(Bx)
        b_y (float): 属性 ベースプレートの寸法(By)
        c1_x (float): 属性 面取りX幅(1)
        c1_y (float): 属性 面取りY幅(1)
        c2_x (float): 属性 面取りX幅(2)
        c2_y (float): 属性 面取りY幅(2)
        c3_x (float): 属性 面取りX幅(3)
        c3_y (float): 属性 面取りY幅(3)
        c4_x (float): 属性 面取りX幅(4)
        c4_y (float): 属性 面取りY幅(4)
        t (float): 属性 ベースプレートの板厚
        strength (str): 属性 ベースプレートの鉄骨強度
        d_bolthole (float): 属性 アンカーボルトの孔径
        offset_x (float): 属性 オフセット(X)
        offset_y (float): 属性 オフセット(Y)
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


class StbSecBaseConventional(StBridgeElement):
    """鉄骨断面柱脚在来工法：StbSecBaseConventional

    Attributes:
        height_mortar (float): 属性 モルタル高さ
        cut_wide (float): 属性 切込み幅
        cut_height (float): 属性 切込み高さ
        stb_sec_base_conventional_plate (StbSecBaseConventionalPlate): 子要素 StbSecBaseConventionalPlate(鉄骨断面柱脚在来工法・ベースプレート)
        stb_sec_base_conventional_anchor_bolts (StbSecBaseConventionalAnchorBolts): 子要素 StbSecBaseConventionalAnchorBolts(鉄骨断面柱脚在来工法・アンカーボルト)
        stb_sec_base_conventional_rib_plates (list[StbSecBaseConventionalRibPlates]): 子要素 StbSecBaseConventionalRibPlates(鉄骨断面柱脚在来工法・リブプレート)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
        "cut_wide": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "cut_height": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "stb_sec_base_conventional_plate": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalPlate,
        ),
        "stb_sec_base_conventional_anchor_bolts": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBaseConventionalAnchorBolts,
        ),
        "stb_sec_base_conventional_rib_plates": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecBaseConventionalRibPlates]
        ),
    }


class StbSecBaseProduct(StBridgeElement):
    """鉄骨断面柱脚製品：StbSecBaseProduct

    Attributes:
        product_code (str): 属性 製品型番
        release_time (str): 属性 リリース時期
        direction_type (StbSecBaseProductDirectionType): 属性 偏心タイプの場合、ベースプレートの向きで、以下のいずれか（度）0、90、180、270
        height_mortar (float): 属性 モルタル高さ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "product_code": _FI(py_type=str, data_type=_DT.STR, required=True),
        "release_time": _FI(py_type=str, data_type=_DT.STR, required=True),
        "direction_type": _FI(
            py_type=StbSecBaseProductDirectionType,
            data_type=_DT.INT_ENUM,
            choices=("0", "90", "180", "270"),
        ),
        "height_mortar": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
            required=True,
        ),
    }


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
        stb_sec_base_product (StbSecBaseProduct): 子要素 StbSecBaseProduct(鉄骨断面柱脚製品)
        stb_sec_base_conventional (StbSecBaseConventional): 子要素 StbSecBaseConventional(鉄骨断面柱脚在来工法)
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
        "stb_sec_base_product": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseProduct
        ),
        "stb_sec_base_conventional": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBaseConventional
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecColumn_S"


class StbSecBarColumnCircleNotSameComplex(StBridgeElement):
    """StbSecBarColumnCircleNotSameComplex

    Attributes:
        pos (StbSecBarColumnCircleNotSameComplexPos): 属性
        stb_sec_bar_column_circle_complex_main (list[StbSecBarColumnCircleComplexMain]): 子要素 StbSecBarColumnCircleComplexMain(コンクリート柱断面配筋・円形・詳細・主筋)
        stb_sec_bar_column_circle_complex_hoop (StbSecBarColumnCircleComplexHoop): 子要素 StbSecBarColumnCircleComplexHoop(コンクリート柱断面配筋・円形・詳細・帯筋)
        stb_sec_bar_column_circle_complex_axial (list[StbSecBarColumnCircleComplexAxial]): 子要素 StbSecBarColumnCircleComplexAxial(コンクリート柱断面配筋・円形・詳細・軸筋)
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnCircleNotSameComplexPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "stb_sec_bar_column_circle_complex_main": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type="list[StbSecBarColumnCircleComplexMain]",
        ),
        "stb_sec_bar_column_circle_complex_hoop": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type="StbSecBarColumnCircleComplexHoop",
        ),
        "stb_sec_bar_column_circle_complex_axial": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnCircleComplexAxial]"
        ),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnAdditional]"
        ),
    }


class StbSecBarColumnCircleNotSameSimple(StBridgeElement):
    """コンクリート柱円形断面配筋・簡易：StbSecBarColumnCircleNotSameSimple

    Attributes:
        pos (StbSecBarColumnCircleNotSameSimplePos): 属性 配筋位置 以下のいずれかBOTTOM：柱脚TOP：柱頭
        depth_cover (float): 属性 かぶり厚さ
        center (float): 属性 主筋重心位置
        d_main (str): 属性 主筋：径
        d_hoop (str): 属性 帯筋：径
        d_axial (str): 属性 軸筋：径
        strength_main (str): 属性 主筋：鉄筋強度
        strength_hoop (str): 属性 帯筋：鉄筋強度
        strength_axial (str): 属性 軸筋：鉄筋強度
        n_main (int): 属性 主筋：本数
        n_hoop_x (int): 属性 帯筋：X方向本数
        n_hoop_y (int): 属性 帯筋：Y方向本数
        n_axial (int): 属性 軸筋：本数
        pitch_hoop (float): 属性 帯筋：ピッチ
        hoop_type (StbSecBarColumnCircleNotSameSimpleHoopType): 属性 帯筋種別NORMAL：普通配筋WELD：溶接閉鎖SPIRAL：スパイラル筋
        bar_start_angle (float): 属性 鉄筋配置する際の開始角度
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnCircleNotSameSimplePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BOTTOM", "TOP"),
        ),
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_hoop": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_hoop"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_hoop": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_hoop_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_X",
        ),
        "n_hoop_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_Y",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "pitch_hoop": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "hoop_type": _FI(
            py_type=StbSecBarColumnCircleNotSameSimpleHoopType,
            data_type=_DT.STR_ENUM,
            choices=("NORMAL", "WELD", "SPIRAL"),
        ),
        "bar_start_angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnAdditional]"
        ),
    }


class StbSecBarColumnCircleNotSame(StBridgeElement):
    """StbSecBarColumnCircleNotSame

    Attributes:
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        stb_sec_bar_column_circle_not_same_simple (list[StbSecBarColumnCircleNotSameSimple]): 子要素 StbSecBarColumnCircleNotSameSimple(コンクリート柱円形断面配筋・簡易)
        stb_sec_bar_column_circle_not_same_complex (list[StbSecBarColumnCircleNotSameComplex]): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_column_circle_not_same_simple": _FI(
            kind=_FK.ELEMENT,
            max_occurs=2,
            py_type=list[StbSecBarColumnCircleNotSameSimple],
        ),
        "stb_sec_bar_column_circle_not_same_complex": _FI(
            kind=_FK.ELEMENT,
            max_occurs=2,
            py_type=list[StbSecBarColumnCircleNotSameComplex],
        ),
    }


class StbSecBarColumnCircleComplexAxialLoc(StBridgeElement):
    """コンクリート柱断面配筋・円形・詳細・軸筋位置：StbSecBarColumnCircleComplexAxialLoc

    Attributes:
        x (float): 属性
        y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
    }


class StbSecBarColumnCircleComplexAxial(StBridgeElement):
    """コンクリート柱断面配筋・円形・詳細・軸筋：StbSecBarColumnCircleComplexAxial

    Attributes:
        d (str): 属性
        strength (str): 属性
        stb_sec_bar_column_circle_complex_axial_loc (list[StbSecBarColumnCircleComplexAxialLoc]): 子要素 StbSecBarColumnCircleComplexAxialLoc(コンクリート柱断面配筋・円形・詳細・軸筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_column_circle_complex_axial_loc": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnCircleComplexAxialLoc],
        ),
    }


class StbSecBarColumnCircleComplexHoopLoc(StBridgeElement):
    """コンクリート柱断面配筋・円形・詳細・帯筋中子位置：StbSecBarColumnCircleComplexHoopLoc

    Attributes:
        angle (float): 属性 鉄筋配置角度
        distance (float): 属性 コンクリート面から芯までの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarColumnCircleComplexHoop(StBridgeElement):
    """コンクリート柱断面配筋・円形・詳細・帯筋：StbSecBarColumnCircleComplexHoop

    Attributes:
        d (str): 属性 鉄筋径
        strength (str): 属性 鉄筋強度
        pitch (float): 属性 ピッチ
        hoop_type (StbSecBarColumnCircleComplexHoopHoopType): 属性 帯筋種別NORMAL：普通配筋WELD：溶接閉鎖SPIRAL：スパイラル筋
        distance (float): 属性 コンクリート面から芯までの距離
        stb_sec_bar_column_circle_complex_hoop_loc (list[StbSecBarColumnCircleComplexHoopLoc]): 子要素 StbSecBarColumnCircleComplexHoopLoc(コンクリート柱断面配筋・円形・詳細・帯筋中子位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "hoop_type": _FI(
            py_type=StbSecBarColumnCircleComplexHoopHoopType,
            data_type=_DT.STR_ENUM,
            choices=("NORMAL", "WELD", "SPIRAL"),
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "stb_sec_bar_column_circle_complex_hoop_loc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecBarColumnCircleComplexHoopLoc]
        ),
    }


class StbSecBarColumnCircleComplexMainLoc(StBridgeElement):
    """コンクリート柱断面配筋・円形・詳細・主筋位置：StbSecBarColumnCircleComplexMainLoc

    Attributes:
        angle (float): 属性 鉄筋配置角度
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "angle": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
    }


class StbSecBarColumnCircleComplexMain(StBridgeElement):
    """コンクリート柱断面配筋・円形・詳細・主筋：StbSecBarColumnCircleComplexMain

    Attributes:
        d (str): 属性 鉄筋径
        strength (str): 属性 鉄筋強度
        step (int): 属性 段数
        distance (float): 属性 コンクリート面から鉄筋列までの距離
        stb_sec_bar_column_circle_complex_main_loc (list[StbSecBarColumnCircleComplexMainLoc]): 子要素 StbSecBarColumnCircleComplexMainLoc(コンクリート柱断面配筋・円形・詳細・主筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "step": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "stb_sec_bar_column_circle_complex_main_loc": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnCircleComplexMainLoc],
        ),
    }


class StbSecBarColumnCircleSameComplex(StBridgeElement):
    """コンクリート柱断面配筋・円形・同一・詳細：StbSecBarColumnCircleSameComplex

    Attributes:
        stb_sec_bar_column_circle_complex_main (list[StbSecBarColumnCircleComplexMain]): 子要素 StbSecBarColumnCircleComplexMain(コンクリート柱断面配筋・円形・詳細・主筋)
        stb_sec_bar_column_circle_complex_hoop (StbSecBarColumnCircleComplexHoop): 子要素 StbSecBarColumnCircleComplexHoop(コンクリート柱断面配筋・円形・詳細・帯筋)
        stb_sec_bar_column_circle_complex_axial (StbSecBarColumnCircleComplexAxial): 子要素 StbSecBarColumnCircleComplexAxial(コンクリート柱断面配筋・円形・詳細・軸筋)
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_bar_column_circle_complex_main": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnCircleComplexMain],
        ),
        "stb_sec_bar_column_circle_complex_hoop": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBarColumnCircleComplexHoop,
        ),
        "stb_sec_bar_column_circle_complex_axial": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnCircleComplexAxial
        ),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnAdditional]"
        ),
    }


class StbSecBarColumnCircleSameSimple(StBridgeElement):
    """コンクリート柱断面配筋・円形・同一・簡易：StbSecBarColumnCircleSameSimple

    Attributes:
        depth_cover (float): 属性 かぶり厚さ
        center (float): 属性 主筋重心位置
        d_main (str): 属性 主筋：径
        d_hoop (str): 属性 帯筋：径
        d_axial (str): 属性 軸筋：径
        strength_main (str): 属性 主筋：鉄筋強度
        strength_hoop (str): 属性 帯筋：鉄筋強度
        strength_axial (str): 属性 軸筋：鉄筋強度
        n_main (int): 属性 主筋：本数
        n_hoop_x (int): 属性 帯筋：X方向本数
        n_hoop_y (int): 属性 帯筋：Y方向本数
        n_axial (int): 属性 軸筋：本数
        pitch_hoop (float): 属性 帯筋：ピッチ
        hoop_type (StbSecBarColumnCircleSameSimpleHoopType): 属性 帯筋種別NORMAL：普通配筋WELD：溶接閉鎖SPIRAL：スパイラル筋
        bar_start_angle (float): 属性 鉄筋配置する際の開始角度
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "center": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_hoop": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_hoop"),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_hoop": _FI(py_type=str, data_type=_DT.STR),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "n_main": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_main",
        ),
        "n_hoop_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_X",
        ),
        "n_hoop_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_Y",
        ),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "pitch_hoop": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "hoop_type": _FI(
            py_type=StbSecBarColumnCircleSameSimpleHoopType,
            data_type=_DT.STR_ENUM,
            choices=("NORMAL", "WELD", "SPIRAL"),
        ),
        "bar_start_angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnAdditional]"
        ),
    }


class StbSecBarColumnCircleSame(StBridgeElement):
    """コンクリート柱断面配筋・円形・同一：StbSecBarColumnCircleSame

    Attributes:
        d_bar_spacing (str): 属性 巾止筋：径
        strength_bar_spacing (str): 属性 巾止筋：鉄筋強度
        pitch_bar_spacing (float): 属性 巾止筋：ピッチ
        stb_sec_bar_column_circle_same_simple (StbSecBarColumnCircleSameSimple): 子要素 StbSecBarColumnCircleSameSimple(コンクリート柱断面配筋・円形・同一・簡易)
        stb_sec_bar_column_circle_same_complex (StbSecBarColumnCircleSameComplex): 子要素 StbSecBarColumnCircleSameComplex(コンクリート柱断面配筋・円形・同一・詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_column_circle_same_simple": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnCircleSameSimple
        ),
        "stb_sec_bar_column_circle_same_complex": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnCircleSameComplex
        ),
    }


class StbSecBarColumnRectNotSameComplex(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細：StbSecBarColumnRectNotSameComplex

    Attributes:
        pos (StbSecBarColumnRectNotSameComplexPos): 属性 配筋位置 以下のいずれかBOTTOM：柱脚TOP：柱頭
        n_main_bar (int): 属性 主筋総本数
        stb_sec_bar_column_rect_complex_main (list[StbSecBarColumnRectComplexMain]): 子要素 StbSecBarColumnRectComplexMain(コンクリート柱断面配筋・矩形・詳細・主筋)
        stb_sec_bar_column_rect_complex_hoop (StbSecBarColumnRectComplexHoop): 子要素 StbSecBarColumnRectComplexHoop(コンクリート柱断面配筋・矩形・詳細・帯筋)
        stb_sec_bar_column_rect_complex_axial (StbSecBarColumnRectComplexAxial): 子要素 StbSecBarColumnRectComplexAxial(コンクリート柱断面配筋・矩形・詳細・軸筋)
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnRectNotSameComplexPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("TOP", "BOTTOM"),
        ),
        "n_main_bar": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_mainBar",
        ),
        "stb_sec_bar_column_rect_complex_main": _FI(
            kind=_FK.ELEMENT,
            max_occurs=4,
            min_occurs=4,
            py_type="list[StbSecBarColumnRectComplexMain]",
        ),
        "stb_sec_bar_column_rect_complex_hoop": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type="StbSecBarColumnRectComplexHoop",
        ),
        "stb_sec_bar_column_rect_complex_axial": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbSecBarColumnRectComplexAxial"
        ),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnAdditional]"
        ),
    }


class StbSecBarColumnRectNotSameSimple(StBridgeElement):
    """コンクリート柱断面配筋・矩形・柱頭脚別・簡易：StbSecBarColumnRectNotSameSimple

    Attributes:
        pos (StbSecBarColumnRectNotSameSimplePos): 属性 柱頭か柱脚か 以下のいずれかTOP：柱頭BOTTOM：柱脚
        main_direction (StbSecBarColumnRectNotSameSimpleMainDirection): 属性 主方向 以下のいずれかXY
        depth_cover_start_x (float): 属性 かぶり厚さ（X始）
        depth_cover_end_x (float): 属性 かぶり厚さ（X終）
        depth_cover_start_y (float): 属性 かぶり厚さ（Y始）
        depth_cover_end_y (float): 属性 かぶり厚さ（Y終）
        interval (float): 属性 ２段筋のあき
        center_start_x (float): 属性 主筋重心位置（X始）
        center_start_y (float): 属性 主筋重心位置（X終）
        center_end_x (float): 属性 主筋重心位置（Y始）
        center_end_y (float): 属性 主筋重心位置（Y終）
        center_interval (float): 属性 ２段筋重心間距離
        d_main (str): 属性 主方向鉄筋径
        d_sub (str): 属性 副方向鉄筋径
        strength_main (str): 属性 主方向鉄筋強度
        strength_sub (str): 属性 副方向鉄筋強度
        n_x (int): 属性 X方向片側一段本数
        n_start_x (int): 属性 X始端側に寄せて配置する本数
        n_end_x (int): 属性 X終端側に寄せて配置する本数
        n_y (int): 属性 Y方向片側一段本数
        n_start_y (int): 属性 Y始端側に寄せて配置する本数
        n_end_y (int): 属性 Y終端側に寄せて配置する本数
        hoop_type (StbSecBarColumnRectNotSameSimpleHoopType): 属性 帯筋種別NORMAL：普通配筋WELD：溶接閉鎖SPIRAL：スパイラル筋
        d_hoop (str): 属性 帯筋径
        strength_hoop (str): 属性 帯筋強度
        n_hoop_x (int): 属性 X方向帯筋本数
        n_hoop_y (int): 属性 Y方向帯筋本数
        pitch_hoop (float): 属性 帯筋ピッチ
        d_axial (str): 属性 軸筋径
        strength_axial (str): 属性 軸筋強度
        n_axial (int): 属性 軸筋本数
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnRectNotSameSimplePos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("TOP", "BOTTOM"),
        ),
        "main_direction": _FI(
            py_type=StbSecBarColumnRectNotSameSimpleMainDirection,
            data_type=_DT.STR_ENUM,
            choices=("X", "Y"),
        ),
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
        "center_start_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_X",
        ),
        "center_start_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_Y",
        ),
        "center_end_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_X",
        ),
        "center_end_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_Y",
        ),
        "center_interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_sub": _FI(py_type=str, data_type=_DT.STR, xml_name="D_sub"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_sub": _FI(py_type=str, data_type=_DT.STR),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_start_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_start_X",
        ),
        "n_end_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_end_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
        "n_start_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_start_Y",
        ),
        "n_end_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_end_Y",
        ),
        "hoop_type": _FI(
            py_type=StbSecBarColumnRectNotSameSimpleHoopType,
            data_type=_DT.STR_ENUM,
            choices=("NORMAL", "WELD", "SPIRAL"),
        ),
        "d_hoop": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_hoop"),
        "strength_hoop": _FI(py_type=str, data_type=_DT.STR),
        "n_hoop_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_X",
        ),
        "n_hoop_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_Y",
        ),
        "pitch_hoop": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnAdditional]"
        ),
    }


class StbSecBarColumnRectNotSame(StBridgeElement):
    """コンクリート柱断面配筋・矩形・柱頭脚別：StbSecBarColumnRectNotSame

    Attributes:
        d_bar_spacing (str): 属性 巾止筋：径
        strength_bar_spacing (str): 属性 巾止筋：鉄筋強度
        pitch_bar_spacing (float): 属性 巾止筋：ピッチ
        stb_sec_bar_column_rect_not_same_simple (list[StbSecBarColumnRectNotSameSimple]): 子要素 StbSecBarColumnRectNotSameSimple(コンクリート柱断面配筋・矩形・柱頭脚別・簡易)
        stb_sec_bar_column_rect_not_same_complex (list[StbSecBarColumnRectNotSameComplex]): 子要素 StbSecBarColumnRectNotSameComplex(コンクリート柱断面配筋・矩形・詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_column_rect_not_same_simple": _FI(
            kind=_FK.ELEMENT,
            max_occurs=2,
            py_type=list[StbSecBarColumnRectNotSameSimple],
        ),
        "stb_sec_bar_column_rect_not_same_complex": _FI(
            kind=_FK.ELEMENT,
            max_occurs=2,
            py_type=list[StbSecBarColumnRectNotSameComplex],
        ),
    }


class StbSecBarColumnXReinforced(StBridgeElement):
    """コンクリート矩形柱 Ｘ形配筋：StbSecBarColumnXReinforced

    Attributes:
        d_main (str): 属性 主筋径
        n_main_x (int): 属性 主筋：X方向本数
        n_main_y (int): 属性 主筋：Y方向本数
        n_main_total (int): 属性 主筋：X形配筋の総本数
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_main": _FI(py_type=str, data_type=_DT.STR, xml_name="D_main"),
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


class StbSecBarColumnRectComplexAxialLoc(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・軸筋位置：StbSecBarColumnRectComplexAxialLoc

    Attributes:
        x (float): 属性
        y (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
    }


class StbSecBarColumnRectComplexAxial(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・軸筋：StbSecBarColumnRectComplexAxial

    Attributes:
        d (str): 属性
        strength (str): 属性
        stb_sec_bar_column_rect_complex_axial_loc (list[StbSecBarColumnRectComplexAxialLoc]): 子要素 StbSecBarColumnRectComplexAxialLoc(コンクリート柱断面配筋・矩形・詳細・軸筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "stb_sec_bar_column_rect_complex_axial_loc": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnRectComplexAxialLoc],
        ),
    }


class StbSecBarColumnRectComplexHoopLocY(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・Y方向帯筋位置：StbSecBarColumnRectComplexHoopLocY

    Attributes:
        distance (float): 属性 コンクリート端から鉄筋芯までの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarColumnRectComplexHoopLocX(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・X方向帯筋位置：StbSecBarColumnRectComplexHoopLocX

    Attributes:
        distance (float): 属性 コンクリート端から鉄筋芯までの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarColumnRectComplexHoop(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・帯筋：StbSecBarColumnRectComplexHoop

    Attributes:
        d (str): 属性 鉄筋径
        strength (str): 属性 鉄筋強度
        pitch (float): 属性 ピッチ
        hoop_type (StbSecBarColumnRectComplexHoopHoopType): 属性 帯筋種別NORMAL：普通配筋WELD：溶接閉鎖SPIRAL：スパイラル筋
        stb_sec_bar_column_rect_complex_hoop_loc_x (list[StbSecBarColumnRectComplexHoopLocX]): 子要素 StbSecBarColumnRectComplexHoopLocX(コンクリート柱断面配筋・矩形・詳細・X方向帯筋位置)
        stb_sec_bar_column_rect_complex_hoop_loc_y (list[StbSecBarColumnRectComplexHoopLocY]): 子要素 StbSecBarColumnRectComplexHoopLocY(コンクリート柱断面配筋・矩形・詳細・Y方向帯筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "pitch": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "hoop_type": _FI(
            py_type=StbSecBarColumnRectComplexHoopHoopType,
            data_type=_DT.STR_ENUM,
            choices=("NORMAL", "WELD", "SPIRAL"),
        ),
        "stb_sec_bar_column_rect_complex_hoop_loc_x": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnRectComplexHoopLocX],
        ),
        "stb_sec_bar_column_rect_complex_hoop_loc_y": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnRectComplexHoopLocY],
        ),
    }


class StbSecBarColumnRectComplexMainLoc(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・主筋位置：StbSecBarColumnRectComplexMainLoc

    Attributes:
        distance (float): 属性 コンクリート端から鉄筋芯までの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbSecBarColumnRectComplexMainLine(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・主筋列：StbSecBarColumnRectComplexMainLine

    Attributes:
        step (int): 属性 段数
        d (str): 属性 鉄筋径
        strength (str): 属性 鉄筋強度
        distance (float): 属性 コンクリート端から鉄筋列までの距離
        stb_sec_bar_column_rect_complex_main_loc (list[StbSecBarColumnRectComplexMainLoc]): 子要素 StbSecBarColumnRectComplexMainLoc(コンクリート柱断面配筋・矩形・詳細・主筋位置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "step": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "stb_sec_bar_column_rect_complex_main_loc": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnRectComplexMainLoc],
        ),
    }


class StbSecBarColumnRectComplexMain(StBridgeElement):
    """コンクリート柱断面配筋・矩形・詳細・主筋：StbSecBarColumnRectComplexMain

    Attributes:
        pos (StbSecBarColumnRectComplexMainPos): 属性 配筋位置 以下のいずれかSTARTX：X始ENDX：X終STARTY：Y始ENDY：Y終
        stb_sec_bar_column_rect_complex_main_line (list[StbSecBarColumnRectComplexMainLine]): 子要素 StbSecBarColumnRectComplexMainLine(コンクリート柱断面配筋・矩形・詳細・主筋列)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pos": _FI(
            py_type=StbSecBarColumnRectComplexMainPos,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("STARTX", "ENDX", "STARTY", "ENDY"),
        ),
        "stb_sec_bar_column_rect_complex_main_line": _FI(
            kind=_FK.ELEMENT,
            min_occurs=1,
            py_type=list[StbSecBarColumnRectComplexMainLine],
        ),
    }


class StbSecBarColumnRectSameComplex(StBridgeElement):
    """コンクリート柱断面配筋・矩形・同一・詳細：StbSecBarColumnRectSameComplex

    Attributes:
        n_main_bar (int): 属性 主筋総本数
        stb_sec_bar_column_rect_complex_main (list[StbSecBarColumnRectComplexMain]): 子要素 StbSecBarColumnRectComplexMain(コンクリート柱断面配筋・矩形・詳細・主筋)
        stb_sec_bar_column_rect_complex_hoop (StbSecBarColumnRectComplexHoop): 子要素 StbSecBarColumnRectComplexHoop(コンクリート柱断面配筋・矩形・詳細・帯筋)
        stb_sec_bar_column_rect_complex_axial (StbSecBarColumnRectComplexAxial): 子要素 StbSecBarColumnRectComplexAxial(コンクリート柱断面配筋・矩形・詳細・軸筋)
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "n_main_bar": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_mainBar",
        ),
        "stb_sec_bar_column_rect_complex_main": _FI(
            kind=_FK.ELEMENT,
            max_occurs=4,
            min_occurs=4,
            py_type=list[StbSecBarColumnRectComplexMain],
        ),
        "stb_sec_bar_column_rect_complex_hoop": _FI(
            kind=_FK.ELEMENT,
            max_occurs=1,
            min_occurs=1,
            py_type=StbSecBarColumnRectComplexHoop,
        ),
        "stb_sec_bar_column_rect_complex_axial": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnRectComplexAxial
        ),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type="list[StbSecBarColumnAdditional]"
        ),
    }


class StbSecBarColumnAdditional(StBridgeElement):
    """コンクリート柱断面配筋・追加鉄筋：StbSecBarColumnAdditional

    Attributes:
        d (str): 属性 径
        strength (str): 属性 強度
        x (float): 属性 X位置
        y (float): 属性 Y位置
        is_structural (bool): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D"),
        "strength": _FI(py_type=str, data_type=_DT.STR),
        "x": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="X"),
        "y": _FI(py_type=float, data_type=_DT.FLOAT, required=True, xml_name="Y"),
        "is_structural": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isStructural"),
    }


class StbSecBarColumnRectSameSimple(StBridgeElement):
    """コンクリート柱断面配筋・矩形・同一・簡易：StbSecBarColumnRectSameSimple

    Attributes:
        main_direction (StbSecBarColumnRectSameSimpleMainDirection): 属性 主方向X、Yのいずれか
        depth_cover_start_x (float): 属性 かぶり厚さ（X始）
        depth_cover_end_x (float): 属性 かぶり厚さ（X終）
        depth_cover_start_y (float): 属性 かぶり厚さ（Y始）
        depth_cover_end_y (float): 属性 かぶり厚さ（Y終）
        interval (float): 属性 ２段筋のあき
        center_start_x (float): 属性 主筋重心位置（X始）
        center_start_y (float): 属性 主筋重心位置（X終）
        center_end_x (float): 属性 主筋重心位置（Y始）
        center_end_y (float): 属性 主筋重心位置（Y終）
        center_interval (float): 属性 ２段筋重心間距離
        d_main (str): 属性 主鉄筋径
        d_sub (str): 属性 副主鉄筋径
        strength_main (str): 属性 主鉄筋強度
        strength_sub (str): 属性 副主鉄筋強度
        n_x (int): 属性 X方向片側一段本数
        n_start_x (int): 属性 X始端側に寄せて配置する本数
        n_end_x (int): 属性 X終端側に寄せて配置する本数
        n_y (int): 属性 Y方向片側一段本数
        n_start_y (int): 属性 Y始端側に寄せて配置する本数
        n_end_y (int): 属性 Y終端側に寄せて配置する本数
        hoop_type (StbSecBarColumnRectSameSimpleHoopType): 属性 帯筋種別NORMAL：普通配筋WELD：溶接閉鎖SPIRAL：スパイラル筋
        d_hoop (str): 属性 帯筋径
        strength_hoop (str): 属性 帯筋強度
        n_hoop_x (int): 属性 X方向帯筋本数
        n_hoop_y (int): 属性 Y方向帯筋本数
        pitch_hoop (float): 属性 帯筋ピッチ
        d_axial (str): 属性 軸筋径
        strength_axial (str): 属性 軸筋強度
        n_axial (int): 属性 軸筋本数
        stb_sec_bar_column_additional (list[StbSecBarColumnAdditional]): 子要素 StbSecBarColumnAdditional(コンクリート柱断面配筋・追加鉄筋)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "main_direction": _FI(
            py_type=StbSecBarColumnRectSameSimpleMainDirection,
            data_type=_DT.STR_ENUM,
            choices=("X", "Y"),
        ),
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
        "center_start_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_X",
        ),
        "center_start_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_start_Y",
        ),
        "center_end_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_X",
        ),
        "center_end_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            xml_name="center_end_Y",
        ),
        "center_interval": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "d_main": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_main"),
        "d_sub": _FI(py_type=str, data_type=_DT.STR, xml_name="D_sub"),
        "strength_main": _FI(py_type=str, data_type=_DT.STR),
        "strength_sub": _FI(py_type=str, data_type=_DT.STR),
        "n_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_X",
        ),
        "n_start_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_start_X",
        ),
        "n_end_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_end_X",
        ),
        "n_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_Y",
        ),
        "n_start_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_start_Y",
        ),
        "n_end_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_end_Y",
        ),
        "hoop_type": _FI(
            py_type=StbSecBarColumnRectSameSimpleHoopType,
            data_type=_DT.STR_ENUM,
            choices=("NORMAL", "WELD", "SPIRAL"),
        ),
        "d_hoop": _FI(py_type=str, data_type=_DT.STR, required=True, xml_name="D_hoop"),
        "strength_hoop": _FI(py_type=str, data_type=_DT.STR),
        "n_hoop_x": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_X",
        ),
        "n_hoop_y": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
            xml_name="N_hoop_Y",
        ),
        "pitch_hoop": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "d_axial": _FI(py_type=str, data_type=_DT.STR, xml_name="D_axial"),
        "strength_axial": _FI(py_type=str, data_type=_DT.STR),
        "n_axial": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            xml_name="N_axial",
        ),
        "stb_sec_bar_column_additional": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecBarColumnAdditional]
        ),
    }


class StbSecBarColumnRectSame(StBridgeElement):
    """コンクリート柱断面配筋・矩形・同一：StbSecBarColumnRectSame

    Attributes:
        d_bar_spacing (str): 属性 巾止筋：径
        strength_bar_spacing (str): 属性 巾止筋：鉄筋強度
        pitch_bar_spacing (float): 属性 巾止筋：ピッチ
        stb_sec_bar_column_rect_same_simple (StbSecBarColumnRectSameSimple): 子要素 StbSecBarColumnRectSameSimple(コンクリート柱断面配筋・矩形・同一・簡易)
        stb_sec_bar_column_rect_same_complex (StbSecBarColumnRectSameComplex): 子要素 StbSecBarColumnRectSameComplex(コンクリート柱断面配筋・矩形・同一・詳細)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_sec_bar_column_rect_same_simple": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnRectSameSimple
        ),
        "stb_sec_bar_column_rect_same_complex": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnRectSameComplex
        ),
    }


class StbSecBarArrangementColumnRc(StBridgeElement):
    """ＲＣ柱断面配筋：StbSecBarArrangementColumn_RC

    Attributes:
        stb_sec_bar_column_rect_same (StbSecBarColumnRectSame): 子要素 StbSecBarColumnRectSame(コンクリート柱断面配筋・矩形・同一)
        stb_sec_bar_column_x_reinforced (StbSecBarColumnXReinforced): 子要素 StbSecBarColumnXReinforced(コンクリート矩形柱 Ｘ形配筋)
        stb_sec_bar_column_rect_not_same (StbSecBarColumnRectNotSame): 子要素 StbSecBarColumnRectNotSame(コンクリート柱断面配筋・矩形・柱頭脚別)
        stb_sec_bar_column_circle_same (StbSecBarColumnCircleSame): 子要素 StbSecBarColumnCircleSame(コンクリート柱断面配筋・円形・同一)
        stb_sec_bar_column_circle_not_same (StbSecBarColumnCircleNotSame): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_bar_column_rect_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnRectSame
        ),
        "stb_sec_bar_column_x_reinforced": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnXReinforced
        ),
        "stb_sec_bar_column_rect_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnRectNotSame
        ),
        "stb_sec_bar_column_circle_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnCircleSame
        ),
        "stb_sec_bar_column_circle_not_same": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecBarColumnCircleNotSame
        ),
    }
    _xml_element_name: ClassVar[str] = "StbSecBarArrangementColumn_RC"


class StbSecColumnCircle(StBridgeElement):
    """コンクリート柱断面形状・円形：StbSecColumnCircle

    Attributes:
        d (float): 属性 直径
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


class StbSecColumnRect(StBridgeElement):
    """コンクリート柱断面形状・矩形：StbSecColumnRect

    Attributes:
        width_x (float): 属性 Ｘ幅
        width_y (float): 属性 Ｙ幅
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


class StbSecFigureColumnRc(StBridgeElement):
    """ＲＣ柱断面形状：StbSecFigureColumn_RC

    Attributes:
        stb_sec_column_rect (StbSecColumnRect): 子要素 StbSecColumnRect(コンクリート柱断面形状・矩形)
        stb_sec_column_circle (StbSecColumnCircle): 子要素 StbSecColumnCircle(コンクリート柱断面形状・円形)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_sec_column_rect": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnRect
        ),
        "stb_sec_column_circle": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecColumnCircle
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
        stb_sec_slab_load (list[StbSecSlabLoad]): 子要素 StbSecSlabLoad(荷重用スラブ断面)
        stb_sec_wall_rc (list[StbSecWallRc]): 子要素 StbSecWall_RC(ＲＣ壁断面)
        stb_sec_wall_load (list[StbSecWallLoad]): 子要素 StbSecWallLoad(荷重用壁断面)
        stb_sec_isolating_device (list[StbSecIsolatingDevice]): 子要素 StbSecIsolatingDevice(免震装置断面)
        stb_sec_damping_device (list[StbSecDampingDevice]): 子要素 StbSecDampingDevice(制振装置断面)
        stb_sec_foundation_rc (list[StbSecFoundationRc]): 子要素 StbSecFoundation_RC(ＲＣ基礎断面)
        stb_sec_pile_rc (list[StbSecPileRc]): 子要素 StbSecPile_RC(ＲＣ杭断面)
        stb_sec_pile_s (list[StbSecPileS]): 子要素 StbSecPile_S(鋼管杭断面)
        stb_sec_pile_precast (list[StbSecPilePrecast]): 子要素 StbSecPilePrecast(既製コンクリート杭断面)
        stb_sec_parapet_rc (list[StbSecParapetRc]): 子要素 StbSecParapet_RC(ＲＣパラペット断面)
        stb_sec_open_rc (list[StbSecOpenRc]): 子要素 StbSecOpen_RC(ＲＣ開口断面)
        stb_sec_penetration_s (list[StbSecPenetrationS]): 子要素 StbSecPenetration_S(S梁貫通孔補強仕様)
        stb_sec_panel_zone (list[StbSecPanelZone]): 子要素 StbSecPanelZone(柱梁接合部断面)
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
        "stb_sec_slab_load": _FI(kind=_FK.ELEMENT, py_type=list[StbSecSlabLoad]),
        "stb_sec_wall_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecWallRc]),
        "stb_sec_wall_load": _FI(kind=_FK.ELEMENT, py_type=list[StbSecWallLoad]),
        "stb_sec_isolating_device": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecIsolatingDevice]
        ),
        "stb_sec_damping_device": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecDampingDevice]
        ),
        "stb_sec_foundation_rc": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecFoundationRc]
        ),
        "stb_sec_pile_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileRc]),
        "stb_sec_pile_s": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPileS]),
        "stb_sec_pile_precast": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPilePrecast]),
        "stb_sec_parapet_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecParapetRc]),
        "stb_sec_open_rc": _FI(kind=_FK.ELEMENT, py_type=list[StbSecOpenRc]),
        "stb_sec_penetration_s": _FI(
            kind=_FK.ELEMENT, py_type=list[StbSecPenetrationS]
        ),
        "stb_sec_panel_zone": _FI(kind=_FK.ELEMENT, py_type=list[StbSecPanelZone]),
        "stb_sec_steel": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbSecSteel),
        "stb_sec_undefined": _FI(kind=_FK.ELEMENT, py_type=list[StbSecUndefined]),
    }


class StbConnectionStiffener(StBridgeElement):
    """StbConnectionStiffener

    Attributes:
        id_stiffener (int): 属性
        offset (float): 属性
        stb_connecting_girder (StbConnectingGirder): 子要素 StbConnectingGirder(接続する大梁)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_stiffener": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "stb_connecting_girder": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbConnectingGirder"
        ),
    }


class StbConnectionDiaphragm(StBridgeElement):
    """ダイアフラム配置情報：StbConnectionDiaphragm

    Attributes:
        id_diaphragm (int): 属性 ID
        offset (float): 属性 節点からのオフセット
        stb_connecting_girder (list[StbConnectingGirder]): 子要素 StbConnectingGirder(接続する大梁)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_diaphragm": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset": _FI(py_type=float, data_type=_DT.FLOAT),
        "stb_connecting_girder": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbConnectingGirder]"
        ),
    }


class StbConnectionRibPlate(StBridgeElement):
    """リブプレート配置情報：StbConnectionRibPlate

    Attributes:
        id_rib_plate (int): 属性 リブプレート詳細ID
        mounting_angle (StbConnectionRibPlateMountingAngle): 属性 リブプレートの取り付け角度以下のいずれかの値をとる。Parallel（取り付き部材に平行）、Right-angled（母材と直行）
        offset (float): 属性 ガセットプレート芯に対するオフセット
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_rib_plate": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "mounting_angle": _FI(
            py_type=StbConnectionRibPlateMountingAngle,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Parallel", "Right-angled"),
        ),
        "offset": _FI(py_type=float, data_type=_DT.FLOAT),
    }


class StbConnectingBrace(StBridgeElement):
    """接続するブレース：StbConnectingBrace

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        pos (StbConnectingBracePos): 属性 接続する端部START、END
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "pos": _FI(
            py_type=StbConnectingBracePos,
            data_type=_DT.STR_ENUM,
            choices=("START", "END"),
        ),
    }


class StbConnectingBeam(StBridgeElement):
    """接続する小梁：StbConnectingBeam

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        pos (StbConnectingBeamPos): 属性 接続する端部START、END
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "pos": _FI(
            py_type=StbConnectingBeamPos,
            data_type=_DT.STR_ENUM,
            choices=("START", "END"),
        ),
    }


class StbConnectingGirder(StBridgeElement):
    """接続する大梁：StbConnectingGirder

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        pos (StbConnectingGirderPos): 属性 接続する端部START、END
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "pos": _FI(
            py_type=StbConnectingGirderPos,
            data_type=_DT.STR_ENUM,
            choices=("START", "END"),
        ),
    }


class StbConnectingPost(StBridgeElement):
    """接続する間柱：StbConnectingPost

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        pos (StbConnectingPostPos): 属性 接続する端部TOP、BOTTOM
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
        "pos": _FI(
            py_type=StbConnectingPostPos,
            data_type=_DT.STR_ENUM,
            choices=("TOP", "BOTTOM"),
        ),
    }


class StbConnectionGussetPlate(StBridgeElement):
    """ガセットプレート配置情報：StbConnectionGussetPlate

    Attributes:
        id_gusset_plate (int): 属性 ガセットプレート詳細ID
        side (StbConnectionGussetPlateSide): 属性 払い込み方向front、back
        stb_connecting_post (StbConnectingPost): 子要素 StbConnectingPost(接続する間柱)
        stb_connecting_girder (StbConnectingGirder): 子要素 StbConnectingGirder(接続する大梁)
        stb_connecting_beam (StbConnectingBeam): 子要素 StbConnectingBeam(接続する小梁)
        stb_connecting_brace (StbConnectingBrace): 子要素 StbConnectingBrace(接続するブレース)
        stb_connection_rib_plate (StbConnectionRibPlate): 子要素 StbConnectionRibPlate(リブプレート配置情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id_gusset_plate": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "side": _FI(
            py_type=StbConnectionGussetPlateSide,
            data_type=_DT.STR_ENUM,
            choices=("front", "back"),
        ),
        "stb_connecting_post": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectingPost
        ),
        "stb_connecting_girder": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectingGirder
        ),
        "stb_connecting_beam": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectingBeam
        ),
        "stb_connecting_brace": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectingBrace
        ),
        "stb_connection_rib_plate": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionRibPlate
        ),
    }


class StbConnectedBrace(StBridgeElement):
    """主材となるブレース：StbConnectedBrace

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
    }


class StbConnectedBeam(StBridgeElement):
    """主材となる小梁：StbConnectedBeam

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
    }


class StbConnectedGirder(StBridgeElement):
    """主材となる大梁：StbConnectedGirder

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
    }


class StbConnectedPost(StBridgeElement):
    """主材となる間柱：StbConnectedPost

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
    }


class StbConnectedColumn(StBridgeElement):
    """主材となる柱：StbConnectedColumn

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "id": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "guid": _FI(py_type=UUID, data_type=_DT.UUID, xml_type="guid"),
    }


class StbConnectionArrangement(StBridgeElement):
    """コネクション配置情報：StbConnectionArrangement

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node (int): 属性 節点ID
        stb_connected_column (StbConnectedColumn): 子要素 StbConnectedColumn(主材となる柱)
        stb_connected_post (StbConnectedPost): 子要素 StbConnectedPost(主材となる間柱)
        stb_connected_girder (StbConnectedGirder): 子要素 StbConnectedGirder(主材となる大梁)
        stb_connected_beam (StbConnectedBeam): 子要素 StbConnectedBeam(主材となる小梁)
        stb_connected_brace (StbConnectedBrace): 子要素 StbConnectedBrace(主材となるブレース)
        stb_connection_gusset_plate (list[StbConnectionGussetPlate]): 子要素 StbConnectionGussetPlate(ガセットプレート配置情報)
        stb_connection_diaphragm (list[StbConnectionDiaphragm]): 子要素 StbConnectionDiaphragm(ダイアフラム配置情報)
        stb_connection_stiffener (list[StbConnectionStiffener]): 子要素
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
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "stb_connected_column": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectedColumn
        ),
        "stb_connected_post": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectedPost
        ),
        "stb_connected_girder": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectedGirder
        ),
        "stb_connected_beam": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectedBeam
        ),
        "stb_connected_brace": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectedBrace
        ),
        "stb_connection_gusset_plate": _FI(
            kind=_FK.ELEMENT, py_type=list[StbConnectionGussetPlate]
        ),
        "stb_connection_diaphragm": _FI(
            kind=_FK.ELEMENT, py_type=list[StbConnectionDiaphragm]
        ),
        "stb_connection_stiffener": _FI(
            kind=_FK.ELEMENT, py_type=list[StbConnectionStiffener]
        ),
    }


class StbConnectionArrangements(StBridgeElement):
    """コネクション配置情報（複数）：StbConnectionArrangements

    Attributes:
        stb_connection_arrangement (list[StbConnectionArrangement]): 子要素 StbConnectionArrangement(コネクション配置情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_connection_arrangement": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbConnectionArrangement]
        ),
    }


class StbPanelZoneArrangement(StBridgeElement):
    """コンクリート柱梁接合部：StbPanelZoneArrangement

    Attributes:
        name (str): 属性 名称
        id_node (int): 属性 節点ID
        offset_x (float): 属性 オフセット(X)
        offset_y (float): 属性 オフセット(Y)
        offset_z (float): 属性 オフセット(Z)
        height (float): 属性 高さ
        rotate (float): 属性 回転角
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "name": _FI(py_type=str, data_type=_DT.STR),
        "id_node": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "offset_x": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_X"),
        "offset_y": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Y"),
        "offset_z": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="offset_Z"),
        "height": _FI(py_type=float, data_type=_DT.FLOAT),
        "rotate": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
    }


class StbPanelZoneArrangements(StBridgeElement):
    """コンクリート柱梁接合部配置情報（複数）：StbPanelZoneArrangements

    Attributes:
        stb_panel_zone_arrangement (list[StbPanelZoneArrangement]): 子要素 StbPanelZoneArrangement(コンクリート柱梁接合部)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_panel_zone_arrangement": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbPanelZoneArrangement]
        ),
    }


class StbJointArrangement(StBridgeElement):
    """継手配置情報：StbJointArrangement

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_section (int): 属性 継手ID
        kind_member (StbJointArrangementKindMember): 属性 部材の種別以下のいずれかCOLUMN(柱)POST(間柱)GIRDER（大梁）BEAM（小梁）BRACE(ブレース)
        id_member (int): 属性 部材ID
        starting_point (StbJointArrangementStartingPoint): 属性 起点の位置以下のいずれかSTART(始端)END(終端)
        distance (float): 属性 距離
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
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_member": _FI(
            py_type=StbJointArrangementKindMember,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("COLUMN", "POST", "GIRDER", "BEAM", "BRACE"),
        ),
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "starting_point": _FI(
            py_type=StbJointArrangementStartingPoint,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("START", "END"),
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbJointArrangements(StBridgeElement):
    """継手配置情報（複数）：StbJointArrangements

    Attributes:
        stb_joint_arrangement (list[StbJointArrangement]): 子要素 StbJointArrangement(継手配置情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_joint_arrangement": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbJointArrangement]
        ),
    }


class StbPenetrationArrangement(StBridgeElement):
    """梁貫通孔配置情報：StbPenetrationArrangement

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_section (int): 属性 梁貫通孔仕様ID
        kind_member (StbPenetrationArrangementKindMember): 属性 部材の種別以下のいずれかGIRDER（大梁）BEAM（小梁）
        id_member (int): 属性 部材ID
        floor_load (float): 属性 床荷重（kN/m2）
        b (float): 属性 床の負担幅
        dl (float): 属性 長期分布荷重（N/mm）
        n (float): 属性 設計用軸力（N）
        lh (float): 属性 梁始端から貫通孔芯までの距離
        e (float): 属性 梁天端から貫通孔芯までの距離
        is_eccentricity (bool): 属性 偏芯判定OK（true）、NG（false）
        is_position (bool): 属性 位置判定OK（true）、NG（false）
        is_pitch (bool): 属性 ピッチ判定OK（true）、NG（false）
        is_axial (bool): 属性 軸力判定OK（true）、NG（false）
        is_other (bool): 属性 その他判定OK（true）、NG（false）
        comment (str): 属性 メーカーコメント
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
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_member": _FI(
            py_type=StbPenetrationArrangementKindMember,
            data_type=_DT.STR_ENUM,
            choices=("GIRDER", "BEAM"),
        ),
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "floor_load": _FI(py_type=float, data_type=_DT.FLOAT),
        "b": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="B"),
        "dl": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="DL"),
        "n": _FI(py_type=float, data_type=_DT.FLOAT, xml_name="N"),
        "lh": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="Lh",
        ),
        "e": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True),
        "is_eccentricity": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isEccentricity"
        ),
        "is_position": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isPosition"
        ),
        "is_pitch": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isPitch"
        ),
        "is_axial": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isAxial"
        ),
        "is_other": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isOther"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }


class StbPenetrationArrangements(StBridgeElement):
    """梁貫通孔配置情報（複数）：StbPenetrationArrangements

    Attributes:
        stb_penetration_arrangement (list[StbPenetrationArrangement]): 子要素 StbPenetrationArrangement(梁貫通孔配置情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_penetration_arrangement": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbPenetrationArrangement]
        ),
    }


class StbOpenArrangement(StBridgeElement):
    """開口配置情報：StbOpenArrangement

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_section (int): 属性 断面ID
        kind_member (StbOpenArrangementKindMember): 属性 部材の種別以下のいずれかWALL（壁）SLAB（スラブ）
        id_member (int): 属性 部材ID
        position_x (float): 属性 開口位置（X）
        position_y (float): 属性 開口位置（Y）
        rotate (float): 属性 回転角度（度）
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
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_member": _FI(
            py_type=StbOpenArrangementKindMember,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("WALL", "SLAB"),
        ),
        "id_member": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "position_x": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="position_X"
        ),
        "position_y": _FI(
            py_type=float, data_type=_DT.FLOAT, required=True, xml_name="position_Y"
        ),
        "rotate": _FI(
            py_type=float, data_type=_DT.ANGLE, xml_type="angle", required=True
        ),
    }


class StbOpenArrangements(StBridgeElement):
    """開口配置情報（複数）：StbOpenArrangements

    Attributes:
        stb_open_arrangement (list[StbOpenArrangement]): 子要素 StbOpenArrangement(開口配置情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_open_arrangement": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbOpenArrangement]
        ),
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
        "name": _FI(py_type=str, data_type=_DT.STR),
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
        "name": _FI(py_type=str, data_type=_DT.STR),
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
        "name": _FI(py_type=str, data_type=_DT.STR),
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
        "name": _FI(py_type=str, data_type=_DT.STR),
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
        "name": _FI(py_type=str, data_type=_DT.STR),
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


class StbFrameDampingDeviceConnection(StBridgeElement):
    """制振装置（フレーム）構成・接合部部材：StbFrameDampingDeviceConnection

    Attributes:
        kind_structure (StbFrameDampingDeviceConnectionKindStructure): 属性 接合部・部材種類以下のいずれかとするBRACE,POST,GIRDER
        id_member (int): 属性 接合部・部材ID
        id_node_start (int): 属性 接合部・始端節点ID
        id_node_end (int): 属性 接合部・終端節点ID
        offset_start_x (float): 属性 接合部・始端側オフセット（）
        offset_start_y (float): 属性 接合部・始端側オフセット（）
        offset_start_z (float): 属性 接合部・始端側オフセット（）
        offset_end_x (float): 属性 接合部・終端側オフセット（）
        offset_end_y (float): 属性 接合部・終端側オフセット（）
        offset_end_z (float): 属性 接合部・終端側オフセット（）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "kind_structure": _FI(
            py_type=StbFrameDampingDeviceConnectionKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BRACE", "POST", "GIRDER"),
        ),
        "id_member": _FI(
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
    }


class StbFrameDampingDeviceMember(StBridgeElement):
    """制振装置（フレーム）構成・制振装置部材：StbFrameDampingDeviceMember

    Attributes:
        id_node_start (int): 属性 構成部材始端節点ID
        id_node_end (int): 属性 構成部材終端節点ID
        offset_start_x (float): 属性 構成部材始端側オフセット（）
        offset_start_y (float): 属性 構成部材始端側オフセット（）
        offset_start_z (float): 属性 構成部材始端側オフセット（）
        offset_end_x (float): 属性 構成部材終端側オフセット（）
        offset_end_y (float): 属性 構成部材終端側オフセット（）
        offset_end_z (float): 属性 構成部材終端側オフセット（）
    """

    _fields: ClassVar[dict[str, _FI]] = {
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
    }


class StbFrameDampingDeviceConfiguration(StBridgeElement):
    """StbFrameDampingDeviceConfiguration

    Attributes:
        stb_frame_damping_device_member (list[StbFrameDampingDeviceMember]): 子要素 StbFrameDampingDeviceMember(制振装置（フレーム）構成・制振装置部材)
        stb_frame_damping_device_connection (list[StbFrameDampingDeviceConnection]): 子要素 StbFrameDampingDeviceConnection(制振装置（フレーム）構成・接合部部材)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_frame_damping_device_member": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbFrameDampingDeviceMember]
        ),
        "stb_frame_damping_device_connection": _FI(
            kind=_FK.ELEMENT, py_type=list[StbFrameDampingDeviceConnection]
        ),
    }


class StbFrameDampingDeviceOffset(StBridgeElement):
    """制振装置（フレーム）オフセット：StbFrameDampingDeviceOffset

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


class StbFrameDampingDeviceOffsetList(StBridgeElement):
    """制振装置（フレーム）オフセットリスト：StbFrameDampingDeviceOffsetList

    Attributes:
        stb_frame_damping_device_offset (list[StbFrameDampingDeviceOffset]): 子要素 StbFrameDampingDeviceOffset(制振装置（フレーム）オフセット)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_frame_damping_device_offset": _FI(
            kind=_FK.ELEMENT,
            max_occurs=4,
            min_occurs=1,
            py_type=list[StbFrameDampingDeviceOffset],
        ),
    }


class StbFrameDampingDevice(StBridgeElement):
    """制振装置（フレーム）：StbFrameDampingDevice

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_section (int): 属性 制振装置断面ID
        type_shape (StbFrameDampingDeviceTypeShape): 属性 部材形状の分類以下のいずれかとする。WALL,BRACES,POSTS,SHEARLINK,HORIZONTALLY_SI_LAYER
        minor_type_shape (StbFrameDampingDeviceMinorTypeShape): 属性 同、小分類
        stb_node_id_order (StbNodeIdOrder): 子要素 StbNodeIdOrder(順序のある節点ID)
        stb_frame_damping_device_offset_list (StbFrameDampingDeviceOffsetList): 子要素 StbFrameDampingDeviceOffsetList(制振装置（フレーム）オフセットリスト)
        stb_frame_damping_device_configuration (StbFrameDampingDeviceConfiguration): 子要素
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
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "type_shape": _FI(
            py_type=StbFrameDampingDeviceTypeShape,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("WALL", "BRACES", "POSTS", "SHEARLINK", "HORIZONTALLY_SI_LAYER"),
        ),
        "minor_type_shape": _FI(
            py_type=StbFrameDampingDeviceMinorTypeShape,
            data_type=_DT.STR_ENUM,
            choices=(
                "NORMAL_V",
                "INVERTED_V",
                "SEPARATED_V",
                "INVERTED_SEPARATED_V",
                "LOWER_BOTH",
                "LOWER_2ND_SIDE",
                "LOWER_1ST_SIDE",
                "UPPER_BOTH",
                "UPPER_3RD_SIDE",
                "UPPER_4TH_SIDE",
                "LOWER_VERTICAL",
                "UPPER_VERTICAL",
            ),
        ),
        "stb_node_id_order": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbNodeIdOrder"
        ),
        "stb_frame_damping_device_offset_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbFrameDampingDeviceOffsetList
        ),
        "stb_frame_damping_device_configuration": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbFrameDampingDeviceConfiguration
        ),
    }


class StbFrameDampingDevices(StBridgeElement):
    """制振装置（フレーム）（複数）：StbFrameDampingDevices

    Attributes:
        stb_frame_damping_device (list[StbFrameDampingDevice]): 子要素 StbFrameDampingDevice(制振装置（フレーム）)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_frame_damping_device": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbFrameDampingDevice]
        ),
    }


class StbDampingDevicePosition(StBridgeElement):
    """制振装置配置位置（複数台数配置時）：StbDampingDevicePosition

    Attributes:
        offset_start_x (float): 属性 始端側オフセット（X）
        offset_start_y (float): 属性 始端側オフセット（Y）
        offset_end_x (float): 属性 終端側オフセット（X）
        offset_end_y (float): 属性 終端側オフセット（Y）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "offset_start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_X"
        ),
        "offset_start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Y"
        ),
        "offset_end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_X"
        ),
        "offset_end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Y"
        ),
    }


class StbDampingDevice(StBridgeElement):
    """制振装置：StbDampingDevice

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node_start (int): 属性 始端節点ID
        id_node_end (int): 属性 終端節点ID
        rotate (float): 属性 回転角
        id_section (int): 属性 制振装置断面ID
        type_shape (StbDampingDeviceTypeShape): 属性 部材形状の分類以下のいずれかとする。BRACE,POST,GIRDER
        offset_start_x (float): 属性 始端側オフセット（）
        offset_start_y (float): 属性 始端側オフセット（）
        offset_start_z (float): 属性 始端側オフセット（）
        offset_end_x (float): 属性 終端側オフセット（）
        offset_end_y (float): 属性 終端側オフセット（）
        offset_end_z (float): 属性 終端側オフセット（）
        number (int): 属性 装置台数
        is_member_arrangement_start (bool): 属性 始端側接合部・部材配置あるか否か
        kind_structure_start (StbDampingDeviceKindStructureStart): 属性 始端側接合部・構造種別以下のいずれかとする。RC,S,SRC,CFT,UNDEFINED
        id_section_start (int): 属性 始端側接合部・断面ID
        connection_length_start (float): 属性 始端側接合部・接合長さ
        is_member_arrangement_end (bool): 属性 終端側接合部・部材配置あるか否か
        kind_structure_end (StbDampingDeviceKindStructureEnd): 属性 終端側接合部・構造種別以下のいずれかとする。RC,S,SRC,CFT,UNDEFINED
        id_section_end (int): 属性 終端側接合部・断面ID
        connection_length_end (float): 属性 終端側接合部・接合長さ
        stb_damping_device_position (list[StbDampingDevicePosition]): 子要素 StbDampingDevicePosition(制振装置配置位置（複数台数配置時）)
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
        "type_shape": _FI(
            py_type=StbDampingDeviceTypeShape,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("BRACE", "POST", "GIRDER"),
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
        "number": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "is_member_arrangement_start": _FI(
            py_type=bool, data_type=_DT.BOOL, xml_name="isMemberArrangement_start"
        ),
        "kind_structure_start": _FI(
            py_type=StbDampingDeviceKindStructureStart,
            data_type=_DT.STR_ENUM,
            choices=("RC", "S", "SRC", "CFT", "UNDEFINED"),
        ),
        "id_section_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "connection_length_start": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "is_member_arrangement_end": _FI(
            py_type=bool, data_type=_DT.BOOL, xml_name="isMemberArrangement_end"
        ),
        "kind_structure_end": _FI(
            py_type=StbDampingDeviceKindStructureEnd,
            data_type=_DT.STR_ENUM,
            choices=("RC", "S", "SRC", "CFT", "UNDEFINED"),
        ),
        "id_section_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "connection_length_end": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_damping_device_position": _FI(
            kind=_FK.ELEMENT, py_type=list[StbDampingDevicePosition]
        ),
    }


class StbDampingDevices(StBridgeElement):
    """制振装置（複数）：StbDampingDevices

    Attributes:
        stb_damping_device (list[StbDampingDevice]): 子要素 StbDampingDevice(制振装置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_damping_device": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbDampingDevice]
        ),
    }


class StbIsolatingDevicePosition(StBridgeElement):
    """免震装置配置位置（複数台数配置時）：StbIsolatingDevicePosition

    Attributes:
        offset_start_x (float): 属性 始端側オフセット（X）
        offset_start_y (float): 属性 始端側オフセット（Y）
        offset_end_x (float): 属性 終端側オフセット（X）
        offset_end_y (float): 属性 終端側オフセット（Y）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "offset_start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_X"
        ),
        "offset_start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_start_Y"
        ),
        "offset_end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_X"
        ),
        "offset_end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="offset_end_Y"
        ),
    }


class StbIsolatingDevice(StBridgeElement):
    """免震装置：StbIsolatingDevice

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 名称
        id_node_start (int): 属性 始端節点ID
        id_node_end (int): 属性 終端節点ID
        rotate (float): 属性 回転角
        id_section (int): 属性 免震装置断面ID
        offset_start_x (float): 属性 始端側オフセット（）
        offset_start_y (float): 属性 始端側オフセット（）
        offset_start_z (float): 属性 始端側オフセット（）
        offset_end_x (float): 属性 終端側オフセット（）
        offset_end_y (float): 属性 終端側オフセット（）
        offset_end_z (float): 属性 終端側オフセット（）
        number (int): 属性 装置台数
        is_member_arrangement_start (bool): 属性 始端側接合部・部材配置あるか否か
        kind_structure_start (StbIsolatingDeviceKindStructureStart): 属性 始端側接合部・構造種別以下のいずれかとする。RC,S,SRC,CFT,UNDEFINED
        id_section_start (int): 属性 始端側接合部・断面ID
        connection_length_start (float): 属性 始端側接合部・接合長さ
        is_member_arrangement_end (bool): 属性 終端側接合部・部材配置あるか否か
        kind_structure_end (StbIsolatingDeviceKindStructureEnd): 属性 終端側接合部・構造種別以下のいずれかとする。RC,S,SRC,CFT,UNDEFINED
        id_section_end (int): 属性 終端側接合部・断面ID
        connection_length_end (float): 属性 終端側接合部・接合長さ
        stb_isolating_device_position (list[StbIsolatingDevicePosition]): 子要素 StbIsolatingDevicePosition(免震装置配置位置（複数台数配置時）)
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
        "number": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "is_member_arrangement_start": _FI(
            py_type=bool, data_type=_DT.BOOL, xml_name="isMemberArrangement_start"
        ),
        "kind_structure_start": _FI(
            py_type=StbIsolatingDeviceKindStructureStart,
            data_type=_DT.STR_ENUM,
            choices=("RC", "S", "SRC", "CFT", "UNDEFINED"),
        ),
        "id_section_start": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "connection_length_start": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "is_member_arrangement_end": _FI(
            py_type=bool, data_type=_DT.BOOL, xml_name="isMemberArrangement_end"
        ),
        "kind_structure_end": _FI(
            py_type=StbIsolatingDeviceKindStructureEnd,
            data_type=_DT.STR_ENUM,
            choices=("RC", "S", "SRC", "CFT", "UNDEFINED"),
        ),
        "id_section_end": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "connection_length_end": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_isolating_device_position": _FI(
            kind=_FK.ELEMENT, py_type=list[StbIsolatingDevicePosition]
        ),
    }


class StbIsolatingDevices(StBridgeElement):
    """免震装置（複数）：StbIsolatingDevices

    Attributes:
        stb_isolating_device (list[StbIsolatingDevice]): 子要素 StbIsolatingDevice(免震装置)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_isolating_device": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type=list[StbIsolatingDevice]
        ),
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
        kind_structure (StbWallKindStructure): 属性 構造種別以下のいずれかの値をとる。RC(RC壁)LOAD(荷重のみ)
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
        type_press (StbWallTypePress): 属性
        stb_node_id_order (StbNodeIdOrder): 子要素 StbNodeIdOrder(順序のある節点ID)
        stb_wall_offset_list (StbWallOffsetList): 子要素 StbWallOffsetList(壁オフセットリスト)
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
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbWallKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "LOAD"),
        ),
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
        "slit_upper": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "slit_bottom": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "slit_right": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "slit_left": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "type_outside": _FI(
            py_type=StbWallTypeOutside,
            data_type=_DT.STR_ENUM,
            choices=("TYPE_PLUS", "TYPE_MINUS"),
        ),
        "type_press": _FI(
            py_type=StbWallTypePress,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "ONESIDE", "BOTH"),
        ),
        "stb_node_id_order": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbNodeIdOrder"
        ),
        "stb_wall_offset_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbWallOffsetList
        ),
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
        angle_deck (float): 属性 デッキ角度
        is_foundation (bool): 属性 基礎か否か
        stb_node_id_order (StbNodeIdOrder): 子要素 StbNodeIdOrder(順序のある節点ID)
        stb_slab_offset_list (StbSlabOffsetList): 子要素 StbSlabOffsetList(スラブオフセットリスト)
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
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "kind_structure": _FI(
            py_type=StbSlabKindStructure,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("RC", "DECK", "PRECAST", "LOAD"),
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
        "angle_deck": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "is_foundation": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isFoundation"
        ),
        "stb_node_id_order": _FI(
            kind=_FK.ELEMENT, max_occurs=1, min_occurs=1, py_type="StbNodeIdOrder"
        ),
        "stb_slab_offset_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbSlabOffsetList
        ),
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
        aim_offset_start_x (float): 属性 始端側狙い点オフセット（）
        aim_offset_start_y (float): 属性 始端側狙い点オフセット（）
        aim_offset_start_z (float): 属性 始端側狙い点オフセット（）
        aim_offset_end_x (float): 属性 終端側狙い点オフセット（）
        aim_offset_end_y (float): 属性 終端側狙い点オフセット（）
        aim_offset_end_z (float): 属性 終端側狙い点オフセット（Z）
        cutback_start (float): 属性 始端側カットバック
        cutback_end (float): 属性 終端側カットバック
        feature_brace (StbBraceFeatureBrace): 属性 ブレース特性引張り：TENSION、引張り圧縮：TENSIONANDCOMPRESSIONのいずれかの値
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
        "aim_offset_start_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="aim_offset_start_X"
        ),
        "aim_offset_start_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="aim_offset_start_Y"
        ),
        "aim_offset_start_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="aim_offset_start_Z"
        ),
        "aim_offset_end_x": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="aim_offset_end_X"
        ),
        "aim_offset_end_y": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="aim_offset_end_Y"
        ),
        "aim_offset_end_z": _FI(
            py_type=float, data_type=_DT.FLOAT, xml_name="aim_offset_end_Z"
        ),
        "cutback_start": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "cutback_end": _FI(
            py_type=float,
            data_type=_DT.NON_NEGATIVE_LENGTH,
            xml_type="nonNegativeLength",
        ),
        "feature_brace": _FI(
            py_type=StbBraceFeatureBrace,
            data_type=_DT.STR_ENUM,
            choices=("TENSION", "TENSIONANDCOMPRESSION"),
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


class StbBeamSteelSwitch(StBridgeElement):
    """S躯体切り替え位置：StbBeamSteelSwitch

    Attributes:
        order (int): 属性
        distance (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbBeamBarSwitch(StBridgeElement):
    """配筋切り替え位置：StbBeamBarSwitch

    Attributes:
        order (int): 属性
        distance (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbBeamConcreteSwitch(StBridgeElement):
    """RC躯体位置：StbBeamConcreteSwitch

    Attributes:
        order (int): 属性
        distance (float): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbBeamViaNode(StBridgeElement):
    """小梁中間節点：StbBeamViaNode

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
        is_on_site (bool): 属性
        composite_beam (StbBeamCompositeBeam): 属性
        steel_cutback_start (float): 属性
        steel_cutback_end (float): 属性
        cover_plate (str): 属性
        stb_beam_via_node (StbBeamViaNode): 子要素 StbBeamViaNode(小梁中間節点)
        stb_beam_concrete_switch (list[StbBeamConcreteSwitch]): 子要素 StbBeamConcreteSwitch(RC躯体位置)
        stb_beam_bar_switch (list[StbBeamBarSwitch]): 子要素 StbBeamBarSwitch(配筋切り替え位置)
        stb_beam_steel_switch (list[StbBeamSteelSwitch]): 子要素 StbBeamSteelSwitch(S躯体切り替え位置)
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
        "is_on_site": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOnSite"),
        "composite_beam": _FI(
            py_type=StbBeamCompositeBeam,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "INCOMPLETE", "COMPLETE"),
        ),
        "steel_cutback_start": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_cutback_end": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "cover_plate": _FI(py_type=str, data_type=_DT.STR),
        "stb_beam_via_node": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeamViaNode
        ),
        "stb_beam_concrete_switch": _FI(
            kind=_FK.ELEMENT, py_type=list[StbBeamConcreteSwitch]
        ),
        "stb_beam_bar_switch": _FI(kind=_FK.ELEMENT, py_type=list[StbBeamBarSwitch]),
        "stb_beam_steel_switch": _FI(
            kind=_FK.ELEMENT, py_type=list[StbBeamSteelSwitch]
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


class StbGirderSteelSwitch(StBridgeElement):
    """S躯体位置：StbGirderSteelSwitch

    Attributes:
        order (int): 属性 要素の順番
        distance (float): 属性 基準点からの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbGirderBarSwitch(StBridgeElement):
    """配筋切り替え位置：StbGirderBarSwitch

    Attributes:
        order (int): 属性 要素の順番
        distance (float): 属性 基準点からの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
    }


class StbGirderConcreteSwitch(StBridgeElement):
    """RC躯体位置：StbGirderConcreteSwitch

    Attributes:
        order (int): 属性 要素の順番
        distance (float): 属性 始端基準点からの距離
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "order": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
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
        is_on_site (bool): 属性 現場打ちかどうか
        composite_beam (StbGirderCompositeBeam): 属性 合成梁以下のいずれかの値をとる。NONE：合成梁として期待しないINCOMPLETE：不完全合成梁COMPLETE：完全合成梁
        steel_cutback_start (float): 属性 鉄骨カットバック（始端）
        steel_cutback_end (float): 属性 鉄骨カットバック（終端）
        cover_plate (str): 属性 カバープレート
        stb_girder_via_node (StbGirderViaNode): 子要素 StbGirderViaNode(大梁中間節点)
        stb_girder_concrete_switch (list[StbGirderConcreteSwitch]): 子要素 StbGirderConcreteSwitch(RC躯体位置)
        stb_girder_bar_switch (list[StbGirderBarSwitch]): 子要素 StbGirderBarSwitch(配筋切り替え位置)
        stb_girder_steel_switch (list[StbGirderSteelSwitch]): 子要素 StbGirderSteelSwitch(S躯体位置)
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
        "is_on_site": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOnSite"),
        "composite_beam": _FI(
            py_type=StbGirderCompositeBeam,
            data_type=_DT.STR_ENUM,
            choices=("NONE", "INCOMPLETE", "COMPLETE"),
        ),
        "steel_cutback_start": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_cutback_end": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "cover_plate": _FI(py_type=str, data_type=_DT.STR),
        "stb_girder_via_node": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbGirderViaNode
        ),
        "stb_girder_concrete_switch": _FI(
            kind=_FK.ELEMENT, py_type=list[StbGirderConcreteSwitch]
        ),
        "stb_girder_bar_switch": _FI(
            kind=_FK.ELEMENT, py_type=list[StbGirderBarSwitch]
        ),
        "stb_girder_steel_switch": _FI(
            kind=_FK.ELEMENT, py_type=list[StbGirderSteelSwitch]
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


class StbPostViaNode(StBridgeElement):
    """間柱中間節点：StbPostViaNode

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
        seam (StbPostSeam): 属性
        bar_switch_height (float): 属性
        steel_cutback_bottom (float): 属性
        steel_cutback_top (float): 属性
        steel_switch_height_bottom (float): 属性
        steel_switch_height_top (float): 属性
        stb_post_via_node (StbPostViaNode): 子要素 StbPostViaNode(間柱中間節点)
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
        "seam": _FI(
            py_type=StbPostSeam,
            data_type=_DT.STR_ENUM,
            choices=("X_P", "X_N", "Y_P", "Y_N", "X", "Y"),
        ),
        "bar_switch_height": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_cutback_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_cutback_top": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_switch_height_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_switch_height_top": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_post_via_node": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbPostViaNode
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
        seam (StbColumnSeam): 属性 シーム方向以下のいずれかの値をとるX始（X_P）、X終（X_N）Y始（Y_P）、X終（Y_N）X、Y
        bar_switch_height (float): 属性 配筋切り替え高さ
        steel_cutback_bottom (float): 属性 鉄骨カットバック（始端側）
        steel_cutback_top (float): 属性 鉄骨カットバック（終端側）
        steel_switch_height_bottom (float): 属性 鉄骨断面切り替え高さ(始端側)
        steel_switch_height_top (float): 属性 鉄骨断面切り替え高さ(終端側)
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
        "name": _FI(py_type=str, data_type=_DT.STR),
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
        "seam": _FI(
            py_type=StbColumnSeam,
            data_type=_DT.STR_ENUM,
            choices=("X_P", "X_N", "Y_P", "Y_N", "X", "Y"),
        ),
        "bar_switch_height": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_cutback_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_cutback_top": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_switch_height_bottom": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "steel_switch_height_top": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
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
        stb_isolating_devices (StbIsolatingDevices): 子要素 StbIsolatingDevices(免震装置（複数）)
        stb_damping_devices (StbDampingDevices): 子要素 StbDampingDevices(制振装置（複数）)
        stb_frame_damping_devices (StbFrameDampingDevices): 子要素 StbFrameDampingDevices(制振装置（フレーム）（複数）)
        stb_footings (StbFootings): 子要素 StbFootings(フーチング（複数）)
        stb_strip_footings (StbStripFootings): 子要素 StbStripFootings(布基礎（複数）)
        stb_piles (StbPiles): 子要素 StbPiles(杭基礎（複数）)
        stb_foundation_columns (StbFoundationColumns): 子要素 StbFoundationColumns(基礎柱（複数）)
        stb_parapets (StbParapets): 子要素 StbParapets(パラペット（複数）)
        stb_open_arrangements (StbOpenArrangements): 子要素 StbOpenArrangements(開口配置情報（複数）)
        stb_penetration_arrangements (StbPenetrationArrangements): 子要素 StbPenetrationArrangements(梁貫通孔配置情報（複数）)
        stb_joint_arrangements (StbJointArrangements): 子要素 StbJointArrangements(継手配置情報（複数）)
        stb_panel_zone_arrangements (StbPanelZoneArrangements): 子要素 StbPanelZoneArrangements(コンクリート柱梁接合部配置情報（複数）)
        stb_connection_arrangements (StbConnectionArrangements): 子要素 StbConnectionArrangements(コネクション配置情報（複数）)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_columns": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbColumns),
        "stb_posts": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbPosts),
        "stb_girders": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbGirders),
        "stb_beams": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbBeams),
        "stb_braces": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbBraces),
        "stb_slabs": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbSlabs),
        "stb_walls": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbWalls),
        "stb_isolating_devices": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbIsolatingDevices
        ),
        "stb_damping_devices": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbDampingDevices
        ),
        "stb_frame_damping_devices": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbFrameDampingDevices
        ),
        "stb_footings": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbFootings),
        "stb_strip_footings": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbStripFootings
        ),
        "stb_piles": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbPiles),
        "stb_foundation_columns": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbFoundationColumns
        ),
        "stb_parapets": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbParapets),
        "stb_open_arrangements": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbOpenArrangements
        ),
        "stb_penetration_arrangements": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbPenetrationArrangements
        ),
        "stb_joint_arrangements": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbJointArrangements
        ),
        "stb_panel_zone_arrangements": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbPanelZoneArrangements
        ),
        "stb_connection_arrangements": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionArrangements
        ),
    }


class StbStory(StBridgeElement):
    """階：StbStory

    Attributes:
        id (int): 属性 ID
        guid (UUID): 属性 GUID
        name (str): 属性 階名称
        level_name (str): 属性 フロアレベル名称
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
        "level_name": _FI(py_type=str, data_type=_DT.STR),
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
        "start_angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "end_angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
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
        "start_angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "end_angle": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
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
            xml_type="monolist_id",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST_ID,
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
        stb_connections (StbConnections): 子要素 StbConnections(コネクション情報)
        stb_weld (StbWeld): 子要素 StbWeld(溶接)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_nodes": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbNodes),
        "stb_axes": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAxes),
        "stb_stories": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbStories),
        "stb_members": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbMembers),
        "stb_sections": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbSections),
        "stb_joints": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbJoints),
        "stb_connections": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnections),
        "stb_weld": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbWeld),
    }


class StbAdditionalInformation(StBridgeElement):
    """追加情報：StbAdditionalInformation

    Attributes:
        pile_allowable_eccentricity_x (float): 属性 杭許容偏心量(X方向)
        pile_allowable_eccentricity_y (float): 属性 杭許容偏心量(Y方向)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "pile_allowable_eccentricity_x": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="pile_allowable_eccentricity_X",
        ),
        "pile_allowable_eccentricity_y": _FI(
            py_type=float,
            data_type=_DT.LENGTH,
            xml_type="length",
            required=True,
            xml_name="pile_allowable_eccentricity_Y",
        ),
    }


class StbWeldCommon(StBridgeElement):
    """溶接情報：StbWeldCommon

    Attributes:
        kind_end_tab (StbWeldCommonKindEndTab): 属性 エンドタブの種類以下のいずれかの値をとる。Steel（鋼製エンドタブ）、Flux（固形エンドタブ）
        strength_backup (str): 属性 裏当て金の材質
        shape_backup (StbWeldCommonShapeBackup): 属性 裏当て金の材種以下の値をとる。PL（プレート）、FB（フラットバー）
        size_backup (str): 属性 裏当て金のサイズ
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "kind_end_tab": _FI(
            py_type=StbWeldCommonKindEndTab,
            data_type=_DT.STR_ENUM,
            choices=("Steel", "Flux"),
        ),
        "strength_backup": _FI(py_type=str, data_type=_DT.STR),
        "shape_backup": _FI(
            py_type=StbWeldCommonShapeBackup,
            data_type=_DT.STR_ENUM,
            choices=("PL", "FB"),
        ),
        "size_backup": _FI(py_type=str, data_type=_DT.STR),
    }


class StbConnectionSpecColumnPipe(StBridgeElement):
    """Ｓ柱仕口・円形鋼管コネクション仕様情報：StbConnectionSpecColumnPipe

    Attributes:
        stb_connection_spec_diaphragm (list[StbConnectionSpecDiaphragm]): 子要素 StbConnectionSpecDiaphragm(ダイアフラム仕様)
        stb_connection_spec_panel (StbConnectionSpecPanel): 子要素 StbConnectionSpecPanel(パネルゾーン仕様)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_connection_spec_diaphragm": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type="list[StbConnectionSpecDiaphragm]"
        ),
        "stb_connection_spec_panel": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbConnectionSpecPanel"
        ),
    }


class StbConnectionSpecPanelStrength(StBridgeElement):
    """パネルゾーン材種：StbConnectionSpecPanelStrength

    Attributes:
        strength (StbConnectionSpecPanelStrengthStrength): 属性 パネルの材種以下のいずれかの値をとる。Same（同一材種）Class_C（同一強度でC種）
        strength_internal (StbConnectionSpecPanelStrengthStrengthInternal): 属性 内ダイアが溶接される場合のパネルの材種以下のいずれかの値をとる。Same（同一材種）Class_C（同一強度でC種）
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength": _FI(
            py_type=StbConnectionSpecPanelStrengthStrength,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Same", "Class_C"),
        ),
        "strength_internal": _FI(
            py_type=StbConnectionSpecPanelStrengthStrengthInternal,
            data_type=_DT.STR_ENUM,
            choices=("Same", "Class_C"),
        ),
    }


class StbConnectionSpecPanel(StBridgeElement):
    """パネルゾーン仕様：StbConnectionSpecPanel

    Attributes:
        is_taper (bool): 属性 絞りの有無
        border_gap (float): 属性 絞りのしきい値
        panel_type (StbConnectionSpecPanelPanelType): 属性 パネルのタイプ以下のいずれかの値をとる。Same（柱と同一）Product（既製品）Plate（プレート）
        dia_size_up_panel (int): 属性 柱の最大板厚に対するサイズアップ
        dia_thickness_up_panel (float): 属性 柱の最大板厚に加算する板厚
        stb_connection_spec_panel_strength (list[StbConnectionSpecPanelStrength]): 子要素 StbConnectionSpecPanelStrength(パネルゾーン材種)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_taper": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isTaper"
        ),
        "border_gap": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "panel_type": _FI(
            py_type=StbConnectionSpecPanelPanelType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Same", "Product", "Plate"),
        ),
        "dia_size_up_panel": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "dia_thickness_up_panel": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "stb_connection_spec_panel_strength": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbConnectionSpecPanelStrength]
        ),
    }


class StbConnectionSpecDiaphragm(StBridgeElement):
    """ダイアフラム仕様：StbConnectionSpecDiaphragm

    Attributes:
        location (StbConnectionSpecDiaphragmLocation): 属性 ダイアフラムの位置以下のいずれかの値をとる。Outer（上下）Inner（中間）
        type (StbConnectionSpecDiaphragmType): 属性 ダイアフラム形式以下のいずれかの値をとる。Through（通しダイア）、Internal（内ダイア）、External（外ダイア）
        is_product (bool): 属性 既製品か否か
        strength_border_thickness (float): 属性 材種の板厚のしきい値
        strength_min (str): 属性 しきい値未満の板厚の場合のダイアフラムの材種
        strength_max (str): 属性 しきい値以上の板厚の場合のダイアフラムの材種
        e_border_dia_thickness (float): 属性 ダイアフラム厚に対するダイアフラム出寸法のしきい値
        dia_size_up_panel (int): 属性 パネル材の最大板厚に対するサイズアップ
        dia_thickness_up_panel (float): 属性 パネル材の最大板厚に加算する板厚
        dia_size_up_flange (int): 属性 梁フランジの最大板厚に対するサイズアップ
        dia_thickness_up_flange (float): 属性 梁フランジの最大板厚に加算する板厚
        e_min_dia_thickness (float): 属性 ダイアフラム厚に対するダイアフラム出寸法の最小値
        e_max_dia_thickness (float): 属性 ダイアフラム厚に対するダイアフラム出寸法の最大値
        e_border_panel_thickness (float): 属性 パネル材の最大板厚に対するダイアフラム出寸法のしきい値
        e_min_panel_thickness (float): 属性 パネル材の最大板厚に対するダイアフラム出寸法の最小値
        e_max_panel_thickness (float): 属性 パネル材の最大板厚に対するダイアフラム出寸法の最大値
        max_flange_gap (float): 属性 梁フランジの目違いの最大値
        min_diaphragm_distance (float): 属性 ダイアフラム間の距離の最小値
        id_weld (int): 属性 溶接ID
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "location": _FI(
            py_type=StbConnectionSpecDiaphragmLocation,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Outer", "Inner"),
        ),
        "type": _FI(
            py_type=StbConnectionSpecDiaphragmType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("Through", "Internal", "External"),
        ),
        "is_product": _FI(
            py_type=bool, data_type=_DT.BOOL, required=True, xml_name="isProduct"
        ),
        "strength_border_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "strength_min": _FI(py_type=str, data_type=_DT.STR),
        "strength_max": _FI(py_type=str, data_type=_DT.STR),
        "e_border_dia_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "dia_size_up_panel": _FI(py_type=int, data_type=_DT.INT),
        "dia_thickness_up_panel": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "dia_size_up_flange": _FI(py_type=int, data_type=_DT.INT),
        "dia_thickness_up_flange": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "e_min_dia_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "e_max_dia_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "e_border_panel_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "e_min_panel_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "e_max_panel_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "max_flange_gap": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "min_diaphragm_distance": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "id_weld": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
    }


class StbConnectionSpecColumnBox(StBridgeElement):
    """Ｓ柱仕口・角形鋼管コネクション仕様情報：StbConnectionSpecColumnBox

    Attributes:
        stb_connection_spec_diaphragm (list[StbConnectionSpecDiaphragm]): 子要素 StbConnectionSpecDiaphragm(ダイアフラム仕様)
        stb_connection_spec_panel (StbConnectionSpecPanel): 子要素 StbConnectionSpecPanel(パネルゾーン仕様)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_connection_spec_diaphragm": _FI(
            kind=_FK.ELEMENT, max_occurs=2, py_type=list[StbConnectionSpecDiaphragm]
        ),
        "stb_connection_spec_panel": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecPanel
        ),
    }


class StbConnectionSpecStiffener(StBridgeElement):
    """StbConnectionSpecStiffener

    Attributes:
        strength_plate (str): 属性
        id_weld (int): 属性
        cutback (int): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "id_weld": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "cutback": _FI(py_type=int, data_type=_DT.INT),
    }


class StbConnectionSpecColumnH(StBridgeElement):
    """Ｓ柱仕口・Ｈ形コネクション仕様情報：StbConnectionSpecColumnH

    Attributes:
        gusset_size_up (int): 属性 ガセットプレートのサイズアップ
        stiffener_size_up_connected (int): 属性
        stiffener_size_up_connecting (int): 属性
        rib_size_up (int): 属性 リブプレートのサイズアップ
        stb_connection_spec_gusset_plate (list[StbConnectionSpecGussetPlate]): 子要素 StbConnectionSpecGussetPlate(ガセットプレート仕様)
        stb_connection_spec_stiffener (list[StbConnectionSpecStiffener]): 子要素
        stb_connection_spec_rib_plate (StbConnectionSpecRibPlate): 子要素 StbConnectionSpecRibPlate(リブプレート仕様)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "gusset_size_up": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stiffener_size_up_connected": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stiffener_size_up_connecting": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "rib_size_up": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_connection_spec_gusset_plate": _FI(
            kind=_FK.ELEMENT, py_type="list[StbConnectionSpecGussetPlate]"
        ),
        "stb_connection_spec_stiffener": _FI(
            kind=_FK.ELEMENT, py_type=list[StbConnectionSpecStiffener]
        ),
        "stb_connection_spec_rib_plate": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type="StbConnectionSpecRibPlate"
        ),
    }


class StbConnectionSpecRibPlate(StBridgeElement):
    """リブプレート仕様：StbConnectionSpecRibPlate

    Attributes:
        strength_plate (str): 属性 リブプレートの材種
        id_weld (int): 属性 溶接ID
        cutback (int): 属性 溶接控え
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate": _FI(py_type=str, data_type=_DT.STR),
        "id_weld": _FI(
            py_type=int,
            data_type=_DT.POSITIVE_INTEGER,
            xml_type="positiveInteger",
            required=True,
        ),
        "cutback": _FI(py_type=int, data_type=_DT.INT),
    }


class StbConnectionSpecSplice(StBridgeElement):
    """スプライスプレート仕様：StbConnectionSpecSplice

    Attributes:
        strength_plate (str): 属性 添え板の材種
        plate_thickness (float): 属性 添え板の厚さ
        strength_filler (str): 属性 フィラープレートの材種
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "plate_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "strength_filler": _FI(py_type=str, data_type=_DT.STR),
    }


class StbConnectionSpecGussetPlate(StBridgeElement):
    """ガセットプレート仕様：StbConnectionSpecGussetPlate

    Attributes:
        connection_type (StbConnectionSpecGussetPlateConnectionType): 属性 仕口タイプgap、web、splice
        flange_type (StbConnectionSpecGussetPlateFlangeType): 属性 フランジ刃落としタイプnone、one_side、both_sides
        strength_plate (str): 属性 ガセットプレートの材種
        strength_bolt (str): 属性 ボルト材種
        name_bolt (str): 属性 ボルト径（呼び名）
        clearance (float): 属性 母材と接続部材の間隔
        flange_cut (float): 属性 フランジ刃落としの長さ
        pitch_depth (float): 属性 部材成方向のボルトピッチ (pC)
        pitch (float): 属性 部材長手方向のボルトピッチ (pL)
        e1 (float): 属性 縁端距離1 (e1)
        e2 (float): 属性 縁端距離2 (e2)
        e3 (float): 属性 縁端距離3 (e3)
        e4 (float): 属性 縁端距離4 (e4)
        h1 (float): 属性 ガセットプレートのあき1 (h1)
        h2 (float): 属性 ガセットプレートのあき2 (h2)
        ey (float): 属性 嵩上げ点の幅方向の距離
        ez (float): 属性 嵩上げ点の高さ方向の距離
        r (float): 属性 入隅半径 (R)
        id_weld (int): 属性 溶接ID
        cutback (int): 属性 溶接控え
        stb_connection_spec_splice (StbConnectionSpecSplice): 子要素 StbConnectionSpecSplice(スプライスプレート仕様)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "connection_type": _FI(
            py_type=StbConnectionSpecGussetPlateConnectionType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("gap", "web", "splice"),
        ),
        "flange_type": _FI(
            py_type=StbConnectionSpecGussetPlateFlangeType,
            data_type=_DT.STR_ENUM,
            required=True,
            choices=("none", "one_side", "both_sides"),
        ),
        "strength_plate": _FI(py_type=str, data_type=_DT.STR, required=True),
        "strength_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "name_bolt": _FI(py_type=str, data_type=_DT.STR, required=True),
        "clearance": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "flange_cut": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch_depth": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "pitch": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e1": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "e2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e3": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "e4": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "h1": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "h2": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "ey": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "ez": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "r": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length", xml_name="R"),
        "id_weld": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "cutback": _FI(py_type=int, data_type=_DT.INT),
        "stb_connection_spec_splice": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecSplice
        ),
    }


class StbConnectionSpecBeamH(StBridgeElement):
    """Ｓ梁仕口・Ｈ形コネクション仕様情報：StbConnectionSpecBeamH

    Attributes:
        gusset_size_up (int): 属性 ガセットプレートのサイズアップ
        rib_size_up (int): 属性 リブプレートのサイズアップ
        stb_connection_spec_gusset_plate (list[StbConnectionSpecGussetPlate]): 子要素 StbConnectionSpecGussetPlate(ガセットプレート仕様)
        stb_connection_spec_rib_plate (StbConnectionSpecRibPlate): 子要素 StbConnectionSpecRibPlate(リブプレート仕様)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "gusset_size_up": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "rib_size_up": _FI(
            py_type=int, data_type=_DT.POSITIVE_INTEGER, xml_type="positiveInteger"
        ),
        "stb_connection_spec_gusset_plate": _FI(
            kind=_FK.ELEMENT, py_type=list[StbConnectionSpecGussetPlate]
        ),
        "stb_connection_spec_rib_plate": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecRibPlate
        ),
    }


class StbConnectionSpecs(StBridgeElement):
    """コネクションスペック情報：StbConnectionSpecs

    Attributes:
        size_up_min_thickness (float): 属性 サイズアップの最小板厚差
        stb_connection_spec_beam_h (StbConnectionSpecBeamH): 子要素 StbConnectionSpecBeamH(Ｓ梁仕口・Ｈ形コネクション仕様情報)
        stb_connection_spec_column_h (StbConnectionSpecColumnH): 子要素 StbConnectionSpecColumnH(Ｓ柱仕口・Ｈ形コネクション仕様情報)
        stb_connection_spec_column_box (StbConnectionSpecColumnBox): 子要素 StbConnectionSpecColumnBox(Ｓ柱仕口・角形鋼管コネクション仕様情報)
        stb_connection_spec_column_pipe (StbConnectionSpecColumnPipe): 子要素 StbConnectionSpecColumnPipe(Ｓ柱仕口・円形鋼管コネクション仕様情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "size_up_min_thickness": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length", required=True
        ),
        "stb_connection_spec_beam_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecBeamH
        ),
        "stb_connection_spec_column_h": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecColumnH
        ),
        "stb_connection_spec_column_box": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecColumnBox
        ),
        "stb_connection_spec_column_pipe": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecColumnPipe
        ),
    }


class StbStandardPlateThicknessList(StBridgeElement):
    """システム標準板厚リスト：StbStandardPlateThicknessList

    Attributes:
        content (list[float]): 内容
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "content": _FI(
            xml_type="monolist_length",
            kind=_FK.CONTENT,
            data_type=_DT.MONOLIST_LENGTH,
            py_type=list[float],
        ),
    }


class StbApplySBeam(StBridgeElement):
    """StbApplySBeam：StbApply_S_Beam

    Attributes:
        stud_rule (str): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stud_rule": _FI(py_type=str, data_type=_DT.STR),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_S_Beam"


class StbApplySGirder(StBridgeElement):
    """StbApplySGirder：StbApply_S_Girder

    Attributes:
        stud_rule (str): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stud_rule": _FI(py_type=str, data_type=_DT.STR),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_S_Girder"


class StbApplySColumn(StBridgeElement):
    """StbApplySColumn：StbApply_S_Column

    Attributes:
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbApply_S_Column"


class StbApplySGeneral(StBridgeElement):
    """StbApplySGeneral：StbApply_S_General

    Attributes:
        planting_rule (str): 属性
        covering_rule (str): 属性
        rustproof_rule (str): 属性
        zone_rule (str): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "planting_rule": _FI(py_type=str, data_type=_DT.STR),
        "covering_rule": _FI(py_type=str, data_type=_DT.STR),
        "rustproof_rule": _FI(py_type=str, data_type=_DT.STR),
        "zone_rule": _FI(py_type=str, data_type=_DT.STR),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_S_General"


class StbApplyConditionListS(StBridgeElement):
    """StbApplyConditionListS：StbApplyConditionList_S

    Attributes:
        stb_apply_s_general (StbApplySGeneral): 子要素
        stb_apply_s_column (StbApplySColumn): 子要素
        stb_apply_s_girder (StbApplySGirder): 子要素
        stb_apply_s_beam (StbApplySBeam): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_apply_s_general": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplySGeneral
        ),
        "stb_apply_s_column": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplySColumn
        ),
        "stb_apply_s_girder": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplySGirder
        ),
        "stb_apply_s_beam": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplySBeam),
    }
    _xml_element_name: ClassVar[str] = "StbApplyConditionList_S"


class StbApplyRcSlab(StBridgeElement):
    """StbApplyRcSlab：StbApply_RC_Slab

    Attributes:
        depth_cover (float): 属性
        beam_reinforcement_rule (str): 属性
        column_reinforcement_rule (str): 属性
        opening_reinforcement_rule (str): 属性
        corner_reinforcement_rule (str): 属性
        step_reinforcement_rule (str): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "beam_reinforcement_rule": _FI(py_type=str, data_type=_DT.STR),
        "column_reinforcement_rule": _FI(py_type=str, data_type=_DT.STR),
        "opening_reinforcement_rule": _FI(py_type=str, data_type=_DT.STR),
        "corner_reinforcement_rule": _FI(py_type=str, data_type=_DT.STR),
        "step_reinforcement_rule": _FI(py_type=str, data_type=_DT.STR),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_Slab"


class StbApplyRcWall(StBridgeElement):
    """StbApplyRcWall：StbApply_RC_Wall

    Attributes:
        depth_cover (float): 属性
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        horizontal_bar_switch_start_ratio (float): 属性
        horizontal_bar_switch_end_ratio (float): 属性
        vertical_bar_switch_bottom_ratio (float): 属性
        vertical_bar_switch_top_ratio (float): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "depth_cover": _FI(py_type=float, data_type=_DT.LENGTH, xml_type="length"),
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "horizontal_bar_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "horizontal_bar_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "vertical_bar_switch_bottom_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "vertical_bar_switch_top_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_Wall"


class StbApplyRcBeam(StBridgeElement):
    """StbApplyRcBeam：StbApply_RC_Beam

    Attributes:
        is_on_site (bool): 属性
        depth_cover_left (float): 属性
        depth_cover_right (float): 属性
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        interval (float): 属性
        center_top (float): 属性
        center_bottom (float): 属性
        center_side (float): 属性
        center_interval (float): 属性
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        allocation_rule_stirrup (str): 属性
        d_additional (str): 属性
        strength_additional (str): 属性
        number_rule_additional (str): 属性
        anchorage_rule (str): 属性
        cut_off_rule (str): 属性
        figure_switch_start_ratio (float): 属性
        figure_switch_end_ratio (float): 属性
        bar_switch_start_ratio (float): 属性
        bar_switch_end_ratio (float): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_on_site": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOnSite"),
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
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "allocation_rule_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "d_additional": _FI(py_type=str, data_type=_DT.STR, xml_name="D_additional"),
        "strength_additional": _FI(py_type=str, data_type=_DT.STR),
        "number_rule_additional": _FI(py_type=str, data_type=_DT.STR),
        "anchorage_rule": _FI(py_type=str, data_type=_DT.STR),
        "cut_off_rule": _FI(py_type=str, data_type=_DT.STR),
        "figure_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "figure_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_Beam"


class StbApplyRcGirder(StBridgeElement):
    """StbApplyRcGirder：StbApply_RC_Girder

    Attributes:
        is_on_site (bool): 属性
        depth_cover_left (float): 属性
        depth_cover_right (float): 属性
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        interval (float): 属性
        center_top (float): 属性
        center_bottom (float): 属性
        center_side (float): 属性
        center_interval (float): 属性
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        allocation_rule_stirrup (str): 属性
        d_additional (str): 属性
        strength_additional (str): 属性
        number_rule_additional (str): 属性
        anchorage_rule (str): 属性
        cut_off_rule (str): 属性
        figure_switch_start_ratio (float): 属性
        figure_switch_end_ratio (float): 属性
        bar_switch_start_ratio (float): 属性
        bar_switch_end_ratio (float): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_on_site": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOnSite"),
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
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "allocation_rule_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "d_additional": _FI(py_type=str, data_type=_DT.STR, xml_name="D_additional"),
        "strength_additional": _FI(py_type=str, data_type=_DT.STR),
        "number_rule_additional": _FI(py_type=str, data_type=_DT.STR),
        "anchorage_rule": _FI(py_type=str, data_type=_DT.STR),
        "cut_off_rule": _FI(py_type=str, data_type=_DT.STR),
        "figure_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "figure_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_Girder"


class StbApplyRcColumn(StBridgeElement):
    """StbApplyRcColumn：StbApply_RC_Column

    Attributes:
        is_on_site (bool): 属性
        depth_cover_start_x (float): 属性
        depth_cover_end_x (float): 属性
        depth_cover_start_y (float): 属性
        depth_cover_end_y (float): 属性
        interval (float): 属性
        center_start_x (float): 属性
        center_end_x (float): 属性
        center_start_y (float): 属性
        center_end_y (float): 属性
        center_interval (float): 属性
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        allocation_rule_hoop (str): 属性
        d_additional (str): 属性
        strength_additional (str): 属性
        number_rule_additional (str): 属性
        anchorage_rule (str): 属性
        bar_switch_ratio (float): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_on_site": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOnSite"),
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
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "allocation_rule_hoop": _FI(py_type=str, data_type=_DT.STR),
        "d_additional": _FI(py_type=str, data_type=_DT.STR, xml_name="D_additional"),
        "strength_additional": _FI(py_type=str, data_type=_DT.STR),
        "number_rule_additional": _FI(py_type=str, data_type=_DT.STR),
        "anchorage_rule": _FI(py_type=str, data_type=_DT.STR),
        "bar_switch_ratio": _FI(py_type=float, data_type=_DT.RATIO, xml_type="ratio"),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_Column"


class StbApplyRcFoundationBeam(StBridgeElement):
    """StbApplyRcFoundationBeam：StbApply_RC_FoundationBeam

    Attributes:
        is_on_site (bool): 属性
        depth_cover_left (float): 属性
        depth_cover_right (float): 属性
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        interval (float): 属性
        center_top (float): 属性
        center_bottom (float): 属性
        center_side (float): 属性
        center_interval (float): 属性
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        allocation_rule_stirrup (str): 属性
        d_additional (str): 属性
        strength_additional (str): 属性
        number_rule_additional (str): 属性
        anchorage_rule (str): 属性
        cut_off_rule (str): 属性
        figure_switch_start_ratio (float): 属性
        figure_switch_end_ratio (float): 属性
        bar_switch_start_ratio (float): 属性
        bar_switch_end_ratio (float): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_on_site": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOnSite"),
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
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "allocation_rule_stirrup": _FI(py_type=str, data_type=_DT.STR),
        "d_additional": _FI(py_type=str, data_type=_DT.STR, xml_name="D_additional"),
        "strength_additional": _FI(py_type=str, data_type=_DT.STR),
        "number_rule_additional": _FI(py_type=str, data_type=_DT.STR),
        "anchorage_rule": _FI(py_type=str, data_type=_DT.STR),
        "cut_off_rule": _FI(py_type=str, data_type=_DT.STR),
        "figure_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "figure_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_FoundationBeam"


class StbApplyRcFoundationGirder(StBridgeElement):
    """StbApplyRcFoundationGirder：StbApply_RC_FoundationGirder

    Attributes:
        is_on_site (bool): 属性
        depth_cover_left (float): 属性
        depth_cover_right (float): 属性
        depth_cover_top (float): 属性
        depth_cover_bottom (float): 属性
        interval (float): 属性
        center_top (float): 属性
        center_bottom (float): 属性
        center_side (float): 属性
        center_interval (float): 属性
        d_bar_spacing (str): 属性
        strength_bar_spacing (str): 属性
        pitch_bar_spacing (float): 属性
        allocation_rule_hoop (str): 属性
        d_additional (str): 属性
        strength_additional (str): 属性
        number_rule_additional (str): 属性
        anchorage_rule (str): 属性
        cut_off_rule (str): 属性
        figure_switch_start_ratio (float): 属性
        figure_switch_end_ratio (float): 属性
        bar_switch_start_ratio (float): 属性
        bar_switch_end_ratio (float): 属性
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "is_on_site": _FI(py_type=bool, data_type=_DT.BOOL, xml_name="isOnSite"),
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
        "d_bar_spacing": _FI(py_type=str, data_type=_DT.STR, xml_name="D_bar_spacing"),
        "strength_bar_spacing": _FI(py_type=str, data_type=_DT.STR),
        "pitch_bar_spacing": _FI(
            py_type=float, data_type=_DT.LENGTH, xml_type="length"
        ),
        "allocation_rule_hoop": _FI(py_type=str, data_type=_DT.STR),
        "d_additional": _FI(py_type=str, data_type=_DT.STR, xml_name="D_additional"),
        "strength_additional": _FI(py_type=str, data_type=_DT.STR),
        "number_rule_additional": _FI(py_type=str, data_type=_DT.STR),
        "anchorage_rule": _FI(py_type=str, data_type=_DT.STR),
        "cut_off_rule": _FI(py_type=str, data_type=_DT.STR),
        "figure_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "figure_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_start_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "bar_switch_end_ratio": _FI(
            py_type=float, data_type=_DT.RATIO, xml_type="ratio"
        ),
        "comment": _FI(py_type=str, data_type=_DT.STR),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_FoundationGirder"


class StbApplyRcFoundation(StBridgeElement):
    """StbApplyRcFoundation：StbApply_RC_Foundation

    Attributes:
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_Foundation"


class StbApplyRcPile(StBridgeElement):
    """StbApplyRcPile：StbApply_RC_Pile

    Attributes:
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_Pile"


class StbApplyRcGeneral(StBridgeElement):
    """StbApplyRcGeneral：StbApply_RC_General

    Attributes:
        comment (str): 属性
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "comment": _FI(py_type=str, data_type=_DT.STR, required=True),
    }
    _xml_element_name: ClassVar[str] = "StbApply_RC_General"


class StbApplyConditionListRc(StBridgeElement):
    """StbApplyConditionListRc：StbApplyConditionList_RC

    Attributes:
        stb_apply_rc_general (StbApplyRcGeneral): 子要素
        stb_apply_rc_pile (StbApplyRcPile): 子要素
        stb_apply_rc_foundation (StbApplyRcFoundation): 子要素
        stb_apply_rc_foundation_girder (StbApplyRcFoundationGirder): 子要素
        stb_apply_rc_foundation_beam (StbApplyRcFoundationBeam): 子要素
        stb_apply_rc_column (StbApplyRcColumn): 子要素
        stb_apply_rc_girder (StbApplyRcGirder): 子要素
        stb_apply_rc_beam (StbApplyRcBeam): 子要素
        stb_apply_rc_wall (StbApplyRcWall): 子要素
        stb_apply_rc_slab (StbApplyRcSlab): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_apply_rc_general": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcGeneral
        ),
        "stb_apply_rc_pile": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcPile
        ),
        "stb_apply_rc_foundation": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcFoundation
        ),
        "stb_apply_rc_foundation_girder": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcFoundationGirder
        ),
        "stb_apply_rc_foundation_beam": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcFoundationBeam
        ),
        "stb_apply_rc_column": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcColumn
        ),
        "stb_apply_rc_girder": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcGirder
        ),
        "stb_apply_rc_beam": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcBeam
        ),
        "stb_apply_rc_wall": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcWall
        ),
        "stb_apply_rc_slab": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyRcSlab
        ),
    }
    _xml_element_name: ClassVar[str] = "StbApplyConditionList_RC"


class StbApplyConditionsList(StBridgeElement):
    """属性・条件適用リスト：StbApplyConditionsList

    Attributes:
        stb_apply_condition_list_rc (StbApplyConditionListRc): 子要素
        stb_apply_condition_list_s (StbApplyConditionListS): 子要素
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_apply_condition_list_rc": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyConditionListRc
        ),
        "stb_apply_condition_list_s": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyConditionListS
        ),
    }


class StbReinforcementStrengthListPile(StBridgeElement):
    """杭の径別鉄筋強度情報リスト：StbReinforcementStrengthListPile

    Attributes:
        stb_reinforcement_strength (list[StbReinforcementStrength]): 子要素 StbReinforcementStrength(径別鉄筋強度情報)
    """

    _fields: ClassVar[dict[str, _FI]] = {
        "stb_reinforcement_strength": _FI(
            kind=_FK.ELEMENT, min_occurs=1, py_type="list[StbReinforcementStrength]"
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
        stb_reinforcement_strength_list_pile (StbReinforcementStrengthListPile): 子要素 StbReinforcementStrengthListPile(杭の径別鉄筋強度情報リスト)
        stb_apply_conditions_list (StbApplyConditionsList): 子要素 StbApplyConditionsList(属性・条件適用リスト)
        stb_standard_plate_thickness_list (StbStandardPlateThicknessList): 子要素 StbStandardPlateThicknessList(システム標準板厚リスト)
        stb_connection_specs (StbConnectionSpecs): 子要素 StbConnectionSpecs(コネクションスペック情報)
        stb_weld_common (StbWeldCommon): 子要素 StbWeldCommon(溶接情報)
        stb_additional_information (StbAdditionalInformation): 子要素 StbAdditionalInformation(追加情報)
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
        "global_rotation": _FI(py_type=float, data_type=_DT.ANGLE, xml_type="angle"),
        "stb_reinforcement_strength_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbReinforcementStrengthList
        ),
        "stb_reinforcement_strength_list_pile": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbReinforcementStrengthListPile
        ),
        "stb_apply_conditions_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbApplyConditionsList
        ),
        "stb_standard_plate_thickness_list": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbStandardPlateThicknessList
        ),
        "stb_connection_specs": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbConnectionSpecs
        ),
        "stb_weld_common": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbWeldCommon),
        "stb_additional_information": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbAdditionalInformation
        ),
    }


class StBridge(StBridgeRoot):
    """ST-Bridge：ST_BRIDGE

    Attributes:
        version (str): 属性 ST-Bridgeのバージョン
        stb_common (StbCommon): 子要素 StbCommon(共通情報)
        stb_model (StbModel): 子要素 StbModel(位置・断面情報)
        stb_extensions (StbExtensions): 子要素 StbExtensions(拡張情報（複数）)
        stb_export_information (StbExportInformation): 子要素 StbExportInformation(出力情報)
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
        "stb_export_information": _FI(
            kind=_FK.ELEMENT, max_occurs=1, py_type=StbExportInformation
        ),
        "stb_cal_data": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbCalData),
        "stb_ana_models": _FI(kind=_FK.ELEMENT, max_occurs=1, py_type=StbAnaModels),
    }
    _xml_element_name: ClassVar[str] = "ST_BRIDGE"
