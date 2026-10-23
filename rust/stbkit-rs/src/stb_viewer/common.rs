// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub(crate) enum DisplayMode {
    #[default]
    Solid,
    Line,
}

#[cfg(not(target_arch = "wasm32"))]
pub(crate) const VIEWER_WINDOW_SIZE: [f32; 2] = [1200.0, 800.0];
