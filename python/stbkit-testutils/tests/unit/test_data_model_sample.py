# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import CollectingReporter
from stbkit.core.validation import validate_schema
from stbkit.testutils import data_model_sample


def test_sample_validate() -> None:
    reporter: CollectingReporter = CollectingReporter()
    stbs = [
        data_model_sample.v2_1_0_minimum(),
        data_model_sample.v2_1_0_has_monolist_id(),
        data_model_sample.v2_0_2_minimum(),
        data_model_sample.v2_0_2_has_node(),
    ]
    for stb in stbs:
        assert validate_schema(stb, reporter=reporter), reporter.report.to_text()
