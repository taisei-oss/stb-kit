# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0


def v2_0_2_minimum() -> stb_v2_0_2.StBridge:
    return stb_v2_0_2.StBridge(
        version=stb_v2_0_2.VERSION,
        stb_common=stb_v2_0_2.StbCommon(
            project_name="v2.0.2 minimum",
            app_name="stbkit",
            app_version="0.0.0",
        ),
        stb_model=stb_v2_0_2.StbModel(),
    )


def v2_0_2_has_node() -> stb_v2_0_2.StBridge:
    stb: stb_v2_0_2.StBridge = v2_0_2_minimum()
    stb.stb_common.project_name = "v2.0.2 has Node"
    stb.stb_model = stb_v2_0_2.StbModel(
        stb_nodes=stb_v2_0_2.StbNodes(
            stb_node=[
                stb_v2_0_2.StbNode(
                    id=1, x=0.0, y=0.0, z=0.0, kind=stb_v2_0_2.StbNodeKind.ON_GRID
                )
            ]
        )
    )
    return stb


def v2_1_0_minimum() -> stb_v2_1_0.StBridge:
    return stb_v2_1_0.StBridge(
        version=stb_v2_1_0.VERSION,
        stb_common=stb_v2_1_0.StbCommon(
            project_name="v2.1.0 minimum",
            app_name="stbkit",
            app_version="0.0.0",
        ),
        stb_model=stb_v2_1_0.StbModel(),
    )


def v2_1_0_has_monolist_id() -> stb_v2_1_0.StBridge:
    stb: stb_v2_1_0.StBridge = v2_1_0_minimum()
    stb.stb_common.project_name = "has monolist id"
    stb.stb_model.stb_nodes = stb_v2_1_0.StbNodes(
        stb_node=[
            stb_v2_1_0.StbNode(
                id=1, x=0.0, y=0.0, z=0.0, kind=stb_v2_1_0.StbNodeKind.ON_GRID
            ),
            stb_v2_1_0.StbNode(
                id=2, x=5000.0, y=0.0, z=0.0, kind=stb_v2_1_0.StbNodeKind.ON_GRID
            ),
            stb_v2_1_0.StbNode(
                id=3, x=5000.0, y=0.0, z=4000.0, kind=stb_v2_1_0.StbNodeKind.ON_GRID
            ),
            stb_v2_1_0.StbNode(
                id=4, x=0.0, y=0.0, z=4000.0, kind=stb_v2_1_0.StbNodeKind.ON_GRID
            ),
        ]
    )
    stb.stb_model.stb_members = stb_v2_1_0.StbMembers(
        stb_walls=stb_v2_1_0.StbWalls(
            stb_wall=[
                stb_v2_1_0.StbWall(
                    id=1,
                    stb_node_id_order=stb_v2_1_0.StbNodeIdOrder(content=[1, 2, 3, 4]),
                    id_section=1,
                    kind_structure=stb_v2_1_0.StbWallKindStructure.RC,
                    kind_layout=stb_v2_1_0.StbWallKindLayout.ON_GIRDER,
                )
            ]
        )
    )
    stb.stb_model.stb_sections = stb_v2_1_0.StbSections(
        stb_sec_wall_rc=[
            stb_v2_1_0.StbSecWallRc(
                id=1,
                name="W15",
                stb_sec_figure_wall_rc=stb_v2_1_0.StbSecFigureWallRc(
                    stb_sec_wall_rc_straight=stb_v2_1_0.StbSecWallRcStraight(t=150.0)
                ),
            )
        ]
    )
    return stb
