# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from logging import Logger
from typing import TYPE_CHECKING

from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_reporting import Reporter, get_reporter

from ._internal.stb_to_ifc_data import (
    convert_option_stb_to_ifc as convert_option_stb_to_ifc,
)

if TYPE_CHECKING:
    import ifcopenshell.file


def to_ifc(
    stb: StBridgeRoot,
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
    convert_option: convert_option_stb_to_ifc.ConvertOptionStbToIfc | None = None,
) -> "ifcopenshell.file":
    """ST-BridgeをIFCへ変換します。

    この関数を利用するためにはifcopenshellが必要です。

    Args:
        stb: ST-Bridgeモデル
        logger: 出力用のLogger。
        reporter: 出力用のReporter。
        convert_option: 変換オプション。現在暫定APIのため、
            将来的に変更される可能性があります。

    Returns:
        ifcopenshell.file: 生成されたIFCモデル
    """
    from .._internal.data_model.ifc_data.entity_data import IfcModel
    from ..upgrade import upgrade_to_latest
    from ._internal.stb_to_ifc_data._stb_to_ifc_data import stb_to_ifc_data

    reporter = get_reporter(logger, reporter)
    stb = upgrade_to_latest(stb, reporter=reporter)
    ifc_model: IfcModel = stb_to_ifc_data(stb, reporter=reporter, option=convert_option)
    return ifc_model.to_ifc(reporter=reporter)


__all__ = [
    "to_ifc",
    "convert_option_stb_to_ifc",
]
