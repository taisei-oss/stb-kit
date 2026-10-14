use eframe::egui;
use egui::IconData;
use image::ImageError;
use std::sync::Arc;

pub(crate) fn native_options(inner_size: [f32; 2]) -> eframe::NativeOptions {
    let mut viewport = egui::viewport::ViewportBuilder::default().with_inner_size(inner_size);
    if let Ok(icon) = icon_data_from_png_bytes(include_bytes!("../../assets/stbkit_icon_16x16.png"))
    {
        viewport = viewport.with_icon(Arc::new(icon));
    }

    eframe::NativeOptions {
        renderer: eframe::Renderer::Glow,
        multisampling: 4,
        depth_buffer: 24,
        viewport,
        ..Default::default()
    }
}
fn icon_data_from_png_bytes(bytes: &[u8]) -> Result<IconData, ImageError> {
    let image = image::load_from_memory_with_format(bytes, image::ImageFormat::Png)?.to_rgba8();
    let (width, height) = image.dimensions();

    Ok(IconData {
        rgba: image.into_vec(),
        width,
        height,
    })
}
