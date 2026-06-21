# CLAUDE.md — App de estudio "Lean Manufacture" (estilo Preguntados)

## 1. Objetivo del proyecto

Construir una **aplicación web autocontenida** que me ayude a estudiar y fijar los conceptos de la materia **Lean Manufacture** para rendir el **final oral**. Tengo **5 días** para prepararme. Voy a ir leyendo el resumen de la materia, pero necesito una herramienta de práctica activa que me obligue a recuperar y aplicar la información, no solo a reconocerla.

La app debe ser **entretenida y enganchante** (estilo *Preguntados*), con desafío real, no un cuestionario aburrido. La idea es que practicar dé ganas de seguir jugando.

> **Regla de oro:** las preguntas NO deben ser obvias. Tienen que ser desafiantes, mezclar conceptos y poner a prueba si realmente entendí, no si tengo buena memoria visual. Si una respuesta correcta "salta a la vista", está mal diseñada.

---

## 2. Contexto y prioridades

- **Plazo de estudio:** 6 días → la app tiene que estar 100% funcional y usable desde el día 1.
- **Modalidad de examen:** oral → las explicaciones tras cada respuesta son tan importantes como la pregunta misma. Quiero entender *por qué*, para poder defenderlo hablando.
- **Portabilidad:** debe poder **ejecutarse en cualquier dispositivo** (PC, notebook, celular) sin instalaciones complicadas. Idealmente abrir un archivo en el navegador o levantar un servidor local con un comando.
- **Persistencia:** mi progreso y estadísticas deben guardarse entre sesiones.

---

## 3. Primer entregable obligatorio: el banco de preguntas

> **El JSON de preguntas lo generás vos (Claude), NO yo.**

### 3.1 Fuente
En la carpeta del proyecto hay una carpeta **/resumen** con el contenido de la materia. El primer paso del proyecto es:

1. **Leer y extraer** todo el contenido de `/resumen`.
2. **Identificar los temas/unidades** principales de la materia (armar una lista de "temas" coherente).
3. **Generar ~150 preguntas** de alta calidad basadas estrictamente en ese contenido, guardadas en `data/questions.json`.

> Ve generando las preguntas por tema o unidad para no saturar los token de salida

### 3.2 Requisitos de las preguntas
- **Cantidad:** mínimo **100 preguntas**.
- **Basadas en el contenido real** de `/resumen`. No inventar datos que no estén respaldados por el material.
- **Distribución por tema:** repartir las preguntas entre todos los temas detectados, de forma razonablemente pareja.
- **Distribución por dificultad:** aproximadamente 30% fácil, 45% media, 25% difícil.
- **Distribución por tipo:** ver tipos en 3.4.
- **Desafiantes:** muchas deben **mezclar conceptos de distintos temas**, usar distractores plausibles (opciones incorrectas que suenan razonables) y evitar que la correcta sea obvia por longitud, redacción o eliminación trivial.
- **Preguntas capciosas:** incluir un subconjunto marcado como `"capciosa": true` donde el truco está en un matiz, una excepción o una confusión conceptual frecuente.
- **Explicación obligatoria:** cada pregunta lleva una explicación **corta y clara** (2–4 oraciones) de por qué la respuesta es correcta y, cuando aporte, por qué las otras no. Pensada para poder defender el tema oralmente.

### 3.3 Esquema JSON (formato exacto)

`data/questions.json` debe ser un objeto con metadatos y un array `preguntas`:

```json
{
  "materia": "LeanManuefacture",
  "generado_desde": "/resumen",
  "temas": ["Tema 1 ...", "Tema 2 ...", "..."],
  "preguntas": [
    {
      "id": "q001",
      "tema": "Tema exacto de la lista 'temas'",
      "tipo": "opcion_multiple",
      "dificultad": "media",
      "capciosa": false,
      "enunciado": "Texto de la pregunta...",
      "opciones": [
        { "id": "a", "texto": "Opción A" },
        { "id": "b", "texto": "Opción B" },
        { "id": "c", "texto": "Opción C" },
        { "id": "d", "texto": "Opción D" }
      ],
      "correcta": "c",
      "explicacion": "Por qué C es correcta y por qué las demás no."
    }
  ]
}
```

### 3.4 Tipos de pregunta (`tipo`)

1. **`opcion_multiple`** — 4 opciones (estilo Preguntados). Campo `correcta` = id de la opción.
2. **`verdadero_falso`** — afirmación a evaluar. `opciones` con `{id:"v","texto":"Verdadero"}` y `{id:"f","texto":"Falso"}`; `correcta` = `"v"` o `"f"`. La explicación debe aclarar el matiz.
3. **`relacion`** — relacionar conceptos entre temas. Se presentan dos columnas a emparejar. Usar esta estructura adicional:
   ```json
   {
     "id": "q050",
     "tema": "...",
     "tipo": "relacion",
     "dificultad": "dificil",
     "capciosa": false,
     "enunciado": "Relacioná cada concepto con su definición/par correcto.",
     "columna_izq": [{ "id": "1", "texto": "Concepto A" }, { "id": "2", "texto": "Concepto B" }],
     "columna_der": [{ "id": "x", "texto": "Definición A" }, { "id": "y", "texto": "Definición B" }],
     "correcta": { "1": "x", "2": "y" },
     "explicacion": "..."
   }
   ```
   (Recomendable 3–5 pares por pregunta de este tipo.)

> Validá el JSON al final: que todo `id` sea único, que `tema` siempre exista en `temas`, que `correcta` referencie opciones válidas, y que ninguna pregunta quede sin `explicacion`.

---

## 4. Funcionalidad de la app (mecánica de juego)

### 4.1 Carga y aleatorización
- Al iniciar, la app **carga `questions.json`** y **baraja las preguntas aleatoriamente** (orden distinto en cada partida). También barajar el orden de las opciones dentro de cada pregunta.
- **Nunca** empezar siempre desde el mismo punto. Usar aleatorización real.
- Evitar repetir preguntas ya respondidas dentro de la misma partida hasta agotar el set seleccionado.

### 4.2 Modos de juego
- **Partida rápida:** N preguntas (configurable: 10 / 20 / 50) mezcladas de todos los temas.
- **Por tema:** poder **seleccionar uno o varios temas** y practicar solo esos.
- **Modo desafío / "examen":** sin comodines, con tiempo más ajustado, pensado para simular presión.
- **Modo repaso de errores:** vuelve a presentar las preguntas que fallé en sesiones anteriores.

### 4.3 Temporizador
- Cada pregunta tiene un **límite de tiempo** (sugerido: 20 s opción múltiple / V-F, 35 s relación; ajustable en config).
- Barra o cuenta regresiva visible.
- Si se acaba el tiempo → cuenta como incorrecta (salvo que se use el comodín de tiempo).
- **Responder rápido da más puntos** (bonus por velocidad).

### 4.4 Sistema de puntos
- Acumulo **puntos** por respuestas correctas. Sugerencia de cálculo:
  - Base por dificultad: fácil 100, media 150, difícil 250.
  - Bonus por velocidad: hasta +50% según tiempo restante.
  - Bonus por racha (combo): +25 por cada acierto consecutivo.
- Los puntos sirven para dos cosas: **puntaje/ranking** y **moneda para gastar en comodines**.
- Mostrar puntaje en vivo durante la partida.

### 4.5 Comodines (estilo Preguntados, se compran/gastan puntos)
- **🛡️ Defensa (segunda oportunidad):** si fallo, no pierdo la racha / me deja volver a intentar la misma pregunta una vez. Costo alto.
- **✂️ Borrar dos (50/50):** elimina dos opciones incorrectas en preguntas de opción múltiple. Costo medio.
- **⏱️ Más tiempo:** suma tiempo extra al temporizador de la pregunta actual. Costo bajo.
- **💡 (opcional) Pista:** muestra una pista breve relacionada con la explicación, sin revelar la respuesta. Costo medio.
- Cada comodín tiene un **costo en puntos** configurable; deshabilitarlo si no alcanzan los puntos. Animación/feedback claro al usarlo.

### 4.6 Feedback tras cada respuesta
- Marcar visualmente correcta (verde) / incorrecta (rojo).
- **Mostrar siempre la explicación corta** de por qué esa es la respuesta. Este paso es central, no opcional.
- Indicar puntos ganados/perdidos en el momento.
- Botón para continuar a la siguiente pregunta.

---

## 5. Seguimiento de rendimiento (estadísticas)

Guardar el progreso de forma **persistente** (ver 6.2) y mostrar un panel de estadísticas con:

- **% de aciertos global** y evolución por sesión.
- **% de aciertos por tema** → para detectar mis puntos débiles.
- **% de aciertos por tipo de pregunta** y por dificultad.
- **Racha máxima**, mejor puntaje, preguntas respondidas en total.
- **Lista de preguntas falladas** (alimenta el modo "repaso de errores").
- Al menos **un gráfico** (ej. barras de aciertos por tema, o línea de evolución) para visualizar rápidamente dónde estoy floja. Usar una librería liviana de charts o canvas/SVG simple.
- Mostrar un mensaje/recomendación: "Tu tema más débil es X, practicá eso".

---

## 6. Stack técnico y arquitectura

### 6.1 Tecnología recomendada
- **App web estática autocontenida**: HTML + CSS + JavaScript (vanilla o un framework liviano, a tu criterio, pero mantenelo simple y sin build pesado).
- Debe poder **abrirse en cualquier navegador** y funcionar también en celular (diseño **responsive**).
- **Python** se usa para la **generación del banco de preguntas** desde `/resumen` (extracción de texto y armado del JSON) y, opcionalmente, para un pequeño servidor local de desarrollo (`python -m http.server`). La app en sí no debe depender de un backend para funcionar.
- Sin dependencias de pago ni servicios externos: todo debe correr offline una vez generado el JSON.

### 6.2 Persistencia
- Usar **`localStorage`** del navegador para guardar estadísticas, puntaje acumulado, comodines y preguntas falladas. (No usar servicios externos ni base de datos; tiene que funcionar offline.)
- Incluir un botón para **reiniciar/borrar progreso**.

### 6.3 Estructura de archivos sugerida
```
/
├── CLAUDE.md
├── resumen                 # fuente (lo pongo yo)
│   ├── unidadN.pdf
├── index.html                 # entrada de la app
├── css/styles.css
├── js/
│   ├── app.js                 # lógica principal / loop de juego
│   ├── game.js                # puntos, comodines, temporizador
│   ├── stats.js               # estadísticas y gráficos
│   └── storage.js             # localStorage
├── data/
│   └── questions.json         # banco generado desde resumen.pdf
├── scripts/
│   └── generar_preguntas.py   # extrae resumen.pdf y arma questions.json (opcional/documentado)
└── README.md                  # cómo ejecutar
```

---

## 7. Diseño / UX

- Estética **moderna, colorida y enganchante** tipo trivia (sin caer en lo infantil). Buen contraste, tipografía legible, animaciones sutiles en aciertos/errores y al usar comodines.
- **Mobile-first / responsive**: que se vea bien y se pueda jugar cómodo desde el celular.
- Pantallas mínimas:
  1. **Inicio** (elegir modo, tema/s, cantidad de preguntas, ver puntaje acumulado).
  2. **Juego** (pregunta, opciones, temporizador, puntaje, comodines).
  3. **Resultado de partida** (puntaje, aciertos, repaso de las que fallé con su explicación).
  4. **Estadísticas** (gráficos y desglose por tema/dificultad).
- Incluir alguna **ilustración o ícono** ligero donde sume (no obligatorio que sean imágenes pesadas; pueden ser íconos/SVG).
- Feedback visual y, si es simple de lograr, **sonidos** cortos de acierto/error (con opción de silenciar).

---

## 8. Orden de trabajo sugerido

1. **Leer `/resumen`**, mapear temas y generar `data/questions.json` con ≥100 preguntas de calidad (este es el cimiento, hacelo bien primero).
2. Validar el JSON (ids únicos, temas consistentes, explicaciones completas).
3. Maqueta de la app: pantallas, navegación, carga y barajado de preguntas.
4. Loop de juego: temporizador, respuestas, feedback con explicación.
5. Puntos, rachas y comodines.
6. Persistencia y estadísticas con gráfico.
7. Modos (por tema, examen, repaso de errores) y selección de temas.
8. Pulido responsive + README con instrucciones de ejecución.

---

## 9. Criterios de aceptación (checklist)

- [ ] `questions.json` tiene ≥100 preguntas derivadas de `/resumen`, con todos los campos del esquema.
- [ ] Hay preguntas de opción múltiple, verdadero/falso y relación entre temas, además de algunas capciosas.
- [ ] Las preguntas son desafiantes y mezclan conceptos; no son triviales.
- [ ] Cada respuesta muestra una explicación corta del porqué.
- [ ] Las preguntas se barajan aleatoriamente en cada partida.
- [ ] Funcionan temporizador, puntos, rachas y los comodines (defensa, borrar dos, más tiempo).
- [ ] Puedo seleccionar y filtrar por tema.
- [ ] Se guardan y muestran estadísticas de rendimiento con al menos un gráfico.
- [ ] Corre en navegador de PC y celular, offline, abriendo `index.html` o con un servidor local simple.
- [ ] Hay un `README.md` con instrucciones claras de ejecución.

---

## 10. Notas / decisiones tomadas (revisables)

- Se asume app **web estática + localStorage** por máxima portabilidad y porque debe correr en cualquier dispositivo sin instalar nada. Si preferís otra cosa (ej. app de escritorio empaquetada), avisá antes de avanzar.
- Los costos de comodines, tiempos y puntajes están como **valores sugeridos**: dejalos en un archivo de config fácil de tocar para poder calibrarlos.
- Idioma de toda la interfaz y las preguntas: **español**.