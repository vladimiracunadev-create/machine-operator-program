# 🧰 Recursos del helicoptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicopteros](../README.md) · 🧰 Recursos

Glosario especifico, enlaces y diagramas de apoyo del curso de helicopteros.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Rotor principal | Conjunto de palas que genera la sustentacion y la traccion. |
| Rotor de cola | Rotor pequeno que compensa el par y controla la guinada. |
| Plato ciclico | Pieza que transmite los mandos a las palas mientras giran. |
| Paso colectivo | Cambio por igual del paso de todas las palas del rotor. |
| Paso ciclico | Cambio del paso pala a pala que inclina el disco rotor. |
| Anti-par | Fuerza que compensa el par del rotor sobre el fuselaje. |
| Autorrotacion | Descenso seguro sin motor usando el flujo de aire por el rotor. |
| Efecto suelo | Aumento de sustentacion al volar cerca del terreno. |
| Disimetria de sustentacion | Diferencia de sustentacion entre la pala que avanza y la que retrocede. |

---

## 🗺️ Diagrama de equilibrio del vuelo estacionario

```mermaid
flowchart LR
    Colectivo[Colectivo] --> Sust[Sustentacion iguala el peso]
    Sust --> Par[Aparece el par del rotor]
    Par --> Pedal[Pedal compensa con anti-par]
    Ciclico[Ciclico] --> Fijo[Mantiene el punto sin derivar]
    Pedal --> Hover[Vuelo estacionario estable]
    Fijo --> Hover
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Autoridad aeronautica (DGAC): ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-helicoptero.md)
