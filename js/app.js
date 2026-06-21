/**
 * app.js — lógica principal / loop de juego
 */

import {
  loadStats, loadFailed, loadPoints, savePoints, loadRecord, saveRecord,
  addFailed, removeFailed, updateStats, resetAll, loadFromServer, saveToServer,
  loadUser, saveUser, clearUser,
} from './storage.js';
import { CONFIG, Timer, calcPuntos, shuffleArray, shuffleOptions, checkRelacionAnswer } from './game.js';
import { renderStats } from './stats.js';

// ──────────────────────────────────────────────
// STATE
// ──────────────────────────────────────────────
let allQuestions = [];
let temas = [];

let gameState = {
  questions: [], current: 0, score: 0, streak: 0, maxStreak: 0,
  answers: [], timer: null, mode: 'rapida', totalQ: 10,
  comodinesUsed: {}, defensaActive: false, answered: false,
};

// ──────────────────────────────────────────────
// INIT
// ──────────────────────────────────────────────
async function init() {
  try {
    const res = await fetch('data/questions.json');
    const data = await res.json();
    allQuestions = data.preguntas;
    temas = data.temas;
  } catch {
    alert('Error cargando questions.json. Asegurate de servir la app con un servidor HTTP.');
    return;
  }

  attachGlobalListeners();

  const nick = loadUser();
  if (nick) {
    await enterHome(nick);
  } else {
    showScreen('user');
    attachUserListeners();
  }
}

// ──────────────────────────────────────────────
// USER SCREEN
// ──────────────────────────────────────────────
function attachUserListeners() {
  const input = document.getElementById('nick-input');
  const btn   = document.getElementById('btn-nick-ok');

  const tryEnter = async () => {
    const nick = input.value.trim();
    if (!nick) { showToast('Ingresá un nick para continuar'); return; }
    saveUser(nick);
    await enterHome(nick);
  };

  btn.addEventListener('click', tryEnter);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') tryEnter(); });

  document.getElementById('btn-leaderboard-from-user')?.addEventListener('click', () => {
    showLeaderboard('user');
  });
}

async function enterHome(nick) {
  await loadFromServer(nick);
  buildTopicSelector();
  updateScoreBanner(nick);
  showScreen('home');
  attachHomeListeners();
}

// ──────────────────────────────────────────────
// NAVIGATION
// ──────────────────────────────────────────────
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  const target = document.getElementById(`screen-${id}`);
  if (target) { target.classList.add('active'); target.scrollTop = 0; }
}

// ──────────────────────────────────────────────
// HOME SCREEN
// ──────────────────────────────────────────────
function buildTopicSelector() {
  const wrap = document.getElementById('topic-list');
  if (!wrap) return;
  wrap.innerHTML = temas.map(t =>
    `<div class="topic-chip" data-tema="${t}">${t.replace('Unidad ', 'U')}</div>`
  ).join('');
  wrap.querySelectorAll('.topic-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      chip.classList.toggle('selected');
      syncTopicVisibility();
    });
  });
}

function syncTopicVisibility() {
  const mode = document.querySelector('.mode-btn.active')?.dataset.mode;
  const topicCard = document.getElementById('topic-card');
  if (!topicCard) return;
  topicCard.style.display = (mode === 'tema') ? 'block' : 'none';
}

function updateScoreBanner(nick) {
  const el  = document.getElementById('score-total');
  const rec = document.getElementById('score-record');
  const nn  = document.getElementById('user-nick-display');
  if (el)  el.textContent  = loadPoints().toLocaleString();
  if (rec) rec.textContent = `Récord: ${loadRecord().toLocaleString()}`;
  if (nn)  nn.textContent  = nick || loadUser();
}

function attachHomeListeners() {
  document.querySelectorAll('.mode-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      syncTopicVisibility();
    });
  });

  document.querySelectorAll('.qty-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.qty-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  document.querySelector('.mode-btn[data-mode="rapida"]')?.classList.add('active');
  document.querySelector('.qty-btn[data-qty="20"]')?.classList.add('active');
  syncTopicVisibility();

  document.getElementById('btn-start')?.addEventListener('click', startGame);
  document.getElementById('btn-stats')?.addEventListener('click', () => {
    renderStats(document.getElementById('stats-body'));
    showScreen('stats');
  });
  document.getElementById('btn-leaderboard')?.addEventListener('click', () => showLeaderboard('home'));
  document.getElementById('btn-change-user')?.addEventListener('click', changeUser);
}

function changeUser() {
  clearUser();
  // limpia localStorage de progreso para que el siguiente usuario empiece limpio
  // (no borra el progreso del servidor, que se recarga al entrar con ese nick)
  ['lm_stats','lm_failed','lm_points','lm_record','lm_comodines'].forEach(k =>
    localStorage.removeItem(k)
  );
  showScreen('user');
  const input = document.getElementById('nick-input');
  if (input) { input.value = ''; input.focus(); }
}

// ──────────────────────────────────────────────
// LEADERBOARD
// ──────────────────────────────────────────────
let leaderboardFrom = 'home';

async function showLeaderboard(from) {
  leaderboardFrom = from;
  showScreen('leaderboard');
  const body = document.getElementById('leaderboard-body');
  body.innerHTML = '<div class="loading-state">Cargando ranking...</div>';

  try {
    const res = await fetch('/api/leaderboard');
    if (!res.ok) throw new Error('offline');
    const board = await res.json();
    const currentNick = loadUser();

    if (board.length === 0) {
      body.innerHTML = '<div class="empty-state"><span class="emoji">🏁</span>Aún no hay jugadores. ¡Sé el primero!</div>';
      return;
    }

    const medals = ['🥇', '🥈', '🥉'];
    body.innerHTML = board.map((entry, i) => {
      const isMe = entry.nick === currentNick;
      const acc = entry.totalAnswered > 0
        ? Math.round((entry.totalCorrect / entry.totalAnswered) * 100)
        : 0;
      return `
        <div class="lb-row${isMe ? ' lb-me' : ''}">
          <div class="lb-rank">${medals[i] || `#${i + 1}`}</div>
          <div class="lb-info">
            <div class="lb-nick">${entry.nick}${isMe ? ' <span class="you-tag">vos</span>' : ''}</div>
            <div class="lb-sub">${entry.totalAnswered} preguntas · ${acc}% aciertos</div>
          </div>
          <div class="lb-score">
            <div class="lb-pts">${entry.record.toLocaleString()}</div>
            <div class="lb-pts-lbl">récord</div>
          </div>
        </div>`;
    }).join('');
  } catch {
    body.innerHTML = '<div class="empty-state"><span class="emoji">📡</span>Ranking no disponible en modo local.</div>';
  }
}

// ──────────────────────────────────────────────
// GAME FLOW
// ──────────────────────────────────────────────
function startGame() {
  const mode = document.querySelector('.mode-btn.active')?.dataset.mode || 'rapida';
  const qty  = parseInt(document.querySelector('.qty-btn.active')?.dataset.qty || '20', 10);
  const selectedTopics = [...document.querySelectorAll('.topic-chip.selected')].map(c => c.dataset.tema);

  let pool = [...allQuestions];

  if (mode === 'tema' && selectedTopics.length > 0) {
    pool = pool.filter(q => selectedTopics.includes(q.tema));
  } else if (mode === 'repaso') {
    const failed = loadFailed();
    pool = Object.values(failed).map(f => f.question).filter(Boolean);
    if (pool.length === 0) { showToast('No hay preguntas falladas aún. ¡Jugá una partida primero!'); return; }
  }

  if (pool.length === 0) { showToast('No hay preguntas para los temas seleccionados.'); return; }

  const shuffled   = shuffleArray(pool);
  const questions  = shuffled.slice(0, Math.min(qty, shuffled.length)).map(q => shuffleOptions(q));

  gameState = {
    questions, current: 0, score: 0, streak: 0, maxStreak: 0,
    answers: [], timer: null, mode, totalQ: questions.length,
    comodinesUsed: {}, defensaActive: false, answered: false,
  };

  showScreen('game');
  renderQuestion();
}

function renderQuestion() {
  const q = gameState.questions[gameState.current];
  if (!q) { endGame(); return; }

  gameState.answered      = false;
  gameState.defensaActive = false;
  gameState.comodinesUsed = {};

  const pct = (gameState.current / gameState.totalQ) * 100;
  document.getElementById('progress-fill').style.width    = `${pct}%`;
  document.getElementById('progress-label').textContent   = `${gameState.current + 1} / ${gameState.totalQ}`;
  document.getElementById('score-live-pts').textContent   = gameState.score.toLocaleString();
  document.getElementById('streak-display').textContent   = gameState.streak > 1 ? `🔥 x${gameState.streak}` : '';
  document.getElementById('badge-tema').textContent       = q.tema.replace('Unidad ', 'U');
  document.getElementById('badge-dif').className         = `badge badge-${q.dificultad}`;
  document.getElementById('badge-dif').textContent       = { facil: 'Fácil', media: 'Media', dificil: 'Difícil' }[q.dificultad] || q.dificultad;
  document.getElementById('badge-capciosa').style.display = q.capciosa ? 'inline' : 'none';
  document.getElementById('question-text').textContent   = q.enunciado;

  const optWrap = document.getElementById('options-wrap');
  if (q.tipo === 'relacion') {
    optWrap.innerHTML = renderRelacion(q);
  } else {
    optWrap.innerHTML = renderOpciones(q);
    optWrap.querySelectorAll('.option-btn').forEach(btn => {
      btn.addEventListener('click', () => { if (!gameState.answered) handleAnswer(btn.dataset.id); });
    });
  }

  const fb = document.getElementById('feedback-box');
  fb.className = 'feedback-box';
  fb.innerHTML = '';

  const btnNext = document.getElementById('btn-next');
  btnNext.className = 'btn-next';
  btnNext.textContent = gameState.current + 1 < gameState.totalQ ? 'Siguiente pregunta →' : 'Ver resultados';
  btnNext.onclick = () => { gameState.current++; renderQuestion(); };

  updateComodines();
  startTimer(q);
}

function renderOpciones(q) {
  const LABELS = ['A', 'B', 'C', 'D', 'E'];
  return `<div class="options-grid">${q.opciones.map((opt, i) =>
    `<button class="option-btn" data-id="${opt.id}">
      <span class="opt-letter">${LABELS[i]}</span>
      <span>${opt.texto}</span>
    </button>`
  ).join('')}</div>`;
}

function renderRelacion(q) {
  const derOpts = shuffleArray(q.columna_der);
  return `<div class="relation-container">${q.columna_izq.map(left =>
    `<div class="relation-pair">
      <div class="rel-left">${left.texto}</div>
      <span class="rel-arrow">→</span>
      <select class="rel-select" data-left="${left.id}">
        <option value="">— elegí —</option>
        ${derOpts.map(right => `<option value="${right.id}">${right.texto}</option>`).join('')}
      </select>
    </div>`
  ).join('')}
  <button class="btn-primary" id="btn-check-rel" style="margin-top:8px">Verificar relación</button>
  </div>`;
}

function startTimer(q) {
  if (gameState.timer) gameState.timer.stop();
  const duracion = q.tipo === 'relacion' ? CONFIG.TIEMPO_REL : CONFIG.TIEMPO_OM;

  const bar = document.getElementById('timer-bar');
  const txt = document.getElementById('timer-txt');

  gameState.timer = new Timer({
    duracion,
    onTick(remaining, total) {
      const pct = (remaining / total) * 100;
      bar.style.width = `${pct}%`;
      txt.textContent = `${remaining}s`;
      bar.className = 'timer-bar';
      if (pct < 40) bar.classList.add('warning');
      if (pct < 20) { bar.classList.remove('warning'); bar.classList.add('danger'); }
    },
    onEnd() { if (!gameState.answered) handleTimeout(); },
  });
  gameState.timer.start();

  if (q.tipo === 'relacion') {
    setTimeout(() => {
      document.getElementById('btn-check-rel')?.addEventListener('click', () => {
        if (gameState.answered) return;
        const userAnswers = {};
        document.querySelectorAll('.rel-select').forEach(sel => { userAnswers[sel.dataset.left] = sel.value; });
        const q2 = gameState.questions[gameState.current];
        const { allCorrect, result } = checkRelacionAnswer(q2, userAnswers);
        document.querySelectorAll('.rel-select').forEach(sel => {
          sel.className = 'rel-select ' + (result[sel.dataset.left] ? 'correct' : 'wrong');
          sel.disabled = true;
        });
        handleAnswerResult(allCorrect, 'relacion', q2);
      });
    }, 0);
  }
}

function handleAnswer(selectedId) {
  const q = gameState.questions[gameState.current];
  const correct = selectedId === q.correcta;
  document.querySelectorAll('.option-btn').forEach(btn => {
    btn.disabled = true;
    if (btn.dataset.id === q.correcta)                         btn.classList.add('correct');
    else if (btn.dataset.id === selectedId && !correct)        btn.classList.add('wrong');
  });
  handleAnswerResult(correct, selectedId, q);
}

function handleAnswerResult(correct, userAnswer, q) {
  gameState.answered = true;

  if (!correct && gameState.defensaUsedThisQ && !gameState.defensaActive) {
    gameState.defensaActive = true;
    gameState.answered = false;
    showFeedback('defensa', null, null, q, '🛡️ ¡Defensa activada! Tenés una segunda oportunidad.');
    document.querySelectorAll('.option-btn').forEach(btn => {
      if (!btn.classList.contains('wrong')) { btn.disabled = false; btn.classList.remove('correct'); }
    });
    document.querySelectorAll('.rel-select').forEach(s => { s.disabled = false; s.className = 'rel-select'; });
    const brc = document.getElementById('btn-check-rel');
    if (brc) brc.disabled = false;
    return;
  }

  if (gameState.timer) gameState.timer.stop();

  const tiempoRestante = gameState.timer?.timeLeft || 0;
  const tiempoMax      = q.tipo === 'relacion' ? CONFIG.TIEMPO_REL : CONFIG.TIEMPO_OM;

  let ptsEarned = 0;
  if (correct) {
    gameState.streak++;
    if (gameState.streak > gameState.maxStreak) gameState.maxStreak = gameState.streak;
    ptsEarned = calcPuntos(q.dificultad, tiempoRestante, tiempoMax, gameState.streak);
    gameState.score += ptsEarned;
    document.getElementById('score-live-pts').textContent = gameState.score.toLocaleString();
    document.getElementById('streak-display').textContent = gameState.streak > 1 ? `🔥 x${gameState.streak}` : '';
    showScorePopup(ptsEarned);
    removeFailed(q.id);
  } else {
    gameState.streak = 0;
    document.getElementById('streak-display').textContent = '';
    addFailed(q, userAnswer === 'timeout' ? 'timeout' : userAnswer);
  }

  gameState.answers.push({ question: q, userAnswer, correct, pts: ptsEarned });
  showFeedback(correct ? 'correct' : 'wrong', ptsEarned, q, q, null);
  document.getElementById('btn-next').classList.add('show');
}

function handleTimeout() {
  gameState.answered = true;
  const q = gameState.questions[gameState.current];
  document.querySelectorAll('.option-btn').forEach(btn => {
    btn.disabled = true;
    if (btn.dataset.id === q?.correcta) btn.classList.add('correct');
  });
  addFailed(q, 'timeout');
  gameState.streak = 0;
  document.getElementById('streak-display').textContent = '';
  gameState.answers.push({ question: q, userAnswer: 'timeout', correct: false, pts: 0 });
  showFeedback('timeout', 0, q, q, null);
  document.getElementById('btn-next').classList.add('show');
}

function showFeedback(type, pts, q, qObj, customMsg) {
  const fb = document.getElementById('feedback-box');
  fb.className = `feedback-box show ${type === 'correct' ? 'correct' : type === 'timeout' ? 'timeout' : type === 'defensa' ? 'timeout' : 'wrong'}`;

  if (type === 'defensa') {
    fb.innerHTML = `<div class="fb-title">${customMsg}</div>`;
    return;
  }
  const icon  = type === 'correct' ? '✅' : type === 'timeout' ? '⏱️' : '❌';
  const title = type === 'correct' ? '¡Correcto!' : type === 'timeout' ? '¡Tiempo!' : '¡Incorrecto!';
  fb.innerHTML = `
    <div class="fb-title">${icon} ${title}${pts > 0 ? ` <span class="pts-earned">+${pts} pts</span>` : ''}</div>
    <div class="fb-explanation">${qObj?.explicacion || ''}</div>
  `;
}

// ──────────────────────────────────────────────
// COMODINES
// ──────────────────────────────────────────────
function updateComodines() {
  const pts = loadPoints() + gameState.score;
  Object.entries(CONFIG.COMODINES).forEach(([key, cfg]) => {
    const btn = document.getElementById(`comodin-${key}`);
    if (!btn) return;
    btn.disabled = pts < cfg.costo || gameState.answered;
    btn.onclick  = () => useComodin(key);
  });
}

function useComodin(key) {
  if (gameState.answered) return;
  const q   = gameState.questions[gameState.current];
  const cfg = CONFIG.COMODINES[key];
  if (loadPoints() + gameState.score < cfg.costo) { showToast('Puntos insuficientes'); return; }

  gameState.score = Math.max(0, gameState.score - cfg.costo);
  document.getElementById('score-live-pts').textContent = gameState.score.toLocaleString();
  document.getElementById(`comodin-${key}`)?.classList.add('used');
  document.getElementById(`comodin-${key}`).disabled = true;

  switch (key) {
    case 'defensa':
      gameState.defensaUsedThisQ = true;
      showToast('🛡️ Defensa activada. Si errás, podrás intentarlo de nuevo.');
      break;
    case 'borrar2': {
      if (q.tipo !== 'opcion_multiple') { showToast('Solo aplica a preguntas de opción múltiple.'); return; }
      const incorrectas = q.opciones.filter(o => o.id !== q.correcta);
      shuffleArray(incorrectas).slice(0, 2).forEach(opt => {
        document.querySelector(`.option-btn[data-id="${opt.id}"]`)?.classList.add('hidden');
      });
      showToast('✂️ Se eliminaron 2 opciones incorrectas');
      break;
    }
    case 'tiempo':
      gameState.timer?.addTime(15);
      showToast('⏱️ +15 segundos al reloj');
      break;
    case 'pista': {
      const fb = document.getElementById('feedback-box');
      fb.className = 'feedback-box show timeout';
      fb.innerHTML = `<div class="fb-title">💡 Pista</div><div class="fb-explanation">${q.explicacion?.split('.')[0]}...</div>`;
      break;
    }
  }
  updateComodines();
}

// ──────────────────────────────────────────────
// END GAME
// ──────────────────────────────────────────────
function endGame() {
  if (gameState.timer) gameState.timer.stop();

  const totalPts = loadPoints() + gameState.score;
  savePoints(totalPts);
  saveRecord(totalPts);
  updateStats({ answers: gameState.answers, score: gameState.score, maxStreak: gameState.maxStreak });
  saveToServer();

  updateScoreBanner();
  renderResult();
  showScreen('result');
}

function renderResult() {
  const answers = gameState.answers;
  const correct = answers.filter(a => a.correct).length;
  const total   = answers.length;
  const acc     = total > 0 ? Math.round((correct / total) * 100) : 0;
  const emoji   = acc >= 80 ? '🏆' : acc >= 60 ? '🎉' : acc >= 40 ? '😤' : '😅';

  document.getElementById('result-emoji').textContent    = emoji;
  document.getElementById('result-score').textContent    = gameState.score.toLocaleString();
  document.getElementById('result-accuracy').textContent = `${acc}% de aciertos (${correct}/${total})`;
  document.getElementById('result-streak').textContent   = gameState.maxStreak;
  document.getElementById('result-correct').textContent  = correct;
  document.getElementById('result-total').textContent    = total;

  const wrongs  = answers.filter(a => !a.correct);
  const wrongsEl = document.getElementById('result-wrongs');
  if (wrongs.length === 0) {
    wrongsEl.innerHTML = '<div class="empty-state"><span class="emoji">🎯</span>¡Perfecto! Todas correctas.</div>';
  } else {
    wrongsEl.innerHTML = `<div class="wrongs-list">${wrongs.map(a => {
      const q = a.question;
      let yourText = a.userAnswer === 'timeout' ? '⏱ Sin respuesta' : '';
      if (!yourText && q.tipo === 'opcion_multiple') {
        const opt = q.opciones?.find(o => o.id === a.userAnswer);
        yourText = opt ? opt.texto : a.userAnswer;
      } else if (!yourText && q.tipo === 'verdadero_falso') {
        yourText = a.userAnswer === 'v' ? 'Verdadero' : 'Falso';
      }
      let correctText = '';
      if (q.tipo === 'opcion_multiple') {
        const opt = q.opciones?.find(o => o.id === q.correcta);
        correctText = opt ? opt.texto : q.correcta;
      } else if (q.tipo === 'verdadero_falso') {
        correctText = q.correcta === 'v' ? 'Verdadero' : 'Falso';
      }
      return `<div class="wrong-item">
        <div class="wi-q">${q.enunciado}</div>
        ${yourText ? `<div class="wi-your">❌ Tu respuesta: ${yourText}</div>` : ''}
        <div class="wi-correct">✅ Correcta: ${correctText}</div>
        <div class="wi-exp">${q.explicacion}</div>
      </div>`;
    }).join('')}</div>`;
  }
}

// ──────────────────────────────────────────────
// UI HELPERS
// ──────────────────────────────────────────────
function showScorePopup(pts) {
  const popup = document.createElement('div');
  popup.className = 'score-popup';
  popup.textContent = `+${pts}`;
  popup.style.left = `${Math.random() * 60 + 20}%`;
  popup.style.top  = `${Math.random() * 30 + 40}%`;
  document.body.appendChild(popup);
  setTimeout(() => popup.remove(), 900);
}

let toastTimer;
function showToast(msg) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('show'), 2500);
}

// ──────────────────────────────────────────────
// GLOBAL LISTENERS
// ──────────────────────────────────────────────
function attachGlobalListeners() {
  document.getElementById('btn-play-again')?.addEventListener('click', () => {
    showScreen('home'); updateScoreBanner();
  });
  document.getElementById('btn-repaso-errores')?.addEventListener('click', () => {
    document.querySelector('.mode-btn[data-mode="repaso"]')?.click();
    document.getElementById('btn-start')?.click();
  });
  document.getElementById('btn-ver-stats')?.addEventListener('click', () => {
    renderStats(document.getElementById('stats-body'));
    showScreen('stats');
  });
  document.getElementById('btn-leaderboard-from-result')?.addEventListener('click', () => showLeaderboard('result'));
  document.getElementById('btn-home-from-stats')?.addEventListener('click', () => showScreen('home'));
  document.getElementById('btn-home-from-leaderboard')?.addEventListener('click', () => {
    showScreen(leaderboardFrom === 'user' ? 'user' : 'home');
  });
  document.getElementById('btn-home-from-game')?.addEventListener('click', () => {
    if (gameState.timer) gameState.timer.stop();
    showScreen('home');
    updateScoreBanner();
  });
  document.getElementById('btn-reset')?.addEventListener('click', () => {
    if (confirm('¿Borrar todo el progreso? Esta acción no se puede deshacer.')) {
      resetAll();
      updateScoreBanner();
      renderStats(document.getElementById('stats-body'));
      showToast('Progreso borrado');
    }
  });
}

// ──────────────────────────────────────────────
// BOOT
// ──────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', init);
