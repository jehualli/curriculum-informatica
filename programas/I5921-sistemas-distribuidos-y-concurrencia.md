> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**SISTEMAS DISTRIBUIDOS Y CONCURRENCIA**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5921 | Escolarizada | Curso | 8 | Especializante obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 41 | 27 | 68 | Uso, Adaptación y Explotación de Sistemas Operativos (I5903), Estructuras de Datos II (I5888) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Ciencias de la Computación |

### Presentación

El Módulo 3 del plan vigente se llama «Sistemas Robustos, Paralelos y
Distribuidos». Las materias que lo integran son Administración de Redes,
Administración de Servidores, Hipermedia y Programación para Internet. Ninguna
trata concurrencia, paralelismo ni sistemas distribuidos: el módulo lleva el
nombre de un campo que no enseña.

Esta unidad cubre ese hueco. Es la más exigente del conjunto propuesto y
también la más duradera: los modelos de concurrencia, la imposibilidad de
distinguir un proceso lento de uno caído, y la tensión entre consistencia y
disponibilidad no dependen de ninguna tecnología y no han cambiado en treinta
años.

### Competencia de la Unidad de Aprendizaje (UA)

Razona sobre sistemas con varios hilos de ejecución y sobre sistemas repartidos
en varias máquinas, identificando condiciones de carrera, modos de falla
parcial y garantías de consistencia, e implementa soluciones correctas bajo
esas condiciones.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| Condiciones de carrera, exclusión mutua, interbloqueo e inanición | Escribir código concurrente correcto | Desconfía de la corrección aparente en sistemas concurrentes |
| Modelos de memoria compartida y de paso de mensajes | Reproducir y diagnosticar una condición de carrera | Asume la falla parcial como estado normal de operación |
| Fallas parciales, relojes y orden causal | Implementar comunicación entre procesos en máquinas distintas | Prefiere el argumento sobre el ensayo y error |
| Tensión entre consistencia, disponibilidad y tolerancia a particiones | Razonar sobre el sistema cuando una parte deja de responder |  |

| Competencia genérica | Competencia profesional |
|---|---|
| Razonamiento formal y capacidad de análisis de sistemas complejos. | Diseño e implementación de sistemas concurrentes y distribuidos correctos. |

### Competencias previas del alumno

- Estructuras de datos y algoritmos
- Sistemas operativos: procesos y planificación
- Fundamentos de redes

### Competencia del perfil de egreso

Contribuye al egresado capaz de construir sistemas que siguen funcionando
cuando una de sus partes falla, y de explicar con precisión qué garantías
ofrece y cuáles no.

### Perfil deseable del docente

Formación en ciencias de la computación con experiencia en sistemas
concurrentes o repartidos, de origen académico o industrial.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. Concurrencia — 12 horas**

&nbsp;&nbsp;1.1 Hilos y planificación
&nbsp;&nbsp;1.2 Condiciones de carrera y exclusión mutua
&nbsp;&nbsp;1.3 Interbloqueo, inanición y sus condiciones
&nbsp;&nbsp;1.4 Estructuras de datos concurrentes

**UNIDAD II. Modelos de concurrencia — 10 horas**

&nbsp;&nbsp;2.1 Memoria compartida
&nbsp;&nbsp;2.2 Paso de mensajes
&nbsp;&nbsp;2.3 Actores y corrutinas
&nbsp;&nbsp;2.4 Comparación y criterios de elección

**UNIDAD III. Fundamentos distribuidos — 10 horas**

&nbsp;&nbsp;3.1 Falla parcial y detección de fallas
&nbsp;&nbsp;3.2 Tiempo, relojes físicos y lógicos
&nbsp;&nbsp;3.3 Orden causal
&nbsp;&nbsp;3.4 Modelos de sistema: síncrono y asíncrono

**UNIDAD IV. Replicación y consistencia — 12 horas**

&nbsp;&nbsp;4.1 Replicación primaria y entre pares
&nbsp;&nbsp;4.2 Consistencia fuerte y eventual
&nbsp;&nbsp;4.3 Particiones de red y sus consecuencias
&nbsp;&nbsp;4.4 Resolución de conflictos

**UNIDAD V. Consenso — 10 horas**

&nbsp;&nbsp;5.1 El problema del acuerdo
&nbsp;&nbsp;5.2 Elección de líder
&nbsp;&nbsp;5.3 Registro replicado
&nbsp;&nbsp;5.4 Límites teóricos

**UNIDAD VI. Comunicación entre procesos — 8 horas**

&nbsp;&nbsp;6.1 Llamada a procedimiento remoto
&nbsp;&nbsp;6.2 Colas de mensajes
&nbsp;&nbsp;6.3 Publicación y suscripción
&nbsp;&nbsp;6.4 Entrega al menos una vez y sus implicaciones

**UNIDAD VII. Paralelismo de datos — 6 horas**

&nbsp;&nbsp;7.1 Descomposición de problemas
&nbsp;&nbsp;7.2 Procesamiento por lotes
&nbsp;&nbsp;7.3 Límites del paralelismo

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Ejercicios con condiciones de carrera reproducibles y su corrección argumentada.
- Implementación de un servicio replicado sencillo con elección de líder.
- Inyección de fallas: se interrumpe la comunicación entre nodos y se observa y explica el comportamiento resultante.

### Bibliografía básica

1. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.
2. Tanenbaum, A. y Van Steen, M. (2023). *Distributed Systems* (4a ed.). Edición de los autores, disponible en línea.

### Bibliografía complementaria

1. Herlihy, M., Shavit, N., Luchangco, V. y Spear, M. (2020). *The Art of Multiprocessor Programming* (2a ed.). Morgan Kaufmann.
2. Ongaro, D. y Ousterhout, J. (2014). *In Search of an Understandable Consensus Algorithm*. USENIX ATC.

## 3.- Evaluación

### Tipo de evaluación

Formativa mediante prácticas de concurrencia; sumativa en el servicio replicado y su comportamiento bajo falla.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Prácticas de programación concurrente | 25 |
| Diagnóstico y corrección de condiciones de carrera | 15 |
| Implementación de comunicación entre procesos remotos | 20 |
| Análisis del comportamiento bajo partición de red | 15 |
| Proyecto final: servicio replicado con tolerancia a fallas | 25 |
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

Contenido nuevo. Llena el hueco entre el nombre del Módulo 3 y su contenido
real. Es la propuesta más exigente y la que más se apoya en la base que el plan
ya tiene bien resuelta: estructuras de datos, algoritmia y sistemas operativos.
