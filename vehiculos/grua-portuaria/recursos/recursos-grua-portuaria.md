# 🧰 Recursos de la grúa portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de grúa portuaria.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Ship-to-shore STS | Grúa pórtico que descarga contenedores del buque al muelle. |
| Pórtico | Estructura de acero en forma de marco que se apoya sobre los rieles. |
| Boom | Pluma abatible del pórtico que se proyecta sobre el buque. |
| Trolley | Carro que corre por la viga llevando el spreader y la cabina. |
| Spreader | Marco telescópico con twist-locks que engancha el contenedor. |
| Twist-lock | Perno giratorio que traba el contenedor por sus esquinas ISO. |
| Gantry | Traslación de todo el pórtico a lo largo del muelle sobre rieles. |
| Hoist | Cabrestante de izaje que sube y baja el spreader. |
| Anti-sway | Sistema que reduce el balanceo de la carga colgada. |
| TEU | Contenedor de 20 pies; unidad de medida del tráfico. |
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
- Manuales de operación y normas de izaje portuario: ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-grua-portuaria.md)
