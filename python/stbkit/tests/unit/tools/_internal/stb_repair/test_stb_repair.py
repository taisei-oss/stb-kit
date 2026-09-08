# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest
from stbkit.core.data_model.stb_v2_1_1 import (
    VERSION,
    StbModel,
    StbNode,
    StbNodes,
    StBridge,
)

from stbkit.tools._internal.stb_repair._stb_repair import repair_stb


def test_repair_stb_required_float_fields() -> None:
    node: StbNode = StbNode(id=1, kind="ON_GRID")
    nodes: StbNodes = StbNodes(stb_node=[node])
    model: StbModel = StbModel(stb_nodes=nodes)
    stb: StBridge = StBridge(version=VERSION, stb_model=model)

    repair_stb(stb, reporter=None)

    repaired_node: StbNode = stb.stb_model.stb_nodes.stb_node[0]
    assert repaired_node.x == pytest.approx(0.0)
    assert repaired_node.y == pytest.approx(0.0)
    assert repaired_node.z == pytest.approx(0.0)


def test_repair_stb_missing_required_child() -> None:
    stb: StBridge = StBridge(version=VERSION)

    repair_stb(stb, reporter=None)

    assert stb.stb_common_or_none is not None
    assert stb.stb_common.project_name is not None
