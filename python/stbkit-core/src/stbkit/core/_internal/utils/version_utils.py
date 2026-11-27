# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True, order=True, init=False)
class Version:
    major: int
    minor: int
    patch: int

    def __init__(self, version: str) -> None:
        parts = version.split(".")
        object.__setattr__(self, "major", int(parts[0]))
        object.__setattr__(self, "minor", int(parts[1]))
        object.__setattr__(self, "patch", int(parts[2]))


V2_0_2: Final[Version] = Version("2.0.2")
V2_1_0: Final[Version] = Version("2.1.0")
