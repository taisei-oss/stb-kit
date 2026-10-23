from stbkit.core.data_model.stb_v2_1_1 import (
    StbColumn,
    StbColumnKindStructure,
    StbColumns,
    StbCommon,
    StbMembers,
    StbModel,
    StbNode,
    StbNodes,
    StBridge,
    StbSecBuildH,
    StbSecColumnRc,
    StbSecRollH,
    StbSecSteel,
    StbSections,
)
from stbkit.core.stb_reporting import Code, CollectingReporter
from stbkit.core.validation import validate_schema


def test_schema_validator_duplicate_keys() -> None:
    stb: StBridge = StBridge(
        version="2.1.1",
        stb_common=StbCommon(
            project_name="test_schema_validator",
            app_name="stbkit-core",
            app_version="0.0.0",
        ),
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[
                    StbNode(id=1, x=0.0, y=0.0, z=0.0, kind="ON_GRID"),
                    StbNode(id=1, x=1.0, y=0.0, z=0.0, kind="ON_GRID"),
                ]
            )
        ),
    )
    reporter: CollectingReporter = CollectingReporter()

    assert not validate_schema(stb, reporter=reporter)
    assert any(
        item.code == Code.SCHEMA_ERROR and "重複" in item.message
        for item in reporter.report
    )
    assert len(reporter.report) == 1


def test_schema_validator_duplicate_sec_steel() -> None:
    stb: StBridge = StBridge(
        version="2.1.1",
        stb_common=StbCommon(
            project_name="test_schema_validator",
            app_name="stbkit-core",
            app_version="0.0.0",
        ),
        stb_model=StbModel(
            stb_sections=StbSections(
                stb_sec_steel=StbSecSteel(
                    stb_sec_roll_h=[
                        StbSecRollH(
                            name="H-700",
                            type="H",
                            a=700.0,
                            b=300.0,
                            t1=13.0,
                            t2=24.0,
                            r=18.0,
                        )
                    ],
                    stb_sec_build_h=[
                        StbSecBuildH(
                            name="H-700",
                            a=700.0,
                            b=300.0,
                            t1=12.0,
                            t2=16.0,
                        )
                    ],
                )
            )
        ),
    )
    reporter: CollectingReporter = CollectingReporter()

    assert not validate_schema(stb, reporter=reporter)
    assert len(reporter.report) == 1
    assert reporter.report[0].code == Code.SCHEMA_ERROR
    assert "name" in reporter.report[0].message
    assert "重複" in reporter.report[0].message


def test_schema_validator_missing_reference() -> None:
    stb: StBridge = StBridge(
        version="2.1.1",
        stb_common=StbCommon(
            project_name="test_schema_validator",
            app_name="stbkit-core",
            app_version="0.0.0",
        ),
        stb_model=StbModel(
            stb_nodes=StbNodes(
                stb_node=[StbNode(id=1, x=0.0, y=0.0, z=0.0, kind="ON_GRID")]
            ),
            stb_members=StbMembers(
                stb_columns=StbColumns(
                    stb_column=[
                        StbColumn(
                            id=10,
                            id_node_bottom=999,
                            id_node_top=1,
                            id_section=1,
                            kind_structure=StbColumnKindStructure.RC,
                        )
                    ]
                )
            ),
            stb_sections=StbSections(
                stb_sec_column_rc=[StbSecColumnRc(id=1, name="C1")]
            ),
        ),
    )
    reporter: CollectingReporter = CollectingReporter()

    assert not validate_schema(stb, reporter=reporter)
    assert any(
        item.code == Code.SCHEMA_ERROR
        and item.value == "999"
        and "id_node_bottom" in item.message
        for item in reporter.report
    )
    assert len(reporter.report) == 1
