# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import sys
from argparse import Namespace, _SubParsersAction
from pathlib import Path
from typing import Any

from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_io import load, loads
from stbkit.core.stb_reporting import CollectingReporter

from stbkit.tools._internal.data_model.summary import StbSummary, get_summary

from . import common
from .constants_exit_code import EXIT_EXECUTION_ERROR, EXIT_INVALID_ARGUMENT, EXIT_OK
from .global_parent import get_max_size, make_global_parent


def register(subparsers: _SubParsersAction[Any]) -> None:
    parser = subparsers.add_parser(
        "summary",
        parents=[make_global_parent()],
        help="ST-Bridgeの概要を出力します。",
    )
    common.use_input(parser)
    parser.add_argument(
        "--output-format",
        choices=("text", "json"),
        default="text",
        help="出力フォーマット。textまたはjsonを指定します。",
    )
    parser.set_defaults(func=_run)


def _run(args: Namespace) -> None:
    input_path: str = common.get_input(args)
    max_size: int = get_max_size(args)
    output_format: str = str(args.output_format)
    verbose: int = int(args.verbose) if hasattr(args, "verbose") else 0

    try:
        reporter: CollectingReporter = CollectingReporter()
        if input_path == "-":
            stb: StBridgeRoot = loads(
                common.read_stdin_xml(max_size=max_size),
                max_size=max_size,
                reporter=reporter,
            )
        else:
            path: Path = Path(input_path)
            if not path.is_file():
                raise FileNotFoundError(f"入力ファイルが見つかりません: {path}")
            stb = load(path, max_size=max_size, reporter=reporter)
        summary: StbSummary = get_summary(stb, reporter=reporter)
        if output_format == "json":
            output_str: str = summary.to_json(indent=2)
        else:
            output_str = summary.to_text(verbose=verbose)
        sys.stdout.write(output_str)
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(EXIT_INVALID_ARGUMENT) from None
    except Exception as error:  # noqa: BLE001
        print(f"summaryの作成に失敗しました: {error}", file=sys.stderr)
        raise SystemExit(EXIT_EXECUTION_ERROR) from None

    raise SystemExit(EXIT_OK)
