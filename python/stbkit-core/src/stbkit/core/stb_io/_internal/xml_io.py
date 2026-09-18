# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import codecs
import os
from collections.abc import Iterator
from logging import Logger
from typing import IO, TYPE_CHECKING, Literal, TextIO, overload

from ..._internal.constants import (
    DEFAULT_MAX_XML_DEPTH,
    DEFAULT_MAX_XML_SIZE,
    VERSION_TO_MODULE_NAME,
    XML_READ_CHUNK_SIZE,
)
from ..._internal.extension_utils import ExtensionInfoRepository
from ...data_model.common import StBridgeRoot
from ...stb_exceptions import (
    SchemaError,
    XmlLimitExceededError,
    XmlLimitKind,
)
from ...stb_reporting import Code, CollectingReporter, Phase, Reporter, get_reporter
from ...stb_typing import StbVersion, TextSource
from ...validation import validate_schema
from ...validation._internal.validator import _validate
from . import loader, serializer, stream_reader

if TYPE_CHECKING:
    from ...data_model import (
        stb_v2_0_0,
        stb_v2_0_1,
        stb_v2_0_2,
        stb_v2_1_0,
        stb_v2_1_1,
    )


def dumps(
    stb: StBridgeRoot,
    *,
    app_name: str | None = None,
    app_version: str | None = None,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> str:
    """ST-BridgeのデータモデルをXML文字列へ出力します。

    出力前にスキーマ検証を行い、スキーマ違反がある場合は例外を投げます。

    Args:
        stb: 出力するST-Bridgeのルート要素
        app_name: StbCommonのapp_nameに記載するアプリケーション名
        app_version: StbCommonのapp_versionに記載するバージョン番号
        logger: 出力先Logger
        reporter: 出力先Reporter

    Returns:
        str: XML宣言を含むST-BridgeのXML文字列。

    Raises:
        SchemaError: スキーマ違反がある場合。
        TypeError: 子要素のリストにStBridgeElement以外の値が含まれる場合。
        RuntimeError: フィールド定義から想定できない属性が含まれる場合。

    Examples:
        >>> import stbkit.api
        >>> xml = stbkit.api.dumps(stb)
    """
    reporter = get_reporter(logger, reporter)
    serializer.set_app_name_and_version(
        stb, app_name=app_name, app_version=app_version, reporter=reporter
    )
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=reporter, phase=Phase.DUMP)
    ext_repo.repair_stb(stb, reporter=reporter, phase=Phase.DUMP)
    schema_reporter: CollectingReporter = CollectingReporter()
    if not validate_schema(
        stb, reporter=schema_reporter, xsd_path=None, require_xsd=False
    ):
        raise SchemaError(
            "スキーマ違反のため出力できません\n" + schema_reporter.report.to_text()
        )
    return serializer._raw_dumps(stb, reporter=reporter, _strict=True)


def dump(
    stb: StBridgeRoot,
    fp: TextIO,
    *,
    app_name: str | None = None,
    app_version: str | None = None,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> None:
    """ST-Bridgeのデータモデルを、テキストストリームへXMLとして書き出します。

    dumpsのファイル書き込み版です。
    ファイルへ保存する場合は、utf-8で開いたストリームを渡してください。

    Args:
        stb: 出力するST-Bridgeのルート要素
        fp: 書き込み先のテキストストリーム
        app_name: StbCommonのapp_nameに記載するアプリケーション名
        app_version: StbCommonのapp_versionに記載するバージョン番号
        logger: 出力先Logger
        reporter: 出力先Reporter

    Raises:
        SchemaError: スキーマ検証に違反した場合、または必須属性がNoneや空文字列の場合。
        TypeError: 子要素のリストにStBridgeElement以外の値が含まれる場合。
        RuntimeError: フィールド定義から想定できない属性が含まれる場合。
        OSError: fpへの書き込みに失敗した場合。
        UnicodeEncodeError: fpのエンコーディングで表現できない文字が含まれる場合。
        ValueError: fpのencodingがUTF-8でない場合。

    Examples:
        >>> import stbkit.api
        >>> with open("model.stb", "w", encoding="utf-8") as f:
        ...     stbkit.api.dump(stb, f)
    """
    _check_encoding(fp)
    fp.write(
        dumps(
            stb,
            app_name=app_name,
            app_version=app_version,
            logger=logger,
            reporter=reporter,
        )
    )


@overload
def loads(
    s: str,
    *,
    version: Literal["2.0.0"],
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_0_0.StBridge": ...


@overload
def loads(
    s: str,
    *,
    version: Literal["2.0.1"],
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_0_1.StBridge": ...


@overload
def loads(
    s: str,
    *,
    version: Literal["2.0.2"],
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_0_2.StBridge": ...


@overload
def loads(
    s: str,
    *,
    version: Literal["2.1.0"],
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_1_0.StBridge": ...


@overload
def loads(
    s: str,
    *,
    version: Literal["2.1.1"],
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_1_1.StBridge": ...


@overload
def loads(
    s: str,
    *,
    version: None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> StBridgeRoot: ...


def loads(
    s: str,
    *,
    version: StbVersion | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> StBridgeRoot:
    """XML文字列をST-Bridgeのデータモデルへ読み込みます。

    Args:
        s: 読み込むST-BridgeのXML文字列。
        version: 読み込むST-Bridgeのバージョン。
            Noneの場合は自動で適切に判定します。
            指定した場合は、強制的に指定したバージョンで読み込みます。
        max_size: 読み込む文字数の上限。超えた場合は読み込みを中止します。
        max_depth: 要素の階層の上限。超えた場合は読み込みを中止します。
        logger: 出力先Logger。
        reporter: 出力先Reporter。

    Returns:
        StBridgeRoot: 読み込んだST-Bridgeのルート要素。
            versionを指定した場合は、そのバージョンのStBridgeを返します。

    Raises:
        UnsafeXmlError: DOCTYPE宣言が含まれる場合。
        XmlLimitExceededError: max_sizeまたはmax_depthを超えた場合。
        SchemaError: versionを省略したときにversionが取得できなかった場合。
        UnsupportedStbVersionError: 対応していないバージョンの場合。
        xml.etree.ElementTree.ParseError: XMLとして解析できない場合。

    Examples:
        >>> import stbkit.api
        >>> stb = stbkit.api.loads(xml_text)
    """
    reporter = get_reporter(logger, reporter)
    return _finish_load(
        stream_reader.read_stream(
            (s,),
            version=version,
            reporter=reporter,
            max_size=max_size,
            max_depth=max_depth,
        ),
        reporter=reporter,
    )


@overload
def load(
    fp: TextSource,
    *,
    version: Literal["2.0.0"],
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_0_0.StBridge": ...


@overload
def load(
    fp: TextSource,
    *,
    version: Literal["2.0.1"],
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_0_1.StBridge": ...


@overload
def load(
    fp: TextSource,
    *,
    version: Literal["2.0.2"],
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_0_2.StBridge": ...


@overload
def load(
    fp: TextSource,
    *,
    version: Literal["2.1.0"],
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_1_0.StBridge": ...


@overload
def load(
    fp: TextSource,
    *,
    version: Literal["2.1.1"],
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> "stb_v2_1_1.StBridge": ...


@overload
def load(
    fp: TextSource,
    *,
    version: None = None,
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> StBridgeRoot: ...


def load(
    fp: TextSource,
    *,
    version: StbVersion | None = None,
    encoding: str | None = None,
    max_size: int = DEFAULT_MAX_XML_SIZE,
    max_depth: int = DEFAULT_MAX_XML_DEPTH,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> StBridgeRoot:
    """ST-Bridgeファイルをデータモデルへ読み込みます。

    Args:
        fp: 読み込むファイルのパス、または開いたテキストストリーム。
        version: 読み込むST-Bridgeのバージョン。
            Noneの場合は自動で適切に判定します。
            指定した場合は、強制的に指定したバージョンで読み込みます。
        encoding: ファイルのエンコーディング。
            Noneの場合は自動判定し、判定できない場合はUTF-8を使用します。
            fpがストリームの場合は無視します。
        max_size: 読み込むサイズの上限。超えた場合は読み込みを中止します。
        max_depth: 要素の階層の上限。超えた場合は読み込みを中止します。
        logger: 出力先Logger。
        reporter: 出力先Reporter。

    Returns:
        StBridgeRoot: 読み込んだST-Bridgeのルート要素。
            versionを指定した場合は、そのバージョンのStBridgeを返します。

    Raises:
        OSError: ファイルを開けない場合。
            存在しない場合はサブクラスのFileNotFoundErrorを投げます。
        LookupError: encodingに未知のエンコーディング名を指定した場合。
        UnicodeDecodeError: デコードできない場合。
        UnsafeXmlError: DOCTYPE宣言が含まれる場合。
        XmlLimitExceededError: max_sizeまたはmax_depthを超えた場合。
        SchemaError: versionを省略したときにversionが取得できなかった場合。
        UnsupportedStbVersionError: 対応していないバージョンの場合。
        xml.etree.ElementTree.ParseError: XMLとして解析できない場合。

    Examples:
        >>> import stbkit.api
        >>> stb = stbkit.api.load("model.stb")
    """
    reporter = get_reporter(logger, reporter)
    if not isinstance(fp, (str, os.PathLike)):
        return _finish_load(
            stream_reader.read_stream(
                _iter_chunks(fp),
                version=version,
                reporter=reporter,
                max_size=max_size,
                max_depth=max_depth,
            ),
            reporter=reporter,
        )
    size: int = os.stat(fp).st_size
    if size > max_size:
        raise XmlLimitExceededError(kind=XmlLimitKind.SIZE, limit=max_size, actual=size)
    if not encoding:
        encoding = loader._detect_encoding(fp)
    with open(fp, encoding=encoding) as f:
        return _finish_load(
            stream_reader.read_stream(
                _iter_chunks(f),
                version=version,
                reporter=reporter,
                max_size=max_size,
                max_depth=max_depth,
            ),
            reporter=reporter,
        )


def _check_encoding(text_io: TextIO) -> None:
    encoding: str | None = getattr(text_io, "encoding", None)

    if encoding is None:
        return

    try:
        normalized: str = codecs.lookup(encoding).name
    except LookupError:
        return

    if normalized != "utf-8":
        raise ValueError(
            f"dumpはUTF-8コーディングである必要があります。現在のエンコーディング:{encoding}"
        )


def _iter_chunks(src: IO[str]) -> Iterator[str]:
    while chunk := src.read(XML_READ_CHUNK_SIZE):
        yield chunk


def _expected_version(stb: StBridgeRoot) -> str:
    stb_type: type[StBridgeRoot] = type(stb)
    if stb_type.__name__ != "StBridge":
        raise RuntimeError(f"{stb_type.__name__}はST-Bridgeのルート要素ではありません")

    for version, module_name in VERSION_TO_MODULE_NAME.items():
        if stb_type.__module__.endswith(f".{module_name}"):
            return version

    raise RuntimeError(f"{stb_type.__name__}はST-Bridgeのルート要素ではありません")


def _finish_load(
    stb: StBridgeRoot, *, reporter: Reporter, check_schema: bool = True
) -> StBridgeRoot:
    """読み込み直後のバージョン確認と拡張情報の整理を行う。

    check_schema=Falseにすると、読み込み時のスキーマチェックを行わない。
    二重の記録を避けるために使用する。
    """
    expected_version: str = _expected_version(stb)
    if stb.version != expected_version:
        reporter.error(
            message="ファイルのバージョンが指定したバージョンと異なります",
            code=Code.VERSION_MISMATCH,
            phase=Phase.LOAD,
            value=stb.version,
            ref_value=expected_version,
        )
    if check_schema:
        _validate(reporter=reporter, stb=stb)
    ext_repo: ExtensionInfoRepository = ExtensionInfoRepository()
    ext_repo.register(stb, reporter=reporter, phase=Phase.LOAD)
    ext_repo.repair_stb(stb, reporter=reporter, phase=Phase.LOAD)
    return stb


def _raw_loads(s: str, *, reporter: Reporter) -> StBridgeRoot:
    """バリデーションのためにXML文字列をデータモデルへ読み込む。

    読み込み時のスキーマチェックは呼び出し元のvalidatorが行うため、ここでは実行しない。
    退避した不正値や拡張情報はreporterへ記録する。
    """
    return _finish_load(
        stream_reader.read_stream((s,), reporter=reporter),
        reporter=reporter,
        check_schema=False,
    )
