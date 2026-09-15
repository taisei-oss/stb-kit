# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import asdict, dataclass
from json import dumps
from typing import TYPE_CHECKING

from stbkit.core.data_model.common import StBridgeElement, StBridgeRoot, _FieldKind
from stbkit.core.stb_exceptions import NoneAccessError, UnsupportedStbVersionError
from stbkit.core.stb_reporting import (
    CollectingReporter,
    ReportingResult,
    Severity,
)
from stbkit.core.validation import validate_schema

if TYPE_CHECKING:
    from stbkit.core.data_model import (
        stb_v2_0_0,
        stb_v2_0_1,
        stb_v2_0_2,
        stb_v2_1_0,
        stb_v2_1_1,
    )

    _SupportedStBridges = (
        stb_v2_0_0.StBridge,
        stb_v2_0_1.StBridge,
        stb_v2_0_2.StBridge,
        stb_v2_1_0.StBridge,
        stb_v2_1_1.StBridge,
    )
else:
    _SupportedStBridges = object


@dataclass(frozen=True, slots=True)
class NodeSummary:
    total_count: int
    min_x: float | None
    min_y: float | None
    min_z: float | None
    max_x: float | None
    max_y: float | None
    max_z: float | None

    def to_text(self, *, verbose: int = 0) -> list[str]:
        lines: list[str] = [
            "Node Summary:",
            f" total count: {self.total_count}",
        ]
        if verbose > 0:
            lines.extend(
                [
                    f"  min(x,y,z): ({self.min_x}, {self.min_y}, {self.min_z})",
                    f"  max(x,y,z): ({self.max_x}, {self.max_y}, {self.max_z})",
                ]
            )
        return lines


@dataclass(frozen=True, slots=True)
class MemberSummary:
    total_count: int
    member_counts: dict[str, int]

    def to_text(self, *, verbose: int = 0) -> list[str]:
        lines: list[str] = [
            "Member Summary:",
            f" total count: {self.total_count}",
        ]
        for name, count in self.member_counts.items():
            lines.append(f"  {name}: {count}")
        return lines


@dataclass(frozen=True, slots=True)
class ValidationSummary:
    is_valid: bool
    error_count: int
    warning_count: int
    messages: ReportingResult

    def to_text(self, *, verbose: int = 0) -> list[str]:
        lines: list[str] = [
            "Validation Summary:",
            f" result: {'OK' if self.is_valid else 'NG'}",
        ]
        if not self.is_valid:
            if self.error_count > 0:
                lines.append(f" error count: {self.error_count}")
            if self.warning_count > 0:
                lines.append(f" warning count: {self.warning_count}")
        if verbose > 0:
            lines.append(self.messages.to_text())
        return lines


@dataclass(frozen=True, slots=True)
class StbSummary:
    version: str | None
    project_name: str | None
    node_summary: NodeSummary
    member_summary: MemberSummary
    validation_summary: ValidationSummary | None

    def to_json(self, *, indent: int | str | None = None) -> str:
        return dumps(asdict(self), ensure_ascii=False, indent=indent)

    def to_text(self, *, verbose: int = 0) -> str:
        lines: list[str] = [
            f"version: {self.version or ''}",
            f"project_name: {self.project_name or ''}",
        ]
        lines.extend(self.node_summary.to_text(verbose=verbose))
        lines.extend(self.member_summary.to_text(verbose=verbose))
        if self.validation_summary is not None:
            lines.extend(self.validation_summary.to_text(verbose=verbose))
        return "\n".join(lines)


def get_summary(
    stb: StBridgeRoot,
    *,
    reporter: CollectingReporter,
    validate: bool = True,
) -> StbSummary:
    if not isinstance(stb, _SupportedStBridges):
        raise UnsupportedStbVersionError(stb.version)
    version: str | None = stb.version_or_none
    if stb_common := stb.stb_common_or_none:
        project_name: str | None = stb_common.project_name_or_none
    else:
        project_name = None
    try:
        nodes = stb.stb_model.stb_nodes.stb_node
        node_count = len(nodes)
        if node_count > 0:
            min_x = min(node.x for node in nodes)
            min_y = min(node.y for node in nodes)
            min_z = min(node.z for node in nodes)
            max_x = max(node.x for node in nodes)
            max_y = max(node.y for node in nodes)
            max_z = max(node.z for node in nodes)
    except NoneAccessError:
        node_count = 0
    node_summary = NodeSummary(
        total_count=node_count,
        min_x=min_x if node_count > 0 else None,
        min_y=min_y if node_count > 0 else None,
        min_z=min_z if node_count > 0 else None,
        max_x=max_x if node_count > 0 else None,
        max_y=max_y if node_count > 0 else None,
        max_z=max_z if node_count > 0 else None,
    )
    member_counts: dict[str, int] = {}
    try:
        members = stb.stb_model.stb_members
        for field_name, field_info in members._fields.items():
            if (
                field_info.kind is _FieldKind.ELEMENT
                and field_info.max_occurs == 1
                and hasattr(members, field_name)
            ):
                list_elem = getattr(members, field_name)
                if not isinstance(list_elem, StBridgeElement):
                    continue
                for field_name2, field_info2 in list_elem._fields.items():
                    if (
                        field_info2.kind is not _FieldKind.ELEMENT
                        or field_info2.max_occurs == 1
                    ):
                        continue
                    member_counts[list_elem._xml_name(field_name2)] = len(
                        getattr(list_elem, field_name2)
                    )
    except NoneAccessError:
        pass
    member_total_count: int = sum(member_counts.values())
    member_summary: MemberSummary = MemberSummary(
        total_count=member_total_count,
        member_counts=member_counts,
    )

    if validate:
        validate_schema(stb, reporter=reporter, require_xsd=False)
        is_valid: bool = reporter.is_valid()
        report: ReportingResult = reporter.report
        error_count: int = len(
            [item for item in report if item.severity == Severity.ERROR]
        )
        warning_count: int = len(
            [item for item in report if item.severity == Severity.WARNING]
        )
        validation_summary: ValidationSummary | None = ValidationSummary(
            is_valid=is_valid,
            error_count=error_count,
            warning_count=warning_count,
            messages=report,
        )
    else:
        validation_summary = None

    return StbSummary(
        version=version,
        project_name=project_name,
        node_summary=node_summary,
        member_summary=member_summary,
        validation_summary=validation_summary,
    )
