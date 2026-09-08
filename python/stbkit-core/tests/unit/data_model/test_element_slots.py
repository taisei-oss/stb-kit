# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from stbkit.core.data_model import stb_v2_1_0


def test_slots() -> None:
    """スロットが適切に設定されているかのテスト"""

    # StbNodeクラスに__slots__が設定されている
    assert hasattr(stb_v2_1_0.StbNode, "__slots__")

    # スロットに各フィールドのプライベート変数名が含まれている
    assert "_id" in stb_v2_1_0.StbNode.__slots__
    assert "_guid" in stb_v2_1_0.StbNode.__slots__
    assert "_x" in stb_v2_1_0.StbNode.__slots__
    assert "_y" in stb_v2_1_0.StbNode.__slots__
    assert "_z" in stb_v2_1_0.StbNode.__slots__
    assert "_kind" in stb_v2_1_0.StbNode.__slots__
    assert "_id_member" in stb_v2_1_0.StbNode.__slots__

    # StbNodeクラスの__slots__に規定クラスの属性である_parent_refが含まれている
    assert "_parent_ref" in stb_v2_1_0.StbNode.__slots__

    # スロットの数がフィールド数+3であること
    assert len(stb_v2_1_0.StbNode.__slots__) == 9

    # スロットに定義されていない属性を設定しようとするとAttributeErrorが発生する
    node = stb_v2_1_0.StbNode(id=1, x=100.0, y=200.0, z=300.0)
    with pytest.raises(AttributeError):
        node.aaa = 123  # type: ignore[attr-defined]
