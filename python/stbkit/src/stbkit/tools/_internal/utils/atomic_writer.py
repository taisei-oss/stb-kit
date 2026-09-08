# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import TextIO


def write_with_temp_file(output_path: Path, writer: Callable[[Path], None]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb",
        dir=output_path.parent,
        prefix=f".{output_path.name}.",
        suffix=".tmp",
        delete=False,
    ) as stream:
        temporary_path: Path = Path(stream.name)
    try:
        writer(temporary_path)
        os.replace(temporary_path, output_path)
    finally:
        temporary_path.unlink(missing_ok=True)


def write_text_with_temp_file(
    output_path: Path, text: str, *, encoding: str = "utf-8", newline: str = "\n"
) -> None:
    def _write(temporary_path: Path) -> None:
        with open(temporary_path, "w", encoding=encoding, newline=newline) as stream:
            stream.write(text)

    write_with_temp_file(output_path, _write)


def write_text_stream_with_temp_file(
    output_path: Path,
    writer: Callable[[TextIO], None],
    *,
    encoding: str = "utf-8",
    newline: str = "\n",
) -> None:
    def _write(temporary_path: Path) -> None:
        with open(
            temporary_path,
            "w",
            encoding=encoding,
            newline=newline,
        ) as stream:
            writer(stream)

    write_with_temp_file(output_path, _write)
