# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""将来の公開を意図した、暫定公開API

※このモジュール内のAPIは暫定的なものであり、今後変更される可能性があります。
  仕様が固まったものはstbkit.apiへ移し、このモジュールからは段階的に外します。
  継続的に利用するコードから使う場合は、この点を了解したうえで、バージョンを固定して使用してください。
  互換性に関する方針は、GitHubリポジトリのCOMPATIBILITY.mdを参照してください。
"""

from stbkit.core.repository import get_repository as get_repository
from stbkit.core.serialization import from_dict as from_dict
from stbkit.core.serialization import to_dict as to_dict

__all__ = ["from_dict", "get_repository", "to_dict"]
