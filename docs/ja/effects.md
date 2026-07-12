# WLED エフェクト

[パレット](palettes.md) · **エフェクト** · [コントロール](controls.md) · [ナイトライト](nightlight.md) · [セグメント](segment.md) · [ボタン](buttons.md) · [ボタンイベント](button-events.md) · [プリセット](presets.md) · [スライダー](fxdata.md) · [情報項目](info.md) · [UIラベル](ui.md) &nbsp;•&nbsp; [日本語リファレンス](README.md)

<sub>他の言語: [EN](../en/effects.md) · [FR](../fr/effects.md) · [DE](../de/effects.md) · [ES](../es/effects.md) · [IT](../it/effects.md) · [KO](../ko/effects.md) · [ZH](../zh/effects.md)</sub>

**エフェクト**はWLEDのアニメーション模様。**エフェクト**タブで選択（`seg.fx`、一覧`/json/eff`）。効果が*動き*、パレットが*色*。

| 画像 | WLED名 | 翻訳 | 説明 |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Solid | 単一の安定した色。 |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Blink | はっきりした点滅——目のように。 |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Breathe | 明るさが膨らんでは沈む。 |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Wipe | ワイパーが払う。 |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | ワイパーが払う。 |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | 全体がランダムな一色に変わる。 |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | ワイパーのように光が振れる。 |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | 色ブロックがランダムに変わる。 |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | 全体が色相を巡る。 |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Rainbow | 虹の弧が巡る。 |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | スキャナーが左右に走る。 |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | スキャナーが左右に走る。 |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Fade | 色が現れては消える。 |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | 光点が尾を引いて走る。 |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | 虹の弧が巡る。 |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | 人影が走る。 |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | のこぎりが行き来する。 |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Twinkle | 星がまたたく。 |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | ランダムにきらめく。 |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | ランダムにきらめく。 |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Sparkle | ランダムにきらめく。 |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | ランダムにきらめく。 |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | ランダムにきらめく。 |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Strobe | 強いストロボ点滅。 |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | 虹の弧が巡る。 |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | 強いストロボ点滅。 |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | 虹の弧が巡る。 |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | スキャナーが左右に走る。 |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Chase | 光点が尾を引いて走る。 |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | 光点が尾を引いて走る。 |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | 虹の弧が巡る。 |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | 光点が尾を引いて走る。 |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | 光点が尾を引いて走る。 |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | 虹の弧が巡る。 |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | 多彩な色の帯。 |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | 信号機が変わる。 |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | ワイパーのように光が振れる。 |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | 光点が尾を引いて走る。 |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | オーロラの帯が揺らめく。 |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | 粒子が流れていく。 |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | スキャナーが左右に走る。 |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | 灯台のように光線が回る。 |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Fireworks | 花火が打ち上がる。 |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Rain | 雨が降る。 |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | テトリスのブロックが落ちて積まれる。 |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Fire Flicker | 炎が揺らめき立ち上る。 |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Gradient | 移り変わるグラデーション。 |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | 進捗バーが満ちる。 |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | ボールが跳ね回る。 |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | 妖精の光がきらめく。 |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | 2つの点が互いを巡る。 |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | 妖精の光がきらめく。 |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | 人影が走る。 |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | 画像が再生される。 |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | 光点が尾を引いて走る。 |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | ワイパーが払う。 |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | 色が現れては消える。 |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Lightning | 稲妻が走る。 |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | 瞳が動いて見渡す。 |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | 彗星が尾を引いて走る。 |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | スキャナーが左右に走る。 |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | 粒子が流れていく。 |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | 色の波がストリップを進む。 |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | 全体が色相を巡る。 |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | ボールが跳ね回る。 |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | 全体が色相を巡る。 |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | 炎が揺らめき立ち上る。 |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | 多彩な色の帯。 |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | 拍ごとに脈打つ。 |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | 単一の安定した色。 |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | ランダムにきらめく。 |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | ランダムにきらめく。 |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | ランダムにきらめく。 |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | ランダムにきらめく。 |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | 星がまたたく。 |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lake | 水面に波紋が広がる。 |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteor | 彗星が尾を引いて走る。 |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | 色の波がストリップを進む。 |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | 光点が尾を引いて走る。 |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | 水面に波紋が広がる。 |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | 星がまたたく。 |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | 星がまたたく。 |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | 暗闇で一対の目がまばたく。 |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | 単一の安定した色。 |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | 単一の安定した色。 |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | 斑点が現れては消える。 |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | 斑点が現れては消える。 |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Glitter | 色の上にグリッターが輝く。 |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Candle | ろうそくの炎が揺らめく。 |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | 花火が打ち上がる。 |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | 花火が打ち上がる。 |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | ボールが跳ね回る。 |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | 彗星が尾を引いて走る。 |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | 彗星が尾を引いて走る。 |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | 彗星が尾を引いて走る。 |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | ポップコーンが弾ける。 |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | しずくが一つずつ落ちる。 |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | 色の塊が形を変える。 |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | バーが所定の量まで満ちる。 |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | 虹の弧が巡る。 |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Heartbeat | 心臓が鼓動する。 |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | 水面に波紋が広がる。 |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | ろうそくの炎が揺らめく。 |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | 色の上にグリッターが輝く。 |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Sunrise | 太陽が昇る。 |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | 重なる正弦波がずれていく。 |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | 星がまたたく。 |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | ランダムにきらめく。 |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | 明るさが膨らんでは沈む。 |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | 重なる正弦波がずれていく。 |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | 粒子が流れていく。 |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | 鳥の群れが飛び去る。 |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | 人影が踊る。 |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | 車輪が回る。 |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | 車輪が回る。 |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | 移り変わるグラデーション。 |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | テレビの砂嵐がちらつく。 |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | 色ブロックがランダムに変わる。 |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | 宇宙船が滑るように進む。 |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | ミツバチが群れで飛び回る。 |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | 幽霊が漂う。 |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | 色の塊が形を変える。 |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | 文字のようにブロックが流れる。 |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | 渦が外へと巻いていく。 |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | 色の波がストリップを進む。 |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | シャボン玉が漂う。 |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | タコが触手を振る。 |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | 色の波がストリップを進む。 |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | マトリックス風にコードが降る。 |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | マトリックス風にコードが降る。 |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | ボールが跳ね回る。 |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | マトリックス風にコードが降る。 |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | ボールが跳ね回る。 |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | 色の塊が形を変える。 |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | 雨が降る。 |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | ランダムにきらめく。 |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | ランダムにきらめく。 |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | 水面に波紋が広がる。 |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | マトリックス風にコードが降る。 |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | 水面に波紋が広がる。 |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Waterfall | 雨が降る。 |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | マトリックス風にコードが降る。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを進む。 |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | 炎が揺らめき立ち上る。 |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | 雨が降る。 |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | ランダムにきらめく。 |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | ランダムにきらめく。 |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | 色の波がストリップを進む。 |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | 水面に波紋が広がる。 |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | 炎が揺らめき立ち上る。 |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | 渦が外へと巻いていく。 |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | パックマンが食べ進む。 |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | 2本の鎖が二重らせんになる。 |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrix | マトリックス風にコードが降る。 |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | ボールが跳ね回る。 |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | 水面に波紋が広がる。 |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | ボールが跳ね回る。 |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | ボールが跳ね回る。 |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | ボールが跳ね回る。 |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | ターンテーブルが回る。 |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | 色の波がストリップを進む。 |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | 色の波がストリップを進む。 |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | 明るさが膨らんでは沈む。 |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | 色の波がストリップを進む。 |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | 渦が外へと巻いていく。 |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | 色の波がストリップを進む。 |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | 太陽が回転する光線を放つ。 |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | 太陽が回転する光線を放つ。 |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | ジュリア集合のフラクタルが変形する。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを進む。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを進む。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色の波がストリップを進む。 |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | 格子上でセルが生と死を繰り返す。 |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | スコットランドのタータン。 |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | オーロラの帯が揺らめく。 |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | 渦が外へと巻いていく。 |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | リサージュ曲線が変形する。 |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | 回転する幾何学模様。 |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | ボールが跳ね回る。 |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | 粒子が流れていく。 |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | 色の波がストリップを進む。 |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | 渦が外へと巻いていく。 |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | 2本の鎖が二重らせんになる。 |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | 輪が暗い核へと崩れ落ちる。 |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | 色の波がストリップを進む。 |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | 音符が流れていく。 |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | WLEDのマスコット、Akemiが現れる。 |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | 炎が揺らめき立ち上る。 |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | 炎が揺らめき立ち上る。 |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | 花火が打ち上がる。 |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | 渦が外へと巻いていく。 |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | ランダムにきらめく。 |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | ボールが跳ね回る。 |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | 色の波がストリップを進む。 |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | 色の波がストリップを進む。 |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | 衝撃波の輪が広がる。 |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | 雨が降る。 |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | 色の波がストリップを進む。 |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | 水面に波紋が広がる。 |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | 水面に波紋が広がる。 |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | 幽霊が漂う。 |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | 色の塊が形を変える。 |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | しずくが一つずつ落ちる。 |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | ボールが跳ね回る。 |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | 人影が踊る。 |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | 花火が打ち上がる。 |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | ランダムにきらめく。 |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | 砂時計の砂が落ちる。 |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | 色の波がストリップを進む。 |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | 色の波がストリップを進む。 |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | 光点が尾を引いて走る。 |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | 星がまたたく。 |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | 水面に波紋が広がる。 |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | 炎が揺らめき立ち上る。 |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | 粒子が流れていく。 |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | 衝撃波の輪が広がる。 |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | 色の波がストリップを進む。 |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | 星が渦を巻く。 |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | 色の塊が形を変える。 |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | 色の波がストリップを進む。 |
