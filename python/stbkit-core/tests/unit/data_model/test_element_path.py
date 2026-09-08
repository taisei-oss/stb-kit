# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.stb_v2_1_0 import (
    StbModel,
    StbNode,
    StbNodeIdOrder,
    StbNodes,
    StBridge,
)


def test_element_path() -> None:
    stb = StBridge(
        version="2.1.0",
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[
                    StbNode(id=1),
                    StbNode(id=2),
                ]
            ),
        ),
    )
    assert stb._path_xml() == "/ST_BRIDGE"
    assert stb._path_py() == "StBridge"
    assert stb.stb_model.stb_nodes._path_xml() == "/ST_BRIDGE/StbModel/StbNodes"
    assert stb.stb_model.stb_nodes._path_py() == "StBridge.stb_model.stb_nodes"
    assert (
        stb.stb_model.stb_nodes.stb_node[0]._path_xml()
        == "/ST_BRIDGE/StbModel/StbNodes/StbNode[1]"
    )
    assert (
        stb.stb_model.stb_nodes.stb_node[0]._path_py()
        == "StBridge.stb_model.stb_nodes.stb_node[0]"
    )
    assert (
        stb.stb_model.stb_nodes.stb_node[0]._path_xml("id")
        == "/ST_BRIDGE/StbModel/StbNodes/StbNode[1]/@id"
    )
    assert (
        stb.stb_model.stb_nodes.stb_node[0]._path_py("id")
        == "StBridge.stb_model.stb_nodes.stb_node[0].id"
    )
    assert (
        stb.stb_model.stb_nodes.stb_node[1]._path_xml("x")
        == "/ST_BRIDGE/StbModel/StbNodes/StbNode[2]/@X"
    )
    assert (
        stb.stb_model.stb_nodes.stb_node[1]._path_py("x")
        == "StBridge.stb_model.stb_nodes.stb_node[1].x"
    )
    assert stb._path_xml("stb_model") == "/ST_BRIDGE/StbModel"
    assert stb.stb_model._path_xml("stb_nodes") == "/ST_BRIDGE/StbModel/StbNodes"
    assert StbNodeIdOrder()._path_xml("content") == "/StbNodeIdOrder/text()"
