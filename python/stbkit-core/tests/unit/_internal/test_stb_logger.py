# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import logging
from io import StringIO
from pathlib import Path
from typing import Any

import pytest

from stbkit.core._internal.stb_logger import get_logger


def test_logger_no_args(capsys: pytest.CaptureFixture[str]) -> None:
    logger: logging.Logger = get_logger(level=logging.INFO)
    logger.error("test error")
    logger.warning("test warning")
    logger.info("test info")

    captured: Any = capsys.readouterr()
    assert "E:test error" in captured.err
    assert "W:test warning" in captured.err
    assert "I:test info" in captured.err


def test_logger_with_file_path(
    capsys: pytest.CaptureFixture[str], tmp_path: Path
) -> None:
    log_file: Path = tmp_path / "test.log"
    logger: logging.Logger = get_logger(file=str(log_file), level=logging.INFO)
    logger.error("test error")
    logger.warning("test warning")
    logger.info("test info")

    with open(log_file) as f:
        content: str = f.read()
        assert "E:test error" in content
        assert "W:test warning" in content
        assert "I:test info" in content
    captured: Any = capsys.readouterr()
    assert "E:test error" not in captured.err
    assert "W:test warning" not in captured.err
    assert "I:test info" not in captured.err


def test_logger_with_file_pointer(capsys: pytest.CaptureFixture[str]) -> None:
    file_pointer: StringIO = StringIO()
    logger: logging.Logger = get_logger(file=file_pointer, level=logging.INFO)
    logger.error("test error")
    logger.warning("test warning")
    logger.info("test info")

    content: str = file_pointer.getvalue()
    assert "E:test error" in content
    assert "W:test warning" in content
    assert "I:test info" in content

    captured: Any = capsys.readouterr()
    assert "E:test error" not in captured.err
    assert "W:test warning" not in captured.err
    assert "I:test info" not in captured.err


def test_logger_no_output(capsys: pytest.CaptureFixture[str]) -> None:
    logger: logging.Logger = get_logger(silent=True, level=logging.INFO)
    logger.error("test error")
    logger.warning("test warning")
    logger.info("test info")

    captured: Any = capsys.readouterr()
    assert "E:test error" not in captured.err
    assert "W:test warning" not in captured.err
    assert "I:test info" not in captured.err


def test_logger_with_true(capsys: pytest.CaptureFixture[str]) -> None:
    logger: logging.Logger = get_logger(level=logging.INFO)
    logger.error("test error")
    logger.warning("test warning")
    logger.info("test info")

    captured: Any = capsys.readouterr()
    assert "E:test error" in captured.err
    assert "W:test warning" in captured.err
    assert "I:test info" in captured.err
