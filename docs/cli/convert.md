# CLI convert

`convert`サブコマンドは、ST-Bridgeを他形式へ変換します。

## 基本的な使い方

### ST-BridgeをIFCへ変換する

```bash
stbkit convert input.stb -o output.ifc
```

### PLYを作成する

```bash
stbkit convert input.stb -o output.ply
```
PLY出力の座標単位はmです。

### 利用できる形式と経路を確認する

```bash
stbkit convert --list-formats
```

## 主なオプション

| オプション         | 説明                               | 
| ----------------- | ---------------------------------- |
| `-h`, `--help`    | ヘルプを表示します                  |
| `-f`, `--from`    | 入力ファイルのフォーマットを指定します|
| `-t`, `--to`      | 出力ファイルのフォーマットを指定します|
| `-o` ,`--output`  | 出力ファイル名を指定します           |
| `-y`, `--yes`     | 上書き確認をスキップします           |
| `-v`, `--verbose` | 詳細な処理内容を表示します           |
| `-V`, `--version` | バージョン情報を表示します           |


## 対応フォーマット

| 形式 | 説明 |
|------|------|
| `stb` | ST-Bridge|
| `stb-2.0.2`, `stb-2.1.1`等,`stb-latest` | バージョン指定付きST-Bridge（latestは最新版で、2026年9月現在v2.1.1） |
| `ifc` | IFC（Industry Foundation Classes、 建築情報モデル） |
| `ply` | PLY（Polygon File Format、 3次元データ） |

### 変換の組み合わせ

| 入力 (`--from`) | 出力 (`--to`) | 内容                       |
| ------------- | ----------- | ------------------------ |
| stb           | ifc         | ST-Bridge → IFC 変換       |
| stb           | ply         | ST-Bridge → PLY 変換 --via=ifcを指定すると、一度IFCに変換してからPLYに変換する       |
| stb           | stb         | バージョン変換（例：2.0.2 → 2.1.0） |

stbのバージョンについては、入力形式を省略するとファイルのversion属性から自動判定します。
出力形式を省略した場合は、出力ファイルの拡張子から自動判定します。

## 終了コード

- 0:変換が完了し、errorが記録されなかった場合
- 1:変換は完了したが、変換中にerrorが記録された場合
- 2:引数や指定が不正で変換を開始できない場合
- 3:読み込みや変換に失敗し、変換を完了できなかった場合
- 4:任意依存パッケージが不足し、要求された変換を実行できない場合

## 詳細仕様

### 変換仕様

IFCへの変換仕様については[ST-BridgeからIFCへの変換仕様](../technical/stb-ifc-conversion.md)を参照ください。

### 入出力形式について

- 入力ファイル、出力ファイルいずれもファイル名が指定された場合はフォーマットを拡張子から自動判定します。意図を明確にしたい場合は`--to`や`--from`を指定してください。
- 入力形式を省略できる場合は拡張子やST-Bridge XMLのバージョンから判定します。判定できない場合は`--from`を指定してください。
- 出力ファイル名を省略、または`-`を指定すると標準出力となります。ただし、この時はフォーマットが自動判定できないため、`--to`オプションが必須となります。
- 入力ファイル名を`-`にすると、標準入力を利用します。

### 上級者向けオプション

これらは通常不要ですが、自動処理や検証用途で便利です。

| オプション                 | 説明                                           | 使用例                           |
| --------------------- | -------------------------------------------- | ----------------------------- |
| `--via` | 経由する中間形式を指定します | `--via ifc` |
| `--save-intermediate` | 変換途中のファイルを保存します。<br>指定内容により保存対象が変わります（下表参照）。 | `--save-intermediate stb,ifc` |

### 中間ファイル出力仕様

| 変換内容 | `--save-intermediate`指定 | 出力される中間ファイル | 備考 |
| --- | --- | --- | --- |
| stb → ifc | `stb` | `output.ifc.stb` | IFC変換前の内部更新後データ |
| stb → ply | `stb,ifc` | `output.ply.stb`、`output.ply.ifc` | `--via ifc`を指定した場合 |
| stb → stb | なし | ― | 通常、中間出力は不要 |



ファイル名を省略すると、出力ファイル名に基づいて自動生成されます。

### コマンド例

#### IFCを経由してPLYを作成する

```bash
stbkit convert input.stb -o output.ply --via ifc
```

#### ST-Bridgeを最新版へ変換する

出力形式をST-Bridgeにすると、ST-Bridgeが最新版へ変換されます。

```bash
stbkit convert input.stb -o output.stb
```

※変換後ST-Bridgeにスキーマエラーがあると出力できません

#### 明示的に出力形式を指定する場合

```bash
stbkit convert input.stb -o output.ifc --to ifc
```

#### 変換の中間ファイルを出力する

```bash
# STB→IFC変換前の中間STBを保存
# output.ifc.stbとして保存される
stbkit convert input.stb -o output.ifc --save-intermediate stb

# IFCを経由してPLYへ変換し、中間STBとIFCを保存
# output.ply.stb、output.ply.ifcとして保存される
stbkit convert input.stb -o output.ply --via ifc --save-intermediate stb,ifc

# 明示的にファイル名を指定
# tmp.stb, tmp.ifcとして保存される
stbkit convert input.stb -o output.ply --via ifc --save-intermediate stb=tmp.stb,ifc=tmp.ifc
```
※変換途中のstbにスキーマ違反が含まれる場合は出力できずエラーになる場合があります。


## 注意事項

- ST-Bridgeのバージョンダウンは実装されていません。
- IFC機能には任意依存のifcopenshellが必要です。
- 対応変換の正確な一覧は`--list-formats`を参照ください。
- 出力先が既に存在する場合は、上書き確認が表示されます。自動実行では`-y`の指定が必要です。

Copyright 2026 TAISEI CORPORATION
