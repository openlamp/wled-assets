// Reference implementation of the 9 WLED effect motion-family animations.
// anim(phase, family) -> inner SVG string (viewBox 0 0 144 144). No rgba() (some
// renderers drop alpha); trails are pre-mixed with a #1a1a1a background.
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

if (typeof module!=='undefined') module.exports={anim,hsv};
