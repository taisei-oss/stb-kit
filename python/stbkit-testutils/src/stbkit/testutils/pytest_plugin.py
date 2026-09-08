# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import shutil
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Final

import pytest
from pytest import OptionGroup
from stbkit.core._internal.constants import (
    ENV_NAME_SCHEMA_PATH_STB_V2_0_1,
    ENV_NAME_SCHEMA_PATH_STB_V2_0_2,
    ENV_NAME_SCHEMA_PATH_STB_V2_1_0,
    ENV_NAME_SCHEMA_PATH_STB_V2_1_1,
)
from stbkit.tools._internal.constants import DEBUG_DUMP_DIR_ENV

from .fixture_repository import FixtureFormat, FixtureRepository
from .golden_runner import RunContext

_XSD_ENV_NAME_BY_STB_VERSION: Final[dict[str, str]] = {
    "2.0.1": ENV_NAME_SCHEMA_PATH_STB_V2_0_1,
    "2.0.2": ENV_NAME_SCHEMA_PATH_STB_V2_0_2,
    "2.1.0": ENV_NAME_SCHEMA_PATH_STB_V2_1_0,
    "2.1.1": ENV_NAME_SCHEMA_PATH_STB_V2_1_1,
}
_XSD_ENV_NAMES: Final[tuple[str, ...]] = tuple(_XSD_ENV_NAME_BY_STB_VERSION.values())

_STB_VERSION_BY_FIXTURE_FORMAT: Final[dict[FixtureFormat, str]] = {
    FixtureFormat.STB_V2_0_1: "2.0.1",
    FixtureFormat.STB_V2_0_2: "2.0.2",
    FixtureFormat.STB_V2_1_0: "2.1.0",
    FixtureFormat.STB_V2_1_1: "2.1.1",
}

# WindowsとLinuxでIFCの出力数値に揺らぎが生じるため、丸める、
_IFC_ROUND_DIGITS_FOR_GOLDEN: Final[int] = 10
_IFC_ROUND_DIGITS_MM_FOR_GOLDEN: Final[int] = 3


def _unset_xsd_env_names(env_names: Iterable[str] | None = None) -> list[str]:
    """XSDの場所が指定されていない環境変数名を返す。"""
    names: Iterable[str] = _XSD_ENV_NAMES if env_names is None else env_names
    return [env_name for env_name in names if not os.getenv(env_name)]


def _xsd_env_names_from_versions(*, versions: Iterable[str], nodeid: str) -> list[str]:
    env_names: list[str] = []
    unknown: list[str] = []
    for version in versions:
        env_name: str | None = _XSD_ENV_NAME_BY_STB_VERSION.get(version)
        if env_name is None:
            unknown.append(version)
            continue
        env_names.append(env_name)
    if unknown:
        raise pytest.UsageError(
            "requires_xsdに未対応のST-Bridgeバージョンが指定されています。"
            f"test={nodeid}, versions=[{', '.join(unknown)}]"
        )
    return env_names


def _required_xsd_env_names_for_item(item: pytest.Item) -> list[str]:
    marker = item.get_closest_marker("requires_xsd")
    if marker is None:
        return []

    marker_versions: list[str] = []
    for arg in marker.args:
        if isinstance(arg, str):
            marker_versions.append(arg)
        elif isinstance(arg, (list, tuple, set)):
            marker_versions.extend(v for v in arg if isinstance(v, str))

    kw_versions = marker.kwargs.get("versions")
    if isinstance(kw_versions, str):
        marker_versions.append(kw_versions)
    elif isinstance(kw_versions, (list, tuple, set)):
        marker_versions.extend(v for v in kw_versions if isinstance(v, str))

    if marker_versions:
        return _xsd_env_names_from_versions(
            versions=marker_versions,
            nodeid=item.nodeid,
        )

    callspec = getattr(item, "callspec", None)
    if callspec is not None:
        spec = callspec.params.get("spec")
        spec_format = getattr(spec, "format", None)
        if isinstance(spec_format, FixtureFormat):
            version: str | None = _STB_VERSION_BY_FIXTURE_FORMAT.get(spec_format)
            if version is not None:
                return [_XSD_ENV_NAME_BY_STB_VERSION[version]]

        version_param = callspec.params.get("version")
        if isinstance(version_param, str):
            return _xsd_env_names_from_versions(
                versions=[version_param], nodeid=item.nodeid
            )

    return list(_XSD_ENV_NAMES)


def _invalid_xsd_env_entries() -> list[tuple[str, str]]:
    """指定された場所にXSDが無い環境変数名と、その値を返す。"""
    entries: list[tuple[str, str]] = []
    for env_name in _XSD_ENV_NAMES:
        raw_path: str | None = os.getenv(env_name)
        if raw_path and not Path(raw_path).is_file():
            entries.append((env_name, raw_path))
    return entries


def _is_rust_available() -> bool:
    return shutil.which("cargo") is not None


def pytest_configure(config: pytest.Config) -> None:
    """XSDを利用できない状態でテストを始めないように、実行前に検査する。

    場所を指定したうえでファイルが無いのは設定ミスなので、常に中止する。
    未設定は既定ではXSDの無い環境として許容するが、--require-xsdを
    指定した場合はスキップを許さず、設定漏れとして中止する。
    """
    invalid: list[tuple[str, str]] = _invalid_xsd_env_entries()
    if invalid:
        details: str = "\n".join(
            f"  {env_name}: {raw_path}" for env_name, raw_path in invalid
        )
        raise pytest.UsageError(
            f"環境変数に指定されたXSDファイルが存在しません。設定を確認してください。\n{details}"
        )

    if bool(config.getoption("--require-xsd")):
        unset: list[str] = _unset_xsd_env_names()
        if unset:
            raise pytest.UsageError(
                "--require-xsdが指定されていますが、XSDの場所が設定されていません。"
                f"環境変数[{', '.join(unset)}]にXSDファイルのパスを設定してください。"
            )

    if bool(config.getoption("--require-rust")) and not _is_rust_available():
        raise pytest.UsageError(
            "--require-rustが指定されていますが、cargoが見つかりません。"
            "Rustをインストールしてください。"
        )


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """XSDが無い環境では、requires_xsdのテストを失敗ではなくスキップにする。

    ST-BridgeのXSDは再配布しないため、リポジトリをcloneしただけの環境には存在しない。
    その状態でも`pytest`がそのまま通るようにする。
    """
    require_xsd: bool = bool(config.getoption("--require-xsd"))
    require_rust: bool = bool(config.getoption("--require-rust"))
    rust_available: bool = _is_rust_available()

    for item in items:
        if not require_xsd:
            required_env_names: list[str] = _required_xsd_env_names_for_item(item)
            if required_env_names:
                missing: list[str] = _unset_xsd_env_names(required_env_names)
                if missing:
                    item.add_marker(
                        pytest.mark.skip(
                            reason=(
                                "ST-BridgeのXSDが利用できないため実行しません。"
                                "環境変数"
                                f"[{', '.join(missing)}]"
                                "にXSDファイルのパスを設定してください。"
                            )
                        )
                    )

        if require_rust:
            continue

        if item.get_closest_marker("requires_rust") is None:
            continue
        if rust_available:
            continue

        item.add_marker(
            pytest.mark.skip(
                reason=(
                    "Rust(cargo)が利用できないため実行しません。"
                    "実行する場合はRustをインストールしてください。"
                )
            )
        )


def pytest_addoption(parser: pytest.Parser) -> None:
    group: OptionGroup = parser.getgroup("stbkit")
    group.addoption(
        "--create-golden",
        action="store_true",
        default=False,
        help="STB-KITのGoldenファイルを作成または上書きするためのオプション。"
        "このオプションを指定すると、テストの出力がGoldenファイルに書き込まれます。"
        "通常は、テストの出力とGoldenファイルを比較してテストの成否を判断しますが、"
        "このオプションを使用することで、出力をGoldenファイルとして保存します。"
        "goldenが変わる実装をした際に利用します。"
        "--create-golden後はgit diffで差分が想定通りになっているか確認が必要です。",
    )
    group.addoption(
        "--require-xsd",
        action="store_true",
        default=False,
        help=(
            "XSDが未設定でもrequires_xsdのテストをスキップせずエラーにします。"
            "XSDを利用できるCIで、設定漏れによる見逃しを防ぐために指定します。"
        ),
    )
    group.addoption(
        "--require-rust",
        action="store_true",
        default=False,
        help=(
            "Rustがインストールされていない場合requires_rustのテストをスキップせずエラーにします。"
            "Rustを利用できるCIで指定します。"
        ),
    )
    fixtures_root: Path = (
        Path(__file__).parent.parent.parent.parent.parent.parent / "tests" / "fixtures"
    )
    group.addoption(
        "--fixtures-root",
        action="store",
        default=str(fixtures_root),
        help="Root directory of fixture cases.",
    )
    group.addoption(
        "--debug-dump-dir",
        action="store",
        default=None,
        help=(
            "STBシリアライズ失敗時のデバッグダンプ出力先ディレクトリ。"
            "指定時のみ有効です。"
        ),
    )


@pytest.fixture(scope="session", autouse=True)
def configure_debug_dump_dir(pytestconfig: pytest.Config) -> Iterator[None]:
    raw_debug_dump_dir = pytestconfig.getoption("--debug-dump-dir")
    if not raw_debug_dump_dir:
        yield
        return

    debug_dump_dir = Path(raw_debug_dump_dir).expanduser()
    debug_dump_dir.mkdir(parents=True, exist_ok=True)

    previous = os.environ.get(DEBUG_DUMP_DIR_ENV)
    os.environ[DEBUG_DUMP_DIR_ENV] = str(debug_dump_dir)
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop(DEBUG_DUMP_DIR_ENV, None)
        else:
            os.environ[DEBUG_DUMP_DIR_ENV] = previous


@pytest.fixture
def create_golden(request: pytest.FixtureRequest) -> bool:
    return bool(request.config.getoption("--create-golden"))


@pytest.fixture(scope="session")
def fixtures_root(pytestconfig: pytest.Config) -> Path:
    return Path(pytestconfig.getoption("--fixtures-root"))


@pytest.fixture(scope="session")
def run_context(pytestconfig: pytest.Config) -> RunContext:
    return RunContext(
        create_golden=bool(pytestconfig.getoption("--create-golden")),
        ifc_round_digits=_IFC_ROUND_DIGITS_FOR_GOLDEN,
        ifc_round_digits_mm=_IFC_ROUND_DIGITS_MM_FOR_GOLDEN,
    )


@pytest.fixture(scope="session")
def fixture_repository(fixtures_root: Path) -> FixtureRepository:
    return FixtureRepository(fixtures_root)
