# wled-assets — TASKS

## Revue des animations d'effets (motions)
- ☐ **Repasser les animations `pas terribles`** (Benoît, 2026-07-13). Certaines des 217 motions
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
