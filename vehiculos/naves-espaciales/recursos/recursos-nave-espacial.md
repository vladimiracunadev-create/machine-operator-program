---
tipo_documento: clase
clase: 10
codigo: NAVESESPACIA-10
curso: naves-espaciales
titulo: "Recursos de la nave espacial"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: NAVESESPACIA-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Naves espaciales."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Naves espaciales."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de naves espaciales.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Órbita | Trayectoria de caída libre continua alrededor de un cuerpo. |
| Delta-v | Cambio total de velocidad que una nave puede lograr; mide su capacidad de maniobra. |
| Microgravedad | Estado de caída libre en que los objetos parecen flotar. |
| Propelente | Masa que la nave expulsa para propulsarse. |
| Oxidante | Sustancia que aporta oxígeno para quemar sin aire externo. |
| RCS | Sistema de propulsores pequeños para orientar y trasladar la nave. |
| Reentrada | Regreso a la atmósfera, con calor por fricción. |
| Escudo térmico | Protección que soporta el calor de la reentrada. |
| Apogeo y perigeo | Puntos más alto y más bajo de una órbita. |

---

## 🗺️ Diagrama de una maniobra orbital

```mermaid
flowchart LR
    Orbita[Órbita inicial] --> Motor[Encender motor]
    Motor --> DeltaV[Gastar delta-v]
    DeltaV --> Nueva[Nueva órbita]
    Nueva --> Reserva[Guardar reserva para volver]
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Seguridad y límites: [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md). Distinguir siempre fuentes de
ciencia real de material de ficción.

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Naves espaciales y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-nave-espacial.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-nave-espacial.md)
