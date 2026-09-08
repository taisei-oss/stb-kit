# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from ._internal.upgrade import upgrade_to as upgrade_to
from ._internal.upgrade import upgrade_to_latest as upgrade_to_latest

__all__ = [
    "upgrade_to",
    "upgrade_to_latest",
]
