# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.common import StBridgeRoot

from stbkit.api import stb_latest

from ....upgrade._internal.upgrade import upgrade_to_latest
from .data import _StbVersion
from .stb_pipeline import StbData
from .step import _ExecutableStep, _ExecutionContext, _ExecutionResult


class StbLatestData(StbData[stb_latest.StBridge]):
    def __init__(self, value: stb_latest.StBridge) -> None:
        super().__init__(value=value, stb_version=_StbVersion.LATEST)


class StbToLatestStep[TStb: StBridgeRoot](
    _ExecutableStep[StbData[TStb], StbLatestData]
):
    name = "STB -> STB Latest"

    def execute(
        self,
        data: StbData[TStb],
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[StbLatestData]:
        stb: StBridgeRoot = data.value
        if isinstance(stb, stb_latest.StBridge):
            return _ExecutionResult(output=StbLatestData(stb))
        if isinstance(stb, StBridgeRoot):
            stb_latest_value = upgrade_to_latest(stb, reporter=context.reporter)
            return _ExecutionResult(output=StbLatestData(stb_latest_value))
        raise TypeError(f"ST-Bridgeデータではありません: {type(stb)}")
