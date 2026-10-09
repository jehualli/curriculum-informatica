# -*- coding: utf-8 -*-
CURSOS = [
{
 "archivo": "I5920-computo-en-la-nube-y-contenedores.md",
 "nombre": "Cómputo en la Nube y Contenedores", "clave": "I5920",
 "modalidad": "Escolarizada", "tipo": "Curso", "creditos": 8,
 "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 27, "practica": 41, "total": 68,
 "seriacion": "Uso, Adaptación y Explotación de Sistemas Operativos (I5903), Administración de Redes (I5907)",
 "departamento": "Ciencias Computacionales", "academia": "Redes y Sistemas",
 "presentacion": """
Administración de Servidores enseña a instalar y configurar servicios sobre
una máquina que se puede tocar. Esa habilidad sigue siendo formativa —explica
qué es un servicio, un puerto y un permiso— pero dejó de describir cómo opera
la mayoría de los sistemas: la máquina se renta por minutos, se define en un
archivo y se reemplaza en lugar de repararse.

Esta unidad recoge esa mitad faltante. Su tema central no es un proveedor de
nube en particular, sino el cambio en la unidad de trabajo: del servidor que se
cuida al entorno que se describe, se reproduce y se descarta.
""",
 "competencia": """
Empaqueta, despliega y opera aplicaciones en entornos reproducibles, define la
infraestructura como código, instrumenta el sistema para poder observarlo y
estima el costo de las decisiones de despliegue.
""",
 "saber": ["Modelos de servicio y de despliegue; responsabilidad compartida",
           "Aislamiento por contenedor frente a virtualización completa",
           "Principios de infraestructura declarativa",
           "Señales de observabilidad y su uso"],
 "saber_hacer": ["Construir imágenes y componer varios servicios",
                 "Desplegar con escalamiento y verificación de salud",
                 "Describir infraestructura en código",
                 "Diagnosticar un sistema en ejecución y estimar su costo"],
 "saber_ser": ["Trata el entorno como algo reproducible y no como configuración manual irrepetible",
               "Considera el costo económico y energético como criterio de ingeniería",
               "Documenta lo necesario para que otro levante el sistema sin ayuda"],
 "comp_generica": "Capacidad de organizar el trabajo de forma reproducible y verificable.",
 "comp_profesional": "Despliegue y operación de sistemas sobre infraestructura rentada.",
 "previas": ["Administración de sistemas operativos", "Fundamentos de redes", "Control de versiones"],
 "perfil_egreso": """
Contribuye al egresado capaz de llevar un sistema desde su código hasta su
operación, con entornos reproducibles y con capacidad de diagnóstico sobre
sistemas en ejecución.
""",
 "perfil_docente": """
Profesional con experiencia en operación de sistemas desplegados en
infraestructura rentada y en diagnóstico de incidentes en producción.
""",
 "contenido": [
  {"titulo":"Modelos de servicio y de despliegue","horas":6,
   "temas":["Infraestructura, plataforma y software como servicio","Nube pública, privada e híbrida","Responsabilidad compartida y sus límites"]},
  {"titulo":"Contenedores","horas":14,
   "temas":["Aislamiento de procesos y de recursos","Imágenes, capas y registros","Construcción reproducible","Datos persistentes y volúmenes"]},
  {"titulo":"Composición de servicios","horas":10,
   "temas":["Varios servicios en un mismo entorno","Redes entre contenedores","Entornos de desarrollo reproducibles","Configuración y secretos"]},
  {"titulo":"Orquestación","horas":12,
   "temas":["Programación de cargas de trabajo","Escalamiento y verificación de salud","Actualizaciones progresivas y reversión","Descubrimiento de servicios"]},
  {"titulo":"Infraestructura como código","horas":10,
   "temas":["Declaración frente a procedimiento","Estado e idempotencia","Entornos equivalentes","Revisión de cambios de infraestructura"]},
  {"titulo":"Observabilidad","horas":10,
   "temas":["Registros estructurados","Métricas e indicadores de servicio","Trazas distribuidas","Alertas que valen la pena atender"]},
  {"titulo":"Costo, seguridad y cumplimiento","horas":6,
   "temas":["Estimación y control de costo","Identidad y permisos mínimos","Residencia de datos y obligaciones legales"]},
 ],
 "estrategias": ["Toda entrega se ejecuta dentro de un contenedor construido por el estudiante.",
   "Ejercicio de reproducibilidad: un equipo levanta el entorno de otro usando únicamente su repositorio.",
   "Simulación de fallas: el profesor detiene componentes y el estudiante diagnostica con las señales que instrumentó.",
   "Ejercicio de costo: estimación mensual de la arquitectura propuesta."],
 "bib_basica": ["Nickoloff, J. y Kuenzli, S. (2019). *Docker in Action* (2a ed.). Manning.",
   "Burns, B., Beda, J. y Hightower, K. (2022). *Kubernetes: Up and Running* (3a ed.). O'Reilly."],
 "bib_comp": ["Beyer, B., Jones, C., Petoff, J. y Murphy, N. (2016). *Site Reliability Engineering*. O'Reilly.",
   "Morris, K. (2020). *Infrastructure as Code* (2a ed.). O'Reilly."],
 "tipo_evaluacion": "Formativa mediante prácticas y ejercicios de diagnóstico; sumativa en el proyecto desplegado e instrumentado.",
 "criterios": [("Prácticas de empaquetado y composición",25),
   ("Despliegue orquestado con escalamiento",20),
   ("Infraestructura declarada en código",15),
   ("Diagnóstico de fallas mediante observabilidad",15),
   ("Proyecto final desplegado, instrumentado y con estimación de costo",25)],
 "nota": """
Toma la mitad de las horas de Administración de Servidores (I5908) dedicadas a
instalación manual. Esa materia conserva la parte formativa —servicios,
permisos, redes y bases de datos— y cede la operación al modelo actual.
""",
},
{
 "archivo": "I5921-sistemas-distribuidos-y-concurrencia.md",
 "nombre": "Sistemas Distribuidos y Concurrencia", "clave": "I5921",
 "modalidad": "Escolarizada", "tipo": "Curso", "creditos": 8,
 "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 41, "practica": 27, "total": 68,
 "seriacion": "Uso, Adaptación y Explotación de Sistemas Operativos (I5903), Estructuras de Datos II (I5888)",
 "departamento": "Ciencias Computacionales", "academia": "Ciencias de la Computación",
 "presentacion": """
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
""",
 "competencia": """
Razona sobre sistemas con varios hilos de ejecución y sobre sistemas repartidos
en varias máquinas, identificando condiciones de carrera, modos de falla
parcial y garantías de consistencia, e implementa soluciones correctas bajo
esas condiciones.
""",
 "saber": ["Condiciones de carrera, exclusión mutua, interbloqueo e inanición",
           "Modelos de memoria compartida y de paso de mensajes",
           "Fallas parciales, relojes y orden causal",
           "Tensión entre consistencia, disponibilidad y tolerancia a particiones"],
 "saber_hacer": ["Escribir código concurrente correcto",
                 "Reproducir y diagnosticar una condición de carrera",
                 "Implementar comunicación entre procesos en máquinas distintas",
                 "Razonar sobre el sistema cuando una parte deja de responder"],
 "saber_ser": ["Desconfía de la corrección aparente en sistemas concurrentes",
               "Asume la falla parcial como estado normal de operación",
               "Prefiere el argumento sobre el ensayo y error"],
 "comp_generica": "Razonamiento formal y capacidad de análisis de sistemas complejos.",
 "comp_profesional": "Diseño e implementación de sistemas concurrentes y distribuidos correctos.",
 "previas": ["Estructuras de datos y algoritmos", "Sistemas operativos: procesos y planificación", "Fundamentos de redes"],
 "perfil_egreso": """
Contribuye al egresado capaz de construir sistemas que siguen funcionando
cuando una de sus partes falla, y de explicar con precisión qué garantías
ofrece y cuáles no.
""",
 "perfil_docente": """
Formación en ciencias de la computación con experiencia en sistemas
concurrentes o repartidos, de origen académico o industrial.
""",
 "contenido": [
  {"titulo":"Concurrencia","horas":12,
   "temas":["Hilos y planificación","Condiciones de carrera y exclusión mutua","Interbloqueo, inanición y sus condiciones","Estructuras de datos concurrentes"]},
  {"titulo":"Modelos de concurrencia","horas":10,
   "temas":["Memoria compartida","Paso de mensajes","Actores y corrutinas","Comparación y criterios de elección"]},
  {"titulo":"Fundamentos distribuidos","horas":10,
   "temas":["Falla parcial y detección de fallas","Tiempo, relojes físicos y lógicos","Orden causal","Modelos de sistema: síncrono y asíncrono"]},
  {"titulo":"Replicación y consistencia","horas":12,
   "temas":["Replicación primaria y entre pares","Consistencia fuerte y eventual","Particiones de red y sus consecuencias","Resolución de conflictos"]},
  {"titulo":"Consenso","horas":10,
   "temas":["El problema del acuerdo","Elección de líder","Registro replicado","Límites teóricos"]},
  {"titulo":"Comunicación entre procesos","horas":8,
   "temas":["Llamada a procedimiento remoto","Colas de mensajes","Publicación y suscripción","Entrega al menos una vez y sus implicaciones"]},
  {"titulo":"Paralelismo de datos","horas":6,
   "temas":["Descomposición de problemas","Procesamiento por lotes","Límites del paralelismo"]},
 ],
 "estrategias": ["Ejercicios con condiciones de carrera reproducibles y su corrección argumentada.",
   "Implementación de un servicio replicado sencillo con elección de líder.",
   "Inyección de fallas: se interrumpe la comunicación entre nodos y se observa y explica el comportamiento resultante."],
 "bib_basica": ["Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.",
   "Tanenbaum, A. y Van Steen, M. (2023). *Distributed Systems* (4a ed.). Edición de los autores, disponible en línea."],
 "bib_comp": ["Herlihy, M., Shavit, N., Luchangco, V. y Spear, M. (2020). *The Art of Multiprocessor Programming* (2a ed.). Morgan Kaufmann.",
   "Ongaro, D. y Ousterhout, J. (2014). *In Search of an Understandable Consensus Algorithm*. USENIX ATC."],
 "tipo_evaluacion": "Formativa mediante prácticas de concurrencia; sumativa en el servicio replicado y su comportamiento bajo falla.",
 "criterios": [("Prácticas de programación concurrente",25),
   ("Diagnóstico y corrección de condiciones de carrera",15),
   ("Implementación de comunicación entre procesos remotos",20),
   ("Análisis del comportamiento bajo partición de red",15),
   ("Proyecto final: servicio replicado con tolerancia a fallas",25)],
 "nota": """
Contenido nuevo. Llena el hueco entre el nombre del Módulo 3 y su contenido
real. Es la propuesta más exigente y la que más se apoya en la base que el plan
ya tiene bien resuelta: estructuras de datos, algoritmia y sistemas operativos.
""",
},
]
