# wled-assets — TASKS

## Revue des animations d'effets (motions)
- ✅ **Passe 1 (2026-07-13)** : 11 effets tombaient sur la vague générique (tous identiques). 9 routés
  vers un motion existant mieux adapté — Copy Segment→wipe, Distortion Waves/Waverly→ripple,
  Waving Cell/Perlin Move→plasma, Funky Plank/Blurz→geq, PS Box/PS 1D Balance→bounce.
  Oscillate + Wavesins restent en « wave » (justifié). Classifier synchronisé sur les 3 copies
  (motions.py, anim.js, plugin.py) + 9 GIF régénérés.
- ☐ **Passe 2 (subjectif, itératif)** : parcourir visuellement les buckets pour repérer les motions
  qui ne représentent pas bien un effet donné (ex. un effet mal rangé dans un bucket). Nécessite
  un œil sur chaque — shortlister avec Benoît les « pas terribles » restants, puis refaire.
- ☐ **Repasser les animations `pas terribles` restantes** (Benoît, 2026-07-13). Certaines des 217 motions
  ne représentent pas bien l'effet / ne sont pas jolies. Méthode : rejouer nom → symbole →
  mouvement, une par une, comme la passe initiale — repérer les faibles et les refaire.
  - Source canonique : `tools/motions.py` (`motion()` classifier + `anim()` renderer).
  - 3 copies à resynchroniser après chaque changement : `tools/motions.py` (canonique),
    `tools/anim.js` (JS), et le portage `plugin.py` `_fx_*` dans **openlamp/lumideck**.
  - Régénérer les GIF (`images/effects/*.gif`) + vérifier le rendu sur fond sombre (deck + sélecteur PI).
  - Candidates faibles à shortlister d'abord : celles qui tombent sur une motion générique
    (sparkle/fallback) plutôt qu'un mouvement dédié.
- ☐ (option) Appliquer ensuite la même méthode nom→symbole aux **palettes** (statique, garder le dégradé),
  puis aux autres illustrations (homogénéité, sans contrainte d'animation ni de palette).
