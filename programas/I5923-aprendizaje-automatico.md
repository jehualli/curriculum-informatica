> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**APRENDIZAJE AUTOMÁTICO**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5923 | Escolarizada | Curso | 8 | Especializante obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 34 | 34 | 68 | Estadística y Procesos Estocásticos (I5897), Minería de Datos (I5911) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Cómputo Flexible |

### Presentación

El Módulo 4 del plan se llama «Cómputo Flexible», término acuñado a inicios de
los años noventa, y su contenido corresponde a esa tradición: sistemas
expertos, lógica difusa y motores de reglas. Son temas legítimos y con
aplicaciones vigentes en control e ingeniería, pero no describen cómo se
construyen hoy los sistemas que aprenden de datos.

Esta unidad no sustituye esa tradición: la continúa. Parte del sistema basado
en reglas que el estudiante ya conoce y muestra qué problema resuelve el modelo
estadístico que las reglas no alcanzan, y a qué costo: opacidad, dependencia de
los datos y necesidad de evaluación honesta. El énfasis está en la evaluación,
que es donde más proyectos fallan y lo que distingue un modelo útil de uno que
sólo memorizó sus datos.

### Competencia de la Unidad de Aprendizaje (UA)

Formula un problema como tarea de aprendizaje, prepara los datos, entrena y
evalúa modelos con metodología correcta, interpreta sus límites y los pone en
operación con monitoreo de su degradación.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| Aprendizaje supervisado y no supervisado | Preparar y explorar un conjunto de datos | Desconfía de una métrica alta antes de auditar la partición de datos |
| Compromiso entre sesgo y varianza; sobreajuste | Entrenar modelos de referencia antes que modelos complejos | Reconoce sesgos en los datos y sus consecuencias sobre personas |
| Métricas según el problema y el costo del error | Validar correctamente e interpretar resultados | Informa los límites del modelo junto con sus resultados |
| Fuga de información entre entrenamiento y evaluación | Desplegar y vigilar un modelo en operación |  |

| Competencia genérica | Competencia profesional |
|---|---|
| Pensamiento estadístico y honestidad en el reporte de resultados. | Construcción, evaluación y operación de modelos de aprendizaje sobre datos reales. |

### Competencias previas del alumno

- Estadística y probabilidad
- Minería de datos
- Programación y manejo de datos

### Competencia del perfil de egreso

Contribuye al egresado capaz de decidir si un problema se resuelve con reglas o
con aprendizaje, de evaluar un modelo con rigor y de explicar honestamente sus
límites.

### Perfil deseable del docente

Formación en estadística, matemáticas o cómputo, con experiencia en
construcción y evaluación de modelos sobre datos reales.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. Del sistema de reglas al modelo estadístico — 6 horas**

&nbsp;&nbsp;1.1 Qué resuelve cada enfoque
&nbsp;&nbsp;1.2 Qué se gana y qué se pierde
&nbsp;&nbsp;1.3 Cuándo no usar aprendizaje automático

**UNIDAD II. Datos — 10 horas**

&nbsp;&nbsp;2.1 Obtención y limpieza
&nbsp;&nbsp;2.2 Representación de variables
&nbsp;&nbsp;2.3 Exploración y visualización
&nbsp;&nbsp;2.4 Fuga de información: origen y detección

**UNIDAD III. Aprendizaje supervisado — 14 horas**

&nbsp;&nbsp;3.1 Regresión
&nbsp;&nbsp;3.2 Clasificación
&nbsp;&nbsp;3.3 Modelos de referencia
&nbsp;&nbsp;3.4 Árboles y métodos de conjunto

**UNIDAD IV. Evaluación — 12 horas**

&nbsp;&nbsp;4.1 Partición y validación cruzada
&nbsp;&nbsp;4.2 Métricas y costo del error
&nbsp;&nbsp;4.3 Sobreajuste y regularización
&nbsp;&nbsp;4.4 Diagnóstico de errores del modelo

**UNIDAD V. Aprendizaje no supervisado — 8 horas**

&nbsp;&nbsp;5.1 Agrupamiento
&nbsp;&nbsp;5.2 Reducción de dimensiones
&nbsp;&nbsp;5.3 Evaluación sin etiquetas

**UNIDAD VI. Redes neuronales — 10 horas**

&nbsp;&nbsp;6.1 Perceptrón multicapa y entrenamiento
&nbsp;&nbsp;6.2 Cuándo aportan y cuándo no
&nbsp;&nbsp;6.3 Costo computacional y de datos

**UNIDAD VII. Puesta en operación — 8 horas**

&nbsp;&nbsp;7.1 Servicio de inferencia
&nbsp;&nbsp;7.2 Versionado de datos y modelos
&nbsp;&nbsp;7.3 Monitoreo de degradación
&nbsp;&nbsp;7.4 Reentrenamiento

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Todo proyecto inicia con un modelo de referencia trivial que debe superarse.
- Auditoría cruzada: cada equipo busca fugas de información en el trabajo de otro equipo.
- Discusión de casos documentados de modelos con sesgo y de sus consecuencias.

### Bibliografía básica

1. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow* (3a ed.). O'Reilly.
2. James, G., Witten, D., Hastie, T. y Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2a ed.). Springer. Disponible en línea sin costo.

### Bibliografía complementaria

1. Murphy, K. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
2. Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly.

## 3.- Evaluación

### Tipo de evaluación

Formativa sobre las prácticas y la auditoría cruzada; sumativa en el modelo final y su protocolo de evaluación.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Prácticas de preparación y exploración de datos | 20 |
| Entrenamiento y comparación contra el modelo de referencia | 20 |
| Protocolo de evaluación y diagnóstico de errores | 20 |
| Auditoría del trabajo de otro equipo | 10 |
| Proyecto final con modelo en operación y monitoreo | 30 |
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

Actualiza la línea de Sistemas Basados en Conocimiento (I5913 y su seminario
I5914), que dedica 28 de 68 horas a un motor de reglas cuya vigencia industrial
terminó alrededor de 2010. La tradición de cómputo flexible se conserva en las
materias de lógica difusa y clasificación inteligente.
