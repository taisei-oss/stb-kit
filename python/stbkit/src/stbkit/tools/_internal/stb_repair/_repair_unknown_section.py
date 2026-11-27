# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from stbkit.core._internal.transform import guid_tools
from stbkit.core._internal.utils.version_utils import V2_0_2, V2_1_0
from stbkit.core.data_model.common import StBridgeElement, StBridgeRoot
from stbkit.core.stb_exceptions import ReferenceElementNotFoundError
from stbkit.core.stb_reporting import Code, Phase

from ._common import RepairContext


def _get_sections(stb: StBridgeRoot) -> StBridgeElement:
    if (
        hasattr(stb, "ensure")
        and hasattr(stb.ensure, "stb_model")
        and hasattr(stb.ensure.stb_model(), "ensure")
        and hasattr(stb.ensure.stb_model().ensure, "stb_sections")
    ):
        sections = stb.ensure.stb_model().ensure.stb_sections()
        if isinstance(sections, StBridgeElement):
            return sections
    raise ValueError("指定したST-Bridgeデータモデルには断面要素がありません。")


def _get_unknown_section_id(context: RepairContext) -> int:
    sections: StBridgeElement = _get_sections(context.stb)
    if not hasattr(sections, "stb_sec_undefined"):
        raise ValueError(
            "指定したST-Bridgeデータモデルには構造種別に依存しない断面リストがありません。"
        )
    max_id: int = 0
    if not isinstance(sections.stb_sec_undefined, list):
        raise ValueError(
            "指定したST-Bridgeデータモデルには構造種別に依存しない断面リストがありません。"
        )
    for sec in sections.stb_sec_undefined:
        if hasattr(sec, "id"):
            max_id = max(max_id, sec.id)
    unknown_id: int = max_id + 1
    context.unknown_section_id = unknown_id
    sec_undefined: StBridgeElement = context.stb._create_instance("StbSecUndefined")
    if hasattr(sec_undefined, "id_or_none"):
        sec_undefined.id_or_none = unknown_id
    if hasattr(sec_undefined, "name_or_none"):
        sec_undefined.name_or_none = "不明断面(stbkitにより自動生成)"
    if hasattr(sec_undefined, "guid_or_none"):
        sec_undefined.guid_or_none = guid_tools.generate_uuid()
    sections.stb_sec_undefined.append(sec_undefined)
    return unknown_id


def _repair_element_unknown_section(
    girder: StBridgeElement,
    /,
    *,
    context: RepairContext,
    id_section_attr_name: str = "id_section",
    kind_structure_attr_name: str = "kind_structure",
) -> None:
    if not hasattr(girder, f"{id_section_attr_name}_or_none") or not hasattr(
        girder, f"{kind_structure_attr_name}_or_none"
    ):
        return
    try:
        context.repo._deref_field(girder, "id_section")
    except ReferenceElementNotFoundError:
        unknown_id: int = _get_unknown_section_id(context=context)
        setattr(girder, f"{id_section_attr_name}_or_none", unknown_id)
        context.reporter.warning(
            f"{girder._xml_name()}の{id_section_attr_name}が不正な参照なので、構造不明断面(id={unknown_id})を設定しました",
            code=Code.REPAIR_LOG,
            phase=Phase.REPAIR,
            stb_element=girder,
            attr_name=id_section_attr_name,
        )
        if getattr(girder, f"{kind_structure_attr_name}_or_none") != "UNDEFINED":
            setattr(girder, f"{kind_structure_attr_name}_or_none", "UNDEFINED")
            context.reporter.warning(
                f"{girder._xml_name()}の{id_section_attr_name}が不正な参照なので、構造種別をUNDEFINEDに設定しました",
                code=Code.REPAIR_LOG,
                phase=Phase.REPAIR,
                stb_element=girder,
                attr_name=kind_structure_attr_name,
            )


def repair_unknown_section(
    element: StBridgeElement, /, *, context: RepairContext
) -> None:
    # StbUndefinedはV2.0.2で導入されたため、それ以前のバージョンでは処理しない
    if context.version < V2_0_2:
        return
    if element._xml_name() in ("StbColumn", "StbPost", "StbGirder", "StbBeam"):
        _repair_element_unknown_section(element, context=context)
    # 免制振装置はv2.1.0で導入されたため、それ以前のバージョンでは処理しない
    if context.version < V2_1_0:
        return
    if element._xml_name() in ("StbIsolatingDevice", "StbDampingDevice"):
        _repair_element_unknown_section(
            element,
            context=context,
            id_section_attr_name="id_section_start",
            kind_structure_attr_name="kind_structure_start",
        )
        _repair_element_unknown_section(
            element,
            context=context,
            id_section_attr_name="id_section_end",
            kind_structure_attr_name="kind_structure_end",
        )
