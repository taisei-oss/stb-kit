# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

from ...data_model.common import StBridgeRoot
from ...stb_reporting import Reporter
from .common import BaseValidator, CompositeValidator, ValidationContext
from .schema_validator import SchemaValidator, _uses_xsd


def validate_schema(
    stb: StBridgeRoot | str,
    *,
    reporter: Reporter,
    xsd_path: Path | None = None,
    require_xsd: bool = False,
    exclude_legal_extensions: bool = True,
) -> bool:
    """ST-Bridgeのスキーマチェックを実施する。

    xsd_pathもrequire_xsdも指定しない場合は、XSDを使わずにデータモデルによるチェックを実施します。
    いずれかを指定した場合はXSDによるチェックを行います。
    XSDのパスを省略したときは、バージョンごとの環境変数からスキーマを探します。
    - STBKIT_SCHEMA_PATH_STB_V2_0_0
    - STBKIT_SCHEMA_PATH_STB_V2_0_1
    - STBKIT_SCHEMA_PATH_STB_V2_0_2
    - STBKIT_SCHEMA_PATH_STB_V2_1_0
    - STBKIT_SCHEMA_PATH_STB_V2_1_1
    また、値が空文字列でないかなどのSTB-KIT独自のチェックも併せて行います。

    検出した不適合は例外にせず、reporterへ出力します。
    XSDチェックに必要なxmlschemaが未インストールの場合やXSDを解決できない場合は、
    require_xsdがFalseならスキップしてTrueを返します。

    Args:
        stb: 検証するST-Bridgeモデル、またはST-BridgeのXML文字列。
        reporter: 出力先Reporter。
        xsd_path: チェックに使用するXSDファイルのパス。
            Noneの場合はrequire_xsd=Trueの場合、環境変数から探します。
        require_xsd: XSDによる検証を必須とするかどうか。
            Trueの場合、XSDを利用できないときはFalseを返します。
        exclude_legal_extensions: 仕様に準拠した拡張に起因するXSD違反を記録しないかどうか。
            Trueの場合、StbExtensionsで定義された拡張属性・拡張子要素についての違反を除外します。
            仕様準拠しているか判断できなかった場合そのままエラーとして残る場合があります。
            XSDを使わない場合は効果がありません。

    Returns:
        bool: スキーマエラーが無ければTrue、あればFalse。

    Raises:
        ValueError: stbがStBridgeRootでもstrでもない場合。
        UnsafeXmlError: stbにXML文字列を渡し、DOCTYPE宣言が含まれる場合。
        SchemaError: XSD検証でxmlのバージョンを判定できない場合。
        TypeError: モデルの子要素リストにStBridgeElement以外の値が含まれる場合。
        AssertionError: 複数回出現しうる子要素の内部値がリストでない場合。

    Examples:
        >>> from stbkit.core.stb_reporting import CollectingReporter
        >>> import stbkit.api
        >>> reporter = CollectingReporter()
        >>> is_valid = stbkit.api.validate_schema(stb, reporter=reporter)
    """
    validator: SchemaValidator = SchemaValidator(
        xsd_path=xsd_path,
        require_xsd=require_xsd,
        exclude_legal_extensions=exclude_legal_extensions,
    )
    ctx: ValidationContext
    match stb:
        case str():
            # XSDでチェックする場合、読み込み時の退避エラーはXSDのチェック結果とかぶるため記録しない。
            # XSDを使わない場合は、退避エラーが検出そのものになるため記録する。
            ctx = ValidationContext(
                reporter=reporter,
                xml=stb,
                report_load=not _uses_xsd(xsd_path=xsd_path, require_xsd=require_xsd),
            )
        case StBridgeRoot():
            ctx = ValidationContext(reporter=reporter, stb=stb)
        case _:
            raise ValueError("引数stbの型が異なります")
    return validator.validate(ctx)


def _validate(
    reporter: Reporter,
    *,
    stb: StBridgeRoot | None = None,
    xml: str | None = None,
    validators: list[BaseValidator] | None = None,
    use_xsd: bool = False,
    xsd_path: Path | None = None,
    check_schema: bool = True,
) -> bool:
    """汎用バリデーター"""
    if not validators:
        validators = []
        if check_schema:
            validators.append(SchemaValidator(require_xsd=use_xsd, xsd_path=xsd_path))
    if not validators:
        reporter.error("バリデーションのためのValidatorが指定されていません")
        return False
    composite: CompositeValidator = CompositeValidator(validators)
    ctx: ValidationContext = ValidationContext(reporter=reporter, stb=stb, xml=xml)
    return composite.validate(ctx)
