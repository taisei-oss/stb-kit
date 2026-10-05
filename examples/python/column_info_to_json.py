# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""柱情報の読み込みサンプル

ST-Bridge2.0.2から、柱のID・名称・断面名・上下端節点のZ座標をJSONに出力します。
取得できなかった柱はエラー一覧に残します。
"""

import argparse
import json
from pathlib import Path

import stbkit.api
import stbkit.api.experimental
from stbkit.api import NoneAccessError, StBridgeRoot, stb_v2_0_2
from stbkit.api.experimental import CollectingReporter, ReferenceElementNotFoundError


def main(stb_path: Path, output_path: Path) -> None:
    # エラーメッセージ等を収集する場合はCollectingReporterを利用します。
    reporter: CollectingReporter = CollectingReporter()
    # 通常の読み込みの場合は戻り値の型注釈は基底クラスですが、
    # 実体は入力バージョンのクラスです
    stb: StBridgeRoot = stbkit.api.load(stb_path, reporter=reporter)
    # バージョンにより要素名や属性名が異なるため、バージョンを判定します。
    if not isinstance(stb, stb_v2_0_2.StBridge):
        raise ValueError(
            "このサンプルはST-Bridge2.0.2用です。入力バージョンに対応する処理を使ってください。"
        )

    # リポジトリは参照解決を行えるクラスです。
    # get_repositoryでバージョン対応のリポジトリ
    # (ここではstbkit.api.experimental.repository.RepositoryV2_0_2)が取得できます。
    repo = stbkit.api.experimental.get_repository(stb)

    column_info: list[dict[str, object]] = []
    errors: list[dict[str, object]] = []

    # 柱リストを取得します。
    # 途中にNoneが含まれる可能性がある場合、NoneAccessErrorで例外処理できます。
    try:
        columns: list[stb_v2_0_2.StbColumn] = (
            stb.stb_model.stb_members.stb_columns.stb_column
        )
    except NoneAccessError as e:
        columns = []
        errors.append({"error": str(e)})

    for column in columns:
        try:
            # repo.derefで参照先を取得するアクセサーが取得できます。
            deref = repo.deref(column)
            column_info.append(
                {
                    "id": column.id,
                    "name": column.name,
                    "section_name": deref.id_section.name,
                    "bottom_z_mm": deref.id_node_bottom.z,
                    "top_z_mm": deref.id_node_top.z,
                }
            )
        # 上記で取得するものは必須属性なので基本的には存在するはずですが、
        # なかった場合に備えて例外処理を行います。
        except (stbkit.api.NoneAccessError, ReferenceElementNotFoundError) as e:
            # ここではidがNoneで到達してる可能性もあるので、
            # id_or_noneを使って安全に取得します。
            errors.append({"column_id": column.id_or_none, "error": str(e)})

    result: dict[str, object] = {
        "input": str(stb_path),
        "version": stb.version_or_none,
        "columns": column_info,
        "errors": errors,
        # 記録されたメッセージはlist[dict]形式で取得できます。
        "messages": reporter.report.to_dict(),
    }
    with open(output_path, "x", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stb_path", type=Path, help="ST-Bridgeファイル")
    parser.add_argument("output_path", type=Path, help="出力JSONファイル")
    main(**vars(parser.parse_args()))
