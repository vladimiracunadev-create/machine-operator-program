# ⚓ Curso: Grua portuaria

[🏠 Inicio](../../README.md) · [🚙 Catalogo de vehiculos](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso de izaje portuario.** Documenta la grua portuaria de contenedores de
> principio a fin: historia, caracteristicas, mecanica del portico en
> profundidad, mandos, principios de estabilidad, entornos del terminal,
> seguridad laboral chilena y diseno de simulacion. Es una grua FIJA que carga y
> descarga buques portacontenedores desde el muelle.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Modulos](https://img.shields.io/badge/modulos-9-blue)
![Marco legal](https://img.shields.io/badge/marco-Izaje%20fijo%20Chile-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como una grua portico ship-to-shore descarga contenedores de un buque.
- Identificar sus sistemas mecanicos y como se conectan sobre los rieles del muelle.
- Reconocer todos los mandos e instrumentos de la cabina del operador.
- Comprender los principios de estabilidad, limites de carga y control del balanceo.
- Conocer el marco chileno de izaje fijo y seguridad laboral aplicable.
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Energia[⚡ Energia electrica] --> Portico[🏗️ Portico STS]
    Portico --> Gantry[Traslacion sobre rieles]
    Portico --> Boom[Pluma boom]
    Boom --> Trolley[🚋 Trolley carro]
    Trolley --> Izaje[Cabrestante de izaje]
    Izaje --> Spreader[🔩 Spreader]
    Spreader --> Contenedor[📦 Contenedor ISO]
    Cabina[🎛️ Cabina del operador] -. informa .-> Operador[🧍 Operador]
    Operador --> Cabina
    AntiSway[Anti-sway] -. estabiliza .-> Spreader
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Del izaje manual y de vapor a las gruas STS y la contenedorizacion. | [Abrir](historia/historia-grua-portuaria.md) |
| 2 | 📋 Caracteristicas | Que es, tipos de grua portuaria, contenedor ISO y spreader. | [Abrir](operacion/caracteristicas-grua-portuaria.md) |
| 3 | 🔧 Sistemas mecanicos | Portico, rieles, trolley, spreader, izaje, anti-sway y seguridad. | [Abrir](operacion/sistemas-mecanicos-grua-portuaria.md) |
| 4 | 🎛️ Mandos e instrumentos | Cabina del operador, joysticks e indicadores. | [Abrir](mandos/manual-mandos-grua-portuaria.md) |
| 5 | 🧪 Principios y operacion | Estabilidad, limites de carga y control del balanceo. | [Abrir](operacion/principios-grua-portuaria.md) |
| 6 | 🌍 Entornos de trabajo | Muelle, viento, jornada diurna y nocturna, patio. | [Abrir](operacion/entornos-grua-portuaria.md) |
| 7 | ⚖️ Reglamentos | Marco chileno: izaje fijo, Ley 16.744 y D.S. 594. | [Abrir](reglamentos/reglamentos-grua-portuaria.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo de descarga y modos de juego. | [Abrir](simulacion/diseno-simulador-grua-portuaria.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-grua-portuaria.md) |

---

## 🧩 Requisitos previos

Conviene haber visto antes el curso de gruas moviles, porque comparte conceptos
de izaje, momento de carga y estabilidad. La grua portuaria agrega la operacion
sobre rieles fijos, el manejo del contenedor ISO y el ciclo repetitivo
buque-muelle. Marco legal comun en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-grua-portuaria.md)
