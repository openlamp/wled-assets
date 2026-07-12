# WLED Effekte

[Paletten](palettes.md) · **Effekte** · [Regler](controls.md) · [Nachtlicht](nightlight.md) · [Segment](segment.md) · [Tasten](buttons.md) · [Tastenereignisse](button-events.md) · [Presets](presets.md) · [Effektregler](fxdata.md) · [Info-Felder](info.md) · [UI-Texte](ui.md) &nbsp;•&nbsp; [Referenz auf Deutsch](README.md)

<sub>Andere Sprachen: [EN](../en/effects.md) · [FR](../fr/effects.md) · [ES](../es/effects.md) · [IT](../it/effects.md) · [JA](../ja/effects.md) · [KO](../ko/effects.md) · [ZH](../zh/effects.md)</sub>

**Effekte** sind WLEDs animierte Muster, wählbar im Reiter **Effekte** (`seg.fx`, Liste `/json/eff`). Der Effekt bestimmt die *Bewegung*, die Palette die *Farbe*.

| Bild | WLED-Name | Übersetzung | Beschreibung |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Statisch | Eine einzelne, ruhige Farbe. |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Blinken | Ein klares An/Aus-Blinzeln — wie ein Auge. |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Atmen | Die Helligkeit schwillt an und ab. |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Wischen | Ein Wischerarm streicht darüber. |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | Ein Wischerarm streicht darüber. |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | Der ganze Streifen wird eine Zufallsfarbe. |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | Ein Strahl wischt wie ein Scheibenwischer. |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | Zufällige Farbblöcke wechseln. |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | Der Streifen durchläuft alle Farbtöne. |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Regenbogen | Ein Regenbogen wandert. |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | Ein Scanner wischt hin und her. |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | Ein Scanner wischt hin und her. |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Verblassen | Eine Farbe blendet ein und aus. |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | Ein Regenbogen wandert. |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | Eine Figur rennt. |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | Eine Säge sägt hin und her. |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Funkeln | Sterne funkeln. |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | Zufällige Funken blitzen. |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | Zufällige Funken blitzen. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Funkeln | Zufällige Funken blitzen. |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | Zufällige Funken blitzen. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | Zufällige Funken blitzen. |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Stroboskop | Ein hartes Stroboskop. |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | Ein Regenbogen wandert. |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | Ein hartes Stroboskop. |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | Ein Regenbogen wandert. |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | Ein Scanner wischt hin und her. |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Verfolgung | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | Ein Regenbogen wandert. |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | Ein Regenbogen wandert. |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | Bänder in vielen Farben. |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | Eine Ampel schaltet um. |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | Ein Strahl wischt wie ein Scheibenwischer. |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | Nordlicht-Bänder schimmern. |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | Teilchen strömen vorbei. |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | Ein Scanner wischt hin und her. |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | Ein Strahl dreht sich wie ein Leuchtturm. |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Feuerwerk | Ein Feuerwerk explodiert. |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Regen | Regen fällt. |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | Tetromino-Blöcke fallen und stapeln sich. |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Feuerflackern | Flammen flackern und steigen. |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Verlauf | Ein wandernder Farbverlauf. |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | Ein Fortschrittsbalken füllt sich. |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | Bälle springen auf und ab. |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | Lichterketten funkeln. |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | Zwei Punkte umkreisen einander. |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | Lichterketten funkeln. |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | Eine Figur rennt. |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | Ein Bild wird abgespielt. |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | Ein Wischerarm streicht darüber. |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | Eine Farbe blendet ein und aus. |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Blitz | Ein Blitz schlägt ein. |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | Ein Auge blickt umher. |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | Ein Komet zieht mit Schweif. |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | Ein Scanner wischt hin und her. |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | Teilchen strömen vorbei. |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | Der Streifen durchläuft alle Farbtöne. |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | Bälle springen auf und ab. |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | Der Streifen durchläuft alle Farbtöne. |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | Flammen flackern und steigen. |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | Bänder in vielen Farben. |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | Ein Puls schlägt im Takt. |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | Zufällige Funken blitzen. |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | Zufällige Funken blitzen. |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | Zufällige Funken blitzen. |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | Zufällige Funken blitzen. |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | Zufällige Funken blitzen. |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | Sterne funkeln. |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | See | Wellen breiten sich über Wasser aus. |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteor | Ein Komet zieht mit Schweif. |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | Wellen breiten sich über Wasser aus. |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | Sterne funkeln. |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | Sterne funkeln. |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | Ein Augenpaar blinzelt im Dunkeln. |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | Ein Muster aus Streifen scrollt. |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | Ein Muster aus Streifen scrollt. |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | Flecken blenden ein und aus. |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | Flecken blenden ein und aus. |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Glitzer | Glitzer funkelt über der Farbe. |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Kerze | Eine Kerzenflamme flackert. |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | Ein Feuerwerk explodiert. |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | Ein Feuerwerk explodiert. |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | Bälle springen auf und ab. |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | Ein Komet zieht mit Schweif. |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | Ein Komet zieht mit Schweif. |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | Ein Komet zieht mit Schweif. |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | Maiskörner platzen auf. |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | Tropfen fallen nacheinander. |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | Farbblasen wandeln sich. |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | Ein Balken füllt sich bis zu einem Wert. |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | Ein Regenbogen wandert. |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Herzschlag | Ein Herz schlägt. |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | Wellen breiten sich über Wasser aus. |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | Eine Kerzenflamme flackert. |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | Glitzer funkelt über der Farbe. |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Sonnenaufgang | Die Sonne geht auf. |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | Geschichtete Sinuswellen verschieben sich. |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | Sterne funkeln. |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | Zufällige Funken blitzen. |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | Die Helligkeit schwillt an und ab. |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | Geschichtete Sinuswellen verschieben sich. |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | Teilchen strömen vorbei. |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | Ein Vogelschwarm fliegt vorbei. |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | Eine Figur tanzt. |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | Ein Rad dreht sich. |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | Ein Rad dreht sich. |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | Ein wandernder Farbverlauf. |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | TV-Rauschen flimmert. |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | Zufällige Farbblöcke wechseln. |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | Ein Raumschiff gleitet vorbei. |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | Bienen schwirren im Schwarm umher. |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | Ein Geist schwebt vorbei. |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | Farbblasen wandeln sich. |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | Blöcke scrollen wie Text. |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | Ein Wirbel windet sich nach außen. |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | Seifenblasen schweben umher. |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | Ein Oktopus schwenkt seine Tentakel. |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | Sterne funkeln. |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | Wellen breiten sich über Wasser aus. |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | Bälle springen auf und ab. |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | Code regnet herab, Matrix-Stil. |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | Bälle springen auf und ab. |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | Farbblasen wandeln sich. |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | Regen fällt. |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | Zufällige Funken blitzen. |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Wasserfall | Regen fällt. |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | Flammen flackern und steigen. |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | Regen fällt. |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | Zufällige Funken blitzen. |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | Zufällige Funken blitzen. |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | Wellen breiten sich über Wasser aus. |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | Flammen flackern und steigen. |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | Ein Wirbel windet sich nach außen. |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | Pac-Man knabbert sich vorwärts. |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | Zwei Stränge bilden eine Doppelhelix. |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrix | Code regnet herab, Matrix-Stil. |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | Farbblasen wandeln sich. |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | Bälle springen auf und ab. |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | Bälle springen auf und ab. |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | Bälle springen auf und ab. |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | Ein Plattenteller dreht sich. |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | Glitzer funkelt über der Farbe. |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | Die Helligkeit schwillt an und ab. |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | Ein Wirbel windet sich nach außen. |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | Eine Sonne strahlt drehende Strahlen aus. |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | Eine Sonne strahlt drehende Strahlen aus. |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | Ein Julia-Fraktal wandelt sich. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | Zellen leben und sterben auf einem Raster. |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | Ein schottisches Tartan-Karo. |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | Nordlicht-Bänder schimmern. |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | Ein Wirbel windet sich nach außen. |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | Eine Lissajous-Kurve wandelt sich. |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | Rotierende geometrische Muster. |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | Elektrische Ranken in einer Plasmakugel. |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | Teilchen strömen vorbei. |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | Farbblasen wandeln sich. |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | Ein Wirbel windet sich nach außen. |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | Zwei Stränge bilden eine Doppelhelix. |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | Ringe stürzen in einen dunklen Kern. |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | Musiknoten ziehen vorbei. |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | Akemi, das WLED-Maskottchen, erscheint. |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | Flammen flackern und steigen. |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | Flammen flackern und steigen. |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | Ein Feuerwerk explodiert. |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | Ein Wirbel windet sich nach außen. |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | Zufällige Funken blitzen. |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | Bälle springen auf und ab. |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | Ringe stürzen in einen dunklen Kern. |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | Ein Schockwellenring dehnt sich aus. |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | Regen fällt. |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | Partikel sprühen aus einer Düse. |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | Ein Geist schwebt vorbei. |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | Farbblasen wandeln sich. |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | Tropfen fallen nacheinander. |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | Bälle springen auf und ab. |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | Eine Figur tanzt. |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | Ein Feuerwerk explodiert. |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | Zufällige Funken blitzen. |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | Sand rinnt durch eine Sanduhr. |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | Partikel sprühen aus einer Düse. |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | Eine Farbwelle wandert über den Streifen. |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | Ein heller Punkt zieht mit Schweif. |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | Ein Feuerwerk explodiert. |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | Ein Audio-Equalizer, Balken tanzen zum Klang. |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | Flammen flackern und steigen. |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | Teilchen strömen vorbei. |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | Ein Schockwellenring dehnt sich aus. |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | Eine Feder lässt ein Gewicht federn. |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | Sterne wirbeln spiralförmig. |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | Farbblasen wandeln sich. |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | Eine Farbe blendet ein und aus. |
