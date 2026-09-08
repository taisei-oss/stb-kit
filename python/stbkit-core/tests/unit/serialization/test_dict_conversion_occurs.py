# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Any

from stbkit.api import StBridgeRoot
from stbkit.api.experimental import from_dict, to_dict

from stbkit.core.data_model.common import _FieldKind
from stbkit.core.data_model.stb_v2_1_0 import VERSION, StbCommon, StBridge
from stbkit.core.stb_reporting import CollectingReporter


def _stb_common_dict(project_name: str) -> dict[str, Any]:
    common: StbCommon = StbCommon(
        project_name=project_name,
        app_name="stbkit",
        app_version="0.0.0",
    )
    return to_dict(common)


def test_invalid_max_occurs() -> None:
    stb_dict: dict[str, Any] = {
        "ST_BRIDGE": {
            "version": VERSION,
            "StbCommon": [_stb_common_dict("first"), _stb_common_dict("second")],
        }
    }

    stb: StBridgeRoot = from_dict(stb_dict, reporter=CollectingReporter())
    assert isinstance(stb, StBridge)
    assert stb.stb_common.project_name == "first"

    assert stb._extension is not None
    invalid_values = stb._extension._invalid_values
    assert invalid_values is not None
    assert len(invalid_values) == 1
    assert invalid_values[0].kind == _FieldKind.ELEMENT
