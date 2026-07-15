# 🧰 Recursos del acorazado

[🏠 Inicio](../../../README.md) · [🛡️ Curso: Acorazados](../README.md) · 🧰 Recursos

Glosario náutico específico, enlaces y diagramas de apoyo del curso de
acorazados. Solo material público e histórico. Amplia el
[glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Desplazamiento | Peso del agua que desplaza el buque; su peso total. |
| Blindaje | Acero de protección del casco (tratado como masa estructural). |
| Compartimentación | División del casco en zonas estancas por mamparos. |
| Escora | Inclinación transversal del buque. |
| Contrainundación | Igualar peso entre costados para corregir escora. |
| Metacentro | Punto de referencia de la estabilidad transversal. |
| Calado | Profundidad sumergida del casco. |
| Nudo | Unidad de velocidad: una milla náutica por hora. |
| Babor / estribor | Costado izquierdo / derecho mirando a proa. |

---

## 🗺️ Diagrama de estabilidad con blindaje

```mermaid
flowchart LR
    Blindaje[Peso del blindaje] --> G[Sube centro de gravedad]
    Lastre[Lastre en el fondo] --> Baja[Baja centro de gravedad]
    G --> Equilibrio[Equilibrio de estabilidad]
    Baja --> Equilibrio
    Equilibrio --> Estable[Buque estable]
```

---

## 🔗 Enlaces y fuentes

- Seguridad y límites: [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md)
- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Buques museo y fuentes históricas públicas: ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-acorazado.md)
