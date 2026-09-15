# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import contextlib
import copy
import uuid
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Protocol
from uuid import UUID

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.repository import RepositoryV2_1_0
from stbkit.core.stb_exceptions import NoneAccessError, SchemaError
from stbkit.core.stb_reporting import Code, Phase, Reporter


class HasShapeAndStrength(Protocol):
    @property
    def shape_or_none(self) -> str | None: ...
    @property
    def strength_main_or_none(self) -> str | None: ...
    @property
    def strength_web_or_none(self) -> str | None: ...


class HasShapeAndStrengthAndPos(HasShapeAndStrength, Protocol):
    @property
    def pos(self) -> str: ...


@dataclass(frozen=True, kw_only=True, slots=True)
class SteelFigure:
    original_element: StBridgeElement
    straight: HasShapeAndStrength | None
    tapers: Sequence[HasShapeAndStrengthAndPos]
    joints: Sequence[HasShapeAndStrengthAndPos]
    haunches: Sequence[HasShapeAndStrengthAndPos]
    five_types: Sequence[HasShapeAndStrengthAndPos]


class HasId(Protocol):
    id: int
    guid: UUID


@dataclass(frozen=True, kw_only=True, slots=True)
class SteelBeamKind[TShape: StBridgeElement, TSection: HasId]:
    """SとSRCで分ける処理"""

    straight_shape: Callable[[int, stb_v2_1_0.StbSecSteelBeamStraight], TShape]
    taper_shape: Callable[[int, stb_v2_1_0.StbSecSteelBeamTaper], TShape]
    set_figure: Callable[[TSection, list[TShape]], None]


def _set_figure_s(
    section: stb_v2_1_0.StbSecBeamS, shapes: list[stb_v2_1_0.StbSecSteelBeamSShape]
) -> None:
    section.stb_sec_steel_figure_beam_s = stb_v2_1_0.StbSecSteelFigureBeamS(
        stb_sec_steel_beam_s_shape=shapes
    )


BEAM_KIND_S: SteelBeamKind[stb_v2_1_0.StbSecSteelBeamSShape, stb_v2_1_0.StbSecBeamS] = (
    SteelBeamKind(
        straight_shape=lambda order, straight: stb_v2_1_0.StbSecSteelBeamSShape(
            order=order, stb_sec_steel_beam_straight=straight
        ),
        taper_shape=lambda order, taper: stb_v2_1_0.StbSecSteelBeamSShape(
            order=order, stb_sec_steel_beam_taper=taper
        ),
        set_figure=_set_figure_s,
    )
)


def _set_figure_src(
    section: stb_v2_1_0.StbSecBeamSrc,
    shapes: list[stb_v2_1_0.StbSecSteelBeamSrcShape],
) -> None:
    section.stb_sec_steel_figure_beam_src = stb_v2_1_0.StbSecSteelFigureBeamSrc(
        stb_sec_steel_beam_src_shape=shapes
    )


BEAM_KIND_SRC: SteelBeamKind[
    stb_v2_1_0.StbSecSteelBeamSrcShape, stb_v2_1_0.StbSecBeamSrc
] = SteelBeamKind(
    straight_shape=lambda order, straight: stb_v2_1_0.StbSecSteelBeamSrcShape(
        order=order, stb_sec_steel_beam_straight=straight
    ),
    taper_shape=lambda order, taper: stb_v2_1_0.StbSecSteelBeamSrcShape(
        order=order, stb_sec_steel_beam_taper=taper
    ),
    set_figure=_set_figure_src,
)


def stb_sec_steel_figure_beam_s_to_v210[TShape: StBridgeElement, TSection: HasId](
    figure: SteelFigure | None,
    id_section: int,
    v210_sec_beam_s_list: list[TSection],
    kind: SteelBeamKind[TShape, TSection],
    *,
    reporter: Reporter,
) -> None:
    if figure is None:
        return
    v210_sec_beam_s: TSection | None = next(
        (s for s in v210_sec_beam_s_list if s.id == id_section), None
    )
    if v210_sec_beam_s is None:
        return
    v210_taper: stb_v2_1_0.StbSecSteelBeamTaper
    v210_shapes: list[TShape] = []
    if figure.straight is not None:
        kind.set_figure(
            v210_sec_beam_s,
            [
                kind.straight_shape(
                    1,
                    stb_v2_1_0.StbSecSteelBeamStraight(
                        shape=figure.straight.shape_or_none,
                        strength_main=figure.straight.strength_main_or_none,
                        strength_web=figure.straight.strength_web_or_none,
                    ),
                )
            ],
        )
        return
    if figure.tapers:
        v202_taper: Sequence[HasShapeAndStrengthAndPos] = figure.tapers
        if len(v202_taper) != 2:
            reporter.warning(
                message="Taperの回数がスキーマ違反のため変換できませんでした",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )
            return
        try:
            v202_taper_start: HasShapeAndStrengthAndPos = next(
                pos for pos in v202_taper if pos.pos == "START"
            )
            v202_taper_end: HasShapeAndStrengthAndPos = next(
                pos for pos in v202_taper if pos.pos == "END"
            )
        except StopIteration:
            reporter.warning(
                message="TaperのSTART,ENDが1回ずつ使われていないため変換できませんでした",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )
            return
        if (
            v202_taper_start.strength_main_or_none
            != v202_taper_end.strength_main_or_none
        ):
            reporter.warning(
                message=f"{figure.original_element._name_for_log()} 始端と終端の"
                "鉄骨強度（主）が異なります。",
                code=Code.SCHEMA_VERSION_MISMATCH,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )
        if v202_taper_start.strength_web_or_none != v202_taper_end.strength_web_or_none:
            reporter.warning(
                message=f"{figure.original_element._name_for_log()} 始端と終端の"
                "鉄骨強度（ウェブ）が異なります。",
                code=Code.SCHEMA_VERSION_MISMATCH,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )

        v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
            start_shape=v202_taper_start.shape_or_none,
            end_shape=v202_taper_end.shape_or_none,
            strength_main=v202_taper_start.strength_main_or_none,
            strength_web=v202_taper_end.strength_web_or_none,
        )
        kind.set_figure(v210_sec_beam_s, [kind.taper_shape(1, v210_taper)])
        return

    if figure.joints:
        v202_joints: Sequence[HasShapeAndStrengthAndPos] = figure.joints
        if len(v202_joints) < 2 or len(v202_joints) > 3:
            reporter.warning(
                message="Jointの回数がスキーマ違反のため変換できません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )
            return
        tmp_joints: dict[str, HasShapeAndStrengthAndPos] = {}
        for pos in ["START", "CENTER", "END"]:
            with contextlib.suppress(StopIteration):
                tmp_joints[pos] = next(
                    joint for joint in v202_joints if joint.pos == pos
                )
        if "CENTER" not in tmp_joints:
            reporter.warning(
                message=f"{figure.original_element._name_for_log()} Jointの"
                "pos=CENTERがありません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )
            return
        elif len(tmp_joints) < 2:
            reporter.warning(
                message=f"{figure.original_element._name_for_log()} Jointの"
                "pos=STARTまたはENDがありません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )
            return
        for i, (_, joint) in enumerate(tmp_joints.items()):
            v210_shapes.append(
                kind.straight_shape(
                    i + 1,
                    stb_v2_1_0.StbSecSteelBeamStraight(
                        shape=joint.shape_or_none,
                        strength_main=joint.strength_main_or_none,
                        strength_web=joint.strength_web_or_none,
                    ),
                )
            )
        kind.set_figure(v210_sec_beam_s, v210_shapes)
        return


def stb_sec_steel_figure_beam_s_haunch_to_v210[
    TShape: StBridgeElement,
    TSection: HasId,
](
    figure: SteelFigure | None,
    id_section: int,
    v202_girders: list[stb_v2_0_2.StbGirder],
    v202_beams: list[stb_v2_0_2.StbBeam],
    v210_girders: list[stb_v2_1_0.StbGirder],
    v210_beams: list[stb_v2_1_0.StbBeam],
    v210_sec_beam_s_list: list[TSection],
    ng_section_id: set[int],
    *,
    kind: SteelBeamKind[TShape, TSection],
    reporter: Reporter,
) -> None:
    if figure is None:
        return
    if not figure.haunches:
        return

    def _invalidate_target_beams() -> None:
        for v202_beam, v210_beam in zip(
            v202_girders_and_beams, v210_girders_and_beams, strict=False
        ):
            if v202_beam.id_section != id_section:
                continue
            if isinstance(v210_beam, stb_v2_1_0.StbGirder):
                v210_beam.stb_girder_steel_switch.clear()
            if isinstance(v210_beam, stb_v2_1_0.StbBeam):
                v210_beam.stb_beam_steel_switch.clear()
            if v210_beam.id_section_or_none is not None:
                ng_section_id.add(v210_beam.id_section)
            v210_beam.id_section_or_none = None

    v202_girders_and_beams: list[stb_v2_0_2.StbGirder | stb_v2_0_2.StbBeam] = (
        v202_girders + v202_beams
    )
    v210_girders_and_beams: list[stb_v2_1_0.StbGirder | stb_v2_1_0.StbBeam] = (
        v210_girders + v210_beams
    )

    v202_haunches: Sequence[HasShapeAndStrengthAndPos] = figure.haunches
    if len(v202_haunches) < 2 or len(v202_haunches) > 3:
        reporter.warning(
            message="haunchの回数がスキーマ違反のため変換できません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.UPGRADE,
            stb_element=figure.original_element,
        )
        _invalidate_target_beams()
        return
    haunch_start: HasShapeAndStrengthAndPos | None = None
    with contextlib.suppress(StopIteration):
        haunch_start = next(haunch for haunch in v202_haunches if haunch.pos == "START")
    try:
        haunch_center: HasShapeAndStrengthAndPos = next(
            haunch for haunch in v202_haunches if haunch.pos == "CENTER"
        )
    except StopIteration:
        reporter.warning(
            message="pos=CENTERが使われていません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.UPGRADE,
            stb_element=figure.original_element,
        )
        _invalidate_target_beams()
        return
    haunch_end: HasShapeAndStrengthAndPos | None = None
    with contextlib.suppress(StopIteration):
        haunch_end = next(haunch for haunch in v202_haunches if haunch.pos == "END")
    if not haunch_start and not haunch_end:
        reporter.warning(
            message=f"{figure.original_element._name_for_log()}posがSTARTもENDも使われていません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.UPGRADE,
            stb_element=figure.original_element,
        )
        _invalidate_target_beams()
        return

    v202_target_beams_dict: dict[
        tuple[str, str], list[stb_v2_0_2.StbGirder | stb_v2_0_2.StbBeam]
    ] = {}
    v210_target_beams_dict: dict[
        tuple[str, str], list[stb_v2_1_0.StbGirder | stb_v2_1_0.StbBeam]
    ] = {}
    for v202_beam, v210_beam in zip(
        v202_girders_and_beams, v210_girders_and_beams, strict=False
    ):
        if v202_beam.id_section != id_section:
            continue
        key = (
            v202_beam.kind_haunch_start_or_none or "SLOPE",
            v202_beam.kind_haunch_end_or_none or "SLOPE",
        )
        v202_target_beams: list[stb_v2_0_2.StbGirder | stb_v2_0_2.StbBeam] = (
            v202_target_beams_dict.setdefault(key, [])
        )
        v210_target_beams: list[stb_v2_1_0.StbGirder | stb_v2_1_0.StbBeam] = (
            v210_target_beams_dict.setdefault(key, [])
        )
        v202_target_beams.append(v202_beam)
        v210_target_beams.append(v210_beam)

    for kind_index, haunch_kind in enumerate(v202_target_beams_dict):
        v210_shapes: list[TShape] = []
        v210_target_beams = v210_target_beams_dict[haunch_kind]
        order: int = 1
        if haunch_start:
            if haunch_kind[0] == "DROP":
                v210_shapes.append(
                    kind.straight_shape(
                        order,
                        stb_v2_1_0.StbSecSteelBeamStraight(
                            shape=haunch_start.shape_or_none,
                            strength_main=haunch_start.strength_main_or_none,
                            strength_web=haunch_start.strength_web_or_none,
                        ),
                    )
                )
            else:
                v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                    start_shape=haunch_start.shape_or_none,
                    end_shape=haunch_center.shape_or_none,
                    strength_main=haunch_start.strength_main_or_none,
                    strength_web=haunch_start.strength_web_or_none,
                )
                v210_shapes.append(kind.taper_shape(order, v210_taper))
            order += 1
        v210_shapes.append(
            kind.straight_shape(
                order,
                stb_v2_1_0.StbSecSteelBeamStraight(
                    shape=haunch_center.shape_or_none,
                    strength_main=haunch_center.strength_main_or_none,
                    strength_web=haunch_center.strength_web_or_none,
                ),
            )
        )
        order += 1
        if haunch_end:
            if haunch_kind[1] == "DROP":
                v210_shapes.append(
                    kind.straight_shape(
                        order,
                        stb_v2_1_0.StbSecSteelBeamStraight(
                            shape=haunch_end.shape_or_none,
                            strength_main=haunch_end.strength_main_or_none,
                            strength_web=haunch_end.strength_web_or_none,
                        ),
                    )
                )
            else:
                v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                    start_shape=haunch_center.shape_or_none,
                    end_shape=haunch_end.shape_or_none,
                    strength_main=haunch_end.strength_main_or_none,
                    strength_web=haunch_end.strength_web_or_none,
                )
                v210_shapes.append(kind.taper_shape(order, v210_taper))
        v210_sec_beam_s = next(
            (s for s in v210_sec_beam_s_list if s.id == id_section), None
        )
        if kind_index > 0 and v210_sec_beam_s is not None:
            new_id_section: int = max(s.id for s in v210_sec_beam_s_list) + 1
            v210_sec_beam_s = copy.deepcopy(v210_sec_beam_s)
            v210_sec_beam_s.id = new_id_section
            v210_sec_beam_s.guid = uuid.uuid4()
            kind.set_figure(v210_sec_beam_s, v210_shapes)
            v210_sec_beam_s_list.append(v210_sec_beam_s)
            for v210_target_beam in v210_target_beams:
                v210_target_beam.id_section = new_id_section
        elif v210_sec_beam_s is not None:
            kind.set_figure(v210_sec_beam_s, v210_shapes)


def get_haunch_edge_shape(
    v210_sec_steel: stb_v2_1_0.StbSecSteel,
    repo_sec_steel: RepositoryV2_1_0,
    shape_out_name: str | None,
    shape_in_name: str | None,
) -> stb_v2_1_0.StbSecBuildH | stb_v2_1_0.StbSecBuildBox | None:
    if shape_out_name is None or shape_in_name is None:
        return None
    shape_out = repo_sec_steel.get_steel(shape_out_name)
    shape_in = repo_sec_steel.get_steel(shape_in_name)
    if isinstance(
        shape_out, (stb_v2_1_0.StbSecRollH, stb_v2_1_0.StbSecBuildH)
    ) and isinstance(shape_in, (stb_v2_1_0.StbSecRollH, stb_v2_1_0.StbSecBuildH)):
        bh: stb_v2_1_0.StbSecBuildH = stb_v2_1_0.StbSecBuildH(
            name=f"out_shape_{shape_out_name}_in_shape_{shape_in_name}",
            a=shape_in.a_or_none,
            b=shape_in.b_or_none,
            t1=shape_out.t1_or_none,
            t2=shape_out.t2_or_none,
        )
        exist_bh: stb_v2_1_0.StbSecBuildH | None = repo_sec_steel.find_equivalent(
            bh, exclude_fields=["name"]
        )
        if exist_bh is not None:
            return exist_bh
        else:
            v210_sec_steel.stb_sec_build_h.append(bh)
            repo_sec_steel.refresh()
            return bh
    elif isinstance(shape_out, (stb_v2_1_0.StbSecRollBox)) and isinstance(
        shape_in, (stb_v2_1_0.StbSecRollBox, stb_v2_1_0.StbSecBuildBox)
    ):
        bb: stb_v2_1_0.StbSecBuildBox = stb_v2_1_0.StbSecBuildBox(
            name=f"out_shape_{shape_out_name}_in_shape_{shape_in_name}",
            a=shape_in.a_or_none,
            b=shape_in.b_or_none,
            t1=shape_out.t_or_none,
            t2=shape_out.t_or_none,
        )
        exist_bb: stb_v2_1_0.StbSecBuildBox | None = repo_sec_steel.find_equivalent(
            bb, exclude_fields=["name"]
        )
        if exist_bb is not None:
            return exist_bb
        else:
            v210_sec_steel.stb_sec_build_box.append(bb)
            repo_sec_steel.refresh()
            return bb
    elif isinstance(shape_out, (stb_v2_1_0.StbSecBuildBox)) and isinstance(
        shape_in, (stb_v2_1_0.StbSecRollBox, stb_v2_1_0.StbSecBuildBox)
    ):
        bb = stb_v2_1_0.StbSecBuildBox(
            name=f"out_shape_{shape_out_name}_in_shape_{shape_in_name}",
            a=shape_in.a_or_none,
            b=shape_in.b_or_none,
            t1=shape_out.t1_or_none,
            t2=shape_out.t2_or_none,
        )
        exist_bb = repo_sec_steel.find_equivalent(bb, exclude_fields=["name"])
        if exist_bb is not None:
            return exist_bb
        else:
            v210_sec_steel.stb_sec_build_box.append(bb)
            repo_sec_steel.refresh()
            return bb
    else:
        return None


def stb_sec_steel_figure_beam_s_five_types_to_v210[
    TShape: StBridgeElement,
    TSection: HasId,
](
    figure: SteelFigure | None,
    id_section: int,
    v202_girders: list[stb_v2_0_2.StbGirder],
    v202_beams: list[stb_v2_0_2.StbBeam],
    v210_girders: list[stb_v2_1_0.StbGirder],
    v210_beams: list[stb_v2_1_0.StbBeam],
    v210_sec_beam_s_list: list[TSection],
    v210_sec_steel: stb_v2_1_0.StbSecSteel,
    repo_sec_steel: RepositoryV2_1_0,
    ng_section_id: set[int],
    *,
    kind: SteelBeamKind[TShape, TSection],
    reporter: Reporter,
) -> None:
    if figure is None:
        return
    if not figure.five_types:
        return

    v202_girders_and_beams: list[stb_v2_0_2.StbGirder | stb_v2_0_2.StbBeam] = (
        v202_girders + v202_beams
    )
    v210_girders_and_beams: list[stb_v2_1_0.StbGirder | stb_v2_1_0.StbBeam] = (
        v210_girders + v210_beams
    )

    def _invalidate_target_beams() -> None:
        for v202_beam, v210_beam in zip(
            v202_girders_and_beams, v210_girders_and_beams, strict=False
        ):
            if v202_beam.id_section != id_section:
                continue
            if isinstance(v210_beam, stb_v2_1_0.StbGirder):
                v210_beam.stb_girder_steel_switch.clear()
            if isinstance(v210_beam, stb_v2_1_0.StbBeam):
                v210_beam.stb_beam_steel_switch.clear()
            if v210_beam.id_section_or_none is not None:
                ng_section_id.add(v210_beam.id_section)
            v210_beam.id_section_or_none = None

    v202_five_types_list: Sequence[HasShapeAndStrengthAndPos] = figure.five_types
    if len(v202_five_types_list) < 3 or len(v202_five_types_list) > 5:
        reporter.warning(
            message="StbSecSteelBeam_S_FiveTypesの回数がスキーマ違反のため変換できません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.UPGRADE,
            stb_element=figure.original_element,
        )
        _invalidate_target_beams()
        return
    pos_choices: tuple[str, str, str, str, str] = (
        "START",
        "CENTER",
        "END",
        "HAUNCH_S",
        "HAUNCH_E",
    )
    five_types_dict: dict[str, HasShapeAndStrengthAndPos] = {}
    for pos in pos_choices:
        with contextlib.suppress(StopIteration):
            five_types_dict[pos] = next(
                five_types
                for five_types in v202_five_types_list
                if five_types.pos == pos
            )

    five_types_start: HasShapeAndStrengthAndPos | None = five_types_dict.get("START")
    five_types_center: HasShapeAndStrengthAndPos | None = five_types_dict.get("CENTER")
    five_types_end: HasShapeAndStrengthAndPos | None = five_types_dict.get("END")
    five_types_haunch_s: HasShapeAndStrengthAndPos | None = five_types_dict.get(
        "HAUNCH_S"
    )
    five_types_haunch_e: HasShapeAndStrengthAndPos | None = five_types_dict.get(
        "HAUNCH_E"
    )
    if five_types_center is None:
        reporter.warning(
            message="pos=CENTERが使われていません",
            code=Code.SCHEMA_ERROR,
            phase=Phase.UPGRADE,
            stb_element=figure.original_element,
        )
        _invalidate_target_beams()
        return

    v202_target_beams_dict: dict[
        tuple[str, str, bool, bool, bool, bool, bool | None, bool | None],
        list[stb_v2_0_2.StbGirder | stb_v2_0_2.StbBeam],
    ] = {}
    v210_target_beams_dict: dict[
        tuple[str, str, bool, bool, bool, bool, bool | None, bool | None],
        list[stb_v2_1_0.StbGirder | stb_v2_1_0.StbBeam],
    ] = {}
    for v202_beam, v210_beam in zip(
        v202_girders_and_beams, v210_girders_and_beams, strict=False
    ):
        if v202_beam.id_section != id_section:
            continue
        is_joint_inside_haunch_start: bool | None = None
        if (
            v202_beam.joint_start_or_none is not None
            and v202_beam.haunch_start_or_none is not None
        ):
            is_joint_inside_haunch_start = (
                v202_beam.haunch_start < v202_beam.joint_start
            )
        is_joint_inside_haunch_end: bool | None = None
        if (
            v202_beam.joint_end_or_none is not None
            and v202_beam.haunch_end_or_none is not None
        ):
            is_joint_inside_haunch_end = v202_beam.haunch_end < v202_beam.joint_end
        has_haunch_length_start: bool = v202_beam.haunch_start_or_none is not None
        has_joint_length_start: bool = v202_beam.joint_start_or_none is not None
        has_haunch_length_end: bool = v202_beam.haunch_end_or_none is not None
        has_joint_length_end: bool = v202_beam.joint_end_or_none is not None

        key = (
            v202_beam.kind_haunch_start_or_none or "SLOPE",
            v202_beam.kind_haunch_end_or_none or "SLOPE",
            has_haunch_length_start,
            has_joint_length_start,
            has_haunch_length_end,
            has_joint_length_end,
            is_joint_inside_haunch_start,
            is_joint_inside_haunch_end,
        )
        v202_target_beams: list[stb_v2_0_2.StbGirder | stb_v2_0_2.StbBeam] = (
            v202_target_beams_dict.setdefault(key, [])
        )
        v210_target_beams: list[stb_v2_1_0.StbGirder | stb_v2_1_0.StbBeam] = (
            v210_target_beams_dict.setdefault(key, [])
        )
        v202_target_beams.append(v202_beam)
        v210_target_beams.append(v210_beam)

    kind_index: int = 0
    for beam_kind in v202_target_beams_dict:
        v202_target_beams = v202_target_beams_dict[beam_kind]
        (
            kind_hanuch_start,
            kind_hanuch_end,
            has_haunch_length_start,
            has_joint_length_start,
            has_haunch_length_end,
            has_joint_length_end,
            is_joint_inside_haunch_start,
            is_joint_inside_haunch_end,
        ) = beam_kind
        v210_shapes: list[TShape] = []
        v210_target_beams = v210_target_beams_dict[beam_kind]
        try:
            order: int = 1
            if has_haunch_length_start and has_joint_length_start:
                if is_joint_inside_haunch_start is None:
                    raise AssertionError("到達しないはずのコードに到達しました")
                if five_types_start is None or five_types_haunch_s is None:
                    raise SchemaError("五断面の定義が不十分です")
                if is_joint_inside_haunch_start:
                    if kind_hanuch_start == "DROP":
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_start.shape_or_none,
                                    strength_main=five_types_start.strength_main_or_none,
                                    strength_web=five_types_start.strength_web_or_none,
                                ),
                            )
                        )
                        order += 1
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_haunch_s.shape_or_none,
                                    strength_main=five_types_haunch_s.strength_main_or_none,
                                    strength_web=five_types_haunch_s.strength_web_or_none,
                                ),
                            )
                        )
                    else:
                        v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                            start_shape=five_types_start.shape_or_none,
                            end_shape=five_types_haunch_s.shape_or_none,
                            strength_main=five_types_start.strength_main_or_none,
                            strength_web=five_types_start.strength_web_or_none,
                        )
                        v210_shapes.append(kind.taper_shape(order, v210_taper))
                        order += 1
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_haunch_s.shape_or_none,
                                    strength_main=five_types_haunch_s.strength_main_or_none,
                                    strength_web=five_types_haunch_s.strength_web_or_none,
                                ),
                            )
                        )
                else:
                    if kind_hanuch_start == "DROP":
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_start.shape_or_none,
                                    strength_main=five_types_start.strength_main_or_none,
                                    strength_web=five_types_start.strength_web_or_none,
                                ),
                            )
                        )
                        order += 1
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_haunch_s.shape_or_none,
                                    strength_main=five_types_haunch_s.strength_main_or_none,
                                    strength_web=five_types_haunch_s.strength_web_or_none,
                                ),
                            )
                        )
                        order += 1
                    else:
                        edge_shape_start = get_haunch_edge_shape(
                            v210_sec_steel,
                            repo_sec_steel,
                            five_types_start.shape_or_none,
                            five_types_haunch_s.shape_or_none,
                        )
                        edge_shape_start_name: str | None = (
                            edge_shape_start.name
                            if edge_shape_start is not None
                            else five_types_haunch_s.shape_or_none
                        )
                        v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                            start_shape=five_types_start.shape_or_none,
                            end_shape=edge_shape_start_name,
                            strength_main=five_types_haunch_s.strength_main_or_none,
                            strength_web=five_types_haunch_s.strength_web_or_none,
                        )
                        v210_shapes.append(kind.taper_shape(order, v210_taper))
                        order += 1
                        v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                            start_shape=five_types_haunch_s.shape_or_none,
                            end_shape=five_types_center.shape_or_none,
                            strength_main=five_types_haunch_s.strength_main_or_none,
                            strength_web=five_types_haunch_s.strength_web_or_none,
                        )
                        v210_shapes.append(kind.taper_shape(order, v210_taper))
                        order += 1
            elif has_haunch_length_start:
                if five_types_start is None:
                    raise SchemaError("五断面の定義が不十分です")
                if kind_hanuch_start == "DROP":
                    v210_shapes.append(
                        kind.straight_shape(
                            order,
                            stb_v2_1_0.StbSecSteelBeamStraight(
                                shape=five_types_start.shape_or_none,
                                strength_main=five_types_start.strength_main_or_none,
                                strength_web=five_types_start.strength_web_or_none,
                            ),
                        )
                    )
                    order += 1
                else:
                    v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                        start_shape=five_types_start.shape_or_none,
                        end_shape=five_types_center.shape_or_none,
                        strength_main=five_types_start.strength_main_or_none,
                        strength_web=five_types_start.strength_web_or_none,
                    )
                    v210_shapes.append(kind.taper_shape(order, v210_taper))
                    order += 1
            elif has_joint_length_start:
                if five_types_start is None:
                    raise SchemaError("五断面の定義が不十分です")
                v210_shapes.append(
                    kind.straight_shape(
                        order,
                        stb_v2_1_0.StbSecSteelBeamStraight(
                            shape=five_types_start.shape_or_none,
                            strength_main=five_types_start.strength_main_or_none,
                            strength_web=five_types_start.strength_web_or_none,
                        ),
                    )
                )
                order += 1
            else:
                pass

            v210_shapes.append(
                kind.straight_shape(
                    order,
                    stb_v2_1_0.StbSecSteelBeamStraight(
                        shape=five_types_center.shape_or_none,
                        strength_main=five_types_center.strength_main_or_none,
                        strength_web=five_types_center.strength_web_or_none,
                    ),
                )
            )
            order += 1

            if has_haunch_length_end and has_joint_length_end:
                if is_joint_inside_haunch_end is None:
                    raise AssertionError("到達しないはずのコードに到達しました")
                if five_types_end is None or five_types_haunch_e is None:
                    raise SchemaError("五断面の定義が不十分です")
                if is_joint_inside_haunch_end:
                    if kind_hanuch_end == "DROP":
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_haunch_e.shape_or_none,
                                    strength_main=five_types_haunch_e.strength_main_or_none,
                                    strength_web=five_types_haunch_e.strength_web_or_none,
                                ),
                            )
                        )
                        order += 1
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_end.shape_or_none,
                                    strength_main=five_types_end.strength_main_or_none,
                                    strength_web=five_types_end.strength_web_or_none,
                                ),
                            )
                        )
                        order += 1
                    else:
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_haunch_e.shape_or_none,
                                    strength_main=five_types_haunch_e.strength_main_or_none,
                                    strength_web=five_types_haunch_e.strength_web_or_none,
                                ),
                            )
                        )
                        order += 1
                        v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                            start_shape=five_types_haunch_e.shape_or_none,
                            end_shape=five_types_end.shape_or_none,
                            strength_main=five_types_end.strength_main_or_none,
                            strength_web=five_types_end.strength_web_or_none,
                        )
                        v210_shapes.append(kind.taper_shape(order, v210_taper))
                        order += 1
                else:
                    if kind_hanuch_end == "DROP":
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_haunch_e.shape_or_none,
                                    strength_main=five_types_haunch_e.strength_main_or_none,
                                    strength_web=five_types_haunch_e.strength_web_or_none,
                                ),
                            )
                        )
                        order += 1
                        v210_shapes.append(
                            kind.straight_shape(
                                order,
                                stb_v2_1_0.StbSecSteelBeamStraight(
                                    shape=five_types_end.shape_or_none,
                                    strength_main=five_types_end.strength_main_or_none,
                                    strength_web=five_types_end.strength_web_or_none,
                                ),
                            )
                        )
                    else:
                        v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                            start_shape=five_types_center.shape_or_none,
                            end_shape=five_types_haunch_e.shape_or_none,
                            strength_main=five_types_haunch_e.strength_main_or_none,
                            strength_web=five_types_haunch_e.strength_web_or_none,
                        )
                        v210_shapes.append(kind.taper_shape(order, v210_taper))
                        order += 1

                        edge_shape_end = get_haunch_edge_shape(
                            v210_sec_steel,
                            repo_sec_steel,
                            five_types_end.shape_or_none,
                            five_types_haunch_e.shape_or_none,
                        )
                        edge_shape_end_name: str | None = (
                            edge_shape_end.name
                            if edge_shape_end is not None
                            else five_types_haunch_e.shape_or_none
                        )
                        v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                            start_shape=edge_shape_end_name,
                            end_shape=five_types_end.shape_or_none,
                            strength_main=five_types_end.strength_main_or_none,
                            strength_web=five_types_end.strength_web_or_none,
                        )
                        v210_shapes.append(kind.taper_shape(order, v210_taper))
                        order += 1
            elif has_haunch_length_end:
                if five_types_end is None:
                    raise SchemaError("五断面の定義が不十分です")
                if kind_hanuch_end == "DROP":
                    v210_shapes.append(
                        kind.straight_shape(
                            order,
                            stb_v2_1_0.StbSecSteelBeamStraight(
                                shape=five_types_end.shape_or_none,
                                strength_main=five_types_end.strength_main_or_none,
                                strength_web=five_types_end.strength_web_or_none,
                            ),
                        )
                    )
                    order += 1
                else:
                    v210_taper = stb_v2_1_0.StbSecSteelBeamTaper(
                        start_shape=five_types_center.shape_or_none,
                        end_shape=five_types_end.shape_or_none,
                        strength_main=five_types_end.strength_main_or_none,
                        strength_web=five_types_end.strength_web_or_none,
                    )
                    v210_shapes.append(kind.taper_shape(order, v210_taper))
                    order += 1
            elif has_joint_length_end:
                if five_types_end is None:
                    raise SchemaError("五断面の定義が不十分です")
                v210_shapes.append(
                    kind.straight_shape(
                        order,
                        stb_v2_1_0.StbSecSteelBeamStraight(
                            shape=five_types_end.shape_or_none,
                            strength_main=five_types_end.strength_main_or_none,
                            strength_web=five_types_end.strength_web_or_none,
                        ),
                    )
                )
                order += 1
            else:
                pass

            v210_sec_beam_s = next(
                (s for s in v210_sec_beam_s_list if s.id == id_section), None
            )
            if kind_index > 0 and v210_sec_beam_s is not None:
                new_id_section: int = max(s.id for s in v210_sec_beam_s_list) + 1
                v210_sec_beam_s = copy.deepcopy(v210_sec_beam_s)
                v210_sec_beam_s.id = new_id_section
                v210_sec_beam_s.guid = uuid.uuid4()
                kind.set_figure(v210_sec_beam_s, v210_shapes)
                v210_sec_beam_s_list.append(v210_sec_beam_s)
                for v210_target_beam in v210_target_beams:
                    v210_target_beam.id_section = new_id_section
            elif v210_sec_beam_s is not None:
                kind.set_figure(v210_sec_beam_s, v210_shapes)
            kind_index += 1
        except SchemaError as e:
            reporter.warning(
                message="StbSecSteelBeam_S_FiveTypesの変換中に"
                f"エラーが発生しました: {e}",
                code=Code.UNEXPECTED_ERROR,
                phase=Phase.UPGRADE,
                stb_element=figure.original_element,
            )
            _invalidate_target_beams()


def _post_sec_beam_steel[
    TShape: StBridgeElement,
    TSection: HasId,
    TSectionFrom: HasId,
](
    v202: stb_v2_0_2.StBridge,
    v210: stb_v2_1_0.StBridge,
    *,
    kind: SteelBeamKind[TShape, TSection],
    sections_from: Callable[[stb_v2_0_2.StbSections], list[TSectionFrom]],
    sections_to: Callable[[stb_v2_1_0.StbSections], list[TSection]],
    to_figure: Callable[[TSectionFrom], SteelFigure | None],
    ng_section_id: set[int],
    post: Callable[[stb_v2_1_0.StBridge], None] | None = None,
    reporter: Reporter,
) -> None:
    try:
        v210_sec_steel: stb_v2_1_0.StbSecSteel = (
            v210.stb_model.stb_sections.stb_sec_steel
        )
    except NoneAccessError:
        return
    v202_s_b_s_list: list[TSectionFrom] | None = None
    v210_s_b_s_list: list[TSection] | None = None
    try:
        v202_s_b_s_list = sections_from(v202.stb_model.stb_sections)
        v210_s_b_s_list = sections_to(v210.stb_model.stb_sections)
    except NoneAccessError:
        pass
    try:
        v202_girders: list[stb_v2_0_2.StbGirder] = (
            v202.stb_model.stb_members.stb_girders.stb_girder
        )
        v210_girders: list[stb_v2_1_0.StbGirder] = (
            v210.stb_model.stb_members.stb_girders.stb_girder
        )
    except NoneAccessError:
        v202_girders = []
        v210_girders = []
    try:
        v202_beams: list[stb_v2_0_2.StbBeam] = (
            v202.stb_model.stb_members.stb_beams.stb_beam
        )
        v210_beams: list[stb_v2_1_0.StbBeam] = (
            v210.stb_model.stb_members.stb_beams.stb_beam
        )
    except NoneAccessError:
        v202_beams = []
        v210_beams = []
    repo_sec_steel: RepositoryV2_1_0 = RepositoryV2_1_0(v210_sec_steel)
    if v202_s_b_s_list and v210_s_b_s_list:
        for i, v202_s_b_s in enumerate(v202_s_b_s_list):
            v210_s_b_s = v210_s_b_s_list[i]
            figure = to_figure(v202_s_b_s)
            stb_sec_steel_figure_beam_s_to_v210(
                figure,
                v202_s_b_s.id,
                v210_s_b_s_list,
                kind,
                reporter=reporter,
            )
            stb_sec_steel_figure_beam_s_haunch_to_v210(
                figure,
                v210_s_b_s.id,
                v202_girders=v202_girders,
                v202_beams=v202_beams,
                v210_girders=v210_girders,
                v210_beams=v210_beams,
                v210_sec_beam_s_list=v210_s_b_s_list,
                ng_section_id=ng_section_id,
                kind=kind,
                reporter=reporter,
            )
            stb_sec_steel_figure_beam_s_five_types_to_v210(
                figure,
                v210_s_b_s.id,
                v202_girders=v202_girders,
                v202_beams=v202_beams,
                v210_girders=v210_girders,
                v210_beams=v210_beams,
                v210_sec_beam_s_list=v210_s_b_s_list,
                v210_sec_steel=v210_sec_steel,
                repo_sec_steel=repo_sec_steel,
                kind=kind,
                reporter=reporter,
                ng_section_id=ng_section_id,
            )
        if post is not None:
            post(v210)


def post_sec_beam_s(
    v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge, *, reporter: Reporter
) -> None:
    ng_section_id: set[int] = set()
    _post_sec_beam_steel(
        v202,
        v210,
        kind=BEAM_KIND_S,
        ng_section_id=ng_section_id,
        sections_from=lambda sections: sections.stb_sec_beam_s,
        sections_to=lambda sections: sections.stb_sec_beam_s,
        to_figure=lambda section: (
            SteelFigure(
                original_element=section.stb_sec_steel_figure_beam_s,
                straight=section.stb_sec_steel_figure_beam_s.stb_sec_steel_beam_s_straight_or_none,
                tapers=section.stb_sec_steel_figure_beam_s.stb_sec_steel_beam_s_taper,
                joints=section.stb_sec_steel_figure_beam_s.stb_sec_steel_beam_s_joint,
                haunches=section.stb_sec_steel_figure_beam_s.stb_sec_steel_beam_s_haunch,
                five_types=section.stb_sec_steel_figure_beam_s.stb_sec_steel_beam_s_five_types,
            )
            if section.stb_sec_steel_figure_beam_s_or_none is not None
            else None
        ),
        reporter=reporter,
    )

    if ng_section_id:
        v210.stb_model.stb_sections.stb_sec_beam_s = [
            stb_sec_beam_s
            for stb_sec_beam_s in v210.stb_model.stb_sections.stb_sec_beam_s
            if stb_sec_beam_s.id_or_none not in ng_section_id
        ]


def _set_src_s_vertical_offset(
    v210: stb_v2_1_0.StBridge, *, reporter: Reporter
) -> None:
    """SRC梁の鉄骨位置を下げる。

    TODO:
        鉄骨の位置を一律-150にしているので、見直しが必要
    """
    for v210_sec_beam in v210.stb_model.stb_sections.stb_sec_beam_src:
        figure_beam = v210_sec_beam.stb_sec_steel_figure_beam_src_or_none
        if figure_beam is None:
            continue
        for shape in figure_beam.stb_sec_steel_beam_src_shape:
            if shape.stb_sec_steel_beam_straight_or_none is not None:
                shape.stb_sec_steel_beam_straight.vertical_offset = -150.0
                reporter.warning(
                    message="SRC梁の上下方向オフセットは仮定として-150.0を設定しました",
                    code=Code.NOT_IMPLEMENTED,
                    phase=Phase.UPGRADE,
                    stb_element=shape.stb_sec_steel_beam_straight,
                    attr_name="vertical_offset",
                )
            if shape.stb_sec_steel_beam_taper_or_none is not None:
                shape.stb_sec_steel_beam_taper.start_vertical_offset = -150.0
                shape.stb_sec_steel_beam_taper.end_vertical_offset = -150.0
                reporter.warning(
                    message="SRC梁の上下方向オフセットは仮定として-150.0を設定しました",
                    code=Code.NOT_IMPLEMENTED,
                    phase=Phase.UPGRADE,
                    stb_element=shape.stb_sec_steel_beam_taper,
                    attr_name="start_vertical_offset",
                )
                reporter.warning(
                    message="SRC梁の上下方向オフセットは仮定として-150.0を設定しました",
                    code=Code.NOT_IMPLEMENTED,
                    phase=Phase.UPGRADE,
                    stb_element=shape.stb_sec_steel_beam_taper,
                    attr_name="end_vertical_offset",
                )


def post_sec_beam_src_s(
    v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge, *, reporter: Reporter
) -> None:
    ng_section_id: set[int] = set()
    _post_sec_beam_steel(
        v202,
        v210,
        kind=BEAM_KIND_SRC,
        ng_section_id=ng_section_id,
        sections_from=lambda sections: sections.stb_sec_beam_src,
        sections_to=lambda sections: sections.stb_sec_beam_src,
        to_figure=lambda section: (
            SteelFigure(
                original_element=section.stb_sec_steel_figure_beam_src,
                straight=section.stb_sec_steel_figure_beam_src.stb_sec_steel_beam_src_straight_or_none,
                tapers=section.stb_sec_steel_figure_beam_src.stb_sec_steel_beam_src_taper,
                joints=section.stb_sec_steel_figure_beam_src.stb_sec_steel_beam_src_joint,
                haunches=section.stb_sec_steel_figure_beam_src.stb_sec_steel_beam_src_haunch,
                five_types=section.stb_sec_steel_figure_beam_src.stb_sec_steel_beam_src_five_types,
            )
            if section.stb_sec_steel_figure_beam_src_or_none is not None
            else None
        ),
        post=lambda stb: _set_src_s_vertical_offset(stb, reporter=reporter),
        reporter=reporter,
    )
    if ng_section_id:
        v210.stb_model.stb_sections.stb_sec_beam_src = [
            stb_sec_beam_src
            for stb_sec_beam_src in v210.stb_model.stb_sections.stb_sec_beam_src
            if stb_sec_beam_src.id_or_none not in ng_section_id
        ]
