# CLI validate

`validate`は、ST-Bridgeが仕様に適合するか検証します。
`--schema`を省略した場合は、XSDを使わずにデータモデルの定義に基づく簡易検査を行います。
検証内容については[スキーマバリデーション](../technical/schema-validation.md)を参照下さい。


## 基本的な使い方

### XSDスキーマファイルを使ってファイルを検証する

検査結果がコンソールに表示されます。

```bash
stbkit validate model.stb --schema path/to/ST-Bridge.xsd
```

結果をファイル出力したい場合は`-o`オプションを使います。
```bash
stbkit validate model.stb --schema path/to/ST-Bridge.xsd -o result.txt
```

### XSDスキーマファイルを利用せずに簡易検証を行う
```bash
stbkit validate model.stb 
# 結果をファイル出力する場合
stbkit validate model.stb -o result.txt
```

### フォルダ内のST-Bridgeファイルを全て検査する

```bash
stbkit validate path/to/stb_models --schema path/to/ST-Bridge.xsd
```

フォルダを指定した場合は、配下のすべての`.stb`ファイルを検証します。

`--schema`で単一のXSDを指定する場合、ST-Bridgeのバージョンが混在するとフォルダ内一括検証の実行はできますが、一部ファイルで適切なスキーマ検証にならない可能性があります。
バージョンが混在するフォルダを検証する場合は、バージョンごとに分けて検証するか、後述の環境変数と`--require-xsd`を利用してください。

### 環境変数でスキーマを指定してXSDバリデーションを行う

事前に、環境変数の設定が必要です。
[環境変数の設定](../reference/environment-settings.md)を参照ください。

```bash
stbkit validate model.stb --require-xsd
# 結果をファイル出力する場合
stbkit validate model.stb -o result.txt --require-xsd
# フォルダ内のST-Bridgeを全て検証する場合
stbkit validate path/to/stb_models --require-xsd
```


## 主なオプション

- `-o`,`--output`: 検証結果をファイルに出力します。
- `--schema`: 使用するXSDファイルを指定します。省略可能です。
- `--require-xsd`: XSDによる検査を必須にします。`--schema`を省略した場合は環境変数からXSD取得を行います。
- `--exclude-legal-extensions`: 拡張情報で定義された適切な拡張に由来するXSDのエラーを結果から除外します。

## 終了コード

- 0:すべてOKの場合
- 1:NGのファイルがある場合
- 2:入力ファイル、フォルダが存在しない、スキーマファイルが見つからない、出力先指定が不正な場合等
- 3:ファイルの読み込みやバリデーションに失敗した場合
- 4:任意依存パッケージが不足し、バリデーションを実行できない場合

## 注意事項

- 入力には、存在するファイルまたはフォルダ、または標準入力を表す`-`を指定してください。
- ST-BridgeとXSDのバージョンが一致しない場合、意図した検査になりません。
- スキーマエラーがなくても、ST-Bridge仕様として正しいことを保証するものではありません。また、設計判断、構造計算上の妥当性等を保証するものでもありません。
- XSDスキーマファイルは本プロジェクトでは配布は行っていないため、利用条件等を確認し、利用者が適切に管理してください。

Copyright 2026 TAISEI CORPORATION
