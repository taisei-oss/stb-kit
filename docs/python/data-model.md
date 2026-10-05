# データモデルの使い方

## モジュール定義

ST-Bridgeの各バージョンは、別のPythonモジュールとして定義されています。

ルート要素は各モジュールの`StBridge`クラスです。

| 利用目的 | モジュール |
| --- | --- |
| stbkitがupgrade可能な最新バージョン | `stbkit.api.stb_latest` |
| 2.0系の最新バージョン | `stbkit.api.stb_v2_0_2` |
| 2.1系の最新バージョン | `stbkit.api.stb_v2_1_1` |
| その他のバージョン | `stbkit.core.data_model.stb_v2_0_1`,`stbkit.core.data_model.stb_v2_1_0`など |

短期的に行う処理では`stbkit.api.stb_latest`を使用し、特定バージョンのXML構造を厳密に扱う場合は`stbkit.core.data_model`を直接使用します。

## データモデル概要

XML要素はclass、XML属性・子要素・内容はPythonの属性に対応します。
クラス名はPascalCase、属性名はsnake_caseです。

クラス名が厳密なPascalCaseではない場合は補正されます。

例：ST_BRIDGE → StBridge、StbSecColumn_RC → StbSecColumnRc

属性名が厳密なsnake_caseではない場合は補正されます。

例：X → x、isFoundation → is_foundation

子要素の入る属性は、クラス名をsnake_caseにした属性に入ります。

例：StbSecColumn_RC → stb_sec_column_rc

内容はcontent属性に入ります。

## 属性

XML属性用のPythonの属性はプロパティになっており、2種類あります。

```python
element.name  # 値を取得。未設定ならstbkit.api.NoneAccessErrorを投げる
element.name_or_none  # 未設定値をNoneとして取得
```

ST-Bridgeの仕様書の必須かどうかにかかわらずに両方のプロパティが利用できます。

これらのプロパティはセッターもあるため、値を設定できます。

```python
element.name = "name"
element.name_or_none = None
```

それぞれのプロパティには型ヒントがあります。基本的な型は下記の対応となります。

| XML上の型 | Python上の型 |
| --- | --- |
| string | str (guidの場合はuuid.UUID) |
| integer | int |
| double | float |

間違った型を代入しようとするとTypeMismatchErrorが発生します。
また、負の長さを代入しようとするなど、仕様違反の値を入れようとするとSchemaErrorが発生します。

```python
element.name = 10  # nameがstringの場合TypeMismatchError
element.length = -10.0  # lengthが長さの場合SchemaError
```

値が制限されている場合は、propertyの出力はStrEnumやIntEnumになります。値のセットはstrやintでも可能です。
Enum名称はクラス名＋属性名のPascalCaseになります。
Enumの値は、値をLARGE_SNAKE_CASEにしたものになります。
IntEnumなど頭が数字になる場合は`VALUE_5`のようになります。

## 子要素

最大回数が1の子要素は単一オブジェクト、最大回数の複数の子要素は種類別のリストになります。

リストはNoneにならず、要素がなければ空リストです。ただし、その親要素はNoneの場合があります。

単一子要素には通常プロパティ、or_noneプロパティの他にensureという仕組みがあります。ensureはアクセサを提供し、Noneの場合は新たな子要素を生成して返すメソッドを提供します。

```python
element.child  # 値を取得。NoneならNoneAccessErrorが発生
element.child_or_none  # Noneの時はNoneとして取得
element.ensure.child()  # 単一子要素を、あればそのまま、なければ作成して取得する
```

リスト要素はリストを継承しているため、通常のlistと同様に利用できます。ただし、セットするときはリストを作り直すため、代入したコレクションとは別のインスタンスとなります。

```python
children: list = element.children  # リストとして扱える
child_1 = element.children[1]  # アクセスが利用できます。
element.children.append(other_child)  # appendなどのリスト操作が可能です

# リストの代入は可能ですが、異なるリストとなります。
element.children = other_children
assert len(element.children) == len(
    other_children
)  # リストの中身がセットされるため、長さは同じ
assert element.children[0] is other_children[0]  # 子要素のインスタンスは同じ
assert element.children is not other_children  # リストのインスタンスは変わる
other_children.append(other_child_2)  # そのため、元のリストに要素を追加しても
assert len(element.children) != len(other_children)  # 子要素リストには反映されない
```

ST-Bridgeは非常に階層が深いため、深い階層にアクセスしたい場合は通常プロパティで直接たどり、Noneを許容する処理単位でNoneAccessErrorを捕捉するとコードが見やすく書けます。
各階層にNone判定を並べる必要はありません。
例えば、RC柱断面sectionから矩形断面のX幅を取得する処理は次のように書けます。
```python
# 以下はST-Bridge v2.1.1の例です
try:
    width_x = section.stb_sec_figure_column_rc.stb_sec_column_rect.width_x
except NoneAccessError:
    width_x = None
```
`except AttributeError`や`except Exception`で広く捕捉するのは、属性名の誤りなど、想定外のエラーが判別できなくなるので避けたほうが良いです。

コンストラクタは各属性を初期化することができます。

## 主要要素構成

```text
ツリー                          型                   内容
StBridge                        StBridge            ルート要素
  stb_common                    StbCommon             共通情報   
  stb_model                     StbModel              モデル
    stb_nodes.stb_node[]        list[StbNode]           節点
    stb_stories.stb_story[]     list[StbStory]          階
    stb_members                 StbMembers              部材群
      stb_columns.stb_column[]  list[StbColumn]           柱
      stb_posts.stb_post[]      list[StbPost]             間柱
      stb_girders.stb_girder[]  list[StbGirder]           大梁
      stb_beams.stb_beam[]      list[StbBeam]             小梁
      stb_braces.stb_brace[]    list[StbBrace]            ブレース
      stb_slabs.stb_slab[]      list[StbSlab]             スラブ
      stb_walls.stb_wall[]      list[StbWall]             壁
    stb_sections                StbSections             断面群
      stb_sec_column_rc[]       list[StbSecColumnRc]      RC柱、間柱リスト
      stb_sec_column_s[]        list[StbSecColumnS]       S柱、間柱リスト
      stb_sec_beam_rc[]         list[StbSecBeamRc]        RC大梁、小梁断面リスト
      stb_sec_beam_s[]          list[StbSecBeamS]         S大梁、小梁断面リスト
      stb_sec_steel             StbSecSteel               鋼材断面群
```

### 属性具体例

下記のようなST-Bridge v2.1.1の節点要素を例にします。

> 4.2.1. 節点：StbNode 
>- 概要
>    - 説明 ：節点 
>    - 親要素：StbNodes
>
>- 属性
>
> | 属性名 | 型 | 必須 | 説明 |
> | --- | --- | --- | --- |
> | id | integer | ○ | ID |
> | guid | string | | GUID |  
> | X | double | ○ | 全体座標系 X |
> | Y | double | ○ | 全体座標系 Y |
> | Z | double | ○ | 全体座標系 Z |
> | kind | string | ○ | 以下のいずれかの値をとる<br>ON_GIRDER：大梁上<br>ON_BEAM：小梁上<br>ON_COLUMN：柱上<br>ON_POST：間柱上<br>ON_GRID：グリッド上<br>ON_CANTI：片持ち大梁先端<br>ON_SLAB：スラブ上<br>OTHER：その他|
> | id_member | integer | | リンクする部材のID |

出典：ST-Bridge_XML仕様説明書（ver.2.1.1）(buildingSMART Japan 構造設計小委員会)

- 要素名がStbNodeであるため、クラスStbNodeに対応します
- XMLの属性はPythonの属性に対応します。
  - X,Y,Z等はsnake_caseのため、小文字になります。
  - guidはUUID型になります。
  - kindはStrEnumになります。
- 全ての属性について、通常アクセスとオプショナルアクセスがあります。

~~~python
import uuid
from stbkit.api.stb_v2_1_1 import StbNode, StbNodeKind

# コンストラクタで値を設定できます
node: StbNode = StbNode(id=1)
# 初期化後に値を代入することもできます
# guidはuuid.UUID型になります。
node.guid = uuid.uuid4()
# XML属性名をsnake_caseにしたものになります
node.x = 1.0
node.y = 2.0
# 通常アクセスの型はオプショナルでないため、Noneでなければ数値演算なども可能です。
node.z = node.x + node.y
# 値が限定されているものはEnumが利用できます
node.kind = StbNodeKind.ON_GRID
assert node.kind is StbNodeKind.ON_GRID
# StrEnumなので、strとの比較も可能です
assert node.kind == "ON_GRID"
# 値の代入はstrでも可能です。代入するとenumとして保持されます。
node.kind = "ON_GIRDER"
assert node.kind is StbNodeKind.ON_GIRDER
~~~

Copyright 2026 TAISEI CORPORATION
