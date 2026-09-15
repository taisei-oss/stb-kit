# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Final

from stbkit.api import StBridgeRoot, loads

from stbkit.core.data_model.common import _FieldKind, _InvalidValue
from stbkit.core.data_model.stb_v2_1_1 import StbCommon, StBridge
from stbkit.core.stb_reporting import Code, CollectingReporter, Phase, Severity

_INVALID_MAX_OCCURS_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="first" app_name="stbkit" app_version="0.0.0"/>
 <StbCommon project_name="second" app_name="stbkit" app_version="0.0.0"/>
 <StbModel>
  <StbNodes>
   <StbNode id="1" X="0" Y="0" Z="0" kind="ON_GRID"/>
  </StbNodes>
 </StbModel>
</ST_BRIDGE>
"""

_VALID_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="first" app_name="stbkit" app_version="0.0.0"/>
 <StbModel>
  <StbNodes>
   <StbNode id="1" X="0" Y="0" Z="0" kind="ON_GRID"/>
  </StbNodes>
 </StbModel>
</ST_BRIDGE>
"""


def test_loads_first_element_when_invalid_max_occurs() -> None:
    stb: StBridgeRoot = loads(_INVALID_MAX_OCCURS_STB, reporter=CollectingReporter())
    assert isinstance(stb, StBridge)

    assert stb.stb_common.project_name == "first"


def test_loads_stores_invalid_value() -> None:
    stb: StBridgeRoot = loads(_INVALID_MAX_OCCURS_STB, reporter=CollectingReporter())
    assert isinstance(stb, StBridge)

    assert stb._extension is not None
    invalid_values: list[_InvalidValue] | None = stb._extension._invalid_values
    assert invalid_values is not None
    assert len(invalid_values) == 1
    assert invalid_values[0].kind == _FieldKind.ELEMENT
    assert isinstance(invalid_values[0].value, StbCommon)
    assert invalid_values[0].value.project_name == "second"


def test_loads_reports_invalid_vale() -> None:
    reporter: CollectingReporter = CollectingReporter()

    _ = loads(_INVALID_MAX_OCCURS_STB, reporter=reporter)

    assert len(reporter.report) == 1
    item = reporter.report[0]
    assert item.severity == Severity.ERROR.value
    assert item.code == Code.SCHEMA_ERROR.value
    assert item.phase == Phase.LOAD.value
    assert item.xpath == "/ST_BRIDGE/StbCommon"
    assert "StbCommon" in item.message
    assert "最大回数" in item.message
    assert item.value == "2"
    assert item.ref_value == "<=1"


def test_loads_valid() -> None:
    reporter: CollectingReporter = CollectingReporter()

    stb: StBridgeRoot = loads(_VALID_STB, reporter=reporter)

    assert isinstance(stb, StBridge)
    assert stb._extension is None
    assert len(reporter.report) == 0
