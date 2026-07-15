# ✈️ Curso: Aviones de combate

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso de marco público e histórico.** Documenta el avión de combate solo
> desde la física del vuelo, la historia pública y los principios generales de
> una aeronave a reacción. **No** incluye sistemas de armas, táctica, doctrina ni
> procedimientos operativos sensibles. Ver
> [🦺 docs/04-seguridad-y-limites.md](../../docs/04-seguridad-y-limites.md).

![Nivel](https://img.shields.io/badge/nivel-divulgativo-green)
![Módulos](https://img.shields.io/badge/modulos-9-blue)
![Marco](https://img.shields.io/badge/marco-publico%20e%20historico-lightgrey)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar cómo vuela un avión a reacción: sustentación, empuje y control.
- Conocer la historia pública de la aviación militar y su evolución técnica.
- Identificar la célula, las alas y las superficies de control de un reactor.
- Comprender los principios físicos del vuelo a alta velocidad, a nivel divulgativo.
- Distinguir el marco institucional civil del militar en Chile.
- Traducir la física del vuelo en variables de un simulador educativo.

---

## 🛡️ Alcance y límites

Este curso se mantiene en el **marco público y divulgativo**. Solo trata física
del vuelo, historia y principios generales. Quedan **fuera** los sistemas de
armas, la táctica, la doctrina y los procedimientos operativos sensibles, según
[🦺 docs/04-seguridad-y-limites.md](../../docs/04-seguridad-y-limites.md).

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Combustible[⛽ Combustible] --> Reactor[🔧 Motor a reacción]
    Reactor --> Empuje[Empuje]
    Alas[✈️ Alas] --> Sustentacion[Sustentación]
    Palanca[🎛️ Palanca] --> Alerones[Alerones]
    Palanca --> Profundidad[Timón de profundidad]
    Pedales[Pedales] --> Direccion[Timón de dirección]
    Alerones --> Alabeo[Alabeo]
    Profundidad --> Cabeceo[Cabeceo]
    Direccion --> Guinada[Guiñada]
    Tablero[📊 Instrumentos] -. informa .-> Piloto[🧍 Piloto]
    Piloto --> Palanca
    Piloto --> Pedales
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Historia pública de la aviación militar, línea de tiempo. | [Abrir](historia/historia-avion-combate.md) |
| 2 | 📋 Características | Que es, generaciones y roles generales de la aeronave. | [Abrir](operacion/caracteristicas-avion-combate.md) |
| 3 | 🔧 Sistemas mecánicos | Célula, alas, superficies de control y motor a reacción. | [Abrir](operacion/sistemas-mecanicos-avion-combate.md) |
| 4 | 🎛️ Mandos e instrumentos | Cabina, controles de vuelo y panel de instrumentos. | [Abrir](mandos/manual-mandos-avion-combate.md) |
| 5 | 🧪 Principios y operación | Física del vuelo a reacción y fases generales. | [Abrir](operacion/principios-avion-combate.md) |
| 6 | 🌍 Entornos de trabajo | Base aérea, espacio aéreo y meteorología. | [Abrir](operacion/entornos-avion-combate.md) |
| 7 | ⚖️ Reglamentos | Marco institucional público (FACH, defensa). | [Abrir](reglamentos/reglamentos-avion-combate.md) |
| 8 | 🎮 Diseño de simulación | Variables de vuelo, ciclo y modos educativos. | [Abrir](simulacion/diseno-simulador-avion-combate.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-avion-combate.md) |

---

## 🧩 Requisitos previos

Se recomienda haber revisado antes el curso de
[🛩️ aviones pequeños](../aviones-pequenos/README.md), que introduce la física del
vuelo con menor velocidad y complejidad. Este curso extiende esos principios al
vuelo a reacción desde un enfoque solo divulgativo. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-avion-combate.md)
