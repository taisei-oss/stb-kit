# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""ST-Bridgeを読み込む関数の違いを確認するサンプル

- load: ファイルをそのversionのまま読み込みます。versionに対応した型になります。
- loads: XML文字列をそのversionのまま読み込みます。versionに対応した型になります。
- load_latest: ファイルを読み込み、最新版のデータモデルに変換します。
- loads_latest: XML文字列を読み込み、最新版のデータモデルに変換します。

load, loadsの場合はversionによって型が変わるため、
処理する際はバージョンごとに分岐が必要です。
末尾が_latestの関数は、最新版になるため、バージョンごとの分岐は不要です。
ただし、最新版への変換実装は開発中のため、全ての要素や属性が正しく更新されるとは限りません。
（現状のv2.0.2からv2.1.0の変換実装は外形形状中心です）
"""

import argparse
from pathlib import Path
from typing import Final

import stbkit.api
from stbkit.api import StBridgeRoot, stb_latest

STB_TEXT: Final = """<?xml version="1.0" encoding="UTF-8"?>
<ST_BRIDGE
 xmlns:xs="http://www.w3.org/2001/XMLSchema"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns="https://www.building-smart.or.jp/dl"
 version="2.0.2">
 <StbCommon project_name="sample load" app_name="stbkit" app_version="0.0.0"/>
 <StbModel/>
</ST_BRIDGE>
"""


def print_model(label: str, stb: StBridgeRoot) -> None:
    """読み込んだルート要素の型とバージョンを表示する。"""

    print(f"{label}:")
    print(f"  型: {type(stb).__module__}.{type(stb).__name__}")
    print(f"  ST-Bridgeバージョン: {stb.version}")


def main(stb_path: Path) -> None:
    """ST-Bridgeファイルをload, loads, load_latest, loads_latestで読み込む"""

    # ファイルから読み込む
    stb_from_file: StBridgeRoot = stbkit.api.load(stb_path)
    print_model("load", stb_from_file)

    # XML文字列から読み込む
    stb_from_text: StBridgeRoot = stbkit.api.loads(STB_TEXT)
    print_model("loads", stb_from_text)

    # ファイルから読み込んだ後に最新版に更新する
    # ファイルのバージョンによらず型が一定になり、バージョンごとの分岐が不要になる。
    latest_from_file: stb_latest.StBridge = stbkit.api.load_latest(stb_path)
    print_model("load_latest", latest_from_file)

    # loadsのlatest版
    latest_from_text: stb_latest.StBridge = stbkit.api.loads_latest(STB_TEXT)
    print_model("loads_latest", latest_from_text)


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stb_path", type=Path, help="ST-Bridgeファイル")
    main(**vars(parser.parse_args()))
