# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# 本ファイルはstbkit-codegenによって自動生成されました。
# このファイルを直接編集しないでください。

from typing import ClassVar, overload

from ..data_model.common import StBridgeElement
from ..data_model.stb_v2_0_2 import (
    StbBeam,
    StbBrace,
    StbColumn,
    StbFooting,
    StbFoundationColumn,
    StbGirder,
    StbNode,
    StbParapet,
    StbPile,
    StbPost,
    StbSecBeamRc,
    StbSecBeamS,
    StbSecBeamSrc,
    StbSecBraceS,
    StbSecBuildBox,
    StbSecBuildH,
    StbSecColumnCft,
    StbSecColumnRc,
    StbSecColumnS,
    StbSecColumnSrc,
    StbSecFlatBar,
    StbSecFoundationRc,
    StbSecLipC,
    StbSecParapetRc,
    StbSecPileProduct,
    StbSecPileRc,
    StbSecPileS,
    StbSecPipe,
    StbSecRollBox,
    StbSecRollC,
    StbSecRollH,
    StbSecRollL,
    StbSecRollT,
    StbSecRoundBar,
    StbSecSlabDeck,
    StbSecSlabPrecast,
    StbSecSlabRc,
    StbSecSteelProduct,
    StbSecSteelUndefined,
    StbSecUndefined,
    StbSecWallRc,
    StbSlab,
    StbStripFooting,
    StbWall,
)
from .repo_common import RepositoryBase, _DerefAccessor, _RefMap

type _StbColumnIdSection = (
    StbSecColumnRc | StbSecColumnS | StbSecColumnSrc | StbSecColumnCft | StbSecUndefined
)
type _StbGirderIdSection = StbSecBeamRc | StbSecBeamS | StbSecBeamSrc | StbSecUndefined
type _StbSlabIdSection = StbSecSlabRc | StbSecSlabDeck | StbSecSlabPrecast
type _StbPileIdSection = StbSecPileRc | StbSecPileS | StbSecPileProduct

class _StbColumnDeref(_DerefAccessor):
    @property
    def id_node_bottom(self) -> StbNode: ...
    @property
    def id_node_bottom_or_none(self) -> StbNode | None: ...
    @property
    def id_node_top(self) -> StbNode: ...
    @property
    def id_node_top_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbColumnIdSection: ...
    @property
    def id_section_or_none(self) -> _StbColumnIdSection | None: ...

class _StbPostDeref(_DerefAccessor):
    @property
    def id_node_bottom(self) -> StbNode: ...
    @property
    def id_node_bottom_or_none(self) -> StbNode | None: ...
    @property
    def id_node_top(self) -> StbNode: ...
    @property
    def id_node_top_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbColumnIdSection: ...
    @property
    def id_section_or_none(self) -> _StbColumnIdSection | None: ...

class _StbGirderDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbGirderIdSection: ...
    @property
    def id_section_or_none(self) -> _StbGirderIdSection | None: ...

class _StbBeamDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbGirderIdSection: ...
    @property
    def id_section_or_none(self) -> _StbGirderIdSection | None: ...

class _StbBraceDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecBraceS: ...
    @property
    def id_section_or_none(self) -> StbSecBraceS | None: ...

class _StbSlabDeref(_DerefAccessor):
    @property
    def id_section(self) -> _StbSlabIdSection: ...
    @property
    def id_section_or_none(self) -> _StbSlabIdSection | None: ...

class _StbWallDeref(_DerefAccessor):
    @property
    def id_section(self) -> StbSecWallRc: ...
    @property
    def id_section_or_none(self) -> StbSecWallRc | None: ...

class _StbFootingDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecFoundationRc: ...
    @property
    def id_section_or_none(self) -> StbSecFoundationRc | None: ...

class _StbStripFootingDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecFoundationRc: ...
    @property
    def id_section_or_none(self) -> StbSecFoundationRc | None: ...

class _StbPileDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> _StbPileIdSection: ...
    @property
    def id_section_or_none(self) -> _StbPileIdSection | None: ...

class _StbFoundationColumnDeref(_DerefAccessor):
    @property
    def id_node(self) -> StbNode: ...
    @property
    def id_node_or_none(self) -> StbNode | None: ...
    @property
    def id_section_fd(self) -> StbSecColumnRc: ...
    @property
    def id_section_fd_or_none(self) -> StbSecColumnRc | None: ...
    @property
    def id_section_wr(self) -> StbSecFoundationRc: ...
    @property
    def id_section_wr_or_none(self) -> StbSecFoundationRc | None: ...

class _StbParapetDeref(_DerefAccessor):
    @property
    def id_node_start(self) -> StbNode: ...
    @property
    def id_node_start_or_none(self) -> StbNode | None: ...
    @property
    def id_node_end(self) -> StbNode: ...
    @property
    def id_node_end_or_none(self) -> StbNode | None: ...
    @property
    def id_section(self) -> StbSecParapetRc: ...
    @property
    def id_section_or_none(self) -> StbSecParapetRc | None: ...

class RepositoryV2_0_2(RepositoryBase):
    _key_field_names: ClassVar[dict[type[StBridgeElement], str]]
    _ref_map: ClassVar[_RefMap]

    @overload
    def deref(self, element: StbColumn) -> _StbColumnDeref: ...
    @overload
    def deref(self, element: StbPost) -> _StbPostDeref: ...
    @overload
    def deref(self, element: StbGirder) -> _StbGirderDeref: ...
    @overload
    def deref(self, element: StbBeam) -> _StbBeamDeref: ...
    @overload
    def deref(self, element: StbBrace) -> _StbBraceDeref: ...
    @overload
    def deref(self, element: StbSlab) -> _StbSlabDeref: ...
    @overload
    def deref(self, element: StbWall) -> _StbWallDeref: ...
    @overload
    def deref(self, element: StbFooting) -> _StbFootingDeref: ...
    @overload
    def deref(self, element: StbStripFooting) -> _StbStripFootingDeref: ...
    @overload
    def deref(self, element: StbPile) -> _StbPileDeref: ...
    @overload
    def deref(self, element: StbFoundationColumn) -> _StbFoundationColumnDeref: ...
    @overload
    def deref(self, element: StbParapet) -> _StbParapetDeref: ...
    def get_steel(
        self,
        name: str,
    ) -> (
        StbSecRollH
        | StbSecBuildH
        | StbSecRollBox
        | StbSecBuildBox
        | StbSecPipe
        | StbSecRollT
        | StbSecRollC
        | StbSecRollL
        | StbSecLipC
        | StbSecFlatBar
        | StbSecRoundBar
        | StbSecSteelProduct
        | StbSecSteelUndefined
    ): ...
