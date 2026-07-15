# 🛰️ Curso: Estación espacial (ISS)

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso del laboratorio orbital.** Documenta la estación espacial de principio a
> fin: historia, características, sistemas (módulos, paneles solares, soporte
> vital de ciclo cerrado, control térmico, acoplamiento), centro de control y
> mandos, física de la microgravedad, entornos de la órbita baja, marco legal
> internacional y diseño de simulación. Toma como referencia la **Estación
> Espacial Internacional (ISS)**.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Módulos](https://img.shields.io/badge/modulos-10-blue)
![Marco](https://img.shields.io/badge/marco-acuerdo%20intergubernamental-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberías poder:

- Explicar que es una estación espacial y cómo se mantiene en órbita baja.
- Identificar sus módulos, paneles solares y sistemas de soporte vital.
- Comprender el soporte vital de ciclo cerrado que recicla aire y agua.
- Entender la microgravedad, el acoplamiento y las caminatas espaciales (EVA).
- Reconocer el papel del centro de control y de la tripulación.
- Conocer el acuerdo intergubernamental de los socios y los tratados espaciales.
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Sol[☀️ Luz solar] --> Paneles[🔆 Paneles solares]
    Paneles --> Energia[🔋 Energía]
    Energia --> Vital[🧑‍🚀 Soporte vital]
    Energia --> Termico[🌡️ Control térmico]
    Vital --> Tripulacion[Tripulación]
    Modulos[🧩 Módulos] --> Laboratorio[Laboratorio y habitat]
    Puertos[🔗 Puertos de acoplamiento] --> Naves[Naves de carga y tripulación]
    Control[📡 Centro de control] -. telemetria .-> Modulos
    Tripulacion --> Mantenimiento[🛠️ Mantenimiento y EVA]
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolución de las estaciones, línea de tiempo. | [Abrir](historia/historia-estacion-espacial.md) |
| 2 | 📋 Características | Que es, sus partes y para que sirve. | [Abrir](operacion/caracteristicas-estacion-espacial.md) |
| 3 | 🔧 Sistemas mecánicos | Módulos, paneles, soporte vital, acoplamiento, EVA. | [Abrir](operacion/sistemas-mecanicos-estacion-espacial.md) |
| 4 | 🎛️ Mandos e instrumentos | Centro de control, telemetría y estaciones de trabajo. | [Abrir](mandos/manual-mandos-estacion-espacial.md) |
| 5 | 🧪 Principios y operación | Microgravedad, órbita baja y fases de operación. | [Abrir](operacion/principios-estacion-espacial.md) |
| 6 | 🌍 Entornos de trabajo | Órbita baja, interior habitable y espacio abierto. | [Abrir](operacion/entornos-estacion-espacial.md) |
| 7 | ⚖️ Reglamentos | Acuerdo intergubernamental y tratados espaciales. | [Abrir](reglamentos/reglamentos-estacion-espacial.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-estacion-espacial.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-estacion-espacial.md) |
| 10 | 🎯 Ejercicios | Autoevaluación con respuestas plegadas. | [Abrir](ejercicios/ejercicios-estacion-espacial.md) |

---

## 🧩 Requisitos previos

Se recomienda revisar antes el curso de
[🚀 naves espaciales](../naves-espaciales/README.md), que introduce la órbita, el
delta-v y la microgravedad, y el de [🚀 cohetes](../cohetes/README.md), que explica
como llega la carga a la órbita. La estación es un habitat permanente en órbita
baja. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-estacion-espacial.md)
