/*
 * wled-assets — drop-in localization overlay for the WLED web UI.
 *
 * Paste this in the browser console while on your WLED device's web UI, or load
 * it as a userscript / bookmarklet. It rewrites the effect and palette list
 * names (#fxlist / #pallist → .lstIname) with localized names from wled-assets,
 * adds a small effect preview thumbnail, and re-applies whenever WLED rebuilds
 * the lists (populateEffects / populatePalettes). Firmware untouched.
 *
 * Language: auto (browser) — override with  window.WA_LANG = 'fr'  before loading.
 * Assets are fetched from jsDelivr (the openlamp/wled-assets repo).
 */
(async function () {
  const LANG = (window.WA_LANG || navigator.language || 'en').slice(0, 2);
  const BASE = window.WA_BASE || 'https://cdn.jsdelivr.net/gh/openlamp/wled-assets@main';
  const slug = n => n.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  let effI18n = {}, palI18n = {};
  try {
    [effI18n, palI18n] = await Promise.all([
      fetch(BASE + '/i18n/effects.json').then(r => r.json()).then(d => d.entries),
      fetch(BASE + '/i18n/palettes.json').then(r => r.json()).then(d => d.entries),
    ]);
  } catch (e) { console.warn('[wled-assets] could not load assets', e); return; }

  const loc = (map, eng) => { const e = map[eng]; return (e && e[LANG] && e[LANG].name) || null; };

  function localize(listId, map, addThumb) {
    const list = document.getElementById(listId);
    if (!list) return;
    list.querySelectorAll('.lstIname').forEach(nameEl => {
      const eng = nameEl.dataset.waEng || nameEl.textContent.trim();
      nameEl.dataset.waEng = eng;                       // remember the English join key
      const l = loc(map, eng);
      if (l && nameEl.lastChild && nameEl.lastChild.nodeType === 3) nameEl.lastChild.textContent = l;
      else if (l && !nameEl.querySelector('img')) nameEl.textContent = l;
      if (addThumb && !nameEl.querySelector('.wa-thumb')) {
        const img = document.createElement('img');
        img.className = 'wa-thumb';
        img.src = BASE + '/images/effects/' + slug(eng) + '.gif';
        img.style.cssText = 'width:22px;height:22px;border-radius:4px;margin-right:8px;vertical-align:middle';
        img.onerror = () => img.remove();
        nameEl.prepend(img);
      }
    });
  }
  const apply = () => { localize('fxlist', effI18n, true); localize('pallist', palI18n, false); };
  apply();
  ['fxlist', 'pallist'].forEach(id => {
    const el = document.getElementById(id);
    if (el) new MutationObserver(apply).observe(el, { childList: true, subtree: true });
  });
  console.log('[wled-assets] overlay applied — language: ' + LANG);
})();
