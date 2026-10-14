// Copyright 2025-2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

use crate::data_model::building_geometry::{
    BuildingGeometry, ElementKind, UINT32_NONE, element_flags,
};
use std::collections::BTreeMap;
use three_d::{CpuMesh, Indices, Positions, Srgba, Vector3, Vector4};

/// RGBによるピッキングで表現できる最大値。
///
/// 0を背景色として使うため、要素idは1からこの値までの対応となる。
const MAX_PICK_ID: usize = 0x00ff_ffff;

/// 階ごとにGPUメッシュを分けるか
const BATCH_BY_STORY: bool = false;

// 要素種別ごとの既定表示色
const COLOR_PRIMARY_STRUCTURE: [u8; 3] = [246, 166, 35];
const COLOR_SECONDARY_STRUCTURE: [u8; 3] = [168, 216, 109];
const COLOR_PLATE: [u8; 3] = [99, 197, 218];
const COLOR_OTHER: [u8; 3] = [255, 255, 255];
const COLOR_ALPHA_SLAB: u8 = 128;
const COLOR_ALPHA_WALL: u8 = 128;
const COLOR_ALPHA_COMPOSITE_CONCRETE: u8 = 96;
const COLOR_SELECTED: [u8; 3] = [255, 0, 0];

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(crate) struct RenderStyle {
    /// RGB値
    pub color: [u8; 3],
    /// 0が透明、255が不透明
    pub alpha: u8,
}

impl RenderStyle {
    pub(crate) const fn opaque(color: [u8; 3]) -> Self {
        Self { color, alpha: 255 }
    }

    pub(crate) const fn translucent(color: [u8; 3], alpha: u8) -> Self {
        Self { color, alpha }
    }

    pub(crate) fn srgba(self) -> Srgba {
        Srgba::new(self.color[0], self.color[1], self.color[2], self.alpha)
    }

    pub(crate) fn is_transparent(self) -> bool {
        self.alpha < 255
    }
}

#[derive(Debug, Clone)]
pub struct ViewerSettings {
    pub(crate) default_style: RenderStyle,
    /// elements.kindごとのスタイル
    pub(crate) kind_styles: Vec<(u32, RenderStyle)>,
    pub(crate) selected_color: [u8; 3],
    /// 合成断面（SRC・CFT）のRC部を半透明にするかどうか。
    pub(crate) translucent_composite_concrete: bool,
}

impl Default for ViewerSettings {
    fn default() -> Self {
        let primary_structure_style = RenderStyle::opaque(COLOR_PRIMARY_STRUCTURE);
        let secondary_structure_style = RenderStyle::opaque(COLOR_SECONDARY_STRUCTURE);

        Self {
            default_style: RenderStyle::opaque(COLOR_OTHER),
            kind_styles: vec![
                (ElementKind::Column.as_u32(), primary_structure_style),
                (ElementKind::Post.as_u32(), secondary_structure_style),
                (ElementKind::Girder.as_u32(), primary_structure_style),
                (ElementKind::Beam.as_u32(), secondary_structure_style),
                (ElementKind::Brace.as_u32(), primary_structure_style),
                (
                    ElementKind::Slab.as_u32(),
                    RenderStyle::translucent(COLOR_PLATE, COLOR_ALPHA_SLAB),
                ),
                (
                    ElementKind::Wall.as_u32(),
                    RenderStyle::translucent(COLOR_PLATE, COLOR_ALPHA_WALL),
                ),
                (ElementKind::Footing.as_u32(), primary_structure_style),
                (ElementKind::StripFooting.as_u32(), primary_structure_style),
                (ElementKind::Pile.as_u32(), primary_structure_style),
                (
                    ElementKind::FoundationColumn.as_u32(),
                    primary_structure_style,
                ),
                (ElementKind::Parapet.as_u32(), secondary_structure_style),
            ],
            selected_color: COLOR_SELECTED,
            translucent_composite_concrete: false,
        }
    }
}

impl ViewerSettings {
    pub(crate) fn get_style_by_kind(&self, kind: u32) -> RenderStyle {
        self.kind_styles
            .iter()
            .find_map(|(registered_kind, style)| (*registered_kind == kind).then_some(*style))
            .unwrap_or(self.default_style)
    }

    /// 合成断面のRCを半透明にしたときの表示設定。
    pub(crate) fn get_style_by_kind_with_translucent_concrete(&self, kind: u32) -> RenderStyle {
        let style = self.get_style_by_kind(kind);
        RenderStyle {
            alpha: style.alpha.min(COLOR_ALPHA_COMPOSITE_CONCRETE),
            ..style
        }
    }
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct ElementFilter {
    visible: Vec<bool>,
}

impl ElementFilter {
    pub fn new(visible: Vec<bool>) -> Self {
        Self { visible }
    }

    pub fn all(element_count: usize) -> Self {
        Self {
            visible: vec![true; element_count],
        }
    }

    pub(crate) fn is_visible(&self, element_index: usize) -> bool {
        self.visible.get(element_index).copied().unwrap_or(false)
    }

    fn validate(&self, element_count: usize) -> Result<(), String> {
        if self.visible.len() != element_count {
            return Err(format!(
                "要素フィルターのlenは要素数と一致させる必要があります: {} != {element_count}",
                self.visible.len()
            ));
        }
        Ok(())
    }
}

/// 描画区分ごとにまとめたCPUメッシュ
pub(crate) struct CpuRenderBatch {
    pub(crate) style: RenderStyle,
    /// 描画オプションで切り替えたときに使う、もう一方の表示設定。
    ///
    /// 現状では合成断面のRCだけが利用。
    /// 半透明の切り替えを頂点の再アップロードなしで行える。
    pub(crate) alternate_style: Option<RenderStyle>,
    /// 通常描画用。フラット法線を持つ。
    pub(crate) mesh: CpuMesh,
    /// ピッキング用の同じ頂点順で設定する要素ID色。
    pub(crate) picking_colors: Vec<Vector4<f32>>,
}

#[derive(Default)]
struct CpuMeshBuilder {
    positions: Vec<Vector3<f32>>,
    indices: Vec<u32>,
    picking_colors: Vec<Vector4<f32>>,
}

impl CpuMeshBuilder {
    /// BuildingGeometryの1要素を追加する。
    ///
    /// 頂点を共有すると、法線が一致しない時に色合いが変になるため、三角形ごとに頂点を独立させて追加する。
    fn append_element(
        &mut self,
        model: &BuildingGeometry,
        element_index: usize,
        picking_color: Option<Vector4<f32>>,
    ) -> Result<(), String> {
        let mesh = model
            .element_mesh_view(element_index)
            .ok_or_else(|| format!("element[{element_index}]に有効なメッシュがありません"))?;

        let additional_vertex_count = mesh.face_count() * 3;
        self.positions.reserve(additional_vertex_count);
        self.indices.reserve(additional_vertex_count);
        if picking_color.is_some() {
            self.picking_colors.reserve(additional_vertex_count);
        }

        for face_index in 0..mesh.face_count() {
            let start = (mesh.face_offsets[face_index] - mesh.index_base) as usize;
            let end = (mesh.face_offsets[face_index + 1] - mesh.index_base) as usize;
            let face = mesh.face_vertex_indices.get(start..end).ok_or_else(|| {
                format!("element[{element_index}] face[{face_index}]が範囲外です")
            })?;

            if face.len() != 3 {
                return Err(format!(
                    "element[{element_index}] face[{face_index}]の頂点数は{}です。stbkit-native用のメッシュを生成する際はallow_polygons=Falseを指定してください",
                    face.len()
                ));
            }

            for global_index in face.iter().copied() {
                let local_index = (global_index - mesh.vertex_base) as usize;
                let coordinate_start = local_index * 3;
                let coordinate_end = coordinate_start + 3;
                let coordinate = mesh
                    .positions
                    .get(coordinate_start..coordinate_end)
                    .ok_or_else(|| {
                        format!(
                            "element[{element_index}] face[{face_index}]が範囲外の頂点を参照しています"
                        )
                    })?;

                let cpu_index = u32::try_from(self.positions.len()).map_err(|_| {
                    format!(
                        "element[{element_index}]を含むメッシュの頂点数がu32の範囲を超えています"
                    )
                })?;
                self.positions
                    .push(Vector3::new(coordinate[0], coordinate[1], coordinate[2]));
                self.indices.push(cpu_index);
                if let Some(color) = picking_color {
                    self.picking_colors.push(color);
                }
            }
        }

        Ok(())
    }

    fn into_cpu_mesh(self) -> CpuMesh {
        CpuMesh {
            positions: Positions::F32(self.positions),
            indices: Indices::U32(self.indices),
            ..Default::default()
        }
    }

    fn into_cpu_render_batch(
        self,
        style: RenderStyle,
        alternate_style: Option<RenderStyle>,
    ) -> CpuRenderBatch {
        let Self {
            positions,
            indices,
            picking_colors,
        } = self;
        let mut mesh = CpuMesh {
            positions: Positions::F32(positions),
            indices: Indices::U32(indices),
            ..Default::default()
        };
        mesh.compute_normals();

        CpuRenderBatch {
            style,
            alternate_style,
            mesh,
            picking_colors,
        }
    }
}

pub(crate) fn build_cpu_render_batches(
    building_geometry: &BuildingGeometry,
    settings: &ViewerSettings,
    filter: &ElementFilter,
) -> Result<Vec<CpuRenderBatch>, String> {
    build_cpu_render_batches_with_story_grouping(
        building_geometry,
        settings,
        filter,
        BATCH_BY_STORY,
    )
}

fn build_cpu_render_batches_with_story_grouping(
    building_geometry: &BuildingGeometry,
    settings: &ViewerSettings,
    filter: &ElementFilter,
    batch_by_story: bool,
) -> Result<Vec<CpuRenderBatch>, String> {
    filter.validate(building_geometry.elements.len())?;

    let mut builders = BTreeMap::<(u32, bool, Option<u32>), CpuMeshBuilder>::new();

    for element_index in 0..building_geometry.elements.len() {
        if !filter.is_visible(element_index) {
            continue;
        }

        let Some(mesh_range) = building_geometry.elements.mesh_range(element_index) else {
            continue;
        };
        if mesh_range.face_count == 0 {
            continue;
        }

        let element_kind = building_geometry.elements.kind[element_index];
        let is_composite_concrete = building_geometry
            .elements
            .has_flag(element_index, element_flags::IS_COMPOSITE_CONCRETE);
        let mut story_index = None;
        if batch_by_story {
            let story_start = building_geometry.elements.story_start[element_index];
            if story_start != UINT32_NONE
                && building_geometry.elements.story_count[element_index] > 0
            {
                story_index = Some(
                    *building_geometry
                        .element_story_indices
                        .get(story_start as usize)
                        .ok_or_else(|| format!("element[{element_index}]のstoryが範囲外です"))?,
                );
            }
        }
        let picking_color = element_index_to_pick_color(element_index)?;
        builders
            .entry((element_kind, is_composite_concrete, story_index))
            .or_default()
            .append_element(building_geometry, element_index, Some(picking_color))?;
    }

    Ok(builders
        .into_iter()
        .map(|((element_kind, is_composite_concrete, _), builder)| {
            let style = settings.get_style_by_kind(element_kind);
            if !is_composite_concrete {
                return builder.into_cpu_render_batch(style, None);
            }
            let translucent_concrete_style =
                settings.get_style_by_kind_with_translucent_concrete(element_kind);
            // 初期スタイルをstyleに、切り替え後をalternate_styleにわたす
            if settings.translucent_composite_concrete {
                builder.into_cpu_render_batch(translucent_concrete_style, Some(style))
            } else {
                builder.into_cpu_render_batch(style, Some(translucent_concrete_style))
            }
        })
        .collect())
}

/// 選択表示用のMesh
///
/// 選択色には光源を使わないため、法線生成は省略する
pub(crate) fn element_cpu_mesh(
    model: &BuildingGeometry,
    element_index: usize,
) -> Result<CpuMesh, String> {
    let mesh_range = model
        .elements
        .mesh_range(element_index)
        .ok_or_else(|| format!("element[{element_index}]にメッシュがありません"))?;
    if mesh_range.face_count == 0 {
        return Err(format!(
            "element[{element_index}]に三角形が含まれていません"
        ));
    }

    let mut builder = CpuMeshBuilder::default();
    builder.append_element(model, element_index, None)?;
    Ok(builder.into_cpu_mesh())
}

/// 要素indexを、背景色と重ならない24bit RGBへ変換する。
fn element_index_to_pick_color(element_index: usize) -> Result<Vector4<f32>, String> {
    let rgb = element_index_to_pick_rgb(element_index)?;
    Ok(Vector4::new(
        rgb[0] as f32 / 255.0,
        rgb[1] as f32 / 255.0,
        rgb[2] as f32 / 255.0,
        1.0,
    ))
}

fn element_index_to_pick_rgb(element_index: usize) -> Result<[u8; 3], String> {
    let pick_id = element_index + 1;
    if pick_id > MAX_PICK_ID {
        return Err(format!(
            "要素インデックス{element_index}は24 bitのピッキングIDの上限を超えています"
        ));
    }

    Ok([
        ((pick_id >> 16) & 0xff) as u8,
        ((pick_id >> 8) & 0xff) as u8,
        (pick_id & 0xff) as u8,
    ])
}

/// ピッキングで読み取ったRGBを要素インデックスへ戻す
pub(crate) fn pick_color_to_element_index(color: [u8; 3]) -> Option<usize> {
    let pick_id = ((color[0] as usize) << 16) | ((color[1] as usize) << 8) | color[2] as usize;
    pick_id.checked_sub(1)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::data_model::building_geometry::{
        AxisTable, ElementTable, LineShapeTable, NodeTable, PlaneShapeTable, PolygonMesh,
        StoryTable, UINT32_NONE,
    };

    fn geometry_for_test(kinds: [u32; 2]) -> BuildingGeometry {
        BuildingGeometry {
            origin_xyz: [0.0, 0.0, 0.0],
            mesh: PolygonMesh {
                positions: vec![
                    0.0, 0.0, 0.0, // element 0-0
                    1.0, 0.0, 0.0, // element 0-1
                    0.0, 1.0, 0.0, // element 0-2
                    0.0, 0.0, 1.0, // element 1-0
                    1.0, 0.0, 1.0, // element 1-1
                    0.0, 1.0, 1.0, // element 1-2
                ],
                face_vertex_indices: vec![
                    0, 1, 2, //element 0
                    3, 4, 5, // element 1
                ],
                face_offsets: vec![0, 3, 6],
            },
            elements: ElementTable {
                kind: kinds.to_vec(),
                flags: vec![0; 2],
                vertex_start: vec![0, 3],
                vertex_count: vec![3, 3],
                face_start: vec![0, 1],
                face_count: vec![1, 1],
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
            },
            line_shapes: LineShapeTable {
                start_end_xyz: Vec::new(),
                reference_y_xyz: Vec::new(),
                reference_y_valid: Vec::new(),
            },
            plane_shapes: PlaneShapeTable {
                points_xyz: Vec::new(),
                loop_point_offsets: vec![0],
                plane_loop_offsets: vec![0],
                loop_types: Vec::new(),
            },
            nodes: NodeTable {
                positions_xyz: Vec::new(),
                source_id: Vec::new(),
                guid: Vec::new(),
                story_index: Vec::new(),
                xpath: Vec::new(),
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
        }
    }
    const SAMPLE_SETTING_DEFAULT_COLOR: [u8; 3] = [180, 180, 180];
    const SAMPLE_SETTING_COLOR_1: [u8; 3] = [100, 120, 140];
    const SAMPLE_SETTING_COLOR_2: [u8; 3] = [150, 170, 190];
    const SAMPLE_SETTING_COLOR_2_ALPHA: u8 = 80;
    const SAMPLE_SETTING_COLOR_SELECTED: [u8; 3] = [255, 0, 0];

    fn settings() -> ViewerSettings {
        ViewerSettings {
            default_style: RenderStyle::opaque(SAMPLE_SETTING_DEFAULT_COLOR),
            kind_styles: vec![
                (1, RenderStyle::opaque(SAMPLE_SETTING_COLOR_1)),
                (
                    2,
                    RenderStyle::translucent(SAMPLE_SETTING_COLOR_2, SAMPLE_SETTING_COLOR_2_ALPHA),
                ),
            ],
            selected_color: SAMPLE_SETTING_COLOR_SELECTED,
            translucent_composite_concrete: false,
        }
    }

    #[test]
    fn default_settings() {
        let settings = ViewerSettings::default();
        let primary_style = RenderStyle::opaque(COLOR_PRIMARY_STRUCTURE);
        let secondary_style = RenderStyle::opaque(COLOR_SECONDARY_STRUCTURE);
        let slab_style = RenderStyle::translucent(COLOR_PLATE, COLOR_ALPHA_SLAB);
        let wall_style = RenderStyle::translucent(COLOR_PLATE, COLOR_ALPHA_WALL);
        let other_style = RenderStyle::opaque(COLOR_OTHER);

        for kind in [
            ElementKind::Column,
            ElementKind::Girder,
            ElementKind::Brace,
            ElementKind::Footing,
            ElementKind::StripFooting,
            ElementKind::Pile,
            ElementKind::FoundationColumn,
        ] {
            assert_eq!(settings.get_style_by_kind(kind.as_u32()), primary_style);
        }
        assert_eq!(
            settings.get_style_by_kind(ElementKind::Slab.as_u32()),
            slab_style
        );
        assert_eq!(
            settings.get_style_by_kind(ElementKind::Wall.as_u32()),
            wall_style
        );
        for kind in [ElementKind::Post, ElementKind::Beam, ElementKind::Parapet] {
            assert_eq!(settings.get_style_by_kind(kind.as_u32()), secondary_style);
        }
        for kind in [
            ElementKind::Unknown,
            ElementKind::IsolatingDevice,
            ElementKind::DampingDevice,
            ElementKind::FrameDampingDevice,
            ElementKind::Open,
            ElementKind::Penetration,
            ElementKind::Joint,
            ElementKind::PanelZone,
            ElementKind::Connection,
            ElementKind::Other,
        ] {
            assert_eq!(settings.get_style_by_kind(kind.as_u32()), other_style);
        }
        assert_eq!(settings.selected_color, COLOR_SELECTED);
    }

    #[test]
    fn same_kind_elements_to_one_batch() {
        let geometry = geometry_for_test([1, 1]);
        let batches = build_cpu_render_batches(
            &geometry,
            &settings(),
            &ElementFilter::all(geometry.elements.len()),
        )
        .unwrap();

        assert_eq!(batches.len(), 1);
        assert_eq!(
            batches[0].style,
            RenderStyle::opaque(SAMPLE_SETTING_COLOR_1)
        );
        assert_eq!(batches[0].mesh.vertex_count(), 6);
        assert_eq!(batches[0].picking_colors.len(), 6);
        assert_eq!(
            batches[0].picking_colors[0],
            element_index_to_pick_color(0).unwrap()
        );
        assert_eq!(
            batches[0].picking_colors[3],
            element_index_to_pick_color(1).unwrap()
        );
    }

    #[test]
    fn different_kinds_to_separate_batches() {
        let geometry = geometry_for_test([1, 2]);
        let batches = build_cpu_render_batches(
            &geometry,
            &settings(),
            &ElementFilter::all(geometry.elements.len()),
        )
        .unwrap();

        assert_eq!(batches.len(), 2);
        assert_eq!(
            batches[0].style,
            RenderStyle::opaque(SAMPLE_SETTING_COLOR_1)
        );
        assert_eq!(
            batches[1].style,
            RenderStyle::translucent(SAMPLE_SETTING_COLOR_2, SAMPLE_SETTING_COLOR_2_ALPHA)
        );
    }

    #[test]
    fn src_batch_with_a_switchable_style() {
        let mut geometry = geometry_for_test([1, 1]);
        geometry.elements.flags = vec![
            element_flags::IS_COMPOSITE_CONCRETE,
            element_flags::IS_COMPOSITE_STEEL,
        ];

        let batches = build_cpu_render_batches(
            &geometry,
            &settings(),
            &ElementFilter::all(geometry.elements.len()),
        )
        .unwrap();

        // 同じkindでも、RC部は別バッチになる
        assert_eq!(batches.len(), 2);
        let opaque = RenderStyle::opaque(SAMPLE_SETTING_COLOR_1);
        let translucent =
            RenderStyle::translucent(SAMPLE_SETTING_COLOR_1, COLOR_ALPHA_COMPOSITE_CONCRETE);

        // BTreeMapのキーは(kind, is_composite_concrete, story_index)なので鉄骨側が先に並ぶ。
        assert_eq!(batches[0].style, opaque);
        assert_eq!(batches[0].alternate_style, None);
        assert_eq!(batches[1].style, opaque);
        assert_eq!(batches[1].alternate_style, Some(translucent));
    }

    #[test]
    fn unregistered_kind() {
        let geometry = geometry_for_test([1, 99]);
        let batches = build_cpu_render_batches(
            &geometry,
            &settings(),
            &ElementFilter::all(geometry.elements.len()),
        )
        .unwrap();

        assert_eq!(batches.len(), 2);
        assert_eq!(
            batches[1].style,
            RenderStyle::opaque(SAMPLE_SETTING_DEFAULT_COLOR)
        );
    }

    #[test]
    fn disable_elements() {
        let geometry = geometry_for_test([1, 1]);
        let batches = build_cpu_render_batches(
            &geometry,
            &settings(),
            &ElementFilter::new(vec![true, false]),
        )
        .unwrap();

        assert_eq!(batches.len(), 1);
        assert_eq!(batches[0].mesh.vertex_count(), 3);
        assert_eq!(batches[0].picking_colors.len(), 3);
    }

    #[test]
    fn picking_color_with_filtering() {
        let geometry = geometry_for_test([1, 1]);
        let batches = build_cpu_render_batches(
            &geometry,
            &settings(),
            &ElementFilter::new(vec![false, true]),
        )
        .unwrap();

        assert_eq!(batches.len(), 1);
        assert_eq!(batches[0].mesh.vertex_count(), 3);
        assert_eq!(
            batches[0].picking_colors[0],
            element_index_to_pick_color(1).unwrap()
        );
    }

    #[test]
    fn filter_length() {
        let geometry = geometry_for_test([1, 1]);
        let result =
            build_cpu_render_batches(&geometry, &settings(), &ElementFilter::new(vec![true]));

        assert!(result.is_err());
    }

    #[test]
    fn picking_color_round_trip() {
        let mut seen_rgbs = std::collections::BTreeSet::new();
        for element_index in (0..=100).chain([255, 65535, MAX_PICK_ID - 1]) {
            let rgb = element_index_to_pick_rgb(element_index).unwrap();
            assert!(
                seen_rgbs.insert(rgb),
                "RGBが重複しました: element_index={element_index}, rgb={rgb:?}"
            );
            assert_eq!(pick_color_to_element_index(rgb), Some(element_index));
        }
        assert_eq!(pick_color_to_element_index([0, 0, 0]), None);
        assert!(element_index_to_pick_rgb(MAX_PICK_ID).is_err());
    }
}
