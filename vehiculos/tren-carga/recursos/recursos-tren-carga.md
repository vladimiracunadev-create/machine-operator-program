# 🧰 Recursos del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de tren de carga.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Bogie | Carro pivotante con ejes que soporta la locomotora o el vagón y sigue la vía. |
| Rueda de pestaña | Rueda con reborde interior que guía el tren sobre el riel. |
| Adherencia rueda-riel | Agarre disponible del contacto acero-acero antes de patinar. |
| Arenado | Lanzar arena sobre el riel para aumentar la adherencia. |
| Tubería de freno | Conducto de aire que recorre el tren y acciona el freno de cada vagón. |
| Freno dinámico | Uso de los motores de tracción como generadores para frenar. |
| Distributed power | Reparto de locomotoras a lo largo del tren para repartir el esfuerzo. |
| Enganche AAR | Enganche automático tipo cuchara que se acopla al juntar vagones. |
| Peso por eje | Carga que cada eje transmite al riel; limita el tonelaje de la vía. |
| Trocha | Distancia entre los dos rieles de la vía. |

---

## 🗺️ Diagrama de tracción diesel-eléctrica

```mermaid
flowchart LR
    Diesel[Motor diesel] --> Generador[Generador / alternador]
    Generador --> Control[Control de tracción]
    Control --> Motores[Motores de tracción]
    Motores --> Ruedas[Ruedas de pestaña]
    Ruedas --> Riel[Riel]
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Empresa de los Ferrocarriles del Estado (EFE): ver el registro de fuentes (efe.cl).

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-tren-carga.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-tren-carga.md)
