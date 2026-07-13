# 🧰 Recursos de la grua portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grua portuaria](../README.md) · 🧰 Recursos

Glosario especifico, enlaces y diagramas de apoyo del curso de grua portuaria.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Ship-to-shore STS | Grua portico que descarga contenedores del buque al muelle. |
| Portico | Estructura de acero en forma de marco que se apoya sobre los rieles. |
| Boom | Pluma abatible del portico que se proyecta sobre el buque. |
| Trolley | Carro que corre por la viga llevando el spreader y la cabina. |
| Spreader | Marco telescopico con twist-locks que engancha el contenedor. |
| Twist-lock | Perno giratorio que traba el contenedor por sus esquinas ISO. |
| Gantry | Traslacion de todo el portico a lo largo del muelle sobre rieles. |
| Hoist | Cabrestante de izaje que sube y baja el spreader. |
| Anti-sway | Sistema que reduce el balanceo de la carga colgada. |
| TEU | Contenedor de 20 pies; unidad de medida del trafico. |
| FEU | Contenedor de 40 pies; equivale a 2 TEU. |

---

## 🗺️ Diagrama del ciclo de descarga

```mermaid
flowchart LR
    Posicion[Posicionar gantry y trolley] --> Enganche[Bajar spreader y trabar]
    Enganche --> Izaje[Izar con anti-sway]
    Izaje --> Traslado[Trasladar al muelle]
    Traslado --> Deposito[Bajar y liberar]
    Deposito --> Repite[Repetir ciclo]
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Manuales de operacion y normas de izaje portuario: ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-grua-portuaria.md)
