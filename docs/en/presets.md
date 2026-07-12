# WLED Presets

[Palettes](palettes.md) · [Effects](effects.md) · [Controls](controls.md) · [Nightlight](nightlight.md) · [Segment](segment.md) · [Buttons](buttons.md) · [Button events](button-events.md) · **Presets** · [Effect sliders](fxdata.md) · [Info fields](info.md) · [UI labels](ui.md) &nbsp;•&nbsp; [Reference in English](README.md)

<sub>Other languages: [FR](../fr/presets.md) · [DE](../de/presets.md) · [ES](../es/presets.md) · [IT](../it/presets.md) · [JA](../ja/presets.md) · [KO](../ko/presets.md) · [ZH](../zh/presets.md)</sub>

**Presets** save a whole look (or a playlist of looks) to recall in one tap — from the **Presets** tab, a physical button, a timer or the API (`ps`/`/presets.json`). These are the *option labels* used when creating a preset; the preset **names** themselves are your own.

| Image | WLED name | Translation | Description |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | Save preset | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | Preset name | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | Quick load label | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | Include brightness | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | Save segment bounds | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | Use current state | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | API command | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | Playlist | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | Duration | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | Transition | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | Repeat | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | Shuffle | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | End preset | The preset to apply when the playlist finishes. |
