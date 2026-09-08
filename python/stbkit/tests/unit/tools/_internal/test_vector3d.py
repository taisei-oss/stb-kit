# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import unittest
from math import sqrt

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0

from stbkit.tools._internal.vectors import Vector3d


class Vector3dTest(unittest.TestCase):
    def test_from_list(self) -> None:
        v: Vector3d = Vector3d.from_collection([1.0, 2.0, 3.0])
        self.assertEqual(1.0, v.x)
        self.assertEqual(2.0, v.y)
        self.assertEqual(3.0, v.z)

    def test_from_tuple(self) -> None:
        v: Vector3d = Vector3d.from_collection((1.0, 2.0, 3.0))
        self.assertEqual(1.0, v.x)
        self.assertEqual(2.0, v.y)
        self.assertEqual(3.0, v.z)

    def test_getitem(self) -> None:
        v: Vector3d = Vector3d(1.0, 2.0, 3.0)
        self.assertEqual(1.0, v[0])
        self.assertEqual(2.0, v[1])
        self.assertEqual(3.0, v[2])

    def test_from_stb_node_202(self) -> None:
        stb_node: stb_v2_0_2.StbNode = stb_v2_0_2.StbNode(x=1000.0, y=2000.0, z=3000.0)
        v: Vector3d = Vector3d.from_stb_node(stb_node)
        self.assertEqual(1000.0, v.x)
        self.assertEqual(2000.0, v.y)
        self.assertEqual(3000.0, v.z)

    def test_from_stb_node_210(self) -> None:
        stb_node: stb_v2_1_0.StbNode = stb_v2_1_0.StbNode(x=1000.0, y=2000.0, z=3000.0)
        v: Vector3d = Vector3d.from_stb_node(stb_node)
        self.assertEqual(1000.0, v.x)
        self.assertEqual(2000.0, v.y)
        self.assertEqual(3000.0, v.z)

    def test_add(self) -> None:
        v1: Vector3d = Vector3d(1.0, 2.0, 3.0)
        v2: Vector3d = Vector3d(4.0, 5.0, 6.0)
        expected: Vector3d = Vector3d(5.0, 7.0, 9.0)
        self.assertEqual(expected, v1 + v2)

    def test_rmul(self) -> None:
        v: Vector3d = Vector3d(1.0, 2.0, 3.0)
        scaler: float = 2.0
        expected: Vector3d = Vector3d(2.0, 4.0, 6.0)
        self.assertEqual(expected, scaler * v)

    def test_sub(self) -> None:
        v1: Vector3d = Vector3d(11.0, 12.0, 13.0)
        v2: Vector3d = Vector3d(4.0, 3.0, 2.0)
        expected: Vector3d = Vector3d(7.0, 9.0, 11.0)
        self.assertEqual(expected, v1 - v2)

    def test_clone(self) -> None:
        v1: Vector3d = Vector3d(1.0, 2.0, 3.0)
        v2: Vector3d = v1.clone()
        self.assertEqual(v1, v2)
        self.assertFalse(v1 is v2)

    def test_cross(self) -> None:
        v1: Vector3d = Vector3d(1.0, 0.0, 0.0)
        v2: Vector3d = Vector3d(0.0, 1.0, 0.0)
        expected: Vector3d = Vector3d(0.0, 0.0, 1.0)
        self.assertEqual(expected, v1.cross(v2))

    def test_distance_to(self) -> None:
        v1: Vector3d = Vector3d(1.0, 2.0, 3.0)
        v2: Vector3d = Vector3d(2.0, 3.0, 4.0)
        expected: float = sqrt(3.0)
        self.assertEqual(expected, v1.distance_to(v2))

    def test_dot(self) -> None:
        v1: Vector3d = Vector3d(1.0, 2.0, 3.0)
        v2: Vector3d = Vector3d(2.0, 3.0, 4.0)
        expected: float = 20.0
        self.assertEqual(expected, v1.dot(v2))

    def test_length(self) -> None:
        v: Vector3d = Vector3d(1.0, 2.0, 3.0)
        expected: float = sqrt(14.0)
        self.assertEqual(expected, v.length())

    def test_mm_to_m(self) -> None:
        v: Vector3d = Vector3d(1000.0, 2000.0, 3000.0)
        expected: Vector3d = Vector3d(1.0, 2.0, 3.0)
        self.assertEqual(expected, v.mm_to_m())

    def test_normalized(self) -> None:
        v: Vector3d = Vector3d(1.0, 2.0, 3.0)
        length: float = sqrt(14.0)
        expected: Vector3d = Vector3d(1.0 / length, 2.0 / length, 3.0 / length)
        self.assertEqual(expected, v.normalize())

    def test_perpendicular_vector_on_plane(self) -> None:
        vec1: Vector3d = Vector3d(2.0, 0.0, 0.0)
        vec2: Vector3d = Vector3d(1.0, 1.0, 0.0)
        actual: Vector3d = vec1.perpendicular_vector_on_plane(vec2)
        expected: Vector3d = Vector3d(0.0, 1.0, 0.0)
        self.assertEqual(expected, actual)

    def test_rotate_around_axis(self) -> None:
        v: Vector3d = Vector3d(1.0, 0.0, 0.0)
        angle: float = 90.0
        axis: Vector3d = Vector3d(0.0, 1.0, 0.0)
        actual: Vector3d = v.rotate_around_axis(angle, axis)
        expected: Vector3d = Vector3d(0.0, 0.0, -1.0)
        tolerance: float = 1e-15
        self.assertAlmostEqual(actual.x, expected.x, delta=tolerance)
        self.assertAlmostEqual(actual.y, expected.y, delta=tolerance)
        self.assertAlmostEqual(actual.z, expected.z, delta=tolerance)

    def test_to_tuple(self) -> None:
        v: Vector3d = Vector3d(1.0, 2.0, 3.0)
        expected: tuple[float, float, float] = (1.0, 2.0, 3.0)
        self.assertEqual(expected, v.to_tuple())

    def test_neg(self) -> None:
        vec: Vector3d = Vector3d(5.0, -7.0, 9.0)
        expected: Vector3d = Vector3d(-5.0, 7.0, -9.0)
        self.assertEqual(expected, -vec)


def test_zero() -> None:
    v: Vector3d = Vector3d.zero()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0
