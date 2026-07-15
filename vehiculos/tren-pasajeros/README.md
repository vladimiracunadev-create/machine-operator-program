# 🚆 Curso: Tren de pasajeros

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso del tren de pasajeros.** Documenta el tren de principio a fin:
> historia, características, mecánica en profundidad, mandos de cabina, física
> de la adherencia rueda-riel, entornos, marco ferroviario chileno y diseño de
> simulación. Sigue el modelo del curso de motos.

![Nivel](https://img.shields.io/badge/nivel-intermedio-yellow)
![Módulos](https://img.shields.io/badge/modulos-11-blue)
![Marco Chile](https://img.shields.io/badge/marco-Ferroviario%20EFE-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberías poder:

- Explicar como un tren acelera, frena y se guía sobre los rieles.
- Distinguir la tracción eléctrica de la tracción diesel-eléctrica.
- Identificar los sistemas mecánicos del tren y cómo se conectan.
- Reconocer los mandos del puesto del maquinista y su función.
- Comprender la adherencia rueda-riel, la gran masa y las distancias de frenado.
- Conocer el marco ferroviario chileno (EFE, MTT, habilitación del maquinista).
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Catenaria[⚡ Catenaria o línea] --> Pantografo[Pantógrafo]
    Pantografo --> Traccion[🔧 Equipo de tracción]
    Diesel[⛽ Motor diesel] --> Generador[Generador]
    Generador --> Traccion
    Traccion --> Motores[Motores de tracción]
    Motores --> Bogies[Bogies y ejes]
    Bogies --> Ruedas[Ruedas de pestaña]
    Ruedas --> Riel[Riel]
    Pupitre[🎛️ Pupitre de cabina] --> Traccion
    Pupitre --> Freno[🛑 Sistema de freno]
    Freno --> Ruedas
    Senales[🚦 Señalización] -. informa .-> Maquinista[🧍 Maquinista]
    Maquinista --> Pupitre
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Del vapor a la electrificación y los metros modernos. | [Abrir](historia/historia-tren-pasajeros.md) |
| 2 | 📋 Características | Que es un tren de pasajeros y sus tipos. | [Abrir](operacion/caracteristicas-tren-pasajeros.md) |
| 3 | 🧩 Modelos y variantes | Que cambia entre modelos: manejo, mando y simulador. | [Abrir](modelos/modelos-tren-pasajeros.md) |
| 4 | 🔧 Sistemas mecánicos | Tracción, bogies, adherencia, freno, señalización. | [Abrir](operacion/sistemas-mecanicos-tren-pasajeros.md) |
| 5 | 🎛️ Mandos e instrumentos | Puesto del maquinista, controles e indicadores. | [Abrir](mandos/manual-mandos-tren-pasajeros.md) |
| 6 | 🧪 Principios y operación | Adherencia, gran masa y fases de operación. | [Abrir](operacion/principios-tren-pasajeros.md) |
| 7 | 🌍 Entornos de trabajo | Metro, superficie, interurbano, túneles, estaciones. | [Abrir](operacion/entornos-tren-pasajeros.md) |
| 8 | ⚖️ Reglamentos | Marco ferroviario chileno: EFE, MTT, habilitación. | [Abrir](reglamentos/reglamentos-tren-pasajeros.md) |
| 9 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-tren-pasajeros.md) |
| 10 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-tren-pasajeros.md) |
| 11 | 🎯 Ejercicios | Autoevaluación con respuestas plegadas. | [Abrir](ejercicios/ejercicios-tren-pasajeros.md) |

---

## 🧩 Requisitos previos

Conviene haber revisado antes un vehículo terrestre más simple como la moto o el
bus, porque el tren comparte ideas de tracción y frenado pero agrega la guía
sobre rieles, la gran masa y el control por señales. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-tren-pasajeros.md)
