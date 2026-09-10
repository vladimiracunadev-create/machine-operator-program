<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: TRACTORES-08
curso: tractores
titulo: "Reglamentos del tractor (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRACTORES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Tractores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tractores."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del tractor (Chile)

[🏠 Inicio](../../../README.md) · [🚜 Curso: Tractores](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
circular se deben consultar la autoridad de tránsito y la ley vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito) para la circulación en vía pública;
  normativa laboral y de prevención para el trabajo agrícola.
- Autoridad: MTT y municipalidades (tránsito y licencias); Carabineros
  (fiscalización); mutuales y Dirección del Trabajo (seguridad laboral).
- Tipo de vehículo: tractor agrícola, maquinaria automotriz autopropulsada.

## Licencia

- Clase **D** (especial) para maquinaria automotriz, Ley 18.290 Art. 12.
- La clase D habilita para operar tractores, grúas, cargadores,
  retroexcavadoras y maquinaria similar.
- Edad mínima: 18 años (Art. 13).
- El examen práctico se rinde sobre el tipo de maquinaria a operar.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Licencia de maquinaria | Ley 18.290, Art. 12 | Clase D para operar el tractor. | Modo licencia por tipo de máquina. |
| Estructura antivuelco (ROPS) | Normativa de prevención laboral | Arco o cabina de protección contra vuelco. | Estado del ROPS y del cinturón. |
| Cinturón de seguridad | Prevención y Ley 18.290 | Obligatorio dentro del ROPS. | Chequeo previo simulado. |
| Protector de la PTO | Normativa de prevención | Cubierta del eje de toma de fuerza. | Bloqueo si falta el protector. |
| Circulación en vía pública | Ley 18.290 | Luces, señalización y velocidad reducida. | Reglas de tránsito al trasladarse. |
| Traslado de aperos | Ley 18.290 y Vialidad | Señalización de carga ancha o larga. | Escenario de traslado por camino. |

## Documentos obligatorios

| Documento | Para que sirve |
| --- | --- |
| Licencia clase D | Habilita para operar maquinaria automotriz. |
| Padrón | Acredita inscripción del vehículo, si circula por vía pública. |
| Permiso de circulación | Requerido para circular por caminos públicos. |
| SOAP | Seguro obligatorio de accidentes personales para vía pública. |
| Registro de mantenimiento | Respalda el estado seguro de la máquina. |

## Reglas de seguridad

- Operar siempre con la estructura antivuelco (ROPS) y el cinturón puesto.
- Mantener el protector de la PTO y nunca acercarse con el eje en marcha.
- Subir y bajar pendientes en línea recta, evitando giros bruscos.
- Enganchar el tiro desde la barra baja, nunca por encima del eje trasero.
- Señalizar y usar luces al circular por camino público.
- Impedir que otras personas suban o esten cerca durante el trabajo.

## Restricciones

- Licencia especial clase D.
- Velocidad reducida en vía pública y prioridad a la señalización.
- El traslado de aperos anchos o largos requiere señalización especial.

## Notas para simulación

- El núcleo educativo es la estabilidad y la seguridad con la PTO.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar el vuelco en pendiente y el atrapamiento de la PTO como riesgos claros.
- Registrar cada norma usada en
  [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Licencia, Requisitos y elementos de seguridad y Documentos obligatorios** a **interrumpir la cadena que podría producir vuelco lateral, atrapamiento en la toma de fuerza o pérdida de dirección**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «vuelco lateral, atrapamiento en la toma de fuerza o pérdida de dirección» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Tractores.

Esta clase se conecta con el resto del curso mediante **tracción a baja velocidad, transferencia de peso y estabilidad frente al vuelco**. El hilo de
seguridad consiste en reconocer a tiempo **vuelco lateral, atrapamiento en la toma de fuerza o pérdida de dirección** y poder justificar la decisión
**bajar el implemento, reducir velocidad y escoger una trayectoria compatible**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → transmisión → toma de fuerza → apero**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Agricultural Operations: Hazards and Controls](https://www.osha.gov/agricultural-operations/hazards) aporta tractores, aperos y riesgos agrícolas;
[Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) se usa para marco legal chileno. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **vuelco lateral, atrapamiento en la toma de fuerza o pérdida de dirección** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **bajar el implemento, reducir velocidad y escoger una trayectoria compatible** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **vuelco lateral, atrapamiento en la toma de fuerza o pérdida de dirección**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Tractores; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-AGRI](https://www.osha.gov/agricultural-operations/hazards): Agricultural Operations: Hazards and Controls, OSHA. Uso: tractores, aperos y riesgos agrícolas.
- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tractor.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tractor.md)
