"""Ensambla las 3 partes en data/questions.json y valida."""
import json, sys, os

# Importar las partes
sys.path.insert(0, os.path.dirname(__file__))

parts = []
for fname in ['gen_q_part1.py', 'gen_q_part2.py', 'gen_q_part3.py']:
    path = os.path.join(os.path.dirname(__file__), fname)
    ns = {}
    exec(open(path, encoding='utf-8').read().replace('print(json.dumps(preguntas, ensure_ascii=False, indent=2))', ''), ns)
    parts.extend(ns['preguntas'])

# Estructura final
temas = [
    "Unidad 1: Localización",
    "Unidad 2: Ingeniería de Producto",
    "Unidad 3: Ingeniería de Proceso",
    "Unidad 4: Layout",
    "Unidad 5: Estudio del Trabajo",
    "Unidad 6: Estudio de Métodos",
    "Unidad 7: Medición del Trabajo",
    "Unidad 8: Organización del Mantenimiento",
    "Unidad 9: Manipulación de Materiales",
    "Unidad 10: Organización de la Manufactura"
]

data = {
    "materia": "Organización Industrial",
    "generado_desde": "resumen.pdf",
    "version": "1.0",
    "temas": temas,
    "preguntas": parts
}

# VALIDACIÓN
ids = [p['id'] for p in parts]
assert len(ids) == len(set(ids)), f"IDs duplicados: {[i for i in ids if ids.count(i)>1]}"
for p in parts:
    assert p['tema'] in temas, f"Tema inválido en {p['id']}: {p['tema']}"
    assert 'explicacion' in p and len(p['explicacion']) > 10, f"Sin explicación: {p['id']}"
    if p['tipo'] == 'opcion_multiple':
        opt_ids = [o['id'] for o in p['opciones']]
        assert p['correcta'] in opt_ids, f"Respuesta inválida en {p['id']}: {p['correcta']}"
    elif p['tipo'] == 'verdadero_falso':
        assert p['correcta'] in ('v','f'), f"Respuesta inválida en {p['id']}"
    elif p['tipo'] == 'relacion':
        izq_ids = [o['id'] for o in p['columna_izq']]
        der_ids = [o['id'] for o in p['columna_der']]
        for k,v in p['correcta'].items():
            assert k in izq_ids, f"Key inválida en relacion {p['id']}: {k}"
            assert v in der_ids, f"Value inválido en relacion {p['id']}: {v}"

# Estadísticas
from collections import Counter
print(f"Total preguntas: {len(parts)}")
print(f"Por dificultad: {dict(Counter(p['dificultad'] for p in parts))}")
print(f"Por tipo: {dict(Counter(p['tipo'] for p in parts))}")
print(f"Por tema: {dict(Counter(p['tema'] for p in parts))}")
print(f"Capciosas: {sum(1 for p in parts if p.get('capciosa'))}")
print("✓ Validación OK")

# Guardar
out = os.path.join(os.path.dirname(__file__), '..', 'data', 'questions.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Guardado en: {os.path.abspath(out)}")
