# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import ClassVar

from ..data_model.common import StBridgeElement
from ._internal.ref_def_v2_0_2 import _key_field_names_v202, _ref_map_v202
from .repo_common import RepositoryBase, _DerefAccessor, _RefMap


class RepositoryV2_0_2(RepositoryBase):
    """ST-Bridge v2.0.2用のリポジトリ。

    インスタンスの生成はget_repositoryの利用を推奨します。
    """

    _key_field_names: ClassVar[dict[type[StBridgeElement], str]] = _key_field_names_v202
    _ref_map: ClassVar[_RefMap] = _ref_map_v202

    def deref(self, element: StBridgeElement) -> _DerefAccessor:
        """要素の参照解決をするアクセサを返します。

        deref(element)の後に、データモデルで参照を表す属性と同じ属性にアクセスすると参照先の要素が取得できます。
        末尾に`_or_none`を付けると、参照を解決できない場合にNoneを返します。
        属性名と参照先の具体的な型は、スタブで定義します。

        Args:
            element: 参照を解決する要素。

        Returns:
            _DerefAccessor: 参照解決アクセサ。

        Raises:
            AttributeError: 属性アクセス時に属性が定義されていない場合。
            ReferenceElementNotFoundError: 属性アクセス時に、参照値がNoneの場合、または参照先の要素が存在しない場合。
                `_or_none`付きの属性では投げず、Noneを返します。
            SchemaError: 属性アクセス時に、属性の値が不正で参照先の型が確定できない場合。
                `_or_none`付きの属性でも投げます。
            TypeError: 属性アクセス時に型が対応したキーの型でない場合。

        Examples:
            >>> section = repo.deref(girder).id_section
            >>> node = repo.deref(girder).id_node_start_or_none
        """
        return _DerefAccessor(self, element)
