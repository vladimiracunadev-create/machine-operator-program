---
tipo_documento: clase
clase: 10
codigo: TRANSBORDADO-10
curso: transbordadores
titulo: "Recursos del transbordador"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: TRANSBORDADO-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Transbordadores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Transbordadores."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de transbordadores.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Orbitador | Nave alada del transbordador que lleva tripulación y carga y regresa a la pista. |
| Propulsores laterales | Cohetes que dan empuje extra en el despegue y luego se separan. |
| Tanque externo | Depósito que alimenta los motores del orbitador y se desecha en el ascenso. |
| Escudo térmico | Protección de losetas que soporta el calor de la reentrada. |
| Reentrada | Regreso a la atmósfera, con calor por fricción con el aire. |
| Planeo sin motor | Descenso final controlado solo por la aerodinámica, sin empuje. |
| Elevones | Superficies del ala que combinan cabeceo y alabeo. |
| Ángulo de reentrada | Inclinación con que la nave vuelve a la atmósfera. |
| Bahía de carga | Compartimento con puertas para desplegar cargas en órbita. |
| Senda de planeo | Trayectoria de descenso hacia la pista. |

---

## 🗺️ Diagrama del ciclo del transbordador

```mermaid
flowchart LR
    Despega[Despegar como cohete] --> Orbita[Trabajar en órbita]
    Orbita --> Desorbita[Frenar y desorbitar]
    Desorbita --> Reentra[Reentrar con escudo]
    Reentra --> Planea[Planear sin motor]
    Planea --> Aterriza[Aterrizar en pista]
    Aterriza --> Prepara[Preparar para otra misión]
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Seguridad y límites: [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Transbordadores y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-SHUTTLE](https://www.nasa.gov/reference/the-space-shuttle/): The Space Shuttle, NASA. Uso: arquitectura y operación del transbordador.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-transbordador.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-transbordador.md)
