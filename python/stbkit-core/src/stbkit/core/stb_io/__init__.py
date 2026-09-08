# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from ._internal.xml_io import dump as dump
from ._internal.xml_io import dumps as dumps
from ._internal.xml_io import load as load
from ._internal.xml_io import loads as loads

__all__ = [
    "dump",
    "dumps",
    "load",
    "loads",
]
