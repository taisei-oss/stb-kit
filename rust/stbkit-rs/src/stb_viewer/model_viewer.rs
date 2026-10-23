// Copyright 2025-2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

use super::common::DisplayMode;
use super::line_renderer::{LineRenderer, project_to_viewport};
use super::line_view::build_line_view;
use super::mesh::{
    CpuRenderBatch, ElementFilter, RenderStyle, ViewerSettings, build_cpu_render_batches,
    element_cpu_mesh, pick_color_to_element_index,
};
use super::viewer_event::{ElementClickEvent, NodeClickEvent};
use crate::data_model::building_geometry::{Aabb, BuildingGeometry};
use eframe::{egui, egui_glow, glow};
use glow::HasContext;
use std::cell::Cell;
#[cfg(target_arch = "wasm32")]
use std::cell::RefCell;
#[cfg(target_arch = "wasm32")]
use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use three_d::{
    Camera, ColorMaterial, CpuMaterial, DepthTest, DirectionalLight, Gm, Light, Mat4, Mesh,
    OrbitControl, PhysicalMaterial, RenderStates, RenderTarget, Srgba, Vector3, Viewport, degrees,
    vec3,
};
use uuid::Uuid;

const VIEWER_BACKGROUND_COLOR: [f32; 4] = [1.0, 1.0, 1.0, 1.0];

/// 節点クリック時の、画面上の許容距離[px]。
const NODE_PICK_TOLERANCE_PX: f32 = 12.0;

/// ソリッド表示用のデータ
struct RenderBatch {
    /// 通常表示用の描画オブジェクト
    visual_gm: Gm<Mesh, PhysicalMaterial>,
    /// 描画オプションで切り替えたときに入れ替えるマテリアル。
    alternate_material: Option<PhysicalMaterial>,
    /// ピッキング用の描画オブジェクト。
    picking_gm: Gm<Mesh, ColorMaterial>,
}

/// 線表示用のデータ
struct LineView {
    renderer: LineRenderer,
    element_line_ranges: Vec<Option<(u32, u32)>>,
    node_positions: Vec<Vector3<f32>>,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum SelectedTarget {
    Element(usize),
    Node(usize),
}

/// three-dの描画状態。
///
/// wasmのglow::ContextはSyncではないため、
/// この値をegui_glow::CallbackFnへ直接渡さないようにする。
struct RenderState {
    ctx: three_d::Context,
    camera: Camera,
    render_batches: Vec<RenderBatch>,
    selected_object: Option<Gm<Mesh, ColorMaterial>>,
    line_view: Option<LineView>,
}

//　描画状態

// nativeではMutexで共有する。
#[cfg(not(target_arch = "wasm32"))]
#[derive(Clone)]
struct RenderStateHandle {
    state: Arc<Mutex<RenderState>>,
}

// wasmではGPUリソースはスレッドローカルへ保持し、Send + Syncな数値IDを描画コールバックへ渡す。
// Copyできるが、.clone()をnative版と同じコードで書くためCloneにする。
#[cfg(target_arch = "wasm32")]
#[derive(Clone)]
struct RenderStateHandle {
    id: usize,
}

#[cfg(target_arch = "wasm32")]
thread_local! {
    static WEB_RENDER_STATES: RefCell<HashMap<usize, RenderState>> =
        RefCell::new(HashMap::new());
    static NEXT_WEB_RENDER_STATE_ID: Cell<usize> = const { Cell::new(1) };
}

#[cfg(not(target_arch = "wasm32"))]
impl RenderStateHandle {
    fn new(state: RenderState) -> Self {
        Self {
            state: Arc::new(Mutex::new(state)),
        }
    }

    fn with_mut<R>(&self, f: impl FnOnce(&mut RenderState) -> R) -> Option<R> {
        let mut state = match self.state.lock() {
            Ok(state) => state,
            Err(poisoned) => poisoned.into_inner(),
        };
        Some(f(&mut state))
    }
}

#[cfg(target_arch = "wasm32")]
impl RenderStateHandle {
    fn new(state: RenderState) -> Self {
        let id = NEXT_WEB_RENDER_STATE_ID.with(|next_id| {
            let id = next_id.get();
            next_id.set(id.wrapping_add(1).max(1));
            id
        });
        WEB_RENDER_STATES.with(|states| {
            let _ = states.borrow_mut().insert(id, state);
        });
        Self { id }
    }

    fn with_mut<R>(&self, f: impl FnOnce(&mut RenderState) -> R) -> Option<R> {
        WEB_RENDER_STATES.with(|states| {
            let mut states = states.borrow_mut();
            states.get_mut(&self.id).map(f)
        })
    }

    fn remove(&self) {
        let state = WEB_RENDER_STATES.with(|states| states.borrow_mut().remove(&self.id));
        drop(state);
    }
}

pub(crate) struct ModelViewer {
    render_state: RenderStateHandle,
    pub(crate) control: OrbitControl,
    /// 選択した要素の描画色
    selected_color: [u8; 3],
    ///要素フィルター
    element_filter: ElementFilter,
    ///モデル
    building_geometry: BuildingGeometry,
    /// ソリッド表示・線表示のモード
    display_mode: DisplayMode,
    /// 線表示に必要なデータを持つかどうか。
    line_view_available: bool,
    /// SRC等の合成構造のRC部を半透明表示するか。
    translucent_composite_concrete: bool,
    /// 合成断面のRCを含むモデルかどうか。含まなければ切り替えを無効化する。
    composite_concrete_available: bool,
    // 現在の選択対象。選択系メソッドは&selfで呼べる必要があるため、Cellで包む。
    selected_target: Cell<Option<SelectedTarget>>,
    // 前フレームで新しく選択された要素インデックス。
    last_clicked_element_index: Option<usize>,
    // 前フレームで新しく選択された節点インデックス。
    last_clicked_node_index: Option<usize>,
    // クリックした座標。
    pending_pick_px: Option<(i32, i32)>,
    // カメラ調整フラグ
    pending_camera_fit: bool,
    // GLのコールバックからUI処理へ渡す選択結果。
    pick_result: Arc<Mutex<Option<usize>>>,
}

impl ModelViewer {
    pub(crate) fn new(
        gl: Arc<glow::Context>,
        building_geometry: BuildingGeometry,
        settings: ViewerSettings,
        filter: ElementFilter,
    ) -> Result<Self, String> {
        let cpu_render_batches = build_cpu_render_batches(&building_geometry, &settings, &filter)?;
        let ctx = three_d::Context::from_gl_context(gl)
            .map_err(|error| format!("three-dのcontextを作成できませんでした: {error:?}"))?;
        let composite_concrete_available = cpu_render_batches
            .iter()
            .any(|batch| batch.alternate_style.is_some());
        let render_batches = cpu_render_batches
            .into_iter()
            .map(|batch| create_render_batch(&ctx, batch))
            .collect::<Result<Vec<_>, _>>()?;
        let cpu_line_view = build_line_view(&building_geometry, &settings, &filter);
        let line_view = if cpu_line_view.is_empty() {
            None
        } else {
            Some(LineView {
                renderer: LineRenderer::new(&ctx, &cpu_line_view)?,
                element_line_ranges: cpu_line_view.element_line_ranges,
                node_positions: cpu_line_view.node_positions,
            })
        };
        let line_view_available = line_view.is_some();
        let (camera, control) = fitted_camera(
            building_geometry.model_bounds,
            Viewport::new_at_origo(800, 600),
        );

        Ok(Self {
            render_state: RenderStateHandle::new(RenderState {
                ctx,
                camera,
                render_batches,
                selected_object: None,
                line_view,
            }),
            control,
            pending_camera_fit: true,
            selected_color: settings.selected_color,
            element_filter: filter,
            building_geometry,
            display_mode: DisplayMode::default(),
            line_view_available,
            translucent_composite_concrete: settings.translucent_composite_concrete,
            composite_concrete_available,
            selected_target: Cell::new(None),
            last_clicked_element_index: None,
            last_clicked_node_index: None,
            pending_pick_px: None,
            pick_result: Arc::new(Mutex::new(None)),
        })
    }

    pub(crate) fn take_element_click_event(&mut self) -> Option<ElementClickEvent> {
        let element_index = self.last_clicked_element_index.take()?;
        let info = self.building_geometry.element_info(element_index)?;
        Some(ElementClickEvent::from_element_info(element_index, info))
    }

    pub(crate) fn take_node_click_event(&mut self) -> Option<NodeClickEvent> {
        let node_index = self.last_clicked_node_index.take()?;
        let nodes = &self.building_geometry.nodes;
        Some(NodeClickEvent {
            node_index,
            source_id: nodes.source_id.get(node_index).cloned().unwrap_or_default(),
            guid: nodes
                .guid
                .get(node_index)
                .and_then(|guid| guid.as_ref())
                .map(|guid| guid.simple().to_string()),
            xpath: nodes.xpath.get(node_index).and_then(Clone::clone),
        })
    }

    /// XPathに対応する要素を選択する。
    /// 表示要素に該当要素がない場合は選択を解除してfalseを返す。
    #[allow(dead_code)]
    pub(crate) fn select_element_by_xpath(&self, xpath: &str) -> Result<bool, String> {
        let Some(element_index) =
            find_element_index_by_xpath(&self.building_geometry.elements.xpath, xpath)
        else {
            self.clear_selected_element();
            return Ok(false);
        };

        if !self.is_element_drawn(element_index) {
            self.clear_selected_element();
            return Ok(false);
        }

        self.select_element(element_index)?;
        Ok(true)
    }

    /// GUIDに対応する要素を選択する。
    /// 表示要素に該当要素がない場合は選択を解除してfalseを返す。
    #[allow(dead_code)]
    pub(crate) fn select_element_by_guid(&self, guid: &str) -> Result<bool, String> {
        let element_index =
            match find_element_index_by_guid(&self.building_geometry.elements.guid, guid) {
                Ok(element_index) => element_index,
                Err(error) => {
                    self.clear_selected_element();
                    return Err(error);
                }
            };
        let Some(element_index) = element_index else {
            self.clear_selected_element();
            return Ok(false);
        };
        if !self.is_element_drawn(element_index) {
            self.clear_selected_element();
            return Ok(false);
        }

        self.select_element(element_index)?;
        Ok(true)
    }

    /// 参照情報から要素を選択する。
    /// GUIDを優先し、見つからない場合はXPathで要素を選択する。
    /// 対応要素がない場合は、現在の選択を維持したままfalseを返す。
    pub(crate) fn select_element_by_reference(
        &self,
        xpath: Option<&str>,
        guid: Option<&str>,
    ) -> Result<bool, String> {
        let Some(element_index) = find_index_by_reference(
            &self.building_geometry.elements.guid,
            &self.building_geometry.elements.xpath,
            guid,
            xpath,
        )?
        else {
            return Ok(false);
        };
        if !self.is_element_drawn(element_index) {
            return Ok(false);
        }

        self.select_element(element_index)?;
        Ok(true)
    }

    /// 参照情報から節点を選択する。
    // 呼び出すコードが現在未公開のため、未使用を許容
    #[allow(dead_code)]
    pub(crate) fn select_node_by_reference(
        &self,
        xpath: Option<&str>,
        guid: Option<&str>,
    ) -> Result<bool, String> {
        if self.display_mode != DisplayMode::Line {
            return Ok(false);
        }

        let Some(node_index) = find_index_by_reference(
            &self.building_geometry.nodes.guid,
            &self.building_geometry.nodes.xpath,
            guid,
            xpath,
        )?
        else {
            return Ok(false);
        };

        self.select_node(node_index);
        Ok(true)
    }

    fn is_element_drawn(&self, element_index: usize) -> bool {
        self.element_filter.is_visible(element_index)
            && self
                .building_geometry
                .elements
                .mesh_range(element_index)
                .is_some_and(|span| span.face_count > 0)
    }

    /// 選択した要素を、指定色で重ねて描画するGPUオブジェクトへ変換する。
    pub(crate) fn select_element(&self, element_index: usize) -> Result<(), String> {
        let cpu_mesh = element_cpu_mesh(&self.building_geometry, element_index)?;
        let selected_color = self.selected_color;
        self.render_state
            .with_mut(|state| {
                let mesh = Mesh::new(&state.ctx, &cpu_mesh);
                let material = ColorMaterial {
                    color: Srgba::new(selected_color[0], selected_color[1], selected_color[2], 255),
                    // 通常メッシュと同じ深度でも選択色を上書きできるようにする
                    render_states: RenderStates {
                        depth_test: DepthTest::LessOrEqual,
                        ..Default::default()
                    },
                    ..Default::default()
                };
                state.selected_object = Some(Gm::new(mesh, material));
            })
            .ok_or_else(|| "3D描画状態を取得できませんでした".to_owned())?;
        self.selected_target
            .set(Some(SelectedTarget::Element(element_index)));
        Ok(())
    }

    /// 線表示で節点を選択する。要素の選択メッシュは解除する。
    fn select_node(&self, node_index: usize) {
        let _ = self.render_state.with_mut(|state| {
            state.selected_object = None;
        });
        self.selected_target
            .set(Some(SelectedTarget::Node(node_index)));
    }

    fn clear_selected_element(&self) {
        let _ = self.render_state.with_mut(|state| {
            state.selected_object = None;
        });
        self.selected_target.set(None);
    }

    pub(crate) fn set_translucent_composite_concrete(&mut self, translucent: bool) {
        if self.translucent_composite_concrete == translucent {
            return;
        }
        self.translucent_composite_concrete = translucent;

        self.render_state.with_mut(|state| {
            for batch in &mut state.render_batches {
                let Some(alternate) = batch.alternate_material.as_mut() else {
                    continue;
                };
                std::mem::swap(&mut batch.visual_gm.material, alternate);
            }
        });
    }

    /// 描画領域の左上へ描画オプションを表示し、占有した矩形を返す。
    /// （矩形は描画オプションパネル操作中にカメラ操作などは反応しないようにする判定に用いる）
    /// Viewの利用をするだけの時はfont読み込みを省略できるように、日本語は使わない。
    fn show_draw_options(
        &mut self,
        ctx: &egui::Context,
        ui: &egui::Ui,
        rect: egui::Rect,
    ) -> egui::Rect {
        let margin = egui::vec2(8.0, 8.0);
        let display_mode = &mut self.display_mode;
        let line_view_available = self.line_view_available;
        let composite_concrete_available = self.composite_concrete_available;
        // マテリアルの差し替えは&mut selfが要るため、UI内では値だけを更新し、ui処理を出た後に反映する。
        let mut translucent_composite_concrete = self.translucent_composite_concrete;

        let response = egui::Area::new(ui.scope_id().with("draw_options"))
            .order(egui::Order::Foreground)
            .fixed_pos(rect.min + margin)
            .constrain_to(rect)
            .show(ctx, |ui| {
                egui::Frame::popup(ui.style()).show(ui, |ui| {
                    egui::CollapsingHeader::new("draw options")
                        .default_open(false)
                        .show(ui, |ui| {
                            ui.add_enabled_ui(line_view_available, |ui| {
                                ui.radio_value(display_mode, DisplayMode::Solid, "Solid");
                                ui.radio_value(display_mode, DisplayMode::Line, "Line");
                            });
                            if !line_view_available {
                                ui.label("This model has no node information");
                            }

                            ui.separator();
                            ui.add_enabled_ui(
                                composite_concrete_available && *display_mode == DisplayMode::Solid,
                                |ui| {
                                    ui.checkbox(
                                        &mut translucent_composite_concrete,
                                        "Make SRC concrete translucent",
                                    );
                                },
                            );
                            if !composite_concrete_available {
                                ui.label("This model has no SRC/CFT member information");
                            }
                        });
                });
            });

        self.set_translucent_composite_concrete(translucent_composite_concrete);
        response.response.rect
    }

    /// クリック位置に最も近い節点(左下原点)
    fn pick_node(&self, pick_x: f32, pick_y: f32) -> Option<usize> {
        if self.display_mode != DisplayMode::Line {
            return None;
        }
        self.render_state.with_mut(|state| {
            let line_view = state.line_view.as_ref()?;
            nearest_node(
                &line_view.node_positions,
                state.camera.projection() * state.camera.view(),
                state.camera.viewport(),
                pick_x,
                pick_y,
            )
        })?
    }

    pub(crate) fn show(&mut self, ctx: &egui::Context, ui: &mut egui::Ui) {
        let picked_element_index = self
            .pick_result
            .lock()
            .ok()
            .and_then(|mut result| result.take());
        if let Some(element_index) = picked_element_index {
            self.last_clicked_element_index = Some(element_index);
            if let Err(message) = self.select_element(element_index) {
                eprintln!("選択要素が描画できませんでした: {message}");
                self.clear_selected_element();
            }
        }

        let (rect, response) = ui.allocate_exact_size(
            egui::vec2(ui.available_width(), ui.available_height()),
            egui::Sense::click_and_drag(),
        );
        // GPU描画前は白く表示する。
        ui.painter()
            .rect_filled(rect, egui::CornerRadius::ZERO, egui::Color32::WHITE);

        if self.pending_camera_fit && rect.width() > 0.0 && rect.height() > 0.0 {
            let ppp = ctx.pixels_per_point();
            let (camera, control) = fitted_camera(
                self.building_geometry.model_bounds,
                Viewport::new_at_origo(
                    ((rect.width() * ppp).round() as u32).max(1),
                    ((rect.height() * ppp).round() as u32).max(1),
                ),
            );
            self.render_state.with_mut(|state| state.camera = camera);
            self.control = control;
            self.pending_camera_fit = false;
        }

        let options_rect = self.show_draw_options(ctx, ui, rect);
        // パネル操作時にカメラが動かないように、ポインタがパネル内にあるフレームは入力を渡さない
        let pointer_on_options = ctx
            .input(|input| input.pointer.latest_pos())
            .is_some_and(|position| options_rect.contains(position));

        // カメラ回転
        if response.dragged() && !pointer_on_options {
            let ppp = ctx.pixels_per_point();
            let delta = ctx.input(|input| input.pointer.delta());
            let dx = delta.x * ppp;
            let dy = delta.y * ppp;

            let mut events = vec![three_d::Event::MouseMotion {
                button: Some(three_d::MouseButton::Left),
                modifiers: three_d::Modifiers::default(),
                position: (0.0, 0.0).into(),
                delta: (dx, dy),
                handled: false,
            }];

            let render_state = self.render_state.clone();
            let control = &mut self.control;
            let _ = render_state.with_mut(|state| {
                control.handle_events(&mut state.camera, &mut events);
            });
        }

        // 拡大縮小
        // パネルのスクロールと拡大縮小が同時に反応しないように3Dビューパネル上にカーソルがある時だけにする。
        let wheel_delta = if response.hovered() && !pointer_on_options {
            ctx.input(|input| input.smooth_scroll_delta.y)
        } else {
            0.0
        };
        if wheel_delta.abs() > 0.0 {
            let mut events = vec![three_d::Event::MouseWheel {
                delta: (0.0, wheel_delta),
                position: (0.0, 0.0).into(),
                modifiers: three_d::Modifiers::default(),
                handled: false,
            }];
            let render_state = self.render_state.clone();
            let control = &mut self.control;
            let _ = render_state.with_mut(|state| {
                control.handle_events(&mut state.camera, &mut events);
            });
        }

        // クリック位置を座標変換して保持
        if response.clicked() && !pointer_on_options {
            let ppp = ctx.pixels_per_point();
            let screen = ctx.viewport_rect();
            if let Some(position) = response.interact_pointer_pos() {
                let in_rect = position.x >= rect.min.x
                    && position.x <= rect.max.x
                    && position.y >= rect.min.y
                    && position.y <= rect.max.y;
                if in_rect {
                    let pick_x = ((position.x - screen.min.x) * ppp).round() as i32;
                    let pick_y = ((screen.max.y - position.y) * ppp).round() as i32;
                    // 節点を先に判定
                    match self.pick_node(pick_x as f32, pick_y as f32) {
                        Some(node_index) => {
                            self.last_clicked_node_index = Some(node_index);
                            self.select_node(node_index);
                        }
                        None => {
                            self.pending_pick_px = Some((pick_x, pick_y));
                        }
                    }
                    ctx.request_repaint();
                }
            }
        }

        let ppp = ctx.pixels_per_point();
        let viewport_rect = ctx.viewport_rect();

        let x_px = ((rect.min.x - viewport_rect.min.x) * ppp).round() as i32;
        let y_px = ((viewport_rect.max.y - rect.max.y) * ppp).round() as i32;
        let w_px = (rect.width() * ppp).round() as i32;
        let h_px = (rect.height() * ppp).round() as i32;
        let fb_w_px = (viewport_rect.width() * ppp).round() as u32;
        let fb_h_px = (viewport_rect.height() * ppp).round() as u32;
        // ピッキング描画で画面色が変わるため、通常描画前に戻すための背景色。
        let background_color = VIEWER_BACKGROUND_COLOR;

        // GPUリソースはコールバックへ渡さず、描画状態だけ渡す。
        // wasmでは数値IDのみになるため、CallbackFnのSend + Sync制約を満たせる。
        let render_state = self.render_state.clone();
        let element_count = self.building_geometry.elements.len();
        let display_mode = self.display_mode;
        let selected_target = self.selected_target.get();
        let selected_color = Srgba::new(
            self.selected_color[0],
            self.selected_color[1],
            self.selected_color[2],
            255,
        );

        let pending_pick_px = std::mem::take(&mut self.pending_pick_px);
        let pick_result_slot = self.pick_result.clone();

        let callback = egui_glow::CallbackFn::new(move |_info, painter| {
            let _ = render_state.with_mut(|state| unsafe {
                let gl = painter.gl();

                gl.enable(glow::SCISSOR_TEST);
                gl.scissor(x_px, y_px, w_px, h_px);

                state.camera.set_viewport(Viewport {
                    x: x_px,
                    y: y_px,
                    width: w_px as u32,
                    height: h_px as u32,
                });

                let target = RenderTarget::screen(&state.ctx, fb_w_px, fb_h_px);

                // クリックされたら1回ピッキング用の画像を描画し、クリック位置の1色を検出する。
                if let Some((pick_x, pick_y)) = pending_pick_px {
                    let max_x = fb_w_px.saturating_sub(1) as i32;
                    let max_y = fb_h_px.saturating_sub(1) as i32;
                    let pick_x = pick_x.clamp(0, max_x);
                    let pick_y = pick_y.clamp(0, max_y);

                    #[cfg(not(target_arch = "wasm32"))]
                    {
                        gl.disable(glow::MULTISAMPLE);
                        gl.disable(glow::FRAMEBUFFER_SRGB);
                    }
                    gl.disable(glow::BLEND);
                    gl.disable(glow::DITHER);
                    gl.clear_color(0.0, 0.0, 0.0, 1.0);
                    gl.depth_mask(true);
                    gl.clear(glow::COLOR_BUFFER_BIT | glow::DEPTH_BUFFER_BIT);

                    // IDにより色を決めるため、色変換を無効にする。
                    let mut picking_camera = state.camera.clone();
                    picking_camera.disable_tone_and_color_mapping();
                    let no_lights: [&dyn Light; 0] = [];
                    target.render(
                        &picking_camera,
                        state.render_batches.iter().map(|batch| &batch.picking_gm),
                        &no_lights,
                    );

                    let mut pixel = [0_u8; 4];
                    gl.read_pixels(
                        pick_x,
                        pick_y,
                        1,
                        1,
                        glow::RGBA,
                        glow::UNSIGNED_BYTE,
                        glow::PixelPackData::Slice(Some(&mut pixel)),
                    );

                    let rgb = [pixel[0], pixel[1], pixel[2]];
                    if let Some(element_index) = pick_color_to_element_index(rgb)
                        .filter(|element_index| *element_index < element_count)
                        && let Ok(mut slot) = pick_result_slot.lock()
                    {
                        *slot = Some(element_index);
                    }

                    #[cfg(not(target_arch = "wasm32"))]
                    {
                        gl.enable(glow::MULTISAMPLE);
                        gl.enable(glow::FRAMEBUFFER_SRGB);
                    }
                    gl.enable(glow::DITHER);
                }

                // 通常描画。
                // 全バッチをまとめて渡すことで、不透明を先に、半透明物を奥から手前へ並べ替えて描画する。
                gl.clear_color(
                    background_color[0],
                    background_color[1],
                    background_color[2],
                    background_color[3],
                );
                gl.depth_mask(true);
                gl.clear(glow::COLOR_BUFFER_BIT | glow::DEPTH_BUFFER_BIT);

                match display_mode {
                    DisplayMode::Solid => {
                        let dir_light = DirectionalLight::new(
                            &state.ctx,
                            1.0,
                            Srgba::WHITE,
                            vec3(3.0, 4.0, -5.0),
                        );
                        // 光が当たらない側が黒くなってしまうので、反対側からも光を当てる
                        let dir_light2 = DirectionalLight::new(
                            &state.ctx,
                            0.5,
                            Srgba::WHITE,
                            vec3(-3.0, -4.0, 5.0),
                        );
                        let lights: [&dyn Light; 2] = [&dir_light, &dir_light2];

                        target.render(
                            &state.camera,
                            state.render_batches.iter().map(|batch| &batch.visual_gm),
                            &lights,
                        );

                        // 選択部材を最後に上書きする。
                        if let Some(selected_object) = &state.selected_object {
                            let no_lights: [&dyn Light; 0] = [];
                            target.render(&state.camera, selected_object, &no_lights);
                        }
                    }
                    DisplayMode::Line => {
                        if let Some(line_view) = &state.line_view {
                            let renderer = &line_view.renderer;
                            renderer.render_lines(gl, &state.camera);
                            renderer.render_nodes(gl, &state.camera, None);

                            // 選択対象は最後に上書きする。
                            match selected_target {
                                Some(SelectedTarget::Element(element_index)) => {
                                    if let Some(range) = line_view
                                        .element_line_ranges
                                        .get(element_index)
                                        .copied()
                                        .flatten()
                                    {
                                        renderer.render_line_range(
                                            gl,
                                            &state.camera,
                                            range,
                                            selected_color,
                                        );
                                    }
                                }
                                Some(SelectedTarget::Node(node_index)) => {
                                    renderer.render_node(
                                        gl,
                                        &state.camera,
                                        node_index as u32,
                                        selected_color,
                                    );
                                }
                                None => {}
                            }
                        }
                    }
                }

                gl.disable(glow::BLEND);
                gl.depth_mask(true);
                gl.disable(glow::SCISSOR_TEST);
            });
        });

        ui.painter().add(egui::PaintCallback {
            rect,
            callback: Arc::new(callback),
        });
    }
}

fn fitted_camera(model_bounds: Option<Aabb>, viewport: Viewport) -> (Camera, OrbitControl) {
    let (position, target, near, far, min_distance, max_distance) = match model_bounds {
        Some(bounds) => {
            let min = vec3(bounds.min[0], bounds.min[1], bounds.min[2]);
            let max = vec3(bounds.max[0], bounds.max[1], bounds.max[2]);
            let target = (min + max) / 2.0;
            let half_size = (max - min) / 2.0;
            let radius = (half_size.x.powi(2) + half_size.y.powi(2) + half_size.z.powi(2))
                .sqrt()
                .max(0.001);
            let vertical_half_fov = 45.0_f32.to_radians() / 2.0;
            let aspect = viewport.width.max(1) as f32 / viewport.height.max(1) as f32;
            let horizontal_half_fov = (vertical_half_fov.tan() * aspect).atan();
            let distance = radius * 1.1 / vertical_half_fov.min(horizontal_half_fov).sin();
            let position = target + vec3(1.0, 1.0, 2.0) * (distance / 6.0_f32.sqrt());
            (
                position,
                target,
                radius * 0.001,
                distance * 2000.0,
                radius * 0.001,
                distance * 1000.0,
            )
        }
        None => (
            vec3(3.0, 3.0, 6.0),
            vec3(0.0, 0.0, 0.0),
            0.1,
            100.0,
            0.001,
            1000.0,
        ),
    };
    let camera = Camera::new_perspective(
        viewport,
        position,
        target,
        vec3(0.0, 0.0, 1.0),
        degrees(45.0),
        near,
        far,
    );
    let control = OrbitControl::new(camera.target(), min_distance, max_distance);
    (camera, control)
}

fn find_element_index_by_xpath(xpaths: &[Option<String>], xpath: &str) -> Option<usize> {
    xpaths
        .iter()
        .position(|candidate| candidate.as_deref() == Some(xpath))
}

fn find_element_index_by_guid(guids: &[Option<Uuid>], guid: &str) -> Result<Option<usize>, String> {
    let guid =
        Uuid::parse_str(guid).map_err(|error| format!("GUIDの形式が不正です: {guid}: {error}"))?;
    Ok(guids
        .iter()
        .position(|candidate| candidate.as_ref() == Some(&guid)))
}

/// GUIDを優先して検索する
fn find_index_by_reference(
    guids: &[Option<Uuid>],
    xpaths: &[Option<String>],
    guid: Option<&str>,
    xpath: Option<&str>,
) -> Result<Option<usize>, String> {
    let mut guid_error = None;
    if let Some(guid) = guid.filter(|guid| !guid.trim().is_empty()) {
        match find_element_index_by_guid(guids, guid) {
            Ok(Some(index)) => return Ok(Some(index)),
            Ok(None) => {}
            Err(error) => guid_error = Some(error),
        }
    }

    if let Some(xpath) = xpath.filter(|xpath| !xpath.trim().is_empty())
        && let Some(index) = find_element_index_by_xpath(xpaths, xpath)
    {
        return Ok(Some(index));
    }

    match guid_error {
        Some(error) => Err(error),
        None => Ok(None),
    }
}

#[cfg(target_arch = "wasm32")]
impl Drop for ModelViewer {
    fn drop(&mut self) {
        // ビューア破棄時にスレッドローカルのGPUリソースを解放する。
        self.render_state.remove();
    }
}

/// クリック位置に最も近い節点を探す。
fn nearest_node(
    node_positions: &[Vector3<f32>],
    view_projection: Mat4,
    viewport: Viewport,
    pick_x: f32,
    pick_y: f32,
) -> Option<usize> {
    let mut nearest: Option<(usize, f32)> = None;
    for (node_index, position) in node_positions.iter().enumerate() {
        let Some((x, y)) = project_to_viewport(view_projection, viewport, *position) else {
            continue;
        };
        let distance_squared = (x - pick_x).powi(2) + (y - pick_y).powi(2);
        if distance_squared > NODE_PICK_TOLERANCE_PX * NODE_PICK_TOLERANCE_PX {
            continue;
        }
        if nearest.is_none_or(|(_, nearest_distance)| distance_squared < nearest_distance) {
            nearest = Some((node_index, distance_squared));
        }
    }
    nearest.map(|(node_index, _)| node_index)
}

fn create_render_batch(
    ctx: &three_d::Context,
    batch: CpuRenderBatch,
) -> Result<RenderBatch, String> {
    let CpuRenderBatch {
        style,
        alternate_style,
        mut mesh,
        picking_colors,
    } = batch;

    let visual_mesh = Mesh::new(ctx, &mesh);
    let visual_material = create_physical_material(ctx, style);
    let alternate_material = alternate_style.map(|style| create_physical_material(ctx, style));

    // ピッキングは法線を必要としないので削除
    mesh.normals = None;
    let mut picking_mesh = Mesh::new(ctx, &mesh);
    // 色はID職を直接指定する
    picking_mesh
        .set_colors(&picking_colors)
        .map_err(|error| format!("ピッキング用の色を設定できませんでした: {error}"))?;
    let picking_material = ColorMaterial {
        color: Srgba::WHITE,
        ..Default::default()
    };

    Ok(RenderBatch {
        visual_gm: Gm::new(visual_mesh, visual_material),
        alternate_material,
        picking_gm: Gm::new(picking_mesh, picking_material),
    })
}

fn create_physical_material(ctx: &three_d::Context, style: RenderStyle) -> PhysicalMaterial {
    let cpu_material = CpuMaterial {
        albedo: style.srgba(),
        ..Default::default()
    };
    if style.is_transparent() {
        PhysicalMaterial::new_transparent(ctx, &cpu_material)
    } else {
        PhysicalMaterial::new_opaque(ctx, &cpu_material)
    }
}

#[cfg(test)]
mod tests {
    use super::find_index_by_reference;
    use super::{NODE_PICK_TOLERANCE_PX, fitted_camera, nearest_node};
    use crate::data_model::building_geometry::Aabb;
    use three_d::{Camera, Vector3, Vector4, Viewport, degrees, vec3};
    use uuid::Uuid;

    #[test]
    fn find_element_index_by_reference_by_guid() {
        let first_guid = Uuid::parse_str("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa").unwrap();
        let second_guid = Uuid::parse_str("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb").unwrap();
        let guids = vec![Some(first_guid), Some(second_guid)];
        let xpaths = vec![Some("/first".to_owned()), Some("/second".to_owned())];

        let index = find_index_by_reference(
            &guids,
            &xpaths,
            Some("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"),
            Some("/first"),
        )
        .unwrap();

        // xpathよりguid優先
        assert_eq!(index, Some(1));
    }

    #[test]
    fn find_element_idex_by_reference_by_xpath() {
        let guids = vec![None, None];
        let xpaths = vec![Some("/first".to_owned()), Some("/second".to_owned())];

        let index = find_index_by_reference(
            &guids,
            &xpaths,
            Some("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
            Some("/second"),
        )
        .unwrap();
        // guidが見つからなければxpathを使用
        assert_eq!(index, Some(1));
    }

    #[test]
    fn find_element_index_by_reference_no_match() {
        let guid = Uuid::parse_str("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa").unwrap();
        let guids = vec![Some(guid)];
        let xpaths = vec![Some("/first".to_owned())];

        let index = find_index_by_reference(
            &guids,
            &xpaths,
            Some("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"),
            Some("/missing"),
        )
        .unwrap();
        // 見つからなければNone
        assert_eq!(index, None);
    }

    #[test]
    fn find_element_index_by_reference_invalid_guid() {
        let guids = vec![None];
        let xpaths = vec![Some("/first".to_owned())];

        let index =
            find_index_by_reference(&guids, &xpaths, Some("invalid-guid"), Some("/first")).unwrap();
        // 無効なguidは無視されxpathで検索
        assert_eq!(index, Some(0));
    }

    #[test]
    fn fitted_camera_contains_all() {
        for scale in [0.001, 1.0, 10000.0] {
            for size in [[8.0, 6.0, 4.0], [1.0, 1.0, 100.0], [100.0, 1.0, 1.0]] {
                let bounds = Aabb {
                    min: [100.0 * scale, -200.0 * scale, 300.0 * scale],
                    max: [
                        (100.0 + size[0]) * scale,
                        (-200.0 + size[1]) * scale,
                        (300.0 + size[2]) * scale,
                    ],
                };
                for (width, height) in [(800, 600), (300, 900), (1400, 400)] {
                    let (camera, _) =
                        fitted_camera(Some(bounds), Viewport::new_at_origo(width, height));
                    let view_projection = camera.projection() * camera.view();
                    for x_coord in [bounds.min[0], bounds.max[0]] {
                        for y_coord in [bounds.min[1], bounds.max[1]] {
                            for z_coord in [bounds.min[2], bounds.max[2]] {
                                let clip =
                                    view_projection * Vector4::new(x_coord, y_coord, z_coord, 1.0);
                                assert!(clip.w > 0.0);
                                for component in [clip.x, clip.y, clip.z] {
                                    assert!((component / clip.w).abs() <= 1.0);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    /// テスト用のXY平面が見える固定カメラ。
    fn camera_for_test() -> Camera {
        Camera::new_perspective(
            Viewport::new_at_origo(800, 600),
            vec3(0.0, 0.0, 10.0),
            vec3(0.0, 0.0, 0.0),
            vec3(0.0, 1.0, 0.0),
            degrees(45.0),
            0.1,
            100.0,
        )
    }

    #[test]
    fn nearest_node_find() {
        let camera = camera_for_test();
        let view_projection = camera.projection() * camera.view();
        let viewport = camera.viewport();
        let center_x = viewport.width as f32 / 2.0;
        let center_y = viewport.height as f32 / 2.0;
        let nodes = [
            Vector3::new(2.0, 0.0, 0.0),
            Vector3::new(0.0, 0.0, 0.0),
            Vector3::new(-2.0, 0.0, 0.0),
        ];

        let index = nearest_node(&nodes, view_projection, viewport, center_x, center_y);

        assert_eq!(index, Some(1));
    }

    #[test]
    fn nearest_node_not_find() {
        let camera = camera_for_test();
        let view_projection = camera.projection() * camera.view();
        let viewport = camera.viewport();
        let center_x = viewport.width as f32 / 2.0;
        let center_y = viewport.height as f32 / 2.0;
        let nodes = [Vector3::new(0.0, 0.0, 0.0)];

        let index = nearest_node(
            &nodes,
            view_projection,
            viewport,
            center_x + NODE_PICK_TOLERANCE_PX * 2.0,
            center_y,
        );

        assert_eq!(index, None);
    }
}
