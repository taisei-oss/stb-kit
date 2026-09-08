# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""
STB-KITの例外クラス定義モジュール
"""

from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .data_model.common import StBridgeElement


class StbError(Exception):
    """STB-KITの基本例外クラス"""

    @property
    def path(self) -> str | None:
        """例外の発生箇所を表すXPath。基底クラスでは常にNoneです。"""
        return None


class NoneAccessError(StbError, AttributeError):
    """アクセスした属性がNoneである例外

    通常プロパティは値がNoneのときにこの例外を投げます。
    Noneを許容して取得する場合は_or_noneプロパティを使用します。

    Args:
        element: アクセスされた要素。
        attr_name: アクセスされた属性名(Pythonでの名前)。
    """

    def __init__(self, *, element: StBridgeElement, attr_name: str) -> None:
        self._class_name: str = element._name_for_log(attr_name)
        self._path: str = element._path_xml(attr_name)

    def __str__(self) -> str:
        return f"{self._class_name}がNoneであるためアクセスできません\npath:{self.path}"

    @property
    def path(self) -> str | None:
        return self._path


class ReferenceElementNotFoundError(StbError):
    """参照先の要素が見つからない場合の例外

    id_nodeやid_sectionなどの参照解決時に要素が見つからなかったときに投げます
    """


class SchemaError(StbError):
    """ST-Bridgeのスキーマ違反の例外

    Args:
        message: 違反の内容。
        element: 違反が見つかった要素。
        attr_name: 違反が見つかった属性名(Pythonでの名前)。
    """

    def __init__(
        self,
        message: str,
        *,
        element: StBridgeElement | None = None,
        attr_name: str | None = None,
    ) -> None:
        self.message: str = message
        self._path: str | None = (
            element._path_xml(attr_name=attr_name) if element else None
        )

    def __str__(self) -> str:
        if self._path:
            return f"{self.message}\npath:{self._path}"
        else:
            return self.message

    @property
    def path(self) -> str | None:
        return self._path


class TypeMismatchError(SchemaError):
    """型の不一致の場合の例外

    Args:
        expected_type: 期待される型。
        actual_type: 実際の型。
        element: 不一致が見つかった要素。
        attr_name: 不一致が見つかった属性名(Pythonでの名前)。
    """

    def __init__(
        self,
        *,
        expected_type: str | type[Any],
        actual_type: str | type[Any],
        element: StBridgeElement | None = None,
        attr_name: str | None = None,
    ) -> None:
        self.expected_type: str = str(expected_type)
        self.actual_type: str = str(actual_type)
        self._path: str | None = (
            element._path_xml(attr_name=attr_name) if element else None
        )

    def __str__(self) -> str:
        if self._path:
            return f"型の不一致: 期待される型 {self.expected_type}, 実際の型 {self.actual_type}\npath:{self._path}"
        else:
            return f"型の不一致: 期待される型 {self.expected_type}, 実際の型 {self.actual_type}"

    @property
    def path(self) -> str | None:
        return self._path


class UnsafeXmlError(StbError):
    """安全でないXML表記を検出した場合の例外

    外部ファイル参照や実体の再帰展開に悪用されうる記述が見つかった場合に投げて拒否します。

    Args:
        reason: 拒否した理由。
    """

    def __init__(self, reason: str) -> None:
        self.reason: str = reason

    def __str__(self) -> str:
        return f"安全でないXMLのため読み込めません: {self.reason}"


class UnsupportedStbVersionError(StbError):
    """stbkitが対応していないST-Bridgeのバージョンを指定された場合の例外

    Args:
        version: 指定されたバージョン文字列。
    """

    def __init__(self, version: str) -> None:
        self.version = version

    def __str__(self) -> str:
        return f"ST-Bridge v{self.version}はサポートしていないバージョンです"


class XmlLimitKind(Enum):
    """XMLの読み込み上限の種類

    Attributes:
        SIZE: 読み込みサイズの上限。
        DEPTH: 要素の階層の上限。
    """

    SIZE = "size"
    DEPTH = "depth"


class XmlLimitExceededError(StbError):
    """XMLのサイズまたは階層が上限を超えた場合の例外

    Args:
        kind: 超過した上限の種類。
        limit: 上限値。
        actual: 実際の値。(不明な場合はNone)
    """

    def __init__(
        self, *, kind: XmlLimitKind, limit: int, actual: int | None = None
    ) -> None:
        self.kind: XmlLimitKind = kind
        self.limit: int = limit
        self.actual: int | None = actual

    def __str__(self) -> str:
        match self.kind:
            case XmlLimitKind.SIZE:
                result = f"XMLのサイズが上限[{self.limit}バイト]を超えています"
            case XmlLimitKind.DEPTH:
                result = f"XMLの階層が上限[{self.limit}]を超えています"
        if self.actual is not None:
            result += f" (実際: {self.actual})"
        return result


class ZeroLengthMemberError(StbError):
    """部材長が0である場合の例外

    始点と終点が同じ節点を指すなど、長さが0で形状を生成できないときに投げます。
    """


class DeveloperError(StbError):
    """実装のバグを報告するエラー"""
