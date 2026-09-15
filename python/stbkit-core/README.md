# stbkit-core

ST-Bridgeを扱うためのツールキットのコアライブラリです。  

_A Python core library for handling ST-Bridge._

ST-Bridgeは、日本の建築構造分野で広く利用されている建築構造データ交換フォーマットです。

_ST-Bridge is a structural data exchange format widely used in Japan._

詳細はリポジトリの[README](https://github.com/taisei-oss/stb-kit)および[DISCLAIMER](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md) をご確認ください。

## 概要

stbkit-coreはST-BridgeのXMLデータをPythonから扱うためのライブラリです。

- ST-Bridgeの仕様に準拠したデータ構造
- 不完全な実データを想定した堅牢性

を重視しています。

本パッケージはデータ処理の支援を目的とし、**安全性検証（構造安全性の保証・確認）や法令適合性判定は行いません**。
出力結果の検証、法令順守の確認は利用者の責任です。

## インストール
通常は`stbkit`パッケージ経由で本パッケージをインストールすることを推奨します。

個別にインストールする場合は下記コマンドをご利用ください。

STB-KITは現在ベータ版です。通常のインストールではベータ版が選ばれない場合があるため、次の例では`--pre`を指定します。利用するベータ版の番号が分かっている場合は、`stbkit-core==バージョン番号`のようにバージョンを直接指定することもできます。

```bash
python -m pip install --pre stbkit-core
```

## 使用例

ここでは、stbkit-coreのみを使ったコード例を示していますが、このパッケージ内のAPIは暫定的なものであり、今後変更される可能性があります。
継続的に利用するコードから使う場合は、この点を了解したうえで、バージョンを固定して使用してください。
互換性に関する方針は、GitHubリポジトリの[COMPATIBILITY](https://github.com/taisei-oss/stb-kit/blob/main/COMPATIBILITY.md)を参照してください。

### ST-Bridgeファイルの節点データを表示する

```python
import stbkit.core

stb = stbkit.core.stb_io.load("example.stb")

for node in stb.stb_model.stb_nodes.stb_node:
    print(f"{node.id}, {node.x}, {node.y}, {node.z}")
```

## ドキュメント

ドキュメントは現在準備中です。公開時にこちらへリンクを掲載します。

- ユーザーガイド（準備中）
- APIリファレンス（準備中）

## バリデーション

XML スキーマによるバリデーションを行う場合、xmlschema パッケージのインストールが必要です。
下記コマンドでxmlschemaもインストールされます。
```bash
python -m pip install --pre "stbkit-core[full]"
```

依存パッケージがない場合でも、型、必須項目等の簡易的な確認は行えます。

## ライセンス
本プロジェクトのソースコードは **Mozilla Public License 2.0 (MPL-2.0)** のもとで提供されます。

- MPL-2.0 はファイル単位のコピーレフトライセンスです。
- 本プロジェクトの改変部分（該当ファイル）を再配布する場合、ソース公開義務が発生します。
- 本ライブラリを利用するアプリケーションはOSSである必要はありません

実務利用とオープンな改善の両立を意図したライセンスです。

## 依存パッケージ（間接依存を除く）
### オプション
- **xmlschema**(MIT): XSDを利用したバリデーションに利用

## 免責（重要）

本ソフトウェアは現状有姿で提供され、いかなる保証もありません。
詳細はリポジトリの[DISCLAIMER](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md)を参照してください。

Copyright 2026 TAISEI CORPORATION
