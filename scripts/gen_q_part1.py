"""Genera preguntas para Unidades 1-3 de Organización Industrial."""
import json

preguntas = [
# ─────────────────────────────────────────────
# UNIDAD 1: LOCALIZACIÓN (18 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q001",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuál es el criterio principal de elección en una decisión de localización industrial?",
  "opciones": [
    {"id": "a", "texto": "El criterio social (generar empleo local)"},
    {"id": "b", "texto": "El criterio económico (maximizar el valor actual del flujo de fondos)"},
    {"id": "c", "texto": "El criterio ambiental (minimizar el impacto ecológico)"},
    {"id": "d", "texto": "El criterio político (cumplir con leyes de promoción industrial)"}
  ],
  "correcta": "b",
  "explicacion": "El criterio de elección en localización es el económico: se elige la opción que maximice el valor actual del flujo de fondos. Los demás factores (sociales, ambientales, políticos) actúan como restricciones del problema, no como criterio de decisión."
},
{
  "id": "q002",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "En el flujo de fondos para decisiones de localización, los ingresos se consideran irrelevantes porque:",
  "opciones": [
    {"id": "a", "texto": "Son difíciles de proyectar a largo plazo"},
    {"id": "b", "texto": "No dependen de la decisión de localización ya que el mercado a atender no se define ahí"},
    {"id": "c", "texto": "Son siempre iguales en cualquier localización"},
    {"id": "d", "texto": "El flujo de fondos solo considera egresos por definición metodológica"}
  ],
  "correcta": "b",
  "explicacion": "Los ingresos no dependen de la decisión de localización porque en esa etapa no se define qué mercado se atenderá. Por eso, el análisis se concentra en los egresos: costo de localización (terreno, construcción, instalaciones) + costo de operación (MP, MO, energía, impuestos)."
},
{
  "id": "q003",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "El método de Brown-Gibson se llama también 'método de factores ponderados'. ¿Qué característica lo distingue de los métodos puramente cuantitativos?",
  "opciones": [
    {"id": "a", "texto": "Es el único método que usa programación lineal"},
    {"id": "b", "texto": "Combina factores cuantificables con factores subjetivos/cualitativos"},
    {"id": "c", "texto": "Solo evalúa costos de transporte entre plantas y mercados"},
    {"id": "d", "texto": "Minimiza el costo de transporte usando coordenadas geográficas"}
  ],
  "correcta": "b",
  "explicacion": "Brown-Gibson pondera tanto factores tangibles (cuantificables) como intangibles (subjetivos). Obtiene una medida de preferencia para cada alternativa. El método del centro de gravedad usa coordenadas; el modelo de transporte usa programación lineal; ninguno de esos es Brown-Gibson."
},
{
  "id": "q004",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "El modelo de transporte para localización minimiza los costos totales de producción y transporte. ¿Cuáles son sus dos tipos de restricciones?",
  "opciones": [
    {"id": "a", "texto": "Capacidad de inversión en la fuente y restricciones ambientales en el destino"},
    {"id": "b", "texto": "Capacidad de producción en la fuente (fábrica) y necesidad de demanda en el destino (mercado)"},
    {"id": "c", "texto": "Costo variable de producción en la fuente y costo fijo de transporte en el destino"},
    {"id": "d", "texto": "Disponibilidad de mano de obra y cercanía al mercado consumidor"}
  ],
  "correcta": "b",
  "explicacion": "El modelo de transporte (tipo de programación lineal) tiene dos restricciones: capacidad de producción disponible en cada planta-fuente y la demanda que debe satisfacerse en cada mercado-destino. El costo variable total se expresa como CV de operación = CV de producción + costo de transporte a mercado."
},
{
  "id": "q005",
  "tema": "Unidad 1: Localización",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "En una decisión de localización, la búsqueda de alternativas debe continuar hasta agotar todas las opciones geográficas posibles para garantizar la solución óptima.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. La búsqueda de alternativas finaliza cuando el costo incremental de seguir buscando se equilibra con la mejora probable en la solución. Continuar indefinidamente generaría un gasto de tiempo y dinero que no se justifica con la mejora obtenida."
},
{
  "id": "q006",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué se entiende por 'macrocefalismo' en el contexto de las tendencias de localización?",
  "opciones": [
    {"id": "a", "texto": "Una técnica para calcular el centro de gravedad de múltiples plantas"},
    {"id": "b", "texto": "La concentración excesiva del desarrollo económico, industrial y poblacional en una sola región"},
    {"id": "c", "texto": "El exceso de personal directivo respecto a operarios en una fábrica"},
    {"id": "d", "texto": "Un modelo de localización que prioriza los mercados más grandes"}
  ],
  "correcta": "b",
  "explicacion": "El macrocefalismo es la concentración excesiva del desarrollo económico, industrial y poblacional en una sola región, como ocurre con Buenos Aires, San Pablo o Londres. Los gobiernos promueven la dispersión geográfica para contrarrestar estos desequilibrios regionales."
},
{
  "id": "q007",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Para una localización en el extranjero, ¿cuál de los siguientes factores es adicional respecto a una localización nacional?",
  "opciones": [
    {"id": "a", "texto": "Cercanía al mercado consumidor y costo de transporte"},
    {"id": "b", "texto": "Disponibilidad de mano de obra calificada y costo de terrenos"},
    {"id": "c", "texto": "Posibilidad de repatriar utilidades y tipo de cambio"},
    {"id": "d", "texto": "Leyes de Promoción Industrial y clima laboral"}
  ],
  "correcta": "c",
  "explicacion": "Para localización en el extranjero se suman factores específicos como: estabilidad política, clima económico, tipo de cambio, legislación vigente (seguridad jurídica), posibilidad de repatriar utilidades y política aduanera. La repatriación de utilidades y el tipo de cambio son riesgos inexistentes en una localización nacional."
},
{
  "id": "q008",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "El método del centro de gravedad minimiza el costo de transporte ubicando un punto de distribución. ¿Cuáles son las variables que se deben considerar?",
  "opciones": [
    {"id": "a", "texto": "Precio del terreno, infraestructura disponible y costo de mano de obra en cada alternativa"},
    {"id": "b", "texto": "Localización de los destinos, volumen de transporte y distancia/costo de transporte (asumiendo costo/unidad/km constante)"},
    {"id": "c", "texto": "Capacidad de producción de cada planta y demanda mínima de cada mercado"},
    {"id": "d", "texto": "Número de proveedores cercanos, temperatura media y disponibilidad hídrica"}
  ],
  "correcta": "b",
  "explicacion": "El método del centro de gravedad usa coordenadas X e Y de los posibles destinos, el volumen de transporte de cada uno y la distancia o costo (asumiendo que el costo/unidad/km es constante). Con eso calcula el punto que minimiza el costo total de transporte."
},
{
  "id": "q009",
  "tema": "Unidad 1: Localización",
  "tipo": "verdadero_falso",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "Las decisiones de localización industrial impactan en el largo plazo y generalmente son reversibles con bajo costo.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Las decisiones de localización impactan en el largo plazo y son prácticamente irreversibles. Mover una planta implica costos altísimos (desinversión, nueva construcción, relocalización de personal, etc.), por eso se sigue una metodología sistemática y cuidadosa."
},
{
  "id": "q010",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuál de los siguientes es un factor condicionante para la localización de una industria?",
  "opciones": [
    {"id": "a", "texto": "La tasa de actualización financiera del flujo de fondos"},
    {"id": "b", "texto": "La marca registrada y las patentes del producto"},
    {"id": "c", "texto": "La cercanía al mercado consumidor y las vías de comunicación y transporte"},
    {"id": "d", "texto": "El organigrama interno del departamento de producción"}
  ],
  "correcta": "c",
  "explicacion": "Los factores condicionantes para la localización incluyen: materia prima, energía y servicios, RRHH y costo, cercanía al mercado consumidor, comunicaciones y transporte, leyes de promoción industrial, disponibilidad de terrenos, legislación local, clima social y laboral, entre otros."
},
{
  "id": "q011",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Según el enfoque metodológico, ¿en qué etapa del proceso de decisión de localización se utiliza el método de transporte (programación lineal) para evaluar los costos variables?",
  "opciones": [
    {"id": "a", "texto": "Etapa 2: Relevamiento y análisis de información"},
    {"id": "b", "texto": "Etapa 3: Búsqueda de alternativas posibles"},
    {"id": "c", "texto": "Etapa 4: Elección de la mejor alternativa"},
    {"id": "d", "texto": "Etapa 1: Formulación del problema"}
  ],
  "correcta": "c",
  "explicacion": "En la etapa 4 (Elección de la mejor alternativa) se analizan los costos de localización y los costos fijos de operación. Los costos variables, en el caso de varias plantas, se evalúan mediante el método del transporte: CV operación = CV producción + costo transporte a mercado."
},
{
  "id": "q012",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Para la localización de instalaciones de servicio (no industriales), ¿cuál de los siguientes es un factor clave específico de este tipo?",
  "opciones": [
    {"id": "a", "texto": "Costo de construcción de la planta y disponibilidad de maquinaria especializada"},
    {"id": "b", "texto": "Poder adquisitivo de los consumidores de la zona y calidad de la competencia"},
    {"id": "c", "texto": "Disponibilidad de materias primas y suministro ininterrumpido de energía"},
    {"id": "d", "texto": "Cercanía a rutas de exportación y acceso a zonas francas"}
  ],
  "correcta": "b",
  "explicacion": "Para servicios, los factores clave incluyen: poder adquisitivo de los consumidores, imagen compatible con la demografía, competencia en la zona y su calidad, particularidades de las localizaciones propias y de competidores, y calidad de gestión. Son factores orientados al cliente, no a la producción."
},
{
  "id": "q013",
  "tema": "Unidad 1: Localización",
  "tipo": "relacion",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Relacioná cada método de localización con su descripción correcta.",
  "columna_izq": [
    {"id": "1", "texto": "Centro de gravedad"},
    {"id": "2", "texto": "Modelo de transporte"},
    {"id": "3", "texto": "Brown-Gibson"},
    {"id": "4", "texto": "Punto muerto de localización"}
  ],
  "columna_der": [
    {"id": "x", "texto": "Técnica matemática para hallar el punto único de distribución que minimiza costo de transporte"},
    {"id": "y", "texto": "Programación lineal que determina el patrón óptimo de entregas entre plantas y mercados"},
    {"id": "z", "texto": "Combina factores tangibles e intangibles asignando pesos; elige la alternativa de mayor valor"},
    {"id": "w", "texto": "Método cuantitativo que elige la localización a partir de un punto de referencia"}
  ],
  "correcta": {"1": "x", "2": "y", "3": "z", "4": "w"},
  "explicacion": "Centro de gravedad: minimiza transporte con coordenadas. Modelo de transporte: programación lineal con restricciones de capacidad y demanda. Brown-Gibson: el más utilizado, combina tangibles e intangibles. Punto muerto: método cuantitativo de referencia comparativa."
},
{
  "id": "q014",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál de las siguientes actividades constituye una 'excepción' que justifica NO seguir la tendencia general de dispersión geográfica?",
  "opciones": [
    {"id": "a", "texto": "Industrias que producen bienes de consumo masivo para mercados amplios"},
    {"id": "b", "texto": "Procesos que requieren mano de obra poco calificada disponible en zonas rurales"},
    {"id": "c", "texto": "Actividades que demandan mano de obra muy calificada con posibilidad de carrera interna"},
    {"id": "d", "texto": "Empresas con alta inversión en publicidad y marketing digital"}
  ],
  "correcta": "c",
  "explicacion": "Las excepciones a la dispersión son: cuando los insumos deben procesarse donde se disponen (por técnica o costo de transporte muy elevado), actividades que demandan mano de obra calificada con posibilidad de carrera dentro de la empresa, y procesos que deben estar cerca del mercado (servicios)."
},
{
  "id": "q015",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "La 'búsqueda de alternativas' en el método de decisión de localización se describe como un proceso 'parcialmente sistemático y parcialmente casual'. ¿Por qué esta dualidad?",
  "opciones": [
    {"id": "a", "texto": "Porque combina datos cuantitativos de mercado con encuestas de opinión al personal"},
    {"id": "b", "texto": "Porque depende tanto de la metodología aplicada como de los conocimientos y experiencia del analista a cargo"},
    {"id": "c", "texto": "Porque alterna entre el método Brown-Gibson (sistemático) y el punto muerto (casual)"},
    {"id": "d", "texto": "Porque se aplica primero a nivel nacional (sistemático) y luego a nivel regional (casual)"}
  ],
  "correcta": "b",
  "explicacion": "El proceso de búsqueda de alternativas es 'parcialmente sistemático' porque sigue pasos metodológicos (definir áreas, luego lugares específicos), pero 'parcialmente casual' porque su efectividad y velocidad dependen en gran medida de los conocimientos y experiencias del analista a cargo del proyecto."
},
{
  "id": "q016",
  "tema": "Unidad 1: Localización",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "Las Leyes de Promoción Industrial siempre generan un beneficio real en las decisiones de localización porque fomentan la dispersión geográfica y el desarrollo regional.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Aunque las Leyes de Promoción Industrial amplían las opciones de localización, la inapropiada administración por parte de los entes de control facilitó que en muchos casos se utilizaran como instrumento de evasión fiscal, desvirtuando su propósito original."
},
{
  "id": "q017",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué componen los Egresos en la fórmula de decisión de localización?",
  "opciones": [
    {"id": "a", "texto": "Costos fijos + costos variables de producción"},
    {"id": "b", "texto": "Costo de localización + Costo de operación"},
    {"id": "c", "texto": "Ingresos esperados - Margen de beneficio"},
    {"id": "d", "texto": "Costo de materia prima + Costo de distribución al mercado"}
  ],
  "correcta": "b",
  "explicacion": "Egresos = Costo de localización + Costo de operación. El costo de localización incluye: compra terreno, construcción planta, instalaciones. El costo de operación incluye: materia prima, mano de obra, energía, impuestos (fijos y variables)."
},
{
  "id": "q018",
  "tema": "Unidad 1: Localización",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "Una empresa ubicada a la DERECHA de la diagonal en la matriz producto-proceso (o servicio-proceso) indica:",
  "opciones": [
    {"id": "a", "texto": "Que aplica tecnología demasiado avanzada respecto al desarrollo del producto (ventaja competitiva)"},
    {"id": "b", "texto": "Que tiene un atraso tecnológico respecto al tipo de producto que fabrica"},
    {"id": "c", "texto": "Que produce commodities con alta estandarización de forma eficiente"},
    {"id": "d", "texto": "Que es convenientemente flexible para adaptarse a cambios de mercado"}
  ],
  "correcta": "b",
  "explicacion": "En la matriz producto-proceso, ubicarse a la DERECHA de la diagonal indica atraso tecnológico: la empresa usa un proceso menos avanzado que el que corresponde al tipo de producto. Ubicarse a la IZQUIERDA indica el exceso opuesto: tecnología demasiado avanzada para el producto. Lo ideal es estar cerca de la diagonal. (Nota: esta pregunta mezcla Unidad 3 con el contexto de Unidad 1 como pregunta de análisis.)"
},

# ─────────────────────────────────────────────
# UNIDAD 2: INGENIERÍA DE PRODUCTO (18 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q019",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "¿Cuál es la diferencia clave entre 'creatividad' e 'innovación' según el material?",
  "opciones": [
    {"id": "a", "texto": "La creatividad es colectiva; la innovación es individual"},
    {"id": "b", "texto": "Creatividad = imaginar cosas nuevas; Innovación = hacer cosas nuevas (pasar de la teoría a la práctica)"},
    {"id": "c", "texto": "Creatividad aplica solo a productos; Innovación aplica solo a procesos"},
    {"id": "d", "texto": "La creatividad requiere I+D; la innovación solo requiere mejoras incrementales"}
  ],
  "correcta": "b",
  "explicacion": "Creatividad es imaginar cosas nuevas (concebirlas mentalmente). Innovación es hacer cosas nuevas, pasar de la teoría a la práctica. Una empresa puede ser creativa sin ser innovadora si nunca concreta sus ideas. Las grandes corporaciones frecuentemente pierden la capacidad de innovar por inercia organizacional."
},
{
  "id": "q020",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿En qué etapa del ciclo de vida del producto el flujo de fondos es positivo y las empresas realizan cambios para perfeccionar sus productos?",
  "opciones": [
    {"id": "a", "texto": "Introducción"},
    {"id": "b", "texto": "Crecimiento"},
    {"id": "c", "texto": "Madurez"},
    {"id": "d", "texto": "Declinación"}
  ],
  "correcta": "c",
  "explicacion": "En la etapa de Madurez las ventas tienden a estabilizarse y el flujo de fondos es positivo. Las empresas realizan cambios perfeccionando sus productos para permanecer en esta zona lo más posible. En Crecimiento las ventas suben aceleradamente pero el flujo aún no se estabiliza."
},
{
  "id": "q021",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "La innovación 'revolucionaria' se distingue porque:",
  "opciones": [
    {"id": "a", "texto": "Reestructura completamente las relaciones del mercado y los sistemas productivos (ej: Ford T, transistor)"},
    {"id": "b", "texto": "Utiliza una nueva tecnología en los mercados actuales, tornando obsoletas las soluciones técnicas establecidas (ej: IBM 360)"},
    {"id": "c", "texto": "Introduce cambios en el mercado aprovechando el factor sorpresa con tecnología existente (ej: Walkman)"},
    {"id": "d", "texto": "Realiza cambios menores que aumentan productividad y bajan costos (ej: motor a pistón en aviones)"}
  ],
  "correcta": "b",
  "explicacion": "La innovación revolucionaria utiliza una nueva tecnología en mercados actuales, tornando obsoletas las soluciones técnicas establecidas. Ejemplo: el computador 360 de IBM. La innovación arquitectural es la que reestructura todo (eje +Y y +X). La de creación de nicho usa tecnología existente. La corriente hace mejoras menores."
},
{
  "id": "q022",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Una empresa que espera que el competidor desarrolle el producto hasta la etapa de INTRODUCCIÓN en el mercado para recién comenzar su desarrollo, aplica la estrategia adaptativa:",
  "opciones": [
    {"id": "a", "texto": "Imitativa"},
    {"id": "b", "texto": "De respuesta"},
    {"id": "c", "texto": "Defensiva"},
    {"id": "d", "texto": "Segundo para mejor"}
  ],
  "correcta": "c",
  "explicacion": "La estrategia defensiva espera que la competencia llegue hasta la INTRODUCCIÓN en el mercado para analizar sus resultados y recién entonces comenzar. La imitativa actúa después de la etapa de PRUEBA DE USO. 'Segundo para mejor' copia y mejora el diseño ya conocido. La 'de respuesta' reacciona directamente a requerimientos del consumidor."
},
{
  "id": "q023",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Qué es la 'confiabilidad' (Cp) de un producto y cuál es su rango de valores?",
  "opciones": [
    {"id": "a", "texto": "La vida útil del producto en condiciones normales; varía entre 0 y 100 años"},
    {"id": "b", "texto": "La probabilidad de que el producto se desempeñe satisfactoriamente en un período dado bajo condiciones especificadas; 0 < Cp < 1"},
    {"id": "c", "texto": "El porcentaje de piezas sin defectos en un lote de producción; varía entre 0% y 100%"},
    {"id": "d", "texto": "La frecuencia de mantenimiento requerida; varía entre 0 (sin mantenimiento) y 1 (mantenimiento diario)"}
  ],
  "correcta": "b",
  "explicacion": "Confiabilidad (Cp) es la probabilidad de que el producto se desempeñe satisfactoriamente durante un período determinado, en tanto sea usado en condiciones especificadas. 0 = certeza de falla, 1 = certeza de buen desempeño. Cuando no se puede lograr alta confiabilidad se recurre a la duplicación de elementos críticos."
},
{
  "id": "q024",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "En el diseño técnico de un producto, el objetivo de la 'durabilidad' es maximizarla, ya que mayor vida útil siempre beneficia tanto al productor como al consumidor.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. La durabilidad es un atributo a OPTIMIZAR desde el punto de vista del productor, NO a maximizar. Una vida útil excesiva puede ser contraproducente para el productor (reduce recompra) y puede elevar innecesariamente los costos. El diseñador debe suboptimizar los factores buscando el mínimo sacrificio del conjunto."
},
{
  "id": "q025",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuáles son los cuatro cursos de acción para concretar la innovación según Peter Drucker?",
  "opciones": [
    {"id": "a", "texto": "Investigar, desarrollar, lanzar y controlar"},
    {"id": "b", "texto": "Meterse a lo grande, encontrar nichos especializados, cambiar características económicas del producto, golpear donde nadie ha golpeado"},
    {"id": "c", "texto": "Copiar, mejorar, patentar y escalar"},
    {"id": "d", "texto": "Innovar en producto, proceso, modelo de negocio y distribución"}
  ],
  "correcta": "b",
  "explicacion": "Drucker identifica 4 cursos: 1) Meterse a lo grande, 2) Encontrar nichos especializados, 3) Cambiar características económicas de un producto (modificar el precio según la realidad), 4) Golpear donde nadie ha golpeado. Son estrategias para concretar la innovación en la práctica."
},
{
  "id": "q026",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "El 'diseño modular' en ingeniería de producto consiste en:",
  "opciones": [
    {"id": "a", "texto": "Diseñar el producto para que sea fácilmente exportable a distintos mercados"},
    {"id": "b", "texto": "Diseñar conjuntos estandarizados (módulos) comunes a varios productos, diferenciados solo en el ensamble final"},
    {"id": "c", "texto": "Dividir el equipo de diseño en módulos independientes para trabajar en paralelo"},
    {"id": "d", "texto": "Reducir el número de materias primas y componentes para simplificar la cadena de suministro"}
  ],
  "correcta": "b",
  "explicacion": "El diseño modular diseña conjuntos estandarizados (módulos) comunes a varios productos, que se diferenciarán unos de otros solo en el ensamble final. Así se reducen costos y se responde a la diversidad que proponen los mercados actuales. La 'simplificación' (opción d) es otro concepto distinto."
},
{
  "id": "q027",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "La curva de la bañadera (tasa de fallas vs tiempo de operación) tiene tres zonas. ¿En qué orden correcto se presentan?",
  "opciones": [
    {"id": "a", "texto": "Período normal → Mortalidad infantil → Salida de uso"},
    {"id": "b", "texto": "Mortalidad infantil → Período normal → Salida de uso"},
    {"id": "c", "texto": "Salida de uso → Período normal → Mortalidad infantil"},
    {"id": "d", "texto": "Mortalidad infantil → Salida de uso → Período normal"}
  ],
  "correcta": "b",
  "explicacion": "La curva de la bañadera (para productos durables) comienza con alta tasa de fallas en la zona de 'mortalidad infantil' (fallas tempranas de fabricación), luego baja a un período de 'operación normal' con tasa baja y estable, y finalmente sube en la zona de 'salida de uso' (desgaste acumulado). La forma de bañadera es alta-baja-alta."
},
{
  "id": "q028",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuáles son los tres niveles de packaging en orden desde el más cercano al producto hasta el de distribución?",
  "opciones": [
    {"id": "a", "texto": "Embalaje → Empaque → Envase"},
    {"id": "b", "texto": "Envase → Empaque → Embalaje"},
    {"id": "c", "texto": "Empaque → Envase → Embalaje"},
    {"id": "d", "texto": "Envase → Embalaje → Empaque"}
  ],
  "correcta": "b",
  "explicacion": "1) Envase: en contacto directo con el producto. 2) Empaque: protege al envase. 3) Embalaje: agrupa una cantidad de productos para transporte y distribución. El etiquetado es un elemento adicional del packaging, no es un nivel estructural."
},
{
  "id": "q029",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál de las siguientes características diferenciales del servicio como producto intangible es la más capciosa para confundir con un bien físico?",
  "opciones": [
    {"id": "a", "texto": "Imposibilidad de almacenamiento"},
    {"id": "b", "texto": "No se puede dar muestras por anticipado"},
    {"id": "c", "texto": "Necesidad de suministro en el lugar donde se encuentra el consumidor"},
    {"id": "d", "texto": "No existe posibilidad de reparación, devolución o reventa"}
  ],
  "correcta": "d",
  "explicacion": "La imposibilidad de reparación, devolución o reventa es altamente diferenciadora: un plazo fijo ya ejecutado o un servicio ya prestado no puede 'devolvérsele' al productor. Esto contrasta fuertemente con los bienes físicos que sí admiten devolución o reventa. Las otras opciones también son válidas pero esta es conceptualmente más profunda."
},
{
  "id": "q030",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "¿Cuándo es conveniente adoptar una estrategia de producto ADAPTATIVA (en lugar de proactiva)?",
  "opciones": [
    {"id": "a", "texto": "Cuando la empresa tiene recursos financieros abundantes y quiere crecer agresivamente"},
    {"id": "b", "texto": "Cuando el mercado es muy pequeño para recuperar costos de desarrollo, o cuando no hay forma de proteger la innovación"},
    {"id": "c", "texto": "Cuando la empresa quiere patentar su innovación y posicionarse antes que la competencia"},
    {"id": "d", "texto": "Cuando se tiene política agresiva de crecimiento y se apunta a grandes volúmenes"}
  ],
  "correcta": "b",
  "explicacion": "La estrategia adaptativa conviene cuando: el mercado es pequeño (no se recuperan costos de desarrollo, ej.: Argentina para autos), no hay protección posible para la innovación, la empresa no cuenta con recursos suficientes, o está fuerte en el manejo de sus productos vigentes. La estrategia proactiva requiere recursos y protección de la innovación."
},
{
  "id": "q031",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "relacion",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "Relacioná cada tipo de innovación con su ejemplo correcto según el material.",
  "columna_izq": [
    {"id": "1", "texto": "Innovación arquitectural"},
    {"id": "2", "texto": "Innovación por creación de nicho"},
    {"id": "3", "texto": "Innovación corriente"},
    {"id": "4", "texto": "Innovación revolucionaria"}
  ],
  "columna_der": [
    {"id": "x", "texto": "Computadora personal, Ford T, transistor"},
    {"id": "y", "texto": "Walkman, GPS en autos"},
    {"id": "z", "texto": "Motor a pistón en aviones comerciales post-2ª GM"},
    {"id": "w", "texto": "Computador 360 IBM"}
  ],
  "correcta": {"1": "x", "2": "y", "3": "z", "4": "w"},
  "explicacion": "Arquitectural: reestructura sistemas productivos Y relaciones de mercado (PC, Ford T). Nicho: combina tecnología existente con factor sorpresa en el mercado (Walkman). Corriente: mejoras menores de productividad (motor a pistón). Revolucionaria: nueva tecnología en mercados actuales, obsoleta las soluciones existentes (IBM 360)."
},
{
  "id": "q032",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué herramienta tecnológica es esencial para el diseñador de productos moderno, ya que ejecuta cálculos, visualizaciones y simulaciones con gran velocidad?",
  "opciones": [
    {"id": "a", "texto": "ERP (Enterprise Resource Planning)"},
    {"id": "b", "texto": "CAD (Diseño Asistido por Computadora)"},
    {"id": "c", "texto": "MRP (Material Requirements Planning)"},
    {"id": "d", "texto": "SCADA (Supervisory Control and Data Acquisition)"}
  ],
  "correcta": "b",
  "explicacion": "El CAD (Computer-Aided Design) es esencial para el diseñador: ejecuta cálculos, visualizaciones y simulaciones con gran velocidad, liberando tiempo para la creatividad. Los ajustes quedan disponibles en archivos digitales para todos los sectores involucrados. ERP y MRP son para planificación de recursos y materiales, no para diseño."
},
{
  "id": "q033",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "Los servicios explícitos de una empresa de servicios son los beneficios psicológicos que el consumidor percibe y que valora, aunque no cambien la esencia del servicio (ej: copa de bienvenida en hotel).",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Los servicios IMPLÍCITOS son los beneficios psicológicos que el consumidor puede percibir (copa de bienvenida, café en peluquería, privacidad de oficina). Los servicios EXPLÍCITOS son los directamente relacionados con la esencia de la actividad (puntualidad y seguridad en línea aérea, celeridad en bomberos)."
},
{
  "id": "q034",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "¿Cuál de los siguientes casos NO puede ser un producto con ciclo de vida 'sin declinación'?",
  "opciones": [
    {"id": "a", "texto": "Un bien que se convierte en básico o commodity y perdura en madurez prolongada"},
    {"id": "b", "texto": "Un servicio esencial con demanda permanente como el agua potable"},
    {"id": "c", "texto": "Un producto de moda que alcanza su pico de ventas y luego cae abruptamente"},
    {"id": "d", "texto": "Un producto industrial estandarizado que se mantiene como referencia del mercado"}
  ],
  "correcta": "c",
  "explicacion": "Un producto de moda que tiene un pico abrupto y luego cae sí tiene declinación. La 'no declinación' ocurre cuando el producto se convierte en bien o servicio básico y perdura mostrando una madurez prolongada en su curva de ciclo de vida. Los productos de moda son el ejemplo opuesto: tienen ciclos cortos y caídas pronunciadas."
},
{
  "id": "q035",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "La 'tensión' en una organización, en el contexto de la innovación, se define como:",
  "opciones": [
    {"id": "a", "texto": "El conflicto entre el equipo de diseño y el de producción por recursos escasos"},
    {"id": "b", "texto": "La diferencia entre el nivel de aspiración y el nivel de realización"},
    {"id": "c", "texto": "La presión comercial de competidores que lanzan productos nuevos"},
    {"id": "d", "texto": "El estrés generado por plazos de desarrollo muy ajustados"}
  ],
  "correcta": "b",
  "explicacion": "La 'tensión' es la diferencia entre nivel de aspiración y nivel de realización. La innovación será rápida y vigorosa cuando esta tensión no sea ni demasiado alta (genera frustración) ni demasiado baja (genera apatía). El nivel de aspiración tiende a ajustarse al nivel de realización con el tiempo."
},
{
  "id": "q036",
  "tema": "Unidad 2: Ingeniería de Producto",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "Las cinco etapas del desarrollo de productos en orden correcto son:",
  "opciones": [
    {"id": "a", "texto": "Diseño → Identificación → Prueba → Especificación → Introducción"},
    {"id": "b", "texto": "Identificación de oportunidades → Diseño → Prueba → Especificación → Introducción"},
    {"id": "c", "texto": "Prueba → Diseño → Especificación → Identificación → Introducción"},
    {"id": "d", "texto": "Identificación → Especificación → Diseño → Prueba → Introducción"}
  ],
  "correcta": "b",
  "explicacion": "Las 5 etapas son: 1) Identificación de oportunidades (ideas, tamización), 2) Diseño (comercial, producción, económico-financiero), 3) Prueba (desempeño operativo y reacciones de consumidores), 4) Especificación (planos, fórmulas, listas), 5) Introducción (lanzamiento al mercado). Hay realimentación entre prueba y diseño, y entre introducción y diseño."
},

# ─────────────────────────────────────────────
# UNIDAD 3: INGENIERÍA DE PROCESO (18 preguntas)
# ─────────────────────────────────────────────
{
  "id": "q037",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál de las siguientes es una característica del flujo CONTINUO (capital intensivo) que NO se aplica al flujo intermitente?",
  "opciones": [
    {"id": "a", "texto": "Maquinaria universal y versátil para distintas tareas"},
    {"id": "b", "texto": "Lay out por producto con secuencia preestablecida"},
    {"id": "c", "texto": "Alto inventario en proceso y bajo en producto terminado"},
    {"id": "d", "texto": "Set up de alta frecuencia y costos elevados"}
  ],
  "correcta": "b",
  "explicacion": "El flujo continuo usa layout por PRODUCTO (secuencia fija y ordenada). El flujo intermitente usa layout por PROCESO o funcional. La maquinaria universal y versátil es del flujo intermitente. El alto inventario en proceso (y bajo en terminado) también es del intermitente. El set up frecuente y costoso es del intermitente (en continuo el set up es prolongado pero de baja frecuencia)."
},
{
  "id": "q038",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "En un sistema de producción continua, el control de calidad se realiza por órdenes según las especificaciones de cada producto.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. En producción CONTINUA, el control de calidad se realiza por métodos estadísticos (porque el alto volumen lo hace necesario y viable). El control por órdenes según especificaciones de cada producto es característico del flujo INTERMITENTE, donde cada orden puede tener diferentes especificaciones."
},
{
  "id": "q039",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuáles son las actividades que AGREGAN VALOR en un proceso productivo?",
  "opciones": [
    {"id": "a", "texto": "Contar, mover, almacenar, controlar"},
    {"id": "b", "texto": "Fundir, mezclar, soldar, moldear, cortar"},
    {"id": "c", "texto": "Inspeccionar, transportar, esperar, almacenar"},
    {"id": "d", "texto": "Planificar, programar, controlar, supervisar"}
  ],
  "correcta": "b",
  "explicacion": "Solo las actividades que producen transformación física del producto agregan valor: fundir, mezclar, soldar, moldear, cortar. Las actividades de contar, mover, almacenar y controlar agregan COSTO pero no valor. La consigna del diseño de procesos es que la mayor parte de las actividades agreguen valor."
},
{
  "id": "q040",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "El sistema Kanban en el contexto del diseño de procesos JIT se utiliza principalmente para:",
  "opciones": [
    {"id": "a", "texto": "Controlar la calidad estadística de los productos terminados"},
    {"id": "b", "texto": "Pedir a la sección anterior los insumos necesarios para producir un lote, especialmente en la parte más lenta del proceso"},
    {"id": "c", "texto": "Gestionar el mantenimiento preventivo de las máquinas en líneas automatizadas"},
    {"id": "d", "texto": "Registrar los tiempos de set up y calcular el tiempo estándar de cada operación"}
  ],
  "correcta": "b",
  "explicacion": "El Kanban son tarjetas de requisición que se usan para pedir a la sección anterior los insumos necesarios para producir un lote. Se aplica en líneas de montaje en la parte más lenta del proceso que funciona con flujo intermitente (alto stock en proceso). Es una herramienta del JIT para controlar el flujo de producción."
},
{
  "id": "q041",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "La fórmula de eficiencia y productividad según el material son conceptos distintos. ¿Cuál de las siguientes afirmaciones es CORRECTA?",
  "opciones": [
    {"id": "a", "texto": "Eficiencia = tiempo trabajado / tiempo presente; Productividad = tiempo estándar / tiempo empleado"},
    {"id": "b", "texto": "Eficiencia = tiempo estándar / tiempo empleado (medida interna); Productividad = tiempo trabajado / tiempo presente (comparación externa)"},
    {"id": "c", "texto": "Ambos conceptos miden lo mismo pero con distintas unidades de medición"},
    {"id": "d", "texto": "Productividad = salida / capital (única forma de medirla); Eficiencia es solo cualitativa"}
  ],
  "correcta": "b",
  "explicacion": "Eficiencia = tiempo estándar / tiempo empleado (%). Es una medida interna que cuantifica el cumplimiento de un estándar. Productividad = tiempo trabajado / tiempo presente. Es un indicador para comparar performance hacia afuera de la organización. También puede expresarse como medidas parciales (salida/trabajo), múltiples o totales."
},
{
  "id": "q042",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "La 'visión integral' del proceso productivo plantea la relación P/D = 1. ¿Qué representa P y qué representa D?",
  "opciones": [
    {"id": "a", "texto": "P = precio de venta; D = demanda del mercado"},
    {"id": "b", "texto": "P = tiempo de la empresa (abastecimiento + producción + entrega); D = tiempo visto por el cliente (pedido + venta + producción + entrega)"},
    {"id": "c", "texto": "P = productividad de la planta; D = disponibilidad de equipos"},
    {"id": "d", "texto": "P = plazos de fabricación; D = días de inventario en proceso"}
  ],
  "correcta": "b",
  "explicacion": "P = tiempo total de la empresa = abastecimiento + producción + entrega. D = tiempo visto por el cliente = pedido + venta + producción + entrega. El objetivo P/D = 1 significa que el sistema de producción puede operar justo a tiempo (JIT) en respuesta a los pedidos de los clientes, eliminando el 'inventario invisible'."
},
{
  "id": "q043",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuántas condiciones deben cumplirse para decidir implementar un proceso de flujo continuo?",
  "opciones": [
    {"id": "a", "texto": "Dos: alto volumen y producto estandarizado"},
    {"id": "b", "texto": "Tres: volumen adecuado, demanda estable y alta estandarización del producto"},
    {"id": "c", "texto": "Cinco: volumen adecuado, demanda estable, alta estandarización, intercambiabilidad de partes y suministro ininterrumpido de MP"},
    {"id": "d", "texto": "Una sola: que el volumen de producción justifique la inversión en equipos"}
  ],
  "correcta": "c",
  "explicacion": "Para decidir un proceso con flujo continuo se deben cumplir 5 condiciones: 1) volumen adecuado que sature el proceso, 2) demanda razonablemente estable, 3) producto con alta estandarización, 4) intercambiabilidad de partes y 5) suministro ininterrumpido de materia prima."
},
{
  "id": "q044",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Una fábrica produce muebles de mediana estandarización en volúmenes medios. Si en la matriz producto-proceso se ubica en la celda de 'Línea de montaje' (flujo regular conectado), ¿cuál es la interpretación correcta?",
  "opciones": [
    {"id": "a", "texto": "La empresa está correctamente posicionada, cercana a la diagonal"},
    {"id": "b", "texto": "La empresa está a la izquierda de la diagonal: aplica tecnología demasiado avanzada para ese tipo de producto"},
    {"id": "c", "texto": "La empresa está a la derecha de la diagonal: tiene atraso tecnológico respecto al tipo de producto"},
    {"id": "d", "texto": "La empresa necesita migrar hacia un proceso de planta procesadora"}
  ],
  "correcta": "b",
  "explicacion": "Muebles de mediana estandarización/volumen medio corresponde a la diagonal cerca del 'taller' (flujo irregular por lotes). Si la empresa usa 'línea de montaje' (flujo regular conectado), está a la IZQUIERDA de la diagonal: aplica tecnología demasiado avanzada respecto al desarrollo del producto. Esto puede ser costoso e innecesario."
},
{
  "id": "q045",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Quién pone el foco en el cambio rápido de herramientas, orientando los tiempos de preparación a 'un dígito' (menos de 10 minutos)?",
  "opciones": [
    {"id": "a", "texto": "Frederick Taylor (tiempos y movimientos)"},
    {"id": "b", "texto": "Shigeo Shingo (SMED - Single Minute Exchange of Die)"},
    {"id": "c", "texto": "Henry Ford (producción en línea continua)"},
    {"id": "d", "texto": "Edward Deming (mejora continua y PDCA)"}
  ],
  "correcta": "b",
  "explicacion": "Shigeo Shingo pone su foco en el cambio rápido de herramientas. Los japoneses se orientaron a tiempos de preparación de un dígito (menos de 10 minutos). Antes, el set up se consideraba un 'mal necesario' y se programaban tiradas largas para minimizar su impacto; Shingo demostró que puede reducirse drásticamente."
},
{
  "id": "q046",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "verdadero_falso",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "En la matriz de prestación de servicios, un hospital se clasifica como 'fábrica de servicios' por ser capital intensivo con alta interacción con el cliente.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "f",
  "explicacion": "Falso. Un hospital es un 'TALLER DE SERVICIOS' (capital intensivo + ALTA interacción con el cliente). La 'fábrica de servicios' es capital intensivo + BAJA interacción (aerolíneas, hoteles, fletes). Confundir estos dos es el error frecuente: el hospital tiene alta tecnología (capital) pero también alta personalización del servicio."
},
{
  "id": "q047",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Cuántos aspectos o decisiones involucra el diseño del proceso según el material?",
  "opciones": [
    {"id": "a", "texto": "10 aspectos"},
    {"id": "b", "texto": "20 aspectos"},
    {"id": "c", "texto": "32 aspectos"},
    {"id": "d", "texto": "7 aspectos (las 7S del proceso)"}
  ],
  "correcta": "c",
  "explicacion": "El diseño del proceso involucra 32 aspectos a estudiar, desde la elección de tecnología y división de operaciones hasta la compatibilización de inversiones, tiempo de diseño y recursos a invertir. Esta amplitud refleja la complejidad de diseñar un sistema de producción completo."
},
{
  "id": "q048",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuál es la ventaja de las células en 'U' respecto a otras configuraciones de lay out?",
  "opciones": [
    {"id": "a", "texto": "Permiten producción continua de grandes volúmenes con maquinaria especializada"},
    {"id": "b", "texto": "El operario tiene todo a mano e incluso puede atender 2 máquinas simultáneamente, eliminando transportes"},
    {"id": "c", "texto": "Centralizan el mantenimiento en un taller único reduciendo los costos de reparación"},
    {"id": "d", "texto": "Facilitan el control estadístico de calidad en líneas de alta velocidad"}
  ],
  "correcta": "b",
  "explicacion": "Las células en 'U' se diseñan para que todo esté a mano del operario, quien incluso puede atender 2 máquinas simultáneamente, eliminando transportes innecesarios. Son grupos compactos y flexibles con mayor retroalimentación entre integrantes. Son parte del enfoque JIT."
},
{
  "id": "q049",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "La curva de aprendizaje en la implementación de un nuevo proceso implica que:",
  "opciones": [
    {"id": "a", "texto": "Los tiempos estándar deben fijarse desde el primer día para incentivar al personal a mejorar"},
    {"id": "b", "texto": "Hay un período de gradualidad hasta alcanzar los valores de eficiencia y tiempos estándar esperados"},
    {"id": "c", "texto": "La eficiencia cae permanentemente después de instalar un nuevo proceso por la resistencia al cambio"},
    {"id": "d", "texto": "El nuevo proceso siempre es más eficiente que el anterior desde el primer día de operación"}
  ],
  "correcta": "b",
  "explicacion": "La curva de aprendizaje implica un período de gradualidad: cuando se implementa un nuevo proceso, los tiempos insumidos comienzan altos y van bajando progresivamente hasta alcanzar los valores estándar de eficiencia. Por eso en la implementación se debe prever este período y dar la asistencia necesaria a producción."
},
{
  "id": "q050",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": False,
  "enunciado": "¿Cuáles son los beneficios de reducir el tiempo de set up?",
  "opciones": [
    {"id": "a", "texto": "Mayor aprovechamiento de equipos, menores plazos de fabricación, mayor adaptación a pedidos y reducción de stocks"},
    {"id": "b", "texto": "Reducción de la mano de obra directa y posibilidad de usar maquinaria más antigua"},
    {"id": "c", "texto": "Aumento del tamaño de lote, mayor estandarización de productos y reducción de variedad"},
    {"id": "d", "texto": "Menores costos de mantenimiento preventivo y mayor vida útil de los equipos"}
  ],
  "correcta": "a",
  "explicacion": "Los beneficios de reducir el set up son: mejor aprovechamiento de equipos y aumento de capacidad de producción, acortamiento de plazos de fabricación, mayor adaptación a pedidos de clientes y variaciones de demanda, y reducción de stocks en proceso y producto terminado. Es uno de los pilares del sistema JIT."
},
{
  "id": "q051",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "facil",
  "capciosa": False,
  "enunciado": "¿Qué es el muestreo de trabajo y para qué se utiliza?",
  "opciones": [
    {"id": "a", "texto": "Un método de control de calidad que toma muestras del producto terminado"},
    {"id": "b", "texto": "Un método estadístico de observaciones aleatorias para determinar proporciones de tiempo productivo, accesorio y no productivo"},
    {"id": "c", "texto": "Un sistema de incentivos basado en muestras de rendimiento del personal"},
    {"id": "d", "texto": "Una técnica de selección de personal mediante pruebas de desempeño en tareas reales"}
  ],
  "correcta": "b",
  "explicacion": "El muestreo de trabajo se basa en métodos estadísticos con observaciones al AZAR del personal respecto a: tiempo de trabajo productivo, trabajo accesorio/colateral, no productivo o ausencia del área. Se usa para determinar la eficiencia en tareas intermitentes con gran variabilidad donde no es viable el cronometraje continuo."
},
{
  "id": "q052",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "verdadero_falso",
  "dificultad": "dificil",
  "capciosa": True,
  "enunciado": "Si en un proceso capital intensivo (automatizado) el equipo fija el ritmo de producción, el diseño del proceso se determina principalmente por las especificaciones de operación de los equipos, no por la metodología del diseño de la mano de obra.",
  "opciones": [
    {"id": "v", "texto": "Verdadero"},
    {"id": "f", "texto": "Falso"}
  ],
  "correcta": "v",
  "explicacion": "Verdadero. En procesos capital intensivos, el proceso es establecido por la tecnología y las tareas de los trabajadores quedan determinadas por las especificaciones de operación de los equipos. La metodología de 7 pasos (planteo, relevamiento, análisis, etc.) se aplica principalmente cuando es mano de obra intensiva."
},
{
  "id": "q053",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "dificil",
  "capciosa": False,
  "enunciado": "La 'industrialización de los servicios' combina tecnologías duras y suaves. ¿Cuál es la consecuencia negativa más relevante de esta tendencia?",
  "opciones": [
    {"id": "a", "texto": "Aumenta los costos operativos por la alta inversión en automatización"},
    {"id": "b", "texto": "El diseño estandarizado mejora calidad pero los clientes se cansan de la uniformidad y los empleados se sienten 'robotizados'"},
    {"id": "c", "texto": "Disminuye la productividad porque el cliente participa menos en la prestación"},
    {"id": "d", "texto": "Genera mayor variabilidad en el servicio por la dependencia de la tecnología"}
  ],
  "correcta": "b",
  "explicacion": "La industrialización de los servicios mejora costos, calidad y productividad, pero el diseño estandarizado se aleja de la prestación a medida: los clientes comienzan a cansarse de la uniformidad y la sustitución del trato personalizado, y los empleados se sienten 'robotizados'. Es la tensión entre eficiencia y personalización."
},
{
  "id": "q054",
  "tema": "Unidad 3: Ingeniería de Proceso",
  "tipo": "opcion_multiple",
  "dificultad": "media",
  "capciosa": True,
  "enunciado": "Una acción para reducir el tiempo de set up es 'efectuar en paralelo algunas tareas'. ¿Qué se gana y qué NO se gana con esta acción?",
  "opciones": [
    {"id": "a", "texto": "Se gana el tiempo total del set up; NO se gana tiempo de máquina productiva"},
    {"id": "b", "texto": "Se gana tiempo de set up (se reduce la duración del mismo); NO se gana el tiempo total (la suma de tareas es la misma)"},
    {"id": "c", "texto": "Se gana producción adicional; NO se reduce el costo de mano de obra del set up"},
    {"id": "d", "texto": "Se gana precisión en los ajustes; NO se reduce el número de operaciones de set up"}
  ],
  "correcta": "b",
  "explicacion": "Ejecutar tareas de set up en paralelo reduce la duración total del set up (el tiempo que la máquina está parada), pero NO reduce el tiempo total de trabajo invertido (la suma de horas-hombre es la misma o similar). La ganancia es en disponibilidad de la máquina, no en el esfuerzo total aplicado."
},
]

print(json.dumps(preguntas, ensure_ascii=False, indent=2))
