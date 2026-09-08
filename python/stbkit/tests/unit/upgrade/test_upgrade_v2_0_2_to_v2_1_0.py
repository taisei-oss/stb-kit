# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.stb_v2_0_2 import (
    VERSION,
    StbCommon,
    StbMembers,
    StbModel,
    StbOpen,
    StbOpenId,
    StbOpenIdList,
    StbOpens,
    StBridge,
    StbWall,
    StbWalls,
)
from stbkit.core.stb_reporting import CollectingReporter, Severity

from stbkit.api import stb_latest, upgrade_to_latest


def test_upgrade_shared_open() -> None:
    """1つのStbOpenを3枚の壁が参照する場合、壁ごとに開口配置が作られる。"""
    stb: StBridge = StBridge(
        version=VERSION,
        stb_common=StbCommon(
            project_name="upgrade test", app_name="stbkit", app_version="0.0.0"
        ),
        stb_model=StbModel(
            stb_members=StbMembers(
                stb_walls=StbWalls(
                    stb_wall=[
                        StbWall(
                            id=1,
                            id_section=1,
                            kind_layout="ON_GIRDER",
                            stb_open_id_list=StbOpenIdList(
                                stb_open_id=[StbOpenId(id=1)]
                            ),
                        ),
                        StbWall(
                            id=2,
                            id_section=1,
                            kind_layout="ON_GIRDER",
                            stb_open_id_list=StbOpenIdList(
                                stb_open_id=[StbOpenId(id=1)]
                            ),
                        ),
                        StbWall(
                            id=3,
                            id_section=1,
                            kind_layout="ON_GIRDER",
                            stb_open_id_list=StbOpenIdList(
                                stb_open_id=[StbOpenId(id=1)]
                            ),
                        ),
                    ]
                ),
                stb_opens=StbOpens(
                    stb_open=[
                        StbOpen(
                            id=1,
                            position_x=100.0,
                            position_y=200.0,
                            length_x=300.0,
                            length_y=400.0,
                        )
                    ]
                ),
            )
        ),
    )

    upgraded: stb_latest.StBridge = upgrade_to_latest(
        stb, reporter=CollectingReporter()
    )

    arrangements: stb_latest.StbOpenArrangements = (
        upgraded.stb_model.stb_members.stb_open_arrangements
    )
    arrs: list[stb_latest.StbOpenArrangement] = arrangements.stb_open_arrangement
    assert sorted(placement.id_member for placement in arrs) == [1, 2, 3]
    # 壁ごとに別インスタンス・別IDでなければ、後から設定した部材で上書きされる
    assert len({id(placement) for placement in arrs}) == 3
    assert len({placement.id for placement in arrs}) == 3
    # 形状は同じなので、断面は3枚で共有する
    assert len({placement.id_section for placement in arrs}) == 1


def test_upgrade_open() -> None:
    """開口は配置と断面へ分かれる"""
    stb: StBridge = StBridge(
        version=VERSION,
        stb_common=StbCommon(
            project_name="upgrade test", app_name="stbkit", app_version="0.0.0"
        ),
        stb_model=StbModel(
            stb_members=StbMembers(
                stb_walls=StbWalls(
                    stb_wall=[
                        StbWall(
                            id=1,
                            id_section=1,
                            kind_layout="ON_GIRDER",
                            stb_open_id_list=StbOpenIdList(
                                stb_open_id=[StbOpenId(id=1)]
                            ),
                        )
                    ]
                ),
                stb_opens=StbOpens(
                    stb_open=[
                        StbOpen(
                            id=1,
                            position_x=100.0,
                            position_y=200.0,
                            length_x=300.0,
                            length_y=400.0,
                        )
                    ]
                ),
            )
        ),
    )
    reporter: CollectingReporter = CollectingReporter()

    upgraded: stb_latest.StBridge = upgrade_to_latest(stb, reporter=reporter)

    # 配置には部材と位置が移る
    arrangements: stb_latest.StbOpenArrangements = (
        upgraded.stb_model.stb_members.stb_open_arrangements
    )
    arr: stb_latest.StbOpenArrangement = arrangements.stb_open_arrangement[0]
    assert arr.kind_member is stb_latest.StbOpenArrangementKindMember.WALL
    assert arr.id_member == 1
    assert (arr.position_x, arr.position_y) == (100.0, 200.0)

    # 寸法は断面へ移る
    sections: list[stb_latest.StbSecOpenRc] = (
        upgraded.stb_model.stb_sections.stb_sec_open_rc
    )
    assert len(sections) == 1
    assert sections[0].id == arr.id_section
    assert (sections[0].length_x, sections[0].length_y) == (300.0, 400.0)

    # 開口は変換できたのでエラーなし
    warnings: list[str] = [
        item.message
        for item in reporter.report
        if item.severity == Severity.WARNING.value
    ]
    assert not [
        message for message in warnings if "変換後のバージョンに属性" in message
    ]
