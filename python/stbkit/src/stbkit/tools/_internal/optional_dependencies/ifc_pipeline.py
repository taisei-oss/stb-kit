# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from typing import TYPE_CHECKING, cast

from stbkit.api import stb_latest

from ...converters._internal.pipeline.data import _DataFormat, _ObjectData
from ...converters._internal.pipeline.ply_pipeline import _PlyData
from ...converters._internal.pipeline.stb_pipeline_latest import StbLatestData
from ...converters._internal.pipeline.step import (
    _compose_steps,
    _ExecutableStep,
    _ExecutionContext,
    _ExecutionResult,
)
from .ifc_common import ensure_ifcopenshell, raise_import_error

if TYPE_CHECKING:
    from ifcopenshell import file as IfcFile

    from ..data_model.ifc_data.entity_data import IfcModel
else:
    type IfcFile = object
    type IfcModel = object


class IfcIntermediateData(_ObjectData[IfcModel]):
    def __init__(self, value: IfcModel) -> None:
        super().__init__(format=_DataFormat.IFC, value=value)


class IfcData(_ObjectData[IfcFile]):
    def __init__(self, value: IfcFile) -> None:
        ensure_ifcopenshell()
        super().__init__(format=_DataFormat.IFC, value=value)


def open_ifc_data(path: Path) -> IfcData:
    try:
        import ifcopenshell

        return IfcData(ifcopenshell.open(str(path)))
    except ImportError as e:
        raise_import_error(e)


def loads_ifc_data(text: str) -> IfcData:
    try:
        import ifcopenshell

        return IfcData(ifcopenshell.file.from_string(text))
    except ImportError as e:
        raise_import_error(e)


class StbLatestToIfcIntermediateStep(
    _ExecutableStep[StbLatestData, IfcIntermediateData]
):
    name = "STB -> IFC中間データ"

    def execute(
        self,
        data: StbLatestData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[IfcIntermediateData]:
        from ...converters._internal.stb_to_ifc_data import _stb_to_ifc_data

        stb: stb_latest.StBridge = data.value
        if not isinstance(stb, stb_latest.StBridge):
            raise TypeError(f"ST-Bridgeデータではありません: {type(stb)}")
        ifc_model: IfcModel = _stb_to_ifc_data.stb_to_ifc_data(
            stb,
            reporter=context.reporter,
        )
        return _ExecutionResult(output=IfcIntermediateData(ifc_model))


class IfcModelToIfcDataStep(_ExecutableStep[IfcIntermediateData, IfcData]):
    name = "IFC中間データ -> IFC"

    def execute(
        self,
        data: IfcIntermediateData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[IfcData]:
        from stbkit.core.stb_reporting import get_reporter

        ensure_ifcopenshell()
        from .ifc_exporter.ifc_entity_exporter import (
            IfcEntityExporter,
        )

        reporter = context.reporter or get_reporter()
        ifc_file = IfcEntityExporter.ifc_model_to_file(
            data.value,
            reporter=reporter,
            round_digits=context.ifc_round_digits,
            round_digits_mm=context.ifc_round_digits_mm,
        )
        return _ExecutionResult(output=IfcData(ifc_file))


class IfcDataToPlyStep(_ExecutableStep[IfcData, _PlyData]):
    name = "IFC -> PLY"

    def execute(
        self,
        data: IfcData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[_PlyData]:
        from .ifc_to_building_geometry import ifc_to_building_geometry

        mesh_data = ifc_to_building_geometry(data.value)
        return _ExecutionResult(output=_PlyData(mesh_data))


def stb_latest_to_ifc_step() -> _ExecutableStep[StbLatestData, IfcData]:
    step = _compose_steps(
        "STB -> IFC",
        (
            StbLatestToIfcIntermediateStep(),
            IfcModelToIfcDataStep(),
        ),
    )
    return cast(_ExecutableStep[StbLatestData, IfcData], step)
