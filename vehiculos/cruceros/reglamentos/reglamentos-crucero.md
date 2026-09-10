<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: CRUCEROS-08
curso: cruceros
titulo: "Reglamentos: Cruceros (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: CRUCEROS-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Cruceros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Cruceros."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos: Cruceros (Chile)

[🏠 Inicio](../../../README.md) · [⛴️ Curso: Cruceros](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: DL 2.222 de 1978 (Ley de Navegación).
- Autoridad: DIRECTEMAR (DGTM y MM), como Autoridad Marítima.
- Marco internacional: OMI / IMO (SOLAS, STCW, MARPOL, COLREG).
- Tipo de nave: buque de pasaje, con énfasis en la seguridad de la vida humana.

## Títulos y dotación

- Títulos de la Marina Mercante otorgados por DIRECTEMAR (Reglamento TM-007A,
  D.S. 127/2019).
- Escalafón de cubierta: Capitán, Piloto Primero, Segundo, Tercero, Costero.
- Título de capitán: ser chileno y poseer el título del Director (DL 2.222,
  Art. 49).
- Dotación mínima de seguridad determinada por la Dirección (DL 2.222, Art. 73),
  con roles de emergencia asignados a toda la tripulación en buques de pasaje.

## Requisitos y convenios

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Seguridad de la vida en el mar | SOLAS 1974 | Compartimentado, botes para todos, detección y extinción de incendios. | Chequeos de seguridad y estado de botes. |
| Evacuación y muster | SOLAS, Cap. III | Ejercicio de reunión del pasaje y medios de salvamento. | Procedimiento de muster antes de zarpar. |
| Estabilidad tras avería | SOLAS, Cap. II-1 | Flotar y mantenerse tras una vía de agua definida. | Modelo de inundación por compartimentos. |
| Formación y guardia | STCW 1978 | Titulación, turnos de guardia y gestión de crisis del pasaje. | Roles de tripulación y guardias. |
| Prevención de la contaminación | MARPOL 73/78 | Gestión de aguas residuales y residuos del buque. | Reglas ambientales del escenario. |
| Prevención de abordajes | COLREG 1972 | Reglas de rumbo, luces y señales. | Reglas de navegación y prioridad. |

## Reglas de seguridad

- Realizar el ejercicio de muster del pasaje antes o poco después de zarpar.
- Mantener los medios de salvamento listos y para todas las personas a bordo.
- Respetar las reglas de rumbo y gobierno para evitar abordajes (COLREG).
- Mantener guardias de navegación según la titulación (STCW).
- Cumplir los procedimientos de seguridad y de protección del medio marino.
- Obligación de auxilio a personas en peligro en el mar (DL 2.222).

## Restricciones

- Operación según el título del personal y la dotación mínima de seguridad.
- Capacidad de pasaje limitada por los medios de salvamento y la certificación.
- Zonas de navegación y de puerto según la Autoridad Marítima.

## Notas para simulación

- El núcleo educativo son la seguridad del pasaje, el muster y la evacuación.
- Modelar luces de navegación, prioridades COLREG y maniobras de puerto.
- Representar el compartimentado y la estabilidad tras avería de forma didáctica.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Títulos y dotación, Requisitos y convenios y Reglas de seguridad** a **interrumpir la cadena que podría producir contacto con muelle o pérdida de separación por subestimar abatimiento**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «contacto con muelle o pérdida de separación por subestimar abatimiento» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Cruceros.

Esta clase se conecta con el resto del curso mediante **maniobrabilidad de gran masa combinada con viento lateral y efecto de aguas restringidas**. El hilo de
seguridad consiste en reconocer a tiempo **contacto con muelle o pérdida de separación por subestimar abatimiento** y poder justificar la decisión
**coordinar propulsión, remolcadores y límites de viento antes de aproximar**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **generación eléctrica → propulsión → hélices o pods → casco y gobierno**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) aporta navegación, SOLAS, COLREG y STCW;
[Collision Regulations](https://www.imo.org/en/about/conventions/pages/colreg.aspx) se usa para prevención de abordajes. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **contacto con muelle o pérdida de separación por subestimar abatimiento** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **coordinar propulsión, remolcadores y límites de viento antes de aproximar** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **contacto con muelle o pérdida de separación por subestimar abatimiento**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Cruceros; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [IMO-COLREG](https://www.imo.org/en/about/conventions/pages/colreg.aspx): Collision Regulations, International Maritime Organization. Uso: prevención de abordajes.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-crucero.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-crucero.md)
