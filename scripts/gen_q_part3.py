"""Genera preguntas para Unidades 7-10 de Organización Industrial."""
import json

preguntas = [
# ─────────────────────────────────────────────
# UNIDAD 7: MEDICIÓN DEL TRABAJO (18 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q097",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuál es la definición de 'tiempo estándar'?",
  "opciones": [
    {"id": "a", "texto": "El tiempo observado con cronómetro dividido por el número de ciclos medidos"},
    {"id": "b", "texto": "El tiempo total que dispone un operario calificado para obtener una unidad de producción, con habilidad y ritmo normal, incluyendo suplementos por necesidades personales, fatiga y demoras inevitables"},
    {"id": "c", "texto": "El tiempo teórico mínimo calculado por ingeniería sin considerar interrupciones ni descansos"},
    {"id": "d", "texto": "El promedio de los tiempos observados en 10 ciclos consecutivos"}
  ],
  "correcta": "b",
  "explicacion": "Tiempo estándar = tiempo total que dispone un operario calificado para obtener una unidad de producción, con habilidad y ritmo normales, siguiendo un método claramente establecido, con una norma de calidad específica, e incluyendo suplementos por: necesidades personales, fatiga acumulada durante la jornada y demoras inevitables."
},
{
  "id": "q098",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "La fórmula para calcular el tiempo normal es:",
  "opciones": [
    {"id": "a", "texto": "Tiempo normal = Tiempo cronometrado + Suplementos"},
    {"id": "b", "texto": "Tiempo normal = Tiempo cronometrado × (Ritmo evaluado / 100)"},
    {"id": "c", "texto": "Tiempo normal = Tiempo estándar − Suplementos"},
    {"id": "d", "texto": "Tiempo normal = Tiempo observado / Número de ciclos"}
  ],
  "correcta": "b",
  "explicacion": "Tiempo normal = Tiempo cronometrado × (Ritmo evaluado / 100). El ritmo evaluado ajusta el tiempo observado al ritmo de un trabajador promedio (100%). Si el operario trabajó al 90%, el tiempo se ajusta multiplicando 0.90. Los suplementos se agregan DESPUÉS para obtener el tiempo estándar."
},
{
  "id": "q099",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "En el cronometraje ACUMULATIVO, el analista detiene el cronómetro al final de cada elemento y obtiene directamente el tiempo de ese elemento.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Eso describe el cronometraje CON VUELTA A CERO. En el cronometraje ACUMULATIVO el reloj corre continuamente durante todo el estudio y al final de cada elemento se anota el tiempo ACUMULADO transcurrido. Los valores individuales por elemento se calculan LUEGO, por diferencia. La OIT recomienda el acumulativo."
},
{
  "id": "q100",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuáles son los 4 motivos por los que los estándares de tiempo son necesarios?",
  "opciones": [
    {"id": "a", "texto": "Controlar asistencia, pagar salarios, medir fatiga y planificar turnos"},
    {"id": "b", "texto": "Programar el trabajo y asignar capacidad, motivar y medir desempeño, presentar cotizaciones, y proporcionar puntos de referencia para mejoras"},
    {"id": "c", "texto": "Calcular el precio de venta, diseñar el lay out, seleccionar maquinaria y entrenar operarios"},
    {"id": "d", "texto": "Determinar el número de operarios, calcular costos de MO, establecer cuotas de producción y controlar calidad"}
  ],
  "correcta": "b",
  "explicacion": "Los 4 motivos son: 1) Programar trabajo y asignar capacidad (todos los enfoques de programación requieren estimar el tiempo), 2) Ofrecer base objetiva para motivar a la fuerza de trabajo y medir desempeño (especialmente en planes de incentivos), 3) Presentar cotizaciones para nuevos contratos y evaluar existentes, 4) Proporcionar puntos de referencia para mejoras y benchmarking."
},
{
  "id": "q101",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "¿Cuáles son los suplementos por necesidades personales y por fatiga según el material?",
  "opciones": [
    {"id": "a", "texto": "Necesidades personales: 2-3%; Fatiga: 8-10%"},
    {"id": "b", "texto": "Necesidades personales: 5-7%; Fatiga: 4%"},
    {"id": "c", "texto": "Necesidades personales: 10%; Fatiga: 5%"},
    {"id": "d", "texto": "Necesidades personales: 15 minutos/turno; Fatiga: 30 minutos/turno"}
  ],
  "correcta": "b",
  "explicacion": "Suplementos por necesidades personales: 5% a 7% (tomar agua, baño). Suplementos por fatiga: 4% (compensa la reducción de energía a lo largo de la jornada). También existen suplementos por demoras inevitables (limpieza de máquina, espera de trabajo) y por incentivos. Estos son los valores de referencia que usa el material."
},
{
  "id": "q102",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "¿Qué significa que un trabajador tenga un ritmo de 133% en la valoración del ritmo?",
  "opciones": [
    {"id": "a", "texto": "El operario trabaja 33% más rápido que el promedio, lo cual es siempre un indicador de excelente desempeño"},
    {"id": "b", "texto": "El operario está en el máximo rendimiento esperable y puede ser señal de un estándar incorrecto o modificación de velocidades de máquina"},
    {"id": "c", "texto": "El operario trabaja 33% más lento que el estándar y debe ser corregido"},
    {"id": "d", "texto": "El operario supera el 100% del estándar porque recibió incentivos económicos adicionales"}
  ],
  "correcta": "b",
  "explicacion": "Un ritmo de 133% significa que el trabajador trabaja al máximo rendimiento esperable para un operario motivado y con aptitudes. Si se observa este nivel de forma sostenida, hay que estar atento: puede ser un aviso de que el estándar fue mal calculado o que hubo una modificación en las velocidades de las máquinas. No es automáticamente 'excelente'."
},
{
  "id": "q103",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuáles son las 4 técnicas básicas para medir el trabajo?",
  "opciones": [
    {"id": "a", "texto": "Cronometraje, muestreo, entrevistas y observación directa"},
    {"id": "b", "texto": "Estudios de tiempo (cronómetro), muestreo de trabajo, datos elementales, y sistemas de datos predeterminados de tiempos y movimientos"},
    {"id": "c", "texto": "MTM, MOST, MODAPTS y tiempos históricos"},
    {"id": "d", "texto": "Cronometraje continuo, intermitente, estimación y simulación"}
  ],
  "correcta": "b",
  "explicacion": "Las 4 técnicas son: 1) Estudios de tiempo con cronómetro (observación directa), 2) Muestreo de trabajo (observación directa estadística), 3) Datos elementales (observación indirecta, suma tiempos de base de datos), 4) Sistemas de datos predeterminados de tiempos y movimientos -tiempos predeterminados- (observación indirecta, tablas de laboratorio)."
},
{
  "id": "q104",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Para qué tipo de trabajo se recomienda el muestreo de trabajo como técnica de medición?",
  "opciones": [
    {"id": "a", "texto": "Para trabajo repetitivo y muy detallado que requiere mucha precisión"},
    {"id": "b", "texto": "Para trabajo con equipamiento de tiempo fijo donde no es necesaria la observación directa"},
    {"id": "c", "texto": "Para trabajo poco frecuente o de largo ciclo donde el cronometraje directo sería ineficiente"},
    {"id": "d", "texto": "Para determinar tiempos de movimientos básicos en un laboratorio controlado"}
  ],
  "correcta": "c",
  "explicacion": "El muestreo de trabajo es el instrumento aconsejable cuando el trabajo es poco frecuente o requiere un largo tiempo dentro del ciclo (donde el cronometraje directo sería muy costoso o impracticable). Para trabajo repetitivo y detallado se usan estudios de tiempos con cronómetro y datos predeterminados."
},
{
  "id": "q105",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "¿Cuántas observaciones se recomiendan en un estudio de tiempos cuando hay GRANDES variaciones entre los elementos?",
  "opciones": [
    {"id": "a", "texto": "25 a 30 observaciones"},
    {"id": "b", "texto": "35 a 40 observaciones"},
    {"id": "c", "texto": "55 a 60 observaciones"},
    {"id": "d", "texto": "Solo 10 observaciones (más variabilidad = menos confianza, no más observaciones)"}
  ],
  "correcta": "c",
  "explicacion": "Las recomendaciones son: sin grandes variaciones → 25 a 30 observaciones; variaciones promedio entre elementos → 35 a 40 observaciones; grandes variaciones entre elementos → 55 a 60 observaciones. A mayor variabilidad, se necesitan MÁS observaciones para que la muestra sea estadísticamente representativa."
},
{
  "id": "q106",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál de los siguientes es un elemento ACÍCLICO en un estudio de tiempos?",
  "opciones": [
    {"id": "a", "texto": "Tomar la pieza al comenzar el ciclo"},
    {"id": "b", "texto": "Girar la pieza en el torno durante el ciclo"},
    {"id": "c", "texto": "Lubricar la máquina cada 50 ciclos"},
    {"id": "d", "texto": "Depositar la pieza terminada al final del ciclo"}
  ],
  "correcta": "c",
  "explicacion": "Los elementos acíclicos aparecen a intervalos regulares o irregulares durante la operación (no en cada ciclo). Lubricar la máquina cada 50 ciclos es acíclico: ocurre cada cierta cantidad de ciclos, no en cada uno. Su frecuencia debe medirse y prorratearse para calcular cómo incide en el tiempo por pieza. Los otros tres son elementos cíclicos."
},
{
  "id": "q107",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué es un 'operario calificado' en el contexto de los estudios de tiempo?",
  "opciones": [
    {"id": "a", "texto": "El operario más rápido de la planta, que sirve como referencia de velocidad máxima"},
    {"id": "b", "texto": "Aquel que tiene aptitudes físicas necesarias, inteligencia e instrucción requeridas, y ha adquirido la destreza para efectuar el trabajo según normas satisfactorias de seguridad, cantidad y calidad"},
    {"id": "c", "texto": "El operario con más años de experiencia en la empresa, sin importar su velocidad"},
    {"id": "d", "texto": "Cualquier operario que supere el 100% de ritmo en la valoración"}
  ],
  "correcta": "b",
  "explicacion": "Operario calificado: aquel de quien se reconoce que tiene las aptitudes físicas necesarias, que posee la inteligencia e instrucción requeridas, y que ha adquirido la destreza y conocimientos necesarios para efectuar el trabajo según normas satisfactorias de seguridad, cantidad y calidad. No es el más rápido, sino el que sigue el método correctamente."
},
{
  "id": "q108",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "Los tiempos predeterminados (sistemas de datos de tiempos y movimientos) ya incluyen la normalización al ritmo 100%, por lo que NO es necesario hacer ningún ajuste por valoración del ritmo.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "v",
  "explicacion": "Verdadero. Los tiempos predeterminados ya están tabulados y 'normalizados' al ritmo 100%. Por lo tanto, no hay que hacer ningún ajuste por valoración del ritmo como en el cronometraje. Sin embargo, sí se deben agregar suplementos (necesidades personales, fatiga, demoras) para obtener el tiempo estándar final."
},
{
  "id": "q109",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Un crítico de los tiempos estándar argumenta: 'Las personas no son uniformes, por lo tanto una línea nunca podrá trabajar a un ritmo superior al del trabajador más lento.' ¿Qué propone como alternativa según el material?",
  "opciones": [
    {"id": "a", "texto": "Eliminar completamente los estándares y medir solo la calidad del producto"},
    {"id": "b", "texto": "Utilizar cálculos globales de productividad para cada célula, línea o planta, previo trabajo de concientización del personal"},
    {"id": "c", "texto": "Reemplazar a los trabajadores lentos para igualar el ritmo de la línea"},
    {"id": "d", "texto": "Establecer estándares individuales por operario en lugar de estándares de línea"}
  ],
  "correcta": "b",
  "explicacion": "Los críticos proponen: en reemplazo de los estándares individuales, utilizar cálculos globales de productividad para cada célula, línea de producción o planta. Tener en cuenta que previo a su aplicación se debe trabajar en la concientización del personal. También argumentan que es mejor fabricar lo que se necesita (JIT) sin estimular la producción máxima mediante incentivos."
},
{
  "id": "q110",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es la diferencia entre 'tiempo normal' y 'tiempo estándar'?",
  "opciones": [
    {"id": "a", "texto": "No hay diferencia; son dos nombres para el mismo concepto"},
    {"id": "b", "texto": "El tiempo normal no incluye suplementos; el tiempo estándar sí incluye suplementos por necesidades personales, fatiga y demoras"},
    {"id": "c", "texto": "El tiempo normal incluye suplementos; el tiempo estándar es el tiempo teórico sin interrupciones"},
    {"id": "d", "texto": "El tiempo normal se mide en segundos; el tiempo estándar se expresa en minutos"}
  ],
  "correcta": "b",
  "explicacion": "Tiempo normal = tiempo básico para realizar la operación a ritmo 100% (tiempo cronometrado × ritmo/100). Tiempo estándar = tiempo normal + suplementos (necesidades personales 5-7%, fatiga 4%, demoras inevitables). El estándar es el que se usa para programar producción, calcular costos y establecer incentivos."
},
{
  "id": "q111",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuál de las siguientes es una ventaja de dividir la operación en elementos en el estudio de tiempos?",
  "opciones": [
    {"id": "a", "texto": "Permite medir solo los tiempos productivos y excluir automáticamente los improductivos"},
    {"id": "b", "texto": "Es frecuente encontrar elementos comunes en distintos productos, formando una base de datos reutilizable"},
    {"id": "c", "texto": "Elimina la necesidad de valorar el ritmo del operario para cada elemento"},
    {"id": "d", "texto": "Permite que el estudio sea realizado por cualquier persona sin formación específica"}
  ],
  "correcta": "b",
  "explicacion": "Entre las ventajas de dividir en elementos: permite evaluar el desempeño durante distintas partes de la operación, analizar tiempos productivos e improductivos con detalle, determinar el número de observaciones necesarias, y es frecuente encontrar elementos COMUNES en distintos productos que forman una importante base de datos reutilizable."
},
{
  "id": "q112",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Se mide un operario y se obtiene que su tiempo cronometrado promedio es de 2 minutos con un ritmo evaluado de 90%. ¿Cuál es su tiempo normal?",
  "opciones": [
    {"id": "a", "texto": "2,22 minutos (2 / 0.90)"},
    {"id": "b", "texto": "1,80 minutos (2 × 0.90)"},
    {"id": "c", "texto": "2 minutos (el tiempo observado ya es el normal al promediarlo)"},
    {"id": "d", "texto": "1,60 minutos (2 × 0.80, usando el complemento del ritmo)"}
  ],
  "correcta": "b",
  "explicacion": "Tiempo normal = Tiempo cronometrado × (Ritmo/100) = 2 × (90/100) = 2 × 0.90 = 1.80 minutos. El operario trabajó más lento que el promedio (90% del ritmo normal), por lo que el tiempo normal (de un operario 100%) es MENOR que el observado. La confusión frecuente es dividir en lugar de multiplicar."
},
{
  "id": "q113",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Por qué la OIT recomienda el cronometraje ACUMULATIVO sobre el de vuelta a cero?",
  "opciones": [
    {"id": "a", "texto": "Porque permite que el analista vea el tiempo de cada elemento en tiempo real para ajustar la valoración"},
    {"id": "b", "texto": "Porque asegura que todos los elementos quedan involucrados en el estudio (no se detiene el cronómetro) y los trabajadores confían más en el sistema"},
    {"id": "c", "texto": "Porque es más rápido de aplicar y requiere menos cálculos posteriores"},
    {"id": "d", "texto": "Porque elimina la necesidad de calcular diferencias entre lecturas consecutivas"}
  ],
  "correcta": "b",
  "explicacion": "El cronometraje acumulativo es recomendado por la OIT porque: 1) El reloj no se detiene, asegurando que TODOS los elementos quedan involucrados en el estudio, 2) El analista no puede ver el tiempo individual durante el estudio, lo que no influye en su valoración del ritmo, y 3) Los trabajadores confían más en este sistema porque ven que no se omite ningún tiempo."
},
{
  "id": "q114",
  "tema": "Unidad 7: Medición del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "La duración mínima recomendada para un elemento en un estudio de tiempos es:",
  "opciones": [
    {"id": "a", "texto": "0,01 minutos (1 segundo)"},
    {"id": "b", "texto": "0,04 minutos"},
    {"id": "c", "texto": "0,10 minutos (6 segundos)"},
    {"id": "d", "texto": "0,25 minutos (15 segundos)"}
  ],
  "correcta": "b",
  "explicacion": "No se recomienda definir elementos de duración inferior a 0,04 minutos. Y aun respetando este límite, es aconsejable combinar secuencialmente elementos cortos y largos para que el analista pueda observar y anotar los datos con comodidad. Elementos demasiado cortos generan errores de lectura en el cronómetro."
},

# ─────────────────────────────────────────────
# UNIDAD 8: ORGANIZACIÓN DEL MANTENIMIENTO (17 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q115",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cómo cambió la ecuación económica del mantenimiento en las empresas modernas?",
  "opciones": [
    {"id": "a", "texto": "Antes: BE = PV – Costo; Ahora: Costo + BE = Precio de Venta"},
    {"id": "b", "texto": "Antes: Costo + BE = Precio de Venta; Ahora: BE = Precio de Venta – Costo (el precio lo fija el cliente)"},
    {"id": "c", "texto": "La ecuación no cambió, siempre fue: Precio de Venta = Costo + Margen"},
    {"id": "d", "texto": "Antes: BE era maximizado; Ahora: BE es un costo fijo definido por el mercado"}
  ],
  "correcta": "b",
  "explicacion": "Antes la ecuación era: Costo + BE = Precio de Venta (la empresa fijaba el precio). Hoy: BE = Precio de Venta – Costo (el precio lo fijan los clientes). Por lo tanto, la única forma de maximizar el beneficio es DISMINUIR LOS COSTOS, lo que hace al mantenimiento un factor económico y global de la empresa."
},
{
  "id": "q116",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuáles son las 5 funciones básicas del servicio de mantenimiento?",
  "opciones": [
    {"id": "a", "texto": "Planificar, ejecutar, controlar, registrar y mejorar"},
    {"id": "b", "texto": "Reparar, preservar, mantener, mejorar y proyectar"},
    {"id": "c", "texto": "Correctivo, preventivo, predictivo, autónomo y total"},
    {"id": "d", "texto": "Diagnosticar, reparar, reemplazar, prevenir y capacitar"}
  ],
  "correcta": "b",
  "explicacion": "Las 5 funciones básicas son: 1) Reparar (resolver averías con mínimo tiempo y costo), 2) Preservar (conservación e incremento de vida útil: lubricación, limpieza), 3) Mantener (programar intervenciones preventivas), 4) Mejorar (realizar mejoras para no tener que reparar), 5) Proyectar (participar en el diseño de nuevas máquinas - gestión temprana de equipos)."
},
{
  "id": "q117",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "¿Cuál es la DESVENTAJA más importante del mantenimiento PREVENTIVO?",
  "opciones": [
    {"id": "a", "texto": "La falla ocurre sin previo aviso, generando interrupción del servicio"},
    {"id": "b", "texto": "Se programan mantenimientos innecesarios: no utiliza la vida útil del elemento al 100% y aumenta costos"},
    {"id": "c", "texto": "Requiere equipos de diagnóstico muy costosos y personal altamente especializado"},
    {"id": "d", "texto": "No puede aplicarse a equipos críticos con altos costos de mantenimiento"}
  ],
  "correcta": "b",
  "explicacion": "La desventaja principal del preventivo es que se programan mantenimientos aunque la pieza todavía no lo necesita (no utiliza la vida útil al 100%), lo que lleva a reducción de disponibilidad y aumento de costos. La opción A es desventaja del CORRECTIVO. La opción C es desventaja del PREDICTIVO. Por eso donde fue posible el preventivo fue reemplazado por el predictivo."
},
{
  "id": "q118",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "El mantenimiento PREDICTIVO se distingue del preventivo porque:",
  "opciones": [
    {"id": "a", "texto": "Se realiza en períodos fijos programados, sin necesidad de monitorear las condiciones del equipo"},
    {"id": "b", "texto": "No depende de un plan sino de las condiciones reales de funcionamiento, detectando cuándo se acerca la falla para intervenir de forma planificada"},
    {"id": "c", "texto": "Solo aplica a equipos de bajo costo de mantenimiento donde la falla no afecta la producción"},
    {"id": "d", "texto": "Es realizado exclusivamente por los operarios del nivel 1, sin intervención de profesionales"}
  ],
  "correcta": "b",
  "explicacion": "El mantenimiento predictivo no depende de un plan periódico sino de las condiciones de funcionamiento de los equipos. Mediante técnicas adecuadas detecta si alguna pieza se está acercando al punto de falla, permitiendo planificar la intervención. Cumple dos objetivos: saber cuándo ocurrirá la falla para evitarla, y alargar al máximo la vida útil de las piezas."
},
{
  "id": "q119",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "relacion",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Relacioná cada tipo de mantenimiento con su descripción correcta.",
  "columna_izq": [
    {"id": "1", "texto": "Mantenimiento correctivo"},
    {"id": "2", "texto": "Mantenimiento preventivo"},
    {"id": "3", "texto": "Mantenimiento predictivo"},
    {"id": "4", "texto": "TPM"}
  ],
  "columna_der": [
    {"id": "x", "texto": "Usar el equipo hasta que falle; no hay programación previa"},
    {"id": "y", "texto": "Revisiones periódicas programadas; sustituye piezas según plan fijo"},
    {"id": "z", "texto": "Monitorea condiciones reales del equipo para planificar intervención justo antes de la falla"},
    {"id": "w", "texto": "Involucra a todos los departamentos; operarios realizan mantenimiento básico de sus equipos"}
  ],
  "correcta": {"1": "x", "2": "y", "3": "z", "4": "w"},
  "explicacion": "Correctivo: basado en el evento/falla. Preventivo: planificado en períodos fijos. Predictivo: basado en condiciones reales de funcionamiento (sin planes fijos). TPM (Mantenimiento Productivo Total): metodología que involucra a toda la organización, con operarios realizando el mantenimiento básico de sus equipos."
},
{
  "id": "q120",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "¿Cuántos PILARES tiene el TPM (Mantenimiento Productivo Total)?",
  "opciones": [
    {"id": "a", "texto": "4 pilares (los mismos que los tipos de mantenimiento)"},
    {"id": "b", "texto": "5 pilares (correspondientes a las 5 'ceros' de las metas)"},
    {"id": "c", "texto": "8 pilares"},
    {"id": "d", "texto": "3 pilares (personas, equipos y seguridad)"}
  ],
  "correcta": "c",
  "explicacion": "El TPM tiene 8 pilares: 1) Mejoras enfocadas, 2) Mantenimiento autónomo, 3) Mantenimiento planificado, 4) Mantenimiento de calidad, 5) Prevención del mantenimiento, 6) Actividades de departamentos administrativos y de apoyo, 7) Formación y adiestramiento, 8) Gestión de seguridad y entorno. Los 3 elementos (personas, equipos, seguridad) son a los que se ENFOCA, no los pilares."
},
{
  "id": "q121",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuáles son las METAS del TPM (las 5 ceros)?",
  "opciones": [
    {"id": "a", "texto": "Cero costos, cero horas extras, cero desperdicios, cero accidentes, cero defectos"},
    {"id": "b", "texto": "Cero paradas no planeadas, cero defectos causados por el equipo, cero pérdidas de velocidad, cero accidentes y mejora de habilidades del personal"},
    {"id": "c", "texto": "Cero correctivo, cero preventivo innecesario, cero tiempo de espera, cero inventario y cero reproceso"},
    {"id": "d", "texto": "Cero fallas, cero quejas de clientes, cero rotación de personal, cero stock y cero sobretiempos"}
  ],
  "correcta": "b",
  "explicacion": "Las metas del TPM son: 1) Cero paradas no planeadas, 2) Cero defectos causados por el equipo, 3) Cero pérdidas de velocidad del equipo, 4) Cero accidentes, y 5) Mejora de habilidades del personal (tanto técnicas como de trabajo en equipo). El enfoque es en las pérdidas causadas por los equipos, no en métricas financieras genéricas."
},
{
  "id": "q122",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuántos niveles de intervención existen en el mantenimiento organizado?",
  "opciones": [
    {"id": "a", "texto": "3 niveles"},
    {"id": "b", "texto": "4 niveles"},
    {"id": "c", "texto": "5 niveles"},
    {"id": "d", "texto": "7 niveles"}
  ],
  "correcta": "c",
  "explicacion": "Existen 5 niveles: 1° Operarios de fabricación (automantenimiento: limpieza, engrases, control básico), 2° Especialistas electromecánicos/electrónicos a pedido del nivel 1, 3° Profesionales del mantenimiento (integración con fabricación), 4° Ingeniería del mantenimiento (especialistas en función global), 5° Mantenimiento contratado (fabricantes y empresas especializadas)."
},
{
  "id": "q123",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El mantenimiento correctivo por 'sustitución de elementos' (cambiar módulos completos) tiene MAYORES costos de mano de obra pero MENORES costos en materiales respecto a la 'reparación propiamente dicha'.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Es al revés. La sustitución de elementos tiene: BAJO costo de MO (por su simplicidad y rapidez) y COSTOS ELEVADOS en materiales y kits stockeados (porque se cambia el módulo completo). La reparación propiamente dicha tiene: ELEVADO costo de MO (desmontaje, ajustes, reconstrucción) y COSTOS BAJOS en material."
},
{
  "id": "q124",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "¿Qué modelo de organización de mantenimiento es adecuado para industrias con UN SOLO PRODUCTO en proceso continuo con altos costos de mantenimiento?",
  "opciones": [
    {"id": "a", "texto": "Mantenimiento dependiendo de la Dirección de Producción (política a corto plazo)"},
    {"id": "b", "texto": "Mantenimiento dependiendo de la Dirección General"},
    {"id": "c", "texto": "Servicio técnico de mantenimiento dependiendo de la Ingeniería de planta"},
    {"id": "d", "texto": "Mantenimiento Total integrado en la Producción (TPM completo)"}
  ],
  "correcta": "b",
  "explicacion": "El modelo donde el servicio de mantenimiento depende de la DIRECCIÓN GENERAL es adecuado para industrias con un solo o pocos productos (proceso continuo) y con costos de mantenimiento significativamente elevados. Este modelo define sus propios métodos, programa y presupuesto, con autonomía respecto a la dirección de producción."
},
{
  "id": "q125",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Por qué se considera necesario un mantenimiento organizado en la industria moderna?",
  "opciones": [
    {"id": "a", "texto": "Solo para reducir costos de mano de obra en producción"},
    {"id": "b", "texto": "Por la creciente automatización, procesos continuos que no permiten horas para reparar, incumplimiento de plazos de entrega y para cumplir legislación de seguridad"},
    {"id": "c", "texto": "Únicamente para gestionar el inventario de repuestos en el almacén"},
    {"id": "d", "texto": "Solo aplica a industrias pesadas con maquinaria muy costosa"}
  ],
  "correcta": "b",
  "explicacion": "Se necesita mantenimiento organizado por: 1) Creciente automatización, 2) Procesos continuos que no dejan horas para reparar, 3) Procesos en cadena donde una avería para todo, 4) Incumplimiento de plazos trae consecuencias económicas, 5) Distribución racional de MO de mantenimiento, 6) Planificación asegura existencia de repuestos, 7) Cumplir legislación y prevenir accidentes."
},
{
  "id": "q126",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "El benchmarking como herramienta de mejora continua tiene 4 pasos. ¿En cuál de ellos se utiliza la matriz FODA?",
  "opciones": [
    {"id": "a", "texto": "Planificación: para identificar los ejes a comparar"},
    {"id": "b", "texto": "Ejecución: para el análisis de diferencias y elaboración de planes de mejora"},
    {"id": "c", "texto": "Seguimiento: para controlar los resultados del ensayo piloto"},
    {"id": "d", "texto": "Evaluación y extensión: para cuantificar el impacto de la mejora"}
  ],
  "correcta": "b",
  "explicacion": "En la etapa de EJECUCIÓN del benchmarking se realiza la recolección y análisis de datos, la determinación de las diferencias más relevantes y la elaboración de un plan de mejoras para cada diferencia. La herramienta sugerida es una matriz FODA para cada diferencia encontrada. El seguimiento usa un proceso piloto."
},
{
  "id": "q127",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "verdadero_falso",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "El mantenimiento industrial incluye ÚNICAMENTE el mantenimiento de máquinas productivas, no de instalaciones como iluminación, redes informáticas o pisos.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. El mantenimiento no solo debe mantener las máquinas sino también todas las instalaciones generales: iluminación, redes de computación, sistemas de energía eléctrica, aire comprimido, agua, aire acondicionado, calles internas, pisos, depósitos, etc. Además debe coordinar con RRHH un plan de capacitación continua del personal."
},
{
  "id": "q128",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es el pilar del TPM que consiste en 'volver a integrar el trabajo del operario con el de mantenimiento'?",
  "opciones": [
    {"id": "a", "texto": "Mejoras enfocadas"},
    {"id": "b", "texto": "Mantenimiento autónomo"},
    {"id": "c", "texto": "Mantenimiento planificado"},
    {"id": "d", "texto": "Prevención del mantenimiento"}
  ],
  "correcta": "b",
  "explicacion": "El mantenimiento autónomo (pilar 2 del TPM) consiste en volver a integrar el trabajo del operario con el de mantenimiento, para lograr disminuir desperdicios. El operario queda preparado para realizar cambios de formatos o mantenimientos básicos. Esto es la base del concepto 'mantenimiento es tarea de todos'."
},
{
  "id": "q129",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "El benchmarking se define como herramienta de ayuda para la mejora continua. ¿Qué proceso de mejora se aplica típicamente en su implementación?",
  "opciones": [
    {"id": "a", "texto": "Las 5S (Seiri, Seiton, Seiso, Seiketsu, Shitsuke)"},
    {"id": "b", "texto": "La rueda de Deming (PDCA: Plan, Do, Check, Act)"},
    {"id": "c", "texto": "El diagrama de Ishikawa (causa-efecto)"},
    {"id": "d", "texto": "El método de los 5 porqués (5 Why)"}
  ],
  "correcta": "b",
  "explicacion": "Como el benchmarking es un proceso de mejora continua, es típico aplicar la rueda de Deming (PDCA: Plan-Do-Check-Act). Los 4 pasos del benchmarking (Planificación, Ejecución, Seguimiento, Evaluación y extensión) se alinean con el ciclo PDCA de mejora continua."
},
{
  "id": "q130",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿En qué consiste el pilar de 'Prevención del mantenimiento' del TPM?",
  "opciones": [
    {"id": "a", "texto": "Realizar el mantenimiento preventivo planificado para todos los equipos"},
    {"id": "b", "texto": "Planificar e investigar sobre nuevas máquinas, diseñar/rediseñar procesos, verificar nuevos proyectos y evaluar test de operaciones"},
    {"id": "c", "texto": "Prevenir accidentes durante las tareas de mantenimiento con EPP y capacitación"},
    {"id": "d", "texto": "Evitar que el mantenimiento correctivo reactive la producción fuera de horario"}
  ],
  "correcta": "b",
  "explicacion": "La prevención del mantenimiento (pilar 5 del TPM) consiste en: planificar e investigar sobre nuevas máquinas a utilizar en la organización, diseñar o rediseñar procesos, verificar nuevos proyectos, realizar y evaluar test de operaciones, y ver la instalación y el arranque. Es una visión prospectiva que actúa antes de incorporar nuevos equipos."
},
{
  "id": "q131",
  "tema": "Unidad 8: Organización del Mantenimiento",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El mantenimiento PREDICTIVO tiene la ventaja de que puede aplicarse a todas las variables y elementos de una máquina, ya que los instrumentos modernos permiten medir cualquier parámetro.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Una desventaja del mantenimiento predictivo es que NO todas las variables ni todos los elementos son mensurables. Además, requiere altos costos de inversión (equipos especiales y entrenamiento) y necesita un período inicial para desarrollar la tendencia de las señales y definir los umbrales de alarma."
},

# ─────────────────────────────────────────────
# UNIDAD 9: MANIPULACIÓN DE MATERIALES (12 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q132",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuántos principios básicos del manejo de materiales existen según el material?",
  "opciones": [
    {"id": "a", "texto": "5 principios fundamentales"},
    {"id": "b", "texto": "10 principios básicos"},
    {"id": "c", "texto": "15 principios de coordinación"},
    {"id": "d", "texto": "27 principios fundamentales"}
  ],
  "correcta": "b",
  "explicacion": "Existen 10 principios básicos del manejo de materiales: Planeación, Estandarización, Trabajo, Ergonomía, Carga unitaria, Utilización del espacio, Sistema, Automatización, Ambiental, y Costo del ciclo de la vida. Adicionalmente hay 27 principios fundamentales más específicos de manipulación. Confundir los 10 con los 27 es un error frecuente."
},
{
  "id": "q133",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "¿Cuáles son los 3 grupos en que se clasifican los aparatos de manipulación según su 'movilidad relativa'?",
  "opciones": [
    {"id": "a", "texto": "Mecánicos, neumáticos e hidráulicos"},
    {"id": "b", "texto": "Fijos, limitados y libres"},
    {"id": "c", "texto": "Manuales, semiauto y automáticos"},
    {"id": "d", "texto": "Elevadores, transportadores y grúas"}
  ],
  "correcta": "b",
  "explicacion": "Por movilidad relativa los aparatos se clasifican en: Fijos (solo trabajan dentro de los límites de su instalación), Limitados (pueden desplazarse en un área limitada) y Libres (pueden moverse libremente e ir a todas partes). Las opciones A y D son clasificaciones por tipo/tecnología, no por movilidad."
},
{
  "id": "q134",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es el objetivo fundamental de la manipulación de materiales?",
  "opciones": [
    {"id": "a", "texto": "Maximizar la velocidad de transporte interno para reducir el tiempo de ciclo"},
    {"id": "b", "texto": "Transportar los materiales de un punto a otro sin retroceder, con mínimo de transbordos, entregándolos en los lugares apropiados para evitar atascos y manipulaciones innecesarias"},
    {"id": "c", "texto": "Reemplazar la mano de obra directa con sistemas automatizados en todas las etapas del proceso"},
    {"id": "d", "texto": "Asegurar el inventario de seguridad en todos los puntos del proceso para evitar paradas"}
  ],
  "correcta": "b",
  "explicacion": "El objetivo es transportar los materiales de un punto a otro sin retroceder, con un mínimo de transbordos, entregándolos en los lugares de trabajo o centros de producción apropiados con el fin de evitar atascos, retrasos y manipulaciones innecesarias. No se trata de velocidad máxima sino de flujo eficiente."
},
{
  "id": "q135",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "Un autoelevador hidráulico es un ejemplo de aparato de manipulación 'neumático' porque usa aire comprimido para levantar cargas.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Los autoelevadores hidráulicos son aparatos HIDRÁULICOS (usan aceite a presión o fluidos hidráulicos para mover o levantar cargas pesadas con gran precisión). Los neumáticos usan aire comprimido y son ideales para movimientos rápidos y ligeros (ej: cilindros neumáticos en líneas de montaje, tubos para papeles en bancos)."
},
{
  "id": "q136",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuál es el medio más económico para bajar materiales en una fábrica?",
  "opciones": [
    {"id": "a", "texto": "Cintas transportadoras motorizadas"},
    {"id": "b", "texto": "Rampas (rectas o espiraladas)"},
    {"id": "c", "texto": "Autoelevadores con conductor"},
    {"id": "d", "texto": "Grúas puente montadas en el techo"}
  ],
  "correcta": "b",
  "explicacion": "Las rampas son el medio más económico para bajar materiales: son de construcción sencilla, en condiciones normales su costo de conservación es casi nulo, y utilizan la fuerza de la gravedad (combinada con la centrífuga en el caso de rampas espiraladas). Pueden ser rectas (distancias cortas) o espiraladas (distancias largas o con limitaciones de espacio)."
},
{
  "id": "q137",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "Al seleccionar equipos de manipulación, ¿cuál es la prioridad entre el costo inicial y el costo total del ciclo de vida?",
  "opciones": [
    {"id": "a", "texto": "El costo inicial es la prioridad porque determina la inversión de capital necesaria"},
    {"id": "b", "texto": "La compra debe realizarse teniendo en cuenta las economías totales del ciclo de vida, no solo el costo inicial"},
    {"id": "c", "texto": "El costo de mantenimiento es el único factor a considerar en la selección de equipos"},
    {"id": "d", "texto": "El costo inicial y el de operación siempre son equivalentes para equipos del mismo tipo"}
  ],
  "correcta": "b",
  "explicacion": "La compra de aparatos/herramientas debe realizarse teniendo en cuenta las economías TOTALES del ciclo de vida, no solo el costo inicial. Un equipo más caro inicialmente puede ser más económico a largo plazo si tiene menores costos operativos, menor mantenimiento o mayor vida útil. El 'mínimo costo global de manipulación' es el factor clave."
},
{
  "id": "q138",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuáles son las variables relevantes en la decisión de manejo de materiales?",
  "opciones": [
    {"id": "a", "texto": "Solo el tipo de material (granel o envasado) y la distancia de recorrido"},
    {"id": "b", "texto": "Materiales, movimiento a realizar, recorrido, velocidad requerida, supervisión, frecuencia, flexibilidad, capacidad de carga, confiabilidad, espacio, energía, seguridad, vida útil e inversión"},
    {"id": "c", "texto": "Exclusivamente el presupuesto disponible y la disponibilidad de proveedores locales"},
    {"id": "d", "texto": "Solo el peso de los materiales y la distancia horizontal a recorrer"}
  ],
  "correcta": "b",
  "explicacion": "Las variables relevantes incluyen: tipo de material (granel/envasado, perecedero), movimiento (horizontal/vertical/combinado), recorrido (fijo/variable), velocidad requerida, supervisión requerida (estricta/ligera/automática), frecuencia de movimientos, flexibilidad, capacidad de carga, confiabilidad, espacio requerido, energía, seguridad, vida útil e inversión y costos de operación."
},
{
  "id": "q139",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "verdadero_falso",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "La manipulación de materiales siempre agrega valor al producto porque facilita que los materiales lleguen donde deben estar en el momento correcto.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. La manipulación de materiales NO agrega valor al producto (igual que el manejo de materiales en el factor de lay out). Solo agrega COSTO. Por eso siempre se debe tender a eliminar la manipulación, y si no se puede, hacerla por medios mecánicos en lugar de manuales, y automatizar la manipulación rutinaria para reducir costos."
},
{
  "id": "q140",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "¿En cuántas formas distintas pueden clasificarse los aparatos de manipulación?",
  "opciones": [
    {"id": "a", "texto": "3 formas (por clase, por servicio y por material)"},
    {"id": "b", "texto": "4 formas"},
    {"id": "c", "texto": "5 formas"},
    {"id": "d", "texto": "7 formas"}
  ],
  "correcta": "c",
  "explicacion": "Existen 5 formas de clasificar los aparatos de manipulación: 1) Por clase de aparato (grúas, transportadores, elevadores, carretillas), 2) Por naturaleza del servicio (elevar, transportar), 3) Por naturaleza del material (suelto, a granel, piezas, cajas), 4) Por sector de actividad (minería, fabricación, construcción), 5) Por movilidad relativa (fijos, limitados, libres)."
},
{
  "id": "q141",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Los AGV (Automated Guided Vehicles) son un ejemplo de aparato de manipulación:",
  "opciones": [
    {"id": "a", "texto": "Neumático (guiado por aire comprimido)"},
    {"id": "b", "texto": "Automotor (motorizado autónomo, diseñado para transporte eficiente)"},
    {"id": "c", "texto": "De sistema de carriles (guiado sobre rieles fijos)"},
    {"id": "d", "texto": "Portátil (fácil traslado, operado manualmente o con baterías)"}
  ],
  "correcta": "b",
  "explicacion": "Los AGV (vehículos de guía automática) son ejemplos de aparatos AUTOMOTORES: equipos motorizados autónomos o con conductor, diseñados para transporte eficiente en distancias internas o externas. La categoría incluye también autoelevadores a combustión o eléctricos y tractores de arrastre."
},
{
  "id": "q142",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuáles son los 3 interrogantes iniciales para un estudio de manejo de materiales (según Tompkins)?",
  "opciones": [
    {"id": "a", "texto": "¿Qué costo tiene? ¿Cuánto pesa? ¿Qué distancia debe recorrer?"},
    {"id": "b", "texto": "¿Qué material transportar? ¿En qué momento? ¿Desde dónde y hasta dónde?"},
    {"id": "c", "texto": "¿Quién lo maneja? ¿Cuándo se compra el equipo? ¿Cómo se mantiene?"},
    {"id": "d", "texto": "¿Cuánta energía consume? ¿Cuánto espacio ocupa? ¿Cuántos operarios requiere?"}
  ],
  "correcta": "b",
  "explicacion": "Los 3 interrogantes iniciales son: ¿Qué material transportar (o personas)? ¿En qué momento? ¿Desde dónde y hasta dónde? Las primeras dos surgen del proceso diseñado y la tercera del layout. Definir CÓMO hacerlo es el problema central de la decisión. Estas preguntas evidencian la interrelación entre manejo de materiales, proceso y layout."
},
{
  "id": "q143",
  "tema": "Unidad 9: Manipulación de Materiales",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "El principio de 'ergonomía' en el manejo de materiales establece que:",
  "opciones": [
    {"id": "a", "texto": "Se debe minimizar el costo de los equipos priorizando los de menor precio"},
    {"id": "b", "texto": "Deben reconocerse las capacidades y limitaciones humanas por encima de todo, y diseñar operaciones seguras y efectivas"},
    {"id": "c", "texto": "El trabajo de manejo de materiales debe minimizarse sin sacrificar la productividad"},
    {"id": "d", "texto": "El impacto ambiental y el consumo de energía deben considerarse al seleccionar equipos"}
  ],
  "correcta": "b",
  "explicacion": "El principio de ergonomía establece que deben reconocerse las capacidades y las limitaciones humanas POR ENCIMA DE TODO, y diseñar operaciones seguras y efectivas. El principio de 'trabajo' es el que dice minimizar el trabajo sin sacrificar productividad. El 'ambiental' considera el impacto en el medioambiente."
},

# ─────────────────────────────────────────────
# UNIDAD 10: ORGANIZACIÓN DE LA MANUFACTURA (12 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q144",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué es el planeamiento de la producción?",
  "opciones": [
    {"id": "a", "texto": "El diseño del proceso productivo y la selección de maquinaria para una nueva planta"},
    {"id": "b", "texto": "Un conjunto de planes sistemáticos y acciones para dirigir la producción de bienes/servicios, definiendo cantidades para un horizonte temporal generalmente anual"},
    {"id": "c", "texto": "La gestión del inventario de materia prima para evitar quiebres de stock"},
    {"id": "d", "texto": "El control de calidad de los productos terminados antes de su despacho"}
  ],
  "correcta": "b",
  "explicacion": "El planeamiento de la producción es un conjunto de planes sistemáticos y acciones para dirigir la producción y los recursos, definiendo cantidades para un horizonte generalmente anual dividido en meses. Controla 3 elementos: hombre, máquina y materiales, para producir la cantidad correcta, con calidad adecuada y en el tiempo preciso."
},
{
  "id": "q145",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es la diferencia entre inventarios con 'demanda independiente' y 'demanda dependiente'?",
  "opciones": [
    {"id": "a", "texto": "Independiente = solo para materias primas; Dependiente = solo para productos terminados"},
    {"id": "b", "texto": "Independiente = influenciado por condiciones del mercado externo (ej: productos finales); Dependiente = deriva de decisiones internas de planeamiento (ej: componentes y subconjuntos)"},
    {"id": "c", "texto": "Independiente = se gestiona con MRP; Dependiente = se gestiona con lote económico"},
    {"id": "d", "texto": "No hay diferencia práctica; ambos se gestionan con el punto de reorden"}
  ],
  "correcta": "b",
  "explicacion": "Demanda independiente: influenciada exclusivamente por condiciones del mercado u otros factores externos. Se gestiona con lote económico óptimo y punto de reorden. Demanda dependiente: deriva de decisiones previas de planeamiento (si decido fabricar X unidades del producto final, necesito Y componentes). Se gestiona con MRP (programa de requerimiento de materiales)."
},
{
  "id": "q146",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El sistema MRP (Material Requirements Planning) para inventarios de demanda dependiente establece que:",
  "opciones": [
    {"id": "a", "texto": "Debe producirse unidades solo cuando se necesitan, sin inventario de seguridad y sin previsión para otros pedidos"},
    {"id": "b", "texto": "Se debe mantener un inventario de seguridad alto para garantizar el cumplimiento de los pedidos"},
    {"id": "c", "texto": "El tamaño del lote debe maximizarse para aprovechar economías de escala"},
    {"id": "d", "texto": "La producción debe planificarse en función de la demanda histórica, no de las decisiones futuras"}
  ],
  "correcta": "a",
  "explicacion": "El MRP establece que debe producirse unidades solamente cuando se necesitan, sin inventario de seguridad y sin previsión para otros pedidos. Es el sistema clásico para inventarios con demanda dependiente. Esto se alinea con la filosofía JIT: producir lo justo cuando se necesita, minimizando el capital inmovilizado en inventarios."
},
{
  "id": "q147",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "El control de la producción compara la actuación real con la prevista. ¿Cuáles son los 2 aspectos que agrupa el control de producción?",
  "opciones": [
    {"id": "a", "texto": "Control de procesos y control de inventarios"},
    {"id": "b", "texto": "Control de las cantidades (seguimiento, cuantitativo, inventarios, costos) y control de la calidad"},
    {"id": "c", "texto": "Control de eficiencia y control de productividad"},
    {"id": "d", "texto": "Control operacional y control estratégico"}
  ],
  "correcta": "b",
  "explicacion": "El control de producción agrupa dos aspectos: 1) Las cantidades (que incluye: seguimiento permanente de la operación, control cuantitativo de producción, control de inventarios con método ABC/Pareto, y control de costos), y 2) La calidad (control de calidad). El control es un proceso dinámico continuo que permite encaminarse hacia los objetivos trazados."
},
{
  "id": "q148",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es el 'lote económico óptimo' en la gestión de inventarios de demanda independiente?",
  "opciones": [
    {"id": "a", "texto": "El lote más grande posible para minimizar el costo por unidad producida"},
    {"id": "b", "texto": "El tamaño de cada pedido que hace mínima la función del costo total (costo de pedido + costo de almacenamiento)"},
    {"id": "c", "texto": "El lote que maximiza el tiempo entre pedidos para reducir la carga administrativa"},
    {"id": "d", "texto": "El lote igual a la demanda mensual promedio para facilitar la planificación"}
  ],
  "correcta": "b",
  "explicacion": "El lote económico óptimo es el tamaño de cada pedido que hace MÍNIMA la función del costo total, que combina: el costo de pedido (disminuye con lotes grandes) y el costo de almacenamiento/tenencia (aumenta con lotes grandes). El óptimo está donde ambos costos se equilibran, minimizando el costo total."
},
{
  "id": "q149",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "Los inventarios siempre representan un costo innecesario para la empresa, por lo que la política óptima es siempre minimizarlos al máximo posible.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Los inventarios cumplen una función de DESACOPLE en la secuencia compras-producción-distribución, permitiendo que cada etapa funcione con mayor independencia. Sin embargo, esto no justifica su creación sin análisis, ya que el capital inmovilizado genera costos. La política óptima es el BALANCE entre los beneficios de mantenerlos y los costos que originan."
},
{
  "id": "q150",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Para qué sirve el método ABC (Pareto) en el control de inventarios?",
  "opciones": [
    {"id": "a", "texto": "Para ordenar alfabéticamente los artículos del inventario"},
    {"id": "b", "texto": "Para tomar en cuenta la dispar importancia relativa de los artículos y enfatizar el control en los de mayor valor"},
    {"id": "c", "texto": "Para calcular el lote económico de cada artículo del inventario"},
    {"id": "d", "texto": "Para determinar el punto de reorden de los artículos de mayor rotación"}
  ],
  "correcta": "b",
  "explicacion": "El método ABC o Pareto clasifica los artículos del inventario según su importancia relativa (valor × consumo), permitiendo enfatizar el control en aquellos de mayor impacto económico. Típicamente: A = 20% de artículos representan el 80% del valor total (control exhaustivo); B = artículos intermedios; C = muchos artículos de bajo valor relativo."
},
{
  "id": "q151",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "¿Cuáles son los objetivos del planeamiento de la producción?",
  "opciones": [
    {"id": "a", "texto": "Solo maximizar ganancias y minimizar costos de producción"},
    {"id": "b", "texto": "Aumentar productividad, coordinar demanda y oferta, maximizar ganancias/minimizar costos, mantener flexibilidad, minimizar stock inmovilizado y maximizar el uso de recursos"},
    {"id": "c", "texto": "Garantizar cero defectos, cero accidentes y cero paradas no planificadas"},
    {"id": "d", "texto": "Diseñar el proceso productivo y seleccionar la tecnología más adecuada"}
  ],
  "correcta": "b",
  "explicacion": "Los objetivos del planeamiento de la producción son: aumentar la productividad, coordinar demanda y oferta, maximizar ganancias y minimizar costos, mantener flexibilidad, minimizar el stock inmovilizado, y maximizar el uso de los recursos. Es un conjunto equilibrado que busca eficiencia operativa y financiera simultáneamente."
},
{
  "id": "q152",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Qué función cumplen los inventarios como 'desacople'?",
  "opciones": [
    {"id": "a", "texto": "Permiten que el proceso productivo opere sin interrupciones eliminando la necesidad de planificación"},
    {"id": "b", "texto": "Equilibran actividades que operan a distinto ritmo: ventas y producción, producción y compras, distintas etapas del proceso"},
    {"id": "c", "texto": "Reemplazan la necesidad de pronósticos de demanda en la empresa"},
    {"id": "d", "texto": "Permiten prescindir de los proveedores locales trabajando con stock de largo plazo"}
  ],
  "correcta": "b",
  "explicacion": "Los inventarios cumplen la función de 'desacople': equilibran actividades que operan a distinto ritmo (ventas y producción, producción y compras, distintas etapas del proceso productivo). Posibilitan que cada actividad funcione con mayor independencia. Sin embargo, esto no justifica su creación arbitraria, ya que el capital para formarlos tiene un costo."
},
{
  "id": "q153",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuáles son las 2 entradas al sistema de control de producción?",
  "opciones": [
    {"id": "a", "texto": "Los pedidos de clientes y las órdenes de producción"},
    {"id": "b", "texto": "Las decisiones y los planes (marco de referencia) y la información sobre la realidad"},
    {"id": "c", "texto": "Los estándares de calidad y los tiempos estándar de producción"},
    {"id": "d", "texto": "El inventario inicial y la capacidad instalada de producción"}
  ],
  "correcta": "b",
  "explicacion": "Las 2 entradas al sistema de control de producción son: 1) Las decisiones y los planes (junto con sus metas), que sirven como marco de referencia contra el cual se coteja la realidad, y 2) La información sobre la realidad. El control compara estas dos entradas, detecta desvíos y genera acciones correctivas o revisiones de planes."
},
{
  "id": "q154",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "verdadero_falso",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "El 'punto de reorden' indica cuántas unidades se deben pedir en cada orden de compra para minimizar el costo total de inventario.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. El punto de reorden indica el MOMENTO en que se debe realizar el pedido (cuándo ordenar), no la cantidad. Indica la modalidad temporal de las decisiones: cuándo ordenar. La CANTIDAD a pedir es determinada por el lote económico óptimo. Son dos decisiones complementarias del sistema de gestión de inventarios de demanda independiente."
},
{
  "id": "q155",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "relacion",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "Relacioná cada subproceso del control de producción (aspecto 'cantidades') con su descripción.",
  "columna_izq": [
    {"id": "1", "texto": "Seguimiento"},
    {"id": "2", "texto": "Control cuantitativo"},
    {"id": "3", "texto": "Control de inventarios"},
    {"id": "4", "texto": "Control de costos"}
  ],
  "columna_der": [
    {"id": "x", "texto": "Vigilancia permanente de la operación para detectar desvíos y tomar medidas inmediatas"},
    {"id": "y", "texto": "Evaluación de cantidades producidas y recursos aplicados"},
    {"id": "z", "texto": "Gestión por importancia relativa de artículos (método ABC o Pareto)"},
    {"id": "w", "texto": "Identificación de costos ocultos e ineficiencias para su reducción"}
  ],
  "correcta": {"1": "x", "2": "y", "3": "z", "4": "w"},
  "explicacion": "Seguimiento: vigilancia permanente para ajuste inmediato. Control cuantitativo: evaluación de cantidades y recursos. Control de inventarios: gestión por importancia relativa con ABC/Pareto para enfatizar control en artículos de mayor valor. Control de costos: identificar costos ocultos e ineficiencias."
},
{
  "id": "q156",
  "tema": "Unidad 10: Organización de la Manufactura",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿En qué consiste el 'seguimiento' como subproceso del control de cantidades en producción?",
  "opciones": [
    {"id": "a", "texto": "En registrar el historial de producción de cada máquina para el mantenimiento preventivo"},
    {"id": "b", "texto": "En la vigilancia permanente de la operación del proceso para asegurarse que su marcha coincide con lo previsto y tomar medidas de ajuste en forma inmediata"},
    {"id": "c", "texto": "En hacer seguimiento de los pedidos de compra a proveedores para asegurar el abastecimiento"},
    {"id": "d", "texto": "En rastrear el movimiento de cada unidad producida desde el inicio hasta la entrega al cliente"}
  ],
  "correcta": "b",
  "explicacion": "El seguimiento consiste en la vigilancia PERMANENTE de la operación del proceso, a fin de asegurarse de que su marcha coincide con lo que se ha previsto. Su objeto es tomar medidas de ajuste de forma inmediata ante cualquier desvío. Es el subproceso de control más dinámico y operacional dentro del control de las cantidades."
},
]

print(json.dumps(preguntas, ensure_ascii=False, indent=2))
