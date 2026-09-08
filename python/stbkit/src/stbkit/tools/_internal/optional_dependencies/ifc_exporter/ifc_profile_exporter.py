# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import ifcopenshell.util.shape_builder
from ifcopenshell import entity_instance, file

from ...data_model.ifc_data.entity_names import EntityName
from ...data_model.shape_data import (
    Shape,
    ShapeArbitrary,
    ShapeBox,
    ShapeBuildBox,
    ShapeChannel,
    ShapeCircle,
    ShapeH,
    ShapeLipC,
    ShapePipe,
    ShapeRectangle,
    ShapeT,
)
from ...utils.float_rounding import round_float, round_vector2d

PROFILE_TYPE_AREA: str = "AREA"


class IfcProfileExporter:
    def __init__(
        self,
        model: file | None = None,
        body: entity_instance | None = None,
        *,
        round_digits_mm: int | None = None,
    ) -> None:
        self._model: file | None = model
        self._body: entity_instance | None = body
        self._round_digits_mm: int | None = round_digits_mm

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

    def get_profile(self, shape: Shape) -> entity_instance:
        """プロファイルを取得する

        IFCに山形鋼のプロファイルは存在するが、
        ST-Bridgeと基準軸方向が異なる。
        そのため、プロファイルを使うと回転角がST-Bridgeと変わってしまい、対応がわかりにくくなるため、
        山形鋼については任意形状(Arbitary)で設定する。
        """
        match shape:
            case ShapeArbitrary():
                return self.get_profile_arbitrary(shape)
            case ShapeBox():
                return self.get_profile_box(shape)
            case ShapeBuildBox():
                return self.get_profile_build_box(shape)
            case ShapeChannel():
                return self.get_profile_channel(shape)
            case ShapeCircle():
                return self.get_profile_circle(shape)
            case ShapeH():
                return self.get_profile_h(shape)
            case ShapeLipC():
                return self.get_profile_lip_c(shape)
            case ShapePipe():
                return self.get_profile_pipe(shape)
            case ShapeRectangle():
                return self.get_profile_rectangle(shape)
            case ShapeT():
                return self.get_profile_t(shape)
            case _:
                return self.get_profile_base(shape)

    def get_profile_base(self, shape: Shape) -> entity_instance:
        builder = ifcopenshell.util.shape_builder.ShapeBuilder(self.model)
        outer_curve = builder.polyline(
            [
                round_vector2d(point, round_digits=self._round_digits_mm)
                for point in shape.get_out_point2ds()
            ],
            closed=True,
        )
        in_point2ds = shape.get_in_point2ds()
        inner_curves: list[entity_instance] = []
        if in_point2ds:
            inner_curve = builder.polyline(
                [
                    round_vector2d(point, round_digits=self._round_digits_mm)
                    for point in in_point2ds
                ],
                closed=True,
            )
            inner_curves.append(inner_curve)
        profile = builder.profile(
            outer_curve, inner_curves=inner_curves, name="Arbitrary"
        )
        return profile

    def get_profile_arbitrary(self, shape: ShapeArbitrary) -> entity_instance:
        builder = ifcopenshell.util.shape_builder.ShapeBuilder(self.model)
        outer_curve = builder.polyline(
            [
                round_vector2d(point, round_digits=self._round_digits_mm)
                for point in shape.get_out_point2ds()
            ],
            closed=True,
        )
        inner_curves: list[entity_instance] = []
        in_point_2ds = shape.in_points
        if in_point_2ds:
            for in_points in in_point_2ds:
                inner_curve = builder.polyline(
                    [
                        round_vector2d(point, round_digits=self._round_digits_mm)
                        for point in in_points
                    ],
                    closed=True,
                )
                inner_curves.append(inner_curve)
        profile = builder.profile(
            outer_curve, inner_curves=inner_curves, name="Arbitrary"
        )
        return profile

    def get_profile_box(self, shape: ShapeBox) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_RECTANGLE_HOLLOW_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            XDim=round_float(shape.b, round_digits=self._round_digits_mm),
            YDim=round_float(shape.a, round_digits=self._round_digits_mm),
            WallThickness=round_float(shape.t, round_digits=self._round_digits_mm),
            InnerFilletRadius=round_float(
                max(0.0, shape.r - shape.t),
                round_digits=self._round_digits_mm,
            ),
            OuterFilletRadius=round_float(
                shape.r,
                round_digits=self._round_digits_mm,
            ),
        )
        return profile

    def get_profile_build_box(self, shape: ShapeBuildBox) -> entity_instance:
        if shape.t1 == shape.t2:
            profile: entity_instance = self.model.create_entity(
                EntityName.IFC_RECTANGLE_HOLLOW_PROFILE_DEF.value,
                ProfileName=shape.name,
                ProfileType=PROFILE_TYPE_AREA,
                XDim=round_float(shape.b, round_digits=self._round_digits_mm),
                YDim=round_float(shape.a, round_digits=self._round_digits_mm),
                WallThickness=round_float(
                    shape.t1,
                    round_digits=self._round_digits_mm,
                ),
                InnerFilletRadius=0.0,
                OuterFilletRadius=0.0,
            )
            return profile
        else:
            return self.get_profile_base(shape)

    def get_profile_channel(self, shape: ShapeChannel) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_U_SHAPE_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            Depth=round_float(shape.a, round_digits=self._round_digits_mm),
            FlangeWidth=round_float(shape.b, round_digits=self._round_digits_mm),
            WebThickness=round_float(shape.t1, round_digits=self._round_digits_mm),
            FlangeThickness=round_float(
                shape.t2,
                round_digits=self._round_digits_mm,
            ),
            FilletRadius=round_float(shape.r1, round_digits=self._round_digits_mm),
            EdgeRadius=round_float(shape.r2, round_digits=self._round_digits_mm),
            FlangeSlope=0,
        )
        return profile

    def get_profile_circle(self, shape: ShapeCircle) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_CIRCLE_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            Radius=round_float(shape.d / 2.0, round_digits=self._round_digits_mm),
        )
        return profile

    def get_profile_h(self, shape: ShapeH) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_I_SHAPE_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            OverallWidth=round_float(shape.b, round_digits=self._round_digits_mm),
            OverallDepth=round_float(shape.a, round_digits=self._round_digits_mm),
            WebThickness=round_float(shape.t1, round_digits=self._round_digits_mm),
            FlangeThickness=round_float(
                shape.t2,
                round_digits=self._round_digits_mm,
            ),
            FilletRadius=round_float(shape.r, round_digits=self._round_digits_mm),
        )
        return profile

    def get_profile_pipe(self, shape: ShapePipe) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_CIRCLE_HOLLOW_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            Radius=round_float(shape.d / 2.0, round_digits=self._round_digits_mm),
            WallThickness=round_float(shape.t, round_digits=self._round_digits_mm),
        )
        return profile

    def get_profile_rectangle(self, shape: ShapeRectangle) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_RECTANGLE_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            XDim=round_float(shape.width_x, round_digits=self._round_digits_mm),
            YDim=round_float(shape.width_y, round_digits=self._round_digits_mm),
        )
        return profile

    def get_profile_t(self, shape: ShapeT) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_T_SHAPE_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            Depth=round_float(shape.b, round_digits=self._round_digits_mm),
            FlangeWidth=round_float(shape.a, round_digits=self._round_digits_mm),
            WebThickness=round_float(shape.t1, round_digits=self._round_digits_mm),
            FlangeThickness=round_float(
                shape.t2,
                round_digits=self._round_digits_mm,
            ),
            FilletRadius=round_float(shape.r, round_digits=self._round_digits_mm),
        )
        return profile

    def get_profile_lip_c(self, shape: ShapeLipC) -> entity_instance:
        profile: entity_instance = self.model.create_entity(
            EntityName.IFC_C_SHAPE_PROFILE_DEF.value,
            ProfileName=shape.name,
            ProfileType=PROFILE_TYPE_AREA,
            Depth=round_float(shape.h, round_digits=self._round_digits_mm),
            Width=round_float(shape.a, round_digits=self._round_digits_mm),
            WallThickness=round_float(shape.t, round_digits=self._round_digits_mm),
            Girth=round_float(shape.c, round_digits=self._round_digits_mm),
        )
        return profile
