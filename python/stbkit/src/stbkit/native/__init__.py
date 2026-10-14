# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""stbkit-nativeの呼び出しをするモジュール。

Rust拡張は任意依存のstbkit-nativeが提供します。
未インストールの場合、MissingOptionalDependencyErrorを投げます。
"""

from ._stb_viewer import ElementClickCallback, ElementClickEvent, view

__all__ = [
    "ElementClickCallback",
    "ElementClickEvent",
    "view",
]
