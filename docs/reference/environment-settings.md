# 環境変数の設定

## XSD Schemaファイルの保存場所

XSDのパスを直接指定せずにXSDを利用したバリデーションを行う場合は、ST-Bridgeのバージョンごとに次の環境変数を設定します。

| 環境変数 | 対象バージョン |
| --- | --- |
| STBKIT_SCHEMA_PATH_STB_V2_0_0 | ST-Bridge 2.0.0 |
| STBKIT_SCHEMA_PATH_STB_V2_0_1 | ST-Bridge 2.0.1 |
| STBKIT_SCHEMA_PATH_STB_V2_0_2 | ST-Bridge 2.0.2 |
| STBKIT_SCHEMA_PATH_STB_V2_1_0 | ST-Bridge 2.1.0 |
| STBKIT_SCHEMA_PATH_STB_V2_1_1 | ST-Bridge 2.1.1 |

値には、対応するXSDファイルのパスを指定します。

全てのパスを指定する必要はないので、検証が必要なバージョンのみ指定してください。

Copyright 2026 TAISEI CORPORATION
