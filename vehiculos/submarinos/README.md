# 🌊 Curso: Submarinos

[🏠 Inicio](../../README.md) · [🚙 Catalogo de vehiculos](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso divulgativo e historico.** Documenta el submarino solo con informacion
> publica: historia, caracteristicas generales, principios fisicos de
> flotabilidad, lastre, presion e inmersion, puesto de control educativo,
> entornos y marco publico. No incluye tactica, doctrina ni sistemas de armas.
> Ver [🦺 docs/04-seguridad-y-limites.md](../../docs/04-seguridad-y-limites.md).

![Nivel](https://img.shields.io/badge/nivel-divulgativo-green)
![Modulos](https://img.shields.io/badge/modulos-9-blue)
![Marco](https://img.shields.io/badge/marco-historico%20publico-lightgrey)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como un submarino flota, se sumerge, avanza y emerge.
- Identificar sus sistemas generales (casco, lastre, propulsion, gobierno).
- Reconocer, a nivel educativo, el puesto de control y sus instrumentos.
- Comprender la fisica publica de flotabilidad, lastre, presion e inmersion.
- Conocer el marco institucional e internacional publico aplicable.
- Traducir todo lo anterior en variables de un simulador educativo responsable.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Energia[⛽ Energia] --> Motor[🔧 Planta propulsora]
    Motor --> Eje[Linea de ejes]
    Eje --> Helice[Helice]
    Helice --> Empuje[Empuje]
    Control[🎛️ Puesto de control] --> Timones[Timones y planos]
    Timones --> Profundidad[Rumbo y profundidad]
    Lastre[🌊 Tanques de lastre] --> Flotabilidad[Flotabilidad]
    Flotabilidad --> Inmersion[Inmersion / emersion]
    Instrumentos[📊 Profundidad y presion] -. informan .-> Tripulacion[🧍 Tripulacion]
    Tripulacion --> Control
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolucion publica del submarino. | [Abrir](historia/historia-submarino.md) |
| 2 | 📋 Caracteristicas | Que es, tipos historicos y su papel general. | [Abrir](operacion/caracteristicas-submarino.md) |
| 3 | 🔧 Sistemas mecanicos | Casco, lastre, inmersion, presion, propulsion y gobierno. | [Abrir](operacion/sistemas-mecanicos-submarino.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto de control, a nivel educativo. | [Abrir](mandos/manual-mandos-submarino.md) |
| 5 | 🧪 Principios y operacion | Fisica de flotabilidad, lastre, presion e inmersion. | [Abrir](operacion/principios-submarino.md) |
| 6 | 🌍 Entornos de trabajo | Superficie, cota, profundidad y clima. | [Abrir](operacion/entornos-submarino.md) |
| 7 | ⚖️ Reglamentos | Marco publico institucional e internacional. | [Abrir](reglamentos/reglamentos-submarino.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo y modos de simulacion. | [Abrir](simulacion/diseno-simulador-submarino.md) |
| 9 | 🧰 Recursos | Glosario nautico, enlaces y diagramas. | [Abrir](recursos/recursos-submarino.md) |

---

## 🧩 Requisitos previos

Conviene haber visto antes el curso de
[🚢 Barcos mercantes](../barcos-mercantes/README.md) para dominar flotacion,
inercia y gobierno. El submarino agrega la flotabilidad variable, el lastre y la
presion, siempre desde un enfoque historico y publico. Limites en
[🦺 docs/04-seguridad-y-limites.md](../../docs/04-seguridad-y-limites.md).

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-submarino.md)
