# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, cast

from stbkit.core import stb_io
from stbkit.core._internal.constants import (
    DEFAULT_MAX_XML_SIZE,
    LATEST_STB_VERSION,
)
from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_exceptions import UnsupportedStbVersionError
from stbkit.core.stb_reporting import NullReporter
from stbkit.core.stb_typing import StbVersion

from ...._internal.stb_repair._stb_repair import repair_stb
from ....upgrade._internal.upgrade import upgrade_to
from .data import (
    _DataFormat,
    _FileData,
    _FileFormat,
    _ObjectData,
    _StbVersion,
    _TextData,
)
from .step import _ExecutableStep, _ExecutionContext, _ExecutionResult


def _get_pipeline_stb_version(stb: StBridgeRoot) -> _StbVersion:
    try:
        return _StbVersion(stb.version)
    except ValueError:
        return _StbVersion.UNSPECIFIED


def _get_load_stb_version(version: _StbVersion) -> StbVersion | None:
    if version == _StbVersion.UNSPECIFIED:
        return None
    if version == _StbVersion.LATEST:
        return LATEST_STB_VERSION
    return cast(StbVersion, version.value)


class StbFileData(_FileData):
    def __init__(
        self,
        path: Path,
        *,
        stb_version: _StbVersion = _StbVersion.UNSPECIFIED,
        encoding: str | None = None,
    ) -> None:
        super().__init__(
            format=_DataFormat.STB,
            path=path,
            file_format=_FileFormat.XML,
            stb_version=stb_version,
            encoding=encoding,
        )


class StbTextData(_TextData):
    def __init__(
        self,
        text: str,
        *,
        stb_version: _StbVersion = _StbVersion.UNSPECIFIED,
        has_xml_declaration: bool = True,
    ) -> None:
        self.has_xml_declaration: bool = has_xml_declaration
        super().__init__(
            format=_DataFormat.STB,
            text=text,
            file_format=_FileFormat.XML,
            stb_version=stb_version,
        )


class StbData[TStb: StBridgeRoot](_ObjectData[TStb]):
    def __init__(self, value: TStb, stb_version: _StbVersion) -> None:
        super().__init__(format=_DataFormat.STB, value=value, stb_version=stb_version)


class StbUnspecifiedData(StbData[StBridgeRoot]):
    def __init__(self, value: StBridgeRoot) -> None:
        super().__init__(value=value, stb_version=_StbVersion.UNSPECIFIED)


class StbLoadStep(_ExecutableStep[StbFileData | StbTextData, StbData[StBridgeRoot]]):
    name = "STB Load"

    def execute(
        self,
        data: StbFileData | StbTextData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[StbData[StBridgeRoot]]:
        stb: StBridgeRoot
        version = _get_load_stb_version(data.stb_version or _StbVersion.UNSPECIFIED)
        max_size: int = (
            context.max_size if context.max_size is not None else DEFAULT_MAX_XML_SIZE
        )
        if isinstance(data, StbTextData):
            stb = stb_io.loads(
                data.text,
                version=version,
                max_size=max_size,
                reporter=context.reporter,
            )
        else:
            stb = stb_io.load(
                data.path,
                version=version,
                encoding=data.encoding,
                max_size=max_size,
                reporter=context.reporter,
            )
        return _ExecutionResult(output=StbData(stb, _get_pipeline_stb_version(stb)))


class StbDumpsStep[TStb: StBridgeRoot](_ExecutableStep[StbData[TStb], StbTextData]):
    name = "STB Dump"

    def execute(
        self,
        data: StbData[TStb],
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[StbTextData]:
        text = stb_io.dumps(data.value, reporter=context.reporter)
        return _ExecutionResult(
            output=StbTextData(
                text,
                stb_version=data.stb_version or _StbVersion.UNSPECIFIED,
            )
        )


@dataclass(frozen=True)
class StbToVersionStep(_ExecutableStep[StbData[StBridgeRoot], StbData[StBridgeRoot]]):
    """ST-Bridgeを指定されたバージョンへ更新するステップ。"""

    target_version: _StbVersion
    name: str = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "name", f"STB -> {self.target_version.value}")

    def execute(
        self,
        data: StbData[StBridgeRoot],
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[StbData[StBridgeRoot]]:
        if self.target_version in (
            _StbVersion.LATEST,
            _StbVersion.UNSPECIFIED,
        ):
            raise ValueError(
                "StbToVersionStepには具体的なST-Bridgeバージョンを指定してください"
            )

        actual_version = _get_pipeline_stb_version(data.value)
        if actual_version == self.target_version:
            return _ExecutionResult(output=StbData(data.value, self.target_version))

        target_version: Literal["2.0.1", "2.0.2", "2.1.0", "2.1.1"]
        match self.target_version:
            case _StbVersion.V2_0_1:
                target_version = "2.0.1"
            case _StbVersion.V2_0_2:
                target_version = "2.0.2"
            case _StbVersion.V2_1_0:
                target_version = "2.1.0"
            case _StbVersion.V2_1_1:
                target_version = "2.1.1"
            case _StbVersion.V2_0_0:
                raise UnsupportedStbVersionError("2.0.0への変換")
            case _:
                raise ValueError(
                    "StbToVersionStepには具体的なST-Bridgeバージョンを指定してください"
                )

        converted: StBridgeRoot = upgrade_to(
            data.value,
            to_version=target_version,
            reporter=context.reporter,
        )

        return _ExecutionResult(output=StbData(converted, self.target_version))


class StbAssignGuidsStep[TStb: StBridgeRoot](
    _ExecutableStep[StbData[TStb], StbData[TStb]]
):
    """ST-Bridge内のguid未設定要素へguidを割り当てるステップ"""

    name = "STB Assign GUIDs"

    def execute(
        self,
        data: StbData[TStb],
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[StbData[TStb]]:
        from stbkit.core._internal.transform.guid_tools import assign_guid_all

        assign_guid_all(data.value)
        return _ExecutionResult(output=data)


class StbRepairStep[TStb: StBridgeRoot](_ExecutableStep[StbData[TStb], StbData[TStb]]):
    name = "STB Repair"

    def execute(
        self,
        data: StbData[TStb],
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[StbData[TStb]]:
        repair_stb(data.value, reporter=context.reporter or NullReporter())
        return _ExecutionResult(output=data)
