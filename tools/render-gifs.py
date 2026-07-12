import json, re, os, subprocess, importlib.util
SP="/private/tmp/claude-501/-Users-benoitbesson-dev-music/b1b0bf2c-2a0b-4a74-83ae-5717d879ef61/scratchpad"
DST="/Users/benoitbesson/dev/music/wled-assets"
spec=importlib.util.spec_from_file_location("sa",SP+"/seeded_anim.py"); sa=importlib.util.module_from_spec(spec); spec.loader.exec_module(sa)
data=json.load(open(SP+"/wled_data.json")); eff=data["eff"]
ns={}; exec(open(SP+"/pages.py").read(), ns); fam=ns["fam"]
def slug(n): return re.sub(r'[^a-z0-9]+','-',n.lower()).strip('-')
os.makedirs(DST+"/images/effects",exist_ok=True)
# remove old family gifs (replaced by per-effect)
for f in os.listdir(DST+"/images/effects"):
    if f.endswith(".gif"): os.remove(DST+"/images/effects/"+f)
N=12
def render_frames(f,seed,fr):
    os.makedirs(fr,exist_ok=True)
    for ph in range(N):
        subprocess.run(["rsvg-convert","-w","72","-h","72","-o","%s/%03d.png"%(fr,ph),"-"],input=sa.wrap(sa.anim(ph,f,seed)).encode())
def make_gif(fr,out,fps=7):
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",fr+"/%03d.png",
        "-vf","split[a][b];[a]palettegen[p];[b][p]paletteuse","-loop","0",out])
# 1) per-effect gifs (seed = index -> unique)
seen=set()
for i,nm in enumerate(eff):
    sg=slug(nm)
    if sg in seen: continue     # duplicate names in the WLED list -> one file
    seen.add(sg)
    fr=SP+"/fx/"+sg; render_frames(fam(nm),i,fr)
    make_gif(fr,"%s/images/effects/%s.gif"%(DST,sg))
print("per-effect GIFs:",len(seen))
# 2) global animated grid of ALL effects (small)
COLS=15; CW=64; rows=(len(eff)+COLS-1)//COLS
gridfr=SP+"/grid"; os.makedirs(gridfr,exist_ok=True)
for ph in range(N):
    tiles=[]
    for i,nm in enumerate(eff):
        cx=(i%COLS)*CW; cy=(i//COLS)*CW
        tiles.append('<svg x="%d" y="%d" width="%d" height="%d" viewBox="0 0 144 144"><rect width="144" height="144" fill="#141414"/>%s</svg>'%(cx+2,cy+2,CW-4,CW-4,sa.anim(ph,fam(nm),i)))
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d"><rect width="%d" height="%d" fill="#0b0d11"/>%s</svg>'%(COLS*CW,rows*CW,COLS*CW,rows*CW,"".join(tiles))
    subprocess.run(["rsvg-convert","-o","%s/%03d.png"%(gridfr,ph),"-"],input=svg.encode())
make_gif(gridfr,DST+"/images/effects-grid.gif",fps=6)
print("grid GIF done")
