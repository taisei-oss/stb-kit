# proxyの設定

社内ネットワーク等でインターネット接続にプロキシが必要な場合、stbkitのインストールが失敗することがあります。  

その場合は、Windowsの「インターネットオプション」または環境変数（`HTTP_PROXY` / `HTTPS_PROXY`）でプロキシ設定を行ってください。下記の様に一時的に環境変数を設定する方法もあります。
~~~powershell
# 実行例(Powershellの場合)
$env:HTTP_PROXY="http://proxy.example.com:8080"
$env:HTTPS_PROXY="http://proxy.example.com:8080"
python -m pip install --pre "stbkit[full]"
~~~

Copyright 2025-2026 TAISEI CORPORATION
