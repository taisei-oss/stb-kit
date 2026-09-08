# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from uuid import UUID

from stbkit.api.stb_latest import (
    StbColumn,
    StbColumns,
    StbGirder,
    StbGirders,
    StbMembers,
    StbModel,
    StbNode,
    StbNodes,
    StBridge,
)

from stbkit.core._internal.transform.select import select_elements
from stbkit.core.data_model._internal.filter_option import FilterOption, NameFilter
from stbkit.core.stb_reporting import get_reporter


def create_stb_sample() -> StBridge:
    return StBridge(
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[
                    StbNode(
                        id=1,
                        guid=UUID("00000000-0000-0000-0000-000000000001"),
                        x=1000.0,
                        y=2000.0,
                        z=3000.0,
                    ),
                    StbNode(
                        id=2,
                        guid=UUID("00000000-0000-0000-0000-000000000002"),
                        x=4000.0,
                        y=5000.0,
                        z=6000.0,
                    ),
                    StbNode(
                        id=3,
                        guid=UUID("00000000-0000-0000-0000-000000000003"),
                        x=7000.0,
                        y=8000.0,
                        z=9000.0,
                    ),
                    StbNode(
                        id=4,
                        guid=UUID("00000000-0000-0000-0000-000000000004"),
                        x=10000.0,
                        y=11000.0,
                        z=12000.0,
                    ),
                    StbNode(
                        id=5,
                        guid=UUID("00000000-0000-0000-0000-000000000005"),
                        x=13000.0,
                        y=14000.0,
                        z=15000.0,
                    ),
                ]
            ),
            stb_members=StbMembers(
                stb_columns=StbColumns(
                    stb_column=[
                        StbColumn(
                            id=1,
                            guid=UUID("00000000-0000-0000-0000-000000000011"),
                            id_node_bottom=1,
                            id_node_top=2,
                        ),
                        StbColumn(
                            id=2,
                            guid=UUID("00000000-0000-0000-0000-000000000012"),
                            id_node_bottom=2,
                            id_node_top=3,
                        ),
                    ]
                ),
                stb_girders=StbGirders(
                    stb_girder=[
                        StbGirder(
                            id=1,
                            guid=UUID("00000000-0000-0000-0000-000000000021"),
                            id_node_start=3,
                            id_node_end=4,
                        ),
                        StbGirder(
                            id=2,
                            guid=UUID("00000000-0000-0000-0000-000000000022"),
                            id_node_start=4,
                            id_node_end=5,
                        ),
                    ]
                ),
            ),
        )
    )


def test_select_elements_exclude_elements() -> None:
    option: FilterOption = FilterOption(
        global_element_filter=NameFilter(exclude=["StbColumn"])
    )
    stb: StBridge = create_stb_sample()
    select_elements(
        stb,
        option,
        reporter=get_reporter(),
    )
    assert stb.stb_model.stb_nodes.stb_node
    assert stb.stb_model.stb_members.stb_girders.stb_girder
    assert not stb.stb_model.stb_members.stb_columns.stb_column


def test_select_elements_include_elements() -> None:
    option: FilterOption = FilterOption(
        global_element_filter=NameFilter(include=["StbNode"])
    )
    stb: StBridge = create_stb_sample()
    select_elements(
        stb,
        option,
        reporter=get_reporter(),
    )
    assert stb.stb_model.stb_nodes.stb_node
    assert not stb.stb_model.stb_members_or_none


def test_select_elements_element_attributes_option() -> None:
    option: FilterOption = FilterOption(
        element_attribute_filters={
            "StbNode": NameFilter(exclude=["guid"]),
            "StbColumn": NameFilter(include=["id"]),
        },
    )
    stb: StBridge = create_stb_sample()
    select_elements(
        stb,
        option,
        reporter=get_reporter(),
    )
    for node in stb.stb_model.stb_nodes.stb_node:
        assert node.id is not None
        assert node.guid_or_none is None
        assert node.x is not None
    for column in stb.stb_model.stb_members.stb_columns.stb_column:
        assert column.id is not None
        assert column.guid_or_none is None
        assert column.id_node_bottom_or_none is None
    for girder in stb.stb_model.stb_members.stb_girders.stb_girder:
        assert girder.id is not None
        assert girder.guid_or_none is not None
        assert girder.id_node_start_or_none is not None


def test_select_elements_exclude_attributes_global() -> None:
    option: FilterOption = FilterOption(
        global_attribute_filter=NameFilter(exclude=["guid"]),
    )
    stb: StBridge = create_stb_sample()
    select_elements(
        stb,
        option,
        reporter=get_reporter(),
    )
    for node in stb.stb_model.stb_nodes.stb_node:
        assert node.id is not None
        assert node.guid_or_none is None
        assert node.x is not None
    for column in stb.stb_model.stb_members.stb_columns.stb_column:
        assert column.id is not None
        assert column.guid_or_none is None
        assert column.id_node_bottom_or_none is not None
    for girder in stb.stb_model.stb_members.stb_girders.stb_girder:
        assert girder.id is not None
        assert girder.guid_or_none is None
        assert girder.id_node_start_or_none is not None
