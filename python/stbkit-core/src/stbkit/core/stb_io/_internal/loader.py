# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import codecs
import re

from ...stb_exceptions import SchemaError
from ...stb_typing import _FilePath


def _detect_encoding(xml_source: _FilePath | bytes) -> str:
    try:
        if isinstance(xml_source, bytes):
            xml_bytes = xml_source
        else:
            with open(xml_source, "rb") as file:
                xml_bytes = file.read(256)

        for bom, encoding in (
            (codecs.BOM_UTF8, "utf-8-sig"),
            (codecs.BOM_UTF32_BE, "utf-32-be"),
            (codecs.BOM_UTF32_LE, "utf-32-le"),
            (codecs.BOM_UTF16_BE, "utf-16-be"),
            (codecs.BOM_UTF16_LE, "utf-16-le"),
        ):
            if xml_bytes.startswith(bom):
                return encoding

        first_line = xml_bytes.splitlines()[0] if xml_bytes else b""
        first_line_text = first_line.decode("ascii", errors="ignore")

        if "<?xml" not in first_line_text:
            return "utf-8"

        match = re.search(r"encoding=[\"']([^\"']+)[\"']", first_line_text)
        if match:
            result: str = match.group(1).lower().replace("_", "-")
            if result == "shift-jis":
                return "cp932"
            else:
                return result

        return "utf-8"
    except (FileNotFoundError, OSError):
        # エンコーディングの検出に失敗した場合はデフォルトでutf-8を返す
        return "utf-8"


def _detect_version(xml: _FilePath | str) -> str:
    try:
        with open(xml, encoding=_detect_encoding(xml)) as f:
            xml_text: str = f.read(256)
    except (FileNotFoundError, OSError):
        if isinstance(xml, str):
            xml_text = xml[:256]
    result = re.search(r"<ST_BRIDGE[^>]*version\s*=\s*[\"']([^\"']+)[\"']", xml_text)
    if result:
        return result.group(1)
    else:
        raise SchemaError("ファイルにversionが含まれません")
