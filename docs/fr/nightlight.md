# WLED Veilleuse

[Palettes](palettes.md) · [Effets](effects.md) · [Contrôles](controls.md) · **Veilleuse** · [Segment](segment.md) · [Boutons](buttons.md) · [Événements bouton](button-events.md) · [Préréglages](presets.md) · [Curseurs d'effet](fxdata.md) · [Champs Info](info.md) · [Libellés d'UI](ui.md) &nbsp;•&nbsp; [Référence en français](README.md)

<sub>Autres langues: [EN](../en/nightlight.md) · [DE](../de/nightlight.md) · [ES](../es/nightlight.md) · [IT](../it/nightlight.md) · [JA](../ja/nightlight.md) · [KO](../ko/nightlight.md) · [ZH](../zh/nightlight.md)</sub>

La **veilleuse** est l'extinction temporisée de WLED (icône lune de la barre du haut). Les quatre modes règlent *comment* elle s'éteint ; ils correspondent à `nl.mode`.

| Image | Nom WLED | Traduction | Description |
|---|---|---|---|
| <img src="../../images/nightlight/instant.png" width="56"> | `Instant` | Instantané | La lumière s'éteint d'un coup à la fin du minuteur — sans fondu. |
| <img src="../../images/nightlight/fade.png" width="56"> | `Fade` | Fondu | La luminosité descend progressivement sur toute la durée. |
| <img src="../../images/nightlight/colour-fade.png" width="56"> | `Colour fade` | Fondu couleur | Fond la luminosité ET la couleur vers la couleur de veilleuse. |
| <img src="../../images/nightlight/sunrise.png" width="56"> | `Sunrise` | Lever de soleil | Réveil lumineux : la luminosité MONTE sur la durée, comme une aube. |
