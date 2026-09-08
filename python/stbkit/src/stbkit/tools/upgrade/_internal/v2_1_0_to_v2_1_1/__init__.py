# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model import (
    stb_v2_1_0,
    stb_v2_1_1,
)
from stbkit.core.stb_reporting import Code, Phase, Reporter
from stbkit.core.validation._internal.validator import _validate

from .. import common
from . import tables
from .hooks import HOOKS


def upgrade_v2_1_0_to_v2_1_1(
    stb: stb_v2_1_0.StBridge,
    *,
    reporter: Reporter,
) -> stb_v2_1_1.StBridge:
    reporter.info(
        "---v2.1.0->v2.1.1変換処理開始---",
        code=Code.PROGRESS_INFO,
        phase=Phase.UPGRADE,
    )
    new_stb = common.convert_element(
        stb,
        stb_v2_1_1,
        ignore_field=tables.ignore_field,
        class_name_table=tables.class_name_table,
        attr_name_table=tables.attr_name_table,
        hooks=HOOKS,
        reporter=reporter,
    )

    if isinstance(new_stb, stb_v2_1_1.StBridge):
        reporter.info(
            "---v2.1.0->v2.1.1変換処理完了---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        reporter.info(
            "---v2.1.1バリデーション開始---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        _validate(reporter=reporter, stb=new_stb)
        reporter.info(
            "---v2.1.1バリデーション完了---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        return new_stb
    else:
        raise TypeError("ST-Bridgeのバージョン変換に失敗しました")
