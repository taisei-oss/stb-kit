# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

from stbkit.core.data_model.stb_v2_1_1 import VERSION, StBridge
from stbkit.core.stb_io import load

CASES_DIR = Path(__file__).parents[6] / "tests" / "fixtures" / "cases"


def golden_v2_1_1_has_extension() -> StBridge:
    PATH: Path = CASES_DIR / "has_extension" / "has_extension.stb_v2_1_1.stb"
    stb: StBridge = load(PATH, version=VERSION)
    return stb


def golden_v2_1_1_frame_1x1x1_rc() -> StBridge:
    PATH: Path = CASES_DIR / "frame_1x1x1_rc" / "frame_1x1x1_rc.stb_v2_1_1.stb"
    stb: StBridge = load(PATH, version=VERSION)
    return stb
