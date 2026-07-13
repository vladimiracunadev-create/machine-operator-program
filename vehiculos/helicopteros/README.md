# 🚁 Curso: Helicopteros

[🏠 Inicio](../../README.md) · [🚙 Catalogo de vehiculos](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso de aeronave de ala rotatoria.** Documenta el helicoptero de principio
> a fin: historia, caracteristicas, mecanica en profundidad, mandos, fisica del
> vuelo, entornos, reglamentos chilenos y diseno de simulacion. Sigue el modelo
> del curso de referencia del repositorio.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Modulos](https://img.shields.io/badge/modulos-9-blue)
![Licencia Chile](https://img.shields.io/badge/licencia-DAN%2061-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como un helicoptero genera sustentacion y logra el vuelo estacionario.
- Identificar sus sistemas mecanicos y como se conectan.
- Reconocer todos los mandos e instrumentos y su funcion.
- Comprender la fisica del vuelo de ala rotatoria (par, anti-par, autorrotacion).
- Conocer los reglamentos chilenos aplicables (licencia, certificacion, seguridad).
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Turbina[⚙️ Turbina / motor] --> Transmision[Transmision principal]
    Transmision --> RotorP[🚁 Rotor principal]
    Transmision --> RotorC[Rotor de cola]
    RotorP --> Sustentacion[Sustentacion y traccion]
    RotorC --> AntiPar[Compensacion del par]
    Colectivo[🎛️ Colectivo] --> RotorP
    Ciclico[🎛️ Ciclico] --> Plato[Plato ciclico]
    Plato --> RotorP
    Pedales[🦶 Pedales] --> RotorC
    Tablero[📊 Tablero] -. informa .-> Piloto[🧍 Piloto]
    Piloto --> Colectivo
    Piloto --> Ciclico
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolucion del helicoptero, linea de tiempo. | [Abrir](historia/historia-helicoptero.md) |
| 2 | 📋 Caracteristicas | Que es, tipos de helicoptero y para que sirve cada uno. | [Abrir](operacion/caracteristicas-helicoptero.md) |
| 3 | 🔧 Sistemas mecanicos | Rotor principal, rotor de cola, plato ciclico, transmision, turbina. | [Abrir](operacion/sistemas-mecanicos-helicoptero.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto de mando, colectivo, ciclico, pedales y tablero. | [Abrir](mandos/manual-mandos-helicoptero.md) |
| 5 | 🧪 Principios y operacion | Fisica del vuelo de ala rotatoria y fases de operacion. | [Abrir](operacion/principios-helicoptero.md) |
| 6 | 🌍 Entornos de trabajo | Helipuertos, rescate, hospitales, incendios forestales. | [Abrir](operacion/entornos-helicoptero.md) |
| 7 | ⚖️ Reglamentos | Ley chilena: Codigo Aeronautico, DGAC, DAN 61, certificacion. | [Abrir](reglamentos/reglamentos-helicoptero.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-helicoptero.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-helicoptero.md) |

---

## 🧩 Requisitos previos

Se recomienda haber revisado antes el curso de aviones pequenos, porque el
helicoptero comparte marco aeronautico y muchos instrumentos de vuelo, pero
agrega la complejidad del vuelo de ala rotatoria: par, anti-par, plato ciclico y
autorrotacion. Marco legal comun en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-helicoptero.md)
