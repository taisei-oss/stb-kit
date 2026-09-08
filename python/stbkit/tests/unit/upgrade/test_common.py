# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Any

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0, stb_v2_1_1
from stbkit.core.data_model.common import (
    StBridgeElement,
    _StBridgeElementList,
    _StBridgeExtensionElement,
)
from stbkit.core.stb_reporting import CollectingReporter
from stbkit.testutils import data_model_sample

from stbkit.tools.upgrade._internal.common import convert_element
from stbkit.tools.upgrade._internal.upgrade import (
    upgrade_to_v2_1_0,
    upgrade_v2_1_0_to_v2_1_1,
)


def test_upgrade_monolist_id() -> None:
    reporter: CollectingReporter = CollectingReporter()
    v210: stb_v2_1_0.StBridge = data_model_sample.v2_1_0_has_monolist_id()
    v211: stb_v2_1_1.StBridge = upgrade_v2_1_0_to_v2_1_1(v210, reporter=reporter)
    assert v211.stb_model.stb_members.stb_walls.stb_wall[
        0
    ].stb_node_id_order.content == [1, 2, 3, 4]


def _convert(stb: stb_v2_0_2.StBridge) -> stb_v2_1_0.StBridge:
    converted = convert_element(stb, stb_v2_1_0, reporter=CollectingReporter())
    assert isinstance(converted, stb_v2_1_0.StBridge)
    return converted


def _add_extension_child(
    parent: StBridgeElement, name: str, attributes: dict[str, Any] | None = None
) -> _StBridgeExtensionElement:
    child = _StBridgeExtensionElement(name)
    for key, value in (attributes or {}).items():
        child._ensure_extension._set_attribute(key, value)
    parent._ensure_extension._set_child(child)
    return child


def _extension_attributes(element: StBridgeElement) -> dict[str, Any]:
    ext = element._extension
    if ext is None or ext._attributes is None:
        return {}
    return dict(ext._attributes)


def _extension_children(element: StBridgeElement) -> list[StBridgeElement]:
    ext = element._extension
    if ext is None or ext._children is None:
        return []
    return list(ext._children)


def test_convert_element_extension_attribute() -> None:
    stb: stb_v2_0_2.StBridge = data_model_sample.v2_0_2_has_node()
    stb.stb_model.stb_nodes.stb_node[0]._ensure_extension._set_attribute(
        "ext_attr_1", "attr1"
    )
    converted: stb_v2_1_0.StBridge = _convert(stb)
    assert _extension_attributes(converted.stb_model.stb_nodes.stb_node[0]) == {
        "ext_attr_1": "attr1"
    }


def test_convert_element_extension_child() -> None:
    stb: stb_v2_0_2.StBridge = data_model_sample.v2_0_2_has_node()
    _add_extension_child(stb.stb_model, "ExtElement1", {"id": "1"})
    _add_extension_child(stb.stb_model, "ExtElement1", {"id": "2"})

    converted: stb_v2_1_0.StBridge = _convert(stb)

    children: list[StBridgeElement] = _extension_children(converted.stb_model)
    assert [child._xml_name() for child in children] == ["ExtElement1", "ExtElement1"]
    assert [_extension_attributes(child) for child in children] == [
        {"id": "1"},
        {"id": "2"},
    ]


def test_convert_element_nested_extension_child() -> None:
    stb: stb_v2_0_2.StBridge = data_model_sample.v2_0_2_has_node()
    parent: _StBridgeExtensionElement = _add_extension_child(
        stb.stb_model, "ExtElement2", {"id": "2"}
    )
    _add_extension_child(parent, "ExtElement3", {"name": "3"})

    converted: stb_v2_1_0.StBridge = _convert(stb)

    children: list[StBridgeElement] = _extension_children(converted.stb_model)
    assert len(children) == 1
    grandchildren: list[StBridgeElement] = _extension_children(children[0])
    assert [child._xml_name() for child in grandchildren] == ["ExtElement3"]
    assert _extension_attributes(grandchildren[0]) == {"name": "3"}


def test_convert_element_clones_extension_child() -> None:
    stb: stb_v2_0_2.StBridge = data_model_sample.v2_0_2_has_node()

    original_child: _StBridgeExtensionElement = _add_extension_child(
        stb.stb_model, "ExtElement1", {"id": "1"}
    )

    converted: stb_v2_1_0.StBridge = _convert(stb)

    new_child: StBridgeElement = _extension_children(converted.stb_model)[0]
    assert new_child is not original_child
    assert original_child._parent is stb.stb_model
    assert new_child._parent is converted.stb_model


def test_convert_element_has_no_extension() -> None:
    converted: stb_v2_1_0.StBridge = _convert(data_model_sample.v2_0_2_has_node())

    assert converted._extension is None
    assert converted.stb_model._extension is None
    assert converted.stb_model.stb_nodes.stb_node[0]._extension is None


def test_upgrade_to_v2_1_0_extensions() -> None:
    stb: stb_v2_0_2.StBridge = data_model_sample.v2_0_2_has_node()
    stb.stb_model.stb_nodes.stb_node[0]._ensure_extension._set_attribute(
        "ext_attr_1", "attr1"
    )
    _add_extension_child(stb.stb_model, "ExtElement1", {"id": "1"})

    upgraded: stb_v2_1_0.StBridge = upgrade_to_v2_1_0(
        stb, reporter=CollectingReporter()
    )

    assert upgraded.version == stb_v2_1_0.VERSION
    assert _extension_attributes(upgraded.stb_model.stb_nodes.stb_node[0]) == {
        "ext_attr_1": "attr1"
    }
    children: list[StBridgeElement] = _extension_children(upgraded.stb_model)
    assert [child._xml_name() for child in children] == ["ExtElement1"]
    assert _extension_attributes(children[0]) == {"id": "1"}


def test_convert_element_has_parent() -> None:
    stb: stb_v2_0_2.StBridge = data_model_sample.v2_0_2_has_node()
    stb.stb_model.stb_nodes.stb_node.append(
        stb_v2_0_2.StbNode(
            id=2, x=1000.0, y=0.0, z=0.0, kind=stb_v2_0_2.StbNodeKind.ON_GRID
        )
    )

    converted: stb_v2_1_0.StBridge = _convert(stb)

    model: stb_v2_1_0.StbModel = converted.stb_model
    nodes: stb_v2_1_0.StbNodes = model.stb_nodes
    node: stb_v2_1_0.StbNode = nodes.stb_node[1]
    assert model._parent is converted
    assert nodes._parent is model
    assert node._parent is nodes
    # 親リンクが無いと、Reporterが出すパスが要素名だけになる
    assert node._path_xml() == "/ST_BRIDGE/StbModel/StbNodes/StbNode[2]"


def test_convert_element_children_has_parent() -> None:
    stb: stb_v2_0_2.StBridge = data_model_sample.v2_0_2_has_node()

    converted: stb_v2_1_0.StBridge = _convert(stb)

    nodes: stb_v2_1_0.StbNodes = converted.stb_model.stb_nodes
    assert isinstance(nodes.stb_node, _StBridgeElementList)
    add_node = stb_v2_1_0.StbNode(
        id=2, x=1000.0, y=0.0, z=0.0, kind=stb_v2_1_0.StbNodeKind.ON_GRID
    )
    nodes.stb_node.append(add_node)
    assert add_node._parent is nodes
    assert add_node._path_xml() == "/ST_BRIDGE/StbModel/StbNodes/StbNode[2]"
