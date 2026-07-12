# WLED プリセット

[パレット](palettes.md) · [エフェクト](effects.md) · [コントロール](controls.md) · [ナイトライト](nightlight.md) · [セグメント](segment.md) · [ボタン](buttons.md) · [ボタンイベント](button-events.md) · **プリセット** · [スライダー](fxdata.md) · [情報項目](info.md) · [UIラベル](ui.md) &nbsp;•&nbsp; [日本語リファレンス](README.md)

<sub>他の言語: [EN](../en/presets.md) · [FR](../fr/presets.md) · [DE](../de/presets.md) · [ES](../es/presets.md) · [IT](../it/presets.md) · [KO](../ko/presets.md) · [ZH](../zh/presets.md)</sub>

**プリセット**は見た目(やプレイリスト)を丸ごと保存して一発呼出——**プリセット**タブ・物理ボタン・タイマー・API(`ps`/`/presets.json`)から。ここは作成時の*オプション名*で、プリセット**名**はあなたのもの。

| 画像 | WLED名 | 翻訳 | 説明 |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | プリセット保存 | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | プリセット名 | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | クイックロードラベル | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | 明るさを含める | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | セグメント範囲を保存 | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | 現在の状態を使用 | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | APIコマンド | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | プレイリスト | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | 再生時間 | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | トランジション | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | 繰り返し | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | シャッフル | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | 終了プリセット | The preset to apply when the playlist finishes. |
