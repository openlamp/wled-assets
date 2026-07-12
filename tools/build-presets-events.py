import json
DST="/Users/benoitbesson/dev/music/wled-assets"
LANGS=["en","fr","de","es","it","ja","ko","zh"]
def mk(items):
    out={}
    for en,(tr,desc) in items.items():
        e={"en":{"name":en,"desc":desc.get("en","")}}
        for lc in LANGS[1:]: e[lc]={"name":tr.get(lc,en),"desc":desc.get(lc,desc.get("en",""))}
        out[en]=e
    return out

BE={  # WLED button EVENTS that trigger an action/preset
"Short press":({"fr":"Appui court","de":"Kurzer Druck","es":"Pulsación corta","it":"Pressione breve","ja":"短押し","ko":"짧게 누름","zh":"短按"},
 {"en":"A quick press-and-release. In WLED it fires the button's short-press action (`btn[].macros[0]`).","fr":"Un appui bref relâché aussitôt. Déclenche l'action d'appui court du bouton (`btn[].macros[0]`).","de":"Kurzes Drücken und Loslassen — löst die Kurz-Aktion der Taste aus (`btn[].macros[0]`).","es":"Pulsar y soltar rápido — dispara la acción de pulsación corta (`btn[].macros[0]`).","it":"Premi e rilascia rapido — attiva l'azione di pressione breve (`btn[].macros[0]`).","ja":"素早く押して離す——ボタンの短押し動作(`btn[].macros[0]`)。","ko":"빠르게 눌렀다 뗌——버튼의 짧게 누름 동작(`btn[].macros[0]`).","zh":"快速按下松开——触发按钮短按动作(`btn[].macros[0]`)。"}),
"Long press":({"fr":"Appui long","de":"Langer Druck","es":"Pulsación larga","it":"Pressione lunga","ja":"長押し","ko":"길게 누름","zh":"长按"},
 {"en":"Holding the button. Fires the long-press action (`btn[].macros[1]`); by default it changes brightness.","fr":"Bouton maintenu. Déclenche l'action d'appui long (`btn[].macros[1]`) ; par défaut règle la luminosité.","de":"Taste gehalten — löst die Lang-Aktion aus (`btn[].macros[1]`); ändert standardmäßig die Helligkeit.","es":"Botón mantenido — acción de pulsación larga (`btn[].macros[1]`); por defecto cambia el brillo.","it":"Pulsante tenuto — azione di pressione lunga (`btn[].macros[1]`); di default regola la luminosità.","ja":"押し続ける——長押し動作(`btn[].macros[1]`)。既定では明るさを変更。","ko":"길게 누름——길게 누름 동작(`btn[].macros[1]`). 기본은 밝기 조절.","zh":"按住不放——长按动作(`btn[].macros[1]`)；默认调节亮度。"}),
"Double press":({"fr":"Double appui","de":"Doppelter Druck","es":"Doble pulsación","it":"Doppia pressione","ja":"ダブル押し","ko":"두 번 누름","zh":"双按"},
 {"en":"Two quick presses. Fires the double-press action (`btn[].macros[2]`).","fr":"Deux appuis rapprochés. Déclenche l'action de double appui (`btn[].macros[2]`).","de":"Zwei schnelle Drücke — löst die Doppel-Aktion aus (`btn[].macros[2]`).","es":"Dos pulsaciones rápidas — acción de doble pulsación (`btn[].macros[2]`).","it":"Due pressioni rapide — azione di doppia pressione (`btn[].macros[2]`).","ja":"素早く2回押す——ダブル押し動作(`btn[].macros[2]`)。","ko":"빠르게 두 번 누름——두 번 누름 동작(`btn[].macros[2]`).","zh":"快速按两次——双按动作(`btn[].macros[2]`)。"}),
}
json.dump({"_note":"WLED button EVENT types — the trigger, not the wiring. Each fires a preset/action per btn[].macros. Key = English name; per-language {name, desc}.","entries":mk(BE)}, open(DST+"/i18n/button-events.json","w"),ensure_ascii=False,indent=1)

PR={  # preset / playlist OPTION labels (standard UI, NOT the user's preset names)
"Save preset":({"fr":"Enregistrer le preset","de":"Preset speichern","es":"Guardar preset","it":"Salva preset","ja":"プリセット保存","ko":"프리셋 저장","zh":"保存预设"},{"en":"Store the current look as a numbered preset."}),
"Preset name":({"fr":"Nom du preset","de":"Preset-Name","es":"Nombre del preset","it":"Nome del preset","ja":"プリセット名","ko":"프리셋 이름","zh":"预设名称"},{"en":"The label a preset appears under."}),
"Quick load label":({"fr":"Étiquette d'accès rapide","de":"Schnellzugriff-Kürzel","es":"Etiqueta de acceso rápido","it":"Etichetta accesso rapido","ja":"クイックロードラベル","ko":"빠른 실행 라벨","zh":"快速加载标签"},{"en":"A 1-2 character tag (QLL) for the quick-select bar."}),
"Include brightness":({"fr":"Inclure la luminosité","de":"Helligkeit einbeziehen","es":"Incluir brillo","it":"Includi luminosità","ja":"明るさを含める","ko":"밝기 포함","zh":"包含亮度"},{"en":"Whether recalling the preset also sets brightness."}),
"Save segment bounds":({"fr":"Enregistrer les bornes de segment","de":"Segmentgrenzen speichern","es":"Guardar límites de segmento","it":"Salva confini segmento","ja":"セグメント範囲を保存","ko":"세그먼트 범위 저장","zh":"保存段边界"},{"en":"Store each segment's start/stop, not just its style."}),
"Use current state":({"fr":"Utiliser l'état actuel","de":"Aktuellen Zustand verwenden","es":"Usar estado actual","it":"Usa stato attuale","ja":"現在の状態を使用","ko":"현재 상태 사용","zh":"使用当前状态"},{"en":"Snapshot the live light state into the preset."}),
"API command":({"fr":"Commande API","de":"API-Befehl","es":"Comando API","it":"Comando API","ja":"APIコマンド","ko":"API 명령","zh":"API 命令"},{"en":"Store a raw HTTP/JSON API call instead of a state snapshot."}),
"Playlist":({"fr":"Playlist","de":"Wiedergabeliste","es":"Lista de reproducción","it":"Playlist","ja":"プレイリスト","ko":"재생목록","zh":"播放列表"},{"en":"A preset that cycles through other presets."}),
"Duration":({"fr":"Durée","de":"Dauer","es":"Duración","it":"Durata","ja":"再生時間","ko":"지속 시간","zh":"时长"},{"en":"How long each playlist entry plays."}),
"Transition":({"fr":"Transition","de":"Übergang","es":"Transición","it":"Transizione","ja":"トランジション","ko":"전환","zh":"过渡"},{"en":"Crossfade time between playlist entries."}),
"Repeat":({"fr":"Répéter","de":"Wiederholen","es":"Repetir","it":"Ripeti","ja":"繰り返し","ko":"반복","zh":"重复"},{"en":"How many times the playlist loops (0 = forever)."}),
"Shuffle":({"fr":"Aléatoire","de":"Zufall","es":"Aleatorio","it":"Casuale","ja":"シャッフル","ko":"셔플","zh":"随机"},{"en":"Play the playlist entries in random order."}),
"End preset":({"fr":"Preset de fin","de":"End-Preset","es":"Preset final","it":"Preset finale","ja":"終了プリセット","ko":"종료 프리셋","zh":"结束预设"},{"en":"The preset to apply when the playlist finishes."}),
}
json.dump({"_note":"WLED preset & playlist OPTION labels — the standard UI for creating presets/playlists (NOT the user's own preset names, which are personal data). Key = English label; per-language {name, desc}.","entries":mk(PR)}, open(DST+"/i18n/presets.json","w"),ensure_ascii=False,indent=1)
print("button-events (%d) + presets (%d)"%(len(BE),len(PR)))
