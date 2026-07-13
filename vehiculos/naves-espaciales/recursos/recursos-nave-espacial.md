# 🧰 Recursos de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🧰 Recursos

Glosario especifico, enlaces y diagramas de apoyo del curso de naves espaciales.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Orbita | Trayectoria de caida libre continua alrededor de un cuerpo. |
| Delta-v | Cambio total de velocidad que una nave puede lograr; mide su capacidad de maniobra. |
| Microgravedad | Estado de caida libre en que los objetos parecen flotar. |
| Propelente | Masa que la nave expulsa para propulsarse. |
| Oxidante | Sustancia que aporta oxigeno para quemar sin aire externo. |
| RCS | Sistema de propulsores pequenos para orientar y trasladar la nave. |
| Reentrada | Regreso a la atmosfera, con calor por friccion. |
| Escudo termico | Proteccion que soporta el calor de la reentrada. |
| Apogeo y perigeo | Puntos mas alto y mas bajo de una orbita. |

---

## 🗺️ Diagrama de una maniobra orbital

```mermaid
flowchart LR
    Orbita[Orbita inicial] --> Motor[Encender motor]
    Motor --> DeltaV[Gastar delta-v]
    DeltaV --> Nueva[Nueva orbita]
    Nueva --> Reserva[Guardar reserva para volver]
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Seguridad y limites: [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md). Distinguir siempre fuentes de
ciencia real de material de ficcion.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-nave-espacial.md)
