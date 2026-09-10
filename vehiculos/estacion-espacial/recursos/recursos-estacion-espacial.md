---
tipo_documento: clase
clase: 10
codigo: ESTACIONESPA-10
curso: estacion-espacial
titulo: "Recursos de la estación espacial"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: ESTACIONESPA-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Estación espacial (ISS)."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Estación espacial (ISS)."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos de la estación espacial

[🏠 Inicio](../../../README.md) · [🛰️ Curso: Estación espacial (ISS)](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de estación espacial.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Estación espacial | Habitat permanente en órbita donde vive y trabaja una tripulación. |
| Módulo | Cada sección presurizada que se une a otras para formar la estación. |
| Nodo de unión | Módulo que conecta otros módulos y reparte el paso interno. |
| Microgravedad | Estado de caída libre en que los objetos parecen flotar. |
| Soporte vital de ciclo cerrado | Sistema que recicla aire y agua para durar más. |
| Acoplamiento | Unión hermética de una nave con la estación. |
| EVA | Actividad extravehicular o caminata espacial en el exterior. |
| Esclusa de aire | Cierre que permite salir al vacío sin despresurizar toda la estación. |
| Reimpulso | Maniobra para elevar la órbita que baja por el rozamiento. |
| Radiador | Panel que expulsa el calor sobrante al espacio. |

---

## 🗺️ Diagrama del soporte vital de ciclo cerrado

```mermaid
flowchart LR
    Aire[Aire usado] --> RetiraCO2[Retirar CO2]
    RetiraCO2 --> GeneraO2[Generar oxígeno]
    GeneraO2 --> AireLimpio[Aire respirable]
    AguaUsada[Agua usada] --> Recicla[Reciclar]
    Recicla --> AguaLimpia[Agua limpia]
    AguaLimpia --> Tripulacion[Tripulación]
    AireLimpio --> Tripulacion
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Seguridad y límites: [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Estación espacial (ISS) y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-ISS](https://www.nasa.gov/reference/international-space-station/): International Space Station, NASA. Uso: módulos, órbita y soporte vital.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-estacion-espacial.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-estacion-espacial.md)
