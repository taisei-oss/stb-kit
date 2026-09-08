# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_1_0, stb_v2_1_1

from stbkit.tools.upgrade import upgrade_to


def test_upgrade_enum() -> None:
    v210: stb_v2_1_0.StBridge = stb_v2_1_0.StBridge(
        version=stb_v2_1_0.VERSION,
        stb_common=stb_v2_1_0.StbCommon(project_name="test"),
        stb_model=stb_v2_1_0.StbModel(
            stb_nodes=stb_v2_1_0.StbNodes(
                stb_node=[
                    stb_v2_1_0.StbNode(
                        id=1,
                        x=0.0,
                        y=0.0,
                        z=0.0,
                        kind=stb_v2_1_0.StbNodeKind.ON_GRID,
                    ),
                ]
            )
        ),
    )
    v211: stb_v2_1_1.StBridge = upgrade_to(v210, stb_v2_1_1.VERSION)
    assert v211.version == stb_v2_1_1.VERSION
    assert isinstance(v211, stb_v2_1_1.StBridge)
    assert isinstance(v211.stb_model, stb_v2_1_1.StbModel)
    assert isinstance(v211.stb_model.stb_nodes, stb_v2_1_1.StbNodes)
    assert isinstance(v211.stb_model.stb_nodes.stb_node[0], stb_v2_1_1.StbNode)
    assert v211.stb_model.stb_nodes.stb_node[0].kind is stb_v2_1_1.StbNodeKind.ON_GRID
