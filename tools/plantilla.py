# -*- coding: utf-8 -*-
"""Renderiza un programa de unidad de aprendizaje con la estructura y el
orden de secciones que usan los programas oficiales del plan 2015B."""

def render(c):
    o = []
    w = o.append

    w("> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación")
    w("> con la Universidad de Guadalajara. La clave, la seriación y la ubicación")
    w("> semestral son propuestas del ejercicio.\n")

    w("*[Aquí va el bloque de Misión del Centro Universitario que encabeza los")
    w("programas oficiales.]*\n")

    w("## 1.- Identificación de la Unidad de Aprendizaje\n")
    w("### Nombre de la Unidad de Aprendizaje\n")
    w(f"**{c['nombre'].upper()}**\n")

    w("| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |")
    w("|---|---|---|---|---|")
    w(f"| {c['clave']} | {c['modalidad']} | {c['tipo']} | {c['creditos']} | {c['area']} |\n")

    w("| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |")
    w("|---|---|---|---|---|")
    w(f"| {c['hora_semana']} | {c['teoria']} | {c['practica']} | {c['total']} | {c['seriacion']} |\n")

    w("| Departamento | Academia |")
    w("|---|---|")
    w(f"| {c['departamento']} | {c['academia']} |\n")

    w("### Presentación\n")
    w(c["presentacion"].strip() + "\n")

    w("### Competencia de la Unidad de Aprendizaje (UA)\n")
    w(c["competencia"].strip() + "\n")

    w("### Tipos de saberes\n")
    w("| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |")
    w("|---|---|---|")
    n = max(len(c["saber"]), len(c["saber_hacer"]), len(c["saber_ser"]))
    for i in range(n):
        a = c["saber"][i] if i < len(c["saber"]) else ""
        b = c["saber_hacer"][i] if i < len(c["saber_hacer"]) else ""
        d = c["saber_ser"][i] if i < len(c["saber_ser"]) else ""
        w(f"| {a} | {b} | {d} |")
    w("")

    w("| Competencia genérica | Competencia profesional |")
    w("|---|---|")
    w(f"| {c['comp_generica']} | {c['comp_profesional']} |\n")

    w("### Competencias previas del alumno\n")
    for x in c["previas"]:
        w(f"- {x}")
    w("")

    w("### Competencia del perfil de egreso\n")
    w(c["perfil_egreso"].strip() + "\n")

    w("### Perfil deseable del docente\n")
    w(c["perfil_docente"].strip() + "\n")

    w("## 2.- Contenidos temáticos\n")
    w("### Contenido\n")
    suma = 0
    for i, u in enumerate(c["contenido"], 1):
        suma += u["horas"]
        w(f"**UNIDAD {roman(i)}. {u['titulo']} — {u['horas']} horas**\n")
        for j, s in enumerate(u["temas"], 1):
            w(f"&nbsp;&nbsp;{i}.{j} {s}")
        w("")
    w(f"**Total: {suma} horas**\n")

    w("### Estrategias docentes para impartir la unidad de aprendizaje\n")
    for x in c["estrategias"]:
        w(f"- {x}")
    w("")

    w("### Bibliografía básica\n")
    for i, x in enumerate(c["bib_basica"], 1):
        w(f"{i}. {x}")
    w("")

    w("### Bibliografía complementaria\n")
    for i, x in enumerate(c["bib_comp"], 1):
        w(f"{i}. {x}")
    w("")

    w("## 3.- Evaluación\n")
    w("### Tipo de evaluación\n")
    w(c["tipo_evaluacion"].strip() + "\n")

    w("### Criterios de Evaluación (% por criterio)\n")
    w("| Criterio | Porcentaje |")
    w("|---|---:|")
    t = 0
    for k, v in c["criterios"]:
        t += v
        w(f"| {k} | {v} |")
    w(f"| **Total** | **{t}** |\n")

    w("### Acreditación\n")
    w("**Ordinaria.** Conforme al Reglamento General de Evaluación y Promoción")
    w("de Alumnos de la Universidad de Guadalajara, artículo 20: se requiere")
    w("estar inscrito en el plan de estudios y curso correspondiente y contar con")
    w("un mínimo de 80 % de asistencia a las clases y actividades del curso.\n")
    w("**Extraordinaria.** Conforme al artículo 25 del mismo reglamento, con la")
    w("ponderación que éste establece entre el resultado del periodo")
    w("extraordinario y la calificación obtenida en el ordinario.\n")
    w("Reglamento: <http://www.secgral.udg.mx/sites/archivos/normatividad/general/ReglamentoGralEPAlumnos.pdf>\n")

    w("---\n")
    w("### Nota de diseño (no forma parte del formato oficial)\n")
    w(c["nota"].strip() + "\n")
    return "\n".join(o)


def roman(n):
    return ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"][n]
