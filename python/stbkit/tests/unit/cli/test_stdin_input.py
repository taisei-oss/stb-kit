# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from typing import Final

import pytest
from stbkit.testutils.cli import run_stbkit_cli

from stbkit.cli._internal.constants_exit_code import EXIT_EXECUTION_ERROR, EXIT_OK

XML_SAMPLE: Final = """<?xml version="1.0" encoding="{encoding}"?>
<ST_BRIDGE xmlns="https://www.building-smart.or.jp/dl" version="2.1.0">
 <StbCommon project_name="日本語の物件名" app_name="stbkit" app_version="0.0.0"/>
  <StbModel>
   <StbNodes>
    <StbNode id="1" X="0" Y="0" Z="0" kind="ON_GRID"/>
   </StbNodes>
  </StbModel>
</ST_BRIDGE>"""


def test_cli_validate_reads_stdin_utf8(monkeypatch: pytest.MonkeyPatch) -> None:
    xml: str = XML_SAMPLE.format(encoding="UTF-8")
    assert (
        run_stbkit_cli(
            monkeypatch,
            "validate",
            "-",
            stdin=xml.encode("utf-8"),
        )
        == EXIT_OK
    )


def test_cli_validate_reads_stdin_shift_jis(monkeypatch: pytest.MonkeyPatch) -> None:
    xml: str = XML_SAMPLE.format(encoding="Shift_JIS")

    assert (
        run_stbkit_cli(
            monkeypatch,
            "validate",
            "-",
            stdin=xml.encode("cp932"),
        )
        == EXIT_OK
    )


def test_cli_validate_reads_stdin_utf8_bom(monkeypatch: pytest.MonkeyPatch) -> None:
    xml: str = XML_SAMPLE.format(encoding="UTF-8")

    assert (
        run_stbkit_cli(
            monkeypatch,
            "validate",
            "-",
            stdin=b"\xef\xbb\xbf" + xml.encode("utf-8"),
        )
        == EXIT_OK
    )


def test_cli_validate_read_broken_xml(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    assert (
        run_stbkit_cli(
            monkeypatch,
            "validate",
            "-",
            stdin=b"broken xml",
        )
        == EXIT_EXECUTION_ERROR
    )
    assert "入力ファイルを処理できません" in capsys.readouterr().err


def test_cli_validate_stdin_oversized(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    xml: str = XML_SAMPLE.format(encoding="UTF-8")

    assert (
        run_stbkit_cli(
            monkeypatch,
            "validate",
            "-",
            "--max-size-mb",
            "0",
            stdin=xml.encode("utf-8"),
        )
        == EXIT_EXECUTION_ERROR
    )
    assert "XMLのサイズが上限" in capsys.readouterr().err


def test_cli_convert_stdin_shift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    xml: str = XML_SAMPLE.format(encoding="Shift_JIS")
    output_path: Path = tmp_path / "result.stb"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            "-",
            "--from",
            "stb",
            "--to",
            "stb-2.1.0",
            "-o",
            str(output_path),
            "--yes",
            stdin=xml.encode("cp932"),
        )
        == EXIT_OK
    )
    assert 'project_name="日本語の物件名"' in output_path.read_text(encoding="utf-8")
