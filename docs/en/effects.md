# WLED Effects

[Palettes](palettes.md) · **Effects** · [Controls](controls.md) · [Nightlight](nightlight.md) · [Segment](segment.md) · [Buttons](buttons.md) · [Button events](button-events.md) · [Presets](presets.md) · [Effect sliders](fxdata.md) · [Info fields](info.md) · [UI labels](ui.md) &nbsp;•&nbsp; [Reference in English](README.md)

<sub>Other languages: [FR](../fr/effects.md) · [DE](../de/effects.md) · [ES](../es/effects.md) · [IT](../it/effects.md) · [JA](../ja/effects.md) · [KO](../ko/effects.md) · [ZH](../zh/effects.md)</sub>

**Effects** are WLED's animated patterns, chosen in the **Effects** tab. They map to `seg.fx`; the list comes from `/json/eff`. An effect defines the *motion*; the palette gives the *colour*.

| Image | WLED name | Translation | Description |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Solid | A single steady colour. |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Blink | A crisp on/off blink — like an eye. |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Breathe | Brightness swells and fades. |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Wipe | A wiper arm sweeps across. |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | A wiper arm sweeps across. |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | The whole strip turns one random colour. |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | A beam sweeps like a wiper. |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | Random colour blocks shuffle. |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | The whole strip cycles through hues. |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Rainbow | A rainbow arc cycles. |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | A scanner sweeps back and forth. |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | A scanner sweeps back and forth. |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Fade | A colour fades in and out. |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | A bright dot sweeps with a trail. |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | A rainbow arc cycles. |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | A figure runs. |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | A saw cuts back and forth. |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Twinkle | Stars twinkle. |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | Random sparkles pop. |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | Random sparkles pop. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Sparkle | Random sparkles pop. |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | Random sparkles pop. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | Random sparkles pop. |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Strobe | A hard strobe flash. |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | A rainbow arc cycles. |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | A hard strobe flash. |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | A rainbow arc cycles. |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | A scanner sweeps back and forth. |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Chase | A bright dot sweeps with a trail. |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | A bright dot sweeps with a trail. |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | A rainbow arc cycles. |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | A bright dot sweeps with a trail. |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | A bright dot sweeps with a trail. |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | A rainbow arc cycles. |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | Bands of many colours. |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | A traffic light cycles. |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | A beam sweeps like a wiper. |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | A bright dot sweeps with a trail. |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | Northern-lights bands shimmer. |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | Particles flow across. |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | A scanner sweeps back and forth. |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | A beam rotates like a lighthouse. |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Fireworks | A firework bursts. |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Rain | Rain falls. |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | Tetromino blocks fall and stack. |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Fire Flicker | Flames flicker and rise. |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Gradient | A shifting colour gradient. |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | A progress bar fills. |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | Balls bounce up and down. |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | Fairy lights twinkle. |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | Two dots orbit each other. |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | Fairy lights twinkle. |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | A figure runs. |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | A picture plays back. |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | A bright dot sweeps with a trail. |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | A wiper arm sweeps across. |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | A colour fades in and out. |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Lightning | Lightning strikes. |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | An eye scans, pupil roving. |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | A comet streaks with a fading tail. |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | A scanner sweeps back and forth. |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | Particles flow across. |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | A colour wave travels along the strip. |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | The whole strip cycles through hues. |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | Balls bounce up and down. |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | The whole strip cycles through hues. |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | Flames flicker and rise. |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | Bands of many colours. |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | A pulse throbs on every beat. |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | A single steady colour. |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | Random sparkles pop. |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | Random sparkles pop. |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | Random sparkles pop. |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | Random sparkles pop. |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | Stars twinkle. |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lake | Ripples spread over water. |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteor | A comet streaks with a fading tail. |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | A colour wave travels along the strip. |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | A bright dot sweeps with a trail. |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | Ripples spread over water. |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | Stars twinkle. |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | Stars twinkle. |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | A pair of eyes blink in the dark. |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | A single steady colour. |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | A single steady colour. |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | Spots fade in and out. |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | Spots fade in and out. |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Glitter | Glitter sparkles over the colour. |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Candle | A candle flame flickers. |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | A firework bursts. |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | A firework bursts. |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | Balls bounce up and down. |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | A comet streaks with a fading tail. |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | A comet streaks with a fading tail. |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | A comet streaks with a fading tail. |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | Kernels pop up. |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | Drops fall one by one. |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | Colour blobs morph and drift. |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | A bar fills to a set level. |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | A rainbow arc cycles. |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Heartbeat | A heart beats. |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | Ripples spread over water. |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | A candle flame flickers. |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | Glitter sparkles over the colour. |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Sunrise | The sun rises. |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | Layered sine waves shift. |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | Stars twinkle. |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | Random sparkles pop. |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | Brightness swells and fades. |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | Layered sine waves shift. |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | Particles flow across. |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | A flock of birds flies across. |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | A figure dances. |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | A wheel spins. |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | A wheel spins. |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | A shifting colour gradient. |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | TV static flickers. |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | Random colour blocks shuffle. |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | A spaceship glides by. |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | Bees buzz around in a swarm. |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | A ghost drifts by. |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | Colour blobs morph and drift. |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | Blocks scroll like text. |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | A vortex winds outward. |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | A colour wave travels along the strip. |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | Soap bubbles float and drift. |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | An octopus waves its tentacles. |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | A colour wave travels along the strip. |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | Code rains down, Matrix-style. |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | Code rains down, Matrix-style. |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | Balls bounce up and down. |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | Code rains down, Matrix-style. |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | Balls bounce up and down. |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | Colour blobs morph and drift. |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | Rain falls. |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | Random sparkles pop. |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | Random sparkles pop. |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | Ripples spread over water. |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | Code rains down, Matrix-style. |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | Ripples spread over water. |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Waterfall | Rain falls. |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | Code rains down, Matrix-style. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | A colour wave travels along the strip. |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | Flames flicker and rise. |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | Rain falls. |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | Random sparkles pop. |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | Random sparkles pop. |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | A colour wave travels along the strip. |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | Ripples spread over water. |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | Flames flicker and rise. |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | A vortex winds outward. |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | Pac-Man chomps along. |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | Two strands weave into a double helix. |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrix | Code rains down, Matrix-style. |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | Balls bounce up and down. |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | Ripples spread over water. |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | Balls bounce up and down. |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | Balls bounce up and down. |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | Balls bounce up and down. |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | A turntable spins. |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | A colour wave travels along the strip. |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | A colour wave travels along the strip. |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | Brightness swells and fades. |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | A colour wave travels along the strip. |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | A vortex winds outward. |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | A colour wave travels along the strip. |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | A sun radiates rotating rays. |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | A sun radiates rotating rays. |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | A Julia-set fractal morphs. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | A colour wave travels along the strip. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | A colour wave travels along the strip. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | A colour wave travels along the strip. |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | Cells live and die on a grid. |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | A Scottish tartan plaid. |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | Northern-lights bands shimmer. |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | A vortex winds outward. |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | A Lissajous curve morphs. |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | Rotating geometric patterns. |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | Balls bounce up and down. |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | Particles flow across. |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | A colour wave travels along the strip. |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | A vortex winds outward. |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | Two strands weave into a double helix. |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | Rings collapse into a dark core. |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | A colour wave travels along the strip. |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | Musical notes drift by. |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | Akemi, the WLED mascot, appears. |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | Flames flicker and rise. |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | Flames flicker and rise. |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | A firework bursts. |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | A vortex winds outward. |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | Random sparkles pop. |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | Balls bounce up and down. |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | A colour wave travels along the strip. |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | A colour wave travels along the strip. |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | A shockwave ring expands. |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | Rain falls. |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | A colour wave travels along the strip. |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | Ripples spread over water. |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | Ripples spread over water. |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | A ghost drifts by. |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | Colour blobs morph and drift. |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | Drops fall one by one. |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | Balls bounce up and down. |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | A figure dances. |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | A firework bursts. |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | Random sparkles pop. |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | Sand falls through an hourglass. |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | A colour wave travels along the strip. |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | A colour wave travels along the strip. |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | A bright dot sweeps with a trail. |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | Stars twinkle. |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | Ripples spread over water. |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | Flames flicker and rise. |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | Particles flow across. |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | A shockwave ring expands. |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | A colour wave travels along the strip. |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | Stars spiral outward. |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | Colour blobs morph and drift. |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | A colour wave travels along the strip. |
