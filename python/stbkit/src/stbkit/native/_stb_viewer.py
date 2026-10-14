from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from logging import Logger
from uuid import UUID

from stbkit.core.data_model.common import StBridgeElement, StBridgeRoot
from stbkit.core.repository import RepositoryBase, get_repository
from stbkit.core.serialization import to_dict
from stbkit.core.stb_reporting import Reporter, get_reporter

from stbkit.api import upgrade_to_latest
from stbkit.api.stb_latest import StBridge
from stbkit.tools._internal.data_model.building_geometry import BuildingGeometry
from stbkit.tools.converters._internal.stb_to_building_geometry import (
    stb_to_building_geometry,
)

from . import _bridge


@dataclass(frozen=True, slots=True)
class ElementClickEvent:
    """3Dビューでクリックされた1要素の情報。

    Attributes:
        element_index: 3D表示データ内での要素の通し番号。
        kind: 柱・大梁などの部材種別を表す番号。ElementKindの値。
        guid: 要素のGUID。持たない要素や取得できなかった場合はNone。
        xpath: 生成元での要素のXPath。取得できなかった場合None。
        name: 要素につけている名前（内部実装）
        source_type: 生成元での要素名。"StbColumn"のような文字列。
        source_id: 生成元での要素のID。持たない要素の場合はNone。
    """

    element_index: int
    kind: int
    guid: str | None
    xpath: str | None
    name: str | None
    source_type: str
    source_id: str | None

    @classmethod
    def from_payload(cls, payload: _bridge.ElementClickEventDict) -> ElementClickEvent:
        """Rustの辞書形式から型付きイベントを作成する。"""

        return cls(
            element_index=payload["element_index"],
            kind=payload["kind"],
            guid=payload["guid"],
            xpath=payload["xpath"],
            name=payload["name"],
            source_type=payload["source_type"],
            source_id=payload["source_id"],
        )


type ElementClickCallback = Callable[[ElementClickEvent], None]
"""3Dビューで要素がクリックされたときに呼び出す関数の型。"""


def _element_click_dispatcher(
    callback: ElementClickCallback,
) -> Callable[[_bridge.ElementClickEventDict], None]:
    """Rustの転送辞書を型付きイベントへ変換するコールバックを作成する。"""

    def dispatch(payload: _bridge.ElementClickEventDict) -> None:
        callback(ElementClickEvent.from_payload(payload))

    return dispatch


def _view_building_geometry(
    building_geometry: BuildingGeometry,
    *,
    on_element_click: ElementClickCallback | None = None,
) -> None:

    raw_callback: Callable[[_bridge.ElementClickEventDict], None] | None = (
        _element_click_dispatcher(on_element_click)
        if on_element_click is not None
        else None
    )
    _bridge.run_viewer(building_geometry, raw_callback)


def _print_dict(d: dict[str, object], indent_lebel: int = 0) -> None:
    indent = " " * indent_lebel
    for key, value in d.items():
        if value is None:
            continue
        elif isinstance(value, list):
            if not value:
                continue
            elif isinstance(value[0], dict):
                for i, item in enumerate(value):
                    print(f"{indent}{key}[{i}]:")
                    _print_dict(item, indent_lebel=indent_lebel + 2)
                continue
            else:
                print(f"{indent}{key}: {value}")
        elif isinstance(value, dict):
            print(f"{indent}{key}:")
            _print_dict(value, indent_lebel=indent_lebel + 2)
        else:
            print(f"{indent}{key}: {value}")


def _print_element_click(
    event: ElementClickEvent, stb: StBridgeRoot, repo: RepositoryBase
) -> None:
    """クリックされた要素情報を標準出力へ表示する。"""
    print(f"要素: {event.source_type}")
    guid = event.guid
    if not guid:
        print(
            "guidが設定されていません。guidを設定された部材は部材情報を表示できます。"
        )
    else:
        element: StBridgeElement | None = repo.get_by_guid_or_none(UUID(guid))
        if element is None:
            print("guidに対応する要素が見つかりません。")
        else:
            _print_dict(to_dict(element), indent_lebel=2)


def view(
    stb: StBridgeRoot,
    *,
    logger: Logger | None = None,
    reporter: Reporter | None = None,
    on_element_click: ElementClickCallback | None = None,
) -> None:
    """ST-Bridgeを3Dビューアで表示します。

    ウィンドウを閉じるまで戻りません。

    Args:
        stb: 表示するST-Bridgeのルート要素。
        on_element_click: 要素がクリックされたときに呼び出す関数。

    Raises:
        RuntimeError: 任意依存のstbkit-nativeが未インストール、または
            Rust拡張を読み込めない場合。
        TypeError: stbkit-nativeのAPIがこのstbkitと互換でない場合。

    Examples:
        >>> import stbkit.api
        >>> import stbkit.api.experimental
        >>> stb = stbkit.api.load("model.stb")
        >>> stbkit.api.experimental.view(stb)
    """
    reporter = get_reporter(logger, reporter)
    upgraded_stb: StBridge = upgrade_to_latest(stb, reporter=reporter)
    repo: RepositoryBase = get_repository(upgraded_stb)

    def print_element_click(event: ElementClickEvent) -> None:
        _print_element_click(event, stb=upgraded_stb, repo=repo)

    building_geometry: BuildingGeometry = stb_to_building_geometry(
        upgraded_stb, reporter=reporter
    )
    if on_element_click is None:
        on_element_click = print_element_click
    _view_building_geometry(
        building_geometry,
        on_element_click=on_element_click,
    )
