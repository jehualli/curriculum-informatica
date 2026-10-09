# -*- coding: utf-8 -*-
CURSOS = [
{
 "archivo": "I5917-servicios-web-y-apis.md",
 "nombre": "Servicios Web y APIs", "clave": "I5917", "modalidad": "Escolarizada",
 "tipo": "Curso", "creditos": 8, "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 34, "practica": 34, "total": 68,
 "seriacion": "Bases de Datos (I5890), Programación para Internet (I5909)",
 "departamento": "Ciencias Computacionales", "academia": "Sistemas de Información",
 "presentacion": """
El plan vigente enseña a conectar una página con datos mediante DOM, XML y
AJAX, técnica dominante entre 2006 y 2012. Hoy la integración entre sistemas
se hace mediante interfaces de programación sobre HTTP que devuelven JSON, y
la habilidad central ya no es manipular el documento del navegador sino
diseñar el contrato entre dos sistemas que no se conocen.

Esta unidad ocupa ese lugar. No enseña un marco de trabajo concreto: enseña el
protocolo, el diseño del recurso, el manejo del error y la negociación de
identidad, que es lo que permanece cuando el marco de trabajo cambia.
""",
 "competencia": """
Diseña, construye, documenta y consume interfaces de programación sobre HTTP,
definiendo contratos estables, resolviendo autenticación y errores, y
sosteniendo la compatibilidad ante la evolución del servicio.
""",
 "saber": ["HTTP como protocolo de aplicación: métodos, estados, encabezados, caché",
           "Modelos de integración: recursos, GraphQL, webhooks",
           "Mecanismos de autorización basados en credenciales portadoras"],
 "saber_hacer": ["Modelar un dominio como recursos e implementar el servicio",
                 "Consumir servicios de terceros con reintentos y límites de tasa",
                 "Documentar mediante una especificación legible por máquina"],
 "saber_ser": ["Considera al consumidor de la interfaz como usuario real",
               "Asume que un contrato publicado es un compromiso con terceros",
               "Documenta antes de dar por terminado un servicio"],
 "comp_generica": "Capacidad de abstracción, análisis y síntesis aplicada al diseño de interfaces.",
 "comp_profesional": "Integración de sistemas heterogéneos mediante contratos de servicio estables.",
 "previas": ["Modelado y consulta de bases de datos relacionales",
             "Programación del lado del servidor", "Manejo de control de versiones"],
 "perfil_egreso": """
Contribuye al egresado capaz de integrar sistemas de origen diverso y de
publicar servicios que otros equipos puedan consumir sin asistencia de sus
autores.
""",
 "perfil_docente": """
Profesional con experiencia en construcción y operación de servicios en
producción, incluyendo el versionado de interfaces con consumidores externos.
""",
 "contenido": [
  {"titulo":"HTTP como protocolo de aplicación","horas":8,
   "temas":["Métodos y su semántica","Códigos de estado y su uso correcto","Encabezados, negociación de contenido y caché","Idempotencia y seguridad de las operaciones"]},
  {"titulo":"Diseño de interfaces orientadas a recursos","horas":12,
   "temas":["Identificación y nombrado de recursos","Colecciones, filtrado, ordenamiento y paginación","Modelado de operaciones que no son recursos","Errores: formato, detalle y consistencia"]},
  {"titulo":"Representación y evolución","horas":8,
   "temas":["JSON y esquemas de validación","Compatibilidad hacia atrás","Estrategias de versionado","Depreciación y retiro de un contrato"]},
  {"titulo":"Identidad y control de acceso","horas":10,
   "temas":["Credenciales portadoras y su almacenamiento","OAuth 2.0: flujos y alcances","Expiración y renovación","Errores frecuentes de autorización"]},
  {"titulo":"Consumo de servicios","horas":8,
   "temas":["Clientes y tiempos de espera","Reintentos con retroceso exponencial","Límites de tasa y cuotas","Degradación ante falla del proveedor"]},
  {"titulo":"Documentación y contrato","horas":8,
   "temas":["Especificación OpenAPI","Generación de clientes y de documentación","Ejemplos ejecutables","Pruebas de conformidad con el contrato"]},
  {"titulo":"Alternativas al modelo de recursos","horas":8,
   "temas":["GraphQL: esquema, consultas y costos","Webhooks y entrega de eventos","Comunicación en tiempo real","Criterios de elección entre modelos"]},
  {"titulo":"Operación de un servicio","horas":6,
   "temas":["Pruebas del servicio","Instrumentación mínima","Publicación y control de cambios"]},
 ],
 "estrategias": ["Construcción progresiva de un servicio propio a lo largo del semestre.",
   "Consumo obligatorio de al menos dos servicios públicos de terceros, con manejo real de sus límites y errores.",
   "Ejercicio cruzado: cada equipo consume la interfaz de otro equipo usando únicamente la documentación publicada, sin preguntar a sus autores."],
 "bib_basica": ["Lauret, A. (2019). *The Design of Web APIs*. Manning.",
   "Masse, M. (2011). *REST API Design Rulebook*. O'Reilly.",
   "OpenAPI Initiative. Especificación OpenAPI, versión vigente."],
 "bib_comp": ["Richardson, L. y Amundsen, M. (2013). *RESTful Web APIs*. O'Reilly.",
   "IETF. Documentos RFC sobre semántica y caché de HTTP."],
 "tipo_evaluacion": "Diagnóstica, formativa mediante prácticas e integración cruzada, y sumativa en el proyecto final.",
 "criterios": [("Prácticas de implementación del servicio",25),
   ("Consumo de servicios de terceros con manejo de fallas",15),
   ("Documentación del contrato en OpenAPI",15),
   ("Ejercicio cruzado de integración entre equipos",15),
   ("Proyecto final: servicio con autenticación y pruebas",30)],
 "nota": """
Sustituye en Programación para Internet (I5909) las unidades de conexión a
datos por DOM/XML/AJAX (5 h), gestores de contenido (8 h), SEO (5 h) y WPO
(7 h): 25 de sus 68 horas. Esa materia conserva HTML5, CSS3, JavaScript,
patrones de diseño y marcos de trabajo, y deja de cargar temas de mercadotecnia.
""",
},
{
 "archivo": "I5918-pruebas-de-software-y-automatizacion.md",
 "nombre": "Pruebas de Software y Automatización", "clave": "I5918",
 "modalidad": "Escolarizada", "tipo": "Curso", "creditos": 8,
 "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 34, "practica": 34, "total": 68,
 "seriacion": "Ingeniería de Software I (I5898), Desarrollo Colaborativo y Control de Versiones (I5916)",
 "departamento": "Ciencias Computacionales", "academia": "Ingeniería de Software",
 "presentacion": """
En los programas vigentes la palabra «pruebas» aparece como una fase del ciclo
de vida: algo que ocurre después de construir y antes de entregar. No aparece
como actividad de ingeniería con técnica propia. No hay mención de pruebas
unitarias, automatización ni depuración sistemática.

La diferencia es grande. Probar como fase produce una lista de defectos al
final. Probar como práctica produce un conjunto de comprobaciones que se
ejecutan con cada cambio y que permiten modificar el sistema sin miedo. Esa
segunda idea es la que sostiene el trabajo en equipo sobre bases de código que
viven años, y es la que esta unidad enseña.
""",
 "competencia": """
Construye y mantiene conjuntos de pruebas automatizadas que verifican el
comportamiento de un sistema en distintos niveles, integrándolos a un proceso
de ejecución continua que impide la incorporación de regresiones.
""",
 "saber": ["Niveles de prueba y qué defecto detecta cada uno",
           "Dobles de prueba y sus usos legítimos",
           "Relación entre acoplamiento, diseño y facilidad de prueba",
           "Límites e interpretación errónea de la cobertura"],
 "saber_hacer": ["Escribir pruebas unitarias aisladas y deterministas",
                 "Aplicar desarrollo guiado por pruebas",
                 "Automatizar la ejecución ante cada cambio",
                 "Diagnosticar una prueba intermitente"],
 "saber_ser": ["Trata una prueba que falla como información y no como estorbo",
               "Prefiere comportamiento verificado sobre porcentaje de cobertura",
               "Deja el código mejor estructurado de como lo encontró"],
 "comp_generica": "Pensamiento crítico y capacidad de verificar afirmaciones con evidencia.",
 "comp_profesional": "Aseguramiento de la calidad del software mediante verificación automatizada.",
 "previas": ["Programación orientada a objetos", "Nociones de diseño de software", "Uso de control de versiones"],
 "perfil_egreso": """
Contribuye al egresado capaz de sostener y modificar sistemas existentes sin
degradar su comportamiento, y de entregar software cuya corrección puede
demostrarse.
""",
 "perfil_docente": """
Profesional con experiencia en mantenimiento de sistemas en producción
respaldados por conjuntos de pruebas automatizadas.
""",
 "contenido": [
  {"titulo":"Por qué se prueba","horas":6,
   "temas":["Costo del defecto según el momento de detección","Taxonomía de pruebas","Qué no puede demostrar una prueba"]},
  {"titulo":"Pruebas unitarias","horas":14,
   "temas":["Aislamiento y determinismo","Dobles de prueba: sustitutos, espías y simuladores","Diseño orientado a la verificabilidad","Nombrado y organización del conjunto de pruebas"]},
  {"titulo":"Desarrollo guiado por pruebas","horas":12,
   "temas":["Ciclo rojo-verde-refactorización","Diseño emergente","Límites y críticas de la técnica"]},
  {"titulo":"Pruebas de integración y de contrato","horas":10,
   "temas":["Dependencias reales frente a sustitutos","Datos de prueba y aislamiento entre casos","Contratos entre componentes"]},
  {"titulo":"Pruebas de extremo a extremo","horas":8,
   "temas":["Automatización de interfaz","Costo, lentitud y fragilidad","Cuántas conviene tener"]},
  {"titulo":"Cobertura y refactorización","horas":8,
   "temas":["Medición de cobertura e interpretación honesta","Calidad del conjunto de pruebas","Refactorización respaldada por pruebas"]},
  {"titulo":"Automatización e integración continua","horas":10,
   "temas":["Ejecución ante cada cambio","Canalizaciones de construcción y prueba","Pruebas intermitentes: causas y manejo","Criterios de bloqueo de integración"]},
 ],
 "estrategias": ["Todo el código entregado en la materia se acompaña de sus pruebas.",
   "Ejercicio de refactorización: se entrega código correcto pero mal estructurado, que debe reestructurarse sin alterar el comportamiento, demostrado por las pruebas.",
   "Recepción de un proyecto ajeno y construcción de pruebas de caracterización sobre él."],
 "bib_basica": ["Khorikov, V. (2020). *Unit Testing: Principles, Practices, and Patterns*. Manning.",
   "Beck, K. (2002). *Test-Driven Development: By Example*. Addison-Wesley."],
 "bib_comp": ["Crispin, L. y Gregory, J. (2009). *Agile Testing*. Addison-Wesley.",
   "Feathers, M. (2004). *Working Effectively with Legacy Code*. Prentice Hall.",
   "Humble, J. y Farley, D. (2010). *Continuous Delivery*. Addison-Wesley."],
 "tipo_evaluacion": "Formativa continua sobre las prácticas y sumativa en el proyecto final y el ejercicio de refactorización.",
 "criterios": [("Prácticas de pruebas unitarias",25),
   ("Ejercicio de desarrollo guiado por pruebas",20),
   ("Refactorización respaldada por pruebas",15),
   ("Configuración de ejecución automática",15),
   ("Proyecto final con pruebas en varios niveles",25)],
 "nota": """
Toma las horas dedicadas al Proceso Unificado en Ingeniería de Software II
(I5900), cuyo contenido corresponde a la práctica de 1999 a 2007. Esa materia
conserva mantenimiento, calidad y MoProSoft, que siguen teniendo uso en la
industria local de certificación.
""",
},
{
 "archivo": "I5919-arquitectura-de-software.md",
 "nombre": "Arquitectura de Software", "clave": "I5919", "modalidad": "Escolarizada",
 "tipo": "Curso", "creditos": 8, "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 41, "practica": 27, "total": 68,
 "seriacion": "Ingeniería de Software II (I5900), Servicios Web y APIs (I5917)",
 "departamento": "Ciencias Computacionales", "academia": "Ingeniería de Software",
 "presentacion": """
La expresión «arquitectura de software» no aparece en ningún programa del plan
vigente. El estudiante aprende a construir componentes y a modelarlos con UML,
pero no a decidir cómo se reparte un sistema, qué atributos de calidad se
privilegian ni qué se sacrifica al elegir una estructura sobre otra.

Esa decisión distingue al ingeniero del programador y es la más cara de
corregir: un error de codificación se arregla en horas; uno de estructura
condiciona el sistema durante años. Esta unidad trata la arquitectura como el
conjunto de decisiones difíciles de revertir, y enseña a tomarlas
explícitamente y a dejarlas registradas.
""",
 "competencia": """
Evalúa alternativas de estructura para un sistema a partir de sus atributos de
calidad, justifica la elección frente a restricciones reales, la documenta de
forma que sobreviva al equipo que la tomó y reconoce cuándo debe revisarse.
""",
 "saber": ["Atributos de calidad y sus tensiones",
           "Estilos arquitectónicos y condiciones en que cada uno conviene",
           "Consistencia de datos en sistemas repartidos",
           "Deuda técnica como decisión y no como accidente"],
 "saber_hacer": ["Derivar requisitos de calidad de necesidades del negocio",
                 "Proponer y comparar alternativas estructurales",
                 "Documentar mediante vistas y registros de decisión",
                 "Evaluar una arquitectura existente por escenarios"],
 "saber_ser": ["Sostiene una decisión con argumentos y la revisa ante evidencia nueva",
               "Reconoce que toda elección de estructura implica una renuncia",
               "Escribe para quien mantendrá el sistema después"],
 "comp_generica": "Capacidad de tomar decisiones bajo incertidumbre y de argumentarlas.",
 "comp_profesional": "Definición y evaluación de la estructura de sistemas de software de mediana y gran escala.",
 "previas": ["Ingeniería de software y modelado", "Diseño e implementación de servicios", "Bases de datos"],
 "perfil_egreso": """
Contribuye al egresado capaz de asumir decisiones estructurales sobre sistemas
de escala real y de justificarlas ante equipos técnicos y no técnicos.
""",
 "perfil_docente": """
Profesional con experiencia en decisiones de estructura sobre sistemas en
producción y en su evolución a lo largo de varios años.
""",
 "contenido": [
  {"titulo":"Qué decide la arquitectura","horas":8,
   "temas":["Atributos de calidad y su especificación por escenarios","Restricciones del negocio y del entorno","Renuncias explícitas"]},
  {"titulo":"Estilos arquitectónicos","horas":14,
   "temas":["Monolito por capas y monolito modular","Arquitectura hexagonal y puertos y adaptadores","Arquitectura orientada a eventos","Servicios distribuidos: cuándo sí y cuándo no"]},
  {"titulo":"Documentación de la arquitectura","horas":10,
   "temas":["Vistas y sus audiencias","Modelo de contexto, contenedores y componentes","Registros de decisión arquitectónica","Documentación que envejece bien"]},
  {"titulo":"Datos y consistencia","horas":10,
   "temas":["Propiedad de los datos y duplicación","Consistencia fuerte y eventual","Transacciones repartidas y sus alternativas"]},
  {"titulo":"Escalabilidad y tolerancia a fallas","horas":12,
   "temas":["Escalamiento vertical y horizontal","Puntos únicos de falla","Degradación elegante y aislamiento","Capacidad y medición"]},
  {"titulo":"Deuda técnica y evolución","horas":8,
   "temas":["Origen y contabilidad de la deuda","Migración por etapas","Arquitecturas que admiten cambio"]},
  {"titulo":"Evaluación de arquitecturas","horas":6,
   "temas":["Evaluación por escenarios","Identificación de riesgos y puntos sensibles","Prototipos de los puntos de riesgo"]},
 ],
 "estrategias": ["Estudio de casos con restricciones contradictorias y defensa de la solución propuesta.",
   "Redacción de un registro de decisión arquitectónica por cada elección relevante.",
   "Evaluación por pares: cada equipo somete su arquitectura a los escenarios de calidad que propone otro equipo."],
 "bib_basica": ["Richards, M. y Ford, N. (2020). *Fundamentals of Software Architecture*. O'Reilly.",
   "Bass, L., Clements, P. y Kazman, R. (2021). *Software Architecture in Practice* (4a ed.). Addison-Wesley."],
 "bib_comp": ["Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.",
   "Newman, S. (2021). *Building Microservices* (2a ed.). O'Reilly.",
   "Ford, N., Parsons, R. y Kua, P. (2017). *Building Evolutionary Architectures*. O'Reilly."],
 "tipo_evaluacion": "Formativa mediante casos y registros de decisión; sumativa en la propuesta arquitectónica final y su evaluación por pares.",
 "criterios": [("Análisis de casos",20),("Registros de decisión arquitectónica",20),
   ("Documentación de vistas del sistema propuesto",20),
   ("Evaluación por escenarios de la arquitectura de otro equipo",15),
   ("Proyecto final: propuesta con prototipo de los puntos de riesgo",25)],
 "nota": """
Contenido nuevo, sin sustitución directa. Se ubica en sexto semestre, entre las
dos materias de Ingeniería de Software y el tercer Proyecto Modular, para que
la decisión estructural del proyecto final sea deliberada y no accidental.
""",
},
]
