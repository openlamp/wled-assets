# Outreach draft — Android / cross-platform app (casvanluijtelaar/WLED-App)

**Where:** a GitHub Issue on https://github.com/casvanluijtelaar/WLED-App
**Status:** DRAFT — not posted. Review before sending.

---

**Title:** Shared client-side assets: localized palette/effect names, icons & previews

Hi — I love that this is a clean cross-platform (Flutter) WLED client.

WLED's palette/effect names are English identifiers compiled into the firmware, and the
core team can't ship translations/artwork there (flash budget). That work belongs on the
client side — so rather than each app rebuilding it, I've assembled a **vendor-neutral,
CC0** asset repo meant to be a common resource for *all* WLED clients:

**https://github.com/openlamp/wled-assets**

What it offers (all keyed by the English name from `/json/pal` / `/json/eff`, with an
English fallback so nothing regresses):

- **Localized names** — palettes & effects in 7 languages.
- **Palette illustrations** — reusable SVG stencils you fill with the palette's real
  colours (`/json/palx`): waves for Ocean, a flame for Fire, a Christmas bulb for C9…
- **Effect previews** — each effect mapped to one of 9 motion families + a small reference
  animation, so users see what an effect does before applying it.
- **Name meanings** — a short explanation per palette name, for tooltips.

It's plain data + SVG + a small JS reference (easy to port to Dart). Would you be open to
consuming it? A shared source means a fix or a new language benefits every app at once,
not just one. Happy to help with the Flutter-side integration and to align the data
shape with what's convenient for you.
