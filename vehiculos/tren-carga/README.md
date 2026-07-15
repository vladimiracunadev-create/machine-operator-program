# 🚂 Curso: Tren de carga

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso del tren de carga.** Documenta el ferrocarril de mercancías de
> principio a fin: historia, características, mecánica en profundidad, mandos,
> principios de gran masa, entornos, marco ferroviario chileno y diseño de
> simulación. Sigue el mismo molde que el curso de motos.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Módulos](https://img.shields.io/badge/modulos-10-blue)
![Marco legal](https://img.shields.io/badge/marco-Ferroviario%20Chile-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberías poder:

- Explicar como un tren de carga arranca, mantiene velocidad y frena gran masa.
- Identificar sus sistemas mecánicos y cómo se conectan.
- Reconocer los mandos del puesto del maquinista y su función.
- Comprender los principios de inercia, adherencia rueda-riel y frenado largo.
- Conocer el marco ferroviario chileno (EFE, MTT, habilitación del maquinista).
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Diesel[⛽ Motor diesel] --> Generador[Generador / alternador]
    Generador --> Motores[Motores de tracción]
    Catenaria[⚡ Catenaria] -. traccion electrica .-> Motores
    Motores --> Bogies[Bogies]
    Bogies --> Ruedas[Ruedas de pestaña]
    Ruedas --> Riel[Riel]
    Puesto[🎛️ Puesto del maquinista] --> Traccion[Manipulador de tracción]
    Puesto --> Freno[Freno automático de tren]
    Traccion --> Motores
    Freno --> Tuberia[Tubería de freno]
    Tuberia --> Vagones[Vagones]
    Locomotora[🚂 Locomotora lider] --> Vagones
    Tablero[📊 Indicadores] -. informa .-> Maquinista[🧍 Maquinista]
    Maquinista --> Puesto
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Del vapor al diesel-eléctrico y trenes de mercancías modernos. | [Abrir](historia/historia-tren-carga.md) |
| 2 | 📋 Características | Que es, tipos de vagón y trenes unitarios o mixtos. | [Abrir](operacion/caracteristicas-tren-carga.md) |
| 3 | 🔧 Sistemas mecánicos | Tracción, bogies, adherencia, frenado, composición y enganches. | [Abrir](operacion/sistemas-mecanicos-tren-carga.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto del maquinista, controles e indicadores. | [Abrir](mandos/manual-mandos-tren-carga.md) |
| 5 | 🧪 Principios y operación | Inercia, adherencia y fuerzas longitudinales del tren. | [Abrir](operacion/principios-tren-carga.md) |
| 6 | 🌍 Entornos de trabajo | Corredores, patios, terminales intermodales y ramales. | [Abrir](operacion/entornos-tren-carga.md) |
| 7 | ⚖️ Reglamentos | Marco ferroviario chileno: EFE, MTT y habilitación. | [Abrir](reglamentos/reglamentos-tren-carga.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-tren-carga.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-tren-carga.md) |
| 10 | 🎯 Ejercicios | Autoevaluación con respuestas plegadas. | [Abrir](ejercicios/ejercicios-tren-carga.md) |

---

## 🧩 Requisitos previos

Se recomienda haber visto antes el curso de motos y el de camiones, porque el
tren de carga lleva al extremo la gestión de masa: gran inercia, adherencia
limitada y distancias de frenado muy largas. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-tren-carga.md)
