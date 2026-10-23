// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

use super::common::VIEWER_WINDOW_SIZE;
use super::mesh::{ElementFilter, ViewerSettings};
use super::viewer_app::{ElementClickHandler, ViewerApp};
use crate::constants::PACKAGE_VERSION;
use crate::data_model::building_geometry::BuildingGeometry;
use crate::utils::desktop_utils::native_options;
use eframe::glow;
use std::sync::Arc;
pub fn run_viewer_window(
    building_geometry: BuildingGeometry,
    settings: ViewerSettings,
    filter: ElementFilter,
    on_element_click: Option<ElementClickHandler>,
) -> eframe::Result<()> {
    let options = native_options(VIEWER_WINDOW_SIZE);

    eframe::run_native(
        &format!("STB-KIT Viewer v{PACKAGE_VERSION}"),
        options,
        Box::new(move |cc| {
            let gl: Arc<glow::Context> = cc
                .gl
                .clone()
                .ok_or_else(|| std::io::Error::other("Glowコンテキストが必要です"))?;
            let app = ViewerApp::from_gl_context(
                gl,
                building_geometry,
                settings,
                filter,
                on_element_click,
            )
            .map_err(std::io::Error::other)?;
            Ok(Box::new(app))
        }),
    )
}
