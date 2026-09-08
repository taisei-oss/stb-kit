# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import Reporter

from stbkit.api.experimental.repository import RepositoryLatest
from stbkit.api.stb_latest import StbSecBeamSrc

from ....._internal.data_model.shape_data import ShapePair
from ...stb_latest_to_element_data.section import (
    sec_beam_rc,
    sec_beam_s,
)


def stb_sec_beam_src_to_shapes(
    repo: RepositoryLatest,
    sec_b_s: StbSecBeamSrc,
    reporter: Reporter,
) -> tuple[list[ShapePair], list[ShapePair]]:
    result_rc: list[ShapePair] = sec_beam_rc.stb_sec_beam_src_to_shapes_rc(sec_b_s)
    result_s: list[ShapePair] = sec_beam_s.stb_sec_beam_s_to_shapes(
        repo, sec_b_s, reporter
    )
    return result_rc, result_s
