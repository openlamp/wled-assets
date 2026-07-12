# WLED Preset

[Tavolozze](palettes.md) · [Effetti](effects.md) · [Controlli](controls.md) · [Luce notturna](nightlight.md) · [Segmento](segment.md) · [Pulsanti](buttons.md) · [Eventi pulsante](button-events.md) · **Preset** · [Cursori effetto](fxdata.md) · [Campi info](info.md) · [Etichette UI](ui.md) &nbsp;•&nbsp; [Riferimento in italiano](README.md)

<sub>Altre lingue: [EN](../en/presets.md) · [FR](../fr/presets.md) · [DE](../de/presets.md) · [ES](../es/presets.md) · [JA](../ja/presets.md) · [KO](../ko/presets.md) · [ZH](../zh/presets.md)</sub>

I **preset** salvano un intero aspetto (o una playlist) da richiamare con un tocco — dalla scheda **Preset**, un pulsante, un timer o l'API (`ps`/`/presets.json`). Queste sono le *etichette delle opzioni*; i **nomi** sono i tuoi.

| Immagine | Nome WLED | Traduzione | Descrizione |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | Salva preset | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | Nome del preset | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | Etichetta accesso rapido | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | Includi luminosità | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | Salva confini segmento | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | Usa stato attuale | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | Comando API | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | Playlist | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | Durata | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | Transizione | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | Ripeti | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | Casuale | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | Preset finale | The preset to apply when the playlist finishes. |
