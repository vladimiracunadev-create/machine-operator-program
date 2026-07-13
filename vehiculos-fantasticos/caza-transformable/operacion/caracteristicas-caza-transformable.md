# 📋 Caracteristicas del caza transformable

[🏠 Inicio](../../../README.md) · [🤖 Curso: Caza transformable](../README.md) · 📋 Caracteristicas

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Este modulo describe que es un caza transformable y presenta sus tres modos. La
idea clave es que una misma maquina adopta formas muy distintas segun lo que
necesite: cruzar el cielo a gran velocidad o moverse y manipular objetos en el
suelo.

```mermaid
flowchart LR
    Caza[✈️ Modo caza] -->|transicion| Intermedio[🔀 Modo intermedio]
    Intermedio -->|transicion| Humanoide[🤖 Modo humanoide]
    Humanoide -->|transicion| Intermedio
    Intermedio -->|transicion| Caza
    Caza -.->|prioriza velocidad| Vel[🌬️ Aerodinamica]
    Humanoide -.->|prioriza destreza| Des[🖐️ Manipulacion]
    Intermedio -.->|compromiso| Mix[⚖️ Equilibrio]
```

---

## Los tres modos

### ✈️ Modo caza

Perfil de avion: fuselaje alargado, alas y superficies de control. Todo se
esconde o se alinea para reducir la resistencia del aire. Es el modo optimo para
volar rapido y lejos.

### 🔀 Modo intermedio

Una forma de transicion, a medio camino. Ya asoman brazos o tren de aterrizaje,
pero conserva parte del perfil aerodinamico. Sirve para maniobras especiales y
como paso obligado entre los otros dos modos.

### 🤖 Modo humanoide

Cuerpo con torso, brazos y piernas. Gana destreza y capacidad de manipular, pero
pierde casi toda la eficiencia aerodinamica. Es el modo optimo para operar en el
suelo o en contacto con estructuras.

---

## Comparacion de los modos

| Aspecto | ✈️ Caza | 🔀 Intermedio | 🤖 Humanoide |
| --- | --- | --- | --- |
| Prioridad | Velocidad | Compromiso | Destreza |
| Resistencia al aire | Baja | Media | Muy alta |
| Superficie frontal | Pequena | Media | Grande |
| Manipulacion | Nula | Limitada | Alta |
| Estabilidad en vuelo | Alta | Media | Muy baja |
| Uso ideal | Cruzar el cielo | Transicion y maniobra | Suelo y contacto |

---

## Para que sirve cada modo

- **Caza**: desplazarse rapido, recorrer grandes distancias, patrullar.
- **Intermedio**: ajustar la trayectoria, frenar, prepararse para el contacto.
- **Humanoide**: caminar, sujetar, empujar, interactuar con el entorno.

La gracia del concepto es no tener que elegir de forma permanente: la maquina se
adapta a cada situacion. El costo de esa flexibilidad, como veremos en el modulo
de sistemas, es enorme en peso, mecanismos y estructura.

---

[⬅️ Anterior: Historia](../historia/historia-caza-transformable.md) · [➡️ Siguiente: Sistemas mecanicos](sistemas-mecanicos-caza-transformable.md)
