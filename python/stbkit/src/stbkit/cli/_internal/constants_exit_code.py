# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""CLIの終了コード

同系統の結果は、サブコマンドが違っても同じ値を返すようにする。
0と1は「処理を正常に実行できた」場合、2以降は「処理が実行できなかった」場合。
"""

from typing import Final

EXIT_OK: Final[int] = 0
"""処理が正常に終了した。バリデーション比較、diff差分なし等"""

EXIT_ISSUE_FOUND: Final[int] = 1
"""処理は正常に実行できたが、対象に問題または差分あり。

バリデーションNG、diffで差分有り、変換の実行はできたがエラーが出た場合が該当。

1は正常に実行した結果でエラーではないが、検査や比較を行うツールの慣習に合わせている。
grepの一致なし、diffの差分あり、`git diff --exit-code`の差分有り等は`1を返す。

想定外例外がそのまま投げられると、終了コードが1になってしまうが、
1はバリデーションや比較の結果に利用したいため、混ざらないように終了コードを変更する処理を行う。
"""

EXIT_INVALID_ARGUMENT: Final[int] = 2
"""引数や指定の間違いで、処理が開始できなかった。

未知のオプション、非対応の変換の指定、存在しないパスの指定等。

argparseが引数エラーに2を使うため、それに合わせている。
stbkitで把握しきれなかった引数エラーが素通りしても同じ値になる。
grepやdiffも異常に2を使い、シェルの慣習でもビルトインの誤用が2。
"""

EXIT_EXECUTION_ERROR: Final[int] = 3
"""処理の実行中に失敗した。

入出力の失敗など、引数の誤りでも実行結果の問題でもない場合。
想定外の例外もこれで終了する。
"""

EXIT_OPTIONAL_DEPENDENCY_MISSING: Final[int] = 4
"""オプション依存パッケージがなく、処理を実行できなかった。

ifcopenshellやxmlschemaを必要とする処理を指定したのにインストールされていない場合。
利用者の環境によって結果が変わるため、EXIT_EXECUTION_ERRORとは分ける。
"""

EXIT_INTERRUPTED: Final[int] = 130
"""中断(Ctrl+C)で終了した。

シグナルnによる終了を128+nで表す慣習に合わせている(128+2=130)。
Pythonの既定ではKeyboardInterruptが1になるため、キャッチして変更する。
"""
