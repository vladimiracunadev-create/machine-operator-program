<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: TRENCARGA-08
curso: tren-carga
titulo: "Reglamentos del tren de carga (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRENCARGA-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Tren de carga."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de carga."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del tren de carga (Chile)

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad ferroviaria y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección 1.6 (Ferroviario).

## Ámbito

- País: Chile.
- Ley base: Ley General de Ferrocarriles (número y fecha por confirmar).
- Autoridad: EFE como dueño de la infraestructura y operador estatal histórico, y
  MTT en el rol regulador del sector.
- Tipo de vehículo: tren de carga sobre la red ferroviaria.

## Habilitación y certificación del maquinista

El ferrocarril no usa una licencia de vía pública como los vehículos de carretera,
porque no circula por caminos abiertos sino sobre una vía férrea controlada. En su
lugar se exige la **habilitación o certificación de maquinista** (requisitos exactos
por confirmar), otorgada según la normativa del sector y del operador.

- No hay licencia de conducir de vía pública para el tren.
- El maquinista requiere habilitación o certificación específica (por confirmar).
- Los operadores de carga privados que usan la red operan sobre la infraestructura
  de EFE (régimen y nombres por confirmar).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Habilitación de maquinista | Marco ferroviario (por confirmar) | Certificación vigente para conducir. | Modo habilitación antes de operar. |
| Carga por eje | Marco ferroviario (por confirmar) | No exceder el peso por eje que admite la vía. | Control de carga y reparto por eje. |
| Señalización de vía | Marco ferroviario (por confirmar) | Obedecer señales de circulación y velocidad. | Reglas de señal en el escenario. |
| Pasos a nivel | Marco ferroviario (por confirmar) | Bocina y prioridad según la señalización. | Advertencia sonora obligatoria. |
| Freno del tren | Marco ferroviario (por confirmar) | Tubería de freno operativa en toda la composición. | Chequeo previo simulado de freno. |
| Ancho de vía / trocha | Marco ferroviario (por confirmar) | Material compatible con la trocha de la ruta. | Coherencia de trocha en el escenario. |

## Reglas de seguridad

- Verificar la presión de la tubería de freno antes de mover el tren.
- Respetar el peso por eje y el reparto de carga que admite la vía.
- Obedecer siempre la señalización y los límites de velocidad de la vía.
- Usar bocina y máxima atención al aproximarse a un paso a nivel.
- Anticipar la larga distancia de frenado por la gran masa del tren.

## Restricciones

- Habilitación o certificación de maquinista vigente (por confirmar).
- Circulación sujeta a la señalización y a la gestión de la vía.
- Cargas o composiciones especiales requieren autorización del operador y de EFE
  (por confirmar).

## Notas para simulación

- El núcleo educativo es la gestión de masa: distancia de frenado, adherencia y
  fuerzas longitudinales del tren.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar la baja presión de la tubería de freno como condición que impide circular.
- Citar solo números de ley confirmados en `docs/07-marco-legal-chile.md`; el resto
  se marca como por confirmar. Fuente institucional: efe.cl.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Habilitación y certificación del maquinista, Requisitos y elementos de seguridad y Reglas de seguridad** a **interrumpir la cadena que podría producir rotura de enganche, patinaje o compresión excesiva del convoy**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «rotura de enganche, patinaje o compresión excesiva del convoy» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Tren de carga.

Esta clase se conecta con el resto del curso mediante **fuerzas longitudinales del tren y propagación del freno neumático**. El hilo de
seguridad consiste en reconocer a tiempo **rotura de enganche, patinaje o compresión excesiva del convoy** y poder justificar la decisión
**aplicar potencia y freno de modo gradual considerando la longitud completa**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **locomotora → generador y tracción → enganches → rueda-carril**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Railroad Operating Practices](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0) aporta operación, señalización y competencias ferroviarias;
[Human Factors: Tasks and Demands](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands) se usa para factores humanos y carga de trabajo. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **rotura de enganche, patinaje o compresión excesiva del convoy** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **aplicar potencia y freno de modo gradual considerando la longitud completa** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **rotura de enganche, patinaje o compresión excesiva del convoy**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Tren de carga; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-carga.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tren-carga.md)
