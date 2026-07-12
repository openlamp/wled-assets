# WLED Préréglages

[Palettes](palettes.md) · [Effets](effects.md) · [Contrôles](controls.md) · [Veilleuse](nightlight.md) · [Segment](segment.md) · [Boutons](buttons.md) · [Événements bouton](button-events.md) · **Préréglages** · [Curseurs d'effet](fxdata.md) · [Champs Info](info.md) · [Libellés d'UI](ui.md) &nbsp;•&nbsp; [Référence en français](README.md)

<sub>Autres langues: [EN](../en/presets.md) · [DE](../de/presets.md) · [ES](../es/presets.md) · [IT](../it/presets.md) · [JA](../ja/presets.md) · [KO](../ko/presets.md) · [ZH](../zh/presets.md)</sub>

Les **presets** enregistrent tout un rendu (ou une playlist de rendus) à rappeler en un geste — depuis l'onglet **Préréglages**, un bouton physique, un minuteur ou l'API (`ps`/`/presets.json`). Voici les *libellés d'options* de création ; les **noms** des presets, eux, sont les tiens.

| Image | Nom WLED | Traduction | Description |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | Enregistrer le preset | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | Nom du preset | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | Étiquette d'accès rapide | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | Inclure la luminosité | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | Enregistrer les bornes de segment | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | Utiliser l'état actuel | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | Commande API | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | Playlist | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | Durée | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | Transition | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | Répéter | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | Aléatoire | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | Preset de fin | The preset to apply when the playlist finishes. |
