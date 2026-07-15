# 🛗 Curso: Ascensores

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso de transporte vertical fijo.** Documenta el ascensor de principio a
> fin: historia, características, mecánica en profundidad, control de llamadas,
> física del transporte vertical, entornos, marco legal chileno (Ley 20.296) y
> diseño de simulación. Es maquinaria fija: no circula por vía pública y su
> núcleo normativo es la mantención e inspección.

![Nivel](https://img.shields.io/badge/nivel-introductorio-green)
![Módulos](https://img.shields.io/badge/modulos-9-blue)
![Marco](https://img.shields.io/badge/marco-Ley%2020.296-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como una cabina sube y baja de forma controlada y segura.
- Identificar cabina, contrapeso, cables, poleas, motor, guías y frenos.
- Reconocer la botonera, el control de llamadas y los indicadores.
- Comprender la física del transporte vertical: equilibrio con contrapeso.
- Conocer el marco legal chileno (Ley 20.296, OGUC) de mantención e inspección.
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Motor[🔧 Motor y reductor] --> Polea[Polea de tracción]
    Polea --> Cable[Cables de tracción]
    Cable --> Cabina[🛗 Cabina]
    Cable --> Contrapeso[Contrapeso]
    Guias[Guías verticales] --> Cabina
    Guias --> Contrapeso
    Gobernador[Gobernador de velocidad] --> Paracaidas[Freno de seguridad]
    Paracaidas --> Cabina
    Botonera[🎛️ Botonera y llamadas] --> Control[Controlador]
    Control --> Motor
    Control -. informa .-> Usuario[🧍 Usuario]
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolución del ascensor, línea de tiempo. | [Abrir](historia/historia-ascensor.md) |
| 2 | 📋 Características | Que es, tipos de ascensor y para que sirve cada uno. | [Abrir](operacion/caracteristicas-ascensor.md) |
| 3 | 🔧 Sistemas mecánicos | Cabina, contrapeso, cables, motor, guías y frenos. | [Abrir](operacion/sistemas-mecanicos-ascensor.md) |
| 4 | 🎛️ Mandos e instrumentos | Botonera, control de llamadas e indicadores. | [Abrir](mandos/manual-mandos-ascensor.md) |
| 5 | 🧪 Principios y operación | Física del transporte vertical y fases de un viaje. | [Abrir](operacion/principios-ascensor.md) |
| 6 | 🌍 Entornos de trabajo | Edificios residenciales, oficinas, hospitales. | [Abrir](operacion/entornos-ascensor.md) |
| 7 | ⚖️ Reglamentos | Ley 20.296 y OGUC: mantención, inspección, certificación. | [Abrir](reglamentos/reglamentos-ascensor.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-ascensor.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-ascensor.md) |

---

## 🧩 Requisitos previos

Ninguno. El ascensor es un buen punto de entrada al transporte vertical: permite
explicar equilibrio con contrapeso, tracción por cable y frenos de seguridad con
menor complejidad que una grúa. Comparte ideas con la
[🗼 grúa torre](../grua-torre/README.md) en cables y poleas. Marco legal en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md), sección
1.8 (ascensores).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-ascensor.md)
