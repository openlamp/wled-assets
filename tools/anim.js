// Reference: per-effect UNIQUE animation for the WLED motion vocabulary (~62 motions).
// motion(name) -> a motion string ; anim(phase, motion, seed) -> inner SVG (viewBox 0 0 144
// 144). seed = the effect's index -> distinct hue/speed/direction/density. Advance phase ~7 fps.
// Canonical reference: tools/motions.py. No rgba() (some SVG renderers drop alpha).
function hsv(h,s,v){s=Math.min(s,0.62);v=Math.max(0,Math.min(0.92,v));h=((h%1)+1)%1;h*=6;const i=Math.floor(h),f=h-i,p=v*(1-s),q=v*(1-s*f),t=v*(1-s*(1-f));
 const a=[[v,t,p],[q,v,p],[p,v,t],[p,q,v],[t,p,v],[v,p,q]][i%6];
 return 'rgb('+Math.round(a[0]*255)+','+Math.round(a[1]*255)+','+Math.round(a[2]*255)+')';}
function motion(name){
 const n=(name||'').toLowerCase(),h=(...k)=>k.some(x=>n.includes(x));
 if(h('glitter'))return'glitter';if(h('chunchun'))return'birds';if(h('dna'))return'dna';if(h('halloween eyes','icu'))return'eye';if(h('lake'))return'ripple';if(h('volcano'))return'fire';
 if(h('solid','static','fill'))return'solid';
 if(h('police'))return'police';if(h('lightning'))return'lightning';
 if(h('popcorn'))return'popcorn';if(h('firework'))return'fireworks';
 if(h('heart'))return'heartbeat';
 if(h('bounc','ball','juggle','gravcen','gravfreq','gravimeter'))return'bounce';
 if(h('comet','meteor','shooting','sinelon'))return'comet';
 if(h('ghost rider','ghost'))return'ghost';
 if(h('two dots','two areas'))return'dots';if(h('traffic'))return'traffic';
 if(h('washing machine','rotozoom'))return'spin';
 if(h('spaceship','ufo','saturn'))return'spaceship';
 if(h('bee','crazy bees'))return'bees';if(h('octopus'))return'octopus';
 if(h('pacman','pac-man'))return'pacman';if(h('dj light','disco'))return'dj';
 if(h('scrolling text','text'))return'text';if(h('black hole','blackhole'))return'blackhole';
 if(h('galaxy','vortex','swirl','drift rose','spiral'))return'galaxy';
 if(h('hourglass'))return'hourglass';if(h('tv sim','tv '))return'tv';
 if(h('bpm'))return'beat';if(h('impact','sonic boom','colored burst'))return'impact';
 if(h('akemi'))return'akemi';if(h('halloween'))return'halloween';if(h('candle'))return'candle';
 if(h('fairy'))return'fairy';if(h('spot'))return'spots';if(h('plasma'))return'plasma';
 if(h('aurora','polar'))return'aurora';if(h('stream','flow','river'))return'stream';
 if(h('drip','drop'))return'drip';if(h('percent'))return'percent';
 if(h('phased','phase'))return'phased';if(h('loading','load'))return'loading';
 if(h('dancing','dance'))return'dancing';if(h('gradient','tricolor'))return'gradient';
 if(h('blob','soap','clouds','plasmoid'))return'plasma';
 if(h('tetri'))return'tetris';if(h('wipe'))return'wipe';
 if(h('android','larson','knight','scanner','scan'))return'scan';
 if(h('saw'))return'saw';if(h('dynamic','random colors'))return'dynamic';
 if(h('rainbow'))return'rainbow';if(h('running','runner'))return'running';
 if(h('sweep'))return'sweep';if(h('matri','game of life','dna','pixel'))return'matrix';
 if(h('snow','frost','ice'))return'snow';if(h('rain','waterfall','puddle','fall'))return'rain';
 if(h('fire','flame','lava','ember','glow'))return'fire';
 if(h('lighthouse','rotat'))return'lighthouse';if(h('sunrise','sunset','sun ','day'))return'sunrise';
 if(h('twinkle','star','firefl'))return'twinkle';if(h('sparkle','dissolve','flicker'))return'sparkle';
 if(h('ripple','pacifica','water','liquid','fluid','freq','geq'))return'ripple';
 if(h('colorful','colorwave','colortwinkle'))return'colorful';if(h('fade'))return'fade';
 if(h('breathe','breath','pulse','sine','blend'))return'breathe';
 if(h('blink'))return'blink';if(h('strobe','stutter','hyper'))return'strobe';
 if(h('chase','marquee','railway','theater','train'))return'chase';
 if(h('colorloop','pride','cycle','hue','spectrum','palette'))return'colorloop';
 if(h('noise'))return'sparkle';
 if(h('lissajou'))return'lissajous';
 return'wave';
}
function _flame(cx,hh,col,base){base=base||124;const w=hh*0.30,top=base-hh;
 return `<path d="M${cx} ${base} C${(cx-w)|0} ${(base-hh*0.4)|0} ${(cx-w*0.55)|0} ${(base-hh*0.78)|0} ${cx} ${top|0} C${(cx+w*0.55)|0} ${(base-hh*0.78)|0} ${(cx+w)|0} ${(base-hh*0.4)|0} ${cx} ${base} Z" fill="${col}"/>`;}
function _mhue(m){const f={octopus:0.74,dj:0.72,galaxy:0.70,blackhole:0.67,plasma:0.73,fairy:0.80,wave:0.52,ripple:0.52,stream:0.52,drip:0.53,comet:0.55,dots:0.55,chase:0.54,spin:0.55,spaceship:0.56,hourglass:0.50,phased:0.58,loading:0.55,text:0.54,wipe:0.53,lissajous:0.50,breathe:0.57,fade:0.54,percent:0.36,blink:0.09,birds:0.55,dna:0.52,eye:0.09,scan:0.02,saw:0.09,solid:0.09,lighthouse:0.09,spots:0.11,bounce:0.09,impact:0.03,running:0.08,dancing:0.95,colorful:0.09,gradient:0.09};return (m in f)?f[m]:0.09;}
function anim(ph,m,seed){
 seed=seed||0;const M=Math;
 const spd=0.55+((seed*13)%110)/100,dr=(M.floor(seed/2)%2)?1:-1,n=5+(seed%4),p=ph*spd*dr,h0=_mhue(m),sat=0.58;
 if(m==='solid')return `<rect x="24" y="24" width="96" height="96" rx="16" fill="${hsv(h0,sat,.85)}"/><rect x="40" y="40" width="48" height="30" rx="14" fill="${hsv(h0,sat*0.5,1)}"/>`;
 if(m==='fade'){const v=0.15+0.85*(0.5+0.5*M.sin(p*0.7));return `<rect x="24" y="34" width="96" height="76" rx="14" fill="${hsv(h0,sat,v)}"/>`;}
 if(m==='breathe'){const br=0.5+0.5*M.sin(p*0.6),r=26+30*br;return `<circle cx="72" cy="72" r="${(r+14)|0}" fill="none" stroke="${hsv(h0,.5,br)}" stroke-width="4"/><circle cx="72" cy="72" r="${r|0}" fill="${hsv(h0,sat*0.85,0.5+0.5*br)}"/>`;}
 if(m==='colorful'){let o='';for(let i=0;i<6;i++)o+=`<rect x="${16+i*19}" y="34" width="18" height="76" fill="${hsv(h0+i/6+ph*0.02*spd,.55,.9)}"/>`;return o;}
 if(m==='gradient'){let o='';for(let i=0;i<24;i++)o+=`<rect x="${(12+i*5).toFixed(1)}" y="40" width="5.5" height="64" fill="${hsv(h0+i*0.03+ph*0.02*spd,.55,.9)}"/>`;return o;}
 if(m==='police'){const a=ph%2,l=a===0?hsv(0,.9,1):'#20242c',r=a===1?hsv(.62,.9,1):'#20242c';return `<rect x="14" y="30" width="54" height="84" rx="10" fill="${l}"/><rect x="76" y="30" width="54" height="84" rx="10" fill="${r}"/>`;}
 if(m==='lightning'){const c=((ph*spd|0)%3===0)?hsv(.15,.5,1):'#2a2f38';return `<path d="M84 16 L44 78 L68 78 L54 128 L104 60 L78 60 Z" fill="${c}"/>`;}
 if(m==='popcorn'){let o='';for(let i=0;i<6;i++){const ph2=ph*spd+i*1.7,pop=M.abs(M.sin(ph2)),x=20+i*20,y=118-pop*pop*92;o+=`<circle cx="${x}" cy="${y|0}" r="${pop>0.5?8:6}" fill="${pop>0.4?'#fff6d8':'#c9a24a'}"/>`;}return o+'<rect x="10" y="116" width="124" height="14" rx="3" fill="#7a4a12"/>';}
 if(m==='fireworks'){const t=(ph%10)/10;if(t<0.35){const y=124-t/0.35*70;return `<circle cx="72" cy="${y|0}" r="4" fill="${hsv(h0,.3,1)}"/><rect x="70" y="${(y+6)|0}" width="4" height="16" fill="${hsv(h0,.5,.6)}"/>`;}const tt=(t-0.35)/0.65,rad=6+tt*52;let o='';for(let i=0;i<12;i++){const a=i/12*2*M.PI;o+=`<circle cx="${(72+M.cos(a)*rad)|0}" cy="${(54+M.sin(a)*rad)|0}" r="${M.max(1,5*(1-tt))}" fill="${hsv(h0+i*0.03,.9,1-tt*0.6)}"/>`;}return o;}
 if(m==='heartbeat'){const s=1+0.18*M.sin(p*1.6);return `<g transform="translate(72 78) scale(${s}) translate(-72 -78)"><path d="M72 108 C24 72 30 36 54 36 C66 36 72 46 72 52 C72 46 78 36 90 36 C114 36 120 72 72 108 Z" fill="${hsv(0.98,.85,1)}"/></g>`;}
 if(m==='bounce'){let o='';for(let i=0;i<3;i++){const bph=M.abs(M.sin(p*0.7+i*1.0)),x=34+i*38,y=108-bph*72,sq=1-0.2*(1-bph);o+=`<ellipse cx="${x}" cy="116" rx="${14-(bph*6|0)}" ry="4" fill="#00000030"/><ellipse cx="${x}" cy="${y|0}" rx="${(14/sq)|0}" ry="${(14*sq)|0}" fill="${hsv(h0+i*0.14,.85,1)}"/>`;}return o;}
 if(m==='comet'){const x=((ph*7*spd|0)%168)-12;let o='';for(let k=0;k<6;k++)o+=`<circle cx="${(x-k*10*dr)|0}" cy="72" r="${10-k*1.4}" fill="${hsv(h0,.7,1-k*0.15)}"/>`;return o;}
 if(m==='drip'){const t=((ph*spd)%7)/7,col=hsv(h0+0.55,.6,1);let o=`<rect x="52" y="12" width="40" height="12" rx="4" fill="${hsv(h0+0.55,.3,.6)}"/>`;if(t<0.55){const g=t/0.55,ry=16+g*22;o+=`<path d="M72 24 C52 24 52 ${(24+ry*0.6)|0} 72 ${(24+ry)|0} C92 ${(24+ry*0.6)|0} 92 24 72 24 Z" fill="${col}"/>`;}else{const fy=24+(t-0.55)/0.45*96;o+=`<path d="M72 ${fy|0} C58 ${(fy+8)|0} 58 ${(fy+22)|0} 72 ${(fy+30)|0} C86 ${(fy+22)|0} 86 ${(fy+8)|0} 72 ${fy|0} Z" fill="${col}"/>`;}return o+`<ellipse cx="72" cy="128" rx="20" ry="4" fill="${hsv(h0+0.55,.4,.5)}"/>`;}
 if(m==='ghost'){const x=72+M.sin(p*0.5)*36,col=hsv(h0,.25,1);return `<path d="M${(x-30)|0} 40 a30 30 0 0 1 30 30 v34 l-8 -8 -8 8 -7 -8 -7 8 -8 -8 -8 8 v-34 a30 30 0 0 1 30 -30 Z" fill="${col}"/><circle cx="${(x-10)|0}" cy="66" r="5" fill="#1a1a1a"/><circle cx="${(x+10)|0}" cy="66" r="5" fill="#1a1a1a"/>`;}
 if(m==='dots'){let o='';for(let i=0;i<2;i++)o+=`<circle cx="${(72+M.cos(p*0.7+i*M.PI)*44)|0}" cy="${(72+M.sin(p*0.9+i*M.PI)*40)|0}" r="16" fill="${hsv(h0+i*0.4,.8,1)}"/>`;return o;}
 if(m==='traffic'){const lit=(ph*spd|0)%3,c=[lit===0?'#e6002a':'#3a1015',lit===1?'#ffcc00':'#3a3410',lit===2?'#2ee06e':'#123a20'];let o='<rect x="52" y="14" width="40" height="116" rx="12" fill="#111"/>';for(let i=0;i<3;i++)o+=`<circle cx="72" cy="${38+i*34}" r="14" fill="${c[i]}"/>`;return o;}
 if(m==='spin'){const a=p*0.6;let o=`<circle cx="72" cy="72" r="46" fill="none" stroke="${hsv(h0,.4,.7)}" stroke-width="6"/>`;for(let k=0;k<4;k++)o+=`<rect x="66" y="72" width="12" height="42" rx="4" fill="${hsv(h0+k*0.08,.7,1)}" transform="rotate(${(a+k*M.PI/2)*57.3} 72 72)"/>`;return o;}
 if(m==='spaceship'){const x=((ph*6*spd|0)%180)-18;return `<g transform="translate(${x|0} 72)"><ellipse cx="0" cy="0" rx="34" ry="12" fill="${hsv(h0,.5,.9)}"/><ellipse cx="0" cy="-8" rx="16" ry="12" fill="${hsv(h0+0.1,.3,1)}"/><circle cx="-16" cy="2" r="3" fill="#fff"/><circle cx="0" cy="4" r="3" fill="#fff"/><circle cx="16" cy="2" r="3" fill="#fff"/></g>`;}
 if(m==='bees'){let o='';for(let i=0;i<5;i++){const x=72+M.sin(p*1.3+i*2.1)*50,y=72+M.cos(p*1.7+i*1.3)*46;o+=`<circle cx="${x|0}" cy="${y|0}" r="8" fill="${hsv(0.14,.9,1)}"/><ellipse cx="${x|0}" cy="${(y-2)|0}" rx="10" ry="5" fill="none" stroke="#ffffff44" stroke-width="1"/>`;}return o;}
 if(m==='octopus'){let o=`<circle cx="72" cy="60" r="24" fill="${hsv(h0,.6,1)}"/>`;for(let k=0;k<6;k++){const a=k/6*2*M.PI,sw=M.sin(p*0.8+k)*16;o+=`<path d="M72 78 Q${(72+M.cos(a)*20+sw)|0} 104 ${(72+M.cos(a)*40+sw)|0} 124" fill="none" stroke="${hsv(h0,.6,1)}" stroke-width="7" stroke-linecap="round"/>`;}return o;}
 if(m==='pacman'){const x=((ph*6*spd|0)%176)-16,mo2=M.abs(M.sin(p*1.4))*40;let o=`<path d="M${x|0} 72 L${(x+34*M.cos(mo2/57.3))|0} ${(72-34*M.sin(mo2/57.3))|0} A34 34 0 1 0 ${(x+34*M.cos(mo2/57.3))|0} ${(72+34*M.sin(mo2/57.3))|0} Z" fill="#ffd200"/>`;for(let d=0;d<3;d++){const dx=x+50+d*26;if(dx<150)o+=`<circle cx="${dx|0}" cy="72" r="6" fill="#ffe680"/>`;}return o;}
 if(m==='dj'){const a=p*0.8;return `<circle cx="72" cy="72" r="46" fill="#222"/><circle cx="72" cy="72" r="46" fill="none" stroke="${hsv(h0,.7,1)}" stroke-width="4"/><circle cx="72" cy="72" r="14" fill="${hsv(h0+0.3,.7,1)}"/><rect x="70" y="30" width="4" height="42" fill="#fff" transform="rotate(${a*57.3} 72 72)"/>`;}
 if(m==='text'){let o='';const off=(ph*7*spd|0)%40;for(let i=0;i<5;i++)o+=`<rect x="${(140-i*32-off)|0}" y="52" width="20" height="40" rx="3" fill="${hsv(h0+i*0.1,.7,1)}"/>`;return o;}
 if(m==='blackhole'){let o='<circle cx="72" cy="72" r="16" fill="#000"/>';for(let k=0;k<3;k++)o+=`<circle cx="72" cy="72" r="${M.max(2,48-((ph*3*spd+k*16)%44))}" fill="none" stroke="${hsv(h0+k*0.1,.7,1)}" stroke-width="5"/>`;return o;}
 if(m==='galaxy'){let o='';for(let k=0;k<14;k++){const t=k/14,a=p*0.5+t*6.5,r=12+t*54;o+=`<circle cx="${(72+M.cos(a)*r)|0}" cy="${(72+M.sin(a)*r)|0}" r="${5-t*3}" fill="${hsv(h0+t*0.4,.7,1)}"/>`;}return o;}
 if(m==='hourglass'){let o=`<path d="M34 20 L110 20 L78 72 L110 124 L34 124 L66 72 Z" fill="none" stroke="${hsv(h0,.4,.8)}" stroke-width="5"/>`;o+=`<circle cx="72" cy="${(72+((ph*4*spd|0)%40))|0}" r="5" fill="${hsv(0.1,.8,1)}"/><path d="M50 108 L94 108 L78 84 L66 84 Z" fill="${hsv(0.1,.7,1)}"/>`;return o;}
 if(m==='tv'){let o='';for(let r=0;r<4;r++)for(let c=0;c<4;c++){const v=((r*4+c)*13+(ph*9*spd|0)+seed*7)%100/100;o+=`<rect x="${16+c*28}" y="${16+r*28}" width="30" height="30" fill="${hsv(h0+v*0.3,.2,0.3+v*0.7)}"/>`;}return o;}
 if(m==='beat'){const b=(p*1.4)%(2*M.PI),pulse=M.max(M.sin(b),M.sin(b-0.5))*0.5+0.5;return `<path d="M72 106 C30 74 34 40 56 40 C66 40 72 50 72 56 C72 50 78 40 88 40 C110 40 114 74 72 106 Z" fill="${hsv(0.98,.8,1)}" transform="translate(72 72) scale(${0.7+0.3*pulse}) translate(-72 -72)"/>`;}
 if(m==='impact'){const t=(ph%9)/9,rad=6+t*58;return `<circle cx="72" cy="72" r="${rad}" fill="none" stroke="${hsv(h0,.8,1-t)}" stroke-width="${M.max(1,10*(1-t))}"/><circle cx="72" cy="72" r="8" fill="${hsv(h0,.5,1-t*0.5)}"/>`;}
 if(m==='akemi')return `<circle cx="72" cy="72" r="42" fill="${hsv(h0,.5,1)}"/><path d="M40 44 Q72 20 104 44" fill="none" stroke="#1a1a1a" stroke-width="4"/><circle cx="58" cy="70" r="7" fill="#1a1a1a"/><circle cx="86" cy="70" r="7" fill="#1a1a1a"/><path d="M60 92 Q72 ${(98+M.sin(p)*6)|0} 84 92" fill="none" stroke="#1a1a1a" stroke-width="4"/>`;
 if(m==='halloween'){const fl=0.75+0.25*(0.5+0.5*M.sin(p*3)),og=hsv(0.07,.9,fl);return `<ellipse cx="72" cy="80" rx="46" ry="40" fill="${og}"/><rect x="66" y="30" width="12" height="14" fill="#3a6b2a"/><path d="M50 68 L64 78 L50 78 Z" fill="#1a1a1a"/><path d="M94 68 L80 78 L94 78 Z" fill="#1a1a1a"/><path d="M48 96 L58 90 L64 98 L72 90 L80 98 L86 90 L96 96 L86 108 L58 108 Z" fill="#1a1a1a"/>`;}
 if(m==='candle'){const fl=1+0.12*M.sin(p*4);let o=`<rect x="58" y="72" width="28" height="52" rx="4" fill="${hsv(0.12,.3,.95)}"/><rect x="58" y="72" width="28" height="8" fill="#ffffff40"/><line x1="72" y1="64" x2="72" y2="72" stroke="#333" stroke-width="3"/>`;o+=`<g transform="translate(72 62) scale(${fl}) translate(-72 -62)">${_flame(72,44,hsv(0.09,1,1),64)}${_flame(72,26,hsv(0.14,.7,1),60)}</g>`;return o;}
 if(m==='glitter'){let o='';for(let i=0;i<16;i++){const x=(i*53+ph*7)%140+2,y=(i*89+ph*3)%128+2,on=((i*3+(ph*4*spd|0))%16)<3;if(on)o+=`<circle cx="${x|0}" cy="${y|0}" r="3" fill="#ffffff"/><circle cx="${x|0}" cy="${y|0}" r="6" fill="${hsv(h0+i*0.06,.4,1)}"/>`;}return o;}
 if(m==='fairy'){let o='';for(let i=0;i<9;i++){const t=(i/9+ph*0.03*spd)%1,x=16+t*112,y=72+M.sin(t*6.28+p)*34,r=2+4*(1-M.abs(0.5-t)*2);o+=`<circle cx="${x|0}" cy="${y|0}" r="${r|0}" fill="${hsv(h0+t*0.5,.4,1)}"/>`;}return o;}
 if(m==='spots'){let o='';for(let i=0;i<3;i++){const x=72+M.sin(p*0.5+i*2.1)*44,y=72+M.cos(p*0.6+i*1.7)*36;o+=`<circle cx="${x|0}" cy="${y|0}" r="26" fill="${hsv(h0+i*0.2,.5,.45)}"/><circle cx="${x|0}" cy="${y|0}" r="15" fill="${hsv(h0+i*0.2,.5,.95)}"/>`;}return o;}
 if(m==='plasma'){let o='';for(let i=0;i<4;i++){const x=72+M.sin(p*0.5+i*1.6)*30,y=72+M.cos(p*0.7+i*2.0)*28,r=26+8*M.sin(p*0.9+i);o+=`<circle cx="${x|0}" cy="${y|0}" r="${r|0}" fill="${hsv(h0+i*0.05+ph*0.01,.7,1)}"/>`;}return o;}
 if(m==='aurora'){let o='';for(let k=0;k<4;k++){const xb=24+k*30,sw=M.sin(p*0.6+k*0.8)*12;o+=`<path d="M${(xb+sw)|0} 18 Q${(xb-8+sw)|0} 70 ${(xb+sw)|0} 126 L${(xb+16+sw)|0} 126 Q${(xb+8+sw)|0} 66 ${(xb+16+sw)|0} 18 Z" fill="${hsv(0.33+k*0.12,.7,.9)}"/>`;}return o;}
 if(m==='stream'){let o='';for(let i=0;i<9;i++){const x=(i*18+ph*8*spd)%156-8,y=52+(i%3)*20;o+=`<rect x="${x|0}" y="${y}" width="18" height="7" rx="3" fill="${hsv(h0+i*0.012,sat,0.9-i*0.03)}"/>`;}return o;}
 if(m==='percent'){const f=((ph*spd)%20)/20;return `<rect x="14" y="58" width="116" height="28" rx="8" fill="none" stroke="${hsv(h0,.4,.6)}" stroke-width="4"/><rect x="18" y="62" width="${(108*f)|0}" height="20" rx="5" fill="${hsv(h0,.8,1)}"/>`;}
 if(m==='phased'){let o='';for(let k=0;k<3;k++){let pts='';for(let x=8;x<140;x+=8)pts+=`${x},${(72+M.sin(x*0.09+p+k*2.0)*(22+k*4))|0} `;o+=`<polyline points="${pts.trim()}" fill="none" stroke="${hsv(h0+k*0.15,.8,1)}" stroke-width="5" stroke-linecap="round"/>`;}return o;}
 if(m==='loading'){let o='';for(let k=0;k<10;k++){const a=k/10*2*M.PI,br=(((ph*spd|0)-k)%10+10)%10/10;o+=`<circle cx="${(72+M.cos(a)*42)|0}" cy="${(72+M.sin(a)*42)|0}" r="7" fill="${hsv(h0,.6,0.25+0.75*br)}"/>`;}return o;}
 if(m==='dancing'){const sw=M.sin(p*1.5),col=hsv(h0,.7,1);let o=`<circle cx="${(72+sw*8)|0}" cy="34" r="12" fill="${col}"/><line x1="${(72+sw*8)|0}" y1="46" x2="72" y2="86" stroke="${col}" stroke-width="7" stroke-linecap="round"/>`;o+=`<line x1="72" y1="86" x2="${(72+30*sw)|0}" y2="122" stroke="${col}" stroke-width="7" stroke-linecap="round"/><line x1="72" y1="86" x2="${(72-30*sw)|0}" y2="122" stroke="${col}" stroke-width="7" stroke-linecap="round"/>`;o+=`<line x1="72" y1="58" x2="${(72+34*sw)|0}" y2="${(44-M.abs(sw)*10)|0}" stroke="${hsv(h0,.5,.9)}" stroke-width="6" stroke-linecap="round"/><line x1="72" y1="58" x2="${(72-34*sw)|0}" y2="${(44-M.abs(sw)*10)|0}" stroke="${hsv(h0,.5,.9)}" stroke-width="6" stroke-linecap="round"/>`;return o;}
 if(m==='wipe'){const ar=M.sin(p*0.6)*58*M.PI/180,x2=72+M.sin(ar)*100,y2=128-M.cos(ar)*100;return `<path d="M6 116 A84 84 0 0 1 138 116" fill="none" stroke="${hsv(h0,.25,.5)}" stroke-width="4"/><line x1="72" y1="126" x2="${x2|0}" y2="${y2|0}" stroke="${hsv(h0,.4,.6)}" stroke-width="5"/><line x1="${(72+M.sin(ar)*44)|0}" y1="${(128-M.cos(ar)*44)|0}" x2="${x2|0}" y2="${y2|0}" stroke="${hsv(h0,.7,1)}" stroke-width="11" stroke-linecap="round"/><circle cx="72" cy="126" r="6" fill="${hsv(h0,.5,.8)}"/>`;}
 if(m==='sweep'){const x=72+M.sin(p*0.5)*40,d=M.cos(p*0.5)>0?1:-1;let o=`<line x1="${x|0}" y1="108" x2="${(x-26)|0}" y2="28" stroke="${hsv(0.08,.55,.85)}" stroke-width="7" stroke-linecap="round"/>`;for(let k=-3;k<4;k++)o+=`<line x1="${x|0}" y1="108" x2="${(x+k*8)|0}" y2="132" stroke="${hsv(0.11,.5,1)}" stroke-width="4"/>`;for(let j=0;j<3;j++)o+=`<circle cx="${(x+d*(26+j*13))|0}" cy="${(122-j*5)|0}" r="${4-j}" fill="${hsv(h0,.25,.7)}"/>`;return o;}
 if(m==='scan'){const pos=72+M.sin(p*0.9)*54,d=M.cos(p*0.9)>0?1:-1;let o='';for(let k=0;k<6;k++)o+=`<rect x="${(pos-k*8*d)|0}" y="30" width="9" height="84" rx="4" fill="${hsv(0,0.9,1-k*0.15)}"/>`;return o;}
 if(m==='running'){const sw=M.sin(p*1.8),col=hsv(h0,.65,1);let o=`<circle cx="88" cy="30" r="11" fill="${col}"/><line x1="84" y1="41" x2="60" y2="80" stroke="${col}" stroke-width="9" stroke-linecap="round"/>`;o+=`<polyline points="60,80 84,100 ${(92+(sw*10|0))},118" fill="none" stroke="${col}" stroke-width="9" stroke-linecap="round"/><polyline points="60,80 44,96 ${(30-(sw*10|0))},112" fill="none" stroke="${col}" stroke-width="9" stroke-linecap="round"/>`;o+=`<polyline points="70,52 ${(96-(sw*8|0))},64 ${(108-(sw*6|0))},58" fill="none" stroke="${hsv(h0,.5,.9)}" stroke-width="7" stroke-linecap="round"/><polyline points="70,52 ${(50+(sw*8|0))},66 ${(40+(sw*6|0))},74" fill="none" stroke="${hsv(h0,.5,.9)}" stroke-width="7" stroke-linecap="round"/>`;return o;}
 if(m==='saw'){const x=M.sin(p*0.8)*16,by=62;let o=`<rect x="${(20+x)|0}" y="${by}" width="94" height="18" rx="3" fill="${hsv(h0,.2,.85)}"/>`;for(let k=0;k<9;k++){const tx=22+x+k*10;o+=`<path d="M${tx|0} ${by+18} L${(tx+5)|0} ${by+30} L${(tx+10)|0} ${by+18} Z" fill="${hsv(h0,.2,.85)}"/>`;}o+=`<rect x="${(4+x)|0}" y="${by-6}" width="26" height="30" rx="7" fill="${hsv(0.07,.6,.9)}"/>`;return o;}
 if(m==='dynamic'){let o='';for(let r=0;r<3;r++)for(let c=0;c<4;c++){const hue=(((r*4+c)*67+(ph*2*spd|0)*53+seed*29)%360)/360;o+=`<rect x="${10+c*32}" y="${20+r*36}" width="30" height="34" rx="4" fill="${hsv(hue,.8,1)}"/>`;}return o;}
 if(m==='tetris'){const cell=14;let o='';const stack=[[2,7],[3,7],[4,7],[2,8],[3,8],[5,8],[6,8],[4,9],[5,9],[1,8],[1,9],[6,9],[0,9],[7,9]];stack.forEach(([cx,cy])=>{o+=`<rect x="${8+cx*cell}" y="${20+cy*cell}" width="${cell}" height="${cell}" rx="2" fill="${hsv(cx*0.13,.6,.9)}" stroke="#1a1a1a" stroke-width="1"/>`;});const shp=[[0,0],[1,0],[2,0],[1,1]],fy=(ph*4*spd|0)%7,col=hsv(h0,.8,1);shp.forEach(([dx,dy])=>{o+=`<rect x="${50+dx*cell}" y="${10+(fy+dy)*cell}" width="${cell}" height="${cell}" rx="2" fill="${col}" stroke="#1a1a1a" stroke-width="1"/>`;});return o;}
 if(m==='matrix'){let o='';for(let c=0;c<6;c++){const x=16+c*20,y=((ph*10*spd|0)+c*37+seed*5)%160-30;for(let k=0;k<4;k++)o+=`<rect x="${x}" y="${y-k*18}" width="12" height="14" rx="2" fill="${hsv(0.33,.8,1-k*0.28)}"/>`;}return o;}
 if(m==='snow'){let o='';for(let i=0;i<5;i++){const x=18+i*28,y=((ph*8*spd|0)+i*33+seed*7)%160-16;o+=`<g stroke="#dff1ff" stroke-width="3" stroke-linecap="round" transform="translate(${x} ${y})"><line x1="0" y1="-9" x2="0" y2="9"/><line x1="-8" y1="-5" x2="8" y2="5"/><line x1="8" y1="-5" x2="-8" y2="5"/></g>`;}return o;}
 if(m==='rain'){let o='';const step=(132/M.max(1,n-2))|0;for(let i=0;i<n-1;i++){const y=((ph*13*spd|0)+i*41+seed*7)%150-20;o+=`<rect x="${18+i*step}" y="${y}" width="9" height="28" rx="4" fill="${hsv(h0+0.55,.65,1)}"/>`;}return o;}
 if(m==='fire'){let o='';[[46,0.85,0.0],[72,1.15,1.6],[98,0.8,3.1]].forEach(([cx,bh,off],k)=>{const hh=(66+34*(0.5+0.5*M.sin(p*1.3+off)))*bh;o+=_flame(cx,hh,hsv(0.02+0.09*k,1,1));});return o;}
 if(m==='lighthouse'){const a=p*0.5;return `<circle cx="72" cy="72" r="12" fill="${hsv(h0,.3,1)}"/><path d="M72 72 L${(72+M.cos(a)*70)|0} ${(72+M.sin(a)*70)|0} L${(72+M.cos(a+0.5)*70)|0} ${(72+M.sin(a+0.5)*70)|0} Z" fill="${hsv(h0,.6,.9)}"/>`;}
 if(m==='sunrise'){const y=110-(0.5+0.5*M.sin(p*0.4))*40;return `<circle cx="72" cy="${y|0}" r="26" fill="${hsv(0.09,.85,1)}"/><rect x="0" y="116" width="144" height="28" fill="${hsv(0.08,.6,.5)}"/>`;}
 if(m==='twinkle'){let o='';for(let i=0;i<6;i++){const x=22+(i*47)%110,yv=30+(i*53)%84,lit=((i*5+(ph*3*spd|0)+seed)%6)<2,r=lit?11:5,col=lit?hsv(h0+i*0.1,.5,1):'#39414e';o+=`<path d="M${x} ${yv-r} l${r*0.3} ${r*0.7} l${r*0.7} ${r*0.3} l${-r*0.7} ${r*0.3} l${-r*0.3} ${r*0.7} Z" fill="${col}"/>`;}return o;}
 if(m==='sparkle'){let o='';for(let i=0;i<9;i++){const cx=24+(i%3)*48,cy=24+((i/3)|0)*48,lit=((i*7+(ph*3*spd|0)+seed)%9)<3;o+=`<circle cx="${cx}" cy="${cy}" r="${lit?13:5}" fill="${lit?hsv(h0+i*0.05,sat,1):'#39414e'}"/>`;}return o;}
 if(m==='ripple'){let o='';for(let k=0;k<3;k++){const rad=((ph*3*spd+k*16)%48)+6;o+=`<circle cx="72" cy="72" r="${rad|0}" fill="none" stroke="${hsv(h0+k*0.1,.6,1-rad/60)}" stroke-width="6"/>`;}return o;}
 if(m==='blink'){const cyc=(ph|0)%6,o=[0.10,0.55,1.0,1.0,1.0,1.0][cyc],H=30*o+3,top=72-H,bot=72+H,iris=hsv(0.09,0.6,0.62);let s=`<path d="M26 72 Q72 ${top|0} 118 72 Q72 ${bot|0} 26 72 Z" fill="#f2ece0"/>`;if(o>0.35){s+=`<ellipse cx="72" cy="72" rx="18" ry="${M.min(18,H-2)|0}" fill="${iris}"/><ellipse cx="72" cy="72" rx="8" ry="${M.min(8,H-4)|0}" fill="#17130d"/><circle cx="66" cy="66" r="3" fill="#ffffff"/>`;}s+=`<path d="M26 72 Q72 ${top|0} 118 72" fill="none" stroke="#3a2f24" stroke-width="4" stroke-linecap="round"/>`;[[44,0.75],[72,1.0],[100,0.75]].forEach(([lx,ly])=>{const lt=72-H*ly;s+=`<line x1="${lx}" y1="${lt|0}" x2="${lx}" y2="${(lt-12)|0}" stroke="#3a2f24" stroke-width="3" stroke-linecap="round"/>`;});return s;}
 if(m==='birds'){let o='';for(let k=0;k<4;k++){const x=(ph*10*spd+k*44)%180-18,y=42+(k%2)*34+M.sin(ph*0.8+k)*6,flap=6+M.abs(M.sin(ph*1.4+k*1.3))*12,col=hsv(h0,sat,0.85);o+=`<path d="M${(x-15)|0} ${y|0} Q${(x-7)|0} ${(y-flap)|0} ${x|0} ${y|0} Q${(x+7)|0} ${(y-flap)|0} ${(x+15)|0} ${y|0}" fill="none" stroke="${col}" stroke-width="5" stroke-linecap="round"/>`;}return o;}
 if(m==='dna'){let o='';for(let i=0;i<15;i++){const t=i/14,yy=14+t*116,a=t*6.283*1.5+p*0.3,x1=72+M.sin(a)*36,x2=72-M.sin(a)*36;o+=`<line x1="${x1|0}" y1="${yy|0}" x2="${x2|0}" y2="${yy|0}" stroke="#5a6472" stroke-width="3"/><circle cx="${x1|0}" cy="${yy|0}" r="6" fill="${hsv(h0,sat,0.9)}"/><circle cx="${x2|0}" cy="${yy|0}" r="6" fill="${hsv(h0+0.10,0.5,0.85)}"/>`;}return o;}
 if(m==='eye'){const look=M.sin(p*0.7)*15,iris=hsv(0.09,0.6,0.62);return `<path d="M18 72 Q72 32 126 72 Q72 112 18 72 Z" fill="#f2ece0"/><path d="M18 72 Q72 32 126 72 Q72 112 18 72 Z" fill="none" stroke="#3a2f24" stroke-width="4"/><circle cx="${(72+look)|0}" cy="72" r="21" fill="${iris}"/><circle cx="${(72+look)|0}" cy="72" r="9" fill="#17130d"/><circle cx="${(72+look-4)|0}" cy="66" r="3" fill="#ffffff"/>`;}
 if(m==='strobe'){const c=ph%2===0?hsv(h0,sat,1):'#272c36';return [[48,48],[96,48],[48,96],[96,96]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="16" fill="${c}"/>`).join('');}
 if(m==='chase'){const pos=(ph*spd+seed|0)%7,b=hsv(h0,.75,1).match(/\d+/g).map(Number);let o='';for(let i=0;i<7;i++){const br=M.max(0.14,1-(((pos-i*dr)%7+7)%7)*0.30);o+=`<circle cx="${18+i*18}" cy="72" r="9" fill="rgb(${(26+(b[0]-26)*br)|0},${(26+(b[1]-26)*br)|0},${(26+(b[2]-26)*br)|0})"/>`;}return o;}
 if(m==='rainbow'){let o='';for(let k=0;k<6;k++)o+=`<path d="M18 128 A${54-k*8} ${54-k*8} 0 0 1 126 128" fill="none" stroke="${hsv((k/6+ph*0.03*spd)%1,.9,1)}" stroke-width="9"/>`;return o;}
 if(m==='colorloop')return `<rect x="20" y="20" width="104" height="104" rx="16" fill="${hsv(h0+ph*0.03*spd,.8,1)}"/>`;
 if(m==='lissajous'){let o='';const N=54,dphi=p*0.25;for(let i=0;i<N;i++){const t=i/N*2*M.PI,x=72+54*M.sin(3*t+dphi),y=72+50*M.sin(2*t);o+=`<circle cx="${x|0}" cy="${y|0}" r="3.4" fill="${hsv(h0+i/N*0.14,sat,0.9)}"/>`;}return o;}
 const wd=(120/n)|0;let o='';for(let i=0;i<n;i++){const br=0.30+0.70*(0.5+0.5*M.sin(p*0.6-i*0.95)),hh=22+96*br;o+=`<rect x="${12+i*wd}" y="${(128-hh)|0}" width="${wd-3}" height="${hh|0}" rx="3" fill="${hsv(h0+i*0.012,sat,br)}"/>`;}return o;
}
if(typeof module!=='undefined')module.exports={anim,motion,hsv};
