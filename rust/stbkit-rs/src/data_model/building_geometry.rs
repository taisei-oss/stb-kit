// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

//! Pythonのstbkit.tools._internal.data_model.building_geometryに対応するデータモデル

use std::convert::From;
use uuid::Uuid;

#[cfg(feature = "serde")]
mod optional_uuid_vec {
    use serde::{Deserialize, Deserializer, Serialize, Serializer};
    use uuid::Uuid;

    pub(crate) fn serialize<S>(values: &[Option<Uuid>], serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        values
            .iter()
            .map(|value| value.as_ref().map(ToString::to_string))
            .collect::<Vec<_>>()
            .serialize(serializer)
    }

    pub(crate) fn deserialize<'de, D>(deserializer: D) -> Result<Vec<Option<Uuid>>, D::Error>
    where
        D: Deserializer<'de>,
    {
        Vec::<Option<String>>::deserialize(deserializer)?
            .into_iter()
            .map(|value| {
                value
                    .map(|text| Uuid::parse_str(&text).map_err(serde::de::Error::custom))
                    .transpose()
            })
            .collect()
    }
}

/// u32で参照なしを表す値。PythonのUINT32_NONEと同じ値。
pub(crate) const UINT32_NONE: u32 = u32::MAX;

/// PythonのElementKindに対応する値
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash)]
#[cfg_attr(test, derive(strum::EnumIter, strum::AsRefStr))]
#[cfg_attr(test, strum(serialize_all = "SCREAMING_SNAKE_CASE"))]
#[repr(u32)]
#[allow(dead_code)]
pub(crate) enum ElementKind {
    Unknown = 0,
    Column = 1,
    Post = 2,
    Girder = 3,
    Beam = 4,
    Brace = 5,
    Slab = 6,
    Wall = 7,
    IsolatingDevice = 8,
    DampingDevice = 9,
    FrameDampingDevice = 10,
    Footing = 11,
    StripFooting = 12,
    Pile = 13,
    FoundationColumn = 14,
    Parapet = 15,
    Open = 16,
    Penetration = 17,
    Joint = 18,
    PanelZone = 19,
    Connection = 20,
    Other = 21,
}

impl ElementKind {
    pub(crate) const fn as_u32(self) -> u32 {
        self as u32
    }
}

impl From<ElementKind> for u32 {
    fn from(value: ElementKind) -> Self {
        value.as_u32()
    }
}

/// PythonのElementFlagsに対応する値
pub mod element_flags {
    macro_rules! define_flags {
        ($($name:ident = $value:expr),* $(,)?) => {
            $(pub const $name: u32 = $value;)*

            #[cfg(test)]
            pub(super) const ALL: &[(&str, u32)] = &[$((stringify!($name), $name)),*];
        };
    }

    define_flags! {
        NONE = 0,
        HAS_MESH = 1 << 0,
        HAS_LINE_SHAPE = 1 << 1,
        HAS_PLANE_SHAPE = 1 << 2,
        HAS_NODE_RELATION = 1 << 3,
        HAS_STORY_RELATION = 1 << 4,
        IS_COMPOSITE_CONCRETE = 1 << 5,
        IS_COMPOSITE_STEEL = 1 << 6,
    }
}

/// uuidのバイトサイズ
pub const UUID_SIZE: usize = 16;

/// PythonのMeshRangeに対応
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct MeshRange {
    pub vertex_start: u32,
    pub vertex_count: u32,
    pub face_start: u32,
    pub face_count: u32,
}

/// PythonのPolygonMeshに対応
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct PolygonMesh {
    pub positions: Vec<f32>,
    pub face_vertex_indices: Vec<u32>,
    pub face_offsets: Vec<u32>,
}

impl PolygonMesh {
    pub fn vertex_count(&self) -> usize {
        self.positions.len() / 3
    }

    pub fn face_count(&self) -> usize {
        self.face_offsets.len() - 1
    }

    pub(crate) fn validate(&self) -> Result<(), String> {
        if !self.positions.len().is_multiple_of(3) {
            return Err("mesh positions.len()が3の倍数ではありません".to_owned());
        }
        if self.positions.iter().any(|value| !value.is_finite()) {
            return Err("mesh positionsは有限値でなければなりません".to_owned());
        }
        if self.face_offsets.first().copied() != Some(0) {
            return Err("mesh face_offsetsの先頭は0でなければなりません".to_owned());
        }
        if self
            .face_offsets
            .last()
            .copied()
            .map(|value| value as usize)
            != Some(self.face_vertex_indices.len())
        {
            return Err(
                "mesh face_offsetsの最後の値はface_vertex_indicesの数と一致しなければなりません"
                    .to_owned(),
            );
        }

        for (face_index, offsets) in self.face_offsets.windows(2).enumerate() {
            let start = offsets[0];
            let end = offsets[1];
            if end < start || end - start < 3 {
                return Err(format!(
                    "mesh face[{face_index}]には3個以上の頂点が必要です"
                ));
            }
        }

        let vertex_count = u32::try_from(self.vertex_count())
            .map_err(|_| "mesh の頂点数がu32の範囲を超えています".to_owned())?;
        if let Some(index) = self
            .face_vertex_indices
            .iter()
            .copied()
            .find(|index| *index >= vertex_count)
        {
            return Err(format!(
                "mesh face_vertex_indices[{index}]は頂点の範囲外です({vertex_count})"
            ));
        }
        Ok(())
    }
}

/// PythonのLineShapeTableに対応
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct LineShapeTable {
    pub start_end_xyz: Vec<f64>,
    pub reference_y_xyz: Vec<f64>,
    pub reference_y_valid: Vec<u8>,
}

impl LineShapeTable {
    pub(crate) fn len(&self) -> usize {
        self.reference_y_valid.len()
    }

    pub(crate) fn validate(&self) -> Result<(), String> {
        let count = self.len();
        if self.start_end_xyz.len() != count * 6 {
            return Err("line start_end_xyzの長さは count * 6 である必要があります".to_owned());
        }
        if self.reference_y_xyz.len() != count * 3 {
            return Err("line reference_y_xyzの長さは count * 3 である必要があります".to_owned());
        }
        if self.reference_y_valid.iter().any(|value| *value > 1) {
            return Err("line reference_y_valid の値は 0 または 1 である必要があります".to_owned());
        }
        if self
            .start_end_xyz
            .iter()
            .chain(self.reference_y_xyz.iter())
            .any(|value| !value.is_finite())
        {
            return Err("line 座標、ベクトルは有限値でなければなりません".to_owned());
        }
        Ok(())
    }
}

/// PythonのPlaneShapeTableに対応
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct PlaneShapeTable {
    pub points_xyz: Vec<f64>,
    pub loop_point_offsets: Vec<u32>,
    pub plane_loop_offsets: Vec<u32>,
    pub loop_types: Vec<u8>,
}

impl PlaneShapeTable {
    pub(crate) fn point_count(&self) -> usize {
        self.points_xyz.len() / 3
    }

    pub(crate) fn loop_count(&self) -> usize {
        self.loop_point_offsets.len() - 1
    }

    pub(crate) fn plane_count(&self) -> usize {
        self.plane_loop_offsets.len() - 1
    }

    pub(crate) fn validate(&self) -> Result<(), String> {
        if !self.points_xyz.len().is_multiple_of(3) {
            return Err("plane points_xyzの長さは3の倍数である必要があります".to_owned());
        }
        if self.points_xyz.iter().any(|value| !value.is_finite()) {
            return Err("plane 座標は有限値でなければなりません".to_owned());
        }
        if self.loop_point_offsets.first().copied() != Some(0) {
            return Err("plane loop_point_offsetsは0で開始する必要があります".to_owned());
        }
        if self.plane_loop_offsets.first().copied() != Some(0) {
            return Err("plane plane_loop_offsetsは0で開始する必要があります".to_owned());
        }
        if self
            .loop_point_offsets
            .last()
            .copied()
            .map(|value| value as usize)
            != Some(self.point_count())
        {
            return Err("plane loop_point_offsetの最後は頂点数と一致する必要があります".to_owned());
        }
        if self
            .plane_loop_offsets
            .last()
            .copied()
            .map(|value| value as usize)
            != Some(self.loop_count())
        {
            return Err(
                "plane plane_loop_offsetsの最後はループ数と一致する必要があります".to_owned(),
            );
        }
        if self.loop_types.len() != self.loop_count() {
            return Err("plane loop_types数はループ数と一致する必要があります".to_owned());
        }
        if self.loop_types.iter().any(|value| *value > 1) {
            return Err("plane loop_typesは0または1でなければなりません".to_owned());
        }

        for (loop_index, offsets) in self.loop_point_offsets.windows(2).enumerate() {
            if offsets[1] < offsets[0] || offsets[1] - offsets[0] < 3 {
                return Err(format!(
                    "plane loop[{loop_index}]には少なくとも3点が必要です"
                ));
            }
        }
        for (surface_index, offsets) in self.plane_loop_offsets.windows(2).enumerate() {
            let start = offsets[0] as usize;
            let end = offsets[1] as usize;
            if end <= start {
                return Err(format!(
                    "plane surface[{surface_index}]には少なくとも1つのループが必要です"
                ));
            }
            let loop_types = self.loop_types.get(start..end).ok_or_else(|| {
                format!("plane surface[{surface_index}]のループ範囲はループ数の範囲外です")
            })?;
            let outer_count = loop_types.iter().filter(|role| **role == 0).count();
            if outer_count != 1 {
                return Err(format!(
                    "plane surface[{surface_index}]にはouter loopが1つである必要があります"
                ));
            }
        }
        Ok(())
    }
}

/// PythonのNodeTableに対応する
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct NodeTable {
    pub positions_xyz: Vec<f64>,
    pub source_id: Vec<String>,
    #[cfg_attr(feature = "serde", serde(with = "optional_uuid_vec"))]
    pub guid: Vec<Option<Uuid>>,
    pub story_index: Vec<u32>,
    pub xpath: Vec<Option<String>>,
}

impl NodeTable {
    pub(crate) fn len(&self) -> usize {
        self.source_id.len()
    }

    pub(crate) fn validate(&self, story_count: usize) -> Result<(), String> {
        let count = self.len();
        if self.positions_xyz.len() != count * 3 {
            return Err("node positionsの長さはnode数 * 3と一致する必要があります".to_owned());
        }
        if self.positions_xyz.iter().any(|value| !value.is_finite()) {
            return Err("node 座標は有限値でなければなりません".to_owned());
        }
        if self.story_index.len() != count {
            return Err("node story_index数はnode数と一致する必要があります".to_owned());
        }
        if self.guid.len() != count {
            return Err(format!(
                "node UUIDの数が不正です: expect={count}, actual={}",
                self.guid.len()
            ));
        }
        if self.xpath.len() != count {
            return Err("node xpath数はnode数と一致する必要があります".to_owned());
        }
        if let Some(index) = self
            .story_index
            .iter()
            .copied()
            .find(|index| *index != UINT32_NONE && *index as usize >= story_count)
        {
            return Err(format!("node story_index:{index} は範囲外です"));
        }
        Ok(())
    }
}

/// PythonのStoryTableに対応する
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct StoryTable {
    pub source_id: Vec<String>,
    pub name: Vec<Option<String>>,
    pub elevations: Vec<f64>,
}

impl StoryTable {
    pub fn len(&self) -> usize {
        self.source_id.len()
    }

    pub fn is_empty(&self) -> bool {
        self.len() == 0
    }

    pub(crate) fn validate(&self) -> Result<(), String> {
        let count = self.len();
        if self.name.len() != count || self.elevations.len() != count {
            return Err("story 各列は同じ長さである必要があります".to_owned());
        }
        if self.elevations.iter().any(|value| !value.is_finite()) {
            return Err("story elevationは有限値である必要があります".to_owned());
        }
        Ok(())
    }
}

/// PythonのAxisTableに対応する
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct AxisTable {
    pub points_xyz: Vec<f64>,
    pub point_start: Vec<u32>,
    pub point_count: Vec<u32>,
    pub source_id: Vec<String>,
    pub name: Vec<Option<String>>,
}

impl AxisTable {
    pub fn len(&self) -> usize {
        self.source_id.len()
    }

    pub fn is_empty(&self) -> bool {
        self.len() == 0
    }

    pub(crate) fn validate(&self) -> Result<(), String> {
        let count = self.len();
        if !self.points_xyz.len().is_multiple_of(3) {
            return Err("axis pointsの長さは3の倍数である必要があります".to_owned());
        }
        if self.points_xyz.iter().any(|value| !value.is_finite()) {
            return Err("axis 座標は有限値でなければなりません".to_owned());
        }
        if self.point_start.len() != count
            || self.point_count.len() != count
            || self.name.len() != count
        {
            return Err("axis 各列は同じ長さである必要があります".to_owned());
        }
        let total_points = self.points_xyz.len() / 3;
        for grid_index in 0..count {
            let start = self.point_start[grid_index] as usize;
            let point_count = self.point_count[grid_index] as usize;
            if point_count < 2 || start.saturating_add(point_count) > total_points {
                return Err(format!("axis point_start[{grid_index}]の範囲が不正です"));
            }
        }
        Ok(())
    }
}

/// PythonのElementTableに対応する
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct ElementTable {
    pub kind: Vec<u32>,
    pub flags: Vec<u32>,

    pub vertex_start: Vec<u32>,
    pub vertex_count: Vec<u32>,
    pub face_start: Vec<u32>,
    pub face_count: Vec<u32>,

    pub line_shape_index: Vec<u32>,
    pub plane_shape_index: Vec<u32>,

    pub node_start: Vec<u32>,
    pub node_count: Vec<u32>,
    pub story_start: Vec<u32>,
    pub story_count: Vec<u32>,

    #[cfg_attr(feature = "serde", serde(with = "optional_uuid_vec"))]
    pub guid: Vec<Option<Uuid>>,
    pub xpath: Vec<Option<String>>,
    pub name: Vec<Option<String>>,
    pub source_type: Vec<String>,
    pub source_id: Vec<Option<String>>,
}

impl ElementTable {
    pub fn len(&self) -> usize {
        self.kind.len()
    }

    pub fn is_empty(&self) -> bool {
        self.kind.is_empty()
    }

    /// 要素に指定のフラグが立っていればtrueを返す。範囲外はfalse。
    ///
    /// bitにはelement_flagsの定数を渡す。
    pub fn has_flag(&self, element_index: usize, bit: u32) -> bool {
        self.flags
            .get(element_index)
            .is_some_and(|flags| flags & bit != 0)
    }

    pub fn mesh_range(&self, element_index: usize) -> Option<MeshRange> {
        let vertex_start = *self.vertex_start.get(element_index)?;
        if vertex_start == UINT32_NONE {
            return None;
        }
        Some(MeshRange {
            vertex_start,
            vertex_count: *self.vertex_count.get(element_index)?,
            face_start: *self.face_start.get(element_index)?,
            face_count: *self.face_count.get(element_index)?,
        })
    }

    pub(crate) fn validate(&self) -> Result<(), String> {
        let count = self.len();
        let columns: [(&str, usize); 16] = [
            ("flags", self.flags.len()),
            ("vertex_start", self.vertex_start.len()),
            ("vertex_count", self.vertex_count.len()),
            ("face_start", self.face_start.len()),
            ("face_count", self.face_count.len()),
            ("line_shape_index", self.line_shape_index.len()),
            ("plane_shape_index", self.plane_shape_index.len()),
            ("node_start", self.node_start.len()),
            ("node_count", self.node_count.len()),
            ("story_start", self.story_start.len()),
            ("story_count", self.story_count.len()),
            ("xpath", self.xpath.len()),
            ("name", self.name.len()),
            ("source_type", self.source_type.len()),
            ("source_id", self.source_id.len()),
            ("guid", self.guid.len()),
        ];
        for (name, length) in columns {
            if length != count {
                return Err(format!(
                    "element {name}.len()は{count}である必要があります: actual={length}"
                ));
            }
        }
        Ok(())
    }
}

/// PythonのBuildingGeometryに対応
///
/// Pythonから渡すときにRust所有のVecやStringへコピーされる。
#[derive(Debug, Clone)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct BuildingGeometry {
    pub origin_xyz: [f64; 3],
    pub mesh: PolygonMesh,
    pub elements: ElementTable,
    pub line_shapes: LineShapeTable,
    pub plane_shapes: PlaneShapeTable,
    pub nodes: NodeTable,
    pub stories: StoryTable,
    pub axes: AxisTable,
    pub element_node_indices: Vec<u32>,
    pub element_story_indices: Vec<u32>,

    // Rust専用データ。Pythonからは渡さず、ロード時に生成する。
    ///要素ごとのAABB
    #[cfg_attr(feature = "serde", serde(skip))]
    pub element_bounds: Vec<Option<Aabb>>,
    ///モデル全体のAABB
    #[cfg_attr(feature = "serde", serde(skip))]
    pub model_bounds: Option<Aabb>,
}

impl BuildingGeometry {
    /// 指定した要素の情報を、借用ビューとして返す。
    pub fn element_info(&self, element_index: usize) -> Option<ElementInfo<'_>> {
        if element_index >= self.elements.len() {
            return None;
        }
        Some(ElementInfo {
            kind: self.elements.kind[element_index],
            guid: self.elements.guid[element_index].as_ref(),
            xpath: self.elements.xpath[element_index].as_deref(),
            name: self.elements.name[element_index].as_deref(),
            source_type: &self.elements.source_type[element_index],
            source_id: self.elements.source_id[element_index].as_deref(),
        })
    }

    /// 全体メッシュから1要素分のメッシュを借用ビューとして返す。
    pub fn element_mesh_view(&self, element_index: usize) -> Option<ElementMeshView<'_>> {
        let span = self.elements.mesh_range(element_index)?;
        let vertex_start = span.vertex_start as usize;
        let vertex_end = vertex_start.checked_add(span.vertex_count as usize)?;
        let face_start = span.face_start as usize;
        let face_end = face_start.checked_add(span.face_count as usize)?;
        let index_start = *self.mesh.face_offsets.get(face_start)? as usize;
        let index_end = *self.mesh.face_offsets.get(face_end)? as usize;

        Some(ElementMeshView {
            positions: &self.mesh.positions[vertex_start * 3..vertex_end * 3],
            face_vertex_indices: &self.mesh.face_vertex_indices[index_start..index_end],
            face_offsets: &self.mesh.face_offsets[face_start..=face_end],
            vertex_base: span.vertex_start,
            index_base: index_start as u32,
        })
    }

    /// 指定した要素の節点番号のスライスを返す。
    pub fn element_node_indices(&self, element_index: usize) -> Option<&[u32]> {
        let start = *self.elements.node_start.get(element_index)?;
        if start == UINT32_NONE {
            return Some(&[]);
        }
        let count = *self.elements.node_count.get(element_index)? as usize;
        let start = start as usize;
        let end = start.checked_add(count)?;
        self.element_node_indices.get(start..end)
    }

    /// AABBBをメッシュ頂点から計算する。
    pub fn calc_aabb(&mut self) {
        let element_bounds = (0..self.elements.len())
            .map(|element_index| {
                self.element_mesh_view(element_index)
                    .and_then(|mesh| Aabb::from_flat_positions(mesh.positions))
            })
            .collect();
        self.element_bounds = element_bounds;

        self.model_bounds =
            self.element_bounds
                .iter()
                .flatten()
                .copied()
                .reduce(|mut left, right| {
                    left.extend(right);
                    left
                });
    }

    pub fn validate(&self) -> Result<(), String> {
        if self.origin_xyz.iter().any(|value| !value.is_finite()) {
            return Err("building origin_xyzは有限値である必要があります".to_owned());
        }

        self.mesh.validate()?;
        self.elements.validate()?;
        self.line_shapes.validate()?;
        self.plane_shapes.validate()?;
        self.stories.validate()?;
        self.nodes.validate(self.stories.len())?;
        self.axes.validate()?;

        let vertex_count = self.mesh.vertex_count();
        let face_count = self.mesh.face_count();
        for element_index in 0..self.elements.len() {
            if let Some(span) = self.elements.mesh_range(element_index) {
                let vertex_start = span.vertex_start as usize;
                let vertex_end = vertex_start
                    .checked_add(span.vertex_count as usize)
                    .ok_or_else(|| {
                        format!("element[{element_index}]の頂点範囲がオーバーフローしました")
                    })?;
                let face_start = span.face_start as usize;
                let face_end = face_start
                    .checked_add(span.face_count as usize)
                    .ok_or_else(|| {
                        format!("element[{element_index}]の面範囲がオーバーフローしました")
                    })?;
                if vertex_end > vertex_count {
                    return Err(format!("element[{element_index}]のvertexが範囲外です"));
                }
                if face_end > face_count {
                    return Err(format!("element[{element_index}]のfaceが範囲外です"));
                }

                for face_index in face_start..face_end {
                    let start = self.mesh.face_offsets[face_index] as usize;
                    let end = self.mesh.face_offsets[face_index + 1] as usize;
                    if self.mesh.face_vertex_indices[start..end]
                        .iter()
                        .copied()
                        .any(|index| {
                            let index = index as usize;
                            index < vertex_start || index >= vertex_end
                        })
                    {
                        return Err(format!(
                            "element[{element_index}] face[{face_index}]が他のelementの頂点を参照しています"
                        ));
                    }
                }
            }

            let line_index = self.elements.line_shape_index[element_index];
            if line_index != UINT32_NONE && line_index as usize >= self.line_shapes.len() {
                return Err(format!(
                    "element[{element_index}]のline_shape_indexは範囲外です"
                ));
            }
            let surface_index = self.elements.plane_shape_index[element_index];
            if surface_index != UINT32_NONE
                && surface_index as usize >= self.plane_shapes.plane_count()
            {
                return Err(format!(
                    "element[{element_index}]のplane_shape_indexは範囲外です"
                ));
            }

            let node_start = self.elements.node_start[element_index];
            let node_count = self.elements.node_count[element_index] as usize;
            if node_start != UINT32_NONE {
                let node_start = node_start as usize;
                let node_end = node_start.checked_add(node_count).ok_or_else(|| {
                    format!("element[{element_index}]のnode範囲の計算でオーバーフローしました")
                })?;
                if node_end > self.element_node_indices.len() {
                    return Err(format!("element[{element_index}]のnodeが範囲外です"));
                }
                if self.element_node_indices[node_start..node_end]
                    .iter()
                    .copied()
                    .any(|index| index as usize >= self.nodes.len())
                {
                    return Err(format!("element[{element_index}]のnode_indexは範囲外です"));
                }
            }

            let story_start = self.elements.story_start[element_index];
            let story_count = self.elements.story_count[element_index] as usize;
            if story_start != UINT32_NONE {
                let story_start = story_start as usize;
                let level_end = story_start.checked_add(story_count).ok_or_else(|| {
                    format!("element[{element_index}]のstory範囲の計算でオーバーフローしました")
                })?;
                if level_end > self.element_story_indices.len() {
                    return Err(format!("element[{element_index}]のstoryが範囲外です"));
                }
                if self.element_story_indices[story_start..level_end]
                    .iter()
                    .copied()
                    .any(|index| index as usize >= self.stories.len())
                {
                    return Err(format!("element[{element_index}]のstory_indexは範囲外です"));
                }
            }
        }
        Ok(())
    }
}

/// AABB（Axis-Aligned Bounding Box）
#[derive(Debug, Clone, Copy, PartialEq)]
#[cfg_attr(feature = "serde", derive(serde::Serialize, serde::Deserialize))]
pub struct Aabb {
    /// x, y, zの最小値。
    pub min: [f32; 3],
    /// x, y, zの最大値。
    pub max: [f32; 3],
}

impl Aabb {
    /// xyz平坦配列をからAABBを計算する。頂点0件ならNone。
    pub(crate) fn from_flat_positions(positions: &[f32]) -> Option<Self> {
        let mut chunks = positions.as_chunks::<3>().0.iter();
        let first = chunks.next()?;
        let mut bounds = Self {
            min: [first[0], first[1], first[2]],
            max: [first[0], first[1], first[2]],
        };
        for point in chunks {
            for (axis, value) in point.iter().enumerate() {
                bounds.min[axis] = bounds.min[axis].min(*value);
                bounds.max[axis] = bounds.max[axis].max(*value);
            }
        }
        Some(bounds)
    }

    /// 別のAABBを包含するように自身の範囲を拡張する。
    pub(crate) fn extend(&mut self, other: Self) {
        for axis in 0..3 {
            self.min[axis] = self.min[axis].min(other.min[axis]);
            self.max[axis] = self.max[axis].max(other.max[axis]);
        }
    }
}

/// 1要素のメッシュ借用ビュー。
///
/// 面インデックスとoffsetは全体配列基準のまま保持し、
/// 必要なときはlocal_faceで要素ローカルインデックスへ変換する。
#[derive(Debug)]
pub struct ElementMeshView<'a> {
    /// この要素の頂点範囲だけを切り出しxyzのスライス。
    pub positions: &'a [f32],
    /// 全体頂点配列に対する絶対インデックス。
    pub face_vertex_indices: &'a [u32],
    /// 全体face_vertex_indicesに対する絶対オフセット。
    pub face_offsets: &'a [u32],
    /// 全体頂点番号からローカル番号へ変換するための差分。
    pub vertex_base: u32,
    /// 全体offsetからビュー内offsetへ変換するための差分。
    pub index_base: u32,
}

impl ElementMeshView<'_> {
    pub fn vertex_count(&self) -> usize {
        self.positions.len() / 3
    }

    pub fn face_count(&self) -> usize {
        self.face_offsets.len() - 1
    }

    /// 指定したfaceを、0はじまりのローカル番号へ変換して返す。
    pub fn local_face(&self, face_index: usize) -> Option<Vec<u32>> {
        let start = *self.face_offsets.get(face_index)? - self.index_base;
        let end = *self.face_offsets.get(face_index + 1)? - self.index_base;
        Some(
            self.face_vertex_indices[start as usize..end as usize]
                .iter()
                .map(|index| *index - self.vertex_base)
                .collect(),
        )
    }
}

/// 要素情報を表示するための借用ビュー。
#[derive(Debug)]
pub struct ElementInfo<'a> {
    pub kind: u32,
    pub guid: Option<&'a Uuid>,
    pub xpath: Option<&'a str>,
    pub name: Option<&'a str>,
    pub source_type: &'a str,
    pub source_id: Option<&'a str>,
}

#[cfg(test)]
mod tests {
    use super::{ElementKind, ElementTable, PolygonMesh, UINT32_NONE, element_flags};
    use regex::Regex;
    use std::collections::BTreeMap;
    use strum::IntoEnumIterator;
    #[test]
    fn mesh_validation() {
        // 座標配列の長さが3の倍数ではない
        let mut mesh = PolygonMesh {
            positions: vec![0.0],
            face_vertex_indices: vec![],
            face_offsets: vec![0],
        };
        assert!(mesh.validate().is_err());

        // 頂点数が3で、頂点インデックス3は範囲外。
        mesh.positions = vec![0.0; 9];
        mesh.face_vertex_indices = vec![0, 1, 3];
        mesh.face_offsets = vec![0, 3];
        assert!(mesh.validate().is_err());

        mesh.face_vertex_indices[2] = 2;
        assert!(mesh.validate().is_ok());
    }
    /// ElementKindがRustとPythonで一致することを確認する
    #[test]
    fn element_kind_values_match_python() {
        let source = include_str!(concat!(
            env!("CARGO_MANIFEST_DIR"),
            "/../../python/stbkit/src/stbkit/tools/_internal/data_model/building_geometry.py"
        ));
        let class_pattern =
            Regex::new(r"(?m)^class ElementKind\(IntEnum\):\r?\n((?:[ \t]+[^\r\n]*\r?\n|\r?\n)*)")
                .unwrap();
        let class_body = class_pattern
            .captures(source)
            .expect("PythonのElementKind定義が見つかりません");
        let value_pattern = Regex::new(r"(?m)^    ([A-Z][A-Z0-9_]*) = ([0-9]+)[ \t]*\r?$").unwrap();
        let python_kinds: BTreeMap<String, u32> = value_pattern
            .captures_iter(&class_body[1])
            .map(|captures| (captures[1].to_owned(), captures[2].parse::<u32>().unwrap()))
            .collect();
        let rust_kinds: BTreeMap<String, u32> = ElementKind::iter()
            .map(|kind| (kind.as_ref().to_owned(), kind.as_u32()))
            .collect();

        assert_eq!(rust_kinds, python_kinds);
    }

    /// ElementFlagsがRustとPythonで一致することを確認する
    #[test]
    fn element_flag_values_match_python() {
        let source = include_str!(concat!(
            env!("CARGO_MANIFEST_DIR"),
            "/../../python/stbkit/src/stbkit/tools/_internal/data_model/building_geometry.py"
        ));
        let class_pattern =
            Regex::new(r"(?m)^class ElementFlags\(IntFlag\):\r?\n((?:[ \t]+[^\r\n]*\r?\n|\r?\n)*)")
                .unwrap();
        let class_body = class_pattern
            .captures(source)
            .expect("PythonのElementFlags定義が見つかりません");
        let assignment_pattern =
            Regex::new(r"(?m)^    ([A-Z][A-Z0-9_]*) = ([^\r\n]+)\r?$").unwrap();
        let expression_pattern = Regex::new(r"^([0-9]+)(?: << ([0-9]+))?$").unwrap();
        let python_flags: BTreeMap<String, u32> = assignment_pattern
            .captures_iter(&class_body[1])
            .map(|assignment| {
                let expression = expression_pattern
                    .captures(assignment[2].trim())
                    .expect("ElementFlagsの値は整数または左シフト式である必要があります");
                let value = expression[1].parse::<u32>().unwrap();
                let value = match expression.get(2) {
                    Some(shift) => value
                        .checked_shl(shift.as_str().parse::<u32>().unwrap())
                        .unwrap(),
                    None => value,
                };
                (assignment[1].to_owned(), value)
            })
            .collect();
        let rust_flags: BTreeMap<String, u32> = element_flags::ALL
            .iter()
            .map(|(name, value)| ((*name).to_owned(), *value))
            .collect();

        assert_eq!(rust_flags, python_flags);
    }

    #[test]
    fn element_table_has_flag() {
        let table = ElementTable {
            kind: vec![0, 0],
            flags: vec![
                element_flags::HAS_MESH | element_flags::IS_COMPOSITE_CONCRETE,
                element_flags::HAS_MESH,
            ],
            vertex_start: vec![UINT32_NONE; 2],
            vertex_count: vec![0; 2],
            face_start: vec![UINT32_NONE; 2],
            face_count: vec![0; 2],
            line_shape_index: vec![UINT32_NONE; 2],
            plane_shape_index: vec![UINT32_NONE; 2],
            node_start: vec![UINT32_NONE; 2],
            node_count: vec![0; 2],
            story_start: vec![UINT32_NONE; 2],
            story_count: vec![0; 2],
            guid: vec![None, None],
            xpath: vec![None, None],
            name: vec![None, None],
            source_type: vec!["test".to_owned(); 2],
            source_id: vec![None, None],
        };

        assert!(table.has_flag(0, element_flags::HAS_MESH));
        assert!(table.has_flag(0, element_flags::IS_COMPOSITE_CONCRETE));
        assert!(!table.has_flag(0, element_flags::IS_COMPOSITE_STEEL));
        assert!(table.has_flag(1, element_flags::HAS_MESH));
        assert!(!table.has_flag(1, element_flags::IS_COMPOSITE_CONCRETE));
        assert!(!table.has_flag(1, element_flags::IS_COMPOSITE_STEEL));
        // 範囲外はfalse
        assert!(!table.has_flag(2, element_flags::HAS_MESH));
    }
}
