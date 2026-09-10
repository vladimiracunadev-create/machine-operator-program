---
tipo_documento: clase
clase: 10
codigo: CAZAESTELAR-10
curso: caza-estelar
titulo: "Recursos del caza estelar"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: CAZAESTELAR-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Caza estelar."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Caza estelar."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos del caza estelar

[🏠 Inicio](../../../README.md) · [🛸 Curso: Caza estelar](../README.md) · 🧰 Recursos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Glosario específico, enlaces y diagramas de apoyo del curso de caza estelar.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Vacío | Espacio sin aire; sin rozamiento ni sonido ni sustentación. |
| Inercia | Tendencia de un objeto a mantener su velocidad si no hay fuerzas. |
| Momento | Producto de masa por velocidad; se conserva sin fuerzas externas. |
| Delta-v | Cambio total de velocidad que la nave puede lograr con su propelente. |
| Propelente | Masa que el motor expulsa para generar empuje por reacción. |
| Empuje | Fuerza que impulsa la nave, resultado de expulsar masa. |
| RCS | Propulsores de control de reacción para rotar o trasladar la nave. |
| Orientación | Hacia donde apunta la nave, distinta de hacia donde se mueve. |
| Viraje bancado | Giro inclinado típico de un avión; imposible sin aire. |
| Reentrada | Entrada a una atmósfera, donde aparecen aire, calor y rozamiento. |

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
- Catálogo de naves de ficción: [🌌 Naves de ficción](../../README.md)
- Glosario general: [📖 docs/05-glosario-general.md](../../../docs/05-glosario-general.md)
- Niveles de realismo: [🎚️ docs/03-niveles-de-realismo.md](../../../docs/03-niveles-de-realismo.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, respetando el aviso de
derechos del catálogo de naves de ficción.

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Caza estelar y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [STARWARS-DATABANK](https://www.starwars.com/databank): Star Wars Databank, Lucasfilm. Uso: canon narrativo y diseño visual.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-caza-estelar.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-caza-estelar.md)
