# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import (
    NoneAccessError,
    ReferenceElementNotFoundError,
    SchemaError,
)
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api import stb_latest
from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbBeam,
    StbBrace,
    StbColumn,
    StbFoundationColumn,
    StbGirder,
    StbParapet,
    StbPile,
    StbPost,
    StbSecBeamRc,
    StbSecBeamS,
    StbSecBeamSrc,
    StbSecBraceS,
    StbSecColumnCft,
    StbSecColumnRc,
    StbSecColumnS,
    StbSecColumnSrc,
    StbSecFoundationRc,
    StbSecParapetRc,
    StbSecPileRc,
    StbSecPileS,
    StbSecUndefined,
    StbStripFooting,
)

from ....._internal.constants import UNKNOWN_ELEMENT_SIZE_MM
from ....._internal.data_model.shape_data import (
    SHAPE_PAIRS_UNDEFINED,
    ShapePair,
)
from ....._internal.vectors import Vector2d
from . import (
    sec_beam_rc,
    sec_beam_s,
    sec_beam_src,
    sec_brace_s,
    sec_column_cft,
    sec_column_rc,
    sec_column_s,
    sec_column_src,
    sec_foundation,
    sec_parapet_rc,
    sec_pile_rc,
    sec_pile_s,
)


def get_shapes_element_line(
    repo: RepositoryLatest,
    ele: StbColumn
    | StbGirder
    | StbPost
    | StbBeam
    | StbBrace
    | StbStripFooting
    | StbPile
    | StbFoundationColumn
    | StbParapet,
    reporter: Reporter,
) -> list[ShapePair] | tuple[list[ShapePair], list[ShapePair]] | None:
    if isinstance(ele, StbFoundationColumn):
        foundation_column_shapes: list[ShapePair] = []
        if ele.id_section_fd_or_none is not None:
            try:
                section_fd: StbSecColumnRc = repo.get(StbSecColumnRc, ele.id_section_fd)
                shapes_fd: list[ShapePair] = sec_column_rc.stb_sec_column_rc_to_shapes(
                    section_fd
                )
                if shapes_fd:
                    foundation_column_shapes.extend(shapes_fd)
            except ReferenceElementNotFoundError:
                pass
        if ele.id_section_wr_or_none is not None:
            try:
                section_wr: StbSecColumnRc = repo.get(StbSecColumnRc, ele.id_section_wr)
                shapes_wr: list[ShapePair] = sec_column_rc.stb_sec_column_rc_to_shapes(
                    section_wr
                )
                if shapes_wr:
                    if (ele.offset_wr_x_or_none or ele.offset_wr_y_or_none) and (
                        ele.offset_fd_x_or_none or ele.offset_fd_y_or_none
                    ):
                        rotate: float = ele.rotate_or_none or 0.0
                        offset_fd: Vector2d = Vector2d(
                            ele.offset_fd_x_or_none or 0.0,
                            ele.offset_fd_y_or_none or 0.0,
                        )
                        offset_wr: Vector2d = Vector2d(
                            ele.offset_wr_x_or_none or 0.0,
                            ele.offset_wr_y_or_none or 0.0,
                        )
                        offset_wr = offset_wr.rotate(-rotate) - offset_fd.rotate(
                            -rotate
                        )
                        for item in shapes_wr:
                            item.start.offset = offset_wr
                            if item.end:
                                item.end.offset = offset_wr
                    foundation_column_shapes.extend(shapes_wr)
            except ReferenceElementNotFoundError:
                pass
        return foundation_column_shapes
    try:
        section: StBridgeElement = repo.deref(ele).id_section
    except ReferenceElementNotFoundError:
        return None
    except SchemaError:
        reporter.error(
            message="断面参照が不正です",
            code=Code.SCHEMA_ERROR,
            phase=Phase.CONVERT_GEOMETRY,
            stb_element=ele,
            attr_name="id_section",
        )
        return None
    match section:
        case StbSecColumnRc():
            return sec_column_rc.stb_sec_column_rc_to_shapes(section)
        case StbSecColumnS():
            return sec_column_s.stb_sec_column_s_to_shapes(repo, section, reporter)
        case StbSecColumnSrc():
            return sec_column_src.stb_sec_column_src_to_shapes(repo, section, reporter)
        case StbSecColumnCft():
            return sec_column_cft.stb_sec_column_cft_to_shapes(repo, section, reporter)
        case StbSecBeamRc():
            return sec_beam_rc.stb_sec_beam_rc_to_shapes(section)
        case StbSecBeamS():
            return sec_beam_s.stb_sec_beam_s_to_shapes(repo, section, reporter)
        case StbSecBeamSrc():
            return sec_beam_src.stb_sec_beam_src_to_shapes(repo, section, reporter)
        case StbSecBraceS():
            return sec_brace_s.stb_sec_brace_s_to_shapes(repo, section, reporter)
        case StbSecFoundationRc():
            shapes, _ = sec_foundation.stb_sec_foundation_rc_to_shapes_and_depth(
                section, reporter
            )
            return shapes
        case StbSecPileRc():
            return sec_pile_rc.stb_sec_pile_rc_to_shapes(section, reporter)
        case StbSecPileS():
            shapes, _ = sec_pile_s.stb_sec_pile_s_to_shapes_and_length(section)
            return shapes
        case StbSecParapetRc():
            return sec_parapet_rc.stb_sec_parapet_rc_to_shapes(section, reporter)
        case StbSecUndefined():
            return SHAPE_PAIRS_UNDEFINED
        case _:
            return None


def get_slab_depth(
    repo: RepositoryLatest, stb_slab: stb_latest.StbSlab, reporter: Reporter
) -> float:
    try:
        section = repo.deref(stb_slab).id_section_or_none
    except SchemaError:
        section = None
    if isinstance(section, stb_latest.StbSecSlabRc):
        try:
            return section.stb_sec_slab_rc_conventional.stb_sec_figure_slab_rc_conventional.stb_sec_slab_rc_conventional_straight.depth  # noqa:E501
        except NoneAccessError:
            pass
    reporter.warning(
        message=(
            f"スラブ断面id={stb_slab.id_section_or_none}が"
            f"見つかりませんでした。d={UNKNOWN_ELEMENT_SIZE_MM}mmで代替します"
        ),
        code=Code.MISSING_ATTRIBUTE,
        phase=Phase.CONVERT_GEOMETRY,
        stb_element=stb_slab,
        attr_name="id_section",
    )
    return UNKNOWN_ELEMENT_SIZE_MM


def get_wall_t(
    repo: RepositoryLatest, stb_wall: stb_latest.StbWall, reporter: Reporter
) -> float:
    try:
        section = repo.deref(stb_wall).id_section_or_none
    except SchemaError:
        section = None
    if isinstance(section, stb_latest.StbSecWallRc):
        fig: stb_latest.StbSecFigureWallRc = section.stb_sec_figure_wall_rc
        if fig.stb_sec_wall_rc_straight:
            return fig.stb_sec_wall_rc_straight.t
    reporter.warning(
        message=(
            f"壁断面id={stb_wall.id_section_or_none}が"
            f"見つかりませんでした。t={UNKNOWN_ELEMENT_SIZE_MM}mmで代替します"
        ),
        code=Code.MISSING_ATTRIBUTE,
        phase=Phase.CONVERT_GEOMETRY,
        stb_element=stb_wall,
        attr_name="id_section",
    )
    return UNKNOWN_ELEMENT_SIZE_MM
