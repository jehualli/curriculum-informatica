> **PROPUESTA NO OFICIAL.** Ejercicio de diseño curricular sin relación
> con la Universidad de Guadalajara. La clave, la seriación y la ubicación
> semestral son propuestas del ejercicio.

*[Aquí va el bloque de Misión del Centro Universitario que encabeza los
programas oficiales.]*

## 1.- Identificación de la Unidad de Aprendizaje

### Nombre de la Unidad de Aprendizaje

**DESARROLLO DE APLICACIONES MÓVILES**

| Clave de la UA | Modalidad de la UA | Tipo de UA | Valor de créditos | Área de formación |
|---|---|---|---|---|
| I5922 | Escolarizada | Curso | 8 | Especializante obligatoria |

| Hora semana | Horas teoría/semestre | Horas práctica/semestre | Total de horas: | Seriación |
|---|---|---|---|---|
| 4 | 27 | 41 | 68 | Servicios Web y APIs (I5917), Experiencia de Usuario y Accesibilidad (I5924) |

| Departamento | Academia |
|---|---|
| Ciencias Computacionales | Sistemas de Información |

### Presentación

El plan vigente no menciona el desarrollo para dispositivos móviles en ningún
documento. Programación para Internet dedica cuatro horas a «Web Móvil», que
trata el tema como una adaptación del sitio de escritorio.

Un dispositivo móvil no es una pantalla pequeña: es un entorno con batería
finita, conectividad intermitente, permisos revocables, un sistema operativo
que suspende procesos sin aviso y un ciclo de publicación controlado por un
tercero. Esta unidad trata esas restricciones como el contenido y no como
detalles de implementación. Se trabaja con un marco multiplataforma para que
el aprendizaje no dependa de un sistema operativo concreto.

### Competencia de la Unidad de Aprendizaje (UA)

Construye aplicaciones para dispositivos móviles que funcionan de forma
razonable con conectividad intermitente, administran el estado local, respetan
el modelo de permisos y el ciclo de vida de la plataforma, y pueden publicarse
en una tienda de distribución.

### Tipos de saberes

| Saber (conocimientos) | Saber hacer (habilidades) | Saber ser (actitudes y valores) |
|---|---|---|
| Ciclo de vida de una aplicación móvil y suspensión de procesos | Construir interfaces declarativas con navegación | Diseña para la interrupción y no para el caso ideal |
| Modelo de permisos y privacidad de la plataforma | Administrar estado y persistencia local | Considera el costo de datos y batería del usuario como responsabilidad propia |
| Restricciones de energía, red y almacenamiento | Sincronizar con servicios remotos tolerando la pérdida de conexión | Solicita únicamente los permisos que la función requiere |
| Requisitos de publicación y revisión | Medir consumo y preparar una entrega firmada |  |

| Competencia genérica | Competencia profesional |
|---|---|
| Capacidad de diseñar soluciones bajo restricciones de recursos. | Desarrollo y publicación de aplicaciones para dispositivos móviles. |

### Competencias previas del alumno

- Consumo de servicios web
- Fundamentos de diseño de interfaces
- Programación orientada a objetos

### Competencia del perfil de egreso

Contribuye al egresado capaz de llevar una aplicación móvil desde su diseño
hasta su publicación y mantenimiento, considerando las restricciones reales
del dispositivo y de su usuario.

### Perfil deseable del docente

Profesional con aplicaciones publicadas en tiendas de distribución y
experiencia en su mantenimiento posterior a la publicación.

## 2.- Contenidos temáticos

### Contenido

**UNIDAD I. La plataforma móvil — 8 horas**

&nbsp;&nbsp;1.1 Ciclo de vida y suspensión de procesos
&nbsp;&nbsp;1.2 Modelo de permisos
&nbsp;&nbsp;1.3 Recursos limitados: batería, red, almacenamiento
&nbsp;&nbsp;1.4 Fragmentación de dispositivos y versiones

**UNIDAD II. Interfaz y navegación — 12 horas**

&nbsp;&nbsp;2.1 Interfaz declarativa y composición
&nbsp;&nbsp;2.2 Navegación y pila de pantallas
&nbsp;&nbsp;2.3 Adaptación a tamaños y orientaciones
&nbsp;&nbsp;2.4 Componentes propios de la plataforma

**UNIDAD III. Estado y persistencia local — 12 horas**

&nbsp;&nbsp;3.1 Administración de estado
&nbsp;&nbsp;3.2 Almacenamiento estructurado en el dispositivo
&nbsp;&nbsp;3.3 Migración de datos entre versiones
&nbsp;&nbsp;3.4 Datos sensibles y cifrado en reposo

**UNIDAD IV. Servicios y operación sin conexión — 12 horas**

&nbsp;&nbsp;4.1 Consumo de servicios remotos
&nbsp;&nbsp;4.2 Almacenamiento temporal y política de vigencia
&nbsp;&nbsp;4.3 Cola de operaciones pendientes
&nbsp;&nbsp;4.4 Sincronización diferida y resolución de conflictos

**UNIDAD V. Notificaciones y segundo plano — 8 horas**

&nbsp;&nbsp;5.1 Notificaciones locales y remotas
&nbsp;&nbsp;5.2 Trabajo en segundo plano y sus límites
&nbsp;&nbsp;5.3 Consentimiento del usuario

**UNIDAD VI. Pruebas y rendimiento — 8 horas**

&nbsp;&nbsp;6.1 Pruebas en dispositivo y en emulador
&nbsp;&nbsp;6.2 Medición de consumo de batería y datos
&nbsp;&nbsp;6.3 Tiempo de arranque y fluidez

**UNIDAD VII. Publicación — 8 horas**

&nbsp;&nbsp;7.1 Firma de la aplicación
&nbsp;&nbsp;7.2 Requisitos de las tiendas y proceso de revisión
&nbsp;&nbsp;7.3 Actualizaciones y compatibilidad
&nbsp;&nbsp;7.4 Distribución de versiones de prueba

**Total: 68 horas**

### Estrategias docentes para impartir la unidad de aprendizaje

- Desarrollo de una aplicación propia a lo largo del semestre.
- Prueba obligatoria en modo avión y con red degradada.
- Medición de consumo de batería y datos, con comparación entre equipos.
- Revisión cruzada de permisos solicitados y su justificación.

### Bibliografía básica

1. Documentación oficial de la plataforma móvil seleccionada y del marco multiplataforma en uso, versión vigente.
2. Griffiths, D. y Griffiths, D. (2021). *Head First Android Development* (3a ed.). O'Reilly.

### Bibliografía complementaria

1. Neil, T. (2014). *Mobile Design Pattern Gallery* (2a ed.). O'Reilly.
2. Lineamientos de interfaz humana de las plataformas de distribución, versión vigente.

## 3.- Evaluación

### Tipo de evaluación

Formativa sobre la aplicación en desarrollo; sumativa en la entrega publicable y sus mediciones.

### Criterios de Evaluación (% por criterio)

| Criterio | Porcentaje |
|---|---:|
| Prácticas de interfaz y navegación | 20 |
| Persistencia local y sincronización | 20 |
| Comportamiento sin conexión | 15 |
| Medición de rendimiento y consumo | 15 |
| Proyecto final publicable con paquete firmado | 30 |
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

Toma el lugar de Hipermedia (I5910), cuyo contenido quedó absorbido por el
diseño web general y cuya bibliografía vigente incluye un libro de programación
en Python sin relación aparente con la materia.
