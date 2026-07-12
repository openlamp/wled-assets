# WLED Presets

[Paletten](palettes.md) · [Effekte](effects.md) · [Regler](controls.md) · [Nachtlicht](nightlight.md) · [Segment](segment.md) · [Tasten](buttons.md) · [Tastenereignisse](button-events.md) · **Presets** · [Effektregler](fxdata.md) · [Info-Felder](info.md) · [UI-Texte](ui.md) &nbsp;•&nbsp; [Referenz auf Deutsch](README.md)

<sub>Andere Sprachen: [EN](../en/presets.md) · [FR](../fr/presets.md) · [ES](../es/presets.md) · [IT](../it/presets.md) · [JA](../ja/presets.md) · [KO](../ko/presets.md) · [ZH](../zh/presets.md)</sub>

**Presets** speichern ein ganzes Bild (oder eine Playlist) zum Abruf mit einem Tipp — aus dem Reiter **Presets**, per Taste, Timer oder API (`ps`/`/presets.json`). Dies sind die *Options-Bezeichnungen*; die **Namen** gehören dir.

| Bild | WLED-Name | Übersetzung | Beschreibung |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | Preset speichern | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | Preset-Name | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | Schnellzugriff-Kürzel | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | Helligkeit einbeziehen | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | Segmentgrenzen speichern | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | Aktuellen Zustand verwenden | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | API-Befehl | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | Wiedergabeliste | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | Dauer | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | Übergang | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | Wiederholen | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | Zufall | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | End-Preset | The preset to apply when the playlist finishes. |
