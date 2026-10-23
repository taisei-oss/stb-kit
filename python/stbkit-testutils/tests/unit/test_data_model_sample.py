# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import CollectingReporter
from stbkit.core.validation import validate_schema
from stbkit.testutils.data_model_sample.v2_0_2 import v2_0_2_has_node, v2_0_2_minimum
from stbkit.testutils.data_model_sample.v2_1_0 import (
    v2_1_0_has_monolist_id,
    v2_1_0_minimum,
)
from stbkit.testutils.data_model_sample.v2_1_1 import v2_1_1_minimum, v2_1_1_rc_column


def test_sample_validate() -> None:
    reporter: CollectingReporter = CollectingReporter()
    stbs = [
        v2_1_1_minimum(),
        v2_1_1_rc_column(),
        v2_1_0_minimum(),
        v2_1_0_has_monolist_id(),
        v2_0_2_minimum(),
        v2_0_2_has_node(),
    ]
    for stb in stbs:
        assert validate_schema(stb, reporter=reporter), reporter.report.to_text()
