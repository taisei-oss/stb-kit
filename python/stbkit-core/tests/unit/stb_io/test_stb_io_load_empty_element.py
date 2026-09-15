# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Final

from stbkit.core.data_model.stb_v2_1_1 import (
    VERSION,
    StbCommon,
    StbMembers,
    StbModel,
    StBridge,
)
from stbkit.core.stb_io import dumps, loads
from stbkit.core.stb_reporting import NullReporter

_EMPTY_STB_MODEL: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.1"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <StbCommon project_name="empty" app_name="stbkit" app_version="0.0.0"/>
 <StbModel/>
</ST_BRIDGE>
"""

_EMPTY_STB_MEMBERS: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.1"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <StbCommon project_name="empty" app_name="stbkit" app_version="0.0.0"/>
 <StbModel>
  <StbMembers/>
 </StbModel>
</ST_BRIDGE>
"""


def test_load_empty_element() -> None:
    stb: StBridge = loads(_EMPTY_STB_MODEL, version=VERSION, reporter=NullReporter())
    assert stb.stb_model_or_none is not None
    assert isinstance(stb.stb_model, StbModel)

    stb = loads(_EMPTY_STB_MEMBERS, version=VERSION, reporter=NullReporter())
    assert stb.stb_model.stb_members_or_none is not None
    assert isinstance(stb.stb_model.stb_members, StbMembers)


def test_dump_empty_required_element() -> None:
    stb: StBridge = StBridge(
        version=VERSION,
        stb_common=StbCommon(
            project_name="empty", app_name="stbkit", app_version="0.0.0"
        ),
        stb_model=StbModel(),
    )

    xml: str = dumps(stb)
    assert "<StbModel/>" in xml

    loaded_stb: StBridge = loads(xml, version=VERSION, reporter=NullReporter())
    assert loaded_stb.stb_model_or_none is not None
    assert isinstance(loaded_stb.stb_model, StbModel)
