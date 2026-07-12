# WLED Tastenereignisse

[Paletten](palettes.md) · [Effekte](effects.md) · [Regler](controls.md) · [Nachtlicht](nightlight.md) · [Segment](segment.md) · [Tasten](buttons.md) · **Tastenereignisse** · [Presets](presets.md) · [Effektregler](fxdata.md) · [Info-Felder](info.md) · [UI-Texte](ui.md) &nbsp;•&nbsp; [Referenz auf Deutsch](README.md)

<sub>Andere Sprachen: [EN](../en/button-events.md) · [FR](../fr/button-events.md) · [ES](../es/button-events.md) · [IT](../it/button-events.md) · [JA](../ja/button-events.md) · [KO](../ko/button-events.md) · [ZH](../zh/button-events.md)</sub>

**Tastenereignisse** sind *wann* eine Taste auslöst — kurz, lang oder doppelt. WLED ordnet jedem Ereignis ein **Preset/eine Aktion** zu (`btn[].macros`), in **Einstellungen → LED & Hardware**.

| Bild | WLED-Name | Übersetzung | Beschreibung |
|---|---|---|---|
| <img src="../../images/button-events/short-press.png" width="56"> | `Short press` | Kurzer Druck | Kurzes Drücken und Loslassen — löst die Kurz-Aktion der Taste aus (`btn[].macros[0]`). |
| <img src="../../images/button-events/long-press.png" width="56"> | `Long press` | Langer Druck | Taste gehalten — löst die Lang-Aktion aus (`btn[].macros[1]`); ändert standardmäßig die Helligkeit. |
| <img src="../../images/button-events/double-press.png" width="56"> | `Double press` | Doppelter Druck | Zwei schnelle Drücke — löst die Doppel-Aktion aus (`btn[].macros[2]`). |
