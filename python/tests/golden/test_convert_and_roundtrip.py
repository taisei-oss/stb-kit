# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from contextlib import ExitStack
from importlib import import_module
from typing import Any, Final
from unittest.mock import patch

import pytest
import stbkit.core._internal.constants
import stbkit.core.stb_io._internal.serializer
from freezegun import freeze_time
from stbkit.testutils.fixture_repository import (
    ConversionNodeSpec,
    FixtureFormat,
    RoundTripSpec,
)
from stbkit.testutils.golden_runner import (
    RunContext,
    run_conversion_node_spec,
    run_roundtrip_dict_spec,
    run_roundtrip_spec,
    run_schema_check_line_count_spec,
    run_schema_check_spec,
)
from stbkit.testutils.patches import IncrementalUUID

PATCHES: Final[tuple[tuple[Any, str, str], ...]] = (
    (stbkit.core._internal.constants, "PACKAGE_VERSION", "0.0.0"),
    (stbkit.core.stb_io._internal.serializer, "PACKAGE_VERSION", "0.0.0"),
)


def _set_patch(monkeypatch: pytest.MonkeyPatch) -> None:
    for module, attr_name, value in PATCHES:
        monkeypatch.setattr(module, attr_name, value)


@freeze_time("2026-09-11 12:00:00")  # IFC出力の日時を固定
def test_conversions(
    spec: ConversionNodeSpec, run_context: RunContext, monkeypatch: pytest.MonkeyPatch
) -> None:
    if FixtureFormat.IFC4 in spec.route_formats:
        # ifcopenshell.guidを使うとguidの利用カウントが増えてしまうため、
        # UUIDモック適用前に読み込んでおいてカウンタが増えるのを防ぐ。
        import_module("ifcopenshell.guid")

    inc_uuid = IncrementalUUID()
    _set_patch(monkeypatch)
    with ExitStack() as stack:
        for target in IncrementalUUID.TARGETS:
            stack.enter_context(patch(target, inc_uuid))
        run_conversion_node_spec(spec, context=run_context)


def test_roundtrip_stb_v202(
    spec: RoundTripSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    _set_patch(monkeypatch)
    run_roundtrip_spec(spec)


def test_roundtrip_stb_v210(
    spec: RoundTripSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    _set_patch(monkeypatch)
    run_roundtrip_spec(spec)


def test_roundtrip_stb_v2_1_1(
    spec: RoundTripSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    _set_patch(monkeypatch)
    run_roundtrip_spec(spec)


def test_roundtrip_dict_stb_v210(
    spec: RoundTripSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    _set_patch(monkeypatch)
    run_roundtrip_dict_spec(spec)


def test_roundtrip_dict_stb_v2_1_1(
    spec: RoundTripSpec, monkeypatch: pytest.MonkeyPatch
) -> None:
    _set_patch(monkeypatch)
    run_roundtrip_dict_spec(spec)


@pytest.mark.requires_xsd
def test_schema_check(
    spec: RoundTripSpec, run_context: RunContext, monkeypatch: pytest.MonkeyPatch
) -> None:
    run_schema_check_spec(spec, context=run_context, use_xsd=True)


@pytest.mark.ai_generated
def test_schema_check_no_xsd(
    spec: RoundTripSpec, run_context: RunContext, monkeypatch: pytest.MonkeyPatch
) -> None:
    run_schema_check_spec(spec, context=run_context, use_xsd=False)


@pytest.mark.ai_generated
def test_schema_check_line_count(spec: RoundTripSpec) -> None:
    run_schema_check_line_count_spec(spec)
