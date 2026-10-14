// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

//! 節点と線によるモデル図表示用のデータを、BuildingGeometryから作る。
//!
//! 画面上の太さを一定に保つため、帯状に描画する。
//! 頂点シェーダが線分の両端を広げるので、
//! データには頂点ごとに「自分側の点」「反対側の点」「どちら側へ寄せるか」を持たせる。

use super::mesh::{ElementFilter, ViewerSettings};
use crate::data_model::building_geometry::{BuildingGeometry, UINT32_NONE};
use three_d::{InnerSpace, Vector3, Vector4};

/// 線材と重ならないよう、面材の外形線を内側へオフセットする長さ[m]。
const SURFACE_OUTLINE_INSET: f32 = 0.5;

/// 小さな面材では割合で指定する。
const SURFACE_OUTLINE_INSET_RATIO: f32 = 0.2;

/// 鋭角な頂点で外形線が飛び出さないよう、二等分方向の伸長に設ける上限。
const INSET_SCALE_LIMIT: f32 = 5.0;

/// 外周ループを表す値。PythonのSurfaceLoopType.OUTERと同じ。
const PLANE_LOOP_TYPE_OUTER: u8 = 0;

/// 線分1本を帯状に描くための頂点数。
/// 帯は3角形2枚で書くので、1つの線につき6頂点が必要。
const VERTICES_PER_LINE: usize = 6;

/// 線表示のCPU頂点
pub(crate) struct CpuLineView {
    /// 帯meshの三角形頂点。1線分につき6頂点で、各頂点はその線分の自分側の点を持つ。
    pub(crate) line_positions: Vec<Vector3<f32>>,
    /// line_positionsと同じ並びで、線分の反対側の点。
    pub(crate) line_others: Vec<Vector3<f32>>,
    /// line_positionsと同じ並びで、帯のどちら側へ寄せるかを表す。+1か-1。
    pub(crate) line_sides: Vec<f32>,
    /// line_positionsと同じ並びで頂点カラー
    pub(crate) line_colors: Vec<Vector4<f32>>,
    /// 選択強調用に、要素が占めるline_positionsの範囲(開始頂点, 頂点数)。
    pub(crate) element_line_ranges: Vec<Option<(u32, u32)>>,
    /// GL_POINTS用。1節点1頂点。
    pub(crate) node_positions: Vec<Vector3<f32>>,
}

impl CpuLineView {
    pub(crate) fn is_empty(&self) -> bool {
        self.line_positions.is_empty() && self.node_positions.is_empty()
    }
}

#[derive(Default)]
struct LineBuilder {
    positions: Vec<Vector3<f32>>,
    others: Vec<Vector3<f32>>,
    sides: Vec<f32>,
}

impl LineBuilder {
    fn vertex_count(&self) -> usize {
        self.positions.len()
    }

    /// 線分1本を、三角形2枚分の6頂点へ展開して追加する。
    ///
    /// 点を入れ替えると法線の向きも反転するため、終点側のsideは始点側と逆符号にする。
    fn push_line(&mut self, start: Vector3<f32>, end: Vector3<f32>) {
        // 三角形は[始点+, 始点-, 終点+]と[始点-, 終点-, 終点+]。
        const AT_START: [bool; VERTICES_PER_LINE] = [true, true, false, true, false, false];
        const SIDES: [f32; VERTICES_PER_LINE] = [1.0, -1.0, -1.0, -1.0, 1.0, -1.0];

        for (at_start, side) in AT_START.into_iter().zip(SIDES) {
            let (position, other) = if at_start { (start, end) } else { (end, start) };
            self.positions.push(position);
            self.others.push(other);
            self.sides.push(side);
        }
    }
}

pub(crate) fn build_line_view(
    model: &BuildingGeometry,
    settings: &ViewerSettings,
    element_filter: &ElementFilter,
) -> CpuLineView {
    let node_positions = model
        .nodes
        .positions_xyz
        .as_chunks::<3>()
        .0
        .iter()
        .map(|position| to_vector3(position))
        .collect();

    let mut lines = LineBuilder::default();
    let mut line_colors: Vec<Vector4<f32>> = Vec::new();
    let mut element_line_ranges: Vec<Option<(u32, u32)>> = Vec::with_capacity(model.elements.len());

    for element_index in 0..model.elements.len() {
        if !element_filter.is_visible(element_index) {
            element_line_ranges.push(None);
            continue;
        }

        let start_vertex = lines.vertex_count();
        append_element_lines(model, element_index, &mut lines);

        let added = lines.vertex_count() - start_vertex;
        if added == 0 {
            element_line_ranges.push(None);
            continue;
        }

        let color = to_vector4(
            settings
                .get_style_by_kind(model.elements.kind[element_index])
                .color,
        );
        line_colors.resize(lines.vertex_count(), color);

        let range = u32::try_from(start_vertex)
            .ok()
            .zip(u32::try_from(added).ok());
        element_line_ranges.push(range);
    }

    let LineBuilder {
        positions: line_positions,
        others: line_others,
        sides: line_sides,
    } = lines;

    CpuLineView {
        line_positions,
        line_others,
        line_sides,
        line_colors,
        element_line_ranges,
        node_positions,
    }
}

fn append_element_lines(model: &BuildingGeometry, element_index: usize, lines: &mut LineBuilder) {
    let line_shape_index = model.elements.line_shape_index[element_index];
    if line_shape_index != UINT32_NONE {
        let offset = line_shape_index as usize * 6;
        if let Some(start_end) = model.line_shapes.start_end_xyz.get(offset..offset + 6) {
            lines.push_line(to_vector3(&start_end[..3]), to_vector3(&start_end[3..]));
        }
    }

    let plane_shape_index = model.elements.plane_shape_index[element_index];
    if plane_shape_index != UINT32_NONE {
        for (role, points) in plane_loops(model, plane_shape_index as usize) {
            // 外周線は線材と重なるため、内側へずらして見分けられるようにする。
            let points = if role == PLANE_LOOP_TYPE_OUTER {
                inset_loop(&points, SURFACE_OUTLINE_INSET)
            } else {
                points
            };
            append_closed_loop(&points, lines);
        }
    }
}

fn plane_loops(model: &BuildingGeometry, plane_index: usize) -> Vec<(u8, Vec<Vector3<f32>>)> {
    let surfaces = &model.plane_shapes;
    let Some(loop_range) = surfaces
        .plane_loop_offsets
        .get(plane_index)
        .zip(surfaces.plane_loop_offsets.get(plane_index + 1))
    else {
        return Vec::new();
    };

    (*loop_range.0 as usize..*loop_range.1 as usize)
        .filter_map(|loop_index| {
            let start = *surfaces.loop_point_offsets.get(loop_index)? as usize;
            let end = *surfaces.loop_point_offsets.get(loop_index + 1)? as usize;
            let points = surfaces
                .points_xyz
                .get(start * 3..end * 3)?
                .as_chunks::<3>()
                .0
                .iter()
                .map(|position| to_vector3(position))
                .collect();
            Some((*surfaces.loop_types.get(loop_index)?, points))
        })
        .collect()
}

fn append_closed_loop(points: &[Vector3<f32>], lines: &mut LineBuilder) {
    if points.len() < 2 {
        return;
    }
    for (index, point) in points.iter().enumerate() {
        lines.push_line(*point, points[(index + 1) % points.len()]);
    }
}

/// 平面上の閉ループを、面内で内側へ縮めた点を返す
fn inset_loop(points: &[Vector3<f32>], inset: f32) -> Vec<Vector3<f32>> {
    if points.len() < 3 || inset <= 0.0 {
        return points.to_vec();
    }
    let Some(normal) = loop_normal(points) else {
        return points.to_vec();
    };
    let inset = capped_inset(points, inset);
    if inset <= 0.0 {
        return points.to_vec();
    }

    let count = points.len();
    (0..count)
        .map(|index| {
            let pre = points[(index + count - 1) % count];
            let current = points[index];
            let next = points[(index + 1) % count];

            // ループは法線から見て反時計回りなので、辺方向と法線の外積が内向きのベクトルとなる。
            let inward_pre = inward_normal_vector(current - pre, normal);
            let inward_next = inward_normal_vector(next - current, normal);
            let bisector = inward_pre + inward_next;
            let length = bisector.magnitude();
            if length < f32::EPSILON {
                return current;
            }

            // 二等分方向へ進む距離は、辺からの距離をinsetにするため半角のcosで割る。
            // ただし鋭角だと長くなりすぎる場合があるので上限を設ける。
            let direction = bisector / length;
            let half_angle_cos = direction.dot(inward_next);
            let scale = if half_angle_cos > 1.0 / INSET_SCALE_LIMIT {
                1.0 / half_angle_cos
            } else {
                INSET_SCALE_LIMIT
            };
            current + direction * (inset * scale)
        })
        .collect()
}

/// 面法線を求める。計算できない場合Noneを返す。
fn loop_normal(points: &[Vector3<f32>]) -> Option<Vector3<f32>> {
    if points.len() < 3 {
        return None;
    }
    let first = points[0];
    let next = points[1];
    let last = points[points.len() - 1];
    let normal = (next - first).cross(last - first);
    let length = normal.magnitude();
    if !length.is_finite() || length < f32::EPSILON {
        return None;
    }
    Some(normal / length)
}

fn inward_normal_vector(edge: Vector3<f32>, normal: Vector3<f32>) -> Vector3<f32> {
    let cross = normal.cross(edge);
    let length = cross.magnitude();
    if length < f32::EPSILON {
        Vector3::new(0.0, 0.0, 0.0)
    } else {
        cross / length
    }
}

/// 小さなループが裏返らないよう、内側オフセット量に上限を設ける。
fn capped_inset(points: &[Vector3<f32>], inset: f32) -> f32 {
    let mut min = [f32::INFINITY; 3];
    let mut max = [f32::NEG_INFINITY; 3];
    for point in points {
        for (axis, value) in [point.x, point.y, point.z].into_iter().enumerate() {
            min[axis] = min[axis].min(value);
            max[axis] = max[axis].max(value);
        }
    }

    let mut extents = [max[0] - min[0], max[1] - min[1], max[2] - min[2]];
    extents.sort_by(|left, right| left.total_cmp(right));
    // 最小値は0の場合があるので、短辺としては2番目に大きい編を使う
    let in_plane_short_side = extents[1];
    if !in_plane_short_side.is_finite() {
        return 0.0;
    }
    inset.min(in_plane_short_side * SURFACE_OUTLINE_INSET_RATIO)
}

fn to_vector3(position: &[f64]) -> Vector3<f32> {
    Vector3::new(position[0] as f32, position[1] as f32, position[2] as f32)
}

fn to_vector4(color: [u8; 3]) -> Vector4<f32> {
    Vector4::new(
        color[0] as f32 / 255.0,
        color[1] as f32 / 255.0,
        color[2] as f32 / 255.0,
        1.0,
    )
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::data_model::building_geometry::{
        AxisTable, BuildingGeometry, ElementKind, ElementTable, LineShapeTable, NodeTable,
        PlaneShapeTable, PolygonMesh, StoryTable, UINT32_NONE,
    };

    #[test]
    fn line_and_slab_model() {
        let model = BuildingGeometry {
            origin_xyz: [0.0, 0.0, 0.0],
            mesh: PolygonMesh {
                positions: Vec::new(),
                face_vertex_indices: Vec::new(),
                face_offsets: vec![0],
            },
            elements: ElementTable {
                kind: vec![ElementKind::Column.as_u32(), ElementKind::Slab.as_u32()],
                flags: vec![0; 2],
                vertex_start: vec![UINT32_NONE; 2],
                vertex_count: vec![0; 2],
                face_start: vec![UINT32_NONE; 2],
                face_count: vec![0; 2],
                line_shape_index: vec![0, UINT32_NONE],
                plane_shape_index: vec![UINT32_NONE, 0],
                node_start: vec![UINT32_NONE; 2],
                node_count: vec![0; 2],
                story_start: vec![UINT32_NONE; 2],
                story_count: vec![0; 2],
                guid: vec![None; 2],
                xpath: vec![None; 2],
                name: vec![None; 2],
                source_type: vec!["StbColumn".to_owned(), "StbSlab".to_owned()],
                source_id: vec![None; 2],
            },
            line_shapes: LineShapeTable {
                start_end_xyz: vec![0.0, 0.0, 0.0, 0.0, 0.0, 3.0],
                reference_y_xyz: vec![0.0, 0.0, 0.0],
                reference_y_valid: vec![0],
            },
            plane_shapes: PlaneShapeTable {
                points_xyz: vec![
                    // 外周
                    0.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 10.0, 0.0, 0.0, 10.0, 0.0,
                    // 開口
                    2.0, 2.0, 0.0, 3.0, 2.0, 0.0, 3.0, 3.0, 0.0, 2.0, 3.0, 0.0,
                ],
                loop_point_offsets: vec![0, 4, 8],
                plane_loop_offsets: vec![0, 2],
                loop_types: vec![0, 1],
            },
            nodes: NodeTable {
                positions_xyz: vec![0.0, 0.0, 0.0, 0.0, 0.0, 3.0],
                source_id: vec!["1".to_owned(), "2".to_owned()],
                guid: vec![None; 2],
                story_index: vec![UINT32_NONE; 2],
                xpath: vec![None; 2],
            },
            stories: StoryTable {
                source_id: Vec::new(),
                name: Vec::new(),
                elevations: Vec::new(),
            },
            axes: AxisTable {
                points_xyz: Vec::new(),
                point_start: Vec::new(),
                point_count: Vec::new(),
                source_id: Vec::new(),
                name: Vec::new(),
            },
            element_node_indices: Vec::new(),
            element_story_indices: Vec::new(),
            element_bounds: Vec::new(),
            model_bounds: None,
        };

        let line_view = build_line_view(
            &model,
            &ViewerSettings::default(),
            &ElementFilter::all(model.elements.len()),
        );

        assert_eq!(line_view.node_positions.len(), 2);
        // 柱は1つの線、スラブは外周と開口で8つの線。線1本は6頂点
        let column_vertices = VERTICES_PER_LINE;
        let slab_vertices = 8 * VERTICES_PER_LINE;
        assert_eq!(
            line_view.line_positions.len(),
            column_vertices + slab_vertices
        );
        assert_eq!(line_view.line_colors.len(), line_view.line_positions.len());
        assert_eq!(line_view.line_others.len(), line_view.line_positions.len());
        assert_eq!(line_view.line_sides.len(), line_view.line_positions.len());
        assert_eq!(
            line_view.element_line_ranges,
            vec![
                Some((0, column_vertices as u32)),
                Some((column_vertices as u32, slab_vertices as u32)),
            ]
        );

        let column = &line_view.line_positions[..column_vertices];
        let column_others = &line_view.line_others[..column_vertices];
        let start = Vector3::new(0.0, 0.0, 0.0);
        let end = Vector3::new(0.0, 0.0, 3.0);
        for (position, other) in column.iter().zip(column_others) {
            assert!((*position == start && *other == end) || (*position == end && *other == start));
        }
        assert_eq!(column.iter().filter(|point| **point == start).count(), 3);
        assert_eq!(
            line_view.line_sides[..column_vertices],
            [1.0, -1.0, -1.0, -1.0, 1.0, -1.0]
        );
    }

    #[test]
    fn inset_loop_standard() {
        let square = [
            Vector3::new(0.0, 0.0, 0.0),
            Vector3::new(4.0, 0.0, 0.0),
            Vector3::new(4.0, 4.0, 0.0),
            Vector3::new(0.0, 4.0, 0.0),
        ];

        let inset = inset_loop(&square, 0.5);

        assert_eq!(inset.len(), 4);
        assert!((inset[0] - Vector3::new(0.5, 0.5, 0.0)).magnitude() < 1.0e-5);
        assert!((inset[2] - Vector3::new(3.5, 3.5, 0.0)).magnitude() < 1.0e-5);
    }

    #[test]
    fn inset_loop_small() {
        let small_square = [
            Vector3::new(0.0, 0.0, 0.0),
            Vector3::new(0.2, 0.0, 0.0),
            Vector3::new(0.2, 0.2, 0.0),
            Vector3::new(0.0, 0.2, 0.0),
        ];

        let inset = inset_loop(&small_square, SURFACE_OUTLINE_INSET);

        // 短辺0.2mに対して20%=0.04mへ制限
        let expected = 0.2 * SURFACE_OUTLINE_INSET_RATIO;
        assert!((inset[0] - Vector3::new(expected, expected, 0.0)).magnitude() < 1.0e-5);
    }
}
