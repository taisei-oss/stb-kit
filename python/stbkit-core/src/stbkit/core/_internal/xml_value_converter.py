# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Any
from uuid import UUID


def any_to_xml_str(value: Any) -> str:
    if isinstance(value, UUID):
        return value.hex
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)
