> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**PRUEBAS DE SOFTWARE Y AUTOMATIZACIÓN**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5918 | Escolarizada | Curso | 8 | Especializante obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 34 | 34 | 68 | Ingeniería de Software I (I5898), Desarrollo Colaborativo y Control de Versiones (I5916) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Ingeniería de Software |

### Presentación

En los programas vigentes la palabra «pruebas» aparece como una fase del ciclo
de vida: algo que ocurre después de construir y antes de entregar. No aparece
como actividad de ingeniería con técnica propia. No hay mención de pruebas
unitarias, automatización ni depuración sistemática.

La diferencia es grande. Probar como fase produce una lista de defectos al
final. Probar como práctica produce un conjunto de comprobaciones que se
ejecutan con cada cambio y que permiten modificar el sistema sin miedo. Esa
segunda idea es la que sostiene el trabajo en equipo sobre bases de código que
viven años, y es la que esta unidad enseña.

### Competencia de la Unidad de Aprendizaje (UA)

Construye y mantiene conjuntos de pruebas automatizadas que verifican el
comportamiento de un sistema en distintos niveles, integrándolos a un proceso
de ejecución continua que impide la incorporación de regresiones.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| Niveles de prueba y qué defecto detecta cada uno | Escribir pruebas unitarias aisladas y deterministas | Trata una prueba que falla como información y no como estorbo |
| Dobles de prueba y sus usos legítimos | Aplicar desarrollo guiado por pruebas | Prefiere comportamiento verificado sobre porcentaje de cobertura |
| Relación entre acoplamiento, diseño y facilidad de prueba | Automatizar la ejecución ante cada cambio | Deja el código mejor estructurado de como lo encontró |
| Límites e interpretación errónea de la cobertura | Diagnosticar una prueba intermitente |  |

| Competencia genérica | Competencia profesional |
|---|---|
| Pensamiento crítico y capacidad de verificar afirmaciones con evidencia. | Aseguramiento de la calidad del software mediante verificación automatizada. |

### Competencias previas del alumno

- Programación orientada a objetos
- Nociones de diseño de software
- Uso de control de versiones

### Competencia del perfil de egreso

Contribuye al egresado capaz de sostener y modificar sistemas existentes sin
degradar su comportamiento, y de entregar software cuya corrección puede
demostrarse.

### Perfil deseable del docente

Profesional con experiencia en mantenimiento de sistemas en producción
respaldados por conjuntos de pruebas automatizadas.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. Por qué se prueba — 6 horas**

&nbsp;&nbsp;1.1 Costo del defecto según el momento de detección
&nbsp;&nbsp;1.2 Taxonomía de pruebas
&nbsp;&nbsp;1.3 Qué no puede demostrar una prueba

**UNIDAD II. Pruebas unitarias — 14 horas**

&nbsp;&nbsp;2.1 Aislamiento y determinismo
&nbsp;&nbsp;2.2 Dobles de prueba: sustitutos, espías y simuladores
&nbsp;&nbsp;2.3 Diseño orientado a la verificabilidad
&nbsp;&nbsp;2.4 Nombrado y organización del conjunto de pruebas

**UNIDAD III. Desarrollo guiado por pruebas — 12 horas**

&nbsp;&nbsp;3.1 Ciclo rojo-verde-refactorización
&nbsp;&nbsp;3.2 Diseño emergente
&nbsp;&nbsp;3.3 Límites y críticas de la técnica

**UNIDAD IV. Pruebas de integración y de contrato — 10 horas**

&nbsp;&nbsp;4.1 Dependencias reales frente a sustitutos
&nbsp;&nbsp;4.2 Datos de prueba y aislamiento entre casos
&nbsp;&nbsp;4.3 Contratos entre componentes

**UNIDAD V. Pruebas de extremo a extremo — 8 horas**

&nbsp;&nbsp;5.1 Automatización de interfaz
&nbsp;&nbsp;5.2 Costo, lentitud y fragilidad
&nbsp;&nbsp;5.3 Cuántas conviene tener

**UNIDAD VI. Cobertura y refactorización — 8 horas**

&nbsp;&nbsp;6.1 Medición de cobertura e interpretación honesta
&nbsp;&nbsp;6.2 Calidad del conjunto de pruebas
&nbsp;&nbsp;6.3 Refactorización respaldada por pruebas

**UNIDAD VII. Automatización e integración continua — 10 horas**

&nbsp;&nbsp;7.1 Ejecución ante cada cambio
&nbsp;&nbsp;7.2 Canalizaciones de construcción y prueba
&nbsp;&nbsp;7.3 Pruebas intermitentes: causas y manejo
&nbsp;&nbsp;7.4 Criterios de bloqueo de integración

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Todo el código entregado en la materia se acompaña de sus pruebas.
- Ejercicio de refactorización: se entrega código correcto pero mal estructurado, que debe reestructurarse sin alterar el comportamiento, demostrado por las pruebas.
- Recepción de un proyecto ajeno y construcción de pruebas de caracterización sobre él.

### Bibliografía básica

1. Khorikov, V. (2020). *Unit Testing: Principles, Practices, and Patterns*. Manning.
2. Beck, K. (2002). *Test-Driven Development: By Example*. Addison-Wesley.

### Bibliografía complementaria

1. Crispin, L. y Gregory, J. (2009). *Agile Testing*. Addison-Wesley.
2. Feathers, M. (2004). *Working Effectively with Legacy Code*. Prentice Hall.
3. Humble, J. y Farley, D. (2010). *Continuous Delivery*. Addison-Wesley.

## 3.- Evaluación

### Tipo de evaluación

Formativa continua sobre las prácticas y sumativa en el proyecto final y el ejercicio de refactorización.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Prácticas de pruebas unitarias | 25 |
| Ejercicio de desarrollo guiado por pruebas | 20 |
| Refactorización respaldada por pruebas | 15 |
| Configuración de ejecución automática | 15 |
| Proyecto final con pruebas en varios niveles | 25 |
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

Toma las horas dedicadas al Proceso Unificado en Ingeniería de Software II
(I5900), cuyo contenido corresponde a la práctica de 1999 a 2007. Esa materia
conserva mantenimiento, calidad y MoProSoft, que siguen teniendo uso en la
industria local de certificación.
