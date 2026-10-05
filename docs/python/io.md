# 読み込みと書き出し

## ファイルから読み込む

```python
from pathlib import Path

import stbkit.api
from stbkit.api import StBridgeRoot


def read_model(path: Path) -> StBridgeRoot:
    return stbkit.api.load(path)
```

`load`はXMLに記録されたST-Bridgeのバージョンを読み取り、そのバージョンに対応する`StBridge`型を返します。

読み込まないとどのモジュールの`StBridge`型になるか不明であるため、型ヒントは基底クラスである`StBridgeRoot`となっています。

そのため、そのままでは補完や型チェックを利用できません。
その後の処理を行う際は読み込まれた型で分岐してから処理を行う必要があります。
```python
from pathlib import Path
import stbkit.api
from stbkit.api import StBridgeRoot, stb_v2_1_1


def print_project_name(path: Path) -> None:
    stb: StBridgeRoot = stbkit.api.load(path)
    if isinstance(stb, stb_v2_1_1.StBridge):
        print(stb.stb_common.project_name)
    else:
        print(f"{stb.version}は対応していないバージョンです")
```

loadの引数でversionを指定すると強制的にそのバージョンとして読み込みます。戻り値の型は指定したバージョンになりますが、ST-Bridgeファイルとバージョンが異なる場合、指定したバージョンにない属性や子要素は正しく読み込まれません。

## XML文字列から読み込む

```python
import stbkit.api
from stbkit.api import StBridgeRoot


def read_xml(xml: str) -> StBridgeRoot:
    return stbkit.api.loads(xml)
```

バージョンの扱い方については`load`と同様です。

## 最新版として読み込む

ST-Bridgeファイルを読み込んだのち、最新版に変換して返す関数です。
```python
from pathlib import Path

import stbkit.api
from stbkit.api.stb_latest import StBridge


def read_model(path: Path) -> StBridge:
    return stbkit.api.load_latest(path)
```

`stb_latest.StBridge`が返るため、型による分岐なしで処理を行うことができます。

`loads`版の`loads_latest`もあります。

ただし下記の注意点があります。
- すべての要素が正しくバージョンアップされない場合があります。特にv2.0からv2.1へのバージョンアップは外形情報が中心で、配筋や細かい属性は変換されない場合があります。
- stbkitのstb_latestが新しいバージョンのデータモデルに変更されると、破壊的変更となります。短期的な用途で使うか、stbkitのバージョンを固定して利用してください。

## ファイルへ書き出す

stbkitのdumpはUTF-8専用となっています。
OSによってはencodingがutf-8ではない場合があるため、必ず`encoding="utf-8"`を指定してください。

必須属性欠落や、子要素の最大・最小回数違反などのST-Bridgeの仕様に違反したデータを書き出そうとするとSchemaErrorが発生し書き出しできないため注意してください。
```python
from pathlib import Path

import stbkit.api
from stbkit.api import StBridgeRoot


def write_model(model: StBridgeRoot, path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stbkit.api.dump(model, stream)
```

書き出す際に下記の値が設定されます。そのため、インスタンスが変更されるため注意してください。なお、app_nameとapp_versionは両方指定するか、両方省略する必要があります。
- `stb.version`:対象のST-Bridgeバージョン
- `stb.stb_common.app_name`:引数でapp_nameを指定した場合はその値、指定しない場合は"stbkit-core"
- `stb.stb_common.app_version`:引数でapp_versionを指定した場合はその値、指定しない場合はstbkit-coreのバージョン
- `stb.stb_common.convert_app_name`:引数でapp_nameを指定した場合は"stbkit-core"
- `stb.stb_common.convert_app_version`:引数でapp_nameを指定した場合はstbkit-coreのバージョン

## 文字列へ書き出す

注意点は`dump`と同様です

```python
import stbkit.api
from stbkit.api import StBridgeRoot


def to_xml(model: StBridgeRoot) -> str:
    return stbkit.api.dumps(model)
```

## 読み込みの上限を変える

`load`と`loads`は、XMLのサイズと要素の入れ子の深さに上限を設けています。

読み込み上限の既定値は、max_size=128 * 1024 * 1024、max_depth=15です。max_sizeは、ファイルパスから読み込む場合はファイルのバイト数(128MB)、XML文字列やテキストストリームから読み込む場合は文字数に適用されます。

通常のモデルであれば既定値で問題なく読み込めます。大規模なファイルや、StbExtension定義で深く入れ子になった拡張要素を扱う場合だけ変更します。

```python
from pathlib import Path

import stbkit.api
from stbkit.api import StBridgeRoot


def read_large_model(path: Path) -> StBridgeRoot:
    return stbkit.api.load(path, max_size=2 * 1024 * 1024 * 1024, max_depth=40)
```

上の例のようにファイルパスを渡す場合、max_sizeはバイト数で指定します。上限を超える入力は読み込まず、`XmlLimitExceededError`になります。DOCTYPE宣言を含むXMLも読み込まず、`UnsafeXmlError`になります。

文字コード、読み込み時に記録されるメッセージ、例外の扱いは、使用する関数のAPIリファレンスを確認してください。

Copyright 2026 TAISEI CORPORATION
