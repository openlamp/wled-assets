import json, re
SP="/private/tmp/claude-501/-Users-benoitbesson-dev-music/b1b0bf2c-2a0b-4a74-83ae-5717d879ef61/scratchpad"
DST="/Users/benoitbesson/dev/music/wled-assets"
LANGS=["en","fr","de","es","it","ja","ko","zh"]
def entry(name,desc_map,tr):
    e={"en":{"name":name,"desc":desc_map["en"]}}
    for lc in LANGS[1:]:
        e[lc]={"name":tr.get(lc,(name,))[0],"desc":desc_map.get(lc,desc_map["en"])}
    return e

# ---------- SEGMENT ACTIONS ----------
SEG={
"Reverse":{"d":{"en":"Play the effect in the opposite direction along the segment.","fr":"Jouer l'effet dans le sens inverse le long du segment.","de":"Den Effekt in umgekehrter Richtung abspielen.","es":"Reproducir el efecto en sentido inverso.","it":"Riprodurre l'effetto in direzione opposta.","ja":"効果をセグメント上で逆方向に再生。","ko":"효과를 세그먼트에서 반대 방향으로 재생.","zh":"沿段以相反方向播放效果。"},"t":{"fr":("Inverser",),"de":("Umkehren",),"es":("Invertir",),"it":("Inverti",),"ja":("反転",),"ko":("반전",),"zh":("反向",)}},
"Mirror":{"d":{"en":"Split the segment and mirror the effect from the centre.","fr":"Couper le segment et refléter l'effet depuis le centre.","de":"Segment teilen und den Effekt von der Mitte spiegeln.","es":"Dividir el segmento y reflejar el efecto desde el centro.","it":"Dividere il segmento e specchiare l'effetto dal centro.","ja":"セグメントを分割し中央から鏡像化。","ko":"세그먼트를 나눠 중앙에서 대칭.","zh":"分割段并从中心镜像效果。"},"t":{"fr":("Miroir",),"de":("Spiegeln",),"es":("Espejo",),"it":("Specchia",),"ja":("ミラー",),"ko":("미러",),"zh":("镜像",)}},
"Freeze":{"d":{"en":"Pause the effect on the current frame.","fr":"Figer l'effet sur l'image courante.","de":"Den Effekt im aktuellen Bild anhalten.","es":"Congelar el efecto en el fotograma actual.","it":"Bloccare l'effetto sul fotogramma corrente.","ja":"現在のフレームで効果を停止。","ko":"현재 프레임에서 효과 정지.","zh":"在当前帧冻结效果。"},"t":{"fr":("Figer",),"de":("Einfrieren",),"es":("Congelar",),"it":("Congela",),"ja":("フリーズ",),"ko":("정지",),"zh":("冻结",)}},
"On/Off":{"d":{"en":"Turn the segment on or off.","fr":"Allumer ou éteindre le segment.","de":"Segment ein- oder ausschalten.","es":"Encender o apagar el segmento.","it":"Accendere o spegnere il segmento.","ja":"セグメントのオン/オフ。","ko":"세그먼트 켜기/끄기.","zh":"打开或关闭该段。"},"t":{"fr":("Marche/Arrêt",),"de":("Ein/Aus",),"es":("Encendido/Apagado",),"it":("Acceso/Spento",),"ja":("オン/オフ",),"ko":("켜기/끄기",),"zh":("开/关",)}},
"Transition":{"d":{"en":"Crossfade time when switching state or preset.","fr":"Durée du fondu enchaîné lors d'un changement d'état ou de preset.","de":"Überblendzeit beim Wechsel von Zustand oder Preset.","es":"Tiempo de fundido al cambiar de estado o preset.","it":"Tempo di dissolvenza al cambio di stato o preset.","ja":"状態/プリセット切替時のクロスフェード時間。","ko":"상태/프리셋 전환 시 크로스페이드 시간.","zh":"切换状态或预设时的交叉淡入时长。"},"t":{"fr":("Transition",),"de":("Übergang",),"es":("Transición",),"it":("Transizione",),"ja":("トランジション",),"ko":("전환",),"zh":("过渡",)}},
"Sound sim":{"d":{"en":"Audio-simulation mode when no live audio is present.","fr":"Mode simulation audio quand il n'y a pas de son en direct.","de":"Audio-Simulationsmodus ohne Live-Ton.","es":"Modo de simulación de audio sin sonido en vivo.","it":"Modalità simulazione audio senza audio dal vivo.","ja":"ライブ音声がない時の音声シミュレーション。","ko":"실시간 오디오가 없을 때 오디오 시뮬레이션.","zh":"无实时音频时的音频模拟模式。"},"t":{"fr":("Simu audio",),"de":("Audio-Simulation",),"es":("Simulación de audio",),"it":("Simulazione audio",),"ja":("音声シミュ",),"ko":("오디오 시뮬",),"zh":("音频模拟",)}},
}
seg={k:entry(k,v["d"],v["t"]) for k,v in SEG.items()}
json.dump({"_note":"WLED segment actions/toggles (seg.rev, seg.mi, seg.frz, seg.on, transition, seg.si). Key = English name; per-language {name, desc}.","entries":seg}, open(DST+"/i18n/segment.json","w"),ensure_ascii=False,indent=1)

# ---------- BUTTON TYPES ----------
BTN={
"Push":{"fr":"Poussoir","de":"Taster","es":"Pulsador","it":"Pulsante","ja":"プッシュ","ko":"푸시","zh":"按钮"},
"Push inverted":{"fr":"Poussoir inversé","de":"Taster invertiert","es":"Pulsador invertido","it":"Pulsante invertito","ja":"プッシュ(反転)","ko":"푸시(반전)","zh":"按钮(反相)"},
"Switch":{"fr":"Interrupteur","de":"Schalter","es":"Interruptor","it":"Interruttore","ja":"スイッチ","ko":"스위치","zh":"开关"},
"PIR sensor":{"fr":"Capteur PIR","de":"PIR-Sensor","es":"Sensor PIR","it":"Sensore PIR","ja":"PIRセンサー","ko":"PIR 센서","zh":"PIR 传感器"},
"Touch":{"fr":"Tactile","de":"Touch","es":"Táctil","it":"Tattile","ja":"タッチ","ko":"터치","zh":"触摸"},
"Analog":{"fr":"Analogique","de":"Analog","es":"Analógico","it":"Analogico","ja":"アナログ","ko":"아날로그","zh":"模拟"},
}
def desc_btn(nm): return {lc:("How the physical button/input is wired." if lc=="en" else {"fr":"Comment l'entrée/le bouton physique est câblé.","de":"Wie der physische Taster/Eingang verdrahtet ist.","es":"Cómo está cableado el botón/entrada físico.","it":"Come è cablato il pulsante/ingresso fisico.","ja":"物理ボタン/入力の配線方式。","ko":"물리 버튼/입력의 배선 방식.","zh":"物理按钮/输入的接线方式。"}[lc]) for lc in LANGS}
btn={}
for nm,tr in BTN.items():
    e={"en":{"name":nm,"desc":desc_btn(nm)["en"]}}
    for lc in LANGS[1:]: e[lc]={"name":tr[lc],"desc":desc_btn(nm)[lc]}
    btn[nm]=e
json.dump({"_note":"WLED button/input types (settings). Key = English name; per-language {name, desc}.","entries":btn}, open(DST+"/i18n/buttons.json","w"),ensure_ascii=False,indent=1)
print("segment.json (%d) + buttons.json (%d)"%(len(seg),len(btn)))
