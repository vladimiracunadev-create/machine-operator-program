# 🛫 Curso: Aviones de pasajeros

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso de aviación comercial de transporte.** Documenta el avión de pasajeros
> de principio a fin: historia, características, sistemas de la aeronave en
> profundidad, cabina de vuelo, física del vuelo, entornos aeronáuticos,
> reglamentos chilenos y diseño de simulación. El eje del curso es la operación
> comercial segura de una aeronave de transporte de pasajeros.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Módulos](https://img.shields.io/badge/modulos-10-blue)
![Licencia Chile](https://img.shields.io/badge/licencia-ATP%20DGAC-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberías poder:

- Explicar como un avión de pasajeros genera sustentación, avanza, gira y desciende.
- Identificar el fuselaje presurizado, las alas, las superficies de control y los motores turbofan.
- Reconocer los instrumentos de la cabina de vuelo y los mandos de una aeronave de transporte.
- Comprender la física del vuelo (sustentación, resistencia, empuje, peso) a alta velocidad y altitud.
- Conocer el marco aeronáutico chileno (DGAC, licencia ATP, operación comercial AOC).
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Combustible[⛽ Combustible] --> Motores[🔧 Motores turbofan]
    Motores --> Empuje[Empuje]
    Alas[🛫 Alas] --> Sustentacion[Sustentación]
    Alas --> Hiper[Flaps y slats]
    Yugo[🎛️ Yugo / sidestick] --> Alerones[Alerones y spoilers]
    Yugo --> Profundidad[Timón de profundidad]
    Pedales[Pedales] --> Direccion[Timón de dirección]
    Alerones --> Alabeo[Alabeo]
    Profundidad --> Cabeceo[Cabeceo]
    Direccion --> Guinada[Guiñada]
    Motores --> Sistemas[Hidráulico y eléctrico]
    Sistemas --> Presion[Presurización]
    Presion --> Cabina[👥 Cabina de pasaje]
    Avionica[📊 Avionica y FMS] -. informa .-> Pilotos[🧍 Tripulación de vuelo]
    Pilotos --> Yugo
    Pilotos --> Pedales
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolución del avión de pasajeros, línea de tiempo. | [Abrir](historia/historia-avion-pasajeros.md) |
| 2 | 📋 Características | Que es, tipos de avión de pasajeros y para que sirve cada uno. | [Abrir](operacion/caracteristicas-avion-pasajeros.md) |
| 3 | 🔧 Sistemas mecánicos | Fuselaje presurizado, alas, control, turbofan, sistemas y avionica. | [Abrir](operacion/sistemas-mecanicos-avion-pasajeros.md) |
| 4 | 🎛️ Mandos e instrumentos | Cabina de vuelo, controles y avionica. | [Abrir](mandos/manual-mandos-avion-pasajeros.md) |
| 5 | 🧪 Principios y operación | Física del vuelo y fases de operación comercial. | [Abrir](operacion/principios-avion-pasajeros.md) |
| 6 | 🌍 Entornos de trabajo | Aeropuerto, espacio aéreo controlado y meteorología. | [Abrir](operacion/entornos-avion-pasajeros.md) |
| 7 | ⚖️ Reglamentos | Ley chilena: DGAC, licencia ATP, operación comercial. | [Abrir](reglamentos/reglamentos-avion-pasajeros.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-avion-pasajeros.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-avion-pasajeros.md) |
| 10 | 🎯 Ejercicios | Autoevaluación con respuestas plegadas. | [Abrir](ejercicios/ejercicios-avion-pasajeros.md) |

---

## 🧩 Requisitos previos

Conviene haber visto antes el curso de
[🛩️ Aviones pequeños](../aviones-pequenos/README.md), que introduce el vuelo en
tres ejes y la física básica con menor complejidad. El avión de pasajeros agrega
la presurización, los motores turbofan, la operación a gran altitud y el marco de
la aviación comercial. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-avion-pasajeros.md)
