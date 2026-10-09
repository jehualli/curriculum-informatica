# -*- coding: utf-8 -*-
import os, plantilla, cursos_a, cursos_b, cursos_c, cursos_d

SALIDA = os.path.join(os.path.dirname(__file__), "..", "programas")
todos = cursos_a.CURSOS + cursos_b.CURSOS + cursos_c.CURSOS + cursos_d.CURSOS
todos.sort(key=lambda c: c["clave"])

for c in todos:
    suma = sum(u["horas"] for u in c["contenido"])
    pct = sum(v for _, v in c["criterios"])
    assert suma == c["total"] == 68, f"{c['clave']}: horas {suma} vs {c['total']}"
    assert pct == 100, f"{c['clave']}: criterios suman {pct}"
    ruta = os.path.join(SALIDA, c["archivo"])
    open(ruta, "w", encoding="utf-8").write(plantilla.render(c))
    print(f"  {c['clave']}  {c['nombre'][:44]:46} {suma} h  {c['creditos']} cr")

print(f"\n{len(todos)} programas generados · {sum(c['creditos'] for c in todos)} créditos")
