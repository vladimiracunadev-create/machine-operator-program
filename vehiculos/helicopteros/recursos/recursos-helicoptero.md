---
tipo_documento: clase
clase: 10
codigo: HELICOPTEROS-10
curso: helicopteros
titulo: "Recursos del helicóptero"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: HELICOPTEROS-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Helicópteros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Helicópteros."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos del helicóptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de helicópteros.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Rotor principal | Conjunto de palas que genera la sustentación y la tracción. |
| Rotor de cola | Rotor pequeño que compensa el par y controla la guiñada. |
| Plato cíclico | Pieza que transmite los mandos a las palas mientras giran. |
| Paso colectivo | Cambio por igual del paso de todas las palas del rotor. |
| Paso cíclico | Cambio del paso pala a pala que inclina el disco rotor. |
| Anti-par | Fuerza que compensa el par del rotor sobre el fuselaje. |
| Autorrotación | Descenso seguro sin motor usando el flujo de aire por el rotor. |
| Efecto suelo | Aumento de sustentación al volar cerca del terreno. |
| Disimetría de sustentación | Diferencia de sustentación entre la pala que avanza y la que retrocede. |

---

## 🗺️ Diagrama de equilibrio del vuelo estacionario

```mermaid
flowchart LR
    Colectivo[Colectivo] --> Sust[Sustentación iguala el peso]
    Sust --> Par[Aparece el par del rotor]
    Par --> Pedal[Pedal compensa con anti-par]
    Ciclico[Cíclico] --> Fijo[Mantiene el punto sin derivar]
    Pedal --> Hover[Vuelo estacionario estable]
    Fijo --> Hover
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Autoridad aeronáutica (DGAC): ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Helicópteros y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HELI](https://www.faa.gov/sites/faa.gov/files/helicopter_flying_handbook.pdf): Helicopter Flying Handbook, FAA. Uso: aerodinámica y control de helicópteros.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-helicoptero.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-helicoptero.md)
