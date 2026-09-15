# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import sys
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from pathlib import Path
from typing import IO

from stbkit.core.stb_exceptions import XmlLimitExceededError, XmlLimitKind
from stbkit.core.stb_io._internal.loader import _detect_encoding

from stbkit.tools._internal.utils.atomic_writer import (
    write_text_with_temp_file as _write_text_via_temporary_file,
)

from .global_parent import get_interactive


def use_input(parser: ArgumentParser) -> None:
    parser.add_argument(
        "input", nargs="?", help="入力ファイルのパス。-で標準入力を使用します。"
    )


def read_stdin_xml(*, max_size: int, encoding: str | None = None) -> str:
    # 端末のエンコーディング設定だとST-Bridgeに記載のencodingを読めないため、
    # bytesとして受け取り、XML宣言から判定する。
    # encodingを明示した場合は判定より優先する。
    buffer: IO[bytes] | None = getattr(sys.stdin, "buffer", None)
    if buffer is None:
        text: str = sys.stdin.read(max_size + 1)
        if len(text) > max_size:
            raise XmlLimitExceededError(kind=XmlLimitKind.SIZE, limit=max_size)
        return text

    raw: bytes = buffer.read(max_size + 1)
    if len(raw) > max_size:
        raise XmlLimitExceededError(kind=XmlLimitKind.SIZE, limit=max_size)
    return raw.decode(encoding or _detect_encoding(raw))


def get_input(args: Namespace) -> str:
    interactive: bool = get_interactive(args)
    input_path: str = args.input
    if not input_path and interactive:
        print("入力ファイルパスを入力してください: ")
        input_path = input().strip()
    if not input_path:
        input_path = "-"
    return input_path


def use_output(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-o",
        "--output",
        default="-",
        help="出力ファイルのパス。-で標準出力を使用します。",
    )


def get_output(args: Namespace) -> str:
    interactive: bool = get_interactive(args)
    output_path: str = args.output
    if not output_path and interactive:
        print("出力ファイルパスを入力してください: ")
        output_path = input().strip()
    if not output_path:
        output_path = "-"
    return output_path


def use_yes(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-y", "--yes", action="store_true", help="確認なしで上書きします。"
    )


def get_yes(args: Namespace) -> bool:
    yes: bool = args.yes
    return yes


def use_quiet(parser: ArgumentParser) -> None:
    parser.add_argument("--quiet", action="store_true", help="エラーのみを表示します。")


def get_quiet(args: Namespace) -> bool:
    quiet: bool = args.quiet
    return quiet


def ensure_output_not_input(output: str, input_paths: Sequence[Path]) -> None:
    if output == "-":
        return

    output_path = Path(output).resolve()
    for input_path in input_paths:
        resolved_input = input_path.resolve()
        is_same_resolved_path = output_path == resolved_input
        is_same_file = output_path.exists() and output_path.samefile(resolved_input)
        if is_same_resolved_path or is_same_file:
            raise ValueError("出力先に入力ファイルは指定できません。")


def confirm_overwrite(*, output: str, yes: bool, interactive: bool) -> bool:
    if output == "-":
        return True

    output_path = Path(output)
    if not output_path.exists() or yes:
        return True
    if not interactive:
        return False

    response = input(f"{output_path}は既に存在します。上書きしますか？(y/N):")
    return response.strip().casefold() in {"y", "yes"}


def write_text_via_temporary_file(
    *, output: str, text: str, encoding: str = "utf-8"
) -> None:
    _write_text_via_temporary_file(Path(output), text, encoding=encoding)
