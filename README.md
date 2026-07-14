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

## For client developers

If you build a WLED client — the **web UI**, a **phone app**, a **browser overlay**, a
Stream Deck / MIDI tool — this repo drops localized names and telling visuals into your UI
for free, at runtime, **without touching the firmware or its binary size**:

1. Read the device's list once: `GET /json/eff`, `GET /json/pal`. The **exact English name**
   at each index is your join key (indices are not stable across WLED versions — names are).
2. Look the name up in `i18n/effects.json` / `i18n/palettes.json` for the user's language
   (`en fr de es it ja ko zh`), fall back to `en`. Show `name` (+ optional `desc`).
3. For a palette thumbnail, take `illustrations/<slug>.svg` and inject the palette's real
   colours from `GET /json/palx`. For an effect preview, use `animations/families.json` +
   `tools/anim.js`.

Everything is **CC0** — vendor it as a submodule, a package, or a plain copy, no attribution
required. Fetch it from a CDN so updates land without an app release. Because it's keyed on
the English name with English fallback, a missing entry is never worse than plain WLED. A
runnable proof-of-concept (a drop-in overlay for the WLED web UI) lives in
[`pages/webui-localize-poc.html`](pages/webui-localize-poc.html).

## Browse the docs (GitHub-rendered)

One page per **language × concept** — English name · translation · description · illustration.
**11 concepts**, each with an icon and an intro: palettes · effects · controls · nightlight · segment · buttons · button-events · presets · effect-sliders · info · UI. Full index (all concepts × languages): **[docs/](docs/)**. Main ones:

| Language | Palettes | Effects | Controls | Nightlight |
|---|---|---|---|---|
| 🇬🇧 English | [palettes](docs/en/palettes.md) | [effects](docs/en/effects.md) | [controls](docs/en/controls.md) | [nightlight](docs/en/nightlight.md) |
| 🇫🇷 Français | [palettes](docs/fr/palettes.md) | [effects](docs/fr/effects.md) | [controls](docs/fr/controls.md) | [nightlight](docs/fr/nightlight.md) |
| 🇩🇪 Deutsch | [palettes](docs/de/palettes.md) | [effects](docs/de/effects.md) | [controls](docs/de/controls.md) | [nightlight](docs/de/nightlight.md) |
| 🇪🇸 Español | [palettes](docs/es/palettes.md) | [effects](docs/es/effects.md) | [controls](docs/es/controls.md) | [nightlight](docs/es/nightlight.md) |
| 🇮🇹 Italiano | [palettes](docs/it/palettes.md) | [effects](docs/it/effects.md) | [controls](docs/it/controls.md) | [nightlight](docs/it/nightlight.md) |
| 🇯🇵 日本語 | [palettes](docs/ja/palettes.md) | [effects](docs/ja/effects.md) | [controls](docs/ja/controls.md) | [nightlight](docs/ja/nightlight.md) |
| 🇰🇷 한국어 | [palettes](docs/ko/palettes.md) | [effects](docs/ko/effects.md) | [controls](docs/ko/controls.md) | [nightlight](docs/ko/nightlight.md) |
| 🇨🇳 中文 | [palettes](docs/zh/palettes.md) | [effects](docs/zh/effects.md) | [controls](docs/zh/controls.md) | [nightlight](docs/zh/nightlight.md) |

## What's inside

| Path | What |
|---|---|
| `data/palettes.json`, `data/effects.json` | The reference WLED enum lists (English names, in index order). |
| `i18n/palettes.json` | Every palette → per language `{ name, desc }` (8 languages, English fallback). |
| `i18n/effects.json` | Every effect → per language `{ name, desc }` (`desc` = its motion family). |
| `i18n/controls.json` | The standard effect **controls** (Speed, Intensity, Custom 1-3, Options 1-3, colour slots, Palette) → `{ name, desc }`. |
| `i18n/concept-intros.json` | A short per-language intro for each concept — *where it lives in WLED* — shown at the top of every doc page. |
| `i18n/nightlight.json`, `i18n/segment.json`, `i18n/buttons.json`, `i18n/button-events.json`, `i18n/presets.json` | Nightlight modes, segment actions, button/input types, button events (short/long/double press → preset), and preset/playlist option labels → `{ name, desc }` per language. |
| `i18n/fxdata-labels.json` | The **234 per-effect slider labels** from `/json/fxdata` (Speed, Blur, # of balls…) → `{ name }` per language (common ones translated, long tail = English fallback). |
| `i18n/info.json`, `i18n/ui.json` | Info-panel field labels and core UI labels (tabs, actions) → `{ name, desc }` per language. |
| `i18n/nightlight.json` | The **4 nightlight modes** (instant, fade, colour fade, sunrise) → mode number + `{ name, desc }` per language. |
| `i18n/effect-families.json` | Descriptions of the 9 broad motion families, per language. |
| `meanings/palette-meanings.json` | Source for palette descriptions. |
| `illustrations/*.svg` | One reusable **gradient-agnostic stencil per palette** (fill `#grad` with the palette's real colours). |
| `animations/families.json` | Maps every effect name → one of **24 motion types** + the per-effect seeding rule. |
| `tools/anim.js` | Reference JS: `anim(phase, motion, seed)` → the effect animation (24 motions; seed = effect index → unique). |
| `docs/<lang>/*.md` | The GitHub-rendered reference pages above. |
| `images/nightlight/*.png`, `images/segment/*.png`, `images/fxdata/*.png` | Icons for nightlight modes (brightness curves), segment actions (reverse/mirror/freeze…), and effect-slider labels (keyword icons + a generic slider). |
| `images/controls/*.png` | Icons for the effect controls (speedometer, sliders, toggles, colour swatches, painter palette). |
| `images/palettes/*.png`, `images/effects/*.gif` | Rendered thumbnails, **transparent background** (adapt to light/dark) — 72 palette PNGs, 216 animated effect GIFs. The 2 contact sheets are transparent too. |
| `pages/` | Standalone interactive HTML reference pages. |

## How to consume

1. Read the current palette/effect index from the device (`/json/state`, `/json/pal`,
   `/json/eff`). The **English name** at that index is your key.
2. Look it up in `i18n/…` for the user's language (fall back to `en`). Show `name` + `desc`.
3. For palettes, load `illustrations/<slug>.svg` and inject a `<linearGradient id="grad">`
   built from the palette's colours (`/json/palx`).
4. For effects, look up its motion in `animations/families.json` and animate with
   `anim(phase, motion, effectIndex)` from `tools/anim.js`.

Vendor it as a git submodule, a package, or a plain copy. It's data + SVG + one small JS file.

## Every identified WLED string is translated here

This repo's goal is to localize **everything WLED exposes as named vocabulary** — not a
curated subset. Concepts covered (each × 8 languages, English fallback):

- **Palettes** (72) · **Effects** (220) · **Effect controls** (Speed, Intensity, Custom 1-3, Options, colour slots, Palette)
- **Segment actions** (reverse, mirror, freeze, on/off, transition, sound-sim)
- **Button/input types** (push, switch, PIR, touch, analog…)
- **Per-effect slider labels** — the **234** parameter names from `/json/fxdata`
- **Info-panel fields** (uptime, free memory, signal, FPS, estimated current…)
- **Core UI labels** (Colours, Effects, Segments, Presets, Settings, Save, Sync, Live…)

Coverage grows over time: the small enums are fully translated; the large sets (the 234
fxdata labels, the UI strings) have the common items translated and the specific long tail
(plus the CJK columns) fall back to English — **extend any of them via PR**, that's the point.

**Kept in English on purpose** (they are identifiers/product names, not words — like
proper-noun palettes such as Rivendell): LED-chip types (`WS2812B`, `SK6812`…) and colour
orders (`GRB`, `RGB`…). If a client wants those localized too, open an issue and we'll add them.

## Updating an illustration or animation

**The palette illustrations and effect animations were bootstrapped from the English
names** (best-effort interpretation — Ghost Rider → a ghost, Lissajous → the curve, etc.).
Some are approximations, and **any of them can be corrected or replaced on request.** Open an
issue / PR providing **either**:

- an **SVG** following the contract (viewBox `0 0 144 144`, no background rect; palette stencils
  fill `#grad`, effect motions are drawn by `tools/anim.js`), **or**
- a ready **image** — a static **PNG** or an **animated GIF** — with: **transparent background**,
  **square** aspect, **≥ 144×144 px**, and a **one-line description** of what it should show
  (which palette/effect it's for, static vs animated, and the intended motion).

Tell us the exact WLED name (the join key) it maps to. We'll wire it into the asset set.

## Status & contributing

**Alpha.** Palettes translated 72/72, effects 217/217, illustrations 72/72. The
**Latin-script translations (fr/de/es/it) are solid; the CJK ones (ja/ko/zh) are a first
pass** and want a native-speaker review before production use.
Corrections, missing translations, new illustrations and new-language columns are all
welcome via PR — the English name is always the stable key.

## License

**Data, translations, meanings and SVG stencils: [CC0-1.0](LICENSE)** (public domain — reuse
freely, no attribution required, so any client can adopt it without friction).

---

Maintained as part of **[OpenLamp](https://github.com/openlamp)** — 100% local stage-light
control for musicians and makers — but **vendor-neutral**: nothing here is
OpenLamp-specific. If it helps a WLED client, it's doing its job.
