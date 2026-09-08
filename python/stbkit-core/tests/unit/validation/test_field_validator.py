# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.data_model.stb_v2_1_0 import StbNode, StbNodeIdOrder
from stbkit.core.stb_reporting import CollectingReporter
from stbkit.core.validation._internal.schema_validator import FieldValidator


def test_field_required_invalid() -> None:
    node: StbNode = StbNode()

    reporter: CollectingReporter = CollectingReporter()
    validator: FieldValidator = FieldValidator()
    assert not validator.validate_element(node, reporter)
    assert len(reporter.report) == 5
    assert not reporter.is_valid()


def test_field_required_valid() -> None:
    node: StbNode = StbNode(id=1, x=0.0, y=0.0, z=0.0, kind="ON_GRID")

    reporter: CollectingReporter = CollectingReporter()
    validator: FieldValidator = FieldValidator()
    assert validator.validate_element(node, reporter)
    assert len(reporter.report) == 0
    assert reporter.is_valid()


def test_field_choice_invalid() -> None:
    node: StbNode = StbNode(id=1, x=0.0, y=0.0, z=0.0, kind="INVALID_KIND")

    reporter: CollectingReporter = CollectingReporter()
    validator: FieldValidator = FieldValidator()
    assert not validator.validate_element(node, reporter)
    assert len(reporter.report) == 1
    assert not reporter.is_valid()


def test_content_invalid() -> None:
    order: StbNodeIdOrder = StbNodeIdOrder()

    reporter: CollectingReporter = CollectingReporter()
    validator: FieldValidator = FieldValidator()
    assert not validator.validate_element(order, reporter)
    assert len(reporter.report) == 1


def test_content_valid() -> None:
    order: StbNodeIdOrder = StbNodeIdOrder()
    order.content = [1, 2, 3]

    reporter: CollectingReporter = CollectingReporter()
    validator: FieldValidator = FieldValidator()
    assert validator.validate_element(order, reporter)
    assert len(reporter.report) == 0
