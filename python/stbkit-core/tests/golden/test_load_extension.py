# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

from stbkit.testutils.fixture_repository import FixtureRepository

from stbkit.core.data_model.stb_v2_1_0 import VERSION, StBridge
from stbkit.core.stb_io import load


def test_read_extension(fixture_repository: FixtureRepository) -> None:
    fixture_path: Path = (
        fixture_repository.get_case("has_extension")
        .conversion_node_specs()[0]
        .golden_output_path
    )
    stb: StBridge = load(fixture_path, version=VERSION)
    assert stb.stb_model.stb_nodes.stb_node[0]._get_ext_attr("ext_attr_1") == "attr1"
    assert len(stb.stb_model._get_ext_children()) == 3
    assert stb.stb_model._get_ext_child(0)._xml_name() == "ExtElement1"
    assert stb.stb_model._get_ext_child(0)._get_ext_attr("id") == "1"
    assert stb.stb_model._get_ext_child(1)._xml_name() == "ExtElement1"
    assert stb.stb_model._get_ext_child(1)._get_ext_attr("id") == "2"
    assert stb.stb_model._get_ext_child(2)._xml_name() == "ExtElement2"
    assert stb.stb_model._get_ext_child(2)._get_ext_attr("id") == "2"
    assert (
        stb.stb_model._get_ext_child(2)._get_ext_child(0)._xml_name() == "ExtElement3"
    )
    assert (
        stb.stb_model._get_ext_child(2)._get_ext_child(0)._get_ext_attr("name") == "3"
    )
