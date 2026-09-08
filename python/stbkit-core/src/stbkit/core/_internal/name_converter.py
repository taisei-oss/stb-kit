# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
from typing import Final

RESERVED_WORDS: Final[set[str]] = {"as", "ensure"}
"""Pythonの予約語及び、基底クラスで利用している属性名。かぶったら末尾にアンダーバーを付ける。"""


def pascal_case_to_snake_case(input_string: str) -> str:
    """
    PascalCase -> snake_case。camelCase -> snake_caseにも対応。
    """
    if not input_string:
        return input_string

    # ColumnSSame -> ColumnS_Same などの対策
    result = re.sub(
        r"([A-Z]+)([A-Z][a-z])",
        r"\1_\2",
        input_string,
    )

    result = re.sub(
        r"([a-z0-9])([A-Z])",
        r"\1_\2",
        result,
    )

    return result.lower()


def snake_case_to_large_snake_case(input_string: str) -> str:
    return input_string.upper()


def snake_case_to_lower_camel_case(input_string: str) -> str:
    if not input_string:
        return input_string
    first, *rest = input_string.split("_")
    return first + "".join(part[:1].upper() + part[1:] for part in rest if part)


def xml_element_name_to_pascal_case(xml_element_name: str) -> str:
    result: str = (
        xml_element_name.replace("-", "_")
        .replace("_member", "_Member")
        .replace("_RC_", "Rc")
        .replace("_S_", "S")
        .replace("_SRC_", "Src")
        .replace("_CFT_", "Cft")
        .replace("ST_BRIDGE", "StBridge")
        .replace("NRBProperty", "NrbProperty")
        .replace("HDRProperty", "HdrProperty")
        .replace("LRBProperty", "LrbProperty")
        .replace("TRBProperty", "TrbProperty")
        .replace("SDRBProperty", "SdrbProperty")
        .replace("ESBProperty", "EsbProperty")
        .replace("RSBProperty", "RsbProperty")
        .replace("CSBProperty", "CsbProperty")
        .replace("CSLBProperty", "CslbProperty")
        .replace("CLBProperty", "ClbProperty")
        .replace("EGring", "Egring")
        .replace("FRring", "Frring")
        .replace("OSring", "Osring")
        .replace("Lip2C", "Lip2c")
    )
    suffix_map = [
        ("_2C", "2c"),
        ("_2L", "2l"),
        ("_BOX", "Box"),
        ("_C", "C"),
        ("_CFT", "Cft"),
        ("CMQ", "Cmq"),
        ("_CPRC", "Cprc"),
        ("_H", "H"),
        ("_HAssymmetric", "HAssymmetric"),
        ("_HAsymmetric", "HAsymmetric"),
        ("_L", "L"),
        ("_PHC", "Phc"),
        ("_PRC", "Prc"),
        ("_RC", "Rc"),
        ("_S", "S"),
        ("_SC", "Sc"),
        ("_SRC", "Src"),
        ("_ST", "St"),
        ("_T", "T"),
        ("NRB", "Nrb"),
        ("SP", "Sp"),
        ("HDR", "Hdr"),
        ("LRB", "Lrb"),
        ("TRB", "Trb"),
        ("SDRB", "Sdrb"),
        ("ESB", "Esb"),
        ("RSB", "Rsb"),
        ("CSB", "Csb"),
        ("CLSB", "Clsb"),
        ("CLB", "Clb"),
        ("LB", "Lb"),
        ("RB", "Rb"),
    ]
    for suffix, replacement in suffix_map:
        if result.endswith(suffix):
            result = result[: -len(suffix)] + replacement
            break
    return result


def xml_element_name_to_snake_case(xml_element_name: str) -> str:
    result: str = (
        pascal_case_to_snake_case(xml_element_name_to_pascal_case(xml_element_name))
        .replace("rc2_way", "rc_2_way")
        .replace("rc1_way", "rc_1_way")
        .replace("roll2c", "roll_2c")
        .replace("roll2l", "roll_2l")
        .replace("lip2c", "lip_2c")
    )
    return result


def xml_element_name_to_large_snake_case(xml_element_name: str) -> str:
    return snake_case_to_large_snake_case(
        xml_element_name_to_snake_case(xml_element_name)
    )


def xml_element_name_to_python_class_name(xml_element_name: str) -> str:
    return xml_element_name_to_pascal_case(xml_element_name)


def xml_attribute_name_to_snake_case(xml_attribute_name: str) -> str:
    return pascal_case_to_snake_case(xml_attribute_name)


def snake_case_to_python_attribute_name(name: str) -> str:
    if name in RESERVED_WORDS:
        name = f"{name}_"
    return name


def xml_element_name_to_key(element_name: str) -> str:
    return xml_attribute_name_to_python_attribute_name(
        xml_element_name_to_snake_case(element_name)
    )


def xml_attribute_name_to_python_attribute_name(attribute_name: str) -> str:
    return snake_case_to_python_attribute_name(
        xml_attribute_name_to_snake_case(attribute_name.replace("@", ""))
    )


def content_py_attr_name() -> str:
    return "content"


def private_field_name(key: str) -> str:
    return f"_{key}"


def property_name(key: str) -> str:
    return key


def or_none_property_name(key: str) -> str:
    return f"{key}_or_none"
