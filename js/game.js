/**
 * game.js — puntos, rachas, comodines, temporizador
 */

export const CONFIG = {
  PUNTOS_BASE: { facil: 100, media: 150, dificil: 250 },
  BONUS_VELOCIDAD_MAX: 0.5,   // +50% por responder rápido
  BONUS_RACHA: 25,            // pts extra por cada acierto consecutivo (si racha ≥ 2)
  TIEMPO_OM: 20,              // segundos por opción múltiple / V-F
  TIEMPO_REL: 35,             // segundos por relación
  COMODINES: {
    defensa:  { costo: 400, emoji: '🛡️', label: 'Defensa',    desc: 'Segunda oportunidad' },
    borrar2:  { costo: 200, emoji: '✂️', label: 'Borrar 2',   desc: 'Elimina 2 incorrectas' },
    tiempo:   { costo: 100, emoji: '⏱️', label: '+Tiempo',    desc: 'Suma 15 segundos' },
    pista:    { costo: 150, emoji: '💡', label: 'Pista',       desc: 'Muestra una pista' },
  },
};

export function calcPuntos(dificultad, tiempoRestante, tiempoMax, racha) {
  const base = CONFIG.PUNTOS_BASE[dificultad] || 100;
  const speedRatio = Math.max(0, tiempoRestante / tiempoMax);
  const bonusSpeed = Math.round(base * CONFIG.BONUS_VELOCIDAD_MAX * speedRatio);
  const bonusRacha = racha >= 2 ? CONFIG.BONUS_RACHA * (racha - 1) : 0;
  return base + bonusSpeed + bonusRacha;
}

export class Timer {
  constructor({ duracion, onTick, onEnd }) {
    this.duracion = duracion;
    this.remaining = duracion;
    this.onTick = onTick;
    this.onEnd = onEnd;
    this._interval = null;
    this._paused = false;
  }

  start() {
    this._interval = setInterval(() => {
      if (this._paused) return;
      this.remaining -= 1;
      this.onTick(this.remaining, this.duracion);
      if (this.remaining <= 0) {
        this.stop();
        this.onEnd();
      }
    }, 1000);
    this.onTick(this.remaining, this.duracion);
  }

  addTime(seconds) {
    this.remaining = Math.min(this.remaining + seconds, this.duracion + seconds);
    this.onTick(this.remaining, this.duracion + seconds);
    this.duracion += seconds;
  }

  pause() { this._paused = true; }
  resume() { this._paused = false; }

  stop() {
    if (this._interval) { clearInterval(this._interval); this._interval = null; }
  }

  get timeLeft() { return this.remaining; }
}

export function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function shuffleOptions(question) {
  if (question.tipo !== 'opcion_multiple') return question;
  const shuffled = shuffleArray(question.opciones);
  return { ...question, opciones: shuffled };
}

export function checkRelacionAnswer(question, userAnswers) {
  const correct = question.correcta;
  let allCorrect = true;
  const result = {};
  for (const [izqId, derExpected] of Object.entries(correct)) {
    const userVal = userAnswers[izqId];
    const ok = userVal === derExpected;
    result[izqId] = ok;
    if (!ok) allCorrect = false;
  }
  return { allCorrect, result };
}
