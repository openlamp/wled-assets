# WLED Luz nocturna

[Paletas](palettes.md) · [Efectos](effects.md) · [Controles](controls.md) · **Luz nocturna** · [Segmento](segment.md) · [Botones](buttons.md) · [Deslizadores](fxdata.md) · [Campos de info](info.md) · [Etiquetas de IU](ui.md) &nbsp;•&nbsp; [Referencia en español](README.md)

<sub>Otros idiomas: [EN](../en/nightlight.md) · [FR](../fr/nightlight.md) · [DE](../de/nightlight.md) · [IT](../it/nightlight.md) · [JA](../ja/nightlight.md) · [KO](../ko/nightlight.md) · [ZH](../zh/nightlight.md)</sub>

La **luz nocturna** es el apagado temporizado de WLED (icono de luna arriba). Los cuatro modos definen *cómo* se atenúa (`nl.mode`).

| Imagen | Nombre WLED | Traducción | Descripción |
|---|---|---|---|
| <img src="../../images/nightlight/instant.png" width="56"> | `Instant` | Instantáneo | La luz se apaga de golpe al terminar el temporizador — sin fundido. |
| <img src="../../images/nightlight/fade.png" width="56"> | `Fade` | Fundido | El brillo baja gradualmente durante toda la duración. |
| <img src="../../images/nightlight/colour-fade.png" width="56"> | `Colour fade` | Fundido de color | Funde brillo Y color hacia el color de luz nocturna. |
| <img src="../../images/nightlight/sunrise.png" width="56"> | `Sunrise` | Amanecer | Luz de despertar: el brillo SUBE durante la duración, como un amanecer. |
