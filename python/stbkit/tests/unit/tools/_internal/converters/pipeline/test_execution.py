# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

from stbkit.core._internal.constants import LATEST_STB_VERSION
from stbkit.core.stb_reporting import NullReporter

from stbkit.tools.converters._internal.pipeline.data import (
    _Data,
    _DataFormat,
    _DataFormatSet,
    _DataKind,
    _StbVersion,
)
from stbkit.tools.converters._internal.pipeline.execution import (
    execute_conversion,
    open_data,
    to_text,
)
from stbkit.tools.converters._internal.pipeline.stb_pipeline import StbData
from stbkit.tools.converters._internal.pipeline.stb_pipeline_latest import (
    StbLatestData,
)
from stbkit.tools.converters._internal.pipeline.step import (
    _ExecutionResult,
)


def _fixture_path() -> Path:
    return Path("tests/fixtures/cases/column_s/column_s.stb_v2_0_2.stb")


def test_convert_stb_to_latest() -> None:
    reporter: NullReporter = NullReporter()
    input_data: _Data = open_data(
        _fixture_path(),
        _DataFormatSet(
            _DataFormat.STB,
            _DataKind.OBJECT,
            stb_version=_StbVersion.V2_0_2,
        ),
        reporter,
    )

    result: _ExecutionResult[_Data] = execute_conversion(
        input_data,
        _DataFormatSet(
            _DataFormat.STB,
            _DataKind.OBJECT,
            stb_version=_StbVersion.LATEST,
        ),
        reporter=reporter,
    )

    assert isinstance(result.output, StbLatestData)
    assert result.output.value.version == LATEST_STB_VERSION
    assert f'version="{LATEST_STB_VERSION}"' in to_text(result.output, reporter)


def test_convert_stb_to_v2_1_0() -> None:
    reporter: NullReporter = NullReporter()
    input_data: _Data = open_data(
        _fixture_path(),
        _DataFormat.STB,
        reporter,
    )

    result: _ExecutionResult[_Data] = execute_conversion(
        input_data,
        _DataFormatSet(
            _DataFormat.STB,
            _DataKind.OBJECT,
            stb_version=_StbVersion.V2_1_0,
        ),
        reporter=reporter,
    )

    assert isinstance(result.output, StbData)
    assert result.output.stb_version == _StbVersion.V2_1_0
    assert result.output.value.version == "2.1.0"
