# stbkit-native

ST-Bridgeを扱うツールキットstbkit用のネイティブ拡張（Rust実装）です。

_A native extension (Rust) for stbkit, an utility library for handling ST-Bridge._

ST-Bridgeは、日本の建築構造分野で広く利用されている建築構造データ交換フォーマットです。

_ST-Bridge is a structural data exchange format widely used in Japan._

詳細はリポジトリの[README](https://github.com/taisei-oss/stb-kit)および[DISCLAIMER](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md) をご確認ください。

![PyPI License](https://img.shields.io/pypi/l/stbkit-native)

## 概要

stbkit-nativeは、STB-KITの主としてGUI関連の拡張機能を提供します。

- 3Dビューワー

本パッケージはデータ処理・表示・編集支援を目的とし、**安全性検証（構造安全性の保証・確認）や法令適合性判定を行いません**。
出力結果の検証、専門家確認、適用法令の確認は利用者の責任です。

## インストール

通常は`stbkit`パッケージ経由で本パッケージをインストールすることを推奨します。

STB-KITは現在ベータ版です。通常のインストールではベータ版が選ばれない場合があるため、次の例では`--pre`を指定します。利用するベータ版の番号が分かっている場合は、`stbkit-native==バージョン番号`のようにバージョンを直接指定することもできます。

個別にインストールする場合は下記コマンドがご利用できますが、stbkit-native単体で利用できる機能はありません。

```bash
python -m pip install --pre stbkit-native
```

通常は、本体パッケージであるstbkitの追加依存としてインストールします。

```bash
python -m pip install --pre "stbkit[native]"
```

native以外も含めた全機能を導入する場合は、次を使用します。

```bash
python -m pip install --pre "stbkit[full]"
```

事前ビルドされたwheelが提供されていない環境では、インストール時にRustのビルド環境が必要です。

## 対応環境

本パッケージの対応環境は、Python 3.12以上のWindowsおよびLinux環境です。

macOSについてはインストール時にRustのビルド環境が必要です。また動作確認も実施していません。

## 重要（バイナリ同梱・第三者ライセンス）

本パッケージはコンパイル済みバイナリ（wheel）を含み、第三者ライセンス（MIT/Apache-2.0/BSD等）のコンポーネントが含まれる場合があります。

- 公式wheelには、同梱コンポーネントのライセンス本文・表示情報を「THIRD_PARTY_LICENSES.html」として含めます。
- 依存crateに含まれるNOTICE情報は「THIRD_PARTY_NOTICES.html」として含めます。
- 再配布者は、ライセンス表示やNOTICE同梱等の義務を確認し遵守してください。

## ドキュメント

- [STB-KITドキュメント](https://taisei-oss.github.io/stb-kit/)

## ライセンス

本プロジェクトのソースコードは **Mozilla Public License 2.0 (MPL-2.0)** のもとで提供されます。

- MPL-2.0 はファイル単位のコピーレフトライセンスです。
- 本プロジェクトの改変部分（該当ファイル）を再配布する場合、ソース公開義務が発生します。
- 本ライブラリを利用するアプリケーションはOSSである必要はありません。

実務利用とオープンな改善の両立を意図したライセンスです。

第三者コンポーネントは各ライセンスに従います（wheel同梱の「THIRD_PARTY_LICENSES.html」および「THIRD_PARTY_NOTICES.html」参照）。

## 依存パッケージ（間接依存を除く）

### Pythonパッケージ

- Pythonパッケージ依存はありません。

### Rustクレート（ビルド済バイナリ）

- stbkit-nativeの直接依存クレート
    - **stbkit-rs**（MPL-2.0）
    - **pyo3**（MIT OR Apache-2.0）
    - **serde_json**（MIT OR Apache-2.0）
    - **uuid**（Apache-2.0 OR MIT）
- stbkit-rsの直接依存クレート
    - **serde**（MIT OR Apache-2.0）
    - **uuid**（Apache-2.0 OR MIT）
    - **eframe**（MIT OR Apache-2.0）
    - **three-d**（MIT）
    - **image**（MIT OR Apache-2.0）

正確な依存関係はstbkit-nativeの[Cargo.toml](https://github.com/taisei-oss/stb-kit/blob/main/rust/stbkit-native/Cargo.toml)、stbkit-rsの[Cargo.toml](https://github.com/taisei-oss/stb-kit/blob/main/rust/stbkit-rs/Cargo.toml)、およびwheel同梱の第三者ライセンス一覧を確認してください。

## 知的財産

stbkit-native に含まれ得る特許に関する取り扱いは[IP.md](https://github.com/taisei-oss/stb-kit/blob/main/IP.md)を参照してください。

## 免責（重要）

本ソフトウェアは現状有姿で提供され、いかなる保証もありません。
詳細はリポジトリの[DISCLAIMER.md](https://github.com/taisei-oss/stb-kit/blob/main/DISCLAIMER.md)を参照してください。

Copyright 2026 TAISEI CORPORATION
