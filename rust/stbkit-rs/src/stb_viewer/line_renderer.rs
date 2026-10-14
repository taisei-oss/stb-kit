// Copyright 2026 TAISEI CORPORATION
// SPDX-License-Identifier: MPL-2.0
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

//! 線や節点を、画面上で太さが一定になるように描画する
//!
//! three-dのAPIは三角形しか描けないため、シェーダとglowの描画呼び出しを行う。

use super::line_view::CpuLineView;
use eframe::glow;
use glow::HasContext;
use three_d::{
    Blend, Camera, Context, DepthTest, Program, RenderStates, Srgba, VertexBuffer, Viewport,
    WriteMask, vec2, vec4,
};

/// 線の太さ[px]
const LINE_WIDTH_PX: f32 = 3.0;
/// 節点の描画サイズ[px]
const NODE_POINT_SIZE_PX: f32 = 9.0;
/// 節点の描画色
const NODE_COLOR: Srgba = Srgba::new(40, 40, 40, 255);

/// 頂点カラーをそのまま使うことを表すoverrideColorの値。
///
/// alphaが負のときは頂点カラーを使い、それ以外は固定色で塗る。
const USE_VERTEX_COLOR: three_d::Vec4 = three_d::Vec4::new(0.0, 0.0, 0.0, -1.0);

/// 線分描画シェーダ
const LINE_VERTEX_SHADER: &str = r"
uniform mat4 viewProjection;
uniform vec2 viewportSize;
uniform float lineWidth;
uniform vec4 overrideColor;
in vec3 position;
in vec3 otherPosition;
in float side;
in vec4 color;
out vec4 vertexColor;
void main() {
    vec4 clip = viewProjection * vec4(position, 1.0);
    vec4 clipOther = viewProjection * vec4(otherPosition, 1.0);
    vec2 screen = clip.xy / clip.w * viewportSize;
    vec2 screenOther = clipOther.xy / clipOther.w * viewportSize;
    vec2 direction = screenOther - screen;
    vec2 normal = dot(direction, direction) > 0.0
        ? normalize(vec2(-direction.y, direction.x))
        : vec2(0.0);
    vec2 offset = normal * side * lineWidth / viewportSize;
    gl_Position = clip + vec4(offset * clip.w, 0.0, 0.0);
    vertexColor = overrideColor.a < 0.0 ? color : overrideColor;
}
";

/// 節点描画シェーダ
const POINT_VERTEX_SHADER: &str = r"
uniform mat4 viewProjection;
uniform vec4 color;
uniform float pointSize;
in vec3 position;
out vec4 vertexColor;
void main() {
    gl_Position = viewProjection * vec4(position, 1.0);
    gl_PointSize = pointSize;
    vertexColor = color;
}
";

/// 線・節点共通のフラグメントシェーダ。
const UNLIT_FRAGMENT_SHADER: &str = r"
in vec4 vertexColor;
layout (location = 0) out vec4 outColor;
void main() {
    outColor = vertexColor;
}
";

pub(crate) struct LineRenderer {
    line_program: Program,
    point_program: Program,
    line_positions: VertexBuffer<three_d::Vec3>,
    line_others: VertexBuffer<three_d::Vec3>,
    line_sides: VertexBuffer<f32>,
    line_colors: VertexBuffer<three_d::Vec4>,
    node_positions: VertexBuffer<three_d::Vec3>,
    line_vertex_count: u32,
    node_count: u32,
}

impl LineRenderer {
    /// CPUの頂点列から、シェーダと頂点バッファを作成する。
    pub(crate) fn new(ctx: &Context, line_view: &CpuLineView) -> Result<Self, String> {
        let line_program = Program::from_source(ctx, LINE_VERTEX_SHADER, UNLIT_FRAGMENT_SHADER)
            .map_err(|error| format!("線描画シェーダプログラムの作成に失敗しました: {error}"))?;
        let point_program = Program::from_source(ctx, POINT_VERTEX_SHADER, UNLIT_FRAGMENT_SHADER)
            .map_err(|error| {
            format!("節点描画シェーダプログラムの作成に失敗しました: {error}")
        })?;

        let line_positions = VertexBuffer::new_with_data(ctx, &line_view.line_positions);
        let line_vertex_count = line_positions.vertex_count();
        let node_positions = VertexBuffer::new_with_data(ctx, &line_view.node_positions);
        let node_count = node_positions.vertex_count();

        Ok(Self {
            line_program,
            point_program,
            line_positions,
            line_others: VertexBuffer::new_with_data(ctx, &line_view.line_others),
            line_sides: VertexBuffer::new_with_data(ctx, &line_view.line_sides),
            line_colors: VertexBuffer::new_with_data(ctx, &line_view.line_colors),
            node_positions,
            line_vertex_count,
            node_count,
        })
    }

    /// 線材・面材の輪郭線を、頂点カラーで描く
    pub(crate) fn render_lines(&self, gl: &glow::Context, camera: &Camera) {
        self.draw_lines(gl, camera, 0, self.line_vertex_count, None, DepthTest::Less);
    }

    /// 指定範囲の線分だけを単色で描き直す。選択部材に使う。
    pub(crate) fn render_line_range(
        &self,
        gl: &glow::Context,
        camera: &Camera,
        range: (u32, u32),
        color: Srgba,
    ) {
        let (first, count) = range;
        self.draw_lines(
            gl,
            camera,
            first,
            count,
            Some(color),
            // 通常描画と同じ深度でも上書きできるようにする
            DepthTest::LessOrEqual,
        );
    }

    /// 全節点を描く。colorを省略すると既定の節点色を使う。
    pub(crate) fn render_nodes(&self, gl: &glow::Context, camera: &Camera, color: Option<Srgba>) {
        self.draw_points(
            gl,
            camera,
            0,
            self.node_count,
            color.unwrap_or(NODE_COLOR),
            DepthTest::Less,
        );
    }

    /// 指定した節点を単色で描き直す。選択節点に使う。
    pub(crate) fn render_node(
        &self,
        gl: &glow::Context,
        camera: &Camera,
        node_index: u32,
        color: Srgba,
    ) {
        if node_index >= self.node_count {
            return;
        }
        self.draw_points(
            gl,
            camera,
            node_index,
            1,
            color,
            // 通常描画と同じ深度でも上書きできるようにする
            DepthTest::LessOrEqual,
        );
    }

    fn draw_lines(
        &self,
        gl: &glow::Context,
        camera: &Camera,
        first: u32,
        count: u32,
        override_color: Option<Srgba>,
        depth_test: DepthTest,
    ) {
        if count == 0 || self.line_vertex_count == 0 {
            return;
        }
        let program = &self.line_program;
        let viewport = camera.viewport();
        program.use_uniform("viewProjection", camera.projection() * camera.view());
        program.use_uniform(
            "viewportSize",
            vec2(viewport.width as f32, viewport.height as f32),
        );
        program.use_uniform("lineWidth", LINE_WIDTH_PX);
        program.use_uniform_if_required(
            "overrideColor",
            override_color.map_or(USE_VERTEX_COLOR, to_vec4),
        );
        program.use_vertex_attribute("position", &self.line_positions);
        program.use_vertex_attribute("otherPosition", &self.line_others);
        program.use_vertex_attribute("side", &self.line_sides);
        program.use_vertex_attribute("color", &self.line_colors);
        program.draw_with(render_states(depth_test), viewport, || unsafe {
            gl.draw_arrays(glow::TRIANGLES, first as i32, count as i32);
        });
    }

    fn draw_points(
        &self,
        gl: &glow::Context,
        camera: &Camera,
        first: u32,
        count: u32,
        color: Srgba,
        depth_test: DepthTest,
    ) {
        if count == 0 || self.node_count == 0 {
            return;
        }

        // gl_PointSizeはWebGL2ではそのまま使えるが、デスクトップでは明示的な許可が必要。
        #[cfg(not(target_arch = "wasm32"))]
        unsafe {
            gl.enable(glow::PROGRAM_POINT_SIZE);
        }

        let program = &self.point_program;
        let viewport = camera.viewport();
        program.use_uniform("viewProjection", camera.projection() * camera.view());
        program.use_uniform_if_required("color", to_vec4(color));
        program.use_uniform_if_required("pointSize", NODE_POINT_SIZE_PX);
        program.use_vertex_attribute("position", &self.node_positions);
        program.draw_with(render_states(depth_test), viewport, || unsafe {
            gl.draw_arrays(glow::POINTS, first as i32, count as i32);
        });

        #[cfg(not(target_arch = "wasm32"))]
        unsafe {
            gl.disable(glow::PROGRAM_POINT_SIZE);
        }
    }
}

fn render_states(depth_test: DepthTest) -> RenderStates {
    RenderStates {
        depth_test,
        write_mask: WriteMask::COLOR_AND_DEPTH,
        blend: Blend::Disabled,
        ..Default::default()
    }
}

fn to_vec4(color: Srgba) -> three_d::Vec4 {
    vec4(
        color.r as f32 / 255.0,
        color.g as f32 / 255.0,
        color.b as f32 / 255.0,
        color.a as f32 / 255.0,
    )
}

pub(crate) fn project_to_viewport(
    view_projection: three_d::Mat4,
    viewport: Viewport,
    position: three_d::Vec3,
) -> Option<(f32, f32)> {
    let clip = view_projection * vec4(position.x, position.y, position.z, 1.0);
    if clip.w <= 0.0 {
        return None;
    }
    let ndc_x = clip.x / clip.w;
    let ndc_y = clip.y / clip.w;
    Some((
        viewport.x as f32 + (ndc_x * 0.5 + 0.5) * viewport.width as f32,
        viewport.y as f32 + (ndc_y * 0.5 + 0.5) * viewport.height as f32,
    ))
}
