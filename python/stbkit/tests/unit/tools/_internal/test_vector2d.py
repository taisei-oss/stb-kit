# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.tools._internal.vectors import Vector2d


def test_vector2d_add() -> None:
    vec1: Vector2d = Vector2d(1.0, 2.0)
    vec2: Vector2d = Vector2d(3.0, 4.0)
    expected: Vector2d = Vector2d(4.0, 6.0)
    assert vec1 + vec2 == expected


def test_vector2d_sub() -> None:
    vec1: Vector2d = Vector2d(11.0, 10.0)
    vec2: Vector2d = Vector2d(3.0, 4.0)
    expected: Vector2d = Vector2d(8.0, 6.0)
    assert vec1 - vec2 == expected


def test_vector2d_neg() -> None:
    vec: Vector2d = Vector2d(5.0, -7.0)
    expected: Vector2d = Vector2d(-5.0, 7.0)
    assert -vec == expected


def test_vector2d_distanse_to() -> None:
    assert Vector2d(4.0, 5.0).distance_to(Vector2d(1.0, 1.0)) == 5.0
