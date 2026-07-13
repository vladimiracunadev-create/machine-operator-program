# 📋 Caracteristicas funcionales del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 📋 Caracteristicas

Que es un tren de carga, que tipos de vagon existen y para que sirve cada
composicion. Este modulo da el contexto antes de abrir la mecanica (Modulo 3).

---

## 🧭 Definicion

Un tren de carga es una composicion formada por una o varias locomotoras que
arrastran un conjunto de vagones para mover gran tonelaje de mercancias sobre una
via de ferrocarril. La adherencia rueda-riel es baja, por lo que el tren depende
de gran fuerza de traccion para arrancar y de largas distancias para frenar.

---

## 🧬 Caracteristicas clave

| Caracteristica | Descripcion |
| --- | --- |
| Gran masa | Miles de toneladas entre locomotoras y vagones cargados. |
| Ruta fija | Circula solo sobre la via; no elige trayectoria libre. |
| Adherencia limitada | El contacto acero-acero da poco agarre; se usa arenado. |
| Frenado largo | La distancia de detencion es muy superior a la de un camion. |
| Composicion modular | Se agregan o quitan vagones segun la carga. |
| Fuerzas longitudinales | Aparecen estirones y compresiones entre vagones. |

---

## 🗂️ Tipos de vagon y composicion

```mermaid
flowchart TD
    Tren[🚂 Tren de carga] --> Locomotoras[Locomotoras]
    Tren --> Vagones[Vagones]
    Locomotoras --> Lider[Lider]
    Locomotoras --> Remotas[Remotas / distributed power]
    Vagones --> Tolva[Tolva]
    Vagones --> Plataforma[Plataforma para contenedores]
    Vagones --> Cisterna[Cisterna]
    Vagones --> Cerrado[Cerrado]
    Vagones --> Gondola[Gondola]
```

| Tipo de vagon | Uso tipico | Rasgo destacado |
| --- | --- | --- |
| Tolva | Mineral, grano, arido | Descarga por el fondo. |
| Plataforma | Contenedores intermodales | Base plana para carga apilada. |
| Cisterna | Liquidos y graneles | Cuerpo sellado y valvulas. |
| Cerrado | Carga que teme la intemperie | Caja techada y con puertas. |
| Gondola | Carga a granel abierta | Caja abierta sin techo. |

- **Tren unitario**: todos los vagones llevan el mismo producto punto a punto.
- **Tren mixto**: combina vagones de distinto tipo y varias mercancias.

---

## 🎯 Para que se usa

- Transporte masivo de mineral, grano y aridos.
- Movimiento intermodal de contenedores entre puerto y terminal.
- Transporte de liquidos y graneles en cisterna.
- Carga forestal e industrial en ramales.
- Corredores de larga distancia con gran tonelaje.

---

[⬅️ Anterior: Historia](../historia/historia-tren-carga.md) · [➡️ Siguiente: Sistemas mecanicos](sistemas-mecanicos-tren-carga.md)
