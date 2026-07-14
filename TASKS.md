# wled-assets — TASKS

## Revue des animations d'effets (motions)
- ✅ **Passe 1 (2026-07-13)** : 11 effets tombaient sur la vague générique (tous identiques). 9 routés
  vers un motion existant mieux adapté — Copy Segment→wipe, Distortion Waves/Waverly→ripple,
  Waving Cell/Perlin Move→plasma, Funky Plank/Blurz→geq, PS Box/PS 1D Balance→bounce.
  Oscillate + Wavesins restent en « wave » (justifié). Classifier synchronisé sur les 3 copies
  (motions.py, anim.js, plugin.py) + 9 GIF régénérés.
- ✅ **Passe 2 (2026-07-13)** : audit visuel des 81 motions → 4 refaits car trompeurs :
  `wave` (fallback, rendait des barres → vraie sinusoïde), `strobe` (4 points → flash plein on/off),
  `colorloop` (carré plein → anneau de teintes tournant), `text` (blocs → « WLED » défilant).
  Synchro 3 copies + 8 GIF régénérés.
- ⏳ **Passe 3 (affinage, optionnel)** : candidats repérés à l'audit —
  `bees` `glitter` `fade` `randcolor` `lissajous` `twinkle`.
  - ✅ `twinkle` (2026-07-13) : rendait des **nœuds papillon/sabliers** (path sablier), pas des étoiles.
    Refait en vraies étoiles qui scintillent (dots + croix d'étincelle 4 branches qui flashent/s'éteignent,
    points ternes au repos). Synchro 3 copies (motions.py, anim.js, plugin.py) + 6 GIF régénérés
    (Colortwinkles/Pixels/Twinkle/Twinklecat/Twinklefox/Twinkleup, seed canonique = index effet).
  - ✅ `fade` `bees` `glitter` (2026-07-13) : `fade` ne pulsait que la luminosité (≈ breathe) → vrai
    crossfade de couleur ; `bees` = cercles peu lisibles → abeilles rayées (corps + bande horizontale +
    aile qui bat, bourdonnement erratique) ; `glitter` trop épars → paillettes fines denses (cœur blanc +
    halo, fondu). 3 copies synchro + 7 GIF régénérés (fade/tri-fade/slow-transition, crazy-bees,
    glitter/solid-glitter/shimmer). Revue avant/après validée par Benoît.
  - ☐ `randcolor` `lissajous` : **corrects et distinctifs** au rendu — laissés (refonte = pur goût,
    rien à gagner). Rouvrir seulement si Benoît le demande explicitement.
- ⏳ **Passe 4 — revue à l'œil de Benoît (2026-07-14)** : 14 critiques traitées + 3 collisions séparées.
  - ✅ Redesignés (moins abstraits) : `breathe` (glow qui respire), `strobe` (éclat + rayons),
    `scan`/Android (scanner KITT + traîne), `chase` (poursuite sur rail), `sweep` (barre projecteur),
    `tetris` (pièce qui tombe lentement sur la pile), `loading` (barre de progression, plus ronde),
    `running` (lumières qui courent, plus de bonhomme), `wipe` (remplissage couleur), `comet` (tête + longue traîne).
  - ✅ Collisions séparées en motions dédiés : `dissolve` (≠ sparkle), `meteor` (≠ comet, diagonal),
    `triwipe` (3 couleurs, ≠ wipe monocolore), `copyseg` (segment dupliqué, ≠ wipe), `sweeprandom`
    (position+teinte aléatoires, ≠ sweep), `lake` (eau horizontale, ≠ ripple). Classifier maj (3 copies).
  - ✅ 3 copies synchro (motions.py ≡ plugin.py vérifié, anim.js porté+testé node) + 37 GIF régénérés.
    Revue avant/après envoyée à Benoît (artifact). En attente validation.
- ✅ **Passe 5 — 2e revue à l'œil de Benoît (2026-07-14)** : 14 points, 7 nouveaux motions + 4 reroutes wave.
  - Nouveaux motions : `railway` (2 rails alternés), `pattern3` (Solid Pattern Tri, 3 couleurs),
    `fireworks1d` (éclats 1D ≠ Starburst), `sinelon`/`sinelondual`/`sinelonrainbow` (≠ comet, dual distinct, rainbow),
    `pacifica` (houle océan ≠ ripple), `washing` (tambour ≠ spin/rotozoomer), `noise` (champ diffus ≠ GEQ),
    `reserved` (RSVD ×3 = placeholder neutre). Redesign `sunrise` (soleil littéral).
  - Reroutes vers la vraie sinusoïde `wave` : Sine, Distortion Waves, Pixelwave, Waverly.
  - 3 copies synchro (motions.py ≡ plugin.py vérifié, anim.js porté+testé) + 24 GIF régénérés. Revue envoyée (artifact).
- ☐ **Repasser les autres animations `pas terribles`** si Benoît en repère d'autres. Méthode : rejouer nom → symbole →
  mouvement, une par une, comme les passes précédentes — repérer les faibles et les refaire.
  - Source canonique : `tools/motions.py` (`motion()` classifier + `anim()` renderer).
  - 3 copies à resynchroniser après chaque changement : `tools/motions.py` (canonique),
    `tools/anim.js` (JS), et le portage `plugin.py` `_fx_*` dans le plugin Stream Deck (privé).
  - Régénérer les GIF (`images/effects/*.gif`) + vérifier le rendu sur fond sombre (deck + sélecteur PI).
  - Candidates faibles à shortlister d'abord : celles qui tombent sur une motion générique
    (sparkle/fallback) plutôt qu'un mouvement dédié.
- ☐ (option) Appliquer ensuite la même méthode nom→symbole aux **palettes** (statique, garder le dégradé),
  puis aux autres illustrations (homogénéité, sans contrainte d'animation ni de palette).
