# WLED 효과

[팔레트](palettes.md) · **효과** · [컨트롤](controls.md) · [야간등](nightlight.md) · [세그먼트](segment.md) · [버튼](buttons.md) · [버튼 이벤트](button-events.md) · [프리셋](presets.md) · [슬라이더](fxdata.md) · [정보 항목](info.md) · [UI 라벨](ui.md) &nbsp;•&nbsp; [한국어 참조](README.md)

<sub>다른 언어: [EN](../en/effects.md) · [FR](../fr/effects.md) · [DE](../de/effects.md) · [ES](../es/effects.md) · [IT](../it/effects.md) · [JA](../ja/effects.md) · [ZH](../zh/effects.md)</sub>

**효과**는 WLED의 애니메이션 패턴. **효과** 탭에서 선택(`seg.fx`, 목록 `/json/eff`). 효과는 *움직임*, 팔레트는 *색*.

| 이미지 | WLED 이름 | 번역 | 설명 |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Solid | 단색의 고정 색상. |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Blink | 선명한 깜빡임 — 눈처럼. |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Breathe | 밝기가 부풀었다 잦아든다. |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Wipe | 와이퍼 팔이 쓸어낸다. |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Wipe Random | 와이퍼 팔이 쓸어낸다. |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Random Colors | 색 블록이 무작위로 바뀐다. |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Sweep | 와이퍼처럼 빛이 쓸어낸다. |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamic | 색 블록이 무작위로 바뀐다. |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Colorloop | 전체가 색상을 순환한다. |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Rainbow | 무지개 호가 순환한다. |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scan | 스캐너가 좌우로 훑는다. |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scan Dual | 스캐너가 좌우로 훑는다. |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Fade | 색이 나타났다 사라진다. |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Theater | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Theater Rainbow | 무지개 호가 순환한다. |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Running | 인물이 달린다. |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Saw | 톱이 오간다. |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Twinkle | 별이 반짝인다. |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolve | 무작위로 반짝인다. |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolve Rnd | 무작위로 반짝인다. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Sparkle | 무작위로 반짝인다. |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Sparkle Dark | 무작위로 반짝인다. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Sparkle+ | 무작위로 반짝인다. |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Strobe | 강한 스트로브 점멸. |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobe Rainbow | 무지개 호가 순환한다. |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobe Mega | 강한 스트로브 점멸. |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Blink Rainbow | 무지개 호가 순환한다. |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | 스캐너가 좌우로 훑는다. |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Chase | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Chase Random | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Chase Rainbow | 무지개 호가 순환한다. |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Chase Flash | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Rainbow Runner | 무지개 호가 순환한다. |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Colorful | 여러 색의 띠. |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Traffic Light | 신호등이 바뀐다. |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Sweep Random | 와이퍼처럼 빛이 쓸어낸다. |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Chase 2 | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurora | 오로라 띠가 일렁인다. |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Stream | 입자가 흘러간다. |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | 스캐너가 좌우로 훑는다. |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Lighthouse | 등대처럼 빛줄기가 돈다. |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Fireworks | 불꽃놀이가 터진다. |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Rain | 비가 내린다. |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetrix | 테트리스 블록이 떨어져 쌓인다. |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Fire Flicker | 불꽃이 일렁이며 오른다. |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Gradient | 흐르는 색상 그라데이션. |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Loading | 진행 막대가 채워진다. |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Rolling Balls | 공이 튀어 오른다. |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fairy | 요정 불빛이 반짝인다. |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Two Dots | 두 점이 서로 돈다. |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Fairytwinkle | 요정 불빛이 반짝인다. |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Running Dual | 인물이 달린다. |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Chase 3 | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Tri Wipe | 와이퍼 팔이 쓸어낸다. |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Tri Fade | 색이 나타났다 사라진다. |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Lightning | 번개가 친다. |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | 눈이 두리번거린다. |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi Comet | 혜성이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner Dual | 스캐너가 좌우로 훑는다. |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Stream 2 | 입자가 흘러간다. |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillate | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | 전체가 색상을 순환한다. |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Juggle | 공이 튀어 오른다. |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | 전체가 색상을 순환한다. |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Fire 2012 | 불꽃이 일렁이며 오른다. |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Colorwaves | 여러 색의 띠. |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | 박자마다 맥동한다. |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Fill Noise | 단색의 고정 색상. |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | 무작위로 반짝인다. |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | 무작위로 반짝인다. |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | 무작위로 반짝인다. |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | 무작위로 반짝인다. |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | 별이 반짝인다. |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lake | 물결이 퍼진다. |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Meteor | 혜성이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copy Segment | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Railway | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ripple | 물결이 퍼진다. |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Twinklefox | 별이 반짝인다. |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | 별이 반짝인다. |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Halloween Eyes | 눈이 두리번거린다. |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Solid Pattern | 단색의 고정 색상. |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Solid Pattern Tri | 단색의 고정 색상. |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Spots | 반점이 나타났다 사라진다. |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Spots Fade | 반점이 나타났다 사라진다. |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Glitter | 색 위로 반짝이가 빛난다. |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Candle | 촛불이 일렁인다. |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Fireworks Starburst | 불꽃놀이가 터진다. |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Fireworks 1D | 불꽃놀이가 터진다. |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Bouncing Balls | 공이 튀어 오른다. |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | 혜성이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | 혜성이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | 혜성이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | 팝콘이 튀어 오른다. |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Drip | 물방울이 하나씩 떨어진다. |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | 색 덩어리가 일렁인다. |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Percent | 막대가 설정 수준까지 찬다. |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ripple Rainbow | 무지개 호가 순환한다. |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Heartbeat | 심장이 뛴다. |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | 물결이 퍼진다. |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Candle Multi | 촛불이 일렁인다. |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Solid Glitter | 색 위로 반짝이가 빛난다. |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Sunrise | 해가 뜬다. |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Phased | 겹친 사인파가 어긋난다. |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Twinkleup | 별이 반짝인다. |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Noise Pal | 무작위로 반짝인다. |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sine | 밝기가 부풀었다 잦아든다. |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | 겹친 사인파가 어긋난다. |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flow | 입자가 흘러간다. |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | 새 떼가 가로질러 난다. |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Dancing Shadows | 인물이 춤춘다. |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Washing Machine | 바퀴가 돈다. |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | 바퀴가 돈다. |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Blends | 밝기가 부풀었다 잦아든다. |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | TV Simulator | TV 노이즈가 깜빡인다. |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamic Smooth | 색 블록이 무작위로 바뀐다. |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Spaceships | 우주선이 미끄러진다. |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Crazy Bees | 벌들이 떼지어 붕붕거린다. |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Ghost Rider | 유령이 떠다닌다. |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Blobs | 색 덩어리가 일렁인다. |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Scrolling Text | 글자처럼 블록이 흐른다. |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Drift Rose | 별이 나선으로 돈다. |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Distortion Waves | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Soap | 색 덩어리가 일렁인다. |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Octopus | 문어가 촉수를 흔든다. |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Waving Cell | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | 매트릭스처럼 코드가 쏟아진다. |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Pixelwave | 매트릭스처럼 코드가 쏟아진다. |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | 공이 튀어 오른다. |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | 매트릭스처럼 코드가 쏟아진다. |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | 공이 튀어 오른다. |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | 색 덩어리가 일렁인다. |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | 비가 내린다. |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | 무작위로 반짝인다. |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | 무작위로 반짝인다. |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | 물결이 퍼진다. |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | 매트릭스처럼 코드가 쏟아진다. |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | 물결이 퍼진다. |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Waterfall | 비가 내린다. |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | 매트릭스처럼 코드가 쏟아진다. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | 불꽃이 일렁이며 오른다. |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | 비가 내린다. |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | 무작위로 반짝인다. |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | 무작위로 반짝인다. |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | 물결이 퍼진다. |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | 불꽃이 일렁이며 오른다. |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | 별이 나선으로 돈다. |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | PacMan | 팩맨이 갉아먹으며 나아간다. |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | 두 가닥이 이중 나선을 이룬다. |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrix | 매트릭스처럼 코드가 쏟아진다. |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | 공이 튀어 오른다. |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | 물결이 퍼진다. |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | 공이 튀어 오른다. |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | 공이 튀어 오른다. |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | 공이 튀어 오른다. |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | DJ Light | 턴테이블이 돈다. |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Shimmer | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | 밝기가 부풀었다 잦아든다. |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Drift | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Sun Radiation | 해가 뜬다. |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Colored Bursts | 충격파 고리가 퍼진다. |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Game Of Life | 매트릭스처럼 코드가 쏟아진다. |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Polar Lights | 오로라 띠가 일렁인다. |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Swirl | 별이 나선으로 돈다. |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | 리사주 곡선이 변형된다. |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Plasma Ball | 공이 튀어 오른다. |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Flow Stripe | 입자가 흘러간다. |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | 두 가닥이 이중 나선을 이룬다. |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Black Hole | 고리가 어두운 핵으로 붕괴한다. |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | WLED 마스코트 Akemi가 나타난다. |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | 불꽃이 일렁이며 오른다. |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | 불꽃이 일렁이며 오른다. |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | 불꽃놀이가 터진다. |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | 별이 나선으로 돈다. |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | 무작위로 반짝인다. |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | 공이 튀어 오른다. |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | 충격파 고리가 퍼진다. |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | 비가 내린다. |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | 물결이 퍼진다. |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | 물결이 퍼진다. |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | 유령이 떠다닌다. |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | 색 덩어리가 일렁인다. |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | 물방울이 하나씩 떨어진다. |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | 공이 튀어 오른다. |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | 인물이 춤춘다. |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | 불꽃놀이가 터진다. |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | 무작위로 반짝인다. |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | 모래시계의 모래가 떨어진다. |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | 밝은 점이 꼬리를 끌며 지나간다. |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | 별이 반짝인다. |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | 물결이 퍼진다. |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | 불꽃이 일렁이며 오른다. |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | 입자가 흘러간다. |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | 충격파 고리가 퍼진다. |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | 색의 파도가 스트립을 따라 흐른다. |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | 별이 나선으로 돈다. |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Color Clouds | 색 덩어리가 일렁인다. |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Slow Transition | 색의 파도가 스트립을 따라 흐른다. |
