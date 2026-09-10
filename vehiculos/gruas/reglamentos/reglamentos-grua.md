<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: GRUAS-08
curso: gruas
titulo: "Reglamentos de la grúa (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: GRUAS-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Grúas."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúas."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos de la grúa (Chile)

[🏠 Inicio](../../../README.md) · [🏗️ Curso: Grúas](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito) para circulación; normativa laboral y
  de seguridad para la operación como maquinaria.
- Autoridad: MTT y municipalidades (tránsito); Dirección del Trabajo y mutuales
  (seguridad laboral); Dirección de Vialidad MOP (cargas sobredimensionadas).
- Tipo de vehículo: grúa / maquinaria automotriz autopropulsada.

## Licencia

- Clase **D** (especial) para maquinaria automotriz, Ley 18.290 Art. 12.
- Edad mínima: 18 años.
- El examen práctico se rinde sobre la maquinaria específica a operar.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Licencia de maquinaria | Ley 18.290, Art. 12 | Clase D para operar la grúa. | Modo licencia por tipo de máquina. |
| Circulación en vía pública | Ley 18.290 | Cumplir señalización y límites. | Reglas de tránsito al desplazarse. |
| Cargas anchas o pesadas | Dirección de Vialidad (MOP) | Autorización y señalización especial. | Escenario de transporte especial. |
| Seguridad de izaje | Normativa laboral y de prevención | Límites de carga, radios, estabilidad. | Modelo de estabilidad y momento de carga. |

## Reglas de seguridad

- Verificar tablas de carga, radio y contrapeso antes de izar.
- Nivelar y estabilizar la máquina (estabilizadores) antes de operar.
- Delimitar el área de trabajo y controlar la presencia de personas.
- No exceder los límites de carga según el ángulo y el alcance.

## Restricciones

- Licencia especial clase D.
- Operación según manual del fabricante y límites de la máquina.
- Permisos adicionales para circular con sobredimensión.

## Notas para simulación

- El núcleo educativo es la estabilidad: momento de carga, radio y contrapeso.
- Modelar el área de exclusión y la señalización.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Licencia, Requisitos y elementos de seguridad y Reglas de seguridad** a **interrumpir la cadena que podría producir exceder la tabla de carga o perder estabilidad del apoyo**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «exceder la tabla de carga o perder estabilidad del apoyo» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Grúas.

Esta clase se conecta con el resto del curso mediante **momento de vuelco igual a carga por radio, condicionado por apoyos y configuración**. El hilo de
seguridad consiste en reconocer a tiempo **exceder la tabla de carga o perder estabilidad del apoyo** y poder justificar la decisión
**confirmar peso, radio, configuración y suelo antes de levantar**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → bombas hidráulicas → cabrestante y pluma → gancho y carga**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Crane, Derrick and Hoist Safety](https://www.osha.gov/cranes-derricks) aporta izaje, riesgos y controles;
[Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) se usa para marco legal chileno. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **exceder la tabla de carga o perder estabilidad del apoyo** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **confirmar peso, radio, configuración y suelo antes de levantar** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **exceder la tabla de carga o perder estabilidad del apoyo**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Grúas; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-grua.md)
