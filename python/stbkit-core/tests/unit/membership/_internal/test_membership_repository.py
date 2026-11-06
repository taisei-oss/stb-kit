# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Any

import pytest

from stbkit.core.data_model import stb_v2_0_0, stb_v2_1_1
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.membership._internal.membership_repository import (
    _ColumnLike,
    _FoundationLike,
    _GirderLike,
    _OpenLike,
    _PanelZoneArrangementLike,
    _PlateLike,
    _StbAxesLike,
    _StbModelLike,
    _StbNodeIdLike,
    _StbNodeIdListLike,
    _StbNodeIdOrderLike,
    _StbParallelAxesLike,
    _StbParallelAxisLike,
    _StBridgeLike,
    _StbStoriesLike,
    _StbStoryLike,
)


@pytest.mark.parametrize("st_bridge_module", [stb_v2_0_0, stb_v2_1_1])
def test_membership_repository_protocol(st_bridge_module: Any) -> None:
    assert isinstance(st_bridge_module.StBridgeElement(), StBridgeElement)
    assert isinstance(st_bridge_module.StBridge(), _StBridgeLike)
    assert isinstance(st_bridge_module.StbModel(), _StbModelLike)
    assert isinstance(st_bridge_module.StbAxes(), _StbAxesLike)
    assert isinstance(st_bridge_module.StbNodeId(), _StbNodeIdLike)
    assert isinstance(st_bridge_module.StbNodeIdList(), _StbNodeIdListLike)
    assert isinstance(st_bridge_module.StbNodeIdOrder(), _StbNodeIdOrderLike)
    assert isinstance(st_bridge_module.StbParallelAxes(), _StbParallelAxesLike)
    assert isinstance(st_bridge_module.StbParallelAxis(), _StbParallelAxisLike)
    assert isinstance(st_bridge_module.StbStories(), _StbStoriesLike)
    assert isinstance(st_bridge_module.StbStory(), _StbStoryLike)
    assert isinstance(st_bridge_module.StbColumn(), _ColumnLike)
    assert isinstance(st_bridge_module.StbPost(), _ColumnLike)
    assert isinstance(st_bridge_module.StbGirder(), _GirderLike)
    assert isinstance(st_bridge_module.StbBeam(), _GirderLike)
    assert isinstance(st_bridge_module.StbBrace(), _GirderLike)
    assert isinstance(st_bridge_module.StbSlab(), _PlateLike)
    assert isinstance(st_bridge_module.StbWall(), _PlateLike)
    if st_bridge_module is not stb_v2_0_0:
        assert isinstance(st_bridge_module.StbIsolatingDevice(), _GirderLike)
        assert isinstance(st_bridge_module.StbDampingDevice(), _GirderLike)
        assert isinstance(st_bridge_module.StbFrameDampingDevice(), _PlateLike)
    assert isinstance(st_bridge_module.StbFooting(), _FoundationLike)
    assert isinstance(st_bridge_module.StbStripFooting(), _GirderLike)
    assert isinstance(st_bridge_module.StbPile(), _FoundationLike)
    assert isinstance(st_bridge_module.StbFoundationColumn(), _FoundationLike)
    assert isinstance(st_bridge_module.StbParapet(), _GirderLike)
    if st_bridge_module is not stb_v2_0_0:
        assert isinstance(st_bridge_module.StbOpenArrangement(), _OpenLike)
        assert isinstance(st_bridge_module.StbPenetrationArrangement(), _OpenLike)
        assert isinstance(st_bridge_module.StbJointArrangement(), _OpenLike)
        assert isinstance(
            st_bridge_module.StbPanelZoneArrangement(), _PanelZoneArrangementLike
        )
        assert isinstance(st_bridge_module.StbConnectionArrangement(), _FoundationLike)
