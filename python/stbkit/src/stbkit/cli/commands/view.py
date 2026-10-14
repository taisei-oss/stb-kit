# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

from argparse import ArgumentParser, Namespace, _SubParsersAction
from pathlib import Path
from typing import Any

from stbkit.cli._internal.global_parent import (
    get_logger,
    get_max_size,
    make_global_parent,
)


def _run_view(args: Namespace) -> None:
    from stbkit.native import view
    from stbkit.tools._internal.stb_io import load_latest

    path: Path = args.path
    logger = get_logger(args)
    stb = load_latest(path, max_size=get_max_size(args), logger=logger)
    view(stb, logger=logger)


def register(subparsers: _SubParsersAction[Any]) -> None:
    parser: ArgumentParser = subparsers.add_parser(
        "view",
        parents=[make_global_parent()],
        help="ST-Bridgeを3D表示",
    )
    parser.add_argument(
        "path",
        type=Path,
        help="表示するST-Bridgeファイル",
    )
    parser.set_defaults(func=_run_view)
