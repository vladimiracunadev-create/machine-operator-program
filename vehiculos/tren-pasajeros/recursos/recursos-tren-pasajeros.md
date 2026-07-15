# 🧰 Recursos del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de tren de pasajeros.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Pantógrafo | Brazo articulado sobre el techo que capta corriente de la catenaria. |
| Catenaria | Cable aéreo bajo tensión que alimenta el tren eléctrico. |
| Bogie | Carro de ejes bajo el vehículo que gira para tomar las curvas. |
| Pestaña | Reborde de la rueda que la guía sobre el riel y evita el descarrilamiento. |
| Adherencia rueda-riel | Agarre disponible del contacto acero-acero antes de patinar. |
| Freno dinámico | Frenado que usa los motores de tracción como generadores. |
| Freno regenerativo | Freno dinámico que devuelve energía a la catenaria. |
| ATP | Sistema que protege la velocidad y frena si se excede el límite. |
| Trocha | Distancia entre las caras internas de los dos rieles. |

---

## 🗺️ Diagrama de reparto de frenado

```mermaid
flowchart LR
    Frenada[Frenada] --> Dinamico[Freno dinámico primero]
    Dinamico --> Regenera[Devuelve energía a la línea]
    Frenada --> Neumatico[Freno neumático complementa]
    Neumatico --> Adherencia[Limitado por adherencia]
    Regenera --> Parada[Detención controlada]
    Adherencia --> Parada
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Fuente institucional del operador estatal (EFE): ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-tren-pasajeros.md)
