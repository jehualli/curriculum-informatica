> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**SERVICIOS WEB Y APIS**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5917 | Escolarizada | Curso | 8 | Especializante obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 34 | 34 | 68 | Bases de Datos (I5890), Programación para Internet (I5909) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Sistemas de Información |

### Presentación

El plan vigente enseña a conectar una página con datos mediante DOM, XML y
AJAX, técnica dominante entre 2006 y 2012. Hoy la integración entre sistemas
se hace mediante interfaces de programación sobre HTTP que devuelven JSON, y
la habilidad central ya no es manipular el documento del navegador sino
diseñar el contrato entre dos sistemas que no se conocen.

Esta unidad ocupa ese lugar. No enseña un marco de trabajo concreto: enseña el
protocolo, el diseño del recurso, el manejo del error y la negociación de
identidad, que es lo que permanece cuando el marco de trabajo cambia.

### Competencia de la Unidad de Aprendizaje (UA)

Diseña, construye, documenta y consume interfaces de programación sobre HTTP,
definiendo contratos estables, resolviendo autenticación y errores, y
sosteniendo la compatibilidad ante la evolución del servicio.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| HTTP como protocolo de aplicación: métodos, estados, encabezados, caché | Modelar un dominio como recursos e implementar el servicio | Considera al consumidor de la interfaz como usuario real |
| Modelos de integración: recursos, GraphQL, webhooks | Consumir servicios de terceros con reintentos y límites de tasa | Asume que un contrato publicado es un compromiso con terceros |
| Mecanismos de autorización basados en credenciales portadoras | Documentar mediante una especificación legible por máquina | Documenta antes de dar por terminado un servicio |

| Competencia genérica | Competencia profesional |
|---|---|
| Capacidad de abstracción, análisis y síntesis aplicada al diseño de interfaces. | Integración de sistemas heterogéneos mediante contratos de servicio estables. |

### Competencias previas del alumno

- Modelado y consulta de bases de datos relacionales
- Programación del lado del servidor
- Manejo de control de versiones

### Competencia del perfil de egreso

Contribuye al egresado capaz de integrar sistemas de origen diverso y de
publicar servicios que otros equipos puedan consumir sin asistencia de sus
autores.

### Perfil deseable del docente

Profesional con experiencia en construcción y operación de servicios en
producción, incluyendo el versionado de interfaces con consumidores externos.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. HTTP como protocolo de aplicación — 8 horas**

&nbsp;&nbsp;1.1 Métodos y su semántica
&nbsp;&nbsp;1.2 Códigos de estado y su uso correcto
&nbsp;&nbsp;1.3 Encabezados, negociación de contenido y caché
&nbsp;&nbsp;1.4 Idempotencia y seguridad de las operaciones

**UNIDAD II. Diseño de interfaces orientadas a recursos — 12 horas**

&nbsp;&nbsp;2.1 Identificación y nombrado de recursos
&nbsp;&nbsp;2.2 Colecciones, filtrado, ordenamiento y paginación
&nbsp;&nbsp;2.3 Modelado de operaciones que no son recursos
&nbsp;&nbsp;2.4 Errores: formato, detalle y consistencia

**UNIDAD III. Representación y evolución — 8 horas**

&nbsp;&nbsp;3.1 JSON y esquemas de validación
&nbsp;&nbsp;3.2 Compatibilidad hacia atrás
&nbsp;&nbsp;3.3 Estrategias de versionado
&nbsp;&nbsp;3.4 Depreciación y retiro de un contrato

**UNIDAD IV. Identidad y control de acceso — 10 horas**

&nbsp;&nbsp;4.1 Credenciales portadoras y su almacenamiento
&nbsp;&nbsp;4.2 OAuth 2.0: flujos y alcances
&nbsp;&nbsp;4.3 Expiración y renovación
&nbsp;&nbsp;4.4 Errores frecuentes de autorización

**UNIDAD V. Consumo de servicios — 8 horas**

&nbsp;&nbsp;5.1 Clientes y tiempos de espera
&nbsp;&nbsp;5.2 Reintentos con retroceso exponencial
&nbsp;&nbsp;5.3 Límites de tasa y cuotas
&nbsp;&nbsp;5.4 Degradación ante falla del proveedor

**UNIDAD VI. Documentación y contrato — 8 horas**

&nbsp;&nbsp;6.1 Especificación OpenAPI
&nbsp;&nbsp;6.2 Generación de clientes y de documentación
&nbsp;&nbsp;6.3 Ejemplos ejecutables
&nbsp;&nbsp;6.4 Pruebas de conformidad con el contrato

**UNIDAD VII. Alternativas al modelo de recursos — 8 horas**

&nbsp;&nbsp;7.1 GraphQL: esquema, consultas y costos
&nbsp;&nbsp;7.2 Webhooks y entrega de eventos
&nbsp;&nbsp;7.3 Comunicación en tiempo real
&nbsp;&nbsp;7.4 Criterios de elección entre modelos

**UNIDAD VIII. Operación de un servicio — 6 horas**

&nbsp;&nbsp;8.1 Pruebas del servicio
&nbsp;&nbsp;8.2 Instrumentación mínima
&nbsp;&nbsp;8.3 Publicación y control de cambios

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Construcción progresiva de un servicio propio a lo largo del semestre.
- Consumo obligatorio de al menos dos servicios públicos de terceros, con manejo real de sus límites y errores.
- Ejercicio cruzado: cada equipo consume la interfaz de otro equipo usando únicamente la documentación publicada, sin preguntar a sus autores.

### Bibliografía básica

1. Lauret, A. (2019). *The Design of Web APIs*. Manning.
2. Masse, M. (2011). *REST API Design Rulebook*. O'Reilly.
3. OpenAPI Initiative. Especificación OpenAPI, versión vigente.

### Bibliografía complementaria

1. Richardson, L. y Amundsen, M. (2013). *RESTful Web APIs*. O'Reilly.
2. IETF. Documentos RFC sobre semántica y caché de HTTP.

## 3.- Evaluación

### Tipo de evaluación

Diagnóstica, formativa mediante prácticas e integración cruzada, y sumativa en el proyecto final.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Prácticas de implementación del servicio | 25 |
| Consumo de servicios de terceros con manejo de fallas | 15 |
| Documentación del contrato en OpenAPI | 15 |
| Ejercicio cruzado de integración entre equipos | 15 |
| Proyecto final: servicio con autenticación y pruebas | 30 |
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

Sustituye en Programación para Internet (I5909) las unidades de conexión a
datos por DOM/XML/AJAX (5 h), gestores de contenido (8 h), SEO (5 h) y WPO
(7 h): 25 de sus 68 horas. Esa materia conserva HTML5, CSS3, JavaScript,
patrones de diseño y marcos de trabajo, y deja de cargar temas de mercadotecnia.
