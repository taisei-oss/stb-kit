# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

import pytest
from stbkit.core import stb_io
from stbkit.core._internal.constants import LATEST_STB_VERSION
from stbkit.core.stb_reporting import NullReporter
from stbkit.testutils.cli import run_stbkit_cli

from stbkit.cli._internal.constants_exit_code import EXIT_INVALID_ARGUMENT, EXIT_OK
from stbkit.cli._internal.converter import (
    _CLI_FORMAT_SPECS,
    _CLI_ROUTE_SPECS,
    _get_pipeline_format,
    _get_route_formats,
    _get_save_intermediate,
)
from stbkit.tools.converters._internal.pipeline.data import _DataFormatSet
from stbkit.tools.converters._internal.pipeline.execution import get_step


def _fixture_path() -> Path:
    return Path("tests/fixtures/cases/column_s/column_s.stb_v2_0_2.stb")


def test_get_save_intermediate() -> None:
    assert _get_save_intermediate("stb, ifc=result.ifc") == {
        "stb": None,
        "ifc": "result.ifc",
    }
    assert _get_save_intermediate("stb=aaa.stb, ifc=result.ifc") == {
        "stb": "aaa.stb",
        "ifc": "result.ifc",
    }


def test_all_format_aliases_can_get() -> None:
    for spec in _CLI_FORMAT_SPECS:
        for alias in spec.aliases:
            assert _get_pipeline_format(alias, for_output=False) is not None
            assert _get_pipeline_format(alias, for_output=True) is not None


def test_all_help_routes_can_get_step() -> None:
    for route in _CLI_ROUTE_SPECS:
        input_format: _DataFormatSet | None = _get_pipeline_format(
            route.from_format,
            for_output=False,
        )
        output_format: _DataFormatSet | None = _get_pipeline_format(
            route.to_format,
            for_output=True,
        )
        assert input_format is not None
        assert output_format is not None

        get_step(
            input_format,
            output_format,
            route_formats=_get_route_formats(",".join(route.via)),
        )


def test_cli_convert_list_formats(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert run_stbkit_cli(monkeypatch, "convert", "--list-formats") == EXIT_OK

    output = capsys.readouterr().out
    assert "ST-Bridge" in output
    assert "IFC" in output
    assert "PLY" in output
    for route in _CLI_ROUTE_SPECS:
        assert route.command_example in output


def test_cli_convert_only_extensions(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    output_path = tmp_path / "column.ply"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(_fixture_path()),
            "-o",
            str(output_path),
            "--yes",
        )
        == EXIT_OK
    )
    assert output_path.read_text(encoding="utf-8").startswith("ply\nformat ascii 1.0\n")


def test_cli_convert_writes_intermediate_latest_stb(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    output_path: Path = tmp_path / "column.ply"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(_fixture_path()),
            "-o",
            str(output_path),
            "--save-intermediate",
            "stb",
            "--yes",
        )
        == EXIT_OK
    )

    intermediate_path: Path = Path(f"{output_path}.stb")
    assert intermediate_path.is_file()
    assert (
        stb_io.load(intermediate_path, reporter=NullReporter()).version
        == LATEST_STB_VERSION
    )


def test_cli_convert_uses_stdin_and_stdout(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    stdin: str = _fixture_path().read_text(encoding="utf-8")

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            "-",
            "--from",
            "stb-2.0.2",
            "--to",
            "stb-2.1.0",
            stdin=stdin,
        )
        == EXIT_OK
    )

    output: str = capsys.readouterr().out
    assert stb_io.loads(output, reporter=NullReporter()).version == "2.1.0"


def test_cli_convert_does_not_overwrite_without_yes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_path: Path = tmp_path / "column.ply"
    output_path.write_text("keep", encoding="utf-8")

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(_fixture_path()),
            "-o",
            str(output_path),
            stdin="n\n",
        )
        == EXIT_INVALID_ARGUMENT
    )
    assert output_path.read_text(encoding="utf-8") == "keep"
    assert "-y/--yesの指定" in capsys.readouterr().err


def test_cli_convert_requires_yes_when_stdin_input_and_output_exists(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_path: Path = tmp_path / "existing.stb"
    output_path.write_text("keep", encoding="utf-8")
    stdin: str = _fixture_path().read_text(encoding="utf-8")

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            "-",
            "--from",
            "stb-2.0.2",
            "--to",
            "stb-2.1.1",
            "-o",
            str(output_path),
            stdin=stdin,
        )
        == EXIT_INVALID_ARGUMENT
    )

    assert output_path.read_text(encoding="utf-8") == "keep"
    assert "-y/--yesの指定" in capsys.readouterr().err


def test_cli_convert_intermediate_output_path_same_to_input(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    input_path: Path = tmp_path / "input.stb"
    input_path.write_text(_fixture_path().read_text(encoding="utf-8"), encoding="utf-8")
    original: str = input_path.read_text(encoding="utf-8")
    output_path: Path = tmp_path / "output.ply"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(input_path),
            "-o",
            str(output_path),
            "--save-intermediate",
            f"stb={input_path}",
            "--yes",
        )
        == EXIT_INVALID_ARGUMENT
    )

    assert input_path.read_text(encoding="utf-8") == original
    assert not output_path.exists()
    assert (
        "入力ファイル・最終出力・中間出力の保存先は重複できません"
        in capsys.readouterr().err
    )


def test_cli_convert_intermediate_output_path_same_to_final_output(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_path: Path = tmp_path / "output.ply"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(_fixture_path()),
            "-o",
            str(output_path),
            "--save-intermediate",
            f"stb={output_path}",
            "--yes",
        )
        == EXIT_INVALID_ARGUMENT
    )

    assert not output_path.exists()
    assert (
        "入力ファイル・最終出力・中間出力の保存先は重複できません"
        in capsys.readouterr().err
    )


def test_cli_convert_same_intermediate_output_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_path = tmp_path / "output.ply"
    duplicate_path = tmp_path / "duplicate.dat"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(_fixture_path()),
            "-o",
            str(output_path),
            "--save-intermediate",
            f"stb={duplicate_path},ifc={duplicate_path}",
            "--yes",
        )
        == EXIT_INVALID_ARGUMENT
    )

    assert not output_path.exists()
    assert (
        "入力ファイル・最終出力・中間出力の保存先は重複できません"
        in capsys.readouterr().err
    )


def test_cli_convert_unsupported_conversion(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_path = tmp_path / "result.stb"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            "input.ply",
            "-o",
            str(output_path),
            "--from",
            "ply",
            "--to",
            "stb",
        )
        == EXIT_INVALID_ARGUMENT
    )

    captured = capsys.readouterr()
    assert "サポートされない変換です" in captured.err
    assert not output_path.exists()


@pytest.mark.parametrize(
    "to_format",
    [
        "stb-garbage",
        "stb-foo201bar",
        "st-bridge-notlatest-butcontainslatest",
        "stb-99.9.9",
    ],
)
def test_cli_convert_unknown_stb(
    to_format: str,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    output_path: Path = tmp_path / "result.stb"

    assert (
        run_stbkit_cli(
            monkeypatch,
            "convert",
            str(_fixture_path()),
            "-o",
            str(output_path),
            "--to",
            to_format,
            "--yes",
        )
        == EXIT_INVALID_ARGUMENT
    )

    captured = capsys.readouterr()
    assert "サポートされない変換です" in captured.err
