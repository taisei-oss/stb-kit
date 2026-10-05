# 要素の検索と参照解決

リポジトリは、読み込んだST-Bridgeのデータモデルに対して、idによる要素検索と、要素間の参照解決機能を提供します。

## 位置づけ

リポジトリは現在、実験的な暫定公開APIとなっています。実験的公開の期間は、名前、シグネチャ、機能などが変更される可能性があります。

安定性についての詳細は、[互換性方針](https://github.com/taisei-oss/stb-kit/blob/main/COMPATIBILITY.md)を参照してください。

## 索引の作成

リポジトリはST-Bridgeのルート要素から構築し、構築時に索引を作成します。

```python
import stbkit.api.experimental

repo = stbkit.api.experimental.get_repository(stb)
```

構築後にデータモデルを変更した場合は、`refresh()`で索引を作り直す必要があります。

索引に入るのは、idなどのキーを持つ型とguidを持つ要素です。
!!! note "すべての要素に対応していません"
    現在すべてのidを持つキーには対応していません。そのため、検索や参照解決ができない要素があります。今後対応要素を拡充していきます。

## キーによる取得

| メソッド | 戻り値 | 見つからない場合 |
| --- | --- | --- |
| `get(ItemType, key)` | 指定した型の要素 | `ReferenceElementNotFoundError` |
| `get_or_none(ItemType, key)` | 指定した型の要素 | `None` |
| `get_by_guid(guid)` | 要素 | `ReferenceElementNotFoundError` |
| `get_by_guid_or_none(guid)` | 要素 | `None` |
| `get_steel(name)` | 鋼材断面 | `ReferenceElementNotFoundError` |
| `find_equivalent(instance, exclude_fields=...)` | 属性が一致する要素 | `None` |

関数の命名規則は下記です。

- `get_*`は一意なキーで1件を検索します。
- `find_*`は条件に一致する要素を探します。
- 末尾の`_or_none`は、対象が存在しない場合に例外ではなく`None`を返します。

ST-Bridgeでは要素種類が異なれば同じidを付けられるため、`get`では型の指定が必要です。guidはST-Bridge全体で一意なため、`get_by_guid`は型を取りません。

`get_steel`は、鋼材断面を`name`で検索します。nameは全鋼材断面で一意である前提です。

## idでの検索

idで検索する型は、stbkit-coreが対応している型のみです。

対応していない型を`get`に渡した場合は`TypeError`になり、データが検索で見つからなかった場合（`ReferenceElementNotFoundError`）とは区別されます。`get_or_none`でも`None`にはせず送出します。

| 例外 | 意味 |
| --- | --- |
| `TypeError` | その型はキーで検索できる型として対応していない |
| `ReferenceElementNotFoundError` | 対応しているが、その要素がST-Bridgeに存在しない |

※`id`で自動で索引を行わないのは、ST-Bridgeには`id`という名前を持つがキーではない属性が存在するためです。

## 参照解決

`deref`は、参照先の要素を返すアクセサを返します。

```python
section = repo.deref(stb_girder).id_section
node = repo.deref(stb_girder).id_node_start_or_none
```

アクセサの属性名は、参照先を探したいidの属性名をそのまま使います。末尾に`_or_none`を付けた属性は、参照が解決できない場合に`None`を返します。

| 例外 | 意味 |
| --- | --- |
| `AttributeError` | その要素に、その名前の参照は定義されていない |
| `ReferenceElementNotFoundError` | 参照値がない、または参照先の要素が存在しない |
| `SchemaError` | 判別属性の値が不正で、参照先の型を確定できない |

`SchemaError`は参照先がない場合とは区別し、`_or_none`付きの属性でも送出します。参照先が存在しないこととデータが不正であることは別の状態として扱います。

### 判別属性を伴う参照

断面への参照のように、同じ属性でも要素の種別によって参照先の型が変わるものがあります。この場合は、`kind_structure`などの判別属性の値で参照先の型を決めてから検索します。

```python
# StbGirder.kind_structure が "RC" なら StbSecBeam_RC を引く
section = repo.deref(stb_girder).id_section
```
判別する値(`kind_structure`等)が定義済みの値に一致しない場合は`SchemaError`になります。

## バージョンごとの定義

参照定義は、ST-Bridgeバージョンごとに定義しているため、バージョンによって参照解決できる要素が異なる場合があります。
また、現時点ではすべての要素に対応していません。

Copyright 2026 TAISEI CORPORATION
