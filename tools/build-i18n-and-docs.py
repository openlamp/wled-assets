import json, re, html, os
SP="/private/tmp/claude-501/-Users-benoitbesson-dev-music/b1b0bf2c-2a0b-4a74-83ae-5717d879ef61/scratchpad"
DST="/Users/benoitbesson/dev/music/wled-assets"; LUM="/Users/benoitbesson/dev/music/wled-assets"
data=json.load(open(SP+"/wled_data.json")); pal,eff=data["pal"],data["eff"]
PT=json.load(open(LUM+"/locales/palettes.json")); ET=json.load(open(LUM+"/locales/effects.json"))
MEAN=json.load(open(DST+"/meanings/palette-meanings.json"))
FAMFILE=json.load(open(DST+"/i18n/effect-families.json"))["families"]
DYN=json.load(open(SP+"/dyn.json"))
ns={}; exec(open(SP+"/pages.py").read(), ns); fam=ns["fam"]   # regenerates pages (idempotent)
LANGS=[("en","English"),("fr","Français"),("de","Deutsch"),("es","Español"),("it","Italiano"),("ja","日本語"),("ko","한국어"),("zh","中文")]
def slug(n): return re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')

# ---- NEW CONCEPT: effect controls (the standard effect parameters) ----
CTRL={
"Speed":{"desc_en":"How fast the effect animates.","tr":{"fr":("Vitesse","À quelle vitesse l'effet s'anime."),"de":("Tempo","Wie schnell der Effekt animiert."),"es":("Velocidad","La rapidez de la animación del efecto."),"it":("Velocità","Quanto velocemente si anima l'effetto."),"ja":("速度","エフェクトのアニメーション速度。"),"ko":("속도","효과 애니메이션의 빠르기."),"zh":("速度","效果动画的快慢。")}},
"Intensity":{"desc_en":"The effect's intensity or density.","tr":{"fr":("Intensité","L'intensité ou la densité de l'effet."),"de":("Intensität","Die Intensität bzw. Dichte des Effekts."),"es":("Intensidad","La intensidad o densidad del efecto."),"it":("Intensità","L'intensità o densità dell'effetto."),"ja":("強度","エフェクトの強さ・密度。"),"ko":("강도","효과의 강도 또는 밀도."),"zh":("强度","效果的强度或密度。")}},
"Custom 1":{"desc_en":"An effect-specific slider (meaning varies by effect).","tr":{"fr":("Perso 1","Curseur propre à l'effet (sens variable)."),"de":("Custom 1","Effektspezifischer Regler (je nach Effekt)."),"es":("Personal. 1","Deslizador propio del efecto (varía)."),"it":("Custom 1","Cursore specifico dell'effetto (varia)."),"ja":("カスタム1","エフェクト固有のスライダー(意味は効果次第)。"),"ko":("커스텀 1","효과별 슬라이더(의미는 효과마다 다름)."),"zh":("自定义 1","效果专属滑块（含义随效果而变）。")}},
"Custom 2":{"desc_en":"A second effect-specific slider.","tr":{"fr":("Perso 2","Deuxième curseur propre à l'effet."),"de":("Custom 2","Zweiter effektspezifischer Regler."),"es":("Personal. 2","Segundo deslizador del efecto."),"it":("Custom 2","Secondo cursore dell'effetto."),"ja":("カスタム2","エフェクト固有の2つ目のスライダー。"),"ko":("커스텀 2","두 번째 효과별 슬라이더."),"zh":("自定义 2","第二个效果专属滑块。")}},
"Custom 3":{"desc_en":"A third effect-specific slider (0-31).","tr":{"fr":("Perso 3","Troisième curseur de l'effet (0-31)."),"de":("Custom 3","Dritter Effektregler (0-31)."),"es":("Personal. 3","Tercer deslizador del efecto (0-31)."),"it":("Custom 3","Terzo cursore dell'effetto (0-31)."),"ja":("カスタム3","3つ目のスライダー(0-31)。"),"ko":("커스텀 3","세 번째 슬라이더(0-31)."),"zh":("自定义 3","第三个滑块（0-31）。")}},
"Option 1":{"desc_en":"An effect-specific on/off toggle.","tr":{"fr":("Option 1","Bascule oui/non propre à l'effet."),"de":("Option 1","Effektspezifischer Schalter."),"es":("Opción 1","Interruptor propio del efecto."),"it":("Opzione 1","Interruttore specifico dell'effetto."),"ja":("オプション1","エフェクト固有のオン/オフ。"),"ko":("옵션 1","효과별 켜기/끄기."),"zh":("选项 1","效果专属开关。")}},
"Option 2":{"desc_en":"A second effect-specific toggle.","tr":{"fr":("Option 2","Deuxième bascule de l'effet."),"de":("Option 2","Zweiter Effektschalter."),"es":("Opción 2","Segundo interruptor del efecto."),"it":("Opzione 2","Secondo interruttore dell'effetto."),"ja":("オプション2","2つ目のオン/オフ。"),"ko":("옵션 2","두 번째 토글."),"zh":("选项 2","第二个开关。")}},
"Option 3":{"desc_en":"A third effect-specific toggle.","tr":{"fr":("Option 3","Troisième bascule de l'effet."),"de":("Option 3","Dritter Effektschalter."),"es":("Opción 3","Tercer interruptor del efecto."),"it":("Opzione 3","Terzo interruttore dell'effetto."),"ja":("オプション3","3つ目のオン/オフ。"),"ko":("옵션 3","세 번째 토글."),"zh":("选项 3","第三个开关。")}},
"Effect color":{"desc_en":"The effect's primary colour.","tr":{"fr":("Couleur d'effet","La couleur principale de l'effet."),"de":("Effektfarbe","Die Hauptfarbe des Effekts."),"es":("Color de efecto","El color principal del efecto."),"it":("Colore effetto","Il colore principale dell'effetto."),"ja":("エフェクト色","エフェクトの主色。"),"ko":("효과 색","효과의 주 색상."),"zh":("效果颜色","效果的主色。")}},
"Background color":{"desc_en":"The effect's background colour.","tr":{"fr":("Couleur de fond","La couleur de fond de l'effet."),"de":("Hintergrundfarbe","Die Hintergrundfarbe des Effekts."),"es":("Color de fondo","El color de fondo del efecto."),"it":("Colore di sfondo","Il colore di sfondo dell'effetto."),"ja":("背景色","エフェクトの背景色。"),"ko":("배경색","효과의 배경 색상."),"zh":("背景色","效果的背景颜色。")}},
"Custom color":{"desc_en":"A third colour slot for the effect.","tr":{"fr":("Couleur perso","Troisième emplacement de couleur."),"de":("Zusatzfarbe","Dritter Farbslot des Effekts."),"es":("Color personal.","Tercer espacio de color."),"it":("Colore custom","Terzo slot di colore."),"ja":("カスタム色","3つ目の色スロット。"),"ko":("커스텀 색","세 번째 색 슬롯."),"zh":("自定义颜色","第三个颜色槽。")}},
"Palette":{"desc_en":"The colour palette the effect draws from.","tr":{"fr":("Palette","La palette de couleurs utilisée par l'effet."),"de":("Palette","Die Farbpalette, die der Effekt nutzt."),"es":("Paleta","La paleta de colores que usa el efecto."),"it":("Tavolozza","La tavolozza usata dall'effetto."),"ja":("パレット","エフェクトが使う配色パレット。"),"ko":("팔레트","효과가 사용하는 색 팔레트."),"zh":("调色板","效果所用的配色板。")}},
}

def L(dic,code,fb): return dic.get(code) or fb   # helper

# ---- combined i18n files (name + desc per language) ----
def pal_entry(nm):
    e={}
    for code,_ in LANGS:
        name = nm if code=="en" else (PT.get(nm,{}).get(code) or nm)
        desc = (MEAN.get(nm,{}) or {}).get(code) or (MEAN.get(nm,{}) or {}).get("en") or ""
        e[code]={"name":name,"desc":desc}
    return e
def eff_entry(nm):
    f=fam(nm); e={}
    for code,_ in LANGS:
        name = nm if code=="en" else (ET.get(nm,{}).get(code) or nm)
        desc = FAMFILE.get(f,{}).get(code) or FAMFILE.get(f,{}).get("en") or ""
        e[code]={"name":name,"desc":desc}
    return e
def ctrl_entry(k):
    d=CTRL[k]; e={"en":{"name":k,"desc":d["desc_en"]}}
    for code,pair in d["tr"].items(): e[code]={"name":pair[0],"desc":pair[1]}
    return e

palettes={nm:pal_entry(nm) for nm in pal}
effects={nm:eff_entry(nm) for nm in eff}
controls={k:ctrl_entry(k) for k in CTRL}
NOTE="Combined translations: each standard WLED enum -> per language {name, desc}. Key = English name (join key). Missing -> English fallback. CJK are a first pass (native review welcome)."
for fn,obj,note in [("palettes",palettes,NOTE+" desc = what the palette NAME refers to."),
                    ("effects",effects,NOTE+" desc = the effect's MOTION FAMILY (see animations/families.json)."),
                    ("controls",controls,NOTE+" Standard effect parameters/controls.")]:
    json.dump({"_note":note,"entries":obj}, open(DST+"/i18n/%s.json"%fn,"w"), ensure_ascii=False, indent=1)
print("combined i18n:",len(palettes),"pal /",len(effects),"eff /",len(controls),"controls")

# ---- markdown docs per concept per language ----
UITXT={"en":("Palettes","Effects","Controls","WLED name","Translation","Description","Image","Other languages"),
 "fr":("Palettes","Effets","Contrôles","Nom WLED","Traduction","Description","Image","Autres langues"),
 "de":("Paletten","Effekte","Regler","WLED-Name","Übersetzung","Beschreibung","Bild","Andere Sprachen"),
 "es":("Paletas","Efectos","Controles","Nombre WLED","Traducción","Descripción","Imagen","Otros idiomas"),
 "it":("Tavolozze","Effetti","Controlli","Nome WLED","Traduzione","Descrizione","Immagine","Altre lingue"),
 "ja":("パレット","エフェクト","コントロール","WLED名","翻訳","説明","画像","他の言語"),
 "ko":("팔레트","효과","컨트롤","WLED 이름","번역","설명","이미지","다른 언어"),
 "zh":("调色板","效果","控件","WLED 名称","翻译","描述","图片","其他语言")}
os.makedirs(DST+"/docs",exist_ok=True)
def md_escape(s): return (s or "").replace("|","\\|")
def header(code,concept):
    u=UITXT[code]; ci={"palettes":0,"effects":1,"controls":2}[concept]
    tabs=" · ".join(("**%s**" if i==ci else "[%s](%s.%s.md)")%((u[i],) if i==ci else (u[i],c,code)) for i,c in enumerate(["palettes","effects","controls"]))
    others=" · ".join("[%s](%s.%s.md)"%(lc.upper(),concept,lc) for lc,_ in LANGS if lc!=code)
    title={"palettes":u[0],"effects":u[1],"controls":u[2]}[concept]
    return "# WLED %s\n\n%s\n\n<sub>%s: %s</sub>\n\n"%(title, tabs, u[7], others)
for code,_ in LANGS:
    u=UITXT[code]
    # palettes
    rows=["| %s | %s | %s | %s |"%(u[6],u[3],u[4],u[5]),"|---|---|---|---|"]
    for nm in pal:
        e=palettes[nm][code]; img="../images/palettes/%s.png"%slug(nm)
        disp=nm[2:] if nm.startswith("* ") else nm
        rows.append("| <img src=\"%s\" width=\"72\"> | `%s` | %s | %s |"%(img,md_escape(disp),md_escape(e["name"]),md_escape(e["desc"])))
    open(DST+"/docs/palettes.%s.md"%code,"w").write(header(code,"palettes")+"\n".join(rows)+"\n")
    # effects
    rows=["| %s | %s | %s | %s |"%(u[6],u[3],u[4],u[5]),"|---|---|---|---|"]
    for nm in eff:
        e=effects[nm][code]; img="../images/effects/%s.gif"%fam(nm)
        rows.append("| <img src=\"%s\" width=\"64\"> | `%s` | %s | %s |"%(img,md_escape(nm),md_escape(e["name"]),md_escape(e["desc"])))
    open(DST+"/docs/effects.%s.md"%code,"w").write(header(code,"effects")+"\n".join(rows)+"\n")
    # controls
    rows=["| %s | %s | %s |"%(u[3],u[4],u[5]),"|---|---|---|"]
    for k in CTRL:
        e=controls[k][code]; rows.append("| `%s` | %s | %s |"%(md_escape(k),md_escape(e["name"]),md_escape(e["desc"])))
    open(DST+"/docs/controls.%s.md"%code,"w").write(header(code,"controls")+"\n".join(rows)+"\n")
print("24 markdown docs written")
