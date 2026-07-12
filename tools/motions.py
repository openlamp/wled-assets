import math, colorsys
def _rgb(h,s,v): return "rgb(%d,%d,%d)"%tuple(round(c*255) for c in colorsys.hsv_to_rgb(h%1.0,s,v))
def _p(seed):
    return (((seed*47)%360)/360.0, 0.55+((seed*13)%110)/100.0, 1 if (seed//2)%2 else -1, 5+(seed%4), 0.7+((seed*5)%30)/100.0)
def motion(name):
    n=(name or "").lower()
    def h(*k): return any(x in n for x in k)
    if h("solid","static","fill"): return "solid"
    if h("police"): return "police"
    if h("lightning"): return "lightning"
    if h("firework","popcorn"): return "fireworks"
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
    if h("bpm","pulse "): return "beat"
    if h("impact","sonic boom","colored burst","fireworks 1d"): return "impact"
    if h("akemi"): return "akemi"
    if h("blob","soap","clouds","plasmoid"): return "blobs"
    if h("tetri"): return "tetris"                 # Tetrix -> falling tetrominoes
    if h("wipe"): return "wipe"                     # windshield wiper
    if h("scan"): return "scan"                     # radar scanner
    if h("saw"): return "saw"                        # saw tool
    if h("dynamic","random colors"): return "dynamic"
    if h("rainbow"): return "rainbow"
    if h("running","runner"): return "running"      # a runner
    if h("sweep","larson","knight","android"): return "sweep"   # broom
    if h("matri","game of life","dna","pixel"): return "matrix"
    if h("snow","frost","ice"): return "snow"
    if h("rain","drip","drop","waterfall","puddle","fall"): return "rain"
    if h("fire","flame","lava","candle","ember","glow","halloween"): return "fire"
    if h("lighthouse","rotat"): return "lighthouse"
    if h("sunrise","sunset","sun ","day"): return "sunrise"
    if h("twinkle","star","fairy","glitter","firefl"): return "twinkle"
    if h("sparkle","dissolve","flicker","noise","spot"): return "sparkle"
    if h("ripple","plasma","pacifica","water","liquid","fluid","aurora","flow","stream","freq","geq"): return "ripple"
    if h("breathe","breath","fade","sine","blend"): return "breathe"
    if h("strobe","blink","stutter","hyper"): return "strobe"
    if h("chase","marquee","railway","theater","train","loading","dancing"): return "chase"
    if h("colorloop","colorwave","colortwinkle","colorful","pride","cycle","hue","spectrum","palette"): return "colorloop"
    if h("sawtooth","gradient","tricolor"): return "saw"
    return "wave"

def _flame(cx,hh,col):
    w=hh*0.30; top=124-hh
    return '<path d="M%d 124 C%.0f %.0f %.0f %.0f %d %.0f C%.0f %.0f %.0f %.0f %d 124 Z" fill="%s"/>'%(
        cx, cx-w,124-hh*0.4, cx-w*0.55,124-hh*0.78, cx,top,
        cx+w*0.55,124-hh*0.78, cx+w,124-hh*0.4, cx, col)

def anim(ph,m,seed=0):
    h0,spd,dr,n,sat=_p(seed); p=ph*spd*dr; M=math
    if m=="solid": return '<rect x="26" y="26" width="92" height="92" rx="14" fill="%s"/>'%_rgb(h0,sat,.9)
    if m=="police":
        a=ph%2; l=_rgb(0,.9,1) if a==0 else "#20242c"; r=_rgb(.62,.9,1) if a==1 else "#20242c"
        return '<rect x="14" y="30" width="54" height="84" rx="10" fill="%s"/><rect x="76" y="30" width="54" height="84" rx="10" fill="%s"/>'%(l,r)
    if m=="lightning":
        c=_rgb(.15,.5,1) if (int(ph*spd)%3==0) else "#2a2f38"
        return '<path d="M84 16 L44 78 L68 78 L54 128 L104 60 L78 60 Z" fill="%s"/>'%c
    if m=="fireworks":
        t=(ph%8)/8.0; rad=8+t*54; o='<circle cx="72" cy="72" r="6" fill="%s"/>'%_rgb(h0,.3,1-t) if t<0.2 else ''
        for i in range(10):
            a=i/10.0*2*M.pi; o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>'%(72+M.cos(a)*rad,72+M.sin(a)*rad,max(1,6*(1-t)),_rgb(h0+i*0.04,.9,1-t*0.7))
        return o
    if m=="heartbeat":
        s=1.0+0.18*M.sin(p*1.6)
        return '<g transform="translate(72 78) scale(%.3f) translate(-72 -78)"><path d="M72 108 C24 72 30 36 54 36 C66 36 72 46 72 52 C72 46 78 36 90 36 C114 36 120 72 72 108 Z" fill="%s"/></g>'%(s,_rgb(0.98,.85,1))
    if m=="bounce":
        o=""
        for i in range(3): o+='<circle cx="%d" cy="%.0f" r="13" fill="%s"/>'%(34+i*38,110-abs(M.sin(p*0.6+i*1.1))*74,_rgb(h0+i*0.14,.8,1))
        return o
    if m=="comet":
        x=(int(ph*7*spd))%168-12; o=""
        for k in range(6): o+='<circle cx="%.0f" cy="72" r="%.0f" fill="%s"/>'%(x-k*10*dr,10-k*1.4,_rgb(h0,.7,1-k*0.15))
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
    if m=="blobs":
        o=""
        for i in range(3): o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>'%(44+i*28,72+14*M.sin(p*0.5+i),22+10*M.sin(p*0.7+i*2),_rgb(h0+i*0.16,.7,1))
        return o
    if m=="wipe":                                   # windshield wiper
        ar=M.sin(p*0.6)*58*M.pi/180; x2=72+M.sin(ar)*100; y2=128-M.cos(ar)*100
        return ('<path d="M6 116 A84 84 0 0 1 138 116" fill="none" stroke="%s" stroke-width="4"/>'
                '<line x1="72" y1="126" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="5"/>'
                '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="11" stroke-linecap="round"/>'
                '<circle cx="72" cy="126" r="6" fill="%s"/>')%(_rgb(h0,.25,.5),x2,y2,_rgb(h0,.4,.6),72+M.sin(ar)*44,128-M.cos(ar)*44,x2,y2,_rgb(h0,.7,1),_rgb(h0,.5,.8))
    if m=="sweep":                                  # a broom sweeping
        x=72+M.sin(p*0.5)*40; d=1 if M.cos(p*0.5)>0 else -1; o=""
        o+='<line x1="%.0f" y1="108" x2="%.0f" y2="28" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(x,x-26,_rgb(0.08,.55,.85))
        for k in range(-3,4): o+='<line x1="%.0f" y1="108" x2="%.0f" y2="132" stroke="%s" stroke-width="4"/>'%(x,x+k*8,_rgb(0.11,.5,1))
        for j in range(3): o+='<circle cx="%.0f" cy="%.0f" r="%d" fill="%s"/>'%(x+d*(26+j*13),122-j*5,4-j,_rgb(h0,.25,.7))
        return o
    if m=="scan":                                   # radar scanner
        a=p*0.8; o='<circle cx="72" cy="72" r="48" fill="none" stroke="%s" stroke-width="3"/><circle cx="72" cy="72" r="28" fill="none" stroke="%s" stroke-width="2"/>'%(_rgb(0.33,.4,.5),_rgb(0.33,.3,.4))
        o+='<line x1="72" y1="72" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="4"/>'%(72+M.cos(a)*48,72+M.sin(a)*48,_rgb(0.33,.8,1))
        lit=abs(((a)%(2*M.pi))-2.0)<0.45
        o+='<circle cx="%.0f" cy="%.0f" r="%d" fill="%s"/>'%(72+M.cos(2.0)*34,72+M.sin(2.0)*34,7 if lit else 4,_rgb(0.33,.9,1) if lit else _rgb(0.33,.4,.4))
        return o
    if m=="running":                                # a runner in stride (bent knees)
        sw=M.sin(p*1.6); col=_rgb(h0,.6,1)
        o='<circle cx="82" cy="32" r="12" fill="%s"/>'%col
        o+='<line x1="79" y1="44" x2="62" y2="82" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%col
        o+='<polyline points="62,82 %d,104 %d,120" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(88,94+int(sw*8),col)
        o+='<polyline points="62,82 %d,100 %d,118" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(46,38-int(sw*8),col)
        o+='<line x1="70" y1="56" x2="%d" y2="72" stroke="%s" stroke-width="6" stroke-linecap="round"/>'%(96-int(sw*8),_rgb(h0,.5,.9))
        o+='<line x1="70" y1="56" x2="%d" y2="76" stroke="%s" stroke-width="6" stroke-linecap="round"/>'%(48+int(sw*8),_rgb(h0,.5,.9))
        return o
    if m=="saw":                                    # a saw tool cutting
        x=M.sin(p*0.8)*16; by=62; o='<rect x="%.0f" y="%d" width="94" height="18" rx="3" fill="%s"/>'%(20+x,by,_rgb(h0,.2,.85))
        for k in range(9): tx=22+x+k*10; o+='<path d="M%.0f %d L%.0f %d L%.0f %d Z" fill="%s"/>'%(tx,by+18,tx+5,by+30,tx+10,by+18,_rgb(h0,.2,.85))
        o+='<rect x="%.0f" y="%d" width="26" height="30" rx="7" fill="%s"/>'%(4+x,by-6,_rgb(0.07,.6,.9))
        return o
    if m=="dynamic":                                # ever-changing colour cells
        o=""
        for r in range(3):
            for c in range(4):
                hue=(( (r*4+c)*67 + int(ph*2*spd)*53 + seed*29)%360)/360.0
                o+='<rect x="%d" y="%d" width="30" height="34" rx="4" fill="%s"/>'%(10+c*32,20+r*36,_rgb(hue,.8,1))
        return o
    if m=="tetris":                                 # falling tetrominoes (varied shapes)
        cell=15; shapes=[[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(2,0),(1,1)],[(0,0),(0,1),(0,2),(1,2)],[(1,0),(2,0),(0,1),(1,1)]]
        o=""
        for pi,(colx,sh) in enumerate([(8,0),(60,2),(104,3)]):
            shp=shapes[(sh+seed)%5]; y=((int(ph*3*spd)+pi*30)%150)-30; col=_rgb(h0+pi*0.2,.75,1)
            for dx,dy in shp: o+='<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" stroke="#1a1a1a" stroke-width="1"/>'%(colx+dx*cell,y+dy*cell,cell,cell,col)
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
    if m=="fire":                                   # real flames (flame tongues)
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
    if m=="breathe":
        br=0.35+0.65*(0.5+0.5*M.sin(p*0.5)); return '<circle cx="72" cy="72" r="%.0f" fill="%s"/>'%(28+34*br,_rgb(h0,sat*0.85,br))
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
