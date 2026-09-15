# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import importlib.util
from types import ModuleType
from typing import Any

import stbkit.api
import stbkit.api.experimental
import stbkit.api.experimental.repository


def test_api_exports() -> None:
    modules: list[ModuleType] = [
        stbkit.api,
        stbkit.api.experimental,
        stbkit.api.experimental.repository,
    ]

    for module in modules:
        missing: list[Any] = [
            name
            for name in module.__all__
            if not hasattr(module, name)
            and importlib.util.find_spec(f"{module.__name__}.{name}") is None
        ]
        assert missing == []
