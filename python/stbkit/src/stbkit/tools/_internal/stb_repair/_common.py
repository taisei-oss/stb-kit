# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass

from stbkit.core.stb_reporting import Reporter


@dataclass
class Defaults:
    steel_strength: str
    default_length: float
    default_float: float = 0.0
    default_string: str = "repair"


@dataclass
class RepairContext:
    defaults: Defaults
    reporter: Reporter
    unknown_section_id: int | None = None
