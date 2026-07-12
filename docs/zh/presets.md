# WLED 预设

[调色板](palettes.md) · [效果](effects.md) · [控件](controls.md) · [夜灯](nightlight.md) · [段](segment.md) · [按钮](buttons.md) · [按钮事件](button-events.md) · **预设** · [滑块](fxdata.md) · [信息字段](info.md) · [界面标签](ui.md) &nbsp;•&nbsp; [中文参考](README.md)

<sub>其他语言: [EN](../en/presets.md) · [FR](../fr/presets.md) · [DE](../de/presets.md) · [ES](../es/presets.md) · [IT](../it/presets.md) · [JA](../ja/presets.md) · [KO](../ko/presets.md)</sub>

**预设**保存整个效果（或播放列表），一键调用——来自**预设**标签、物理按钮、定时器或 API（`ps`/`/presets.json`）。这里是创建时的*选项标签*；预设**名称**是你自己的。

| 图片 | WLED 名称 | 翻译 | 描述 |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | 保存预设 | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | 预设名称 | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | 快速加载标签 | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | 包含亮度 | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | 保存段边界 | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | 使用当前状态 | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | API 命令 | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | 播放列表 | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | 时长 | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | 过渡 | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | 重复 | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | 随机 | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | 结束预设 | The preset to apply when the playlist finishes. |
