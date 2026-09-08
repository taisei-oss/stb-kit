# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import importlib.metadata
from typing import Final

PACKAGE_NAME: Final = "stbkit"

_tmp_version: str
try:
    _tmp_version = importlib.metadata.version(PACKAGE_NAME)
except ImportError:
    _tmp_version = "unknown"
PACKAGE_VERSION: Final[str] = _tmp_version

REPAIR_DEFAULT_LENGTH_MM: Final[float] = 0.1
UNKNOWN_ELEMENT_SIZE_MM: Final[float] = 10.0
DEBUG_DUMP_DIR_ENV: Final[str] = "STBKIT_DEBUG_DUMP_DIR"
