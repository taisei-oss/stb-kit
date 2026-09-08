# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import math


def mm_to_m(value: float) -> float:
    return value / 1000.0


def m_to_mm(value: float) -> float:
    return value * 1000.0


def radian_to_degree(value: float) -> float:
    return math.degrees(value)


def degree_to_radian(value: float) -> float:
    return math.radians(value)
