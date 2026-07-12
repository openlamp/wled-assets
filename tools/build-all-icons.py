import math
def _gear():
    o='<circle cx="72" cy="72" r="20" fill="none" stroke="#8b93a1" stroke-width="9"/>'
    for k in range(8):
        a=k/8*2*math.pi; o+='<rect x="66" y="20" width="12" height="16" rx="2" fill="#8b93a1" transform="rotate(%.0f 72 72)"/>'%(a*57.3)
    return o
BTN={
"Push":'<circle cx="72" cy="72" r="42" fill="none" stroke="#8b93a1" stroke-width="7"/><circle cx="72" cy="72" r="24" fill="#4aa3ff"/>',
"Push inverted":'<circle cx="72" cy="72" r="42" fill="#4aa3ff"/><circle cx="72" cy="72" r="24" fill="none" stroke="#fff" stroke-width="7"/>',
"Switch":'<rect x="30" y="54" width="84" height="40" rx="20" fill="#2ee06e"/><circle cx="94" cy="74" r="16" fill="#fff"/>',
"PIR sensor":'<circle cx="72" cy="94" r="15" fill="#ffb454"/><g stroke="#ffb454" stroke-width="6" fill="none" stroke-linecap="round"><path d="M50 72 a30 30 0 0 1 44 0"/><path d="M40 56 a44 44 0 0 1 64 0"/></g>',
"Touch":'<rect x="62" y="34" width="20" height="58" rx="10" fill="#ffd2a8"/><g fill="none" stroke="#4aa3ff" stroke-width="5" stroke-linecap="round"><path d="M96 60 a20 20 0 0 1 0 28"/><path d="M106 50 a34 34 0 0 1 0 48"/></g>',
"Analog":'<circle cx="72" cy="72" r="38" fill="none" stroke="#8b93a1" stroke-width="7"/><line x1="72" y1="72" x2="98" y2="46" stroke="#4aa3ff" stroke-width="8" stroke-linecap="round"/><circle cx="72" cy="72" r="9" fill="#4aa3ff"/>',
}
INFO={
"Uptime":'<circle cx="72" cy="72" r="40" fill="none" stroke="#4aa3ff" stroke-width="7"/><line x1="72" y1="72" x2="72" y2="46" stroke="#4aa3ff" stroke-width="7" stroke-linecap="round"/><line x1="72" y1="72" x2="94" y2="82" stroke="#4aa3ff" stroke-width="7" stroke-linecap="round"/>',
"Free memory":'<rect x="42" y="42" width="60" height="60" rx="8" fill="#4aa3ff"/><rect x="54" y="54" width="36" height="36" rx="4" fill="#eef"/><g stroke="#4aa3ff" stroke-width="5">'+"".join('<line x1="%d" y1="36" x2="%d" y2="42"/><line x1="%d" y1="102" x2="%d" y2="108"/>'%(52+i*14,52+i*14,52+i*14,52+i*14) for i in range(3))+'</g>',
"Signal strength":'<g fill="#2ee06e"><rect x="34" y="88" width="16" height="20" rx="3"/><rect x="58" y="72" width="16" height="36" rx="3"/><rect x="82" y="52" width="16" height="56" rx="3"/></g>',
"Frames per second":'<path d="M18 104 A54 54 0 0 1 126 104" fill="none" stroke="#5a6472" stroke-width="9" stroke-linecap="round"/><line x1="72" y1="104" x2="108" y2="58" stroke="#2ee06e" stroke-width="7" stroke-linecap="round"/><circle cx="72" cy="104" r="10" fill="#2ee06e"/>',
"Estimated current":'<path d="M84 20 L44 78 L68 78 L54 124 L104 62 L78 62 Z" fill="#ffd200"/>',
"LED count":'<circle cx="72" cy="62" r="26" fill="#ffd200"/><rect x="58" y="86" width="28" height="18" rx="4" fill="#8b93a1"/><rect x="62" y="104" width="20" height="8" rx="2" fill="#8b93a1"/>',
"Environment":'<rect x="32" y="46" width="80" height="52" rx="6" fill="#2ee06e"/><circle cx="54" cy="72" r="6" fill="#0b3a18"/><circle cx="90" cy="72" r="6" fill="#0b3a18"/><rect x="66" y="66" width="12" height="12" fill="#0b3a18"/>',
"Filesystem":'<path d="M26 52 h30 l8 10 h52 v44 a5 5 0 0 1 -5 5 h-80 a5 5 0 0 1 -5 -5 Z" fill="#ffb454"/>',
"MAC address":'<circle cx="72" cy="42" r="12" fill="#4aa3ff"/><circle cx="42" cy="100" r="12" fill="#4aa3ff"/><circle cx="102" cy="100" r="12" fill="#4aa3ff"/><g stroke="#4aa3ff" stroke-width="5"><line x1="72" y1="54" x2="42" y2="88"/><line x1="72" y1="54" x2="102" y2="88"/></g>',
"IP address":'<circle cx="72" cy="72" r="40" fill="none" stroke="#4aa3ff" stroke-width="5"/><ellipse cx="72" cy="72" rx="18" ry="40" fill="none" stroke="#4aa3ff" stroke-width="4"/><line x1="32" y1="72" x2="112" y2="72" stroke="#4aa3ff" stroke-width="4"/><line x1="40" y1="52" x2="104" y2="52" stroke="#4aa3ff" stroke-width="3"/><line x1="40" y1="92" x2="104" y2="92" stroke="#4aa3ff" stroke-width="3"/>',
"WiFi channel":'<g fill="none" stroke="#4aa3ff" stroke-width="8" stroke-linecap="round"><path d="M38 64 a48 48 0 0 1 68 0"/><path d="M52 82 a28 28 0 0 1 40 0"/></g><circle cx="72" cy="98" r="8" fill="#4aa3ff"/>',
"Version":'<path d="M34 58 L76 58 L110 92 L76 126 L42 92 Z" fill="#8b5cf6"/><circle cx="58" cy="82" r="9" fill="#fff"/>',
}
UI={
"Colors":'<circle cx="52" cy="58" r="17" fill="#e6002a"/><circle cx="92" cy="58" r="17" fill="#2ee06e"/><circle cx="72" cy="92" r="17" fill="#4aa3ff"/>',
"Effects":'<path d="M72 22 l11 32 32 11 -32 11 -11 32 -11 -32 -32 -11 32 -11 Z" fill="#ffd200"/>',
"Segments":'<rect x="18" y="58" width="30" height="28" rx="5" fill="#e6002a"/><rect x="56" y="58" width="30" height="28" rx="5" fill="#2ee06e"/><rect x="94" y="58" width="30" height="28" rx="5" fill="#4aa3ff"/>',
"Presets":'<path d="M72 22 l14 34 37 3 -28 24 9 36 -32 -20 -32 20 9 -36 -28 -24 37 -3 Z" fill="#ffd200"/>',
"Settings":_gear(),
"Info":'<circle cx="72" cy="72" r="40" fill="#4aa3ff"/><circle cx="72" cy="52" r="6" fill="#fff"/><rect x="66" y="64" width="12" height="36" rx="4" fill="#fff"/>',
"Brightness":'<circle cx="72" cy="72" r="22" fill="#ffd200"/><g stroke="#ffd200" stroke-width="6" stroke-linecap="round">'+"".join('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f"/>'%(72+math.cos(a)*32,72+math.sin(a)*32,72+math.cos(a)*44,72+math.sin(a)*44) for a in [math.radians(d) for d in range(0,360,45)])+'</g>',
"Save":'<path d="M34 34 h64 l12 12 v64 h-76 Z" fill="#4aa3ff"/><rect x="50" y="34" width="40" height="24" fill="#eef"/><rect x="50" y="72" width="44" height="30" rx="3" fill="#eef"/><rect x="76" y="38" width="10" height="16" fill="#4aa3ff"/>',
"Delete":'<rect x="46" y="50" width="52" height="62" rx="6" fill="#e6002a"/><rect x="36" y="40" width="72" height="12" rx="4" fill="#e6002a"/><rect x="58" y="32" width="28" height="12" rx="4" fill="#e6002a"/>',
"Rename":'<path d="M38 106 L42 84 L98 28 L116 46 L60 102 Z" fill="#ffb454"/><path d="M98 28 L116 46" stroke="#8a5a1a" stroke-width="4"/>',
"Add segment":'<line x1="72" y1="34" x2="72" y2="110" stroke="#2ee06e" stroke-width="13" stroke-linecap="round"/><line x1="34" y1="72" x2="110" y2="72" stroke="#2ee06e" stroke-width="13" stroke-linecap="round"/>',
"Duplicate":'<rect x="38" y="40" width="46" height="58" rx="6" fill="none" stroke="#4aa3ff" stroke-width="6"/><rect x="60" y="56" width="46" height="58" rx="6" fill="#4aa3ff"/>',
"Reset":'<path d="M104 54 A40 40 0 1 0 110 86" fill="none" stroke="#4aa3ff" stroke-width="8" stroke-linecap="round"/><path d="M90 36 L110 52 L88 62 Z" fill="#4aa3ff"/>',
"Apply":'<path d="M40 74 L64 98 L106 48" fill="none" stroke="#2ee06e" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>',
"Timer":'<path d="M34 20 L110 20 L78 72 L110 124 L34 124 L66 72 Z" fill="none" stroke="#ffb454" stroke-width="6"/><path d="M50 108 L94 108 L78 84 L66 84 Z" fill="#ffb454"/>',
"Sync":'<g fill="none" stroke="#4aa3ff" stroke-width="8" stroke-linecap="round"><path d="M40 62 A32 32 0 0 1 100 54"/><path d="M104 82 A32 32 0 0 1 44 90"/></g><path d="M98 40 L104 56 L88 58 Z" fill="#4aa3ff"/><path d="M46 104 L40 88 L56 86 Z" fill="#4aa3ff"/>',
"Live":'<circle cx="72" cy="72" r="12" fill="#e6002a"/><g fill="none" stroke="#e6002a" stroke-width="6"><circle cx="72" cy="72" r="26"/><circle cx="72" cy="72" r="40"/></g>',
"Peek":'<path d="M22 72 Q72 34 122 72 Q72 110 22 72 Z" fill="none" stroke="#4aa3ff" stroke-width="6"/><circle cx="72" cy="72" r="15" fill="#4aa3ff"/>',
"Reboot":'<circle cx="72" cy="76" r="36" fill="none" stroke="#ffb454" stroke-width="8"/><line x1="72" y1="30" x2="72" y2="72" stroke="#ffb454" stroke-width="8" stroke-linecap="round"/>',
"Discover devices":'<circle cx="72" cy="72" r="44" fill="none" stroke="#2ee06e" stroke-width="4"/><circle cx="72" cy="72" r="26" fill="none" stroke="#2ee06e" stroke-width="3"/><line x1="72" y1="72" x2="108" y2="52" stroke="#2ee06e" stroke-width="5"/><circle cx="96" cy="88" r="6" fill="#2ee06e"/>',
}
CONCEPT={
"palettes":'<ellipse cx="70" cy="78" rx="50" ry="42" fill="#efe6d2"/><ellipse cx="96" cy="92" rx="13" ry="10" fill="#1a1a1a" opacity="0.35"/><circle cx="52" cy="58" r="9" fill="#e6002a"/><circle cx="80" cy="52" r="9" fill="#ffd200"/><circle cx="100" cy="66" r="9" fill="#2ee06e"/><circle cx="46" cy="86" r="9" fill="#3399ff"/><circle cx="70" cy="98" r="9" fill="#8b5cf6"/>',
"effects":'<path d="M72 22 l11 32 32 11 -32 11 -11 32 -11 -32 -32 -11 32 -11 Z" fill="#ffd200"/><circle cx="112" cy="40" r="7" fill="#e6002a"/><circle cx="34" cy="104" r="6" fill="#4aa3ff"/>',
"controls":"".join('<rect x="20" y="%d" width="104" height="10" rx="5" fill="#5a6472"/><circle cx="%d" cy="%d" r="12" fill="%s"/>'%(44+i*32,40+i*30,49+i*32,c) for i,c in enumerate(["#3399ff","#8b5cf6","#2ee06e"])),
"nightlight":'<path d="M56 24 a24 24 0 1 0 2 48 a30 30 0 0 1 -2 -48 z" fill="#cfd8ff"/><circle cx="98" cy="44" r="4" fill="#cfd8ff"/><circle cx="108" cy="64" r="3" fill="#cfd8ff"/>',
"segment":'<rect x="18" y="58" width="30" height="28" rx="5" fill="#e6002a"/><rect x="56" y="58" width="30" height="28" rx="5" fill="#2ee06e"/><rect x="94" y="58" width="30" height="28" rx="5" fill="#4aa3ff"/>',
"buttons":'<circle cx="72" cy="72" r="42" fill="none" stroke="#8b93a1" stroke-width="7"/><circle cx="72" cy="72" r="24" fill="#4aa3ff"/>',
"fxdata":'<rect x="20" y="54" width="104" height="10" rx="5" fill="#5a6472"/><circle cx="60" cy="59" r="13" fill="#4aa3ff"/><rect x="34" y="80" width="76" height="16" rx="4" fill="#8b93a1"/>',
"info":'<circle cx="72" cy="72" r="40" fill="#4aa3ff"/><circle cx="72" cy="52" r="6" fill="#fff"/><rect x="66" y="64" width="12" height="36" rx="4" fill="#fff"/>',
"ui":'<rect x="24" y="34" width="96" height="76" rx="8" fill="none" stroke="#8b93a1" stroke-width="6"/><rect x="24" y="34" width="96" height="20" rx="8" fill="#8b93a1"/><circle cx="38" cy="44" r="4" fill="#fff"/><rect x="40" y="66" width="30" height="30" rx="4" fill="#4aa3ff"/>',
}
def wrapT(i): return '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">%s</svg>'%i
