# 🧰 Recursos del tanque (marco público)

[🏠 Inicio](../../../README.md) · [🪖 Curso: Tanques](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de tanques, **solo
de movilidad e historia pública**. Amplia el
[glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Tren de rodaje | Conjunto de ruedas y cadena que permite avanzar sobre orugas. |
| Oruga | Cadena continua que reparte el peso y da agarre en terreno difícil. |
| Rueda motriz | Rueda dentada que engrana y mueve la cadena. |
| Rueda tensora | Mantiene la tensión correcta de la oruga. |
| Dirección diferencial | Giro logrado variando la velocidad de cada oruga. |
| Presión sobre el suelo | Peso repartido por la superficie de las orugas. |
| Relación potencia/peso | Potencia del motor frente a la masa del vehículo. |
| Barra de torsión | Elemento de suspensión que se retuerce como resorte. |

---

## 🗺️ Diagrama de movilidad

```mermaid
flowchart LR
    Motor[Motor] --> Trans[Transmisión]
    Trans --> Motriz[Rueda motriz]
    Motriz --> Oruga[Cadena de oruga]
    Oruga --> Presion[Reparto de presión]
    Presion --> Avance[Avance todo terreno]
    Susp[Suspensión] --> Oruga
```

---

## 🔗 Enlaces y fuentes

- Seguridad y límites: [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md)
- Marco institucional: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md). Solo fuentes públicas.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-tanque.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-tanque.md)
