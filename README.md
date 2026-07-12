# wled-assets

**A shared, client-side asset layer for [WLED](https://github.com/wled/WLED)'s standard
palettes and effects: localized names, evocative palette illustrations, and effect motion
previews — for any WLED client to render.**

<table>
<tr>
<td width="50%" align="center" valign="top">
<img src="images/palettes/rivendell.png" width="132" alt="Rivendell palette illustration"><br>
<b>Palette · Rivendell</b><br>
<sub>The Elven valley from Tolkien's <i>Lord of the Rings</i> — misty mountains and forests. The palette's own gradient is poured into the silhouette.</sub>
</td>
<td width="50%" align="center" valign="top">
<img src="images/effects/aurora.gif" width="132" alt="Aurora effect animation"><br>
<b>Effect · Aurora</b><br>
<sub>The full spectrum cycles through (the <i>rainbow</i> motion family). Every effect gets its <b>own</b> animation — hue, speed and density seeded by the effect.</sub>
</td>
</tr>
</table>

That's the idea in two tiles: a palette becomes a **telling illustration in its real colours**,
an effect becomes a **living preview of how it moves** — each with a **localized name and a
one-line description**. Below: all 72 palettes and all 220 effects at a glance.

<p align="center">
<img src="images/palettes-contact-sheet.png" width="880" alt="All 72 WLED palettes as illustrations"><br>
<sub><i>The 72 standard WLED palettes, each as its gradient-filled illustration.</i></sub>
</p>

<p align="center">
<img src="images/effects-grid.gif" width="640" alt="All 220 WLED effects animated"><br>
<sub><i>The 220 standard WLED effects, each animated and visually distinct.</i></sub>
</p>

## Why

WLED's effect and palette names are English identifiers, compiled into the firmware and
referenced by index (`fx:63`, `pal:11`). There is no official localization, and the
firmware can't carry translations or artwork without inflating the binary that ships to
every ESP. **This repo is the firmware-independent, client-side complement**: a single
source of truth that phone apps, web UIs, overlays and third-party tools can all consume
to show localized names, telling palette icons, and a preview of what each effect *does*.

> Not affiliated with the WLED project. WLED is an independent open-source project; this
> repo merely *interoperates* with its public enumerations. The join key is the exact
> English name returned by `/json/pal` and `/json/eff`. Everything falls back to that
> English name when a translation or asset is missing — so a consumer is never worse off
> than plain WLED.

## Browse the docs (GitHub-rendered)

One page per **concept × language** — English name · translation · description · illustration:

| Language | Palettes | Effects | Controls |
|---|---|---|---|
| 🇬🇧 English | [palettes](docs/palettes.en.md) | [effects](docs/effects.en.md) | [controls](docs/controls.en.md) |
| 🇫🇷 Français | [palettes](docs/palettes.fr.md) | [effects](docs/effects.fr.md) | [controls](docs/controls.fr.md) |
| 🇩🇪 Deutsch | [palettes](docs/palettes.de.md) | [effects](docs/effects.de.md) | [controls](docs/controls.de.md) |
| 🇪🇸 Español | [palettes](docs/palettes.es.md) | [effects](docs/effects.es.md) | [controls](docs/controls.es.md) |
| 🇮🇹 Italiano | [palettes](docs/palettes.it.md) | [effects](docs/effects.it.md) | [controls](docs/controls.it.md) |
| 🇯🇵 日本語 | [palettes](docs/palettes.ja.md) | [effects](docs/effects.ja.md) | [controls](docs/controls.ja.md) |
| 🇰🇷 한국어 | [palettes](docs/palettes.ko.md) | [effects](docs/effects.ko.md) | [controls](docs/controls.ko.md) |
| 🇨🇳 中文 | [palettes](docs/palettes.zh.md) | [effects](docs/effects.zh.md) | [controls](docs/controls.zh.md) |

## What's inside

| Path | What |
|---|---|
| `data/palettes.json`, `data/effects.json` | The reference WLED enum lists (English names, in index order). |
| `i18n/palettes.json` | Every palette → per language `{ name, desc }` (8 languages, English fallback). |
| `i18n/effects.json` | Every effect → per language `{ name, desc }` (`desc` = its motion family). |
| `i18n/controls.json` | The standard effect **controls** (Speed, Intensity, Custom 1-3, Options 1-3, colour slots, Palette) → `{ name, desc }`. |
| `i18n/effect-families.json` | Descriptions of the 9 effect motion families, per language. |
| `meanings/palette-meanings.json` | Source for palette descriptions. |
| `illustrations/*.svg` | One reusable **gradient-agnostic stencil per palette** (fill `#grad` with the palette's real colours). |
| `animations/families.json` | Maps every effect name → one of 9 motion families + the per-effect seeding rule. |
| `tools/anim.js` | Reference JS: `anim(phase, family, seed)` → the effect animation (seed = effect index → unique). |
| `docs/*.md` | The GitHub-rendered reference pages above. |
| `images/palettes/*.png`, `images/effects/*.gif` | Rendered thumbnails used by the docs (72 palette PNGs, 216 effect GIFs, 2 contact sheets). |
| `pages/` | Standalone interactive HTML reference pages. |

## How to consume

1. Read the current palette/effect index from the device (`/json/state`, `/json/pal`,
   `/json/eff`). The **English name** at that index is your key.
2. Look it up in `i18n/…` for the user's language (fall back to `en`). Show `name` + `desc`.
3. For palettes, load `illustrations/<slug>.svg` and inject a `<linearGradient id="grad">`
   built from the palette's colours (`/json/palx`).
4. For effects, look up its family in `animations/families.json` and animate with
   `anim(phase, family, effectIndex)` from `tools/anim.js`.

Vendor it as a git submodule, a package, or a plain copy. It's data + SVG + one small JS file.

## Beyond palettes & effects

Also internationalized here: **controls** (the effect parameters). Further WLED enums that
*could* join this layer next — small, still English-only in the firmware:

- **Nightlight modes** (instant, fade, colour-fade, sunrise)
- **Segment actions** (reverse, mirror, freeze, mapping)
- **Playlist / preset** UX labels · **info/status** field labels

Open an issue if one of these would help your client.

## Status & contributing

**Alpha.** Palettes translated 55/72, effects 131/220, illustrations 72/72, palette
meanings 68. The **Latin-script translations (fr/de/es/it) are solid; the CJK ones
(ja/ko/zh) are a first pass** and want a native-speaker review before production use.
Corrections, missing translations, new illustrations and new-language columns are all
welcome via PR — the English name is always the stable key.

## License

**Data, translations, meanings and SVG stencils: [CC0-1.0](LICENSE)** (public domain — reuse
freely, no attribution required, so any client can adopt it without friction).

---

Maintained as part of **[OpenLamp](https://github.com/openlamp)** — 100% local stage-light
control for musicians and makers — but **vendor-neutral**: nothing here is LumiDeck- or
OpenLamp-specific. If it helps a WLED client, it's doing its job.
