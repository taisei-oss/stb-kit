# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from typing import Protocol

from stbkit.core._internal.utils.version_utils import Version
from stbkit.core.data_model.common import StBridgeElement, StBridgeRoot
from stbkit.core.repository import get_repository
from stbkit.core.repository.repo_common import RepositoryBase
from stbkit.core.stb_reporting import Reporter


@dataclass
class Defaults:
    steel_strength: str
    default_length: float
    default_float: float = 0.0
    default_string: str = "repair"


@dataclass
class RepairContext:
    stb: StBridgeRoot
    defaults: Defaults
    reporter: Reporter
    unknown_section_id: int | None = None
    _repo: RepositoryBase | None = None
    _version: Version | None = None

    @property
    def repo(self) -> RepositoryBase:
        if self._repo is None:
            self._repo = get_repository(self.stb)
        return self._repo

    @property
    def version(self) -> Version:
        if self._version is None:
            self._version = Version(self.stb.version)
        return self._version


class ElementRepairHook(Protocol):
    def __call__(
        self, element: StBridgeElement, /, *, context: RepairContext
    ) -> None: ...
