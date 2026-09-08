# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest
from stbkit.api.stb_latest import (
    StbModel,
    StbNode,
    StbNodes,
    StBridge,
    StbSections,
)

from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_exceptions import NoneAccessError


def test_none_access() -> None:
    stb: StBridge = StBridge()
    # Noneである属性はnoneAccessErrorが発生する
    with pytest.raises(NoneAccessError):
        _ = stb.stb_model
    # NoneAccessErrorはAttributeErrorでもあるため、AttributeErrorも発生する
    with pytest.raises(AttributeError):
        _ = stb.stb_model
    # AttrubuteErrorが発生するためhasattrはFalseを返す
    assert not hasattr(stb, "stb_model")

    # 属性に値をセットする
    _ = stb.ensure.stb_model()
    # 値がセットされているためエラーは発生しない
    _ = stb.stb_model
    # hasattrもTrueを返す
    assert hasattr(stb, "stb_model")


def test_create_instance() -> None:
    stb: StBridge = StBridge()
    new_instance: StBridgeElement = stb._create_instance("StbNode")
    assert isinstance(new_instance, StbNode)


def test_create_child_instance() -> None:
    stb: StBridge = StBridge()
    new_instance: StBridgeElement = stb._create_child_instance("stb_model")
    assert isinstance(new_instance, StbModel)


def test_ensure_child_none() -> None:
    stb: StBridge = StBridge()
    assert stb.stb_model_or_none is None
    new_instance: StBridgeElement = stb._ensure_child("stb_model")
    assert isinstance(new_instance, StbModel)
    assert stb.stb_model is new_instance


def test_ensure_child_not_none() -> None:
    stb: StBridge = StBridge()
    stb_model: StbModel = StbModel()
    stb.stb_model = stb_model
    new_instance: StBridgeElement = stb._ensure_child("stb_model")
    assert isinstance(new_instance, StbModel)
    assert new_instance is stb_model
    assert stb.stb_model is stb_model


def test_ensure_none() -> None:
    stb: StBridge = StBridge()
    assert stb.stb_ana_models_or_none is None
    stb_model: StbModel = stb.ensure.stb_model()
    assert isinstance(stb_model, StbModel)
    assert stb.stb_model is stb_model


def test_ensure_not_none() -> None:
    stb: StBridge = StBridge()
    stb_model: StbModel = StbModel()
    stb.stb_model = stb_model
    stb_model2: StbModel = stb.ensure.stb_model()
    isinstance(stb_model2, StbModel)
    assert stb_model is stb_model2
    assert stb.stb_model is stb_model2


def test_xml_name_of_attribute_field() -> None:
    node: StbNode = StbNode()
    assert node._xml_name("x") == "X"
    assert node._xml_name("kind") == "kind"


def test_xml_name_of_child_field() -> None:
    stb: StBridge = StBridge()
    assert stb._xml_name("stb_model") == "StbModel"
    assert StbSections()._xml_name("stb_sec_beam_rc") == "StbSecBeam_RC"


def test_xml_name_without_attr_name() -> None:
    assert StbModel()._xml_name() == "StbModel"
    assert StbModel._xml_class_name() == "StbModel"


def test_child_class() -> None:
    assert StBridge._child_class("stb_model") is StbModel
    assert StbNodes._child_class("stb_node") is StbNode


def test_child_class_error() -> None:
    with pytest.raises(ValueError):
        StbNode._child_class("x")
    with pytest.raises(ValueError):
        StbNode._child_class("not_exist")
