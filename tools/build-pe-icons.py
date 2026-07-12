BE={
"Short press":'<circle cx="72" cy="72" r="24" fill="#4aa3ff"/><circle cx="72" cy="72" r="40" fill="none" stroke="#4aa3ff" stroke-width="6" opacity="0.5"/>',
"Long press":'<circle cx="72" cy="72" r="24" fill="#4aa3ff"/><circle cx="72" cy="72" r="40" fill="none" stroke="#4aa3ff" stroke-width="7" stroke-dasharray="150 90" transform="rotate(-90 72 72)" stroke-linecap="round"/><circle cx="112" cy="34" r="14" fill="#ffb454"/><line x1="112" y1="34" x2="112" y2="26" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round"/><line x1="112" y1="34" x2="119" y2="38" stroke="#1a1a1a" stroke-width="3" stroke-linecap="round"/>',
"Double press":'<circle cx="72" cy="72" r="22" fill="#4aa3ff"/><circle cx="72" cy="72" r="37" fill="none" stroke="#4aa3ff" stroke-width="6" opacity="0.6"/><circle cx="72" cy="72" r="52" fill="none" stroke="#4aa3ff" stroke-width="5" opacity="0.32"/>',
}
_clock='<circle cx="72" cy="72" r="38" fill="none" stroke="#4aa3ff" stroke-width="7"/><line x1="72" y1="72" x2="72" y2="48" stroke="#4aa3ff" stroke-width="7" stroke-linecap="round"/><line x1="72" y1="72" x2="92" y2="82" stroke="#4aa3ff" stroke-width="7" stroke-linecap="round"/>'
PR={
"Save preset":'<path d="M34 34 h64 l12 12 v64 h-76 Z" fill="#4aa3ff"/><path d="M72 58 l6 14 15 1 -11 10 3 15 -13 -8 -13 8 3 -15 -11 -10 15 -1 Z" fill="#ffd200"/>',
"Preset name":'<path d="M30 56 L78 56 L112 90 L78 124 L36 90 Z" fill="#8b5cf6"/><circle cx="54" cy="80" r="9" fill="#fff"/><rect x="74" y="66" width="30" height="8" rx="4" fill="#fff" opacity="0.7"/>',
"Quick load label":'<rect x="30" y="52" width="84" height="44" rx="10" fill="#2ee06e"/><text x="72" y="86" font-family="Helvetica" font-weight="bold" font-size="30" fill="#0b3a18" text-anchor="middle">QL</text>',
"Include brightness":'<circle cx="60" cy="66" r="18" fill="#ffd200"/><g stroke="#ffd200" stroke-width="5" stroke-linecap="round"><line x1="60" y1="40" x2="60" y2="46"/><line x1="60" y1="86" x2="60" y2="92"/><line x1="34" y1="66" x2="40" y2="66"/><line x1="80" y1="66" x2="86" y2="66"/></g><path d="M84 96 L98 110 L124 78" fill="none" stroke="#2ee06e" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>',
"Save segment bounds":'<rect x="34" y="58" width="30" height="28" rx="4" fill="#e6002a"/><rect x="80" y="58" width="30" height="28" rx="4" fill="#4aa3ff"/><path d="M26 46 L20 46 L20 98 L26 98" fill="none" stroke="#8b93a1" stroke-width="5"/><path d="M118 46 L124 46 L124 98 L118 98" fill="none" stroke="#8b93a1" stroke-width="5"/>',
"Use current state":'<rect x="26" y="48" width="92" height="62" rx="8" fill="#4aa3ff"/><rect x="58" y="38" width="28" height="14" rx="4" fill="#4aa3ff"/><circle cx="72" cy="80" r="20" fill="#0b2a4a"/><circle cx="72" cy="80" r="11" fill="#a8d4ff"/>',
"API command":'<path d="M52 48 L26 78 L52 108" fill="none" stroke="#8b5cf6" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M92 48 L118 78 L92 108" fill="none" stroke="#8b5cf6" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><line x1="80" y1="40" x2="64" y2="116" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round"/>',
"Playlist":'<g stroke="#4aa3ff" stroke-width="9" stroke-linecap="round"><line x1="26" y1="48" x2="86" y2="48"/><line x1="26" y1="72" x2="86" y2="72"/><line x1="26" y1="96" x2="64" y2="96"/></g><path d="M92 82 L92 114 L120 98 Z" fill="#2ee06e"/>',
"Duration":_clock,
"Transition":'<circle cx="56" cy="72" r="30" fill="#3399ff"/><circle cx="88" cy="72" r="30" fill="#e6002a" opacity="0.65"/>',
"Repeat":'<path d="M40 56 H98 a20 20 0 0 1 0 40 H60" fill="none" stroke="#2ee06e" stroke-width="8" stroke-linecap="round"/><path d="M74 40 L40 56 L74 72 Z" fill="#2ee06e"/>',
"Shuffle":'<g fill="none" stroke="#8b5cf6" stroke-width="8" stroke-linecap="round"><path d="M26 52 H50 L96 96 H118"/><path d="M26 96 H50 L96 52 H118"/></g><path d="M106 40 L122 52 L106 64 Z" fill="#8b5cf6"/><path d="M106 84 L122 96 L106 108 Z" fill="#8b5cf6"/>',
"End preset":'<rect x="34" y="44" width="56" height="56" rx="8" fill="#e6002a"/><g stroke="#ffb454" stroke-width="9" stroke-linecap="round"><line x1="104" y1="44" x2="104" y2="100"/></g>',
}
CONCEPT_EXTRA={
"button-events":'<circle cx="66" cy="72" r="22" fill="#4aa3ff"/><circle cx="66" cy="72" r="36" fill="none" stroke="#4aa3ff" stroke-width="6" opacity="0.5"/><text x="112" y="52" font-family="Helvetica" font-weight="bold" font-size="26" fill="#4aa3ff" text-anchor="middle">×</text>',
"presets":'<path d="M34 34 h64 l12 12 v64 h-76 Z" fill="#4aa3ff"/><path d="M72 58 l6 14 15 1 -11 10 3 15 -13 -8 -13 8 3 -15 -11 -10 15 -1 Z" fill="#ffd200"/>',
}
def wrapT(i): return '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144" viewBox="0 0 144 144">%s</svg>'%i
