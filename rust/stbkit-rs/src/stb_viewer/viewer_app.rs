// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

use super::mesh::{ElementFilter, ViewerSettings};
use super::model_viewer::ModelViewer;
use super::viewer_event::{ElementClickEvent, ElementReference, NodeClickEvent};
use crate::data_model::building_geometry::BuildingGeometry;
use eframe::{App, egui, glow};
use std::sync::Arc;

/// 要素クリックをアプリケーション外へ通知するコールバック。
pub type ElementClickHandler = Box<dyn FnMut(&ElementClickEvent) + 'static>;

/// 節点クリックをアプリケーション外へ通知するコールバック。
pub type NodeClickHandler = Box<dyn FnMut(&NodeClickEvent) + 'static>;

pub struct ViewerApp {
    gl: Option<Arc<glow::Context>>,
    model_viewer: Option<ModelViewer>,
    on_element_click: Option<ElementClickHandler>,
    on_node_click: Option<NodeClickHandler>,
    egui_ctx: Option<egui::Context>,
}

impl ViewerApp {
    /// 構築済みのModelViewerから作成
    ///
    /// GLコンテキストを保持しないため、表示モデルの差し替えはできない。
    #[allow(dead_code)]
    pub(crate) fn new(
        model_viewer: ModelViewer,
        on_element_click: Option<ElementClickHandler>,
    ) -> Self {
        Self {
            gl: None,
            model_viewer: Some(model_viewer),
            on_element_click,
            on_node_click: None,
            egui_ctx: None,
        }
    }

    /// eguiのGLコンテキストから作成
    ///
    /// eframe::CreationContextから取得したGLコンテキストを渡す
    pub fn from_gl_context(
        gl: Arc<glow::Context>,
        building_geometry: BuildingGeometry,
        settings: ViewerSettings,
        filter: ElementFilter,
        on_element_click: Option<ElementClickHandler>,
    ) -> Result<Self, String> {
        let model_viewer = ModelViewer::new(Arc::clone(&gl), building_geometry, settings, filter)?;
        Ok(Self {
            gl: Some(gl),
            model_viewer: Some(model_viewer),
            on_element_click,
            on_node_click: None,
            egui_ctx: None,
        })
    }

    /// モデル未設定で作成
    ///
    /// eframe::CreationContextから取得したGLコンテキストを渡す
    pub fn empty(gl: Arc<glow::Context>) -> Self {
        Self {
            gl: Some(gl),
            model_viewer: None,
            on_element_click: None,
            on_node_click: None,
            egui_ctx: None,
        }
    }

    pub fn set_building_geometry(
        &mut self,
        mut geometry: BuildingGeometry,
        settings: ViewerSettings,
        filter: ElementFilter,
    ) -> Result<(), String> {
        geometry.validate()?;
        geometry.calc_aabb();

        let gl = self
            .gl
            .as_ref()
            .map(Arc::clone)
            .ok_or_else(|| "GLコンテキストが初期化されていません".to_owned())?;
        self.model_viewer = Some(ModelViewer::new(gl, geometry, settings, filter)?);
        Ok(())
    }

    pub fn clear_building_geometry(&mut self) {
        self.model_viewer = None;
    }

    pub fn set_element_click_handler(&mut self, handler: Option<ElementClickHandler>) {
        self.on_element_click = handler;
    }

    pub fn set_node_click_handler(&mut self, handler: Option<NodeClickHandler>) {
        self.on_node_click = handler;
    }

    pub fn select_element(&self, reference: &ElementReference) -> Result<bool, String> {
        let Some(model_viewer) = &self.model_viewer else {
            return Ok(false);
        };

        model_viewer
            .select_element_by_reference(reference.xpath.as_deref(), reference.guid.as_deref())
    }

    pub fn request_repaint(&self) {
        if let Some(ctx) = &self.egui_ctx {
            ctx.request_repaint();
        }
    }
}

impl App for ViewerApp {
    #[cfg(target_arch = "wasm32")]
    fn as_any_mut(&mut self) -> Option<&mut dyn std::any::Any> {
        Some(self)
    }

    fn ui(&mut self, ui: &mut egui::Ui, _frame: &mut eframe::Frame) {
        let ctx = ui.ctx().clone();
        self.egui_ctx = Some(ctx.clone());

        egui::CentralPanel::default().show(ui, |ui| {
            if let Some(model_viewer) = &mut self.model_viewer {
                model_viewer.show(&ctx, ui);
            } else {
                ui.centered_and_justified(|ui| {
                    ui.label("ST-Bridgeファイルを開いてください");
                });
            }
        });

        let element_click_event = self
            .model_viewer
            .as_mut()
            .and_then(ModelViewer::take_element_click_event);
        if let Some(event) = element_click_event
            && let Some(handler) = &mut self.on_element_click
        {
            handler(&event);
        }

        let node_click_event = self
            .model_viewer
            .as_mut()
            .and_then(ModelViewer::take_node_click_event);
        if let Some(event) = node_click_event
            && let Some(handler) = &mut self.on_node_click
        {
            handler(&event);
        }
    }
}
