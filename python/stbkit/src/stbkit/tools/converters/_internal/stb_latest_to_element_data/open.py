# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.stb_latest import (
    StbModel,
    StbOpenArrangement,
    StbOpenArrangementKindMember,
    StbSecOpenRc,
)

from ...._internal.data_model.element_data import ElementOpen, ElementPlane
from ...._internal.vectors import Vector2d


def add_open(
    stb_model: StbModel,
    stb_id_to_planes: dict[tuple[StbOpenArrangementKindMember, int], ElementPlane],
    *,
    reporter: Reporter,
) -> None:
    """開口の追加
    TODO:回転は未実装"""
    try:
        stb_opens: list[StbOpenArrangement] = (
            stb_model.stb_members.stb_open_arrangements.stb_open_arrangement
        )
        stb_sec_opens: list[StbSecOpenRc] = stb_model.stb_sections.stb_sec_open_rc
    except NoneAccessError:
        return
    for stb_open in stb_opens:
        if stb_open.rotate_or_none is not None and stb_open.rotate != 0.0:
            reporter.warning(
                message="開口の回転は未実装です",
                code=Code.NOT_IMPLEMENTED,
                phase=Phase.CONVERT_GEOMETRY,
                stb_element=stb_open,
                attr_name="rotate",
            )
        stb_sec_open: StbSecOpenRc | None = next(
            filter(
                lambda obj: obj is not None and obj.id == stb_open.id_section,
                stb_sec_opens,
            ),
            None,
        )
        if not stb_sec_open:
            continue
        plane: ElementPlane | None = stb_id_to_planes.get(
            (stb_open.kind_member, stb_open.id_member)
        )
        if plane is None:
            reporter.error(
                "開口のある部材が変換に失敗しているため、開口を変換できません",
                code=Code.REFERENCE_NOT_FOUND,
                phase=Phase.CONVERT_GEOMETRY,
                stb_element=stb_open,
                attr_name="id_member",
            )
            continue
        if not plane.thickness:
            continue
        x = stb_open.position_x
        y = stb_open.position_y
        if (
            stb_sec_open.length_x_or_none is None
            or stb_sec_open.length_y_or_none is None
        ):
            continue
        w = stb_sec_open.length_x
        h = stb_sec_open.length_y
        if x is not None and y is not None and w and h:
            open_points: list[Vector2d] = [
                Vector2d(x, y),
                Vector2d(x + w, y),
                Vector2d(x + w, y + h),
                Vector2d(x, y + h),
            ]
            open_name: str = str(stb_open.id_or_none or "")
            if stb_open.name_or_none:
                open_name += f"_{stb_open.name}"
            plane.opens.append(
                ElementOpen(
                    points=open_points,
                    name=open_name,
                    guid=stb_open.guid_or_none,
                    path=stb_open._path_xml(),
                    source_type=type(stb_open),
                    source_id=stb_open.id_or_none,
                )
            )
