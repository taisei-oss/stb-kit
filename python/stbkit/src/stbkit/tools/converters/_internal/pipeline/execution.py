# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import hashlib
import itertools
import os
import re
import shutil
from collections.abc import Callable, Sequence
from enum import StrEnum
from pathlib import Path
from typing import Any
from uuid import uuid4

from stbkit.core import stb_io
from stbkit.core.data_model.common import StBridgeRoot
from stbkit.core.stb_exceptions import SchemaError
from stbkit.core.stb_io._internal.serializer import _raw_dumps
from stbkit.core.stb_reporting import Reporter, get_reporter

from stbkit.tools._internal.constants import DEBUG_DUMP_DIR_ENV

from ...._internal.utils.atomic_writer import (
    write_text_stream_with_temp_file,
    write_text_with_temp_file,
    write_with_temp_file,
)
from ..building_geometry_to_ply_text import building_geometry_to_ply_text
from .data import (
    _Data,
    _DataFormat,
    _DataFormatSet,
    _DataKind,
    _FileData,
    _StbVersion,
    _TextData,
)
from .ply_pipeline import _PlyData, _StbToPlyStep, save_ply_data
from .stb_pipeline import (
    StbAssignGuidsStep,
    StbData,
    StbDumpsStep,
    StbFileData,
    StbLoadStep,
    StbRepairStep,
    StbTextData,
    StbToVersionStep,
)
from .stb_pipeline_latest import StbToLatestStep
from .step import (
    _compose_steps,
    _ExecutableStep,
    _execute_step,
    _ExecutionContext,
    _ExecutionResult,
    _NoOpStep,
)


class ConvertResultFormat(StrEnum):
    FILE = "file"
    TEXT = "text"
    FILE_OR_TEXT = "file_or_text"


class _UnsupportedConversionError(NotImplementedError):
    """パイプラインに変換ルートが登録されていない場合の例外"""


def _short_name_for_dump(name: str, *, max_length: int = 64) -> str:
    cleaned: str = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("._-") or "unknown"
    if len(cleaned) <= max_length:
        return cleaned
    hash: str = hashlib.sha1(cleaned.encode("utf-8")).hexdigest()[:12]
    length = max_length - (len(hash) + 1)
    if length <= 0:
        return hash
    return f"{cleaned[:length]}_{hash}"


def _debug_dump_path_for_test(data: StbData[Any]) -> Path | None:
    debug_dump_dir = os.getenv(DEBUG_DUMP_DIR_ENV)
    if not debug_dump_dir:
        return None

    test_name: str = os.getenv("PYTEST_CURRENT_TEST", "unknown_test")
    node_id: str = test_name.split(" ", maxsplit=1)[0]
    short_test_name: str = _short_name_for_dump(node_id.rsplit("::", maxsplit=1)[-1])
    stb_version: _StbVersion = data.stb_version or _StbVersion.UNSPECIFIED
    model_name: str = _short_name_for_dump(f"object_stb_{stb_version.value}")
    file_name: str = f"{model_name}_{short_test_name}_{uuid4().hex}_error.stb"
    return Path(debug_dump_dir).expanduser() / file_name


def _normalize_format_set(
    data_format: _DataFormat | _DataFormatSet,
    *,
    kind: _DataKind,
    stb_version: _StbVersion | None = None,
) -> _DataFormatSet:
    if isinstance(data_format, _DataFormatSet):
        return data_format
    return _DataFormatSet(
        format=data_format,
        kind=kind,
        stb_version=stb_version if data_format == _DataFormat.STB else None,
    )


def to_text(
    data: _Data,
    reporter: Reporter,
) -> str:
    if isinstance(data, _TextData):
        return data.text
    if isinstance(data, _FileData):
        with open(data.path, encoding=data.encoding) as f:
            return f.read()
    if data.format == _DataFormat.STB and isinstance(data, StbData):
        try:
            return stb_io.dumps(data.value, reporter=reporter)
        except SchemaError:
            debug_dump_path = _debug_dump_path_for_test(data)
            if debug_dump_path is not None:
                stb_error: str = _raw_dumps(
                    data.value, reporter=reporter, _strict=False
                )
                try:
                    debug_dump_path.parent.mkdir(parents=True, exist_ok=True)
                    write_text_with_temp_file(
                        debug_dump_path,
                        stb_error,
                        encoding="utf-8",
                    )
                except OSError as error:
                    reporter.warning(
                        "デバッグダンプの保存に失敗しました: "
                        f"path={debug_dump_path} error={error}"
                    )
            raise
    if data.format == _DataFormat.PLY and isinstance(data, _PlyData):
        return building_geometry_to_ply_text(data.value)
    if data.format == _DataFormat.IFC:
        from ...._internal.optional_dependencies import ifc_pipeline

        if isinstance(data, ifc_pipeline.IfcData):
            return data.value.to_string()
    raise ValueError(f"テキスト化できないデータ形式です: {type(data)}")


def save_data(
    data: _Data,
    path: Path,
    reporter: Reporter,
    encoding: str = "utf-8",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, _FileData):
        if data.path.absolute() != path.absolute():

            def _copy_to_temp(temporary_path: Path) -> None:
                shutil.copyfile(data.path, temporary_path)

            write_with_temp_file(path, _copy_to_temp)
        return
    if isinstance(data, _TextData):
        write_text_with_temp_file(path, data.text, encoding=encoding)
        return
    if data.format == _DataFormat.STB and isinstance(data, StbData):
        write_text_stream_with_temp_file(
            path,
            lambda stream: stb_io.dump(data.value, stream, reporter=reporter),
            encoding=encoding,
        )
        return
    if data.format == _DataFormat.IFC:
        from ...._internal.optional_dependencies import ifc_pipeline

        if isinstance(data, ifc_pipeline.IfcData):
            write_with_temp_file(
                path, lambda temporary_path: data.value.write(temporary_path)
            )
            return
    if data.format == _DataFormat.PLY and isinstance(data, _PlyData):
        write_with_temp_file(
            path,
            lambda temporary_path: save_ply_data(data, temporary_path),
        )
        return
    raise ValueError(f"保存できないデータ形式です: {type(data)}")


def open_data(
    path: Path,
    data_format: _DataFormat | _DataFormatSet,
    reporter: Reporter,
    *,
    stb_version: _StbVersion | None = None,
    encoding: str | None = None,
    enable_repair: bool = False,
    max_size: int | None = None,
) -> _Data:
    format_set = _normalize_format_set(
        data_format,
        kind=_DataKind.OBJECT,
        stb_version=stb_version,
    )
    match format_set.format:
        case _DataFormat.STB:
            stb_file: StbFileData = StbFileData(
                path,
                stb_version=format_set.stb_version or _StbVersion.UNSPECIFIED,
                encoding=encoding,
            )
            result = _execute_step(
                StbLoadStep(),
                stb_file,
                context=_ExecutionContext(reporter=reporter, max_size=max_size),
            )
            data: StbData[StBridgeRoot] = result.output
            if enable_repair:
                repaired = _execute_step(
                    StbRepairStep[StBridgeRoot](),
                    data,
                    context=_ExecutionContext(reporter=reporter),
                )
                data = repaired.output
            return data
        case _DataFormat.IFC:
            from ...._internal.optional_dependencies import ifc_pipeline

            return ifc_pipeline.open_ifc_data(path)
        case _:
            raise _UnsupportedConversionError(
                f"読み込みできないデータ形式です: {format_set.format}"
            )


def open_text_data(
    text: str,
    data_format: _DataFormat | _DataFormatSet,
    reporter: Reporter,
    *,
    stb_version: _StbVersion | None = None,
    enable_repair: bool = False,
    max_size: int | None = None,
) -> _Data:
    format_set = _normalize_format_set(
        data_format,
        kind=_DataKind.OBJECT,
        stb_version=stb_version,
    )
    if format_set.format == _DataFormat.STB:
        stb_text: StbTextData = StbTextData(
            text,
            stb_version=format_set.stb_version or _StbVersion.UNSPECIFIED,
        )
        result = _execute_step(
            StbLoadStep(),
            stb_text,
            context=_ExecutionContext(reporter=reporter, max_size=max_size),
        )
        data: StbData[StBridgeRoot] = result.output
        if enable_repair:
            repaired = _execute_step(
                StbRepairStep[StBridgeRoot](),
                data,
                context=_ExecutionContext(reporter=reporter),
            )
            data = repaired.output
        return data
    if format_set.format == _DataFormat.IFC:
        from ...._internal.optional_dependencies import ifc_pipeline

        return ifc_pipeline.loads_ifc_data(text)
    raise _UnsupportedConversionError(
        f"テキストから読み込みできないデータ形式です: {format_set.format}"
    )


def _get_direct_step(
    input_format: _DataFormatSet,
    output_format: _DataFormatSet,
    *,
    assign_guids: bool = False,
) -> _ExecutableStep[Any, Any]:
    """中間形式を含まない1区間分の変換ステップ"""
    if (
        input_format.format == _DataFormat.STB
        and output_format.format == _DataFormat.STB
    ):
        if input_format.kind in (_DataKind.FILE, _DataKind.TEXT) and (
            output_format.kind == _DataKind.OBJECT
        ):
            loaded_format = _DataFormatSet(
                _DataFormat.STB,
                _DataKind.OBJECT,
                stb_version=_StbVersion.UNSPECIFIED,
            )
            return _compose_steps(
                f"{input_format} -> {output_format}",
                (
                    StbLoadStep(),
                    _get_direct_step(
                        loaded_format,
                        output_format,
                        assign_guids=assign_guids,
                    ),
                ),
            )

        if input_format.kind == _DataKind.OBJECT and (
            output_format.kind == _DataKind.TEXT
        ):
            object_output = _DataFormatSet(
                _DataFormat.STB,
                _DataKind.OBJECT,
                stb_version=output_format.stb_version,
            )
            return _compose_steps(
                f"{input_format} -> {output_format}",
                (
                    _get_direct_step(
                        input_format,
                        object_output,
                        assign_guids=assign_guids,
                    ),
                    StbDumpsStep(),
                ),
            )

        if (
            input_format.kind == _DataKind.OBJECT
            and output_format.kind == _DataKind.OBJECT
        ):
            steps: list[_ExecutableStep[Any, Any]] = []
            output_version = output_format.stb_version or _StbVersion.UNSPECIFIED
            if output_version == _StbVersion.LATEST:
                if input_format.stb_version != _StbVersion.LATEST:
                    steps.append(StbToLatestStep())
            elif output_version != _StbVersion.UNSPECIFIED and (
                input_format.stb_version != output_version
            ):
                steps.append(StbToVersionStep(output_version))
            if assign_guids:
                steps.append(StbAssignGuidsStep())
            return _compose_steps(
                f"{input_format} -> {output_format}",
                steps,
            )

    if input_format == output_format:
        return _NoOpStep()

    if (
        input_format.format == _DataFormat.STB
        and output_format.format == _DataFormat.IFC
        and input_format.kind == _DataKind.OBJECT
        and output_format.kind == _DataKind.OBJECT
    ):
        from ...._internal.optional_dependencies import ifc_pipeline

        steps = []
        if input_format.stb_version != _StbVersion.LATEST:
            steps.append(StbToLatestStep())
        if assign_guids:
            steps.append(StbAssignGuidsStep())
        steps.append(ifc_pipeline.stb_latest_to_ifc_step())
        return _compose_steps("STB to IFC", steps)

    if (
        input_format.format == _DataFormat.IFC
        and output_format.format == _DataFormat.PLY
        and input_format.kind == _DataKind.OBJECT
        and output_format.kind == _DataKind.OBJECT
    ):
        from ...._internal.optional_dependencies import ifc_pipeline

        return ifc_pipeline.IfcDataToPlyStep()

    if (
        input_format.format == _DataFormat.STB
        and output_format.format == _DataFormat.PLY
        and input_format.kind == _DataKind.OBJECT
        and output_format.kind == _DataKind.OBJECT
    ):
        steps = []
        if input_format.stb_version != _StbVersion.LATEST:
            steps.append(StbToLatestStep())
        if assign_guids:
            steps.append(StbAssignGuidsStep())
        steps.append(_StbToPlyStep())
        return _compose_steps("STB to PLY", steps)

    raise _UnsupportedConversionError(
        f"変換ルートが未実装です: {input_format} -> {output_format}"
    )


def get_step(
    input_format: _DataFormatSet,
    output_format: _DataFormatSet,
    *,
    route_formats: Sequence[_DataFormatSet] | None = None,
    assign_guids: bool = False,
) -> _ExecutableStep[Any, Any]:
    """入力・中間・出力形式から実行可能な変換ステップを組み立てる。"""
    if not route_formats:
        return _get_direct_step(
            input_format,
            output_format,
            assign_guids=assign_guids,
        )

    waypoints = [input_format, *route_formats, output_format]
    steps: list[_ExecutableStep[Any, Any]] = []
    guid_pending = assign_guids
    last_index = len(waypoints) - 2
    for index, (source, target) in enumerate(itertools.pairwise(waypoints)):
        apply_guid = bool(
            guid_pending
            and source.format == _DataFormat.STB
            and (target.format != _DataFormat.STB or index == last_index)
        )
        steps.append(
            _get_direct_step(
                source,
                target,
                assign_guids=apply_guid,
            )
        )
        if apply_guid:
            guid_pending = False

    return _compose_steps(
        f"{input_format} -> {output_format}",
        steps,
    )


def execute_conversion(
    input_data: _Data,
    output_format: _DataFormatSet,
    *,
    route_formats: Sequence[_DataFormatSet] | None = None,
    reporter: Reporter | None = None,
    assign_guids: bool = False,
    output_enable_repair: bool = False,
    on_step_completed: Callable[[str, _Data], None] | None = None,
    work_dir: Path | None = None,
    keep_temporary_files: bool = False,
    ifc_round_digits: int | None = None,
    ifc_round_digits_mm: int | None = None,
) -> _ExecutionResult[_Data]:
    reporter = reporter or get_reporter()
    step = get_step(
        input_data.format_set,
        output_format,
        route_formats=route_formats,
        assign_guids=assign_guids,
    )
    if output_enable_repair and output_format.format == _DataFormat.STB:
        step = _compose_steps(
            "Conversion with Repair",
            (step, StbRepairStep()),
        )
    context = _ExecutionContext(
        work_dir=work_dir,
        keep_temporary_files=keep_temporary_files,
        reporter=reporter,
        on_step_completed=on_step_completed,
        ifc_round_digits=ifc_round_digits,
        ifc_round_digits_mm=ifc_round_digits_mm,
    )
    return _execute_step(step, input_data, context=context)


def cleanup_paths(paths: Sequence[Path]) -> None:
    """パイプラインが生成した一時ファイル・ディレクトリを削除する"""
    for path in reversed(tuple(dict.fromkeys(paths))):
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        else:
            path.unlink(missing_ok=True)


def convert(
    input_path: Path,
    input_format: _DataFormat,
    output_format: _DataFormat,
    result_format: ConvertResultFormat,
    *,
    input_stb_version: _StbVersion = _StbVersion.UNSPECIFIED,
    output_stb_version: _StbVersion | None = None,
    route_formats: Sequence[_DataFormat | _DataFormatSet] | None = None,
    output_path: Path | None = None,
    reporter: Reporter | None = None,
    input_encoding: str | None = None,
    input_enable_repair: bool = False,
    output_enable_repair: bool = False,
    assign_guids: bool = False,
    keep_temporary_files: bool = False,
    ifc_round_digits: int | None = None,
    ifc_round_digits_mm: int | None = None,
) -> str | Path:
    reporter = reporter or get_reporter()
    if output_format == _DataFormat.STB:
        output_stb_version = output_stb_version or _StbVersion.LATEST
    else:
        output_stb_version = None

    input_format_set = _DataFormatSet(
        input_format,
        _DataKind.OBJECT,
        stb_version=input_stb_version if input_format == _DataFormat.STB else None,
    )
    output_format_set = _DataFormatSet(
        output_format,
        _DataKind.OBJECT,
        stb_version=output_stb_version if output_format == _DataFormat.STB else None,
    )
    normalized_routes = [
        route
        if isinstance(route, _DataFormatSet)
        else _DataFormatSet(route, _DataKind.OBJECT)
        for route in (route_formats or ())
    ]

    input_data = open_data(
        input_path,
        input_format_set,
        reporter,
        encoding=input_encoding,
        enable_repair=input_enable_repair,
    )
    result = execute_conversion(
        input_data,
        output_format_set,
        route_formats=normalized_routes,
        reporter=reporter,
        assign_guids=assign_guids,
        output_enable_repair=output_enable_repair,
        keep_temporary_files=keep_temporary_files,
        ifc_round_digits=ifc_round_digits,
        ifc_round_digits_mm=ifc_round_digits_mm,
    )
    try:
        if result_format in (
            ConvertResultFormat.TEXT,
            ConvertResultFormat.FILE_OR_TEXT,
        ):
            return to_text(
                result.output,
                reporter,
            )
        if result_format == ConvertResultFormat.FILE:
            if output_path is None:
                raise ValueError(
                    "output_path must be specified when result_format is FILE"
                )
            save_data(result.output, output_path, reporter)
            return output_path
        raise NotImplementedError(f"未実装の結果形式です: {result_format}")
    finally:
        if not keep_temporary_files:
            cleanup_paths(result.cleanup_paths)
