import math
def _sl(pos=0.6,col="#4aa3ff"):  # generic slider
    x=24+pos*84
    return '<rect x="20" y="66" width="104" height="12" rx="6" fill="#5a6472"/><rect x="20" y="66" width="%d" height="12" rx="6" fill="%s"/><circle cx="%d" cy="72" r="15" fill="%s"/>'%(int(x-20),col,x,col)
_speed='<path d="M18 104 A54 54 0 0 1 126 104" fill="none" stroke="#5a6472" stroke-width="9" stroke-linecap="round"/><line x1="72" y1="104" x2="108" y2="58" stroke="#3399ff" stroke-width="7" stroke-linecap="round"/><circle cx="72" cy="104" r="10" fill="#3399ff"/>'
_bars="".join('<rect x="%d" y="%d" width="18" height="%d" rx="4" fill="#ffb454"/>'%(24+i*24,108-(28+i*22),28+i*22) for i in range(4))
_flame='<path d="M72 22 C96 58 100 70 90 92 C104 86 104 74 100 66 C118 96 106 128 72 128 C38 128 26 96 44 66 C40 74 40 86 54 92 C44 70 48 58 72 22 Z" fill="#ff5a1e"/>'
_snow='<g stroke="#7dd8ff" stroke-width="8" stroke-linecap="round"><line x1="72" y1="24" x2="72" y2="120"/><line x1="30" y1="48" x2="114" y2="96"/><line x1="114" y1="48" x2="30" y2="96"/></g>'
_sun='<circle cx="72" cy="72" r="24" fill="#ffd200"/><g stroke="#ffd200" stroke-width="6" stroke-linecap="round">'+"".join('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f"/>'%(72+math.cos(a)*34,72+math.sin(a)*34,72+math.cos(a)*44,72+math.sin(a)*44) for a in [math.radians(d) for d in range(0,360,45)])+'</g>'
_drop='<path d="M72 24 C94 58 98 70 88 90 C102 84 102 74 98 66 C114 94 104 126 72 126 C40 126 30 94 46 66 C42 74 42 84 56 90 C46 70 50 58 72 24 Z" fill="#e6002a"/>'
_dots='<g fill="#4aa3ff"><circle cx="40" cy="52" r="10"/><circle cx="72" cy="72" r="10"/><circle cx="104" cy="92" r="10"/><circle cx="104" cy="52" r="10"/><circle cx="40" cy="92" r="10"/></g>'
_multi='<g><circle cx="46" cy="60" r="13" fill="#e6002a"/><circle cx="72" cy="60" r="13" fill="#ffd200"/><circle cx="98" cy="60" r="13" fill="#2ee06e"/><circle cx="59" cy="88" r="13" fill="#3399ff"/><circle cx="85" cy="88" r="13" fill="#8b5cf6"/></g>'
_wind='<g fill="none" stroke="#a8e6ff" stroke-width="8" stroke-linecap="round"><path d="M24 54 H88 a14 14 0 1 0 -14 -14"/><path d="M24 80 H104 a14 14 0 1 1 -14 14"/><path d="M24 104 H74"/></g>'
_balls='<circle cx="48" cy="88" r="16" fill="#e6002a"/><circle cx="84" cy="70" r="16" fill="#2ee06e"/><circle cx="104" cy="98" r="12" fill="#ffd200"/>'
_dice='<rect x="34" y="34" width="76" height="76" rx="14" fill="#eef" /><g fill="#1a1a1a"><circle cx="54" cy="54" r="7"/><circle cx="90" cy="54" r="7"/><circle cx="72" cy="72" r="7"/><circle cx="54" cy="90" r="7"/><circle cx="90" cy="90" r="7"/></g>'
_wave='<path d="M14 72 Q34 40 54 72 T94 72 T134 72" fill="none" stroke="#4aa3ff" stroke-width="8" stroke-linecap="round"/>'
_rot='<path d="M100 44 A40 40 0 1 0 108 84" fill="none" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round"/><path d="M92 30 L108 44 L90 54 Z" fill="#8b5cf6"/>'
_arrowsH='<g stroke="#4aa3ff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"><line x1="26" y1="72" x2="118" y2="72"/><path d="M42 56 L26 72 L42 88"/><path d="M102 56 L118 72 L102 88"/></g>'
_arrowsV='<g stroke="#2ee06e" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"><line x1="72" y1="26" x2="72" y2="118"/><path d="M56 42 L72 26 L88 42"/><path d="M56 102 L72 118 L88 102"/></g>'
_expand='<g stroke="#ffb454" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"><path d="M30 58 V30 H58"/><path d="M114 58 V30 H86"/><path d="M30 86 V114 H58"/><path d="M114 86 V114 H86"/></g>'
_star='<path d="M72 22 l14 34 37 3 -28 24 9 36 -32 -20 -32 20 9 -36 -28 -24 37 -3 Z" fill="#ffd200"/>'
_ramp='<path d="M22 118 L118 40" fill="none" stroke="#4aa3ff" stroke-width="8" stroke-linecap="round"/><line x1="22" y1="118" x2="118" y2="118" stroke="#5a6472" stroke-width="4"/>'
_hash='<text x="72" y="96" font-family="Helvetica" font-weight="bold" font-size="80" fill="#4aa3ff" text-anchor="middle">#</text>'
_blur='<circle cx="72" cy="72" r="34" fill="#4aa3ff"/><circle cx="72" cy="72" r="46" fill="none" stroke="#4aa3ff" stroke-width="6" opacity="0.4"/><circle cx="72" cy="72" r="22" fill="#a8d4ff"/>'
ICONS={"slider":_sl(),"speed":_speed,"intensity":_bars,"flame":_flame,"snow":_snow,"sun":_sun,"drop":_drop,"dots":_dots,"multi":_multi,"wind":_wind,"balls":_balls,"dice":_dice,"wave":_wave,"rot":_rot,"arrowsh":_arrowsH,"arrowsv":_arrowsV,"expand":_expand,"star":_star,"ramp":_ramp,"hash":_hash,"blur":_blur}
def icon_key(lab):
    n=lab.lower()
    if n.startswith("# ") or "# of" in n or n.startswith("#"): return "hash"
    if "speed" in n: return "speed"
    if "intensity" in n or "amplif" in n or "boost" in n: return "intensity"
    if "blur" in n: return "blur"
    if "colors" in n or "colorful" in n or "palette" in n or "color bars" in n: return "multi"
    if "color" in n: return "drop"
    if "bright" in n: return "sun"
    if "cool" in n or "snow" in n or "ice" in n or "frost" in n: return "snow"
    if "fire" in n or "flame" in n or "heat" in n or "warm" in n or "spark" in n or "ember" in n: return "flame"
    if "wind" in n or "breeze" in n: return "wind"
    if "ball" in n or "blob" in n: return "balls"
    if "dot" in n or "pixel" in n or "star" in n or "twinkle" in n: return ("star" if ("star" in n or "twinkle" in n) else "dots")
    if "chance" in n or "random" in n or "probab" in n: return "dice"
    if "wave" in n or "freq" in n or "sine" in n or "sin" in n: return "wave"
    if "rotat" in n or "angle" in n or "spin" in n or "swirl" in n: return "rot"
    if "width" in n: return "arrowsh"
    if "height" in n: return "arrowsv"
    if "size" in n or "scale" in n or "zoom" in n or "spread" in n or "area" in n: return "expand"
    if "fade" in n or "blend" in n or "ramp" in n or "cozy" in n: return "ramp"
    return "slider"
def wrapT(i): return '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">%s</svg>'%i
