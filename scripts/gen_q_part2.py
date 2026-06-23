"""Genera preguntas para Unidades 4-6 de Organización Industrial."""
import json

preguntas = [
# ─────────────────────────────────────────────
# UNIDAD 4: LAY OUT (18 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q055",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuál es el tipo de lay out adecuado para la producción intermitente (por lotes, a pedido del cliente)?",
  "opciones": [
    {"id": "a", "texto": "Lay out por producto (línea de producción)"},
    {"id": "b", "texto": "Lay out por proceso o funcional"},
    {"id": "c", "texto": "Lay out de posición fija"},
    {"id": "d", "texto": "Lay out celular en U"}
  ],
  "correcta": "b",
  "explicacion": "El lay out por PROCESO o funcional agrupa máquinas afines en un mismo sector. Es adecuado para producción intermitente: gran variedad de productos, poca estandarización, reducido volumen por orden, maquinaria universal/versátil. El lay out por producto es para producción continua; el celular es para familias de productos."
},
{
  "id": "q056",
  "tema": "Unidad 4: Layout",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "Una de las ventajas del lay out por PROCESO es que las paradas en un equipo NO detienen toda la producción, a diferencia del lay out por producto.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "v",
  "explicacion": "Verdadero. En el lay out por proceso, una parada mecánica no detiene toda la producción (salvo detenciones prolongadas), porque hay otros equipos similares en el mismo sector. En el lay out por producto (línea continua), una parada en cualquier punto detiene toda la línea, generando pérdidas de producción."
},
{
  "id": "q057",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuáles son los 'síntomas de una mala distribución' que indican que el lay out debe rediseñarse?",
  "opciones": [
    {"id": "a", "texto": "Baja rotación de personal, alta automatización y buena iluminación"},
    {"id": "b", "texto": "Congestión de materiales, cantidades excesivas de stocks intermedios, largos recorridos y tensión de operarios"},
    {"id": "c", "texto": "Exceso de inventario de producto terminado y bajo stock de materias primas"},
    {"id": "d", "texto": "Maquinaria antigua, personal sin capacitación y falta de mantenimiento preventivo"}
  ],
  "correcta": "b",
  "explicacion": "Los síntomas de mala distribución incluyen: congestión de materiales o conjuntos, cantidades excesivas de stocks intermedios, utilización deficiente del espacio, largos recorridos, estancamiento en puestos similares, excesiva manipulación de operarios calificados, tensión física o mental, y dificultades para el control efectivo."
},
{
  "id": "q058",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "El lay out celular se describe como adecuado para JIT. ¿Cuál de las siguientes afirmaciones sobre sus ventajas es INCORRECTA?",
  "opciones": [
    {"id": "a", "texto": "Reduce el tiempo de ciclo respecto al tipo funcional"},
    {"id": "b", "texto": "Elimina stocks intermedios y transportes innecesarios"},
    {"id": "c", "texto": "Requiere menor inversión inicial que el lay out por proceso porque evita la duplicación de equipos"},
    {"id": "d", "texto": "Mejora el aprovechamiento del recurso humano"}
  ],
  "correcta": "c",
  "explicacion": "La opción incorrecta es C. La ventaja de 'menor inversión por evitar duplicación de equipos' pertenece al lay out POR PROCESO, no al celular. Las ventajas del celular son: mejora del flujo, optimización del espacio, reducción de inventarios en proceso, mejor uso del RRHH, disminución de transporte y mejora del mantenimiento."
},
{
  "id": "q059",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "El lay out de posición fija se aplica cuando:",
  "opciones": [
    {"id": "a", "texto": "El producto es altamente estandarizado y se produce en grandes volúmenes continuamente"},
    {"id": "b", "texto": "La producción es única, de magnitud importante (obra o proyecto), y los recursos convergen hacia el producto"},
    {"id": "c", "texto": "Hay gran variedad de productos a pedido y se usan máquinas universales agrupadas por tipo"},
    {"id": "d", "texto": "Se fabrican familias de productos con células en forma de U"}
  ],
  "correcta": "b",
  "explicacion": "El lay out de posición fija aplica cuando: la producción es única (o pocas veces), son obras de magnitud (barco, trasplante de órgano, edificio), los equipos y MO se contratan cuando se necesitan y se distribuyen convergiendo hacia el producto/servicio estático. No tiene inventarios en proceso ni líneas permanentes."
},
{
  "id": "q060",
  "tema": "Unidad 4: Layout",
  "tipo": "relacion",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Relacioná cada tipo de lay out con el tipo de producción al que corresponde.",
  "columna_izq": [
    {"id": "1", "texto": "Lay out por producto"},
    {"id": "2", "texto": "Lay out por proceso"},
    {"id": "3", "texto": "Lay out celular"},
    {"id": "4", "texto": "Lay out de posición fija"}
  ],
  "columna_der": [
    {"id": "x", "texto": "Producción continua (estandarizada, alto volumen)"},
    {"id": "y", "texto": "Producción intermitente (por lotes, a pedido)"},
    {"id": "z", "texto": "Producción por montaje (familias de productos, JIT)"},
    {"id": "w", "texto": "Producción por proyecto (único, recursos convergen)"}
  ],
  "correcta": {"1": "x", "2": "y", "3": "z", "4": "w"},
  "explicacion": "Por producto = continua. Por proceso = intermitente (lotes, pedido). Celular = montaje de familias de productos con enfoque JIT. Posición fija = proyecto único donde el producto no se mueve y los recursos van a él."
},
{
  "id": "q061",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuántos son los 'factores del lay out' que deben considerarse en el diseño?",
  "opciones": [
    {"id": "a", "texto": "5 factores"},
    {"id": "b", "texto": "6 factores"},
    {"id": "c", "texto": "8 factores"},
    {"id": "d", "texto": "10 factores"}
  ],
  "correcta": "c",
  "explicacion": "Los 8 factores del lay out son: 1) Materiales, 2) Maquinaria, 3) Personal, 4) Manejo de materiales, 5) Almacenamiento, 6) Edificio, 7) Servicios y 8) Cambios. Son notorias las conexiones entre ellos, por lo que en muchas ocasiones debe tenerse presente más de uno a la vez."
},
{
  "id": "q062",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El factor 'almacenamiento' en el diseño del lay out establece que la espera de materiales SIEMPRE debe evitarse porque genera costos. ¿Esto es correcto?",
  "opciones": [
    {"id": "a", "texto": "Sí, la espera siempre es un costo que debe eliminarse en cualquier caso"},
    {"id": "b", "texto": "No, la espera no siempre supone un costo a evitar: puede proveer una economía superior (ej: proteger la producción frente a demora de entregas)"},
    {"id": "c", "texto": "Sí, pero solo aplica a materias primas; el producto terminado puede esperar sin costo"},
    {"id": "d", "texto": "No, pero solo si la espera es menor a 24 horas en procesos continuos"}
  ],
  "correcta": "b",
  "explicacion": "La espera no siempre supone un costo a evitar: puede proveer una economía superior. Ejemplo: un stock de seguridad protege la producción frente a demoras en entregas programadas. Si el criterio es producir 'lotes de tamaño económico', los espacios para materiales en espera son necesarios y justificados."
},
{
  "id": "q063",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "¿Qué favorece la construcción de la planta en una SOLA planta (planta baja) en lugar de múltiples pisos?",
  "opciones": [
    {"id": "a", "texto": "Bajo costo del terreno, mayor flexibilidad para ampliaciones y cuando hay maquinaria o productos muy pesados"},
    {"id": "b", "texto": "Alto precio del terreno, necesidad de aprovechar la altura disponible y productos livianos"},
    {"id": "c", "texto": "Cuando la producción es intermitente y requiere gran variedad de equipos universales"},
    {"id": "d", "texto": "Cuando se necesita climatización centralizada y tuberías complejas de servicios"}
  ],
  "correcta": "a",
  "explicacion": "Favorecen la construcción en una sola planta: bajo costo del terreno, disponibilidad de terreno para ampliaciones, menos tiempo para construir, menor pérdida de superficie (sin escaleras, ascensores), mayor flexibilidad para cambios, y cuando hay cargas elevadas por máquinas o productos muy pesados."
},
{
  "id": "q064",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "El 'lay out aritmético' consiste en:",
  "opciones": [
    {"id": "a", "texto": "El diseño geométrico de la disposición física de los sectores en el plano"},
    {"id": "b", "texto": "El cálculo de los metros cuadrados totales necesarios para todas las estaciones, oficinas, servicios y pasillos"},
    {"id": "c", "texto": "La evaluación económica comparativa entre distintas alternativas de lay out"},
    {"id": "d", "texto": "La determinación matemática del flujo óptimo de materiales entre estaciones"}
  ],
  "correcta": "b",
  "explicacion": "El lay out aritmético (paso 4 de la metodología) implica calcular los metros cuadrados totales necesarios no solo para cada estación de trabajo, sino también para oficinas, servicios auxiliares, pasillos y depósitos. Su objetivo es dimensionar correctamente el espacio físico de la planta para el diseño del edificio o redistribución."
},
{
  "id": "q065",
  "tema": "Unidad 4: Layout",
  "tipo": "verdadero_falso",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "El factor 'manejo de materiales' en el lay out es considerado una operación productiva porque determina la eficiencia del flujo entre estaciones de trabajo.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. El manejo de materiales NO es una operación productiva: no añade ningún valor al producto. Solo agrega costo. Por eso, el factor manejo de materiales en el diseño del lay out busca minimizarlo, combinar su realización con otras operaciones cuando sea posible, y tender a eliminar movimientos innecesarios y antieconómicos."
},
{
  "id": "q066",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "El factor 'servicios' del lay out incluye vías de acceso, protección contra incendios y control de calidad. ¿Qué porcentaje aproximado del espacio suele estar dedicado a servicios auxiliares?",
  "opciones": [
    {"id": "a", "texto": "Aproximadamente un tercio (33%) de cada planta o departamento"},
    {"id": "b", "texto": "Aproximadamente un quinto (20%) de cada planta o departamento"},
    {"id": "c", "texto": "Aproximadamente la mitad (50%) de cada planta o departamento"},
    {"id": "d", "texto": "Depende exclusivamente del tipo de proceso (continuo vs. intermitente)"}
  ],
  "correcta": "a",
  "explicacion": "Aproximadamente un tercio de cada planta o departamento suele estar dedicado a los servicios auxiliares. Esto suele sorprender y es visto como 'gasto innecesario', pero los servicios permiten y facilitan la actividad principal: mantenimiento, control de calidad, seguridad, primeros auxilios, supervisión, etc."
},
{
  "id": "q067",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál de los siguientes elementos debe considerarse en la 'enumeración y configuración de estaciones de trabajo' al diseñar un lay out?",
  "opciones": [
    {"id": "a", "texto": "Solo la máquina y el operario que la atiende"},
    {"id": "b", "texto": "La máquina, el/los operarios, el espacio para MP entrante/saliente, lugar para herramientas y espacio adicional para movilidad/seguridad/mantenimiento"},
    {"id": "c", "texto": "La máquina, el costo de instalación y el proveedor del equipo"},
    {"id": "d", "texto": "El volumen de producción esperado y el precio de venta del producto"}
  ],
  "correcta": "b",
  "explicacion": "Una estación de trabajo incluye: la máquina (o unidad de prestación de servicio), el/los operarios, el espacio para materia prima entrante y saliente (o para clientes si es servicio), lugar para herramientas/instrumentos/dispositivos, y espacio adicional para movilidad, seguridad, tareas de mantenimiento y limpieza."
},
{
  "id": "q068",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué requisito es necesario para que el lay out por producto (línea) sea eficiente?",
  "opciones": [
    {"id": "a", "texto": "Gran variedad de productos y maquinaria universal"},
    {"id": "b", "texto": "Productos estandarizados, grandes volúmenes y demanda previsiblemente sostenida"},
    {"id": "c", "texto": "Producción a pedido con bajo volumen y alta personalización"},
    {"id": "d", "texto": "Operarios altamente calificados y supervisión intensiva"}
  ],
  "correcta": "b",
  "explicacion": "Para que el lay out por producto sea eficiente se requiere: productos estandarizados, volúmenes de producción grandes (que justifiquen duplicación de equipos), continuidad con demanda previsiblemente sostenida, diseño estable, seguridad en el abastecimiento de materias primas y disponibilidad de equipamiento específico."
},
{
  "id": "q069",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "En el factor 'cambios' del lay out, ¿cuál es la estrategia correcta para mantener la flexibilidad?",
  "opciones": [
    {"id": "a", "texto": "Fijar la distribución de forma permanente con estructuras sólidas para evitar modificaciones costosas"},
    {"id": "b", "texto": "Mantener la distribución original tan libre como sea posible de características fijas e identificar cambios posibles y su magnitud"},
    {"id": "c", "texto": "Rediseñar el lay out cada año para adaptarse a las variaciones del mercado"},
    {"id": "d", "texto": "Invertir en equipos especializados de alto rendimiento que no puedan moverse para asegurar la productividad"}
  ],
  "correcta": "b",
  "explicacion": "Para el factor 'cambios', la estrategia es: identificar posibles cambios y su magnitud, buscar una distribución capaz de adaptarse dentro de límites razonables y mantener la distribución original tan libre como sea posible de características fijas, permanentes o especiales. Esto es lo opuesto a fijar estructuras permanentes."
},
{
  "id": "q070",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es el objetivo principal al diseñar o cambiar el lay out de una planta?",
  "opciones": [
    {"id": "a", "texto": "Maximizar la estética del ambiente de trabajo y reducir el ausentismo"},
    {"id": "b", "texto": "Lograr una asignación óptima del espacio considerando aspectos económicos, técnicos y humanos"},
    {"id": "c", "texto": "Minimizar exclusivamente el costo del manejo de materiales"},
    {"id": "d", "texto": "Aumentar la capacidad de producción duplicando las estaciones de trabajo"}
  ],
  "correcta": "b",
  "explicacion": "El objetivo del lay out es lograr una asignación ÓPTIMA del espacio de una planta, incluyendo aspectos económicos (costos de manejo, inversión), técnicos (flujo de proceso, equipos) y humanos (monotonía, tensión, seguridad). El análisis no se reduce solo a la dimensión económica sino que es integral."
},
{
  "id": "q071",
  "tema": "Unidad 4: Layout",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El factor 'edificio' del lay out es más limitante cuando se trata de una construcción nueva que cuando el edificio ya existe.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. El factor 'edificio' influye más como limitante cuando el edificio YA EXISTE (número de pisos, forma de planta, columnas, ventanas, resistencia de suelos, altura de techos, etc. son fijos). Cuando el edificio es de nueva construcción, estas limitaciones no ocurren y el diseñador tiene mayor libertad."
},
{
  "id": "q072",
  "tema": "Unidad 4: Layout",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "Al diseñar el lay out geométrico, ¿cuál de los siguientes aspectos se recomienda considerar específicamente para los servicios (no para la industria)?",
  "opciones": [
    {"id": "a", "texto": "Evitar cruces y codos en la circulación de materiales"},
    {"id": "b", "texto": "Considerar el grado de personalización del servicio al distribuir los espacios"},
    {"id": "c", "texto": "Prever la utilización de la altura del edificio para almacenamiento"},
    {"id": "d", "texto": "Incluir el ancho adecuado de pasillos para autoelevadores"}
  ],
  "correcta": "b",
  "explicacion": "Para servicios, el lay out geométrico debe considerar el GRADO DE PERSONALIZACIÓN: un servicio muy personalizado requiere espacios más privados y diferenciados, mientras que uno masivo puede ser más abierto y estandarizado. Los pasillos para autoelevadores y el aprovechamiento de altura son consideraciones principalmente industriales."
},

# ─────────────────────────────────────────────
# UNIDAD 5: ESTUDIO DEL TRABAJO (12 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q073",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuál es el objetivo del estudio del trabajo?",
  "opciones": [
    {"id": "a", "texto": "Maximizar la producción imponiendo ritmos más exigentes al personal"},
    {"id": "b", "texto": "Examinar cómo se realiza una tarea, simplificar o modificar el método para reducir trabajo innecesario y fijar el tiempo normal"},
    {"id": "c", "texto": "Controlar la asistencia y el desempeño individual de los trabajadores mediante observación directa"},
    {"id": "d", "texto": "Diseñar los programas de capacitación y entrenamiento del personal productivo"}
  ],
  "correcta": "b",
  "explicacion": "El estudio del trabajo examina de qué manera se realiza una tarea, simplifica o modifica el método para reducir el trabajo innecesario o excesivo, o el uso antieconómico de recursos, y fija el tiempo normal para esa actividad. Es una herramienta de mejora de la productividad, no de control disciplinario."
},
{
  "id": "q074",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuántos pasos tiene el procedimiento básico para el estudio del trabajo y cuáles son los primeros 3 que son 'inevitables'?",
  "opciones": [
    {"id": "a", "texto": "6 pasos; los 3 primeros: planificar, ejecutar, verificar"},
    {"id": "b", "texto": "8 pasos; los 3 inevitables: seleccionar, registrar, examinar"},
    {"id": "c", "texto": "5 pasos; los 3 primeros: seleccionar, medir, implantar"},
    {"id": "d", "texto": "7 pasos; los 3 inevitables: observar, analizar, proponer"}
  ],
  "correcta": "b",
  "explicacion": "El procedimiento básico tiene 8 pasos: Seleccionar, Registrar, Examinar, Establecer, Evaluar, Definir, Implantar, Controlar. Los 3 primeros (Seleccionar, Registrar, Examinar) son inevitables porque se aplican tanto en estudio de métodos como en medición de trabajo. El paso 4 es del estudio de métodos; el 5 exige medición del trabajo."
},
{
  "id": "q075",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "¿Por qué los trabajadores temen que un aumento de la productividad genere desempleo y cuál es la actitud correcta del especialista en métodos y tiempos?",
  "opciones": [
    {"id": "a", "texto": "El temor es infundado; el especialista debe ignorarlo y aplicar los métodos sin consulta"},
    {"id": "b", "texto": "El temor es legítimo; el especialista debe explicar el objetivo del estudio en forma abierta, lograr participación y aclarar que estudia el trabajo, no a los trabajadores"},
    {"id": "c", "texto": "El temor es irrelevante si la empresa garantiza contractualmente el empleo a todos"},
    {"id": "d", "texto": "El especialista debe trabajar solo con supervisores para evitar la resistencia obrera"}
  ],
  "correcta": "b",
  "explicacion": "El temor al desempleo es una dificultad real. El especialista debe: hablar en forma abierta sobre el objetivo, lograr participación de todos (supervisor, operarios, representantes), reconocer los aportes del trabajador, y dejar claro que estudia el TRABAJO, no a los TRABAJADORES. La participación frecuentemente aporta ideas valiosas."
},
{
  "id": "q076",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "¿Cuál de las siguientes intervenciones de ciencias de la conducta es la MÁS EFECTIVA para mejorar la productividad según el material?",
  "opciones": [
    {"id": "a", "texto": "Liderazgo y participación"},
    {"id": "b", "texto": "Enriquecimiento del puesto desde el diseño"},
    {"id": "c", "texto": "Sistemas de incentivos y selección de personal con pruebas/test"},
    {"id": "d", "texto": "Programas de opciones como horarios flexibles y semana reducida"}
  ],
  "correcta": "c",
  "explicacion": "Según el material, los sistemas de incentivos y la selección de personal y tecnología (mediante test/pruebas) son las más efectivas (++). Las menos efectivas son: liderazgo y participación, enriquecimiento del puesto, y programas opcionales (--). Esto va contra la intuición: el liderazgo parece fundamental pero las intervenciones 'duras' demuestran mayor impacto en productividad."
},
{
  "id": "q077",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "El 80% de la información que se requiere para efectuar un trabajo se adquiere por la vista, lo que hace de la iluminación un factor esencial para la productividad.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "v",
  "explicacion": "Verdadero. El 80% de la información para efectuar un trabajo se adquiere por la vista. La iluminación influye en factores como: tamaño del objeto, color, distancia a los ojos, intensidad de la luz y contrastes. Es esencial para la realización de tareas de forma precisa, rápida y con calidad."
},
{
  "id": "q078",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuáles son los 5 recursos o factores internos de una empresa que son los insumos básicos de producción?",
  "opciones": [
    {"id": "a", "texto": "Producto, proceso, lay out, mantenimiento y calidad"},
    {"id": "b", "texto": "Terrenos y edificios, materiales, energía, máquinas y equipos, y recursos humanos"},
    {"id": "c", "texto": "Capital, tecnología, información, proveedores y clientes"},
    {"id": "d", "texto": "Diseño, producción, comercialización, finanzas y logística"}
  ],
  "correcta": "b",
  "explicacion": "Los 5 recursos o insumos internos son: terrenos y edificios, materiales, energía, máquinas y equipos, y recursos humanos. Todos implican la disponibilidad de capital para financiarlos. La dirección es la encargada de combinarlos de la mejor manera para obtener la máxima productividad."
},
{
  "id": "q079",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Por qué los supervisores suelen ser el 'primer escollo' en la realización de estudios del trabajo?",
  "opciones": [
    {"id": "a", "texto": "Porque ganan comisiones por ocultar ineficiencias del proceso a la dirección"},
    {"id": "b", "texto": "Porque temen quedar desprestigiados si se encuentran mejoras en el trabajo que dirigieron, o perder poder si se delegan funciones en el especialista"},
    {"id": "c", "texto": "Porque no tienen formación técnica suficiente para entender los estudios de tiempos"},
    {"id": "d", "texto": "Porque el sindicato les prohíbe colaborar con estudios de métodos y tiempos"}
  ],
  "correcta": "b",
  "explicacion": "Los supervisores presentan obstáculos porque: 1) Si se encuentran mejoras en el trabajo que dirigieron por años, quedarán desprestigiados ante superiores y subordinados; 2) Si se delegan al especialista funciones que antes eran suyas (tiempos, cantidades, contrataciones), sienten que perdieron categoría o poder."
},
{
  "id": "q080",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "verdadero_falso",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Según el material, mejorar la productividad se logra fundamentalmente trabajando sobre los FACTORES EXTERNOS de la empresa (políticas del estado, aranceles, infraestructura), ya que son los que más impacto tienen.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Los factores EXTERNOS (disponibilidad de MP, políticas del estado, impuestos, aranceles, infraestructura) están fuera del control del empresario: no puede decidir cambios en ellos. El estudio del trabajo actúa sobre los factores INTERNOS (terrenos, materiales, energía, máquinas, RRHH) donde la dirección SÍ tiene poder de decisión."
},
{
  "id": "q081",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es la normativa mínima para los locales de trabajo en términos de altura de techos y espacio de aire por trabajador?",
  "opciones": [
    {"id": "a", "texto": "Techos mínimo 2 m; 5 m³ de aire por trabajador"},
    {"id": "b", "texto": "Techos mínimo 3 m; 10 m³ de aire por trabajador"},
    {"id": "c", "texto": "Techos mínimo 4 m; 15 m³ de aire por trabajador"},
    {"id": "d", "texto": "No hay restricciones fijas; depende del tipo de actividad"}
  ],
  "correcta": "b",
  "explicacion": "Los locales de trabajo deben: construirse sobre el nivel del suelo, tener techos no inferiores a 3 metros, y cada trabajador debe disponer de al menos 10 metros cúbicos de aire. También deben aislarse toda actividad peligrosa o perjudicial."
},
{
  "id": "q082",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "La productividad se define como:",
  "opciones": [
    {"id": "a", "texto": "La relación entre el tiempo estándar y el tiempo empleado"},
    {"id": "b", "texto": "La relación entre producción e insumos"},
    {"id": "c", "texto": "El número de unidades producidas por hora de trabajo"},
    {"id": "d", "texto": "El costo de producción dividido entre el precio de venta"}
  ],
  "correcta": "b",
  "explicacion": "Productividad = relación entre producción e insumos. Aumentar la producción NO equivale a mejorar la productividad. Siempre se debe apuntar a hacer más con los mismos recursos, o lograr la misma cantidad con menos recursos. La eficiencia (tiempo estándar / tiempo empleado) es un concepto distinto."
},
{
  "id": "q083",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "La organización INFORMAL dentro de una empresa puede fijar 'cupos de producción' que no coinciden con los que desea la empresa. ¿Qué implica esto para el estudio del trabajo?",
  "opciones": [
    {"id": "a", "texto": "El especialista debe ignorar la organización informal y aplicar los estándares sin consulta"},
    {"id": "b", "texto": "La producción real tenderá a ajustarse al cupo tácito del grupo, por presiones sociales, aunque sea diferente al estándar formal. Esto debe tenerse en cuenta al diseñar la implementación"},
    {"id": "c", "texto": "La organización informal siempre producirá más que el cupo formal por competencia entre pares"},
    {"id": "d", "texto": "El cupo informal queda obsoleto automáticamente cuando se implementan sistemas de incentivos económicos"}
  ],
  "correcta": "b",
  "explicacion": "Los grupos informales tienden a fijar cupos de producción tácitamente aceptados. El trabajador que se desvíe (produzca más o menos) recibirá presiones del grupo para ajustarse. Esto significa que al implementar mejoras, el especialista debe trabajar activamente con los grupos informales y no solo con la estructura formal."
},
{
  "id": "q084",
  "tema": "Unidad 5: Estudio del Trabajo",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Para mejorar la productividad de plantas y equipos, ¿cuál de las siguientes acciones se menciona en el material?",
  "opciones": [
    {"id": "a", "texto": "Contratar más operarios para duplicar la capacidad instalada"},
    {"id": "b", "texto": "Un buen mantenimiento, funcionamiento de equipos en condiciones óptimas, eliminación de estrangulamientos y reducción del tiempo de parada"},
    {"id": "c", "texto": "Aumentar las horas de trabajo mediante turnos nocturnos obligatorios"},
    {"id": "d", "texto": "Reemplazar todos los equipos con tecnología de última generación cada 5 años"}
  ],
  "correcta": "b",
  "explicacion": "Para mejorar la productividad de plantas y equipos se puede: mantener buen mantenimiento, operar equipos en condiciones óptimas, eliminar estrangulamientos (cuellos de botella), y reducir tiempo de parada e incrementar capacidad de planta. No implica necesariamente contratar más personal ni renovar equipos."
},

# ─────────────────────────────────────────────
# UNIDAD 6: ESTUDIO DE MÉTODOS (12 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q085",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué es el estudio de métodos?",
  "opciones": [
    {"id": "a", "texto": "La técnica para medir el tiempo que tarda un operario calificado en realizar una tarea"},
    {"id": "b", "texto": "El registro y examen crítico sistemático de los modos de realizar actividades con el fin de efectuar mejoras"},
    {"id": "c", "texto": "El análisis estadístico de la variabilidad en los tiempos de producción"},
    {"id": "d", "texto": "El diseño de los sistemas de incentivos para mejorar el rendimiento del personal"}
  ],
  "correcta": "b",
  "explicacion": "El estudio de métodos es el registro y examen crítico sistemático de los modos de realizar actividades con el fin de efectuar mejoras. Es el paso PREVIO antes de la medición del tiempo: primero se determina el MEJOR método, luego se mide el tiempo de ese método. Reduce costos y optimiza el uso de recursos."
},
{
  "id": "q086",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El 'método de los 5 por qué' en el análisis del estudio de métodos se refiere a:",
  "opciones": [
    {"id": "a", "texto": "Hacer 5 preguntas estadísticas sobre la variabilidad de cada operación"},
    {"id": "b", "texto": "Preguntar ¿Por qué hay que hacer la operación? ¿Es imprescindible? ¿Cuándo? ¿Quién? ¿Cómo? para cuestionar críticamente cada aspecto del método"},
    {"id": "c", "texto": "Identificar 5 causas raíz de cada defecto usando el diagrama de Ishikawa"},
    {"id": "d", "texto": "Aplicar 5 ciclos de mejora PDCA antes de implantar el nuevo método"}
  ],
  "correcta": "b",
  "explicacion": "Las 5 preguntas son la esencia del estudio de métodos: ¿Por qué hay que hacer la operación? ¿Es realmente imprescindible? ¿Cuándo corresponde que se haga? ¿Quién debe hacerla? ¿Cómo debe hacerla? Estas preguntas constituyen el cuestionamiento crítico que permite identificar operaciones innecesarias o mejorables."
},
{
  "id": "q087",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál de las siguientes NO es una herramienta de registro de información en el estudio de métodos?",
  "opciones": [
    {"id": "a", "texto": "Diagrama de flujo del proceso"},
    {"id": "b", "texto": "Diagrama bimanual"},
    {"id": "c", "texto": "Diagrama de Gantt de actividades"},
    {"id": "d", "texto": "Gráfico de trayectorias"}
  ],
  "correcta": "c",
  "explicacion": "Las herramientas de registro en estudio de métodos son: diagrama de flujo del proceso, diagrama bimanual, diagrama de actividades múltiples, gráfico de trayectorias, diagrama de hilos y registros de micro movimientos. El diagrama de Gantt es una herramienta de programación/planificación, no de registro de métodos."
},
{
  "id": "q088",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Entre el 70% y el 80% del tiempo asignado a una operación es de mano de obra. ¿Qué implica esto para el alcance del estudio de métodos?",
  "opciones": [
    {"id": "a", "texto": "Que el estudio de métodos debe enfocarse exclusivamente en las tareas manuales y nunca en los equipos"},
    {"id": "b", "texto": "Que los movimientos en el puesto de trabajo deben orientarse siguiendo principios de economía de movimientos, y también se debe analizar la maquinaria, equipos y lay out"},
    {"id": "c", "texto": "Que el 20-30% restante de tiempo (de máquina) es irrelevante para el estudio de métodos"},
    {"id": "d", "texto": "Que la única forma de mejorar el método es reducir la cantidad de operarios en la tarea"}
  ],
  "correcta": "b",
  "explicacion": "Dado que 70-80% del tiempo es de MO, los movimientos en el puesto deben seguir principios de economía de movimientos: uso del cuerpo humano, distribución del puesto y utilización de máquinas/herramientas. Pero el alcance también incluye máquinas, equipos, lay out y el desarrollo de dispositivos automáticos; no se limita solo a lo manual."
},
{
  "id": "q089",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuáles son los 3 grupos de principios de economía de movimientos en el puesto de trabajo?",
  "opciones": [
    {"id": "a", "texto": "Planear, ejecutar y controlar"},
    {"id": "b", "texto": "Utilización del cuerpo humano, distribución del lugar de trabajo, y modelo de las máquinas y herramientas"},
    {"id": "c", "texto": "Reducción de distancias, eliminación de esperas y combinación de operaciones"},
    {"id": "d", "texto": "Seguridad, ergonomía y calidad del producto"}
  ],
  "correcta": "b",
  "explicacion": "Los 3 grupos de principios de economía de movimientos son: 1) Utilización del cuerpo humano (ej: no deben estar inactivas ambas manos salvo en descansos), 2) Distribución del lugar de trabajo (ej: lugar definido para cada herramienta y material), 3) Modelo de las máquinas y herramientas (ej: usar plantillas o brazos en lugar de sostener piezas con las manos)."
},
{
  "id": "q090",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El estudio de métodos se enfoca SOLO en aumentar la productividad. No considera la reducción de la fatiga ni las condiciones de trabajo del operario.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. El estudio de métodos también considera: reducir la fatiga del operario, mejorar el puesto de trabajo para reducirla, mejorar la calidad del producto y considerar el factor humano. No hay que centrarse SOLO en el aumento de la productividad, sino también en la reducción de la carga de trabajo y las condiciones del operario."
},
{
  "id": "q091",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es el factor 'económico' que justifica seleccionar una tarea para el estudio de métodos?",
  "opciones": [
    {"id": "a", "texto": "Cuando la tarea es la que paga mejor sueldo al operario"},
    {"id": "b", "texto": "Cuando la tarea genera estrangulamientos, requiere mucha MO o tiene largas distancias de recorrido de materiales (usar Pareto)"},
    {"id": "c", "texto": "Cuando la tarea forma parte de un proceso de alto volumen de producción sin importar su costo"},
    {"id": "d", "texto": "Cuando la empresa quiere sustituir tecnología para modernizarse"}
  ],
  "correcta": "b",
  "explicacion": "El factor económico para seleccionar una tarea incluye: operaciones con estrangulamientos que generan desperdicio de tiempo, actividades que requieren mucha mano de obra o largas distancias de recorrido de materiales, y acciones que tienen mayor impacto en costos. Se recomienda usar el principio de Pareto (20/80) para priorizar."
},
{
  "id": "q092",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "¿Por qué el 'mejor método aún no existe'? ¿Qué implica esta frase en la práctica?",
  "opciones": [
    {"id": "a", "texto": "Que el estudio de métodos nunca puede terminar porque los métodos son perfectibles y siempre se puede encontrar una mejora"},
    {"id": "b", "texto": "Que los métodos actuales son tan buenos que no necesitan mejora, pero la ciencia no puede comprobarlo"},
    {"id": "c", "texto": "Que se debe contratar siempre especialistas externos para evaluar los métodos internos"},
    {"id": "d", "texto": "Que el mejor método depende de la tecnología disponible y cambia con cada nueva máquina que se compra"}
  ],
  "correcta": "a",
  "explicacion": "'El mejor método aún no existe' implica que el proceso de mejora de métodos es continuo y permanente: siempre se puede mejorar algo. Esto refleja la filosofía de mejora continua: después de implementar un nuevo método, se siguen buscando nuevas mejoras. No existe un método 'definitivo' u 'óptimo absoluto'."
},
{
  "id": "q093",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Antes de estudiar los movimientos en el lugar de trabajo, ¿qué se debe verificar primero?",
  "opciones": [
    {"id": "a", "texto": "Que el operario haya sido informado y acepte el estudio"},
    {"id": "b", "texto": "Si la tarea es realmente necesaria y si se ejecuta de manera adecuada (propósito, lugar, sucesión y persona)"},
    {"id": "c", "texto": "Que el estudio de tiempos con cronómetro ya esté finalizado"},
    {"id": "d", "texto": "Que el diagrama de lay out de la planta esté actualizado"}
  ],
  "correcta": "b",
  "explicacion": "Antes de estudiar los movimientos, se debe comprobar si la tarea es realmente necesaria y si se ejecuta de manera adecuada. Se debe interrogar sobre: el propósito de la tarea, el lugar donde se realiza, la sucesión que ocupa dentro del proceso, y si la realiza la persona indicada. Solo entonces tiene sentido estudiar y optimizar sus movimientos."
},
{
  "id": "q094",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué factor 'humano' justifica seleccionar una tarea para el estudio de métodos?",
  "opciones": [
    {"id": "a", "texto": "Cuando la tarea genera alta rentabilidad y el gerente quiere documentarla"},
    {"id": "b", "texto": "Cuando la tarea causa insatisfacción en los trabajadores, genera fatiga excesiva, monotonía o accidentes"},
    {"id": "c", "texto": "Cuando la tarea requiere trabajadores muy especializados difíciles de contratar"},
    {"id": "d", "texto": "Cuando los trabajadores piden aumentos de sueldo por la complejidad de la tarea"}
  ],
  "correcta": "b",
  "explicacion": "El factor humano para seleccionar una tarea incluye: actividades que causan insatisfacción de los trabajadores, que provocan fatiga excesiva, monotonía o accidentes. Esto refleja que el estudio de métodos no solo busca eficiencia económica, sino también mejorar las condiciones de trabajo."
},
{
  "id": "q095",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El alcance del estudio de métodos se limita a una operación individual, sin considerar el diseño del producto ni las especificaciones de las máquinas.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. El alcance del estudio de métodos no se limita a una operación: debe atender también al diseño del producto, las especificaciones, la definición de máquinas y el lay out. El análisis alcanza a máquinas, equipos, desarrollo de ayudas de trabajo y dispositivos automáticos. Es una visión de sistema, no puntual."
},
{
  "id": "q096",
  "tema": "Unidad 6: Estudio de Métodos",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "El 'factor técnico' para seleccionar una tarea de estudio de métodos es especialmente relevante cuando la dirección quiere ADQUIRIR NUEVA TECNOLOGÍA. ¿Por qué?",
  "opciones": [
    {"id": "a", "texto": "Porque el proveedor de tecnología exige un estudio de métodos previo como condición de venta"},
    {"id": "b", "texto": "Porque el estudio de métodos puede señalar las verdaderas necesidades antes de automatizar, evitando comprar tecnología innecesaria"},
    {"id": "c", "texto": "Porque la nueva tecnología siempre requiere métodos completamente diferentes que no pueden derivarse del método anterior"},
    {"id": "d", "texto": "Porque la adquisición de tecnología es siempre más cara si no va acompañada de un estudio previo de tiempos"}
  ],
  "correcta": "b",
  "explicacion": "El factor técnico es relevante cuando la dirección quiere adquirir nueva tecnología o automatizar actividades: un estudio de métodos PREVIO puede señalar las verdaderas necesidades y evitar comprar tecnología innecesaria o inadecuada. A veces una mejora de método puede reemplazar la automatización a mucho menor costo."
},
]

print(json.dumps(preguntas, ensure_ascii=False, indent=2))
