# 🚀 Curso: Cohetes

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso de lanzadores actuales.** Documenta el cohete lanzador de principio a
> fin: historia, características, sistemas (motores de combustible líquido y
> sólido, etapas, estructura, avionica), control de misión, física del empuje y
> la ecuación del cohete, entornos de lanzamiento, marco legal internacional y
> diseño de simulación. Se centra en **cohetes reales de hoy**, incluida la
> recuperación de propulsores reutilizables.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Módulos](https://img.shields.io/badge/modulos-11-blue)
![Marco](https://img.shields.io/badge/marco-tratados%20espaciales-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberías poder:

- Explicar como un cohete vence la gravedad y alcanza la velocidad orbital.
- Identificar motores de combustible líquido y sólido, etapas y estructura.
- Comprender el empuje, la relación empuje-peso y la ecuación del cohete.
- Entender la separación de etapas y el aterrizaje de un propulsor reutilizable.
- Reconocer el control de misión, la telemetría y la cuenta atrás.
- Conocer el marco de tratados espaciales que aplica al lanzamiento.
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Propelente[⛽ Propelente] --> Motor[🔧 Motores]
    Motor --> Empuje[Empuje]
    Empuje --> Etapa1[Etapa 1 propulsor]
    Etapa1 --> Separacion[Separación de etapas]
    Separacion --> Etapa2[Etapa 2 superior]
    Etapa2 --> Orbita[🛰️ Carga en órbita]
    Separacion --> Retorno[Propulsor aterriza]
    Avionica[🎛️ Avionica] --> Guiado[Guiado y control]
    Guiado --> Motor
    Tierra[📡 Control de misión] -. telemetria .-> Avionica
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolución del cohete, línea de tiempo. | [Abrir](historia/historia-cohete.md) |
| 2 | 📋 Características | Que es, tipos de cohete y para que sirve cada uno. | [Abrir](operacion/caracteristicas-cohete.md) |
| 3 | 🧩 Modelos y variantes | Que cambia entre modelos: manejo, mando y simulador. | [Abrir](modelos/modelos-cohete.md) |
| 4 | 🔧 Sistemas mecánicos | Motores, propelentes, etapas, estructura, avionica. | [Abrir](operacion/sistemas-mecanicos-cohete.md) |
| 5 | 🎛️ Mandos e instrumentos | Control de misión, telemetría y cuenta atrás. | [Abrir](mandos/manual-mandos-cohete.md) |
| 6 | 🧪 Principios y operación | Empuje, ecuación del cohete y fases de vuelo. | [Abrir](operacion/principios-cohete.md) |
| 7 | 🌍 Entornos de trabajo | Plataforma, ascenso, órbita y retorno del propulsor. | [Abrir](operacion/entornos-cohete.md) |
| 8 | ⚖️ Reglamentos | Estado de lanzamiento y tratados espaciales. | [Abrir](reglamentos/reglamentos-cohete.md) |
| 9 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-cohete.md) |
| 10 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-cohete.md) |
| 11 | 🎯 Ejercicios | Autoevaluación con respuestas plegadas. | [Abrir](ejercicios/ejercicios-cohete.md) |

---

## 🧩 Requisitos previos

Se recomienda revisar antes el curso de
[🚀 naves espaciales](../naves-espaciales/README.md), que introduce la órbita, el
delta-v y la microgravedad. El cohete profundiza en la fase más exigente: el
lanzamiento y el ascenso hasta la órbita. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-cohete.md)
