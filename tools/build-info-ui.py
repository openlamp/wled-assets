import json
DST="/Users/benoitbesson/dev/music/wled-assets"
LANGS=["en","fr","de","es","it","ja","ko","zh"]
def mk(items):  # items: {en_name:{lang:name, "_d":{lang:desc}}}
    out={}
    for en,d in items.items():
        e={}
        for lc in LANGS:
            e[lc]={"name":(en if lc=="en" else d.get(lc,en)),"desc":d.get("_d",{}).get(lc,d.get("_d",{}).get("en",""))}
        out[en]=e
    return out

# ---------- INFO / STATUS FIELDS (labels shown in WLED's Info panel) ----------
INFO={
"Uptime":{"fr":"Temps de fonctionnement","de":"Betriebszeit","es":"Tiempo activo","it":"Tempo di attività","ja":"稼働時間","ko":"가동 시간","zh":"运行时间","_d":{"en":"How long the device has been running since boot."}},
"Free memory":{"fr":"Mémoire libre","de":"Freier Speicher","es":"Memoria libre","it":"Memoria libera","ja":"空きメモリ","ko":"여유 메모리","zh":"可用内存","_d":{"en":"Free heap (RAM) on the controller."}},
"Signal strength":{"fr":"Force du signal","de":"Signalstärke","es":"Intensidad de señal","it":"Intensità del segnale","ja":"信号強度","ko":"신호 세기","zh":"信号强度","_d":{"en":"Wi-Fi signal quality."}},
"Frames per second":{"fr":"Images par seconde","de":"Bilder pro Sekunde","es":"Fotogramas por segundo","it":"Fotogrammi al secondo","ja":"フレーム毎秒","ko":"초당 프레임","zh":"每秒帧数","_d":{"en":"Effect refresh rate (FPS)."}},
"Estimated current":{"fr":"Courant estimé","de":"Geschätzter Strom","es":"Corriente estimada","it":"Corrente stimata","ja":"推定電流","ko":"예상 전류","zh":"估计电流","_d":{"en":"Estimated power draw of the LEDs."}},
"LED count":{"fr":"Nombre de LED","de":"LED-Anzahl","es":"Número de LED","it":"Numero di LED","ja":"LED数","ko":"LED 수","zh":"LED 数量","_d":{"en":"Total LEDs configured."}},
"Environment":{"fr":"Environnement","de":"Umgebung","es":"Entorno","it":"Ambiente","ja":"環境","ko":"환경","zh":"环境","_d":{"en":"Build/platform info (ESP variant, WLED version)."}},
"Filesystem":{"fr":"Système de fichiers","de":"Dateisystem","es":"Sistema de archivos","it":"File system","ja":"ファイルシステム","ko":"파일 시스템","zh":"文件系统","_d":{"en":"On-device storage usage."}},
"MAC address":{"fr":"Adresse MAC","de":"MAC-Adresse","es":"Dirección MAC","it":"Indirizzo MAC","ja":"MACアドレス","ko":"MAC 주소","zh":"MAC 地址","_d":{"en":"Hardware network address."}},
"IP address":{"fr":"Adresse IP","de":"IP-Adresse","es":"Dirección IP","it":"Indirizzo IP","ja":"IPアドレス","ko":"IP 주소","zh":"IP 地址","_d":{"en":"The device's network address."}},
"WiFi channel":{"fr":"Canal Wi-Fi","de":"WLAN-Kanal","es":"Canal Wi-Fi","it":"Canale Wi-Fi","ja":"Wi-Fiチャンネル","ko":"Wi-Fi 채널","zh":"Wi-Fi 信道","_d":{"en":"The Wi-Fi channel in use."}},
"Version":{"fr":"Version","de":"Version","es":"Versión","it":"Versione","ja":"バージョン","ko":"버전","zh":"版本","_d":{"en":"WLED firmware version."}},
}
json.dump({"_note":"Labels of the fields in WLED's Info panel (/json/info). Key = English label; per-language {name, desc}.","entries":mk(INFO)}, open(DST+"/i18n/info.json","w"),ensure_ascii=False,indent=1)

# ---------- CORE UI LABELS (the web-UI / app chrome: tabs, actions) ----------
UI={
"Colors":{"fr":"Couleurs","de":"Farben","es":"Colores","it":"Colori","ja":"色","ko":"색","zh":"颜色"},
"Effects":{"fr":"Effets","de":"Effekte","es":"Efectos","it":"Effetti","ja":"エフェクト","ko":"효과","zh":"效果"},
"Segments":{"fr":"Segments","de":"Segmente","es":"Segmentos","it":"Segmenti","ja":"セグメント","ko":"세그먼트","zh":"段"},
"Presets":{"fr":"Préréglages","de":"Voreinstellungen","es":"Ajustes","it":"Preset","ja":"プリセット","ko":"프리셋","zh":"预设"},
"Settings":{"fr":"Réglages","de":"Einstellungen","es":"Ajustes","it":"Impostazioni","ja":"設定","ko":"설정","zh":"设置"},
"Info":{"fr":"Infos","de":"Info","es":"Información","it":"Info","ja":"情報","ko":"정보","zh":"信息"},
"Brightness":{"fr":"Luminosité","de":"Helligkeit","es":"Brillo","it":"Luminosità","ja":"明るさ","ko":"밝기","zh":"亮度"},
"Save":{"fr":"Enregistrer","de":"Speichern","es":"Guardar","it":"Salva","ja":"保存","ko":"저장","zh":"保存"},
"Delete":{"fr":"Supprimer","de":"Löschen","es":"Eliminar","it":"Elimina","ja":"削除","ko":"삭제","zh":"删除"},
"Rename":{"fr":"Renommer","de":"Umbenennen","es":"Renombrar","it":"Rinomina","ja":"名前変更","ko":"이름 변경","zh":"重命名"},
"Add segment":{"fr":"Ajouter un segment","de":"Segment hinzufügen","es":"Añadir segmento","it":"Aggiungi segmento","ja":"セグメント追加","ko":"세그먼트 추가","zh":"添加段"},
"Duplicate":{"fr":"Dupliquer","de":"Duplizieren","es":"Duplicar","it":"Duplica","ja":"複製","ko":"복제","zh":"复制"},
"Reset":{"fr":"Réinitialiser","de":"Zurücksetzen","es":"Restablecer","it":"Reimposta","ja":"リセット","ko":"초기화","zh":"重置"},
"Apply":{"fr":"Appliquer","de":"Anwenden","es":"Aplicar","it":"Applica","ja":"適用","ko":"적용","zh":"应用"},
"Timer":{"fr":"Minuteur","de":"Timer","es":"Temporizador","it":"Timer","ja":"タイマー","ko":"타이머","zh":"定时器"},
"Sync":{"fr":"Synchronisation","de":"Synchronisierung","es":"Sincronización","it":"Sincronizzazione","ja":"同期","ko":"동기화","zh":"同步"},
"Live":{"fr":"En direct","de":"Live","es":"En vivo","it":"Live","ja":"ライブ","ko":"라이브","zh":"实时"},
"Peek":{"fr":"Aperçu","de":"Vorschau","es":"Vista previa","it":"Anteprima","ja":"プレビュー","ko":"미리보기","zh":"预览"},
"Reboot":{"fr":"Redémarrer","de":"Neu starten","es":"Reiniciar","it":"Riavvia","ja":"再起動","ko":"재부팅","zh":"重启"},
"Discover devices":{"fr":"Découvrir les appareils","de":"Geräte suchen","es":"Descubrir dispositivos","it":"Trova dispositivi","ja":"デバイス検出","ko":"장치 검색","zh":"发现设备"},
}
json.dump({"_note":"Core WLED web-UI / app labels (tabs, actions). Key = English label; per-language {name, desc}. Extensible — add strings as they are identified.","entries":mk(UI)}, open(DST+"/i18n/ui.json","w"),ensure_ascii=False,indent=1)
print("info.json (%d) + ui.json (%d)"%(len(INFO),len(UI)))
