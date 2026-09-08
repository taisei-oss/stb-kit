# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from enum import StrEnum


class EntityName(StrEnum):
    IFC_BEAM = "IfcBeam"
    IFC_BUILDING = "IfcBuilding"
    IFC_BUILDING_STOREY = "IfcBuildingStorey"
    IFC_C_SHAPE_PROFILE_DEF = "IfcCShapeProfileDef"
    IFC_CIRCLE_PROFILE_DEF = "IfcCircleProfileDef"
    IFC_CIRCLE_HOLLOW_PROFILE_DEF = "IfcCircleHollowProfileDef"
    IFC_COLUMN = "IfcColumn"
    IFC_ELEMENT_ASSEMBLY = "IfcElementAssembly"
    IFC_FOOTING = "IfcFooting"
    IFC_I_SHAPE_PROFILE_DEF = "IfcIShapeProfileDef"
    IFC_MEMBER = "IfcMember"
    IFC_PILE = "IfcPile"
    IFC_PROJECT = "IfcProject"
    IFC_REL_AGGREGATES = "IfcRelAggregates"
    IFC_REL_CONTAINED_IN_SPATIAL_STRUCTURE = "IfcRelContainedInSpatialStructure"
    IFC_RECTANGLE_HOLLOW_PROFILE_DEF = "IfcRectangleHollowProfileDef"
    IFC_RECTANGLE_PROFILE_DEF = "IfcRectangleProfileDef"
    IFC_SITE = "IfcSite"
    IFC_SLAB = "IfcSlab"
    IFC_T_SHAPE_PROFILE_DEF = "IfcTShapeProfileDef"
    IFC_U_SHAPE_PROFILE_DEF = "IfcUShapeProfileDef"
    IFC_WALL = "IfcWall"
