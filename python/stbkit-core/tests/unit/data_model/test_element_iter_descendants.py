from stbkit.testutils.data_model_sample.v2_1_1 import v2_1_1_rc_column

from stbkit.core.data_model.common import StBridgeElement, _StBridgeExtensionElement
from stbkit.core.data_model.stb_v2_1_1 import StbNode, StbSecFigureColumnRc


def test_iter_descendants() -> None:
    stb = v2_1_1_rc_column()
    common = stb.stb_common
    model = stb.stb_model
    nodes = model.stb_nodes
    node1 = nodes.stb_node[0]
    node2 = nodes.stb_node[1]
    members = model.stb_members
    columns = members.stb_columns
    column = columns.stb_column[0]
    sections = model.stb_sections
    sec_column = sections.stb_sec_column_rc[0]
    figure = sec_column.stb_sec_figure_column_rc
    rect = figure.stb_sec_column_rect

    descendants: list[StBridgeElement] = list(stb.iter_descendants())
    assert descendants == [
        common,
        model,
        nodes,
        node1,
        node2,
        members,
        columns,
        column,
        sections,
        sec_column,
        figure,
        rect,
    ]

    descendants = list(stb.iter_descendants(include_self=True))
    assert descendants == [
        stb,
        common,
        model,
        nodes,
        node1,
        node2,
        members,
        columns,
        column,
        sections,
        sec_column,
        figure,
        rect,
    ]

    descendants = list(stb.iter_descendants(StbNode))
    assert descendants == [
        node1,
        node2,
    ]
    descendants = list(stb.iter_descendants(element_types=StbNode))
    assert descendants == [
        node1,
        node2,
    ]

    descendants = list(stb.iter_descendants((StbNode, StbSecFigureColumnRc)))
    assert descendants == [
        node1,
        node2,
        figure,
    ]

    descendants = list(stb.iter_descendants(class_names="StbNode"))
    assert descendants == [
        node1,
        node2,
    ]
    descendants = list(
        stb.iter_descendants(class_names=("StbNode", "StbSecFigureColumnRc"))
    )
    assert descendants == [
        node1,
        node2,
        figure,
    ]
    descendants = list(stb.iter_descendants(xml_names="StbNode"))
    assert descendants == [
        node1,
        node2,
    ]
    descendants = list(
        stb.iter_descendants(xml_names=("StbNode", "StbSecFigureColumn_RC"))
    )
    assert descendants == [
        node1,
        node2,
        figure,
    ]
    descendants = list(stb.iter_descendants(max_depth=2))
    assert descendants == [
        common,
        model,
        nodes,
        members,
        sections,
    ]


def test_iter_descendants_extension() -> None:
    from stbkit.testutils.data_model_sample.golden_v2_1_1 import (
        golden_v2_1_1_has_extension,
    )

    stb = golden_v2_1_1_has_extension()
    descendants: list[StBridgeElement] = list(
        stb.iter_descendants(xml_names="ExtElement1")
    )
    assert len(descendants) == 0

    descendants = list(
        stb.iter_descendants(xml_names="ExtElement1", include_extensions=True)
    )
    assert len(descendants) == 2
    assert all(
        isinstance(descendant, _StBridgeExtensionElement) for descendant in descendants
    )
    assert descendants[0] is not descendants[1]
