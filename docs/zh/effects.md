# WLED 效果

[调色板](palettes.md) · **效果** · [控件](controls.md) · [夜灯](nightlight.md) · [段](segment.md) · [按钮](buttons.md) · [按钮事件](button-events.md) · [预设](presets.md) · [滑块](fxdata.md) · [信息字段](info.md) · [界面标签](ui.md) &nbsp;•&nbsp; [中文参考](README.md)

<sub>其他语言: [EN](../en/effects.md) · [FR](../fr/effects.md) · [DE](../de/effects.md) · [ES](../es/effects.md) · [IT](../it/effects.md) · [JA](../ja/effects.md) · [KO](../ko/effects.md)</sub>

**效果**是 WLED 的动画图案，在**效果**标签选择（`seg.fx`，列表 `/json/eff`）。效果决定*运动*，调色板决定*颜色*。

| 图片 | WLED 名称 | 翻译 | 描述 |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Solid | 单一稳定的颜色。 |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Blink | 干脆的开关闪烁——像眨眼。 |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Breathe | 亮度渐强又渐弱。 |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Wipe | 雨刷臂扫过。 |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | 雨刷臂扫过。 |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | 色块随机变换。 |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | 光束如雨刷般摆动。 |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | 色块随机变换。 |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | 整条灯带循环变色。 |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Rainbow | 彩虹弧流转。 |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | 扫描光左右往返。 |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | 扫描光左右往返。 |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Fade | 颜色渐显渐隐。 |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | 彩虹弧流转。 |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | 人影奔跑。 |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | 锯子来回切割。 |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Twinkle | 星星闪烁。 |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | 随机闪光。 |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | 随机闪光。 |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Sparkle | 随机闪光。 |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | 随机闪光。 |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | 随机闪光。 |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Strobe | 强烈频闪。 |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | 彩虹弧流转。 |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | 强烈频闪。 |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | 彩虹弧流转。 |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | 扫描光左右往返。 |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Chase | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | 彩虹弧流转。 |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | 彩虹弧流转。 |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | 多彩的色带。 |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | 红绿灯变换。 |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | 光束如雨刷般摆动。 |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | 极光带状光影摇曳。 |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | 粒子流动而过。 |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | 扫描光左右往返。 |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | 光束如灯塔旋转。 |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Fireworks | 烟花绽放。 |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Rain | 雨落下。 |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | 俄罗斯方块落下堆叠。 |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Fire Flicker | 火焰摇曳升腾。 |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Gradient | 流动的颜色渐变。 |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | 进度条填满。 |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | 小球上下弹跳。 |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | 仙灯闪烁。 |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | 两点相互环绕。 |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | 仙灯闪烁。 |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | 人影奔跑。 |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | 色波沿灯带流动。 |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | 雨刷臂扫过。 |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | 颜色渐显渐隐。 |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Lightning | 闪电劈下。 |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | 眼睛四处张望。 |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | 彗星拖尾划过。 |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | 扫描光左右往返。 |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | 粒子流动而过。 |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | 色波沿灯带流动。 |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | 整条灯带循环变色。 |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | 小球上下弹跳。 |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | 整条灯带循环变色。 |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | 火焰摇曳升腾。 |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | 多彩的色带。 |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | 随每一拍脉动。 |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | 单一稳定的颜色。 |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | 随机闪光。 |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | 随机闪光。 |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | 随机闪光。 |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | 随机闪光。 |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | 星星闪烁。 |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lake | 水面涟漪扩散。 |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteor | 彗星拖尾划过。 |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | 色波沿灯带流动。 |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | 水面涟漪扩散。 |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | 星星闪烁。 |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | 星星闪烁。 |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | 眼睛四处张望。 |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | 单一稳定的颜色。 |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | 单一稳定的颜色。 |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | 光斑忽隐忽现。 |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | 光斑忽隐忽现。 |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Glitter | 色彩上闪着亮片。 |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Candle | 烛火摇曳。 |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | 烟花绽放。 |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | 烟花绽放。 |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | 小球上下弹跳。 |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | 彗星拖尾划过。 |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | 彗星拖尾划过。 |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | 彗星拖尾划过。 |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | 爆米花蹦起。 |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | 水滴逐一落下。 |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | 色团流变漂移。 |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | 进度条填至设定值。 |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | 彩虹弧流转。 |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Heartbeat | 心脏跳动。 |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | 水面涟漪扩散。 |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | 烛火摇曳。 |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | 色彩上闪着亮片。 |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Sunrise | 太阳升起。 |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | 层叠的正弦波错动。 |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | 星星闪烁。 |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | 随机闪光。 |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | 亮度渐强又渐弱。 |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | 层叠的正弦波错动。 |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | 粒子流动而过。 |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | 一群鸟飞过。 |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | 人影起舞。 |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | 轮子旋转。 |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | 轮子旋转。 |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | 亮度渐强又渐弱。 |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | 电视雪花闪烁。 |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | 色块随机变换。 |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | 飞船滑过。 |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | 蜜蜂成群嗡嗡飞舞。 |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | 幽灵飘过。 |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | 色团流变漂移。 |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | 色块如文字滚动。 |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | 星辰旋涡外扩。 |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | 色波沿灯带流动。 |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | 色团流变漂移。 |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | 章鱼舞动触手。 |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | 色波沿灯带流动。 |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | 代码如《黑客帝国》般落下。 |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | 代码如《黑客帝国》般落下。 |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | 小球上下弹跳。 |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | 代码如《黑客帝国》般落下。 |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | 小球上下弹跳。 |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | 色团流变漂移。 |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | 雨落下。 |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | 随机闪光。 |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | 随机闪光。 |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | 水面涟漪扩散。 |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | 代码如《黑客帝国》般落下。 |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | 水面涟漪扩散。 |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Waterfall | 雨落下。 |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | 代码如《黑客帝国》般落下。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色波沿灯带流动。 |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | 火焰摇曳升腾。 |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | 雨落下。 |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | 随机闪光。 |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | 随机闪光。 |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | 色波沿灯带流动。 |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | 水面涟漪扩散。 |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | 火焰摇曳升腾。 |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | 星辰旋涡外扩。 |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | 吃豆人一路吞食。 |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | 两条链交织成双螺旋。 |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrix | 代码如《黑客帝国》般落下。 |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | 小球上下弹跳。 |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | 水面涟漪扩散。 |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | 小球上下弹跳。 |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | 小球上下弹跳。 |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | 小球上下弹跳。 |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | 唱盘旋转。 |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | 色波沿灯带流动。 |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | 色波沿灯带流动。 |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | 亮度渐强又渐弱。 |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | 色波沿灯带流动。 |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | 色波沿灯带流动。 |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | 色波沿灯带流动。 |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | 太阳升起。 |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | 冲击波环扩散。 |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | 色波沿灯带流动。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色波沿灯带流动。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色波沿灯带流动。 |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 色波沿灯带流动。 |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | 代码如《黑客帝国》般落下。 |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | 色波沿灯带流动。 |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | 极光带状光影摇曳。 |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | 星辰旋涡外扩。 |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | 李萨如曲线变形。 |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | 色波沿灯带流动。 |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | 小球上下弹跳。 |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | 粒子流动而过。 |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | 色波沿灯带流动。 |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | 色波沿灯带流动。 |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | 两条链交织成双螺旋。 |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | 光环塌缩入黑暗核心。 |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | 色波沿灯带流动。 |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | 色波沿灯带流动。 |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | WLED 吉祥物 Akemi 出现。 |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | 火焰摇曳升腾。 |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | 火焰摇曳升腾。 |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | 烟花绽放。 |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | 星辰旋涡外扩。 |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | 随机闪光。 |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | 小球上下弹跳。 |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | 色波沿灯带流动。 |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | 色波沿灯带流动。 |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | 冲击波环扩散。 |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | 雨落下。 |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | 色波沿灯带流动。 |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | 水面涟漪扩散。 |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | 水面涟漪扩散。 |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | 幽灵飘过。 |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | 色团流变漂移。 |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | 水滴逐一落下。 |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | 小球上下弹跳。 |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | 人影起舞。 |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | 烟花绽放。 |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | 随机闪光。 |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | 沙漏中沙粒落下。 |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | 色波沿灯带流动。 |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | 色波沿灯带流动。 |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | 亮点拖着尾巴掠过。 |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | 星星闪烁。 |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | 水面涟漪扩散。 |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | 火焰摇曳升腾。 |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | 粒子流动而过。 |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | 冲击波环扩散。 |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | 色波沿灯带流动。 |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | 星辰旋涡外扩。 |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | 色团流变漂移。 |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | 色波沿灯带流动。 |
