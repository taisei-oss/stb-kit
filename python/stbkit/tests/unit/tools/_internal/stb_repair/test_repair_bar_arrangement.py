# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import stb_v2_0_2, stb_v2_1_1
from stbkit.core.stb_reporting import NullReporter
from stbkit.testutils.constants import (
    V2_0_MODELS,
    V2_1_MODELS,
)

from stbkit.tools._internal.stb_repair._repair_bar_arrangement import (
    _repair_stb_sec_beam_rc,
    _StbSecBeamRcLike,
    _StbSecBeamRcLikeV20,
)


def test_repair_bar_arrangement_stb_sec_beam_rc_like() -> None:
    for module in V2_0_MODELS:
        assert isinstance(module.StbSecBeamRc(), _StbSecBeamRcLikeV20)
    for module in V2_1_MODELS:
        assert isinstance(module.StbSecBeamRc(), _StbSecBeamRcLike)


def test_repair_bar_arrangement_v2_0_2() -> None:
    element = stb_v2_0_2.StbSecBeamRc(
        stb_sec_bar_arrangement_beam_rc=stb_v2_0_2.StbSecBarArrangementBeamRc(
            stb_sec_bar_beam_rc_same=stb_v2_0_2.StbSecBarBeamRcSame()
        )
    )
    assert element.stb_sec_bar_arrangement_beam_rc_or_none is not None
    _repair_stb_sec_beam_rc(element, reporter=NullReporter())
    assert element.stb_sec_bar_arrangement_beam_rc_or_none is None


def test_repair_bar_arrangement_v2_1_1() -> None:
    element = stb_v2_1_1.StbSecBeamRc(
        stb_sec_bar_arrangement_beam_rc=[
            stb_v2_1_1.StbSecBarArrangementBeamRc(
                stb_sec_bar_beam_simple=stb_v2_1_1.StbSecBarBeamSimple()
            )
        ]
    )
    assert len(element.stb_sec_bar_arrangement_beam_rc) == 1
    _repair_stb_sec_beam_rc(element, reporter=NullReporter())
    assert len(element.stb_sec_bar_arrangement_beam_rc) == 0
