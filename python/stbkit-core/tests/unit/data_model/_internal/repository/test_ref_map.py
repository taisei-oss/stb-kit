# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""
_ref_mapの整合性検証。

参照定義は公式スキーマから取得できず、仕様書を読んで手書きであるため、typoがないか確認する。
"""

from collections.abc import Iterator
from types import ModuleType

import pytest

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0, stb_v2_1_1
from stbkit.core.data_model.common import StBridgeElement, _FieldKind
from stbkit.core.repository import (
    RepositoryBase,
    RepositoryV2_0_2,
    RepositoryV2_1_0,
    RepositoryV2_1_1,
)
from stbkit.core.repository.repo_common import (
    _ByKind,
    _RefTarget,
)

_REPOSITORIES = [RepositoryV2_0_2, RepositoryV2_1_0, RepositoryV2_1_1]
_REPOSITORY_IDS = [r.__name__ for r in _REPOSITORIES]
_DATA_MODELS = [stb_v2_0_2, stb_v2_1_0, stb_v2_1_1]

_IGNORE_ID_FIELDS = {
    # 拡張情報の参照解決は現在未対応。
    "StbExtObject": {"id_object"},
    # 出力ログ系は参照解決の対象外。
    "StbExportError": {"id", "id_object"},
    "StbExportWarning": {"id", "id_object"},
    "StbExportNotice": {"id", "id_object"},
}


def _targets(ref_target: _RefTarget) -> tuple[type[StBridgeElement], ...]:
    if isinstance(ref_target, _ByKind):
        return tuple(
            target
            for nested in ref_target.targets.values()
            for target in _targets(nested)
        )
    if isinstance(ref_target, tuple):
        return ref_target
    return (ref_target,)


def _by_kinds(ref_target: _RefTarget) -> Iterator[_ByKind]:
    if isinstance(ref_target, _ByKind):
        yield ref_target
        for nested in ref_target.targets.values():
            yield from _by_kinds(nested)


def _entries(
    Repo: type[RepositoryBase],
) -> list[tuple[type[StBridgeElement], str, _RefTarget]]:
    return [
        (owner, field_name, ref_target)
        for owner, fields in Repo._ref_map.references.items()
        for field_name, ref_target in fields.items()
    ]


@pytest.mark.parametrize(
    ("model", "Repo"),
    list(zip(_DATA_MODELS, _REPOSITORIES, strict=True)),
    ids=_REPOSITORY_IDS,
)
def test_check_all_id(model: ModuleType, Repo: type[RepositoryBase]) -> None:
    """明示的な除外を除き、"id"という文字列を含む属性が
    参照先またはキーとして登録されていることのチェック。

    idは_で区切られているもののみ判定する（guidなどの部分一致は除外）。
    ※内容にidがあるものや、鉄骨断面のnameはここでは未検証
    """
    missing: list[str] = []
    for name, owner in vars(model).items():
        if (
            not isinstance(owner, type)
            or not issubclass(owner, StBridgeElement)
            or name.startswith(("StbAna", "StbCal"))
        ):
            # 計算編はまだ実装していないためスキップ
            # TODO: 計算編の実装を行ったらスキップ解除
            continue
        for field_name, info in owner._fields.items():
            if (
                info.kind is not _FieldKind.ATTRIBUTE
                or "id" not in field_name.split("_")
                or field_name == "id_order"  # 参照ではない。
                or field_name in _IGNORE_ID_FIELDS.get(name, set())
            ):
                continue
            if (
                field_name not in Repo._ref_map.references.get(owner, {})
                and Repo._key_field_names.get(owner) != field_name
            ):
                missing.append(f"{name}.{field_name}")
    assert not missing, (
        "_ref_mapにも_key_field_namesにも登録されていないID属性があります:\n"
        + "\n".join(sorted(missing))
    )


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
    for owner, field_name, target in _entries(Repo):
        for ref_target in _by_kinds(target):
            assert ref_target.discriminator in owner._fields, (
                f"{owner.__name__}に参照先の判定属性{ref_target.discriminator}がありません"
                f"({field_name})"
            )


@pytest.mark.parametrize("Repo", _REPOSITORIES, ids=_REPOSITORY_IDS)
def test_by_kind_covers_all_choices(Repo: type[RepositoryBase]) -> None:
    """参照先の判別属性の取りうる値をすべて網羅していること。

    網羅漏れは実行時にSchemaErrorを投げるため、ここでチェックする。
    """
    for owner, field_name, target in _entries(Repo):
        for ref_target in _by_kinds(target):
            choices = owner._fields[ref_target.discriminator].choices
            assert choices is not None, (
                f"{owner.__name__}.{ref_target.discriminator}にchoicesがありません"
            )
            missing = set(choices) - set(ref_target.targets)
            expected_missing: set[str] = set()
            if owner.__name__ == "StbNode":
                # 節点はON＿GRID、OTHERはリンク部材がない
                expected_missing = {"ON_GRID", "OTHER"}
            elif (
                owner.__name__ == "StbDampingDevice"
                and ref_target.discriminator.startswith("kind_structure_")
                and "CFT" not in ref_target.targets
            ):
                # 梁タイプはCFTは指定できない（仕様書5-49）。
                expected_missing = {"CFT"}
            assert missing == expected_missing, (
                f"{owner.__name__}.{field_name}が{ref_target.discriminator}の値"
                f"{sorted(missing)}を解決できません"
            )
            unknown = set(ref_target.targets) - set(choices)
            assert not unknown, (
                f"{owner.__name__}.{field_name}に{ref_target.discriminator}の値として"
                f"存在しない{sorted(unknown)}が指定されています"
            )
            assert ref_target.default is None or ref_target.default in choices


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
