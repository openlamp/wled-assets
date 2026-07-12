# WLED ボタンイベント

[パレット](palettes.md) · [エフェクト](effects.md) · [コントロール](controls.md) · [ナイトライト](nightlight.md) · [セグメント](segment.md) · [ボタン](buttons.md) · **ボタンイベント** · [プリセット](presets.md) · [スライダー](fxdata.md) · [情報項目](info.md) · [UIラベル](ui.md) &nbsp;•&nbsp; [日本語リファレンス](README.md)

<sub>他の言語: [EN](../en/button-events.md) · [FR](../fr/button-events.md) · [DE](../de/button-events.md) · [ES](../es/button-events.md) · [IT](../it/button-events.md) · [KO](../ko/button-events.md) · [ZH](../zh/button-events.md)</sub>

**ボタンイベント**は物理ボタンが*いつ*発火するか——短押し・長押し・ダブル押し。WLEDは各イベントに**プリセット/動作**を割当(`btn[].macros`、設定→LEDとハードウェア)。

| 画像 | WLED名 | 翻訳 | 説明 |
|---|---|---|---|
| <img src="../../images/button-events/short-press.png" width="56"> | `Short press` | 短押し | 素早く押して離す——ボタンの短押し動作(`btn[].macros[0]`)。 |
| <img src="../../images/button-events/long-press.png" width="56"> | `Long press` | 長押し | 押し続ける——長押し動作(`btn[].macros[1]`)。既定では明るさを変更。 |
| <img src="../../images/button-events/double-press.png" width="56"> | `Double press` | ダブル押し | 素早く2回押す——ダブル押し動作(`btn[].macros[2]`)。 |
