# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""ST-Bridgeモデルの定義済辞書変換プロファイル。"""

from .config import DictProfile, KeyStyle, ValueStyle

# ST-Bridge上の属性名・要素名を、そのまま使用する辞書変換の標準プロファイル。
DEFAULT = DictProfile(
    attribute_prefix="",
    child_prefix="",
    content_key="content",
    key_style=KeyStyle.XML,
    value_style=ValueStyle.PYTHON,
    wrap_root=True,
    omit_none=False,
    omit_empty=False,
)

# 以下は検証用プロファイル。
_ANALYSIS = DictProfile(
    attribute_prefix="",
    child_prefix="",
    content_key="content",
    key_style=KeyStyle.SNAKE,
    value_style=ValueStyle.PYTHON,
    wrap_root=False,
    omit_none=False,
    omit_empty=False,
)

_XMLTODICT_COMPAT = DictProfile(
    attribute_prefix="@",
    child_prefix="",
    content_key="#text",
    key_style=KeyStyle.XML,
    value_style=ValueStyle.XML,
    wrap_root=True,
    omit_none=True,
    omit_empty=False,
)

_JSON_CAMEL = DictProfile(
    attribute_prefix="",
    child_prefix="",
    content_key="content",
    key_style=KeyStyle.CAMEL,
    value_style=ValueStyle.JSON,
    wrap_root=False,
    omit_none=False,
    omit_empty=False,
)

__all__ = ["DEFAULT"]
