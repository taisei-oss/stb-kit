# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import ifcopenshell.api.geometry
from ifcopenshell import entity_instance, file
from ifcopenshell.util.shape_builder import SequenceOfVectors
from stbkit.core.stb_reporting import Reporter

from ....converters._internal import coord_converter
from ....converters._internal.element_data_to_building_geometry import (
    create_local_line_meshes,
)
from ...constants import UNKNOWN_ELEMENT_SIZE_MM
from ...data_model.shape_data import (
    ShapeArbitrary,
    ShapePair,
    ShapePosition,
    ShapeRectangle,
)
from ...utils.float_rounding import round_float, round_vector2d, round_vector3d
from ...utils.unit_utils import mm_to_m
from ...vectors import Vector2d, Vector3d
from .ifc_profile_exporter import IfcProfileExporter


class IfcRepresentationExporter:
    def __init__(
        self,
        model: file | None = None,
        body: entity_instance | None = None,
        *,
        reporter: Reporter,
        round_digits_mm: int | None = None,
    ) -> None:
        self._model: file | None = model
        self._body: entity_instance | None = body
        self._reporter: Reporter = reporter
        self._round_digits_mm: int | None = round_digits_mm
        self.profile_exporter: IfcProfileExporter = IfcProfileExporter(
            model,
            body,
            round_digits_mm=round_digits_mm,
        )

    @property
    def model(self) -> file:
        if self._model is None:
            raise AssertionError("modelが初期化されていません")
        return self._model

    @property
    def body(self) -> entity_instance:
        if self._body is None:
            raise AssertionError("bodyが初期化されていません")
        return self._body

    @body.setter
    def body(self, value: entity_instance) -> None:
        self._body = value
        self.profile_exporter.body = value

    @classmethod
    def is_extrusion(cls, shapes: list[ShapePair]) -> bool:
        return (
            len(shapes) == 1
            and (shapes[0].end is None or shapes[0].end == shapes[0].start)
            and shapes[0].start.rotate_degree is None
        )

    def get_line_representation(
        self,
        shapes: list[ShapePair],
        axis_position: ShapePosition,
        lengths: list[float],
    ) -> entity_instance:
        round_digits_m = (
            None if self._round_digits_mm is None else self._round_digits_mm + 3
        )
        if not shapes:
            raise AssertionError("形状が設定されていません")
        if len(shapes) != len(lengths):
            raise AssertionError("形状と長さの数が異なります")
        if self.is_extrusion(shapes):
            profile: entity_instance = self.profile_exporter.get_profile(
                shapes[0].start
            )
            representation: entity_instance = (
                ifcopenshell.api.geometry.add_profile_representation(
                    self.model,
                    context=self.body,
                    profile=profile,
                    depth=round_float(
                        mm_to_m(lengths[0]),
                        round_digits=round_digits_m,
                    ),
                )
            )
        else:
            points_list: list[SequenceOfVectors] = []
            faces_list: list[list[list[int]]] = []
            for mesh in create_local_line_meshes(
                shapes,
                axis_position,
                lengths,
            ):
                points_list.append(
                    [
                        round_vector3d(
                            point.mm_to_m(),
                            round_digits=round_digits_m,
                        ).to_tuple()
                        for point in mesh.vertices
                    ]
                )
                faces_list.append([list(face) for face in mesh.faces])
            representation = ifcopenshell.api.geometry.add_mesh_representation(
                self.model, context=self.body, vertices=points_list, faces=faces_list
            )
        return representation

    def get_line_unknown_representation(self, lengths: list[float]) -> entity_instance:
        shape: ShapeRectangle = ShapeRectangle(name="unknown", width_x=10, width_y=10)
        return self.get_line_representation(
            shapes=[ShapePair(shape)],
            axis_position=ShapePosition.CENTER_CENTER,
            lengths=lengths,
        )

    def get_plate_representation(
        self,
        thickness: float | None,
        opens: list[list[Vector2d]] | None,
        points: list[Vector3d],
    ) -> entity_instance:
        if len(points) < 3:
            raise AssertionError("外形の頂点数が足りません")
        if thickness is None:
            raise AssertionError("厚さが設定されていません")
        round_digits_m = (
            None if self._round_digits_mm is None else self._round_digits_mm + 3
        )
        shape: ShapeArbitrary = ShapeArbitrary()
        shape.out_points.extend(
            Vector2d(
                rounded_point.x,
                rounded_point.y,
            )
            for item in coord_converter.to_plate_element_coord(points)
            for rounded_point in [
                round_vector3d(item, round_digits=self._round_digits_mm)
            ]
        )
        shape.in_points = (
            [
                [round_vector2d(p, round_digits=self._round_digits_mm) for p in open]
                for open in opens
            ]
            if opens is not None
            else []
        )
        profile = self.profile_exporter.get_profile(shape)
        representation = ifcopenshell.api.geometry.add_profile_representation(
            self.model,
            context=self.body,
            profile=profile,
            depth=round_float(
                mm_to_m(thickness),
                round_digits=round_digits_m,
            ),
        )
        return representation

    def get_unknown_plate_representation(
        self, points: list[Vector3d]
    ) -> entity_instance:
        return self.get_plate_representation(
            thickness=UNKNOWN_ELEMENT_SIZE_MM,
            opens=None,
            points=points,
        )
