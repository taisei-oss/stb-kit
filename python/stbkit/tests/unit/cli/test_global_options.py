# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from argparse import ArgumentParser, Namespace

from stbkit.core._internal.constants import BYTES_PER_MB, DEFAULT_MAX_XML_SIZE

from stbkit.cli._internal import converter
from stbkit.cli._internal.cli_main import SubcommandHelpArgumentParser
from stbkit.cli._internal.global_parent import (
    get_interactive,
    get_max_size,
    make_global_parent,
)


def _tmp_parser() -> ArgumentParser:
    parser: ArgumentParser = SubcommandHelpArgumentParser(
        prog="stbkit", parents=[make_global_parent()]
    )
    subparsers = parser.add_subparsers(dest="command")
    converter.register(subparsers)
    return parser


def test_cli_parser_verbose() -> None:
    parser: ArgumentParser = _tmp_parser()

    before: Namespace = parser.parse_args(["-vv", "convert", "--list-formats"])
    after: Namespace = parser.parse_args(["convert", "--list-formats", "-vv"])
    default: Namespace = parser.parse_args(["convert", "--list-formats"])

    assert getattr(before, "verbose", 0) == 2
    assert getattr(after, "verbose", 0) == 2
    assert getattr(default, "verbose", 0) == 0


def test_cli_parser_version() -> None:
    parser: ArgumentParser = _tmp_parser()

    before: Namespace = parser.parse_args(["-V", "convert", "--list-formats"])
    after: Namespace = parser.parse_args(["convert", "--list-formats", "-V"])
    default: Namespace = parser.parse_args(["convert", "--list-formats"])

    assert getattr(before, "version", False)
    assert getattr(after, "version", False)
    assert not getattr(default, "version", False)


def test_cli_parser_interactive() -> None:
    parser: ArgumentParser = _tmp_parser()

    before: Namespace = parser.parse_args(
        ["--interactive", "convert", "--list-formats"]
    )
    after: Namespace = parser.parse_args(["convert", "--list-formats", "--interactive"])
    default: Namespace = parser.parse_args(["convert", "--list-formats"])

    assert get_interactive(before)
    assert get_interactive(after)
    assert not get_interactive(default)


def test_cli_parser_max_size() -> None:
    parser: ArgumentParser = _tmp_parser()

    before: Namespace = parser.parse_args(
        ["--max-size-mb", "5", "convert", "--list-formats"]
    )
    after: Namespace = parser.parse_args(
        ["convert", "--list-formats", "--max-size-mb", "5"]
    )
    default: Namespace = parser.parse_args(["convert", "--list-formats"])

    assert get_max_size(before) == get_max_size(after) == 5 * BYTES_PER_MB
    assert get_max_size(default) == DEFAULT_MAX_XML_SIZE
