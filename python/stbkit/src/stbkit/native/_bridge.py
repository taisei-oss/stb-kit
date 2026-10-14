# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Callable
from importlib import import_module
from types import ModuleType
from typing import Final, Never, Protocol, TypedDict, runtime_checkable

from stbkit.core.stb_exceptions import MissingOptionalDependencyError

from stbkit.tools._internal.data_model.building_geometry import BuildingGeometry

_NATIVE_PACKAGE_NAME_SPACE: Final = "stbkit._native"
_NATIVE_MODULE_NAME: Final = f"{_NATIVE_PACKAGE_NAME_SPACE}.stbkit_native_rs"


class ElementClickEventDict(TypedDict):
    """Rustから受け取るクリックイベントデータ"""

    element_index: int
    kind: int
    guid: str | None
    xpath: str | None
    name: str | None
    source_type: str
    source_id: str | None


@runtime_checkable
class _NativeBackend(Protocol):
    """Rust拡張が公開している関数のインターフェース"""

    def _run_viewer(
        self,
        building_geometry: BuildingGeometry,
        on_element_click: Callable[[ElementClickEventDict], None] | None = None,
    ) -> None: ...

def _raise_missing_native(error: ModuleNotFoundError) -> Never:
    """任意依存がない場合の処理"""

    raise MissingOptionalDependencyError(
        package_name="stbkit-native",
        install_command='python -m pip install --pre "stbkit[native]"',
    ) from error


def _raise_unloadable_native(error: ImportError | OSError) -> Never:
    """Rust拡張をロードできない場合の処理"""

    raise RuntimeError(
        "stbkit-nativeのRust拡張を読み込めませんでした。"
        "Pythonのバージョン、CPUアーキテクチャ、および"
        "stbkitとstbkit-nativeのバージョンを確認してください。"
    ) from error


def _load_native_backend() -> _NativeBackend:
    """Rust拡張を遅延読み込みする。"""

    try:
        module: ModuleType = import_module(_NATIVE_MODULE_NAME)
    except ModuleNotFoundError as error:
        if error.name in {_NATIVE_PACKAGE_NAME_SPACE, _NATIVE_MODULE_NAME}:
            _raise_missing_native(error)
        _raise_unloadable_native(error)
    except (ImportError, OSError) as error:
        _raise_unloadable_native(error)

    if not isinstance(module, _NativeBackend):
        raise TypeError(
            "stbkit-nativeのAPIに互換性がありません。"
            "stbkitとstbkit-nativeを最新版に更新してください。"
        )
    return module


def run_viewer(
    building_geometry: BuildingGeometry,
    on_element_click: Callable[[ElementClickEventDict], None] | None = None,
) -> None:
    backend: _NativeBackend = _load_native_backend()
    backend._run_viewer(building_geometry, on_element_click)


