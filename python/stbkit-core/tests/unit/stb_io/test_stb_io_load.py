# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from io import StringIO
from typing import Final

import pytest

from stbkit.core.stb_exceptions import UnsupportedStbVersionError
from stbkit.core.stb_io import load, loads

UNSUPPORTED_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="99.9.9">
 <StbCommon project_name="unsupported_version" app_name="stbkit" app_version="0.0.0"/>
</ST_BRIDGE>
"""


def test_load_unsupported_version() -> None:
    with pytest.raises(UnsupportedStbVersionError):
        loads(UNSUPPORTED_STB)


def test_loads_unsupported_version() -> None:
    with pytest.raises(UnsupportedStbVersionError):
        str_io: StringIO = StringIO(UNSUPPORTED_STB)
        load(str_io)
