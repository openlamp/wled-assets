# WLED Eventi pulsante

[Tavolozze](palettes.md) · [Effetti](effects.md) · [Controlli](controls.md) · [Luce notturna](nightlight.md) · [Segmento](segment.md) · [Pulsanti](buttons.md) · **Eventi pulsante** · [Preset](presets.md) · [Cursori effetto](fxdata.md) · [Campi info](info.md) · [Etichette UI](ui.md) &nbsp;•&nbsp; [Riferimento in italiano](README.md)

<sub>Altre lingue: [EN](../en/button-events.md) · [FR](../fr/button-events.md) · [DE](../de/button-events.md) · [ES](../es/button-events.md) · [JA](../ja/button-events.md) · [KO](../ko/button-events.md) · [ZH](../zh/button-events.md)</sub>

Gli **eventi di pulsante** sono *quando* un pulsante fisico attiva — pressione breve, lunga o doppia. WLED associa a ogni evento un **preset o azione** (`btn[].macros`), in **Impostazioni → LED e hardware**.

| Immagine | Nome WLED | Traduzione | Descrizione |
|---|---|---|---|
| <img src="../../images/button-events/short-press.png" width="56"> | `Short press` | Pressione breve | Premi e rilascia rapido — attiva l'azione di pressione breve (`btn[].macros[0]`). |
| <img src="../../images/button-events/long-press.png" width="56"> | `Long press` | Pressione lunga | Pulsante tenuto — azione di pressione lunga (`btn[].macros[1]`); di default regola la luminosità. |
| <img src="../../images/button-events/double-press.png" width="56"> | `Double press` | Doppia pressione | Due pressioni rapide — azione di doppia pressione (`btn[].macros[2]`). |
