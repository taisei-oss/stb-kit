# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from stbkit.core.data_model.stb_v2_1_1 import (
    StbCommon,
    StbExtensions,
    StbNode,
    StBridge,
)
from stbkit.core.stb_exceptions import NoneAccessError, SchemaError


def test_getter() -> None:
    node_none: StbNode = StbNode(x=None)
    with pytest.raises(NoneAccessError):
        _ = node_none.x
    node: StbNode = StbNode(x=100.0)
    assert node.x == 100.0


def test_getter_or_none() -> None:
    node_none: StbNode = StbNode(x=None)
    assert node_none.x_or_none is None
    node: StbNode = StbNode(x=100.0)
    assert node.x_or_none == 100.0


def test_setter() -> None:
    node: StbNode = StbNode()
    node.x = 100.0
    assert node.x == 100.0
    node.x = None  # type: ignore[assignment]
    assert node.x_or_none is None


def test_setter_or_none() -> None:
    node: StbNode = StbNode()
    node.x_or_none = 100.0
    assert node.x == 100.0
    node.x_or_none = None
    assert node.x_or_none is None


def test_setter_child_none() -> None:
    stb: StBridge = StBridge(stb_common=StbCommon(), stb_extensions=StbExtensions())
    assert stb.stb_common_or_none is not None
    assert stb.stb_extensions_or_none is not None
    # 必須項目にNoneを設定するとスキーマエラー
    with pytest.raises(SchemaError):
        stb.stb_common_or_none = None
    # 必須でなければそのまま設定できる
    stb.stb_extensions_or_none = None
    assert stb.stb_extensions_or_none is None
