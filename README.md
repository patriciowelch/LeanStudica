# Organización Industrial — App de Estudio

App de trivia estilo *Preguntados* para repasar la materia Organización Industrial antes del final oral.

## Cómo ejecutar

### Opción 1 — Python (recomendado)
```bash
cd <carpeta del proyecto>
py -m http.server 8080
```
Abrí el navegador en: **http://localhost:8080**

### Opción 2 — Abrir directo (puede no funcionar en todos los navegadores por CORS)
Abrí `index.html` directamente en el navegador.

## Modos de juego

| Modo | Descripción |
|------|-------------|
| ⚡ Partida rápida | Preguntas aleatorias de todos los temas |
| 📚 Por tema | Elegís uno o varios temas |
| 🎯 Modo examen | Sin comodines, simula presión de examen |
| 🔄 Repaso errores | Solo las preguntas que fallaste |

## Comodines (se pagan con puntos)

| Comodín | Costo | Efecto |
|---------|-------|--------|
| 🛡️ Defensa | 400 pts | Segunda oportunidad si errás |
| ✂️ Borrar 2 | 200 pts | Elimina 2 opciones incorrectas |
| ⏱️ +Tiempo | 100 pts | Suma 15 segundos al reloj |
| 💡 Pista | 150 pts | Muestra una pista sin revelar la respuesta |

## Sistema de puntos

- **Base por dificultad:** Fácil=100, Media=150, Difícil=250
- **Bonus velocidad:** hasta +50% según tiempo restante
- **Bonus racha:** +25 pts por cada acierto consecutivo (si racha ≥ 2)

## Banco de preguntas

156 preguntas divididas en 10 unidades temáticas:
- Unidad 1: Localización
- Unidad 2: Ingeniería de Producto
- Unidad 3: Ingeniería de Proceso
- Unidad 4: Layout
- Unidad 5: Estudio del Trabajo
- Unidad 6: Estudio de Métodos
- Unidad 7: Medición del Trabajo
- Unidad 8: Organización del Mantenimiento
- Unidad 9: Manipulación de Materiales
- Unidad 10: Organización de la Manufactura

Tipos: opción múltiple (127), verdadero/falso (24), relación (5). Incluye 55 preguntas "capciosas".

## Estructura de archivos

```
├── index.html           # App principal
├── css/styles.css       # Estilos
├── js/
│   ├── app.js           # Lógica principal
│   ├── game.js          # Puntos, comodines, temporizador
│   ├── stats.js         # Estadísticas y gráficos
│   └── storage.js       # localStorage
├── data/
│   └── questions.json   # Banco de 156 preguntas
└── scripts/             # Scripts de generación (Python)
```

## Regenerar preguntas

```bash
py -m pip install pdfplumber pypdf
py scripts/assemble_questions.py
```
