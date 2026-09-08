# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import subprocess
import tarfile
import tomllib
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def get_pyproject_dict(pyproject_path: Path) -> dict[str, Any]:
    data: dict[str, Any] = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
    return data


def get_version(pyproject_path: Path) -> str:
    data: dict[str, Any] = get_pyproject_dict(pyproject_path)
    return str(data["project"]["version"])


def get_tag_version(tag: str, prefix: str) -> str:
    if not tag.startswith(prefix):
        raise ValueError(f"tagは[{prefix}]で始まる必要があります: {tag}")
    version: str = tag[len(prefix) :]
    if not version:
        raise ValueError("tagのバージョン部分が空です")
    return version


def get_wheel_path(dist_dir: Path, pattern: str) -> Path:
    wheels: list[Path] = sorted(dist_dir.glob(pattern))
    if len(wheels) != 1:
        raise RuntimeError(
            f"wheelの数が1ではありません:。expected:{pattern}, actual: {wheels}"
        )
    return wheels[0]


def get_venv_python(venv_dir: Path) -> Path:
    venv_paths: tuple[Path, Path] = (
        venv_dir / "bin" / "python",
        venv_dir / "Scripts" / "python.exe",
    )
    for path in venv_paths:
        if path.exists():
            return path
    return venv_paths[0]


def _check_license_text(license_text: str, metadata_text: str) -> None:
    if "Mozilla Public License Version 2.0" not in license_text:
        raise RuntimeError("LICENSEにMPL-2.0の記載が見つかりません")
    if "MPL-2.0" not in metadata_text or "License-File: LICENSE" not in metadata_text:
        raise RuntimeError("METADATAにライセンスの記載が見つかりません")


def check_license(artifact: Path) -> None:
    if artifact.suffix == ".whl":
        with zipfile.ZipFile(artifact) as zf:
            names: list[str] = zf.namelist()
            license_file: str | None = None
            metadata_file: str | None = None
            for name in names:
                if name.endswith("LICENSE"):
                    license_file = name
                if name.endswith(".dist-info/METADATA"):
                    metadata_file = name
            if not license_file:
                raise RuntimeError("LICENSEファイルが見つかりません")
            if not metadata_file:
                raise RuntimeError("METADATAファイルが見つかりません")
            _check_license_text(
                license_text=zf.read(license_file).decode("utf-8"),
                metadata_text=zf.read(metadata_file).decode("utf-8"),
            )
        return

    if artifact.suffixes[-2:] == [".tar", ".gz"]:
        with tarfile.open(artifact, "r:gz") as tf:
            members: list[tarfile.TarInfo] = tf.getmembers()
            license_member: tarfile.TarInfo | None = next(
                (
                    member
                    for member in members
                    if member.isfile() and member.name.endswith("LICENSE")
                ),
                None,
            )
            metadata_member: tarfile.TarInfo | None = next(
                (
                    member
                    for member in members
                    if member.isfile() and PurePosixPath(member.name).name == "PKG-INFO"
                ),
                None,
            )
            if not license_member:
                raise RuntimeError("LICENSEファイルが見つかりません")
            if not metadata_member:
                raise RuntimeError("PKG-INFOファイルが見つかりません")
            license_fp = tf.extractfile(license_member)
            if not license_fp:
                raise RuntimeError("LICENSEファイルが読み込めません")
            license_text = license_fp.read().decode("utf-8")
            metadata_fp = tf.extractfile(metadata_member)
            if not metadata_fp:
                raise RuntimeError("PKG-INFOファイルが読み込めません")
            metadata_text = metadata_fp.read().decode("utf-8")
            _check_license_text(license_text=license_text, metadata_text=metadata_text)

        return

    raise RuntimeError(f"不明なのアーティファクト形式です: {artifact.name}")
