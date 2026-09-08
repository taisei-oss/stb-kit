# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path

import pytest
from stbkit.testutils.fixture_repository import (
    FixtureFormat,
    FixtureRepository,
)


def get_fixture_repo(config: pytest.Config) -> FixtureRepository:
    opt = config.getoption("--fixtures-root")
    path = Path(opt)
    path = path.resolve()

    if not path.exists():
        raise pytest.UsageError(f"Fixtures ファイルが見つかりません: {path}")

    return FixtureRepository(path)


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if "spec" not in metafunc.fixturenames:
        return

    repo = get_fixture_repo(metafunc.config)

    if metafunc.function.__name__ == "test_conversions":
        spec_conversions = repo.iter_conversion_node_specs()
        metafunc.parametrize(
            "spec",
            [
                # IFCを経由する変換はifcopenshellが必要
                pytest.param(
                    spec,
                    marks=[pytest.mark.requires_ifcopenshell]
                    if FixtureFormat.IFC4 in spec.route_formats
                    else [],
                )
                for spec in spec_conversions
            ],
            ids=lambda s: (
                f"{s.case_id}:{'_to_'.join(fmt.value for fmt in s.route_formats)}"
            ),
        )
    elif metafunc.function.__name__ == "test_roundtrip_stb_v202":
        spec_roundtrips = repo.iter_roundtrip_specs(fmt=FixtureFormat.STB_V2_0_2)
        metafunc.parametrize(
            "spec",
            spec_roundtrips,
            ids=lambda s: f"{s.case_id}:{s.format.value}:{s.source_path.name}",
        )
    elif (
        metafunc.function.__name__ == "test_roundtrip_stb_v210"
        or metafunc.function.__name__ == "test_roundtrip_dict_stb_v210"
    ):
        spec_roundtrips = repo.iter_roundtrip_specs(fmt=FixtureFormat.STB_V2_1_0)
        metafunc.parametrize(
            "spec",
            spec_roundtrips,
            ids=lambda s: f"{s.case_id}:{s.format.value}:{s.source_path.name}",
        )
    elif (
        metafunc.function.__name__ == "test_roundtrip_stb_v2_1_1"
        or metafunc.function.__name__ == "test_roundtrip_dict_stb_v2_1_1"
    ):
        spec_roundtrips = repo.iter_roundtrip_specs(fmt=FixtureFormat.STB_V2_1_1)
        metafunc.parametrize(
            "spec",
            spec_roundtrips,
            ids=lambda s: f"{s.case_id}:{s.format.value}:{s.source_path.name}",
        )
    elif metafunc.function.__name__ in (
        "test_schema_check",
        "test_schema_check_no_xsd",
    ):
        spec_roundtrips = (
            repo.iter_roundtrip_specs(fmt=FixtureFormat.STB_V2_1_1)
            + repo.iter_roundtrip_specs(fmt=FixtureFormat.STB_V2_1_0)
            + repo.iter_roundtrip_specs(fmt=FixtureFormat.STB_V2_0_2)
        )
        metafunc.parametrize(
            "spec",
            spec_roundtrips,
            ids=lambda s: f"{s.case_id}:{s.format.value}:{s.source_path.name}",
        )
    elif metafunc.function.__name__ in ("test_schema_check_line_count",):
        # 現在v2.1.1のスキーマのバージョン指定が誤記になっているため、行数比較は行わない
        # TODO: v2.1.1のスキーマのバージョン指定が修正されたら、v2.1.1も対象にする
        spec_roundtrips = repo.iter_roundtrip_specs(
            fmt=FixtureFormat.STB_V2_1_0
        ) + repo.iter_roundtrip_specs(fmt=FixtureFormat.STB_V2_0_2)
        metafunc.parametrize(
            "spec",
            spec_roundtrips,
            ids=lambda s: f"{s.case_id}:{s.format.value}:{s.source_path.name}",
        )
