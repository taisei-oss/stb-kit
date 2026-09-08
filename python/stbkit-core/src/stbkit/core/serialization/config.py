# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""ST-Bridgeモデルと辞書の変換ルール"""

from dataclasses import dataclass
from enum import StrEnum


class KeyStyle(StrEnum):
    """辞書キーの名前形式"""

    XML = "xml"
    """ST-Bridge上の属性名・要素名そのまま"""
    SNAKE = "snake"
    """Pythonの属性名と同じスネークケース"""
    CAMEL = "camel"
    """スネークケースをキャメルケースにしたもの"""


class ValueStyle(StrEnum):
    """辞書値の表現形式"""

    PYTHON = "python"
    """モデルが保持するPythonの値そのまま"""
    JSON = "json"
    """JSONで表現可能な値へ変換"""
    XML = "xml"
    """XML上の表現と同じstrへ変換"""


@dataclass(frozen=True, slots=True, init=False)
class DictProfile:
    """ST-Bridgeモデルと辞書の変換ルール

    omit_noneはNoneだけを省略します。
    omit_emptyはNoneに加え、空辞書と空リストも省略します。
    両方を指定した場合も、動作はomit_empty=Trueと同じです。

    Attributes:
        attribute_prefix: 属性のキーへ付ける接頭辞。
        child_prefix: 子要素のキーへ付ける接頭辞。
        content_key: 要素の内容を格納するキー。
        key_style: 辞書キーの名前形式。
        value_style: 辞書値の表現形式。
        wrap_root: ルート要素をルート要素名のキーで包むかどうか。
        omit_none: Noneの値を省略するかどうか。
        omit_empty: Noneと空辞書・リストを省略するかどうか。
    """

    attribute_prefix: str
    child_prefix: str
    content_key: str
    key_style: KeyStyle
    value_style: ValueStyle
    wrap_root: bool
    omit_none: bool
    omit_empty: bool

    def __init__(
        self,
        *,
        attribute_prefix: str = "",
        child_prefix: str = "",
        content_key: str = "content",
        key_style: KeyStyle | str = KeyStyle.XML,
        value_style: ValueStyle | str = ValueStyle.PYTHON,
        wrap_root: bool = False,
        omit_none: bool = False,
        omit_empty: bool = False,
    ) -> None:
        """辞書変換の変換ルールのコンストラクタ

        Raises:
            TypeError: attribute_prefix・child_prefix・content_keyがstrでない場合
                またはwrap_root・omit_none・omit_emptyがboolでない場合。
            ValueError: content_keyが空文字列の場合、
                またはkey_style・value_styleが未対応の値の場合。
        """
        if not isinstance(attribute_prefix, str):
            raise TypeError("attribute_prefixはstrで指定してください")
        if not isinstance(child_prefix, str):
            raise TypeError("child_prefixはstrで指定してください")
        if not isinstance(content_key, str):
            raise TypeError("content_keyはstrで指定してください")
        if content_key == "":
            raise ValueError("content_keyに空文字列は指定できません")
        if not isinstance(wrap_root, bool):
            raise TypeError("wrap_rootはboolで指定してください")
        if not isinstance(omit_none, bool):
            raise TypeError("omit_noneはboolで指定してください")
        if not isinstance(omit_empty, bool):
            raise TypeError("omit_emptyはboolで指定してください")

        try:
            normalized_key_style = KeyStyle(key_style)
        except (TypeError, ValueError):
            raise ValueError(f"未対応のkey_styleです: {key_style!r}") from None
        try:
            normalized_value_style = ValueStyle(value_style)
        except (TypeError, ValueError):
            raise ValueError(f"未対応のvalue_styleです: {value_style!r}") from None

        object.__setattr__(self, "attribute_prefix", attribute_prefix)
        object.__setattr__(self, "child_prefix", child_prefix)
        object.__setattr__(self, "content_key", content_key)
        object.__setattr__(self, "key_style", normalized_key_style)
        object.__setattr__(self, "value_style", normalized_value_style)
        object.__setattr__(self, "wrap_root", wrap_root)
        object.__setattr__(self, "omit_none", omit_none)
        object.__setattr__(self, "omit_empty", omit_empty)
