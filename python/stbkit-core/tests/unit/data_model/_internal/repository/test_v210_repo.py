# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid

import pytest

from stbkit.core.data_model.stb_v2_1_0 import (
    StbColumn,
    StbColumns,
    StbGirder,
    StbGirders,
    StbMembers,
    StbModel,
    StbNode,
    StbNodes,
    StBridge,
    StbSecBuildH,
    StbSecColumnRc,
    StbSecColumnS,
    StbSecSteel,
    StbSections,
    StbSecUndefined,
)
from stbkit.core.repository import RepositoryV2_1_0
from stbkit.core.stb_exceptions import ReferenceElementNotFoundError, SchemaError


def test_repository_v210_storage_keys() -> None:
    stb: StBridge = StBridge(
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[
                    StbNode(id=1, x=1.0, y=1.0, z=1.0),
                    StbNode(id=2, x=2.0, y=2.0, z=2.0),
                    StbNode(id=3, x=3.0, y=3.0, z=3.0),
                ]
            ),
            stb_members=StbMembers(
                stb_girders=StbGirders(
                    stb_girder=[
                        StbGirder(id=1, id_node_start=1, id_node_end=2),
                        StbGirder(id=2, id_node_start=2, id_node_end=3),
                    ]
                )
            ),
            stb_sections=StbSections(
                stb_sec_steel=StbSecSteel(
                    stb_sec_build_h=[
                        StbSecBuildH(
                            name="BH-700x300x12x16", a=700, b=300, t1=12, t2=16
                        )
                    ]
                )
            ),
        ),
    )
    repo: RepositoryV2_1_0 = RepositoryV2_1_0(stb)

    assert len(repo._storage[StbNode]) == 3
    assert repo.get(StbNode, 2).x == 2.0
    assert repo.get(StbSecBuildH, "BH-700x300x12x16").b == 300

    # 見つからない場合: getは例外、get_or_noneはNone
    with pytest.raises(ReferenceElementNotFoundError):
        _ = repo.get(StbNode, 999)
    assert repo.get_or_none(StbNode, 999) is None
    assert repo.get_or_none(StbNode, 2) is not None

    with pytest.raises(ReferenceElementNotFoundError):
        _ = repo.get(StbSecColumnRc, 1)
    assert repo.get_or_none(StbSecColumnRc, 1) is None


def test_repository_v210_ref_map() -> None:
    stb: StBridge = StBridge(
        stb_model=StbModel(
            stb_members=StbMembers(
                stb_columns=StbColumns(
                    stb_column=[
                        StbColumn(
                            id=1,
                            id_node_bottom=1,
                            id_node_top=2,
                            id_section=1,
                            kind_structure="RC",
                        ),
                        StbColumn(
                            id=2,
                            id_node_bottom=2,
                            id_node_top=3,
                            id_section=1,
                            kind_structure="S",
                        ),
                        StbColumn(
                            id=2,
                            id_node_bottom=2,
                            id_node_top=3,
                            id_section=1,
                            kind_structure="UNDEFINED",
                        ),
                    ]
                )
            ),
            stb_sections=StbSections(
                stb_sec_column_rc=[
                    StbSecColumnRc(id=1, name="RC_COLUMN"),
                ],
                stb_sec_column_s=[
                    StbSecColumnS(id=1, name="S_COLUMN"),
                ],
                stb_sec_undefined=[StbSecUndefined(id=1, name="UNDEFINED_COLUMN")],
            ),
        )
    )
    repo: RepositoryV2_1_0 = RepositoryV2_1_0(stb)
    columns: list[StbColumn] = stb.stb_model.stb_members.stb_columns.stb_column
    sec_rc = repo.deref(columns[0]).id_section
    assert isinstance(sec_rc, StbSecColumnRc)
    assert sec_rc.name == "RC_COLUMN"
    sec_s = repo.deref(columns[1]).id_section
    assert isinstance(sec_s, StbSecColumnS)
    assert sec_s.name == "S_COLUMN"
    sec_undefined = repo.deref(columns[2]).id_section
    assert isinstance(sec_undefined, StbSecUndefined)
    assert sec_undefined.name == "UNDEFINED_COLUMN"


def test_repository_v210_deref_or_none() -> None:
    stb: StBridge = StBridge(
        stb_model=StbModel(
            stb_nodes=StbNodes(stb_node=[StbNode(id=1, x=1.0, y=1.0, z=1.0)]),
            stb_members=StbMembers(
                stb_girders=StbGirders(
                    stb_girder=[
                        StbGirder(
                            id=1,
                            id_node_start=1,
                            id_node_end=999,
                            kind_structure="RC",
                        ),
                        StbGirder(id=2, id_node_start=1, id_node_end=1),
                    ]
                )
            ),
        )
    )
    repo: RepositoryV2_1_0 = RepositoryV2_1_0(stb)
    girders: list[StbGirder] = stb.stb_model.stb_members.stb_girders.stb_girder
    girder: StbGirder = girders[0]

    assert repo.deref(girder).id_node_start.id == 1
    # 参照先が存在しない場合、_or_none付きはNone、無しは例外
    assert repo.deref(girder).id_node_end_or_none is None
    with pytest.raises(ReferenceElementNotFoundError):
        _ = repo.deref(girder).id_node_end
    # id自体がNoneの場合も_or_noneはNone
    assert repo.deref(girder).id_section_or_none is None
    # スキーマ不正(kind_structureがNone)は_or_noneでも握り潰さない
    with pytest.raises(SchemaError):
        _ = repo.deref(girders[1]).id_section_or_none


def test_repository_v210_deref_unknown_field() -> None:
    """未登録の参照フィールドはAttributeError"""
    stb: StBridge = StBridge(
        stb_model=StbModel(
            stb_members=StbMembers(
                stb_girders=StbGirders(
                    stb_girder=[StbGirder(id=1, id_node_start=1, id_node_end=2)]
                )
            )
        )
    )
    repo: RepositoryV2_1_0 = RepositoryV2_1_0(stb)
    girder: StbGirder = stb.stb_model.stb_members.stb_girders.stb_girder[0]
    accessor = repo.deref(girder)

    for bad_name in ("id_node_bottom", "id_node_statr"):
        with pytest.raises(AttributeError):
            _ = getattr(accessor, bad_name)
    assert not hasattr(accessor, "id_node_bottom")


def test_repository_v210_deref_covers_ref_map() -> None:
    for owner_type, fields in RepositoryV2_1_0._ref_map.items():
        accessor_fields = {name for name in fields if not name.startswith("_")}
        assert accessor_fields, f"{owner_type.__name__}の参照が空です"
        for field_name in accessor_fields:
            assert field_name in owner_type._fields, (
                f"{owner_type.__name__}に{field_name}が存在しません"
            )


def test_repository_v210_ref_guid() -> None:
    guid1 = uuid.uuid4()
    guid2 = uuid.uuid4()
    guid3 = uuid.uuid4()
    id1 = 1
    id2 = 2
    id3 = 3
    stb: StBridge = StBridge(
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[
                    StbNode(id=id1, guid=guid1, x=1.0, y=1.0, z=1.0),
                    StbNode(id=id2, guid=guid2, x=2.0, y=2.0, z=2.0),
                    StbNode(id=id3, guid=guid3, x=3.0, y=3.0, z=3.0),
                ]
            ),
        ),
    )
    repo: RepositoryV2_1_0 = RepositoryV2_1_0(stb)
    node1 = repo.get_by_guid(guid1)
    node2 = repo.get_by_guid(guid2)
    node3 = repo.get_by_guid(guid3)
    assert isinstance(node1, StbNode) and node1.id == id1
    assert isinstance(node2, StbNode) and node2.id == id2
    assert isinstance(node3, StbNode) and node3.id == id3
