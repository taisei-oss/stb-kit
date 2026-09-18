# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from importlib import import_module
from types import ModuleType
from typing import TYPE_CHECKING, Any, Final

from ..._internal.constants import (
    DEFAULT_MAX_XML_DEPTH,
    DEFAULT_MAX_XML_SIZE,
    VERSION_TO_MODULE_IMPORT_PATH,
    XML_READ_HEADER_CHUNK_SIZE,
)
from ..._internal.name_converter import (
    content_py_attr_name,
    private_field_name,
    xml_attribute_name_to_python_attribute_name,
    xml_element_name_to_key,
    xml_element_name_to_python_class_name,
)
from ...data_model.common import (
    StBridgeElement,
    StBridgeRoot,
    _FieldInfo,
    _FieldKind,
    _InvalidValue,
    _StBridgeExtensionElement,
)
from ...stb_exceptions import (
    SchemaError,
    UnsafeXmlError,
    UnsupportedStbVersionError,
    XmlLimitExceededError,
    XmlLimitKind,
)
from ...stb_reporting import Code, Phase, Reporter
from ...stb_typing import StbVersion

if TYPE_CHECKING:
    from collections.abc import Iterable

_ROOT_XML_NAME: Final[str] = "ST_BRIDGE"


def read_stream(
    chunks: Iterable[str],
    *,
    version: StbVersion | None = None,
    reporter: Reporter,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
) -> StBridgeRoot:
    """XMLを逐次読み込みし、モデルを生成する。

    Args:
        chunks: XMLを先頭から順に分割した文字列。
        version: 読み込むST-Bridgeのバージョン。Noneの場合はルート要素から判定。
        reporter: 出力Reporter。
        max_size: 読み込む文字数の上限。
        max_depth: 要素の階層の上限。
    """
    builder: _StbDataModelBuilder = _StbDataModelBuilder(
        version=version, reporter=reporter, max_depth=max_depth
    )
    parser: ET.XMLParser = ET.XMLParser(target=builder)
    size: int = 0
    for chunk in chunks:
        size += len(chunk)
        if size > max_size:
            raise XmlLimitExceededError(kind=XmlLimitKind.SIZE, limit=max_size)
        parser.feed(chunk)
    result: Any = parser.close()
    if not isinstance(result, StBridgeRoot):
        raise SchemaError(f"{_ROOT_XML_NAME}要素が見つかりません")
    return result


def check_no_doctype(xml: str) -> None:
    """XMLの前文にDOCTYPE宣言が無いことを確認する"""
    # DOCTYPE宣言はルート要素より前に記述するため、
    # ルート要素の開始までを読んで判定する。
    parser: ET.XMLParser = ET.XMLParser(target=_TargetForCheckDoctype())
    try:
        for index in range(0, len(xml), XML_READ_HEADER_CHUNK_SIZE):
            parser.feed(xml[index : index + XML_READ_HEADER_CHUNK_SIZE])
        parser.close()
    except _CompleteCheckDoctype:
        # ルート要素に到達したため、DOCTYPE宣言が無い。
        return
    except ET.ParseError:
        # パースに失敗する場合は、本編の処理で対応。
        return


class _CompleteCheckDoctype(Exception):
    pass


class _TargetForCheckDoctype:
    """DOCTYPE宣言を検出するためのET.XMLParserのターゲット"""

    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        raise UnsafeXmlError("DOCTYPE宣言は使用できません")

    def start(self, tag: str, attrib: dict[str, str]) -> None:
        raise _CompleteCheckDoctype

    def end(self, tag: str) -> None:
        pass

    def data(self, data: str) -> None:
        pass

    def close(self) -> None:
        return None


@dataclass(slots=True)
class _Element:
    """生成途中の要素"""

    element: StBridgeElement
    xml_name: str
    text: list[str] | None = field(default_factory=list)
    """内容の断片。子要素が現れたらNoneにして、以降のテキストは無視する。"""

    child_counts: dict[str, int] = field(default_factory=dict)
    """同名の子要素が現れた回数"""

    excess_of: str | None = None
    """最大回数を超過した子要素の、親のフィールド名"""


class _StbDataModelBuilder:
    """XMLのイベントから要素を生成するためのET.XMLParserのターゲット"""

    def __init__(
        self,
        *,
        version: StbVersion | None,
        reporter: Reporter,
        max_depth: int,
    ) -> None:
        self._version: StbVersion | None = version
        self._reporter: Reporter = reporter
        self._max_depth: int = max_depth
        self._module: ModuleType | None = None
        self._root: StBridgeRoot | None = None
        self._stack: list[_Element] = []

    def doctype(self, name: str, pubid: str | None, system: str | None) -> None:
        raise UnsafeXmlError("DOCTYPE宣言は使用できません")

    def start(self, tag: str, attrib: dict[str, str]) -> None:
        if len(self._stack) + 1 > self._max_depth:
            raise XmlLimitExceededError(
                kind=XmlLimitKind.DEPTH,
                limit=self._max_depth,
                actual=len(self._stack) + 1,
            )
        xml_name: str = _delete_namespace(tag)
        frame: _Element
        if not self._stack:
            frame = self._start_root(xml_name, attrib)
        else:
            frame = self._start_child(self._stack[-1], xml_name)
        self._stack.append(frame)
        self._set_attributes(frame.element, attrib)

    def data(self, data: str) -> None:
        if not self._stack:
            return
        text: list[str] | None = self._stack[-1].text
        if text is not None:
            text.append(data)

    def end(self, tag: str) -> None:
        frame: _Element = self._stack.pop()
        self._set_content(frame)
        if frame.excess_of is not None:
            self._invalid_occurs(frame)

    def close(self) -> StBridgeRoot | None:
        return self._root

    def _start_root(self, xml_name: str, attrib: dict[str, str]) -> _Element:
        if xml_name != _ROOT_XML_NAME:
            self._reporter.error(
                message=f"{_ROOT_XML_NAME}要素が見つかりません",
                code=Code.SCHEMA_ERROR,
                phase=Phase.LOAD,
            )
        module: ModuleType = _get_module(self._version or _read_version(attrib))
        self._module = module
        root: StBridgeRoot = module.StBridge()
        self._root = root
        return _Element(element=root, xml_name=xml_name)

    def _start_child(self, parent: _Element, xml_name: str) -> _Element:
        # 子要素が現れたら、それ以降のテキストは内容として扱わない。
        parent.text = None
        count: int = parent.child_counts.get(xml_name, 0) + 1
        parent.child_counts[xml_name] = count

        attr_name: str = xml_element_name_to_key(xml_name)
        if not hasattr(parent.element, private_field_name(attr_name)):
            return self._start_extension_child(parent, xml_name)

        assert self._module is not None, "読み込みモジュールが解決できませんでした"
        value_class: type[StBridgeElement] = getattr(
            self._module, xml_element_name_to_python_class_name(xml_name)
        )
        instance: StBridgeElement = value_class()
        field_info: _FieldInfo = parent.element._field_info(attr_name)
        max_occurs: int | None = field_info.max_occurs
        if max_occurs is not None and count > max_occurs:
            # 超過分はchildrenに追加せず、要素を読み終えてから不正値として退避する。
            return _Element(element=instance, xml_name=xml_name, excess_of=attr_name)
        if max_occurs != 1:
            children: Any = getattr(parent.element, private_field_name(attr_name))
            children.append(instance)
        else:
            setattr(parent.element, attr_name, instance)
        return _Element(element=instance, xml_name=xml_name)

    def _start_extension_child(self, parent: _Element, xml_name: str) -> _Element:
        instance: _StBridgeExtensionElement = _StBridgeExtensionElement(name=xml_name)
        parent.element._ensure_extension._get_children().append(instance)
        return _Element(element=instance, xml_name=xml_name)

    def _set_attributes(self, element: StBridgeElement, attrib: dict[str, str]) -> None:
        for key, value in attrib.items():
            raw_attr_name: str = _delete_namespace(key)
            attr_name: str = xml_attribute_name_to_python_attribute_name(raw_attr_name)
            if attr_name.startswith("xmlns"):
                continue
            element._set_attribute_by_str(attr_name, value, raw_attr_name=raw_attr_name)

    def _set_content(self, frame: _Element) -> None:
        if frame.text is None:
            return
        content: str = "".join(frame.text).strip()
        if not content:
            return
        element: StBridgeElement = frame.element
        py_attr_name: str = content_py_attr_name()
        field_info: _FieldInfo | None = element._fields.get(py_attr_name)
        if field_info is None:
            self._invalid_content(frame, content)
            return
        if field_info.xml_type in (
            "monolist",
            "monolist_id",
            "positiveIntegerList",
        ):
            setattr(element, py_attr_name, [int(item) for item in content.split()])
        elif field_info.xml_type == "monolist_length":
            setattr(element, py_attr_name, [float(item) for item in content.split()])
        else:
            setattr(element, py_attr_name, content)

    def _invalid_content(self, frame: _Element, content: str) -> None:
        reason: str = f"要素[{frame.xml_name}]は内容を持ちません"
        path_xml: str = frame.element._path_xml()
        self._reporter.error(
            message=f"{reason}。内容を不正値として退避しました",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
            xpath=path_xml,
            value=content,
        )
        frame.element._ensure_extension._set_invalid_value(
            _InvalidValue(
                kind=_FieldKind.CONTENT,
                value=content,
                path=path_xml,
                reason=reason,
            )
        )

    def _invalid_occurs(self, frame: _Element) -> None:
        parent: StBridgeElement = self._stack[-1].element
        excess_of: str | None = frame.excess_of
        assert excess_of is not None, "最大回数超過フィールド名が取得できませんでした"
        field_info: _FieldInfo = parent._field_info(excess_of)
        max_occurs: int | None = field_info.max_occurs
        assert max_occurs is not None, "最大回数が未定義です"
        count: int = self._stack[-1].child_counts[frame.xml_name]
        path_xml: str = f"{parent._path_xml()}/{frame.xml_name}"
        reason: str = f"要素[{frame.xml_name}]の最大回数[{max_occurs}]を超過しています"
        self._reporter.error(
            message=f"{reason}。超過分を不正値として退避しました",
            code=Code.SCHEMA_ERROR,
            phase=Phase.LOAD,
            xpath=path_xml,
            value=str(count),
            ref_value=f"<={max_occurs}",
        )
        parent._ensure_extension._set_invalid_value(
            _InvalidValue(
                kind=_FieldKind.ELEMENT,
                value=frame.element,
                path=path_xml,
                reason=reason,
            )
        )


def _delete_namespace(name: str) -> str:
    if "}" in name:
        return name.split("}", 1)[1]
    return name


def _read_version(attrib: dict[str, str]) -> str:
    for key, value in attrib.items():
        if _delete_namespace(key) == "version":
            return value
    raise SchemaError("ファイルにversionが含まれません")


def _get_module(version: str) -> ModuleType:
    module_import_path: str | None = VERSION_TO_MODULE_IMPORT_PATH.get(version)
    if module_import_path is None:
        raise UnsupportedStbVersionError(version)
    return import_module(module_import_path)
