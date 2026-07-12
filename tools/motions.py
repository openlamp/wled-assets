import math, colorsys
def _rgb(h,s,v): return "rgb(%d,%d,%d)"%tuple(round(c*255) for c in colorsys.hsv_to_rgb(h%1.0,s,max(0,min(1,v))))
def _p(seed):
    return (((seed*47)%360)/360.0, 0.55+((seed*13)%110)/100.0, 1 if (seed//2)%2 else -1, 5+(seed%4), 0.7+((seed*5)%30)/100.0)
def motion(name):
    n=(name or "").lower()
    def h(*k): return any(x in n for x in k)
    if h("glitter"): return "glitter"
    if h("solid","static","fill"): return "solid"
    if h("police"): return "police"
    if h("lightning"): return "lightning"
    if h("popcorn"): return "popcorn"
    if h("firework"): return "fireworks"
    if h("heart"): return "heartbeat"
    if h("bounc","ball","juggle","gravcen","gravfreq","gravimeter"): return "bounce"
    if h("comet","meteor","shooting","sinelon"): return "comet"
    if h("ghost rider","ghost"): return "ghost"
    if h("two dots","two areas"): return "dots"
    if h("traffic"): return "traffic"
    if h("washing machine","rotozoom"): return "spin"
    if h("spaceship","ufo","saturn"): return "spaceship"
    if h("bee","crazy bees"): return "bees"
    if h("octopus"): return "octopus"
    if h("pacman","pac-man"): return "pacman"
    if h("dj light","disco"): return "dj"
    if h("scrolling text","text"): return "text"
    if h("black hole","blackhole"): return "blackhole"
    if h("galaxy","vortex","swirl","drift rose","spiral"): return "galaxy"
    if h("hourglass"): return "hourglass"
    if h("tv sim","tv "): return "tv"
    if h("bpm"): return "beat"
    if h("impact","sonic boom","colored burst"): return "impact"
    if h("akemi"): return "akemi"
    if h("halloween"): return "halloween"
    if h("candle"): return "candle"
    if h("fairy"): return "fairy"
    if h("spot"): return "spots"
    if h("plasma"): return "plasma"
    if h("aurora","polar"): return "aurora"
    if h("stream","flow","river"): return "stream"
    if h("drip","drop"): return "drip"
    if h("percent"): return "percent"
    if h("phased","phase"): return "phased"
    if h("loading","load"): return "loading"
    if h("dancing","dance"): return "dancing"
    if h("gradient","tricolor"): return "gradient"
    if h("blob","soap","clouds","plasmoid"): return "plasma"
    if h("tetri"): return "tetris"
    if h("wipe"): return "wipe"
    if h("android","larson","knight","scanner","scan"): return "scan"
    if h("saw"): return "saw"
    if h("dynamic","random colors"): return "dynamic"
    if h("rainbow"): return "rainbow"
    if h("running","runner"): return "running"
    if h("sweep"): return "sweep"
    if h("matri","game of life","dna","pixel"): return "matrix"
    if h("snow","frost","ice"): return "snow"
    if h("rain","waterfall","puddle","fall"): return "rain"
    if h("fire","flame","lava","ember","glow"): return "fire"
    if h("lighthouse","rotat"): return "lighthouse"
    if h("sunrise","sunset","sun ","day"): return "sunrise"
    if h("twinkle","star","firefl"): return "twinkle"
    if h("sparkle","dissolve","flicker"): return "sparkle"
    if h("ripple","pacifica","water","liquid","fluid","freq","geq"): return "ripple"
    if h("colorful","colorwave","colortwinkle"): return "colorful"
    if h("fade"): return "fade"
    if h("breathe","breath","pulse","sine","blend"): return "breathe"
    if h("strobe","blink","stutter","hyper"): return "strobe"
    if h("chase","marquee","railway","theater","train"): return "chase"
    if h("colorloop","pride","cycle","hue","spectrum","palette"): return "colorloop"
    if h("noise"): return "sparkle"
    return "wave"

def _flame(cx,hh,col,base=124):
    w=hh*0.30; top=base-hh
    return '<path d="M%d %d C%.0f %.0f %.0f %.0f %d %.0f C%.0f %.0f %.0f %.0f %d %d Z" fill="%s"/>'%(
        cx,base, cx-w,base-hh*0.4, cx-w*0.55,base-hh*0.78, cx,top,
        cx+w*0.55,base-hh*0.78, cx+w,base-hh*0.4, cx,base, col)

def anim(ph,m,seed=0):
    h0,spd,dr,n,sat=_p(seed); p=ph*spd*dr; M=math
    if m=="solid":
        return '<rect x="24" y="24" width="96" height="96" rx="16" fill="%s"/><rect x="40" y="40" width="48" height="30" rx="14" fill="%s"/>'%(_rgb(h0,sat,.85),_rgb(h0,sat*0.5,1))
    if m=="fade":
        v=0.15+0.85*(0.5+0.5*M.sin(p*0.7)); return '<rect x="24" y="34" width="96" height="76" rx="14" fill="%s"/>'%_rgb(h0,sat,v)
    if m=="breathe":
        br=0.5+0.5*M.sin(p*0.6); r=26+30*br
        return '<circle cx="72" cy="72" r="%.0f" fill="none" stroke="%s" stroke-width="4"/><circle cx="72" cy="72" r="%.0f" fill="%s"/>'%(r+14,_rgb(h0,.5,br),r,_rgb(h0,sat*0.85,0.5+0.5*br))
    if m=="colorful":
        o=""
        for i in range(6): o+='<rect x="%d" y="34" width="18" height="76" fill="%s"/>'%(16+i*19,_rgb(h0+i/6.0+ph*0.02*spd,.85,1))
        return o
    if m=="gradient":                               # smooth shifting gradient (banded, no defs)
        o=""
        for i in range(24): o+='<rect x="%.1f" y="40" width="5.5" height="64" fill="%s"/>'%(12+i*5,_rgb(h0+i*0.03+ph*0.02*spd,.8,1))
        return o
    if m=="police":
        a=ph%2; l=_rgb(0,.9,1) if a==0 else "#20242c"; r=_rgb(.62,.9,1) if a==1 else "#20242c"
        return '<rect x="14" y="30" width="54" height="84" rx="10" fill="%s"/><rect x="76" y="30" width="54" height="84" rx="10" fill="%s"/>'%(l,r)
    if m=="lightning":
        c=_rgb(.15,.5,1) if (int(ph*spd)%3==0) else "#2a2f38"
        return '<path d="M84 16 L44 78 L68 78 L54 128 L104 60 L78 60 Z" fill="%s"/>'%c
    if m=="popcorn":                                # kernels popping up
        o=""
        for i in range(6):
            ph2=(ph*spd+i*1.7); pop=abs(M.sin(ph2))
            x=20+i*20; y=118-pop*pop*92
            o+='<circle cx="%d" cy="%.0f" r="%d" fill="%s"/>'%(x,y,8 if pop>0.5 else 6,"#fff6d8" if pop>0.4 else "#c9a24a")
        return o+'<rect x="10" y="116" width="124" height="14" rx="3" fill="#7a4a12"/>'
    if m=="fireworks":                             # rocket streak + colourful burst with trails
        t=(ph%10)/10.0
        if t<0.35:
            y=124-t/0.35*70; return '<circle cx="72" cy="%.0f" r="4" fill="%s"/><rect x="70" y="%.0f" width="4" height="16" fill="%s"/>'%(y,_rgb(h0,.3,1),y+6,_rgb(h0,.5,.6))
        tt=(t-0.35)/0.65; rad=6+tt*52; o=""
        for i in range(12):
            a=i/12.0*2*M.pi
            o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>'%(72+M.cos(a)*rad,54+M.sin(a)*rad,max(1,5*(1-tt)),_rgb(h0+i*0.03,.9,1-tt*0.6))
        return o
    if m=="heartbeat":
        s=1.0+0.18*M.sin(p*1.6)
        return '<g transform="translate(72 78) scale(%.3f) translate(-72 -78)"><path d="M72 108 C24 72 30 36 54 36 C66 36 72 46 72 52 C72 46 78 36 90 36 C114 36 120 72 72 108 Z" fill="%s"/></g>'%(s,_rgb(0.98,.85,1))
    if m=="bounce":                                # bouncing balls (with squash + shadow)
        o=""
        for i in range(3):
            bph=abs(M.sin(p*0.7+i*1.0)); x=34+i*38; y=108-bph*72; sq=1.0-0.2*(1-bph)
            o+='<ellipse cx="%d" cy="116" rx="%d" ry="4" fill="#00000030"/>'%(x,14-int(bph*6))
            o+='<ellipse cx="%d" cy="%.0f" rx="%.0f" ry="%.0f" fill="%s"/>'%(x,y,14/sq,14*sq,_rgb(h0+i*0.14,.85,1))
        return o
    if m=="comet":
        x=(int(ph*7*spd))%168-12; o=""
        for k in range(6): o+='<circle cx="%.0f" cy="72" r="%.0f" fill="%s"/>'%(x-k*10*dr,10-k*1.4,_rgb(h0,.7,1-k*0.15))
        return o
    if m=="drip":                                  # a fat drop swells at a tap then falls
        t=((ph*spd)%7)/7.0; col=_rgb(h0+0.55,.6,1); o='<rect x="52" y="12" width="40" height="12" rx="4" fill="%s"/>'%_rgb(h0+0.55,.3,.6)
        if t<0.55:
            g=t/0.55; ry=16+g*22
            o+='<path d="M72 24 C%d 24 %d %d 72 %d C%d %d %d 24 72 24 Z" fill="%s"/>'%(52,52,24+ry*0.6,24+ry,92,24+ry*0.6,92,col)
        else:
            fy=24+(t-0.55)/0.45*96; o+='<path d="M72 %d C58 %d 58 %d 72 %d C86 %d 86 %d 72 %d Z" fill="%s"/>'%(int(fy),int(fy+8),int(fy+22),int(fy+30),int(fy+22),int(fy+8),int(fy),col)
        o+='<ellipse cx="72" cy="128" rx="20" ry="4" fill="%s"/>'%_rgb(h0+0.55,.4,.5)
        return o
    if m=="ghost":
        x=72+M.sin(p*0.5)*36; col=_rgb(h0,.25,1)
        return ('<path d="M%.0f 40 a30 30 0 0 1 30 30 v34 l-8 -8 -8 8 -7 -8 -7 8 -8 -8 -8 8 v-34 a30 30 0 0 1 30 -30 Z" fill="%s"/>'
                '<circle cx="%.0f" cy="66" r="5" fill="#1a1a1a"/><circle cx="%.0f" cy="66" r="5" fill="#1a1a1a"/>')%(x-30,col,x-10,x+10)
    if m=="dots":
        o=""
        for i in range(2): o+='<circle cx="%.0f" cy="%.0f" r="16" fill="%s"/>'%(72+M.cos(p*0.7+i*M.pi)*44,72+M.sin(p*0.9+i*M.pi)*40,_rgb(h0+i*0.4,.8,1))
        return o
    if m=="traffic":
        lit=int(ph*spd)%3; cols=[("#e6002a" if lit==0 else "#3a1015"),("#ffcc00" if lit==1 else "#3a3410"),("#2ee06e" if lit==2 else "#123a20")]
        o='<rect x="52" y="14" width="40" height="116" rx="12" fill="#111"/>'
        for i,c in enumerate(cols): o+='<circle cx="72" cy="%d" r="14" fill="%s"/>'%(38+i*34,c)
        return o
    if m=="spin":
        a=p*0.6; o='<circle cx="72" cy="72" r="46" fill="none" stroke="%s" stroke-width="6"/>'%_rgb(h0,.4,.7)
        for k in range(4): o+='<rect x="66" y="72" width="12" height="42" rx="4" fill="%s" transform="rotate(%.0f 72 72)"/>'%(_rgb(h0+k*0.08,.7,1),(a+k*M.pi/2)*57.3)
        return o
    if m=="spaceship":
        x=(int(ph*6*spd))%180-18
        return '<g transform="translate(%.0f 72)"><ellipse cx="0" cy="0" rx="34" ry="12" fill="%s"/><ellipse cx="0" cy="-8" rx="16" ry="12" fill="%s"/><circle cx="-16" cy="2" r="3" fill="#fff"/><circle cx="0" cy="4" r="3" fill="#fff"/><circle cx="16" cy="2" r="3" fill="#fff"/></g>'%(x,_rgb(h0,.5,.9),_rgb(h0+0.1,.3,1))
    if m=="bees":
        o=""
        for i in range(5):
            x=72+M.sin(p*1.3+i*2.1)*50; y=72+M.cos(p*1.7+i*1.3)*46
            o+='<circle cx="%.0f" cy="%.0f" r="8" fill="%s"/><ellipse cx="%.0f" cy="%.0f" rx="10" ry="5" fill="none" stroke="#ffffff44" stroke-width="1"/>'%(x,y,_rgb(0.14,.9,1),x,y-2)
        return o
    if m=="octopus":
        o='<circle cx="72" cy="60" r="24" fill="%s"/>'%_rgb(h0,.6,1)
        for k in range(6):
            a=k/6.0*2*M.pi; sw=M.sin(p*0.8+k)*16
            o+='<path d="M72 78 Q%.0f 104 %.0f 124" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(72+M.cos(a)*20+sw,72+M.cos(a)*40+sw,_rgb(h0,.6,1))
        return o
    if m=="pacman":
        x=(int(ph*6*spd))%176-16; mo2=abs(M.sin(p*1.4))*40
        o='<path d="M%.0f 72 L%.0f %.0f A34 34 0 1 0 %.0f %.0f Z" fill="#ffd200"/>'%(x,x+34*M.cos(mo2/57.3),72-34*M.sin(mo2/57.3),x+34*M.cos(mo2/57.3),72+34*M.sin(mo2/57.3))
        for d in range(3):
            dx=x+50+d*26
            if dx<150: o+='<circle cx="%.0f" cy="72" r="6" fill="#ffe680"/>'%dx
        return o
    if m=="dj":
        a=p*0.8
        return '<circle cx="72" cy="72" r="46" fill="#222"/><circle cx="72" cy="72" r="46" fill="none" stroke="%s" stroke-width="4"/><circle cx="72" cy="72" r="14" fill="%s"/><rect x="70" y="30" width="4" height="42" fill="#fff" transform="rotate(%.0f 72 72)"/>'%(_rgb(h0,.7,1),_rgb(h0+0.3,.7,1),a*57.3)
    if m=="text":
        o="";off=(int(ph*7*spd))%40
        for i in range(5): o+='<rect x="%.0f" y="52" width="20" height="40" rx="3" fill="%s"/>'%(140-i*32-off,_rgb(h0+i*0.1,.7,1))
        return o
    if m=="blackhole":
        o='<circle cx="72" cy="72" r="16" fill="#000"/>'
        for k in range(3): o+='<circle cx="72" cy="72" r="%.0f" fill="none" stroke="%s" stroke-width="5"/>'%(max(2,48-((ph*3*spd+k*16)%44)),_rgb(h0+k*0.1,.7,1))
        return o
    if m=="galaxy":
        o=""
        for k in range(14):
            t=k/14.0; a=p*0.5+t*6.5; r=12+t*54
            o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>'%(72+M.cos(a)*r,72+M.sin(a)*r,5-t*3,_rgb(h0+t*0.4,.7,1))
        return o
    if m=="hourglass":
        o='<path d="M34 20 L110 20 L78 72 L110 124 L34 124 L66 72 Z" fill="none" stroke="%s" stroke-width="5"/>'%_rgb(h0,.4,.8)
        o+='<circle cx="72" cy="%.0f" r="5" fill="%s"/><path d="M50 108 L94 108 L78 84 L66 84 Z" fill="%s"/>'%(72+((int(ph*4*spd))%40),_rgb(0.1,.8,1),_rgb(0.1,.7,1))
        return o
    if m=="tv":
        o=""
        for r in range(4):
            for c in range(4):
                v=((r*4+c)*13+int(ph*9*spd)+seed*7)%100/100.0
                o+='<rect x="%d" y="%d" width="30" height="30" fill="%s"/>'%(16+c*28,16+r*28,_rgb(h0+v*0.3,.2,0.3+v*0.7))
        return o
    if m=="beat":
        b=(p*1.4)%(2*M.pi); pulse=max(M.sin(b),M.sin(b-0.5))*0.5+0.5
        return '<path d="M72 106 C30 74 34 40 56 40 C66 40 72 50 72 56 C72 50 78 40 88 40 C110 40 114 74 72 106 Z" fill="%s" transform="translate(72 72) scale(%.2f) translate(-72 -72)"/>'%(_rgb(0.98,.8,1),0.7+0.3*pulse)
    if m=="impact":
        t=(ph%9)/9.0; rad=6+t*58
        return '<circle cx="72" cy="72" r="%.0f" fill="none" stroke="%s" stroke-width="%.0f"/><circle cx="72" cy="72" r="8" fill="%s"/>'%(rad,_rgb(h0,.8,1-t),max(1,10*(1-t)),_rgb(h0,.5,1-t*0.5))
    if m=="akemi":
        return '<circle cx="72" cy="72" r="42" fill="%s"/><path d="M40 44 Q72 20 104 44" fill="none" stroke="#1a1a1a" stroke-width="4"/><circle cx="58" cy="70" r="7" fill="#1a1a1a"/><circle cx="86" cy="70" r="7" fill="#1a1a1a"/><path d="M60 92 Q72 %.0f 84 92" fill="none" stroke="#1a1a1a" stroke-width="4"/>'%(_rgb(h0,.5,1),98+M.sin(p)*6)
    if m=="halloween":                             # jack-o'-lantern, flickering
        fl=0.75+0.25*(0.5+0.5*M.sin(p*3)); og=_rgb(0.07,.9,fl)
        o='<ellipse cx="72" cy="80" rx="46" ry="40" fill="%s"/><rect x="66" y="30" width="12" height="14" fill="#3a6b2a"/>'%og
        o+='<path d="M50 68 L64 78 L50 78 Z" fill="#1a1a1a"/><path d="M94 68 L80 78 L94 78 Z" fill="#1a1a1a"/>'
        o+='<path d="M48 96 L58 90 L64 98 L72 90 L80 98 L86 90 L96 96 L86 108 L58 108 Z" fill="#1a1a1a"/>'
        return o
    if m=="candle":                                # candle body + flickering flame
        fl=1.0+0.12*M.sin(p*4)
        o='<rect x="58" y="72" width="28" height="52" rx="4" fill="%s"/><rect x="58" y="72" width="28" height="8" fill="#ffffff40"/>'%_rgb(0.12,.3,.95)
        o+='<line x1="72" y1="64" x2="72" y2="72" stroke="#333" stroke-width="3"/>'
        o+='<g transform="translate(72 62) scale(%.2f) translate(-72 -62)">%s%s</g>'%(fl,_flame(72,44,_rgb(0.09,1,1),base=64),_flame(72,26,_rgb(0.14,.7,1),base=60))
        return o
    if m=="glitter":                               # fine sparse bright flecks
        o=""
        for i in range(16):
            x=(i*53+ph*7)%140+2; y=(i*89+ph*3)%128+2; on=((i*3+int(ph*4*spd))%16)<3
            if on: o+='<circle cx="%.0f" cy="%.0f" r="3" fill="#ffffff"/><circle cx="%.0f" cy="%.0f" r="6" fill="%s"/>'%(x,y,x,y,_rgb(h0+i*0.06,.4,1))
        return o
    if m=="fairy":                                 # fairy dust trail along a curve
        o=""
        for i in range(9):
            t=(i/9.0+ph*0.03*spd)%1.0; x=16+t*112; y=72+M.sin(t*6.28+p)*34; r=2+4*(1-abs(0.5-t)*2)
            o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>'%(x,y,r,_rgb(h0+t*0.5,.4,1))
        return o
    if m=="spots":                                 # moving stage spotlights
        o=""
        for i in range(3):
            x=72+M.sin(p*0.5+i*2.1)*44; y=72+M.cos(p*0.6+i*1.7)*36
            o+='<circle cx="%.0f" cy="%.0f" r="26" fill="%s"/><circle cx="%.0f" cy="%.0f" r="15" fill="%s"/>'%(x,y,_rgb(h0+i*0.2,.5,.45),x,y,_rgb(h0+i*0.2,.5,.95))
        return o
    if m=="plasma":                                # morphing colour blobs
        o=""
        for i in range(4):
            x=72+M.sin(p*0.5+i*1.6)*30; y=72+M.cos(p*0.7+i*2.0)*28; r=26+8*M.sin(p*0.9+i)
            o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>'%(x,y,r,_rgb(h0+i*0.18+ph*0.01,.8,1))
        return o
    if m=="aurora":                                # northern-lights curtains swaying
        o=""
        for k in range(4):
            xb=24+k*30; sw=M.sin(p*0.6+k*0.8)*12
            o+='<path d="M%.0f 18 Q%.0f 70 %.0f 126 L%.0f 126 Q%.0f 66 %.0f 18 Z" fill="%s"/>'%(xb+sw,xb-8+sw,xb+sw,xb+16+sw,xb+8+sw,xb+16+sw,_rgb(0.33+k*0.12,.7,.9))
        return o
    if m=="stream":                                # flowing particles across
        o=""
        for i in range(9):
            x=(i*18+ph*8*spd)%156-8; y=52+ (i%3)*20
            o+='<rect x="%.0f" y="%d" width="18" height="7" rx="3" fill="%s"/>'%(x,y,_rgb(h0+i*0.05,.7,1))
        return o
    if m=="percent":                               # progress bar filling
        f=((ph*spd)%20)/20.0
        return '<rect x="14" y="58" width="116" height="28" rx="8" fill="none" stroke="%s" stroke-width="4"/><rect x="18" y="62" width="%.0f" height="20" rx="5" fill="%s"/>'%(_rgb(h0,.4,.6),108*f,_rgb(h0,.8,1))
    if m=="phased":                                # phase-shifted sine lines
        o=""
        for k in range(3):
            pts=" ".join("%d,%.0f"%(x,72+M.sin(x*0.09+p+k*2.0)*(22+k*4)) for x in range(8,140,8))
            o+='<polyline points="%s" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round"/>'%(pts,_rgb(h0+k*0.15,.8,1))
        return o
    if m=="loading":                               # spinner (dots fading around)
        o=""
        for k in range(10):
            a=k/10.0*2*M.pi; br=((int(ph*spd)-k)%10)/10.0
            o+='<circle cx="%.0f" cy="%.0f" r="7" fill="%s"/>'%(72+M.cos(a)*42,72+M.sin(a)*42,_rgb(h0,.6,0.25+0.75*br))
        return o
    if m=="dancing":                               # a dancing figure
        sw=M.sin(p*1.5); col=_rgb(h0,.7,1)
        o='<circle cx="%.0f" cy="34" r="12" fill="%s"/>'%(72+sw*8,col)
        o+='<line x1="%.0f" y1="46" x2="72" y2="86" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(72+sw*8,col)
        o+='<line x1="72" y1="86" x2="%.0f" y2="122" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(72+30*sw,col)
        o+='<line x1="72" y1="86" x2="%.0f" y2="122" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(72-30*sw,col)
        o+='<line x1="72" y1="58" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="6" stroke-linecap="round"/>'%(72+34*sw,44-abs(sw)*10,_rgb(h0,.5,.9))
        o+='<line x1="72" y1="58" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="6" stroke-linecap="round"/>'%(72-34*sw,44-abs(sw)*10,_rgb(h0,.5,.9))
        return o
    if m=="gradient": pass
    if m=="wipe":
        ar=M.sin(p*0.6)*58*M.pi/180; x2=72+M.sin(ar)*100; y2=128-M.cos(ar)*100
        return ('<path d="M6 116 A84 84 0 0 1 138 116" fill="none" stroke="%s" stroke-width="4"/>'
                '<line x1="72" y1="126" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="5"/>'
                '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="11" stroke-linecap="round"/>'
                '<circle cx="72" cy="126" r="6" fill="%s"/>')%(_rgb(h0,.25,.5),x2,y2,_rgb(h0,.4,.6),72+M.sin(ar)*44,128-M.cos(ar)*44,x2,y2,_rgb(h0,.7,1),_rgb(h0,.5,.8))
    if m=="sweep":
        x=72+M.sin(p*0.5)*40; d=1 if M.cos(p*0.5)>0 else -1; o=""
        o+='<line x1="%.0f" y1="108" x2="%.0f" y2="28" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(x,x-26,_rgb(0.08,.55,.85))
        for k in range(-3,4): o+='<line x1="%.0f" y1="108" x2="%.0f" y2="132" stroke="%s" stroke-width="4"/>'%(x,x+k*8,_rgb(0.11,.5,1))
        for j in range(3): o+='<circle cx="%.0f" cy="%.0f" r="%d" fill="%s"/>'%(x+d*(26+j*13),122-j*5,4-j,_rgb(h0,.25,.7))
        return o
    if m=="scan":
        pos=72+M.sin(p*0.9)*54; o=""
        for k in range(6):
            xx=pos-k*8*(1 if M.cos(p*0.9)>0 else -1)
            o+='<rect x="%.0f" y="30" width="9" height="84" rx="4" fill="%s"/>'%(xx,_rgb(0,0.9,1-k*0.15))
        return o
    if m=="running":                               # runner (thick, leaning, clear stride)
        sw=M.sin(p*1.8); col=_rgb(h0,.65,1)
        o='<circle cx="88" cy="30" r="11" fill="%s"/>'%col
        o+='<line x1="84" y1="41" x2="60" y2="80" stroke="%s" stroke-width="9" stroke-linecap="round"/>'%col
        o+='<polyline points="60,80 %d,%d %d,%d" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round"/>'%(84,100,92+int(sw*10),118,col)
        o+='<polyline points="60,80 %d,%d %d,%d" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round"/>'%(44,96,30-int(sw*10),112,col)
        o+='<polyline points="70,52 %d,64 %d,58" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(96-int(sw*8),108-int(sw*6),_rgb(h0,.5,.9))
        o+='<polyline points="70,52 %d,66 %d,74" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(50+int(sw*8),40+int(sw*6),_rgb(h0,.5,.9))
        return o
    if m=="saw":
        x=M.sin(p*0.8)*16; by=62; o='<rect x="%.0f" y="%d" width="94" height="18" rx="3" fill="%s"/>'%(20+x,by,_rgb(h0,.2,.85))
        for k in range(9): tx=22+x+k*10; o+='<path d="M%.0f %d L%.0f %d L%.0f %d Z" fill="%s"/>'%(tx,by+18,tx+5,by+30,tx+10,by+18,_rgb(h0,.2,.85))
        o+='<rect x="%.0f" y="%d" width="26" height="30" rx="7" fill="%s"/>'%(4+x,by-6,_rgb(0.07,.6,.9))
        return o
    if m=="dynamic":
        o=""
        for r in range(3):
            for c in range(4):
                hue=(( (r*4+c)*67 + int(ph*2*spd)*53 + seed*29)%360)/360.0
                o+='<rect x="%d" y="%d" width="30" height="34" rx="4" fill="%s"/>'%(10+c*32,20+r*36,_rgb(hue,.8,1))
        return o
    if m=="tetris":                                # a fall in progress: settled stack + a falling piece
        cell=14; o=""
        stack=[(2,7),(3,7),(4,7),(2,8),(3,8),(5,8),(6,8),(4,9),(5,9),(1,8),(1,9),(6,9),(0,9),(7,9)]
        for cx,cy in stack: o+='<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" stroke="#1a1a1a" stroke-width="1"/>'%(8+cx*cell,20+cy*cell,cell,cell,_rgb((cx*0.13),.6,.9))
        shp=[(0,0),(1,0),(2,0),(1,1)][:]; fy=((int(ph*4*spd))%7); col=_rgb(h0,.8,1)
        for dx,dy in shp: o+='<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" stroke="#1a1a1a" stroke-width="1"/>'%(50+dx*cell,10+(fy+dy)*cell,cell,cell,col)
        return o
    if m=="matrix":
        o=""
        for c in range(6):
            x=16+c*20; y=(int(ph*10*spd)+c*37+seed*5)%160-30
            for k in range(4): o+='<rect x="%d" y="%d" width="12" height="14" rx="2" fill="%s"/>'%(x,y-k*18,_rgb(0.33,.8,1-k*0.28))
        return o
    if m=="snow":
        o=""
        for i in range(5):
            x=18+i*28; y=(int(ph*8*spd)+i*33+seed*7)%160-16
            o+='<g stroke="#dff1ff" stroke-width="3" stroke-linecap="round" transform="translate(%d %d)"><line x1="0" y1="-9" x2="0" y2="9"/><line x1="-8" y1="-5" x2="8" y2="5"/><line x1="8" y1="-5" x2="-8" y2="5"/></g>'%(x,y)
        return o
    if m=="rain":
        o="";step=132//max(1,n-2)
        for i in range(n-1): o+='<rect x="%d" y="%d" width="9" height="28" rx="4" fill="%s"/>'%(18+i*step,(int(ph*13*spd)+i*41+seed*7)%150-20,_rgb(h0+0.55,.65,1))
        return o
    if m=="fire":
        o=""
        for k,(cx,bh,off) in enumerate([(46,0.85,0.0),(72,1.15,1.6),(98,0.8,3.1)]):
            hh=(66+34*(0.5+0.5*M.sin(p*1.3+off)))*bh
            o+=_flame(cx,hh,_rgb(0.02+0.09*k,1,1))
        return o
    if m=="lighthouse":
        a=p*0.5
        return '<circle cx="72" cy="72" r="12" fill="%s"/><path d="M72 72 L%.0f %.0f L%.0f %.0f Z" fill="%s"/>'%(_rgb(h0,.3,1),72+M.cos(a)*70,72+M.sin(a)*70,72+M.cos(a+0.5)*70,72+M.sin(a+0.5)*70,_rgb(h0,.6,.9))
    if m=="sunrise":
        y=110-(0.5+0.5*M.sin(p*0.4))*40
        return '<circle cx="72" cy="%.0f" r="26" fill="%s"/><rect x="0" y="116" width="144" height="28" fill="%s"/>'%(y,_rgb(0.09,.85,1),_rgb(0.08,.6,.5))
    if m=="twinkle":
        o=""
        for i in range(6):
            x=22+(i*47)%110; yv=30+(i*53)%84; lit=((i*5+int(ph*3*spd)+seed)%6)<2; r=11 if lit else 5; col=_rgb(h0+i*0.1,.5,1) if lit else "#39414e"
            o+='<path d="M%d %d l%.1f %.1f l%.1f %.1f l%.1f %.1f l%.1f %.1f Z" fill="%s"/>'%(x,yv-r,r*0.3,r*0.7,r*0.7,r*0.3,-r*0.7,r*0.3,-r*0.3,r*0.7,col)
        return o
    if m=="sparkle":
        o=""
        for i in range(9):
            cx,cy=24+(i%3)*48,24+(i//3)*48; lit=((i*7+int(ph*3*spd)+seed)%9)<3
            o+='<circle cx="%d" cy="%d" r="%d" fill="%s"/>'%(cx,cy,13 if lit else 5,_rgb(h0+i*0.05,sat,1) if lit else "#39414e")
        return o
    if m=="ripple":
        o=""
        for k in range(3):
            rad=((ph*3*spd+k*16)%48)+6; o+='<circle cx="72" cy="72" r="%.0f" fill="none" stroke="%s" stroke-width="6"/>'%(rad,_rgb(h0+k*0.1,.6,1-rad/60))
        return o
    if m=="strobe":
        c=_rgb(h0,sat,1) if ph%2==0 else "#272c36"
        return "".join('<circle cx="%d" cy="%d" r="16" fill="%s"/>'%(x,y,c) for x,y in ((48,48),(96,48),(48,96),(96,96)))
    if m=="chase":
        pos=int(ph*spd+seed)%7; o="";base=colorsys.hsv_to_rgb(h0,.75,1)
        for i in range(7):
            br=max(0.14,1-(((pos-i*dr)%7+7)%7)*0.30); r,g,b=(int(26+(round(base[k]*255)-26)*br) for k in range(3))
            o+='<circle cx="%d" cy="72" r="9" fill="rgb(%d,%d,%d)"/>'%(18+i*18,r,g,b)
        return o
    if m=="rainbow":
        o=""
        for k in range(6): o+='<path d="M18 128 A%d %d 0 0 1 126 128" fill="none" stroke="%s" stroke-width="9"/>'%(54-k*8,54-k*8,_rgb((k/6.0+ph*0.03*spd)%1.0,.9,1))
        return o
    if m=="colorloop":
        return '<rect x="20" y="20" width="104" height="104" rx="16" fill="%s"/>'%_rgb(h0+ph*0.03*spd,.8,1)
    wd=120//n; o=""                                # wave (default)
    for i in range(n):
        br=0.30+0.70*(0.5+0.5*M.sin(p*0.6-i*0.95)); hh=22+96*br
        o+='<rect x="%d" y="%.0f" width="%d" height="%.0f" rx="3" fill="%s"/>'%(12+i*wd,128-hh,wd-3,hh,_rgb(h0+((i*34+ph*12*spd)%360)/360,0.85,br))
    return o
def wrap(i): return '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144"><rect width="144" height="144" fill="#1a1a1a"/>%s</svg>'%i
