# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from typing import Any

from stbkit.core.stb_reporting import Code, CollectingReporter, Phase, ReportingResult


@dataclass(frozen=True, kw_only=True)
class DiffItem:
    message: str
    path: str
    left: Any = None
    right: Any = None
    attribute_name: str | None = None
    match_reason: str | None = None

    @property
    def display_message(self) -> str:
        if self.match_reason is None:
            return self.message
        return f"{self.message}（{self.match_reason}）"


@dataclass(frozen=True, kw_only=True)
class CompareResult:
    equal: bool
    diffs: list[DiffItem]

    def to_reporting_result(
        self, *, code: Code = Code.DIFF, phase: Phase = Phase.DIFF
    ) -> ReportingResult:
        reporter = CollectingReporter(default_code=code, default_phase=phase)
        for diff in self.diffs:
            reporter.error(
                message=diff.display_message,
                xpath=diff.path,
                value=diff.left,
                ref_value=diff.right,
            )
        return reporter.report


@dataclass(kw_only=True)
class CompareOption:
    pass
