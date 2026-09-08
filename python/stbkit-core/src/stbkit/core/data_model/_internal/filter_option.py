# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass, field


@dataclass
class NameFilter:
    """
    include, excludeのフィルター。同時指定時はexclude優先
    """

    include: list[str] = field(default_factory=list)
    exclude: list[str] = field(default_factory=list)


@dataclass
class FilterOption:
    global_attribute_filter: NameFilter = field(default_factory=NameFilter)
    global_element_filter: NameFilter = field(default_factory=NameFilter)
    element_attribute_filters: dict[str, NameFilter] = field(default_factory=dict)
    element_child_filters: dict[str, NameFilter] = field(default_factory=dict)
