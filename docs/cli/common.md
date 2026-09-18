# CLI 共通的な使い方

## ヘルプとバージョン

```bash
# 全体のヘルプの表示
stbkit --help
# バージョンの表示
stbkit --version
# convertサブコマンドのヘルプの表示
stbkit convert --help
```

コマンド名の後ろに`--help`を付けると、そのコマンドで使用する引数を確認できます。

## 共通オプション

各サブコマンドの共通オプションとして`--help`の他に`-v`、`--interactive`、`--max-size-mb`があります。
記載位置はサブコマンドの前後どちらでも構いません。

```bash
stbkit -v convert input.stb -o output.ifc
stbkit convert input.stb -o output.ifc -v
```

### 詳細ログ

`-v`を指定すると、通常より詳しい処理状況を表示します。

```bash
stbkit -v convert input.stb --output output.ifc
```

### 読み込みサイズの上限

stbkitのST-Bridgeファイルの読み込みサイズの上限は128MBです。
`--max-size-mb`を指定することで、読み込むXMLのサイズ上限を緩和したり、制限を強めたりできます。
単位はMBで指定します。

```bash
stbkit convert input.stb -o output.ifc --max-size-mb 500
```

上限を超えるファイルは読み込まずにエラーになります。
ST-Bridgeを読み込むコマンドに適用されます。

### 対話モード

`--interactive`を指定すると、対話モードで実行できます。

```bash
# サブコマンドも対話モードで選択する場合
stbkit --interactive
# サブコマンドを指定したうえで対話モードで実行する場合
stbkit convert --interactive
```

スクリプトによる実行を行う場合などは、対話モードは利用せず、必要な引数を明示してください。

Copyright 2026 TAISEI CORPORATION
