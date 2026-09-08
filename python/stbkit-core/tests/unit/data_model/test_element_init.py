# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid

import pytest

from stbkit.core.data_model.stb_v2_1_0 import StbNode, StbNodeIdOrder


def test_init() -> None:
    node_none: StbNode = StbNode()
    assert node_none is not None
    assert node_none.id_or_none is None
    assert node_none.x_or_none is None
    assert node_none.y_or_none is None
    assert node_none.z_or_none is None
    assert node_none.kind_or_none is None
    assert node_none.id_member_or_none is None
    assert node_none.guid_or_none is None

    guid: uuid.UUID = uuid.uuid4()
    kind: str = "ON_GRID"

    node: StbNode = StbNode(
        id=1, x=100.0, y=200.0, z=300.0, kind=kind, id_member=2, guid=guid
    )
    assert node.id == 1
    assert node.x == 100.0
    assert node.y == 200.0
    assert node.z == 300.0
    assert node.kind == kind
    assert node.id_member == 2
    assert node.guid == guid


def test_init_error() -> None:
    with pytest.raises(TypeError):
        _ = StbNode(100.0)  # type: ignore


def test_init_monolist() -> None:
    node_id_order: StbNodeIdOrder = StbNodeIdOrder(content=[1, 2, 3])
    assert node_id_order.content == [1, 2, 3]
