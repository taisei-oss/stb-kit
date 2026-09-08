# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

from stbkit.api import load
from stbkit.testutils.fixture_repository import FixtureRepository

from stbkit.core.data_model.stb_v2_1_0 import VERSION, StbNodeKind, StBridge


def test_load_enum(fixture_repository: FixtureRepository) -> None:
    """制限値がある値がEnumとして読み込まれているかのテスト"""
    fixture_path: Path = (
        fixture_repository.get_case("column_s")
        .conversion_node_specs()[0]
        .golden_output_path
    )
    stb: StBridge = load(fixture_path, version=VERSION)
    assert stb.stb_model.stb_nodes.stb_node[0].kind is StbNodeKind.ON_GRID
