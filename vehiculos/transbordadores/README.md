# 🛬 Curso: Transbordadores

[🏠 Inicio](../../README.md) · [🚙 Catalogo de vehiculos](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso del vehiculo espacial reutilizable con reentrada alada.** Documenta el
> transbordador de principio a fin: historia, caracteristicas, sistemas
> (orbitador, propulsores, tanque externo, escudo termico), cabina y mandos,
> fisica del planeo sin motor en la reentrada, entornos del vuelo, marco legal
> internacional y diseno de simulacion. Enfoque **historico y de principios**.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Modulos](https://img.shields.io/badge/modulos-9-blue)
![Marco](https://img.shields.io/badge/marco-tratados%20espaciales-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como despega, orbita y reingresa un transbordador reutilizable.
- Identificar el orbitador, los propulsores, el tanque externo y el escudo termico.
- Comprender por que la reentrada es un planeo sin motor y como se controla.
- Reconocer los mandos e instrumentos de la cabina del orbitador.
- Entender el papel del escudo termico frente al calor de la reentrada.
- Conocer el marco de tratados espaciales que aplica a la actividad espacial.
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Tanque[⛽ Tanque externo] --> Motores[🔧 Motores del orbitador]
    Propulsores[Propulsores laterales] --> Empuje[Empuje de despegue]
    Motores --> Empuje
    Empuje --> Orbita[🛰️ Orbita]
    Orbita --> Desorbita[Frenado con motor]
    Desorbita --> Reentrada[Reentrada con escudo]
    Reentrada --> Planeo[🛬 Planeo sin motor]
    Planeo --> Pista[Aterrizaje en pista]
    Cabina[🎛️ Cabina] --> Control[Control de vuelo]
    Control --> Orbita
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolucion del transbordador, linea de tiempo. | [Abrir](historia/historia-transbordador.md) |
| 2 | 📋 Caracteristicas | Que es, sus partes y para que sirve. | [Abrir](operacion/caracteristicas-transbordador.md) |
| 3 | 🔧 Sistemas mecanicos | Orbitador, propulsores, tanque externo, escudo termico. | [Abrir](operacion/sistemas-mecanicos-transbordador.md) |
| 4 | 🎛️ Mandos e instrumentos | Cabina del orbitador, controles y paneles. | [Abrir](mandos/manual-mandos-transbordador.md) |
| 5 | 🧪 Principios y operacion | Reentrada, planeo sin motor y fases de la mision. | [Abrir](operacion/principios-transbordador.md) |
| 6 | 🌍 Entornos de trabajo | Plataforma, ascenso, orbita y reentrada alada. | [Abrir](operacion/entornos-transbordador.md) |
| 7 | ⚖️ Reglamentos | Estado de lanzamiento y tratados espaciales. | [Abrir](reglamentos/reglamentos-transbordador.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-transbordador.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-transbordador.md) |

---

## 🧩 Requisitos previos

Se recomienda revisar antes el curso de [🚀 cohetes](../cohetes/README.md), que
explica el despegue y el ascenso, y el de
[🚀 naves espaciales](../naves-espaciales/README.md), que introduce la orbita. El
transbordador combina un despegue de cohete con un aterrizaje de avion. Marco
legal comun en [⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-transbordador.md)
