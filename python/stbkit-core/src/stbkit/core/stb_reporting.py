# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""IO・変換・バリデーション等で発生した処理メッセージを記録するモジュール。

stbkitの各APIは、load時にスキーマ違反等があっても続行可能であれば例外にせずReporterへ記録します。
記録内容をあとから処理したい場合はCollectingReporter、ログへ流す場合はLoggerReporterを使用します。
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import UTC, datetime
from enum import IntEnum, StrEnum
from logging import Logger
from typing import Any, Literal

from ._internal.name_converter import private_field_name
from ._internal.stb_logger import get_logger
from .data_model.common import StBridgeElement


class Severity(IntEnum):
    """メッセージの重大度。値はloggingのレベルと同じです。"""

    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40


class Code(StrEnum):
    """メッセージの分類コード。"""

    DIFF = "diff"
    """差分（比較結果）"""
    DEVELOPER_ERROR = "developer_error"
    """実装にバグがあることを示すエラー"""
    EXTENSION_ERROR = "extension_error"
    """拡張の定義/使用に関するエラー"""
    MEMBER_NOT_FOUND = "member_not_found"
    """部材が見つからない"""
    MISSING_ATTRIBUTE = "missing_attribute"
    """属性不足"""
    NOT_IMPLEMENTED = "not_implemented"
    """未実装"""
    OPTIONAL_DEPENDENCY_MISSING = "optional_dependency_missing"
    """オプション依存が見つからない"""
    PROGRESS_INFO = "progress_info"
    """進行状況の情報"""
    REFERENCE_NOT_FOUND = "reference_not_found"
    """参照先が見つからない"""
    REPAIR_LOG = "repair_log"
    """修復記録"""
    SCHEMA_ERROR = "schema_error"
    """スキーマ違反"""
    SCHEMA_VERSION_MISMATCH = "schema_version_mismatch"
    """スキーマのバージョンが異なる"""
    TEST = "test"
    """テスト用"""
    TYPE_MISMATCH = "type_mismatch"
    """型の不一致"""
    UNEXPECTED_ERROR = "unexpected_error"
    """想定外のエラー"""
    UNKNOWN = "unknown"
    """不明"""
    UNKNOWN_SHAPE = "unknown_shape"
    """不明な形状"""
    VERSION_MISMATCH = "version_mismatch"
    """バージョン不一致"""
    VERSION_UNSUPPORTED = "version_unsupported"
    """対応していないバージョン"""
    ZERO_LENGTH_MEMBER = "zero_length_member"
    """部材長が0である"""


class Phase(StrEnum):
    """メッセージが発生した処理段階。"""

    CONVERT_GEOMETRY = "convert_geometry"
    """ジオメトリ作成"""
    CONVERT_IFC = "convert_ifc"
    """IFC変換"""
    DIFF = "diff"
    """差分"""
    DIFF_GEOMETRY = "diff_geometry"
    """ジオメトリ差分"""
    DUMP = "dump"
    """書き出し"""
    LOAD = "load"
    """読み込み"""
    REPAIR = "repair"
    """修復"""
    EXTRACT = "extract"
    """抽出"""
    TEST = "test"
    """テスト"""
    TRANSFORM = "transform"
    """加工"""
    UNKNOWN = "unknown"
    """不明"""
    UPGRADE = "upgrade"
    """ST-Bridgeのバージョンアップ"""
    VALIDATE = "validate"
    """バリデーション"""


@dataclass(slots=True, frozen=True)
class _ReportItem:
    severity: int
    message: str
    timestamp: str
    code: str
    phase: str
    element_guid: str | None = None
    xpath: str | None = None
    value: str | None = None
    ref_element_guid: str | None = None
    ref_xpath: str | None = None
    ref_value: str | None = None

    @property
    def severity_enum(self) -> Severity:
        try:
            return Severity(self.severity)
        except ValueError:
            return Severity.ERROR

    @property
    def code_enum(self) -> Code:
        try:
            return Code(self.code)
        except ValueError:
            if self.code == "unknown_error":
                return Code.UNEXPECTED_ERROR
            return Code.UNKNOWN

    @property
    def phase_enum(self) -> Phase:
        try:
            return Phase(self.phase)
        except ValueError:
            return Phase.UNKNOWN

    @property
    def timestamp_dt(self) -> datetime | None:
        try:
            return datetime.fromisoformat(self.timestamp)
        except ValueError:
            return None


@dataclass(slots=True, frozen=True)
class _ResolvedDetails:
    element_name: str | None
    xpath: str | None
    ref_xpath: str | None
    value: Any | None
    ref_value: Any | None


def _resolve_details(
    *,
    stb_element: StBridgeElement | None = None,
    attr_name: str | None = None,
    value: Any | None = None,
    xpath: str | None = None,
    ref_stb_element: StBridgeElement | None = None,
    ref_attr_name: str | None = None,
    ref_value: Any | None = None,
    ref_xpath: str | None = None,
) -> _ResolvedDetails:
    def convert_value(v: Any | None) -> Any | None:
        if v is None:
            return None
        if isinstance(v, (str, int, float, bool)):
            return v
        if isinstance(v, list):
            return [convert_value(x) for x in v]
        if isinstance(v, dict):
            return {k: convert_value(val) for k, val in v.items()}
        return v.__repr__()

    if value is None and stb_element is not None and attr_name is not None:
        private_attr_name = private_field_name(attr_name)
        if hasattr(stb_element, private_attr_name):
            value = getattr(stb_element, private_attr_name, None)
    value = convert_value(value)

    if ref_value is None and ref_stb_element is not None and ref_attr_name is not None:
        private_ref_attr_name = private_field_name(ref_attr_name)
        if hasattr(ref_stb_element, private_ref_attr_name):
            ref_value = getattr(ref_stb_element, private_ref_attr_name, None)
    ref_value = convert_value(ref_value)

    if xpath is None and stb_element is not None:
        xpath = stb_element._path_xml(attr_name=attr_name)

    if ref_xpath is None and ref_stb_element is not None:
        ref_xpath = ref_stb_element._path_xml(attr_name=ref_attr_name)

    element_name = None
    if stb_element is not None:
        element_name = stb_element._xml_name()

    return _ResolvedDetails(
        element_name=element_name,
        xpath=xpath,
        ref_xpath=ref_xpath,
        value=value,
        ref_value=ref_value,
    )


class _MessageType(StrEnum):
    LOGGER = "logger"
    TEXT = "text"


def _compose_message(
    *,
    mode: _MessageType,
    message: str,
    code: str | None = None,
    phase: str | None = None,
    element_name: str | None = None,
    xpath: str | None = None,
    value: Any | None = None,
    ref_value: Any | None = None,
    has_code: bool = False,
    has_phase: bool = False,
    has_path: bool = False,
    severity_name: str = "",
    timestamp: str | None = None,
    separator: str = " ",
) -> str:
    messages: list[str] = []
    if mode != _MessageType.LOGGER:
        messages.append(f"{severity_name}")
    if timestamp is not None and mode != _MessageType.LOGGER:
        messages.append(f"[{timestamp}]")
    if code and has_code:
        messages.append(code)
    if phase and has_phase:
        messages.append(phase)
    if xpath and has_path:
        messages.append(xpath)
    elif element_name:
        messages.append(element_name)
    messages.append(message)
    details: list[str] = []
    if value is not None and value != "":
        details.append(f"value: {value}")
    if ref_value is not None and ref_value != "":
        details.append(f"expected: {ref_value}")
    if details:
        messages.append(f"({' '.join(details)})")
    return separator.join(messages)


class ReportingResult(list[_ReportItem]):
    """メッセージリスト"""

    def to_text(
        self,
        *,
        has_timestamp: bool = False,
        has_code: bool = True,
        has_phase: bool = True,
        has_path: bool = True,
        show_level: Severity = Severity.WARNING,
        separator: str = " ",
    ) -> str:
        """記録されたメッセージをテキストに変換します。

        Args:
            has_timestamp: timestampを含めるかどうか。
            has_code: codeを含めるかどうか。
            has_phase: phaseを含めるかどうか。
            has_path: xpathを含めるかどうか。
            show_level: 出力する最低の重大度。これ未満のメッセージは除きます。

        Returns:
            str: 改行区切りのテキスト。該当するメッセージが無い場合は空文字列。
        """
        lines: list[str] = []
        for item in self:
            if item.severity < show_level.value:
                continue
            lines.append(
                _compose_message(
                    mode=_MessageType.TEXT,
                    message=item.message,
                    code=item.code,
                    phase=item.phase,
                    xpath=item.xpath,
                    value=item.value,
                    ref_value=item.ref_value,
                    has_code=has_code,
                    has_phase=has_phase,
                    has_path=has_path,
                    severity_name=item.severity_enum.name,
                    timestamp=item.timestamp if has_timestamp else None,
                    separator=separator,
                )
            )
        return "\n".join(lines)


class Reporter(ABC):
    """処理メッセージの記録先の基底クラス。

    debug・info・warning・errorが受け取る引数は共通です。
    codeとphaseの優先度は、引数>set_contextやcontextで設定した既定値>bindで束縛した値です。
    """

    @abstractmethod
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
        """指定された重大度でメッセージを記録します。"""
        ...

    def debug(
        self,
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
        """DEBUGレベルのメッセージを記録します。

        Args:
            message: メッセージ
            code: 分類コード。
            phase: 処理段階。
            element_guid: 対象要素のGUID。
            xpath: 対象箇所のXPath。
            value: 実際の値。
            stb_element: 対象要素。
            attr_name: 対象属性名(Python名)。
            ref_element_guid: 比較対象要素のGUID。
            ref_xpath: 比較対象のXPath。
            ref_value: 期待される値、または比較対象の値。
            ref_stb_element: 比較対象の要素。
            ref_attr_name: 比較対象の属性名。
        """
        self._emit(
            Severity.DEBUG,
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

    def info(
        self,
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
        """infoレベルのメッセージを記録します。

        Args:
            message: メッセージ
            code: 分類コード。
            phase: 処理段階。
            element_guid: 対象要素のGUID。
            xpath: 対象箇所のXPath。
            value: 実際の値。
            stb_element: 対象要素。
            attr_name: 対象属性名(Python名)。
            ref_element_guid: 比較対象要素のGUID。
            ref_xpath: 比較対象のXPath。
            ref_value: 期待される値、または比較対象の値。
            ref_stb_element: 比較対象の要素。
            ref_attr_name: 比較対象の属性名。
        """
        self._emit(
            Severity.INFO,
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

    def warning(
        self,
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
        """warningレベルのメッセージを記録します。

        Args:
            message: メッセージ
            code: 分類コード。
            phase: 処理段階。
            element_guid: 対象要素のGUID。
            xpath: 対象箇所のXPath。
            value: 実際の値。
            stb_element: 対象要素。
            attr_name: 対象属性名(Python名)。
            ref_element_guid: 比較対象要素のGUID。
            ref_xpath: 比較対象のXPath。
            ref_value: 期待される値、または比較対象の値。
            ref_stb_element: 比較対象の要素。
            ref_attr_name: 比較対象の属性名。
        """
        self._emit(
            Severity.WARNING,
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

    def error(
        self,
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
        """errorレベルのメッセージを記録します。

        Args:
            message: メッセージ
            code: 分類コード。
            phase: 処理段階。
            element_guid: 対象要素のGUID。
            xpath: 対象箇所のXPath。
            value: 実際の値。
            stb_element: 対象要素。
            attr_name: 対象属性名(Python名)。
            ref_element_guid: 比較対象要素のGUID。
            ref_xpath: 比較対象のXPath。
            ref_value: 期待される値、または比較対象の値。
            ref_stb_element: 比較対象の要素。
            ref_attr_name: 比較対象の属性名。
        """
        self._emit(
            Severity.ERROR,
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

    def set_context(
        self, *, code: Code | None = None, phase: Phase | None = None
    ) -> None:
        """以後に記録するメッセージのcode,phaseのデフォルトを更新します。

        基底クラスでは何もしないので、継承先で実装します。

        Args:
            code: 以後で記録するときのcode。Noneの場合は変更しません。
            phase: 以後で記録するときのphase。Noneの場合は変更しません。

        Examples:
            >>> reporter.set_context(code=Code.SCHEMA_ERROR, phase=Phase.LOAD)
            >>> reporter.error("スキーマ違反がありました")
        """
        _ = code, phase

    @contextmanager
    def context(
        self, *, code: Code | None = None, phase: Phase | None = None
    ) -> Generator[Reporter, None, None]:
        """code,phaseのデフォルト値を一時的に変更し、ブロックを抜けるときに元へ戻します。

        基底クラスでは何も変更せず、自身をそのまま返すため、継承先で実装します。

        Args:
            code: ブロック内で使用するcode。
            phase: ブロック内で使用するphase。

        Yields:
            Reporter: デフォルトを変更したReporter。

        Examples:
            >>> with reporter.context(code=Code.SCHEMA_ERROR, phase=Phase.LOAD):
            ...     reporter.error("スキーマ違反がありました")
        """
        _ = code, phase
        yield self

    def bind(self, *, code: Code | None = None, phase: Phase | None = None) -> Reporter:
        """デフォルト値を固定した新しいReporterを返します。

        自身の状態は変更しません。withを使わずにデフォルト値を固定したい場合に使用します。

        Args:
            code: 固定する分類コード。
            phase: 固定する処理段階。

        Returns:
            Reporter: 固定した値を補って自身へ委譲するReporter。
        Examples:
            >>> reporter2 = reporter.bind(code=Code.SCHEMA_ERROR, phase=Phase.LOAD)
            >>> reporter2.error("スキーマ違反がありました")
        """
        return _BoundReporter(self, code=code, phase=phase)


class _BoundReporter(Reporter):
    """
    bindで取得するラッパー。
    - 呼び出し時にcode/phaseがNoneなら、固定した値を補う
    - 元のreporterの状態は変更しない
    """

    def __init__(
        self, base: Reporter, *, code: Code | None = None, phase: Phase | None = None
    ) -> None:
        self._base = base
        self._code = code
        self._phase = phase

    def _merge(
        self, code: Code | None, phase: Phase | None
    ) -> tuple[Code | None, Phase | None]:
        return (
            code if code is not None else self._code,
            phase if phase is not None else self._phase,
        )

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
        code_m, phase_m = self._merge(code, phase)
        self._base._emit(
            severity,
            message,
            code=code_m,
            phase=phase_m,
            element_guid=element_guid,
            stb_element=stb_element,
            attr_name=attr_name,
            xpath=xpath,
            value=value,
            ref_element_guid=ref_element_guid,
            ref_xpath=ref_xpath,
            ref_value=ref_value,
            ref_stb_element=ref_stb_element,
            ref_attr_name=ref_attr_name,
        )

    def bind(self, *, code: Code | None = None, phase: Phase | None = None) -> Reporter:
        return _BoundReporter(
            self._base,
            code=code if code is not None else self._code,
            phase=phase if phase is not None else self._phase,
        )

    def set_context(
        self, *, code: Code | None = None, phase: Phase | None = None
    ) -> None:
        self._code = code if code is not None else self._code
        self._phase = phase if phase is not None else self._phase

    @contextmanager
    def context(
        self, *, code: Code | None = None, phase: Phase | None = None
    ) -> Generator[Reporter, None, None]:
        with self._base.context(code=code, phase=phase):
            yield self


@dataclass(slots=True)
class _ReporterContext:
    code: Code | None = None
    phase: Phase | None = None


class _BaseReporter(Reporter):
    """
    - code/phase は引数が優先
    - 未指定ならインスタンスが保持する値を使う
    - それでも無ければ例外（ログ/レポートが壊れるより早く気づく）
    """

    def __init__(
        self,
        *,
        default_code: Code | None = None,
        default_phase: Phase | None = None,
    ) -> None:
        self._ctx = _ReporterContext(code=default_code, phase=default_phase)

    def set_context(
        self, *, code: Code | None = None, phase: Phase | None = None
    ) -> None:
        if code is not None:
            self._ctx.code = code
        if phase is not None:
            self._ctx.phase = phase

    @contextmanager
    def context(
        self, *, code: Code | None = None, phase: Phase | None = None
    ) -> Generator[Reporter, None, None]:
        prev = _ReporterContext(code=self._ctx.code, phase=self._ctx.phase)
        try:
            self.set_context(code=code, phase=phase)
            yield self
        finally:
            self._ctx = prev

    def _resolve(self, code: Code | None, phase: Phase | None) -> tuple[Code, Phase]:
        r_code = code if code is not None else self._ctx.code
        r_phase = phase if phase is not None else self._ctx.phase
        if r_code is None or r_phase is None:
            raise ValueError("code/phaseが設定されていません")
        return r_code, r_phase


class CollectingReporter(_BaseReporter):
    """メッセージをメモリ上へ蓄積するReporter。

    ログ出力は行わず、処理後にreportでまとめて取り出します。

    Args:
        default_code: デフォルトのcode。
        default_phase: デフォルトのphase。
    """

    def __init__(
        self,
        *,
        default_code: Code | None = None,
        default_phase: Phase | None = None,
    ) -> None:
        super().__init__(default_code=default_code, default_phase=default_phase)
        self._report = ReportingResult()

    @property
    def report(self) -> ReportingResult:
        """蓄積されたメッセージリスト"""
        return self._report

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
        ref_element_guid: str | None = None,
        ref_xpath: str | None = None,
        ref_value: str | None = None,
        stb_element: StBridgeElement | None = None,
        attr_name: str | None = None,
        ref_stb_element: StBridgeElement | None = None,
        ref_attr_name: str | None = None,
    ) -> None:
        code_r, phase_r = self._resolve(code, phase)
        resolved = _resolve_details(
            stb_element=stb_element,
            attr_name=attr_name,
            value=value,
            xpath=xpath,
            ref_stb_element=ref_stb_element,
            ref_attr_name=ref_attr_name,
            ref_value=ref_value,
            ref_xpath=ref_xpath,
        )

        self._report.append(
            _ReportItem(
                severity=severity.value,
                message=message,
                timestamp=datetime.now(UTC).astimezone().isoformat(),
                code=code_r.value,
                phase=phase_r.value,
                element_guid=element_guid,
                xpath=resolved.xpath,
                value=str(resolved.value) if resolved.value is not None else "",
                ref_element_guid=ref_element_guid,
                ref_xpath=resolved.ref_xpath,
                ref_value=(
                    str(resolved.ref_value) if resolved.ref_value is not None else ""
                ),
            )
        )

    def is_valid(self, *, min_level: Severity = Severity.WARNING) -> bool:
        """指定した重大度以上のメッセージが無いかどうかを返します。
        min_levelを指定しない場合はWARNING以上のメッセージが無いかどうかを返します。

        Args:
            min_level: 不適合とみなす最低の重大度。省略した場合WARNING以上のメッセージがあるかどうかを判定します。

        Returns:
            bool: min_level以上のメッセージが1件も無ければTrue。
        """
        return not any(item.severity >= min_level.value for item in self._report)


class LoggerReporter(_BaseReporter):
    """メッセージをloggingのLoggerへ出力するReporter。

    Args:
        logger: 出力先のロガー。Noneの場合はstbkitののロガーを作成します。
        level: stbkitのロガーを作成する場合の出力レベル。loggerを指定した場合は参照しません。
        default_code: codeのデフォルト。
        default_phase: phaseのデフォルト。
    """

    def __init__(
        self,
        logger: Logger | None = None,
        *,
        level: Literal[0, 10, 20, 30, 40, 50] = logging.WARNING,
        default_code: Code | None = None,
        default_phase: Phase | None = None,
    ) -> None:
        super().__init__(default_code=default_code, default_phase=default_phase)
        self.logger: Logger = logger if logger is not None else get_logger(level=level)

    def _log(
        self,
        level_name: Literal["info", "warning", "error", "debug"],
        *,
        message: str,
        code: Code,
        phase: Phase,
        xpath: str | None = None,
        value: Any | None = None,
        stb_element: StBridgeElement | None = None,
        attr_name: str | None = None,
        ref_value: Any | None = None,
        ref_stb_element: StBridgeElement | None = None,
        ref_attr_name: str | None = None,
    ) -> None:
        resolved = _resolve_details(
            stb_element=stb_element,
            attr_name=attr_name,
            value=value,
            xpath=xpath,
            ref_stb_element=ref_stb_element,
            ref_attr_name=ref_attr_name,
            ref_value=ref_value,
        )
        log_message = _compose_message(
            mode=_MessageType.LOGGER,
            message=message,
            code=code.value,
            phase=phase.value,
            element_name=resolved.element_name,
            xpath=resolved.xpath,
            value=resolved.value,
            ref_value=resolved.ref_value,
            has_code=True,
            has_phase=True,
            has_path=True,
        )
        logger_method = getattr(self.logger, level_name)
        logger_method(msg=log_message)

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
        code_r, phase_r = self._resolve(code, phase)
        if severity == Severity.INFO:
            level_name: Literal["info", "warning", "error", "debug"] = "info"
        elif severity == Severity.WARNING:
            level_name = "warning"
        elif severity == Severity.ERROR:
            level_name = "error"
        else:
            level_name = "debug"
        self._log(
            level_name,
            message=message,
            code=code_r,
            phase=phase_r,
            xpath=xpath,
            value=value,
            stb_element=stb_element,
            attr_name=attr_name,
            ref_value=ref_value,
            ref_stb_element=ref_stb_element,
            ref_attr_name=ref_attr_name,
        )


class CompositeReporter(_BaseReporter):
    """複数のReporterへ同じメッセージを送るReporter。

    メモリへの蓄積とログ出力を同時に行う場合などに使用します。

    Args:
        reporters: メッセージを送るReporter。
        default_code: codeのデフォルト。
        default_phase: phaseのデフォルト。
    """

    def __init__(
        self,
        reporters: list[Reporter],
        *,
        default_code: Code | None = None,
        default_phase: Phase | None = None,
    ) -> None:
        super().__init__(default_code=default_code, default_phase=default_phase)
        self.reporters = reporters

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
        code_r, phase_r = self._resolve(code, phase)
        for reporter in self.reporters:
            reporter._emit(
                severity,
                message,
                code=code_r,
                phase=phase_r,
                element_guid=element_guid,
                stb_element=stb_element,
                attr_name=attr_name,
                xpath=xpath,
                value=value,
                ref_element_guid=ref_element_guid,
                ref_xpath=ref_xpath,
                ref_value=ref_value,
                ref_stb_element=ref_stb_element,
                ref_attr_name=ref_attr_name,
            )


class NullReporter(Reporter):
    """メッセージを記録しないReporter"""

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
        _ = (
            severity,
            message,
            code,
            phase,
            element_guid,
            xpath,
            value,
            stb_element,
            attr_name,
            ref_element_guid,
            ref_xpath,
            ref_value,
            ref_stb_element,
            ref_attr_name,
        )


def get_reporter(
    logger: Logger | None = None,
    reporter: Reporter | None = None,
) -> Reporter:
    """loggerとreporterの指定から、実際に使用するReporterを決めます。

    - どちらも省略した場合は、stbkitの既定のロガーへ出力するLoggerReporterを作成します。
    - loggerだけを指定した場合は、そのloggerへ出力するLoggerReporterを作成します。
    - reporterだけを指定した場合は、それをそのまま返します。
    - 両方を指定した場合は、reporterが既にそのロガーへ出力していればそのまま返します。
      そうでなければ、両方へ記録するCompositeReporterを返します。
      reporterがCompositeReporterの場合は、そこに追加して返します。

    Args:
        logger: 出力するLogger。
        reporter: 出力するReporter。

    Returns:
        Reporter: 実際に使用するReporter。
    """

    def has_logger(rep: Reporter, target: Logger) -> bool:
        if isinstance(rep, LoggerReporter):
            return rep.logger == target
        if isinstance(rep, CompositeReporter):
            return any(has_logger(r, target) for r in rep.reporters)
        return False

    if reporter is None:
        if logger is None:
            logger = get_logger()
        return LoggerReporter(logger=logger)
    else:
        if logger is not None:
            if has_logger(reporter, logger):
                return reporter
            logger_reporter = LoggerReporter(logger=logger)
            if isinstance(reporter, CompositeReporter):
                reporter.reporters.append(logger_reporter)
                return reporter
            return CompositeReporter(reporters=[reporter, logger_reporter])
        return reporter
