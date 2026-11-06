# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api import stb_latest

from ...._internal.data_model.ifc_data.entity_data import (
    IfcBuilding,
    IfcBuildingStorey,
    IfcModel,
    IfcProject,
    IfcSite,
)
from ..stb_latest_to_element_data import stb_to_element_data
from ..stb_latest_to_element_data.axes import stb_axes_to_ifc_grid_data
from .convert_option_stb_to_ifc import (
    CompositeOutputMode,
    ConvertOptionStbToIfc,
    StoryMode,
)


def stb_to_ifc_data(
    stb: stb_latest.StBridge,
    *,
    option: ConvertOptionStbToIfc | None = None,
    reporter: Reporter,
) -> IfcModel:
    reporter.info(
        "---ST-Bridge->IFCジオメトリデータ変換処理開始---",
        code=Code.PROGRESS_INFO,
        phase=Phase.CONVERT_IFC,
    )
    option = option or ConvertOptionStbToIfc()

    elements = stb_to_element_data(
        stb,
        reporter=reporter,
        include_src_concrete=option.src_output_mode != CompositeOutputMode.STEEL_ONLY,
        include_src_steel=option.src_output_mode != CompositeOutputMode.RC_ONLY,
        include_cft_concrete=option.cft_output_mode != CompositeOutputMode.STEEL_ONLY,
        include_cft_steel=option.cft_output_mode != CompositeOutputMode.RC_ONLY,
        story_mode=option.story_mode,
    )
    grids = stb_axes_to_ifc_grid_data(stb, reporter=reporter)
    building_storey_undefined: IfcBuildingStorey = IfcBuildingStorey(name="undefined")
    building_storeys: list[IfcBuildingStorey] = []
    story_dict: dict[int, IfcBuildingStorey] = {}
    if option.story_mode is not StoryMode.UNDEFINED:
        try:
            for stb_story in stb.stb_model.stb_stories.stb_story:
                building_story = IfcBuildingStorey(
                    name=stb_story.name_or_none,
                    guid=stb_story.guid_or_none,
                    elevation=stb_story.height_or_none,
                )
                building_storeys.append(building_story)
                story_dict[stb_story.id] = building_story
        except NoneAccessError:
            pass
        for element in elements:
            if element.story_id in story_dict:
                story_dict[element.story_id].elements.append(element)
            else:
                building_storey_undefined.elements.append(element)
    else:
        building_storey_undefined.elements.extend(elements)
    if building_storey_undefined.elements or (not building_storeys and grids):
        building_storeys.append(building_storey_undefined)
    if building_storeys:
        building_storeys[0].grids = grids

    building: IfcBuilding = IfcBuilding(
        name="Building", building_storeys=building_storeys
    )
    site: IfcSite = IfcSite(name="Site", building=building)
    if stb.stb_common_or_none and stb.stb_common.project_name:
        project_name: str = stb.stb_common.project_name
    else:
        project_name = "Untitled Project"
    project: IfcProject = IfcProject(name=project_name, site=site)
    model: IfcModel = IfcModel(project=project)
    reporter.info(
        "---ST-Bridge->IFCジオメトリデータ変換処理終了---",
        code=Code.PROGRESS_INFO,
        phase=Phase.CONVERT_IFC,
    )
    return model
