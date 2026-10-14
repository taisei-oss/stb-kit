from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from email.message import Message
from email.parser import Parser
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
from release_check_stbkit import check_core_dependency

PACKAGE_NAME: Final = "stbkit-native"
CORE_PACKAGE_NAME: Final = "stbkit-core"
STBKIT_PACKAGE_NAME: Final = "stbkit"
TAG_PREFIX: Final = "stbkit-native-v"
FIXTURE_PATH: Final = (
    Path.cwd()
    / "tests"
    / "fixtures"
    / "cases"
    / "column_rc"
    / "column_rc.stb_v2_1_1.stb"
)
FIXTURE_PATH_STR: Final = str(FIXTURE_PATH)


def check_native_wheel(wheel: Path, target: str, version: str) -> None:
    if wheel.name.split("-")[-3:-1] != ["cp312", "abi3"]:
        raise RuntimeError("native wheelはcp312-abi3である必要があります")
    with zipfile.ZipFile(wheel) as archive:
        names: set[str] = set(archive.namelist())
        wheel_metadata_path: str = next(
            name for name in names if name.endswith(".dist-info/WHEEL")
        )
        wheel_metadata: Message[str, str] = Parser().parsestr(
            archive.read(wheel_metadata_path).decode("utf-8")
        )
        tags: list[str] = wheel_metadata.get_all("Tag", [])
        if not tags or any(not tag.startswith("cp312-abi3-") for tag in tags):
            raise RuntimeError("native wheelのTagはcp312-abi3である必要があります")
        metadata_path: str = next(
            name for name in names if name.endswith(".dist-info/METADATA")
        )
        metadata: Message[str, str] = Parser().parsestr(
            archive.read(metadata_path).decode("utf-8")
        )
        if metadata["Name"] != PACKAGE_NAME or metadata["Version"] != version:
            raise RuntimeError("native wheelのバージョンが異なります")
        if metadata.get_all("Requires-Dist", []):
            raise RuntimeError("native wheelに依存が含まれています")
        unexpected: list[str] = [
            name
            for name in names
            if name.startswith("stbkit/")
            and not name.endswith("/")
            and (not name.startswith("stbkit/_native/") or name.endswith(".py"))
        ]
        if unexpected:
            raise RuntimeError(
                f"native wheelにPythonを上書きするファイルがあります: {unexpected}"
            )
        for required in ("stbkit_native_rs.pyi", "py.typed"):
            if f"stbkit/_native/{required}" not in names:
                raise RuntimeError(
                    f"nativeの型情報ファイルが見つかりません: {required}"
                )
        extensions: list[str] = [
            name
            for name in names
            if name.startswith("stbkit/_native/stbkit_native_rs")
            and name.endswith((".so", ".pyd"))
        ]
        if len(extensions) != 1:
            raise RuntimeError(f"native拡張がありません: {extensions}")
        for name in names:
            if name.endswith(".dist-info/entry_points.txt") and (
                "[stbkit.commands]" in archive.read(name).decode("utf-8")
            ):
                raise RuntimeError("native wheelにはCLIコマンドを登録しません")
        for filename in ("THIRD_PARTY_LICENSES.html", "THIRD_PARTY_NOTICES.html"):
            text: str = archive.read(f"stbkit/_native/{filename}").decode("utf-8")
            if target not in text:
                raise RuntimeError(
                    f"{filename}にターゲット{target}の記載が見つかりません"
                )
            if filename == "THIRD_PARTY_LICENSES.html" and "MIT" not in text:
                raise RuntimeError(f"{filename}にMITライセンスの記載が見つかりません")


def check_versions(
    tag: str,
    package_data: dict[str, Any],
    cargo_data: dict[str, Any],
    core_data: dict[str, Any],
    stbkit_data: dict[str, Any],
) -> str:
    tag_version: str = get_tag_version(tag, TAG_PREFIX)
    package_version: str = str(package_data["project"]["version"])
    cargo_version: str = str(cargo_data["package"]["version"])
    core_version: str = str(core_data["project"]["version"])
    stbkit_version: str = str(stbkit_data["project"]["version"])

    if tag_version != package_version:
        raise RuntimeError(
            "tagのバージョンとpyprojectのバージョンが一致しません: "
            f"tag={tag_version}, pyproject={package_version}"
        )
    cargo_version_match: re.Match[str] | None = re.fullmatch(
        r"(?P<release>\d+\.\d+\.\d+)"
        r"(?:-(?P<stage>alpha|beta|rc|dev)\.(?P<number>\d+))?",
        cargo_version,
    )
    if cargo_version_match is None:
        raise RuntimeError(f"Cargoのバージョン表記に対応していません: {cargo_version}")
    cargo_python_version: str = cargo_version_match.group("release")
    cargo_stage: str | None = cargo_version_match.group("stage")
    if cargo_stage is not None:
        python_stages: dict[str, str] = {
            "alpha": "a",
            "beta": "b",
            "rc": "rc",
            "dev": ".dev",
        }
        cargo_python_version += python_stages[cargo_stage] + cargo_version_match.group(
            "number"
        )
    if cargo_python_version != package_version:
        raise RuntimeError(
            "Cargoとpyprojectのバージョンが一致しません: "
            f"Cargo={cargo_version} (Python表記: {cargo_python_version}), "
            f"pyproject={package_version}"
        )
    check_core_dependency(stbkit_data, stbkit_version)
    if core_version != package_version or stbkit_version != package_version:
        raise RuntimeError(
            "開発初期段階のため、各パッケージのバージョンは一致している必要があります: "
            f"{CORE_PACKAGE_NAME}={core_version}, "
            f"{STBKIT_PACKAGE_NAME}={stbkit_version}, "
            f"{PACKAGE_NAME}={package_version}"
        )
    for extra in ("native", "full"):
        dependencies: list[str] = stbkit_data["project"]["optional-dependencies"][extra]
        if f"{PACKAGE_NAME}=={package_version}" not in dependencies:
            raise RuntimeError(
                f"追加依存{extra}に{PACKAGE_NAME}=={package_version}が宣言されていません"
            )

    return package_version


def main() -> int:
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--python-version", default="3.12")
    parser.add_argument("--test-python-versions", nargs="+")
    parser.add_argument("--compatibility", default="off")
    parser.add_argument("--sdist", action="store_true")
    args: argparse.Namespace = parser.parse_args()

    root_path: Path = Path.cwd()
    package_dir: Path = root_path / "rust" / PACKAGE_NAME
    pyproject_path: Path = package_dir / "pyproject.toml"
    manifest_path: Path = package_dir / "Cargo.toml"
    core_pyproject: Path = root_path / "python" / CORE_PACKAGE_NAME / "pyproject.toml"
    stbkit_pyproject: Path = (
        root_path / "python" / STBKIT_PACKAGE_NAME / "pyproject.toml"
    )

    dist_dir: Path = root_path / "dist"
    core_dist_dir: Path = root_path / "dist-stbkit-core"
    stbkit_dist_dir: Path = root_path / "dist-stbkit"
    smoke_venv_wheel_dir: Path = root_path / f".venv-release-smoke-wheel-{PACKAGE_NAME}"
    smoke_venv_sdist_dir: Path = root_path / f".venv-release-smoke-sdist-{PACKAGE_NAME}"

    package_data: dict[str, Any] = get_pyproject_dict(pyproject_path)
    cargo_data: dict[str, Any] = get_pyproject_dict(manifest_path)
    core_data: dict[str, Any] = get_pyproject_dict(core_pyproject)
    stbkit_data: dict[str, Any] = get_pyproject_dict(stbkit_pyproject)
    package_version: str = check_versions(
        args.tag, package_data, cargo_data, core_data, stbkit_data
    )

    for directory in (dist_dir, core_dist_dir, stbkit_dist_dir, smoke_venv_wheel_dir):
        if directory.exists():
            shutil.rmtree(directory)
    if args.sdist and smoke_venv_sdist_dir.exists():
        shutil.rmtree(smoke_venv_sdist_dir)

    run(
        [
            "uv",
            "build",
            "--wheel",
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
            "--wheel",
            "--python",
            args.python_version,
            "--no-python-downloads",
            "--package",
            STBKIT_PACKAGE_NAME,
            "--out-dir",
            str(stbkit_dist_dir),
            "--clear",
        ]
    )
    run(
        [
            sys.executable,
            "scripts/generate_third_party_licenses.py",
            "native",
            "--target",
            args.target,
        ]
    )
    build_python: str = subprocess.check_output(
        ["uv", "python", "find", args.python_version, "--no-python-downloads"],
        text=True,
    ).strip()
    run(
        [
            "uv",
            "tool",
            "run",
            "maturin",
            "build",
            "--manifest-path",
            str(manifest_path),
            "--release",
            "--locked",
            "--target",
            args.target,
            "--interpreter",
            build_python,
            "--compatibility",
            args.compatibility,
            "--out",
            str(dist_dir),
        ]
    )
    if args.sdist:
        run(
            [
                "uv",
                "tool",
                "run",
                "--from",
                "maturin>=1.15,<2",
                "maturin",
                "sdist",
                "--manifest-path",
                str(manifest_path),
                "--out",
                str(dist_dir),
            ]
        )

    core_wheel: Path = get_wheel_path(
        core_dist_dir, f"{CORE_PACKAGE_NAME.replace('-', '_')}-*.whl"
    )
    stbkit_wheel: Path = get_wheel_path(stbkit_dist_dir, f"{STBKIT_PACKAGE_NAME}-*.whl")
    wheel_path: Path = get_wheel_path(
        dist_dir, f"{PACKAGE_NAME.replace('-', '_')}-*.whl"
    )
    for wheel in (core_wheel, stbkit_wheel, wheel_path):
        check_license(wheel)
    check_native_wheel(wheel_path, args.target, package_version)

    smoke_code: str = f"""from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
import json
from pathlib import Path
import subprocess
import sys
from types import ModuleType
import stbkit
import stbkit.api
import stbkit.core.stb_io
import stbkit.tools
from stbkit.core.data_model import stb_v2_1_1
from stbkit.core.data_model.common import StBridgeRoot

expected: str = {package_version!r}
native: bool = sys.argv[2] == 'native'
for package in ('stbkit-core', 'stbkit'):
    if version(package) != expected:
        raise RuntimeError('インストール済みのバージョンが一致しません: ' + package)
if stbkit.__spec__ is None or stbkit.__spec__.origin is not None:
    raise RuntimeError('stbkitの名前空間パッケージが維持されていません')
if native:
    import stbkit.native
    backend: ModuleType = import_module('stbkit._native.stbkit_native_rs')
    if version('stbkit-native') != expected:
        raise RuntimeError('インストール済みのstbkit-nativeのバージョンが一致しません')
    if not callable(backend._run_viewer):
        raise RuntimeError('nativeのビューア起動関数が見つかりません')
else:
    try:
        version('stbkit-native')
    except PackageNotFoundError:
        pass
    else:
        raise RuntimeError('比較用の基準環境にstbkit-nativeがインストールされています')

stb: stb_v2_1_1.StBridge = stbkit.api.load_latest({FIXTURE_PATH_STR!r})
if stb.stb_common.project_name != 'column_rc':
    raise RuntimeError('STBの読み込みに失敗しました')
xml: str = stbkit.core.stb_io.dumps(stb)
roundtrip: StBridgeRoot = stbkit.core.stb_io.loads(xml)
if stbkit.core.stb_io.dumps(roundtrip) != xml:
    raise RuntimeError('STBの書き出し・再読み込みの結果が一致しません')
cli: subprocess.CompletedProcess[str] = subprocess.run(
    [sys.executable, '-X', 'utf8', '-m', 'stbkit', '--help'],
    check=True, capture_output=True, text=True, encoding='utf-8',
)
if 'usage' not in (cli.stdout + cli.stderr).lower():
    raise RuntimeError('stbkitのCLIヘルプが動いていません')
result: dict[str, str] = {{
    'xml': xml, 'cli_stdout': cli.stdout, 'cli_stderr': cli.stderr,
}}
snapshot: Path = Path(sys.argv[1])
if native:
    baseline: dict[str, str] = json.loads(snapshot.read_text(encoding='utf-8'))
    if result != baseline:
        raise RuntimeError(
            'nativeの導入前後でPythonの読み書きまたはCLIの結果が変わりました'
        )
else:
    snapshot.write_text(json.dumps(result), encoding='utf-8')
print('Release smoke check passed; native:', native)
"""
    test_python_versions: list[str] = args.test_python_versions or [args.python_version]
    for python_version in test_python_versions:
        run(
            [
                "uv",
                "venv",
                str(smoke_venv_wheel_dir),
                "--clear",
                "--python",
                python_version,
                "--no-python-downloads",
            ]
        )
        venv_python: Path = get_venv_python(smoke_venv_wheel_dir)
        snapshot_path: Path = smoke_venv_wheel_dir / "baseline.json"
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
        run([str(venv_python), "-I", "-c", smoke_code, str(snapshot_path), "baseline"])
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
        run(["uv", "pip", "check", "--python", str(venv_python)])
        run([str(venv_python), "-I", "-c", smoke_code, str(snapshot_path), "native"])

    if args.sdist:
        sdist_path: Path = get_wheel_path(dist_dir, "*.tar.gz")
        check_license(sdist_path)
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
        sdist_snapshot_path: Path = smoke_venv_sdist_dir / "baseline.json"
        run(
            [
                "uv",
                "pip",
                "install",
                "--python",
                str(sdist_venv_python),
                "--no-deps",
                str(core_wheel),
                str(stbkit_wheel),
            ]
        )
        run(
            [
                str(sdist_venv_python),
                "-I",
                "-c",
                smoke_code,
                str(sdist_snapshot_path),
                "baseline",
            ]
        )
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
        run(["uv", "pip", "check", "--python", str(sdist_venv_python)])
        run(
            [
                str(sdist_venv_python),
                "-I",
                "-c",
                smoke_code,
                str(sdist_snapshot_path),
                "native",
            ]
        )

    print("Release verification succeeded for stbkit-native", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
