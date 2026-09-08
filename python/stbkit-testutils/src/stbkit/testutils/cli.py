# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import io
import sys

import pytest
from stbkit.cli._internal import cli_main


def prepare_stbkit_cli(
    monkeypatch: pytest.MonkeyPatch,
    *argv: str,
    stdin: str | bytes = "",
) -> None:
    """CLI実行に必要なargv,stdinを設定する"""
    monkeypatch.setattr(sys, "argv", ["stbkit", *argv])

    if isinstance(stdin, bytes):
        monkeypatch.setattr(
            sys,
            "stdin",
            io.TextIOWrapper(io.BytesIO(stdin), encoding="utf-8"),
        )
    else:
        monkeypatch.setattr(sys, "stdin", io.StringIO(stdin))


def run_stbkit_cli(
    monkeypatch: pytest.MonkeyPatch,
    *argv: str,
    stdin: str | bytes = "",
) -> int:
    """CLIを実行して終了コードを返す"""
    prepare_stbkit_cli(
        monkeypatch,
        *argv,
        stdin=stdin,
    )

    with pytest.raises(SystemExit) as error:
        cli_main.main()
    return int(error.value.code or 0)
