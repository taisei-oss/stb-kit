# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""
ST-Bridge v2.0.2の参照定義

公式スキーマでは表現されないため、仕様書に基づいて手書きで記述する。
現在はすべての参照定義は書いておらず、convert機能などで利用するものだけとなっている。
TODO: 仕様書の内容をすべて書き出す
"""

from ...data_model.common import StBridgeElement
from ...data_model.stb_v2_0_2 import (
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
from ..repo_common import _ByKind, _RefMap

_COLUMN_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecColumnRc,
        "S": StbSecColumnS,
        "SRC": StbSecColumnSrc,
        "CFT": StbSecColumnCft,
        "UNDEFINED": StbSecUndefined,
    },
)
_BEAM_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecBeamRc,
        "S": StbSecBeamS,
        "SRC": StbSecBeamSrc,
        "UNDEFINED": StbSecUndefined,
    },
)
_PILE_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecPileRc,
        "S": StbSecPileS,
        "PC": StbSecPileProduct,
    },
)

_SLAB_SECTION = _ByKind(
    "kind_structure",
    {
        "RC": StbSecSlabRc,
        "DECK": StbSecSlabDeck,
        "PRECAST": StbSecSlabPrecast,
    },
)

_ref_map_v202: _RefMap = {
    StbColumn: {
        "id_node_bottom": StbNode,
        "id_node_top": StbNode,
        "id_section": _COLUMN_SECTION,
    },
    StbPost: {
        "id_node_bottom": StbNode,
        "id_node_top": StbNode,
        "id_section": _COLUMN_SECTION,
    },
    StbGirder: {
        "id_node_start": StbNode,
        "id_node_end": StbNode,
        "id_section": _BEAM_SECTION,
    },
    StbBeam: {
        "id_node_start": StbNode,
        "id_node_end": StbNode,
        "id_section": _BEAM_SECTION,
    },
    StbBrace: {
        "id_node_start": StbNode,
        "id_node_end": StbNode,
        "id_section": StbSecBraceS,
    },
    StbSlab: {
        "id_section": _SLAB_SECTION,
    },
    StbWall: {
        "id_section": StbSecWallRc,
    },
    StbFooting: {
        "id_node": StbNode,
        "id_section": StbSecFoundationRc,
    },
    StbStripFooting: {
        "id_node_start": StbNode,
        "id_node_end": StbNode,
        "id_section": StbSecFoundationRc,
    },
    StbPile: {
        "id_node": StbNode,
        "id_section": _PILE_SECTION,
    },
    StbFoundationColumn: {
        "id_node": StbNode,
        "id_section_fd": StbSecColumnRc,
        "id_section_wr": StbSecFoundationRc,
    },
    StbParapet: {
        "id_node_start": StbNode,
        "id_node_end": StbNode,
        "id_section": StbSecParapetRc,
    },
}

_key_field_names_v202: dict[type[StBridgeElement], str] = {
    StbNode: "id",
    StbSecBeamRc: "id",
    StbSecBeamS: "id",
    StbSecBeamSrc: "id",
    StbSecBraceS: "id",
    StbSecColumnCft: "id",
    StbSecColumnRc: "id",
    StbSecColumnS: "id",
    StbSecColumnSrc: "id",
    StbSecFoundationRc: "id",
    StbSecParapetRc: "id",
    StbSecPileProduct: "id",
    StbSecPileRc: "id",
    StbSecPileS: "id",
    StbSecSlabDeck: "id",
    StbSecSlabPrecast: "id",
    StbSecSlabRc: "id",
    StbSecUndefined: "id",
    StbSecWallRc: "id",
    StbSecRollH: "name",
    StbSecBuildH: "name",
    StbSecRollBox: "name",
    StbSecBuildBox: "name",
    StbSecPipe: "name",
    StbSecRollT: "name",
    StbSecRollC: "name",
    StbSecRollL: "name",
    StbSecLipC: "name",
    StbSecFlatBar: "name",
    StbSecRoundBar: "name",
    StbSecSteelProduct: "name",
    StbSecSteelUndefined: "name",
}
