# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""StudioAppへ渡すReporter結果文字列を生成するモジュール"""

import json
from dataclasses import asdict
from pathlib import Path

from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_io import load, loads
from stbkit.core.stb_reporting import (
    CollectingReporter,
    NullReporter,
    Reporter,
    ReportingResult,
)
from stbkit.core.validation import validate_schema


def _read_source(source: str, is_path: bool, *, reporter: Reporter) -> StBridgeRoot:
    """Rustから渡されたST-Bridgeデータを読み込む

    Rust側の読み込みの都合でpathで渡される場合と文字列で渡される場合がある。
    """
    if is_path:
        return load(Path(source), reporter=reporter)
    return loads(source, reporter=reporter)


def load_report_json(source: str, is_path: bool) -> str:
    reporter: CollectingReporter = CollectingReporter()
    _read_source(source, is_path, reporter=reporter)
    return _report_to_json(reporter.report)


def validation_report_json(source: str, is_path: bool) -> str:
    stb: StBridgeRoot = _read_source(source, is_path, reporter=NullReporter())
    reporter: CollectingReporter = CollectingReporter()
    validate_schema(stb, reporter=reporter, require_xsd=False)
    return _report_to_json(reporter.report)


def _report_to_json(report: ReportingResult) -> str:
    payload = [asdict(item) for item in report]
    return json.dumps(payload, ensure_ascii=False)
