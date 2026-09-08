# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from stbkit.core._internal.extension_utils import ExtensionInfoRepository
from stbkit.core.stb_io import loads
from stbkit.core.stb_reporting import CollectingReporter, NullReporter
from stbkit.core.validation import validate_schema


def _stb_xml_with_extension(*, extra_attribute: str, extra_element: str) -> str:
    """拡張定義を持つST-BridgeのXML。
    デフォルトで入っているStbNodeのext_attr_1と、StbModel直下のExtElement1は拡張定義がされている。
    引数で定義されていない拡張属性・拡張子要素を追加できる。
    """
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.0">\n'
        ' <StbCommon project_name="pj" app_name="stbkit-core" app_version="0.0.0"/>\n'
        " <StbModel>\n"
        "  <StbNodes>\n"
        '   <StbNode id="1" X="0" Y="0" Z="0" kind="ON_GRID"'
        f' ext_attr_1="a"{extra_attribute}/>\n'
        "  </StbNodes>\n"
        '  <ExtElement1 id="1"/>\n'
        f"{extra_element}"
        " </StbModel>\n"
        " <StbExtensions>\n"
        '  <StbExtension identifier="test_ext">\n'
        '   <StbExtElement object_name="StbNode">\n'
        '    <StbExtPropertyDef key="ext_attr_1" type="string"/>\n'
        "   </StbExtElement>\n"
        '   <StbExtElement object_name="StbModel" element_name="ExtElement1">\n'
        '    <StbExtPropertyDef key="id" type="integer"/>\n'
        "   </StbExtElement>\n"
        "  </StbExtension>\n"
        " </StbExtensions>\n"
        "</ST_BRIDGE>\n"
    )


@pytest.mark.requires_xsd("2.1.0")
def test_exclude_legal_extensions() -> None:
    xml: str = _stb_xml_with_extension(extra_attribute="", extra_element="")

    # Trueの場合
    reporter: CollectingReporter = CollectingReporter()
    assert validate_schema(
        xml, reporter=reporter, require_xsd=True, exclude_legal_extensions=True
    )
    assert reporter.is_valid()

    # Falseの場合
    reporter = CollectingReporter()
    assert not validate_schema(
        xml, reporter=reporter, require_xsd=True, exclude_legal_extensions=False
    )
    messages: list[str] = [item.message for item in reporter.report]
    assert any("ext_attr_1" in message for message in messages)
    assert any("ExtElement1" in message for message in messages)

    # デフォルトはTrue
    reporter = CollectingReporter()
    assert validate_schema(xml, reporter=reporter, require_xsd=True)
    assert reporter.is_valid()


@pytest.mark.requires_xsd("2.1.0")
def test_exclude_legal_extensions_with_invalid_extension() -> None:
    """定義されていない属性・子要素は、除外を指定してもエラー。"""
    xml: str = _stb_xml_with_extension(
        extra_attribute=' undefined_attr="x"',
        extra_element='  <UndefinedElement id="9"/>\n',
    )
    reporter: CollectingReporter = CollectingReporter()

    assert not validate_schema(
        xml, reporter=reporter, require_xsd=True, exclude_legal_extensions=True
    )
    messages: list[str] = [item.message for item in reporter.report]
    assert any("undefined_attr" in message for message in messages)
    assert any("UndefinedElement" in message for message in messages)
    assert not any("ext_attr_1" in message for message in messages)
    assert not any("ExtElement1" in message for message in messages)


# 内容的にはtest_extension_utils.pyに入れるべきだが、こちらのXMLを使いたいためここで実施
def test_extension_repository() -> None:
    xml: str = _stb_xml_with_extension(extra_attribute="", extra_element="")
    stb = loads(xml, reporter=NullReporter(), version="2.1.0")
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=NullReporter())

    node = stb.stb_model.stb_nodes.stb_node[0]
    assert ext_repo._allowed_attribute_names_by_element_name(
        node._xml_name()
    ) == ext_repo._allowed_attribute_names(node)
    assert ext_repo._allowed_attribute_names_by_element_name("StbNode") == {
        "ext_attr_1"
    }
    assert ext_repo._allowed_attribute_names_by_element_name("StbCommon") == set()

    assert ext_repo._is_allowed_child_name(
        child_name="ExtElement1", parent_name="StbModel"
    )
    assert not ext_repo._is_allowed_child_name(
        child_name="ExtElement1", parent_name="StbNodes"
    )
    assert not ext_repo._is_allowed_child_name(
        child_name="StbNode", parent_name="StbNodes"
    )
