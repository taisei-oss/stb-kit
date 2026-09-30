# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import json
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="対象パッケージのバージョンがPyPIに公開済かどうかのチェック。"
    )
    parser.add_argument(
        "--package-name",
        default="stbkit",
        help="PyPI上のパッケージ名。",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="PyPI APIリクエストのタイムアウト秒",
    )
    return parser.parse_args()


VERSION_PATTERN: re.Pattern[str] = re.compile(
    r'^const\s+STBKIT_VERSION\s*=\s*"(?P<version>[^"]+)";\s*$',
    re.MULTILINE,
)


def load_playground_version(convert_js_path: Path) -> str:
    content: str = convert_js_path.read_text(encoding="utf-8")
    match: re.Match[str] | None = VERSION_PATTERN.search(content)
    if match is None:
        raise SystemExit("convert.jsからSTBKIT_VERSIONを取得できません。")
    return match.group("version")


def fetch_releases(package_name: str, timeout: float) -> dict[str, Any]:
    url: str = f"https://pypi.org/pypi/{package_name}/json"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            response_data = json.load(response)
    except urllib.error.HTTPError as exc:
        raise SystemExit(
            f"{package_name} のPyPIメタデータ取得に失敗しました: HTTP {exc.code}"
        ) from exc
    releases = response_data.get("releases")
    if not isinstance(releases, dict):
        raise SystemExit(f"{package_name} のPyPI応答形式が想定外です。")
    return {str(key): value for key, value in releases.items()}


def main() -> None:
    args: argparse.Namespace = parse_args()
    version: str = load_playground_version(Path("docs/playground/converter/convert.js"))
    releases: dict[str, Any] = fetch_releases(args.package_name, args.timeout)

    if version not in releases or not releases[version]:
        raise SystemExit(f"{args.package_name}=={version} はPyPIに公開されていません。")

    print(f"確認完了: {args.package_name}=={version} はPyPIで公開済みです。")


if __name__ == "__main__":
    main()
