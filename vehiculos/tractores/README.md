# 🚜 Curso: Tractores

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso completo del tractor agrícola.** Documenta la máquina de principio a
> fin: historia, características, mecánica en profundidad, mandos, física de la
> tracción y la estabilidad, entornos, reglamentos chilenos y diseño de
> simulación. El núcleo del curso es la toma de fuerza, el enganche de tres
> puntos y la estabilidad en pendiente.

![Nivel](https://img.shields.io/badge/nivel-intermedio-yellow)
![Módulos](https://img.shields.io/badge/modulos-11-blue)
![Licencia Chile](https://img.shields.io/badge/licencia-Clase%20D-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberías poder:

- Explicar como un tractor tracciona, tira de aperos y transmite fuerza al campo.
- Identificar sus sistemas mecánicos, la toma de fuerza y el enganche de tres puntos.
- Comprender la hidráulica, el lastre y la estabilidad en pendiente.
- Reconocer todos los mandos e instrumentos y su función.
- Conocer los reglamentos chilenos aplicables (licencia clase D, seguridad).
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Diesel[⛽ Motor diesel] --> Caja[Caja de cambios]
    Caja --> Difer[Diferencial]
    Difer --> Traseras[Ruedas traseras grandes]
    Motor2[🔧 Motor] --> PTO[Toma de fuerza PTO]
    PTO --> Apero[Apero accionado]
    Motor2 --> Bomba[Bomba hidráulica]
    Bomba --> TresPuntos[Enganche de tres puntos]
    TresPuntos --> AperoT[Apero de arrastre o montado]
    Lastre[⚖️ Lastre y contrapeso] --> Estabilidad[Estabilidad]
    Mandos[🎛️ Mandos] --> Caja
    Tablero[📊 Tablero] -. informa .-> Operador[🧍 Operador]
    Operador --> Mandos
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolución del tractor, línea de tiempo. | [Abrir](historia/historia-tractor.md) |
| 2 | 📋 Características | Que es, tipos de tractor y para que sirve cada uno. | [Abrir](operacion/caracteristicas-tractor.md) |
| 3 | 🧩 Modelos y variantes | Que cambia entre modelos: manejo, mando y simulador. | [Abrir](modelos/modelos-tractor.md) |
| 4 | 🔧 Sistemas mecánicos | Motor diesel, PTO, tres puntos, hidráulica, lastre. | [Abrir](operacion/sistemas-mecanicos-tractor.md) |
| 5 | 🎛️ Mandos e instrumentos | Cabina, controles, mandos hidráulicos y tablero. | [Abrir](mandos/manual-mandos-tractor.md) |
| 6 | 🧪 Principios y operación | Tracción, patinaje, estabilidad y fases de trabajo. | [Abrir](operacion/principios-tractor.md) |
| 7 | 🌍 Entornos de trabajo | Campo, pendiente, camino rural y faena. | [Abrir](operacion/entornos-tractor.md) |
| 8 | ⚖️ Reglamentos | Ley chilena: licencia clase D, seguridad agrícola. | [Abrir](reglamentos/reglamentos-tractor.md) |
| 9 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-tractor.md) |
| 10 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-tractor.md) |
| 11 | 🎯 Ejercicios | Autoevaluación con respuestas plegadas. | [Abrir](ejercicios/ejercicios-tractor.md) |

---

## 🧩 Requisitos previos

Se recomienda haber revisado antes el [curso de motos](../motos/README.md) para
los conceptos base de propulsión y transmisión. El tractor agrega la toma de
fuerza, el enganche de tres puntos, la hidráulica de trabajo y una estabilidad
muy sensible a la pendiente y al lastre. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-tractor.md)
