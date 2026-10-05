# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""ST-Bridgeを生成するサンプル

原点からZ方向に3000mmのRC柱を1本作成しします。
矩形断面は600×600mm、コンクリート強度はFc30、通り・階・配筋は作成せず、ST-Bridge2.1.1で保存します。
通り心を作成していないため、節点kindはOTHERにしています。
"""

import argparse
import sys
from pathlib import Path

import stbkit.api
from stbkit.api import stb_v2_1_1

if sys.version_info >= (3, 14):
    from uuid import uuid7 as new_guid
else:
    from uuid import uuid4 as new_guid


def main(output_stb_path: Path) -> None:
    # ST-Bridgeモデルを作成します
    # StbCommonのapp_name,app_versionは必須ですが、dump時に指定するためここでは不要です
    stb = stb_v2_1_1.StBridge(
        version=stb_v2_1_1.VERSION,
        stb_common=stb_v2_1_1.StbCommon(
            project_name="RC柱の作成例",
        ),
    )
    # 単一要素はensureで生成しながら取得できます
    model: stb_v2_1_1.StbModel = stb.ensure.stb_model()
    # ---
    # 節点を作成します
    bottom_node = stb_v2_1_1.StbNode(
        id=1,
        guid=new_guid(),
        x=0.0,
        y=0.0,
        z=0.0,
        # 入力値に制限がある場合はenumが定義されているため利用できます。
        kind=stb_v2_1_1.StbNodeKind.OTHER,
    )
    top_node = stb_v2_1_1.StbNode(
        id=2,
        guid=new_guid(),
        x=0.0,
        y=0.0,
        z=3000.0,
        # 値が制限を満たしていればそのまま文字列で入力することもできます。
        kind="OTHER",
    )
    model.ensure.stb_nodes().stb_node.extend([bottom_node, top_node])
    # ---
    # 断面を作成します
    section = stb_v2_1_1.StbSecColumnRc(
        id=1,
        guid=new_guid(),
        name="C1",
        kind_column=stb_v2_1_1.StbSecColumnRcKindColumn.COLUMN,
        strength_concrete="FC30",
        stb_sec_figure_column_rc=stb_v2_1_1.StbSecFigureColumnRc(
            stb_sec_column_rect=stb_v2_1_1.StbSecColumnRect(
                width_x=600.0, width_y=600.0
            )
        ),
    )
    model.ensure.stb_sections().stb_sec_column_rc.append(section)

    # ---
    # RC柱を作成します
    column = stb_v2_1_1.StbColumn(
        id=1,
        guid=new_guid(),
        name="C1",
        id_node_bottom=bottom_node.id,
        id_node_top=top_node.id,
        id_section=section.id,
        kind_structure=stb_v2_1_1.StbColumnKindStructure.RC,
        rotate=0.0,
    )
    # リストは空リストで初期化されているため、ensureは不要でappendで要素を追加します。
    model.ensure.stb_members().ensure.stb_columns().stb_column.append(column)

    with open(output_stb_path, "x", encoding="utf-8") as fp:
        stbkit.api.dump(
            stb, fp, app_name="stbkit-examples-create-stb-column", app_version="1.0"
        )


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_stb_path", type=Path, help="ST-Bridgeファイル")
    main(**vars(parser.parse_args()))
