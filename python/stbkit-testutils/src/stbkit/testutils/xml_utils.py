# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import xml.etree.ElementTree as ET


def is_well_formed_xml(xml_string: str) -> bool:
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False
