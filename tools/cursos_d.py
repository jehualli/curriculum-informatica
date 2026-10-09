# -*- coding: utf-8 -*-
CURSOS = [
{
 "archivo": "I5922-desarrollo-de-aplicaciones-moviles.md",
 "nombre": "Desarrollo de Aplicaciones Móviles", "clave": "I5922",
 "modalidad": "Escolarizada", "tipo": "Curso", "creditos": 8,
 "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 27, "practica": 41, "total": 68,
 "seriacion": "Servicios Web y APIs (I5917), Experiencia de Usuario y Accesibilidad (I5924)",
 "departamento": "Ciencias Computacionales", "academia": "Sistemas de Información",
 "presentacion": """
El plan vigente no menciona el desarrollo para dispositivos móviles en ningún
documento. Programación para Internet dedica cuatro horas a «Web Móvil», que
trata el tema como una adaptación del sitio de escritorio.

Un dispositivo móvil no es una pantalla pequeña: es un entorno con batería
finita, conectividad intermitente, permisos revocables, un sistema operativo
que suspende procesos sin aviso y un ciclo de publicación controlado por un
tercero. Esta unidad trata esas restricciones como el contenido y no como
detalles de implementación. Se trabaja con un marco multiplataforma para que
el aprendizaje no dependa de un sistema operativo concreto.
""",
 "competencia": """
Construye aplicaciones para dispositivos móviles que funcionan de forma
razonable con conectividad intermitente, administran el estado local, respetan
el modelo de permisos y el ciclo de vida de la plataforma, y pueden publicarse
en una tienda de distribución.
""",
 "saber": ["Ciclo de vida de una aplicación móvil y suspensión de procesos",
           "Modelo de permisos y privacidad de la plataforma",
           "Restricciones de energía, red y almacenamiento",
           "Requisitos de publicación y revisión"],
 "saber_hacer": ["Construir interfaces declarativas con navegación",
                 "Administrar estado y persistencia local",
                 "Sincronizar con servicios remotos tolerando la pérdida de conexión",
                 "Medir consumo y preparar una entrega firmada"],
 "saber_ser": ["Diseña para la interrupción y no para el caso ideal",
               "Considera el costo de datos y batería del usuario como responsabilidad propia",
               "Solicita únicamente los permisos que la función requiere"],
 "comp_generica": "Capacidad de diseñar soluciones bajo restricciones de recursos.",
 "comp_profesional": "Desarrollo y publicación de aplicaciones para dispositivos móviles.",
 "previas": ["Consumo de servicios web", "Fundamentos de diseño de interfaces", "Programación orientada a objetos"],
 "perfil_egreso": """
Contribuye al egresado capaz de llevar una aplicación móvil desde su diseño
hasta su publicación y mantenimiento, considerando las restricciones reales
del dispositivo y de su usuario.
""",
 "perfil_docente": """
Profesional con aplicaciones publicadas en tiendas de distribución y
experiencia en su mantenimiento posterior a la publicación.
""",
 "contenido": [
  {"titulo":"La plataforma móvil","horas":8,
   "temas":["Ciclo de vida y suspensión de procesos","Modelo de permisos","Recursos limitados: batería, red, almacenamiento","Fragmentación de dispositivos y versiones"]},
  {"titulo":"Interfaz y navegación","horas":12,
   "temas":["Interfaz declarativa y composición","Navegación y pila de pantallas","Adaptación a tamaños y orientaciones","Componentes propios de la plataforma"]},
  {"titulo":"Estado y persistencia local","horas":12,
   "temas":["Administración de estado","Almacenamiento estructurado en el dispositivo","Migración de datos entre versiones","Datos sensibles y cifrado en reposo"]},
  {"titulo":"Servicios y operación sin conexión","horas":12,
   "temas":["Consumo de servicios remotos","Almacenamiento temporal y política de vigencia","Cola de operaciones pendientes","Sincronización diferida y resolución de conflictos"]},
  {"titulo":"Notificaciones y segundo plano","horas":8,
   "temas":["Notificaciones locales y remotas","Trabajo en segundo plano y sus límites","Consentimiento del usuario"]},
  {"titulo":"Pruebas y rendimiento","horas":8,
   "temas":["Pruebas en dispositivo y en emulador","Medición de consumo de batería y datos","Tiempo de arranque y fluidez"]},
  {"titulo":"Publicación","horas":8,
   "temas":["Firma de la aplicación","Requisitos de las tiendas y proceso de revisión","Actualizaciones y compatibilidad","Distribución de versiones de prueba"]},
 ],
 "estrategias": ["Desarrollo de una aplicación propia a lo largo del semestre.",
   "Prueba obligatoria en modo avión y con red degradada.",
   "Medición de consumo de batería y datos, con comparación entre equipos.",
   "Revisión cruzada de permisos solicitados y su justificación."],
 "bib_basica": ["Documentación oficial de la plataforma móvil seleccionada y del marco multiplataforma en uso, versión vigente.",
   "Griffiths, D. y Griffiths, D. (2021). *Head First Android Development* (3a ed.). O'Reilly."],
 "bib_comp": ["Neil, T. (2014). *Mobile Design Pattern Gallery* (2a ed.). O'Reilly.",
   "Lineamientos de interfaz humana de las plataformas de distribución, versión vigente."],
 "tipo_evaluacion": "Formativa sobre la aplicación en desarrollo; sumativa en la entrega publicable y sus mediciones.",
 "criterios": [("Prácticas de interfaz y navegación",20),
   ("Persistencia local y sincronización",20),
   ("Comportamiento sin conexión",15),
   ("Medición de rendimiento y consumo",15),
   ("Proyecto final publicable con paquete firmado",30)],
 "nota": """
Toma el lugar de Hipermedia (I5910), cuyo contenido quedó absorbido por el
diseño web general y cuya bibliografía vigente incluye un libro de programación
en Python sin relación aparente con la materia.
""",
},
{
 "archivo": "I5923-aprendizaje-automatico.md",
 "nombre": "Aprendizaje Automático", "clave": "I5923", "modalidad": "Escolarizada",
 "tipo": "Curso", "creditos": 8, "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 34, "practica": 34, "total": 68,
 "seriacion": "Estadística y Procesos Estocásticos (I5897), Minería de Datos (I5911)",
 "departamento": "Ciencias Computacionales", "academia": "Cómputo Flexible",
 "presentacion": """
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
""",
 "competencia": """
Formula un problema como tarea de aprendizaje, prepara los datos, entrena y
evalúa modelos con metodología correcta, interpreta sus límites y los pone en
operación con monitoreo de su degradación.
""",
 "saber": ["Aprendizaje supervisado y no supervisado",
           "Compromiso entre sesgo y varianza; sobreajuste",
           "Métricas según el problema y el costo del error",
           "Fuga de información entre entrenamiento y evaluación"],
 "saber_hacer": ["Preparar y explorar un conjunto de datos",
                 "Entrenar modelos de referencia antes que modelos complejos",
                 "Validar correctamente e interpretar resultados",
                 "Desplegar y vigilar un modelo en operación"],
 "saber_ser": ["Desconfía de una métrica alta antes de auditar la partición de datos",
               "Reconoce sesgos en los datos y sus consecuencias sobre personas",
               "Informa los límites del modelo junto con sus resultados"],
 "comp_generica": "Pensamiento estadístico y honestidad en el reporte de resultados.",
 "comp_profesional": "Construcción, evaluación y operación de modelos de aprendizaje sobre datos reales.",
 "previas": ["Estadística y probabilidad", "Minería de datos", "Programación y manejo de datos"],
 "perfil_egreso": """
Contribuye al egresado capaz de decidir si un problema se resuelve con reglas o
con aprendizaje, de evaluar un modelo con rigor y de explicar honestamente sus
límites.
""",
 "perfil_docente": """
Formación en estadística, matemáticas o cómputo, con experiencia en
construcción y evaluación de modelos sobre datos reales.
""",
 "contenido": [
  {"titulo":"Del sistema de reglas al modelo estadístico","horas":6,
   "temas":["Qué resuelve cada enfoque","Qué se gana y qué se pierde","Cuándo no usar aprendizaje automático"]},
  {"titulo":"Datos","horas":10,
   "temas":["Obtención y limpieza","Representación de variables","Exploración y visualización","Fuga de información: origen y detección"]},
  {"titulo":"Aprendizaje supervisado","horas":14,
   "temas":["Regresión","Clasificación","Modelos de referencia","Árboles y métodos de conjunto"]},
  {"titulo":"Evaluación","horas":12,
   "temas":["Partición y validación cruzada","Métricas y costo del error","Sobreajuste y regularización","Diagnóstico de errores del modelo"]},
  {"titulo":"Aprendizaje no supervisado","horas":8,
   "temas":["Agrupamiento","Reducción de dimensiones","Evaluación sin etiquetas"]},
  {"titulo":"Redes neuronales","horas":10,
   "temas":["Perceptrón multicapa y entrenamiento","Cuándo aportan y cuándo no","Costo computacional y de datos"]},
  {"titulo":"Puesta en operación","horas":8,
   "temas":["Servicio de inferencia","Versionado de datos y modelos","Monitoreo de degradación","Reentrenamiento"]},
 ],
 "estrategias": ["Todo proyecto inicia con un modelo de referencia trivial que debe superarse.",
   "Auditoría cruzada: cada equipo busca fugas de información en el trabajo de otro equipo.",
   "Discusión de casos documentados de modelos con sesgo y de sus consecuencias."],
 "bib_basica": ["Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow* (3a ed.). O'Reilly.",
   "James, G., Witten, D., Hastie, T. y Tibshirani, R. (2021). *An Introduction to Statistical Learning* (2a ed.). Springer. Disponible en línea sin costo."],
 "bib_comp": ["Murphy, K. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.",
   "Huyen, C. (2022). *Designing Machine Learning Systems*. O'Reilly."],
 "tipo_evaluacion": "Formativa sobre las prácticas y la auditoría cruzada; sumativa en el modelo final y su protocolo de evaluación.",
 "criterios": [("Prácticas de preparación y exploración de datos",20),
   ("Entrenamiento y comparación contra el modelo de referencia",20),
   ("Protocolo de evaluación y diagnóstico de errores",20),
   ("Auditoría del trabajo de otro equipo",10),
   ("Proyecto final con modelo en operación y monitoreo",30)],
 "nota": """
Actualiza la línea de Sistemas Basados en Conocimiento (I5913 y su seminario
I5914), que dedica 28 de 68 horas a un motor de reglas cuya vigencia industrial
terminó alrededor de 2010. La tradición de cómputo flexible se conserva en las
materias de lógica difusa y clasificación inteligente.
""",
},
{
 "archivo": "I5924-experiencia-de-usuario-y-accesibilidad.md",
 "nombre": "Experiencia de Usuario y Accesibilidad", "clave": "I5924",
 "modalidad": "Escolarizada", "tipo": "Curso", "creditos": 8,
 "area": "Especializante obligatoria",
 "hora_semana": 4, "teoria": 27, "practica": 41, "total": 68,
 "seriacion": "Programación para Internet (I5909)",
 "departamento": "Ciencias Computacionales", "academia": "Sistemas de Información",
 "presentacion": """
Las palabras «usabilidad» y «experiencia de usuario» no aparecen en ningún
programa del plan vigente; «accesibilidad» aparece una sola vez. El plan
incluye Hipermedia y Programación para Internet, de modo que el estudiante
construye interfaces durante toda la carrera sin haber estudiado nunca cómo se
evalúa si una interfaz funciona.

Esta unidad no es un curso de diseño gráfico. Trata la interfaz como un
problema de ingeniería con criterios verificables: si el usuario completa la
tarea, cuántos errores comete, cuánto tarda y si puede usarla alguien que no ve
la pantalla. La accesibilidad ocupa la unidad más extensa por dos razones: es
obligación legal en un número creciente de contextos y es la parte del diseño
de interfaces con criterios objetivos y comprobables.
""",
 "competencia": """
Diseña y evalúa interfaces a partir de las tareas reales de sus usuarios,
aplicando criterios de accesibilidad verificables y midiendo la usabilidad con
métodos reproducibles.
""",
 "saber": ["Modelos de tarea y contexto de uso",
           "Principios de interacción y carga cognitiva",
           "Criterios de accesibilidad y tecnologías de asistencia",
           "Métodos de evaluación y su validez"],
 "saber_hacer": ["Levantar requisitos mediante observación",
                 "Construir prototipos de distinta fidelidad",
                 "Auditar una interfaz contra criterios de accesibilidad",
                 "Conducir una prueba de usabilidad e interpretar sus resultados"],
 "saber_ser": ["Separa la preferencia personal de la evidencia de uso",
               "Asume que la persona con discapacidad es usuaria y no caso excepcional",
               "Rechaza patrones de diseño que manipulan al usuario"],
 "comp_generica": "Empatía, observación sistemática y comunicación con usuarios no técnicos.",
 "comp_profesional": "Diseño y evaluación de interfaces usables y accesibles.",
 "previas": ["Desarrollo de interfaces web", "Nociones de ingeniería de requisitos"],
 "perfil_egreso": """
Contribuye al egresado capaz de justificar sus decisiones de interfaz con
evidencia de uso y de entregar productos utilizables por personas con
discapacidad.
""",
 "perfil_docente": """
Profesional con experiencia en diseño y evaluación de interfaces, incluyendo
conducción de pruebas con usuarios y auditorías de accesibilidad.
""",
 "contenido": [
  {"titulo":"Usuarios, tareas y contexto","horas":10,
   "temas":["Observación y entrevista","Definición del problema","Perfiles y escenarios de uso","Del requisito declarado al comportamiento observado"]},
  {"titulo":"Arquitectura de información","horas":10,
   "temas":["Organización del contenido","Nomenclatura y etiquetado","Diseño de flujos de tarea","Navegación y orientación"]},
  {"titulo":"Principios de interacción","horas":10,
   "temas":["Retroalimentación y visibilidad del estado","Prevención y recuperación de errores","Carga cognitiva y consistencia","Formularios y entrada de datos"]},
  {"titulo":"Prototipado","horas":10,
   "temas":["Prototipo de baja fidelidad","Prototipo navegable","Iteración a partir de hallazgos","Comunicación del diseño al equipo"]},
  {"titulo":"Accesibilidad","horas":14,
   "temas":["Criterios WCAG y niveles de conformidad","Semántica y estructura del documento","Navegación por teclado y foco","Lectores de pantalla, contraste y texto alternativo"]},
  {"titulo":"Pruebas de usabilidad","horas":10,
   "temas":["Diseño de la prueba y selección de participantes","Conducción sin inducir respuestas","Métricas: éxito de tarea, errores, tiempo","Análisis y priorización de hallazgos"]},
  {"titulo":"Ética del diseño","horas":4,
   "temas":["Consentimiento y datos de los participantes","Patrones engañosos","Diseño persuasivo y sus límites"]},
 ],
 "estrategias": ["Prueba de usabilidad con al menos cinco personas ajenas al curso.",
   "Auditoría de accesibilidad sobre un sitio público real, con informe de hallazgos y propuesta de corrección.",
   "Ejercicio de navegación exclusiva por teclado y con lector de pantalla sobre el propio proyecto."],
 "bib_basica": ["Krug, S. (2014). *Don't Make Me Think, Revisited* (3a ed.). New Riders.",
   "W3C (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. Recomendación del W3C."],
 "bib_comp": ["Norman, D. (2013). *The Design of Everyday Things* (edición revisada). Basic Books.",
   "Rubin, J. y Chisnell, D. (2008). *Handbook of Usability Testing* (2a ed.). Wiley."],
 "tipo_evaluacion": "Formativa a lo largo de las iteraciones de diseño; sumativa en la auditoría, la prueba de usabilidad y el proyecto final.",
 "criterios": [("Investigación de usuarios y definición del problema",15),
   ("Prototipos e iteraciones documentadas",20),
   ("Auditoría de accesibilidad con informe",20),
   ("Prueba de usabilidad conducida y analizada",20),
   ("Proyecto final: interfaz accesible con evidencia de evaluación",25)],
 "nota": """
Toma la otra mitad del espacio de Hipermedia (I5910). Se ubica en cuarto
semestre, antes de Programación para Internet y de los proyectos modulares,
para que el estudiante evalúe interfaces antes de construir las suyas.
""",
},
]
