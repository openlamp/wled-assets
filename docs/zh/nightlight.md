# WLED 夜灯

[调色板](palettes.md) · [效果](effects.md) · [控件](controls.md) · **夜灯** · [段](segment.md) · [按钮](buttons.md) · [按钮事件](button-events.md) · [预设](presets.md) · [滑块](fxdata.md) · [信息字段](info.md) · [界面标签](ui.md) &nbsp;•&nbsp; [中文参考](README.md)

<sub>其他语言: [EN](../en/nightlight.md) · [FR](../fr/nightlight.md) · [DE](../de/nightlight.md) · [ES](../es/nightlight.md) · [IT](../it/nightlight.md) · [JA](../ja/nightlight.md) · [KO](../ko/nightlight.md)</sub>

**夜灯**是 WLED 的定时淡出（顶栏月亮图标）。四种模式决定*如何*淡出（`nl.mode`）。

| 图片 | WLED 名称 | 翻译 | 描述 |
|---|---|---|---|
| <img src="../../images/nightlight/instant.png" width="56"> | `Instant` | 即时 | 计时结束时立即熄灭 — 无渐变。 |
| <img src="../../images/nightlight/fade.png" width="56"> | `Fade` | 渐暗 | 在整个时长内亮度逐渐降低。 |
| <img src="../../images/nightlight/colour-fade.png" width="56"> | `Colour fade` | 颜色渐变 | 亮度和颜色一起渐变到夜灯颜色。 |
| <img src="../../images/nightlight/sunrise.png" width="56"> | `Sunrise` | 日出 | 唤醒灯：亮度在时长内逐渐升高，如日出。 |
