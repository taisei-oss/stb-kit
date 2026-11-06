# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from enum import Enum


class CompositeOutputMode(Enum):
    """SRC・CFT部材の出力モード"""

    RC_ONLY = "rc_only"
    """RC形状のみ変換"""
    STEEL_ONLY = "steel_only"
    """鉄骨形状のみ変換"""
    RC_AND_STEEL = "rc_and_steel"
    """RC,鉄骨全て変換"""


class StoryMode(Enum):
    LOOKING_DOWN = "looking_down"
    """見下げ"""
    LOOKING_UP = "looking_up"
    """見上げ"""
    UNDEFINED = "undefined"
    """階を定義しない"""


@dataclass(kw_only=True)
class ConvertOptionStbToIfc:
    cft_output_mode: CompositeOutputMode = CompositeOutputMode.RC_AND_STEEL
    src_output_mode: CompositeOutputMode = CompositeOutputMode.RC_AND_STEEL
    story_mode: StoryMode = StoryMode.LOOKING_DOWN
