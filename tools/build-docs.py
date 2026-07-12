import json, html, importlib.util
DST="/Users/benoitbesson/dev/music/wled-assets"
SP="/private/tmp/claude-501/-Users-benoitbesson-dev-music/b1b0bf2c-2a0b-4a74-83ae-5717d879ef61/scratchpad"
def slug(n):
    import re; return re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')
data=json.load(open(SP+"/wled_data.json")); pal,eff=data["pal"],data["eff"]
PAL=json.load(open(DST+"/i18n/palettes.json"))["entries"]
EFF=json.load(open(DST+"/i18n/effects.json"))["entries"]
CTRL=json.load(open(DST+"/i18n/controls.json"))["entries"]
COL=json.load(open(DST+"/i18n/colors.json")); COLE=COL["entries"]; RAT=COL["_rationale"]
spec=importlib.util.spec_from_file_location("m",SP+"/motions.py"); mo=importlib.util.module_from_spec(spec); spec.loader.exec_module(mo)
LANGS=["en","fr","de","es","it","ja","ko","zh"]
UI={"en":{"pal":"Palettes","eff":"Effects","ctrl":"Controls","col":"Colours","name":"WLED name","tr":"Translation","desc":"Description","img":"Image","other":"Other languages","hex":"Hex","total":"%d total"},
 "fr":{"pal":"Palettes","eff":"Effets","ctrl":"Contrôles","col":"Couleurs","name":"Nom WLED","tr":"Traduction","desc":"Description","img":"Image","other":"Autres langues","hex":"Hex","total":"%d au total"},
 "de":{"pal":"Paletten","eff":"Effekte","ctrl":"Regler","col":"Farben","name":"WLED-Name","tr":"Übersetzung","desc":"Beschreibung","img":"Bild","other":"Andere Sprachen","hex":"Hex","total":"%d gesamt"},
 "es":{"pal":"Paletas","eff":"Efectos","ctrl":"Controles","col":"Colores","name":"Nombre WLED","tr":"Traducción","desc":"Descripción","img":"Imagen","other":"Otros idiomas","hex":"Hex","total":"%d en total"},
 "it":{"pal":"Tavolozze","eff":"Effetti","ctrl":"Controlli","col":"Colori","name":"Nome WLED","tr":"Traduzione","desc":"Descrizione","img":"Immagine","other":"Altre lingue","hex":"Hex","total":"%d in totale"},
 "ja":{"pal":"パレット","eff":"エフェクト","ctrl":"コントロール","col":"色","name":"WLED名","tr":"翻訳","desc":"説明","img":"画像","other":"他の言語","hex":"Hex","total":"全%d件"},
 "ko":{"pal":"팔레트","eff":"효과","ctrl":"컨트롤","col":"색","name":"WLED 이름","tr":"번역","desc":"설명","img":"이미지","other":"다른 언어","hex":"Hex","total":"총 %d개"},
 "zh":{"pal":"调色板","eff":"效果","ctrl":"控件","col":"颜色","name":"WLED 名称","tr":"翻译","desc":"描述","img":"图片","other":"其他语言","hex":"Hex","total":"共 %d 个"}}
CONC=[("palettes","pal"),("effects","eff"),("controls","ctrl"),("colors","col")]
def esc(s): return (s or "").replace("|","\\|")
def nav(code,concept):
    u=UI[code]
    tabs=" · ".join(("**%s**"%u[k] if c==concept else "[%s](%s.%s.md)"%(u[k],c,code)) for c,k in CONC)
    others=" · ".join("[%s](%s.%s.md)"%(lc.upper(),concept,lc) for lc in LANGS if lc!=code)
    title={"palettes":u["pal"],"effects":u["eff"],"controls":u["ctrl"],"colors":u["col"]}[concept]
    return "# WLED %s\n\n%s\n\n<sub>%s: %s</sub>\n\n"%(title,tabs,u["other"],others)
for code in LANGS:
    u=UI[code]
    # palettes
    r=["| %s | %s | %s | %s |"%(u["img"],u["name"],u["tr"],u["desc"]),"|---|---|---|---|"]
    for nm in pal:
        e=PAL[nm][code]; disp=nm[2:] if nm.startswith("* ") else nm
        r.append('| <img src="../images/palettes/%s.png" width="72"> | `%s` | %s | %s |'%(slug(nm),esc(disp),esc(e["name"]),esc(e["desc"])))
    open(DST+"/docs/palettes.%s.md"%code,"w").write(nav(code,"palettes")+"\n".join(r)+"\n")
    # effects
    r=["| %s | %s | %s | %s |"%(u["img"],u["name"],u["tr"],u["desc"]),"|---|---|---|---|"]
    for nm in eff:
        e=EFF.get(nm,{}).get(code,{"name":nm,"desc":""})
        r.append('| <img src="../images/effects/%s.gif" width="64"> | `%s` | %s | %s |'%(slug(nm),esc(nm),esc(e["name"]),esc(e["desc"])))
    open(DST+"/docs/effects.%s.md"%code,"w").write(nav(code,"effects")+"\n".join(r)+"\n")
    # controls
    r=["| %s | %s | %s |"%(u["name"],u["tr"],u["desc"]),"|---|---|---|"]
    for k in CTRL:
        e=CTRL[k][code]; r.append("| `%s` | %s | %s |"%(esc(k),esc(e["name"]),esc(e["desc"])))
    open(DST+"/docs/controls.%s.md"%code,"w").write(nav(code,"controls")+"\n".join(r)+"\n")
    # colors (with rationale intro)
    r=["> "+RAT[code].replace("\n"," "),"","| %s | %s | %s | %s | %s |"%(u["img"],u["name"],u["tr"],u["hex"],u["desc"]),"|---|---|---|---|---|"]
    for nm,e in COLE.items():
        rgb=e["rgb"]; hexv="#%02X%02X%02X"%tuple(rgb); ce=e[code]
        r.append('| <img src="../images/colors/%s.png" width="48"> | `%s` | %s | `%s` | %s |'%(slug(nm),esc(nm),esc(ce["name"]),hexv,esc(ce["desc"])))
    open(DST+"/docs/colors.%s.md"%code,"w").write(nav(code,"colors")+"\n".join(r)+"\n")
print("32 docs regenerated (4 concepts x 8 langs)")
