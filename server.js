const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8080;

// Railway: montá un volume en /data y seteá DATA_DIR=/data como env var.
// Local: usa ./state/ (gitignoreado).
const DATA_DIR = process.env.DATA_DIR || path.join(__dirname, 'state');
const DATA_FILE = path.join(DATA_DIR, 'users_state.json');

app.use(express.json({ limit: '5mb' }));
app.use(express.static(__dirname));

function readAll() {
  try {
    if (fs.existsSync(DATA_FILE)) return JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
  } catch {}
  return {};
}

function writeAll(data) {
  if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });
  fs.writeFileSync(DATA_FILE, JSON.stringify(data), 'utf8');
}

// GET /api/state/:nick — estado de un usuario
app.get('/api/state/:nick', (req, res) => {
  const all = readAll();
  res.json(all[req.params.nick] || {});
});

// PUT /api/state/:nick — guarda estado de un usuario
app.put('/api/state/:nick', (req, res) => {
  try {
    const all = readAll();
    all[req.params.nick] = req.body;
    writeAll(all);
    res.json({ ok: true });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// GET /api/leaderboard — ranking de todos los usuarios
app.get('/api/leaderboard', (req, res) => {
  const all = readAll();
  const board = Object.entries(all).map(([nick, state]) => ({
    nick,
    points: parseInt(state['lm_points'] || '0', 10),
    record: parseInt(state['lm_record'] || '0', 10),
    totalAnswered: (() => {
      try { return JSON.parse(state['lm_stats'] || '{}').totalAnswered || 0; } catch { return 0; }
    })(),
    totalCorrect: (() => {
      try { return JSON.parse(state['lm_stats'] || '{}').totalCorrect || 0; } catch { return 0; }
    })(),
  }));
  board.sort((a, b) => b.record - a.record);
  res.json(board);
});

// SPA fallback
app.get('*', (req, res) => {
  if (!req.path.startsWith('/api')) res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => console.log(`Servidor en http://localhost:${PORT}  |  state: ${DATA_FILE}`));
