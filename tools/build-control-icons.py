import math
def _slider(pos,num,col):   # horizontal slider track + knob + number
    x=24+pos*84
    return ('<rect x="20" y="66" width="104" height="12" rx="6" fill="#5a6472"/>'
            '<rect x="20" y="66" width="%d" height="12" rx="6" fill="%s"/>'
            '<circle cx="%d" cy="72" r="17" fill="%s"/>'
            '<text x="%d" y="79" font-family="Helvetica" font-weight="bold" font-size="19" fill="#fff" text-anchor="middle">%s</text>'%(int((x-20)),col,x,col,x,num))
def _toggle(on,num,col):
    track= col if on else "#5a6472"; kx=94 if on else 50
    return ('<rect x="34" y="52" width="76" height="40" rx="20" fill="%s"/>'
            '<circle cx="%d" cy="72" r="16" fill="#fff"/>'
            '<text x="72" y="118" font-family="Helvetica" font-weight="bold" font-size="20" fill="%s" text-anchor="middle">%s</text>'%(track,kx,col,num))
def _swatch_drop(col):   # paint drop = effect (foreground) colour
    return '<path d="M72 20 C96 56 100 68 90 90 C104 84 104 72 100 64 C118 94 106 128 72 128 C38 128 26 94 44 64 C40 72 40 84 54 90 C44 68 48 56 72 20 Z" fill="%s"/>'%col
CTRL_ICONS={
"Speed": '<path d="M18 104 A54 54 0 0 1 126 104" fill="none" stroke="#5a6472" stroke-width="9" stroke-linecap="round"/>'
         '<g stroke="#8b93a1" stroke-width="4">'+"".join('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f"/>'%(72+math.cos(a)*54,104+math.sin(a)*54,72+math.cos(a)*44,104+math.sin(a)*44) for a in [math.radians(d) for d in (180,210,240,270,300,330,360)]) + '</g>'
         '<line x1="72" y1="104" x2="108" y2="58" stroke="#3399ff" stroke-width="7" stroke-linecap="round"/><circle cx="72" cy="104" r="10" fill="#3399ff"/>',
"Intensity": "".join('<rect x="%d" y="%d" width="18" height="%d" rx="4" fill="#ffb454"/>'%(24+i*24,108-(28+i*22),28+i*22) for i in range(4)),
"Custom 1": _slider(0.25,"1","#8b5cf6"),
"Custom 2": _slider(0.55,"2","#8b5cf6"),
"Custom 3": _slider(0.8,"3","#8b5cf6"),
"Option 1": _toggle(True,"1","#3bb4c9"),   # same toggle image, 3 colours (Benoit 2026-07-12)
"Option 2": _toggle(True,"2","#e0a44c"),
"Option 3": _toggle(True,"3","#8b5cf6"),
"Effect color": _swatch_drop("#e6002a"),
"Background color": '<rect x="22" y="30" width="100" height="84" rx="12" fill="#3399ff"/><rect x="46" y="52" width="52" height="40" rx="8" fill="#1a1a1a" opacity="0.25"/>',
"Custom color": '<circle cx="72" cy="72" r="40" fill="#2ee06e"/><path d="M72 72 L72 32 A40 40 0 0 1 106 92 Z" fill="#ffd200"/><path d="M72 72 L106 92 A40 40 0 0 1 38 92 Z" fill="#e6002a"/>',
"Palette": '<ellipse cx="70" cy="78" rx="50" ry="42" fill="#efe6d2"/><ellipse cx="96" cy="92" rx="13" ry="10" fill="#1a1a1a" opacity="0.35"/>'
           '<circle cx="52" cy="58" r="9" fill="#e6002a"/><circle cx="80" cy="52" r="9" fill="#ffd200"/><circle cx="100" cy="66" r="9" fill="#2ee06e"/><circle cx="46" cy="86" r="9" fill="#3399ff"/><circle cx="70" cy="98" r="9" fill="#8b5cf6"/>',
}
def wrapT(i): return '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">%s</svg>'%i
