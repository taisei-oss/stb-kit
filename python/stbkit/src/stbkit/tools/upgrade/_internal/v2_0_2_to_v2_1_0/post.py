# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_0
from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.repository import RepositoryV2_0_2
from stbkit.core.stb_reporting import Code, Phase, Reporter

from .hook_funcs.post_girder import post_girder
from .hook_funcs.post_open import post_open
from .hook_funcs.post_sec_beam_rc import post_sec_beam_rc, post_sec_beam_src_rc
from .hook_funcs.post_sec_beam_s import post_sec_beam_s, post_sec_beam_src_s


def post_conversion(
    before: StBridgeElement, after: StBridgeElement, *, reporter: Reporter
) -> None:
    if not isinstance(before, stb_v2_0_2.StBridge) or not isinstance(
        after, stb_v2_1_0.StBridge
    ):
        reporter.error(
            "変換後後処理が正しく実装されていません",
            code=Code.DEVELOPER_ERROR,
            phase=Phase.UPGRADE,
        )
        return
    repo_v202: RepositoryV2_0_2 = RepositoryV2_0_2(before)
    # Girder
    post_girder(before, after, repo_v202=repo_v202, reporter=reporter)
    # StbSecBeam_S
    post_sec_beam_s(before, after, reporter=reporter)
    # StbSecBeam_RC
    post_sec_beam_rc(before, after, reporter=reporter)
    # StbSecBeam_SRC
    # S断面処理時に断面をコピーする場合があるため、RC断面処理の後に実行する
    post_sec_beam_src_rc(before, after, reporter=reporter)
    post_sec_beam_src_s(before, after, reporter=reporter)
    # open
    post_open(before, after)
