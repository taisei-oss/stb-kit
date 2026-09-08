# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

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
from .convert_option import ConvertOptionStbToIfc


def stb_to_ifc_data(
    stb: stb_latest.StBridge,
    *,
    option: ConvertOptionStbToIfc | None = None,
    reporter: Reporter,
) -> IfcModel:
    """現在Storeyを1つしか作っていない。
    階を定義していないST-Bridgeもあるため暫定処置。
    TODO:ST-Bridgeの階情報に応じてIFCの階を設定する
    """
    reporter.info(
        "---ST-Bridge->IFCジオメトリデータ変換処理開始---",
        code=Code.PROGRESS_INFO,
        phase=Phase.CONVERT_IFC,
    )
    option = option or ConvertOptionStbToIfc()

    elements = stb_to_element_data(stb, reporter=reporter)

    building_storey: IfcBuildingStorey = IfcBuildingStorey(
        name="1FL", elements=elements
    )
    building: IfcBuilding = IfcBuilding(
        name="Building", building_storeys=[building_storey]
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
