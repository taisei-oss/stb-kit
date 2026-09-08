# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from io import StringIO
from pathlib import Path
from typing import Final

import pytest

from stbkit.core._internal.constants import DEFAULT_MAX_XML_DEPTH
from stbkit.core._internal.io_text import load_text
from stbkit.core.data_model.stb_v2_1_1 import VERSION
from stbkit.core.stb_exceptions import XmlLimitExceededError, XmlLimitKind
from stbkit.core.stb_io import load, loads
from stbkit.core.stb_reporting import CollectingReporter, NullReporter

_SAMPLE_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.1"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <StbCommon project_name="limits" app_name="stbkit" app_version="0.0.0"/>
 <StbModel/>
</ST_BRIDGE>
"""


def _nested_stb(depth: int) -> str:
    """拡張要素の階層が大きいST-BridgeのXML文字列を生成する。"""
    nest: int = depth - 1
    opening: str = "".join(f"<Nested{index}>" for index in range(nest))
    closing: str = "".join(f"</Nested{index}>" for index in reversed(range(nest)))

    def def_tag(index: int) -> str:
        return f'<StbExtElement object_name="Nested{index - 1}" element_name="Nested{index}"/>'

    definition: str = "".join(def_tag(index) for index in range(1, nest))

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.1"'
        ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        ' xmlns:xs="http://www.w3.org/2001/XMLSchema">'
        '<StbCommon project_name="limits" app_name="stbkit" app_version="0.0.0"/>'
        "<StbModel/>"
        f"{opening}{closing}"
        "<StbExtensions>"
        '<StbExtension identifier="stbkit-test">'
        f'<StbExtElement object_name="ST_BRIDGE" element_name="Nested0"/>'
        f" {definition}"
        "</StbExtension>"
        "</StbExtensions>"
        "</ST_BRIDGE>\n"
    )


def test_validate_nested_stb() -> None:
    xml: str = _nested_stb(5)
    assert xml.count("<Nested") == 4
    reporter: CollectingReporter = CollectingReporter()
    _ = loads(xml, version=VERSION, reporter=reporter)
    assert reporter.is_valid(), reporter.report.to_text()


def test_loads_oversized_xml() -> None:
    with pytest.raises(XmlLimitExceededError) as error:
        loads(_SAMPLE_STB, max_size=10, reporter=NullReporter())

    assert error.value.kind == XmlLimitKind.SIZE


def test_load_oversized_file(tmp_path: Path) -> None:
    stb_path: Path = tmp_path / "oversized.stb"
    stb_path.write_text(_SAMPLE_STB, encoding="utf-8")

    with pytest.raises(XmlLimitExceededError) as error:
        load(stb_path, max_size=10, reporter=NullReporter())

    assert error.value.kind == XmlLimitKind.SIZE


def test_loads_too_deep_xml() -> None:
    with pytest.raises(XmlLimitExceededError) as error:
        loads(
            _nested_stb(DEFAULT_MAX_XML_DEPTH + 1),
            max_size=len(_SAMPLE_STB) * 100,
            reporter=NullReporter(),
        )

    assert error.value.kind == XmlLimitKind.DEPTH

    # 上限ちょうどはOK
    loads(_nested_stb(DEFAULT_MAX_XML_DEPTH), reporter=NullReporter())


def test_load_text_oversized_file(tmp_path: Path) -> None:
    xml_path: Path = tmp_path / "oversized.stb"
    xml_path.write_text(_SAMPLE_STB, encoding="utf-8")

    with pytest.raises(XmlLimitExceededError):
        load_text(xml_path, encoding="utf-8", max_size=10)


def test_load_text_stops_reading_at_limit() -> None:
    """サイズオーバーは読み込みを打ち切る"""
    str_io: StringIO = StringIO("<root>" + "<Nested/>" * 100 + "</root>")

    with pytest.raises(XmlLimitExceededError) as error:
        load_text(str_io, encoding="utf-8", max_size=100)

    assert error.value.kind == XmlLimitKind.SIZE
    # 上限を超える分を読み込まないことが、この上限の目的である。
    assert str_io.tell() == 101


def test_load_text_can_read_max_size() -> None:
    """上限までのサイズは読み込める"""
    str_io: StringIO = StringIO("a" * 100)
    assert load_text(str_io, encoding="utf-8", max_size=100) == "a" * 100
