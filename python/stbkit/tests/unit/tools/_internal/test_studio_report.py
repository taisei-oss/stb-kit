# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
from pathlib import Path
from typing import Any, Final

from stbkit.tools._internal.studio_report import (
    load_report_json,
    validation_report_json,
)

INVALID_XML: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE version="2.1.0">
</ST_BRIDGE>
"""


def _report(json_text: str) -> list[dict[str, Any]]:
    value: object = json.loads(json_text)
    assert isinstance(value, list)
    return value


def test_load_report_json() -> None:
    report = _report(load_report_json(INVALID_XML, False))

    assert report
    assert all("severity" in item and "message" in item for item in report)


def test_validation_report_json() -> None:
    report = _report(validation_report_json(INVALID_XML, False))

    assert report
    assert all(item["phase"] == "validate" for item in report)
    assert not any("xsd" in str(item["message"]).lower() for item in report)


def _without_timestamp(report: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {key: value for key, value in item.items() if key != "timestamp"}
        for item in report
    ]


def test_studio_report_same_path_and_xml(tmp_path: Path) -> None:
    stb_path = tmp_path / "invalid.stb"
    stb_path.write_text(INVALID_XML, encoding="utf-8")

    assert _without_timestamp(
        _report(load_report_json(str(stb_path), True))
    ) == _without_timestamp(_report(load_report_json(INVALID_XML, False)))
    assert _without_timestamp(
        _report(validation_report_json(str(stb_path), True))
    ) == _without_timestamp(_report(validation_report_json(INVALID_XML, False)))
