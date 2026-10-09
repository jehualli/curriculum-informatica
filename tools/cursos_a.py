# -*- coding: utf-8 -*-
CURSOS = [
{
 "archivo": "I5916-desarrollo-colaborativo-control-de-versiones.md",
 "nombre": "Desarrollo Colaborativo y Control de Versiones",
 "clave": "I5916", "modalidad": "Escolarizada",
 "tipo": "Seminario de solución de problemas", "creditos": 5,
 "area": "Básica particular obligatoria",
 "hora_semana": 4, "teoria": 0, "practica": 68, "total": 68,
 "seriacion": "N/A (se cursa junto con Programación, I5882)",
 "departamento": "Ciencias Computacionales", "academia": "Programación",
 "presentacion": """
Ningún programa del plan vigente menciona el control de versiones. En la
práctica el estudiante organiza su trabajo en carpetas numeradas, pierde
estados anteriores, intercambia archivos por mensajería y resuelve la
integración copiando y pegando. El problema se vuelve visible hasta los
Proyectos Modulares, cuando ya hay que trabajar en equipo y el costo de no
saberlo es alto.

Esta unidad se ubica en primer semestre de manera deliberada: el control de
versiones no es una herramienta avanzada, es la forma en que se guarda el
trabajo. Aprenderlo antes que cualquier otra práctica de ingeniería permite
que las materias posteriores lo den por supuesto y lo exijan como forma normal
de entrega. Se imparte sin horas de teoría: todo el contenido se trabaja sobre
repositorios reales, incluidos ejercicios de recuperación de errores cometidos
a propósito.
""",
 "competencia": """
Gestiona la evolución del código propio y de equipo mediante un sistema de
control de versiones distribuido, integrando cambios de varios autores,
recuperando estados anteriores y sosteniendo un historial legible que sirva
como documentación del proyecto.
""",
 "saber": ["Modelo de datos de un repositorio distribuido: instantáneas, confirmaciones y referencias",
           "Diferencia entre historial local y remoto",
           "Estrategias de integración y su efecto sobre el historial"],
 "saber_hacer": ["Versionar un proyecto desde su inicio y trabajar en ramas",
                 "Resolver conflictos de fusión",
                 "Revisar el trabajo de otra persona y recuperar estados perdidos"],
 "saber_ser": ["Escribe mensajes que explican la intención del cambio",
               "Revisa el trabajo ajeno con rigor y sin hostilidad",
               "Acepta observaciones sobre el trabajo propio como parte del proceso"],
 "comp_generica": "Capacidad de trabajo en equipo y de comunicación técnica escrita.",
 "comp_profesional": "Gestión disciplinada del código fuente a lo largo del ciclo de vida de un sistema.",
 "previas": ["Manejo básico de sistema de archivos y línea de comandos",
             "Nociones elementales de programación (cursada en paralelo)"],
 "perfil_egreso": """
Contribuye al egresado capaz de incorporarse a un equipo de desarrollo y
producir software de manera colaborativa, con trazabilidad de los cambios y
responsabilidad sobre el trabajo compartido.
""",
 "perfil_docente": """
Ingeniero o licenciado del área de cómputo con experiencia demostrable en
equipos de desarrollo que usen control de versiones distribuido de forma
cotidiana. Se valora la experiencia en revisión de código entre pares.
""",
 "contenido": [
  {"titulo":"Por qué el código necesita historia","horas":4,
   "temas":["Pérdida de trabajo y versiones paralelas","Integración manual y sus fallas",
            "Panorama histórico: de la copia con fecha al repositorio distribuido"]},
  {"titulo":"Fundamentos del repositorio","horas":10,
   "temas":["Repositorio, copia de trabajo y área de preparación","Estados de un archivo",
            "Confirmaciones y navegación del historial","Ignorar archivos y contenido que no se versiona"]},
  {"titulo":"Ramas y fusión","horas":12,
   "temas":["Creación y cambio de contexto","Fusión y sus estrategias",
            "Conflictos: origen, lectura y resolución","Etiquetas y marcado de versiones"]},
  {"titulo":"Repositorios remotos y flujos de trabajo","horas":10,
   "temas":["Sincronización con un remoto","Flujo de rama única y flujo de ramas de función",
            "Bifurcaciones y contribución externa","Protección de ramas y permisos"]},
  {"titulo":"Revisión de código","horas":10,
   "temas":["Solicitudes de integración","Qué observar y cómo redactar una observación",
            "Criterios de aceptación y tamaño del cambio","Revisión como registro de decisiones"]},
  {"titulo":"Historial legible","horas":8,
   "temas":["Mensajes de confirmación: intención sobre mecánica",
            "Reorganización y combinación de cambios","Cuándo no reescribir el historial"]},
  {"titulo":"Recuperación de estados","horas":8,
   "temas":["Deshacer, revertir y restablecer","Registro de referencias",
            "Búsqueda binaria del cambio que introdujo un defecto","Rescate de trabajo no confirmado"]},
  {"titulo":"Convenciones de equipo","horas":6,
   "temas":["Acuerdos de nombrado y de integración","Preparación del repositorio del Proyecto Modular",
            "Documentación mínima del repositorio"]},
 ],
 "estrategias": ["Práctica guiada sobre repositorios reales desde la primera sesión.",
   "Ejercicios de recuperación: el profesor entrega repositorios dañados a propósito y el estudiante los restaura.",
   "Trabajo en parejas con intercambio obligatorio de los roles de autor y revisor.",
   "Integración con Programación (I5882): a partir de la cuarta semana las entregas de esa materia se reciben por repositorio."],
 "bib_basica": ["Chacon, S. y Straub, B. (2014). *Pro Git* (2a ed.). Apress. Disponible en línea sin costo.",
   "Documentación oficial de Git: manual de referencia y libro de usuario, versión vigente."],
 "bib_comp": ["Forsgren, N., Humble, J. y Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press.",
   "Humble, J. y Farley, D. (2010). *Continuous Delivery*. Addison-Wesley."],
 "tipo_evaluacion": "Diagnóstica al inicio del curso, formativa en cada práctica semanal y sumativa en el proyecto colaborativo y el examen práctico.",
 "criterios": [("Prácticas semanales (repositorio y bitácora de comandos)",30),
   ("Ejercicios de recuperación de estados perdidos",15),
   ("Calidad de las revisiones de código realizadas a compañeros",15),
   ("Proyecto colaborativo en equipo de tres integrantes",30),
   ("Examen práctico sobre repositorio con conflictos",10)],
 "nota": """
Única propuesta del conjunto que no sustituye contenido existente: se agrega.
También es la más barata del plan —cinco créditos— y la de mayor efecto,
porque habilita la exigencia de trabajo versionado en las quince materias
posteriores y en los tres Proyectos Modulares.
""",
},
]
