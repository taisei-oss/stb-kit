# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.testutils import xml_utils


def test_is_well_formed_xml() -> None:
    assert xml_utils.is_well_formed_xml("<root><child>Content</child></root>")
    assert xml_utils.is_well_formed_xml("<root>\n  <child>Content</child>\n</root>")
    assert xml_utils.is_well_formed_xml(
        '<root attr="value" > <child id="1"> Content </child> </root>'
    )
    assert not xml_utils.is_well_formed_xml("<root><child>Content</root>")
    assert not xml_utils.is_well_formed_xml("<root>\n  <child>Content\n</root>")
    assert xml_utils.is_well_formed_xml(
        '<root attr="value"><child id="1">Content</child></root>'
    )
    assert xml_utils.is_well_formed_xml('<root><item key="a" enabled="true" /></root>')
    assert not xml_utils.is_well_formed_xml(
        "<root attr=value><child>Content</child></root>"
    )
    assert not xml_utils.is_well_formed_xml(
        '<root><child id="1">Content</child id="1"></root>'
    )
