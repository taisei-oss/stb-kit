# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Protocol

from stbkit.core.data_model import (
    stb_v2_0_0,
    stb_v2_0_1,
    stb_v2_0_2,
    stb_v2_1_0,
    stb_v2_1_1,
)
from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_exceptions import (
    ReferenceElementNotFoundError,
    UnsupportedStbVersionError,
)

from ..vectors import Vector3d


class HasXyz(Protocol):
    @property
    def x(self) -> float: ...
    @property
    def y(self) -> float: ...
    @property
    def z(self) -> float: ...


def get_node_coordinate(stb: StBridgeRoot, id: int) -> Vector3d:
    if not isinstance(
        stb,
        (
            stb_v2_0_0.StBridge,
            stb_v2_0_1.StBridge,
            stb_v2_0_2.StBridge,
            stb_v2_1_0.StBridge,
            stb_v2_1_1.StBridge,
        ),
    ):
        raise UnsupportedStbVersionError(stb.version)

    for node in stb.stb_model.stb_nodes.stb_node:
        if node.id == id:
            return Vector3d.from_stb_node(node)
    raise ReferenceElementNotFoundError(f"StbNode id={id}が見つかりません")
