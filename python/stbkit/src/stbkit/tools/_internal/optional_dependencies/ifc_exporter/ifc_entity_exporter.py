# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Protocol
from uuid import UUID

import ifcopenshell.api.aggregate
import ifcopenshell.api.context
import ifcopenshell.api.geometry
import ifcopenshell.api.project
import ifcopenshell.api.root
import ifcopenshell.api.unit
import ifcopenshell.file
import numpy as np
from ifcopenshell import entity_instance
from numpy.typing import NDArray
from stbkit.core._internal.transform.guid_tools import generate_uuid
from stbkit.core.stb_exceptions import ZeroLengthMemberError
from stbkit.core.stb_reporting import Code, Phase, Reporter, get_reporter

from ....converters._internal import coord_converter
from ...constants import UNKNOWN_ELEMENT_SIZE_MM
from ...data_model.element_data import (
    ElementLine,
    ElementLineSrc,
    ElementPlane,
    ElementType,
)
from ...data_model.ifc_data.entity_data import (
    IfcBuilding,
    IfcBuildingStorey,
    IfcModel,
    IfcProject,
    IfcSite,
)
from ...data_model.ifc_data.entity_names import EntityName
from ...matrix import RotationMatrix
from ...utils.float_rounding import round_float
from ...utils.guid_utils import to_ifc_guid
from ...vectors import Vector2d, Vector3d
from .ifc_representation_exporter import IfcRepresentationExporter


def _rotation_matrix_to_ndarray(
    matrix: RotationMatrix,
    *,
    round_digits: int | None,
    round_digits_mm: int | None,
) -> NDArray[np.float64]:
    result: NDArray[np.float64] = np.array(matrix.to_matrix_tuple(), dtype=np.float64)
    if result.shape != (4, 4):
        raise AssertionError(f"4x4行列ではありません: {result.shape}")
    if round_digits is None and round_digits_mm is None:
        return result
    rounded: NDArray[np.float64] = result.copy()
    if round_digits is not None:
        for i in range(3):
            for j in range(3):
                rounded[i, j] = round_float(
                    rounded[i, j],
                    round_digits=round_digits,
                )
    if round_digits_mm is not None:
        round_digits_m: int = round_digits_mm + 3
        rounded[0, 3] = round_float(rounded[0, 3], round_digits=round_digits_m)
        rounded[1, 3] = round_float(rounded[1, 3], round_digits=round_digits_m)
        rounded[2, 3] = round_float(rounded[2, 3], round_digits=round_digits_m)
    return rounded


class _HasGuid(Protocol):
    guid: UUID | None


def _unit_sort_key(unit: entity_instance) -> tuple[str, str]:
    """単位を固定順序へ並べるためのkey"""
    return (unit.is_a(), str(getattr(unit, "UnitType", "")))


def _set_guid(ifc_entity: entity_instance, obj: _HasGuid) -> None:
    if obj.guid is None:
        obj.guid = generate_uuid()
    if obj.guid:
        ifc_entity.GlobalId = to_ifc_guid(obj.guid)


class IfcEntityExporter:
    def __init__(
        self,
        *,
        model: ifcopenshell.file | None = None,
        reporter: Reporter | None = None,
        round_digits: int | None = None,
        round_digits_mm: int | None = None,
    ) -> None:
        self._model: ifcopenshell.file | None = model
        self._body: entity_instance | None = None
        self._round_digits: int | None = round_digits
        self._round_digits_mm: int | None = round_digits_mm
        self.reporter: Reporter = reporter or get_reporter()
        self.representation_exporter: IfcRepresentationExporter = (
            IfcRepresentationExporter(
                model,
                reporter=self.reporter,
                round_digits_mm=round_digits_mm,
            )
        )

    @property
    def model(self) -> ifcopenshell.file:
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
        self.representation_exporter.body = value

    def create_entity_plane_element(
        self,
        plane_element: ElementPlane,
    ) -> entity_instance:
        if not plane_element.points:
            raise AssertionError(f"{plane_element.name}にpointsが設定されていません")
        if len(plane_element.points) < 3:
            raise AssertionError(f"{plane_element.name}のpointsの数が3未満です")
        if plane_element.element_type is None:
            raise AssertionError(
                f"{plane_element.name}にelement_typeが設定されていません"
            )
        plate_element: entity_instance = ifcopenshell.api.root.create_entity(
            self.model,
            ifc_class=IfcEntityExporter.to_entity_name(
                plane_element.element_type
            ).value,
            name=plane_element.name,
        )
        _set_guid(plate_element, plane_element)
        thickness: float | None = plane_element.thickness
        if thickness is None:
            self.reporter.warning(
                f"要素[{plane_element.name}]にthicknessが設定されていないため、厚さ{UNKNOWN_ELEMENT_SIZE_MM}mmで出力します。",
                code=Code.UNKNOWN_SHAPE,
                phase=Phase.CONVERT_IFC,
            )
            thickness = UNKNOWN_ELEMENT_SIZE_MM

        representation = self.representation_exporter.get_plate_representation(
            thickness=thickness,
            opens=plane_element.opens,
            points=plane_element.points,
        )

        ifcopenshell.api.geometry.assign_representation(
            self.model, product=plate_element, representation=representation
        )
        matrix = _rotation_matrix_to_ndarray(
            coord_converter.rotation_matrix_plate(
                [p.mm_to_m() for p in plane_element.points]
            ),
            round_digits=self._round_digits,
            round_digits_mm=self._round_digits_mm,
        )
        ifcopenshell.api.geometry.edit_object_placement(
            self.model, product=plate_element, matrix=matrix
        )
        return plate_element

    def create_entity_element_line(
        self,
        element_line: ElementLine,
    ) -> entity_instance | None:
        if not element_line.lengths:
            self.reporter.warning(
                f"要素[{element_line.name}]にlengthsが設定されていないため、IFCエクスポートをスキップしました。",
                code=Code.ZERO_LENGTH_MEMBER,
                phase=Phase.CONVERT_IFC,
            )
            return None
        if not element_line.point_start:
            raise AssertionError(
                f"{element_line.name}にpoint_startが設定されていません"
            )
        if not element_line.point_end:
            raise AssertionError(f"{element_line.name}にpoint_endが設定されていません")
        if element_line.element_type is None:
            raise AssertionError(
                f"{element_line.name}にelement_typeが設定されていません"
            )
        line_element: entity_instance = ifcopenshell.api.root.create_entity(
            self.model,
            ifc_class=IfcEntityExporter.to_entity_name(element_line.element_type).value,
            name=element_line.name,
        )
        _set_guid(line_element, element_line)
        point_start: Vector3d = element_line.point_start
        point_end: Vector3d = element_line.point_end
        if element_line.shapes:
            representation = self.representation_exporter.get_line_representation(
                shapes=element_line.shapes,
                axis_position=element_line.axis_position,
                lengths=element_line.lengths,
            )

            if self.representation_exporter.is_extrusion(element_line.shapes):
                offset: Vector2d = Vector2d.zero() - element_line.shapes[
                    0
                ].start.get_position_point(element_line.axis_position)
                if element_line.shapes[0].start.offset:
                    offset += element_line.shapes[0].start.offset
                _, vy, vz = coord_converter.axis_vector_by_element_type(
                    element_line.point_start,
                    element_line.point_end,
                    element_line.angle,
                    element_line.element_type,
                )
                point_start += offset.x * vy + offset.y * vz
                point_end += offset.x * vy + offset.y * vz

        else:
            representation = (
                self.representation_exporter.get_line_unknown_representation(
                    element_line.lengths
                )
            )
        ifcopenshell.api.geometry.assign_representation(
            self.model, product=line_element, representation=representation
        )
        matrix = _rotation_matrix_to_ndarray(
            coord_converter.rotation_matrix_by_element_type(
                point_start.mm_to_m(),
                point_end.mm_to_m(),
                element_line.angle,
                element_line.element_type,
            ),
            round_digits=self._round_digits,
            round_digits_mm=self._round_digits_mm,
        )
        ifcopenshell.api.geometry.edit_object_placement(
            self.model, product=line_element, matrix=matrix
        )
        return line_element

    def create_entity_element_line_src(
        self,
        line_element_src: ElementLineSrc,
    ) -> entity_instance:
        element_assembly: entity_instance = ifcopenshell.api.root.create_entity(
            self.model,
            ifc_class=EntityName.IFC_ELEMENT_ASSEMBLY.value,
            name=line_element_src.name,
        )
        _set_guid(element_assembly, line_element_src)

        items: list[entity_instance] = []
        if line_element_src.steel:
            item_steel: entity_instance | None = self.create_entity_element_line(
                line_element_src.steel
            )
            if item_steel is not None:
                items.append(item_steel)
        if line_element_src.rc:
            item_rc: entity_instance | None = self.create_entity_element_line(
                line_element_src.rc
            )
            if item_rc is not None:
                items.append(item_rc)
        # ifcopenshellのassign_objectは呼ぶたびに集合演算を行うため
        # 処理時間がかかり順序も安定しなくなる。
        # そのため、参照関係はここで1度だけ作る。
        if items:
            self.model.create_entity(
                EntityName.IFC_REL_AGGREGATES.value,
                GlobalId=to_ifc_guid(generate_uuid()),
                RelatingObject=element_assembly,
                RelatedObjects=items,
            )
        return element_assembly

    def create_entity_element(
        self,
        element: ElementLine | ElementPlane | ElementLineSrc,
    ) -> entity_instance | None:
        try:
            match element:
                case ElementLine() as line_element:
                    return self.create_entity_element_line(line_element)
                case ElementPlane() as plane_element:
                    return self.create_entity_plane_element(plane_element)
                case ElementLineSrc() as line_element_src:
                    return self.create_entity_element_line_src(line_element_src)
                case _:
                    raise AssertionError(f"不明な要素タイプです: {type(element)}")
        except ZeroLengthMemberError:
            self.reporter.warning(
                f"要素'{element.name}'の始端と終端が同じ位置のため、IFCエクスポートをスキップしました。",
                code=Code.ZERO_LENGTH_MEMBER,
                phase=Phase.CONVERT_IFC,
            )
            return None

    def create_entity_building_storey(
        self,
        ifc_building_storey: IfcBuildingStorey,
    ) -> entity_instance:
        building_storey: entity_instance = ifcopenshell.api.root.create_entity(
            self.model,
            ifc_class=EntityName.IFC_BUILDING_STOREY.value,
            name=ifc_building_storey.name,
        )
        _set_guid(building_storey, ifc_building_storey)
        n_element: int = len(ifc_building_storey.elements)
        self.reporter.info(
            message=f"---要素のIFCエンティティ変換処理({n_element}件)---",
            code=Code.PROGRESS_INFO,
            phase=Phase.CONVERT_IFC,
        )
        elements: list[entity_instance] = []
        batch_size: int = 1000
        for i, element in enumerate(ifc_building_storey.elements, 1):
            e = self.create_entity_element(element)
            if e is not None:
                elements.append(e)
            if i % batch_size == 0 or i == n_element:
                self.reporter.info(
                    message=f"---要素のIFCエンティティ変換処理（{i}/{n_element}件）---",
                    code=Code.PROGRESS_INFO,
                    phase=Phase.CONVERT_IFC,
                )
        n_element = len(elements)
        self.reporter.info(
            message=f"---要素のIFCエンティティ配置処理({n_element}件)---",
            code=Code.PROGRESS_INFO,
            phase=Phase.CONVERT_IFC,
        )
        # ifcopenshellのassign_containerは、呼ぶたびに集合演算を行うため
        # 処理時間がかかり順序も安定しなくなる。
        # そのため、参照関係はここで1度だけ作る。
        if elements:
            self.model.create_entity(
                EntityName.IFC_REL_CONTAINED_IN_SPATIAL_STRUCTURE.value,
                GlobalId=to_ifc_guid(generate_uuid()),
                RelatedElements=elements,
                RelatingStructure=building_storey,
            )
        return building_storey

    def create_entity_ifc_building(self, ifc_building: IfcBuilding) -> entity_instance:
        building: entity_instance = ifcopenshell.api.root.create_entity(
            self.model,
            ifc_class=EntityName.IFC_BUILDING.value,
            name=ifc_building.name,
        )
        _set_guid(building, ifc_building)
        building_storeys: list[entity_instance] = [
            self.create_entity_building_storey(building_storey)
            for building_storey in ifc_building.building_storeys
        ]
        rel: entity_instance | None = ifcopenshell.api.aggregate.assign_object(
            self.model, relating_object=building, products=building_storeys
        )
        if rel is not None:
            rel.GlobalId = to_ifc_guid(generate_uuid())
        return building

    def create_entity_ifc_site(self, ifc_site: IfcSite) -> entity_instance:
        site: entity_instance = ifcopenshell.api.root.create_entity(
            self.model, ifc_class=EntityName.IFC_SITE.value, name=ifc_site.name
        )
        if not ifc_site.building:
            raise AssertionError("buildingが設定されていません")
        building: entity_instance = self.create_entity_ifc_building(ifc_site.building)
        _set_guid(site, ifc_site)
        rel: entity_instance | None = ifcopenshell.api.aggregate.assign_object(
            self.model, relating_object=site, products=[building]
        )
        if rel is not None:
            rel.GlobalId = to_ifc_guid(generate_uuid())
        return site

    def create_entity_project(self, ifc_project: IfcProject) -> entity_instance:
        project: entity_instance = ifcopenshell.api.root.create_entity(
            self.model, ifc_class=EntityName.IFC_PROJECT.value, name=ifc_project.name
        )
        _set_guid(project, ifc_project)
        ifcopenshell.api.unit.assign_unit(self.model)
        # assign_unitはsetを経由するため並びが実行ごとに変わるため、順序を固定する
        units = project.UnitsInContext
        if units is not None:
            units.Units = sorted(units.Units, key=_unit_sort_key)
        context: entity_instance = ifcopenshell.api.context.add_context(
            self.model, context_type="Model"
        )
        self.body = ifcopenshell.api.context.add_context(
            self.model,
            context_type="Model",
            context_identifier="Body",
            target_view="MODEL_VIEW",
            parent=context,
        )
        if not ifc_project.site:
            raise AssertionError("siteが設定されていません")
        site: entity_instance = self.create_entity_ifc_site(ifc_project.site)
        rel: entity_instance | None = ifcopenshell.api.aggregate.assign_object(
            self.model, relating_object=project, products=[site]
        )
        if rel is not None:
            rel.GlobalId = to_ifc_guid(generate_uuid())
        return project

    @staticmethod
    def ifc_model_to_file(
        ifc_model: IfcModel,
        *,
        reporter: Reporter,
        round_digits: int | None = None,
        round_digits_mm: int | None = None,
    ) -> ifcopenshell.file:
        reporter.info(
            "---IFCジオメトリデータ->IFC Entityデータ変換処理開始---",
            code=Code.PROGRESS_INFO,
            phase=Phase.CONVERT_IFC,
        )
        model: ifcopenshell.file = ifcopenshell.api.project.create_file()
        exporter: IfcEntityExporter = IfcEntityExporter(
            model=model,
            reporter=reporter,
            round_digits=round_digits,
            round_digits_mm=round_digits_mm,
        )

        if not ifc_model.project:
            raise AssertionError("projectが設定されていません")
        exporter.create_entity_project(ifc_model.project)
        reporter.info(
            "---IFCジオメトリデータ->IFC Entityデータ変換処理終了---",
            code=Code.PROGRESS_INFO,
            phase=Phase.CONVERT_IFC,
        )
        return model

    @staticmethod
    def to_entity_name(element_type: ElementType) -> EntityName:
        match element_type:
            case (
                ElementType.GIRDER
                | ElementType.BEAM
                | ElementType.STRIP_FOOTING
                | ElementType.PARAPET
            ):
                return EntityName.IFC_BEAM
            case ElementType.COLUMN | ElementType.POST | ElementType.FOUNDATION_COLUMN:
                return EntityName.IFC_COLUMN
            case ElementType.BRACE:
                return EntityName.IFC_MEMBER
            case ElementType.WALL:
                return EntityName.IFC_WALL
            case ElementType.SLAB:
                return EntityName.IFC_SLAB
            case ElementType.FOOTING:
                return EntityName.IFC_FOOTING
            case ElementType.PILE:
                return EntityName.IFC_PILE
            case _:
                raise AssertionError(f"不明なElementTypeです: {element_type}")
