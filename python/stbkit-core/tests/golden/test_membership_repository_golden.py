# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.testutils.data_model_sample.golden_v2_1_1 import (
    golden_v2_1_1_frame_1x1x1_rc,
)

from stbkit.core.data_model.stb_v2_1_1 import (
    StbColumn,
    StbGirder,
    StbNode,
    StbParallelAxes,
    StbParallelAxis,
    StBridge,
)
from stbkit.core.membership._internal.membership_repository import MembershipRepository
from stbkit.core.repository import RepositoryV2_1_1, get_repository


def test_membership_repository_with_golden_v2_1_1_frame_1x1x1_rc() -> None:
    stb: StBridge = golden_v2_1_1_frame_1x1x1_rc()
    repo: RepositoryV2_1_1 = get_repository(stb)
    repo_m: MembershipRepository = MembershipRepository(
        stb,
        repository=repo,
        looking_up=True,
        looking_down=True,
        concrete_strength=True,
    )
    parallel_axes = repo_m.parallel_axes
    assert len(parallel_axes) == 4
    assert list(parallel_axes.keys()) == [11, 12, 21, 22]
    stb_parallel_axis_list = list(
        stb.stb_model.stb_axes.iter_descendants(StbParallelAxis)
    )
    assert len(stb_parallel_axis_list) == 4
    for stb_parallel_axis in stb_parallel_axis_list:
        membership = parallel_axes.get(stb_parallel_axis.id)
        assert membership is not None
        assert len(membership.node_ids) == 4
        stb_parallel_axes = stb_parallel_axis._parent
        assert isinstance(stb_parallel_axes, StbParallelAxes)
        assert stb_parallel_axes.x == 0
        assert stb_parallel_axes.y == 0
        for node_id in membership.node_ids:
            node = repo.get(StbNode, node_id)
            if stb_parallel_axes.angle == 270:
                assert node.x == stb_parallel_axis.distance
            elif stb_parallel_axes.angle == 0:
                assert node.y == stb_parallel_axis.distance
            else:
                raise ValueError("利用していない角度")
        assert len(membership.member_ids) == 4
        for element_type, element_id in membership.member_ids:
            element = repo.get(element_type, element_id)
            if element_type is StbColumn:
                assert isinstance(element, StbColumn)
                assert element.id_node_bottom in membership.node_ids
                assert element.id_node_top in membership.node_ids
            elif element_type is StbGirder:
                assert isinstance(element, StbGirder)
                assert element.id_node_start in membership.node_ids
                assert element.id_node_end in membership.node_ids
            else:
                raise ValueError("利用していない部材")
    assert len(repo_m._node_id_to_story_id) == 8
    concrete_column_counts: dict[int, int] = {}
    for stb_story in stb.stb_model.stb_stories.stb_story:
        story_membership = repo_m.stories.get(stb_story.id)
        assert story_membership is not None
        assert len(story_membership.node_ids) == 4
        girder_count: int = 0
        concrete_girder_count: int = 0
        for element_type, element_id in story_membership.member_ids:
            element = repo.get(element_type, element_id)
            if element_type is StbGirder:
                assert isinstance(element, StbGirder)
                assert element.id_node_start in story_membership.node_ids
                assert element.id_node_end in story_membership.node_ids
                girder_count += 1
            else:
                raise ValueError("利用していない部材")
        for eleent_type, element_id in story_membership.concrete_strength_member_ids:
            element = repo.get(eleent_type, element_id)
            if eleent_type is StbGirder:
                assert isinstance(element, StbGirder)
                assert element.id_node_start in story_membership.node_ids
                assert element.id_node_end in story_membership.node_ids
                concrete_girder_count += 1
            elif eleent_type is StbColumn:
                assert isinstance(element, StbColumn)
                assert element.id_node_top in story_membership.node_ids
                concrete_column_counts[stb_story.id] = (
                    concrete_column_counts.get(stb_story.id, 0) + 1
                )
            else:
                raise ValueError("利用していない部材")
        assert girder_count == 4
        assert concrete_girder_count == 4
    import sys

    print("Concrete column counts:", concrete_column_counts, file=sys.stderr)
    assert concrete_column_counts == {2: 4}
