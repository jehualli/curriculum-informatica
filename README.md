# Materias faltantes — Ingeniería Informática (CUCEI, plan 2015B)

**Ejercicio de diseño curricular. Propuesta no oficial, sin relación con la
Universidad de Guadalajara.**

Se analizaron los 27 programas publicados del plan 2015B y la malla curricular
(334 créditos, 8 semestres). El análisis encontró que la formación básica es
sólida y duradera, que cerca del 11 % de los créditos verificables corresponde
a contenido superado por la práctica actual, y que un conjunto de temas hoy
indispensables no aparece en ningún documento del plan.

Este repositorio contiene esos temas escritos como programas formales de
unidad de aprendizaje, con la misma estructura administrativa que usan los
programas oficiales, para responder a una sola pregunta: **¿cómo se vería el
plan si esos huecos estuvieran cubiertos?**

## Ausencias verificadas

Búsqueda literal sobre los 27 programas publicados. Cero apariciones de:

`git` · `subversion` · `control de versiones` · `docker` · `contenedor` ·
`kubernetes` · `aws` · `azure` · `nube` · `microservicio` · `devops` ·
`integración continua` · `pruebas unitarias` · `testing` · `rest` ·
`graphql` · `react` · `angular` · `node.js` · `android` · `ios` · `scrum` ·
`kanban` · `tdd` · `refactorización` · `usabilidad` · `ux` ·
`arquitectura de software` · `escalabilidad`

Dos hallazgos corrigen el análisis inicial: el plan **sí** incluye
*Seguridad de la Información* (I5905) y *Control de Proyectos* (I5901). Sus
programas no estaban publicados en la página de la carrera.

## Programas propuestos

| Clave | Unidad de aprendizaje | Cr | Hrs | Sem | Sustituye / complementa |
|---|---|---:|---:|---:|---|
| I5916 | Desarrollo Colaborativo y Control de Versiones | 5 | 68 | 1 | nuevo; se integra a la carga de seminarios |
| I5924 | Experiencia de Usuario y Accesibilidad | 8 | 68 | 4 | Hipermedia (I5910) |
| I5917 | Servicios Web y APIs | 8 | 68 | 5 | unidades de AJAX/XML, CMS, SEO y WPO de I5909 |
| I5918 | Pruebas de Software y Automatización | 8 | 68 | 5 | horas de RUP en Ingeniería de Software II (I5900) |
| I5919 | Arquitectura de Software | 8 | 68 | 6 | nuevo |
| I5920 | Cómputo en la Nube y Contenedores | 8 | 68 | 6 | mitad de Administración de Servidores (I5908) |
| I5921 | Sistemas Distribuidos y Concurrencia | 8 | 68 | 6 | llena el hueco del Módulo 3 |
| I5922 | Desarrollo de Aplicaciones Móviles | 8 | 68 | 7 | Hipermedia (I5910) |
| I5923 | Aprendizaje Automático | 8 | 68 | 8 | actualiza la línea de Sistemas Basados en Conocimiento |

Total propuesto: **69 créditos**.

## Aritmética honesta

El análisis identificó 47 créditos recuperables (35 de contenido superado,
12 de bajo rendimiento formativo). La propuesta pide 69. **Faltan 22
créditos**, y hay tres caminos:

1. El plan crece de 334 a 356 créditos. Es la salida fácil y la peor.
2. I5916 no se imparte como materia sino dentro de los seminarios que ya
   existen, y I5924 toma el lugar completo de Hipermedia. Eso recupera 13
   créditos y deja un faltante de 9.
3. Se reduce el Módulo 4 (*Cómputo Flexible*, 91 créditos, 27 % del plan) en
   una materia. Es el módulo con mayor peso y el de contenido más antiguo.

La opción 2 combinada con la 3 cierra la cuenta sin crecer.

## Una nota sobre los Proyectos Modulares

Los tres Proyectos Modulares suman 60 créditos, el 18 % del plan, y son el
espacio donde estos temas aparecen hoy: no por diseño, sino porque el
estudiante los necesita para construir lo que se propuso. Eso funciona para
quien ya sabe qué buscar y deja sin piso a quien no. Estos programas existen
para que ese piso no dependa del estudiante.

## Estructura

```
programas/    un archivo por unidad de aprendizaje propuesta
```

Cada programa incluye identificación, presentación, competencia, tipos de
saberes, contenidos temáticos con horas, estrategias de enseñanza, criterios
de evaluación, bibliografía y perfil docente. La suma de horas de cada
programa es 68, como en los programas oficiales.
