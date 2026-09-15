# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from logging import Logger
from typing import TYPE_CHECKING, Literal, overload

from stbkit.core.data_model import (
    stb_v2_0_0,
    stb_v2_0_1,
    stb_v2_0_2,
    stb_v2_1_0,
    stb_v2_1_1,
)
from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_exceptions import UnsupportedStbVersionError
from stbkit.core.stb_reporting import Code, Phase, Reporter, get_reporter
from stbkit.core.validation._internal.validator import _validate

from .common import convert_element
from .v2_0_2_to_v2_1_0 import upgrade_v2_0_2_to_v2_1_0
from .v2_1_0_to_v2_1_1 import upgrade_v2_1_0_to_v2_1_1

if TYPE_CHECKING:
    from stbkit.api import stb_latest

__all__ = ["upgrade_v2_0_2_to_v2_1_0", "upgrade_v2_1_0_to_v2_1_1"]


def upgrade_v2_0_0_to_v2_0_1(
    stb: stb_v2_0_0.StBridge,
    *,
    reporter: Reporter,
) -> stb_v2_0_1.StBridge:
    reporter.info(
        "---v2.0.0->v2.0.1変換処理開始---",
        code=Code.PROGRESS_INFO,
        phase=Phase.UPGRADE,
    )
    new_stb = convert_element(
        stb,
        stb_v2_0_1,
        reporter=reporter,
    )
    if isinstance(new_stb, stb_v2_0_1.StBridge):
        new_stb.version = stb_v2_0_1.VERSION
        reporter.info(
            "---v2.0.0->v2.0.1変換処理完了---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        reporter.info(
            "---v2.0.1バリデーション開始---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        _validate(reporter=reporter, stb=new_stb)
        reporter.info(
            "---v2.0.1バリデーション完了---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        return new_stb
    else:
        raise TypeError("ST-Bridgeのバージョン変換に失敗しました")


def upgrade_v2_0_1_to_v2_0_2(
    stb: stb_v2_0_1.StBridge,
    *,
    reporter: Reporter,
) -> stb_v2_0_2.StBridge:
    reporter.info(
        "---v2.0.1->v2.0.2変換処理開始---",
        code=Code.PROGRESS_INFO,
        phase=Phase.UPGRADE,
    )
    new_stb = convert_element(
        stb,
        stb_v2_0_2,
        reporter=reporter,
    )
    if isinstance(new_stb, stb_v2_0_2.StBridge):
        new_stb.version = stb_v2_0_2.VERSION
        reporter.info(
            "---v2.0.1->v2.0.2変換処理完了---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        reporter.info(
            "---v2.0.2バリデーション開始---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        _validate(reporter=reporter, stb=new_stb)
        reporter.info(
            "---v2.0.2バリデーション完了---",
            code=Code.PROGRESS_INFO,
            phase=Phase.UPGRADE,
        )
        return new_stb
    else:
        raise TypeError("ST-Bridgeのバージョン変換に失敗しました")


def upgrade_to_v2_0_1(stb: StBridgeRoot, *, reporter: Reporter) -> stb_v2_0_1.StBridge:
    if isinstance(stb, stb_v2_0_1.StBridge):
        return stb
    elif isinstance(stb, stb_v2_0_0.StBridge):
        return upgrade_v2_0_0_to_v2_0_1(stb, reporter=reporter)
    else:
        raise NotImplementedError("対応していないバージョン変換です")


def upgrade_to_v2_0_2(stb: StBridgeRoot, *, reporter: Reporter) -> stb_v2_0_2.StBridge:
    if isinstance(stb, stb_v2_0_2.StBridge):
        return stb
    elif not isinstance(stb, stb_v2_0_1.StBridge):
        stb = upgrade_to_v2_0_1(stb, reporter=reporter)
    return upgrade_v2_0_1_to_v2_0_2(stb, reporter=reporter)


def upgrade_to_v2_1_0(stb: StBridgeRoot, *, reporter: Reporter) -> stb_v2_1_0.StBridge:
    if isinstance(stb, stb_v2_1_0.StBridge):
        return stb
    elif not isinstance(stb, stb_v2_0_2.StBridge):
        stb = upgrade_to_v2_0_2(stb, reporter=reporter)
    return upgrade_v2_0_2_to_v2_1_0(stb, reporter=reporter)


def upgrade_to_v2_1_1(stb: StBridgeRoot, *, reporter: Reporter) -> stb_v2_1_1.StBridge:
    if isinstance(stb, stb_v2_1_1.StBridge):
        return stb
    elif not isinstance(stb, stb_v2_1_0.StBridge):
        stb = upgrade_to_v2_1_0(stb, reporter=reporter)
    return upgrade_v2_1_0_to_v2_1_1(stb, reporter=reporter)


@overload
def upgrade_to(
    stb: StBridgeRoot,
    to_version: Literal["2.0.1"],
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> stb_v2_0_1.StBridge: ...
@overload
def upgrade_to(
    stb: StBridgeRoot,
    to_version: Literal["2.0.2"],
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> stb_v2_0_2.StBridge: ...
@overload
def upgrade_to(
    stb: StBridgeRoot,
    to_version: Literal["2.1.0"],
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> stb_v2_1_0.StBridge: ...
@overload
def upgrade_to(
    stb: StBridgeRoot,
    to_version: Literal["2.1.1", "latest"],
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> stb_v2_1_1.StBridge: ...
def upgrade_to(
    stb: StBridgeRoot,
    to_version: Literal["2.0.1", "2.0.2", "2.1.0", "2.1.1", "latest"] = "latest",
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> StBridgeRoot:
    """指定したバージョンにST-Bridgeを変換する"""
    reporter = get_reporter(logger=logger, reporter=reporter)
    if to_version == "latest":
        return upgrade_to_latest(stb, reporter=reporter)
    match to_version:
        case "2.0.1":
            return upgrade_to_v2_0_1(stb, reporter=reporter)
        case "2.0.2":
            return upgrade_to_v2_0_2(stb, reporter=reporter)
        case "2.1.0":
            return upgrade_to_v2_1_0(stb, reporter=reporter)
        case "2.1.1":
            return upgrade_to_v2_1_1(stb, reporter=reporter)
        case _:
            raise UnsupportedStbVersionError(version=to_version)


def upgrade_to_latest(
    stb: StBridgeRoot,
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_latest.StBridge":
    """ST-Bridgeモデルをstbkitが対応する最新版へ変換します。

    既に最新版の場合は、変換せず同じインスタンスをそのまま返します。
    変換後のモデルはバリデーションを行い、結果をreporterへ記録します。

    変換が実装されていない要素や属性があっても例外にせず、reporterへ記録して変換を続けます。

    Args:
        stb: 変換元のST-Bridgeのルート要素。
        logger: 出力先Logger
        reporter: 出力先Reporter。

    Returns:
        stb_latest.StBridge: 最新版のST-Bridgeのルート要素。

    Raises:
        UnsupportedStbVersionError: 対応していないバージョンのモデルを渡した場合。
        TypeError: バージョン変換に失敗した場合。

    Examples:
        >>> import stbkit.api
        >>> stb = stbkit.api.upgrade_to_latest(stbkit.api.load("model_v2_0_1.stb"))
    """
    reporter = get_reporter(logger, reporter)
    return upgrade_to_v2_1_1(stb, reporter=reporter)
