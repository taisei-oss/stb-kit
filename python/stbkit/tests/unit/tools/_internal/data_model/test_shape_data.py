# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.tools._internal.data_model.shape_data import diagram_core
from stbkit.tools._internal.vectors import Vector2d


def test_diagram_core_rectangle() -> None:
    points: list[Vector2d] = [
        Vector2d(0.0, 0.0),
        Vector2d(4.0, 0.0),
        Vector2d(4.0, 2.0),
        Vector2d(0.0, 2.0),
    ]
    assert Vector2d(2.0, 1.0) == diagram_core(points)


def test_diagram_core_triangle() -> None:
    points: list[Vector2d] = [
        Vector2d(0.0, 0.0),
        Vector2d(4.0, 0.0),
        Vector2d(2.0, 3.0),
    ]
    assert Vector2d(2.0, 1.0) == diagram_core(points)


def test_diagram_core_octagon() -> None:
    points: list[Vector2d] = [
        Vector2d(1.0, 0.0),
        Vector2d(3.0, 0.0),
        Vector2d(4.0, 1.0),
        Vector2d(4.0, 3.0),
        Vector2d(3.0, 4.0),
        Vector2d(1.0, 4.0),
        Vector2d(0.0, 3.0),
        Vector2d(0.0, 1.0),
    ]
    assert Vector2d(2.0, 2.0) == diagram_core(points)
