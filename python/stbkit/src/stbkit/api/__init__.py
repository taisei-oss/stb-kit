# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""stbkitの基本機能をまとめたAPI

ST-Bridgeファイルの読み書き、バージョンアップ、他形式への変換を提供します。
バージョンごとのデータモデルはstb_latest、stb_v2_0、stb_v2_1から利用してください。

読み込みは、ファイルのバージョンをそのまま扱うload・loadsと、
読み込んでから最新版へ変換するload_latest・loads_latestがあります。

IFCへの変換を利用する場合はifcopenshellのインストールが必要です。
"""

from stbkit.core.data_model.common import StBridgeElement as StBridgeElement
from stbkit.core.data_model.common import StBridgeRoot as StBridgeRoot
from stbkit.core.stb_exceptions import NoneAccessError as NoneAccessError
from stbkit.core.stb_io import dump as dump
from stbkit.core.stb_io import dumps as dumps
from stbkit.core.stb_io import load as load
from stbkit.core.stb_io import loads as loads
from stbkit.core.validation import validate_schema as validate_schema

from stbkit.tools._internal.stb_io import load_latest as load_latest
from stbkit.tools._internal.stb_io import loads_latest as loads_latest
from stbkit.tools.converters import to_ifc as to_ifc
from stbkit.tools.upgrade import upgrade_to_latest as upgrade_to_latest

__all__ = [
    "NoneAccessError",
    "StBridgeElement",
    "StBridgeRoot",
    "dump",
    "dumps",
    "load",
    "load_latest",
    "loads",
    "loads_latest",
    "stb_latest",
    "stb_v2_0",
    "stb_v2_1",
    "to_ifc",
    "upgrade_to_latest",
    "validate_schema",
]
