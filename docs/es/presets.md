# WLED Presets

[Paletas](palettes.md) · [Efectos](effects.md) · [Controles](controls.md) · [Luz nocturna](nightlight.md) · [Segmento](segment.md) · [Botones](buttons.md) · [Eventos de botón](button-events.md) · **Presets** · [Deslizadores](fxdata.md) · [Campos de info](info.md) · [Etiquetas de IU](ui.md) &nbsp;•&nbsp; [Referencia en español](README.md)

<sub>Otros idiomas: [EN](../en/presets.md) · [FR](../fr/presets.md) · [DE](../de/presets.md) · [IT](../it/presets.md) · [JA](../ja/presets.md) · [KO](../ko/presets.md) · [ZH](../zh/presets.md)</sub>

Los **presets** guardan todo un aspecto (o una lista) para recuperarlo con un toque — desde la pestaña **Ajustes**, un botón, un temporizador o la API (`ps`/`/presets.json`). Estas son las *etiquetas de opciones*; los **nombres** son tuyos.

| Imagen | Nombre WLED | Traducción | Descripción |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | Guardar preset | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | Nombre del preset | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | Etiqueta de acceso rápido | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | Incluir brillo | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | Guardar límites de segmento | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | Usar estado actual | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | Comando API | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | Lista de reproducción | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | Duración | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | Transición | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | Repetir | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | Aleatorio | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | Preset final | The preset to apply when the playlist finishes. |
