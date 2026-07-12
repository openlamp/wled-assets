# Draft — WLED Discourse announcement (Projects / Development category)

**Where:** https://wled.discourse.group/ — "Projects" or "Development".
**Status:** DRAFT — not posted. Post yourself, ideally once the WLED author is aware
(the courtesy email is out). Lead with CC0 / no-strings.

---

**Subject:** A CC0 localization + icon layer any WLED client can use (names in 8 languages, palette/effect visuals)

Hi all,

Building a WLED Stream Deck plugin, I kept hitting the same gap: effect and palette names
are English identifiers, and there's no localization or artwork — for good reason, the
firmware can't carry that without bloating the binary on every ESP.

So I assembled a **firmware-independent, client-side** layer and put it out as CC0:
**https://github.com/openlamp/wled-assets**

- **Localized names** (`en fr de es it ja ko zh`, English fallback) for the standard
  **palettes** and **effects** — plus controls, nightlight modes, segment actions, button
  events, presets, info & UI labels.
- **Illustrations**: each palette drawn as a telling icon filled with its *own* gradient
  (Rivendell → mountains, Fire → a flame…), and a distinct animated motion preview per
  effect (Rainbow → an arc, Sweep → a broom, Tartan → a plaid, Julia → the fractal…).

**How a client uses it** (no firmware change, no binary bloat):
read `/json/eff` and `/json/pal` once → the exact English name is the join key → look it up
for the user's language, fall back to English → show the localized name + a palette
thumbnail (colours from `/json/palx`) or an effect preview. Fetch it from a CDN so updates
land without an app release.

I made a **runnable proof-of-concept**: a drop-in overlay for the WLED web UI that rewrites
the effect/palette dropdowns with localized names and adds palette thumbnails, live against
a real device. It's in the repo (`pages/webui-localize-poc.html`).

It's **CC0 and vendor-neutral** — nothing in it is specific to my project. If it's useful to
the web UI, the native apps, or your own tool: adopt it, fork it, ignore it, or tell me how
to shape it. Corrections, missing translations and new-language columns are all welcome via
PR — the English name is always the stable key.

Not affiliated with or endorsed by the WLED project — this just interoperates with the public
enumerations.

Cheers,
Benoît (@Beennnn)
