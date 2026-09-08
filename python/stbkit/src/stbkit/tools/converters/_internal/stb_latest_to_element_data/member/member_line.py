# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Literal

from stbkit.core.stb_exceptions import (
    ReferenceElementNotFoundError,
    SchemaError,
)
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbBeam,
    StbBeamConcreteSwitch,
    StbBeamSteelSwitch,
    StbBrace,
    StbColumn,
    StbFoundationColumn,
    StbGirder,
    StbGirderConcreteSwitch,
    StbGirderSteelSwitch,
    StbParapet,
    StbPile,
    StbPost,
    StbSecPileS,
    StbStripFooting,
)

from ....._internal.data_model.element_data import (
    ElementLine,
    ElementLineSrc,
    ElementType,
)
from ....._internal.data_model.shape_data import ShapePair, ShapePosition
from ....._internal.utils import girder_utils
from ....._internal.vectors import Vector3d
from ... import coord_converter, name_converter
from ..section import sec, sec_pile_s
from . import member_pile


def get_axis_position(
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
) -> ShapePosition:
    match stb_element:
        case StbColumn() | StbPost() | StbBrace() | StbPile() | StbFoundationColumn():
            return ShapePosition.CENTER_CENTER
        case StbGirder() | StbBeam():
            return ShapePosition.TOP_CENTER
        case StbStripFooting() | StbParapet():
            return ShapePosition.BOTTOM_CENTER
        case _:
            raise AssertionError(
                type(stb_element).__name__ + "は想定外の部材タイプです"
            )


def get_element_type(
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
) -> ElementType:
    match stb_element:
        case StbColumn():
            return ElementType.COLUMN
        case StbPost():
            return ElementType.POST
        case StbGirder():
            return ElementType.GIRDER
        case StbBeam():
            return ElementType.BEAM
        case StbBrace():
            return ElementType.BRACE
        case StbStripFooting():
            return ElementType.STRIP_FOOTING
        case StbPile():
            return ElementType.PILE
        case StbFoundationColumn():
            return ElementType.FOUNDATION_COLUMN
        case StbParapet():
            return ElementType.PARAPET
        case _:
            raise AssertionError("想定外の部材タイプです")


def get_node_ids(
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
) -> list[int]:
    match stb_element:
        case StbColumn() | StbPost():
            return [stb_element.id_node_bottom, stb_element.id_node_top]
        case StbGirder() | StbBeam() | StbBrace() | StbStripFooting() | StbParapet():
            return [stb_element.id_node_start, stb_element.id_node_end]
        case StbPile() | StbFoundationColumn():
            # 杭と基礎柱は1節点しか参照しないため1件リストにする
            return [stb_element.id_node]
        case _:
            raise AssertionError("想定外の部材タイプです")


def get_points(
    repo: RepositoryLatest,
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
    node_coords: dict[int, Vector3d],
    reporter: Reporter,
) -> tuple[Vector3d, Vector3d]:
    try:
        match stb_element:
            case StbColumn() | StbPost():
                point_start: Vector3d = node_coords[stb_element.id_node_bottom]
                point_end: Vector3d = node_coords[stb_element.id_node_top]
            case (
                StbGirder() | StbBeam() | StbBrace() | StbStripFooting() | StbParapet()
            ):
                point_start = node_coords[stb_element.id_node_start]
                point_end = node_coords[stb_element.id_node_end]
            case StbPile() as pile:
                offset_pile: Vector3d = Vector3d(
                    pile.offset_x_or_none or 0.0,
                    pile.offset_y_or_none or 0.0,
                    pile.level_top_or_none or 0.0,
                )
                point_end = node_coords[pile.id_node] + offset_pile
                length: float = pile.length_all_or_none or 0.0
                if pile.kind_structure_or_none == "S":
                    stb_sec_pile_s: StbSecPileS = repo.get(StbSecPileS, pile.id_section)
                    _, lengths = sec_pile_s.stb_sec_pile_s_to_shapes_and_length(
                        stb_sec_pile_s
                    )
                    length = sum(lengths)
                point_start = point_end - length * Vector3d.unit_z()
            case StbFoundationColumn() as foundation_column:
                point_base: Vector3d = node_coords[foundation_column.id_node]

                point_fd_top: Vector3d = point_base
                point_fd_bottom: Vector3d = (
                    point_fd_top
                    - (foundation_column.length_fd_or_none or 0.0) * Vector3d.unit_z()
                )
                point_start = point_fd_bottom
                point_end = point_fd_top
            case _:
                raise AssertionError("想定外の部材タイプです")
    except KeyError as e:
        reporter.error(
            message=f"節点が見つかりません: {e}",
            code=Code.REFERENCE_NOT_FOUND,
            phase=Phase.CONVERT_IFC,
            stb_element=stb_element,
            value=str(e),
        )
        return Vector3d.zero(), Vector3d.zero()

    return point_start, point_end


def get_offset(
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
    point_start: Vector3d,
    point_end: Vector3d,
) -> tuple[Vector3d, Vector3d]:
    offset_start: Vector3d
    offset_end: Vector3d
    match stb_element:
        case StbColumn() | StbPost():
            offset_start = Vector3d(
                stb_element.offset_bottom_x_or_none or 0.0,
                stb_element.offset_bottom_y_or_none or 0.0,
                stb_element.offset_bottom_z_or_none or 0.0,
            )
            offset_end = Vector3d(
                stb_element.offset_top_x_or_none or 0.0,
                stb_element.offset_top_y_or_none or 0.0,
                stb_element.offset_top_z_or_none or 0.0,
            )
        case StbGirder() | StbBeam():
            offset_start = girder_utils.girder_offset_start(stb_element)
            offset_end = girder_utils.girder_offset_end(stb_element)
        case StbBrace() as brace:
            offset_start = Vector3d(
                brace.aim_offset_start_x_or_none or 0.0,
                brace.aim_offset_start_y_or_none or 0.0,
                brace.aim_offset_start_z_or_none or 0.0,
            )
            offset_end = Vector3d(
                brace.aim_offset_end_x_or_none or 0.0,
                brace.aim_offset_end_y_or_none or 0.0,
                brace.aim_offset_end_z_or_none or 0.0,
            )
            if brace.cutback_start_or_none or brace.cutback_end_or_none:
                vx, vy, vz = coord_converter.axis_vector_beam(
                    point_start, point_end, 0.0
                )
                if brace.cutback_start_or_none:
                    offset_start += (brace.cutback_start_or_none or 0.0) * vx
                if brace.cutback_end_or_none:
                    offset_end -= (brace.cutback_end_or_none or 0.0) * vx
        case StbStripFooting() as stb_strip_footing:
            vx, vy, vz = coord_converter.axis_vector_beam(point_start, point_end, 0.0)
            strip_footing_base_offset: Vector3d = (
                stb_strip_footing.offset_or_none or 0.0
            ) * vy + (stb_strip_footing.level_or_none or 0.0) * vz
            offset_start = (
                -(stb_strip_footing.length_ex_start_or_none or 0.0) * vx
                + strip_footing_base_offset
            )
            offset_end = (
                stb_strip_footing.length_ex_end_or_none or 0.0
            ) * vx + strip_footing_base_offset
        case StbPile():
            return Vector3d.zero(), Vector3d.zero()
        case StbFoundationColumn() as foundation_column:
            if (
                foundation_column.id_section_fd_or_none is None
                or foundation_column.length_fd_or_none is None
            ):
                if (
                    foundation_column.offset_wr_x_or_none
                    or foundation_column.offset_wr_y_or_none
                ):
                    offset = Vector3d(
                        foundation_column.offset_wr_x_or_none or 0.0,
                        foundation_column.offset_wr_y_or_none or 0.0,
                        foundation_column.offset_z_or_none or 0.0,
                    )
                    offset_start = offset
                    offset_end = offset
                else:
                    offset = Vector3d(
                        0.0, 0.0, foundation_column.offset_z_or_none or 0.0
                    )
                    offset_start = offset
                    offset_end = offset
            else:
                offset = Vector3d(
                    foundation_column.offset_fd_x_or_none or 0.0,
                    foundation_column.offset_fd_y_or_none or 0.0,
                    foundation_column.offset_z_or_none or 0.0,
                )
                offset_start = offset
                offset_end = offset
        case StbParapet() as parapet:
            vx, vy, vz = coord_converter.axis_vector_beam(point_start, point_end, 0.0)
            offset_start = (parapet.offset_or_none or 0.0) * vy + (
                parapet.level_or_none or 0.0
            ) * vz
            offset_end = offset_start
        case _:
            raise AssertionError("想定外の部材タイプです")
    return offset_start, offset_end


def get_angle(
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
) -> float:
    match stb_element:
        case (
            StbColumn()
            | StbPost()
            | StbGirder()
            | StbBeam()
            | StbBrace()
            | StbFoundationColumn()
        ):
            return stb_element.rotate_or_none or 0.0
        case StbStripFooting() | StbPile() | StbParapet():
            return 0.0
        case _:
            raise AssertionError("想定外の部材タイプです")


def get_lengths(
    repo: RepositoryLatest,
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
    length: float,
    kind: Literal["S", "RC"],
) -> list[float]:
    lengths: list[float] = []
    match stb_element:
        case StbColumn() | StbPost():
            if kind == "S":
                if stb_element.steel_switch_height_bottom_or_none:
                    lengths.append(stb_element.steel_switch_height_bottom)
                if stb_element.steel_switch_height_top_or_none:
                    lengths.append(stb_element.steel_switch_height_top)
            lengths.insert(1, length - sum(lengths))
            return lengths
        case StbGirder() | StbBeam():
            switch: (
                list[StbGirderSteelSwitch]
                | list[StbGirderConcreteSwitch]
                | list[StbBeamSteelSwitch]
                | list[StbBeamConcreteSwitch]
            )
            match stb_element, kind:
                case StbGirder(), "S":
                    switch = stb_element.stb_girder_steel_switch
                case StbGirder(), "RC":
                    switch = stb_element.stb_girder_concrete_switch
                case StbBeam(), "S":
                    switch = stb_element.stb_beam_steel_switch
                case StbBeam(), "RC":
                    switch = stb_element.stb_beam_concrete_switch
            for i in range(len(switch)):
                value = switch[i].distance
                if i > 0:
                    value -= switch[i - 1].distance
                lengths.append(value)
            lengths.append(length - sum(lengths))
            return lengths
        case StbPile() as stb_pile:
            if kind == "RC":
                return member_pile.stb_pile_get_length_rc(repo, stb_pile)
            elif kind == "S":
                try:
                    stb_sec_pile_s: StbSecPileS = repo.get(
                        StbSecPileS, stb_pile.id_section
                    )
                    _, lengths = sec_pile_s.stb_sec_pile_s_to_shapes_and_length(
                        stb_sec_pile_s
                    )
                    return lengths
                except ReferenceElementNotFoundError:
                    raise SchemaError(
                        f"部材 {stb_pile._name_for_log()} の断面が見つかりません。",
                    )
            else:
                raise AssertionError("想定外の部材タイプです")
        case StbFoundationColumn() as foundation_column:
            if foundation_column.length_fd_or_none is not None:
                lengths.append(abs(foundation_column.length_fd))
            if foundation_column.length_wr_or_none is not None:
                lengths.append(abs(foundation_column.length_wr))
            return lengths
        case StbBrace() | StbStripFooting() | StbParapet():
            lengths.append(length)
            return lengths
        case _:
            raise AssertionError("想定外の部材タイプです")


def check_lengths(
    length: float,
    lengths: list[float],
    shapes: list[ShapePair],
    reporter: Reporter,
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
) -> list[float]:
    if len(shapes) != len(lengths):
        reporter.warning(
            message=f"{stb_element._name_for_log()} 断面切換位置の長さが"
            "取得できなかったため、等間隔に分割します",
            code=Code.MISSING_ATTRIBUTE,
            phase=Phase.CONVERT_IFC,
            stb_element=stb_element,
        )
        lengths = []
        for i in range(len(shapes)):
            lengths.append(length / len(shapes))
    return lengths


def stb_element_to_element_line(
    repo: RepositoryLatest,
    stb_element: StbColumn
    | StbPost
    | StbGirder
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
    node_coords: dict[int, Vector3d],
    reporter: Reporter,
) -> ElementLine | ElementLineSrc:
    axis_position: ShapePosition = get_axis_position(stb_element)
    element_type: ElementType = get_element_type(stb_element)
    node_ids: list[int] = get_node_ids(stb_element)
    point_start, point_end = get_points(
        repo, stb_element, node_coords, reporter=reporter
    )
    offset_start, offset_end = get_offset(stb_element, point_start, point_end)
    point_start += offset_start
    point_end += offset_end
    length: float = point_start.distance_to(point_end)
    lengths: list[float] = [length]
    angle: float = get_angle(stb_element)
    name: str = name_converter.stb_element_to_ifc_name(stb_element)
    shapes: list[ShapePair] | tuple[list[ShapePair], list[ShapePair]] | None = (
        sec.get_shapes_element_line(repo, stb_element, reporter)
    )
    if isinstance(shapes, tuple):
        shapes_rc, shapes_s = shapes
        lengths_s: list[float] = [length]
        lengths_rc: list[float] = [length]
        if shapes_s and shapes_s[0].start and len(shapes_s) > 1:
            lengths_s = get_lengths(repo, stb_element, length, kind="S")
        lengths_s = check_lengths(length, lengths_s, shapes_s, reporter, stb_element)
        if stb_element.kind_structure_or_none == "CFT":
            lengths_rc = lengths_s
        elif shapes_rc and shapes_rc[0].start and len(shapes_rc) > 1:
            lengths_rc = get_lengths(repo, stb_element, length, kind="RC")
        lengths_rc = check_lengths(length, lengths_rc, shapes_rc, reporter, stb_element)

        element_line_s: ElementLine = ElementLine(
            element_type=element_type,
            lengths=lengths_s,
            point_start=point_start,
            point_end=point_end,
            angle=angle,
            shapes=shapes_s if shapes_s is not None else [],
            axis_position=axis_position,
            path=stb_element._path_xml(),
            node_ids=node_ids,
        )
        element_line_rc: ElementLine = ElementLine(
            element_type=element_type,
            lengths=lengths_rc,
            point_start=point_start,
            point_end=point_end,
            angle=angle,
            shapes=shapes_rc if shapes_rc is not None else [],
            axis_position=axis_position,
            path=stb_element._path_xml(),
            node_ids=node_ids,
        )
        element_line_src: ElementLineSrc = ElementLineSrc(
            element_type=element_type,
            guid=stb_element.guid_or_none,
            name=name,
            rc=element_line_rc,
            steel=element_line_s,
            path=stb_element._path_xml(),
            node_ids=node_ids,
        )
        return element_line_src

    if shapes and shapes[0].start:
        kind_structure: str | None = stb_element.kind_structure_or_none
        if kind_structure == "UNDEFINED":
            lengths = [length]
        elif kind_structure == "RC" or kind_structure == "S":
            lengths = get_lengths(repo, stb_element, length, kind_structure)  # type: ignore[arg-type]
        else:
            reporter.warning(
                message=f"{kind_structure}は想定外の構造種別です。",
                code=Code.SCHEMA_ERROR,
                phase=Phase.CONVERT_IFC,
                stb_element=stb_element,
            )
            lengths = [length]
        lengths = check_lengths(length, lengths, shapes, reporter, stb_element)

    element_line: ElementLine = ElementLine(
        element_type=element_type,
        guid=stb_element.guid_or_none,
        lengths=lengths,
        point_start=point_start,
        point_end=point_end,
        angle=angle,
        shapes=shapes if shapes is not None else [],
        axis_position=axis_position,
        path=stb_element._path_xml(),
        node_ids=node_ids,
    )
    return element_line
