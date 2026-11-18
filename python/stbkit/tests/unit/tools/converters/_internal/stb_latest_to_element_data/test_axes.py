# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core.stb_reporting import LoggerReporter

from stbkit.tools.converters._internal.stb_latest_to_element_data.axes import (
    _divide_grid,
)


def test_divide_grid() -> None:
    reporter = LoggerReporter()
    # 1しかない場合は組み合わせは作れない
    items = [(0.0, "a")]
    result = _divide_grid(items, reporter)
    assert result == []
    # X,Y軸のみ
    items = [(0.0, "a"), (90.0, "b")]
    result = _divide_grid(items, reporter)
    assert result == [[(0.0, "a"), (90.0, "b")]]
    # X,Y軸のみ
    items = [(0.0, "a"), (270.0, "b")]
    result = _divide_grid(items, reporter)
    assert result == [[(0.0, "a"), (270.0, "b")]]
    # 3つの軸(1つかぶる)
    items = [(0.0, "a"), (90.0, "b"), (180.0, "c")]
    result = _divide_grid(items, reporter)
    assert result == []
    # 3つの軸（かぶらない）
    items = [(0.0, "a"), (60.0, "b"), (120.0, "c")]
    result = _divide_grid(items, reporter)
    assert result == [[(0.0, "a"), (60.0, "b"), (120.0, "c")]]
    # 4つの軸
    items = [(0.0, "a"), (90.0, "b"), (180.0, "c"), (270.0, "d")]
    result = _divide_grid(items, reporter)
    assert result == [[(0.0, "a"), (90.0, "b")], [(180.0, "c"), (270.0, "d")]]
