# WLED Button events

[Palettes](palettes.md) · [Effects](effects.md) · [Controls](controls.md) · [Nightlight](nightlight.md) · [Segment](segment.md) · [Buttons](buttons.md) · **Button events** · [Presets](presets.md) · [Effect sliders](fxdata.md) · [Info fields](info.md) · [UI labels](ui.md) &nbsp;•&nbsp; [Reference in English](README.md)

<sub>Other languages: [FR](../fr/button-events.md) · [DE](../de/button-events.md) · [ES](../es/button-events.md) · [IT](../it/button-events.md) · [JA](../ja/button-events.md) · [KO](../ko/button-events.md) · [ZH](../zh/button-events.md)</sub>

**Button events** are *when* a physical button fires — a short press, a long press or a double press. WLED maps each event to a **preset or action** (`btn[].macros`), set in **Settings → LED & Hardware**.

| Image | WLED name | Translation | Description |
|---|---|---|---|
| <img src="../../images/button-events/short-press.png" width="56"> | `Short press` | Short press | A quick press-and-release. In WLED it fires the button's short-press action (`btn[].macros[0]`). |
| <img src="../../images/button-events/long-press.png" width="56"> | `Long press` | Long press | Holding the button. Fires the long-press action (`btn[].macros[1]`); by default it changes brightness. |
| <img src="../../images/button-events/double-press.png" width="56"> | `Double press` | Double press | Two quick presses. Fires the double-press action (`btn[].macros[2]`). |
