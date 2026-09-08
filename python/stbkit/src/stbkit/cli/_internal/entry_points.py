# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from importlib import metadata
from typing import Final

COMMAND_GROUP: Final = "stbkit.commands"

# pyproject.tomlの[project.entry-points."stbkit.commands"]に該当。
# 将来的にpackageを分離した際にpyproject.tomlへ書けるように、この形式で登録する。
BUILTIN_COMMANDS: Final[dict[str, str]] = {
    "convert": "stbkit.cli.commands.convert:register",
    "diff": "stbkit.cli.commands.diff:register",
    "validate": "stbkit.cli.commands.validate:register",
}


def load_command_entry_points() -> metadata.EntryPoints:
    return metadata.EntryPoints(
        metadata.EntryPoint(name=name, value=value, group=COMMAND_GROUP)
        for name, value in sorted(BUILTIN_COMMANDS.items())
    )
