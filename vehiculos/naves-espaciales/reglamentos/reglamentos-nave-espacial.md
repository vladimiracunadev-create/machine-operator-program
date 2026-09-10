<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: NAVESESPACIA-08
curso: naves-espaciales
titulo: "Reglamentos de la nave espacial (marco público)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: NAVESESPACIA-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Naves espaciales."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Naves espaciales."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos de la nave espacial (marco público)

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · ⚖️ Reglamentos

Referencia educativa e institucional. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- Tipo de vehículo: nave o vehículo espacial (real o de ciencia ficción
  plausible).
- Chile no cuenta a la fecha con una ley espacial nacional integral; el marco
  interno es de política pública más los tratados internacionales.

## Marco nacional

- Política Nacional Espacial: Decreto 30 del Ministerio de Ciencia, Tecnología,
  Conocimiento e Innovación.
- Sistema Nacional Satelital (SNSat), liderado por la FACH.

## Tratados internacionales (marco de UNOOSA)

| Tratado | Objeto |
| --- | --- |
| Tratado del Espacio Ultraterrestre (1967) | Principios de la actividad espacial de los Estados. |
| Acuerdo de Salvamento (1968) | Rescate de astronautas y devolución de objetos. |
| Convenio de Responsabilidad (1972) | Responsabilidad por daños de objetos espaciales. |
| Convenio de Registro (1975) | Registro de objetos lanzados al espacio. |

Principios útiles para el diseño: uso pacífico del espacio, no apropiación
nacional, responsabilidad del Estado de lanzamiento y cooperación internacional.

## Enfoque permitido en simulación

- Principios físicos: propulsión, órbitas, energía, soporte vital, acoplamiento.
- Diferencia entre ciencia realista y ficción interactiva.
- Marco de tratados como reglas del "mundo" del simulador.

## Restricciones de contenido

- No incluir información sensible de sistemas reales de lanzamiento militar.
- Distinguir siempre lo real de lo ficticio.

## Notas para simulación

- Enfocar en orbitalidad, propulsión y soporte vital.
- Usar los tratados como marco narrativo y de reglas.
- Registrar cada fuente pública en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Marco nacional, Tratados internacionales (marco de UNOOSA) y Enfoque permitido en simulación** a **interrumpir la cadena que podría producir colisión o imposibilidad de retirada por quemado mal orientado o tardío**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «colisión o imposibilidad de retirada por quemado mal orientado o tardío» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Naves espaciales.

Esta clase se conecta con el resto del curso mediante **pequeños cambios de velocidad producen cambios acumulativos de órbita y ventanas de encuentro**. El hilo de
seguridad consiste en reconocer a tiempo **colisión o imposibilidad de retirada por quemado mal orientado o tardío** y poder justificar la decisión
**verificar marco de referencia, ventana, delta-v y opción de aborto antes del encendido**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **fuente de energía → propulsión → navegación y control → órbita o trayectoria**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Spaceships and Rockets](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/) aporta naves, sistemas y misiones;
[Space Law Treaties and Principles](https://www.unoosa.org/oosa/SpaceLaw/treaties.html) se usa para derecho espacial internacional. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **colisión o imposibilidad de retirada por quemado mal orientado o tardío** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **verificar marco de referencia, ventana, delta-v y opción de aborto antes del encendido** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **colisión o imposibilidad de retirada por quemado mal orientado o tardío**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Naves espaciales; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-nave-espacial.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-nave-espacial.md)
