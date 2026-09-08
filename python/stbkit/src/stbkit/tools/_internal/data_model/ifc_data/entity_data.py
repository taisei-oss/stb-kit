# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from uuid import UUID

from stbkit.core.stb_reporting import Reporter

from ..element_data import ElementData

if TYPE_CHECKING:
    import ifcopenshell.file


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class IfcBuildingStorey:
    name: str | None = None
    guid: UUID | None = None
    elements: ElementData = field(default_factory=ElementData)


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class IfcBuilding:
    name: str | None = None
    guid: UUID | None = None
    building_storeys: list[IfcBuildingStorey] = field(default_factory=list)


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class IfcSite:
    name: str | None = None
    guid: UUID | None = None
    building: IfcBuilding | None = None


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class IfcProject:
    name: str | None = None
    guid: UUID | None = None
    site: IfcSite | None = None


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class IfcModel:
    project: IfcProject | None = None

    def to_ifc(
        self,
        *,
        reporter: Reporter,
        round_digits: int | None = None,
        round_digits_mm: int | None = None,
    ) -> "ifcopenshell.file":
        from ...optional_dependencies.ifc_exporter.ifc_entity_exporter import (
            IfcEntityExporter,
        )

        return IfcEntityExporter.ifc_model_to_file(
            self,
            reporter=reporter,
            round_digits=round_digits,
            round_digits_mm=round_digits_mm,
        )
