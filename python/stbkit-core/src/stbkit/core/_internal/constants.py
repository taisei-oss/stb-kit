# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import importlib.metadata
from typing import Final

PACKAGE_NAME: Final = "stbkit-core"

_tmp_version: str
try:
    _tmp_version = importlib.metadata.version(PACKAGE_NAME)
except ImportError:
    _tmp_version = "unknown"
PACKAGE_VERSION: Final[str] = _tmp_version

LATEST_STB_VERSION: Final = "2.1.1"
"""stbkit-coreがサポートしているST-Bridgeの最新バージョン"""
SUPPORTED_STB_VERSIONS: Final = ("2.0.0", "2.0.1", "2.0.2", "2.1.0", "2.1.1")
"""stbkit-coreがサポートしているST-Bridgeのバージョン"""

ENV_NAME_SCHEMA_PATH_STB_V2_0_0: Final = "STBKIT_SCHEMA_PATH_STB_V2_0_0"
ENV_NAME_SCHEMA_PATH_STB_V2_0_1: Final = "STBKIT_SCHEMA_PATH_STB_V2_0_1"
ENV_NAME_SCHEMA_PATH_STB_V2_0_2: Final = "STBKIT_SCHEMA_PATH_STB_V2_0_2"
ENV_NAME_SCHEMA_PATH_STB_V2_1_0: Final = "STBKIT_SCHEMA_PATH_STB_V2_1_0"
ENV_NAME_SCHEMA_PATH_STB_V2_1_1: Final = "STBKIT_SCHEMA_PATH_STB_V2_1_1"

BYTES_PER_MB: Final[int] = 1024 * 1024

DEFAULT_MAX_XML_SIZE: Final[int] = 128 * BYTES_PER_MB
"""読み込めるXMLファイルのデフォルトのサイズ上限(byte)"""

DEFAULT_MAX_XML_DEPTH: Final[int] = 15
"""読み込めるXMLの要素の階層の上限。ST-Bridgeの階層は10程度だが、拡張要素もあるので少し余裕を持たせる"""

XML_READ_CHUNK_SIZE: Final[int] = 64 * 1024
"""XMLを逐次読み込みする際の1回あたりの文字数"""

XML_READ_HEADER_CHUNK_SIZE: Final[int] = 8 * 1024
"""XMLの前文を逐次読み込みする際の1回あたりの文字数"""
