// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

//! BuildingGeometryをPythonからRustへ変換する。
//!
//! 変換時はコピーを行い、Rustの所有物とする。

use pyo3::buffer::{Element, PyBuffer};
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyAny;
use uuid::Uuid;

use stbkit_rs::data_model::building_geometry::{
    AxisTable, BuildingGeometry, ElementTable, LineShapeTable, NodeTable, PlaneShapeTable,
    PolygonMesh, StoryTable, UUID_SIZE,
};

fn python_attr_to_rust_vec<T>(
    py: Python<'_>,
    source: &Bound<'_, PyAny>,
    name: &str,
) -> PyResult<Vec<T>>
where
    T: Element,
{
    // array("d")が空の時をPyBuffer<f64>で取得するとBufferErrorが発生する。
    // そのため、事前にlenを確認し、空の場合はVec::new()にする。
    let value = source.getattr(name)?;
    if value.len()? == 0 {
        return Ok(Vec::new());
    }
    PyBuffer::<T>::get(&value)?.to_vec(py)
}

fn guid_array(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<Vec<Option<Uuid>>> {
    let data = python_attr_to_rust_vec::<u8>(py, source, "guid")?;
    let (chunks, remainder) = data.as_chunks::<UUID_SIZE>();
    if !remainder.is_empty() {
        return Err(PyValueError::new_err(format!(
            "UUIDデータの長さは{UUID_SIZE}バイトの倍数である必要があります: {}",
            data.len(),
        )));
    }

    Ok(chunks
        .iter()
        .map(|bytes| (*bytes != [u8::MAX; UUID_SIZE]).then(|| Uuid::from_bytes(*bytes)))
        .collect())
}

fn polygon_mesh(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<PolygonMesh> {
    Ok(PolygonMesh {
        positions: python_attr_to_rust_vec::<f32>(py, source, "positions")?,
        face_vertex_indices: python_attr_to_rust_vec::<u32>(py, source, "face_vertex_indices")?,
        face_offsets: python_attr_to_rust_vec::<u32>(py, source, "face_offsets")?,
    })
}

fn element_table(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<ElementTable> {
    Ok(ElementTable {
        kind: python_attr_to_rust_vec::<u32>(py, source, "kind")?,
        flags: python_attr_to_rust_vec::<u32>(py, source, "flags")?,
        vertex_start: python_attr_to_rust_vec::<u32>(py, source, "vertex_start")?,
        vertex_count: python_attr_to_rust_vec::<u32>(py, source, "vertex_count")?,
        face_start: python_attr_to_rust_vec::<u32>(py, source, "face_start")?,
        face_count: python_attr_to_rust_vec::<u32>(py, source, "face_count")?,
        line_shape_index: python_attr_to_rust_vec::<u32>(py, source, "line_shape_index")?,
        plane_shape_index: python_attr_to_rust_vec::<u32>(py, source, "plane_shape_index")?,
        node_start: python_attr_to_rust_vec::<u32>(py, source, "node_start")?,
        node_count: python_attr_to_rust_vec::<u32>(py, source, "node_count")?,
        story_start: python_attr_to_rust_vec::<u32>(py, source, "story_start")?,
        story_count: python_attr_to_rust_vec::<u32>(py, source, "story_count")?,
        guid: guid_array(py, source)?,
        xpath: source.getattr("xpath")?.extract()?,
        name: source.getattr("name")?.extract()?,
        source_type: source.getattr("source_type")?.extract()?,
        source_id: source.getattr("source_id")?.extract()?,
    })
}

fn line_shape_table(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<LineShapeTable> {
    Ok(LineShapeTable {
        start_end_xyz: python_attr_to_rust_vec::<f64>(py, source, "start_end_xyz")?,
        reference_y_xyz: python_attr_to_rust_vec::<f64>(py, source, "reference_y_xyz")?,
        reference_y_valid: python_attr_to_rust_vec::<u8>(py, source, "reference_y_valid")?,
    })
}

fn plane_shape_table(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<PlaneShapeTable> {
    Ok(PlaneShapeTable {
        points_xyz: python_attr_to_rust_vec::<f64>(py, source, "points_xyz")?,
        loop_point_offsets: python_attr_to_rust_vec::<u32>(py, source, "loop_point_offsets")?,
        plane_loop_offsets: python_attr_to_rust_vec::<u32>(py, source, "plane_loop_offsets")?,
        loop_types: python_attr_to_rust_vec::<u8>(py, source, "loop_types")?,
    })
}

fn node_table(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<NodeTable> {
    Ok(NodeTable {
        positions_xyz: python_attr_to_rust_vec::<f64>(py, source, "positions_xyz")?,
        source_id: source.getattr("source_id")?.extract()?,
        guid: guid_array(py, source)?,
        story_index: python_attr_to_rust_vec::<u32>(py, source, "story_index")?,
        xpath: source.getattr("xpath")?.extract()?,
    })
}

fn story_table(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<StoryTable> {
    Ok(StoryTable {
        source_id: source.getattr("source_id")?.extract()?,
        name: source.getattr("name")?.extract()?,
        elevations: python_attr_to_rust_vec::<f64>(py, source, "elevations")?,
    })
}

fn axis_table(py: Python<'_>, source: &Bound<'_, PyAny>) -> PyResult<AxisTable> {
    Ok(AxisTable {
        points_xyz: python_attr_to_rust_vec::<f64>(py, source, "points_xyz")?,
        point_start: python_attr_to_rust_vec::<u32>(py, source, "point_start")?,
        point_count: python_attr_to_rust_vec::<u32>(py, source, "point_count")?,
        source_id: source.getattr("source_id")?.extract()?,
        name: source.getattr("name")?.extract()?,
    })
}

/// PythonのデータをRustのデータへ変換する。
pub(crate) fn building_geometry_from_python(
    py: Python<'_>,
    source: &Bound<'_, PyAny>,
) -> PyResult<BuildingGeometry> {
    // 転送中にPythonのarrayが変更されないよう、転送前に読み取り専用にする。
    source.call_method0("freeze")?;

    // 各データのコピー
    let origin: [f64; 3] = source.getattr("origin_xyz")?.extract()?;
    let mesh_source = source.getattr("mesh")?;
    let elements_source = source.getattr("elements")?;
    let lines_source = source.getattr("line_shapes")?;
    let surfaces_source = source.getattr("plane_shapes")?;
    let nodes_source = source.getattr("nodes")?;
    let stories_source = source.getattr("stories")?;
    let axes_source = source.getattr("axes")?;

    let mut model = BuildingGeometry {
        origin_xyz: origin,
        mesh: polygon_mesh(py, &mesh_source)?,
        elements: element_table(py, &elements_source)?,
        line_shapes: line_shape_table(py, &lines_source)?,
        plane_shapes: plane_shape_table(py, &surfaces_source)?,
        nodes: node_table(py, &nodes_source)?,
        stories: story_table(py, &stories_source)?,
        axes: axis_table(py, &axes_source)?,
        element_node_indices: python_attr_to_rust_vec::<u32>(py, source, "element_node_indices")?,
        element_story_indices: python_attr_to_rust_vec::<u32>(py, source, "element_story_indices")?,

        // AABBはPythonから渡さないでRust側でメッシュから生成する。
        element_bounds: Vec::new(),
        model_bounds: None,
    };

    // 値のチェック
    model.validate().map_err(PyValueError::new_err)?;
    // AABBの計算
    model.calc_aabb();

    Ok(model)
}

