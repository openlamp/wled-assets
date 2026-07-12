# wled-assets

**A shared, client-side asset layer for [WLED](https://github.com/wled/WLED)'s standard
palettes and effects: localized names, evocative palette illustrations, and effect motion
previews — for any WLED client to render.**

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

## What's inside

| Path | What |
|---|---|
| `data/palettes.json`, `data/effects.json` | The reference WLED enum lists (English names, in index order). |
| **`i18n/palettes.json`** | Every palette → per language `{ name, desc }` (8 languages, English fallback). `desc` = what the name refers to. |
| **`i18n/effects.json`** | Every effect → per language `{ name, desc }`. `desc` = its motion family. |
| **`i18n/controls.json`** | A **third concept**: the standard effect controls (Speed, Intensity, Custom 1-3, Options 1-3, colour slots, Palette) → `{ name, desc }` per language. |
| `i18n/effect-families.json` | Descriptions of the 9 effect **motion families**, per language (source for effect `desc`). |
| `meanings/palette-meanings.json` | The palette name meanings (source for palette `desc`). |
| `illustrations/*.svg` | One reusable **gradient-agnostic stencil per palette** (fill `#grad` with the palette's real colours). `index.json` lists them. |
| `animations/families.json` | Maps every effect name → one of 9 motion families + the algorithm for each. |
| `tools/anim.js` | Reference JS implementation of the 9 family animations (`anim(phase, family)`). |
| **`docs/*.md`** | **GitHub-rendered reference pages**, one per **concept × language** (`palettes.fr.md`, `effects.de.md`, `controls.ja.md`…): a table of English name · translation · description · illustration. Start here to browse. |
| `images/palettes/*.png`, `images/effects/*.gif` | Rendered thumbnails: each palette illustration (real gradient) and each effect family as an **animated GIF** — used by the `docs/` pages. |
| `pages/` | Standalone HTML reference pages (all palettes / all effects × 8 languages). |

### Browse the docs

The Markdown pages render directly on GitHub — pick a concept and a language:

- Palettes: [EN](docs/palettes.en.md) · [FR](docs/palettes.fr.md) · [DE](docs/palettes.de.md) · [ES](docs/palettes.es.md) · [IT](docs/palettes.it.md) · [JA](docs/palettes.ja.md) · [KO](docs/palettes.ko.md) · [ZH](docs/palettes.zh.md)
- Effects: [EN](docs/effects.en.md) · [FR](docs/effects.fr.md) · [DE](docs/effects.de.md) · [ES](docs/effects.es.md) · [IT](docs/effects.it.md) · [JA](docs/effects.ja.md) · [KO](docs/effects.ko.md) · [ZH](docs/effects.zh.md)
- Controls: [EN](docs/controls.en.md) · [FR](docs/controls.fr.md) · [DE](docs/controls.de.md) · [ES](docs/controls.es.md) · [IT](docs/controls.it.md) · [JA](docs/controls.ja.md) · [KO](docs/controls.ko.md) · [ZH](docs/controls.zh.md)

## The idea in one picture

```
        WLED device  ──/json/pal, /json/eff──▶  English enum name  ( the JOIN KEY )
                                                        │
              ┌─────────────────────────────────────────┼─────────────────────────────┐
              ▼                        ▼                 ▼                              ▼
        i18n/*.json            meanings/*.json    illustrations/*.svg          animations/families.json
     localized name           what the name       gradient poured into        motion-family preview
        (7 langs)                means             a telling silhouette          of the effect
              └─────────────────────────────────────────┬─────────────────────────────┘
                                                         ▼
                        any WLED client (iOS app, Android app, web UI, overlays…)
                        renders a friendlier, localized, more visual picker
```

## How to consume

1. Read the current palette/effect by index from the device (`/json/state`, `/json/pal`,
   `/json/eff`). The **English name** at that index is your key.
2. Look it up in `i18n/…` for the user's language (fall back to the English key).
3. Optionally show `meanings/…` as a tooltip/subtitle.
4. For palettes, load `illustrations/<slug>.svg` and inject a `<linearGradient id="grad">`
   built from the palette's colours (`/json/palx`); palettes with no stencil get a plain
   gradient bar.
5. For effects, look up its family in `animations/families.json` and animate with
   `tools/anim.js` (or your own port).

Vendor it as a git submodule, a package, or a plain copy. It's just data + SVG + one small
JS file.

## Status & contributing

**Alpha.** Coverage today: palettes translated 55/72, effects 131/220, illustrations 54,
palette meanings 68. The **Latin-script translations (fr/de/es/it) are solid; the CJK
ones (ja/ko/zh) are a first pass and want a native-speaker review** before production use.
Corrections, missing translations, new illustrations and new-language columns are all
welcome via PR — the English name is always the stable key.

## License

**Data, translations and meanings: [CC0-1.0](LICENSE)** (public domain — reuse freely,
no attribution required, so any client can adopt it without friction). The SVG stencils
are contributed under the same terms.

---

Maintained as part of **[OpenLamp](https://github.com/openlamp)** — 100% local stage-light
control for musicians and makers — but designed to be **vendor-neutral**: nothing here is
LumiDeck- or OpenLamp-specific. If it helps a WLED client, it's doing its job.
