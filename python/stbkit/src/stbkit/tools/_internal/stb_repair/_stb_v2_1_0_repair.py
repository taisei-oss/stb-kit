# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid

from stbkit.core.data_model.stb_v2_1_0 import (
    StbGirder,
    StBridge,
    StbSections,
    StbSecUndefined,
)
from stbkit.core.repository import RepositoryV2_1_0
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase

from ._common import RepairContext


def _get_unknown_section_id(stb: StBridge, *, context: RepairContext) -> int:
    if context.unknown_section_id is not None:
        return context.unknown_section_id
    sections: StbSections = stb.ensure.stb_model().ensure.stb_sections()
    max_id: int = 1
    for sec in sections.stb_sec_undefined:
        max_id = max(max_id, sec.id)
    unknown_id: int = max_id + 1
    context.unknown_section_id = unknown_id
    undefined: StbSecUndefined = StbSecUndefined(
        id=unknown_id,
        name="不明断面(stbkitにより自動生成)",
        guid=uuid.uuid4(),
    )
    sections.stb_sec_undefined.append(undefined)
    context.reporter.warning(
        f"構造不明断面(id={unknown_id})を新規に作成しました",
        code=Code.REPAIR_LOG,
        phase=Phase.REPAIR,
        stb_element=undefined,
    )
    return unknown_id


def _repair_stb_girder(
    stb: StBridge, *, context: RepairContext, repo: RepositoryV2_1_0
) -> None:
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
        if repo.deref(girder).id_section_or_none is None:
            unknown_id = _get_unknown_section_id(stb, context=context)
            girder.id_section = unknown_id
            context.reporter.warning(
                f"StbGirderのid_sectionが不正な参照なので、構造不明断面(id={unknown_id})を設定しました",
                code=Code.REPAIR_LOG,
                phase=Phase.REPAIR,
                stb_element=girder,
                attr_name="id_section",
            )
            if girder.kind_structure_or_none != "UNDEFINED":
                girder.kind_structure = "UNDEFINED"
                context.reporter.warning(
                    "StbGirderのid_sectionが不正な参照なので、構造種別をUNDEFINEDに設定しました",
                    code=Code.REPAIR_LOG,
                    phase=Phase.REPAIR,
                    stb_element=girder,
                    attr_name="kind_structure",
                )


def _repair_stb_joint_beam_shape_h(stb: StBridge, *, context: RepairContext) -> None:
    try:
        joints = stb.stb_model.stb_joints.stb_joint_beam_shape_h
    except NoneAccessError:
        return
    for joint in joints:
        if (
            joint.stb_joint_shape_h_or_none is not None
            and joint.stb_joint_shape_h.strength_plate_flange_or_none is None
        ):
            joint.stb_joint_shape_h.strength_plate_flange_or_none = (
                context.defaults.steel_strength
            )
            context.reporter.warning(
                "StbJointShapeHのstrength_plate_flangeがNoneなので、デフォルト値を設定しました",
                code=Code.REPAIR_LOG,
                phase=Phase.REPAIR,
                stb_element=joint.stb_joint_shape_h,
                attr_name="strength_plate_flange",
            )


def repair_stb(stb: StBridge, *, context: RepairContext) -> None:
    repo: RepositoryV2_1_0 = RepositoryV2_1_0(stb)
    _repair_stb_girder(stb, context=context, repo=repo)
    _repair_stb_joint_beam_shape_h(stb, context=context)
