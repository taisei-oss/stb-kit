# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""
_ref_mapの整合性検証。

参照定義は公式スキーマから取得できず、仕様書を読んで手書きであるため、typoがないか確認する。
"""

import pytest

from stbkit.core.data_model.common import StBridgeElement, _FieldKind
from stbkit.core.repository import RepositoryBase, RepositoryV2_0_2, RepositoryV2_1_0
from stbkit.core.repository.repo_common import (
    _ByKind,
    _RefTarget,
)

_REPOSITORIES = [RepositoryV2_0_2, RepositoryV2_1_0]
_REPOSITORY_IDS = [r.__name__ for r in _REPOSITORIES]


def _targets(ref_target: _RefTarget) -> tuple[type[StBridgeElement], ...]:
    if isinstance(ref_target, _ByKind):
        return tuple(ref_target.targets.values())
    if isinstance(ref_target, tuple):
        return ref_target
    return (ref_target,)


def _entries(
    Repo: type[RepositoryBase],
) -> list[tuple[type[StBridgeElement], str, _RefTarget]]:
    return [
        (owner, field_name, ref_target)
        for owner, fields in Repo._ref_map.items()
        for field_name, ref_target in fields.items()
    ]


@pytest.mark.parametrize("Repo", _REPOSITORIES, ids=_REPOSITORY_IDS)
def test_ref_source_fields_exist(Repo: type[RepositoryBase]) -> None:
    """参照元の属性がモデルに実在し、kindがATTRIBUTE"""
    for owner, field_name, _ in _entries(Repo):
        assert field_name in owner._fields, (
            f"{owner.__name__}に{field_name}がありません"
        )
        assert owner._fields[field_name].kind is _FieldKind.ATTRIBUTE, (
            f"{owner.__name__}.{field_name}は属性ではありません"
        )


@pytest.mark.parametrize("Repo", _REPOSITORIES, ids=_REPOSITORY_IDS)
def test_ref_targets_are_gettable(Repo: type[RepositoryBase]) -> None:
    """参照先の型がキーで引ける型として宣言され、そのキー属性を実際に持つ"""
    for owner, field_name, ref_target in _entries(Repo):
        for target in _targets(ref_target):
            key_field_name = Repo._key_field_names.get(target)
            assert key_field_name is not None, (
                f"{owner.__name__}.{field_name}の解決先{target.__name__}が"
                "_key_field_namesに宣言されていません"
            )
            assert key_field_name in target._fields, (
                f"{target.__name__}に{key_field_name}がありません"
            )


@pytest.mark.parametrize("Repo", _REPOSITORIES, ids=_REPOSITORY_IDS)
def test_ref_key_types_match(Repo: type[RepositoryBase]) -> None:
    """参照属性の型と、解決先のキー属性の型が一致する

    intのidでnameキーの型を引こうとしている等の不整合チェック。
    """
    for owner, field_name, ref_target in _entries(Repo):
        source_type = owner._fields[field_name].py_type_str
        for target in _targets(ref_target):
            key_field_name = Repo._key_field_names[target]
            key_type = target._fields[key_field_name].py_type_str
            assert source_type == key_type, (
                f"{owner.__name__}.{field_name}({source_type})と"
                f"{target.__name__}.{key_field_name}({key_type})の型が異なります"
            )


@pytest.mark.parametrize("Repo", _REPOSITORIES, ids=_REPOSITORY_IDS)
def test_by_kind_discriminator_exists(Repo: type[RepositoryBase]) -> None:
    """参照先の判定属性が参照元に実在すること。"""
    for owner, field_name, ref_target in _entries(Repo):
        if not isinstance(ref_target, _ByKind):
            continue
        assert ref_target.discriminator in owner._fields, (
            f"{owner.__name__}に参照先の判定属性{ref_target.discriminator}がありません"
            f"({field_name})"
        )


@pytest.mark.parametrize("Repo", _REPOSITORIES, ids=_REPOSITORY_IDS)
def test_by_kind_covers_all_choices(Repo: type[RepositoryBase]) -> None:
    """参照先の判別属性の取りうる値をすべて網羅していること。

    網羅漏れは実行時にSchemaErrorを投げるため、ここでチェックする。
    """
    for owner, field_name, ref_target in _entries(Repo):
        if not isinstance(ref_target, _ByKind):
            continue
        choices = owner._fields[ref_target.discriminator].choices
        assert choices is not None, (
            f"{owner.__name__}.{ref_target.discriminator}にchoicesがありません"
        )
        missing = set(choices) - set(ref_target.targets)
        assert not missing, (
            f"{owner.__name__}.{field_name}が{ref_target.discriminator}の値"
            f"{sorted(missing)}を解決できません"
        )
        unknown = set(ref_target.targets) - set(choices)
        assert not unknown, (
            f"{owner.__name__}.{field_name}に{ref_target.discriminator}の値として"
            f"存在しない{sorted(unknown)}が指定されています"
        )


@pytest.mark.parametrize("Repo", _REPOSITORIES, ids=_REPOSITORY_IDS)
def test_declared_keys_exist(Repo: type[RepositoryBase]) -> None:
    """キー宣言した属性がモデルに実在し、キーになりうる型であること。"""
    for ItemType, key_field_name in Repo._key_field_names.items():
        assert key_field_name in ItemType._fields, (
            f"{ItemType.__name__}に{key_field_name}がありません"
        )
        field_info = ItemType._fields[key_field_name]
        assert field_info.kind is _FieldKind.ATTRIBUTE, (
            f"{ItemType.__name__}.{key_field_name}は属性ではありません"
        )
        assert field_info.py_type_str in ("int", "str"), (
            f"{ItemType.__name__}.{key_field_name}の型"
            f"{field_info.py_type_str}はキーにできません"
        )
