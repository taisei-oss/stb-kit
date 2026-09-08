# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.stb_v2_0_2 import StbGirder, StBridge
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase

from ._common import RepairContext


def _repair_stb_girder(stb: StBridge, *, context: RepairContext) -> None:
    # isfoundationが無い場合falseを入れる
    try:
        girders: list[StbGirder] = stb.stb_model.stb_members.stb_girders.stb_girder
    except NoneAccessError:
        return
    for girder in girders:
        if girder.is_foundation_or_none is None:
            girder.is_foundation = False
            context.reporter.warning(
                "StbGirderのisfoundationがNoneなのでFalseに設定しました",
                code=Code.REPAIR_LOG,
                phase=Phase.REPAIR,
                stb_element=girder,
            )


def _repair_stb_joint_beam_shape_h(stb: StBridge, *, context: RepairContext) -> None:
    try:
        joints = stb.stb_model.stb_joints.stb_joint_beam_shape_h
    except NoneAccessError:
        return
    for joint in joints:
        if (
            joint.stb_joint_shape_h_or_none is not None
            and joint.stb_joint_shape_h.strength_plate_or_none is None
        ):
            joint.stb_joint_shape_h.strength_plate = context.defaults.steel_strength
            context.reporter.warning(
                "StbJointShapeHのstrength_plateがNoneなので、デフォルト値を設定しました",
                code=Code.REPAIR_LOG,
                phase=Phase.REPAIR,
                stb_element=joint.stb_joint_shape_h,
                attr_name="strength_plate",
            )


def repair_stb(stb: StBridge, *, context: RepairContext) -> None:
    _repair_stb_girder(stb, context=context)
    _repair_stb_joint_beam_shape_h(stb, context=context)
