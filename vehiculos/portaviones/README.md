# 🛳️ Curso: Portaviones

[🏠 Inicio](../../README.md) · [🚙 Catalogo de vehiculos](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso divulgativo e historico.** Documenta el portaviones solo con
> informacion publica: historia, caracteristicas generales, principios fisicos
> de flotacion y estabilidad, cubierta de vuelo y hangar a nivel divulgativo,
> puente educativo, entornos y marco publico. No incluye tactica, doctrina ni
> sistemas de armas. Ver [🦺 docs/04-seguridad-y-limites.md](../../docs/04-seguridad-y-limites.md).

![Nivel](https://img.shields.io/badge/nivel-divulgativo-green)
![Modulos](https://img.shields.io/badge/modulos-9-blue)
![Marco](https://img.shields.io/badge/marco-historico%20publico-lightgrey)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como un buque muy grande flota, avanza y mantiene estabilidad.
- Identificar sus sistemas generales (casco, propulsion, gobierno, cubierta).
- Reconocer, a nivel divulgativo, la cubierta de vuelo y el hangar.
- Comprender la fisica publica de flotacion, estabilidad y logistica de cubierta.
- Conocer el marco institucional e internacional publico aplicable.
- Traducir todo lo anterior en variables de un simulador educativo responsable.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Energia[⛽ Energia] --> Motor[🔧 Planta propulsora]
    Motor --> Eje[Linea de ejes]
    Eje --> Helice[Helices]
    Helice --> Empuje[Empuje]
    Puente[🎛️ Puente / isla] --> Timon[Timon]
    Timon --> Pala[Pala del timon]
    Pala --> Gobierno[Gobierno / rumbo]
    Casco[🚢 Casco] --> Flotacion[Flotacion]
    Cubierta[🛫 Cubierta de vuelo] --> Hangar[Hangar]
    Instrumentos[📊 Navegacion] -. informan .-> Tripulacion[🧍 Tripulacion]
    Tripulacion --> Puente
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolucion publica de la aviacion naval. | [Abrir](historia/historia-portaviones.md) |
| 2 | 📋 Caracteristicas | Que es, tipos historicos y su papel general. | [Abrir](operacion/caracteristicas-portaviones.md) |
| 3 | 🔧 Sistemas mecanicos | Casco, propulsion, gobierno, cubierta y hangar. | [Abrir](operacion/sistemas-mecanicos-portaviones.md) |
| 4 | 🎛️ Mandos e instrumentos | Puente e isla, a nivel educativo. | [Abrir](mandos/manual-mandos-portaviones.md) |
| 5 | 🧪 Principios y operacion | Fisica de flotacion, estabilidad y cubierta. | [Abrir](operacion/principios-portaviones.md) |
| 6 | 🌍 Entornos de trabajo | Puerto, costa, mar abierto y clima. | [Abrir](operacion/entornos-portaviones.md) |
| 7 | ⚖️ Reglamentos | Marco publico institucional e internacional. | [Abrir](reglamentos/reglamentos-portaviones.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo y modos de simulacion. | [Abrir](simulacion/diseno-simulador-portaviones.md) |
| 9 | 🧰 Recursos | Glosario nautico, enlaces y diagramas. | [Abrir](recursos/recursos-portaviones.md) |

---

## 🧩 Requisitos previos

Conviene haber visto antes el curso de
[🚢 Barcos mercantes](../barcos-mercantes/README.md) para dominar flotacion,
inercia y gobierno. El portaviones agrega la escala y la cubierta de vuelo,
siempre desde un enfoque historico y publico. Limites en
[🦺 docs/04-seguridad-y-limites.md](../../docs/04-seguridad-y-limites.md).

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-portaviones.md)
