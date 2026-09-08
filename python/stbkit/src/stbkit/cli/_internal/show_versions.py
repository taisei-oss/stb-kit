# Copyright 2025-2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from importlib import metadata


def print_versions(dist_name: str) -> None:
    try:
        version = metadata.version(dist_name)
        print(f"{dist_name}: {version}")
    except metadata.PackageNotFoundError:
        print(f"{dist_name}: unknown")


def show_versions(entry_points: metadata.EntryPoints) -> None:
    print_versions("stbkit")
    stbkit_set: set[str] = set()
    for dist in metadata.distributions():
        name = dist.metadata.get("Name")
        if not isinstance(name, str):
            continue
        dist_name: str = name.strip()
        if dist_name.replace("_", "-").lower().startswith("stbkit-"):
            stbkit_set.add(dist_name)
    for package in sorted(stbkit_set):
        print_versions(package)
    stbkit_set.add("stbkit")
    for ep in entry_points:
        if ep.dist:
            dist_name = ep.dist.name
            if dist_name not in stbkit_set:
                stbkit_set.add(dist_name)
                print_versions(dist_name)
