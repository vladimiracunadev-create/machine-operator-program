# 🦅 Curso: Halcón Milenario

[🏠 Inicio](../../README.md) · [🌌 Naves de ficción](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

---

> Curso de análisis educativo de ciencia ficción inspirado en el estilo
> "Star Wars". Estudiamos un carguero rápido genérico para entender la física
> real de la relación empuje/masa, la maniobra en el vacío y por qué el "salto
> al hiperespacio" rompe la física que conocemos hoy.

![Tipo](https://img.shields.io/badge/tipo-ficcion-purple)
![Módulos](https://img.shields.io/badge/modulos-9-blue)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar la relación empuje/masa y por qué decide la aceleración de una nave.
- Entender que un carguero cargado acelera menos que uno vacío, y por qué.
- Describir cómo se maniobra en el vacío con propulsión y propulsores de control.
- Razonar sobre delta-v y el presupuesto de maniobra de un carguero.
- Distinguir por qué un "salto" instantáneo entre estrellas rompe la física real.
- Traducir todo lo anterior a variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Energia[🔋 Fuente de energía] --> Motores[🚀 Motores principales]
    Energia --> RCS[🛰️ Propulsores de control]
    Motores --> Empuje[Empuje frente a masa]
    Carga[📦 Bodega de carga] --> Masa[Masa total variable]
    Masa --> Empuje
    RCS --> Orientacion[Reorientar sin cambiar rumbo]
    Empuje --> Momento[Conservación del momento]
    Piloto[🧑 Piloto] --> Mandos[🎛️ Mandos]
    Mandos --> Motores
    Mandos --> RCS
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Contexto del carguero rápido de ficción y su idea de vuelo. | [Abrir](historia/historia-halcon-milenario.md) |
| 2 | 📋 Características | Que es un carguero rápido genérico y para que sirve. | [Abrir](operacion/caracteristicas-halcon-milenario.md) |
| 3 | 🔧 Sistemas mecánicos | Tecnología imaginaria frente a la física real. | [Abrir](operacion/sistemas-mecanicos-halcon-milenario.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto de mando conceptual y controles. | [Abrir](mandos/manual-mandos-halcon-milenario.md) |
| 5 | 🧪 Principios y operación | Empuje, masa y maniobra: que si, que no y por qué. | [Abrir](operacion/principios-halcon-milenario.md) |
| 6 | 🌍 Entornos | El vacío, órbitas, atmósferas y hangares. | [Abrir](operacion/entornos-halcon-milenario.md) |
| 7 | ⚖️ Reglas del universo | Las leyes internas de la ficción frente a la física. | [Abrir](reglamentos/reglas-universo-halcon-milenario.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modo ciencia o ficción. | [Abrir](simulacion/diseno-simulador-halcon-milenario.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-halcon-milenario.md) |

---

## 🧩 Requisitos previos

Ninguno formal. Ayuda tener nociones básicas de las leyes de Newton, pero el
curso las explica desde cero. La idea central es simple y potente: la
aceleración de un carguero depende de cuanto empuje tienen sus motores frente a
cuanta masa arrastra, y ninguna carga viaja gratis.

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-halcon-milenario.md)
