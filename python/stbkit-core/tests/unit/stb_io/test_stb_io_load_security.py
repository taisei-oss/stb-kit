# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import xml.etree.ElementTree as ET
from typing import Final

import pytest

from stbkit.core.stb_exceptions import UnsafeXmlError
from stbkit.core.stb_io import loads
from stbkit.core.stb_io._internal.stream_reader import check_no_doctype
from stbkit.core.stb_reporting import NullReporter
from stbkit.core.validation import validate_schema

# 安全なXML
_VALID_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="safe" app_name="stbkit" app_version="0.0.0"/>
 <StbModel/>
</ST_BRIDGE>
"""

# 内部実体定義を含むXML
_INTERNAL_ENTITY_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ST_BRIDGE [ <!ENTITY name "leaked"> ]>
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="&name;" app_name="stbkit" app_version="0.0.0"/>
</ST_BRIDGE>
"""

# エンティティ爆発のXML
_BILLION_LAUGHS_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ST_BRIDGE [
 <!ENTITY a "xxxxxxxxxx">
 <!ENTITY b "&a;&a;&a;&a;&a;&a;&a;&a;&a;&a;">
 <!ENTITY c "&b;&b;&b;&b;&b;&b;&b;&b;&b;&b;">
 <!ENTITY d "&c;&c;&c;&c;&c;&c;&c;&c;&c;&c;">
]>
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="&d;" app_name="stbkit" app_version="0.0.0"/>
</ST_BRIDGE>
"""

# 外部DTD参照を含むXML
_EXTERNAL_ENTITY_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ST_BRIDGE SYSTEM "http://example.invalid/evil.dtd">
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="external" app_name="stbkit" app_version="0.0.0"/>
</ST_BRIDGE>
"""

# DTDなしの未定義実体参照: セキュリティ例外ではなくXML構文エラーとなる
_UNDEFINED_ENTITY_STB: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="&undefined;" app_name="stbkit" app_version="0.0.0"/>
</ST_BRIDGE>
"""


@pytest.mark.parametrize(
    "xml_data",
    [_INTERNAL_ENTITY_STB, _BILLION_LAUGHS_STB, _EXTERNAL_ENTITY_STB],
)
def test_loads_doctype(xml_data: str) -> None:
    """DOCTYPE宣言があるXMLは、読み込み前に拒否する。"""
    with pytest.raises(UnsafeXmlError):
        loads(xml_data, reporter=NullReporter())


def test_loads_undefined_entity() -> None:
    """DTDのない実体参照は、XMLの構文エラーとして扱う。"""
    with pytest.raises(ET.ParseError):
        loads(_UNDEFINED_ENTITY_STB, reporter=NullReporter())


def test_check_no_doctype_valid() -> None:
    check_no_doctype(_VALID_STB)


def test_check_no_doctype_invalid() -> None:
    with pytest.raises(UnsafeXmlError):
        check_no_doctype(_INTERNAL_ENTITY_STB)


def test_check_no_doctype_ignores_doctype_in_comment() -> None:
    """コメント内の記述は無視する"""
    xml_data: str = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<!-- <!DOCTYPE ST_BRIDGE [ <!ENTITY a 'x'> ]> -->\n"
        '<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.1"/>\n'
    )

    check_no_doctype(xml_data)


def test_check_no_doctype_broken_xml() -> None:
    """XMLとして壊れている場合は無視する(そのごのXMLパーサでの検証でエラーになる)"""
    check_no_doctype("<ST_BRIDGE><unclosed>")


def test_validate_schema_unsafe_xml() -> None:
    """XSDスキーマチェックへXMLを渡す前に拒否する。"""
    with pytest.raises(UnsafeXmlError):
        validate_schema(_INTERNAL_ENTITY_STB, reporter=NullReporter())
