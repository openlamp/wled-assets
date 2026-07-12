// Reference: per-effect UNIQUE animation for the 9 WLED motion families.
// anim(phase, family, seed) -> inner SVG string (viewBox 0 0 144 144). seed = the effect's
// index, so each effect gets its own hue/speed/direction/density. Advance phase ~6 fps.
// No rgba() (some SVG renderers drop alpha); trails are pre-mixed with the background.
function hsv(h,s,v){h=((h%1)+1)%1;h*=6;const i=Math.floor(h),f=h-i,p=v*(1-s),q=v*(1-s*f),t=v*(1-s*(1-f));
 const a=[[v,t,p],[q,v,p],[p,v,t],[p,q,v],[t,p,v],[v,p,q]][i%6];
 return 'rgb('+Math.round(a[0]*255)+','+Math.round(a[1]*255)+','+Math.round(a[2]*255)+')';}
function anim(ph,f,seed){
 seed=seed||0;
 const h0=((seed*47)%360)/360, spd=0.55+((seed*13)%110)/100, dr=(Math.floor(seed/2)%2)?1:-1,
       n=5+(seed%4), sat=0.7+((seed*5)%30)/100, p=ph*spd*dr, M=Math;
 if(f==='solid') return `<rect x="26" y="26" width="92" height="92" rx="14" fill="${hsv(h0,sat,0.9)}"/>`;
 if(f==='strobe'){const c=ph%2===0?hsv(h0,sat,1):'#272c36';return [[48,48],[96,48],[48,96],[96,96]].map(([x,y])=>`<circle cx="${x}" cy="${y}" r="16" fill="${c}"/>`).join('');}
 if(f==='sparkle'){let o='';for(let i=0;i<9;i++){const cx=24+(i%3)*48,cy=24+((i/3)|0)*48,lit=(((i*7+((ph*3*spd)|0)+seed)%9)<3);o+=`<circle cx="${cx}" cy="${cy}" r="${lit?13:5}" fill="${lit?hsv(h0+i*0.05,sat,1):'#39414e'}"/>`;}return o;}
 if(f==='fire'){let o='';for(let i=0;i<5;i++){const h=42+62*(0.5+0.5*M.sin(p*0.9+i*1.7+seed));o+=`<rect x="${16+i*24}" y="${128-h}" width="18" height="${h}" rx="8" fill="${hsv(0.02+0.10*(h/104)+h0*0.08,1,1)}"/>`;}return o;}
 if(f==='rain'){let o='';const step=(132/M.max(1,n-2))|0;for(let i=0;i<n-1;i++){const y=(((ph*13*spd)|0)+i*41+seed*7)%150-20;o+=`<rect x="${18+i*step}" y="${y}" width="9" height="28" rx="4" fill="${hsv(h0+0.55,0.65,1)}"/>`;}return o;}
 if(f==='chase'){const pos=((ph*spd+seed)|0)%7;let o='';for(let i=0;i<7;i++){const br=M.max(0.14,1-(((pos-i*dr)%7+7)%7)*0.30);const b=hsv(h0,0.75,1).match(/\d+/g).map(x=>(26+(x-26)*br)|0);o+=`<circle cx="${18+i*18}" cy="72" r="9" fill="rgb(${b[0]},${b[1]},${b[2]})"/>`;}return o;}
 if(f==='breathe'){const br=0.35+0.65*(0.5+0.5*M.sin(p*0.5));return `<circle cx="72" cy="72" r="${28+34*br}" fill="${hsv(h0,sat*0.85,br)}"/>`;}
 if(f==='rainbow'){const wd=(120/n)|0;let o='';for(let i=0;i<n;i++)o+=`<rect x="${12+i*wd}" y="30" width="${wd-3}" height="84" rx="3" fill="${hsv(h0+((i*51+ph*14*spd)%360)/360,0.9,1)}"/>`;return o;}
 const wd=(120/n)|0;let o='';for(let i=0;i<n;i++){const br=0.30+0.70*(0.5+0.5*M.sin(p*0.6-i*0.95)),h=22+96*br;o+=`<rect x="${12+i*wd}" y="${128-h}" width="${wd-3}" height="${h}" rx="3" fill="${hsv(h0+((i*34+ph*12*spd)%360)/360,0.85,br)}"/>`;}return o;
}
if (typeof module!=='undefined') module.exports={anim,hsv};
