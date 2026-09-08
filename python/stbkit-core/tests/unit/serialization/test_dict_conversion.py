# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
import sys
from copy import deepcopy
from pathlib import Path
from types import ModuleType
from typing import Any, ClassVar, assert_type
from uuid import UUID

import pytest

from stbkit.core.data_model import stb_v2_0_1, stb_v2_0_2, stb_v2_1_0, stb_v2_1_1
from stbkit.core.data_model._internal.stb_types import DataType
from stbkit.core.data_model.common import (
    StBridgeElement,
    StBridgeRoot,
    _FieldInfo,
    _FieldKind,
    _StBridgeExtensionElement,
)
from stbkit.core.data_model.stb_v2_1_1 import (
    VERSION,
    StbModel,
    StbNode,
    StbNodeIdOrder,
    StbNodes,
    StBridge,
)
from stbkit.core.serialization import (
    DictProfile,
    KeyStyle,
    from_dict,
    profiles,
    to_dict,
)
from stbkit.core.serialization._dict_converter import (
    _resolve_model_version,
)
from stbkit.core.stb_exceptions import SchemaError, UnsupportedStbVersionError
from stbkit.core.stb_reporting import CollectingReporter, Phase


def _sample_stb(module: Any) -> StBridgeRoot:
    node: StBridgeElement = module.StbNode(
        id=1,
        x=1.0,
        y=2.0,
        z=3.0,
        kind="ON_GRID",
    )
    nodes: StBridgeElement = module.StbNodes(stb_node=[node])
    model: StBridgeElement = module.StbModel(stb_nodes=nodes)
    common: StBridgeElement = module.StbCommon(
        project_name="dict test",
        app_name="stbkit",
        app_version="0.0.0",
    )
    stb: StBridgeRoot = module.StBridge(
        version=module.VERSION,
        stb_common=common,
        stb_model=model,
    )
    return stb


@pytest.mark.parametrize("module", [stb_v2_0_1, stb_v2_0_2, stb_v2_1_0, stb_v2_1_1])
def test_dict_roundtrip_default(module: Any) -> None:
    stb: StBridgeRoot = _sample_stb(module)

    stb_dict: dict[str, Any] = to_dict(stb)
    new_stb: StBridgeRoot = from_dict(stb_dict, reporter=CollectingReporter())

    assert stb_dict["ST_BRIDGE"]["version"] == module.VERSION
    assert "StbCommon" in stb_dict["ST_BRIDGE"]
    assert "StbModel" in stb_dict["ST_BRIDGE"]
    assert stb_dict["ST_BRIDGE"]["StbExtensions"] is None
    assert "stb_common" not in stb_dict["ST_BRIDGE"]
    assert to_dict(new_stb) == stb_dict
    assert type(new_stb) is type(stb)


def test_dict_roundtrip_custom_prefixes() -> None:
    stb: StBridgeRoot = _sample_stb(stb_v2_1_1)
    profile: DictProfile = DictProfile(
        attribute_prefix="@",
        child_prefix="$",
        content_key="#text",
        key_style=KeyStyle.CAMEL,
        omit_none=True,
    )

    stb_dict: dict[str, Any] = to_dict(stb, _profile=profile)
    new_stb: StBridgeRoot = from_dict(
        stb_dict,
        _profile=profile,
        reporter=CollectingReporter(),
    )

    assert stb_dict["@version"] == stb_v2_1_1.VERSION
    assert "$stbCommon" in stb_dict
    assert to_dict(new_stb) == to_dict(stb)

    nodes_dict: list[Any] = stb_dict["$stbModel"]["$stbNodes"]["$stbNode"]
    nodes_dict.clear()
    model: StbModel = stb.stb_model  # type: ignore[attr-defined]
    assert len(model.stb_nodes.stb_node) == 1


def test_dict_convert_omit() -> None:
    node: StbNode = StbNode(
        id=1,
        x=1.0,
        y=2.0,
        z=3.0,
        kind="ON_GRID",
    )
    profile_omit: DictProfile = DictProfile(omit_empty=True)

    node_dict: dict[str, Any] = to_dict(node, _profile=profile_omit)
    assert node_dict["id"] == 1
    assert "guid" not in node_dict
    assert node_dict["X"] == 1.0
    assert node_dict["kind"] == "ON_GRID"
    assert "id_member" not in node_dict

    profile_not_omit: DictProfile = DictProfile(omit_empty=False)

    node_dict = to_dict(node, _profile=profile_not_omit)
    assert node_dict["id"] == 1
    assert node_dict["guid"] is None
    assert node_dict["X"] == 1.0
    assert node_dict["kind"] == "ON_GRID"
    assert node_dict["id_member"] is None


def test_omit_empty_child_elements() -> None:
    stb: StBridge = StBridge(
        version=VERSION,
        stb_model=StbModel(
            stb_nodes=StbNodes(stb_node=[]),
        ),
    )

    stb_dict: dict[str, Any] = to_dict(stb, _profile=DictProfile(omit_empty=True))

    assert stb_dict == {"version": VERSION}


def test_dict_wrap_root() -> None:
    profile_wrap_root: DictProfile = DictProfile(wrap_root=True, omit_empty=True)
    stb_dict: dict[str, Any] = to_dict(
        _sample_stb(stb_v2_1_0), _profile=profile_wrap_root
    )
    assert "ST_BRIDGE" in stb_dict
    new_stb: StBridgeRoot = from_dict(stb_dict, _profile=profile_wrap_root)
    assert to_dict(new_stb, _profile=profile_wrap_root) == stb_dict

    profile_no_wrap: DictProfile = DictProfile(wrap_root=False, omit_empty=True)
    stb_dict_no_wrap: dict[str, Any] = to_dict(
        _sample_stb(stb_v2_1_0), _profile=profile_no_wrap
    )
    assert "ST_BRIDGE" not in stb_dict_no_wrap
    new_stb_no_wrap: StBridgeRoot = from_dict(
        stb_dict_no_wrap, _profile=profile_no_wrap
    )
    assert to_dict(new_stb_no_wrap, _profile=profile_no_wrap) == stb_dict_no_wrap

    assert stb_dict["ST_BRIDGE"] == stb_dict_no_wrap


def test_to_dict_child_and_content() -> None:
    node: StbNode = StbNode(id=1, x=1.0, y=2.0, z=3.0, kind="ON_GRID")
    node_id_order: StbNodeIdOrder = StbNodeIdOrder()
    node_id_order.content = [1, 2, 3]

    node_dict: dict[str, Any] = to_dict(node)
    content_dict: dict[str, Any] = to_dict(node_id_order)
    xml_content_dict: dict[str, Any] = to_dict(
        node_id_order,
        _profile=profiles._XMLTODICT_COMPAT,
    )

    assert node_dict["X"] == 1.0
    assert "x" not in node_dict
    assert node_dict["kind"] == "ON_GRID"
    assert "kind_or_none" not in node_dict
    assert content_dict == {"content": [1, 2, 3]}
    assert xml_content_dict == {"#text": "1 2 3"}


def test_external_model_uses_each_definition_module_version(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root_module: ModuleType = ModuleType("tests.external_model_root")
    child_module: ModuleType = ModuleType("tests.external_model_child")
    root_module.__dict__["VERSION"] = "8.0.0"
    child_module.__dict__["VERSION"] = "8.1.0"
    monkeypatch.setitem(sys.modules, root_module.__name__, root_module)
    monkeypatch.setitem(sys.modules, child_module.__name__, child_module)

    class ExternalChild(StBridgeElement):
        _fields: ClassVar[dict[str, _FieldInfo]] = {}
        _xml_element_name: ClassVar[str] = "ExternalChild"

    class ExternalRoot(StBridgeRoot):
        _fields: ClassVar[dict[str, _FieldInfo]] = {
            "child": _FieldInfo(
                kind=_FieldKind.ELEMENT,
                max_occurs=1,
                py_type="ExternalChild",
            )
        }
        _xml_element_name: ClassVar[str] = "EXTERNAL_ROOT"

    monkeypatch.setattr(ExternalRoot, "__module__", root_module.__name__)
    monkeypatch.setattr(ExternalChild, "__module__", child_module.__name__)
    root_module.__dict__["ExternalChild"] = ExternalChild

    root: ExternalRoot = ExternalRoot()
    child: StBridgeElement = root._ensure_child("child")
    assert isinstance(child, ExternalChild)

    assert _resolve_model_version(root) == "8.0.0"
    assert _resolve_model_version(ExternalRoot) == "8.0.0"
    assert _resolve_model_version(child) == "8.1.0"
    assert _resolve_model_version(ExternalChild) == "8.1.0"
    assert to_dict(root) == {"EXTERNAL_ROOT": {"ExternalChild": {}}}


@pytest.mark.parametrize(
    ("key_style", "expected_root_key"),
    [
        ("xml", "EXTERNAL_ROOT"),
        ("snake", "external_root"),
        ("camel", "externalRoot"),
    ],
)
def test_wrap_root_uses_selected_root_element_name(
    monkeypatch: pytest.MonkeyPatch,
    key_style: str,
    expected_root_key: str,
) -> None:
    model_module: ModuleType = ModuleType("tests.external_named_root")
    version: str = "8.4.0"
    model_module.__dict__["VERSION"] = version
    monkeypatch.setitem(sys.modules, model_module.__name__, model_module)

    class ExternalNamedRoot(StBridgeRoot):
        _fields: ClassVar[dict[str, _FieldInfo]] = {
            "version": _FieldInfo(
                py_type=str,
                data_type=DataType.STR,
                required=True,
            )
        }
        _xml_element_name: ClassVar[str] = "EXTERNAL_ROOT"

    monkeypatch.setattr(
        ExternalNamedRoot,
        "__module__",
        model_module.__name__,
    )
    model_module.__dict__["ExternalNamedRoot"] = ExternalNamedRoot

    profile: DictProfile = DictProfile(wrap_root=True, key_style=key_style)
    root: ExternalNamedRoot = ExternalNamedRoot()
    root._set_attribute_by_any(
        "version",
        version,
    )
    root_dict: dict[str, Any] = to_dict(root, _profile=profile)
    reporter: CollectingReporter = CollectingReporter()

    new_root = from_dict(
        root_dict,
        root_type=ExternalNamedRoot,
        _profile=profile,
        reporter=reporter,
    )

    assert root_dict == {expected_root_key: {"version": "8.4.0"}}
    assert_type(new_root, ExternalNamedRoot)
    assert type(new_root) is ExternalNamedRoot
    assert not any("ルート" in item.message for item in reporter.report)


def test_from_dict_accepts_unregistered_root_type_without_version(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root_module: ModuleType = ModuleType("tests.external_root_without_version")
    child_module: ModuleType = ModuleType("tests.external_child_with_other_version")
    root_module.__dict__["VERSION"] = "0.1.0"
    child_module.__dict__["VERSION"] = "0.2.0"
    monkeypatch.setitem(sys.modules, root_module.__name__, root_module)
    monkeypatch.setitem(sys.modules, child_module.__name__, child_module)

    class ExternalChild(StBridgeElement):
        _fields: ClassVar[dict[str, _FieldInfo]] = {
            "version": _FieldInfo(
                py_type=str,
                data_type=DataType.STR,
                required=True,
            ),
            "name": _FieldInfo(
                py_type=str,
                data_type=DataType.STR,
                required=True,
            ),
        }
        _xml_element_name: ClassVar[str] = "ExternalChild"

    class ExternalRoot(StBridgeRoot):
        _fields: ClassVar[dict[str, _FieldInfo]] = {
            "child": _FieldInfo(
                kind=_FieldKind.ELEMENT,
                py_type=ExternalChild,
                max_occurs=1,
            )
        }
        _xml_element_name: ClassVar[str] = "EXTERNAL_ROOT"

    monkeypatch.setattr(ExternalRoot, "__module__", root_module.__name__)
    monkeypatch.setattr(ExternalChild, "__module__", child_module.__name__)
    root_module.__dict__["ExternalRoot"] = ExternalRoot
    root_module.__dict__["ExternalChild"] = ExternalChild
    child_module.__dict__["ExternalChild"] = ExternalChild

    root: ExternalRoot = ExternalRoot()
    child: StBridgeElement = root._ensure_child("child")
    child._set_attribute_by_any("version", "child-0.2.0")
    child._set_attribute_by_any("name", "sample")
    root_dict: dict[str, Any] = to_dict(root)

    new_root: StBridgeRoot = from_dict(
        root_dict,
        root_type=ExternalRoot,
        reporter=CollectingReporter(),
    )

    assert "version" not in root_dict
    assert type(new_root) is ExternalRoot
    assert to_dict(new_root) == root_dict


def test_from_dict_rejects_non_root_type() -> None:
    invalid_root_type: type = StBridgeElement

    with pytest.raises(TypeError, match="StBridgeRootを継承"):
        from_dict(
            {},
            root_type=invalid_root_type,
            reporter=CollectingReporter(),
        )


def test_extension_model_version_is_resolved_from_parent_module(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    model_module: ModuleType = ModuleType("tests.external_model_with_extension")
    model_module.__dict__["VERSION"] = "8.2.0"
    monkeypatch.setitem(sys.modules, model_module.__name__, model_module)

    class ExternalElement(StBridgeElement):
        pass

    monkeypatch.setattr(ExternalElement, "__module__", model_module.__name__)

    parent: ExternalElement = ExternalElement()
    extension: _StBridgeExtensionElement = _StBridgeExtensionElement("Extension")
    nested_extension: _StBridgeExtensionElement = _StBridgeExtensionElement(
        "NestedExtension"
    )
    extension._attach_to_parent(parent)
    nested_extension._attach_to_parent(extension)

    assert _resolve_model_version(extension) == "8.2.0"
    assert _resolve_model_version(nested_extension) == "8.2.0"
    assert to_dict(extension) == {}
    assert to_dict(nested_extension) == {}


def test_normal_element_does_not_inherit_parent_module_version(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    parent_module: ModuleType = ModuleType("tests.external_model_parent")
    child_module: ModuleType = ModuleType("tests.external_model_without_version")
    parent_module.__dict__["VERSION"] = "8.3.0"
    monkeypatch.setitem(sys.modules, parent_module.__name__, parent_module)
    monkeypatch.setitem(sys.modules, child_module.__name__, child_module)

    class ExternalChild(StBridgeElement):
        _fields: ClassVar[dict[str, _FieldInfo]] = {}
        _xml_element_name: ClassVar[str] = "ExternalChild"

    class ExternalParent(StBridgeElement):
        _fields: ClassVar[dict[str, _FieldInfo]] = {
            "child": _FieldInfo(
                kind=_FieldKind.ELEMENT,
                max_occurs=1,
                py_type=ExternalChild,
            )
        }
        _xml_element_name: ClassVar[str] = "ExternalParent"

    monkeypatch.setattr(ExternalParent, "__module__", parent_module.__name__)
    monkeypatch.setattr(ExternalChild, "__module__", child_module.__name__)
    parent_module.__dict__["ExternalChild"] = ExternalChild

    parent: ExternalParent = ExternalParent()
    child: StBridgeElement = parent._ensure_child("child")
    assert isinstance(child, ExternalChild)

    with pytest.raises(ValueError, match="VERSION定数がありません"):
        to_dict(parent)


def test_json_and_xml_value_styles_use_expected_uuid_representation() -> None:
    guid: UUID = UUID("12345678-1234-5678-1234-567812345678")
    node: StBridgeElement = stb_v2_1_0.StbNode(
        id=1,
        guid=guid,
        x=1.0,
        y=2.0,
        z=3.0,
        kind="ON_GRID",
    )

    json_dict: dict[str, Any] = to_dict(node, _profile=profiles._JSON_CAMEL)
    xml_dict: dict[str, Any] = to_dict(node, _profile=profiles._XMLTODICT_COMPAT)

    assert json_dict["guid"] == str(guid)
    assert xml_dict["@guid"] == guid.hex


@pytest.mark.parametrize("module", [stb_v2_0_1, stb_v2_0_2, stb_v2_1_0, stb_v2_1_1])
def test_non_default_profiles_roundtrip_for_all_versions(
    module: Any,
) -> None:
    stb: StBridgeRoot = _sample_stb(module)

    for profile in (
        profiles._ANALYSIS,
        profiles._JSON_CAMEL,
        profiles._XMLTODICT_COMPAT,
    ):
        stb_dict: dict[str, Any] = to_dict(stb, _profile=profile)
        new_stb: StBridgeRoot = from_dict(
            stb_dict,
            _profile=profile,
            reporter=CollectingReporter(),
        )

        if profile == profiles._JSON_CAMEL:
            json.dumps(stb_dict, ensure_ascii=False)
        assert to_dict(new_stb) == to_dict(stb)


def test_json_and_xml_profile_shape() -> None:
    stb: StBridgeRoot = _sample_stb(stb_v2_1_1)

    json_dict: dict[str, Any] = to_dict(stb, _profile=profiles._JSON_CAMEL)
    xml_dict: dict[str, Any] = to_dict(stb, _profile=profiles._XMLTODICT_COMPAT)

    assert "stbCommon" in json_dict
    assert list(xml_dict) == ["ST_BRIDGE"]
    assert "@version" in xml_dict["ST_BRIDGE"]


def test_from_dict_continues_after_value_and_structure_errors() -> None:
    stb_dict: dict[str, Any] = to_dict(_sample_stb(stb_v2_1_1))
    edited_stb_dict: dict[str, Any] = deepcopy(stb_dict)
    node_dict: dict[str, Any] = edited_stb_dict["ST_BRIDGE"]["StbModel"]["StbNodes"][
        "StbNode"
    ][0]
    node_dict["X"] = "invalid-float"
    node_dict["unknown_attribute"] = "unknown"
    node_dict["UnknownChild"] = {"id": "1"}
    del edited_stb_dict["ST_BRIDGE"]["StbCommon"]
    original_input: dict[str, Any] = deepcopy(edited_stb_dict)
    reporter: CollectingReporter = CollectingReporter()

    new_stb: StBridgeRoot = from_dict(edited_stb_dict, reporter=reporter)
    node: Any = new_stb.stb_model.stb_nodes.stb_node[0]  # type: ignore[attr-defined]

    assert edited_stb_dict == original_input
    assert new_stb.stb_common_or_none is None  # type: ignore[attr-defined]
    assert node.x_or_none is None
    assert node._extension is not None
    assert node._extension._invalid_values is not None
    assert any(
        invalid.value == "invalid-float" for invalid in node._extension._invalid_values
    )
    # 拡張定義で説明できない属性・子要素は不正値へ退避され、出力されない
    assert not node._extension._attributes
    assert not node._extension._children
    assert any(
        invalid.value == "unknown" for invalid in node._extension._invalid_values
    )
    assert any(
        isinstance(invalid.value, StBridgeElement)
        and invalid.value._xml_name() == "UnknownChild"
        for invalid in node._extension._invalid_values
    )
    assert any(item.phase == Phase.LOAD.value for item in reporter.report)
    assert any("必須要素" in item.message for item in reporter.report)


def test_invalid_content_is_stored_as_content_invalid_value() -> None:
    from stbkit.core.stb_io import loads

    path: Path = Path("tests/fixtures/cases/open_wall/open_wall.stb_v2_0_2.stb")
    stb: StBridgeRoot = loads(
        path.read_text(encoding="utf-8"), reporter=CollectingReporter()
    )
    stb_dict: dict[str, Any] = to_dict(stb)
    wall_dict: dict[str, Any] = stb_dict["ST_BRIDGE"]["StbModel"]["StbMembers"][
        "StbWalls"
    ]["StbWall"][0]
    wall_dict["StbNodeIdOrder"]["content"] = ["invalid"]

    new_stb: StBridgeRoot = from_dict(stb_dict, reporter=CollectingReporter())
    walls: Any = new_stb.stb_model.stb_members.stb_walls  # type: ignore[attr-defined]
    node_id_order: Any = walls.stb_wall[0].stb_node_id_order

    assert node_id_order._content is None
    assert node_id_order._extension is not None
    invalid_values: list[Any] | None = node_id_order._extension._invalid_values
    assert invalid_values is not None
    assert invalid_values[0].kind.value == "content"
    assert invalid_values[0].path.endswith("/StbNodeIdOrder")


def test_profiles_preserve_extension_names() -> None:
    from stbkit.core.stb_io import loads

    path: Path = Path("tests/fixtures/cases/has_extension/has_extension.stb_v2_1_1.stb")
    stb: StBridgeRoot = loads(
        path.read_text(encoding="utf-8"), reporter=CollectingReporter()
    )

    for profile in (
        profiles.DEFAULT,
        profiles._ANALYSIS,
        profiles._JSON_CAMEL,
        profiles._XMLTODICT_COMPAT,
    ):
        stb_dict: dict[str, Any] = to_dict(stb, _profile=profile)
        new_stb: StBridgeRoot = from_dict(
            stb_dict,
            _profile=profile,
            reporter=CollectingReporter(),
        )

        assert to_dict(new_stb) == to_dict(stb)


def test_extension_repository_moves_undefined_key_to_invalid_value() -> None:
    from stbkit.core.stb_io import loads

    path: Path = Path("tests/fixtures/cases/has_extension/has_extension.stb_v2_1_1.stb")
    stb: StBridgeRoot = loads(
        path.read_text(encoding="utf-8"), reporter=CollectingReporter()
    )
    stb_dict: dict[str, Any] = to_dict(stb)
    stb_dict["ST_BRIDGE"]["StbModel"]["StbNodes"]["undefined_attribute"] = "invalid"
    reporter: CollectingReporter = CollectingReporter()

    new_stb: StBridgeRoot = from_dict(stb_dict, reporter=reporter)
    nodes: StBridgeElement = new_stb.stb_model.stb_nodes  # type: ignore[attr-defined]

    assert nodes._extension is not None
    assert not nodes._extension._attributes
    assert nodes._extension._invalid_values is not None
    assert any(
        invalid.value == "invalid" for invalid in nodes._extension._invalid_values
    )
    assert any(item.code == "extension_error" for item in reporter.report)


def test_list_single_value_is_only_accepted_by_xmltodict_profile() -> None:
    stb: StBridgeRoot = _sample_stb(stb_v2_1_0)
    default_dict: dict[str, Any] = to_dict(stb)
    default_dict["ST_BRIDGE"]["StbModel"]["StbNodes"]["StbNode"] = default_dict[
        "ST_BRIDGE"
    ]["StbModel"]["StbNodes"]["StbNode"][0]

    new_stb_default: StBridgeRoot = from_dict(
        default_dict,
        reporter=CollectingReporter(),
    )
    default_nodes: Any = new_stb_default.stb_model.stb_nodes  # type: ignore[attr-defined]
    assert default_nodes.stb_node == []

    xml_dict: dict[str, Any] = to_dict(stb, _profile=profiles._XMLTODICT_COMPAT)
    xml_nodes: dict[str, Any] = xml_dict["ST_BRIDGE"]["StbModel"]["StbNodes"]
    xml_nodes["StbNode"] = xml_nodes["StbNode"][0]
    xml_new_stb: StBridgeRoot = from_dict(
        xml_dict,
        _profile=profiles._XMLTODICT_COMPAT,
        reporter=CollectingReporter(),
    )
    xml_new_nodes: Any = xml_new_stb.stb_model.stb_nodes  # type: ignore[attr-defined]
    assert len(xml_new_nodes.stb_node) == 1


def test_from_dict_requires_a_supported_version() -> None:
    with pytest.raises(SchemaError):
        from_dict({}, reporter=CollectingReporter())

    with pytest.raises(UnsupportedStbVersionError):
        from_dict(
            {"version": "9.9.9"},
            reporter=CollectingReporter(),
        )
