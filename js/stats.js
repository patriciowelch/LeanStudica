/**
 * stats.js — render estadísticas y gráficos
 */

import { loadStats, loadFailed, loadPoints, loadRecord } from './storage.js';

export function renderStats(container) {
  const stats = loadStats();
  const failed = loadFailed();
  const pts = loadPoints();
  const record = loadRecord();

  const globalAcc = stats.totalAnswered > 0
    ? Math.round((stats.totalCorrect / stats.totalAnswered) * 100)
    : 0;

  container.innerHTML = `
    <div class="stats-grid">
      <div class="stat-card">
        <div class="s-val">${globalAcc}%</div>
        <div class="s-lbl">Aciertos global</div>
      </div>
      <div class="stat-card">
        <div class="s-val">${stats.totalAnswered}</div>
        <div class="s-lbl">Preguntas respondidas</div>
      </div>
      <div class="stat-card">
        <div class="s-val">${stats.maxStreak}</div>
        <div class="s-lbl">Racha máxima</div>
      </div>
      <div class="stat-card">
        <div class="s-val">${record.toLocaleString()}</div>
        <div class="s-lbl">Mejor puntaje</div>
      </div>
    </div>

    <div class="chart-wrap">
      <h3>% Aciertos por Tema</h3>
      <div class="theme-bars" id="tema-bars"></div>
    </div>

    <div class="chart-wrap">
      <h3>Por Dificultad</h3>
      <div class="theme-bars" id="dif-bars"></div>
    </div>

    <div class="chart-wrap">
      <h3>Por Tipo de Pregunta</h3>
      <div class="theme-bars" id="tipo-bars"></div>
    </div>

    <div id="recommendation-box"></div>

    <div class="chart-wrap">
      <h3>Preguntas Falladas (${Object.keys(failed).length})</h3>
      <div id="failed-list"></div>
    </div>
  `;

  renderBars('tema-bars', stats.byTema, (k) => k.replace('Unidad ', 'U'));
  renderBars('dif-bars', stats.byDificultad, (k) => ({ facil: 'Fácil', media: 'Media', dificil: 'Difícil' }[k] || k));
  renderBars('tipo-bars', stats.byTipo, (k) => ({ opcion_multiple: 'Opción múltiple', verdadero_falso: 'V/F', relacion: 'Relación' }[k] || k));
  renderRecommendation(stats);
  renderFailed(failed);
}

function renderBars(containerId, data, labelFn) {
  const el = document.getElementById(containerId);
  if (!el) return;
  const entries = Object.entries(data);
  if (entries.length === 0) {
    el.innerHTML = '<div class="empty-state"><span class="emoji">📊</span>Sin datos aún</div>';
    return;
  }
  el.innerHTML = entries.map(([key, val]) => {
    const pct = val.total > 0 ? Math.round((val.correct / val.total) * 100) : 0;
    const color = pct >= 70 ? 'var(--accent)' : pct >= 40 ? 'var(--warning)' : 'var(--danger)';
    return `
      <div class="theme-bar-item">
        <div class="theme-bar-label">
          <span>${labelFn(key)}</span>
          <span style="color:${color};font-weight:700">${pct}% (${val.correct}/${val.total})</span>
        </div>
        <div class="theme-bar-track">
          <div class="theme-bar-fill" style="width:${pct}%;background:${color}"></div>
        </div>
      </div>`;
  }).join('');
}

function renderRecommendation(stats) {
  const box = document.getElementById('recommendation-box');
  if (!box) return;
  const entries = Object.entries(stats.byTema);
  if (entries.length === 0) return;

  const worst = entries
    .filter(([, v]) => v.total >= 3)
    .sort(([, a], [, b]) => (a.correct / a.total) - (b.correct / b.total))[0];
  const best = entries
    .filter(([, v]) => v.total >= 3)
    .sort(([, a], [, b]) => (b.correct / b.total) - (a.correct / a.total))[0];

  if (!worst) return;
  const worstPct = Math.round((worst[1].correct / worst[1].total) * 100);
  const bestPct = best ? Math.round((best[1].correct / best[1].total) * 100) : 0;

  box.innerHTML = `
    <div class="recommendation">
      ⚠️ Tu tema más débil es <strong>${worst[0]}</strong> (${worstPct}% aciertos).
      ¡Practicá ese tema primero!<br>
      ${best && best[0] !== worst[0] ? `✅ Tu punto más fuerte es <strong>${best[0]}</strong> (${bestPct}%).` : ''}
    </div>`;
}

function renderFailed(failed) {
  const el = document.getElementById('failed-list');
  if (!el) return;
  const entries = Object.values(failed);
  if (entries.length === 0) {
    el.innerHTML = '<div class="empty-state"><span class="emoji">🎯</span>¡Sin errores registrados todavía!</div>';
    return;
  }
  el.innerHTML = `<div class="wrongs-list">${entries.slice(0, 20).map(f => {
    const q = f.question;
    let yourText = f.yourAnswer === 'timeout' ? '⏱ Sin respuesta' : '';
    if (!yourText && q.tipo === 'opcion_multiple') {
      const opt = q.opciones?.find(o => o.id === f.yourAnswer);
      yourText = opt ? opt.texto : f.yourAnswer;
    } else if (!yourText && q.tipo === 'verdadero_falso') {
      yourText = f.yourAnswer === 'v' ? 'Verdadero' : 'Falso';
    }
    let correctText = '';
    if (q.tipo === 'opcion_multiple') {
      const opt = q.opciones?.find(o => o.id === q.correcta);
      correctText = opt ? opt.texto : q.correcta;
    } else if (q.tipo === 'verdadero_falso') {
      correctText = q.correcta === 'v' ? 'Verdadero' : 'Falso';
    } else {
      correctText = JSON.stringify(q.correcta);
    }
    return `
      <div class="wrong-item">
        <div class="wi-q">${q.enunciado}</div>
        ${yourText ? `<div class="wi-your">❌ Tu respuesta: ${yourText}</div>` : ''}
        <div class="wi-correct">✅ Correcta: ${correctText}</div>
        <div class="wi-exp">${q.explicacion}</div>
      </div>`;
  }).join('')}</div>`;
}
