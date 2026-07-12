# WLED 按钮事件

[调色板](palettes.md) · [效果](effects.md) · [控件](controls.md) · [夜灯](nightlight.md) · [段](segment.md) · [按钮](buttons.md) · **按钮事件** · [预设](presets.md) · [滑块](fxdata.md) · [信息字段](info.md) · [界面标签](ui.md) &nbsp;•&nbsp; [中文参考](README.md)

<sub>其他语言: [EN](../en/button-events.md) · [FR](../fr/button-events.md) · [DE](../de/button-events.md) · [ES](../es/button-events.md) · [IT](../it/button-events.md) · [JA](../ja/button-events.md) · [KO](../ko/button-events.md)</sub>

**按钮事件**是物理按钮*何时*触发——短按、长按或双按。WLED 为每个事件映射一个**预设或动作**（`btn[].macros`，设置 → LED 与硬件）。

| 图片 | WLED 名称 | 翻译 | 描述 |
|---|---|---|---|
| <img src="../../images/button-events/short-press.png" width="56"> | `Short press` | 短按 | 快速按下松开——触发按钮短按动作(`btn[].macros[0]`)。 |
| <img src="../../images/button-events/long-press.png" width="56"> | `Long press` | 长按 | 按住不放——长按动作(`btn[].macros[1]`)；默认调节亮度。 |
| <img src="../../images/button-events/double-press.png" width="56"> | `Double press` | 双按 | 快速按两次——双按动作(`btn[].macros[2]`)。 |
