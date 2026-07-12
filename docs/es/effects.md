# WLED Efectos

[Paletas](palettes.md) · **Efectos** · [Controles](controls.md) · [Luz nocturna](nightlight.md) · [Segmento](segment.md) · [Botones](buttons.md) · [Eventos de botón](button-events.md) · [Presets](presets.md) · [Deslizadores](fxdata.md) · [Campos de info](info.md) · [Etiquetas de IU](ui.md) &nbsp;•&nbsp; [Referencia en español](README.md)

<sub>Otros idiomas: [EN](../en/effects.md) · [FR](../fr/effects.md) · [DE](../de/effects.md) · [IT](../it/effects.md) · [JA](../ja/effects.md) · [KO](../ko/effects.md) · [ZH](../zh/effects.md)</sub>

Los **efectos** son los patrones animados de WLED, en la pestaña **Efectos** (`seg.fx`, lista `/json/eff`). El efecto define el *movimiento*; la paleta, el *color*.

| Imagen | Nombre WLED | Traducción | Descripción |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Fijo | Un color fijo y uniforme. |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Parpadeo | Un parpadeo nítido de encendido/apagado — como un ojo que parpadea. |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Respiración | El brillo crece y decae (respiración). |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Barrido | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | Una onda de color recorre la tira. |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | Una onda de color recorre la tira. |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | El espectro completo se desplaza. |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Arcoíris | El espectro completo se desplaza. |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Desvanecer | El brillo crece y decae (respiración). |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | El espectro completo se desplaza. |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | Una onda de color recorre la tira. |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Centelleo | Puntos que centellean al azar. |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | Puntos que centellean al azar. |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | Puntos que centellean al azar. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Destellos | Puntos que centellean al azar. |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | Puntos que centellean al azar. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | Puntos que centellean al azar. |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Estroboscopio | Destellos nítidos, encendido/apagado. |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | Destellos nítidos, encendido/apagado. |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | Destellos nítidos, encendido/apagado. |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | Destellos nítidos, encendido/apagado. |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | Una onda de color recorre la tira. |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Persecución | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | El espectro completo se desplaza. |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | El espectro completo se desplaza. |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | El espectro completo se desplaza. |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | Una onda de color recorre la tira. |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | El espectro completo se desplaza. |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | Una onda de color recorre la tira. |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Fuegos artificiales | Puntos que centellean al azar. |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Lluvia | Puntos que caen como lluvia. |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | Puntos que caen como lluvia. |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Fuego parpadeante | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Degradado | El brillo crece y decae (respiración). |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | Una onda de color recorre la tira. |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | Puntos que centellean al azar. |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | Una onda de color recorre la tira. |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | Puntos que centellean al azar. |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | Una onda de color recorre la tira. |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | El brillo crece y decae (respiración). |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Relámpago | Destellos nítidos, encendido/apagado. |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | Un ojo recorre la tira con la mirada. |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | Una onda de color recorre la tira. |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | Una onda de color recorre la tira. |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | El espectro completo se desplaza. |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | Una onda de color recorre la tira. |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | El espectro completo se desplaza. |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | Una onda de color recorre la tira. |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | Una onda de color recorre la tira. |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | Un color fijo y uniforme. |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | Una onda de color recorre la tira. |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | Una onda de color recorre la tira. |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | Una onda de color recorre la tira. |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | Una onda de color recorre la tira. |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | Puntos que centellean al azar. |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lago | Agua tranquila que reluce y ondula. |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteoro | Puntos que caen como lluvia. |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | Una onda de color recorre la tira. |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | Una onda de color recorre la tira. |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | Puntos que centellean al azar. |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | Puntos que centellean al azar. |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | Unos ojos se abren y miran en la oscuridad. |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | Un color fijo y uniforme. |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | Un color fijo y uniforme. |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | Una onda de color recorre la tira. |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | El brillo crece y decae (respiración). |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Purpurina | Puntos que centellean al azar. |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Vela | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | Puntos que centellean al azar. |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | Puntos que centellean al azar. |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | Una onda de color recorre la tira. |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | El brillo crece y decae (respiración). |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | El brillo crece y decae (respiración). |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | El espectro completo se desplaza. |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | Puntos que centellean al azar. |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | Puntos que caen como lluvia. |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | Una onda de color recorre la tira. |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | Una onda de color recorre la tira. |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | El espectro completo se desplaza. |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Latido | Una onda de color recorre la tira. |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | Una onda de color recorre la tira. |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | Un color fijo y uniforme. |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Amanecer | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | Una onda de color recorre la tira. |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | Puntos que centellean al azar. |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | Una onda de color recorre la tira. |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | El brillo crece y decae (respiración). |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | Una onda de color recorre la tira. |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | Una onda de color recorre la tira. |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | Una bandada de pájaros cruza la tira. |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | Una onda de color recorre la tira. |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | Una onda de color recorre la tira. |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | El brillo crece y decae (respiración). |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | Una onda de color recorre la tira. |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | Una onda de color recorre la tira. |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | Una onda de color recorre la tira. |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | Una onda de color recorre la tira. |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | Una onda de color recorre la tira. |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | Una onda de color recorre la tira. |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | Una onda de color recorre la tira. |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | Una onda de color recorre la tira. |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | Una onda de color recorre la tira. |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | Una onda de color recorre la tira. |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | Una onda de color recorre la tira. |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | Una onda de color recorre la tira. |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | Una onda de color recorre la tira. |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | Una onda de color recorre la tira. |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | Una onda de color recorre la tira. |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | Una onda de color recorre la tira. |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | Una onda de color recorre la tira. |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | Una onda de color recorre la tira. |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | Una onda de color recorre la tira. |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | Una onda de color recorre la tira. |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | Una onda de color recorre la tira. |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | Una onda de color recorre la tira. |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | Puntos que caen como lluvia. |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | Una onda de color recorre la tira. |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Cascada | Puntos que caen como lluvia. |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | Una onda de color recorre la tira. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Una onda de color recorre la tira. |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | Una onda de color recorre la tira. |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | Una onda de color recorre la tira. |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | Una onda de color recorre la tira. |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | Una onda de color recorre la tira. |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | Una onda de color recorre la tira. |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | Una onda de color recorre la tira. |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | Una onda de color recorre la tira. |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | Dos hebras se entrelazan en doble hélice. |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matriz | Puntos que caen como lluvia. |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | Una onda de color recorre la tira. |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | Una onda de color recorre la tira. |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | Una onda de color recorre la tira. |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | Una onda de color recorre la tira. |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | Una onda de color recorre la tira. |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | Una onda de color recorre la tira. |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | Una onda de color recorre la tira. |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | Una onda de color recorre la tira. |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | El brillo crece y decae (respiración). |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | Una onda de color recorre la tira. |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | Una onda de color recorre la tira. |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | Una onda de color recorre la tira. |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | Una onda de color recorre la tira. |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | Una onda de color recorre la tira. |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | Una onda de color recorre la tira. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Una onda de color recorre la tira. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Una onda de color recorre la tira. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Una onda de color recorre la tira. |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | Una onda de color recorre la tira. |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | Una onda de color recorre la tira. |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | Una onda de color recorre la tira. |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | Una onda de color recorre la tira. |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | Una onda de color recorre la tira. |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | Una onda de color recorre la tira. |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | Una onda de color recorre la tira. |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | Una onda de color recorre la tira. |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | Una onda de color recorre la tira. |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | Una onda de color recorre la tira. |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | Una doble hélice que gira. |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | Una onda de color recorre la tira. |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | Una onda de color recorre la tira. |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | Una onda de color recorre la tira. |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | Partículas brotan como un volcán. |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | Puntos que centellean al azar. |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | Puntos que caen como lluvia. |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | Puntos que caen como lluvia. |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | Puntos que centellean al azar. |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | Puntos que centellean al azar. |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | Un punto de luz recorre la tira (persecución). |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | Puntos que centellean al azar. |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | Tonos cálidos titilan como llamas. |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | Una onda de color recorre la tira. |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | Una onda de color recorre la tira. |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | Una onda de color recorre la tira. |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | Una onda de color recorre la tira. |
