# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from abc import ABC, abstractmethod

from ...data_model.common import StBridgeElement, StBridgeRoot
from ...stb_reporting import Code, NullReporter, Phase, Reporter, Severity


class _ValidationLoadReporter(Reporter):
    def __init__(self, reporter: Reporter) -> None:
        self._reporter = reporter

    def _emit(
        self,
        severity: Severity,
        message: str,
        *,
        code: Code | None = None,
        phase: Phase | None = None,
        element_guid: str | None = None,
        xpath: str | None = None,
        value: str | None = None,
        stb_element: StBridgeElement | None = None,
        attr_name: str | None = None,
        ref_element_guid: str | None = None,
        ref_xpath: str | None = None,
        ref_value: str | None = None,
        ref_stb_element: StBridgeElement | None = None,
        ref_attr_name: str | None = None,
    ) -> None:
        if code is Code.REPAIR_LOG:
            return
        self._reporter._emit(
            severity,
            message,
            code=code,
            phase=phase,
            element_guid=element_guid,
            xpath=xpath,
            value=value,
            stb_element=stb_element,
            attr_name=attr_name,
            ref_element_guid=ref_element_guid,
            ref_xpath=ref_xpath,
            ref_value=ref_value,
            ref_stb_element=ref_stb_element,
            ref_attr_name=ref_attr_name,
        )


class ValidationContext:
    def __init__(
        self,
        *,
        reporter: Reporter,
        stb: StBridgeRoot | None = None,
        xml: str | None = None,
        use_xsd: bool = False,
        _report_invalid_values: bool = False,
    ) -> None:
        """バリデーションを行うコンテキスト。

        Args:
            reporter: 出力するReporter
            stb: 検証するST-Bridgeのデータモデル
            xml: 検証するST-BridgeのXML文字列
            use_xsd: XSDによる検証を行うかどうか。
                Trueにすると、XSDチェックと重複するSTB-KITによる報告を除外する。
        """
        if stb is None and xml is None:
            raise ValueError("stbまたはxmlのいずれかを指定する必要があります")
        if xml is not None:
            # XSD検証はxmlschemaへXMLを直接渡すため、
            # その前に危険な記述がないかチェックする。
            from ...stb_io._internal.stream_reader import check_no_doctype

            check_no_doctype(xml)
        self._stb: StBridgeRoot | None = stb
        self._xml: str | None = xml
        self._report_load: bool = not use_xsd
        self._use_xsd: bool = use_xsd
        self.reporter: Reporter = reporter
        # 退避済みの不整値を報告するかどうか。
        # 読み込み時やスキーマチェック時は
        # 元ファイルの不整値を報告する必要があるため、Trueにする
        # 編集後や出力時のチェックでは、すでに不整値が退避されているためFalseにする。
        self._report_invalid_values: bool = _report_invalid_values

    def obj(self) -> StBridgeRoot:
        from ...stb_io._internal.xml_io import _raw_loads

        if self._stb is None:
            assert self._xml is not None, "StBridgeまたはXMLのいずれかが必要です"
            self._stb = _raw_loads(
                self._xml,
                reporter=(
                    _ValidationLoadReporter(self.reporter)
                    if self._report_load
                    else NullReporter()
                ),
            )
        return self._stb

    def xml(self) -> str:
        from ...stb_io._internal.serializer import _raw_dumps

        if self._xml is None:
            assert self._stb is not None, "StBridgeまたはXMLのいずれかが必要です"
            self._xml = _raw_dumps(self._stb, reporter=NullReporter(), _strict=False)
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
