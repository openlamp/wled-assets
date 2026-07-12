# Outreach draft — official iOS app (Moustachauve/WLED-Native-iOS)

**Where:** a GitHub Discussion (or Issue) on https://github.com/Moustachauve/WLED-Native-iOS
**Status:** DRAFT — not posted. Review before sending.

---

**Title:** A shared, client-side asset layer for palette/effect names, icons & previews

Hi — thanks for maintaining the native iOS app 🙌

WLED's effect and palette names are English identifiers baked into the firmware, and the
core team has been clear that the firmware can't carry translations or artwork (flash
budget). So the natural home for that is **client-side** — which is exactly where a native
app like this one has an advantage: it isn't flash-constrained.

To avoid every client reinventing this, I've put together a small **vendor-neutral, CC0**
asset repo that any WLED client can consume:

**https://github.com/openlamp/wled-assets**

It's a common space for the "presentation layer" of WLED's standard enums:

- **Localized names** for palettes & effects (7 languages, fallback → English).
- **Meanings** — a one-clause explanation of what each palette name refers to (Rivendell →
  Tolkien's elven valley, Tiamat → Babylonian sea-dragon…), great for a subtitle/tooltip.
- **Palette illustrations** — a reusable SVG stencil per evocative palette that you fill
  with the palette's *own* colours (from `/json/palx`): a flame for Fire, waves for
  Atlantica, a real clown for Retro Clown…
- **Effect motion previews** — every effect mapped to one of 9 motion families, with a
  tiny reference animation, so a user sees roughly what an effect *does* before applying it.

The join key is the exact English name from `/json/pal` / `/json/eff`, so integration is
just a lookup with an English fallback — nothing regresses if an entry is missing. It's
data + SVG + one small JS reference; CC0, no attribution needed.

Would this be interesting to wire into the app? I'm happy to help with the integration
(Swift-side loading, gradient injection into the stencils) and to prioritize whatever the
app needs first. The CJK translations are a first pass and would benefit from native review
— PRs welcome on the asset repo.

> Note: if this app renders the WLED controls in a WebView of the device's own web UI (rather than native pickers), the localization belongs in the web UI instead — see the parallel `wled-webui.md` proposal, which covers every WebView-based client at once.
