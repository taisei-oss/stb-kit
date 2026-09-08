# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.tools._internal.utils.mesh_utils import create_mesh
from stbkit.tools._internal.vectors import Vector2d


def test_mesh_rectangle() -> None:
    out_points: list[Vector2d] = [
        Vector2d(0.0, 0.0),
        Vector2d(1.0, 0.0),
        Vector2d(1.0, 1.0),
        Vector2d(0.0, 1.0),
    ]
    vertices, faces, new_out_points, new_in_points = create_mesh(out_points, [])
    assert vertices == [
        Vector2d(0.0, 1.0),
        Vector2d(0.0, 0.0),
        Vector2d(1.0, 0.0),
        Vector2d(1.0, 1.0),
    ]
    assert faces == [(0, 1, 2), (2, 3, 0)]
    assert new_out_points is None
    assert new_in_points is None


def test_mesh_rectangle_with_open() -> None:
    out_points: list[Vector2d] = [
        Vector2d(0.0, 0.0),
        Vector2d(1.0, 0.0),
        Vector2d(1.0, 1.0),
        Vector2d(0.0, 1.0),
    ]
    in_points: list[list[Vector2d]] = [
        [
            Vector2d(0.4, 0.4),
            Vector2d(0.6, 0.4),
            Vector2d(0.6, 0.6),
            Vector2d(0.4, 0.6),
        ]
    ]
    vertices, faces, new_out_points, new_in_points = create_mesh(out_points, in_points)
    assert vertices == [
        Vector2d(0.0, 0.4),
        Vector2d(0.0, 0.0),
        Vector2d(1.0, 0.0),
        Vector2d(0.4, 0.4),
        Vector2d(0.6, 0.4),
        Vector2d(1.0, 0.4),
        Vector2d(0.0, 0.6),
        Vector2d(0.4, 0.6),
        Vector2d(0.6, 0.6),
        Vector2d(1.0, 0.6),
        Vector2d(0.0, 1.0),
        Vector2d(1.0, 1.0),
    ]
    assert faces == [
        (0, 1, 2),
        (2, 3, 0),
        (2, 4, 3),
        (2, 5, 4),
        (6, 0, 3),
        (3, 7, 6),
        (8, 4, 5),
        (5, 9, 8),
        (10, 6, 7),
        (10, 7, 8),
        (10, 8, 9),
        (9, 11, 10),
    ]
    assert new_out_points is None
    assert new_in_points is None
