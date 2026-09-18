# AGENTS運用ガイド

STB-KITは建築構造設計の実務に基づくドメイン知識を重視して開発している。
構造設計上の意味を伴う処理について、既存実装の意図を推測で変更しないこと。
不明な場合は仕様、テスト、ドキュメント等を確認し、人の判断が必要な場合は確認を求めること。

## 最重要: 必ず最初に守ること
このセクションは最優先ルール。以下に違反する変更は行ってはいけない。

### 絶対禁止（最重要）

1. ARCHITECTURE.mdは編集禁止。
   - フォーマット調整
   - 誤記修正
   - 言い回しの修正
   上記を含め、いかなる変更も禁止。
2. 下記の法務関連文書は指示がない限り編集禁止。
  - README.md(プログラムに関する部分を除く)
  - CODE_OF_CONDUCT.md
  - CONTRIBUTING.md
  - DISCLAIMER.md
  - IP.md
  - LICENSE
  - SECURITY.md
  - SUPPORT.md
  - THIRD_PARTY_COMPLIANCE.md
3. 自動生成コードは編集しない（対象ファイルは本書末尾の一覧を参照）。
4. goldenテストのinput用fixtureを勝手に生成しない。

### 重要ルール（必須）

1. 不必要なテストを大量に生成しない。生成する場合、区別するために下記を実行する。
  - Pythonのテスト生成時は ai_generated マーカーを付ける。
  - Rustのテスト生成時は tests.ai_generated モジュール内に作る。
2. ruff/cargo が利用可能なら、変更したコードに対して check と format を実施する。
  - mypyが利用可能な環境ではmypyも実施する。
3. 型ヒントは厳密に書く。
4. cast / type:ignore / noqa を安易に使わない。
5. --create-goldenの実行時は必ず人に確認をとり、実行した場合変更点を伝える

## その他ルール
- コードの実装を変更した場合、コード内のdocstringやdocs内のドキュメントに影響がないか確認し、必要な修正を提案する。

## パッケージ責務

### Python

#### stbkit-core
path: python/stbkit-core

- Pythonのコアパッケージ。データモデル、読み書き、バリデーションを行う。
- 依存はオプションのxmlschema以外使ってはいけない。
- 基本的に人の解釈を伴わない処理を入れる。
- 長期的に保守できることを目標とする。
- PyPIに公開。

#### stbkit
path: python/stbkit

- Pythonの総合パッケージ。APIやCLIの入口のほか、変換処理などを実装する。
- ifcopenshell以外の依存は、できるだけ利用しない。
- PyPIに公開。

#### stbkit-testutils
path: python/stbkit-testutils

- testを行うためのユーティリティ。
- 最低限の依存を用いてよい。
- PyPIには公開せず、開発環境での利用を想定。

## 開発ガイド

### ドキュメント

ドキュメント生成は下記コマンドで行える

~~~bash
uv run --only-group docs scripts/docs.py build
~~~

デフォルトではデータモデルのドキュメントは省略する。フル版を生成する場合は下記コマンドを利用する。

~~~bash
uv run --only-group docs scripts/docs.py build --include-generated-api
~~~

docs/_generatedは自動生成したファイルが入る。


## 開発者向け補足

### 編集禁止: 自動生成コード一覧

下記コードは stbkit-codegen により自動生成されるため、直接修正してはいけない。

- python/stbkit-core/src/stbkit/core/data_model/stb_v2_0_0.py
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_0_0.pyi
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_0_1.py
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_0_1.pyi
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_0_2.py
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_0_2.pyi
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_1_0.py
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_1_0.pyi
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_1_1.py
- python/stbkit-core/src/stbkit/core/data_model/stb_v2_1_1.pyi
- python/stbkit-core/src/stbkit/core/repository/repo_v2_0_2.pyi
- python/stbkit-core/src/stbkit/core/repository/repo_v2_1_0.pyi
- python/stbkit-core/src/stbkit/core/repository/repo_v2_1_1.pyi

Copyright 2026 TAISEI CORPORATION
