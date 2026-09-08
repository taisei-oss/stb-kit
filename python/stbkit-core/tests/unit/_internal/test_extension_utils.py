# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core._internal.extension_utils import (
    AttributeInfo,
    ExtensionInfo,
    ExtensionInfoRepository,
)
from stbkit.core.data_model.common import (
    StBridgeElement,
    _ExtensionData,
    _FieldKind,
    _InvalidValue,
    _StBridgeExtensionElement,
)
from stbkit.core.data_model.stb_v2_1_0 import (
    VERSION,
    StbCommon,
    StbExtElement,
    StbExtension,
    StbExtensions,
    StbExtPropertyDef,
    StbModel,
    StbNode,
    StbNodeKind,
    StbNodes,
    StBridge,
)
from stbkit.core.stb_reporting import Code, CollectingReporter, Phase


def _extension_child_names(element: StBridgeElement) -> list[str]:
    ext: _ExtensionData | None = element._extension
    if ext is None or ext._children is None:
        return []
    return [child._xml_name() for child in ext._children]


def _invalid_values(element: StBridgeElement) -> list[_InvalidValue]:
    ext: _ExtensionData | None = element._extension
    if ext is None or ext._invalid_values is None:
        return []
    return list(ext._invalid_values)


def _repair_stb(stb: StBridge, reporter: CollectingReporter) -> None:
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=reporter, phase=Phase.LOAD)
    ext_repo.repair_stb(stb, reporter, Phase.LOAD)


def _messages(reporter: CollectingReporter, code: Code) -> list[str]:
    return [item.message for item in reporter.report if item.code == code.value]


def _create_model(extensions: StbExtensions | None) -> StBridge:
    return StBridge(
        version=VERSION,
        stb_common=StbCommon(
            project_name="extension test",
            app_name="stbkit",
            app_version="0.0.0",
        ),
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[StbNode(id=1, x=0.0, y=0.0, z=0.0, kind=StbNodeKind.ON_GRID)]
            )
        ),
        stb_extensions=extensions,
    )


def test_ext_repo_defines_attributes_to_existing_element() -> None:
    """既存要素への属性追加"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbNode",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="ext_attr_1", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )

    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=CollectingReporter(), phase=Phase.LOAD)

    ext_info: ExtensionInfo = ext_repo._registry["StbNode"]
    assert ext_info.parent_name is None
    assert {attr.name for attr in ext_info.attribute_infos} == {"ext_attr_1"}


def test_ext_repo_defines_ext_child_element() -> None:
    """拡張子要素定義"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=CollectingReporter(), phase=Phase.LOAD)
    ext_info: ExtensionInfo = ext_repo._registry["ExtElement1"]
    assert ext_info.parent_name == "StbModel"
    assert {attr.name for attr in ext_info.attribute_infos} == {"id"}


def test_ext_repo_not_defines_extensions() -> None:
    """拡張定義なし"""
    stb: StBridge = _create_model(None)
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=CollectingReporter(), phase=Phase.LOAD)

    assert ext_repo._registry == {}


def test_ext_repo_defines_conflict_exist_and_extension() -> None:
    """同じ要素名が属性追加と拡張子要素の双方で定義された場合のエラー"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        ),
                        StbExtElement(
                            object_name="ExtElement1",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="extra", type="string")
                            ],
                        ),
                    ],
                )
            ]
        )
    )
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    reporter: CollectingReporter = CollectingReporter()
    ext_repo.register(stb, reporter=reporter, phase=Phase.LOAD)

    messages: list[str] = _messages(reporter, Code.EXTENSION_ERROR)
    assert len(messages) == 1
    assert "ExtElement1" in messages[0]
    # 先に定義した内容を採用
    assert ext_repo._registry["ExtElement1"].parent_name == "StbModel"


def test_ext_repo_defines_conflict_two_exist() -> None:
    """同じ拡張子要素が異なる既存要素に定義された場合のエラー"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        ),
                        StbExtElement(
                            object_name="StbNodes",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        ),
                    ],
                )
            ]
        )
    )
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    reporter: CollectingReporter = CollectingReporter()
    ext_repo.register(stb, reporter=reporter, phase=Phase.LOAD)

    assert len(_messages(reporter, Code.EXTENSION_ERROR)) == 1
    # 先に定義した内容を採用
    assert ext_repo._registry["ExtElement1"].parent_name == "StbModel"


def test_ext_repo_defines_split() -> None:
    """2か所でobject_nameとelement_nameが共通の拡張属性を定義した場合マージする"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        ),
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="name", type="string")
                            ],
                        ),
                    ],
                )
            ]
        )
    )
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    reporter: CollectingReporter = CollectingReporter()

    ext_repo.register(stb, reporter=reporter, phase=Phase.LOAD)

    assert _messages(reporter, Code.EXTENSION_ERROR) == []
    ext_info: ExtensionInfo = ext_repo._registry["ExtElement1"]
    assert {attr.name for attr in ext_info.attribute_infos} == {"id", "name"}


def test_defined_attribute() -> None:
    """正しい拡張属性"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbNode",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="ext_attr_1", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )
    node: StbNode = stb.stb_model.stb_nodes.stb_node[0]
    node._ensure_extension._set_attribute("ext_attr_1", "attr1")

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert node._extension is not None
    assert node._extension._attributes == {"ext_attr_1": "attr1"}
    assert _invalid_values(node) == []


def test_missing_define_attribute_child() -> None:
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbNode",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="ext_attr_1", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )
    nodes: StbNodes = stb.stb_model.stb_nodes
    nodes._ensure_extension._set_attribute("ext_attr_1", "attr1")

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert nodes._extension is not None
    assert nodes._extension._attributes in (None, {})
    invalid: list[_InvalidValue] = _invalid_values(nodes)
    assert len(invalid) == 1
    assert invalid[0].kind is _FieldKind.ATTRIBUTE
    assert invalid[0].value == "attr1"
    assert invalid[0].reason == "拡張定義されていない拡張属性"
    assert len(_messages(reporter, Code.EXTENSION_ERROR)) == 1


def test_missing_define_attribute_parent() -> None:
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbNodes",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="ext_attr_1", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )
    node: StbNode = stb.stb_model.stb_nodes.stb_node[0]
    node._ensure_extension._set_attribute("ext_attr_1", "attr1")

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert node._extension is not None
    assert node._extension._attributes in (None, {})
    assert [invalid.value for invalid in _invalid_values(node)] == ["attr1"]
    assert len(_messages(reporter, Code.EXTENSION_ERROR)) == 1


def test_undefined_attribute() -> None:
    """未定義の属性"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbNode",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="ext_attr_1", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )
    node: StbNode = stb.stb_model.stb_nodes.stb_node[0]
    node._ensure_extension._set_attribute("unknown_attr", "value")

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert node._extension is not None
    assert node._extension._attributes in (None, {})
    assert [invalid.value for invalid in _invalid_values(node)] == ["value"]


def test_not_defined_extension() -> None:
    """拡張定義の定義がない場合"""
    stb: StBridge = _create_model(None)
    node: StbNode = stb.stb_model.stb_nodes.stb_node[0]
    node._ensure_extension._set_attribute("err_attr", "error")

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert node._extension is not None
    assert node._extension._attributes in (None, {})
    assert [invalid.value for invalid in _invalid_values(node)] == ["error"]
    assert len(_messages(reporter, Code.EXTENSION_ERROR)) == 1


def test_defined_ext_element() -> None:
    """正しい拡張子要素"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )
    model: StbModel = stb.stb_model
    model._ensure_extension._set_child(
        _StBridgeExtensionElement("ExtElement1", {"id": "1"})
    )

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert _extension_child_names(model) == ["ExtElement1"]
    assert _invalid_values(model) == []


def test_defined_nested_ext_element() -> None:
    """正しい拡張子要素(階層)"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        ),
                        StbExtElement(
                            object_name="ExtElement1",
                            element_name="ExtElement2",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="name", type="string")
                            ],
                        ),
                    ],
                )
            ]
        )
    )
    model: StbModel = stb.stb_model
    parent: _StBridgeExtensionElement = _StBridgeExtensionElement(
        "ExtElement1", {"id": "1"}
    )
    model._ensure_extension._set_child(parent)
    parent._ensure_extension._set_child(
        _StBridgeExtensionElement("ExtElement2", {"name": "n"})
    )

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert _extension_child_names(model) == ["ExtElement1"]
    assert _extension_child_names(parent) == ["ExtElement2"]
    assert _messages(reporter, Code.EXTENSION_ERROR) == []


def test_missing_defined_ext_element() -> None:
    """宣言された対象要素以外へ置かれた拡張子要素は、不正値へ退避する。"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtElement1",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="id", type="string")
                            ],
                        ),
                        StbExtElement(
                            object_name="ExtElement1",
                            element_name="ExtElement2",
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="name", type="string")
                            ],
                        ),
                    ],
                )
            ]
        )
    )
    model: StbModel = stb.stb_model
    model._ensure_extension._set_child(
        _StBridgeExtensionElement("ExtElement1", {"id": "1"})
    )
    model._ensure_extension._set_child(
        _StBridgeExtensionElement("ExtElement2", {"name": "n"})
    )

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert _extension_child_names(model) == ["ExtElement1"]
    invalid: list[_InvalidValue] = _invalid_values(model)
    assert len(invalid) == 1
    assert invalid[0].kind is _FieldKind.ELEMENT
    assert invalid[0].reason == "拡張定義されていない拡張子要素"
    assert len(_messages(reporter, Code.EXTENSION_ERROR)) == 1


def test_missing_defined_ext_element_and_attr() -> None:
    """object_nameのみの定義は属性追加であり、拡張子要素の追加は許可しない。"""
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbNode",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="ext_attr_1", type="string")
                            ],
                        )
                    ],
                )
            ]
        )
    )
    model: StbModel = stb.stb_model
    model._ensure_extension._set_child(
        _StBridgeExtensionElement("StbNode", {"id": "99"})
    )

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert _extension_child_names(model) == []
    assert len(_invalid_values(model)) == 1


def test_not_defined_ext_element() -> None:
    """拡張定義が無い場合、拡張子要素を許容しない。"""
    stb: StBridge = _create_model(None)
    model: StbModel = stb.stb_model
    model._ensure_extension._set_child(
        _StBridgeExtensionElement("ErrorChild", {"attr1": "error"})
    )

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert _extension_child_names(model) == []
    assert len(_invalid_values(model)) == 1


def test_reported_path() -> None:
    """退避した拡張属性のxpathがReportに含まれrる"""
    stb: StBridge = _create_model(None)
    node: StbNode = stb.stb_model.stb_nodes.stb_node[0]
    node._ensure_extension._set_attribute("err_attr", "error")

    reporter: CollectingReporter = CollectingReporter()
    _repair_stb(stb, reporter)

    assert reporter.report[0].xpath is not None
    assert reporter.report[0].xpath.endswith("/@err_attr")


def test_attribute_infos() -> None:
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbNode",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="zeta_attr", type="string"),
                                StbExtPropertyDef(key="alpha_attr", type="string"),
                            ],
                        )
                    ],
                )
            ]
        )
    )
    node: StbNode = stb.stb_model.stb_nodes.stb_node[0]
    nodes: StbNodes = stb.stb_model.stb_nodes
    reporter: CollectingReporter = CollectingReporter()
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=reporter)

    infos: tuple[AttributeInfo, ...] = ext_repo._attribute_infos(node)

    assert [info.name for info in infos] == ["alpha_attr", "zeta_attr"]
    assert [info.type for info in infos] == ["string", "string"]
    # 定義の無い型では空
    assert ext_repo._attribute_infos(nodes) == ()


def test_child_element_names() -> None:
    stb: StBridge = _create_model(
        StbExtensions(
            stb_extension=[
                StbExtension(
                    identifier="test_ext",
                    stb_ext_element=[
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtChildB",
                            stb_ext_property_def=[],
                        ),
                        StbExtElement(
                            object_name="StbModel",
                            element_name="ExtChildA",
                            stb_ext_property_def=[],
                        ),
                        # object_nameのみの定義は属性追加なので、拡張子要素には含めない
                        StbExtElement(
                            object_name="StbModel",
                            element_name=None,
                            stb_ext_property_def=[
                                StbExtPropertyDef(key="model_attr", type="string")
                            ],
                        ),
                        StbExtElement(
                            object_name="ExtChildB",
                            element_name="ExtGrandChild",
                            stb_ext_property_def=[],
                        ),
                    ],
                )
            ]
        )
    )
    model: StbModel = stb.stb_model
    node: StbNode = model.stb_nodes.stb_node[0]
    reporter: CollectingReporter = CollectingReporter()
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=reporter)

    assert ext_repo._child_element_names(model) == (
        "ExtChildB",
        "ExtChildA",
    )
    assert ext_repo._child_element_names(node) == ()
