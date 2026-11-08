// Separate SeqBrowser counter; counts are hosted and refreshed by Flag Counter on page loads.
(() => {
  const dark = matchMedia('(prefers-color-scheme: dark)').matches;   // image background must equal the card colour (Flag Counter has no transparent mode)
  const pal = dark ? 'bg_1C1C1F/txt_B493F0/border_1C1C1F' : 'bg_FFFFFF/txt_883CBA/border_FFFFFF';
  if (document.getElementById('visitor-footer')) return;
  const footer = document.createElement('footer');
  footer.id = 'visitor-footer';
  footer.className = 'visitor-footer';
  footer.innerHTML = `<div class="visitor-card">
    <a href="https://info.flagcounter.com/ZeJc" target="_blank" rel="noopener" aria-label="View SeqBrowser visitor statistics on Flag Counter">
      <img src="https://s05.flagcounter.com/count2/ZeJc/${pal}/columns_4/maxflags_49/viewers_0/labels_0/pageviews_1/flags_0/percent_0/"
        alt="SeqBrowser visitor counts by country, with country flags and page views" decoding="async">
    </a>
  </div>`;
  // Keep the counter outside the table body that search, sorting and expansion replace.
  const llm = document.querySelector('main > .llm');
  if (llm) llm.insertAdjacentElement('afterend', footer);
  else document.body.appendChild(footer);
})();
