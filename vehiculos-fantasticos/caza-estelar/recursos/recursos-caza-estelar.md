# 🧰 Recursos del caza estelar

[🏠 Inicio](../../../README.md) · [🛸 Curso: Caza estelar](../README.md) · 🧰 Recursos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Glosario especifico, enlaces y diagramas de apoyo del curso de caza estelar.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Vacio | Espacio sin aire; sin rozamiento ni sonido ni sustentacion. |
| Inercia | Tendencia de un objeto a mantener su velocidad si no hay fuerzas. |
| Momento | Producto de masa por velocidad; se conserva sin fuerzas externas. |
| Delta-v | Cambio total de velocidad que la nave puede lograr con su propelente. |
| Propelente | Masa que el motor expulsa para generar empuje por reaccion. |
| Empuje | Fuerza que impulsa la nave, resultado de expulsar masa. |
| RCS | Propulsores de control de reaccion para rotar o trasladar la nave. |
| Orientacion | Hacia donde apunta la nave, distinta de hacia donde se mueve. |
| Viraje bancado | Giro inclinado tipico de un avion; imposible sin aire. |
| Reentrada | Entrada a una atmosfera, donde aparecen aire, calor y rozamiento. |

---

## 🗺️ Diagrama: apuntar frente a moverse

```mermaid
flowchart LR
    Motor[Encender motor] --> Rumbo[Cambia hacia donde se mueve]
    RCS[Usar RCS] --> Apunta[Cambia hacia donde apunta]
    Apunta --> Momento[El rumbo se conserva]
    Rumbo --> Nuevo[Nuevo vector de velocidad]
    Momento --> Idea[Apuntar no es moverse]
```

---

## 🔗 Enlaces y fuentes

- Portada del curso: [🛸 Curso: Caza estelar](../README.md)
- Catalogo de naves de ficcion: [🌌 Naves de ficcion](../../README.md)
- Glosario general: [📖 docs/05-glosario-general.md](../../../docs/05-glosario-general.md)
- Niveles de realismo: [🎚️ docs/03-niveles-de-realismo.md](../../../docs/03-niveles-de-realismo.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, respetando el aviso de
derechos del catalogo de naves de ficcion.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-caza-estelar.md)
