# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""バージョンごとのリポジトリ

リポジトリは、読み込んだST-Bridgeの参照解決や検索を行うクラスです。
型注釈を利用したい場合に利用します。
インスタンスはstbkit.api.experimental.get_repositoryを使って取得できます。
モデルのバージョンに対応する型を選ぶため、バージョンごとの分岐が不要になります。

※このモジュール内のAPIは暫定的なものであり、今後変更される可能性があります。
  仕様が固まったものはstbkit.apiへ移し、このモジュールからは段階的に外します。
  継続的に利用するコードから使う場合は、この点を了解したうえで、バージョンを固定して使用してください。
  互換性に関する方針は、GitHubリポジトリのCOMPATIBILITY.mdを参照してください。
"""

from stbkit.core.repository import RepositoryV2_0_2 as RepositoryV2_0_2
from stbkit.core.repository import RepositoryV2_1_0 as RepositoryV2_1_0
from stbkit.core.repository import RepositoryV2_1_1 as RepositoryLatest
from stbkit.core.repository import RepositoryV2_1_1 as RepositoryV2_1_1

__all__ = [
    "RepositoryLatest",
    "RepositoryV2_0_2",
    "RepositoryV2_1_0",
    "RepositoryV2_1_1",
]
