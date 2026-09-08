# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from enum import Enum


class SrcConversionMode(Enum):
    """SRC部材の変換モード"""

    RC_ONLY = "rc_only"
    """RC形状のみ変換"""
    RC_AND_STEEL = "rc_and_steel"
    """鉄骨も含めて変換"""


@dataclass
class ConvertOptionStbToIfc:
    src_conversion_mode: SrcConversionMode = SrcConversionMode.RC_AND_STEEL
