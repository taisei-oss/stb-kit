# stbkit

ST-Bridgeを扱うためのツールキットです。  

_An utility library for handling ST-Bridge._

ST-Bridgeは、日本の建築構造分野で広く利用されている建築構造データ交換フォーマットです。

_ST-Bridge is a structural data exchange format widely used in Japan._

詳細はリポジトリの[README](https://github.com/taisei-oss/stb-kit)および[DISCLAIMER](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md)をご確認ください。

## 概要

stbkitはST-Bridgeを扱うためのツールキットSTB-KITの統合パッケージです。  

stbkit-core（データモデル・バリデーション）をコアの依存とし、主に以下の機能を提供します。

- CLIコマンドツール（フォーマット変換、バリデーション、差分検出等）
- PLYへの変換
- IFCへの変換（ifcopenshell利用）

本パッケージは **安全性検証（構造安全性の保証・確認）や法令適合性判定を行いません**。  
出力結果の検証、専門家確認、適用法令の確認は利用者の責任です。

## インストール(最小構成)

STB-KITは現在アルファ版です。通常のインストールではアルファ版が選ばれない場合があるため、次の例では`--pre`を指定します。利用するアルファ版の番号が分かっている場合は、`stbkit==バージョン番号`のようにバージョンを直接指定することもできます。

```bash
python -m pip install --pre stbkit
```

## オプション依存について

- `ifc` : IFC関連の処理を利用する場合に必要です。  
  例）IFC形式への変換など  
  インストール方法：
  ```bash
  python -m pip install --pre "stbkit[ifc]"
  ```
  ※300MB程度のディスク容量が必要です
- `xsd` : XSDによるスキーマ検証を利用する場合に必要です。  
  例）`stbkit validate --schema` の指定など  
  インストール方法：
  ```bash
  python -m pip install --pre "stbkit[xsd]"
  ```
- `full` : 全機能を利用する場合に必要です（xsd, ifc を含む）。
  インストール方法：
  ```bash
  python -m pip install --pre "stbkit[full]"
  ```
  ※300MB程度のディスク容量が必要です

## CLI使用例
- ヘルプを表示する

```bash
stbkit -h
```

- ST-Bridgeをのバリデーションを行う

```bash
stbkit validate model.stb
```

- ST-BridgeをPLYへ変換する

```bash
stbkit convert model.stb -o model.ply
```

- ST-BridgeをIFCへ変換する（依存パッケージのifcopenshellが必要です）

```bash
stbkit convert model.stb -o model.ifc
```

- 2つのST-BridgeのXML差分を表示する

```bash
stbkit diff xml reference.stb target.stb
```

- 標準入力から読み込む

```bash
cat model.stb | stbkit validate -
```
validateとconvertが対応しています。
diffは入力が2つあるため対応していません。

## CLIの終了コード

終了コードについてはstbkitのサブコマンドで、同系統の結果で同じになるようにしています。
0と1は処理を正常に実行できた場合、2以降は処理が実行しきれなかった場合です。
正常に完了したかどうかのみを判定したい場合は、終了コードが1以下かで判定できます。

|終了コード|意味|例|
|----|----|----|
|0|正常に終了|バリデーションOK、diffの差分無し、変換成功|
|1|正常に実行できたが、対象に問題または差分が見つかった|バリデーションNG、diffの差分有り, 変換は実行できたがエラーあり|
|2|引数や指定の間違いで、処理が開始できなかった|未知のオプション、非対応の変換、存在しないパスの指定|
|3|処理の実行中にエラーが生じた|XMLの構文エラー、サイズ上限の超過、比較の失敗|
|4|任意依存パッケージが導入されておらず、要求された処理が実行できない|ifcopenshell無しでのIFC変換、xmlschema無しでの`--schema`指定|
|130|中断終了|Ctrl+C|

1は正常に実行した結果でエラーではないですが、検査や比較を行うツールの慣習に合わせているためです。
`grep`の一致なし、`diff`の差分あり、`git diff --exit-code`の差分有り等は1を返します。
エラーは2以降へ割り当て、正常実行の1がエラーと混ざらないようにしています。
想定外例外も3を返すので、1はバリデーションや差分が正しくできた場合の結果となります。

`validate`でバリデーション不合格と実行中エラーが同時に生じた場合は、バリデーション不合格の問題を優先して1を返します。
ディレクトリ内をまとめて検査する場合、読み込めないファイルがあっても残りの検査は続行します。

`diff`で差分があっても0を返したい場合は、`--exit-zero`を指定します。

## ドキュメント

ドキュメントは現在準備中です。公開時にこちらへリンクを掲載します。

- ユーザーガイド（準備中）
- バージョンアップ、IFC変換の仕様（準備中）

## 依存ライブラリ・再配布に関する注意

- 一部の依存ライブラリはライセンスがLGPLです。本プロジェクトはLGPLライブラリを同梱して再配布しません。ライセンスに関しては利用者が確認してください。
- 詳細はリポジトリの[THIRD_PARTY_COMPLIANCE](https://github.com/taisei-oss/stb-kit/blob/main/THIRD_PARTY_COMPLIANCE.md)を参照してください。

## 依存パッケージ（間接依存を除く）
### 必須
- stbkit-core(MPL-2.0)
### オプション
- xmlschema(MIT): XSDを利用したバリデーションで利用
- ifcopenshell(LGPL): IFCへの変換で利用
- numpy(BSD-3-Clause): ifcopenshellへ渡す回転用列の作成に利用

## ライセンス

本プロジェクトのソースコードは **Mozilla Public License 2.0 (MPL-2.0)** のもとで提供されます。

- MPL-2.0 はファイル単位のコピーレフトライセンスです。
- 本プロジェクトの改変部分（該当ファイル）を再配布する場合、ソース公開義務が発生します。
- 本ライブラリを利用するアプリケーションはOSSである必要はありません

実務利用とオープンな改善の両立を意図したライセンスです。

## 免責（重要）

本ソフトウェアは現状有姿で提供され、いかなる保証もありません。
詳細はリポジトリの[DISCLAIMER](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md)を参照してください。

Copyright 2026 TAISEI CORPORATION
