# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from types import ModuleType

from stbkit.core.data_model import (
    stb_v2_0_0,
    stb_v2_0_1,
    stb_v2_0_2,
    stb_v2_1_0,
    stb_v2_1_1,
)

OLDEST_STB_MODEL: ModuleType = stb_v2_0_0
LATEST_STB_MODEL: ModuleType = stb_v2_1_1
V2_0_MODELS: tuple[ModuleType, ...] = (stb_v2_0_0, stb_v2_0_1, stb_v2_0_2)
V2_1_MODELS: tuple[ModuleType, ...] = (stb_v2_1_0, stb_v2_1_1)
ALL_MODELS: tuple[ModuleType, ...] = V2_0_MODELS + V2_1_MODELS


def models(
    *, start_version: str | None = None, end_version: str | None = None
) -> tuple[ModuleType, ...]:

    if start_version is None:
        start_index: int = 0
    else:
        start_index = next(
            i for i, m in enumerate(ALL_MODELS) if start_version == m.VERSION
        )
    if end_version is None:
        end_index: int = len(ALL_MODELS) - 1
    else:
        end_index = next(
            i for i, m in enumerate(ALL_MODELS) if end_version == m.VERSION
        )
    return ALL_MODELS[start_index : end_index + 1]
