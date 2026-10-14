# STB-KITのインストール

STB-KITは、Pythonパッケージのstbkitをインストールすることにより利用できます。

Python環境が無い方はPython環境を用意してください。(Microsoft Store等で入手できます)

対応するPythonバージョンは3.12-3.15です。

!!! note "Python 3.15でのIFC"
    Python 3.15では、IFC関連の依存ライブラリの関係で、IFC関連機能が動作しない可能性があります。利用環境で動作をご確認ください。

次のようにインストールします。
2つ目のコマンドでバージョン番号が表示されればインストール成功です。

```bash
python -m pip install --pre "stbkit[full]"
python -m stbkit --version
```

!!! note "ベータ版のインストール"
    STB-KITは現在ベータ版です。pipは通常コマンドではベータ版はインストールされないため、上記の例のように`--pre`を指定する必要があります。利用するベータ版の番号が分かっている場合は、`stbkit==バージョン番号`のようにバージョンを直接指定することもできます。

!!! note "proxyの設定"
    会社の環境によっては、インストール時にproxyの設定が必要な場合があります。proxyエラーとなった場合は[proxyの設定](proxy-setting.md)を参照ください。

## 利用する機能に応じた追加パッケージ

stbkit[full]は、xsd（公式XSDを利用したスキーマ検証）、ifc（IFC変換）、native（3Dビュー機能）を含みます。依存にifcopenshellがあるため、数百MBのディスク容量が必要となります。

必要な機能だけを利用したい場合やディスク容量を節約したい場合は、下記のように追加機能を指定します。

```bash
# 依存なしの最小構成でインストールする場合
python -m pip install --pre stbkit
# 公式スキーマファイルを利用したスキーマチェックを使いたい場合
python -m pip install --pre "stbkit[xsd]"
# IFC変換機能を使いたい場合
python -m pip install --pre "stbkit[ifc]"
# 3Dビュー機能を使いたい場合
python -m pip install --pre "stbkit[native]"
# すべての機能を利用したい場合
python -m pip install --pre "stbkit[full]"
```

Copyright 2026 TAISEI CORPORATION
