# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core._internal.transform.guid_tools import assign_guid_all
from stbkit.core.data_model.stb_v2_1_0 import StbModel, StbNode, StbNodes, StBridge


def test_assign_guid_all() -> None:
    stb: StBridge = StBridge(
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[
                    StbNode(),
                    StbNode(),
                ]
            )
        )
    )
    assert stb.stb_model.stb_nodes.stb_node[0].guid_or_none is None
    assert stb.stb_model.stb_nodes.stb_node[1].guid_or_none is None
    assign_guid_all(stb)
    assert stb.stb_model.stb_nodes.stb_node[0].guid_or_none is not None
    assert stb.stb_model.stb_nodes.stb_node[1].guid_or_none is not None  # type:ignore[unreachable]
    assert (
        stb.stb_model.stb_nodes.stb_node[0].guid_or_none
        != stb.stb_model.stb_nodes.stb_node[1].guid_or_none
    )
