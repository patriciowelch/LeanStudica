/**
 * storage.js — localStorage wrapper + server sync (multi-usuario)
 */

const KEYS = {
  STATS:     'lm_stats',
  FAILED:    'lm_failed',
  POINTS:    'lm_points',
  RECORD:    'lm_record',
  COMODINES: 'lm_comodines',
  USER:      'lm_user',   // nick actual
};

const DEFAULT_STATS = {
  totalAnswered: 0,
  totalCorrect:  0,
  maxStreak:     0,
  sessions:      [],
  byTema:        {},
  byTipo:        {},
  byDificultad:  {},
};

// ── Usuario ─────────────────────────────────────────────────────────
export function loadUser()       { return localStorage.getItem(KEYS.USER) || ''; }
export function saveUser(nick)   { localStorage.setItem(KEYS.USER, nick); }
export function clearUser()      { localStorage.removeItem(KEYS.USER); }

// ── Stats ────────────────────────────────────────────────────────────
export function loadStats() {
  try {
    const raw = localStorage.getItem(KEYS.STATS);
    return raw ? { ...DEFAULT_STATS, ...JSON.parse(raw) } : { ...DEFAULT_STATS };
  } catch { return { ...DEFAULT_STATS }; }
}
export function saveStats(stats) { localStorage.setItem(KEYS.STATS, JSON.stringify(stats)); }

// ── Failed ───────────────────────────────────────────────────────────
export function loadFailed() {
  try { const raw = localStorage.getItem(KEYS.FAILED); return raw ? JSON.parse(raw) : {}; }
  catch { return {}; }
}
export function saveFailed(m) { localStorage.setItem(KEYS.FAILED, JSON.stringify(m)); }

export function addFailed(question, yourAnswer) {
  const failed = loadFailed();
  failed[question.id] = {
    question, yourAnswer,
    count: (failed[question.id]?.count || 0) + 1,
    lastFailed: Date.now(),
  };
  saveFailed(failed);
}
export function removeFailed(id) {
  const failed = loadFailed(); delete failed[id]; saveFailed(failed);
}

// ── Points ───────────────────────────────────────────────────────────
export function loadPoints() { return parseInt(localStorage.getItem(KEYS.POINTS) || '0', 10); }
export function savePoints(pts) { localStorage.setItem(KEYS.POINTS, String(pts)); }
export function loadRecord() { return parseInt(localStorage.getItem(KEYS.RECORD) || '0', 10); }
export function saveRecord(pts) {
  if (pts > loadRecord()) localStorage.setItem(KEYS.RECORD, String(pts));
}

// ── Comodines ────────────────────────────────────────────────────────
export function loadComodines() {
  try { const raw = localStorage.getItem(KEYS.COMODINES); return raw ? JSON.parse(raw) : {}; }
  catch { return {}; }
}
export function saveComodines(c) { localStorage.setItem(KEYS.COMODINES, JSON.stringify(c)); }

// ── updateStats ──────────────────────────────────────────────────────
export function updateStats(sessionData) {
  const stats = loadStats();
  const { answers, score } = sessionData;

  stats.totalAnswered += answers.length;
  stats.totalCorrect  += answers.filter(a => a.correct).length;
  if (sessionData.maxStreak > stats.maxStreak) stats.maxStreak = sessionData.maxStreak;

  stats.sessions.push({
    date: Date.now(), score,
    correct: answers.filter(a => a.correct).length,
    total: answers.length,
  });
  if (stats.sessions.length > 50) stats.sessions = stats.sessions.slice(-50);

  for (const a of answers) {
    const q = a.question;
    if (!stats.byTema[q.tema])        stats.byTema[q.tema]               = { correct: 0, total: 0 };
    stats.byTema[q.tema].total++;
    if (a.correct) stats.byTema[q.tema].correct++;

    if (!stats.byTipo[q.tipo])        stats.byTipo[q.tipo]               = { correct: 0, total: 0 };
    stats.byTipo[q.tipo].total++;
    if (a.correct) stats.byTipo[q.tipo].correct++;

    if (!stats.byDificultad[q.dificultad]) stats.byDificultad[q.dificultad] = { correct: 0, total: 0 };
    stats.byDificultad[q.dificultad].total++;
    if (a.correct) stats.byDificultad[q.dificultad].correct++;
  }

  saveStats(stats);
}

export function resetAll() {
  [KEYS.STATS, KEYS.FAILED, KEYS.POINTS, KEYS.RECORD, KEYS.COMODINES].forEach(k =>
    localStorage.removeItem(k)
  );
  saveToServer();
}

// ── Server sync (per-user) ───────────────────────────────────────────
export async function loadFromServer(nick) {
  if (!nick) return;
  try {
    const res = await fetch(`/api/state/${encodeURIComponent(nick)}`);
    if (!res.ok) return;
    const data = await res.json();
    for (const [key, value] of Object.entries(data)) {
      if (value != null) localStorage.setItem(key, value);
    }
  } catch { /* modo local / file:// */ }
}

export function saveToServer() {
  const nick = loadUser();
  if (!nick) return;
  const state = {};
  [KEYS.STATS, KEYS.FAILED, KEYS.POINTS, KEYS.RECORD, KEYS.COMODINES].forEach(k => {
    const val = localStorage.getItem(k);
    if (val !== null) state[k] = val;
  });
  fetch(`/api/state/${encodeURIComponent(nick)}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(state),
  }).catch(() => {});
}
