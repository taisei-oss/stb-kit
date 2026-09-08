# 互換性とAPI安定性

STB-KITは現在`0.x`系であり、`1.0`に向けてAPIの安定化を目指しています。
`1.0`より前は破壊的変更を行う可能性がありますが、通常利用向けAPIは可能な限り変更を抑えます。

## APIの安定性

| 名前空間                   | 位置付け    | 方針                                          |
| ------------------------- | ---------- | ---------------------------------------------- |
| `stbkit.api`              | 公開API    | 通常利用向け。優先的に安定化する                   |
| `stbkit.api.experimental` | 暫定公開API | 将来`stbkit.api`への移行を予定するが、変更の可能性がある |
| `stbkit.core`             | 暫定公開API | 低レベル機能。変更の可能性がある                   |
| `stbkit.tools`            | 暫定公開API | 変換・補助機能。変更の可能性がある                  |
| `stbkit.cli`              | 内部実装    | CLIからの呼び出し用。互換性を保証しない             |
| `_internal`を含むimportパス | 内部実装   | 公開予定なし。互換性を保証しない                   |

通常のアプリケーションでは、可能な限り`stbkit.api`からimportしてください。

```python
from stbkit.api import load, NoneAccessError
```

`stbkit.core`と`stbkit.tools`は直接利用できますが、`0.x`の間はモジュール構成、名称、シグネチャ、型、設定形式などが変更される可能性があります。

なお、`stbkit.core.data_model`は、他の`core`APIより強い互換性を維持することを目標とします。

## 公開APIの判定

公開APIは、利用者向けドキュメントへの掲載や公開エントリーポイントからのexportにより明示します。

次のものは、明示的に公開されない限り互換性の対象外です。

- importパスに`_internal`を含むもの
- 名前が`_`で始まるもの
- ドキュメントに掲載されていない補助的なシンボル

実装ファイルが`_internal`以下にあっても、公開名前空間から再exportされている場合は公開APIとして扱います。

## バージョニング

STB-KITはSemantic Versioningを基礎とします。

- パッチ更新（例:`0.1.1`→`0.1.2`）では、`stbkit.api`の意図的な破壊的変更を原則として行いません。
- マイナー更新（例:`0.1.x`→`0.2.0`）では、破壊的変更を行う場合があります。
- `_internal`の互換性は保証しません。

`stbkit.api`に重要な破壊的変更を行う場合は、可能な範囲で変更履歴、移行方法、非推奨化などを案内します。ただし、`1.0`より前は移行期間を保証しません。

重大な不具合やセキュリティ問題については、パッチ更新でも挙動を修正する場合があります。

## 配布パッケージ間の互換性

`stbkit.core`は`stbkit-core`、`stbkit.api`と`stbkit.tools`は`stbkit`から提供されます。

互換性のある組み合わせは依存メタデータで管理します。`stbkit`と`stbkit-core`を依存関係を無視して個別に更新しないでください。

## ST-Bridgeバージョン

STB-KITのAPIバージョンと、対応するST-Bridgeのバージョンは別に管理します。

短期的な利用では`stb_latest`を使用できますが、参照先は将来変更される可能性があります。

```python
# 最新版を利用
from stbkit.api.stb_latest import StBridge

# 長期利用ではバージョンを明示
from stbkit.api.stb_v2_1_1 import StBridge
```

サポートを終了したST-Bridgeバージョンは、将来`stbkit.api`から削除する場合があります。

古いST-Bridgeファイルを長期間扱う必要がある場合は、`stbkit.core.data_model`を利用してください。

```python
from stbkit.core.data_model.stb_v2_0_2 import StBridge
```

`stbkit.core.data_model`の固定モデルは、サポート終了後も原則としてimportパスを維持します。ただし、archivedモデルには新機能や完全な不具合対応を保証しません。
また、データモデルは公式xsdスキーマと対応しているため、誤記修正などで公式xsdスキーマに変更があった場合はデータモデルに破壊的変更が生じる場合があります。

`stb_latest`または`load_latest`の対象となるST-Bridgeメジャーバージョンが変わる場合は、STB-KITの破壊的変更として扱います。

## `1.0`に向けて

`stbkit.api`を通常利用向けの安定した公開APIとすることを目標とします。

`stbkit.core`と`stbkit.tools`については、`1.0`公開時に安定APIとする範囲を改めて明示します。

それまでは、通常の利用では`stbkit.api`を第一の依存先としてください。

Copyright 2026 TAISEI CORPORATION
