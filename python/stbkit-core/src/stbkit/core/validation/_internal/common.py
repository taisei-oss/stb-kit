# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from abc import ABC, abstractmethod

from ...data_model.common import StBridgeRoot
from ...stb_reporting import NullReporter, Reporter


class ValidationContext:
    def __init__(
        self,
        *,
        reporter: Reporter,
        stb: StBridgeRoot | None = None,
        xml: str | None = None,
        report_load: bool = True,
    ) -> None:
        """バリデーションを行うコンテキスト。

        Args:
            reporter: 出力するReporter
            stb: 検証するST-Bridgeのデータモデル
            xml: 検証するST-BridgeのXML文字列
            report_load: XML文字列からモデルをloadするときに、エラーをreporterへ記録するかどうか。
                読み込み時の退避報告と同じエラーをvalidatorが別の根拠で報告する場合に、Falseを指定して二重記録を防ぐ。
        """
        if stb is None and xml is None:
            raise ValueError("stbまたはxmlのいずれかを指定する必要があります")
        if xml is not None:
            # XSD検証はxmlschemaへXMLを直接渡すため、その前に危険な記述がないかチェックする。
            from ...stb_io._internal.stream_reader import check_no_doctype

            check_no_doctype(xml)
        self._stb: StBridgeRoot | None = stb
        self._xml: str | None = xml
        self._report_load: bool = report_load
        self.reporter: Reporter = reporter

    def obj(self) -> StBridgeRoot:
        from ...stb_io._internal.xml_io import _raw_loads

        if self._stb is None:
            assert self._xml is not None, "StBridgeまたはXMLのいずれかが必要です"
            self._stb = _raw_loads(
                self._xml,
                reporter=self.reporter if self._report_load else NullReporter(),
            )
        return self._stb

    def xml(self) -> str:
        from ...stb_io._internal.serializer import _raw_dumps

        if self._xml is None:
            assert self._stb is not None, "StBridgeまたはXMLのいずれかが必要です"
            self._xml = _raw_dumps(self._stb, reporter=self.reporter)
        return self._xml


class BaseValidator(ABC):
    @abstractmethod
    def validate(self, ctx: ValidationContext) -> bool:
        raise NotImplementedError("サブクラスで実装してください")


class CompositeValidator(BaseValidator):
    def __init__(self, validators: list[BaseValidator]) -> None:
        self.validators = validators

    def validate(self, ctx: ValidationContext) -> bool:
        is_valid = True
        for validator in self.validators:
            tmp_result: bool = validator.validate(ctx)
            is_valid = is_valid and tmp_result
        return is_valid
