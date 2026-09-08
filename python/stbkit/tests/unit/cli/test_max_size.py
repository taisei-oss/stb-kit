# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

import pytest
from stbkit.testutils.cli import run_stbkit_cli

from stbkit.cli._internal.constants_exit_code import EXIT_EXECUTION_ERROR


def _fixture_path() -> Path:
    return Path("tests/fixtures/cases/column_s/column_s.stb_v2_0_2.stb")


def test_cli_convert_oversized_input(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(_fixture_path()),
            "--output",
            str(tmp_path / "output.stb"),
            "--to",
            "stb-2.1.0",
            "--yes",
            "--max-size-mb",
            "0",
        )
        == EXIT_EXECUTION_ERROR
    )
    assert "入力ファイルを処理できません" in capsys.readouterr().err


def test_cli_validate_oversized_input(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    schema_path: Path = tmp_path / "schema.xsd"
    schema_path.write_text("<xs:schema xmlns:xs='http://www.w3.org/2001/XMLSchema' />")

    assert (
        run_stbkit_cli(
            monkeypatch,
            "validate",
            str(_fixture_path()),
            "--schema",
            str(schema_path),
            "--max-size-mb",
            "0",
        )
        == EXIT_EXECUTION_ERROR
    )
    assert "入力ファイルを処理できません" in capsys.readouterr().err


def test_cli_diff_xml_oversized_input(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert (
        run_stbkit_cli(
            monkeypatch,
            "diff",
            "--max-size-mb",
            "0",
            "xml",
            str(_fixture_path()),
            str(_fixture_path()),
        )
        == EXIT_EXECUTION_ERROR
    )
    assert "XML比較に失敗しました" in capsys.readouterr().err
