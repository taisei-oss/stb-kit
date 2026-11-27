# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core._internal.utils.version_utils import Version


def test_version_comparison() -> None:
    v2_1_0 = Version("2.1.0")
    v2_1_1 = Version("2.1.1")
    v2_0_2 = Version("2.0.2")
    v2_10_0 = Version("2.10.0")
    assert v2_1_1 == Version("2.1.1")
    assert v2_1_1 <= Version("2.1.1")
    assert v2_1_1 >= Version("2.1.1")
    assert v2_1_0 < v2_1_1
    assert v2_1_0 <= v2_1_1
    assert v2_0_2 < v2_1_0
    assert v2_0_2 <= v2_1_0
    assert v2_10_0 > v2_1_1
    assert v2_10_0 >= v2_1_1
