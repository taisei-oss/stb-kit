# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_reporting import Code, Phase, Reporter

from ..common import ElementHook


def post_sec_damping_device_friction(
    before: StBridgeElement,
    after: StBridgeElement,
    *,
    reporter: Reporter,
) -> None:
    if isinstance(before, stb_v2_1_0.StbSecDampingDeviceFriction):
        reporter.error(
            "StbSecDampingDeviceFrictionの子要素StbSecIsolatingDeviceSpecificationChangeは"
            "XSDに誤記がありstbkitで扱えないため、値を破棄しました",
            code=Code.UNEXPECTED_ERROR,
            phase=Phase.UPGRADE,
            stb_element=before,
        )


HOOKS: dict[str, ElementHook] = {
    "StbSecDampingDeviceFriction": post_sec_damping_device_friction,
}
