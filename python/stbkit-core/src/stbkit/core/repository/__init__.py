# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""参照解決の実装"""

from typing import overload

from ..data_model import stb_v2_0_2, stb_v2_1_0, stb_v2_1_1
from ..data_model.common import StBridgeRoot
from .repo_common import Repository as Repository
from .repo_common import RepositoryBase as RepositoryBase
from .repo_v2_0_2 import RepositoryV2_0_2 as RepositoryV2_0_2
from .repo_v2_1_0 import RepositoryV2_1_0 as RepositoryV2_1_0
from .repo_v2_1_1 import RepositoryV2_1_1 as RepositoryV2_1_1


@overload
def get_repository(stb: stb_v2_1_1.StBridge) -> RepositoryV2_1_1: ...
@overload
def get_repository(stb: stb_v2_1_0.StBridge) -> RepositoryV2_1_0: ...
@overload
def get_repository(stb: stb_v2_0_2.StBridge) -> RepositoryV2_0_2: ...
@overload
def get_repository(stb: StBridgeRoot) -> RepositoryBase: ...
def get_repository(
    stb: StBridgeRoot,
) -> RepositoryBase:
    """ST-Bridgeモデルの参照解決をおこなうリポジトリを取得する。

    作成時に参照解決用の索引を作るため、モデルを変更した場合はrefresh()を呼び出す必要があります

    Args:
        stb: ST-Bridgeのルート要素

    Returns:
        RepositoryBase: stbのバージョンに対応するリポジトリ。

    Raises:
        TypeError: 引数に対応していないバージョンのモデルを渡した場合。

    Examples:
        >>> import stbkit.api
        >>> import stbkit.api.experimental
        >>> stb = stbkit.api.load_latest("model.stb")
        >>> repo = stbkit.api.experimental.get_repository(stb)
    """
    match stb:
        case stb_v2_0_2.StBridge():
            return RepositoryV2_0_2(stb)
        case stb_v2_1_0.StBridge():
            return RepositoryV2_1_0(stb)
        case stb_v2_1_1.StBridge():
            return RepositoryV2_1_1(stb)
        case _:
            return Repository(stb)


__all__ = [
    "Repository",
    "RepositoryBase",
    "RepositoryV2_0_2",
    "RepositoryV2_1_0",
    "RepositoryV2_1_1",
    "get_repository",
]
