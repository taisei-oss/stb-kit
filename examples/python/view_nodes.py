# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""ST-Bridgeを開き、グリッド上の節点情報を表示するサンプル"""

import argparse
from pathlib import Path

import stbkit.api
from stbkit.api import NoneAccessError
from stbkit.api.stb_latest import StbNode, StbNodeKind, StBridge


def main(stb_path: Path) -> None:
    # load_latestを使うことで、型ヒントが使えるようになる
    stb: StBridge = stbkit.api.load_latest(stb_path)
    # try-exceptでNoneAccessErrorをキャッチすることで、
    # 途中のstb_modelやstb_nodesがNoneの場合のエラーを回避できる
    try:
        node_list: list[StbNode] = stb.stb_model.stb_nodes.stb_node
    except NoneAccessError as e:
        print(e)
        return
    # 値が限られている属性は列挙型を使うことで、補完や型チェックが効くようになります。
    # StrEnum等であるため、文字列で比較することも可能です。
    node_list = [node for node in node_list if node.kind is StbNodeKind.ON_GRID]
    print(f"グリッド上の節点数: {len(node_list)}")
    # 複数要素はリストであるため、for文で回せます。
    for node in node_list:
        print(f"id: {node.id}  x: {node.x}  y: {node.y}  z: {node.z}")


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stb_path", type=Path, help="ST-Bridgeファイル")
    main(**vars(parser.parse_args()))
