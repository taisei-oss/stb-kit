# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

from argparse import _SubParsersAction
from typing import Any

from .._internal import summary


def register(subparsers: _SubParsersAction[Any]) -> None:
    summary.register(subparsers)
