# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import contextlib

from stbkit.core.stb_exceptions import NoneAccessError
from stbkit.core.stb_reporting import Reporter

from stbkit.api.stb_latest import StBridge
from stbkit.tools._internal.data_model.building_geometry import BuildingGeometry
from stbkit.tools._internal.data_model.element_data import (
    ElementData,
    Node,
)

from .element_data_to_building_geometry import element_data_to_building_geometry
from .stb_latest_to_element_data import (
    node_infos_from_stb_nodes,
    stb_to_element_data,
)


def stb_to_building_geometry(
    stb: StBridge,
    *,
    reporter: Reporter,
) -> BuildingGeometry:
    elements: ElementData = stb_to_element_data(
        stb,
        reporter=reporter,
    )

    node_datas: dict[int, Node] | None = None
    with contextlib.suppress(NoneAccessError):
        node_datas = node_infos_from_stb_nodes(stb.stb_model.stb_nodes)
    return element_data_to_building_geometry(
        elements,
        allow_polygons=False,
        reporter=reporter,
        node_infos=node_datas,
    )
