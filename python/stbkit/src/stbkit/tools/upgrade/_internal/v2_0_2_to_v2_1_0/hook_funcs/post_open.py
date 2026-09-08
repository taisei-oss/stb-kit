# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid
from copy import deepcopy

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.stb_exceptions import NoneAccessError


def find_wall_or_slabs(
    stb: stb_v2_0_2.StBridge, id_open: int | None
) -> list[stb_v2_0_2.StbWall | stb_v2_0_2.StbSlab]:
    result: list[stb_v2_0_2.StbWall | stb_v2_0_2.StbSlab] = []
    if id_open is None:
        return result
    walls: stb_v2_0_2.StbWalls | None = None
    try:
        walls = stb.stb_model.stb_members.stb_walls
        for wall in walls.stb_wall:
            if not wall.stb_open_id_list_or_none:
                continue
            for open_id in wall.stb_open_id_list.stb_open_id:
                if open_id.id == id_open:
                    result.append(wall)
    except NoneAccessError:
        pass
    try:
        slabs: stb_v2_0_2.StbSlabs = stb.stb_model.stb_members.stb_slabs
        for slab in slabs.stb_slab:
            if not slab.stb_open_id_list_or_none:
                continue
            for open_id in slab.stb_open_id_list.stb_open_id:
                if open_id.id == id_open:
                    result.append(slab)
    except NoneAccessError:
        pass
    return result


def post_open(v202: stb_v2_0_2.StBridge, v210: stb_v2_1_0.StBridge) -> None:
    try:
        v202_opens: stb_v2_0_2.StbOpens = v202.stb_model.stb_members.stb_opens
    except NoneAccessError:
        return
    max_open_id: int = (
        max(obj.id if obj.id else 0 for obj in v202_opens.stb_open)
        if v202_opens.stb_open
        else 0
    )
    v210_opens: list[stb_v2_1_0.StbOpenArrangement] = (
        v210.ensure.stb_model()
        .ensure.stb_members()
        .ensure.stb_open_arrangements()
        .stb_open_arrangement
    )
    v210_sec_opens: list[stb_v2_1_0.StbSecOpenRc] = (
        v210.stb_model.ensure.stb_sections().stb_sec_open_rc
    )
    max_sec_open_id: int = (
        max(obj.id if obj.id else 0 for obj in v210_sec_opens) if v210_sec_opens else 0
    )
    for v202_open in v202_opens.stb_open:
        v210_open: stb_v2_1_0.StbOpenArrangement = stb_v2_1_0.StbOpenArrangement(
            id=v202_open.id_or_none,
            guid=v202_open.guid_or_none,
            name=v202_open.name_or_none,
            id_section=v202_open.id_section_or_none,
            position_x=v202_open.position_x_or_none,
            position_y=v202_open.position_y_or_none,
            rotate=v202_open.rotate_or_none,
        )
        wall_or_slabs: list[stb_v2_0_2.StbWall | stb_v2_0_2.StbSlab] = (
            find_wall_or_slabs(v202, v202_open.id)
        )
        if not wall_or_slabs:
            continue
        if v202_open.id_section_or_none is not None:
            id_section: int = v202_open.id_section
        else:
            max_sec_open_id += 1
            id_section = max_sec_open_id
        for index, wall_or_slab in enumerate(wall_or_slabs):
            # 2件目以降は、同一インスタンスを使い回すと先に設定したid_memberを
            # 上書きしてしまうため、複製して別IDを振る
            if index > 0:
                new_v210_open: stb_v2_1_0.StbOpenArrangement = deepcopy(v210_open)
                max_open_id += 1
                new_v210_open.id = max_open_id
            else:
                new_v210_open = v210_open

            if isinstance(wall_or_slab, stb_v2_0_2.StbWall):
                new_v210_open.kind_member = "WALL"
            else:
                new_v210_open.kind_member = "SLAB"
            new_v210_open.id_member = wall_or_slab.id
            new_v210_open.id_section = id_section
            v210_opens.append(new_v210_open)
        v210_sec_open: stb_v2_1_0.StbSecOpenRc = stb_v2_1_0.StbSecOpenRc(
            id=id_section,
            guid=uuid.uuid4(),
            name=(v202_open.name + "_sec") if v202_open.name_or_none else "unnamed_sec",
            length_x=v202_open.length_x,
            length_y=v202_open.length_y,
        )
        v210_sec_opens.append(v210_sec_open)
