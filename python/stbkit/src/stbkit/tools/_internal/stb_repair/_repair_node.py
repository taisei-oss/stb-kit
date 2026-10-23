"""節点の修復"""

from typing import Protocol, runtime_checkable

from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_reporting import Code, Phase, Reporter


@runtime_checkable
class _NodeLike(Protocol):
    @property
    def kind_or_none(self) -> str | None: ...
    @property
    def id_member_or_none(self) -> str | None: ...
    @id_member_or_none.setter
    def id_member_or_none(self, value: str | None) -> None: ...


def _repair_node(element: StBridgeElement, /, *, reporter: Reporter) -> None:
    if (
        element._xml_name() == "StbNode"
        and isinstance(element, _NodeLike)
        and (element.kind_or_none == "ON_GRID" or element.kind_or_none == "OTHER")
        and element.id_member_or_none is not None
    ):
        before_id_member = element.id_member_or_none
        element.id_member_or_none = None
        reporter.warning(
            f"節点種類[{element.kind_or_none}]はid_memberが不要であるため、削除しました",
            code=Code.REPAIR_LOG,
            phase=Phase.REPAIR,
            stb_element=element,
            attr_name="id_member",
            value=before_id_member,
        )
