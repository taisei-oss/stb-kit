# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.testutils.data_model_sample.v2_1_1 import v2_1_1_minimum

from stbkit.core.data_model.stb_v2_1_1 import (
    StbColumn,
    StbColumnKindStructure,
    StbNode,
    StbNodeId,
    StbNodeIdList,
    StbNodeKind,
    StBridge,
    StbSecUndefined,
    StbStory,
    StbStoryKind,
)
from stbkit.core.membership._internal.membership_repository import MembershipRepository
from stbkit.core.stb_reporting import CollectingReporter
from stbkit.core.validation import validate_schema


def _create_model() -> StBridge:
    """
    部材の階所属検討用に下記モデルを作成する
    * node600
    | column500
    * node500 story5
    | column400
    * node400
    | column300
    * node300
    | column200
    * node200 story2
    | column100
    * node100
    """
    stb: StBridge = v2_1_1_minimum()
    stb.stb_model.ensure.stb_sections().stb_sec_undefined = [
        StbSecUndefined(id=1, name="Unknown")
    ]
    MAX_STORY = 6
    nodes = stb.stb_model.ensure.stb_nodes().stb_node
    columns = stb.stb_model.ensure.stb_members().ensure.stb_columns().stb_column
    for i in range(MAX_STORY):
        nodes.append(
            StbNode(id=(i + 1) * 100, x=0, y=0, z=i * 5000, kind=StbNodeKind.ON_GRID)
        )
        if i < MAX_STORY - 1:
            columns.append(
                StbColumn(
                    id=(i + 1) * 100,
                    kind_structure=StbColumnKindStructure.UNDEFINED,
                    id_section=1,
                    name=f"Column{i + 1}",
                    id_node_bottom=(i + 1) * 100,
                    id_node_top=(i + 2) * 100,
                )
            )
    stories = stb.stb_model.ensure.stb_stories().stb_story
    stories.append(
        StbStory(
            id=1,
            name="Story2",
            height=5000.0,
            kind=StbStoryKind.GENERAL,
            stb_node_id_list=StbNodeIdList(stb_node_id=[StbNodeId(id=200)]),
        )
    )
    stories.append(
        StbStory(
            id=2,
            name="Story5",
            height=20000.0,
            kind=StbStoryKind.GENERAL,
            stb_node_id_list=StbNodeIdList(stb_node_id=[StbNodeId(id=500)]),
        )
    )
    return stb


def test_membership_repository_story_member() -> None:
    stb: StBridge = _create_model()
    reporter = CollectingReporter()
    validate_schema(stb, reporter=reporter)
    assert reporter.is_valid(), reporter.report.to_text()
    m_repo: MembershipRepository = MembershipRepository(
        stb, looking_up=True, looking_down=True, concrete_strength=True
    )
    story_1 = m_repo.stories[1]
    assert story_1.node_ids == {200}
    assert story_1.member_ids == set()
    assert story_1.concrete_strength_member_ids == {(StbColumn, 100)}
    assert story_1.looking_up_member_ids == {(StbColumn, 100)}
    assert story_1.looking_down_member_ids == {
        (StbColumn, 200),
        (StbColumn, 300),
        (StbColumn, 400),
    }

    story_2 = m_repo.stories[2]
    assert story_2.node_ids == {500}
    assert story_2.member_ids == set()
    assert story_2.concrete_strength_member_ids == {(StbColumn, 400)}
    assert story_2.looking_up_member_ids == {
        (StbColumn, 200),
        (StbColumn, 300),
        (StbColumn, 400),
    }
    assert story_2.looking_down_member_ids == {(StbColumn, 500)}
