# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass
from difflib import unified_diff


@dataclass(frozen=True, kw_only=True)
class CompareResult:
    """テキストファイル比較の結果

    Attributes:
        equal (bool): 一致ならTrue
        reason (str | None): 不一致理由（一致ならNone）
    """

    equal: bool
    reason: str | None = None
    formated_actual: str | None = None
    formated_expected: str | None = None
    diff: str | None = None

    def get_diff(self) -> str | None:
        """差分を取得する。

        Returns:
            str | None: 差分文字列。差分がない場合はNone。
        """
        if self.equal:
            return None
        if self.diff is not None:
            return self.diff
        if self.formated_actual is not None and self.formated_expected is not None:
            return "\n".join(
                unified_diff(
                    self.formated_expected.splitlines(),
                    self.formated_actual.splitlines(),
                    fromfile="expected",
                    tofile="actual",
                    lineterm="",
                )
            )
        return None


class TextComparator:
    def __init__(self, ignore_newlines: bool = True) -> None:
        self.ignore_newlines: bool = ignore_newlines

    def compare(
        self,
        expected: str,
        actual: str,
    ) -> CompareResult:

        result: bool = True
        if expected == actual:
            return CompareResult(equal=result)
        formatted_lines_expected: list[str] = expected.splitlines()
        formatted_lines_actual: list[str] = actual.splitlines()
        if self.ignore_newlines and len(formatted_lines_expected) == len(
            formatted_lines_actual
        ):
            for line_expected, line_actual in zip(
                formatted_lines_expected, formatted_lines_actual, strict=True
            ):
                if line_expected.strip() != line_actual.strip():
                    result = False
                    break
        else:
            result = False

        return CompareResult(
            equal=result,
            reason="テキストに不一致行があります",
            formated_actual="\n".join(formatted_lines_actual),
            formated_expected="\n".join(formatted_lines_expected),
        )

    def assert_equal(
        self,
        expected: str,
        actual: str,
        *,
        message: str = "テキストが一致しません",
    ) -> None:
        """2つのテキストが一致することをチェックする。

        Args:
            expected (str): 期待されるテキスト
            actual (str): 実際のテキスト
            message (str): 不一致時のエラーメッセージの先頭行

        Raises:
            AssertionError: テキストが一致しない場合。
        """
        compare_result: CompareResult = self.compare(expected, actual)
        if compare_result.equal:
            return
        raise AssertionError(
            f"{message}:{compare_result.reason}\n"
            f"--- 差分 ---\n{compare_result.get_diff()}"
        )
