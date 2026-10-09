> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**CÓMPUTO EN LA NUBE Y CONTENEDORES**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5920 | Escolarizada | Curso | 8 | Especializante obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 27 | 41 | 68 | Uso, Adaptación y Explotación de Sistemas Operativos (I5903), Administración de Redes (I5907) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Redes y Sistemas |

### Presentación

Administración de Servidores enseña a instalar y configurar servicios sobre
una máquina que se puede tocar. Esa habilidad sigue siendo formativa —explica
qué es un servicio, un puerto y un permiso— pero dejó de describir cómo opera
la mayoría de los sistemas: la máquina se renta por minutos, se define en un
archivo y se reemplaza en lugar de repararse.

Esta unidad recoge esa mitad faltante. Su tema central no es un proveedor de
nube en particular, sino el cambio en la unidad de trabajo: del servidor que se
cuida al entorno que se describe, se reproduce y se descarta.

### Competencia de la Unidad de Aprendizaje (UA)

Empaqueta, despliega y opera aplicaciones en entornos reproducibles, define la
infraestructura como código, instrumenta el sistema para poder observarlo y
estima el costo de las decisiones de despliegue.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| Modelos de servicio y de despliegue; responsabilidad compartida | Construir imágenes y componer varios servicios | Trata el entorno como algo reproducible y no como configuración manual irrepetible |
| Aislamiento por contenedor frente a virtualización completa | Desplegar con escalamiento y verificación de salud | Considera el costo económico y energético como criterio de ingeniería |
| Principios de infraestructura declarativa | Describir infraestructura en código | Documenta lo necesario para que otro levante el sistema sin ayuda |
| Señales de observabilidad y su uso | Diagnosticar un sistema en ejecución y estimar su costo |  |

| Competencia genérica | Competencia profesional |
|---|---|
| Capacidad de organizar el trabajo de forma reproducible y verificable. | Despliegue y operación de sistemas sobre infraestructura rentada. |

### Competencias previas del alumno

- Administración de sistemas operativos
- Fundamentos de redes
- Control de versiones

### Competencia del perfil de egreso

Contribuye al egresado capaz de llevar un sistema desde su código hasta su
operación, con entornos reproducibles y con capacidad de diagnóstico sobre
sistemas en ejecución.

### Perfil deseable del docente

Profesional con experiencia en operación de sistemas desplegados en
infraestructura rentada y en diagnóstico de incidentes en producción.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. Modelos de servicio y de despliegue — 6 horas**

&nbsp;&nbsp;1.1 Infraestructura, plataforma y software como servicio
&nbsp;&nbsp;1.2 Nube pública, privada e híbrida
&nbsp;&nbsp;1.3 Responsabilidad compartida y sus límites

**UNIDAD II. Contenedores — 14 horas**

&nbsp;&nbsp;2.1 Aislamiento de procesos y de recursos
&nbsp;&nbsp;2.2 Imágenes, capas y registros
&nbsp;&nbsp;2.3 Construcción reproducible
&nbsp;&nbsp;2.4 Datos persistentes y volúmenes

**UNIDAD III. Composición de servicios — 10 horas**

&nbsp;&nbsp;3.1 Varios servicios en un mismo entorno
&nbsp;&nbsp;3.2 Redes entre contenedores
&nbsp;&nbsp;3.3 Entornos de desarrollo reproducibles
&nbsp;&nbsp;3.4 Configuración y secretos

**UNIDAD IV. Orquestación — 12 horas**

&nbsp;&nbsp;4.1 Programación de cargas de trabajo
&nbsp;&nbsp;4.2 Escalamiento y verificación de salud
&nbsp;&nbsp;4.3 Actualizaciones progresivas y reversión
&nbsp;&nbsp;4.4 Descubrimiento de servicios

**UNIDAD V. Infraestructura como código — 10 horas**

&nbsp;&nbsp;5.1 Declaración frente a procedimiento
&nbsp;&nbsp;5.2 Estado e idempotencia
&nbsp;&nbsp;5.3 Entornos equivalentes
&nbsp;&nbsp;5.4 Revisión de cambios de infraestructura

**UNIDAD VI. Observabilidad — 10 horas**

&nbsp;&nbsp;6.1 Registros estructurados
&nbsp;&nbsp;6.2 Métricas e indicadores de servicio
&nbsp;&nbsp;6.3 Trazas distribuidas
&nbsp;&nbsp;6.4 Alertas que valen la pena atender

**UNIDAD VII. Costo, seguridad y cumplimiento — 6 horas**

&nbsp;&nbsp;7.1 Estimación y control de costo
&nbsp;&nbsp;7.2 Identidad y permisos mínimos
&nbsp;&nbsp;7.3 Residencia de datos y obligaciones legales

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Toda entrega se ejecuta dentro de un contenedor construido por el estudiante.
- Ejercicio de reproducibilidad: un equipo levanta el entorno de otro usando únicamente su repositorio.
- Simulación de fallas: el profesor detiene componentes y el estudiante diagnostica con las señales que instrumentó.
- Ejercicio de costo: estimación mensual de la arquitectura propuesta.

### Bibliografía básica

1. Nickoloff, J. y Kuenzli, S. (2019). *Docker in Action* (2a ed.). Manning.
2. Burns, B., Beda, J. y Hightower, K. (2022). *Kubernetes: Up and Running* (3a ed.). O'Reilly.

### Bibliografía complementaria

1. Beyer, B., Jones, C., Petoff, J. y Murphy, N. (2016). *Site Reliability Engineering*. O'Reilly.
2. Morris, K. (2020). *Infrastructure as Code* (2a ed.). O'Reilly.

## 3.- Evaluación

### Tipo de evaluación

Formativa mediante prácticas y ejercicios de diagnóstico; sumativa en el proyecto desplegado e instrumentado.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Prácticas de empaquetado y composición | 25 |
| Despliegue orquestado con escalamiento | 20 |
| Infraestructura declarada en código | 15 |
| Diagnóstico de fallas mediante observabilidad | 15 |
| Proyecto final desplegado, instrumentado y con estimación de costo | 25 |
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

Toma la mitad de las horas de Administración de Servidores (I5908) dedicadas a
instalación manual. Esa materia conserva la parte formativa —servicios,
permisos, redes y bases de datos— y cede la operación al modelo actual.
