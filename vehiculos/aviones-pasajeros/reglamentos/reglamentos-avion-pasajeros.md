<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: AVIONESPASAJ-08
curso: aviones-pasajeros
titulo: "Reglamentos del avión de pasajeros (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: AVIONESPASAJ-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Aviones de pasajeros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones de pasajeros."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del avión de pasajeros (Chile)

[🏠 Inicio](../../../README.md) · [🛫 Curso: Aviones de pasajeros](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.916 (Código Aeronáutico).
- Autoridad: Dirección General de Aeronáutica Civil (DGAC).
- Marco internacional: OACI / ICAO (Convenio de Chicago, 1944).
- Tipo de operación: transporte aéreo comercial de pasajeros.

## Licencias del personal

- Otorgadas por la DGAC según la reglamentación DAR-01 y normas DAN.
- Para volar un avión de pasajeros en línea se requiere la licencia de **Piloto de
  Transporte de Línea Aérea (ATP)**, el nivel más alto de piloto.
- La ATP exige experiencia y horas de vuelo muy superiores a la PPL o la CPL,
  examenes teóricos y prácticos, y habilitación de vuelo por instrumentos.
- Cada piloto necesita **habilitación de tipo** para el modelo de avión y un
  **certificado médico** aeronáutico de la clase correspondiente vigente.

## Operación comercial (AOC)

- El transporte comercial se realiza bajo un **Certificado de Operador Aéreo
  (AOC)** emitido por la DGAC, que autoriza a la aerolinea a operar.
- La operación se rige por un manual de operaciones, procedimientos aprobados y
  limitaciones de tiempo de servicio de la tripulación.
- La aeronave debe mantener su **certificado de aeronavegabilidad** mediante un
  programa de mantenimiento aprobado.

## Requisitos y normas

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Matrícula | Código Aeronáutico, Art. 32 | Inscripción en el Registro Nacional de Aeronaves. | Estado documental de la aeronave. |
| Aeronavegabilidad | Código Aeronáutico, Art. 52 | Certificado de aeronavegabilidad vigente. | Chequeo previo al vuelo. |
| Licencia ATP | DAR-01 / normas DAN | Piloto de transporte de línea con habilitación de tipo. | Perfil de tripulación del escenario. |
| Operador aéreo | Código Aeronáutico / DAN | Certificado de operador aéreo (AOC) para operar comercial. | Marco de operación de la aerolinea. |
| Espacio aéreo | Código Aeronáutico, Art. 1 | Soberanía y reglas del espacio aéreo. | Reglas de tráfico aéreo del escenario. |
| Reglas de vuelo | Normas DAN | Vuelo por instrumentos (IFR) en operación de línea. | Aproximaciones y aerovias del escenario. |

## Reglas de seguridad

- Volar con licencia ATP, habilitación de tipo y certificado médico vigentes.
- Completar las listas de verificación y el briefing antes de cada fase.
- Respetar el espacio aéreo controlado y las instrucciones del control de tráfico.
- Vigilar combustible, meteorología y peso y balance dentro de límites.
- Operar bajo el AOC y los procedimientos aprobados del operador.

## Restricciones

- Operación de línea solo bajo un certificado de operador aéreo (AOC).
- Limitaciones de tiempo de vuelo y de servicio de la tripulación.
- Reglas de vuelo por instrumentos y mínimos de aeropuerto según la autoridad.
- Zonas restringidas y controladas según la autoridad aeronáutica.

## Notas para simulación

- El núcleo educativo son la operación en tripulación, los instrumentos y los procedimientos.
- Modelar plan de vuelo, comunicaciones, checklist y aproximaciones instrumentales.
- Representar la operación comercial (AOC) como marco, sin datos sensibles reales.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Licencias del personal, Operación comercial (AOC) y Requisitos y normas** a **interrumpir la cadena que podría producir continuar una aproximación inestable o automatizar sin comprender el modo activo**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «continuar una aproximación inestable o automatizar sin comprender el modo activo» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Aviones de pasajeros.

Esta clase se conecta con el resto del curso mediante **gestión de energía vertical y horizontal mediante actitud, empuje y configuración**. El hilo de
seguridad consiste en reconocer a tiempo **continuar una aproximación inestable o automatizar sin comprender el modo activo** y poder justificar la decisión
**confirmar modo, energía y configuración; frustrar si la estabilidad no se recupera**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → empuje → flujo de aire → alas y controles**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Aviation Handbooks and Manuals](https://www.faa.gov/regulations_policies/handbooks_manuals) aporta aerodinámica, sistemas y operación;
[Normativa aeronáutica](https://www.dgac.gob.cl/normativa/) se usa para marco aeronáutico chileno. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **continuar una aproximación inestable o automatizar sin comprender el modo activo** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **confirmar modo, energía y configuración; frustrar si la estabilidad no se recupera** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **continuar una aproximación inestable o automatizar sin comprender el modo activo**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Aviones de pasajeros; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-avion-pasajeros.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-avion-pasajeros.md)
