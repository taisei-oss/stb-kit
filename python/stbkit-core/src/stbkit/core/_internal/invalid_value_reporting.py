# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Any

from ..data_model.common import StBridgeElement
from ..stb_reporting import Code, Phase, Reporter


def report_invalid_value(
    reporter: Reporter,
    *,
    message: str,
    phase: Phase,
    xpath: str,
    value: Any = None,
    ref_value: str | None = None,
    element: StBridgeElement | None = None,
    is_extension: bool = False,
) -> None:
    if is_extension and phase is not Phase.LOAD:
        reporter.error(
            message=f"{message}。不正値として退避しました",
            code=Code.SCHEMA_ERROR,
            phase=phase,
            xpath=xpath,
            value=value,
            stb_element=element,
        )
        return
    if is_extension and value is not None:
        value = str(value)
    reporter.error(
        message=message,
        code=Code.SCHEMA_ERROR,
        phase=phase,
        xpath=xpath,
        value=value,
        ref_value=ref_value,
        stb_element=element,
    )
    reporter.warning(
        message="不正値をinvalid_valueに退避しました",
        code=Code.REPAIR_LOG,
        phase=phase,
        xpath=xpath,
        value=value,
        stb_element=element,
    )
