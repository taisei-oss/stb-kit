# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import logging
from typing import Any

from stbkit.core.data_model.stb_v2_1_1 import StbModel, StBridge
from stbkit.core.stb_reporting import Code, LoggerReporter, Phase


def test_logger_reporter_report(capsys: Any) -> None:
    reporter: LoggerReporter = LoggerReporter(level=logging.INFO)
    stb = StBridge(version="2.1.1", stb_model=StbModel())
    reporter.info("test info", code=Code.TEST, phase=Phase.TEST, stb_element=stb)
    reporter.warning(
        "test warning", code=Code.TEST, phase=Phase.TEST, stb_element=stb.stb_model
    )
    captured = capsys.readouterr()
    assert "test info" in captured.err
    assert "test warning" in captured.err
    assert "/ST_BRIDGE/StbModel" in captured.err
