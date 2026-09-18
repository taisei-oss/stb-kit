# 対応バージョン・形式

## ST-Bridge

| バージョン | 読み込み | 書き出し | 最新版への変換 |
| --- | --- | --- | --- |
| 2.0.0 | 対応 | 対応 | 対応 |
| 2.0.1 | 対応 | 対応 | 対応 |
| 2.0.2 | 対応 | 対応 | 対応 |
| 2.1.0 | 対応 | 対応 | 対応 |
| 2.1.1 | 対応 | 対応 | 最新版 |

データモデルのstb_latestはstb_v2_1_1へのエイリアスです。

## フォーマット変換対応形式

`stbkit convert`コマンドで変換できる形式です。

| 入力 | 出力 | 備考 |
| --- | --- | --- |
| ST-Bridge | ST-Bridge | バージョンアップのみ。バージョンダウンは非対応。 |
| ST-Bridge | IFC | 依存のifcopenshellが必要 |
| ST-Bridge | PLY | ST-Bridgeを直接変換、IFC経由で変換が選べます。 |

実行可能な変換は`stbkit convert --list-formats`で確認できます。

ST-Bridgeのバージョンアップは`stbkit upgrade`コマンドでも可能です。（エイリアス）

> **IFC変換の対応範囲**
>
> IFC変換はST-Bridgeの主要要素の外形形状を中心に対応しています。
> 配筋、詳細属性および一部要素は変換されません。
> 詳細は[ST-BridgeからIFCへの変換仕様](../technical/stb-ifc-conversion.md)を参照してください。

Copyright 2026 TAISEI CORPORATION
