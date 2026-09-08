# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol, cast

from stbkit.core.stb_reporting import NullReporter, Reporter

from .data import _Data


@dataclass
class _ExecutionContext:
    work_dir: Path | None = None
    keep_temporary_files: bool = False
    reporter: Reporter = field(default_factory=NullReporter)
    max_size: int | None = None
    """max_sizeは読み込む ST-Bridgeのサイズ上限(バイト)。
    Noneの場合は読み込み側の既定値を使用する。"""
    on_step_completed: Callable[[str, _Data], None] | None = None
    """複合ステップ内を含む各単一ステップの完了時に呼び出される。
    CLIの中間ファイル保存など、変換処理そのものとは独立した処理の実装のために使用する。"""
    ifc_round_digits: int | None = None
    ifc_round_digits_mm: int | None = None


@dataclass(frozen=True)
class _ExecutionResult[OutData: _Data]:
    output: OutData
    cleanup_paths: tuple[Path, ...] = ()
    """結果を利用し終わった後に削除してよい一時パス。
    複合ステップでは直ちに削除せず、最上位の呼び出し側へ集約して返す。"""


class _ExecutableStep[InData: _Data, OutData: _Data](Protocol):
    name: str

    def execute(
        self,
        data: InData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[OutData]: ...


@dataclass(frozen=True)
class _FunctionExecutableStep[InData: _Data, OutData: _Data]:
    name: str
    func: Callable[[InData, _ExecutionContext], _ExecutionResult[OutData]]

    def execute(
        self,
        data: InData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[OutData]:
        return self.func(data, context)


@dataclass(frozen=True)
class _CompositeExecutableStep[InData: _Data, OutData: _Data](
    _ExecutableStep[InData, OutData]
):
    name: str
    runners: Sequence[_ExecutableStep[Any, Any]]

    def execute(
        self,
        data: InData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[OutData]:
        tmp_data: _Data = data
        cleanup_paths: list[Path] = []
        for runner in self.runners:
            result = _execute_step(runner, tmp_data, context=context)
            tmp_data = result.output
            cleanup_paths.extend(result.cleanup_paths)
        return _ExecutionResult(
            output=cast(OutData, tmp_data),
            cleanup_paths=tuple(cleanup_paths),
        )


class _NoOpStep[InData: _Data](_ExecutableStep[InData, InData]):
    name = "No-Op"

    def execute(
        self,
        data: InData,
        *,
        context: _ExecutionContext,
    ) -> _ExecutionResult[InData]:
        return _ExecutionResult(output=data)


def _execute_step[InData: _Data, OutData: _Data](
    step: _ExecutableStep[InData, OutData],
    data: InData,
    *,
    context: _ExecutionContext,
) -> _ExecutionResult[OutData]:
    """ステップを実行し、単一ステップであれば完了通知も行う"""
    result = step.execute(data, context=context)
    if context.on_step_completed is not None and not isinstance(
        step, _CompositeExecutableStep
    ):
        context.on_step_completed(step.name, result.output)
    return result


def _compose_steps(
    name: str,
    steps: Sequence[_ExecutableStep[Any, Any]],
) -> _ExecutableStep[Any, Any]:
    """
    ステップを平坦化し、不要なNo-Opを除いて最小の実行単位を返す。

    変換ルートを組み立てる側が複合ステップの入れ子や、単一ステップだけの複合オブジェクトを意識せずに済むようにする。
    """
    flattened: list[_ExecutableStep[Any, Any]] = []
    for step in steps:
        if isinstance(step, _CompositeExecutableStep):
            flattened.extend(step.runners)
        elif isinstance(step, _NoOpStep):
            continue
        else:
            flattened.append(step)

    if not flattened:
        return _NoOpStep()
    if len(flattened) == 1:
        return flattened[0]
    return _CompositeExecutableStep(name=name, runners=tuple(flattened))
