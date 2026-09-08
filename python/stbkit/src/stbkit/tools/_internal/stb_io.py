# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from logging import Logger

from stbkit.core._internal.constants import (
    DEFAULT_MAX_XML_DEPTH,
    DEFAULT_MAX_XML_SIZE,
)
from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_io import load, loads
from stbkit.core.stb_reporting import Reporter
from stbkit.core.stb_typing import TextSource

from stbkit.api import stb_latest

from ..upgrade import upgrade_to_latest


def load_latest(
    fp: TextSource,
    *,
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> stb_latest.StBridge:
    """ST-Bridgeファイルを読み込み、最新版のデータモデルへ変換して返します。

    Args:
        fp: 読み込むファイルのパス、または開いたテキストストリーム。
        encoding: ファイルのエンコーディング。
            Noneの場合は自動判定し、判定できない場合はUTF-8を使用します。
            fpがストリームの場合は無視します。
        max_size: 読み込むサイズの上限。超えた場合は読み込みを中止します。
        max_depth: 要素の階層の上限。超えた場合は読み込みを中止します。
        logger: 出力先Logger。
        reporter: 出力先Reporter。

    Returns:
        StBridge: 最新版のST-Bridgeのルート要素。

    Raises:
        OSError: ファイルを開けない場合。存在しない場合はサブクラスのFileNotFoundErrorを投げます。
        LookupError: encodingに未知のエンコーディング名を指定した場合。
        UnicodeDecodeError: デコードできない場合。
        UnsafeXmlError: DOCTYPE宣言が含まれる場合。
        XmlLimitExceededError: max_sizeまたはmax_depthを超えた場合。
        SchemaError: versionを省略したときにversionが取得できなかった場合。
        UnsupportedStbVersionError: 対応していないバージョンの場合。
        xml.etree.ElementTree.ParseError: XMLとして解析できない場合。

    Examples:
        >>> import stbkit.api
        >>> stb = stbkit.api.load_latest("model.stb")
    """
    stb: StBridgeRoot = load(
        fp,
        encoding=encoding,
        max_size=max_size,
        max_depth=max_depth,
        logger=logger,
        reporter=reporter,
    )
    latest: stb_latest.StBridge = upgrade_to_latest(
        stb, logger=logger, reporter=reporter
    )
    return latest


def loads_latest(
    s: str,
    *,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> stb_latest.StBridge:
    """XML文字列をST-Bridgeのデータモデルへ読み込み、最新版のデータモデルへ変換して返します。

    Args:
        s: 読み込むST-BridgeのXML文字列。
        max_size: 読み込む文字数の上限。超えた場合は読み込みを中止します。
        max_depth: 要素の階層の上限。超えた場合は読み込みを中止します。
        logger: 出力先Logger。
        reporter: 出力先Reporter。

    Returns:
        StBridgeRoot: 最新版のST-Bridgeのルート要素。

    Raises:
        UnsafeXmlError: DOCTYPE宣言が含まれる場合。
        XmlLimitExceededError: max_sizeまたはmax_depthを超えた場合。
        SchemaError: versionを省略したときにversionが取得できなかった場合。
        UnsupportedStbVersionError: 対応していないバージョンの場合。
        xml.etree.ElementTree.ParseError: XMLとして解析できない場合。

    Examples:
        >>> import stbkit.api
        >>> stb = stbkit.api.loads_latest(xml_text)
    """
    stb: StBridgeRoot = loads(
        s,
        max_size=max_size,
        max_depth=max_depth,
        logger=logger,
        reporter=reporter,
    )
    latest: stb_latest.StBridge = upgrade_to_latest(
        stb, logger=logger, reporter=reporter
    )
    return latest
