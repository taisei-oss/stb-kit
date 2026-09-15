# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""タイプエイリアスの定義"""

from os import PathLike as _PathLike
from pathlib import Path
from typing import IO, Literal

# ST-Bridgeのスキーマ上の型のタイプエイリアス。
# 見やすくしたもので、値の範囲を制限するものではなく、
# バリデーションはクラス側のFieldInfoで行う。
# コード補完などでわかりやすいように定義している

Angle = float
"""角度。0以上360未満。"""

Length = float
"""長さ。0より大きい値。"""

Monolist = list[int]
"""要素の内容で整数リスト。"""

MonolistLength = list[float]
"""要素の内容で実数リスト。"""

MonolistId = list[int]
"""要素の内容で整数リスト。各値は1以上。"""

NonNegativeInteger = int
"""0以上の整数。"""

NonNegativeLength = float
"""長さで。0を許容する場合。"""

PositiveInteger = int
"""1以上の整数。"""

PositiveIntegerList = list[int]
"""要素の内容で整数リスト。各値は1以上。"""

Ratio = float
"""比率。0より大きく1より小さい。"""

# その他、型の定義に使うもの

type _FilePath = str | _PathLike[str] | Path

type TextSource = _FilePath | IO[str]
"""読み込み元。ファイルパス、または開いたテキストストリーム。"""

type StbVersion = Literal[
    "2.0.0",
    "2.0.1",
    "2.0.2",
    "2.1.0",
    "2.1.1",
]
"""stbkitが対応するST-Bridgeのバージョン。"""
