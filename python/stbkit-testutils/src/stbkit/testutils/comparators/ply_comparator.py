# Copyright 2026 TAISEI CORPORATION
# SPDX-License-Identifier: MPL-2.0
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import io

import numpy as np
import trimesh
from trimesh import Geometry
from trimesh.caching import TrackedArray

from .text_comparator import CompareResult, TextComparator


class PlyComparator(TextComparator):
    """PLYファイル比較クラス。3d形状的に等価かどうかを判定する。

    IFC→PLY変換は、Windows環境とLinux環境で出力順が変わる場合があるため、
    ファイル完全一致ではなく、3d形状的に等価かどうかを判定する。

    Attributes:
        tolerance (float): 許容誤差
        check_bounds (bool): バウンディングボックスを比較するか
        check_area (bool): 表面積を比較するか
        check_volume (bool): 体積を比較するか（閉メッシュのみ）
    """

    def __init__(
        self,
        *,
        tolerance: float = 1e-6,
        check_bounds: bool = True,
        check_area: bool = True,
        check_volume: bool = True,
    ) -> None:
        self.tolerance = tolerance
        self.check_bounds = check_bounds
        self.check_area = check_area
        self.check_volume = check_volume

    def _vertex_fingerprint(self, vertices: np.ndarray) -> tuple[int, ...]:
        """頂点の順序非依存な配列データ指紋を作成する。

        マイクロメートルの精度で丸めて整数のタプルにする
        Args:
            vertices (np.ndarray): 頂点配列 (N,3)
        """
        q: np.ndarray = np.round(vertices / self.tolerance).astype(np.int64)
        idx: np.ndarray = np.lexsort((q[:, 2], q[:, 1], q[:, 0]))
        q_sorted: np.ndarray = q[idx]
        return tuple(int(v) for v in q_sorted.ravel())

    def compare(
        self,
        expected: str,
        actual: str,
    ) -> CompareResult:
        """2つのPLYファイル文字列を比較し、3d形状的に同等か判定する"""

        # 文字列一致ならOK
        if expected == actual:
            return CompareResult(equal=True, reason=None)

        mesh_excepted: Geometry = trimesh.load(
            io.BytesIO(expected.encode("utf-8")), file_type="ply", process=False
        )
        assert isinstance(mesh_excepted, trimesh.Trimesh)

        mesh_actual: Geometry = trimesh.load(
            io.BytesIO(actual.encode("utf-8")), file_type="ply", process=False
        )
        assert isinstance(mesh_actual, trimesh.Trimesh)

        # bbox
        if self.check_bounds and (
            not np.allclose(
                mesh_excepted.bounds, mesh_actual.bounds, atol=self.tolerance
            )
        ):
            return CompareResult(
                equal=False,
                reason="バウンディングボックスが一致しません",
                diff=f"expected={mesh_excepted.bounds}, actual={mesh_actual.bounds}",
            )

        # 頂点数
        vertices_expected: TrackedArray = mesh_excepted.vertices
        vertices_actual: TrackedArray = mesh_actual.vertices
        if len(vertices_expected) != len(vertices_actual):
            return CompareResult(
                equal=False,
                reason="節点数が異なります",
                diff=f"expected={len(vertices_expected)}, "
                f"actual={len(vertices_actual)}",
            )

        # 表面積
        if self.check_area:
            area_expected: float = float(mesh_excepted.area)
            area_actual: float = float(mesh_actual.area)
            denom: float = max(area_expected, area_actual, 1.0)
            if abs(area_expected - area_actual) / denom > 1e-7:
                return CompareResult(
                    equal=False,
                    reason="表面積が一致しません",
                    diff=f"expected={area_expected}, actual={area_actual}",
                )

        # 体積(体積が計算できない場合はスキップ)
        if (
            self.check_volume
            and mesh_excepted.is_watertight
            and mesh_actual.is_watertight
        ):
            volume_expected: float = float(mesh_excepted.volume)
            volume_actual: float = float(mesh_actual.volume)
            denom = max(abs(volume_expected), abs(volume_actual), 1.0)
            if abs(volume_expected - volume_actual) / denom > 1e-6:
                return CompareResult(
                    equal=False,
                    reason="体積が一致しません",
                    diff=f"expected={volume_expected}, actual={volume_actual}",
                )

        # 頂点座標（集合として）— 決定的に判定
        fingerprint_expected: tuple[int, ...] = self._vertex_fingerprint(
            vertices_expected
        )
        finger_print_actual: tuple[int, ...] = self._vertex_fingerprint(vertices_actual)
        if fingerprint_expected != finger_print_actual:
            return CompareResult(equal=False, reason="頂点座標が一致しません")

        return CompareResult(equal=True, reason=None)
