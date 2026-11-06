# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

from collections.abc import Collection, Iterator
from dataclasses import dataclass
from typing import Final, Protocol, runtime_checkable

from ...data_model.common import (
    StBridgeElement,
    StBridgeRoot,
    _ElementNames,
    _ElementTypes,
)
from ...repository import RepositoryBase, get_repository
from ...stb_exceptions import (
    DeveloperError,
    NoneAccessError,
    ReferenceElementNotFoundError,
)
from ...stb_reporting import Code, Phase, Reporter, get_reporter

_UNKNOWN_STORY_ID: Final[int] = -1


@runtime_checkable
class _StBridgeElementLike(Protocol):
    def iter_descendants(
        self,
        element_types: _ElementTypes | None = None,
        *,
        class_names: _ElementNames | None = None,
        xml_names: _ElementNames | None = None,
        min_depth: int = 1,
        max_depth: int | None = None,
        include_extensions: bool = False,
    ) -> Iterator[StBridgeElement]: ...


@runtime_checkable
class _StBridgeLike(Protocol):
    @property
    def stb_model(self) -> _StbModelLike: ...


@runtime_checkable
class _StbModelLike(Protocol):
    @property
    def stb_axes(self) -> _StbAxesLike: ...
    @property
    def stb_stories(self) -> _StbStoriesLike: ...
    @property
    def stb_members(self) -> _StBridgeElementLike: ...


@runtime_checkable
class _StbAxesLike(Protocol):
    @property
    def stb_parallel_axes(self) -> list[_StbParallelAxesLike]: ...


@runtime_checkable
class _StbParallelAxesLike(Protocol):
    @property
    def stb_parallel_axis(self) -> list[_StbParallelAxisLike]: ...


@runtime_checkable
class _StbParallelAxisLike(Protocol):
    @property
    def id(self) -> int: ...
    @property
    def stb_node_id_list(self) -> _StbNodeIdListLike: ...


@runtime_checkable
class _StbNodeIdListLike(Protocol):
    @property
    def stb_node_id(self) -> list[_StbNodeIdLike]: ...


@runtime_checkable
class _StbNodeIdLike(Protocol):
    @property
    def id(self) -> int: ...


@runtime_checkable
class _StbNodeIdOrderLike(Protocol):
    @property
    def content(self) -> list[int]: ...


@runtime_checkable
class _StbStoriesLike(Protocol):
    @property
    def stb_story(self) -> list[_StbStoryLike]: ...


@runtime_checkable
class _StbStoryLike(Protocol):
    @property
    def id(self) -> int: ...
    @property
    def height(self) -> float: ...
    @property
    def stb_node_id_list(self) -> _StbNodeIdListLike: ...


@runtime_checkable
class _ColumnLike(Protocol):
    @property
    def id(self) -> int: ...
    @property
    def id_node_bottom(self) -> int: ...
    @property
    def id_node_top(self) -> int: ...


@runtime_checkable
class _GirderLike(Protocol):
    @property
    def id(self) -> int: ...
    @property
    def id_node_start(self) -> int: ...
    @property
    def id_node_end(self) -> int: ...


@runtime_checkable
class _PlateLike(Protocol):
    @property
    def id(self) -> int: ...
    @property
    def stb_node_id_order(self) -> _StbNodeIdOrderLike: ...


@runtime_checkable
class _FoundationLike(Protocol):
    @property
    def id(self) -> int: ...
    @property
    def id_node(self) -> int: ...


@runtime_checkable
class _OpenLike(Protocol):
    @property
    def id(self) -> int: ...
    @property
    def id_member(self) -> int: ...


@runtime_checkable
class _PanelZoneArrangementLike(Protocol):
    @property
    def id_node(self) -> int: ...


@dataclass
class _AxisMembership:
    node_ids: set[int]
    member_ids: set[tuple[type[StBridgeElement], int]]


@dataclass
class _StoryMembership:
    node_ids: set[int]
    member_ids: set[tuple[type[StBridgeElement], int]]
    looking_up_member_ids: set[tuple[type[StBridgeElement], int]]
    looking_down_member_ids: set[tuple[type[StBridgeElement], int]]
    concrete_strength_member_ids: set[tuple[type[StBridgeElement], int]]


class MembershipRepository:
    def __init__(
        self,
        stb: StBridgeRoot,
        *,
        reporter: Reporter | None = None,
        repository: RepositoryBase | None = None,
        looking_up: bool = False,
        looking_down: bool = False,
        concrete_strength: bool = False,
    ):
        self.reporter = reporter or get_reporter()
        self.looking_up = looking_up
        self.looking_down = looking_down
        self.concrete_strength = concrete_strength
        if not isinstance(stb, _StBridgeLike):
            raise DeveloperError("対応していないStBridgeです")
        self._stb = stb
        self._repository = repository or get_repository(stb)
        if self._repository._stb is not self._stb:
            raise DeveloperError("対象のStBridgeと異なるリポジトリが指定されています")
        self.parallel_axes: dict[int, _AxisMembership] = {}
        # 未所属は-1に属させる
        self.stories: dict[int, _StoryMembership] = {}

        self._node_id_to_story_id: dict[int, int] = {}
        self._set_axes()
        self._set_members(self.parallel_axes.values())
        self._set_stories()
        self._set_story_members()

    def _set_members(self, memberships: Collection[_AxisMembership]) -> None:
        stb_members: _StBridgeElementLike = self._stb.stb_model.stb_members
        for member in stb_members.iter_descendants(min_depth=2, max_depth=2):
            for membership in memberships:
                try:
                    node_ids = membership.node_ids
                    if isinstance(
                        member, (_ColumnLike, _GirderLike, _PlateLike, _FoundationLike)
                    ):
                        if (
                            (
                                isinstance(member, _ColumnLike)
                                and member.id_node_bottom in node_ids
                                and member.id_node_top in node_ids
                            )
                            or (
                                isinstance(member, _GirderLike)
                                and member.id_node_start in node_ids
                                and member.id_node_end in node_ids
                            )
                            or (
                                isinstance(member, _PlateLike)
                                and all(
                                    id_node in node_ids
                                    for id_node in member.stb_node_id_order.content
                                )
                            )
                            or (
                                isinstance(member, _FoundationLike)
                                and member.id_node in node_ids
                            )
                        ):
                            membership.member_ids.add((type(member), member.id))
                    elif isinstance(member, _OpenLike):
                        try:
                            ref_element = self._repository._deref_field(
                                member, "id_member"
                            )
                            if hasattr(ref_element, "id"):
                                ref_id = ref_element.id
                                if (type(ref_element), ref_id) in membership.member_ids:
                                    membership.member_ids.add((type(member), member.id))
                            else:
                                self.reporter.error(
                                    "参照部材にidが存在しないため、"
                                    "通り心処理で問題が生じる可能性があります: "
                                    f"{member}",
                                    code=Code.SCHEMA_ERROR,
                                    phase=Phase.LOAD,
                                    stb_element=member
                                    if isinstance(member, StBridgeElement)
                                    else None,
                                )
                        except ReferenceElementNotFoundError as e:
                            self.reporter.error(
                                "参照部材が見つからなかったため、"
                                f"通り心処理で問題が生じる可能性があります: {e}",
                                code=Code.SCHEMA_ERROR,
                                phase=Phase.LOAD,
                                stb_element=member
                                if isinstance(member, StBridgeElement)
                                else None,
                            )
                            continue
                    elif isinstance(member, _PanelZoneArrangementLike):
                        if member.id_node in node_ids:
                            membership.member_ids.add((type(member), member.id_node))
                    else:
                        if member._xml_name() == "StbOpen":
                            # v2.0.XのStbOpenは、断面につき、部材につかないため、
                            # 階の判定ができない
                            pass
                        else:
                            self.reporter.error(
                                "想定外の部材タイプが検出されたため、"
                                "通り心処理で問題が生じる可能性があります",
                                code=Code.UNEXPECTED_ERROR,
                                phase=Phase.LOAD,
                                stb_element=member
                                if isinstance(member, StBridgeElement)
                                else None,
                            )
                except NoneAccessError as e:
                    self.reporter.error(
                        f"通り心処理の最中にNoneが検出されたため、"
                        f"通り心処理で問題が生じる可能性があります: {e}",
                        code=Code.SCHEMA_ERROR,
                        phase=Phase.LOAD,
                        stb_element=member
                        if isinstance(member, StBridgeElement)
                        else None,
                    )
                    continue

    def _set_axes(self) -> None:
        try:
            stb_axes: _StbAxesLike = self._stb.stb_model.stb_axes
        except NoneAccessError:
            return
        for stb_parallel_axes in stb_axes.stb_parallel_axes:
            for stb_parallel_axis in stb_parallel_axes.stb_parallel_axis:
                try:
                    stb_node_id_list = stb_parallel_axis.stb_node_id_list
                except NoneAccessError:
                    continue
                try:
                    node_ids: set[int] = {
                        stb_node_id.id for stb_node_id in stb_node_id_list.stb_node_id
                    }
                except NoneAccessError as e:
                    self.reporter.error(
                        "StbNodeId.idがNoneの場合があり、"
                        f"通り心処理で問題が生じている可能性があります: {e}",
                        code=Code.SCHEMA_ERROR,
                        phase=Phase.LOAD,
                        stb_element=stb_parallel_axis
                        if isinstance(stb_parallel_axis, StBridgeElement)
                        else None,
                    )
                    continue
                membership: _AxisMembership = _AxisMembership(
                    node_ids=node_ids,
                    member_ids=set(),
                )
                self.parallel_axes[stb_parallel_axis.id] = membership

    def _set_stories(self) -> None:
        try:
            stb_stories: _StbStoriesLike = self._stb.stb_model.stb_stories
        except NoneAccessError:
            return
        for stb_story in stb_stories.stb_story:
            try:
                stb_node_id_list = stb_story.stb_node_id_list
            except NoneAccessError:
                node_ids: set[int] = set()
            else:
                try:
                    node_ids = {
                        stb_node_id.id for stb_node_id in stb_node_id_list.stb_node_id
                    }
                except NoneAccessError as e:
                    self.reporter.error(
                        "StbNodeId.idがNoneの場合があり、"
                        f"通り心処理で問題が生じている可能性があります: {e}",
                        code=Code.SCHEMA_ERROR,
                        phase=Phase.LOAD,
                        stb_element=stb_story
                        if isinstance(stb_story, StBridgeElement)
                        else None,
                    )
                    continue
            for node_id in node_ids:
                if node_id in self._node_id_to_story_id:
                    self.reporter.error(
                        "複数の階に所属する節点があるため、"
                        "階の処理で問題が生じている可能性があります: "
                        f"StbNode.id={node_id} は既に"
                        f"StbStory.id={self._node_id_to_story_id[node_id]}に所属しています",
                        code=Code.SCHEMA_ERROR,
                        phase=Phase.LOAD,
                        stb_element=stb_story
                        if isinstance(stb_story, StBridgeElement)
                        else None,
                    )
                self._node_id_to_story_id[node_id] = stb_story.id
            membership: _StoryMembership = _StoryMembership(
                node_ids=node_ids,
                member_ids=set(),
                looking_up_member_ids=set(),
                looking_down_member_ids=set(),
                concrete_strength_member_ids=set(),
            )
            self.stories[stb_story.id] = membership

    def _set_story_members(self) -> None:
        """部材の階所属を設定する

        階所属のルールは現状では下記のようにしている
        - member_ids: 全ての節点がその会に含まれている部材
        - concrete_strength_member_ids: ST-Bridge_XML使用説明書(v.2.1.1) p.4-22
            に基づき、所属判定した部材。コンクリート強度の確認に用いる
        - looking_up_member_ids: 見上げ図相当の部材
            一番上の節点が所属している部部材、または、
            一番上の節点が階に所属しておらずその階と１つ下の階の間にある部材
        - looking_down_member_ids: 見下げ図相当の部材
            一番下の節点が所属している部材、または、
            一番下の節点が階に所属しておらずその階と１つ上の階の間にある部材

        階所属の判定は試験的な実装のためパフォーマンスを考慮していない。
        TODO: 階所属判定の効率化
        """
        stb_members: _StBridgeElementLike = self._stb.stb_model.stb_members
        # _OpenLikeで部材を参照させるための辞書
        member_id_to_story_id: dict[tuple[type[StBridgeElement], int], int] = {}
        NodeClass: type[StBridgeElement] | None = None
        story_list: list[_StbStoryLike] = []
        story_list_reverse: list[_StbStoryLike] = []
        NodeClass = self._stb._get_type_same_module("StbNode")
        if not hasattr(NodeClass, "z") or not hasattr(NodeClass, "id"):
            self.reporter.error(
                "StbNodeクラスが正しく取得できなかったため、"
                "階の処理で問題が生じている可能性があります",
                code=Code.UNEXPECTED_ERROR,
                phase=Phase.LOAD,
            )
            return
        if self.looking_up or self.looking_down:
            try:
                story_list = sorted(
                    self._stb.stb_model.stb_stories.stb_story, key=lambda s: s.height
                )
                story_list_reverse = sorted(
                    self._stb.stb_model.stb_stories.stb_story,
                    key=lambda s: s.height,
                    reverse=True,
                )
            except NoneAccessError:
                pass
        for member in stb_members.iter_descendants(min_depth=2, max_depth=2):
            story_ids: set[int] = set()
            node_ids: set[int] = set()
            try:
                if isinstance(
                    member, (_ColumnLike, _GirderLike, _PlateLike, _FoundationLike)
                ):
                    if isinstance(member, _ColumnLike):
                        node_ids = {member.id_node_bottom, member.id_node_top}
                    elif isinstance(member, _GirderLike):
                        node_ids = {member.id_node_start, member.id_node_end}
                    elif isinstance(member, _PlateLike):
                        node_ids = set(member.stb_node_id_order.content)
                    elif isinstance(member, _FoundationLike):
                        node_ids = {member.id_node}
                    if not node_ids:
                        self.reporter.error(
                            "部材の節点が空のため、階の判定に失敗しました",
                            code=Code.SCHEMA_ERROR,
                            phase=Phase.LOAD,
                            stb_element=member
                            if isinstance(member, StBridgeElement)
                            else None,
                        )
                        continue
                    story_ids = {
                        self._node_id_to_story_id.get(node_id, _UNKNOWN_STORY_ID)
                        for node_id in node_ids
                    }
                    story_id: int = next(iter(story_ids), _UNKNOWN_STORY_ID)
                    if len(story_ids) == 1 and story_id != _UNKNOWN_STORY_ID:
                        membership = self.stories.get(story_id)
                        if membership:
                            item = (type(member), member.id)
                            membership.member_ids.add(item)
                            if self.looking_up:
                                membership.looking_up_member_ids.add(item)
                            if self.looking_down:
                                membership.looking_down_member_ids.add(item)
                            if self.concrete_strength:
                                membership.concrete_strength_member_ids.add(item)
                            member_id_to_story_id[(type(member), member.id)] = story_id
                    else:
                        if self.concrete_strength:
                            # ST-Bridge_XML使用説明書(v.2.1.1) p.4-22を参考にした
                            # コンクリート強度を参照する階の設定
                            if isinstance(
                                member, _ColumnLike
                            ) and member._xml_name() in (
                                "StbColumn",
                                "StbPost",
                            ):
                                story_id = (
                                    self._node_id_to_story_id.get(member.id_node_top)
                                    or _UNKNOWN_STORY_ID
                                )
                            elif isinstance(
                                member, _GirderLike
                            ) and member._xml_name() in (
                                "StbGirder",
                                "StbBeam",
                                "StbStripFooting",
                                "StbParapet",
                            ):
                                story_id = (
                                    self._node_id_to_story_id.get(member.id_node_start)
                                    or _UNKNOWN_STORY_ID
                                )
                            elif (
                                isinstance(member, _PlateLike)
                                and member._xml_name() == "StbSlab"
                            ):
                                story_id = (
                                    self._node_id_to_story_id.get(
                                        member.stb_node_id_order.content[0]
                                    )
                                    or _UNKNOWN_STORY_ID
                                )
                            elif (
                                isinstance(member, _PlateLike)
                                and member._xml_name() == "StbWall"
                            ):
                                story_id = (
                                    self._node_id_to_story_id.get(
                                        member.stb_node_id_order.content[-1]
                                    )
                                    or _UNKNOWN_STORY_ID
                                )
                            elif isinstance(
                                member, _FoundationLike
                            ) and member._xml_name() in (
                                "StbFooting",
                                "StbFoundationColumn",
                            ):
                                story_id = (
                                    self._node_id_to_story_id.get(member.id_node)
                                    or _UNKNOWN_STORY_ID
                                )
                            else:
                                self.reporter.error(
                                    "想定しない要素タイプです",
                                    code=Code.SCHEMA_ERROR,
                                    phase=Phase.LOAD,
                                    stb_element=member
                                    if isinstance(member, StBridgeElement)
                                    else None,
                                )
                                continue
                            membership = self.stories.get(story_id)
                            if membership:
                                item = (type(member), member.id)
                                membership.concrete_strength_member_ids.add(item)
                                member_id_to_story_id[item] = story_id

                        if self.looking_up or self.looking_down:
                            # 見上げ,見下げ処理
                            it = iter(node_ids)
                            bottom_node = self._repository.get(NodeClass, next(it))
                            top_node = bottom_node
                            for node_id in it:
                                tmp_node = self._repository.get(NodeClass, node_id)
                                if (
                                    hasattr(bottom_node, "z")
                                    and hasattr(tmp_node, "z")
                                    and bottom_node.z > tmp_node.z
                                ):
                                    bottom_node = tmp_node
                                if (
                                    hasattr(top_node, "z")
                                    and hasattr(tmp_node, "z")
                                    and top_node.z < tmp_node.z
                                ):
                                    top_node = tmp_node
                            bottom_story: _StbStoryLike | None = None
                            top_story: _StbStoryLike | None = None
                            if self.looking_up:
                                for story in story_list:
                                    story_membership = self.stories.get(story.id)
                                    if story_membership is None:
                                        continue
                                    if (
                                        hasattr(top_node, "id")
                                        and top_node.id in story_membership.node_ids
                                    ):
                                        top_story = story
                                        break
                                if top_story is None:
                                    for story in story_list:
                                        if (
                                            hasattr(top_node, "z")
                                            and top_node.z <= story.height
                                        ):
                                            top_story = story
                                            break
                            if self.looking_down:
                                for story in story_list_reverse:
                                    story_membership = self.stories.get(story.id)
                                    if story_membership is None:
                                        continue
                                    if (
                                        hasattr(bottom_node, "id")
                                        and bottom_node.id in story_membership.node_ids
                                    ):
                                        bottom_story = story
                                        break
                                if bottom_story is None:
                                    for story in story_list_reverse:
                                        if (
                                            hasattr(bottom_node, "z")
                                            and bottom_node.z >= story.height
                                        ):
                                            bottom_story = story
                                            break
                            if top_story is not None:
                                top_story_membership = self.stories.get(top_story.id)
                                if top_story_membership is not None:
                                    top_story_membership.looking_up_member_ids.add(
                                        (type(member), member.id)
                                    )
                            if bottom_story is not None:
                                bottom_story_membership = self.stories.get(
                                    bottom_story.id
                                )
                                if bottom_story_membership is not None:
                                    bottom_story_membership.looking_down_member_ids.add(
                                        (type(member), member.id)
                                    )

                elif isinstance(member, _OpenLike):
                    try:
                        ref_element = self._repository._deref_field(member, "id_member")
                        if hasattr(ref_element, "id"):
                            ref_id = ref_element.id
                            if (type(ref_element), ref_id) in member_id_to_story_id:
                                story_id = member_id_to_story_id[
                                    (type(ref_element), ref_id)
                                ]
                                membership = self.stories.get(story_id)
                                if membership:
                                    membership.member_ids.add((type(member), member.id))
                                    member_id_to_story_id[(type(member), member.id)] = (
                                        story_id
                                    )
                        else:
                            self.reporter.error(
                                "参照部材にidが存在しないため、"
                                "階の処理で問題が生じる可能性があります: "
                                f"{member}",
                                code=Code.SCHEMA_ERROR,
                                phase=Phase.LOAD,
                                stb_element=member
                                if isinstance(member, StBridgeElement)
                                else None,
                            )
                    except ReferenceElementNotFoundError as e:
                        self.reporter.error(
                            "参照部材が見つからなかったため、"
                            f"階の処理で問題が生じる可能性があります: {e}",
                            code=Code.SCHEMA_ERROR,
                            phase=Phase.LOAD,
                            stb_element=member
                            if isinstance(member, StBridgeElement)
                            else None,
                        )
                        continue
                elif isinstance(member, _PanelZoneArrangementLike):
                    story_id_or_none: int | None = self._node_id_to_story_id.get(
                        member.id_node
                    )
                    if story_id_or_none:
                        membership = self.stories.get(story_id_or_none)
                        if membership:
                            membership.member_ids.add((type(member), member.id_node))
                else:
                    if member._xml_name() == "StbOpen":
                        # v2.0.XのStbOpenは、断面につき、部材につかないため、
                        # 階の判定ができない
                        pass
                    else:
                        self.reporter.error(
                            "想定外の部材タイプが検出されたため、"
                            "通り心処理で問題が生じる可能性があります",
                            code=Code.UNEXPECTED_ERROR,
                            phase=Phase.LOAD,
                            stb_element=member
                            if isinstance(member, StBridgeElement)
                            else None,
                        )
            except NoneAccessError as e:
                self.reporter.error(
                    f"通り心処理の最中にNoneが検出されたため、"
                    f"通り心処理で問題が生じる可能性があります: {e}",
                    code=Code.SCHEMA_ERROR,
                    phase=Phase.LOAD,
                    stb_element=member if isinstance(member, StBridgeElement) else None,
                )
                continue

    def refresh(self) -> None:
        self._repository.refresh()
        self.parallel_axes.clear()
        self.stories.clear()
        self._node_id_to_story_id.clear()
        self._set_axes()
        self._set_members(self.parallel_axes.values())
        self._set_stories()
        self._set_story_members()
