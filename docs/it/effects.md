# WLED Effetti

[Tavolozze](palettes.md) · **Effetti** · [Controlli](controls.md) · [Luce notturna](nightlight.md) · [Segmento](segment.md) · [Pulsanti](buttons.md) · [Eventi pulsante](button-events.md) · [Preset](presets.md) · [Cursori effetto](fxdata.md) · [Campi info](info.md) · [Etichette UI](ui.md) &nbsp;•&nbsp; [Riferimento in italiano](README.md)

<sub>Altre lingue: [EN](../en/effects.md) · [FR](../fr/effects.md) · [DE](../de/effects.md) · [ES](../es/effects.md) · [JA](../ja/effects.md) · [KO](../ko/effects.md) · [ZH](../zh/effects.md)</sub>

Gli **effetti** sono i motivi animati di WLED, nella scheda **Effetti** (`seg.fx`, elenco `/json/eff`). L'effetto definisce il *movimento*; la tavolozza il *colore*.

| Immagine | Nome WLED | Traduzione | Descrizione |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Fisso | Un unico colore fisso. |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Lampeggio | Un lampeggio netto — come un occhio. |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Respiro | La luminosità cresce e cala. |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Spazzata | Un braccio tergicristallo spazza. |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | Un braccio tergicristallo spazza. |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | L'intera striscia vira a un colore casuale. |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | Un fascio spazza come un tergicristallo. |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | Blocchi di colore cambiano a caso. |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | L'intera striscia scorre le tinte. |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Arcobaleno | Un arcobaleno scorre. |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | Uno scanner spazza avanti e indietro. |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | Uno scanner spazza avanti e indietro. |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Dissolvenza | Un colore appare e svanisce. |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | Un arcobaleno scorre. |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | Una figura corre. |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | Una sega taglia avanti e indietro. |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Scintillio | Stelle brillano. |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | Scintille casuali guizzano. |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | Scintille casuali guizzano. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Scintillii | Scintille casuali guizzano. |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | Scintille casuali guizzano. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | Scintille casuali guizzano. |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Stroboscopio | Uno stroboscopio deciso. |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | Un arcobaleno scorre. |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | Uno stroboscopio deciso. |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | Un arcobaleno scorre. |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | Uno scanner spazza avanti e indietro. |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Inseguimento | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | Un arcobaleno scorre. |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | Un arcobaleno scorre. |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | Bande di molti colori. |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | Un semaforo cambia. |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | Un fascio spazza come un tergicristallo. |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | Bande di aurora boreale ondeggiano. |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | Particelle scorrono. |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | Uno scanner spazza avanti e indietro. |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | Un fascio ruota come un faro. |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Fuochi d'artificio | Un fuoco d'artificio esplode. |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Pioggia | Cade la pioggia. |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | Pezzi di Tetris cadono e si impilano. |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Fuoco tremolante | Fiamme guizzano e salgono. |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Gradiente | Un gradiente di colore che scorre. |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | Una barra di avanzamento si riempie. |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | Palline rimbalzano. |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | Lucine fatate scintillano. |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | Due punti si orbitano. |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | Lucine fatate scintillano. |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | Una figura corre. |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | Un'immagine scorre. |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | Un braccio tergicristallo spazza. |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | Un colore appare e svanisce. |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Fulmine | Un fulmine colpisce. |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | Un occhio scruta intorno. |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | Una cometa sfreccia con la coda. |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | Uno scanner spazza avanti e indietro. |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | Particelle scorrono. |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | L'intera striscia scorre le tinte. |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | Palline rimbalzano. |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | L'intera striscia scorre le tinte. |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | Fiamme guizzano e salgono. |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | Bande di molti colori. |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | Un battito pulsa a ogni tempo. |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | Un unico colore fisso. |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | Scintille casuali guizzano. |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | Scintille casuali guizzano. |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | Scintille casuali guizzano. |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | Scintille casuali guizzano. |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | Stelle brillano. |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lago | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteora | Una cometa sfreccia con la coda. |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | Stelle brillano. |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | Stelle brillano. |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | Un paio di occhi sbatte nel buio. |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | Un unico colore fisso. |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | Un unico colore fisso. |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | Macchie appaiono e svaniscono. |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | Macchie appaiono e svaniscono. |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Glitter | Glitter scintilla sul colore. |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Candela | La fiamma di una candela tremola. |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | Un fuoco d'artificio esplode. |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | Un fuoco d'artificio esplode. |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | Palline rimbalzano. |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | Una cometa sfreccia con la coda. |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | Una cometa sfreccia con la coda. |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | Una cometa sfreccia con la coda. |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | Chicchi di popcorn scoppiano. |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | Gocce cadono una a una. |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | Bolle di colore si trasformano. |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | Una barra si riempie a un livello. |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | Un arcobaleno scorre. |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Battito | Un cuore batte. |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | La fiamma di una candela tremola. |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | Glitter scintilla sul colore. |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Alba | Il sole sorge. |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | Onde sinusoidali sovrapposte scorrono. |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | Stelle brillano. |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | Scintille casuali guizzano. |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | La luminosità cresce e cala. |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | Onde sinusoidali sovrapposte scorrono. |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | Particelle scorrono. |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | Uno stormo di uccelli attraversa. |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | Una figura balla. |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | Una ruota gira. |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | Una ruota gira. |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | Un gradiente di colore che scorre. |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | Il disturbo TV tremola. |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | Blocchi di colore cambiano a caso. |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | Un'astronave scivola. |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | Api ronzano in sciame. |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | Un fantasma fluttua. |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | Bolle di colore si trasformano. |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | Blocchi scorrono come testo. |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | Un vortice si avvolge verso l'esterno. |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | Bolle di sapone fluttuano. |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | Un polpo agita i tentacoli. |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | Codice cade, stile Matrix. |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | Codice cade, stile Matrix. |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | Palline rimbalzano. |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | Codice cade, stile Matrix. |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | Palline rimbalzano. |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | Bolle di colore si trasformano. |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | Cade la pioggia. |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | Scintille casuali guizzano. |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | Scintille casuali guizzano. |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | Codice cade, stile Matrix. |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Cascata | Cade la pioggia. |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | Codice cade, stile Matrix. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | Fiamme guizzano e salgono. |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | Cade la pioggia. |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | Scintille casuali guizzano. |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | Scintille casuali guizzano. |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | Fiamme guizzano e salgono. |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | Un vortice si avvolge verso l'esterno. |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | Pac-Man avanza sgranocchiando. |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | Due filamenti formano una doppia elica. |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrice | Codice cade, stile Matrix. |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | Palline rimbalzano. |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | Palline rimbalzano. |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | Palline rimbalzano. |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | Palline rimbalzano. |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | Un giradischi gira. |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | La luminosità cresce e cala. |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | Un vortice si avvolge verso l'esterno. |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | Un sole irradia raggi rotanti. |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | Un sole irradia raggi rotanti. |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | Un frattale di Julia si trasforma. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | Cellule nascono e muoiono su una griglia. |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | Un tartan scozzese. |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | Bande di aurora boreale ondeggiano. |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | Un vortice si avvolge verso l'esterno. |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | Una curva di Lissajous si trasforma. |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | Motivi geometrici rotanti. |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | Palline rimbalzano. |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | Particelle scorrono. |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | Un vortice si avvolge verso l'esterno. |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | Due filamenti formano una doppia elica. |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | Anelli collassano in un nucleo scuro. |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | Note musicali scorrono. |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | Akemi, la mascotte di WLED, appare. |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | Fiamme guizzano e salgono. |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | Fiamme guizzano e salgono. |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | Un fuoco d'artificio esplode. |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | Un vortice si avvolge verso l'esterno. |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | Scintille casuali guizzano. |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | Palline rimbalzano. |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | Un anello d'urto si espande. |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | Cade la pioggia. |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | Un fantasma fluttua. |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | Bolle di colore si trasformano. |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | Gocce cadono una a una. |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | Palline rimbalzano. |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | Una figura balla. |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | Un fuoco d'artificio esplode. |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | Scintille casuali guizzano. |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | La sabbia scende in una clessidra. |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | Un punto luminoso scorre con scia. |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | Stelle brillano. |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | Increspature si diffondono sull'acqua. |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | Fiamme guizzano e salgono. |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | Particelle scorrono. |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | Un anello d'urto si espande. |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | Un'onda di colore percorre la striscia. |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | Stelle vorticano a spirale. |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | Bolle di colore si trasformano. |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | Un'onda di colore percorre la striscia. |
