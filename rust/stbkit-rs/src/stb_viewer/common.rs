#[derive(Debug, Clone, Copy, PartialEq, Eq, Default)]
pub(crate) enum DisplayMode {
    #[default]
    Solid,
    Line,
}

#[cfg(not(target_arch = "wasm32"))]
pub(crate) const VIEWER_WINDOW_SIZE: [f32; 2] = [1200.0, 800.0];
