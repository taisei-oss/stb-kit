# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.stb_v2_1_1 import (
    VERSION,
    StbColumn,
    StbColumnKindStructure,
    StbColumns,
    StbCommon,
    StbMembers,
    StbModel,
    StbNode,
    StbNodeKind,
    StbNodes,
    StBridge,
    StbSecColumnRc,
    StbSecColumnRect,
    StbSecFigureColumnRc,
    StbSections,
)


def v2_1_1_minimum() -> StBridge:
    return StBridge(
        version=VERSION,
        stb_common=StbCommon(
            project_name="v2.1.1 minimum",
            app_name="stbkit",
            app_version="0.0.0",
        ),
        stb_model=StbModel(),
    )


def v2_1_1_rc_column() -> StBridge:
    stb: StBridge = v2_1_1_minimum()
    stb.stb_model.stb_nodes = StbNodes(
        stb_node=[
            StbNode(id=1, x=0.0, y=0.0, z=0.0, kind=StbNodeKind.ON_GRID),
            StbNode(id=2, x=1.0, y=1.0, z=5.0, kind=StbNodeKind.ON_GRID),
        ]
    )
    stb.stb_model.stb_members = StbMembers(
        stb_columns=StbColumns(
            stb_column=[
                StbColumn(
                    id=1,
                    id_node_bottom=1,
                    id_node_top=2,
                    id_section=1,
                    kind_structure=StbColumnKindStructure.RC,
                )
            ]
        )
    )
    stb.stb_model.stb_sections = StbSections(
        stb_sec_column_rc=[
            StbSecColumnRc(
                id=1,
                name="C1",
                stb_sec_figure_column_rc=StbSecFigureColumnRc(
                    stb_sec_column_rect=StbSecColumnRect(width_x=800.0, width_y=700.0)
                ),
            )
        ]
    )
    return stb
