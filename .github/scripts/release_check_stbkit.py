# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Final

from release_check_common import (
    check_license,
    get_pyproject_dict,
    get_tag_version,
    get_venv_python,
    get_wheel_path,
    run,
)

PACKAGE_NAME: str = "stbkit"
CORE_PACKAGE_NAME: str = "stbkit-core"
FIXTURE_PATH: Final = (
    Path.cwd()
    / "tests"
    / "fixtures"
    / "cases"
    / "column_rc"
    / "column_rc.stb_v2_1_1.stb"
)
FIXTURE_PATH_STR: Final = str(FIXTURE_PATH)


def check_core_dependency(stbkit_data: dict[str, Any], version: str) -> None:
    """開発初期段階なので、stbkitとstbkit-coreは同じバージョンとする"""
    project: Any = stbkit_data["project"]
    dependencies: Any = project.get("dependencies", [])
    if not isinstance(dependencies, list):
        raise RuntimeError("project.dependenciesがリストではありません")

    pattern: re.Pattern[str] = re.compile(
        rf"^{CORE_PACKAGE_NAME}\s*==\s*(?P<version>.+)$"
    )
    for dep in dependencies:
        if not isinstance(dep, str):
            continue
        match: re.Match[str] | None = pattern.fullmatch(dep.strip())
        if match is None:
            continue
        dep_version: str = match.group("version").strip()
        if dep_version != version:
            raise RuntimeError(
                f"{CORE_PACKAGE_NAME}のバージョンが異なります: "
                f"expected: {version}, actual: {dep_version}"
            )
        return

    raise RuntimeError(f"{CORE_PACKAGE_NAME}の正確な依存関係が宣言されていません")


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--python-version", default="3.14")
    args: argparse.Namespace = parser.parse_args()

    root_path: Path = Path.cwd()
    core_pyproject: Path = root_path / "python" / CORE_PACKAGE_NAME / "pyproject.toml"
    stbkit_pyproject: Path = root_path / "python" / PACKAGE_NAME / "pyproject.toml"

    dist_dir: Path = root_path / "dist"
    core_dist_dir: Path = root_path / "dist-stbkit-core"
    smoke_venv_wheel_dir: Path = root_path / f".venv-release-smoke-wheel-{PACKAGE_NAME}"
    smoke_venv_sdist_dir: Path = root_path / f".venv-release-smoke-sdist-{PACKAGE_NAME}"

    tag_version: str = get_tag_version(args.tag, f"{PACKAGE_NAME}-v")
    core_data: dict[str, Any] = get_pyproject_dict(core_pyproject)
    stbkit_data: dict[str, Any] = get_pyproject_dict(stbkit_pyproject)

    core_version: str = str(core_data["project"]["version"])
    stbkit_version: str = str(stbkit_data["project"]["version"])

    if tag_version != stbkit_version:
        raise RuntimeError(
            "tagのバージョンとpyprojectのバージョンが一致しません: "
            f"tag={tag_version}, pyproject={stbkit_version}"
        )

    check_core_dependency(stbkit_data, stbkit_version)

    if core_version != stbkit_version:
        raise RuntimeError(
            f"{CORE_PACKAGE_NAME}と{PACKAGE_NAME}のバージョンは"
            "開発初期段階のため一致している必要があります:"
            f"{CORE_PACKAGE_NAME}={core_version}, {PACKAGE_NAME}={stbkit_version}"
        )

    for directory in (
        dist_dir,
        core_dist_dir,
        smoke_venv_wheel_dir,
        smoke_venv_sdist_dir,
    ):
        if directory.exists():
            shutil.rmtree(directory)

    run(
        [
            "uv",
            "build",
            "--python",
            args.python_version,
            "--no-python-downloads",
            "--package",
            CORE_PACKAGE_NAME,
            "--out-dir",
            str(core_dist_dir),
            "--clear",
        ]
    )
    run(
        [
            "uv",
            "build",
            "--python",
            args.python_version,
            "--no-python-downloads",
            "--package",
            PACKAGE_NAME,
            "--out-dir",
            str(dist_dir),
            "--clear",
        ]
    )

    core_wheel: Path = get_wheel_path(
        core_dist_dir, f"{CORE_PACKAGE_NAME.replace('-', '_')}-*.whl"
    )
    stbkit_wheel: Path = get_wheel_path(dist_dir, f"{PACKAGE_NAME}-*.whl")
    core_sdist: Path = get_wheel_path(core_dist_dir, "*.tar.gz")
    stbkit_sdist: Path = get_wheel_path(dist_dir, "*.tar.gz")

    for artifact in (core_wheel, stbkit_wheel, core_sdist, stbkit_sdist):
        check_license(artifact)

    smoke_code: str = f"""from importlib.metadata import version
import subprocess
import sys
import stbkit.core
import stbkit.tools
expected = {stbkit_version!r}
stbkit_v = version('{PACKAGE_NAME}')
core_v = version('{CORE_PACKAGE_NAME}')
if stbkit_v != expected:
    raise RuntimeError(
        f'{PACKAGE_NAME}のバージョンが一致しません: {{stbkit_v}} != {{expected}}'
    )
if core_v != expected:
    raise RuntimeError(
        f'{CORE_PACKAGE_NAME}のバージョンが一致しません: {{core_v}} != {{expected}}'
    )
proc = subprocess.run(
    [sys.executable, '-m', '{PACKAGE_NAME}', '--help'],
    check=True,
    capture_output=True,
    text=True,
)
if ('usage' not in proc.stdout.lower()
    and 'usage' not in proc.stderr.lower()):
    raise RuntimeError(
        '{PACKAGE_NAME}のCLIが動いていません'
    )
import stbkit.api
stb = stbkit.api.load_latest({FIXTURE_PATH_STR!r})
print("project_name:" + stb.stb_common.project_name)
if stb.stb_common.project_name != 'column_rc':
    raise RuntimeError(f'loadに失敗しました')
print('{PACKAGE_NAME} smoke check passed:', stbkit_v, core_v)
        """
    run(
        [
            "uv",
            "venv",
            str(smoke_venv_wheel_dir),
            "--python",
            args.python_version,
            "--no-python-downloads",
        ]
    )
    venv_python: Path = get_venv_python(smoke_venv_wheel_dir)
    run(
        [
            "uv",
            "pip",
            "install",
            "--python",
            str(venv_python),
            "--no-deps",
            str(core_wheel),
            str(stbkit_wheel),
        ]
    )
    run([str(venv_python), "-c", smoke_code])

    run(
        [
            "uv",
            "venv",
            str(smoke_venv_sdist_dir),
            "--python",
            args.python_version,
            "--no-python-downloads",
        ]
    )
    sdist_venv_python: Path = get_venv_python(smoke_venv_sdist_dir)
    run(
        [
            "uv",
            "pip",
            "install",
            "--python",
            str(sdist_venv_python),
            "--no-deps",
            str(core_sdist),
            str(stbkit_sdist),
        ]
    )
    run([str(sdist_venv_python), "-c", smoke_code])

    print("Release verification succeeded for stbkit", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
