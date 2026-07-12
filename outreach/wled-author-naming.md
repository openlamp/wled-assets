# Draft — message to the WLED author/team (naming OK + asset offer)

**Where:** email `dev.aircoookie@gmail.com`, or the WLED Discord / [Discourse](https://wled.discourse.group/).
**Status:** DRAFT — not sent. Review, tweak, and send yourself. Do not claim affiliation.

---

**Subject:** A Stream Deck plugin *for WLED* + a CC0 community asset repo — quick naming check

Hi Christian / WLED team,

I'm Benoît (GitHub @Beennnn). I've been building **LumiDeck**, an Elgato Stream Deck plugin
to drive WLED lamps & strips — **100 % local**, over the JSON API, no cloud. It started
multi-vendor, but I'm dropping Tuya to focus **entirely on WLED**.

Two things, and I'd rather do them cleanly:

**1. Naming.** I'd like to present it as *"**LumiDeck — a Stream Deck controller for WLED**"*:
my own distinctive name, "for WLED" purely **descriptive**, always with a clear disclaimer
(*"not affiliated with or endorsed by the WLED project; it interoperates via the public
local API"*). Before I push it publicly — and possibly onto the Elgato Marketplace — I
wanted to **check you're comfortable** with that framing and with using "WLED" as a
descriptor. If you'd prefer different wording, I'll happily adjust.

**2. Something I'd like to give back.** While building it I assembled
**[openlamp/wled-assets](https://github.com/openlamp/wled-assets)** (CC0, vendor-neutral):

- **Localized names**, English fallback, for the standard **palettes** and **effects**
  (plus controls, nightlight modes, segment actions, button events, presets, info & UI
  labels) in **8 languages** — the firmware stays English-only, this is a client-side layer.
- **Illustrations**: each palette drawn as a telling icon filled with its *own* gradient
  (Rivendell → mountains, Fire → a flame…), and a **distinct animated motion preview per
  effect** (Rainbow → an arc, Sweep → a broom, Ghost Rider → a ghost, Lissajous → the
  curve…), all transparent so they sit on light or dark.

It's firmware-independent by design, so **any** WLED client could use it — the embedded web
UI, the native iOS/Android apps, or third-party tools. I'd be glad to shape it however
would be most useful to the project, or simply hand it over.

No rush at all — and thank you for WLED, it's a genuine joy to build on.

Best,
Benoît (@Beennnn)
