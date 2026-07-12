# WLED Effets

[Palettes](palettes.md) · **Effets** · [Contrôles](controls.md) · [Veilleuse](nightlight.md) · [Segment](segment.md) · [Boutons](buttons.md) · [Événements bouton](button-events.md) · [Préréglages](presets.md) · [Curseurs d'effet](fxdata.md) · [Champs Info](info.md) · [Libellés d'UI](ui.md) &nbsp;•&nbsp; [Référence en français](README.md)

<sub>Autres langues: [EN](../en/effects.md) · [DE](../de/effects.md) · [ES](../es/effects.md) · [IT](../it/effects.md) · [JA](../ja/effects.md) · [KO](../ko/effects.md) · [ZH](../zh/effects.md)</sub>

Les **effets** sont les motifs animés de WLED, choisis dans l'onglet **Effets**. Ils correspondent à `seg.fx` ; la liste vient de `/json/eff`. L'effet définit le *mouvement* ; la palette donne la *couleur*.

| Image | Nom WLED | Traduction | Description |
|---|---|---|---|
| <img src="../../images/effects/solid.gif" width="64"> | `Solid` | Fixe | Une couleur unie et stable. |
| <img src="../../images/effects/blink.gif" width="64"> | `Blink` | Clignotement | Un clignotement franc — comme un œil. |
| <img src="../../images/effects/breathe.gif" width="64"> | `Breathe` | Respiration | La luminosité enfle et retombe. |
| <img src="../../images/effects/wipe.gif" width="64"> | `Wipe` | Balayage | Un bras d'essuie-glace balaie. |
| <img src="../../images/effects/wipe-random.gif" width="64"> | `Wipe Random` | Balayage aléatoire | Un bras d'essuie-glace balaie. |
| <img src="../../images/effects/random-colors.gif" width="64"> | `Random Colors` | Couleurs aléatoires | Des blocs de couleur changent au hasard. |
| <img src="../../images/effects/sweep.gif" width="64"> | `Sweep` | Va-et-vient | Un faisceau balaie comme un essuie-glace. |
| <img src="../../images/effects/dynamic.gif" width="64"> | `Dynamic` | Dynamique | Des blocs de couleur changent au hasard. |
| <img src="../../images/effects/colorloop.gif" width="64"> | `Colorloop` | Boucle de couleurs | Tout le ruban parcourt les teintes. |
| <img src="../../images/effects/rainbow.gif" width="64"> | `Rainbow` | Arc-en-ciel | Un arc-en-ciel défile. |
| <img src="../../images/effects/scan.gif" width="64"> | `Scan` | Scanner | Un scanner balaie de gauche à droite. |
| <img src="../../images/effects/scan-dual.gif" width="64"> | `Scan Dual` | Scanner double | Un scanner balaie de gauche à droite. |
| <img src="../../images/effects/fade.gif" width="64"> | `Fade` | Fondu | Une couleur apparaît et disparaît. |
| <img src="../../images/effects/theater.gif" width="64"> | `Theater` | Chenillard | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/theater-rainbow.gif" width="64"> | `Theater Rainbow` | Chenillard arc-en-ciel | Un arc-en-ciel défile. |
| <img src="../../images/effects/running.gif" width="64"> | `Running` | Défilement | Un personnage court. |
| <img src="../../images/effects/saw.gif" width="64"> | `Saw` | Dents de scie | Une scie va-et-vient. |
| <img src="../../images/effects/twinkle.gif" width="64"> | `Twinkle` | Scintillement | Des étoiles scintillent. |
| <img src="../../images/effects/dissolve.gif" width="64"> | `Dissolve` | Dissolution | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/dissolve-rnd.gif" width="64"> | `Dissolve Rnd` | Dissolution aléatoire | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle` | Étincelles | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/sparkle-dark.gif" width="64"> | `Sparkle Dark` | Étincelles sombres | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/sparkle.gif" width="64"> | `Sparkle+` | Étincelles+ | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/strobe.gif" width="64"> | `Strobe` | Stroboscope | Un stroboscope franc. |
| <img src="../../images/effects/strobe-rainbow.gif" width="64"> | `Strobe Rainbow` | Strobo arc-en-ciel | Un arc-en-ciel défile. |
| <img src="../../images/effects/strobe-mega.gif" width="64"> | `Strobe Mega` | Strobo méga | Un stroboscope franc. |
| <img src="../../images/effects/blink-rainbow.gif" width="64"> | `Blink Rainbow` | Clignotement arc-en-ciel | Un arc-en-ciel défile. |
| <img src="../../images/effects/android.gif" width="64"> | `Android` | Android | Un scanner balaie de gauche à droite. |
| <img src="../../images/effects/chase.gif" width="64"> | `Chase` | Poursuite | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/chase-random.gif" width="64"> | `Chase Random` | Poursuite aléatoire | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/chase-rainbow.gif" width="64"> | `Chase Rainbow` | Poursuite arc-en-ciel | Un arc-en-ciel défile. |
| <img src="../../images/effects/chase-flash.gif" width="64"> | `Chase Flash` | Poursuite flash | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/chase-flash-rnd.gif" width="64"> | `Chase Flash Rnd` | Chase Flash Rnd | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/rainbow-runner.gif" width="64"> | `Rainbow Runner` | Coureur arc-en-ciel | Un arc-en-ciel défile. |
| <img src="../../images/effects/colorful.gif" width="64"> | `Colorful` | Coloré | Des bandes multicolores. |
| <img src="../../images/effects/traffic-light.gif" width="64"> | `Traffic Light` | Feu tricolore | Un feu tricolore change. |
| <img src="../../images/effects/sweep-random.gif" width="64"> | `Sweep Random` | Va-et-vient aléatoire | Un faisceau balaie comme un essuie-glace. |
| <img src="../../images/effects/chase-2.gif" width="64"> | `Chase 2` | Poursuite 2 | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/aurora.gif" width="64"> | `Aurora` | Aurore | Des bandes d'aurore boréale ondulent. |
| <img src="../../images/effects/stream.gif" width="64"> | `Stream` | Flux | Des particules s'écoulent. |
| <img src="../../images/effects/scanner.gif" width="64"> | `Scanner` | Scanner | Un scanner balaie de gauche à droite. |
| <img src="../../images/effects/lighthouse.gif" width="64"> | `Lighthouse` | Phare | Un faisceau tourne comme un phare. |
| <img src="../../images/effects/fireworks.gif" width="64"> | `Fireworks` | Feux d'artifice | Un feu d'artifice éclate. |
| <img src="../../images/effects/rain.gif" width="64"> | `Rain` | Pluie | La pluie tombe. |
| <img src="../../images/effects/tetrix.gif" width="64"> | `Tetrix` | Tetris | Des pièces de Tetris tombent et s'empilent. |
| <img src="../../images/effects/fire-flicker.gif" width="64"> | `Fire Flicker` | Feu vacillant | Des flammes vacillent et montent. |
| <img src="../../images/effects/gradient.gif" width="64"> | `Gradient` | Dégradé | Un dégradé de couleurs qui glisse. |
| <img src="../../images/effects/loading.gif" width="64"> | `Loading` | Chargement | Une barre de progression se remplit. |
| <img src="../../images/effects/rolling-balls.gif" width="64"> | `Rolling Balls` | Billes roulantes | Des balles rebondissent. |
| <img src="../../images/effects/fairy.gif" width="64"> | `Fairy` | Fée | Des guirlandes féeriques scintillent. |
| <img src="../../images/effects/two-dots.gif" width="64"> | `Two Dots` | Deux points | Deux points tournent l'un autour de l'autre. |
| <img src="../../images/effects/fairytwinkle.gif" width="64"> | `Fairytwinkle` | Scintillement féerique | Des guirlandes féeriques scintillent. |
| <img src="../../images/effects/running-dual.gif" width="64"> | `Running Dual` | Défilement double | Un personnage court. |
| <img src="../../images/effects/image.gif" width="64"> | `Image` | Image | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/chase-3.gif" width="64"> | `Chase 3` | Poursuite 3 | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/tri-wipe.gif" width="64"> | `Tri Wipe` | Balayage tricolore | Un bras d'essuie-glace balaie. |
| <img src="../../images/effects/tri-fade.gif" width="64"> | `Tri Fade` | Fondu tricolore | Une couleur apparaît et disparaît. |
| <img src="../../images/effects/lightning.gif" width="64"> | `Lightning` | Éclair | La foudre frappe. |
| <img src="../../images/effects/icu.gif" width="64"> | `ICU` | ICU | Un œil balaie du regard. |
| <img src="../../images/effects/multi-comet.gif" width="64"> | `Multi Comet` | Multi-comètes | Une comète file avec une traîne. |
| <img src="../../images/effects/scanner-dual.gif" width="64"> | `Scanner Dual` | Scanner double | Un scanner balaie de gauche à droite. |
| <img src="../../images/effects/stream-2.gif" width="64"> | `Stream 2` | Flux 2 | Des particules s'écoulent. |
| <img src="../../images/effects/oscillate.gif" width="64"> | `Oscillate` | Oscillation | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/pride-2015.gif" width="64"> | `Pride 2015` | Pride 2015 | Tout le ruban parcourt les teintes. |
| <img src="../../images/effects/juggle.gif" width="64"> | `Juggle` | Jonglage | Des balles rebondissent. |
| <img src="../../images/effects/palette.gif" width="64"> | `Palette` | Palette | Tout le ruban parcourt les teintes. |
| <img src="../../images/effects/fire-2012.gif" width="64"> | `Fire 2012` | Feu 2012 | Des flammes vacillent et montent. |
| <img src="../../images/effects/colorwaves.gif" width="64"> | `Colorwaves` | Vagues colorées | Des bandes multicolores. |
| <img src="../../images/effects/bpm.gif" width="64"> | `Bpm` | Bpm | Une pulsation bat à chaque temps. |
| <img src="../../images/effects/fill-noise.gif" width="64"> | `Fill Noise` | Bruit rempli | Une couleur unie et stable. |
| <img src="../../images/effects/noise-1.gif" width="64"> | `Noise 1` | Noise 1 | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/noise-2.gif" width="64"> | `Noise 2` | Noise 2 | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/noise-3.gif" width="64"> | `Noise 3` | Noise 3 | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/noise-4.gif" width="64"> | `Noise 4` | Noise 4 | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/colortwinkles.gif" width="64"> | `Colortwinkles` | Colortwinkles | Des étoiles scintillent. |
| <img src="../../images/effects/lake.gif" width="64"> | `Lake` | Lac | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/meteor.gif" width="64"> | `Meteor` | Météore | Une comète file avec une traîne. |
| <img src="../../images/effects/copy-segment.gif" width="64"> | `Copy Segment` | Copier segment | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/railway.gif" width="64"> | `Railway` | Voie ferrée | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/ripple.gif" width="64"> | `Ripple` | Ondulation | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/twinklefox.gif" width="64"> | `Twinklefox` | Scintillement renard | Des étoiles scintillent. |
| <img src="../../images/effects/twinklecat.gif" width="64"> | `Twinklecat` | Twinklecat | Des étoiles scintillent. |
| <img src="../../images/effects/halloween-eyes.gif" width="64"> | `Halloween Eyes` | Yeux d'Halloween | Un œil balaie du regard. |
| <img src="../../images/effects/solid-pattern.gif" width="64"> | `Solid Pattern` | Motif fixe | Une couleur unie et stable. |
| <img src="../../images/effects/solid-pattern-tri.gif" width="64"> | `Solid Pattern Tri` | Motif fixe tricolore | Une couleur unie et stable. |
| <img src="../../images/effects/spots.gif" width="64"> | `Spots` | Points | Des taches apparaissent et s'estompent. |
| <img src="../../images/effects/spots-fade.gif" width="64"> | `Spots Fade` | Points fondus | Des taches apparaissent et s'estompent. |
| <img src="../../images/effects/glitter.gif" width="64"> | `Glitter` | Paillettes | Des paillettes scintillent sur la couleur. |
| <img src="../../images/effects/candle.gif" width="64"> | `Candle` | Bougie | Une flamme de bougie vacille. |
| <img src="../../images/effects/fireworks-starburst.gif" width="64"> | `Fireworks Starburst` | Feu d'artifice étoilé | Un feu d'artifice éclate. |
| <img src="../../images/effects/fireworks-1d.gif" width="64"> | `Fireworks 1D` | Feux d'artifice 1D | Un feu d'artifice éclate. |
| <img src="../../images/effects/bouncing-balls.gif" width="64"> | `Bouncing Balls` | Billes rebondissantes | Des balles rebondissent. |
| <img src="../../images/effects/sinelon.gif" width="64"> | `Sinelon` | Sinelon | Une comète file avec une traîne. |
| <img src="../../images/effects/sinelon-dual.gif" width="64"> | `Sinelon Dual` | Sinelon Dual | Une comète file avec une traîne. |
| <img src="../../images/effects/sinelon-rainbow.gif" width="64"> | `Sinelon Rainbow` | Sinelon Rainbow | Une comète file avec une traîne. |
| <img src="../../images/effects/popcorn.gif" width="64"> | `Popcorn` | Popcorn | Des grains de pop-corn éclatent. |
| <img src="../../images/effects/drip.gif" width="64"> | `Drip` | Goutte | Des gouttes tombent une à une. |
| <img src="../../images/effects/plasma.gif" width="64"> | `Plasma` | Plasma | Des blobs de couleur se déforment. |
| <img src="../../images/effects/percent.gif" width="64"> | `Percent` | Pourcentage | Une barre se remplit à un niveau. |
| <img src="../../images/effects/ripple-rainbow.gif" width="64"> | `Ripple Rainbow` | Ondulation arc-en-ciel | Un arc-en-ciel défile. |
| <img src="../../images/effects/heartbeat.gif" width="64"> | `Heartbeat` | Battement de cœur | Un cœur bat. |
| <img src="../../images/effects/pacifica.gif" width="64"> | `Pacifica` | Pacifica | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/candle-multi.gif" width="64"> | `Candle Multi` | Bougies multiples | Une flamme de bougie vacille. |
| <img src="../../images/effects/solid-glitter.gif" width="64"> | `Solid Glitter` | Paillettes fixes | Des paillettes scintillent sur la couleur. |
| <img src="../../images/effects/sunrise.gif" width="64"> | `Sunrise` | Lever de soleil | Le soleil se lève. |
| <img src="../../images/effects/phased.gif" width="64"> | `Phased` | Déphasé | Des ondes sinusoïdales superposées glissent. |
| <img src="../../images/effects/twinkleup.gif" width="64"> | `Twinkleup` | Scintillement montant | Des étoiles scintillent. |
| <img src="../../images/effects/noise-pal.gif" width="64"> | `Noise Pal` | Bruit palette | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/sine.gif" width="64"> | `Sine` | Sinus | La luminosité enfle et retombe. |
| <img src="../../images/effects/phased-noise.gif" width="64"> | `Phased Noise` | Phased Noise | Des ondes sinusoïdales superposées glissent. |
| <img src="../../images/effects/flow.gif" width="64"> | `Flow` | Flux | Des particules s'écoulent. |
| <img src="../../images/effects/chunchun.gif" width="64"> | `Chunchun` | Chunchun | Une nuée d'oiseaux traverse. |
| <img src="../../images/effects/dancing-shadows.gif" width="64"> | `Dancing Shadows` | Ombres dansantes | Un personnage danse. |
| <img src="../../images/effects/washing-machine.gif" width="64"> | `Washing Machine` | Machine à laver | Une roue tourne. |
| <img src="../../images/effects/rotozoomer.gif" width="64"> | `Rotozoomer` | Rotozoomer | Une roue tourne. |
| <img src="../../images/effects/blends.gif" width="64"> | `Blends` | Mélanges | La luminosité enfle et retombe. |
| <img src="../../images/effects/tv-simulator.gif" width="64"> | `TV Simulator` | Simulateur TV | De la neige de télé scintille. |
| <img src="../../images/effects/dynamic-smooth.gif" width="64"> | `Dynamic Smooth` | Dynamique doux | Des blocs de couleur changent au hasard. |
| <img src="../../images/effects/spaceships.gif" width="64"> | `Spaceships` | Vaisseaux | Un vaisseau spatial glisse. |
| <img src="../../images/effects/crazy-bees.gif" width="64"> | `Crazy Bees` | Abeilles folles | Des abeilles bourdonnent en essaim. |
| <img src="../../images/effects/ghost-rider.gif" width="64"> | `Ghost Rider` | Cavalier fantôme | Un fantôme flotte. |
| <img src="../../images/effects/blobs.gif" width="64"> | `Blobs` | Bulles | Des blobs de couleur se déforment. |
| <img src="../../images/effects/scrolling-text.gif" width="64"> | `Scrolling Text` | Texte défilant | Des blocs défilent comme du texte. |
| <img src="../../images/effects/drift-rose.gif" width="64"> | `Drift Rose` | Rosace | Des étoiles s'enroulent en spirale. |
| <img src="../../images/effects/distortion-waves.gif" width="64"> | `Distortion Waves` | Vagues déformées | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/soap.gif" width="64"> | `Soap` | Savon | Des blobs de couleur se déforment. |
| <img src="../../images/effects/octopus.gif" width="64"> | `Octopus` | Pieuvre | Une pieuvre agite ses tentacules. |
| <img src="../../images/effects/waving-cell.gif" width="64"> | `Waving Cell` | Cellule ondulante | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/pixels.gif" width="64"> | `Pixels` | Pixels | Du code tombe, façon Matrix. |
| <img src="../../images/effects/pixelwave.gif" width="64"> | `Pixelwave` | Vague de pixels | Du code tombe, façon Matrix. |
| <img src="../../images/effects/juggles.gif" width="64"> | `Juggles` | Juggles | Des balles rebondissent. |
| <img src="../../images/effects/matripix.gif" width="64"> | `Matripix` | Matripix | Du code tombe, façon Matrix. |
| <img src="../../images/effects/gravimeter.gif" width="64"> | `Gravimeter` | Gravimeter | Des balles rebondissent. |
| <img src="../../images/effects/plasmoid.gif" width="64"> | `Plasmoid` | Plasmoid | Des blobs de couleur se déforment. |
| <img src="../../images/effects/puddles.gif" width="64"> | `Puddles` | Puddles | La pluie tombe. |
| <img src="../../images/effects/midnoise.gif" width="64"> | `Midnoise` | Midnoise | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/noisemeter.gif" width="64"> | `Noisemeter` | Noisemeter | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/freqwave.gif" width="64"> | `Freqwave` | Freqwave | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/freqmatrix.gif" width="64"> | `Freqmatrix` | Freqmatrix | Du code tombe, façon Matrix. |
| <img src="../../images/effects/geq.gif" width="64"> | `GEQ` | GEQ | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/waterfall.gif" width="64"> | `Waterfall` | Cascade | La pluie tombe. |
| <img src="../../images/effects/freqpixels.gif" width="64"> | `Freqpixels` | Freqpixels | Du code tombe, façon Matrix. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/noisefire.gif" width="64"> | `Noisefire` | Noisefire | Des flammes vacillent et montent. |
| <img src="../../images/effects/puddlepeak.gif" width="64"> | `Puddlepeak` | Puddlepeak | La pluie tombe. |
| <img src="../../images/effects/noisemove.gif" width="64"> | `Noisemove` | Noisemove | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/noise2d.gif" width="64"> | `Noise2D` | Noise2D | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/perlin-move.gif" width="64"> | `Perlin Move` | Perlin Move | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/ripple-peak.gif" width="64"> | `Ripple Peak` | Ripple Peak | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/firenoise.gif" width="64"> | `Firenoise` | Firenoise | Des flammes vacillent et montent. |
| <img src="../../images/effects/squared-swirl.gif" width="64"> | `Squared Swirl` | Squared Swirl | Des étoiles s'enroulent en spirale. |
| <img src="../../images/effects/pacman.gif" width="64"> | `PacMan` | Pac-Man | Pac-Man avance en croquant. |
| <img src="../../images/effects/dna.gif" width="64"> | `DNA` | DNA | Deux brins s'entrelacent en double hélice. |
| <img src="../../images/effects/matrix.gif" width="64"> | `Matrix` | Matrice | Du code tombe, façon Matrix. |
| <img src="../../images/effects/metaballs.gif" width="64"> | `Metaballs` | Metaballs | Des balles rebondissent. |
| <img src="../../images/effects/freqmap.gif" width="64"> | `Freqmap` | Freqmap | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/gravcenter.gif" width="64"> | `Gravcenter` | Gravcenter | Des balles rebondissent. |
| <img src="../../images/effects/gravcentric.gif" width="64"> | `Gravcentric` | Gravcentric | Des balles rebondissent. |
| <img src="../../images/effects/gravfreq.gif" width="64"> | `Gravfreq` | Gravfreq | Des balles rebondissent. |
| <img src="../../images/effects/dj-light.gif" width="64"> | `DJ Light` | Lumière DJ | Une platine tourne. |
| <img src="../../images/effects/funky-plank.gif" width="64"> | `Funky Plank` | Funky Plank | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/shimmer.gif" width="64"> | `Shimmer` | Miroitement | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/pulser.gif" width="64"> | `Pulser` | Pulser | La luminosité enfle et retombe. |
| <img src="../../images/effects/blurz.gif" width="64"> | `Blurz` | Blurz | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/drift.gif" width="64"> | `Drift` | Dérive | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/waverly.gif" width="64"> | `Waverly` | Waverly | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/sun-radiation.gif" width="64"> | `Sun Radiation` | Rayonnement solaire | Le soleil se lève. |
| <img src="../../images/effects/colored-bursts.gif" width="64"> | `Colored Bursts` | Éclats colorés | Une onde de choc s'étend. |
| <img src="../../images/effects/julia.gif" width="64"> | `Julia` | Julia | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/rsvd.gif" width="64"> | `RSVD` | RSVD | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/game-of-life.gif" width="64"> | `Game Of Life` | Jeu de la vie | Du code tombe, façon Matrix. |
| <img src="../../images/effects/tartan.gif" width="64"> | `Tartan` | Tartan | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/polar-lights.gif" width="64"> | `Polar Lights` | Aurores polaires | Des bandes d'aurore boréale ondulent. |
| <img src="../../images/effects/swirl.gif" width="64"> | `Swirl` | Tourbillon | Des étoiles s'enroulent en spirale. |
| <img src="../../images/effects/lissajous.gif" width="64"> | `Lissajous` | Lissajous | Une courbe de Lissajous se déforme. |
| <img src="../../images/effects/frizzles.gif" width="64"> | `Frizzles` | Frizzles | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/plasma-ball.gif" width="64"> | `Plasma Ball` | Boule de plasma | Des balles rebondissent. |
| <img src="../../images/effects/flow-stripe.gif" width="64"> | `Flow Stripe` | Bande fluide | Des particules s'écoulent. |
| <img src="../../images/effects/hiphotic.gif" width="64"> | `Hiphotic` | Hiphotic | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/sindots.gif" width="64"> | `Sindots` | Sindots | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/dna-spiral.gif" width="64"> | `DNA Spiral` | DNA Spiral | Deux brins s'entrelacent en double hélice. |
| <img src="../../images/effects/black-hole.gif" width="64"> | `Black Hole` | Trou noir | Des anneaux s'effondrent vers un cœur noir. |
| <img src="../../images/effects/wavesins.gif" width="64"> | `Wavesins` | Wavesins | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/rocktaves.gif" width="64"> | `Rocktaves` | Rocktaves | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/akemi.gif" width="64"> | `Akemi` | Akemi | Akemi, la mascotte de WLED, apparaît. |
| <img src="../../images/effects/ps-volcano.gif" width="64"> | `PS Volcano` | PS Volcano | Des flammes vacillent et montent. |
| <img src="../../images/effects/ps-fire.gif" width="64"> | `PS Fire` | PS Fire | Des flammes vacillent et montent. |
| <img src="../../images/effects/ps-fireworks.gif" width="64"> | `PS Fireworks` | PS Fireworks | Un feu d'artifice éclate. |
| <img src="../../images/effects/ps-vortex.gif" width="64"> | `PS Vortex` | PS Vortex | Des étoiles s'enroulent en spirale. |
| <img src="../../images/effects/ps-fuzzy-noise.gif" width="64"> | `PS Fuzzy Noise` | PS Fuzzy Noise | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/ps-ballpit.gif" width="64"> | `PS Ballpit` | PS Ballpit | Des balles rebondissent. |
| <img src="../../images/effects/ps-box.gif" width="64"> | `PS Box` | PS Box | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/ps-attractor.gif" width="64"> | `PS Attractor` | PS Attractor | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/ps-impact.gif" width="64"> | `PS Impact` | PS Impact | Une onde de choc s'étend. |
| <img src="../../images/effects/ps-waterfall.gif" width="64"> | `PS Waterfall` | PS Waterfall | La pluie tombe. |
| <img src="../../images/effects/ps-spray.gif" width="64"> | `PS Spray` | PS Spray | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/ps-geq-2d.gif" width="64"> | `PS GEQ 2D` | PS GEQ 2D | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/ps-geq-nova.gif" width="64"> | `PS GEQ Nova` | PS GEQ Nova | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/ps-ghost-rider.gif" width="64"> | `PS Ghost Rider` | PS Ghost Rider | Un fantôme flotte. |
| <img src="../../images/effects/ps-blobs.gif" width="64"> | `PS Blobs` | PS Blobs | Des blobs de couleur se déforment. |
| <img src="../../images/effects/ps-dripdrop.gif" width="64"> | `PS DripDrop` | PS DripDrop | Des gouttes tombent une à une. |
| <img src="../../images/effects/ps-pinball.gif" width="64"> | `PS Pinball` | PS Pinball | Des balles rebondissent. |
| <img src="../../images/effects/ps-dancing-shadows.gif" width="64"> | `PS Dancing Shadows` | PS Dancing Shadows | Un personnage danse. |
| <img src="../../images/effects/ps-fireworks-1d.gif" width="64"> | `PS Fireworks 1D` | PS Fireworks 1D | Un feu d'artifice éclate. |
| <img src="../../images/effects/ps-sparkler.gif" width="64"> | `PS Sparkler` | PS Sparkler | Des étincelles jaillissent au hasard. |
| <img src="../../images/effects/ps-hourglass.gif" width="64"> | `PS Hourglass` | PS Hourglass | Le sable tombe dans un sablier. |
| <img src="../../images/effects/ps-spray-1d.gif" width="64"> | `PS Spray 1D` | PS Spray 1D | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/ps-1d-balance.gif" width="64"> | `PS 1D Balance` | PS 1D Balance | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/ps-chase.gif" width="64"> | `PS Chase` | PS Chase | Un point lumineux balaie avec une traîne. |
| <img src="../../images/effects/ps-starburst.gif" width="64"> | `PS Starburst` | PS Starburst | Des étoiles scintillent. |
| <img src="../../images/effects/ps-geq-1d.gif" width="64"> | `PS GEQ 1D` | PS GEQ 1D | Des ondulations se propagent sur l'eau. |
| <img src="../../images/effects/ps-fire-1d.gif" width="64"> | `PS Fire 1D` | PS Fire 1D | Des flammes vacillent et montent. |
| <img src="../../images/effects/ps-sonic-stream.gif" width="64"> | `PS Sonic Stream` | PS Sonic Stream | Des particules s'écoulent. |
| <img src="../../images/effects/ps-sonic-boom.gif" width="64"> | `PS Sonic Boom` | PS Sonic Boom | Une onde de choc s'étend. |
| <img src="../../images/effects/ps-springy.gif" width="64"> | `PS Springy` | PS Springy | Une vague de couleur parcourt le ruban. |
| <img src="../../images/effects/ps-galaxy.gif" width="64"> | `PS Galaxy` | PS Galaxy | Des étoiles s'enroulent en spirale. |
| <img src="../../images/effects/color-clouds.gif" width="64"> | `Color Clouds` | Nuages colorés | Des blobs de couleur se déforment. |
| <img src="../../images/effects/slow-transition.gif" width="64"> | `Slow Transition` | Transition lente | Une vague de couleur parcourt le ruban. |
