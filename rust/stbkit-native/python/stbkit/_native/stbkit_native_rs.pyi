# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Callable
from typing import TYPE_CHECKING

# stbkit-nativeはstbkitへの依存を持たないので、
# 型チェック時のみstbkitの型をインポートする
if TYPE_CHECKING:
    from stbkit.tools._internal.data_model.building_geometry import BuildingGeometry

def _run_viewer(
    building_geometry: BuildingGeometry,
    on_element_click: Callable[..., None] | None = None,
) -> None: ...

