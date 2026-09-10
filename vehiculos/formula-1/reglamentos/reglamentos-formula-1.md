<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: FORMULA1-08
curso: formula-1
titulo: "Reglamentos de la Fórmula 1 (FIA)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: FORMULA1-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Fórmula 1."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Fórmula 1."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos de la Fórmula 1 (FIA)

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. La Fórmula 1 **no** se rige por
la ley de tránsito: es una competición regulada por la FIA. Las normas cambian
cada temporada; para datos oficiales hay que consultar el reglamento vigente.
Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección
1.9 (Fórmula 1).

## Ámbito

- Tipo de vehículo: monoplaza de competición, no circula por vía pública.
- Autoridad: FIA (Federación Internacional del Automóvil).
- No requiere licencia de conducir común: exige una superlicencia deportiva de
  la FIA para pilotar en el campeonato.
- En Chile, el automovilismo deportivo se organiza por la federación nacional del
  automovilismo.

## Los dos reglamentos

| Reglamento | Que regula | Ejemplos |
| --- | --- | --- |
| Deportivo | Como se compite | Formato de fin de semana, puntos, banderas, penalizaciones. |
| Técnico | Como es el coche | Dimensiones, peso mínimo, unidad de potencia, seguridad. |

## Reglamento deportivo (resumen educativo)

- **Formato**: entrenamientos, clasificación y carrera.
- **Banderas**: comunican estado de pista (peligro, adelantamiento, fin).
- **Coche de seguridad**: neutraliza la carrera ante un incidente.
- **Penalizaciones**: por tiempo o posiciones ante infracciones.
- **Parque cerrado**: limita los cambios al coche tras la clasificación.

## Reglamento técnico (resumen educativo)

| Tema | Idea general | Aplicación en simulación |
| --- | --- | --- |
| Peso mínimo | El coche no puede bajar de un peso definido. | Parámetro fijo del modelo. |
| Unidad de potencia | Número de componentes limitado por temporada. | Gestión de fiabilidad. |
| Aerodinámica | Superficies y fondo dentro de un reglamento. | Reglaje de carga acotado. |
| Seguridad | Monocasco, halo, pruebas de choque. | Contexto de protección del piloto. |
| Combustible | Cantidad y flujo máximos regulados. | Gestión de consumo por vuelta. |

## Seguridad del piloto

- Monocasco de carbono, cinturones de seguridad y sistema HANS.
- Arco de protección halo sobre la cabeza.
- Casco homologado y traje ignífugo.
- Barreras, escapatorias y sistemas de extracción en el circuito.

## Notas para simulación

- Representar banderas y coche de seguridad como reglas del escenario.
- Usar penalizaciones educativas (avisos, tiempo) en vez de castigos frustrantes.
- Modelar límites técnicos como parámetros (peso, energía, consumo).
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Los dos reglamentos, Reglamento deportivo (resumen educativo) y Reglamento técnico (resumen educativo)** a **interrumpir la cadena que podría producir sobrepasar el agarre disponible al cambiar el balance con freno, volante o acelerador**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «sobrepasar el agarre disponible al cambiar el balance con freno, volante o acelerador» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Fórmula 1.

Esta clase se conecta con el resto del curso mediante **interacción entre carga aerodinámica, temperatura del neumático y balance del monoplaza**. El hilo de
seguridad consiste en reconocer a tiempo **sobrepasar el agarre disponible al cambiar el balance con freno, volante o acelerador** y poder justificar la decisión
**sacrificar velocidad de entrada para conservar estabilidad y tracción de salida**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **unidad de potencia → caja secuencial → diferencial → neumáticos**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Formula 1 Regulations](https://www.fia.com/regulations/formula-1) aporta reglamento, arquitectura y seguridad de Fórmula 1;
[Vehicle Safety](https://www.nhtsa.gov/vehicle-safety) se usa para seguridad de vehículos terrestres. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **sobrepasar el agarre disponible al cambiar el balance con freno, volante o acelerador** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **sacrificar velocidad de entrada para conservar estabilidad y tracción de salida** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **sobrepasar el agarre disponible al cambiar el balance con freno, volante o acelerador**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Fórmula 1; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [FIA-F1-2026](https://www.fia.com/regulations/formula-1): Formula 1 Regulations, FIA. Uso: reglamento, arquitectura y seguridad de Fórmula 1.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-formula-1.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-formula-1.md)
