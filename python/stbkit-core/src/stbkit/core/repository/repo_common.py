# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Final
from uuid import UUID

from .._internal.name_converter import private_field_name
from ..data_model.common import StBridgeElement, _FieldKind
from ..stb_exceptions import (
    NoneAccessError,
    ReferenceElementNotFoundError,
    SchemaError,
)

_OR_NONE_SUFFIX: Final[str] = "_or_none"


@dataclass(frozen=True, slots=True)
class _ByKind:
    """
    kind_structureの値によって解決先の型が変わる参照
    """

    discriminator: str
    """判別に使う属性名。"""

    targets: Mapping[str, type[StBridgeElement]]
    """判別属性の値と参照先の型の辞書"""

    def resolve(self, element: StBridgeElement) -> type[StBridgeElement]:
        value = getattr(element, private_field_name(self.discriminator), None)
        target = self.targets.get(value) if isinstance(value, str) else None
        if target is None:
            raise SchemaError(
                f"{self.discriminator}={value}は不正です。", element=element
            )
        return target


type _RefTarget = type[StBridgeElement] | tuple[type[StBridgeElement], ...] | _ByKind

type _RefMap = dict[type[StBridgeElement], dict[str, _RefTarget]]


class RepositoryBase:
    """リポジトリの基底クラス。

    作成後にモデルを変更した場合はrefresh()で索引を作り直す必要があります。

    Args:
        stb: ST-Bridgeのルート。
    """

    # 下記変数をサブクラスで継承させる
    # ABCにしたいが、クラス変数の上書きはabstractmethodで強制できず、
    # B024がでるので、普通のクラスとしている
    _key_field_names: ClassVar[dict[type[StBridgeElement], str]] = {}
    _ref_map: ClassVar[_RefMap] = {}

    def __init__(self, stb: StBridgeElement) -> None:
        self._stb: StBridgeElement = stb
        self._storage: dict[
            type[StBridgeElement], dict[int | str, StBridgeElement]
        ] = {}
        self._guid_storage: dict[UUID, StBridgeElement] = {}
        self._name_keyed_types: tuple[type[StBridgeElement], ...] = tuple(
            ItemType
            for ItemType, key_field_name in self._key_field_names.items()
            if key_field_name == "name"
        )
        self._set_storage(stb)

    def _set_storage(self, element: StBridgeElement) -> None:
        for key, field_ in element._fields.items():
            if field_.kind is not _FieldKind.ELEMENT:
                if field_.py_type == UUID or field_.py_type == "UUID":
                    field_name: str = private_field_name(key)
                    guid_value: UUID | None = getattr(element, field_name)
                    if guid_value is not None:
                        self._guid_storage[guid_value] = element
                continue
            field_name = private_field_name(key)
            if field_.max_occurs == 1:
                child = getattr(element, field_name)
                if isinstance(child, StBridgeElement):
                    self._set_storage(child)
            else:
                children: list[StBridgeElement] = getattr(element, field_name)
                for child in children:
                    # 索引の対象は要素ごとに判定する。
                    # 孫要素などもあるため、対象かどうかに関わらず
                    # 全要素に対して探索する。
                    self._set_key_index(child)
                    self._set_storage(child)

    def _set_key_index(self, child: StBridgeElement) -> None:
        ChildType: type[StBridgeElement] = type(child)
        key_field_name: str | None = self._key_field_names.get(ChildType)
        if key_field_name is None:
            return
        try:
            key_field_value: int | str = getattr(child, key_field_name)
        except NoneAccessError:
            return
        self._storage.setdefault(ChildType, {})[key_field_value] = child

    def refresh(self) -> None:
        """モデルを編集した場合に、索引を作り直します。

        リポジトリ構築後に要素を追加・削除したりid,name,guid等の属性を変更した場合に呼び出します。
        """
        self._storage.clear()
        self._guid_storage.clear()
        self._set_storage(self._stb)

    def get[T: StBridgeElement](self, ItemType: type[T], key: int | str) -> T:
        """
        指定した型とキーで要素を1つ取得します。

        キーは一般的にはid、鋼材断面はnameです。

        Args:
            ItemType (type[T]): 取得する要素の型。
            key (int | str): キーの値。

        Returns:
            T: 見つかった要素。

        Raises:
            TypeError: ItemTypeが参照定義されていない場合、
                または索引の要素がItemTypeのインスタンスでない場合。
            ReferenceElementNotFoundError: 参照先が見つからなかった場合。
        """
        key_field_name: str | None = self._key_field_names.get(ItemType)
        if key_field_name is None:
            raise TypeError(
                f"{ItemType.__name__}は参照定義されていないため取得できません。"
            )
        children_dict: dict[int | str, StBridgeElement] | None = self._storage.get(
            ItemType
        )
        if not children_dict:
            raise ReferenceElementNotFoundError(
                f"[{ItemType.__name__}]の要素は存在しません。"
            )
        item: StBridgeElement | None = children_dict.get(key)
        if item is None:
            raise ReferenceElementNotFoundError(
                f"[{ItemType.__name__}].{key_field_name}={key}が見つかりません。"
            )
        if not isinstance(item, ItemType):
            raise TypeError(
                f"型が異なります。expect:{ItemType.__name__}, "
                f"actual:{type(item).__name__}"
            )
        return item

    def get_or_none[T: StBridgeElement](
        self, ItemType: type[T], key: int | str
    ) -> T | None:
        """
        get()と同じですが、要素が見つからない場合はNoneを返します。

        TypeErrorは、Noneにはせずそのまま投げます。

        Args:
            ItemType (type[T]): 取得する要素の型。
            key (int | str): キーの値。

        Returns:
            T | None: 見つかった要素。見つからない場合はNone。

        Raises:
            TypeError: ItemTypeが参照定義されていない場合、
                または索引の要素がItemTypeのインスタンスでない場合。
        """
        try:
            return self.get(ItemType, key)
        except ReferenceElementNotFoundError:
            return None

    def _get_any[T: StBridgeElement](
        self, ItemTypes: tuple[type[T], ...], key: int | str
    ) -> T:
        """
        複数の型を順に試し、最初に見つかった要素を返します。

        候補型の間でキーが一意に振られている場合に使います。
        断面等のkind_structureで参照先が変わる参照には使えません。

        Raises:
            ReferenceElementNotFoundError: 参照先が見つからない場合。
        """
        for ItemType in ItemTypes:
            try:
                return self.get(ItemType, key)
            except ReferenceElementNotFoundError:
                continue
        raise ReferenceElementNotFoundError(
            f"[{', '.join(t.__name__ for t in ItemTypes)}].key={key} が見つかりません。"
        )

    def get_steel(self, name: str) -> StBridgeElement:
        """
        鋼材断面をnameで取得します。

        Args:
            name: 鋼材断面のname。

        Returns:
            StBridgeElement: 見つかった鋼材断面の要素。

        Raises:
            ReferenceElementNotFoundError: 参照先が見つからない場合。
        """
        # 戻り値の型はスタブで宣言する
        return self._get_any(self._name_keyed_types, name)

    def find_equivalent[T: StBridgeElement](
        self, instance: T, *, exclude_fields: Iterable[str] | None = None
    ) -> T | None:
        """
        指定された要素と同等（属性が等価）の要素を検索します。
        exclude_fieldsで指定された属性は比較から除外されます。

        ※現在、子要素は比較に含まれません。含めるかどうかは要協議。

        用途としては、同じ形状の鋼材断面などを検索する場合です。

        Args:
            instance (T): 比較対象要素。
            exclude_fields (Iterable[str], optional): 比較から除外する
                フィールド名のリスト。デフォルトはNone。

        Returns:
            T | None: 同等の要素が見つかった場合はその要素。見つからない場合はNone。
            索引に入っている型だけが対象のため、現状では参照解決に使われない型の場合常にNoneになります。
            TODO: 全要素を対象にするか協議
        """
        if exclude_fields is None:
            exclude_fields = []

        for item in self._storage.get(type(instance), {}).values():
            if all(
                getattr(item, private_field_name(field_name))
                == getattr(instance, private_field_name(field_name))
                for field_name, field_info in item._fields.items()
                if field_name not in exclude_fields
                and field_info.kind == _FieldKind.ATTRIBUTE
            ) and isinstance(item, type(instance)):
                return item
        return None

    def get_by_guid(self, guid: UUID) -> StBridgeElement:
        """
        guidで検索します。

        guidはキーによる取得、型の宣言は不要です。guid属性を持つすべての要素が対象になります。

        Args:
            guid: 取得する要素のguid。

        Returns:
            StBridgeElement: 見つかった要素。

        Raises:
            ReferenceElementNotFoundError: 要素が見つからない場合。
        """
        item = self._guid_storage.get(guid)
        if item is None:
            raise ReferenceElementNotFoundError(f"guid={guid} が見つかりません。")
        return item

    def get_by_guid_or_none(self, guid: UUID) -> StBridgeElement | None:
        """get_by_guid()と同じですが、見つからない場合はNoneを返します。

        Args:
            guid: 取得する要素のguid。

        Returns:
            StBridgeElement | None: 見つかった要素。見つからない場合はNone。
        """
        return self._guid_storage.get(guid)

    def _reference_field_names(self, element: StBridgeElement) -> tuple[str, ...]:
        return tuple(self._ref_map.get(type(element), {}))

    def _deref_field(
        self, element: StBridgeElement, id_field_name: str
    ) -> StBridgeElement:
        try:
            ref_target: _RefTarget = self._ref_map[type(element)][id_field_name]
        except KeyError:
            raise KeyError(
                f"{type(element).__name__}のフィールド名{id_field_name}は想定されない参照です"
            ) from None
        RefTypes: type[StBridgeElement] | tuple[type[StBridgeElement], ...]
        if isinstance(ref_target, _ByKind):
            RefTypes = ref_target.resolve(element)
        else:
            RefTypes = ref_target
        key = getattr(element, private_field_name(id_field_name))
        if key is None:
            raise ReferenceElementNotFoundError(
                f"{type(element).__name__}.{id_field_name}がNoneのため参照できません。"
            )
        if not isinstance(key, (int, str)):
            raise TypeError(
                f"{type(element).__name__}.{id_field_name}の型が不正です。intまたはstrである必要があります。実際の型:{type(key).__name__}"
            )
        if isinstance(RefTypes, tuple):
            return self._get_any(RefTypes, key)
        return self.get(RefTypes, key)


class _DerefAccessor:
    """
    deref()が返す参照解決アクセサ。

    属性名はST-Bridgeのフィールド名と同じで、値は参照先の要素です。

        section = repo.deref(girder).id_section
        node = repo.deref(girder).id_node_start_or_none

    実行時の実装はこのクラス1つで、要素の型ごとの属性名と戻り値の型はスタブが与えます。

    """

    # deref()は基底クラスRepositoryBaseに置くと、
    # スタブのオーバーロードで警告が出るため、各バージョンのリポジトリ側で定義する。

    __slots__ = ("_element", "_repo")

    def __init__(self, repo: RepositoryBase, element: StBridgeElement) -> None:
        self._repo: RepositoryBase = repo
        self._element: StBridgeElement = element

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._element._name_for_log()})"

    # not TYPE_CHECKINGにより__getattr__を型チェッカから隠す。
    # 見えているとスタブで定義していない属性で方エラーが出ず、
    # 属性名のtypoの危険性がある。
    if not TYPE_CHECKING:

        def __getattr__(self, name: str) -> StBridgeElement | None:
            if name.startswith("_"):
                raise AttributeError(name)
            is_or_none: bool = name.endswith(_OR_NONE_SUFFIX)
            field_name: str = name[: -len(_OR_NONE_SUFFIX)] if is_or_none else name
            try:
                return self._repo._deref_field(self._element, field_name)
            except KeyError:
                raise AttributeError(
                    f"{type(self._element).__name__}に参照フィールド{field_name}はありません"
                ) from None
            except ReferenceElementNotFoundError:
                if is_or_none:
                    return None
                raise


class Repository(RepositoryBase):
    """バージョンに依存しない汎用リポジトリ。"""
