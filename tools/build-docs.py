import json, os
DST="/Users/benoitbesson/dev/music/wled-assets"
SP="/private/tmp/claude-501/-Users-benoitbesson-dev-music/b1b0bf2c-2a0b-4a74-83ae-5717d879ef61/scratchpad"
def slug(n):
    import re; return re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')
data=json.load(open(SP+"/wled_data.json")); pal,eff=data["pal"],data["eff"]
PAL=json.load(open(DST+"/i18n/palettes.json"))["entries"]
EFF=json.load(open(DST+"/i18n/effects.json"))["entries"]
CTRL=json.load(open(DST+"/i18n/controls.json"))["entries"]
SEG=json.load(open(DST+"/i18n/segment.json"))["entries"]
BTN=json.load(open(DST+"/i18n/buttons.json"))["entries"]
FXL=json.load(open(DST+"/i18n/fxdata-labels.json"))["entries"]
COL=json.load(open(DST+"/i18n/colors.json")); COLE=COL["entries"]; RAT=COL["_rationale"]
NL=json.load(open(DST+"/i18n/nightlight.json"))["entries"]
LANGS=[("en","English","🇬🇧"),("fr","Français","🇫🇷"),("de","Deutsch","🇩🇪"),("es","Español","🇪🇸"),("it","Italiano","🇮🇹"),("ja","日本語","🇯🇵"),("ko","한국어","🇰🇷"),("zh","中文","🇨🇳")]
LC=[c for c,_,_ in LANGS]
UI={"en":{"pal":"Palettes","eff":"Effects","ctrl":"Controls","col":"Colours","nl":"Nightlight","seg":"Segment","btn":"Buttons","fx":"Effect sliders","name":"WLED name","tr":"Translation","desc":"Description","img":"Image","other":"Other languages","hex":"Hex","idx":"Reference in English","home":"↑ all languages"},
 "fr":{"pal":"Palettes","eff":"Effets","ctrl":"Contrôles","col":"Couleurs","nl":"Veilleuse","seg":"Segment","btn":"Boutons","fx":"Curseurs d'effet","name":"Nom WLED","tr":"Traduction","desc":"Description","img":"Image","other":"Autres langues","hex":"Hex","idx":"Référence en français","home":"↑ toutes les langues"},
 "de":{"pal":"Paletten","eff":"Effekte","ctrl":"Regler","col":"Farben","nl":"Nachtlicht","seg":"Segment","btn":"Tasten","fx":"Effektregler","name":"WLED-Name","tr":"Übersetzung","desc":"Beschreibung","img":"Bild","other":"Andere Sprachen","hex":"Hex","idx":"Referenz auf Deutsch","home":"↑ alle Sprachen"},
 "es":{"pal":"Paletas","eff":"Efectos","ctrl":"Controles","col":"Colores","nl":"Luz nocturna","seg":"Segmento","btn":"Botones","fx":"Deslizadores","name":"Nombre WLED","tr":"Traducción","desc":"Descripción","img":"Imagen","other":"Otros idiomas","hex":"Hex","idx":"Referencia en español","home":"↑ todos los idiomas"},
 "it":{"pal":"Tavolozze","eff":"Effetti","ctrl":"Controlli","col":"Colori","nl":"Luce notturna","seg":"Segmento","btn":"Pulsanti","fx":"Cursori effetto","name":"Nome WLED","tr":"Traduzione","desc":"Descrizione","img":"Immagine","other":"Altre lingue","hex":"Hex","idx":"Riferimento in italiano","home":"↑ tutte le lingue"},
 "ja":{"pal":"パレット","eff":"エフェクト","ctrl":"コントロール","col":"色","nl":"ナイトライト","seg":"セグメント","btn":"ボタン","fx":"スライダー","name":"WLED名","tr":"翻訳","desc":"説明","img":"画像","other":"他の言語","hex":"Hex","idx":"日本語リファレンス","home":"↑ すべての言語"},
 "ko":{"pal":"팔레트","eff":"효과","ctrl":"컨트롤","col":"색","nl":"야간등","seg":"세그먼트","btn":"버튼","fx":"슬라이더","name":"WLED 이름","tr":"번역","desc":"설명","img":"이미지","other":"다른 언어","hex":"Hex","idx":"한국어 참조","home":"↑ 모든 언어"},
 "zh":{"pal":"调色板","eff":"效果","ctrl":"控件","col":"颜色","nl":"夜灯","seg":"段","btn":"按钮","fx":"滑块","name":"WLED 名称","tr":"翻译","desc":"描述","img":"图片","other":"其他语言","hex":"Hex","idx":"中文参考","home":"↑ 所有语言"}}
CONC=[("palettes","pal"),("effects","eff"),("controls","ctrl"),("colors","col"),("nightlight","nl"),("segment","seg"),("buttons","btn"),("fxdata","fx")]
def esc(s): return (s or "").replace("|","\\|")
IMG="../../images"                                   # docs/<lang>/x.md -> images/
def nav(code,concept):
    u=UI[code]
    tabs=" · ".join(("**%s**"%u[k] if c==concept else "[%s](%s.md)"%(u[k],c)) for c,k in CONC)
    others=" · ".join("[%s](../%s/%s.md)"%(lc.upper(),lc,concept) for lc in LC if lc!=code)
    title={"palettes":u["pal"],"effects":u["eff"],"controls":u["ctrl"],"colors":u["col"],"nightlight":u["nl"],"segment":u["seg"],"buttons":u["btn"],"fxdata":u["fx"]}[concept]
    return ("# WLED %s\n\n%s &nbsp;•&nbsp; [%s](README.md)\n\n<sub>%s: %s</sub>\n\n"
            %(title,tabs,u["idx"],u["other"],others))
for code,label,flag in LANGS:
    d="%s/docs/%s"%(DST,code); os.makedirs(d,exist_ok=True); u=UI[code]
    r=["| %s | %s | %s | %s |"%(u["img"],u["name"],u["tr"],u["desc"]),"|---|---|---|---|"]
    for nm in pal:
        e=PAL[nm][code]; disp=nm[2:] if nm.startswith("* ") else nm
        r.append('| <img src="%s/palettes/%s.png" width="72"> | `%s` | %s | %s |'%(IMG,slug(nm),esc(disp),esc(e["name"]),esc(e["desc"])))
    open(d+"/palettes.md","w").write(nav(code,"palettes")+"\n".join(r)+"\n")
    r=["| %s | %s | %s | %s |"%(u["img"],u["name"],u["tr"],u["desc"]),"|---|---|---|---|"]
    for nm in eff:
        e=EFF.get(nm,{}).get(code,{"name":nm,"desc":""})
        r.append('| <img src="%s/effects/%s.gif" width="64"> | `%s` | %s | %s |'%(IMG,slug(nm),esc(nm),esc(e["name"]),esc(e["desc"])))
    open(d+"/effects.md","w").write(nav(code,"effects")+"\n".join(r)+"\n")
    r=["| %s | %s | %s |"%(u["name"],u["tr"],u["desc"]),"|---|---|---|"]
    for k in CTRL:
        e=CTRL[k][code]; r.append("| `%s` | %s | %s |"%(esc(k),esc(e["name"]),esc(e["desc"])))
    open(d+"/controls.md","w").write(nav(code,"controls")+"\n".join(r)+"\n")
    r=["> "+RAT[code].replace("\n"," "),"","| %s | %s | %s | %s | %s |"%(u["img"],u["name"],u["tr"],u["hex"],u["desc"]),"|---|---|---|---|---|"]
    for nm,e in COLE.items():
        rgb=e["rgb"]; hexv="#%02X%02X%02X"%tuple(rgb); ce=e[code]
        r.append('| <img src="%s/colors/%s.png" width="48"> | `%s` | %s | `%s` | %s |'%(IMG,slug(nm),esc(nm),esc(ce["name"]),hexv,esc(ce["desc"])))
    open(d+"/colors.md","w").write(nav(code,"colors")+"\n".join(r)+"\n")
    r=["| %s | %s | %s |"%(u["name"],u["tr"],u["desc"]),"|---|---|---|"]
    for k in NL:
        e=NL[k][code]; r.append("| `%s` | %s | %s |"%(esc(k),esc(e["name"]),esc(e["desc"])))
    open(d+"/nightlight.md","w").write(nav(code,"nightlight")+"\n".join(r)+"\n")
    for concept,DATA in (("segment",SEG),("buttons",BTN)):
        r=["| %s | %s | %s |"%(u["name"],u["tr"],u["desc"]),"|---|---|---|"]
        for k in DATA:
            e=DATA[k][code]; r.append("| `%s` | %s | %s |"%(esc(k),esc(e["name"]),esc(e["desc"])))
        open(d+"/%s.md"%concept,"w").write(nav(code,concept)+"\n".join(r)+"\n")
    r=["| %s | %s |"%(u["name"],u["tr"]),"|---|---|"]
    for k in FXL:
        e=FXL[k][code]; r.append("| `%s` | %s |"%(esc(k),esc(e["name"])))
    open(d+"/fxdata.md","w").write(nav(code,"fxdata")+"\n".join(r)+"\n")
    # per-language index (shown when opening docs/<lang>/)
    links="\n".join("- [%s](%s.md)"%(u[k],c) for c,k in CONC)
    other=" · ".join("[%s %s](../%s/README.md)"%(fl,lb,lcc) for lcc,lb,fl in LANGS if lcc!=code)
    open(d+"/README.md","w").write("# WLED %s — %s\n\n%s\n\n---\n\n**%s:** %s\n\n[%s](../README.md)\n"
        %(flag,label,links,u["other"],other,u["home"]))
# top index docs/README.md
rows=["| | "+" | ".join(u2 for _,u2 in [("pal","Palettes"),("eff","Effects"),("ctrl","Controls"),("col","Colours")])+" |","|---|---|---|---|---|"]
for code,label,flag in LANGS:
    cells=" | ".join("[%s](%s/%s.md)"%(nm,code,c) for c,nm in [("palettes","palettes"),("effects","effects"),("controls","controls"),("colors","colors")])
    rows.append("| %s **%s** | %s |"%(flag,label,cells))
open(DST+"/docs/README.md","w").write("# Reference docs\n\nEnglish name · translation · description · illustration — one page per **language × concept**. "
    "Open a language folder for its index, or jump straight in:\n\n"+"\n".join(rows)+"\n\n<sub>Back to the [repo README](../README.md).</sub>\n")
print("hierarchical docs written under docs/<lang>/")
