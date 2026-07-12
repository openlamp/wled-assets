# WLED 프리셋

[팔레트](palettes.md) · [효과](effects.md) · [컨트롤](controls.md) · [야간등](nightlight.md) · [세그먼트](segment.md) · [버튼](buttons.md) · [버튼 이벤트](button-events.md) · **프리셋** · [슬라이더](fxdata.md) · [정보 항목](info.md) · [UI 라벨](ui.md) &nbsp;•&nbsp; [한국어 참조](README.md)

<sub>다른 언어: [EN](../en/presets.md) · [FR](../fr/presets.md) · [DE](../de/presets.md) · [ES](../es/presets.md) · [IT](../it/presets.md) · [JA](../ja/presets.md) · [ZH](../zh/presets.md)</sub>

**프리셋**은 전체 룩(또는 플레이리스트)을 저장해 한 번에 불러옴——**프리셋** 탭, 물리 버튼, 타이머, API(`ps`/`/presets.json`). 여기는 생성 시 *옵션 라벨*이며, 프리셋 **이름**은 사용자 것.

| 이미지 | WLED 이름 | 번역 | 설명 |
|---|---|---|---|
| <img src="../../images/presets/save-preset.png" width="56"> | `Save preset` | 프리셋 저장 | Store the current look as a numbered preset. |
| <img src="../../images/presets/preset-name.png" width="56"> | `Preset name` | 프리셋 이름 | The label a preset appears under. |
| <img src="../../images/presets/quick-load-label.png" width="56"> | `Quick load label` | 빠른 실행 라벨 | A 1-2 character tag (QLL) for the quick-select bar. |
| <img src="../../images/presets/include-brightness.png" width="56"> | `Include brightness` | 밝기 포함 | Whether recalling the preset also sets brightness. |
| <img src="../../images/presets/save-segment-bounds.png" width="56"> | `Save segment bounds` | 세그먼트 범위 저장 | Store each segment's start/stop, not just its style. |
| <img src="../../images/presets/use-current-state.png" width="56"> | `Use current state` | 현재 상태 사용 | Snapshot the live light state into the preset. |
| <img src="../../images/presets/api-command.png" width="56"> | `API command` | API 명령 | Store a raw HTTP/JSON API call instead of a state snapshot. |
| <img src="../../images/presets/playlist.png" width="56"> | `Playlist` | 재생목록 | A preset that cycles through other presets. |
| <img src="../../images/presets/duration.png" width="56"> | `Duration` | 지속 시간 | How long each playlist entry plays. |
| <img src="../../images/presets/transition.png" width="56"> | `Transition` | 전환 | Crossfade time between playlist entries. |
| <img src="../../images/presets/repeat.png" width="56"> | `Repeat` | 반복 | How many times the playlist loops (0 = forever). |
| <img src="../../images/presets/shuffle.png" width="56"> | `Shuffle` | 셔플 | Play the playlist entries in random order. |
| <img src="../../images/presets/end-preset.png" width="56"> | `End preset` | 종료 프리셋 | The preset to apply when the playlist finishes. |
