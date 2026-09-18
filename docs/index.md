# STB-KIT ドキュメント

**STB-KIT**(商標登録出願中)はST-Bridgeを扱うためのオープンソースツールキットです。

_An open-source toolkit for handling ST-Bridge._

## 概要 / Overview

ST-Bridgeは、日本の建築構造分野で広く利用されている建築構造データ交換フォーマットです。

_ST-Bridge is a structural data exchange format widely used in Japan._

本ソフトウェアは、利用者の入力・判断に基づいてデータ処理を行う「ツール」であり、**安全性検証（構造安全性の保証・確認）や法令適合性判定を行うものではありません。**  
（将来的に構造解析等の機能を追加する可能性はありますが、本プロジェクトは安全性検証や法令適合性の保証を目的としません。）

_This software is a “tool” that processes data based on user input and judgment. It is **not intended for safety verification or determining regulatory compliance.**_

責任制限および法域に関する詳細は[DISCLAIMER](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md)を参照してください。

_For detailed warranty disclaimers and limitations of liability, including jurisdictional considerations, please refer to DISCLAIMER.md._

また、利用前に必ずプロジェクトの[README](https://github.com/taisei-oss/stb-kit/tree/main)を参照してください。

> **注意**
> 一部機能は公開準備中です。現在利用できる機能と制約は、各機能のドキュメントを確認してください。 

## インストール方法

STB-KITを利用するにはPython環境にSTB-KITをインストールする必要があります。
（ブラウザで試す場合は不要です）

[STB-KITのインストール](getting-started/install.md){ .md-button .md-button--primary }

## CLIを使う

STB-KITの機能をコマンドから実行します。Pythonの知識がなくても利用できます。

[CLIの利用を始める](getting-started/first-cli.md){ .md-button .md-button--primary }

## Pythonから利用する

ST-BridgeをPythonオブジェクトとして読み込み、プログラミングからST-Bridgeを利用します。

※準備中

## ブラウザで試す

※準備中

## STB-KITの開発に参加する

STB-KITの開発にご協力いただける方向けのガイドです。

※準備中

## 主な機能

- **データモデル**
    - ST-Bridgeデータを扱いやすい形で表現するクラス群
    - 入出力・変換のための共通基盤
- **フォーマット変換**
    - IFC出力（ifcopenshellを利用）
    - PLY等の3Dオブジェクトファイル出力
- **サマリー**
    - 入力データの概要表示
- **バリデーション**
    - ST-Bridge仕様に基づく検証

フォーマットやバージョンの対応範囲は[対応バージョン・形式](reference/versions-formats.md)を参照ください。

## ライセンスと注意事項

STB-KITはMozilla Public License 2.0で提供します。利用前に[ライセンス](https://github.com/taisei-oss/stb-kit/blob/main/LICENSE)、[免責事項](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md)および[THIRD_PARTY_COMPLIANCE](https://github.com/taisei-oss/stb-kit/blob/main/THIRD_PARTY_COMPLIANCE.md)を確認してください。

Copyright 2026 TAISEI CORPORATION
