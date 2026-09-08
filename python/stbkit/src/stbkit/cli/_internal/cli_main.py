# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import sys
import traceback
from argparse import ArgumentParser, Namespace, _SubParsersAction
from importlib import metadata
from typing import Any, Never

from .constants_exit_code import (
    EXIT_EXECUTION_ERROR,
    EXIT_INTERRUPTED,
    EXIT_INVALID_ARGUMENT,
)
from .entry_points import load_command_entry_points
from .global_parent import make_global_parent


class SubcommandHelpArgumentParser(ArgumentParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.subparsers_action: _SubParsersAction[ArgumentParser] | None = None

    def add_subparsers(self, *args: Any, **kwargs: Any) -> _SubParsersAction[Any]:
        self.subparsers_action = super().add_subparsers(*args, **kwargs)
        return self.subparsers_action

    def error(self, message: str) -> Never:
        self._print_message(f"error: {message}\n", sys.stderr)
        if self.subparsers_action:
            for subcmd in self.subparsers_action.choices:
                if subcmd in sys.argv:
                    self.subparsers_action.choices[subcmd].print_help()
                    self.exit(EXIT_INVALID_ARGUMENT)
        self.print_help()
        self.exit(EXIT_INVALID_ARGUMENT)


def main() -> None:
    """stbkitのcliを実行する"""
    try:
        _main()
    # 想定外例外がそのまま投げられると、終了コードが1になるが、
    # 1はバリデーションや比較の結果に利用したいため終了コードを変更する。
    except KeyboardInterrupt:
        # Ctrl+Cによる中断。
        raise SystemExit(EXIT_INTERRUPTED) from None
    except Exception:  # noqa: BLE001
        # 終了コードを変更するための最後の受け皿なので種類を問わずキャッチする。
        traceback.print_exc()
        raise SystemExit(EXIT_EXECUTION_ERROR) from None


def _main() -> None:
    parser: ArgumentParser = SubcommandHelpArgumentParser(
        prog="stbkit", parents=[make_global_parent()]
    )
    subparsers: _SubParsersAction[Any] = parser.add_subparsers(dest="command")
    entry_points: metadata.EntryPoints = load_command_entry_points()

    for entry_point in entry_points:
        register: Any = entry_point.load()
        try:
            register(subparsers)
        except Exception as e:  # noqa: BLE001
            print(
                f"不明なサブコマンドを登録しようとして失敗しました[{entry_point.name}]: {e}",
                file=sys.stderr,
            )

    if ("--interactive" in sys.argv) and (
        len([a for a in sys.argv[1:] if not a.startswith("-")]) == 0
    ):
        subcommands = list(subparsers.choices.keys())
        print("利用可能なサブコマンド:")
        for idx, cmd in enumerate(subcommands, 1):
            print(f"  {idx}: {cmd}")
        while True:
            print("実行するサブコマンドの番号またはコマンド名を入力してください: ")
            choice = input().strip()
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(subcommands):
                    selected = subcommands[idx - 1]
                    break
                else:
                    print("無効な番号です。")
            elif choice in subcommands:
                selected = choice
                break
            else:
                print("無効な入力です。番号またはコマンド名を入力してください。")
        insert_pos = 1
        sys.argv.insert(insert_pos, selected)
        args: Namespace = parser.parse_args()
        # エラーメッセージを拾いやすいように改行を挟む
        print()
    else:
        args = parser.parse_args()

    if getattr(args, "version", False):
        from .show_versions import show_versions

        show_versions(entry_points)
        return
    if getattr(args, "command", None):
        args.func(args)
        return
    parser.print_help()
