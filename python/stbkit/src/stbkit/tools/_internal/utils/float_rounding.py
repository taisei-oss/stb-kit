# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from ..vectors import Vector2d, Vector3d


def validated_round_digits(round_digits: int | None) -> int | None:
    if round_digits is None:
        return None
    if round_digits < 0:
        raise AssertionError("round_digitsは0以上である必要があります")
    return round_digits


def round_float(value: float, *, round_digits: int | None) -> float:
    round_digits = validated_round_digits(round_digits)
    if round_digits is None:
        return value
    return round(value, ndigits=round_digits)


def round_vector2d(
    value: Vector2d,
    *,
    round_digits: int | None,
) -> Vector2d:
    if round_digits is None:
        return value
    return Vector2d(
        round_float(value.x, round_digits=round_digits),
        round_float(value.y, round_digits=round_digits),
    )


def round_vector3d(
    value: Vector3d,
    *,
    round_digits: int | None,
) -> Vector3d:
    if round_digits is None:
        return value
    return Vector3d(
        round_float(value.x, round_digits=round_digits),
        round_float(value.y, round_digits=round_digits),
        round_float(value.z, round_digits=round_digits),
    )
