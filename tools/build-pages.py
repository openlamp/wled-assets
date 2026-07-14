import json, re, html
SP="/private/tmp/claude-501/-Users-benoitbesson-dev-music/b1b0bf2c-2a0b-4a74-83ae-5717d879ef61/scratchpad"
REPO="/Users/benoitbesson/dev/music/wled-assets"
data=json.load(open(SP+"/wled_data.json")); pal,eff,palx=data["pal"],data["eff"],{int(k):v for k,v in data["palx"].items()}
PT=json.load(open(REPO+"/i18n/palettes.json")); ET=json.load(open(REPO+"/i18n/effects.json"))
MEAN=json.load(open(REPO+"/docs/palette-meanings.json"))
ns={}; exec(re.search(r'_PAL_ART = \{.*?\n\}', open(REPO+"/plugin.py").read(), re.S).group(0), ns); ART=ns["_PAL_ART"]

LANGS=[("fr","Français"),("en","English"),("de","Deutsch"),("es","Español"),("it","Italiano"),("ja","日本語"),("ko","한국어"),("zh","中文")]
UI={ # page chrome per language
 "fr":{"ptitle":"Palettes WLED — noms, traductions & illustrations","etitle":"Effets WLED — noms, traductions & animations","orig":"Nom WLED","trad":"Nom traduit","desc":"Description","img":"Illustration","anim":"Animation","pal":"Palettes","eff":"Effets","other":"Autres langues","count":"%d au total"},
 "en":{"ptitle":"WLED palettes — names, translations & illustrations","etitle":"WLED effects — names, translations & animations","orig":"WLED name","trad":"Translated","desc":"Description","img":"Illustration","anim":"Animation","pal":"Palettes","eff":"Effects","other":"Other languages","count":"%d total"},
 "de":{"ptitle":"WLED-Paletten — Namen, Übersetzungen & Illustrationen","etitle":"WLED-Effekte — Namen, Übersetzungen & Animationen","orig":"WLED-Name","trad":"Übersetzt","desc":"Beschreibung","img":"Illustration","anim":"Animation","pal":"Paletten","eff":"Effekte","other":"Andere Sprachen","count":"%d gesamt"},
 "es":{"ptitle":"Paletas WLED — nombres, traducciones e ilustraciones","etitle":"Efectos WLED — nombres, traducciones y animaciones","orig":"Nombre WLED","trad":"Traducido","desc":"Descripción","img":"Ilustración","anim":"Animación","pal":"Paletas","eff":"Efectos","other":"Otros idiomas","count":"%d en total"},
 "it":{"ptitle":"Tavolozze WLED — nomi, traduzioni e illustrazioni","etitle":"Effetti WLED — nomi, traduzioni e animazioni","orig":"Nome WLED","trad":"Tradotto","desc":"Descrizione","img":"Illustrazione","anim":"Animazione","pal":"Tavolozze","eff":"Effetti","other":"Altre lingue","count":"%d in totale"},
 "ja":{"ptitle":"WLEDパレット — 名前・翻訳・イラスト","etitle":"WLEDエフェクト — 名前・翻訳・アニメーション","orig":"WLED名","trad":"翻訳","desc":"説明","img":"イラスト","anim":"アニメ","pal":"パレット","eff":"エフェクト","other":"他の言語","count":"全%d件"},
 "ko":{"ptitle":"WLED 팔레트 — 이름·번역·일러스트","etitle":"WLED 효과 — 이름·번역·애니메이션","orig":"WLED 이름","trad":"번역","desc":"설명","img":"일러스트","anim":"애니메이션","pal":"팔레트","eff":"효과","other":"다른 언어","count":"총 %d개"},
 "zh":{"ptitle":"WLED 调色板 — 名称、翻译与插图","etitle":"WLED 效果 — 名称、翻译与动画","orig":"WLED 名称","trad":"翻译","desc":"描述","img":"插图","anim":"动画","pal":"调色板","eff":"效果","other":"其他语言","count":"共 %d 个"}}

def fam(name):
    n=(name or "").lower()
    def has(*ks): return any(k in n for k in ks)
    if has("solid","static","fill"): return "solid"
    if has("strobe","blink","stutter","lightning","police","hyper"): return "strobe"
    if has("sparkle","twinkle","glitter","fairy","popcorn","firework","star","dissolve"): return "sparkle"
    if has("rainbow","colorloop","colorful","aurora","pride","colortwinkle","palette","candy"): return "rainbow"
    if has("chase","comet","scan","running","marquee","theater","sweep","dancing","lighthouse","wipe","loading","railway"): return "chase"
    if has("fire","flicker","lava","candle","ember","halloween","sunrise","sunset","flame"): return "fire"
    if has("rain","drip","drop","tetrix","matrix","meteor","waterfall","spectrum","fall"): return "rain"
    if has("breathe","breath","fade","pulse","sine","sinelon","gradient","blend"): return "breathe"
    return "wave"
FAMDESC={
 "wave":{"fr":"Une vague de couleur parcourt le ruban.","en":"A colour wave travels along the strip.","de":"Eine Farbwelle wandert über den Streifen.","es":"Una onda de color recorre la tira.","it":"Un'onda di colore percorre la striscia.","ja":"色の波がストリップを流れる。","ko":"색의 물결이 스트립을 따라 흐른다.","zh":"色彩波沿灯带流动。"},
 "chase":{"fr":"Un point lumineux balaie le ruban (poursuite).","en":"A point of light sweeps along (a chase).","de":"Ein Lichtpunkt zieht entlang (Verfolgung).","es":"Un punto de luz recorre la tira (persecución).","it":"Un punto luminoso scorre (inseguimento).","ja":"光点が走る(チェイス)。","ko":"빛점이 훑고 지나간다(체이스).","zh":"一个光点扫过（追逐）。"},
 "sparkle":{"fr":"Des points scintillent au hasard.","en":"Points twinkle on and off at random.","de":"Punkte funkeln zufällig auf und ab.","es":"Puntos que centellean al azar.","it":"Punti che scintillano a caso.","ja":"点がランダムに瞬く。","ko":"점들이 무작위로 반짝인다.","zh":"光点随机闪烁。"},
 "rainbow":{"fr":"Le spectre complet défile.","en":"The full spectrum cycles through.","de":"Das volle Spektrum läuft durch.","es":"El espectro completo se desplaza.","it":"L'intero spettro scorre.","ja":"全スペクトルが巡る。","ko":"전체 스펙트럼이 순환한다.","zh":"完整光谱循环流动。"},
 "breathe":{"fr":"La luminosité enfle et retombe (respiration).","en":"Brightness swells and fades (breathing).","de":"Die Helligkeit schwillt an und ab (Atmen).","es":"El brillo crece y decae (respiración).","it":"La luminosità cresce e cala (respiro).","ja":"明るさが強弱する(呼吸)。","ko":"밝기가 커졌다 작아진다(호흡).","zh":"亮度起伏（呼吸）。"},
 "fire":{"fr":"Des tons chauds vacillent comme des flammes.","en":"Warm tones flicker like flames.","de":"Warme Töne flackern wie Flammen.","es":"Tonos cálidos titilan como llamas.","it":"Toni caldi tremolano come fiamme.","ja":"暖色が炎のように揺らめく。","ko":"따뜻한 색이 불꽃처럼 일렁인다.","zh":"暖色如火焰般跳动。"},
 "rain":{"fr":"Des points tombent comme la pluie.","en":"Points fall like rain.","de":"Punkte fallen wie Regen.","es":"Puntos que caen como lluvia.","it":"Punti che cadono come pioggia.","ja":"点が雨のように落ちる。","ko":"점들이 비처럼 떨어진다.","zh":"光点如雨落下。"},
 "strobe":{"fr":"Des éclairs nets, allumé/éteint.","en":"Sharp flashes, on and off.","de":"Scharfe Blitze, an und aus.","es":"Destellos nítidos, encendido/apagado.","it":"Lampi netti, acceso/spento.","ja":"鋭い点滅。","ko":"날카로운 점멸.","zh":"急促闪烁，忽明忽灭。"},
 "solid":{"fr":"Une couleur unie et stable.","en":"A single steady colour.","de":"Eine einzelne, ruhige Farbe.","es":"Un color fijo y uniforme.","it":"Un unico colore fisso.","ja":"単一の安定した色。","ko":"단일한 고정 색.","zh":"单一稳定的颜色。"}}

def pal_svg(idx,name):
    cols=[s for s in (palx.get(idx) or []) if isinstance(s,list) and len(s)==4]
    gid="g%d"%idx
    if not cols:
        bars="".join('<rect x="%.1f" y="0" width="%.1f" height="144" fill="%s"/>'%(k*24,24.5,c) for k,c in enumerate(["#e6002a","#ff7d00","#ffd200","#2ee06e","#3399ff","#8b5cf6"]))
        return '<svg viewBox="0 0 144 144" preserveAspectRatio="none"><rect width="144" height="144" fill="#1a1a1a"/>%s</svg>'%bars
    gs="".join('<stop offset="%.3f" stop-color="rgb(%d,%d,%d)"/>'%(p/255.0,r,g,b) for p,r,g,b in cols)
    key=(name[2:] if name.startswith("* ") else name).lower(); art=ART.get(key)
    if art:
        vert,shape=art; x2,y2=(0,1) if vert else (1,0)
        return '<svg viewBox="0 0 144 144"><rect width="144" height="144" fill="#1a1a1a"/><defs><linearGradient id="%s" x1="0" y1="0" x2="%d" y2="%d">%s</linearGradient></defs><g fill="url(#%s)">%s</g></svg>'%(gid,x2,y2,gs,gid,shape.replace("GRAD",gid))
    return '<svg viewBox="0 0 144 144" preserveAspectRatio="none"><defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="0">%s</linearGradient></defs><rect width="144" height="144" fill="url(#%s)"/></svg>'%(gid,gs,gid)

CSS='''*{box-sizing:border-box}body{margin:0;background:#0b0d11;color:#eae8e2;font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:0 20px}
header{padding:48px 20px 20px;max-width:1000px;margin:0 auto}
.kick{letter-spacing:.28em;text-transform:uppercase;font-size:11px;font-weight:700;color:#37d3e6}
h1{font-size:clamp(24px,4vw,34px);margin:.3em 0 .2em;font-weight:800;text-wrap:balance}
.sub{color:#8b93a1}
nav{position:sticky;top:0;z-index:9;background:rgba(11,13,17,.85);backdrop-filter:blur(10px);border-bottom:1px solid #252b35}
nav .wrap{display:flex;gap:6px;padding:9px 20px;flex-wrap:wrap;align-items:center}
nav a{color:#8b93a1;text-decoration:none;font-weight:600;font-size:13px;padding:6px 11px;border-radius:8px}
nav a:hover{color:#eae8e2;background:#13161d}nav a.on{color:#0b0d11;background:#37d3e6}
nav .sep{flex:1}nav .lg{font-size:12px}
.tablewrap{overflow-x:auto;border:1px solid #252b35;border-radius:12px;margin:22px 0 60px}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:10px 14px;border-bottom:1px solid #20242d;vertical-align:middle}
thead th{position:sticky;top:44px;background:#161a21;color:#8b93a1;font-size:11px;letter-spacing:.07em;text-transform:uppercase}
tbody tr:hover td{background:#14171e}
.viz{width:66px}.viz svg{width:56px;height:56px;display:block;background:#1a1a1a;border-radius:9px}
.on-name{font-weight:700}.tr-name{color:#37d3e6}.tr-name.fb{color:#5b6270;font-style:italic}
.d{color:#c3c8d2}.idx{color:#5b6270;font-variant-numeric:tabular-nums;font-size:12px}
footer{padding:40px 20px 70px;text-align:center;color:#8b93a1;font-size:13px;border-top:1px solid #252b35}
footer a{color:#37d3e6}
@media(prefers-reduced-motion:reduce){.viz svg *{animation:none}}'''

def nav_html(L,cat):
    u=UI[L]
    tabs='<a href="palettes-%s.html" class="%s">%s</a><a href="effects-%s.html" class="%s">%s</a>'%(L,"on" if cat=="pal" else "",u["pal"],L,"on" if cat=="eff" else "",u["eff"])
    others=" ".join('<a class="lg" href="%s-%s.html">%s</a>'%(cat if cat=="palettes" else "effects", code, code.upper()) for code,_ in LANGS if code!=L)
    base="palettes" if cat=="pal" else "effects"
    others=" ".join('<a class="lg" href="%s-%s.html">%s</a>'%(base,code,code.upper()) for code,_ in LANGS if code!=L)
    return '<nav><div class="wrap">%s<span class="sep"></span><span style="color:#5b6270;font-size:12px">%s:</span>%s</div></nav>'%(tabs,UI[L]["other"],others)

def palettes_page(L):
    u=UI[L]; rows=[]
    for i,nm in enumerate(pal):
        disp=nm[2:] if nm.startswith("* ") else nm
        tr=PT.get(nm,{}).get(L)
        trname=html.escape(tr) if tr else html.escape(disp); fb="" if tr else " fb"
        m=MEAN.get(nm,{}); dsc=html.escape(m.get(L) or m.get("en") or "")
        rows.append('<tr><td class="viz">%s</td><td class="idx">%d</td><td class="on-name">%s</td><td class="tr-name%s">%s</td><td class="d">%s</td></tr>'
                    %(pal_svg(i,nm),i,html.escape(disp),fb,trname,dsc))
    return page(L,"pal",u["ptitle"],u["count"]%len(pal),
        '<thead><tr><th>%s</th><th>#</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody>'%(u["img"],u["orig"],u["trad"],u["desc"],"".join(rows)),anim=False)

def effects_page(L):
    u=UI[L]; rows=[]
    for i,nm in enumerate(eff):
        f=fam(nm); tr=ET.get(nm,{}).get(L)
        trname=html.escape(tr) if tr else html.escape(nm); fb="" if tr else " fb"
        dsc=html.escape(FAMDESC[f][L])
        rows.append('<tr><td class="viz"><span class="fx" data-fam="%s"></span></td><td class="idx">%d</td><td class="on-name">%s</td><td class="tr-name%s">%s</td><td class="d">%s</td></tr>'
                    %(f,i,html.escape(nm),fb,trname,dsc))
    return page(L,"eff",u["etitle"],u["count"]%len(eff),
        '<thead><tr><th>%s</th><th>#</th><th>%s</th><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody>'%(u["anim"],u["orig"],u["trad"],u["desc"],"".join(rows)),anim=True)

ANIMJS=r'''<script>
const M=Math;
function hsv(h,s,v){h*=6;const i=M.floor(h),f=h-i,p=v*(1-s),q=v*(1-s*f),t=v*(1-s*(1-f));const a=[[v,t,p],[q,v,p],[p,v,t],[p,q,v],[t,p,v],[v,p,q]][i%6];return 'rgb('+M.round(a[0]*255)+','+M.round(a[1]*255)+','+M.round(a[2]*255)+')';}
function anim(ph,f){
 if(f==='solid')return '<rect x="26" y="26" width="92" height="92" rx="14" fill="#f0a838"/>';
 if(f==='strobe'){const c=ph%2===0?'#fff':'#272c36';return [[48,48],[96,48],[48,96],[96,96]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="16" fill="${c}"/>`).join('');}
 if(f==='sparkle'){let o='';for(let i=0;i<9;i++){const cx=24+(i%3)*48,cy=24+((i/3)|0)*48,lit=((i*7+ph*3)%9)<3;o+=`<circle cx="${cx}" cy="${cy}" r="${lit?13:5}" fill="${lit?'#eaf2ff':'#39414e'}"/>`;}return o;}
 if(f==='fire'){let o='';for(let i=0;i<5;i++){const h=42+62*(0.5+0.5*M.sin(ph*0.9+i*1.7));o+=`<rect x="${16+i*24}" y="${128-h}" width="18" height="${h}" rx="8" fill="${hsv(0.02+0.09*(h/104),1,1)}"/>`;}return o;}
 if(f==='rain'){let o='';for(let i=0;i<4;i++){const y=(ph*13+i*41)%150-20;o+=`<rect x="${26+i*32}" y="${y}" width="9" height="28" rx="4" fill="#57b0ff"/>`;}return o;}
 if(f==='chase'){const pos=ph%7;let o='';for(let i=0;i<7;i++){const br=M.max(0.12,1-(((pos-i)%7+7)%7)*0.32),r=(26+64*br)|0,g=(26+154*br)|0,b=(26+229*br)|0;o+=`<circle cx="${18+i*18}" cy="72" r="9" fill="rgb(${r},${g},${b})"/>`;}return o;}
 if(f==='breathe'){const br=0.35+0.65*(0.5+0.5*M.sin(ph*0.5));return `<circle cx="72" cy="72" r="${28+34*br}" fill="${hsv(0.6,0.5,br)}"/>`;}
 if(f==='rainbow'){let o='';for(let i=0;i<7;i++)o+=`<rect x="${12+i*18}" y="30" width="13" height="84" rx="3" fill="${hsv(((i*51+ph*14)%360)/360,0.9,1)}"/>`;return o;}
 let o='';for(let i=0;i<7;i++){const br=0.30+0.70*(0.5+0.5*M.sin(ph*0.6-i*0.95)),h=22+96*br;o+=`<rect x="${12+i*18}" y="${128-h}" width="13" height="${h}" rx="3" fill="${hsv(((i*34+ph*12)%360)/360,0.85,br)}"/>`;}return o;}
const fams={},vis=new Set();
document.querySelectorAll('.fx').forEach(el=>{const s=document.createElementNS('http://www.w3.org/2000/svg','svg');s.setAttribute('viewBox','0 0 144 144');el.appendChild(s);(fams[el.dataset.fam]=fams[el.dataset.fam]||[]).push(s);});
const io=new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting?vis.add(e.target):vis.delete(e.target)),{rootMargin:'120px'});
Object.values(fams).flat().forEach(s=>io.observe(s));
const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;let ph=0;
function tick(){ph++;const cache={};for(const f in fams){const svg=anim(ph,f);for(const s of fams[f])if(vis.has(s))s.innerHTML=svg;}}
tick();if(!reduce)setInterval(tick,170);
</script>'''

def page(L,cat,title,count,tablebody,anim):
    u=UI[L]
    body='<title>%s</title><style>%s</style>%s<header><div class="kick">OpenLamp · WLED</div><h1>%s</h1><p class="sub">%s · openlamp/wled-assets</p></header><main class="wrap"><div class="tablewrap"><table>%s</table></div></main><footer><a href="https://github.com/openlamp/wled-assets">openlamp/wled-assets</a></footer>'%(title,CSS,nav_html(L,cat),title,count,tablebody)
    if anim: body+=ANIMJS
    return "<!doctype html><meta charset=utf-8>"+body

import os
os.makedirs(REPO+"/docs/pages",exist_ok=True)
for code,_ in LANGS:
    open(REPO+"/docs/pages/palettes-%s.html"%code,"w").write(palettes_page(code))
    open(REPO+"/docs/pages/effects-%s.html"%code,"w").write(effects_page(code))
# also drop plain fr copies to scratchpad for the Artifact (strip doctype/meta for Artifact wrapper)
for cat in ("palettes","effects"):
    h=open(REPO+"/docs/pages/%s-fr.html"%cat).read().replace("<!doctype html><meta charset=utf-8>","",1)
    open(SP+"/%s-fr.html"%cat,"w").write(h)
print("generated 16 pages ->", len([f for f in os.listdir(REPO+"/docs/pages")]))
