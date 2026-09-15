# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass, field

from ..data_model.common import StBridgeElement, StBridgeRoot, _FieldKind, _InvalidValue
from ..stb_reporting import Code, Phase, Reporter
from .name_converter import private_field_name


@dataclass(kw_only=True, frozen=True)
class AttributeInfo:
    name: str
    type: str


@dataclass(kw_only=True)
class ExtensionInfo:
    """拡張情報により定義された、要素の拡張。

    リポジトリで処理しやすいように、ST-Bridge上の表記と表現を変えているので注意。

    - element_name: 対象の要素。
    - attribute_infos: その要素が持ってよい属性一覧
    - parent_name: 対象の要素が所属する親要素。既存要素は既に親が決まっており、
        親チェックが不要なため省略。
    """

    element_name: str
    attribute_infos: set[AttributeInfo] = field(default_factory=set)
    parent_name: str | None = None


class ExtensionInfoRepository:
    def __init__(self) -> None:
        self._registry: dict[str, ExtensionInfo] = {}

    def register(
        self,
        stb: StBridgeRoot,
        *,
        reporter: Reporter,
        phase: Phase = Phase.VALIDATE,
    ) -> None:
        from stbkit.core.data_model import (
            stb_v2_0_1,
            stb_v2_0_2,
            stb_v2_1_0,
            stb_v2_1_1,
        )

        if isinstance(
            stb,
            (
                stb_v2_0_1.StBridge,
                stb_v2_0_2.StBridge,
                stb_v2_1_0.StBridge,
                stb_v2_1_1.StBridge,
            ),
        ):
            if stb.stb_extensions_or_none is None:
                return
            for extension in stb.stb_extensions.stb_extension:
                for ext_elm in extension.stb_ext_element:
                    if ext_elm.object_name_or_none is None:
                        continue
                    element_name: str
                    parent_name: str | None
                    if ext_elm.element_name_or_none is None:
                        element_name = ext_elm.object_name
                        parent_name = None
                    else:
                        element_name = ext_elm.element_name
                        parent_name = ext_elm.object_name
                    ext_info: ExtensionInfo = self._register_element(
                        element_name,
                        parent_name,
                        definition=ext_elm,
                        reporter=reporter,
                        phase=phase,
                    )
                    for ext_prop in ext_elm.stb_ext_property_def:
                        if ext_prop.key_or_none is None:
                            continue
                        if ext_prop.type_or_none is None:
                            continue
                        attr_info = AttributeInfo(
                            name=ext_prop.key,
                            type=ext_prop.type,
                        )
                        if attr_info not in ext_info.attribute_infos:
                            ext_info.attribute_infos.add(attr_info)

    def _register_element(
        self,
        element_name: str,
        parent_name: str | None,
        *,
        definition: StBridgeElement,
        reporter: Reporter,
        phase: Phase,
    ) -> ExtensionInfo:
        """対象要素の拡張定義登録。

        同じ要素名に対して別の定義ある場合は、拡張定義として矛盾しているためエラー出力し、先にでてきた定義を優先します。
        """
        ext_info: ExtensionInfo | None = self._registry.get(element_name)
        if ext_info is None:
            ext_info = ExtensionInfo(
                element_name=element_name,
                attribute_infos=set(),
                parent_name=parent_name,
            )
            self._registry[element_name] = ext_info
            return ext_info
        if ext_info.parent_name != parent_name:
            reporter.error(
                message=(
                    f"要素[{element_name}]の拡張定義が重複しています。"
                    "element_nameに記載する、拡張する子要素の名前は、拡張する子要素同志で重複しないことが求められます。"
                    "処理では先に定義した内容を採用します"
                ),
                code=Code.EXTENSION_ERROR,
                phase=phase,
                stb_element=definition,
                value=f"採用:element_name={ext_info.element_name},object_name={ext_info.parent_name},",
                ref_value=f"無視:element_name={element_name},object_name={parent_name},",
            )
        return ext_info

    def _allowed_attribute_names_by_element_name(self, element_name: str) -> set[str]:
        ext_info: ExtensionInfo | None = self._registry.get(element_name)
        if ext_info is None:
            return set()
        return {attr.name for attr in ext_info.attribute_infos}

    def _allowed_attribute_names(self, stb_element: StBridgeElement) -> set[str]:
        return self._allowed_attribute_names_by_element_name(stb_element._xml_name())

    def _is_allowed_child_name(self, *, child_name: str, parent_name: str) -> bool:
        ext_info: ExtensionInfo | None = self._registry.get(child_name)
        if ext_info is None or ext_info.parent_name is None:
            return False
        return ext_info.parent_name == parent_name

    def _is_allowed_child(
        self, *, child: StBridgeElement, parent: StBridgeElement
    ) -> bool:
        return self._is_allowed_child_name(
            child_name=child._xml_name(), parent_name=parent._xml_name()
        )

    def _attribute_infos(
        self, stb_element: StBridgeElement
    ) -> tuple[AttributeInfo, ...]:
        ext_info: ExtensionInfo | None = self._registry.get(stb_element._xml_name())
        if ext_info is None:
            return ()
        return tuple(sorted(ext_info.attribute_infos, key=lambda info: info.name))

    def _child_element_names(self, parent: StBridgeElement) -> tuple[str, ...]:
        parent_name: str = parent._xml_name()
        return tuple(
            ext_info.element_name
            for ext_info in self._registry.values()
            if ext_info.parent_name == parent_name
        )

    def repair_stb(
        self,
        stb_element: StBridgeElement,
        reporter: Reporter,
        phase: Phase = Phase.VALIDATE,
    ) -> None:
        ext = stb_element._extension
        element_name: str = stb_element._xml_name()
        # 拡張情報で説明できない属性・子要素は不正値として退避させる
        allowed_attribute_names: set[str] = self._allowed_attribute_names(stb_element)
        if ext is not None:
            keys = list(ext._attributes.keys()) if ext._attributes else []
            for key in keys:
                if ext._attributes and key not in allowed_attribute_names:
                    value = ext._attributes.pop(key)
                    # 未知属性はモデルの_field_infoに存在しないため、XPathを直接生成する
                    path_xml = f"{stb_element._path_xml()}/@{key}"
                    reporter.error(
                        message=(
                            f"要素[{element_name}]の不明な拡張属性[{key}]を削除しました"
                        ),
                        code=Code.EXTENSION_ERROR,
                        phase=phase,
                        value=value,
                        xpath=path_xml,
                    )
                    ext._set_invalid_value(
                        _InvalidValue(
                            kind=_FieldKind.ATTRIBUTE,
                            value=value,
                            path=path_xml,
                            reason="拡張定義されていない拡張属性",
                        )
                    )
            if ext._children:
                for i in reversed(range(len(ext._children))):
                    child = ext._children[i]
                    child_name: str = child._xml_name()
                    if not self._is_allowed_child(child=child, parent=stb_element):
                        reporter.error(
                            message=(
                                f"要素[{element_name}]の不明な拡張要素[{child_name}]を削除しました"
                            ),
                            code=Code.EXTENSION_ERROR,
                            phase=phase,
                            xpath=child._path_xml(),
                        )
                        ext._set_invalid_value(
                            _InvalidValue(
                                kind=_FieldKind.ELEMENT,
                                value=child,
                                path=child._path_xml(),
                                reason="拡張定義されていない拡張子要素",
                            )
                        )
                        ext._children.pop(i)
                for child in ext._children:
                    self.repair_stb(child, reporter, phase)
        for key, fi in stb_element._fields.items():
            if fi.kind is _FieldKind.ELEMENT:
                p_name: str = private_field_name(key)
                value = getattr(stb_element, p_name)
                if isinstance(value, StBridgeElement):
                    self.repair_stb(value, reporter, phase)
                elif isinstance(value, list):
                    for v in value:
                        if isinstance(v, StBridgeElement):
                            self.repair_stb(v, reporter, phase)
