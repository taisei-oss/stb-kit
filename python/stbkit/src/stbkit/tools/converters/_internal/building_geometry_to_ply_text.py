# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from ..._internal.data_model.building_geometry import BuildingGeometry


def building_geometry_to_ply_text(geom: BuildingGeometry) -> str:
    result: list[str] = []
    result.append("ply")
    result.append("format ascii 1.0")
    result.append(f"element vertex {geom.mesh.vertex_count}")
    result.append("property float x")
    result.append("property float y")
    result.append("property float z")
    result.append(f"element face {geom.mesh.face_count}")
    result.append("property list uchar int vertex_index")
    result.append("end_header")
    positions = geom.mesh.positions
    for i in range(geom.mesh.vertex_count):
        result.append(
            f"{round(positions[i * 3], 5)} {round(positions[i * 3 + 1], 5)} "
            f"{round(positions[i * 3 + 2], 5)}"
        )

    face_offsets = geom.mesh.face_offsets
    for i in range(geom.mesh.face_count):
        face = geom.mesh.face_vertex_indices[face_offsets[i] : face_offsets[i + 1]]
        result.append(f"{len(face)} {' '.join(map(str, face))}")

    return "\n".join(result)
