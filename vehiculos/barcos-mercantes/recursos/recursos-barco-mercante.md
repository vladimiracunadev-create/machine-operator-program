# 🧰 Recursos del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🧰 Recursos

Glosario nautico especifico, enlaces y diagramas de apoyo del curso de barcos
mercantes. Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Calado | Profundidad sumergida del casco desde la linea de flotacion. |
| Francobordo | Altura del casco desde la flotacion hasta la cubierta. |
| Escora | Inclinacion transversal del buque. |
| Asiento (trimado) | Diferencia de calado entre proa y popa. |
| Lastre | Agua que se toma o descarga para ajustar peso y estabilidad. |
| Metacentro | Punto de referencia de la estabilidad transversal. |
| Estiba | Distribucion de la carga a bordo. |
| Nudo | Unidad de velocidad: una milla nautica por hora. |
| Babor / estribor | Costado izquierdo / derecho mirando a proa. |

---

## 🗺️ Diagrama de flotacion y estabilidad

```mermaid
flowchart LR
    Peso[Peso del buque] --> Desplaza[Desplaza agua]
    Desplaza --> Empuje[Empuje de Arquimedes]
    Empuje --> Flota[El buque flota]
    Carga[Carga y lastre] --> G[Centro de gravedad]
    G --> Estable[G bajo M: estable]
    G --> Riesgo[G sobre M: riesgo de vuelco]
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Convenios OMI (SOLAS, MARPOL, STCW, COLREG) y DIRECTEMAR: ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-barco-mercante.md)
