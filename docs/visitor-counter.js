// Separate SeqBrowser counter; counts are hosted and refreshed by Flag Counter on page loads.
(() => {
  if (document.getElementById('visitor-footer')) return;
  const footer = document.createElement('footer');
  footer.id = 'visitor-footer';
  footer.className = 'visitor-footer';
  footer.innerHTML = `<div class="visitor-card">
    <div><span class="visitor-eyebrow">Around the world</span><p>Visitors to SeqBrowser</p></div>
    <a href="https://info.flagcounter.com/ZeJc" target="_blank" rel="noopener" aria-label="View SeqBrowser visitor statistics on Flag Counter">
      <img src="https://s05.flagcounter.com/count2/ZeJc/bg_FAFAF8/txt_883CBA/border_FAFAF8/columns_8/maxflags_49/viewers_0/labels_0/pageviews_1/flags_0/percent_0/"
        alt="SeqBrowser visitor counts by country, with country flags and page views" decoding="async">
    </a>
    <small>Country totals · <a href="https://flagcounter.com/" target="_blank" rel="noopener">Flag Counter</a></small>
  </div>`;
  // Keep the counter outside the table body that search, sorting and expansion replace.
  const llm = document.querySelector('main > .llm');
  if (llm) llm.insertAdjacentElement('afterend', footer);
  else document.body.appendChild(footer);
})();
