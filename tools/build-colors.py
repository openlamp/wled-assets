import json, re, os, subprocess
DST="/Users/benoitbesson/dev/music/wled-assets"
COLORS=[  # English key, rgb, rank(1=most distinguishable), per-lang name
 ("Yellow",     (255,210,0),  1, {"fr":"Jaune","de":"Gelb","es":"Amarillo","it":"Giallo","ja":"黄","ko":"노랑","zh":"黄色"}),
 ("Violet",     (150,70,170), 2, {"fr":"Violet","de":"Violett","es":"Violeta","it":"Viola","ja":"紫","ko":"보라","zh":"紫色"}),
 ("Orange",     (255,125,0),  3, {"fr":"Orange","de":"Orange","es":"Naranja","it":"Arancione","ja":"オレンジ","ko":"주황","zh":"橙色"}),
 ("Light Blue", (130,195,255),4, {"fr":"Bleu clair","de":"Hellblau","es":"Azul claro","it":"Azzurro","ja":"水色","ko":"하늘색","zh":"浅蓝"}),
 ("Red",        (230,0,40),   5, {"fr":"Rouge","de":"Rot","es":"Rojo","it":"Rosso","ja":"赤","ko":"빨강","zh":"红色"}),
 ("Green",      (0,200,80),   6, {"fr":"Vert","de":"Grün","es":"Verde","it":"Verde","ja":"緑","ko":"초록","zh":"绿色"}),
 ("Pink",       (255,130,170),7, {"fr":"Rose","de":"Rosa","es":"Rosa","it":"Rosa","ja":"ピンク","ko":"분홍","zh":"粉色"}),
 ("Blue",       (0,100,200),  8, {"fr":"Bleu","de":"Blau","es":"Azul","it":"Blu","ja":"青","ko":"파랑","zh":"蓝色"}),
]
def rankdesc(r):
    return {"en":"Stage colour #%d — one of the 8 maximum-contrast hues, ranked by at-a-glance distinguishability."%r,
     "fr":"Couleur scène n°%d — l'une des 8 teintes de contraste maximal, classées par lisibilité au premier coup d'œil."%r,
     "de":"Bühnenfarbe Nr. %d — eine der 8 kontraststärksten Farbtöne, nach Auf-einen-Blick-Unterscheidbarkeit gereiht."%r,
     "es":"Color de escena n.º %d — uno de los 8 tonos de máximo contraste, ordenados por distinguibilidad a simple vista."%r,
     "it":"Colore scena n.%d — una delle 8 tinte a massimo contrasto, ordinate per distinguibilità a colpo d'occhio."%r,
     "ja":"ステージ色 第%d位 — 一目での識別性で並べた最大コントラストの8色の一つ。"%r,
     "ko":"무대 색 %d위 — 한눈에 구별되는 순으로 정렬한 최대 대비 8색 중 하나."%r,
     "zh":"舞台色第 %d 位 — 按一眼可辨性排序的 8 种最大对比色之一。"%r}
RAT={
"en":"**Why only 8 named colours?** Naming hundreds of colours is pointless: on a saturated stage LED, most would be indistinguishable and no one remembers 300 names. Instead we take the set of colours the eye can actually tell apart at a glance — **Kelly's colours of maximum contrast** (Kelly 1965), minus the achromatics, in Kelly's *prefix-optimal* order (the first N are the N most distinguishable). **5** is colour-blind-safe; **8** is the sweet spot (it overlaps Wong 2011's palette); beyond ~7–12, at-a-glance discrimination degrades (Healey 1996) — more so on a bright physical LED. So: 8 short, memorable, unmistakable names — not a wall of near-identical ones.",
"fr":"**Pourquoi seulement 8 couleurs nommées ?** Nommer des centaines de couleurs ne sert à rien : sur une LED de scène saturée, la plupart seraient indistinguables et personne ne retient 300 noms. On prend donc l'ensemble des couleurs que l'œil sait vraiment séparer d'un coup d'œil — **les couleurs de contraste maximal de Kelly** (Kelly 1965), sans les achromatiques, dans l'ordre *préfixe-optimal* de Kelly (les N premières sont les N plus distinguables). **5** est sûr pour les daltoniens ; **8** est le point idéal (recoupe la palette de Wong 2011) ; au-delà de ~7–12, la discrimination au premier coup d'œil se dégrade (Healey 1996) — encore plus sur une LED physique vive. Donc : 8 noms courts, mémorisables, sans ambiguïté — pas un mur de couleurs quasi identiques.",
"de":"**Warum nur 8 benannte Farben?** Hunderte Farben zu benennen ist sinnlos: Auf einer gesättigten Bühnen-LED wären die meisten ununterscheidbar. Wir nehmen die Farben, die das Auge auf einen Blick wirklich trennt — **Kellys Farben maximalen Kontrasts** (Kelly 1965), ohne Achromatische, in Kellys präfix-optimaler Reihenfolge. **5** ist farbenblind-sicher; **8** ist der Sweet Spot (überschneidet Wong 2011); jenseits von ~7–12 sinkt die Unterscheidbarkeit (Healey 1996).",
"es":"**¿Por qué solo 8 colores con nombre?** Nombrar cientos de colores es inútil: en un LED de escena saturado la mayoría serían indistinguibles. Tomamos los colores que el ojo distingue de un vistazo — **los colores de máximo contraste de Kelly** (Kelly 1965), sin los acromáticos, en orden prefijo-óptimo. **5** es seguro para daltónicos; **8** es el punto ideal (coincide con Wong 2011); más allá de ~7–12 la distinción se degrada (Healey 1996).",
"it":"**Perché solo 8 colori con nome?** Dare un nome a centinaia di colori è inutile: su un LED da palco saturo la maggior parte sarebbe indistinguibile. Prendiamo i colori che l'occhio separa a colpo d'occhio — **i colori a massimo contrasto di Kelly** (Kelly 1965), senza gli acromatici, in ordine prefisso-ottimale. **5** è sicuro per i daltonici; **8** è il punto ideale (coincide con Wong 2011); oltre ~7–12 la distinzione peggiora (Healey 1996).",
"ja":"**なぜ名前付きは8色だけ？** 何百もの色に名前を付けても無意味です。飽和したステージLEDでは大半が見分けられません。そこで一目で識別できる色 —**ケリーの最大コントラスト色**(Kelly 1965)から無彩色を除き、ケリーの接頭辞最適順に採用。**5**色は色覚多様性に安全、**8**色が最適点(Wong 2011と重なる)。約7〜12を超えると識別性が低下(Healey 1996)。",
"ko":"**왜 이름 붙인 색이 8개뿐인가?** 수백 개 색에 이름을 붙이는 것은 무의미합니다. 포화된 무대 LED에서는 대부분 구별되지 않습니다. 그래서 한눈에 구별되는 색 —**켈리의 최대 대비 색**(Kelly 1965)에서 무채색을 빼고 접두사 최적 순으로 사용. **5**색은 색맹 안전, **8**색이 최적점(Wong 2011과 겹침). 약 7~12를 넘으면 식별성이 떨어짐(Healey 1996).",
"zh":"**为何只命名 8 种颜色？** 给数百种颜色命名毫无意义：在饱和的舞台 LED 上大多无法区分。我们只取肉眼一眼可辨的颜色 —**Kelly 最大对比色**(Kelly 1965)去掉无彩色，按 Kelly 前缀最优顺序排列。**5** 色对色盲友好，**8** 色是最佳点（与 Wong 2011 重合）；超过约 7–12，可辨性下降(Healey 1996)。",
}
entries={}
os.makedirs(DST+"/images/colors",exist_ok=True)
def slug(n): return re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')
for name,rgb,rank,tr in COLORS:
    e={"rgb":list(rgb),"rank":rank,"en":{"name":name,"desc":rankdesc(rank)["en"]}}
    for lc in ("fr","de","es","it","ja","ko","zh"):
        e[lc]={"name":tr[lc],"desc":rankdesc(rank)[lc]}
    entries[name]=e
    # swatch
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120"><rect width="120" height="120" rx="16" fill="rgb(%d,%d,%d)"/></svg>'%rgb
    subprocess.run(["rsvg-convert","-o","%s/images/colors/%s.png"%(DST,slug(name)),"-"],input=svg.encode())
json.dump({"_note":"OpenLamp's 8 stage colours = Kelly's maximum-contrast palette (minus achromatics), prefix-optimal order. Key = English name; each has rgb, rank, and per-language {name, desc}. See _rationale.","_rationale":RAT,"entries":entries},
          open(DST+"/i18n/colors.json","w"),ensure_ascii=False,indent=1)
print("colors.json + 8 swatches")
