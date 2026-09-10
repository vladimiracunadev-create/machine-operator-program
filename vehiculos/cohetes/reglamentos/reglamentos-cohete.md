<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: COHETES-08
curso: cohetes
titulo: "Reglamentos del cohete (marco público)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: COHETES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Cohetes."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Cohetes."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del cohete (marco público)

[🏠 Inicio](../../../README.md) · [🚀 Curso: Cohetes](../README.md) · ⚖️ Reglamentos

Referencia educativa e institucional. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md) sección 4.

## Ámbito

- Tipo de vehículo: cohete lanzador real de uso civil o comercial.
- Un cohete opera bajo la jurisdicción del **Estado de lanzamiento** y su agencia
  espacial, dentro del marco de los tratados internacionales.
- Chile no cuenta a la fecha con una ley espacial nacional integral; el marco
  interno es de política pública más los tratados internacionales.

## Estado de lanzamiento y su agencia

Cada lanzamiento tiene un **Estado de lanzamiento** responsable ante la comunidad
internacional. Ese Estado autoriza y supervisa la operación a través de su
agencia espacial o autoridad reguladora.

| Agencia o rol | Ejemplo | Función |
| --- | --- | --- |
| Agencia espacial nacional | NASA, ESA, Roscosmos, JAXA, CSA | Programa y supervisa misiones. |
| Autoridad de licencias | Regulador civil de lanzamiento | Autoriza el vuelo y la seguridad de rango. |
| Estado de lanzamiento | País responsable | Responde por daños ante los tratados. |
| Marco nacional en Chile | Política Nacional Espacial | Orienta la actividad espacial del país. |

## Tratados internacionales (marco de UNOOSA)

| Tratado | Objeto |
| --- | --- |
| Tratado del Espacio Ultraterrestre (1967) | Principios de la actividad espacial de los Estados. |
| Acuerdo de Salvamento (1968) | Rescate de astronautas y devolución de objetos. |
| Convenio de Responsabilidad (1972) | Responsabilidad por daños de objetos espaciales. |
| Convenio de Registro (1975) | Registro de objetos lanzados al espacio. |

Principios útiles para el diseño: uso pacífico del espacio, no apropiación
nacional, responsabilidad del Estado de lanzamiento y registro de cada objeto que
se pone en órbita. El detalle chileno está en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md) sección 4.

## Enfoque permitido en simulación

- Principios físicos: empuje, etapas, ascenso y velocidad orbital.
- Seguridad de rango y ventanas de lanzamiento como reglas del escenario.
- Marco de tratados como reglas del "mundo" del simulador.

## Restricciones de contenido

- No incluir información sensible de sistemas de lanzamiento militar.
- No detallar procedimientos que permitan replicar armamento.
- Mantener el enfoque público, educativo y general.

## Notas para simulación

- Exigir sistemas en verde y autorización antes de encender motores.
- Usar avisos educativos en vez de castigos frustrantes.
- Registrar cada fuente pública en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Estado de lanzamiento y su agencia, Tratados internacionales (marco de UNOOSA) y Enfoque permitido en simulación** a **interrumpir la cadena que podría producir inestabilidad, desviación o cargas excesivas durante máxima presión dinámica**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «inestabilidad, desviación o cargas excesivas durante máxima presión dinámica» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Cohetes.

Esta clase se conecta con el resto del curso mediante **la aceleración depende de empuje menos peso y resistencia, mientras la masa disminuye**. El hilo de
seguridad consiste en reconocer a tiempo **inestabilidad, desviación o cargas excesivas durante máxima presión dinámica** y poder justificar la decisión
**evaluar trayectoria, estabilidad y condiciones de aborto antes del lanzamiento**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **propelentes → cámara → tobera → empuje y trayectoria**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Rockets Educator Guide](https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf) aporta propulsión, estabilidad y trayectoria;
[Space Law Treaties and Principles](https://www.unoosa.org/oosa/SpaceLaw/treaties.html) se usa para derecho espacial internacional. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **inestabilidad, desviación o cargas excesivas durante máxima presión dinámica** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **evaluar trayectoria, estabilidad y condiciones de aborto antes del lanzamiento** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **inestabilidad, desviación o cargas excesivas durante máxima presión dinámica**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Cohetes; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-ROCKETS](https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf): Rockets Educator Guide, NASA. Uso: propulsión, estabilidad y trayectoria.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-cohete.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-cohete.md)
