import json, re, os, subprocess, importlib.util
SP="/private/tmp/claude-501/-Users-benoitbesson-dev-music/b1b0bf2c-2a0b-4a74-83ae-5717d879ef61/scratchpad"
DST="/Users/benoitbesson/dev/music/wled-assets"
spec=importlib.util.spec_from_file_location("m",SP+"/motions.py"); mo=importlib.util.module_from_spec(spec); spec.loader.exec_module(mo)
eff=json.load(open(SP+"/wled_data.json"))["eff"]
def slug(n): return re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')
os.makedirs(DST+"/images/effects",exist_ok=True)
for f in os.listdir(DST+"/images/effects"):
    if f.endswith(".gif"): os.remove(DST+"/images/effects/"+f)
N=14
def frames(m,seed,fr,w=72):
    os.makedirs(fr,exist_ok=True)
    for ph in range(N):
        subprocess.run(["rsvg-convert","-w",str(w),"-h",str(w),"-o","%s/%03d.png"%(fr,ph),"-"],input=mo.wrap(mo.anim(ph,m,seed)).encode())
def gif(fr,out,fps=8):
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",fr+"/%03d.png",
        "-vf","split[a][b];[a]palettegen[p];[b][p]paletteuse","-loop","0",out])
seen=set()
for i,nm in enumerate(eff):
    sg=slug(nm)
    if sg in seen: continue
    seen.add(sg); fr=SP+"/fx2/"+sg; frames(mo.motion(nm),i,fr); gif(fr,"%s/images/effects/%s.gif"%(DST,sg))
print("per-effect GIFs:",len(seen))
# global animated grid (all together), smoother
COLS=15; CW=64; rows=(len(eff)+COLS-1)//COLS; gfr=SP+"/grid2"; os.makedirs(gfr,exist_ok=True)
NG=20
for ph in range(NG):
    tiles=[]
    for i,nm in enumerate(eff):
        cx=(i%COLS)*CW; cy=(i//COLS)*CW
        tiles.append('<svg x="%d" y="%d" width="%d" height="%d" viewBox="0 0 144 144"><rect width="144" height="144" fill="#141414"/>%s</svg>'%(cx+2,cy+2,CW-4,CW-4,mo.anim(ph,mo.motion(nm),i)))
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d"><rect width="%d" height="%d" fill="#0b0d11"/>%s</svg>'%(COLS*CW,rows*CW,COLS*CW,rows*CW,"".join(tiles))
    subprocess.run(["rsvg-convert","-o","%s/%03d.png"%(gfr,ph),"-"],input=svg.encode())
gif(gfr,DST+"/images/effects-grid.gif",fps=8)
print("grid GIF done")
