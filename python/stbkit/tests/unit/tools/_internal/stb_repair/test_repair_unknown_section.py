# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from types import ModuleType

import pytest
from stbkit.core.stb_reporting import CollectingReporter
from stbkit.testutils.constants import models

from stbkit.tools._internal.stb_repair._common import Defaults, RepairContext
from stbkit.tools._internal.stb_repair._repair_unknown_section import (
    _get_unknown_section_id,
)


@pytest.mark.parametrize("module", models(start_version="2.0.2"))
def test_repair_unknown_section_get_unknown_section_id(module: ModuleType) -> None:
    context = RepairContext(
        stb=module.StBridge(),
        defaults=Defaults(steel_strength="SS400", default_length=0.1),
        reporter=CollectingReporter(),
    )
    unknown_section_id = _get_unknown_section_id(context)
    assert unknown_section_id == 1
