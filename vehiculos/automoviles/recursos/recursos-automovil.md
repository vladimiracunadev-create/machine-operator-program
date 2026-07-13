# 🧰 Recursos del automovil

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automoviles](../README.md) · 🧰 Recursos

Glosario especifico, enlaces y diagramas de apoyo del curso de automoviles.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Traccion | Ruedas que reciben la fuerza del motor: delantera, trasera o integral. |
| Diferencial | Mecanismo que permite a las ruedas de un eje girar a distinta velocidad. |
| Subviraje | El auto no gira lo suficiente porque el eje delantero pierde agarre. |
| Sobreviraje | La parte trasera se abre y el auto gira mas de lo deseado. |
| Transferencia de peso | Desplazamiento de la carga entre ruedas al frenar, acelerar o girar. |
| ABS | Sistema que evita el bloqueo de las ruedas al frenar fuerte. |
| ESC | Control de estabilidad que corrige derrapes con frenado selectivo. |
| Cilindrada | Volumen total de los cilindros del motor, en litros o cc. |
| Aquaplaning | Perdida de contacto del neumatico por una capa de agua. |

---

## 🗺️ Diagrama de flujo de la fuerza

```mermaid
flowchart LR
    Motor[Motor] --> Trans[Transmision]
    Trans --> Dif[Diferencial]
    Dif --> Ruedas[Ruedas motrices]
    Ruedas --> Suelo[Adherencia con el suelo]
    Suelo --> Movimiento[Movimiento controlado]
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Manuales oficiales del conductor (CONASET): ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-automovil.md)
