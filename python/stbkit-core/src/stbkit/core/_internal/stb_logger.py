# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import io
import logging
import sys
import time
from logging import Logger
from typing import Any, TextIO


def get_logger(
    *,
    logger: Logger | None = None,
    file: str | TextIO | None = None,
    silent: bool = False,
    show_time: bool = False,
    show_elapsed: bool = False,
    name: str = "stb",
    show_name: bool = False,
    separator: str = ":",
    level: int = logging.WARNING,
) -> Logger:
    """
    ロガー、ファイル、標準出力、出力無しのいずれかに対応するLoggerを返す。
    logger: Loggerオブジェクトを指定（優先）
    file: ファイルパス(str)またはファイルオブジェクト(io.TextIOBase)を指定
    silent: Trueなら出力無し（NullHandlerを返す）
    show_time: Trueで時刻を表示
    show_elapsed: Trueで経過時間を表示
    name: ロガー名を指定
    すべて未指定なら標準出力
    """
    log: Logger = logging.getLogger(name)
    log.handlers.clear()
    log.propagate = False

    if silent:
        log.addHandler(logging.NullHandler())
        return log
    if logger is not None:
        return logger

    if file is not None:
        if isinstance(file, str):
            handler: logging.Handler = logging.FileHandler(file)
        elif isinstance(file, io.TextIOBase):
            handler = logging.StreamHandler(file)
        else:
            raise TypeError("fileはstrまたはio.TextIOBaseで指定してください")
    else:
        handler = logging.StreamHandler(sys.stderr)

    # フォーマットの組み立て
    fmt_parts: list[str] = []
    if show_time:
        fmt_parts.append("%(asctime)s")
    if show_elapsed:
        fmt_parts.append("%(elapsed)s")
    fmt_parts.append("%(levelname).1s")
    if show_name:
        fmt_parts.append("%(name)s")

    fmt_parts.append("%(message)s")
    fmt: str = separator.join(fmt_parts)

    class ElapsedFormatter(logging.Formatter):
        def __init__(self, fmt: str):
            super().__init__(fmt)
            self.start_time = time.time()

        def format(self, record: Any) -> str:
            if show_elapsed:
                elapsed = time.time() - self.start_time
                record.elapsed = f"{elapsed:.2f}s"
            else:
                record.elapsed = ""
            return super().format(record)

    handler.setFormatter(ElapsedFormatter(fmt))
    log.addHandler(handler)
    log.setLevel(level=level)
    return log
