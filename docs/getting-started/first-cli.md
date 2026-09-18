# 最初のCLI実行

各コマンド内のinput.stbは用意したST-Bridgeファイルのパスを入力します。
サンプルデータを利用したい場合は[こちら](../examples/data.md)から入手できます。

パスが通っていない場合stbkitで実行できない場合があります。その時は下記のように、モジュール呼び出しコマンドに置き換えてください。

```bash
# パスが通っている場合
stbkit --help
# パスが通っていない場合
python -m stbkit --help
```

## ST-Bridgeの概要を表示する

input.stbのプロジェクト名、節点数、要素数など概要情報を表示できます。

```bash
stbkit summary input.stb
```

## ST-BridgeファイルをIFCファイルへ変換する

input.stbをoutput.ifcへIFCファイルとして書き出します。

```bash
stbkit convert input.stb -o output.ifc
```

!!! note "ifcopenshellが必要です"
    IFCへの変換には依存のifcopenshellが必要です。
    依存不足のエラーが出る場合は"stbkit[ifc]"を指定してインストールしてください。

## ST-Bridgeのバリデーションを行う

input.stbが仕様通りになっているかバリデーションを行い、結果を表示します。
こちらは簡易的な検証であり、より厳密なバリデーションを行う場合は公式XMLスキーマを利用します。

```bash
stbkit validate input.stb
```

## CLIのヘルプを表示する

全体のヘルプ

```bash
stbkit --help
```

サブコマンドのヘルプ
```bash
# 変換のヘルプ
stbkit convert --help
# バリデーションのヘルプ
stbkit validate --help
```

## 詳細ドキュメント
- [共通事項](../cli/common.md)
- [convert](../cli/convert.md)
- [upgrade](../cli/upgrade.md)
- [validate](../cli/validate.md)

Copyright 2026 TAISEI CORPORATION
