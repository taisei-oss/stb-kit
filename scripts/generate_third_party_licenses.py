# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final, Never

LICENSES_FILE_NAME: Final = "THIRD_PARTY_LICENSES.html"
NOTICES_FILE_NAME: Final = "THIRD_PARTY_NOTICES.html"
WEB_TARGET: Final = "wasm32-unknown-unknown"
CARGO_ABOUT_VERSION: Final = "0.9.2"
NOTICE_FILE_NAME_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^(?:(?:third[-_. ]?party[-_. ]?)?notices?)(?:$|[-_. ].*)",
    re.IGNORECASE,
)
IGNORE_NOTICE_DIRECTORIES: Final = frozenset(
    {".git", ".hg", ".svn", "__pycache__", "node_modules", "target"}
)


class LicenseGenerationError(RuntimeError):
    """第三者ライセンス生成時エラー"""


@dataclass(frozen=True)
class WheelData:
    name: str
    manifest_path: Path
    output_dir_path: Path
    targets: tuple[str, ...]


@dataclass(frozen=True)
class CargoPackageData:
    package_id: str
    name: str
    version: str
    path: Path
    repository: str | None
    source: str | None

    @property
    def label(self) -> str:
        return f"{self.name} v{self.version}"


@dataclass(frozen=True)
class PackageLicense:
    package: CargoPackageData
    license: str


@dataclass(frozen=True)
class LicenseEntry:
    id: str
    name: str
    text: str
    packages: tuple[CargoPackageData, ...]


@dataclass(frozen=True)
class CargoAboutJson:
    packages: tuple[PackageLicense, ...]
    licenses: tuple[LicenseEntry, ...]


@dataclass(frozen=True, order=True)
class NoticeReference:
    package_name: str
    package_version: str
    relative_path: str

    @property
    def package_label(self) -> str:
        return f"{self.package_name} v{self.package_version}"


@dataclass(frozen=True)
class NoticeGroup:
    text: str
    references: tuple[NoticeReference, ...]


@dataclass(frozen=True)
class ResultDocuments:
    licenses: str
    notices: str


def create_cargo_about_command(
    wheel_data: WheelData,
    config_path: Path,
    output_file_path: Path,
    *,
    offline: bool,
) -> list[str]:
    command: list[str] = [
        "cargo",
        "about",
        "generate",
        "--manifest-path",
        str(wheel_data.manifest_path),
        "--config",
        str(config_path),
        "--format",
        "json",
        "--output-file",
        str(output_file_path),
        "--locked",
        "--fail",
    ]
    for target in wheel_data.targets:
        command.extend(("--target", target))
    if offline:
        command.append("--offline")
    return command


def run_cargo_about(command: Sequence[str], repository_root: Path) -> None:
    if shutil.which(command[0]) is None:
        raise LicenseGenerationError(
            "Cargoが見つかりません\n"
            "Rustツールチェーンをインストールしてから再実行してください。"
        )

    completed = subprocess.run(
        list(command),
        cwd=repository_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if completed.stderr.strip():
        print(completed.stderr.rstrip(), file=sys.stderr)
    if completed.returncode == 0:
        return

    raise LicenseGenerationError(
        f"cargo-aboutの実行に失敗しました（終了コード: {completed.returncode}）。"
    )


def load_cargo_about_output(
    output_path: Path,
    repository_root: Path,
) -> CargoAboutJson:
    try:
        output_data: Any = json.loads(output_path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise LicenseGenerationError(
            f"cargo-aboutのJSON出力が見つかりません: {output_path}"
        ) from error
    except json.JSONDecodeError as error:
        raise LicenseGenerationError(
            f"cargo-aboutのJSON出力をloadできません: {error}"
        ) from error

    crates = output_data.get("crates")
    licenses = output_data.get("licenses")

    package_licenses: list[PackageLicense] = []
    package_cache: dict[str, CargoPackageData] = {}
    for index, crate in enumerate(crates):
        package = _parse_package(
            crate.get("package"),
            repository_root,
            f"crates[{index}].package",
        )
        package_cache[package.package_id] = package
        package_licenses.append(
            PackageLicense(package=package, license=crate.get("license")),
        )

    license_entries: list[LicenseEntry] = []
    for index, license in enumerate(licenses):
        raw_used_by = license.get("used_by")
        used_by: dict[str, CargoPackageData] = {}
        for use_index, use in enumerate(raw_used_by):
            package = _parse_package(
                use.get("crate"),
                repository_root,
                f"licenses[{index}].used_by[{use_index}].crate",
            )
            package = package_cache.get(package.package_id, package)
            used_by[package.package_id] = package

        license_entries.append(
            LicenseEntry(
                id=license.get("id"),
                name=license.get("name"),
                text=license.get("text"),
                packages=tuple(
                    sorted(
                        used_by.values(),
                        key=_package_sort_key,
                    )
                ),
            )
        )

    return CargoAboutJson(
        packages=tuple(
            sorted(
                package_licenses,
                key=lambda entry: _package_sort_key(entry.package),
            )
        ),
        licenses=tuple(
            sorted(
                license_entries,
                key=lambda entry: (entry.id, entry.name, entry.text),
            )
        ),
    )


def collect_notice_groups(
    cargo_about_json: CargoAboutJson,
    repository_root: Path,
) -> tuple[NoticeGroup, ...]:
    notice_references: dict[str, set[NoticeReference]] = defaultdict(set)
    packages = _unique_packages(
        entry.package
        for entry in cargo_about_json.packages
        if _is_third_party_package(entry.package, repository_root)
    )

    for package in packages:
        package_root = package.path.parent
        if not package.path.is_file():
            raise LicenseGenerationError(
                f"NOTICEを探索するcrateのCargo.tomlが見つかりません: {package.label}"
            )

        for notice_path in _iter_notice_files(package_root):
            text = _read_notice_text(notice_path)
            if not text:
                continue
            notice_references[text].add(
                NoticeReference(
                    package_name=package.name,
                    package_version=package.version,
                    relative_path=notice_path.relative_to(package_root).as_posix(),
                )
            )

    groups = [
        NoticeGroup(text=text, references=tuple(sorted(references)))
        for text, references in notice_references.items()
    ]
    return tuple(
        sorted(
            groups,
            key=lambda group: (
                group.references[0].package_name,
                group.references[0].package_version,
                group.references[0].relative_path,
                hashlib.sha256(group.text.encode("utf-8")).hexdigest(),
            ),
        )
    )


def render_documents(
    cargo_about_json: CargoAboutJson,
    notice_groups: Sequence[NoticeGroup],
    wheel_data: WheelData,
    repository_root: Path,
) -> ResultDocuments:
    lock_bytes: bytes = (repository_root / "Cargo.lock").read_bytes()
    lock_hash: str = hashlib.sha256(lock_bytes).hexdigest()
    return ResultDocuments(
        licenses=_render_licenses_html(
            cargo_about_json, wheel_data, repository_root, lock_hash
        ),
        notices=_render_notices_html(notice_groups, wheel_data, lock_hash),
    )


def write_documents(
    documents: ResultDocuments,
    output_dir: Path,
    *,
    check: bool,
) -> None:
    outputs: dict[str, str] = {
        LICENSES_FILE_NAME: documents.licenses,
        NOTICES_FILE_NAME: documents.notices,
    }
    ng_files: list[Path] = []

    for file_name, content in outputs.items():
        output_path: Path = output_dir / file_name
        if check:
            current = (
                output_path.read_text(encoding="utf-8")
                if output_path.is_file()
                else None
            )
            if current != content:
                ng_files.append(output_path)
            continue

        output_dir.mkdir(parents=True, exist_ok=True)
        if output_path.is_file() and output_path.read_text(encoding="utf-8") == content:
            print(f"更新不要: {output_path}")
            continue
        output_path.write_text(content, encoding="utf-8")
        print(f"更新しました: {output_path}")

    if ng_files:
        paths = "\n".join(f"- {path}" for path in ng_files)
        raise LicenseGenerationError(
            "第三者ライセンスファイルが未生成または古くなっています。\n"
            f"{paths}\n"
            "--checkを外して再生成してください。"
        )
    if check:
        print("第三者ライセンスファイルは最新です。")


def generate_third_party_documents(
    wheel_data: WheelData,
    repository_root: Path,
    *,
    offline: bool,
    check: bool,
) -> None:
    about_config_path: Path = repository_root / "about.toml"
    if not about_config_path.is_file():
        raise LicenseGenerationError(
            f"cargo-about設定が見つかりません: {about_config_path}"
        )
    if not wheel_data.manifest_path.is_file():
        raise LicenseGenerationError(
            f"Cargo.tomlが見つかりません: {wheel_data.manifest_path}"
        )
    print("サードパーティライセンスファイルを作成します")
    print(f"対象: {wheel_data.name}")
    print(f"ターゲット: {', '.join(wheel_data.targets)}")

    with tempfile.TemporaryDirectory(prefix="stbkit-third-party-") as temp_dir:
        output_path: Path = Path(temp_dir) / "cargo-about.json"
        command: list[str] = create_cargo_about_command(
            wheel_data,
            about_config_path,
            output_path,
            offline=offline,
        )
        run_cargo_about(command, repository_root)
        cargo_about_json = load_cargo_about_output(output_path, repository_root)
        notices = collect_notice_groups(cargo_about_json, repository_root)
        documents = render_documents(
            cargo_about_json, notices, wheel_data, repository_root
        )
        write_documents(documents, wheel_data.output_dir_path, check=check)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="crate-third-party-licenses",
        description=("cargo-aboutを用いて、第三者ライセンスとNOTICEを生成します。"),
    )
    subparsers = parser.add_subparsers(dest="package_type", required=True)

    native_parser = subparsers.add_parser(
        "native",
        help="stbkit-native wheel用のHTMLを生成します。",
    )
    _add_common_arguments(native_parser)
    native_parser.add_argument(
        "--target",
        action="append",
        help=(
            "wheelをビルドするRustターゲット。"
            "省略時は現在の環境のターゲットを使用します。"
            "複数アーキテクチャを含むwheelでは複数回指定します。"
        ),
    )

    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    try:
        repository_root: Path = (
            args.repository_root
            if args.repository_root is not None
            else Path(__file__).parent.parent
        ).resolve()
        output_dir = _get_output_dir(
            args.output_dir,
            repository_root,
            args.package_type,
        )
        package_type = args.package_type
        if package_type == "native":
            targets = (
                (_get_host_target(repository_root),)
                if args.target is None
                else _normalize_targets(args.target)
            )
            wheel_data = WheelData(
                name="stbkit-native wheel",
                manifest_path=repository_root / "rust/stbkit-native/Cargo.toml",
                output_dir_path=output_dir,
                targets=targets,
            )
        else:
            raise LicenseGenerationError(f"未知のパッケージタイプです: {package_type}")

        generate_third_party_documents(
            wheel_data,
            repository_root,
            offline=args.offline,
            check=args.check,
        )
    except LicenseGenerationError as error:
        parser.exit(1, f"エラー: {error}\n")


def _add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--repository-root",
        type=Path,
        help="リポジトリルート。指定しない場合は二つ上のディレクトリ",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="出力先",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="cargo-aboutをオフラインで実行する",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="ファイルを更新せず、生成結果と一致するか確認する",
    )


def _get_output_dir(
    output_dir: Path | None,
    repository_root: Path,
    package_type: str,
) -> Path:
    if output_dir is None:
        relative = (
            Path("rust/stbkit-native/python/stbkit/_native")
            if package_type == "native"
            else Path("rust/stbkit-web/web/pkg")
        )
        return repository_root / relative
    if output_dir.is_absolute():
        return output_dir
    return repository_root / output_dir


def _get_host_target(repository_root: Path) -> str:
    try:
        completed = subprocess.run(
            ["rustc", "-vV"],
            cwd=repository_root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except OSError as error:
        raise LicenseGenerationError(
            "rustcを実行できません。Rustツールチェーンを確認してください。"
        ) from error
    if completed.returncode != 0:
        raise LicenseGenerationError(
            "Rustのホストターゲットを取得できませんでした。"
            f"（終了コード: {completed.returncode}）"
        )
    for line in completed.stdout.splitlines():
        if line.startswith("host:"):
            target = line.removeprefix("host:").strip()
            if target:
                return target
    raise LicenseGenerationError("rustcの出力にホストターゲットがありません。")


def _normalize_targets(targets: Sequence[str]) -> tuple[str, ...]:
    normalized = tuple(
        dict.fromkeys(target.strip() for target in targets if target.strip())
    )
    if not normalized:
        raise LicenseGenerationError("Rustターゲットを1件以上指定してください。")
    return normalized


def _raise_error(message: str) -> Never:
    raise LicenseGenerationError(message)


def _parse_package(
    package: dict[str, Any],
    repository_root: Path,
    context: str,
) -> CargoPackageData:
    name = package.get("name") or _raise_error(f"{context}.nameが存在しません。")
    version = package.get("version") or _raise_error(
        f"{context}.versionが存在しません。"
    )
    manifest_path_str = package.get("manifest_path") or _raise_error(
        f"{context}.manifest_pathが存在しません。"
    )
    raw_manifest_path = Path(manifest_path_str)
    manifest_path = (
        raw_manifest_path
        if raw_manifest_path.is_absolute()
        else repository_root / raw_manifest_path
    ).resolve()
    package_id = package.get("id")
    return CargoPackageData(
        package_id=package_id or f"{name} {version} ({manifest_path})",
        name=name,
        version=version,
        path=manifest_path,
        repository=package.get("repository"),
        source=package.get("source"),
    )


def _unique_packages(
    packages: Iterable[CargoPackageData],
) -> tuple[CargoPackageData, ...]:
    unique: dict[str, CargoPackageData] = {}
    for package in packages:
        unique[package.package_id] = package
    return tuple(sorted(unique.values(), key=_package_sort_key))


def _package_sort_key(package: CargoPackageData) -> tuple[str, str, str]:
    return package.name, package.version, package.package_id


def _is_third_party_package(package: CargoPackageData, repository_root: Path) -> bool:
    if package.source is not None:
        return True
    return not _is_relative_to(package.path, repository_root)


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError:
        return False
    return True


def _iter_notice_files(package_root: Path) -> tuple[Path, ...]:
    notice_files: list[Path] = []
    resolved_root = package_root.resolve()
    for current_root, directories, files in os.walk(package_root, followlinks=False):
        directories[:] = sorted(
            directory
            for directory in directories
            if directory not in IGNORE_NOTICE_DIRECTORIES
            and not (Path(current_root) / directory).is_symlink()
        )
        for file_name in sorted(files):
            if NOTICE_FILE_NAME_PATTERN.match(file_name) is None:
                continue
            path = Path(current_root) / file_name
            if not path.is_file() or not _is_relative_to(path, resolved_root):
                continue
            notice_files.append(path)
    return tuple(notice_files)


def _read_notice_text(path: Path) -> str:
    raw = path.read_bytes()
    if b"\x00" in raw:
        raise LicenseGenerationError(f"NOTICEファイルがテキストではありません: {path}")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def _render_licenses_html(
    cargo_about_json: CargoAboutJson,
    wheel_data: WheelData,
    repository_root: Path,
    lock_hash: str,
) -> str:
    package_licensess = tuple(
        entry
        for entry in cargo_about_json.packages
        if _is_third_party_package(entry.package, repository_root)
    )
    package_rows = "\n".join(_render_package_row(entry) for entry in package_licensess)

    license_sections: list[str] = []
    for license in cargo_about_json.licenses:
        packages = _unique_packages(
            tuple(
                package
                for package in license.packages
                if _is_third_party_package(package, repository_root)
            )
        )
        if not packages:
            continue
        anchor = _content_anchor(
            "license",
            f"{license.id}\n{license.text}",
        )
        package_items = "\n".join(
            f"<li>{html.escape(package.label)}</li>" for package in packages
        )
        license_sections.append(
            "\n".join(
                (
                    f'<section class="document" id="{anchor}">',
                    f"<h2>{html.escape(license.name)} ({html.escape(license.id)})</h2>",
                    "<h3>使用しているcrate</h3>",
                    f"<ul>{package_items}</ul>",
                    f"<pre>{html.escape(license.text)}</pre>",
                    "</section>",
                )
            )
        )

    body = "\n".join(
        (
            "<h1>Third-Party Licenses</h1>",
            "<p>このファイルはcargo-aboutのターゲット別依存グラフから自動生成されています。</p>",
            _render_build_metadata(wheel_data, lock_hash),
            "<h2>対象crate</h2>",
            "<table><thead><tr><th>crate</th><th>ライセンス式</th>"
            "<th>リポジトリ</th></tr></thead>",
            f"<tbody>{package_rows}</tbody></table>",
            "<h2>ライセンス本文</h2>",
            "\n".join(license_sections),
        )
    )
    return _render_html_document(
        title=f"Third-Party Licenses - {wheel_data.name}",
        body=body,
    )


def _render_package_row(entry: PackageLicense) -> str:
    package = entry.package
    repository = ""
    if package.repository is not None and package.repository.startswith(
        ("https://", "http://")
    ):
        escaped_url = html.escape(package.repository, quote=True)
        repository = f'<a href="{escaped_url}">{escaped_url}</a>'
    return (
        "<tr>"
        f"<td>{html.escape(package.label)}</td>"
        f"<td>{html.escape(entry.license)}</td>"
        f"<td>{repository}</td>"
        "</tr>"
    )


def _render_notices_html(
    notice_groups: Sequence[NoticeGroup],
    wheel_data: WheelData,
    lock_hash: str,
) -> str:
    sections: list[str] = []
    for group in notice_groups:
        anchor = _content_anchor("notice", group.text)
        references = "\n".join(
            "<li>"
            f"{html.escape(reference.package_label)}: "
            f"<code>{html.escape(reference.relative_path)}</code>"
            "</li>"
            for reference in group.references
        )
        sections.append(
            "\n".join(
                (
                    f'<section class="document" id="{anchor}">',
                    "<h2>NOTICE</h2>",
                    "<h3>出典</h3>",
                    f"<ul>{references}</ul>",
                    f"<pre>{html.escape(group.text)}</pre>",
                    "</section>",
                )
            )
        )

    if sections:
        notice_body = "\n".join(sections)
    else:
        notice_body = (
            '<p class="empty">対象となる第三者crateに'
            "NOTICEファイルは見つかりませんでした。</p>"
        )

    body = "\n".join(
        (
            "<h1>Third-Party Notices</h1>",
            "<p>cargo-aboutが列挙したターゲット別crateを対象に、"
            "NOTICE、NOTICE.txtなどのファイルを収集しています。</p>",
            _render_build_metadata(wheel_data, lock_hash),
            notice_body,
        )
    )
    return _render_html_document(
        title=f"Third-Party Notices - {wheel_data.name}",
        body=body,
    )


def _render_build_metadata(wheel_data: WheelData, lock_hash: str) -> str:
    targets = "".join(
        f"<li><code>{html.escape(target)}</code></li>" for target in wheel_data.targets
    )
    return "\n".join(
        (
            '<dl class="metadata">',
            f"<dt>対象</dt><dd>{html.escape(wheel_data.name)}</dd>",
            f"<dt>Rustターゲット</dt><dd><ul>{targets}</ul></dd>",
            f"<dt>Cargo.lock SHA-256</dt><dd><code>{lock_hash}</code></dd>",
            "</dl>",
        )
    )


def _render_html_document(*, title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
body {{ margin: 1rem; line-height: 1.5; overflow-wrap: anywhere; }}
table {{ border-collapse: collapse; }}
th, td {{ border: 1px solid; padding: .25rem; text-align: left; }}
td {{ vertical-align: top; }}
pre {{ white-space: pre-wrap; }}
</style>
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""


def _content_anchor(prefix: str, content: str) -> str:
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]
    return f"{prefix}-{digest}"


if __name__ == "__main__":
    main()
