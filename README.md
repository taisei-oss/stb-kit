# STB-KIT

STB-KIT(商標登録出願中) はST-Bridgeを扱うためのオープンソースツールキットです。

_An open-source toolkit for handling ST-Bridge._

## 1. 概要 / Overview

ST-Bridgeは、日本の建築構造分野で広く利用されている建築構造データ交換フォーマットです。

_ST-Bridge is a structural data exchange format widely used in Japan._

本ソフトウェアは、利用者の入力・判断に基づいてデータ処理を行う「ツール」であり、**安全性検証（構造安全性の保証・確認）や法令適合性判定を行うものではありません。**  
（将来的に構造解析等の機能を追加する可能性はありますが、本プロジェクトは安全性検証や法令適合性の保証を目的としません。）

_This software is a “tool” that processes data based on user input and judgment. It is **not intended for safety verification or determining regulatory compliance.**_

責任制限および法域に関する詳細は[DISCLAIMER](DISCLAIMER.md)を参照してください。

_For detailed warranty disclaimers and limitations of liability, including jurisdictional considerations, please refer to DISCLAIMER.md._

> [!IMPORTANT]
> 現在社内レビュー中のため、まだ全ての機能が公開されていません。順次公開していく予定です。

## 2. 主な機能

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
- **3DビューおよびGUIによる簡易編集（現在非公開）**
  - 軽微な可視化・編集・確認を補助する機能（目的は利便性であり、正統性・適合性を保証しません）

## 3. ST-BridgeおよびIFCとの関係

- ST-Bridgeの権利は 一般社団法人buildingSMART Japan(bSJ) に帰属します。
- 本プロジェクト運営主体（大成建設株式会社）は、bSJとの利用許諾契約に基づき、ST-Bridge仕様書に基づく実装（仕様書の記述を参照・転記した部分を含む場合があります）をオープンソース（MPL-2.0）として公開しています。
- ただし、本記載は、利用者に対して ST-Bridge仕様書そのもの等の引用・転載・再配布等の権利を付与するものではありません。仕様書の利用条件は、別途bSJが定める条件に従ってください。
- 本ソフトウェアは **bSJの公認・認証プログラムではありません。**
- IFC出力はサードパーティ製ライブラリifcopenshellを利用しています。
- buildingSMART International（bSI）との契約関係はありません。
- 権利表示
    - ST-Bridge
        - 著作権者:buildingSMART Japan
        - 出典:
            - [ST-Bridge_XML仕様説明書（ver.2.1.1）](https://www.building-smart.or.jp/wp-content/uploads/2026/07/ST-Bridge_XML%E4%BB%95%E6%A7%98%E8%AA%AC%E6%98%8E%E6%9B%B8%EF%BC%88ver.2.1.1%EF%BC%89.pdf)
            - [ST-Bridge_XML仕様説明書（ver.2.1.0）](https://www.building-smart.or.jp/wp-content/uploads/2023/05/ST-Bridge2.1_XML%E4%BB%95%E6%A7%98%E8%AA%AC%E6%98%8E%E6%9B%B8ver.2.1.0.pdf)
            - [ST-Bridge_XML仕様説明書（ver.2.1.0）計算データ編](https://www.building-smart.or.jp/wp-content/uploads/2023/05/ST-Bridge%E8%A8%88%E7%AE%97%E3%83%87%E3%83%BC%E3%82%BF%E7%B7%A8_XML%E4%BB%95%E6%A7%98%E8%AA%AC%E6%98%8E%E6%9B%B8ver.2.1.0.pdf)
            - [ST-Bridge_XML仕様説明書（ver.2.0.2）](https://www.building-smart.or.jp/wp-content/uploads/2022/06/ST-Bridge_XML%E4%BB%95%E6%A7%98%E8%AA%AC%E6%98%8E%E6%9B%B8%EF%BC%88ver.2.0.2%EF%BC%89_20220615.pdf)
            - [ST-Bridge_XML仕様説明書（ver.2.0.2）計算データ編](https://www.building-smart.or.jp/wp-content/uploads/2021/03/ST-Bridge%E8%A8%88%E7%AE%97%E3%83%87%E3%83%BC%E3%82%BF%E7%B7%A8_XML%E4%BB%95%E6%A7%98%E8%AA%AC%E6%98%8E%E6%9B%B8ver.2.0.2.pdf)
        - 仕様書の利用方法：原文の引用（仕様書やXSDスキーマファイルそのもの再配布は行っていません）
    - IFC（Industry Foundation Classes）
        - 著作権者:buildingSMART International
        - 出典: https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/
        - 本アプリはサードパーティ製ライブラリifcopenshellを用いてIFC出力を行いますが、スキーマ本文の同梱・引用は行っていません。

## 4. インストール

STB-KITは現在ベータ版です。通常のインストールではベータ版が選ばれない場合があるため、次の例のように`--pre`を指定します。利用するベータ版の番号が分かっている場合は、`stbkit==バージョン番号`のようにバージョンを直接指定することもできます。

```bash
python -m pip install --pre "stbkit[full]"
```


## 5. クイックスタート

### ST-Bridgeのバリデーション

```bash
stbkit validate model.stb
```
ST-Bridgeの仕様に基づいてファイルを検証し、問題があればエラーメッセージを表示します。
検証内容はstbkit独自のチェックとなります。
公式XSDによる検証も併せて行う場合は、`--schema`にXSDファイルのパスを指定してください。

```bash
stbkit validate model.stb --schema ST-Bridge210.xsd
```

`--schema`の指定を行うには依存パッケージのxmlschemaが必要です。インストール時に`stbkit[full]`または`stbkit[xsd]`としてインストールしてください。
なお、XSDファイルは本プロジェクトでは配布していないため、利用者が別途用意する必要があります。

### ST-BridgeからPLYへの変換

```bash
stbkit convert model.stb -o model.ply
```

入出力の形式は拡張子から判定します。明示する場合は`--from`と`--to`を指定します。

```bash
stbkit convert model.stb --from stb --to ply -o model.ply
```

### ST-BridgeからIFCへの変換

```bash
stbkit convert model.stb -o model.ifc
```

IFC出力には依存パッケージのifcopenshellが必要です。インストール時に`stbkit[full]`、または`stbkit[ifc]`としてインストールしてください。

対応しているフォーマットと変換の対応は、次コマンドで確認できます。

```bash
stbkit convert --list-formats
```

詳細な利用方法や実践的な例については、ドキュメント及び各パッケージのREADMEを参照してください。

## 6. 利用状況アンケート

STB-KITの今後の開発・改善や開発方針の検討の参考とするため、利用状況アンケートを実施しています。

STB-KITをご利用いただいている方は、ぜひご回答ください。試用のみの場合や、現在は利用していない場合でもご回答いただけます。

利用状況に変更があった場合は、以前に回答された方も再度ご回答いただけます。

[STB-KIT利用状況アンケートに回答する](https://forms.cloud.microsoft/r/z5cN8eTX4v)

## 7. マニュアル/ドキュメント
ドキュメントは現在準備中です。公開時にこちらへリンクを掲載します。

- ユーザーガイド（準備中）
- APIリファレンス（準備中）

## 8. パッケージ一覧
順次公開していくため、未公開のパッケージも記載しています。公開状況は「公開」列を参照してください。

|パッケージ名|Github公開|PyPI公開|path|言語|概要|
|----|----|----|----|----|----|
|stbkit-core|済|済|python/stbkit-core|Python|コアライブラリ|
|stbkit|済|済|python/stbkit|Python|ユーティリティ|
|stbkit-native|未|未|rust/stbkit-native|Python+Rust|3D・GUI機能のRust拡張|
|stbkit-core-rs|未|未|rust/stbkit-core-rs|Rust|Rust用のコアライブラリ|
|stbkit-rs|未|未|rust/stbkit-rs|Rust|Rust用のユーティリティ|

## 9. ロードマップ
現在の方向性と優先事項は[ROADMAP](ROADMAP.md)を参照してください。

## 10. 破壊的変更と互換性ポリシー
バージョニングと互換性の方針は[COMPATIBILITY](COMPATIBILITY.md)を参照してください。

## 11. 依存ライブラリに関する重要事項

- 一部依存ライブラリは**LGPL**を含む場合があります。
- 本プロジェクトは**LGPLライブラリの再配布を行いません**（利用者が別途導入する形）。
- `stbkit-native` は **コンパイル済みバイナリ** を含み、MIT/Apache-2.0等の第三者ライセンスが含まれる場合があります。
- 利用者・再配布者は、各ライセンス条件を確認し遵守してください。

詳細は[THIRD_PARTY_COMPLIANCE](THIRD_PARTY_COMPLIANCE.md)を参照してください。

## 12. ライセンス

本プロジェクトのソースコードは [**Mozilla Public License 2.0 (MPL-2.0)**](LICENSE) のもとで提供されます。

- MPL-2.0 はファイル単位のコピーレフトライセンスです。
- 本プロジェクトの改変部分（該当ファイル）を再配布する場合、ソース公開義務が発生します。
- 本ライブラリを利用するアプリケーションはOSSである必要はありません

実務利用とオープンな改善の両立を意図したライセンスです。

## 13. 重要な免責事項

本ソフトウェアは現状有姿（AS IS）で提供され、**安全性検証、法令適合性、正確性、完全性、特定目的適合性**を含む一切の保証を行いません。
利用者は、出力結果の検証、専門家確認、適用法令の確認を自己責任で行ってください。

詳細は[DISCLAIMER](DISCLAIMER.md)を参照してください。

## 14. 開発について

STB-KITは、建築構造設計の実務に携わる構造設計者が中心となって開発しています。

ST-Bridgeの仕様だけでなく、構造設計での実際の利用方法を踏まえた実装を重視しています。

一方で、より使いやすく、保守しやすいOSSとして改善していくためには、構造設計以外の分野の知見も重要だと考えています。

ソフトウェア設計、API設計、テスト、ドキュメント、開発ツール、セキュリティなど、さまざまな観点からのレビューや改善提案を歓迎します。

構造設計やST-Bridgeに詳しくない方からのご意見や貢献も歓迎します。気になる点や改善案があれば、IssueやDiscussionでぜひお知らせください。

## 15. コントリビュート

> [!IMPORTANT]
> 現在コードを順次公開中のため、プルリクエストは受け付けていません。
> IssueやDiscussionの投稿でのご貢献は歓迎いたします。

本プロジェクトへのご貢献を歓迎いたします。
本プロジェクトは一部でRustを利用していますが、Rust部分の知識がなくとも、Python部分(pythonディレクトリ内)のみのご提案・修正・機能追加等も受け付けております。
また、ドキュメントの改善、誤記修正、テスト追加、テスト用サンプルの提供や、IssueやDiscussionの投稿のみでも歓迎しております。幅広いご協力をお待ちしております。

本プロジェクトは **DCO（Developer Certificate of Origin）** を採用します。
詳細は[CONTRIBUTING](CONTRIBUTING.md)を参照してください。

## 16. セキュリティ

脆弱性報告は[SECURITY](SECURITY.md)の手順に従ってください。

## 17. サポート方針について

本プロジェクトはベストエフォートでの対応となり、個別サポートや応答保証はありません。サポート範囲や免責事項などの詳細は[SUPPORT.md](SUPPORT.md) をご参照ください。


## 18. 知的財産について
商標（出願中）およびstbkitに含まれ得る特許（出願中）に関する取り扱いは[INTELLECTUAL PROPERTY GUIDELINES](IP.md)を参照してください。

Copyright 2026 TAISEI CORPORATION
