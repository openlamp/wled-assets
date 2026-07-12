# WLED Luce notturna

[Tavolozze](palettes.md) · [Effetti](effects.md) · [Controlli](controls.md) · **Luce notturna** · [Segmento](segment.md) · [Pulsanti](buttons.md) · [Cursori effetto](fxdata.md) · [Campi info](info.md) · [Etichette UI](ui.md) &nbsp;•&nbsp; [Riferimento in italiano](README.md)

<sub>Altre lingue: [EN](../en/nightlight.md) · [FR](../fr/nightlight.md) · [DE](../de/nightlight.md) · [ES](../es/nightlight.md) · [JA](../ja/nightlight.md) · [KO](../ko/nightlight.md) · [ZH](../zh/nightlight.md)</sub>

La **luce notturna** è lo spegnimento temporizzato di WLED (icona luna in alto). I quattro modi definiscono *come* si spegne (`nl.mode`).

| Immagine | Nome WLED | Traduzione | Descrizione |
|---|---|---|---|
| <img src="../../images/nightlight/instant.png" width="56"> | `Instant` | Istantaneo | La luce si spegne di colpo alla fine del timer — senza dissolvenza. |
| <img src="../../images/nightlight/fade.png" width="56"> | `Fade` | Dissolvenza | La luminosità cala gradualmente per tutta la durata. |
| <img src="../../images/nightlight/colour-fade.png" width="56"> | `Colour fade` | Dissolvenza colore | Sfuma luminosità E colore verso il colore notturno. |
| <img src="../../images/nightlight/sunrise.png" width="56"> | `Sunrise` | Alba | Luce sveglia: la luminosità SALE per la durata, come un'alba. |
