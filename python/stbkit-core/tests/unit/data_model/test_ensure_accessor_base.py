# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.api.stb_latest import StbModel, StBridge

from stbkit.core.data_model.common import StBridgeElement, _EnsureAccessorBase


def test_ensure_accessor_base_getattr_none() -> None:
    stb: StBridge = StBridge()
    assert stb.stb_model_or_none is None
    ensure: _EnsureAccessorBase = _EnsureAccessorBase(stb)
    new_instance: StBridgeElement = ensure.stb_model()  # type:ignore[attr-defined]
    assert isinstance(new_instance, StbModel)
    assert stb.stb_model is new_instance


def test_ensure_accessor_base_getattr_not_none() -> None:
    stb: StBridge = StBridge()
    stb_model: StbModel = StbModel()
    stb.stb_model = stb_model
    ensure: _EnsureAccessorBase = _EnsureAccessorBase(stb)
    new_instance: StBridgeElement = ensure.stb_model()  # type:ignore[attr-defined]
    assert isinstance(new_instance, StbModel)
    assert new_instance is stb_model
    assert stb.stb_model is stb_model
