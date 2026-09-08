# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import shutil
import sys
from pathlib import Path
from typing import Final

from release_check_common import (
    check_license,
    get_tag_version,
    get_venv_python,
    get_version,
    get_wheel_path,
    run,
)

PACKAGE_NAME: Final = "stbkit-core"
TAG_PREFIX: Final = "stbkit-core-v"
FIXTURE_PATH: Final = (
    Path.cwd()
    / "tests"
    / "fixtures"
    / "cases"
    / "column_rc"
    / "column_rc.stb_v2_1_1.stb"
)
FIXTURE_PATH_STR: Final = str(FIXTURE_PATH)


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--python-version", default="3.14")
    args: argparse.Namespace = parser.parse_args()

    root_path: Path = Path.cwd()
    package_dir: Path = root_path / "python" / PACKAGE_NAME
    pyproject_path: Path = package_dir / "pyproject.toml"
    dist_dir: Path = root_path / "dist"
    smoke_venv_wheel_dir: Path = root_path / f".venv-release-smoke-wheel-{PACKAGE_NAME}"
    smoke_venv_sdist_dir: Path = root_path / f".venv-release-smoke-sdist-{PACKAGE_NAME}"

    tag_version: str = get_tag_version(args.tag, TAG_PREFIX)
    package_version: str = get_version(pyproject_path)
    if tag_version != package_version:
        raise RuntimeError(
            "tagのバージョンとpyprojectのバージョンが一致しません: "
            f"tag={tag_version}, pyproject={package_version}"
        )

    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    if smoke_venv_wheel_dir.exists():
        shutil.rmtree(smoke_venv_wheel_dir)
    if smoke_venv_sdist_dir.exists():
        shutil.rmtree(smoke_venv_sdist_dir)

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

    wheel_path: Path = get_wheel_path(
        dist_dir, f"{PACKAGE_NAME.replace('-', '_')}-*.whl"
    )
    sdist_path: Path = get_wheel_path(dist_dir, "*.tar.gz")

    check_license(wheel_path)
    check_license(sdist_path)

    smoke_code: str = f"""from importlib.metadata import version
import stbkit.core
installed = version('{PACKAGE_NAME}')
expected = {package_version!r}
if installed != expected:
    raise RuntimeError(f'versionが一致しません: {{installed}} != {{expected}}')
from stbkit.core.stb_io import load
stb=load({FIXTURE_PATH_STR!r})
print("project_name:" + stb.stb_common.project_name)
if stb.stb_common.project_name != 'column_rc':
    raise RuntimeError(f'loadに失敗しました')
print('{PACKAGE_NAME} smoke check passed:', installed)
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
            str(wheel_path),
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
            str(sdist_path),
        ]
    )
    run([str(sdist_venv_python), "-c", smoke_code])

    print("Release check succeeded for stbkit-core", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
