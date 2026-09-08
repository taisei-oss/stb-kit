# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.common import _StBridgeExtensionElement
from stbkit.core.data_model.stb_v2_1_0 import (
    StbCommon,
    StbModel,
    StbNode,
    StbNodes,
    StbReinforcementStrengthList,
    StBridge,
)


def test_element_parent() -> None:
    rsl: StbReinforcementStrengthList = StbReinforcementStrengthList()
    assert rsl._parent is None

    stb_common: StbCommon = StbCommon()
    assert stb_common._parent is None

    stb_common.stb_reinforcement_strength_list = rsl
    assert rsl._parent is stb_common
    assert stb_common._parent is None  # type:ignore[unreachable]

    stb: StBridge = StBridge()
    assert stb._parent is None
    stb.stb_common = stb_common
    assert rsl._parent is stb_common
    assert stb_common._parent is stb
    assert stb._parent is None

    stb2: StBridge = StBridge(stb_common=stb_common)
    assert rsl._parent is stb_common
    assert stb_common._parent is stb2
    assert stb2._parent is None


def test_element_list_parent() -> None:
    node: StbNode = StbNode()
    assert node._parent is None

    nodes: StbNodes = StbNodes()
    assert nodes._parent is None
    assert nodes.stb_node._parent is nodes  # type: ignore


def test_element_list_parent_init() -> None:
    node: StbNode = StbNode()
    nodes: StbNodes = StbNodes(stb_node=[node])
    assert node._parent is nodes


def test_element_list_parent_append() -> None:
    node: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.append(node)
    assert node._parent is nodes


def test_element_list_parent_extend() -> None:
    node1: StbNode = StbNode()
    node2: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.extend([node1, node2])
    assert node1._parent is nodes
    assert node2._parent is nodes


def test_element_list_parent_insert() -> None:
    node1: StbNode = StbNode()
    node2: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.append(node1)
    nodes.stb_node.insert(0, node2)
    assert node1._parent is nodes
    assert node2._parent is nodes


def test_element_list_parent_setitem() -> None:
    node1: StbNode = StbNode()
    node2: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.append(node1)
    nodes.stb_node[0] = node2
    assert node1._parent is None
    assert node2._parent is nodes


def test_element_list_parent_delitem() -> None:
    node1: StbNode = StbNode()
    node2: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.append(node1)
    nodes.stb_node.append(node2)
    del nodes.stb_node[0]
    assert node1._parent is None
    assert node2._parent is nodes


def test_element_list_parent_clear() -> None:
    node1: StbNode = StbNode()
    node2: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.append(node1)
    nodes.stb_node.append(node2)
    nodes.stb_node.clear()
    assert node1._parent is None
    assert node2._parent is None


def test_element_list_parent_pop() -> None:
    node1: StbNode = StbNode()
    node2: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.append(node1)
    nodes.stb_node.append(node2)
    popped_node = nodes.stb_node.pop(0)
    assert popped_node is node1
    assert node1._parent is None
    assert node2._parent is nodes


def test_element_list_parent_remove() -> None:
    node1: StbNode = StbNode()
    node2: StbNode = StbNode()
    nodes: StbNodes = StbNodes()
    nodes.stb_node.append(node1)
    nodes.stb_node.append(node2)
    nodes.stb_node.remove(node1)
    assert node1._parent is None
    assert node2._parent is nodes


def test_set_parent_extension_elements() -> None:
    stb: StBridge = StBridge(stb_model=StbModel())
    ext_child = _StBridgeExtensionElement("ExtChild")
    grand_child = _StBridgeExtensionElement("ExtGrandChild")
    stb.stb_model._ensure_extension._set_child(ext_child)
    ext_child._ensure_extension._set_child(grand_child)

    stb._set_parent_all()

    assert ext_child._path_xml() == "/ST_BRIDGE/StbModel/ExtChild[1]"
    assert grand_child._path_xml() == "/ST_BRIDGE/StbModel/ExtChild[1]/ExtGrandChild[1]"
