# WLED Nightlight

[Palettes](palettes.md) · [Effects](effects.md) · [Controls](controls.md) · **Nightlight** · [Segment](segment.md) · [Buttons](buttons.md) · [Button events](button-events.md) · [Presets](presets.md) · [Effect sliders](fxdata.md) · [Info fields](info.md) · [UI labels](ui.md) &nbsp;•&nbsp; [Reference in English](README.md)

<sub>Other languages: [FR](../fr/nightlight.md) · [DE](../de/nightlight.md) · [ES](../es/nightlight.md) · [IT](../it/nightlight.md) · [JA](../ja/nightlight.md) · [KO](../ko/nightlight.md) · [ZH](../zh/nightlight.md)</sub>

**Nightlight** is WLED's timed fade-off (the moon icon in the top bar). The four modes set *how* it fades; they map to `nl.mode`.

| Image | WLED name | Translation | Description |
|---|---|---|---|
| <img src="../../images/nightlight/instant.png" width="56"> | `Instant` | Instant | The light switches off at once when the timer ends — no fade. |
| <img src="../../images/nightlight/fade.png" width="56"> | `Fade` | Fade | Brightness fades down gradually over the whole duration. |
| <img src="../../images/nightlight/colour-fade.png" width="56"> | `Colour fade` | Colour fade | Fades brightness AND colour toward the nightlight colour. |
| <img src="../../images/nightlight/sunrise.png" width="56"> | `Sunrise` | Sunrise | Wake-up light: brightness fades UP over the duration, like a sunrise. |
