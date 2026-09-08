# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import Reporter

from stbkit.api.stb_latest import StBridge

from .building_geometry_to_ply_text import building_geometry_to_ply_text
from .element_data_to_building_geometry import element_data_to_building_geometry
from .stb_latest_to_element_data import stb_to_element_data


def stb_to_ply_text(stb: StBridge, *, reporter: Reporter) -> str:
    geom = element_data_to_building_geometry(
        stb_to_element_data(stb, reporter=reporter),
        allow_polygons=True,
        reporter=reporter,
    )
    return building_geometry_to_ply_text(geom)
