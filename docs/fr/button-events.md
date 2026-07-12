# WLED Événements bouton

[Palettes](palettes.md) · [Effets](effects.md) · [Contrôles](controls.md) · [Veilleuse](nightlight.md) · [Segment](segment.md) · [Boutons](buttons.md) · **Événements bouton** · [Préréglages](presets.md) · [Curseurs d'effet](fxdata.md) · [Champs Info](info.md) · [Libellés d'UI](ui.md) &nbsp;•&nbsp; [Référence en français](README.md)

<sub>Autres langues: [EN](../en/button-events.md) · [DE](../de/button-events.md) · [ES](../es/button-events.md) · [IT](../it/button-events.md) · [JA](../ja/button-events.md) · [KO](../ko/button-events.md) · [ZH](../zh/button-events.md)</sub>

Les **événements de bouton** sont *quand* un bouton physique déclenche — appui court, long ou double. WLED associe chaque événement à un **preset ou une action** (`btn[].macros`), réglé dans **Réglages → LED & matériel**.

| Image | Nom WLED | Traduction | Description |
|---|---|---|---|
| <img src="../../images/button-events/short-press.png" width="56"> | `Short press` | Appui court | Un appui bref relâché aussitôt. Déclenche l'action d'appui court du bouton (`btn[].macros[0]`). |
| <img src="../../images/button-events/long-press.png" width="56"> | `Long press` | Appui long | Bouton maintenu. Déclenche l'action d'appui long (`btn[].macros[1]`) ; par défaut règle la luminosité. |
| <img src="../../images/button-events/double-press.png" width="56"> | `Double press` | Double appui | Deux appuis rapprochés. Déclenche l'action de double appui (`btn[].macros[2]`). |
