# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""ST-BridgeからIFCへの変換(外形形状のみ)を行うサンプル

実行にはifcopenshellが必要です。
インストールされていない場合は、以下のコマンドでインストールしてください。
pip install ifcopenshell
または
pip install stbkit[ifc]
"""

import argparse
from pathlib import Path

import ifcopenshell.file
import stbkit.api
from stbkit.api.stb_latest import StBridge


def main(stb_path: Path, ifc_path: Path) -> None:
    stb: StBridge = stbkit.api.load_latest(stb_path)
    ifc: ifcopenshell.file = stbkit.api.to_ifc(stb)
    ifc.write(str(ifc_path))


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="ST-BridgeからIFCへの変換(外形形状のみ)を行うサンプル。"
    )
    parser.add_argument("stb_path", type=Path, help="読み込むST-Bridgeファイル")
    parser.add_argument("ifc_path", type=Path, help="書き出すIFCファイル")
    main(**vars(parser.parse_args()))
