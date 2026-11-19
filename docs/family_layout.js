// Pack circles vertically without moving their publication-date coordinates.
function packFamilyLane(nodes, gap = 12) {
  const ordered = [...nodes].sort((a, b) => a.x - b.x || String(a.id).localeCompare(String(b.id)));
  const maxRadius = ordered.reduce((m, n) => Math.max(m, n.r), 0);
  let active = [];
  for (const n of ordered) {
    active = active.filter(p => n.x - p.x < n.r + maxRadius + gap);
    const intervals = [];
    for (const p of active) {
      const distance = p.r + n.r + gap, dx = n.x - p.x;
      if (dx >= distance) continue;
      const dy = Math.sqrt(Math.max(0, distance * distance - dx * dx));
      intervals.push([p.y - dy, p.y + dy]);
    }
    intervals.sort((a, b) => a[0] - b[0]);
    const merged = [];
    for (const interval of intervals) {
      const last = merged[merged.length - 1];
      if (last && interval[0] <= last[1]) last[1] = Math.max(last[1], interval[1]);
      else merged.push([...interval]);
    }
    const occupied = merged.find(([low, high]) => low <= 0 && high >= 0);
    n.y = occupied ? (Math.abs(occupied[0]) <= Math.abs(occupied[1]) ? occupied[0] - 0.01 : occupied[1] + 0.01) : 0;
    active.push(n);
  }
  return ordered;
}
if (typeof module !== 'undefined') module.exports = {packFamilyLane};
