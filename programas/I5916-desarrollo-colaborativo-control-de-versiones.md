> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**DESARROLLO COLABORATIVO Y CONTROL DE VERSIONES**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5916 | Escolarizada | Seminario de solución de problemas | 5 | Básica particular obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 0 | 68 | 68 | N/A (se cursa junto con Programación, I5882) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Programación |

### Presentación

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

### Competencia de la Unidad de Aprendizaje (UA)

Gestiona la evolución del código propio y de equipo mediante un sistema de
control de versiones distribuido, integrando cambios de varios autores,
recuperando estados anteriores y sosteniendo un historial legible que sirva
como documentación del proyecto.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| Modelo de datos de un repositorio distribuido: instantáneas, confirmaciones y referencias | Versionar un proyecto desde su inicio y trabajar en ramas | Escribe mensajes que explican la intención del cambio |
| Diferencia entre historial local y remoto | Resolver conflictos de fusión | Revisa el trabajo ajeno con rigor y sin hostilidad |
| Estrategias de integración y su efecto sobre el historial | Revisar el trabajo de otra persona y recuperar estados perdidos | Acepta observaciones sobre el trabajo propio como parte del proceso |

| Competencia genérica | Competencia profesional |
|---|---|
| Capacidad de trabajo en equipo y de comunicación técnica escrita. | Gestión disciplinada del código fuente a lo largo del ciclo de vida de un sistema. |

### Competencias previas del alumno

- Manejo básico de sistema de archivos y línea de comandos
- Nociones elementales de programación (cursada en paralelo)

### Competencia del perfil de egreso

Contribuye al egresado capaz de incorporarse a un equipo de desarrollo y
producir software de manera colaborativa, con trazabilidad de los cambios y
responsabilidad sobre el trabajo compartido.

### Perfil deseable del docente

Ingeniero o licenciado del área de cómputo con experiencia demostrable en
equipos de desarrollo que usen control de versiones distribuido de forma
cotidiana. Se valora la experiencia en revisión de código entre pares.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. Por qué el código necesita historia — 4 horas**

&nbsp;&nbsp;1.1 Pérdida de trabajo y versiones paralelas
&nbsp;&nbsp;1.2 Integración manual y sus fallas
&nbsp;&nbsp;1.3 Panorama histórico: de la copia con fecha al repositorio distribuido

**UNIDAD II. Fundamentos del repositorio — 10 horas**

&nbsp;&nbsp;2.1 Repositorio, copia de trabajo y área de preparación
&nbsp;&nbsp;2.2 Estados de un archivo
&nbsp;&nbsp;2.3 Confirmaciones y navegación del historial
&nbsp;&nbsp;2.4 Ignorar archivos y contenido que no se versiona

**UNIDAD III. Ramas y fusión — 12 horas**

&nbsp;&nbsp;3.1 Creación y cambio de contexto
&nbsp;&nbsp;3.2 Fusión y sus estrategias
&nbsp;&nbsp;3.3 Conflictos: origen, lectura y resolución
&nbsp;&nbsp;3.4 Etiquetas y marcado de versiones

**UNIDAD IV. Repositorios remotos y flujos de trabajo — 10 horas**

&nbsp;&nbsp;4.1 Sincronización con un remoto
&nbsp;&nbsp;4.2 Flujo de rama única y flujo de ramas de función
&nbsp;&nbsp;4.3 Bifurcaciones y contribución externa
&nbsp;&nbsp;4.4 Protección de ramas y permisos

**UNIDAD V. Revisión de código — 10 horas**

&nbsp;&nbsp;5.1 Solicitudes de integración
&nbsp;&nbsp;5.2 Qué observar y cómo redactar una observación
&nbsp;&nbsp;5.3 Criterios de aceptación y tamaño del cambio
&nbsp;&nbsp;5.4 Revisión como registro de decisiones

**UNIDAD VI. Historial legible — 8 horas**

&nbsp;&nbsp;6.1 Mensajes de confirmación: intención sobre mecánica
&nbsp;&nbsp;6.2 Reorganización y combinación de cambios
&nbsp;&nbsp;6.3 Cuándo no reescribir el historial

**UNIDAD VII. Recuperación de estados — 8 horas**

&nbsp;&nbsp;7.1 Deshacer, revertir y restablecer
&nbsp;&nbsp;7.2 Registro de referencias
&nbsp;&nbsp;7.3 Búsqueda binaria del cambio que introdujo un defecto
&nbsp;&nbsp;7.4 Rescate de trabajo no confirmado

**UNIDAD VIII. Convenciones de equipo — 6 horas**

&nbsp;&nbsp;8.1 Acuerdos de nombrado y de integración
&nbsp;&nbsp;8.2 Preparación del repositorio del Proyecto Modular
&nbsp;&nbsp;8.3 Documentación mínima del repositorio

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Práctica guiada sobre repositorios reales desde la primera sesión.
- Ejercicios de recuperación: el profesor entrega repositorios dañados a propósito y el estudiante los restaura.
- Trabajo en parejas con intercambio obligatorio de los roles de autor y revisor.
- Integración con Programación (I5882): a partir de la cuarta semana las entregas de esa materia se reciben por repositorio.

### Bibliografía básica

1. Chacon, S. y Straub, B. (2014). *Pro Git* (2a ed.). Apress. Disponible en línea sin costo.
2. Documentación oficial de Git: manual de referencia y libro de usuario, versión vigente.

### Bibliografía complementaria

1. Forsgren, N., Humble, J. y Kim, G. (2018). *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press.
2. Humble, J. y Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.

## 3.- Evaluación

### Tipo de evaluación

Diagnóstica al inicio del curso, formativa en cada práctica semanal y sumativa en el proyecto colaborativo y el examen práctico.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Prácticas semanales (repositorio y bitácora de comandos) | 30 |
| Ejercicios de recuperación de estados perdidos | 15 |
| Calidad de las revisiones de código realizadas a compañeros | 15 |
| Proyecto colaborativo en equipo de tres integrantes | 30 |
| Examen práctico sobre repositorio con conflictos | 10 |
| **Total** | **100** |

### Acreditación

**Ordinaria.** Conforme al Reglamento General de Evaluación y Promoción
de Alumnos de la Universidad de Guadalajara, artículo 20: se requiere
estar inscrito en el plan de estudios y curso correspondiente y contar con
un mínimo de 80 % de asistencia a las clases y actividades del curso.

**Extraordinaria.** Conforme al artículo 25 del mismo reglamento, con la
ponderación que éste establece entre el resultado del periodo
extraordinario y la calificación obtenida en el ordinario.

Reglamento: <http://www.secgral.udg.mx/sites/archivos/normatividad/general/ReglamentoGralEPAlumnos.pdf>

---

### Nota de diseño (no forma parte del formato oficial)

Única propuesta del conjunto que no sustituye contenido existente: se agrega.
También es la más barata del plan —cinco créditos— y la de mayor efecto,
porque habilita la exigencia de trabajo versionado en las quince materias
posteriores y en los tres Proyectos Modulares.
