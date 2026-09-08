# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID

from stbkit.tools._internal.vectors import Vector2d, Vector3d

from .shape_data import (
    ShapePair,
    ShapePosition,
)


class ElementType(StrEnum):
    COLUMN = "column"
    POST = "post"
    GIRDER = "girder"
    BEAM = "beam"
    BRACE = "brace"
    SLAB = "slab"
    WALL = "wall"
    ISOLATING_DEVICE = "isolating_device"
    DAMPING_DEVICE = "damping_device"
    FRAME_DAMPING_DEVICE = "frame_damping_device"
    FOOTING = "footing"
    STRIP_FOOTING = "strip_footing"
    PILE = "pile"
    FOUNDATION_COLUMN = "foundation_column"
    PARAPET = "parapet"
    OPEN = "open"
    PENETRATION = "penetration"
    JOINT = "joint"
    PANEL_ZONE = "panel_zone"
    CONNECTION = "connection"
    OTHER = "other"


@dataclass(frozen=True, kw_only=True, slots=True)
class Node:
    position: Vector3d
    xpath: str | None = None
    guid: UUID | None = None


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class ElementPlane:
    element_type: ElementType | None = None
    name: str | None = None
    guid: UUID | None = None
    points: list[Vector3d] | None = None
    thickness: float | None = None
    opens: list[list[Vector2d]] = field(default_factory=list)
    path: str | None = None
    node_ids: list[int] = field(default_factory=list)
    node_points: list[Vector3d] | None = None


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class ElementLine:
    element_type: ElementType | None = None
    name: str | None = None
    guid: UUID | None = None
    lengths: list[float] = field(default_factory=list)
    point_start: Vector3d | None = None
    point_end: Vector3d | None = None
    angle: float = 0.0
    shapes: list[ShapePair] = field(default_factory=list)
    axis_position: ShapePosition = ShapePosition.CENTER_CENTER
    path: str | None = None
    node_ids: list[int] = field(default_factory=list)


@dataclass(eq=False, order=False, kw_only=True, slots=True)
class ElementLineSrc:
    element_type: ElementType | None = None
    name: str | None = None
    guid: UUID | None = None
    steel: ElementLine | None = None
    rc: ElementLine | None = None
    path: str | None = None
    node_ids: list[int] = field(default_factory=list)


class ElementData(list[ElementLine | ElementPlane | ElementLineSrc]):
    def __init__(
        self, elements: list[ElementLine | ElementPlane | ElementLineSrc] | None = None
    ):
        super().__init__(elements or [])
