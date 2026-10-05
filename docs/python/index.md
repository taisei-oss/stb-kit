# Python利用ガイド

stbkitはPython APIを利用して、ST-Bridgeの読み書き、編集、変換などの独自処理を使うことができます。

`stbkit.api`にAPIが公開されています。

## インストール

[STB-KITのインストール](../getting-started/install.md)を参照してください。

## 目次

| 内容 | 主なAPI |
| --- | --- |
| [読み込みと書き出し](io.md) | `stbkit.api.load_latest` `stbkit.api.dump` |
| [データモデルの使い方](data-model.md) | `stbkit.api.stb_latest`、`stbkit.api.StBridgeElement`、`stbkit.api.StBridgeRoot` |
| [要素の検索と参照解決](repository.md)|`stbkit.api.experimental.get_repository`|

クラスや関数の型は[Python APIリファレンス](../_generated/reference/python/index.md)を参照してください。

Copyright 2026 TAISEI CORPORATION
