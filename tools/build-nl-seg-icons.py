_moon='<path d="M52 26 a22 22 0 1 0 2 44 a28 28 0 0 1 -2 -44 z" fill="#cfd8ff"/>'
_sun='<circle cx="42" cy="44" r="13" fill="#ffd200"/><g stroke="#ffd200" stroke-width="4" stroke-linecap="round"><line x1="42" y1="20" x2="42" y2="26"/><line x1="42" y1="62" x2="42" y2="68"/><line x1="18" y1="44" x2="24" y2="44"/><line x1="60" y1="44" x2="66" y2="44"/><line x1="25" y1="27" x2="29" y2="31"/><line x1="55" y1="57" x2="59" y2="61"/></g>'
NL={   # nightlight modes = a brightness-vs-time curve + moon/sun
"Instant":     _moon+'<path d="M22 92 L92 92 L92 124 L122 124" fill="none" stroke="#ffb454" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>',
"Fade":        _moon+'<path d="M22 88 L122 124" fill="none" stroke="#ffb454" stroke-width="7" stroke-linecap="round"/>',
"Colour fade": _moon+''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="9" stroke-linecap="round"/>'%(22+i*25,88+i*9,47+i*25,97+i*9,c) for i,c in enumerate(["#ffd200","#ff7d00","#e6002a","#8b5cf6"])),
"Sunrise":     _sun+'<path d="M22 124 L122 88" fill="none" stroke="#ffb454" stroke-width="7" stroke-linecap="round"/>',
}
SEG={  # segment actions
"Reverse":    '<path d="M28 56 H104 l-16 -16 M104 56 l-16 16" fill="none" stroke="#3399ff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><path d="M116 96 H40 l16 -16 M40 96 l16 16" fill="none" stroke="#3399ff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
"Mirror":     '<line x1="72" y1="24" x2="72" y2="120" stroke="#8b93a1" stroke-width="4" stroke-dasharray="8 7"/><path d="M60 44 L28 72 L60 100 Z" fill="#2ee06e"/><path d="M84 44 L116 72 L84 100 Z" fill="#2ee06e"/>',
"Freeze":     '<g stroke="#7dd8ff" stroke-width="8" stroke-linecap="round"><line x1="72" y1="22" x2="72" y2="122"/><line x1="29" y1="47" x2="115" y2="97"/><line x1="115" y1="47" x2="29" y2="97"/><line x1="72" y1="22" x2="62" y2="34"/><line x1="72" y1="22" x2="82" y2="34"/><line x1="72" y1="122" x2="62" y2="110"/><line x1="72" y1="122" x2="82" y2="110"/></g>',
"On/Off":     '<circle cx="72" cy="76" r="38" fill="none" stroke="#2ee06e" stroke-width="8"/><line x1="72" y1="30" x2="72" y2="72" stroke="#2ee06e" stroke-width="8" stroke-linecap="round"/>',
"Transition": '<circle cx="56" cy="72" r="30" fill="#3399ff"/><circle cx="88" cy="72" r="30" fill="#e6002a" opacity="0.65"/>',
"Sound sim":  '<path d="M34 60 H50 L72 40 V104 L50 84 H34 Z" fill="#ffb454"/><path d="M86 54 a26 26 0 0 1 0 36" fill="none" stroke="#ffb454" stroke-width="6" stroke-linecap="round"/><path d="M96 44 a40 40 0 0 1 0 56" fill="none" stroke="#ffb454" stroke-width="6" stroke-linecap="round"/>',
}
def wrapT(i): return '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">%s</svg>'%i
