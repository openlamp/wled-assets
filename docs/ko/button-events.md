# WLED 버튼 이벤트

[팔레트](palettes.md) · [효과](effects.md) · [컨트롤](controls.md) · [야간등](nightlight.md) · [세그먼트](segment.md) · [버튼](buttons.md) · **버튼 이벤트** · [프리셋](presets.md) · [슬라이더](fxdata.md) · [정보 항목](info.md) · [UI 라벨](ui.md) &nbsp;•&nbsp; [한국어 참조](README.md)

<sub>다른 언어: [EN](../en/button-events.md) · [FR](../fr/button-events.md) · [DE](../de/button-events.md) · [ES](../es/button-events.md) · [IT](../it/button-events.md) · [JA](../ja/button-events.md) · [ZH](../zh/button-events.md)</sub>

**버튼 이벤트**는 물리 버튼이 *언제* 작동하는지——짧게/길게/두 번 누름. WLED는 각 이벤트에 **프리셋/동작**을 매핑(`btn[].macros`, 설정 → LED 및 하드웨어).

| 이미지 | WLED 이름 | 번역 | 설명 |
|---|---|---|---|
| <img src="../../images/button-events/short-press.png" width="56"> | `Short press` | 짧게 누름 | 빠르게 눌렀다 뗌——버튼의 짧게 누름 동작(`btn[].macros[0]`). |
| <img src="../../images/button-events/long-press.png" width="56"> | `Long press` | 길게 누름 | 길게 누름——길게 누름 동작(`btn[].macros[1]`). 기본은 밝기 조절. |
| <img src="../../images/button-events/double-press.png" width="56"> | `Double press` | 두 번 누름 | 빠르게 두 번 누름——두 번 누름 동작(`btn[].macros[2]`). |
