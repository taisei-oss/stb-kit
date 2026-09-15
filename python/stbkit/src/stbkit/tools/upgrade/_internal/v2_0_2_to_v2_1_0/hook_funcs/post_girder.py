# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.repository import RepositoryV2_0_2
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Reporter

from ....._internal.utils import girder_utils


def post_girder(
    v202: stb_v2_0_2.StBridge,
    v210: stb_v2_1_0.StBridge,
    repo_v202: RepositoryV2_0_2,
    reporter: Reporter,
) -> None:
    try:
        v202_girders: list[stb_v2_0_2.StbGirder] = (
            v202.stb_model.stb_members.stb_girders.stb_girder
        )
    except NoneAccessError:
        return
    v210_girders: list[stb_v2_1_0.StbGirder] = (
        v210.stb_model.stb_members.stb_girders.stb_girder
    )
    for v202_girder, v210_girder in zip(v202_girders, v210_girders, strict=False):
        girder_length_value: girder_utils.GirderLengthValue = (
            girder_utils.girder_length(v202_girder, v202)
        )
        length: float = girder_length_value.length
        pos_control_point_start: float = girder_length_value.pos_control_point_start
        pos_control_point_end: float = girder_length_value.pos_control_point_end
        v202_sec: StBridgeElement = repo_v202.deref(v202_girder).id_section
        distances_s: list[float] = []
        distances_rc: list[float] = []
        match v202_sec:
            case stb_v2_0_2.StbSecBeamRc():
                figure_rc: stb_v2_0_2.StbSecFigureBeamRc = (
                    v202_sec.stb_sec_figure_beam_rc
                )
                if figure_rc.stb_sec_beam_rc_haunch:
                    if v202_girder.haunch_start_or_none is not None:
                        distances_rc.append(
                            pos_control_point_start + v202_girder.haunch_start
                        )
                    if v202_girder.haunch_end_or_none is not None:
                        distances_rc.append(
                            pos_control_point_end - v202_girder.haunch_end
                        )
            case stb_v2_0_2.StbSecBeamS():
                figure_s: stb_v2_0_2.StbSecSteelFigureBeamS = (
                    v202_sec.stb_sec_steel_figure_beam_s
                )
                if (
                    figure_s.stb_sec_steel_beam_s_haunch
                    or figure_s.stb_sec_steel_beam_s_five_types
                ):
                    if v202_girder.haunch_start_or_none is not None:
                        distances_s.append(
                            pos_control_point_start + v202_girder.haunch_start
                        )
                    if v202_girder.haunch_end_or_none is not None:
                        distances_s.append(
                            pos_control_point_end - v202_girder.haunch_end
                        )
                if (
                    figure_s.stb_sec_steel_beam_s_joint
                    or figure_s.stb_sec_steel_beam_s_five_types
                ):
                    if v202_girder.joint_start_or_none is not None:
                        distances_s.append(v202_girder.joint_start)
                    if v202_girder.joint_end_or_none is not None:
                        distances_s.append(length - v202_girder.joint_end)
            case stb_v2_0_2.StbSecBeamSrc():
                figure_s_src: stb_v2_0_2.StbSecSteelFigureBeamSrc = (
                    v202_sec.stb_sec_steel_figure_beam_src
                )
                if (
                    figure_s_src.stb_sec_steel_beam_src_haunch
                    or figure_s_src.stb_sec_steel_beam_src_five_types
                ):
                    if v202_girder.haunch_start_or_none is not None:
                        distances_s.append(
                            pos_control_point_start + v202_girder.haunch_start
                        )
                    if v202_girder.haunch_end_or_none is not None:
                        distances_s.append(
                            pos_control_point_end - v202_girder.haunch_end
                        )
                if (
                    figure_s_src.stb_sec_steel_beam_src_joint
                    or figure_s_src.stb_sec_steel_beam_src_five_types
                ):
                    if v202_girder.joint_start_or_none is not None:
                        distances_s.append(v202_girder.joint_start)
                    if v202_girder.joint_end_or_none is not None:
                        distances_s.append(length - v202_girder.joint_end)
                figure_rc_src: stb_v2_0_2.StbSecFigureBeamSrc = (
                    v202_sec.stb_sec_figure_beam_src
                )
                if figure_rc_src.stb_sec_beam_src_haunch:
                    if v202_girder.haunch_start_or_none is not None:
                        distances_rc.append(
                            pos_control_point_start + v202_girder.haunch_start
                        )
                    if v202_girder.haunch_end_or_none is not None:
                        distances_rc.append(
                            pos_control_point_end - v202_girder.haunch_end
                        )
        distances_rc.sort()
        distances_s.sort()
        if distances_s:
            v210_girder.stb_girder_steel_switch = [
                stb_v2_1_0.StbGirderSteelSwitch(order=index + 1, distance=distance)
                for index, distance in enumerate(distances_s)
            ]
        if distances_rc:
            v210_girder.stb_girder_concrete_switch = [
                stb_v2_1_0.StbGirderConcreteSwitch(order=index + 1, distance=distance)
                for index, distance in enumerate(distances_rc)
            ]
