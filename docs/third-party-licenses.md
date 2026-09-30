# ドキュメントサイトのサードパーティライセンス

このページは、ドキュメントサイトのサードパーティライセンスについて記載します。
STB-KIT本体、Python wheel等の依存ライセンスは、それぞれの配布物に含まれるライセンスファイルを参照ください。

## サイトで配布されているテーマ

| パッケージ | バージョン | ライセンス |
| --- | --- | --- |
| mkdocs-material | 9.7.7 | MIT |

Material for MkDocsのテーマCSS、JavaScript等がドキュメントサイトへ含まれます。

## ブラウザ版で外部サイトから読み込んで利用するソフトウェア

ブラウザ版の一部ページでは、ページ表示後に次のソフトウェアを外部配信元から自動取得して実行します。

| ソフトウェア | バージョン | ライセンス | 配布元 |
| --- | --- | --- | --- |
| Pyodide | 0.29.5 | MPL-2.0 | https://cdn.jsdelivr.net/pyodide/v0.29.5/full/pyodide.js |
| IfcOpenShell（WebAssembly版wheel） | 0.8.5 | LGPL-3.0-or-later | https://ifcopenshell.github.io/wasm-wheels/ |
| STB-KIT | 0.1.0b2 | MPL-2.0 | https://pypi.org/project/stbkit/ |

上記の取得時には、パッケージ解決とダウンロードのためPyPI（pypi.org / files.pythonhosted.org）への接続が発生する場合があります。
また、間接依存パッケージのダウンロードも発生する場合があります。

## 参考：生成時に利用しているツール

| パッケージ | ライセンス |
| --- | --- |
| mkdocs | BSD-2-Clause |
| mkdocstrings-python | ISC |

これらはドキュメントサイトの生成時に使用します。再配布は致しません。

Copyright 2026 TAISEI CORPORATION
