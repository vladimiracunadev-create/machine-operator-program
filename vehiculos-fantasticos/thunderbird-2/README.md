# 📦 Curso: Thunderbird 2

[🏠 Inicio](../../README.md) · [🌌 Naves de ficción](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

---

> Curso de análisis educativo de ciencia ficción inspirado en el estilo
> "Thunderbirds". Estudiamos un transporte pesado modular genérico para
> entender la física real de llevar carga: cuanta masa útil puede mover un
> vehículo, por  qué los módulos intercambiables son tan potentes y que precio
> paga la estructura por sostener tanto peso.

![Tipo](https://img.shields.io/badge/tipo-ficcion-purple)
![Módulos](https://img.shields.io/badge/modulos-9-blue)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar la fracción de carga útil: cuanta masa aprovechable lleva un vehículo.
- Entender la ventaja de los módulos intercambiables frente a un vehículo fijo.
- Describir como el reparto de peso mueve el centro de masa y afecta la estabilidad.
- Razonar sobre la relación empuje-peso en un vehículo de carga pesada.
- Distinguir el compromiso entre estructura resistente y carga aprovechable.
- Traducir todo lo anterior a variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Energia[🔋 Fuente de energía] --> Propulsion[🚀 Propulsión de carga pesada]
    Estructura[🏗️ Bastidor portante] --> Anclaje[🔗 Anclaje de módulos]
    Anclaje --> Modulo[📦 Módulo intercambiable]
    Propulsion --> Empuje[Empuje frente al peso total]
    Modulo --> Peso[Suma masa útil al conjunto]
    Peso --> Centro[Desplaza el centro de masa]
    Piloto[🧑 Piloto] --> Mandos[🎛️ Mandos]
    Mandos --> Propulsion
    Mandos --> Anclaje
    Sensores[📡 Sensores de carga] -. informan .-> Piloto
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Contexto de la nave de ficción y su idea de carga. | [Abrir](historia/historia-thunderbird-2.md) |
| 2 | 📋 Características | Que es un transporte pesado modular y para que sirve. | [Abrir](operacion/caracteristicas-thunderbird-2.md) |
| 3 | 🔧 Sistemas mecánicos | Tecnología imaginaria frente a la física real. | [Abrir](operacion/sistemas-mecanicos-thunderbird-2.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto de mando conceptual y controles. | [Abrir](mandos/manual-mandos-thunderbird-2.md) |
| 5 | 🧪 Principios y operación | Carga útil, empuje y estabilidad: que si y que no. | [Abrir](operacion/principios-thunderbird-2.md) |
| 6 | 🌍 Entornos | Bases, rutas y zonas de descarga. | [Abrir](operacion/entornos-thunderbird-2.md) |
| 7 | ⚖️ Reglas del universo | Las leyes internas de la ficción frente a la física. | [Abrir](reglamentos/reglas-universo-thunderbird-2.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modo ciencia o ficción. | [Abrir](simulacion/diseno-simulador-thunderbird-2.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-thunderbird-2.md) |

---

## 🧩 Requisitos previos

Ninguno formal. Ayuda tener nociones básicas de peso, masa y equilibrio, pero
el curso las explica desde cero. La idea central es simple y potente: llevar
carga siempre es un compromiso entre cuanto peso útil cargas y cuanta
estructura y energía necesitas para sostenerlo y moverlo.

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-thunderbird-2.md)
