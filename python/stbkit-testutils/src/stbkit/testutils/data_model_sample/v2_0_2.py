# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2


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
