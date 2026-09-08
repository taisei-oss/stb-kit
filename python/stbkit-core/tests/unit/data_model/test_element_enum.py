# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from stbkit.core.data_model.stb_v2_1_0 import (
    StbNode,
    StbNodeKind,
    StbSecBaseProduct,
    StbSecBaseProductDirectionType,
)
from stbkit.core.stb_exceptions import NoneAccessError, TypeMismatchError


def test_element_str_enum() -> None:
    node: StbNode = StbNode()
    assert node.kind_or_none is None

    node.kind = StbNodeKind.ON_GRID
    assert node.kind is StbNodeKind.ON_GRID

    node.kind = StbNodeKind.ON_GIRDER
    assert node.kind is StbNodeKind.ON_GIRDER

    node.kind = "ON_GRID"
    assert node.kind is StbNodeKind.ON_GRID

    node.kind_or_none = "ON_GIRDER"
    assert node.kind_or_none is StbNodeKind.ON_GIRDER

    with pytest.raises(TypeMismatchError):
        node.kind = 1  # type:ignore[assignment]

    with pytest.raises(TypeMismatchError):
        node.kind_or_none = 1  # type:ignore[assignment]

    node.kind_or_none = None
    assert node.kind_or_none is None

    with pytest.raises(NoneAccessError):
        _ = node.kind


def test_element_int_enum() -> None:
    sec: StbSecBaseProduct = StbSecBaseProduct()
    assert sec.direction_type_or_none is None

    sec.direction_type = StbSecBaseProductDirectionType.VALUE_90
    assert sec.direction_type is StbSecBaseProductDirectionType.VALUE_90

    sec.direction_type = 180
    assert sec.direction_type is StbSecBaseProductDirectionType.VALUE_180

    sec.direction_type_or_none = 90
    assert sec.direction_type_or_none is StbSecBaseProductDirectionType.VALUE_90

    with pytest.raises(TypeMismatchError):
        sec.direction_type = "180"  # type:ignore[assignment]

    with pytest.raises(TypeMismatchError):
        sec.direction_type_or_none = "180"  # type:ignore[assignment]

    sec.direction_type_or_none = None
    assert sec.direction_type_or_none is None

    with pytest.raises(NoneAccessError):
        _ = sec.direction_type
