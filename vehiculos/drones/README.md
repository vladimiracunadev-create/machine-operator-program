# 🕹️ Curso: Drones

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso de aeronave pilotada a distancia (RPAS).** Documenta el dron de
> principio a fin: historia, características, mecánica en profundidad, mandos,
> física del vuelo multirotor, entornos, reglamentos chilenos y diseño de
> simulación. Sigue el modelo del curso de referencia del repositorio.

![Nivel](https://img.shields.io/badge/nivel-intermedio-yellow)
![Módulos](https://img.shields.io/badge/modulos-9-blue)
![Marco Chile](https://img.shields.io/badge/marco-DAN%20151-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como un dron multirotor genera sustentación y se mantiene estable.
- Identificar sus sistemas y cómo se conectan: motores, ESC, batería y controladora.
- Reconocer los mandos del radiocontrol y la estación de tierra y su función.
- Comprender la física del vuelo por variación de rpm de cada rotor.
- Conocer el marco chileno aplicable (DGAC, DAN 151, registro y restricciones).
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Bateria[🔋 Batería LiPo] --> ESC[Controladores ESC]
    ESC --> Motores[⚙️ Motores brushless]
    Motores --> Helices[Hélices y empuje]
    Controladora[🧠 Controladora de vuelo] --> ESC
    IMU[Sensores IMU y GPS] --> Controladora
    Radio[🎛️ Radiocontrol] --> Receptor[Receptor]
    Receptor --> Controladora
    Helices --> Estabilidad[Sustentación y estabilidad]
    Controladora -. telemetria .-> Piloto[🧍 Piloto a distancia]
    Piloto --> Radio
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolución del dron, línea de tiempo. | [Abrir](historia/historia-dron.md) |
| 2 | 📋 Características | Que es un RPAS, tipos de dron y para que sirve cada uno. | [Abrir](operacion/caracteristicas-dron.md) |
| 3 | 🔧 Sistemas mecánicos | Motores, ESC, hélices, batería, controladora, radio y cámara. | [Abrir](operacion/sistemas-mecanicos-dron.md) |
| 4 | 🎛️ Mandos e instrumentos | Radiocontrol, estación de tierra, sticks y telemetría. | [Abrir](mandos/manual-mandos-dron.md) |
| 5 | 🧪 Principios y operación | Física del vuelo multirotor y fases de operación. | [Abrir](operacion/principios-dron.md) |
| 6 | 🌍 Entornos de trabajo | Urbano, agrícola, industrial, interiores y zonas prohibidas. | [Abrir](operacion/entornos-dron.md) |
| 7 | ⚖️ Reglamentos | Marco chileno: DGAC, DAN 151, registro y restricciones. | [Abrir](reglamentos/reglamentos-dron.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-dron.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-dron.md) |

---

## 🧩 Requisitos previos

Conviene haber revisado antes el curso de helicópteros, porque el dron comparte
el vuelo de ala rotatoria y el marco aeronáutico de la DGAC, pero lo simplifica:
no lleva piloto a bordo, se gobierna a distancia y una controladora de vuelo
estabiliza el aparato variando el régimen de cada rotor. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-dron.md)
