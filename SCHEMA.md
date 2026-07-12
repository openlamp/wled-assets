# Data formats

The **join key everywhere is the exact English name** returned by WLED's `/json/pal`
(palettes) and `/json/eff` (effects). Indices are not stable across WLED versions; names
are. Every consumer must fall back to the English key when a value is missing.

## `i18n/palettes.json`, `i18n/effects.json`, `i18n/controls.json`

Each concept is one file: **English key → per-language `{ name, desc }`.**

```json
{
  "_note": "…",
  "entries": {
    "Rivendell": {
      "en": { "name": "Rivendell", "desc": "The Elven valley from Tolkien's Lord of the Rings…" },
      "fr": { "name": "Rivendell", "desc": "Fondcombe, la vallée elfique du Seigneur des Anneaux…" },
      "…": { "…": "…" }
    }
  }
}
```

- Key = English WLED name (from `/json/pal`, `/json/eff`). Languages: `en fr de es it ja ko zh`.
- `name` = the localized display name (equals the English key when there's no translation
  — e.g. proper nouns like Rivendell, Tiamat, C9 stay English on purpose).
- `desc` = a short description: for **palettes**, what the name refers to; for **effects**,
  the motion family (`animations/families.json`); for **controls**, what the parameter does.
- Missing language → fall back to the `en` entry.
- `controls.json` covers the standard effect parameters: `Speed`, `Intensity`,
  `Custom 1-3`, `Option 1-3`, `Effect color`, `Background color`, `Custom color`, `Palette`.

## `i18n/effect-families.json`

```json
{ "families": { "chase": { "fr": "Un point lumineux balaie le ruban…", "en": "…" } } }
```

Nine motion families: `solid strobe sparkle rainbow chase fire rain breathe wave`.

## `meanings/palette-meanings.json`

```json
{ "Rivendell": { "en": "The Elven valley from Tolkien's Lord of the Rings…", "fr": "…" } }
```

One clause per language explaining what the name refers to. Best shown as a subtitle/tooltip.

## `illustrations/<slug>.svg` + `illustrations/index.json`

Each stencil is `viewBox="0 0 144 144"` and carries `data-palette` (English name) and
`data-gradient` (`vertical` | `horizontal`). To render:

1. Fetch the palette's colours from the device: `GET /json/palx?page=N` → `[[pos,r,g,b], …]`
   (or the `c1`/`c2`/`c3`/`r` tokens for dynamic palettes — those have no fixed gradient,
   fall back to a bar).
2. Replace the `<linearGradient id="grad">` stops with `<stop offset="pos/255" stop-color="rgb(r,g,b)"/>`.
3. Keep the gradient direction from `data-gradient` (`x2=0 y2=1` vertical, `x2=1 y2=0` horizontal).

Shapes inherit the gradient from a `<g fill="url(#grad)">`; details drawn in `#1a1a1a`
carve features (clown eyes, traffic-light lamps, orange segments…). **Avoid `rgba()`** —
some embedded SVG renderers drop the alpha channel; pre-mix with the background instead.

`index.json` lists every stencil. Palettes not listed there simply have no illustration.

## `animations/families.json`

```json
{
  "match_order": ["solid","strobe","sparkle","rainbow","chase","fire","rain","breathe","wave"],
  "keywords":    { "chase": ["chase","comet","scan", …], … },
  "algorithm":   { "chase": "a bright dot sweeps with a fading trail", … },
  "effect_family": { "Comet": "chase", "Fire 2012": "fire", … }
}
```

- To classify an effect: use `effect_family[name]` directly, or re-derive by testing
  `keywords` **in `match_order`** (order matters — `rainbow` before `rain`, so "Rainbow"
  doesn't match "rain"; `chase` before `fire`, so "Theater" doesn't hit "heat").
- `tools/anim.js` exports `anim(phase, family)` → inner SVG (advance `phase` ~5–6 fps).

## Backgrounds (transparency)

Everything is **background-agnostic** so a client can composite on any UI colour:

- **Illustration stencils** (`illustrations/*.svg`) and **`tools/anim.js`** output the drawing
  only — **no background rect**. The consumer picks the background (transparent, dark, light…).
- **Thumbnails** `images/palettes/*.png` (alpha) and `images/effects/*.gif` (1-bit alpha) are
  rendered **transparent** — they adapt to light *and* dark (e.g. GitHub's two themes).
- `#1a1a1a` inside a drawing is an intentional **dark detail** (clown eyes, traffic-light
  lamps, ghost eyes…), not the background — it stays opaque on any surface, as intended.
- The **contact sheets** (`images/palettes-contact-sheet.png`, `images/effects-grid.gif`) are
  **transparent** too (labels in mid-grey so they read on light and dark).

## Versioning

Semver. Breaking = renaming/removing a key or changing the SVG contract. Additive
(new translations, new illustrations, new languages) = minor/patch.
