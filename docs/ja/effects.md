# WLED エフェクト

[パレット](palettes.md) · **エフェクト** · [コントロール](controls.md) · [ナイトライト](nightlight.md) · [セグメント](segment.md) · [ボタン](buttons.md) · [スライダー](fxdata.md) · [情報項目](info.md) · [UIラベル](ui.md) &nbsp;•&nbsp; [日本語リファレンス](README.md)

<sub>他の言語: [EN](../en/effects.md) · [FR](../fr/effects.md) · [DE](../de/effects.md) · [ES](../es/effects.md) · [IT](../it/effects.md) · [KO](../ko/effects.md) · [ZH](../zh/effects.md)</sub>

**エフェクト**はWLEDのアニメーション模様。**エフェクト**タブで選択（`seg.fx`、一覧`/json/eff`）。効果が*動き*、パレットが*色*。

| 画像 | WLED名 | 翻訳 | 説明 |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Solid | 単一の安定した色。 |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Blink | 鋭い点滅。 |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Breathe | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Wipe | 光点が走る(チェイス)。 |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | 光点が走る(チェイス)。 |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | 色の波がストリップを流れる。 |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | 光点が走る(チェイス)。 |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | 色の波がストリップを流れる。 |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | 全スペクトルが巡る。 |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Rainbow | 全スペクトルが巡る。 |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | 光点が走る(チェイス)。 |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | 光点が走る(チェイス)。 |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Fade | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | 光点が走る(チェイス)。 |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | 全スペクトルが巡る。 |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | 光点が走る(チェイス)。 |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | 色の波がストリップを流れる。 |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Twinkle | 点がランダムに瞬く。 |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | 点がランダムに瞬く。 |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | 点がランダムに瞬く。 |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Sparkle | 点がランダムに瞬く。 |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | 点がランダムに瞬く。 |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | 点がランダムに瞬く。 |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Strobe | 鋭い点滅。 |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | 鋭い点滅。 |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | 鋭い点滅。 |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | 鋭い点滅。 |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | 色の波がストリップを流れる。 |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Chase | 光点が走る(チェイス)。 |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | 光点が走る(チェイス)。 |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | 全スペクトルが巡る。 |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | 光点が走る(チェイス)。 |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | 光点が走る(チェイス)。 |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | 全スペクトルが巡る。 |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | 全スペクトルが巡る。 |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | 色の波がストリップを流れる。 |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | 光点が走る(チェイス)。 |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | 光点が走る(チェイス)。 |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | 全スペクトルが巡る。 |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | 色の波がストリップを流れる。 |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | 光点が走る(チェイス)。 |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | 光点が走る(チェイス)。 |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Fireworks | 点がランダムに瞬く。 |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Rain | 点が雨のように落ちる。 |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | 点が雨のように落ちる。 |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Fire Flicker | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Gradient | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | 光点が走る(チェイス)。 |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | 色の波がストリップを流れる。 |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | 点がランダムに瞬く。 |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | 色の波がストリップを流れる。 |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | 点がランダムに瞬く。 |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | 光点が走る(チェイス)。 |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | 色の波がストリップを流れる。 |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | 光点が走る(チェイス)。 |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | 光点が走る(チェイス)。 |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Lightning | 鋭い点滅。 |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | 色の波がストリップを流れる。 |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | 光点が走る(チェイス)。 |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | 光点が走る(チェイス)。 |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | 色の波がストリップを流れる。 |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | 色の波がストリップを流れる。 |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | 全スペクトルが巡る。 |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | 色の波がストリップを流れる。 |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | 全スペクトルが巡る。 |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | 色の波がストリップを流れる。 |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | 色の波がストリップを流れる。 |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | 単一の安定した色。 |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | 色の波がストリップを流れる。 |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | 色の波がストリップを流れる。 |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | 色の波がストリップを流れる。 |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | 色の波がストリップを流れる。 |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | 点がランダムに瞬く。 |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lake | 色の波がストリップを流れる。 |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteor | 点が雨のように落ちる。 |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | 色の波がストリップを流れる。 |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | 光点が走る(チェイス)。 |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | 色の波がストリップを流れる。 |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | 点がランダムに瞬く。 |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | 点がランダムに瞬く。 |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | 単一の安定した色。 |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | 単一の安定した色。 |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | 色の波がストリップを流れる。 |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Glitter | 点がランダムに瞬く。 |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Candle | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | 点がランダムに瞬く。 |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | 点がランダムに瞬く。 |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | 色の波がストリップを流れる。 |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | 全スペクトルが巡る。 |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | 点がランダムに瞬く。 |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | 点が雨のように落ちる。 |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | 色の波がストリップを流れる。 |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | 全スペクトルが巡る。 |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Heartbeat | 色の波がストリップを流れる。 |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | 色の波がストリップを流れる。 |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | 単一の安定した色。 |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Sunrise | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | 色の波がストリップを流れる。 |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | 点がランダムに瞬く。 |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | 色の波がストリップを流れる。 |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | 色の波がストリップを流れる。 |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | 色の波がストリップを流れる。 |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | 色の波がストリップを流れる。 |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | 光点が走る(チェイス)。 |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | 色の波がストリップを流れる。 |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | 色の波がストリップを流れる。 |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | 色の波がストリップを流れる。 |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | 色の波がストリップを流れる。 |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | 色の波がストリップを流れる。 |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | 色の波がストリップを流れる。 |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | 色の波がストリップを流れる。 |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | 色の波がストリップを流れる。 |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | 色の波がストリップを流れる。 |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | 色の波がストリップを流れる。 |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | 色の波がストリップを流れる。 |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | 色の波がストリップを流れる。 |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | 色の波がストリップを流れる。 |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | 色の波がストリップを流れる。 |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | 色の波がストリップを流れる。 |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | 色の波がストリップを流れる。 |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | 色の波がストリップを流れる。 |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | 色の波がストリップを流れる。 |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | 色の波がストリップを流れる。 |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | 色の波がストリップを流れる。 |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | 色の波がストリップを流れる。 |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | 色の波がストリップを流れる。 |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | 色の波がストリップを流れる。 |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | 点が雨のように落ちる。 |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | 色の波がストリップを流れる。 |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Waterfall | 点が雨のように落ちる。 |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | 色の波がストリップを流れる。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを流れる。 |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | 色の波がストリップを流れる。 |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | 色の波がストリップを流れる。 |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | 色の波がストリップを流れる。 |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | 色の波がストリップを流れる。 |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | 色の波がストリップを流れる。 |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | 色の波がストリップを流れる。 |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | 色の波がストリップを流れる。 |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrix | 点が雨のように落ちる。 |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | 色の波がストリップを流れる。 |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | 色の波がストリップを流れる。 |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | 色の波がストリップを流れる。 |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | 色の波がストリップを流れる。 |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | 色の波がストリップを流れる。 |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | 色の波がストリップを流れる。 |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | 色の波がストリップを流れる。 |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | 色の波がストリップを流れる。 |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | 明るさが強弱する(呼吸)。 |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | 色の波がストリップを流れる。 |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | 色の波がストリップを流れる。 |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | 色の波がストリップを流れる。 |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | 色の波がストリップを流れる。 |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | 色の波がストリップを流れる。 |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | 色の波がストリップを流れる。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを流れる。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを流れる。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを流れる。 |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | 色の波がストリップを流れる。 |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | 色の波がストリップを流れる。 |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | 色の波がストリップを流れる。 |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | 色の波がストリップを流れる。 |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | 色の波がストリップを流れる。 |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | 色の波がストリップを流れる。 |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | 色の波がストリップを流れる。 |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | 色の波がストリップを流れる。 |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | 色の波がストリップを流れる。 |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | 色の波がストリップを流れる。 |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | 色の波がストリップを流れる。 |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | 色の波がストリップを流れる。 |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | 色の波がストリップを流れる。 |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | 色の波がストリップを流れる。 |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | 点がランダムに瞬く。 |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | 点が雨のように落ちる。 |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | 点が雨のように落ちる。 |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | 光点が走る(チェイス)。 |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | 点がランダムに瞬く。 |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | 点がランダムに瞬く。 |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | 光点が走る(チェイス)。 |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | 点がランダムに瞬く。 |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | 暖色が炎のように揺らめく。 |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | 色の波がストリップを流れる。 |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | 色の波がストリップを流れる。 |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | 色の波がストリップを流れる。 |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | 色の波がストリップを流れる。 |
