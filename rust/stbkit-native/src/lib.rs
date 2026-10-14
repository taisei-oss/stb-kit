// Copyright 2025-2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

use pyo3::prelude::*;
use pyo3::types::PyDict;
use stbkit_rs::stb_viewer::{
    ElementClickEvent, ElementClickHandler, ElementFilter, ViewerSettings,
};
mod building_geometry_bridge;
use building_geometry_bridge::building_geometry_from_python;

fn model_viewer_settings() -> ViewerSettings {
    ViewerSettings::default()
}
/// RustのElementClickEventをPythonのdictへ変換してコールバックを呼び出す。
///
/// stbkit-rsにPython型が入らないようにするための処理。
/// Python例外はpanicさせずに内容を表示する。
fn python_element_click_handler(callback: Py<PyAny>) -> ElementClickHandler {
    Box::new(move |event: &ElementClickEvent| {
        Python::attach(|py| {
            let element_click_event = PyDict::new(py);
            let result = (|| -> PyResult<()> {
                element_click_event.set_item("element_index", event.element_index)?;
                element_click_event.set_item("kind", event.kind)?;
                element_click_event.set_item("guid", event.guid.as_deref())?;
                element_click_event.set_item("xpath", event.xpath.as_deref())?;
                element_click_event.set_item("name", event.name.as_deref())?;
                element_click_event.set_item("source_type", &event.source_type)?;
                element_click_event.set_item("source_id", event.source_id.as_deref())?;
                callback.call1(py, (element_click_event,))?;
                Ok(())
            })();
            if let Err(error) = result {
                error.print(py);
            }
        });
    })
}

/// Pythonから呼び出すモジュール
#[pymodule(gil_used = true)]
mod stbkit_native_rs {
    use pyo3::prelude::*;
    /// BuildingGeometryを3D表示する
    ///
    /// ウインドウ表示中はdetachし、Pythonスレッドを停止させない。
    /// コールバックの処理時はattachして呼び出す。
    #[pyfunction]
    #[pyo3(signature = (building_geometry, on_element_click=None))]
    fn _run_viewer(
        py: Python<'_>,
        building_geometry: Py<PyAny>,
        on_element_click: Option<Py<PyAny>>,
    ) -> PyResult<()> {
        let building_geometry =
            super::building_geometry_from_python(py, building_geometry.bind(py))?;
        let element_filter = super::ElementFilter::all(building_geometry.elements.len());
        let settings = super::model_viewer_settings();

        let result = py.detach(move || {
            let handler = on_element_click.map(super::python_element_click_handler);
            stbkit_rs::stb_viewer::run_viewer_window(
                building_geometry,
                settings,
                element_filter,
                handler,
            )
            .map_err(|error| format!("{error:?}"))
        });

        result.map_err(pyo3::exceptions::PyRuntimeError::new_err)
    }
}
