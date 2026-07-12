// Reference: per-effect UNIQUE animation for 24 WLED motion types.
// motion(name) -> one of 24 motion strings ; anim(phase, motion, seed) -> inner SVG
// (viewBox 0 0 144 144). seed = the effect's index -> distinct hue/speed/direction/density.
// Advance phase ~7 fps. No rgba() (some SVG renderers drop alpha).
function hsv(h,s,v){h=((h%1)+1)%1;h*=6;const i=Math.floor(h),f=h-i,p=v*(1-s),q=v*(1-s*f),t=v*(1-s*(1-f));
 const a=[[v,t,p],[q,v,p],[p,v,t],[p,q,v],[t,p,v],[v,p,q]][i%6];
 return 'rgb('+Math.round(a[0]*255)+','+Math.round(a[1]*255)+','+Math.round(a[2]*255)+')';}
function motion(name){
 const n=(name||'').toLowerCase(), h=(...k)=>k.some(x=>n.includes(x));
 if(h('solid','static','fill'))return'solid';
 if(h('police'))return'police';
 if(h('ghost rider','ghost'))return'ghost';
 if(h('two dots','two areas','dual'))return'dots';
 if(h('traffic'))return'traffic';
 if(h('washing machine','rotozoom','spin'))return'spin';
 if(h('spaceship','ufo','saturn'))return'spaceship';
 if(h('bee','crazy bees'))return'bees';
 if(h('octopus'))return'octopus';
 if(h('pacman','pac-man'))return'pacman';
 if(h('dj light','disco'))return'dj';
 if(h('scrolling text','text'))return'text';
 if(h('black hole','blackhole'))return'blackhole';
 if(h('galaxy','vortex','swirl','drift rose','spiral'))return'galaxy';
 if(h('hourglass'))return'hourglass';
 if(h('tv sim','tv '))return'tv';
 if(h('bpm','pulse '))return'beat';
 if(h('impact','sonic boom','colored burst','fireworks 1d'))return'impact';
 if(h('akemi'))return'akemi';
 if(h('blob','soap','clouds','plasmoid'))return'blobs';
 if(h('lightning'))return'lightning';
 if(h('firework','popcorn'))return'fireworks';
 if(h('heart'))return'heartbeat';
 if(h('bounc','ball','juggle','gravcen','gravfreq','gravimeter'))return'bounce';
 if(h('comet','meteor','shooting'))return'comet';
 if(h('rainbow'))return'rainbow';
 if(h('sweep','scan','wipe','larson','knight','android'))return'sweep';
 if(h('matri','tetrix','game of life','dna','pixel'))return'matrix';
 if(h('snow','frost','ice'))return'snow';
 if(h('rain','drip','drop','waterfall','puddle','fall'))return'rain';
 if(h('fire','flame','lava','candle','ember','glow','halloween'))return'fire';
 if(h('lighthouse','rotat'))return'lighthouse';
 if(h('sunrise','sunset','sun ','day'))return'sunrise';
 if(h('twinkle','star','fairy','glitter','firefl'))return'twinkle';
 if(h('sparkle','dissolve','flicker','noise','spot'))return'sparkle';
 if(h('ripple','plasma','pacifica','water','liquid','fluid','aurora','flow','stream','freq','geq'))return'ripple';
 if(h('breathe','breath','fade','pulse','sine','sinelon','blend','heartbeat'))return'breathe';
 if(h('strobe','blink','stutter','hyper'))return'strobe';
 if(h('chase','running','marquee','railway','theater','train','loading','dancing'))return'chase';
 if(h('colorloop','colorwave','colortwinkle','colorful','pride','cycle','hue','spectrum','palette'))return'colorloop';
 if(h('saw','sawtooth','gradient','tricolor'))return'saw';
 return'wave';
}
function anim(ph,m,seed){
 seed=seed||0; const M=Math;
 const h0=((seed*47)%360)/360, spd=0.55+((seed*13)%110)/100, dr=(M.floor(seed/2)%2)?1:-1,
       n=5+(seed%4), sat=0.7+((seed*5)%30)/100, p=ph*spd*dr;
 if(m==='solid')return `<rect x="26" y="26" width="92" height="92" rx="14" fill="${hsv(h0,sat,.9)}"/>`;
 if(m==='police'){const a=ph%2,l=a===0?hsv(0,.9,1):'#20242c',r=a===1?hsv(.62,.9,1):'#20242c';return `<rect x="14" y="30" width="54" height="84" rx="10" fill="${l}"/><rect x="76" y="30" width="54" height="84" rx="10" fill="${r}"/>`;}
 if(m==='lightning'){const c=((ph*spd|0)%3===0)?hsv(.15,.5,1):'#2a2f38';return `<path d="M84 16 L44 78 L68 78 L54 128 L104 60 L78 60 Z" fill="${c}"/>`;}
 if(m==='fireworks'){const t=(ph%8)/8,rad=8+t*54;let o=t<0.2?`<circle cx="72" cy="72" r="6" fill="${hsv(h0,.3,1-t)}"/>`:'';for(let i=0;i<10;i++){const a=i/10*2*M.PI,x=72+M.cos(a)*rad,y=72+M.sin(a)*rad;o+=`<circle cx="${x|0}" cy="${y|0}" r="${M.max(1,6*(1-t))}" fill="${hsv(h0+i*0.04,.9,1-t*0.7)}"/>`;}return o;}
 if(m==='heartbeat'){const s=1+0.18*M.sin(p*1.6);return `<g transform="translate(72 78) scale(${s}) translate(-72 -78)"><path d="M72 108 C24 72 30 36 54 36 C66 36 72 46 72 52 C72 46 78 36 90 36 C114 36 120 72 72 108 Z" fill="${hsv(0.98,.85,1)}"/></g>`;}
 if(m==='bounce'){let o='';for(let i=0;i<3;i++){const x=34+i*38,y=110-M.abs(M.sin(p*0.6+i*1.1))*74;o+=`<circle cx="${x}" cy="${y|0}" r="13" fill="${hsv(h0+i*0.14,.8,1)}"/>`;}return o;}
 if(m==='comet'){const x=((ph*7*spd|0)%168)-12;let o='';for(let k=0;k<6;k++){o+=`<circle cx="${(x-k*10*dr)|0}" cy="72" r="${10-k*1.4}" fill="${hsv(h0,.7,1-k*0.15)}"/>`;}return o;}
 if(m==='sweep'){const x=12+(0.5+0.5*M.sin(p*0.5))*108,s=M.cos(p*0.5)>0?1:-1;let o=`<rect x="${x|0}" y="24" width="12" height="96" rx="6" fill="${hsv(h0,.7,1)}"/>`;for(let k=1;k<5;k++)o+=`<rect x="${(x-k*11*s)|0}" y="30" width="8" height="84" rx="4" fill="${hsv(h0,.55,1-k*0.18)}"/>`;return o;}
 if(m==='matrix'){let o='';for(let c=0;c<6;c++){const x=16+c*20,y=((ph*10*spd|0)+c*37+seed*5)%160-30;for(let k=0;k<4;k++)o+=`<rect x="${x}" y="${y-k*18}" width="12" height="14" rx="2" fill="${hsv(0.33,.8,1-k*0.28)}"/>`;}return o;}
 if(m==='snow'){let o='';for(let i=0;i<5;i++){const x=18+i*28,y=((ph*8*spd|0)+i*33+seed*7)%160-16;o+=`<g stroke="#dff1ff" stroke-width="3" stroke-linecap="round" transform="translate(${x} ${y})"><line x1="0" y1="-9" x2="0" y2="9"/><line x1="-8" y1="-5" x2="8" y2="5"/><line x1="8" y1="-5" x2="-8" y2="5"/></g>`;}return o;}
 if(m==='rain'){let o='';const step=(132/M.max(1,n-2))|0;for(let i=0;i<n-1;i++){const y=((ph*13*spd|0)+i*41+seed*7)%150-20;o+=`<rect x="${18+i*step}" y="${y}" width="9" height="28" rx="4" fill="${hsv(h0+0.55,.65,1)}"/>`;}return o;}
 if(m==='fire'){let o='';for(let i=0;i<5;i++){const hh=42+62*(0.5+0.5*M.sin(p*0.9+i*1.7+seed));o+=`<rect x="${16+i*24}" y="${128-hh}" width="18" height="${hh}" rx="8" fill="${hsv(0.02+0.10*(hh/104),1,1)}"/>`;}return o;}
 if(m==='lighthouse'){const a=p*0.5,x2=72+M.cos(a)*70,y2=72+M.sin(a)*70,x3=72+M.cos(a+0.5)*70,y3=72+M.sin(a+0.5)*70;return `<circle cx="72" cy="72" r="12" fill="${hsv(h0,.3,1)}"/><path d="M72 72 L${x2|0} ${y2|0} L${x3|0} ${y3|0} Z" fill="${hsv(h0,.6,.9)}"/>`;}
 if(m==='sunrise'){const y=110-(0.5+0.5*M.sin(p*0.4))*40;return `<circle cx="72" cy="${y|0}" r="26" fill="${hsv(0.09,.85,1)}"/><rect x="0" y="116" width="144" height="28" fill="${hsv(0.08,.6,.5)}"/>`;}
 if(m==='twinkle'){let o='';for(let i=0;i<6;i++){const x=22+(i*47)%110,yv=30+(i*53)%84,lit=(((i*5+(ph*3*spd|0)+seed)%6)<2),r=lit?11:5,col=lit?hsv(h0+i*0.1,.5,1):'#39414e';o+=`<path d="M${x} ${yv-r} l${r*0.3} ${r*0.7} l${r*0.7} ${r*0.3} l${-r*0.7} ${r*0.3} l${-r*0.3} ${r*0.7} Z" fill="${col}"/>`;}return o;}
 if(m==='sparkle'){let o='';for(let i=0;i<9;i++){const cx=24+(i%3)*48,cy=24+((i/3)|0)*48,lit=(((i*7+(ph*3*spd|0)+seed)%9)<3);o+=`<circle cx="${cx}" cy="${cy}" r="${lit?13:5}" fill="${lit?hsv(h0+i*0.05,sat,1):'#39414e'}"/>`;}return o;}
 if(m==='ripple'){let o='';for(let k=0;k<3;k++){const rad=((ph*3*spd+k*16)%48)+6;o+=`<circle cx="72" cy="72" r="${rad}" fill="none" stroke="${hsv(h0+k*0.1,.6,1-rad/60)}" stroke-width="6"/>`;}return o;}
 if(m==='breathe'){const br=0.35+0.65*(0.5+0.5*M.sin(p*0.5));return `<circle cx="72" cy="72" r="${28+34*br}" fill="${hsv(h0,sat*0.85,br)}"/>`;}
 if(m==='strobe'){const c=ph%2===0?hsv(h0,sat,1):'#272c36';return [[48,48],[96,48],[48,96],[96,96]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="16" fill="${c}"/>`).join('');}
 if(m==='chase'){const pos=(ph*spd+seed|0)%7,b=hsv(h0,.75,1).match(/\d+/g).map(Number);let o='';for(let i=0;i<7;i++){const br=M.max(0.14,1-(((pos-i*dr)%7+7)%7)*0.30);o+=`<circle cx="${18+i*18}" cy="72" r="9" fill="rgb(${(26+(b[0]-26)*br)|0},${(26+(b[1]-26)*br)|0},${(26+(b[2]-26)*br)|0})"/>`;}return o;}
 if(m==='rainbow'){let o='';for(let k=0;k<6;k++)o+=`<path d="M18 128 A${54-k*8} ${54-k*8} 0 0 1 126 128" fill="none" stroke="${hsv((k/6+ph*0.03*spd)%1,.9,1)}" stroke-width="9"/>`;return o;}
 if(m==='colorloop')return `<rect x="20" y="20" width="104" height="104" rx="16" fill="${hsv(h0+ph*0.03*spd,.8,1)}"/>`;
 if(m==='saw'){const wd=(120/n)|0;let o='';for(let i=0;i<n;i++){const hh=20+((i*20+(ph*6*spd|0))%100);o+=`<rect x="${12+i*wd}" y="${128-hh}" width="${wd-3}" height="${hh}" fill="${hsv(h0+i*0.08,.85,1)}"/>`;}return o;}

 if(m==='ghost'){const x=72+M.sin(p*0.5)*36,col=hsv(h0,.25,1);return `<path d="M${(x-30)|0} 40 a30 30 0 0 1 30 30 v34 l-8 -8 -8 8 -7 -8 -7 8 -8 -8 -8 8 v-34 a30 30 0 0 1 30 -30 Z" fill="${col}"/><circle cx="${(x-10)|0}" cy="66" r="5" fill="#1a1a1a"/><circle cx="${(x+10)|0}" cy="66" r="5" fill="#1a1a1a"/>`;}
 if(m==='dots'){let o='';for(let i=0;i<2;i++){const x=72+M.cos(p*0.7+i*M.PI)*44,y=72+M.sin(p*0.9+i*M.PI)*40;o+=`<circle cx="${x|0}" cy="${y|0}" r="16" fill="${hsv(h0+i*0.4,.8,1)}"/>`;}return o;}
 if(m==='traffic'){const lit=(ph*spd|0)%3,c=[lit===0?'#e6002a':'#3a1015',lit===1?'#ffcc00':'#3a3410',lit===2?'#2ee06e':'#123a20'];let o='<rect x="52" y="14" width="40" height="116" rx="12" fill="#111"/>';for(let i=0;i<3;i++)o+=`<circle cx="72" cy="${38+i*34}" r="14" fill="${c[i]}"/>`;return o;}
 if(m==='spin'){const a=p*0.6;let o=`<circle cx="72" cy="72" r="46" fill="none" stroke="${hsv(h0,.4,.7)}" stroke-width="6"/>`;for(let k=0;k<4;k++)o+=`<rect x="66" y="72" width="12" height="42" rx="4" fill="${hsv(h0+k*0.08,.7,1)}" transform="rotate(${(a+k*M.PI/2)*57.3} 72 72)"/>`;return o;}
 if(m==='spaceship'){const x=((ph*6*spd|0)%180)-18;return `<g transform="translate(${x|0} 72)"><ellipse cx="0" cy="0" rx="34" ry="12" fill="${hsv(h0,.5,.9)}"/><ellipse cx="0" cy="-8" rx="16" ry="12" fill="${hsv(h0+0.1,.3,1)}"/><circle cx="-16" cy="2" r="3" fill="#fff"/><circle cx="0" cy="4" r="3" fill="#fff"/><circle cx="16" cy="2" r="3" fill="#fff"/></g>`;}
 if(m==='bees'){let o='';for(let i=0;i<5;i++){const x=72+M.sin(p*1.3+i*2.1)*50,y=72+M.cos(p*1.7+i*1.3)*46;o+=`<circle cx="${x|0}" cy="${y|0}" r="8" fill="${hsv(0.14,.9,1)}"/><ellipse cx="${x|0}" cy="${(y-2)|0}" rx="10" ry="5" fill="none" stroke="#ffffff44" stroke-width="1"/>`;}return o;}
 if(m==='octopus'){let o=`<circle cx="72" cy="60" r="24" fill="${hsv(h0,.6,1)}"/>`;for(let k=0;k<6;k++){const a=k/6*2*M.PI,sw=M.sin(p*0.8+k)*16;o+=`<path d="M72 78 Q${(72+M.cos(a)*20+sw)|0} 104 ${(72+M.cos(a)*40+sw)|0} 124" fill="none" stroke="${hsv(h0,.6,1)}" stroke-width="7" stroke-linecap="round"/>`;}return o;}
 if(m==='pacman'){const x=((ph*6*spd|0)%176)-16,mo2=M.abs(M.sin(p*1.4))*40;let o=`<path d="M${x|0} 72 L${(x+34*M.cos(mo2/57.3))|0} ${(72-34*M.sin(mo2/57.3))|0} A34 34 0 1 0 ${(x+34*M.cos(mo2/57.3))|0} ${(72+34*M.sin(mo2/57.3))|0} Z" fill="#ffd200"/>`;for(let d=0;d<3;d++){const dx=x+50+d*26;if(dx<150)o+=`<circle cx="${dx|0}" cy="72" r="6" fill="#ffe680"/>`;}return o;}
 if(m==='dj'){const a=p*0.8;return `<circle cx="72" cy="72" r="46" fill="#222"/><circle cx="72" cy="72" r="46" fill="none" stroke="${hsv(h0,.7,1)}" stroke-width="4"/><circle cx="72" cy="72" r="14" fill="${hsv(h0+0.3,.7,1)}"/><rect x="70" y="30" width="4" height="42" fill="#fff" transform="rotate(${a*57.3} 72 72)"/>`;}
 if(m==='text'){let o='';const off=(ph*7*spd|0)%40;for(let i=0;i<5;i++)o+=`<rect x="${(140-i*32-off)|0}" y="52" width="20" height="40" rx="3" fill="${hsv(h0+i*0.1,.7,1)}"/>`;return o;}
 if(m==='blackhole'){let o='<circle cx="72" cy="72" r="16" fill="#000"/>';for(let k=0;k<3;k++){const rad=48-((ph*3*spd+k*16)%44);o+=`<circle cx="72" cy="72" r="${M.max(2,rad)}" fill="none" stroke="${hsv(h0+k*0.1,.7,1)}" stroke-width="5"/>`;}return o;}
 if(m==='galaxy'){let o='';for(let k=0;k<14;k++){const t=k/14,a=p*0.5+t*6.5,r=12+t*54;o+=`<circle cx="${(72+M.cos(a)*r)|0}" cy="${(72+M.sin(a)*r)|0}" r="${5-t*3}" fill="${hsv(h0+t*0.4,.7,1)}"/>`;}return o;}
 if(m==='hourglass'){let o=`<path d="M34 20 L110 20 L78 72 L110 124 L34 124 L66 72 Z" fill="none" stroke="${hsv(h0,.4,.8)}" stroke-width="5"/>`;o+=`<circle cx="72" cy="${(72+((ph*4*spd|0)%40))|0}" r="5" fill="${hsv(0.1,.8,1)}"/><path d="M50 108 L94 108 L78 84 L66 84 Z" fill="${hsv(0.1,.7,1)}"/>`;return o;}
 if(m==='tv'){let o='';for(let r=0;r<4;r++)for(let c=0;c<4;c++){const v=((r*4+c)*13+(ph*9*spd|0)+seed*7)%100/100;o+=`<rect x="${16+c*28}" y="${16+r*28}" width="30" height="30" fill="${hsv(h0+v*0.3,.2,0.3+v*0.7)}"/>`;}return o;}
 if(m==='beat'){const b=(p*1.4)%(2*M.PI),pulse=M.max(M.sin(b),M.sin(b-0.5))*0.5+0.5;return `<path d="M72 106 C30 74 34 40 56 40 C66 40 72 50 72 56 C72 50 78 40 88 40 C110 40 114 74 72 106 Z" fill="${hsv(0.98,.8,1)}" transform="translate(72 72) scale(${0.7+0.3*pulse}) translate(-72 -72)"/>`;}
 if(m==='impact'){const t=(ph%9)/9,rad=6+t*58;return `<circle cx="72" cy="72" r="${rad}" fill="none" stroke="${hsv(h0,.8,1-t)}" stroke-width="${M.max(1,10*(1-t))}"/><circle cx="72" cy="72" r="8" fill="${hsv(h0,.5,1-t*0.5)}"/>`;}
 if(m==='akemi'){return `<circle cx="72" cy="72" r="42" fill="${hsv(h0,.5,1)}"/><path d="M40 44 Q72 20 104 44" fill="none" stroke="#1a1a1a" stroke-width="4"/><circle cx="58" cy="70" r="7" fill="#1a1a1a"/><circle cx="86" cy="70" r="7" fill="#1a1a1a"/><path d="M60 92 Q72 ${(98+M.sin(p)*6)|0} 84 92" fill="none" stroke="#1a1a1a" stroke-width="4"/>`;}
 if(m==='blobs'){let o='';for(let i=0;i<3;i++){const r=22+10*M.sin(p*0.7+i*2),x=44+i*28,y=72+14*M.sin(p*0.5+i);o+=`<circle cx="${x|0}" cy="${y|0}" r="${r|0}" fill="${hsv(h0+i*0.16,.7,1)}"/>`;}return o;}
 const wd=(120/n)|0;let o='';for(let i=0;i<n;i++){const br=0.30+0.70*(0.5+0.5*M.sin(p*0.6-i*0.95)),hh=22+96*br;o+=`<rect x="${12+i*wd}" y="${128-hh}" width="${wd-3}" height="${hh}" rx="3" fill="${hsv(h0+((i*34+ph*12*spd)%360)/360,0.85,br)}"/>`;}return o;
}
if(typeof module!=='undefined')module.exports={anim,motion,hsv};
