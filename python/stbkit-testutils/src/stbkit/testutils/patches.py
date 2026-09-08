# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import uuid
from typing import Final


class IncrementalUUID:
    TARGETS: Final[tuple[str, ...]] = (
        "uuid.uuid4",
        "stbkit.core._internal.transform.guid_tools._uuid7",
    )

    def __init__(self) -> None:
        self.counter: int = 0

    def __call__(self) -> uuid.UUID:
        # 16バイトのUUIDを生成（counterを埋め込む）
        b: bytes = self.counter.to_bytes(16, byteorder="big")
        self.counter += 1
        return uuid.UUID(bytes=b)
