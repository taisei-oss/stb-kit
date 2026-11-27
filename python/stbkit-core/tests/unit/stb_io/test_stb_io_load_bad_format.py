# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Final
from uuid import UUID

import pytest
from stbkit.testutils.data_model_sample.v2_1_1 import v2_1_1_minimum

from stbkit.core.stb_io import dumps, loads
from stbkit.core.stb_reporting import CollectingReporter

_STB_WITH_NUMERIC_BOOL: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.1">
 <StbCommon project_name="numeric_bool_error" app_name="stbkit" app_version="0.0.0"/>
 <StbModel>
  <StbNodes>
   <StbNode id="1" X="0" Y="0" Z="0" kind="ON_GRID"/>
   <StbNode id="2" X="1" Y="0" Z="0" kind="ON_GRID"/>
  </StbNodes>
  <StbMembers>
   <StbGirders>
    <StbGirder id="1" id_node_start="1" id_node_end="2" id_section="1"
      kind_structure="RC" isFoundation="1"/>
   </StbGirders>
  </StbMembers>
  <StbSections>
   <StbSecBeam_RC id="1" name="test">
    <StbSecFigureBeam_RC order="1">
     <StbSecBeamStraight width="400" depth="700"/>
    </StbSecFigureBeam_RC>
   </StbSecBeam_RC>
  </StbSections>
 </StbModel>
</ST_BRIDGE>
"""


def test_numeric_bool_error() -> None:
    """数値のboolは読み込めるがエラーを記録する"""
    reporter: CollectingReporter = CollectingReporter()

    stb = loads(_STB_WITH_NUMERIC_BOOL, version="2.1.1", reporter=reporter)
    assert stb.stb_model.stb_members.stb_girders.stb_girder[0].is_foundation is True
    assert len(reporter.report) == 1
    assert reporter.report[0].message == (
        'ST-Bridgeはbool値は"true"と記載する必要があります'
    )


@pytest.mark.parametrize(
    ("guid", "has_error"),
    [
        ("1234567890abcdef1234567890abcdef", False),
        ("1234567890ABCDEF1234567890ABCDEF", True),
        ("12345678-90ab-cdef-1234-567890abcdef", True),
        ("{12345678-90ab-cdef-1234-567890abcdef}", True),
        ("urn:uuid:12345678-90ab-cdef-1234-567890abcdef", True),
    ],
)
def test_uuid_string_format_error(guid: str, has_error: bool) -> None:
    stb_template = v2_1_1_minimum()
    stb_template.stb_common.guid = UUID("1234567890abcdef1234567890abcdef")
    xml_template: str = dumps(stb_template)
    xml = xml_template.replace(
        'guid="1234567890abcdef1234567890abcdef"', f'guid="{guid}"'
    )
    reporter = CollectingReporter()
    stb = loads(xml, version="2.1.1", reporter=reporter)
    assert stb.stb_common.guid == UUID(guid)
    len_report: int = 1 if has_error else 0
    assert len(reporter.report) == len_report
    if has_error:
        assert (
            "GUIDは32桁の16進数値を文字列表現した値とする必要があります"
            in reporter.report[0].message
        )
