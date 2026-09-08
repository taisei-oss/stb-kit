# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.repository import get_repository
from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Code, Phase, Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import (
    StbBeam,
    StbBrace,
    StbColumn,
    StbFoundationColumn,
    StbGirder,
    StbMembers,
    StbModel,
    StbNodes,
    StbParapet,
    StbPile,
    StbPost,
    StBridge,
    StbStripFooting,
)

from ...._internal.data_model.element_data import (
    ElementData,
    ElementPlane,
    Node,
)
from ...._internal.vectors import Vector3d
from . import open
from .member.member_footing import stb_footing_to_line_element
from .member.member_line import stb_element_to_element_line
from .member.member_plane import (
    stb_slab_to_ifc_data,
    stb_wall_to_ifc_data,
)


def node_coords_from_stb_nodes(stb_nodes: StbNodes) -> dict[int, Vector3d]:
    return {node.id: Vector3d.from_stb_node(node) for node in stb_nodes.stb_node}


def node_infos_from_stb_nodes(stb_nodes: StbNodes) -> dict[int, Node]:
    return {
        node.id: Node(
            position=Vector3d.from_stb_node(node),
            xpath=node._path_xml(),
            guid=node.guid_or_none,
        )
        for node in stb_nodes.stb_node
    }


def stb_to_element_data(
    stb: StBridge,
    *,
    reporter: Reporter,
) -> ElementData:
    reporter.info(
        "---ST-Bridge->ジオメトリデータ変換処理開始---",
        code=Code.PROGRESS_INFO,
        phase=Phase.CONVERT_GEOMETRY,
    )
    result: ElementData = ElementData()
    repo: RepositoryLatest = get_repository(stb)
    try:
        stb_model: StbModel = stb.stb_model
        stb_members: StbMembers = stb_model.stb_members
    except NoneAccessError:
        reporter.error(
            "部材情報がありません",
            code=Code.MEMBER_NOT_FOUND,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return result
    try:
        stb_nodes: StbNodes = stb.stb_model.stb_nodes
    except NoneAccessError:
        reporter.error(
            "節点情報がありません",
            code=Code.MEMBER_NOT_FOUND,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return result
    node_coords: dict[int, Vector3d] = node_coords_from_stb_nodes(stb_nodes)
    try:
        _ = stb.stb_model.stb_sections
    except NoneAccessError:
        reporter.error(
            "断面情報がありません",
            code=Code.MEMBER_NOT_FOUND,
            phase=Phase.CONVERT_GEOMETRY,
        )
        return result
    stb_member_lines: list[
        StbColumn
        | StbPost
        | StbGirder
        | StbBeam
        | StbBrace
        | StbPile
        | StbStripFooting
        | StbFoundationColumn
        | StbParapet
    ] = []
    try:
        stb_member_lines.extend(stb_members.stb_columns.stb_column)
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(stb_members.stb_posts.stb_post)
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(stb_members.stb_girders.stb_girder)
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(stb_members.stb_beams.stb_beam)
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(stb_members.stb_braces.stb_brace)
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(stb_members.stb_strip_footings.stb_strip_footing)
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(stb_members.stb_piles.stb_pile)
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(
            stb_members.stb_foundation_columns.stb_foundation_column
        )
    except NoneAccessError:
        pass
    try:
        stb_member_lines.extend(stb_members.stb_parapets.stb_parapet)
    except NoneAccessError:
        pass

    result.extend(
        [
            stb_element_to_element_line(repo, ele, node_coords, reporter)
            for ele in stb_member_lines
        ]
    )
    stb_id_to_planes: dict[int, ElementPlane] = {}
    if stb_members.stb_slabs_or_none:
        for stb_slab in stb_members.stb_slabs.stb_slab:
            result.append(
                stb_slab_to_ifc_data(
                    stb_slab,
                    node_coords,
                    repo,
                    stb_id_to_planes,
                    reporter,
                )
            )
    if stb_members.stb_walls_or_none:
        for stb_wall in stb_members.stb_walls.stb_wall:
            result.append(
                stb_wall_to_ifc_data(
                    stb_wall,
                    node_coords,
                    repo,
                    stb_id_to_planes,
                    reporter,
                )
            )
    if stb_members.stb_open_arrangements_or_none:
        open.add_open(stb_model, stb_id_to_planes, reporter=reporter)

    if stb_members.stb_footings_or_none and stb_members.stb_footings.stb_footing:
        for stb_footing in stb_members.stb_footings.stb_footing:
            result.append(
                stb_footing_to_line_element(repo, stb_footing, node_coords, reporter)
            )
    return result
