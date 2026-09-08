# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import logging
from argparse import Namespace
from logging import Logger

from stbkit.core._internal.constants import BYTES_PER_MB, DEFAULT_MAX_XML_SIZE
from stbkit.core._internal.stb_logger import get_logger as get_stb_logger

DEFAULT_MAX_SIZE_MB: int = DEFAULT_MAX_XML_SIZE // BYTES_PER_MB


def make_global_parent() -> argparse.ArgumentParser:
    # 共通引数に既定値を持たせるとサブコマンドより前で指定した値がサブコマンドで上書きされてしまうため、
    # 共通引数は既定値を持たせず、下のget_xxxを用いる。
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument(
        "-V",
        "--version",
        action="store_true",
        default=argparse.SUPPRESS,
        help="バージョン情報",
    )
    parent.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=argparse.SUPPRESS,
        help="詳細ログを出力する場合に指定します (-v, -vv, -vvv)",
    )
    parent.add_argument(
        "--max-size-mb",
        type=int,
        default=argparse.SUPPRESS,
        help=f"読み込むXMLのサイズ上限(MB)。既定は{DEFAULT_MAX_SIZE_MB}です。",
    )
    parent.add_argument(
        "--interactive",
        action="store_true",
        default=argparse.SUPPRESS,
        help="対話モードで実行します。",
    )

    return parent


def get_max_size(args: Namespace) -> int:
    max_size_mb: int = getattr(args, "max_size_mb", DEFAULT_MAX_SIZE_MB)
    return max_size_mb * BYTES_PER_MB


def get_interactive(args: Namespace) -> bool:
    interactive: bool = getattr(args, "interactive", False)
    return interactive


def get_logger(args: Namespace) -> Logger:
    verbose: int = getattr(args, "verbose", 0)
    if verbose >= 2:
        logging_level = logging.DEBUG
    elif verbose >= 1:
        logging_level = logging.INFO
    else:
        logging_level = logging.WARNING
    return get_stb_logger(level=logging_level)
