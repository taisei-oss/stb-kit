# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import io
import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING
from xml.dom import minidom

from ..._internal.constants import PACKAGE_NAME, PACKAGE_VERSION
from ..._internal.xml_value_converter import any_to_xml_str
from ...data_model.common import StBridgeElement, StBridgeRoot
from ...stb_exceptions import SchemaError
from ...stb_reporting import Code, Phase, Reporter

if TYPE_CHECKING:
    from typing import Any


def set_element_data(
    xml_element: ET.Element,
    stb_element: StBridgeElement,
    *,
    reporter: Reporter,
    _strict: bool = True,
) -> None:
    for key, field_ in stb_element._fields.items():
        attr_name: str = key
        if attr_name.startswith("_"):
            continue
        value: Any = getattr(stb_element, f"_{attr_name}")
        if value is None:
            if field_.required:
                if _strict:
                    raise SchemaError(
                        f"{stb_element._name_for_log()}の{attr_name}は必須です"
                    )
                else:
                    reporter.error(
                        f"{stb_element._name_for_log()}の{attr_name}は必須です",
                        code=Code.SCHEMA_ERROR,
                        phase=Phase.DUMP,
                    )
            continue
        elif isinstance(value, list) and not value:
            continue
        elif stb_element._is_attr(attr_name):
            xml_value = any_to_xml_str(value)
            if xml_value == "":
                if field_.required:
                    if _strict:
                        raise SchemaError(
                            f"{stb_element._name_for_log()}の{attr_name}は必須です"
                        )
                    else:
                        reporter.error(
                            f"{stb_element._name_for_log()}の{attr_name}は必須です",
                            code=Code.SCHEMA_ERROR,
                            phase=Phase.DUMP,
                        )
                continue
            xml_element.set(
                stb_element._xml_name(attr_name),
                xml_value,
            )
        elif stb_element._is_content(attr_name):
            if isinstance(value, list):
                text = " ".join(any_to_xml_str(item) for item in value)
            else:
                text = any_to_xml_str(value)
            xml_element.text = text
        elif isinstance(value, StBridgeElement):
            child: ET.Element = ET.SubElement(xml_element, value._xml_name())
            set_element_data(child, value, reporter=reporter, _strict=_strict)
            if (
                len(child) == 0
                and not child.attrib
                and (child.text is None or child.text.strip() == "")
            ):
                xml_element.remove(child)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, StBridgeElement):
                    child = ET.SubElement(xml_element, item._xml_name())
                    set_element_data(child, item, reporter=reporter, _strict=_strict)
                else:
                    raise TypeError(
                        f"{stb_element._name_for_log()}の{attr_name}が"
                        "StBridgeElementではありません"
                    )
        else:
            name = stb_element._name_for_log()
            message = f"{name}の{attr_name}は想定していない属性です"
            raise RuntimeError(message)
    if stb_element._extension:
        if stb_element._extension._attributes:
            for (
                ext_attr_name,
                ext_attr_value,
            ) in stb_element._extension._attributes.items():
                xml_element.set(ext_attr_name, str(ext_attr_value))
        if stb_element._extension._children:
            for ext_child in stb_element._extension._children:
                child = ET.SubElement(xml_element, ext_child._xml_name())
                set_element_data(child, ext_child, reporter=reporter, _strict=_strict)


def to_xml_tree(
    stb: StBridgeRoot, *, reporter: Reporter, _strict: bool = True
) -> ET.Element:
    root: ET.Element = ET.Element("ST_BRIDGE")
    root.set("xmlns:xs", "http://www.w3.org/2001/XMLSchema")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    set_element_data(root, stb, reporter=reporter, _strict=_strict)
    root.set("xmlns", "https://www.building-smart.or.jp/dl")
    return root


def set_app_name_and_version(
    stb: StBridgeRoot,
    *,
    app_name: str | None = None,
    app_version: str | None = None,
    reporter: Reporter,
) -> None:
    stb._set_version(reporter=reporter, phase=Phase.DUMP)
    if (app_name and not app_version) or (not app_name and app_version):
        raise ValueError("app_nameとapp_versionは両方指定、または両方省略してください")
    if app_name:
        convert_app_name: str | None = PACKAGE_NAME
    else:
        app_name = PACKAGE_NAME
        convert_app_name = None
    if app_version:
        convert_app_version: str | None = PACKAGE_VERSION
    else:
        app_version = PACKAGE_VERSION
        convert_app_version = None
    stb_common = stb._ensure_child("stb_common")
    if hasattr(stb_common, "app_name_or_none"):
        stb_common.app_name_or_none = app_name
    if hasattr(stb_common, "app_version_or_none"):
        stb_common.app_version_or_none = app_version
    if hasattr(stb_common, "convert_app_name_or_none"):
        stb_common.convert_app_name_or_none = convert_app_name
    if hasattr(stb_common, "convert_app_version_or_none"):
        stb_common.convert_app_version_or_none = convert_app_version


def _raw_dumps(stb: StBridgeRoot, reporter: Reporter, _strict: bool = True) -> str:
    et_element: ET.Element = to_xml_tree(stb, reporter=reporter, _strict=_strict)
    doc: minidom.Document = minidom.parseString(ET.tostring(et_element, "utf-8"))
    f: io.StringIO = io.StringIO()
    doc.writexml(f, encoding="UTF-8", newl="\n", indent="", addindent=" ")
    return f.getvalue()
