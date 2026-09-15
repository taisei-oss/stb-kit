# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
from typing import IO

from ..stb_exceptions import XmlLimitExceededError, XmlLimitKind
from ..stb_typing import TextSource
from .constants import DEFAULT_MAX_XML_SIZE, XML_READ_CHUNK_SIZE


def load_text(
    src: TextSource, *, encoding: str, max_size: int = DEFAULT_MAX_XML_SIZE
) -> str:
    """テキストの読み込み

    メモリ保護のため、サイズの上限を設ける。
    """
    # ファイルオブジェクトの場合は上限より1文字多く読み、超過したら例外を投げる
    if not isinstance(src, (str, os.PathLike)):
        return _read_limited(src, max_size=max_size)
    # ファイルパスの場合はファイルサイズを確認し、上限を超えるファイルは例外を投げる
    size: int = os.stat(src).st_size
    if size > max_size:
        raise XmlLimitExceededError(kind=XmlLimitKind.SIZE, limit=max_size, actual=size)
    with open(src, encoding=encoding) as f:
        return _read_limited(f, max_size=max_size)


def _read_limited(src: IO[str], *, max_size: int) -> str:
    """上限より1文字多く読み、超過したら例外を投げる"""
    # readにmax_sizeをそのまま渡すと、
    # 実際のデータ量と無関係にその大きさのバッファを確保するため、分割して読みこむ。
    chunks: list[str] = []
    remaining: int = max_size + 1
    while remaining > 0:
        chunk: str = src.read(min(remaining, XML_READ_CHUNK_SIZE))
        if not chunk:
            break
        chunks.append(chunk)
        remaining -= len(chunk)

    result: str = "".join(chunks)
    if len(result) > max_size:
        raise XmlLimitExceededError(kind=XmlLimitKind.SIZE, limit=max_size)
    return result
