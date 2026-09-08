# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import ReferenceElementNotFoundError, StbError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbSecBuildBox,
    StbSecBuildH,
    StbSecBuildT,
    StbSecFlatBar,
    StbSecLipC,
    StbSecPipe,
    StbSecRollBox,
    StbSecRollC,
    StbSecRollH,
    StbSecRollL,
    StbSecRollT,
    StbSecRoundBar,
    StbSecSteelColumnSrcNotSame,
    StbSecSteelColumnSrcSame,
    StbSecSteelColumnSrcShapeBox,
    StbSecSteelColumnSrcShapeCross1,
    StbSecSteelColumnSrcShapeH,
    StbSecSteelColumnSrcShapePipe,
    StbSecSteelColumnSrcShapeT,
    StbSecSteelColumnSrcThreeTypes,
)

from ....._internal.data_model.shape_data import (
    SHAPE_PAIR_UNKNOWN,
    Shape,
    ShapeAngle,
    ShapeBox,
    ShapeBuildBox,
    ShapeChannel,
    ShapeCircle,
    ShapeCrossH,
    ShapeH,
    ShapeLipC,
    ShapePair,
    ShapePipe,
    ShapeRectangle,
    ShapeT,
    ShapeTSrc,
)
from ....._internal.vectors import Vector2d
from ... import name_converter


def stb_sec_steel_column_src_shape_to_shape_pair(
    repo: RepositoryLatest,
    sec_steel_column_src: StbSecSteelColumnSrcSame
    | StbSecSteelColumnSrcNotSame
    | StbSecSteelColumnSrcThreeTypes,
    reporter: Reporter,
) -> ShapePair:
    try:
        if sec_steel_column_src.stb_sec_steel_column_src_shape_h_or_none:
            return ShapePair(
                stb_sec_steel_column_src_shape_h_to_shape(
                    repo,
                    sec_steel_column_src.stb_sec_steel_column_src_shape_h,
                )
            )
        elif sec_steel_column_src.stb_sec_steel_column_src_shape_box_or_none:
            return ShapePair(
                stb_sec_steel_column_src_shape_box_to_shape(
                    repo,
                    sec_steel_column_src.stb_sec_steel_column_src_shape_box,
                )
            )
        elif sec_steel_column_src.stb_sec_steel_column_src_shape_pipe_or_none:
            return ShapePair(
                stb_sec_steel_column_src_shape_pipe_to_shape(
                    repo,
                    sec_steel_column_src.stb_sec_steel_column_src_shape_pipe,
                )
            )
        elif sec_steel_column_src.stb_sec_steel_column_src_shape_cross1_or_none:
            return ShapePair(
                stb_sec_steel_column_src_shape_cross1_to_shape(
                    repo,
                    sec_steel_column_src.stb_sec_steel_column_src_shape_cross1,
                )
            )
        elif sec_steel_column_src.stb_sec_steel_column_src_shape_t_or_none:
            return ShapePair(
                stb_sec_steel_column_src_shape_t_to_shape(
                    repo,
                    sec_steel_column_src.stb_sec_steel_column_src_shape_t,
                )
            )
        else:
            reporter.warning(
                message="非対応の断面です",
                code=Code.MISSING_ATTRIBUTE,
                phase=Phase.CONVERT_IFC,
                stb_element=sec_steel_column_src,
            )
            return SHAPE_PAIR_UNKNOWN
    except ReferenceElementNotFoundError as e:
        reporter.warning(
            message=str(e),
            code=Code.REFERENCE_NOT_FOUND,
            phase=Phase.CONVERT_IFC,
            stb_element=sec_steel_column_src,
        )
        return SHAPE_PAIR_UNKNOWN
    except (StbError, RuntimeError, AssertionError, TypeError):
        reporter.error(
            message="断面の変換中にエラーが発生しました",
            code=Code.UNEXPECTED_ERROR,
            phase=Phase.CONVERT_IFC,
            stb_element=sec_steel_column_src,
        )
        return SHAPE_PAIR_UNKNOWN


def stb_sec_steel_column_src_shape_h_to_shape(
    repo: RepositoryLatest,
    stb_sec_steel_column_src_shape_h: StbSecSteelColumnSrcShapeH,
) -> ShapeH:
    stb_sec_h: StBridgeElement = repo.get_steel(stb_sec_steel_column_src_shape_h.shape)
    match stb_sec_h:
        case StbSecRollH() as roll_h:
            result: ShapeH = stb_sec_roll_h_to_shape(roll_h)
        case StbSecBuildH() as build_h:
            result = stb_sec_build_h_to_shape(build_h)
        case _:
            raise ReferenceElementNotFoundError(
                f"{stb_sec_steel_column_src_shape_h.shape}はH形鋼ではありません",
            )

    result.offset = Vector2d(
        stb_sec_steel_column_src_shape_h.offset_x_or_none or 0.0,
        stb_sec_steel_column_src_shape_h.offset_y_or_none or 0.0,
    )
    if stb_sec_steel_column_src_shape_h.direction_type == "H":
        result.rotate_degree = 90.0
    return result


def stb_sec_steel_column_src_shape_box_to_shape(
    repo: RepositoryLatest,
    stb_sec_steel_column_src_shape_box: StbSecSteelColumnSrcShapeBox,
) -> ShapeBox | ShapeBuildBox:
    stb_sec_box: StBridgeElement = repo.get_steel(
        stb_sec_steel_column_src_shape_box.shape
    )
    match stb_sec_box:
        case StbSecRollBox() as roll_box:
            result: ShapeBox | ShapeBuildBox = stb_sec_roll_box_to_shape(roll_box)
        case StbSecBuildBox() as build_box:
            result = stb_sec_build_box_to_shape(build_box)
        case _:
            raise ReferenceElementNotFoundError(
                f"{stb_sec_steel_column_src_shape_box.shape}は角形鋼管ではありません",
            )

    result.offset = Vector2d(
        stb_sec_steel_column_src_shape_box.offset_x_or_none or 0.0,
        stb_sec_steel_column_src_shape_box.offset_y_or_none or 0.0,
    )
    return result


def stb_sec_steel_column_src_shape_pipe_to_shape(
    repo: RepositoryLatest,
    stb_sec_steel_column_src_shape_pipe: StbSecSteelColumnSrcShapePipe,
) -> ShapePipe:
    stb_sec_pipe: StBridgeElement = repo.get_steel(
        stb_sec_steel_column_src_shape_pipe.shape
    )
    match stb_sec_pipe:
        case StbSecPipe() as pipe:
            result: ShapePipe = stb_sec_pipe_to_shape(pipe)
        case _:
            raise ReferenceElementNotFoundError(
                f"{stb_sec_steel_column_src_shape_pipe.shape}は円形鋼管ではありません",
            )

    result.offset = Vector2d(
        stb_sec_steel_column_src_shape_pipe.offset_x_or_none or 0.0,
        stb_sec_steel_column_src_shape_pipe.offset_y_or_none or 0.0,
    )
    return result


def stb_sec_steel_column_src_shape_cross1_to_shape(
    repo: RepositoryLatest,
    stb_sec_steel_column_src_shape_cross1: StbSecSteelColumnSrcShapeCross1,
) -> ShapeCrossH:
    stb_sec_h_x: StBridgeElement = repo.get_steel(
        stb_sec_steel_column_src_shape_cross1.shape_x
    )
    stb_sec_h_y: StBridgeElement = repo.get_steel(
        stb_sec_steel_column_src_shape_cross1.shape_y
    )
    if not isinstance(stb_sec_h_x, (StbSecRollH, StbSecBuildH)) or not isinstance(
        stb_sec_h_y, (StbSecRollH, StbSecBuildH)
    ):
        raise ReferenceElementNotFoundError(
            f"{stb_sec_steel_column_src_shape_cross1.shape_x}または{stb_sec_steel_column_src_shape_cross1.shape_y}はH形鋼ではありません",
        )
    return ShapeCrossH(
        name="",
        h_h=stb_sec_h_x.a,
        h_b=stb_sec_h_x.b,
        h_tw=stb_sec_h_x.t1,
        h_tf=stb_sec_h_x.t2,
        i_h=stb_sec_h_y.a,
        i_b=stb_sec_h_y.b,
        i_tw=stb_sec_h_y.t1,
        i_tf=stb_sec_h_y.t2,
        h_offset_y=(stb_sec_steel_column_src_shape_cross1.offset_xy_or_none or 0.0)
        - (stb_sec_steel_column_src_shape_cross1.offset_yy_or_none or 0.0),
        i_offset_x=(stb_sec_steel_column_src_shape_cross1.offset_yx_or_none or 0.0)
        - (stb_sec_steel_column_src_shape_cross1.offset_xx_or_none or 0.0),
        offset=Vector2d(
            stb_sec_steel_column_src_shape_cross1.offset_xx_or_none or 0.0,
            stb_sec_steel_column_src_shape_cross1.offset_yy_or_none or 0.0,
        ),
    )


def stb_sec_steel_column_src_shape_t_to_shape(
    repo: RepositoryLatest, stb_sec_steel_column_src_shape_t: StbSecSteelColumnSrcShapeT
) -> ShapeTSrc:
    stb_sec_h: StBridgeElement = repo.get_steel(
        stb_sec_steel_column_src_shape_t.shape_h
    )
    stb_sec_t: StBridgeElement = repo.get_steel(
        stb_sec_steel_column_src_shape_t.shape_t
    )
    if not isinstance(stb_sec_h, (StbSecRollH, StbSecBuildH)):
        raise ReferenceElementNotFoundError(
            f"{stb_sec_steel_column_src_shape_t.shape_h}はH形鋼ではありません",
        )
    if not isinstance(stb_sec_t, (StbSecRollT, StbSecBuildT)):
        raise ReferenceElementNotFoundError(
            f"{stb_sec_steel_column_src_shape_t.shape_t}はT形鋼ではありません",
        )
    match stb_sec_steel_column_src_shape_t.direction_type_or_none:
        case "T4":
            rotate_degree = 90.0
        case "T3":
            rotate_degree = 180.0
        case "T2":
            rotate_degree = 270.0
        case _:
            rotate_degree = 0.0
    name: str = name_converter.stb_element_to_ifc_name(stb_sec_steel_column_src_shape_t)
    offset: Vector2d = Vector2d(
        stb_sec_steel_column_src_shape_t.offset_hx_or_none or 0.0,
        (stb_sec_steel_column_src_shape_t.offset_hy_or_none or 0.0)
        - ((stb_sec_t.a + stb_sec_h.b / 2.0) / 2.0 - (stb_sec_h.b / 2.0)),
    ).rotate(rotate_degree)
    return ShapeTSrc(
        name=name,
        h_h=stb_sec_h.a,
        h_b=stb_sec_h.b,
        h_tw=stb_sec_h.t1,
        h_tf=stb_sec_h.t2,
        t_h=stb_sec_t.a,
        t_b=stb_sec_t.b,
        t_tw=stb_sec_t.t1,
        t_tf=stb_sec_t.t2,
        offset=offset,
        t_offset_x=(stb_sec_steel_column_src_shape_t.offset_t_or_none or 0.0)
        - (stb_sec_steel_column_src_shape_t.offset_hx_or_none or 0.0),
        rotate_degree=rotate_degree,
    )


def stb_sec_roll_h_to_shape(
    stb_sec_roll_h: StbSecRollH,
) -> ShapeH:
    return ShapeH(
        name=stb_sec_roll_h.name,
        a=stb_sec_roll_h.a,
        b=stb_sec_roll_h.b,
        t1=stb_sec_roll_h.t1,
        t2=stb_sec_roll_h.t2,
        r=stb_sec_roll_h.r,
    )


def stb_sec_build_h_to_shape(
    stb_sec_build_h: StbSecBuildH,
) -> ShapeH:
    return ShapeH(
        name=stb_sec_build_h.name,
        a=stb_sec_build_h.a,
        b=stb_sec_build_h.b,
        t1=stb_sec_build_h.t1,
        t2=stb_sec_build_h.t2,
        r=0.0,
    )


def stb_sec_roll_box_to_shape(
    stb_sec_roll_box: StbSecRollBox,
) -> ShapeBox:
    return ShapeBox(
        name=stb_sec_roll_box.name,
        a=stb_sec_roll_box.a,
        b=stb_sec_roll_box.b,
        t=stb_sec_roll_box.t,
        r=stb_sec_roll_box.r,
    )


def stb_sec_build_box_to_shape(
    stb_sec_build_box: StbSecBuildBox,
) -> ShapeBuildBox:
    return ShapeBuildBox(
        name=stb_sec_build_box.name,
        a=stb_sec_build_box.a,
        b=stb_sec_build_box.b,
        t1=stb_sec_build_box.t1,
        t2=stb_sec_build_box.t2,
    )


def stb_sec_pipe_to_shape(stb_sec_pipe: StbSecPipe) -> ShapePipe:
    return ShapePipe(name=stb_sec_pipe.name, d=stb_sec_pipe.d, t=stb_sec_pipe.t)


def stb_sec_roll_t_to_shape(
    stb_sec_roll_t: StbSecRollT,
) -> ShapeT:
    return ShapeT(
        name=stb_sec_roll_t.name,
        a=stb_sec_roll_t.a,
        b=stb_sec_roll_t.b,
        t1=stb_sec_roll_t.t1,
        t2=stb_sec_roll_t.t2,
        r=stb_sec_roll_t.r,
    )


def stb_sec_roll_c_to_shape(stb_sec_roll_c: StbSecRollC) -> ShapeChannel:
    return ShapeChannel(
        name=stb_sec_roll_c.name,
        a=stb_sec_roll_c.a,
        b=stb_sec_roll_c.b,
        t1=stb_sec_roll_c.t1,
        t2=stb_sec_roll_c.t2,
        r1=stb_sec_roll_c.r1_or_none or 0.0,
        r2=stb_sec_roll_c.r2_or_none or 0.0,
    )


def stb_sec_roll_l_to_shape(stb_sec_roll_l: StbSecRollL) -> ShapeAngle:
    return ShapeAngle(
        name=stb_sec_roll_l.name,
        a=stb_sec_roll_l.a,
        b=stb_sec_roll_l.b,
        t1=stb_sec_roll_l.t1,
        t2=stb_sec_roll_l.t2,
        r1=stb_sec_roll_l.r1_or_none or 0.0,
        r2=stb_sec_roll_l.r2_or_none or 0.0,
    )


def stb_sec_lip_c_to_shape(stb_sec_lip_c: StbSecLipC) -> ShapeLipC:
    return ShapeLipC(
        name=stb_sec_lip_c.name,
        h=stb_sec_lip_c.h,
        a=stb_sec_lip_c.a,
        c=stb_sec_lip_c.c,
        t=stb_sec_lip_c.t,
    )


def stb_sec_flat_bar_to_shape(stb_sec_float_bar: StbSecFlatBar) -> ShapeRectangle:
    return ShapeRectangle(
        name=stb_sec_float_bar.name,
        width_x=stb_sec_float_bar.t,
        width_y=stb_sec_float_bar.b,
    )


def stb_sec_round_bar_to_shape(stb_sec_round_bar: StbSecRoundBar) -> ShapeCircle:
    return ShapeCircle(
        name=stb_sec_round_bar.name,
        d=stb_sec_round_bar.r,
    )


def stb_sec_steel_name_to_shape(
    repo: RepositoryLatest, name: str, reporter: Reporter
) -> Shape:
    stb_sec = repo.get_steel(name)
    match stb_sec:
        case StbSecRollH():
            return stb_sec_roll_h_to_shape(stb_sec)
        case StbSecBuildH():
            return stb_sec_build_h_to_shape(stb_sec)
        case StbSecRollBox():
            return stb_sec_roll_box_to_shape(stb_sec)
        case StbSecBuildBox():
            return stb_sec_build_box_to_shape(stb_sec)
        case StbSecPipe():
            return stb_sec_pipe_to_shape(stb_sec)
        case StbSecRollT():
            return stb_sec_roll_t_to_shape(stb_sec)
        case StbSecRollC():
            return stb_sec_roll_c_to_shape(stb_sec)
        case StbSecRollL():
            return stb_sec_roll_l_to_shape(stb_sec)
        case StbSecLipC():
            return stb_sec_lip_c_to_shape(stb_sec)
        case StbSecFlatBar():
            return stb_sec_flat_bar_to_shape(stb_sec)
        case StbSecRoundBar():
            return stb_sec_round_bar_to_shape(stb_sec)
        case _:
            pass

    reporter.warning(
        message=f"{name}という鉄骨形状が見つかりません",
        code=Code.REFERENCE_NOT_FOUND,
        phase=Phase.CONVERT_IFC,
    )
    return ShapeRectangle(name="UNKNOWN", width_x=10.0, width_y=10.0)
