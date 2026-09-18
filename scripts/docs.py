# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse
import logging
import subprocess
from collections.abc import Sequence
from logging import Logger
from pathlib import Path

_PUBLIC_API_PACKAGES = ((Path("python/stbkit/src"), "stbkit.api"),)

_GENERATED_MODULES: set[str] = {
    "stbkit.api.stb_latest",
    "stbkit.api.stb_v2_0_2",
    "stbkit.api.stb_v2_1_1",
}
_PYTHON_API_REFERENCE: Path = Path("docs/_generated/reference/python")


# データモデルを抜粋するためのフィルター
# - StBridge   : ルートクラス
# - Stb...     : 通常要素
# - 大文字   : Enum値とVERSION
# - UUID       : importされた名前なので除外
_COMPACT_MEMBER_FILTER = r"^(?:Stb[A-Za-z0-9_]*|StBridge|(?!UUID$)[A-Z][A-Z0-9_]*)$"


def _collect_public_modules(source_root: Path, module: str) -> list[str]:

    modules: list[str] = [module]
    directory: Path = source_root.joinpath(*module.split("."))
    if not directory.is_dir():
        return modules
    for item in sorted(directory.iterdir()):
        if item.name.startswith("_"):
            continue
        if item.is_dir():
            if not (item / "__init__.py").exists():
                continue
            modules.extend(
                _collect_public_modules(source_root, f"{module}.{item.name}")
            )
        elif item.suffix == ".py":
            modules.append(f"{module}.{item.stem}")
    return modules


def _generate_python_reference(*, include_generated_api: bool) -> None:

    modules: list[str] = []
    for module_path, module_name in _PUBLIC_API_PACKAGES:
        modules.extend(_collect_public_modules(module_path, module_name))
    reference_dir: Path = _PYTHON_API_REFERENCE
    reference_dir.mkdir(parents=True, exist_ok=True)
    index_rows: list[str] = []

    for module in modules:
        page_path: Path = reference_dir / f"{module.replace('.', '_')}.md"
        if module in _GENERATED_MODULES and not include_generated_api:
            body: str = "自動生成データモデルのAPIは処理が重いため生成を省略しています"
        elif module in _GENERATED_MODULES:
            body = f"""このページでは表示を軽量化するため、
コンストラクター、個別プロパティ、`xxx_or_none`、`ensure`などの共通メンバーを展開していません。

各クラスで使用できるフィールドと型は、クラスの「属性」を参照してください。

::: {module}
    options:
      show_root_toc_entry: true
      filters:
        - "{_COMPACT_MEMBER_FILTER}"
      inherited_members: false
      group_by_category: false
      docstring_section_style: list
      show_bases: false
      show_signature: false
      show_attribute_values: true
      show_source: false
      signature_crossrefs: false
"""
        else:
            body = f"""::: {module}
"""
        content = f"""# {module}

{body}
"""
        page_path.write_text(content, encoding="utf-8", newline="\n")
        if module.startswith("stbkit.core"):
            package_name: str = "stbkit-core"
        else:
            package_name = "stbkit"

        index_rows.append(f"| [`{module}`]({page_path.name}) | `{package_name}` |")

    index = f"""# Python APIリファレンス

## モジュール一覧

| モジュール | 配布パッケージ |
| --- | --- |
{"\n".join(index_rows)}

## 互換性方針
[互換性方針](https://github.com/taisei-oss/stb-kit/blob/main/COMPATIBILITY.md)を確認してください。
"""
    index_path: Path = reference_dir / "index.md"
    index_path.write_text(index, encoding="utf-8", newline="\n")


def _build_docs(*, logger: Logger, include_generated_api: bool) -> None:
    logger.info("ドキュメント生成開始")
    logger.info("Python APIリファレンス生成開始")
    _generate_python_reference(include_generated_api=include_generated_api)
    logger.info("ビルド開始")
    subprocess.run(
        [
            "mkdocs",
            "build",
        ],
        check=True,
    )
    logger.info("ドキュメント生成完了")


def _serve_docs(*, logger: Logger, port: int, include_generated_api: bool) -> None:
    logger.info("Python APIリファレンス生成開始")
    _generate_python_reference(include_generated_api=include_generated_api)
    logger.info(f"ローカルサーバーをポート {port} で起動")
    subprocess.run(
        [
            "mkdocs",
            "serve",
            f"--dev-addr=0.0.0.0:{port}",
        ],
        check=True,
    )


def _create_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="ドキュメント生成"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="ドキュメントをビルドする")
    build_parser.add_argument(
        "--include-generated-api",
        action="store_true",
        dest="include_generated_api",
        help="重い自動生成データモデルAPIのページも生成する",
    )

    run_server_parser = subparsers.add_parser(
        "serve", help="ローカルサーバーでドキュメントを表示する"
    )
    run_server_parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="ローカルサーバーのポート番号 (デフォルト: 8000)",
    )
    run_server_parser.add_argument(
        "--include-generated-api",
        action="store_true",
        dest="include_generated_api",
        help="重い自動生成データモデルAPIのページも生成する",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> None:
    logging.basicConfig(
        level=logging.INFO, format="[%(name)s]%(levelname).1s:%(message)s"
    )
    logger: Logger = logging.getLogger("stb-docs")
    logger.setLevel(logging.INFO)
    parser: argparse.ArgumentParser = _create_parser()
    args: argparse.Namespace = parser.parse_args(
        list(argv) if argv is not None else None
    )

    if args.command == "build":
        _build_docs(
            logger=logger,
            include_generated_api=args.include_generated_api,
        )
    elif args.command == "serve":
        port: int = args.port
        _serve_docs(
            logger=logger, port=port, include_generated_api=args.include_generated_api
        )


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
