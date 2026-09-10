<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: CAMIONES-08
curso: camiones
titulo: "Reglamentos del camión (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: CAMIONES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Camiones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Camiones."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del camión (Chile)

[🏠 Inicio](../../../README.md) · [🚛 Curso: Camiones](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
circular se deben consultar la autoridad de tránsito y la ley vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito).
- Autoridad: MTT, CONASET, municipalidades (licencias), Carabineros
  (fiscalización) y Dirección de Vialidad MOP (pesos y cargas en ruta).
- Tipo de vehículo: camión de carga, simple o articulado, de vía pública.

## Licencia

- Clase **A-4** (profesional) para vehículos simples de carga con peso bruto
  vehicular superior a 3.500 kg, Ley 18.290 Art. 12.
- Clase **A-5** (profesional) para todo vehículo de carga, simple o articulado;
  incluye la clase A-4, Ley 18.290 Art. 12.
- Edad mínima: 18 años (Art. 13); las clases profesionales exigen además haber
  sido titular previo de licencia Clase B (requisitos exactos en el marco legal).
- El tractocamion con semirremolque (articulado) requiere clase **A-5**.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Licencia profesional | Ley 18.290, Art. 12 | A-4 para simple; A-5 para articulado. | Modo licencia según configuración del camión. |
| Peso por eje y total | Ley 18.290 y Vialidad (MOP) | No exceder los pesos máximos por eje ni el PBV. | Control de carga y reparto por eje. |
| Cinturón de seguridad | Ley 18.290, Art. 79 | Obligatorio para conductor y acompañante. | Chequeo previo simulado. |
| Amarre de carga | Ley 18.290 y normas de transporte | Carga asegurada y sin sobresalir. | Estado de amarre antes de partir. |
| Documentos | Ley 18.290 / Ley 18.490 | Padrón, permiso de circulación, revisión técnica, SOAP. | Chequeo previo simulado. |
| Velocidad de pesados | Ley 18.290, Art. 150 | Límites menores que livianos en ruta. | Límite del escenario según vía. |

## Documentos obligatorios

| Documento | Para que sirve |
| --- | --- |
| Padrón | Acredita inscripción en el Registro de Vehículos Motorizados. |
| Permiso de circulación | Autorización anual, vence el 31 de marzo. |
| Revisión técnica y de gases | Verifica estado mecánico y emisiones. |
| SOAP | Seguro obligatorio que cubre lesiones a personas. |
| Guía de despacho / documentos de la carga | Respaldan la mercancía transportada. |

## Reglas de seguridad

- Verificar la presión de aire antes de mover el camión.
- Respetar los límites de peso por eje y el peso bruto vehicular.
- Asegurar la carga y revisar el amarre en cada parada.
- Usar freno de motor y retarder en descensos largos.
- Mantener gran distancia de seguimiento por la distancia de frenado.
- Respetar la jornada de conducción y los descansos para evitar la fatiga.

## Restricciones

- Licencia profesional clase A-4 (simple) o A-5 (articulado).
- Circulación sujeta a límites de peso y a restricciones de vía o horario.
- Cargas anchas, largas o pesadas requieren autorización especial de Vialidad.

## Notas para simulación

- El núcleo educativo es la gestión de masa: distancia de frenado, pendientes y
  reparto de carga.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar la baja presión de aire como condición que impide circular.
- Registrar cada norma usada en
  [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Licencia, Requisitos y elementos de seguridad y Documentos obligatorios** a **interrumpir la cadena que podría producir embalamiento, fatiga de frenos o pérdida de estabilidad de la carga**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «embalamiento, fatiga de frenos o pérdida de estabilidad de la carga» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Camiones.

Esta clase se conecta con el resto del curso mediante **relación entre masa, pendiente, energía cinética y capacidad térmica de frenado**. El hilo de
seguridad consiste en reconocer a tiempo **embalamiento, fatiga de frenos o pérdida de estabilidad de la carga** y poder justificar la decisión
**planificar velocidad y relación de transmisión antes de entrar en la pendiente**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → caja de cambios → árbol y diferencial → ruedas motrices**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) aporta marco legal chileno;
[Commercial Driver's License Manual](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual) se usa para operación de buses y camiones. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **embalamiento, fatiga de frenos o pérdida de estabilidad de la carga** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **planificar velocidad y relación de transmisión antes de entrar en la pendiente** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **embalamiento, fatiga de frenos o pérdida de estabilidad de la carga**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Camiones; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [US-FMCSA-CDL](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual): Commercial Driver's License Manual, FMCSA. Uso: operación de buses y camiones.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-camion.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-camion.md)
