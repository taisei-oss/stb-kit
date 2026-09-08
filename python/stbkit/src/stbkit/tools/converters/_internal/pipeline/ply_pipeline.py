# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

from stbkit.core.stb_reporting import NullReporter

from ...._internal.data_model.building_geometry import BuildingGeometry
from ..building_geometry_to_ply_text import building_geometry_to_ply_text
from ..element_data_to_building_geometry import element_data_to_building_geometry
from ..stb_latest_to_element_data import stb_to_element_data
from .data import _DataFormat, _ObjectData
from .stb_pipeline_latest import StbLatestData
from .step import _ExecutableStep, _ExecutionContext, _ExecutionResult


class _PlyData(_ObjectData[BuildingGeometry]):
    def __init__(self, value: BuildingGeometry) -> None:
        super().__init__(format=_DataFormat.PLY, value=value)


def save_ply_data(data: _PlyData, path: Path) -> None:
    ply_text: str = building_geometry_to_ply_text(data.value)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ply_text)


class _StbToPlyStep(_ExecutableStep[StbLatestData, _PlyData]):
    name = "STB -> PLY"

    def execute(
        self, input: StbLatestData, *, context: _ExecutionContext
    ) -> _ExecutionResult[_PlyData]:
        if not isinstance(input, StbLatestData):
            raise TypeError(f"StBridgeデータではありません: {type(input)}")
        elements = stb_to_element_data(
            input.value,
            reporter=context.reporter
            if context.reporter is not None
            else NullReporter(),
        )
        mesh_data = element_data_to_building_geometry(
            elements,
            allow_polygons=True,
            reporter=context.reporter
            if context.reporter is not None
            else NullReporter(),
        )
        return _ExecutionResult(_PlyData(mesh_data))
