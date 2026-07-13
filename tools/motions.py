import math, colorsys
def _rgb(h,s,v):
    # Refined ceilings (2026-07-12): cap saturation + value so no motion renders as neon.
    # Qualitative, cinematic tones instead of flashy primaries. Hard-coded hex bypass this.
    s=min(s,0.62); v=min(max(0.0,v),0.92)
    return "rgb(%d,%d,%d)"%tuple(round(c*255) for c in colorsys.hsv_to_rgb(h%1.0,s,v))
def _p(seed):
    return (((seed*47)%360)/360.0, 0.55+((seed*13)%110)/100.0, 1 if (seed//2)%2 else -1, 5+(seed%4), 0.7+((seed*5)%30)/100.0)
def motion(name):
    n=(name or "").lower()
    def h(*k): return any(x in n for x in k)
    # --- precise per-name routing (wins over the generic families below) ---
    if h("geq","freqwave","freqmap","freqmatrix","freqpixels","noisemeter"): return "geq"  # audio equalizer bars
    if h("plasma ball"): return "plasmaball"   # electric plasma globe
    if h("spray"): return "spray"              # particle spray from a nozzle
    if h("springy","spring"): return "spring"  # spring-connected bob
    if h("rsvd"): return "reserved"            # reserved/unused WLED slot — neutral placeholder
    if h("solid pattern tri"): return "pattern3"  # 3-colour striped pattern
    if h("solid pattern"): return "pattern"    # on/off striped pattern
    if h("pixelwave"): return "wave"           # "…wave" -> a travelling wave, not rings
    if h("pixels"): return "twinkle"           # random pixel twinkles
    if h("starburst"): return "fireworks"      # exploding star fragments
    if h("metaball"): return "plasma"          # merging blobs
    if h("hiphotic"): return "plasma"          # moving plasma
    if h("attractor"): return "blackhole"      # particles round a black hole
    if h("slow transition"): return "fade"     # very slow colour fade
    if h("shimmer"): return "glitter"          # shimmering sparkle
    if h("fill noise"): return "sparkle"       # noise fill
    if h("glitter"): return "glitter"
    if h("chunchun"): return "birds"           # flock of birds
    if h("dna"): return "dna"                  # double helix (before matrix/galaxy)
    if h("halloween eyes"): return "spookeyes" # a pair of glowing eyes in the dark
    if h("tartan"): return "tartan"            # Scottish plaid: crossed bands
    if h("julia"): return "fractal"            # Julia-set fractal
    if h("sun radiation","colored burst"): return "sunburst"  # a sun/rays radiating
    if h("game of life"): return "gol"         # cellular-automaton grid
    if h("rocktaves","octave"): return "notes" # musical notes
    if h("soap"): return "bubbles"             # floating soap bubbles
    if h("image"): return "image"              # a picture frame
    if h("swirl","vortex","drift"): return "swirl"  # spinning vortex (Drift, Swirl, Vortex, Drift Rose)
    if h("frizzle"): return "geo"              # moving geometric patterns
    if h("sindot"): return "swirl"             # revolving dots
    if h("blend"): return "gradient"           # smooth colour blend
    if h("icu"): return "eye"                  # a single looking eye (before halloween)
    if h("lake"): return "lake"                # calm horizontal water shimmer (distinct from ripple rings)
    if h("volcano"): return "fire"
    if h("solid","static","fill"): return "solid"
    if h("police"): return "police"
    if h("lightning"): return "lightning"
    if h("popcorn"): return "popcorn"
    if h("fireworks 1d","firework 1d"): return "fireworks1d"  # bursts along a 1D strip
    if h("firework"): return "fireworks"
    if h("heart"): return "heartbeat"
    if h("bounc","ball","juggle","gravcen","gravfreq","gravimeter"): return "bounce"
    if h("meteor"): return "meteor"            # diagonal falling streak (distinct from horizontal comet)
    if h("sinelon rainbow"): return "sinelonrainbow"
    if h("sinelon dual"): return "sinelondual"
    if h("sinelon"): return "sinelon"
    if h("comet","shooting"): return "comet"
    if h("ghost rider","ghost"): return "ghost"
    if h("two dots","two areas"): return "dots"
    if h("traffic"): return "traffic"
    if h("washing machine"): return "washing"        # tumbling drum (distinct from spin/rotozoomer)
    if h("rotozoom"): return "spin"
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
    # salvage effects that used to fall to the generic "wave" fallback — give each a
    # more telling existing motion (Benoit 2026-07-13, animation review pass 1).
    if h("perlin","waving cell"): return "plasma"       # smooth noise field, not a flat wave
    if h("funky plank","blurz"): return "geq"           # audio bar-graph effects
    if h("distortion","waverly"): return "wave"         # "…waves" -> travelling waves, not rings
    if h("ps box","ps 1d balance"): return "bounce"     # particle-system gravity/bounce
    if h("copy segment"): return "copyseg"              # a pattern block duplicated across the strip
    # (Oscillate + Wavesins stay on "wave" — an oscillating/sine waveform genuinely fits.)
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
    if h("tri wipe","triwipe"): return "triwipe"        # 3 colours wiping in (not the monocolour wipe)
    if h("wipe"): return "wipe"
    if h("android","larson","knight","scanner","scan"): return "scan"
    if h("saw"): return "saw"
    if h("random colors"): return "randcolor"  # whole strip = ONE random colour, changing
    if h("dynamic"): return "dynamic"          # each pixel a random colour (mosaic)
    if h("rainbow"): return "rainbow"
    if h("running","runner"): return "running"
    if h("sweep random"): return "sweeprandom"          # sweeps that jump to random positions
    if h("sweep"): return "sweep"
    if h("matri","game of life","dna","pixel"): return "matrix"
    if h("snow","frost","ice"): return "snow"
    if h("rain","waterfall","puddle","fall"): return "rain"
    if h("fire","flame","lava","ember","glow"): return "fire"
    if h("lighthouse","rotat"): return "lighthouse"
    if h("sunrise","sunset","sun ","day"): return "sunrise"
    if h("twinkle","star","firefl"): return "twinkle"
    if h("dissolve"): return "dissolve"                 # progressive pixel fill/clear (distinct from sparkle)
    if h("sparkle","flicker"): return "sparkle"
    if h("pacifica"): return "pacifica"                 # calm layered ocean swells
    if h("ripple","water","liquid","fluid","freq","geq"): return "ripple"
    if h("colorful","colorwave","colortwinkle"): return "colorful"
    if h("fade"): return "fade"
    if h("sine"): return "wave"                         # a sine curve, not a breathing glow
    if h("breathe","breath","pulse","blend"): return "breathe"
    if h("blink"): return "blink"   # an eyelid blink (Blink Rainbow already caught by rainbow above)
    if h("strobe","stutter","hyper"): return "strobe"
    if h("railway"): return "railway"                   # two rails with alternating lights
    if h("chase","marquee","theater","train"): return "chase"
    if h("colorloop","pride","cycle","hue","spectrum","palette"): return "colorloop"
    if h("noise"): return "noise"                       # smooth shifting colour field (distinct from GEQ bars)
    if h("lissajou"): return "lissajous"
    return "wave"

def _flame(cx,hh,col,base=124):
    w=hh*0.30; top=base-hh
    return '<path d="M%d %d C%.0f %.0f %.0f %.0f %d %.0f C%.0f %.0f %.0f %.0f %d %d Z" fill="%s"/>'%(
        cx,base, cx-w,base-hh*0.4, cx-w*0.55,base-hh*0.78, cx,top,
        cx+w*0.55,base-hh*0.78, cx+w,base-hh*0.4, cx,base, col)

def _mhue(m):   # a stable, hand-picked hue per motion (free of the effect seed)
    # Curated, cohesive palette (2026-07-12, Benoit: "moins arc-en-ciel, plus réaliste").
    # Three restrained families instead of the full wheel + a random-hash fallback:
    #   warm  ~0.03-0.10  ember / amber / gold  (fire, energy, mechanical sweeps)
    #   cool  ~0.47-0.58  teal / ocean / soft blue  (water, calm, motion trails)
    #   deep  ~0.66-0.80  indigo / dusty violet  (cosmic, moody)
    # Saturation is kept moderate (see `sat` below) so nothing reads as neon.
    fixed={
     # deep / rich
     "octopus":0.74,"dj":0.72,"galaxy":0.70,"blackhole":0.67,"plasma":0.73,"fairy":0.80,
     # cool / calm
     "wave":0.52,"ripple":0.52,"stream":0.52,"drip":0.53,"comet":0.55,"dots":0.55,"chase":0.54,
     "spin":0.55,"spaceship":0.56,"hourglass":0.50,"phased":0.58,"loading":0.55,"text":0.54,
     "wipe":0.53,"lissajous":0.50,"breathe":0.57,"fade":0.54,"percent":0.36,"blink":0.09,
     "birds":0.55,"dna":0.52,"eye":0.09,
     # warm / earthy
     "scan":0.02,"saw":0.09,"solid":0.09,"lighthouse":0.09,"spots":0.11,"bounce":0.09,
     "impact":0.03,"running":0.08,"dancing":0.95,"colorful":0.09,"gradient":0.09}
    return fixed.get(m, 0.09)   # refined warm-amber default (no more per-name random hue)

def anim(ph,m,seed=0):
    h0,spd,dr,n,sat=_p(seed); p=ph*spd*dr; M=math
    h0=_mhue(m); sat=0.58  # fixed deliberate colour PER MOTION; moderate sat = refined, not neon
    if m=="solid":
        return '<rect x="24" y="24" width="96" height="96" rx="16" fill="%s"/><rect x="40" y="40" width="48" height="30" rx="14" fill="%s"/>'%(_rgb(h0,sat,.85),_rgb(h0,sat*0.5,1))
    if m=="fade":                                   # slow COLOUR crossfade (not a brightness pulse — that's breathe)
        hue=(p*0.09)%1.0; return '<rect x="24" y="34" width="96" height="76" rx="14" fill="%s"/>'%_rgb(hue,sat,0.88)
    if m=="breathe":                               # a soft glow that swells + brightens, then fades (lung-like)
        br=0.5+0.5*M.sin(p*0.55); r=30+24*br
        o ='<circle cx="72" cy="72" r="%.0f" fill="%s" opacity="0.22"/>'%(r+24,_rgb(h0,.5,.9))   # outer halo
        o+='<circle cx="72" cy="72" r="%.0f" fill="%s" opacity="0.5"/>'%(r+11,_rgb(h0,.55,.95))
        o+='<circle cx="72" cy="72" r="%.0f" fill="%s"/>'%(r,_rgb(h0,sat,0.35+0.6*br))            # bright core
        return o
    if m=="colorful":
        o=""
        for i in range(6): o+='<rect x="%d" y="34" width="18" height="76" fill="%s"/>'%(16+i*19,_rgb(h0+i/6.0+ph*0.02*spd,.55,.9))
        return o
    if m=="gradient":                               # smooth shifting gradient (banded, no defs)
        o=""
        for i in range(24): o+='<rect x="%.1f" y="40" width="5.5" height="64" fill="%s"/>'%(12+i*5,_rgb(h0+i*0.03+ph*0.02*spd,.55,.9))
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
    if m=="comet":                                 # bright white head + a long tapering glowing tail
        x=(ph*8*spd)%180-20; o=""
        for k in range(14):
            tx=x-k*7*dr
            if -8<tx<150: o+='<circle cx="%.0f" cy="72" r="%.1f" fill="%s" opacity="%.2f"/>'%(tx,max(1,9-k*0.55),_rgb(h0,.6,1),max(0.05,1-k*0.09))
        o+='<circle cx="%.0f" cy="72" r="10" fill="%s"/>'%(x,_rgb(h0,.4,1))
        o+='<circle cx="%.0f" cy="72" r="5.5" fill="#ffffff"/>'%x                                # incandescent core
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
    if m=="bees":                                   # buzzing bees: striped body + fluttering wing + erratic jitter
        o=""
        for i in range(5):
            x=72+M.sin(p*1.3+i*2.1)*46+M.sin(p*7+i)*4   # slow orbit + fast buzz jitter
            y=72+M.cos(p*1.7+i*1.3)*42+M.cos(p*6+i)*4
            wf=2.6+abs(M.sin(p*9+i))*5                    # wing flap
            o+='<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="2.6" fill="#ffffff66"/>'%(x,y-6,wf)   # wing (fluttering)
            o+='<ellipse cx="%.1f" cy="%.1f" rx="9" ry="6.5" fill="%s"/>'%(x,y,_rgb(0.13,.95,1))  # yellow abdomen
            o+='<rect x="%.1f" y="%.1f" width="12" height="2.2" rx="1" fill="#20160a"/>'%(x-6,y-1.1)  # HORIZONTAL stripe
        return o
    if m=="octopus":
        o='<circle cx="72" cy="60" r="24" fill="%s"/>'%_rgb(h0,.6,1)
        for k in range(6):
            a=k/6.0*2*M.pi; sw=M.sin(p*0.8+k)*16
            o+='<path d="M72 78 Q%.0f 104 %.0f 124" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(72+M.cos(a)*20+sw,72+M.cos(a)*40+sw,_rgb(h0+k*0.03,.6,1))
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
    if m=="text":                                  # scrolling letters (reads as "text")
        off=(int(ph*6*spd)+70)%150                 # start with the word on-screen (good thumbnail)
        return ('<clipPath id="tc"><rect x="8" y="16" width="128" height="112" rx="10"/></clipPath>'
                '<g clip-path="url(#tc)"><text x="%d" y="96" font-family="Helvetica" font-size="56" '
                'font-weight="bold" fill="%s">WLED</text></g>'%(132-off,_rgb(h0,.7,1)))
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
    if m=="glitter":                               # dense fine shimmer: many small flecks fading in and out
        o=""
        for i in range(26):
            x=(i*53+ph*7)%140+2; y=(i*89+ph*3)%128+2; t=(i*3+int(ph*5*spd))%12
            if t<4:                                 # a fleck's brief sparkle, brightest on the first frame
                b=1-t*0.22; r=1.6+b*2.4
                o+='<circle cx="%.0f" cy="%.0f" r="%.1f" fill="%s" opacity="%.2f"/>'%(x,y,r,_rgb(h0+i*0.06,.35,1),b)
                o+='<circle cx="%.0f" cy="%.0f" r="%.1f" fill="#ffffff" opacity="%.2f"/>'%(x,y,r*0.5,b)
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
            o+='<circle cx="%.0f" cy="%.0f" r="26" fill="%s"/><circle cx="%.0f" cy="%.0f" r="15" fill="%s"/>'%(x,y,_rgb(h0+i*0.33,.5,.45),x,y,_rgb(h0+i*0.33,.6,.95))
        return o
    if m=="plasma":                                # morphing colour blobs
        o=""
        for i in range(4):
            x=72+M.sin(p*0.5+i*1.6)*30; y=72+M.cos(p*0.7+i*2.0)*28; r=26+8*M.sin(p*0.9+i)
            o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>'%(x,y,r,_rgb(h0+i*0.05+ph*0.01,.7,1))
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
            o+='<rect x="%.0f" y="%d" width="18" height="7" rx="3" fill="%s"/>'%(x,y,_rgb(h0+i*0.012,sat,0.9-i*0.03))
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
    if m=="loading":                               # a horizontal progress bar filling (not a round spinner)
        o='<rect x="14" y="60" width="116" height="24" rx="12" fill="#22262d"/>'
        prog=((int(ph*spd))%14)/13.0
        o+='<rect x="17" y="63" width="%d" height="18" rx="9" fill="%s"/>'%(max(4,int(110*prog)),_rgb(h0,.6,1))
        o+='<rect x="17" y="63" width="%d" height="7" rx="4" fill="#ffffff" opacity="0.25"/>'%max(4,int(110*prog))  # gloss
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
    if m=="wipe":                                  # one colour progressively filling the strip from the left
        prog=M.sin(p*0.5)*0.5+0.5; w=int(120*prog)
        o='<rect x="12" y="44" width="120" height="56" rx="10" fill="#20242b"/>'
        o+='<rect x="12" y="44" width="%d" height="56" rx="10" fill="%s"/>'%(max(2,w),_rgb(h0,.65,1))
        if 3<w<117: o+='<rect x="%d" y="44" width="5" height="56" fill="#ffffff" opacity="0.5"/>'%(12+w-3)  # leading edge
        return o
    if m=="sweep":                                 # a bright searchlight bar sweeping across a dim panel
        x=72+M.sin(p*0.6)*54; d=1 if M.cos(p*0.6)>0 else -1; o='<rect x="8" y="40" width="128" height="64" rx="10" fill="#20242b"/>'
        for k in range(5,0,-1): o+='<rect x="%.0f" y="40" width="10" height="64" rx="5" fill="%s" opacity="%.2f"/>'%(x-5-d*k*12,_rgb(h0,.6,1),max(0.06,0.5-k*0.09))
        o+='<rect x="%.0f" y="40" width="14" height="64" rx="6" fill="%s"/>'%(x-7,_rgb(h0,.7,1))
        return o
    if m=="scan":                                  # KITT/Cylon: a bright bar sweeping with a fading trail
        pos=72+M.sin(p*0.9)*52; d=1 if M.cos(p*0.9)>0 else -1; o=""
        for k in range(7,0,-1):
            xx=pos-d*k*11
            if 8<xx<136: o+='<rect x="%.0f" y="34" width="10" height="76" rx="5" fill="%s"/>'%(xx-5,_rgb(h0,.85,max(0.12,1-k*0.15)))
        o+='<rect x="%.0f" y="34" width="10" height="76" rx="5" fill="%s"/>'%(pos-5,_rgb(h0,.8,1))
        return o
    if m=="running":                               # running lights: glowing streaks flowing along a rail
        o='<line x1="10" y1="72" x2="134" y2="72" stroke="#23272e" stroke-width="16" stroke-linecap="round"/>'
        for j in range(4):
            x=(ph*10*spd+j*40)%176-16
            o+='<ellipse cx="%.0f" cy="72" rx="26" ry="7" fill="%s" opacity="0.28"/>'%(x-14,_rgb(h0,.5,1))    # motion blur
            o+='<ellipse cx="%.0f" cy="72" rx="15" ry="9" fill="%s"/>'%(x,_rgb(h0+j*0.05,.6,1))                # bright head
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
    if m=="tetris":                                # one piece falling SLOWLY onto a settled stack
        cell=15; o=""
        stack=[(0,9),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9),(2,8),(3,8),(5,8),(6,8),(3,7)]
        for cx,cy in stack: o+='<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" stroke="#151515" stroke-width="1"/>'%(6+cx*cell,14+cy*cell,cell,cell,_rgb((cx*0.12)%1.0,.55,.85))
        fy=int((ph/14.0)*7); col=_rgb(h0,.8,1)     # O-piece descends across the whole loop (2 frames/row = slow)
        for dx,dy in [(0,0),(1,0),(0,1),(1,1)]:
            o+='<rect x="%d" y="%d" width="%d" height="%d" rx="2" fill="%s" stroke="#151515" stroke-width="1"/>'%(6+(4+dx)*cell,14+(fy+dy)*cell,cell,cell,col)
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
    if m=="sunrise":                               # a sun climbing over the horizon, sky warming + rays
        prog=0.5+0.5*M.sin(p*0.35); sy=118-prog*46
        o='<rect x="0" y="0" width="144" height="144" fill="#191233"/>'                       # night sky
        o+='<rect x="0" y="66" width="144" height="52" fill="%s" opacity="%.2f"/>'%(_rgb(0.06,.7,1),0.25+0.55*prog)  # dawn glow
        for k in range(12):
            a=k/12.0*2*M.pi
            o+='<line x1="72" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="3" stroke-linecap="round" opacity="%.2f"/>'%(sy,72+M.cos(a)*40,sy+M.sin(a)*40,_rgb(0.13,.8,1),0.25+0.55*prog)
        o+='<circle cx="72" cy="%.0f" r="24" fill="%s"/>'%(sy,_rgb(0.11,.9,1))                 # the sun
        o+='<rect x="0" y="118" width="144" height="26" fill="#0d2a1a"/>'                      # ground
        return o
    if m=="twinkle":                                # stars/fireflies: dots that flash + a sparkle cross, then fade
        o=""
        pts=[(28,34),(70,26),(112,40),(46,66),(96,72),(24,104),(120,100),(66,112),(90,46)]
        for i,(x,yv) in enumerate(pts):
            tw=(int(ph*3*spd)+i*5+seed)%9           # each star has its own flash cycle
            if tw<3:                                # lit for 3 frames, brightest on the first
                b=1.0-tw*0.28; col=_rgb(h0+i*0.08,0.45,1); L=6+b*6
                o+='<circle cx="%d" cy="%d" r="%.1f" fill="%s"/>'%(x,yv,3+b*2,col)
                o+='<path d="M%d %.1f L%d %.1f M%.1f %d L%.1f %d" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>'%(x,yv-L,x,yv+L,x-L,yv,x+L,yv,col,1+b)
            else:
                o+='<circle cx="%d" cy="%d" r="1.6" fill="#39414e"/>'%(x,yv)   # resting star
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
    if m=="blink":                                  # an eyelid blink: eye + lashes, closes briefly
        cyc=int(ph)%6; o=[0.10,0.55,1.0,1.0,1.0,1.0][cyc]   # near-closed, half, then open 4 frames
        H=30*o+3; top=72-H; bot=72+H; iris=_rgb(0.09,0.6,0.62)
        s='<path d="M26 72 Q72 %.0f 118 72 Q72 %.0f 26 72 Z" fill="#f2ece0"/>'%(top,bot)
        if o>0.35:                                  # iris/pupil visible only while the eye is open
            s+='<ellipse cx="72" cy="72" rx="18" ry="%.0f" fill="%s"/>'%(min(18,H-2),iris)
            s+='<ellipse cx="72" cy="72" rx="8" ry="%.0f" fill="#17130d"/>'%min(8,H-4)
            s+='<circle cx="66" cy="66" r="3" fill="#ffffff"/>'
        s+='<path d="M26 72 Q72 %.0f 118 72" fill="none" stroke="#3a2f24" stroke-width="4" stroke-linecap="round"/>'%top
        for lx,ly in ((44,0.75),(72,1.0),(100,0.75)):
            lt=72-H*ly; s+='<line x1="%d" y1="%.0f" x2="%d" y2="%.0f" stroke="#3a2f24" stroke-width="3" stroke-linecap="round"/>'%(lx,lt,lx,lt-12)
        return s
    if m=="birds":                                  # a flock of birds flying across, wings flapping
        o=""
        for k in range(4):
            x=(ph*10*spd+k*44)%180-18; y=42+(k%2)*34+M.sin(ph*0.8+k)*6
            flap=6+abs(M.sin(ph*1.4+k*1.3))*12; col=_rgb(h0,sat,0.85)
            o+='<path d="M%.0f %.0f Q%.0f %.0f %.0f %.0f Q%.0f %.0f %.0f %.0f" fill="none" stroke="%s" stroke-width="5" stroke-linecap="round"/>'%(x-15,y,x-7,y-flap,x,y,x+7,y-flap,x+15,y,col)
        return o
    if m=="dna":                                    # a rotating double helix + rungs
        o=""
        for i in range(15):
            t=i/14.0; yy=14+t*116; a=t*6.283*1.5+p*0.3
            x1=72+M.sin(a)*36; x2=72-M.sin(a)*36
            o+='<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="#5a6472" stroke-width="3"/>'%(x1,yy,x2,yy)
            o+='<circle cx="%.0f" cy="%.0f" r="6" fill="%s"/><circle cx="%.0f" cy="%.0f" r="6" fill="%s"/>'%(x1,yy,_rgb(h0,sat,0.9),x2,yy,_rgb(h0+0.10,0.5,0.85))
        return o
    if m=="eye":                                    # an open eye whose pupil looks around
        look=M.sin(p*0.7)*15; iris=_rgb(0.09,0.6,0.62)
        return ('<path d="M18 72 Q72 32 126 72 Q72 112 18 72 Z" fill="#f2ece0"/>'
            '<path d="M18 72 Q72 32 126 72 Q72 112 18 72 Z" fill="none" stroke="#3a2f24" stroke-width="4"/>'
            '<circle cx="%.0f" cy="72" r="21" fill="%s"/><circle cx="%.0f" cy="72" r="9" fill="#17130d"/>'
            '<circle cx="%.0f" cy="66" r="3" fill="#ffffff"/>'%(72+look,iris,72+look,72+look-4))
    if m=="spookeyes":                              # Halloween Eyes: a pair of glowing eyes blinking in the dark
        cyc=int(ph)%5; op=0.0 if cyc==0 else (0.4 if cyc==1 else 1.0)
        if op<=0: return ''                         # closed = darkness
        o=""; ry=9*op+1
        for cx,hue in ((50,0.13),(94,0.30)):        # one amber eye, one sickly-green — spooky pair
            o+='<ellipse cx="%d" cy="72" rx="16" ry="%.0f" fill="%s"/>'%(cx,ry,_rgb(hue,0.9,0.9))
            o+='<ellipse cx="%d" cy="72" rx="3" ry="%.0f" fill="#0c0a06"/>'%(cx,max(1,ry*0.85))   # cat-slit pupil
        return o
    if m=="tartan":                                 # Scottish plaid: crossed horizontal + vertical bands
        o='<rect x="14" y="14" width="116" height="116" rx="8" fill="#241109"/>'
        off=int(ph*2*spd)%24
        hb=("#7a1f1f","#1f5030"); vb=("#c9a24a","#2f5f7a")
        for i,y in enumerate(range(14-off,132,24)):
            if 6<=y<=128: o+='<rect x="14" y="%d" width="116" height="9" fill="%s"/>'%(y,hb[i%2])
        for i,x in enumerate(range(14,132,24)):
            o+='<rect x="%d" y="14" width="9" height="116" fill="%s"/>'%(x,vb[i%2])
        return o
    if m=="randcolor":                              # Random Colors: the WHOLE strip is ONE colour that changes
        hh=((int(ph*spd)*137+seed*53)%360)/360.0    # a new pseudo-random hue each step
        return '<rect x="20" y="20" width="104" height="104" rx="16" fill="%s"/>'%_rgb(hh,0.55,0.85)
    if m=="fractal":                                # Julia: a morphing fractal bulb
        o=""; N=52
        for i in range(N):
            t=i/N*6.283; rr=22+18*M.cos(3*t+p*0.3)
            x=72+M.cos(t)*rr; y=72+M.sin(t)*rr
            o+='<circle cx="%.0f" cy="%.0f" r="2.6" fill="%s"/>'%(x,y,_rgb(0.66+0.05*M.sin(t*3),0.5,0.85))
        return o
    if m=="sunburst":                               # Sun Radiation / Colored Bursts: a sun with rotating rays
        a0=p*0.3; o='<circle cx="72" cy="72" r="18" fill="%s"/>'%_rgb(0.11,0.65,0.9)
        for k in range(12):
            a=a0+k/12.0*6.283; r2=44+7*M.sin(p+k)
            o+='<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="5" stroke-linecap="round"/>'%(72+M.cos(a)*24,72+M.sin(a)*24,72+M.cos(a)*r2,72+M.sin(a)*r2,_rgb(0.09,0.7,0.85))
        return o
    if m=="gol":                                    # Game Of Life: a grid of cells toggling
        o=""; g=6; cell=18; ox=(144-g*cell)//2
        for r in range(g):
            for c in range(g):
                if ((r*7+c*13+int(ph*2*spd)*5+seed)%9)<4:
                    o+='<rect x="%d" y="%d" width="14" height="14" rx="2" fill="%s"/>'%(ox+c*cell,ox+r*cell,_rgb(0.33,0.5,0.85))
        return o
    if m=="notes":                                  # Rocktaves: musical notes drifting by
        o='<line x1="18" y1="104" x2="126" y2="104" stroke="#5a6472" stroke-width="2"/>'
        for k in range(3):
            x=(ph*10*spd+k*46)%176-16; y=54+((k+int(ph))%3)*16
            col=_rgb(0.7-k*0.12,0.5,0.85)
            o+='<ellipse cx="%.0f" cy="%.0f" rx="9" ry="7" fill="%s" transform="rotate(-20 %.0f %.0f)"/>'%(x,y,col,x,y)
            o+='<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="3"/>'%(x+8,y-2,x+8,y-32,col)
        return o
    if m=="swirl":                                  # Drift / Swirl / Vortex: a spiral vortex winding out
        o=""; N=42
        for i in range(N):
            t=i/N*12.566; rr=6+i*1.35; a=t+p*0.3
            o+='<circle cx="%.0f" cy="%.0f" r="3" fill="%s"/>'%(72+M.cos(a)*rr,72+M.sin(a)*rr,_rgb(0.55+i*0.004,0.5,0.85))
        return o
    if m=="bubbles":                                # Soap: floating bubbles with a highlight
        o=""
        for k in range(5):
            x=72+M.sin(p*0.4+k*1.3)*36; y=72+M.cos(p*0.5+k*1.9)*34; r=15+6*M.sin(p*0.7+k)
            o+='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="none" stroke="%s" stroke-width="3"/>'%(x,y,r,_rgb(0.5+0.08*k,0.4,0.9))
            o+='<circle cx="%.0f" cy="%.0f" r="3" fill="#ffffff"/>'%(x-r*0.4,y-r*0.4)
        return o
    if m=="image":                                  # Image: a picture frame with a little landscape
        return ('<rect x="26" y="34" width="92" height="76" rx="6" fill="none" stroke="%s" stroke-width="5"/>'
            '<circle cx="48" cy="56" r="8" fill="%s"/>'
            '<path d="M30 104 L60 74 L80 94 L98 78 L114 104 Z" fill="%s"/>'%(_rgb(0.58,0.4,0.8),_rgb(0.12,0.7,0.9),_rgb(0.33,0.45,0.7)))
    if m=="geo":                                    # Frizzles: rotating nested geometric polygons
        o=""
        for k in range(3):
            a=p*0.3+k*2.09; rr=30-k*7+8*M.sin(p*0.5+k); pts=[]
            for j in range(5):
                t=a+j/5.0*6.283; pts.append("%.0f,%.0f"%(72+M.cos(t)*rr,72+M.sin(t)*rr))
            o+='<polygon points="%s" fill="none" stroke="%s" stroke-width="3"/>'%(" ".join(pts),_rgb(0.6-k*0.06,0.5,0.85))
        return o
    if m=="geq":                                    # GEQ / Freq*: an audio equalizer, bars bouncing
        o=""
        for i in range(8):
            hh=18+abs(M.sin(p*0.5+i*0.7))*92
            o+='<rect x="%d" y="%.0f" width="13" height="%.0f" rx="2" fill="%s"/>'%(12+i*16,124-hh,hh,_rgb(0.55-i*0.03,sat,0.85))
        return o
    if m=="spray":                                  # PS Spray: particles sprayed from a nozzle
        o='<rect x="12" y="62" width="22" height="18" rx="3" fill="#8b93a1"/>'
        for k in range(10):
            d=(k*13+int(ph*8*spd))%116; x=34+d; y=72+M.sin(p*0.6+k)*(6+d*0.2)
            o+='<circle cx="%.0f" cy="%.0f" r="%.1f" fill="%s"/>'%(x,y,max(2,5-d*0.03),_rgb(h0,sat,0.85))
        return o
    if m=="spring":                                 # PS Springy: a coil spring with a bouncing bob
        cy=48+abs(M.sin(p*0.9))*40; o=""
        for i in range(6):
            y1=18+i*(cy-18)/6.0; y2=18+(i+1)*(cy-18)/6.0
            o+='<line x1="%d" y1="%.0f" x2="%d" y2="%.0f" stroke="%s" stroke-width="4"/>'%(58 if i%2 else 86,y1,86 if i%2 else 58,y2,_rgb(h0,0.4,0.8))
        o+='<circle cx="72" cy="%.0f" r="16" fill="%s"/>'%(cy+16,_rgb(h0,sat,0.85))
        return o
    if m=="plasmaball":                             # Plasma Ball: a globe with electric tendrils
        o='<circle cx="72" cy="72" r="46" fill="#130a20"/><circle cx="72" cy="72" r="46" fill="none" stroke="%s" stroke-width="2"/>'%_rgb(0.75,0.4,0.7)
        for k in range(5):
            a=p*0.4+k*1.257; mx=72+M.cos(a)*24+M.sin(p+k)*8; my=72+M.sin(a)*24
            o+='<path d="M72 72 L%.0f %.0f L%.0f %.0f" fill="none" stroke="%s" stroke-width="2.5"/>'%(mx,my,72+M.cos(a)*44,72+M.sin(a)*44,_rgb(0.74,0.5,0.95))
        o+='<circle cx="72" cy="72" r="9" fill="%s"/>'%_rgb(0.78,0.55,0.95)
        return o
    if m=="pattern":                                # Solid Pattern: on/off stripes scrolling
        o=""; off=int(ph*3*spd)%36
        for x in range(-off,144,36):
            o+='<rect x="%d" y="30" width="18" height="84" rx="4" fill="%s"/>'%(x,_rgb(h0,sat,0.85))
        return o
    if m=="strobe":                                # a strobe FLASH: bright burst with radiating rays, dark between
        if ph%2==0:
            o='<circle cx="72" cy="72" r="30" fill="%s"/>'%_rgb(h0,0.28,1)
            for k in range(8):
                a=k/8.0*2*M.pi
                o+='<line x1="72" y1="72" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="7" stroke-linecap="round"/>'%(72+M.cos(a)*58,72+M.sin(a)*58,_rgb(h0,0.35,1))
            o+='<circle cx="72" cy="72" r="15" fill="#ffffff"/>'
            return o
        return '<circle cx="72" cy="72" r="7" fill="#262b32"/>'                                    # dark gap between flashes
    if m=="chase":                                 # a bright cluster chasing along a track, fading trail
        o='<line x1="14" y1="72" x2="130" y2="72" stroke="#2a2e35" stroke-width="2"/>'
        pos=(ph*spd)%9
        for i in range(9):
            d=(i-pos)%9; br=max(0.12,1-d*0.30)
            o+='<circle cx="%d" cy="72" r="%.1f" fill="%s"/>'%(16+i*14,5+br*4,_rgb(h0,.7,br))
        return o
    if m=="rainbow":
        o=""
        for k in range(6): o+='<path d="M18 128 A%d %d 0 0 1 126 128" fill="none" stroke="%s" stroke-width="9"/>'%(54-k*8,54-k*8,_rgb((k/6.0+ph*0.03*spd)%1.0,.9,1))
        return o
    if m=="colorloop":                             # rotating ring of the whole hue wheel
        o=""
        for k in range(12):
            a=(k/12.0)*2*M.pi+ph*0.05*spd
            o+='<circle cx="%.0f" cy="%.0f" r="10" fill="%s"/>'%(72+42*M.cos(a),72+42*M.sin(a),_rgb(h0+k/12.0,.85,1))
        return o
    if m=="lissajous":                             # a real Lissajous curve, morphing
        o=""; N=54; dphi=p*0.25
        for i in range(N):
            t=i/N*2*M.pi; x=72+54*M.sin(3*t+dphi); y=72+50*M.sin(2*t)
            o+='<circle cx="%.0f" cy="%.0f" r="3.4" fill="%s"/>'%(x,y,_rgb(h0+i/N*0.14,sat,0.9))
        return o
    if m=="dissolve":                              # pixels fill in random order, then dissolve away
        o=""; cols,rows=8,7; tot=cols*rows
        t=((int(ph*spd*1.2))%14)/14.0
        frac=(t/0.5) if t<0.5 else (1-(t-0.5)/0.5)  # 0→1→0 fill then clear
        n=int(tot*frac)
        for i in range(tot):
            cx,cy=i%cols,i//cols; on=((i*53+7)%tot)<n   # pseudo-random fill order
            col=_rgb(h0+(i%5)*0.03,.55,.95) if on else "#23272e"
            o+='<rect x="%d" y="%d" width="15" height="15" rx="2" fill="%s"/>'%(8+cx*16,14+cy*16,col)
        return o
    if m=="meteor":                                # a diagonal falling streak (top-left → bottom-right)
        t=((ph*spd)%14)/14.0; hx=8+t*132; hy=4+t*122; o=""
        for k in range(12):
            tx=hx-k*9; ty=hy-k*8.5
            if tx>-6 and ty>-6: o+='<circle cx="%.0f" cy="%.0f" r="%.1f" fill="%s" opacity="%.2f"/>'%(tx,ty,max(1,8-k*0.55),_rgb(h0,.55,1),max(0.05,1-k*0.1))
        o+='<circle cx="%.0f" cy="%.0f" r="8" fill="#ffffff"/>'%(hx,hy)
        return o
    if m=="triwipe":                               # THREE colours wiping in one after another
        prog=((int(ph*spd*1.0))%14)/13.0; seg=120/3.0
        o='<rect x="12" y="44" width="120" height="56" rx="10" fill="#20242b"/>'
        for b in range(3):
            local=max(0.0,min(1.0,prog*3-b)); w=int(seg*local)
            if w>0: o+='<rect x="%d" y="44" width="%d" height="56" fill="%s"/>'%(int(12+b*seg),w,_rgb(h0+b*0.33,.65,1))
        return o
    if m=="sweeprandom":                           # a bar that jumps to a RANDOM position + hue each step
        step=int(ph*spd); rx=8+((step*67+seed*13)%101)/100.0*110; rh=(h0+((step*37+seed)%360)/360.0)%1.0
        o='<rect x="8" y="40" width="128" height="64" rx="10" fill="#20242b"/>'
        o+='<rect x="%.0f" y="40" width="16" height="64" rx="6" fill="%s"/>'%(rx,_rgb(rh,.7,1))
        return o
    if m=="copyseg":                               # a small source segment duplicated across the strip
        pat=[_rgb(h0,.7,1),_rgb(h0+0.12,.7,1),_rgb(h0+0.24,.6,1)]; shift=int(ph*spd)%3; seg_w=34; o=""
        for c in range(4):
            for i in range(3):
                o+='<rect x="%d" y="50" width="9" height="44" rx="2" fill="%s"/>'%(9+c*seg_w+i*10,pat[(i+shift)%3])
        o+='<rect x="6" y="46" width="34" height="52" rx="3" fill="none" stroke="#ffffff66" stroke-width="2" stroke-dasharray="4 3"/>'  # the source block
        return o
    if m=="lake":                                  # calm horizontal water shimmer (distinct from ripple rings)
        o=""
        for lay in range(4):
            yy=44+lay*20
            pts=" ".join("%d %.1f"%(x,yy+M.sin((x-12)*0.06+p*0.5+lay*0.8)*5) for x in range(8,138,6))
            o+='<polyline points="%s" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round" opacity="0.85"/>'%(pts,_rgb(0.55+lay*0.02,.5,.68+lay*0.06))
        return o
    if m=="railway":                               # two rails, alternating lights running (level-crossing feel)
        o='<rect x="10" y="52" width="124" height="4" rx="2" fill="#3a3f47"/><rect x="10" y="88" width="124" height="4" rx="2" fill="#3a3f47"/>'
        for i in range(8):
            on=(i+int(ph*spd))%2==0
            o+='<circle cx="%d" cy="54" r="7" fill="%s"/>'%(18+i*15,_rgb(h0,.75,1) if on else "#2a2e35")
            o+='<circle cx="%d" cy="90" r="7" fill="%s"/>'%(18+i*15,_rgb(h0+0.5,.75,1) if not on else "#2a2e35")
        return o
    if m=="pattern3":                              # Solid Pattern Tri: 3 colours in scrolling stripes
        o=""; off=int(ph*3*spd)%54; cols=[_rgb(h0,sat,.9),_rgb(h0+0.33,sat,.9),_rgb(h0+0.66,sat,.9)]
        for x in range(-off,150,18):
            o+='<rect x="%d" y="30" width="18" height="84" fill="%s"/>'%(x,cols[((x+off)//18)%3])
        return o
    if m=="fireworks1d":                           # several small bursts along a 1D strip (vs one central starburst)
        o='<line x1="8" y1="112" x2="136" y2="112" stroke="#2a2e35" stroke-width="3"/>'
        for b in range(4):
            cx=26+b*32; t=((ph*spd+b*3)%8)/8.0
            if t<0.5:
                rad=t*44
                for i in range(8):
                    a=i/8.0*2*M.pi
                    o+='<circle cx="%.0f" cy="%.0f" r="%.1f" fill="%s" opacity="%.2f"/>'%(cx+M.cos(a)*rad,112+M.sin(a)*rad*0.55,max(1,4*(1-t*2)),_rgb(h0+b*0.15,.9,1),max(0.08,1-t*2))
        return o
    if m=="sinelon":                               # a dot sweeping sinusoidally, leaving a fading colour trail
        o=""
        for k in range(11):
            x=72+M.sin((p-k*0.18)*0.9)*58
            o+='<circle cx="%.0f" cy="72" r="%.1f" fill="%s" opacity="%.2f"/>'%(x,max(2,9-k*0.7),_rgb(h0,.7,1),max(0.06,1-k*0.11))
        return o
    if m=="sinelondual":                           # two dots in counter-phase, each on its own rail
        o=""
        for d,ph0 in ((0,0.0),(1,M.pi)):
            for k in range(9):
                x=72+M.sin((p-k*0.18)*0.9+ph0)*58
                o+='<circle cx="%.0f" cy="%d" r="%.1f" fill="%s" opacity="%.2f"/>'%(x,56 if d==0 else 88,max(2,8-k*0.7),_rgb(h0+d*0.4,.7,1),max(0.06,1-k*0.12))
        return o
    if m=="sinelonrainbow":                        # a sinelon whose trail cycles through the whole spectrum
        o=""
        for k in range(12):
            x=72+M.sin((p-k*0.16)*0.9)*58
            o+='<circle cx="%.0f" cy="72" r="%.1f" fill="%s" opacity="%.2f"/>'%(x,max(2,9-k*0.6),_rgb((ph*0.05+k*0.09)%1.0,.85,1),max(0.08,1-k*0.09))
        return o
    if m=="pacifica":                              # calm layered ocean swells (teal/blue filled bands)
        o='<rect x="0" y="30" width="144" height="90" fill="#08243a"/>'
        for lay in range(4):
            yy=50+lay*17; hue=[0.53,0.50,0.47,0.56][lay]
            top="".join("L%d %.1f "%(x,yy+M.sin((x-12)*0.05+p*0.4+lay*1.2)*7) for x in range(0,150,6))
            o+='<path d="M0 120 %sL144 120 Z" fill="%s" opacity="0.55"/>'%(top,_rgb(hue,.55,.62))
        return o
    if m=="washing":                               # washing machine: a drum tumbling clothes back and forth
        o='<circle cx="72" cy="72" r="48" fill="#16212c"/><circle cx="72" cy="72" r="48" fill="none" stroke="%s" stroke-width="5"/>'%_rgb(h0,.4,.7)
        a=M.sin(p*0.5)*2.2                          # oscillating tumble (not continuous like spin)
        for k in range(3):
            ang=a+k*2.094
            o+='<circle cx="%.0f" cy="%.0f" r="11" fill="%s"/>'%(72+M.cos(ang)*24,72+M.sin(ang)*24,_rgb(h0+k*0.2,.7,1))
        o+='<circle cx="72" cy="72" r="13" fill="none" stroke="#33404d" stroke-width="4"/>'
        return o
    if m=="noise":                                 # a smooth shifting colour field (overlapping soft blobs)
        o='<rect x="8" y="24" width="128" height="96" rx="12" fill="#0e1420"/>'
        for i in range(7):
            x=72+M.sin(p*0.4+i*1.3)*44; y=72+M.cos(p*0.5+i*0.9)*34
            o+='<circle cx="%.0f" cy="%.0f" r="30" fill="%s" opacity="0.4"/>'%(x,y,_rgb((h0+i*0.08+0.1*M.sin(p*0.3+i))%1.0,.5,.8))
        return o
    if m=="reserved":                              # RSVD: reserved/unused WLED slot — a neutral placeholder
        return ('<rect x="26" y="40" width="92" height="64" rx="10" fill="none" stroke="#4a505a" stroke-width="3" stroke-dasharray="6 5"/>'
                '<line x1="52" y1="72" x2="92" y2="72" stroke="#4a505a" stroke-width="5" stroke-linecap="round"/>')
    o=""                                           # wave (default) — travelling sine wave
    for lay,(amp,wdt,val,dph) in enumerate(((30,9,1.0,0.0),(22,6,0.62,1.7))):
        pts=" ".join("%d %.0f"%(x,72+amp*M.sin((x-12)*0.09+p*0.5+dph)) for x in range(12,134,5))
        o+='<polyline points="%s" fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round" stroke-linejoin="round"/>'%(pts,_rgb(h0+lay*0.12,sat,val),wdt)
    return o
def wrap(i): return '<svg xmlns="http://www.w3.org/2000/svg" width="144" height="144"><rect width="144" height="144" fill="#1a1a1a"/>%s</svg>'%i
