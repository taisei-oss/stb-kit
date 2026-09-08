# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from typing import Any

from stbkit.api import StBridgeRoot, dumps, loads
from stbkit.api.experimental import from_dict, to_dict
from stbkit.core.data_model._internal.filter_option import FilterOption
from stbkit.core.stb_io._internal.loader import _detect_encoding
from stbkit.tools._internal.stb_repair._stb_repair import repair_stb

from .comparators import XmlComparator


def roundtrip_stb(
    input: Path,
    *,
    enable_repair: bool = False,
    filter_option: FilterOption | None = None,
    ignore_application_information: bool = False,
    ignore_empty_attributes: bool = False,
    ignore_empty_element: bool = False,
    sort_elements: bool = False,
) -> None:
    encoding: str = _detect_encoding(input)
    in_str: str = input.read_text(encoding=encoding)
    stb_in: StBridgeRoot = loads(in_str)
    if enable_repair:
        repair_stb(stb_in, reporter=None)
    out_str: str = dumps(stb_in)
    xml_comparator: XmlComparator = XmlComparator(
        ignore_application_information=ignore_application_information,
        ignore_empty_attributes=ignore_empty_attributes,
        ignore_empty_element=ignore_empty_element,
        filter_option=filter_option,
        sort_elements=sort_elements,
    )
    xml_comparator.assert_equal(
        in_str,
        out_str,
        message="STBのラウンドトリップに失敗しました",
    )


def roundtrip_dict(input: Path) -> None:
    encoding: str = _detect_encoding(input)
    in_str: str = input.read_text(encoding=encoding)
    stb_in: StBridgeRoot = loads(in_str)

    dict_a: dict[str, Any] = to_dict(stb_in)
    stb_load: StBridgeRoot = from_dict(dict_a)
    dict_b: dict[str, Any] = to_dict(stb_load)
    assert dict_a == dict_b
