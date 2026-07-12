# Outreach draft — WLED embedded web UI (wled/WLED)

**Where:** a GitHub Discussion on https://github.com/wled/WLED (NOT a firmware PR).
**Status:** DRAFT — not posted. Review before sending.
**Note:** frame this as *optional, opt-in, zero cost to the default binary* — the core
team's stated objection is flash budget, so lead with that constraint being respected.

---

**Title:** Optional, client-side i18n + palette icons + effect previews (no firmware cost)

Hi — fully aware the firmware can't carry translations or artwork; the flash budget makes
that a non-starter, and that's the right call. This proposal is deliberately **outside**
that constraint.

I've put together a **vendor-neutral, CC0** asset repo — localized names, palette
illustrations, effect motion previews, and name meanings — for WLED's standard palette and
effect enumerations, keyed by the English name from `/json/pal` / `/json/eff`:

**https://github.com/openlamp/wled-assets**

Several long-standing requests ask for localized names (#459, #2165, #3688, forum threads).
This asset is the reusable, firmware-independent answer. For the **embedded web UI**, if
there's ever appetite, it could be adopted as an **opt-in** layer that:

- **adds zero bytes to the default binary** — assets fetched on demand only when the user
  picks a non-English language / enables palette icons, never compiled into PROGMEM;
- **falls back to today's English** behaviour when disabled or when an entry is missing;
- reuses colours the UI already has (`/json/palx`) to render palette icons client-side.

Totally understand if the embedded UI wants to stay lean and leave this to the apps — I'm
mainly flagging the asset exists and is CC0, so any WLED client (the native iOS/Android
apps, third-party tools, or the UI) can use it without reinventing it. Happy to discuss a
shape that would be acceptable if there's interest.
