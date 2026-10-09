> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**ARQUITECTURA DE SOFTWARE**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5919 | Escolarizada | Curso | 8 | Especializante obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 41 | 27 | 68 | Ingeniería de Software II (I5900), Servicios Web y APIs (I5917) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Ingeniería de Software |

### Presentación

La expresión «arquitectura de software» no aparece en ningún programa del plan
vigente. El estudiante aprende a construir componentes y a modelarlos con UML,
pero no a decidir cómo se reparte un sistema, qué atributos de calidad se
privilegian ni qué se sacrifica al elegir una estructura sobre otra.

Esa decisión distingue al ingeniero del programador y es la más cara de
corregir: un error de codificación se arregla en horas; uno de estructura
condiciona el sistema durante años. Esta unidad trata la arquitectura como el
conjunto de decisiones difíciles de revertir, y enseña a tomarlas
explícitamente y a dejarlas registradas.

### Competencia de la Unidad de Aprendizaje (UA)

Evalúa alternativas de estructura para un sistema a partir de sus atributos de
calidad, justifica la elección frente a restricciones reales, la documenta de
forma que sobreviva al equipo que la tomó y reconoce cuándo debe revisarse.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| Atributos de calidad y sus tensiones | Derivar requisitos de calidad de necesidades del negocio | Sostiene una decisión con argumentos y la revisa ante evidencia nueva |
| Estilos arquitectónicos y condiciones en que cada uno conviene | Proponer y comparar alternativas estructurales | Reconoce que toda elección de estructura implica una renuncia |
| Consistencia de datos en sistemas repartidos | Documentar mediante vistas y registros de decisión | Escribe para quien mantendrá el sistema después |
| Deuda técnica como decisión y no como accidente | Evaluar una arquitectura existente por escenarios |  |

| Competencia genérica | Competencia profesional |
|---|---|
| Capacidad de tomar decisiones bajo incertidumbre y de argumentarlas. | Definición y evaluación de la estructura de sistemas de software de mediana y gran escala. |

### Competencias previas del alumno

- Ingeniería de software y modelado
- Diseño e implementación de servicios
- Bases de datos

### Competencia del perfil de egreso

Contribuye al egresado capaz de asumir decisiones estructurales sobre sistemas
de escala real y de justificarlas ante equipos técnicos y no técnicos.

### Perfil deseable del docente

Profesional con experiencia en decisiones de estructura sobre sistemas en
producción y en su evolución a lo largo de varios años.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. Qué decide la arquitectura — 8 horas**

&nbsp;&nbsp;1.1 Atributos de calidad y su especificación por escenarios
&nbsp;&nbsp;1.2 Restricciones del negocio y del entorno
&nbsp;&nbsp;1.3 Renuncias explícitas

**UNIDAD II. Estilos arquitectónicos — 14 horas**

&nbsp;&nbsp;2.1 Monolito por capas y monolito modular
&nbsp;&nbsp;2.2 Arquitectura hexagonal y puertos y adaptadores
&nbsp;&nbsp;2.3 Arquitectura orientada a eventos
&nbsp;&nbsp;2.4 Servicios distribuidos: cuándo sí y cuándo no

**UNIDAD III. Documentación de la arquitectura — 10 horas**

&nbsp;&nbsp;3.1 Vistas y sus audiencias
&nbsp;&nbsp;3.2 Modelo de contexto, contenedores y componentes
&nbsp;&nbsp;3.3 Registros de decisión arquitectónica
&nbsp;&nbsp;3.4 Documentación que envejece bien

**UNIDAD IV. Datos y consistencia — 10 horas**

&nbsp;&nbsp;4.1 Propiedad de los datos y duplicación
&nbsp;&nbsp;4.2 Consistencia fuerte y eventual
&nbsp;&nbsp;4.3 Transacciones repartidas y sus alternativas

**UNIDAD V. Escalabilidad y tolerancia a fallas — 12 horas**

&nbsp;&nbsp;5.1 Escalamiento vertical y horizontal
&nbsp;&nbsp;5.2 Puntos únicos de falla
&nbsp;&nbsp;5.3 Degradación elegante y aislamiento
&nbsp;&nbsp;5.4 Capacidad y medición

**UNIDAD VI. Deuda técnica y evolución — 8 horas**

&nbsp;&nbsp;6.1 Origen y contabilidad de la deuda
&nbsp;&nbsp;6.2 Migración por etapas
&nbsp;&nbsp;6.3 Arquitecturas que admiten cambio

**UNIDAD VII. Evaluación de arquitecturas — 6 horas**

&nbsp;&nbsp;7.1 Evaluación por escenarios
&nbsp;&nbsp;7.2 Identificación de riesgos y puntos sensibles
&nbsp;&nbsp;7.3 Prototipos de los puntos de riesgo

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Estudio de casos con restricciones contradictorias y defensa de la solución propuesta.
- Redacción de un registro de decisión arquitectónica por cada elección relevante.
- Evaluación por pares: cada equipo somete su arquitectura a los escenarios de calidad que propone otro equipo.

### Bibliografía básica

1. Richards, M. y Ford, N. (2020). *Fundamentals of Software Architecture*. O'Reilly.
2. Bass, L., Clements, P. y Kazman, R. (2021). *Software Architecture in Practice* (4a ed.). Addison-Wesley.

### Bibliografía complementaria

1. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.
2. Newman, S. (2021). *Building Microservices* (2a ed.). O'Reilly.
3. Ford, N., Parsons, R. y Kua, P. (2017). *Building Evolutionary Architectures*. O'Reilly.

## 3.- Evaluación

### Tipo de evaluación

Formativa mediante casos y registros de decisión; sumativa en la propuesta arquitectónica final y su evaluación por pares.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Análisis de casos | 20 |
| Registros de decisión arquitectónica | 20 |
| Documentación de vistas del sistema propuesto | 20 |
| Evaluación por escenarios de la arquitectura de otro equipo | 15 |
| Proyecto final: propuesta con prototipo de los puntos de riesgo | 25 |
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

Contenido nuevo, sin sustitución directa. Se ubica en sexto semestre, entre las
dos materias de Ingeniería de Software y el tercer Proyecto Modular, para que
la decisión estructural del proyecto final sea deliberada y no accidental.
