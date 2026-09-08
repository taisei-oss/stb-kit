# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Never

_IFCOPENSHELL_IMPORT_ERROR_MESSAGE = (
    "ifcopenshellがインストールされていません。IFCファイルの機能を利用するにはifcopenshellをインストールしてください。\n"
    "インストール方法: \npip install ifcopenshell\n"
    "または\npip install stbkit[ifc]"
)


def raise_import_error(e: ImportError) -> Never:
    if e.name == "ifcopenshell" or (
        e.name is not None and e.name.startswith("ifcopenshell.")
    ):
        raise ImportError(_IFCOPENSHELL_IMPORT_ERROR_MESSAGE) from e
    raise ImportError(f"予期しないImportErrorが発生しました: {e}") from e


def ensure_ifcopenshell() -> None:
    try:
        import ifcopenshell  # noqa: F401
    except ImportError as e:
        raise_import_error(e)
