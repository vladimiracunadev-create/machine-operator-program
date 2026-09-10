<!-- clase-meta
tipo_documento: clase
clase: 10
codigo: ESTRELLADELA-10
curso: estrella-de-la-muerte
titulo: "Recursos de la Estrella de la Muerte"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: ESTRELLADELA-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Estrella de la Muerte."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Estrella de la Muerte."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧰 Recursos de la Estrella de la Muerte

[🏠 Inicio](../../../README.md) · [🌑 Curso: Estrella de la Muerte](../README.md) · 🧰 Recursos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Glosario específico, enlaces y diagramas de apoyo del curso de la estación-mundo.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Gravedad propia | Atracción que genera un cuerpo por su propia masa. |
| Masa total | Cantidad de materia de la estación; a escala lunar es gigantesca. |
| Presupuesto de energía | Energía disponible por unidad de tiempo, a repartir entre sistemas. |
| Reparto de energía | Decisión de cuanta potencia recibe cada sistema. |
| Conservación de la energía | La energía no se pierde; se transforma, a menudo en calor. |
| Disipación de calor | Expulsión de calor; en el vacío, solo por radiación. |
| Radiación | Única vía de expulsar calor sin aire, a través de la superficie. |
| Soporte vital | Sistemas que mantienen aire, agua y temperatura habitables. |
| Logística | Gestión de suministros y transporte para la población. |
| Escala | Tamaño relativo; a escala de luna cambian las reglas físicas. |

---

## 🗺️ Diagrama: energía, calor y vida

```mermaid
flowchart LR
    Presu[Presupuesto de energía] --> Reparto[Reparto entre sistemas]
    Reparto --> Vida[Soporte vital y logística]
    Reparto --> Otros[Otros consumos]
    Vida --> Calor[Todo genera calor]
    Otros --> Calor
    Calor --> Radia[Radiar por la superficie]
    Radia --> Idea[Energía y calor son el gran equilibrio]
```

---

## 🔗 Enlaces y fuentes

- Portada del curso: [🌑 Curso: Estrella de la Muerte](../README.md)
- Catálogo de naves de ficción: [🌌 Naves de ficción](../../README.md)
- Glosario general: [📖 docs/05-glosario-general.md](../../../docs/05-glosario-general.md)
- Niveles de realismo: [🎚️ docs/03-niveles-de-realismo.md](../../../docs/03-niveles-de-realismo.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, respetando el aviso de
derechos del catálogo de naves de ficción.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Glosario específico, Diagrama: energía, calor y vida, Enlaces y fuentes y Guía de estudio aplicada** a **explicar con fuentes los términos reactor ficticio, distribución, propulsión y control y estación**?

### Explicación razonada

El vocabulario técnico organiza relaciones: reactor ficticio, distribución, propulsión y control y estación nombran partes distintas de una misma cadena funcional. Una fuente se usa para sostener una afirmación concreta —principio, límite, procedimiento o contexto— y debe distinguirse del manual particular de un fabricante o de una regla narrativa.

Esta clase se conecta con el resto del curso mediante **una megaestructura debe modelarse como red de subsistemas y dependencias, no como un solo vehículo**. El hilo de
seguridad consiste en reconocer a tiempo **crear un sistema invulnerable o sin propagación comprensible de fallas** y poder justificar la decisión
**mapear dependencias, redundancias y estados degradados antes de decidir**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **reactor ficticio → distribución → propulsión y control → estación**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Death Star](https://www.starwars.com/databank/death-star) aporta canon narrativo de la estación;
[Spaceships and Rockets](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/) se usa para naves, sistemas y misiones. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir en contexto:** explica **reactor ficticio**, **distribución**, **propulsión y control** y **estación** por su función y relación.
2. **Respaldar:** enlaza cada afirmación importante con una fuente identificable y declara su alcance.
3. **Contrastar:** separa principios generales, requisitos locales, manual de fabricante y —si aplica— canon ficticio.
4. **Reformular:** convierte una definición copiada en una explicación propia con un ejemplo de **Estrella de la Muerte**.

### Comprueba tu comprensión

1. Explica la diferencia funcional entre **distribución** y **propulsión y control** sin copiar una definición.
2. ¿Qué fuente respalda el principio «una megaestructura debe modelarse como red de subsistemas y dependencias, no como un solo vehículo» y cuál es su alcance?
3. ¿Qué dato exigiría un manual de fabricante en vez de una fuente general?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Estrella de la Muerte y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [STARWARS-DEATHSTAR](https://www.starwars.com/databank/death-star): Death Star, Lucasfilm. Uso: canon narrativo de la estación.
- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-estrella-de-la-muerte.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-estrella-de-la-muerte.md)
