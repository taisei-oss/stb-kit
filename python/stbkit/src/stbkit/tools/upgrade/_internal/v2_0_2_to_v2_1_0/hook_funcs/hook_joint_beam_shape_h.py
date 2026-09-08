# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_reporting import Reporter


def joint_beam_shape_h(
    before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
) -> None:
    if not isinstance(before, stb_v2_0_2.StbJointBeamShapeH) or not isinstance(
        after, stb_v2_1_0.StbJointBeamShapeH
    ):
        return
    frange_202: stb_v2_0_2.StbJointShapeHFlange | None = (
        before.stb_joint_shape_h_flange_or_none
    )
    if frange_202:
        nf: int | None = frange_202.nf_or_none
        mf: int | None = frange_202.mf_or_none
        frange_210: stb_v2_1_0.StbJointShapeHFlange = (
            after.ensure.stb_joint_shape_h_flange()
        )
        if nf is not None and mf is not None:
            for i in range(1, nf + 1):
                frange_bolt: stb_v2_1_0.StbJointShapeHFlangeBolt = (
                    stb_v2_1_0.StbJointShapeHFlangeBolt(id_order=i, mf=mf)
                )
                frange_210.stb_joint_shape_h_flange_bolt.append(frange_bolt)
    web_202: stb_v2_0_2.StbJointShapeHWeb | None = before.stb_joint_shape_h_web_or_none
    if web_202:
        nw: int | None = web_202.nw_or_none
        mw: int | None = web_202.mw_or_none
        web_210: stb_v2_1_0.StbJointShapeHWeb = after.ensure.stb_joint_shape_h_web()
        if nw is not None and mw is not None:
            for i in range(1, nw + 1):
                web_bolt: stb_v2_1_0.StbJointShapeHWebBolt = (
                    stb_v2_1_0.StbJointShapeHWebBolt(id_order=i, mw=mw)
                )
                web_210.stb_joint_shape_h_web_bolt.append(web_bolt)
