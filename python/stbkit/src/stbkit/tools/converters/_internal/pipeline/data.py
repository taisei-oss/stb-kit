# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path


class _DataFormat(StrEnum):
    BUILDING_GEOMETRY = "building_geometry"
    IFC = "ifc"
    PLY = "ply"
    STB = "stb"
    STL = "stl"
    WAVEFRONT_OBJ = "wavefront_obj"


class _DataKind(StrEnum):
    BYTES = "bytes"
    DICT = "dict"
    FILE = "file"
    OBJECT = "object"
    TEXT = "text"


class _FileFormat(StrEnum):
    ASCII = "ascii"
    BINARY = "binary"
    JSON = "json"
    STEP = "step"
    XML = "xml"


class _StbVersion(StrEnum):
    LATEST = "latest"
    UNSPECIFIED = "unspecified"
    V2_0_0 = "2.0.0"
    V2_0_1 = "2.0.1"
    V2_0_2 = "2.0.2"
    V2_1_0 = "2.1.0"
    V2_1_1 = "2.1.1"


@dataclass(frozen=True)
class _DataFormatSet:
    format: _DataFormat
    kind: _DataKind
    stb_version: _StbVersion | None = None
    file_format: _FileFormat | None = None

    def __str__(self) -> str:
        parts = [self.format, self.kind]
        if self.stb_version is not None:
            parts.append(self.stb_version)
        if self.file_format is not None:
            parts.append(self.file_format)
        return ":".join(parts)


def _get_extension(format: _DataFormat) -> str:
    match format:
        case _DataFormat.IFC:
            return ".ifc"
        case _DataFormat.WAVEFRONT_OBJ:
            return ".obj"
        case _DataFormat.PLY:
            return ".ply"
        case _DataFormat.STB:
            return ".stb"
        case _DataFormat.STL:
            return ".stl"
        case _:
            raise ValueError(f"サポートしていないフォーマットです: {format}")


@dataclass(frozen=True)
class _Data:
    """変換パイプラインで扱うDataの共通基底クラス"""

    format: _DataFormat
    kind: _DataKind
    stb_version: _StbVersion | None

    @property
    def format_set(self) -> _DataFormatSet:
        return _DataFormatSet(
            format=self.format,
            kind=self.kind,
            stb_version=self.stb_version,
            file_format=getattr(self, "file_format", None),
        )


@dataclass(frozen=True)
class _SerializedData(_Data):
    """リアライズ済み表現の共通基底。"""

    file_format: _FileFormat


@dataclass(frozen=True)
class _FileData(_SerializedData):
    path: Path
    encoding: str | None

    def __init__(
        self,
        format: _DataFormat,
        path: Path,
        file_format: _FileFormat,
        *,
        stb_version: _StbVersion | None = None,
        encoding: str | None = "utf-8",
    ) -> None:
        object.__setattr__(self, "format", format)
        object.__setattr__(self, "kind", _DataKind.FILE)
        object.__setattr__(self, "file_format", file_format)
        object.__setattr__(self, "stb_version", stb_version)
        object.__setattr__(self, "path", path)
        object.__setattr__(self, "encoding", encoding)


@dataclass(frozen=True)
class _TextData(_SerializedData):
    text: str

    def __init__(
        self,
        format: _DataFormat,
        text: str,
        file_format: _FileFormat,
        *,
        stb_version: _StbVersion | None = None,
    ) -> None:
        if file_format is _FileFormat.BINARY:
            raise ValueError("TextDataはFileFormat.BINARYを使用できません")
        object.__setattr__(self, "format", format)
        object.__setattr__(self, "kind", _DataKind.TEXT)
        object.__setattr__(self, "file_format", file_format)
        object.__setattr__(self, "stb_version", stb_version)
        object.__setattr__(self, "text", text)


@dataclass(frozen=True)
class _BytesData(_SerializedData):
    value: bytes

    def __init__(
        self, format: _DataFormat, value: bytes, file_format: _FileFormat
    ) -> None:
        object.__setattr__(self, "format", format)
        object.__setattr__(self, "kind", _DataKind.BYTES)
        object.__setattr__(self, "file_format", file_format)
        object.__setattr__(self, "value", value)


@dataclass(frozen=True)
class _ObjectData[T](_Data):
    value: T

    def __init__(
        self, format: _DataFormat, value: T, *, stb_version: _StbVersion | None = None
    ) -> None:
        object.__setattr__(self, "format", format)
        object.__setattr__(self, "kind", _DataKind.OBJECT)
        object.__setattr__(self, "stb_version", stb_version)
        object.__setattr__(self, "value", value)


@dataclass(frozen=True)
class _DictData(_Data):
    value: Mapping[str, object]

    def __init__(
        self,
        format: _DataFormat,
        value: Mapping[str, object],
        *,
        stb_version: _StbVersion | None = None,
    ) -> None:
        object.__setattr__(self, "format", format)
        object.__setattr__(self, "kind", _DataKind.DICT)
        object.__setattr__(self, "stb_version", stb_version)
        object.__setattr__(self, "value", value)
