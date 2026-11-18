# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""配筋の修復
ST-Bridgeは配筋情報がなくても成立するため、不正な配筋があった場合は配筋情報を削除する

構造計算プログラムによっては小梁は重量のみいれ、断面検定しない場合がある。
その時に配筋本数が0本のように不正になる場合があるため、その対策。
"""

from typing import Protocol, runtime_checkable

from stbkit.core.data_model.common import StBridgeElement
from stbkit.core.stb_reporting import (
    Code,
    CollectingReporter,
    Phase,
    Reporter,
)
from stbkit.core.validation._internal.schema_validator import FieldValidator


@runtime_checkable
class _StbSecBeamRcLikeV20(Protocol):
    @property
    def stb_sec_bar_arrangement_beam_rc_or_none(self) -> StBridgeElement | None: ...
    @stb_sec_bar_arrangement_beam_rc_or_none.setter
    def stb_sec_bar_arrangement_beam_rc_or_none(
        self, value: StBridgeElement | None
    ) -> None: ...


@runtime_checkable
class _StbSecBeamRcLike(Protocol):
    @property
    def stb_sec_bar_arrangement_beam_rc(self) -> list[StBridgeElement]: ...
    @stb_sec_bar_arrangement_beam_rc.setter
    def stb_sec_bar_arrangement_beam_rc(self, value: list[StBridgeElement]) -> None: ...


def _repair_stb_sec_beam_rc(element: StBridgeElement, /, *, reporter: Reporter) -> None:
    if element._xml_name() == "StbSecBeam_RC":
        if (
            isinstance(element, _StbSecBeamRcLikeV20)
            and element.stb_sec_bar_arrangement_beam_rc_or_none is not None
        ):
            tmp_reporter: CollectingReporter = CollectingReporter()
            if not FieldValidator.validate_element(
                element.stb_sec_bar_arrangement_beam_rc_or_none, tmp_reporter
            ):
                reporter.error(
                    "梁配筋情報に不正値が含まれていたため、配筋情報を削除しました"
                    f"{tmp_reporter.report.to_text().replace('\n', '')}",
                    code=Code.REPAIR_LOG,
                    phase=Phase.REPAIR,
                    stb_element=element.stb_sec_bar_arrangement_beam_rc_or_none,
                )
                element.stb_sec_bar_arrangement_beam_rc_or_none = None
        elif isinstance(element, _StbSecBeamRcLike) and isinstance(
            element.stb_sec_bar_arrangement_beam_rc, list
        ):
            tmp_reporter = CollectingReporter()
            is_valid: bool = True
            for child in element.stb_sec_bar_arrangement_beam_rc:
                is_valid &= FieldValidator.validate_element(child, tmp_reporter)
            if not is_valid:
                # 配筋情報は一部のみ削除するとorderが崩れるため、
                # 不正が1か所あったらすべて削除する
                for child in element.stb_sec_bar_arrangement_beam_rc:
                    reporter.error(
                        "梁配筋情報に不正値が含まれていたため、配筋情報を削除しました"
                        f"{tmp_reporter.report.to_text().replace('\n', '')}",
                        code=Code.REPAIR_LOG,
                        phase=Phase.REPAIR,
                        stb_element=child,
                    )
                element.stb_sec_bar_arrangement_beam_rc.clear()
