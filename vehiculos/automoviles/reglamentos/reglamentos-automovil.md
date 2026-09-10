<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: AUTOMOVILES-08
curso: automoviles
titulo: "Reglamentos del automóvil (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: AUTOMOVILES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Automóviles."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Automóviles."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del automóvil (Chile)

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automóviles](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito).
- Autoridad: CONASET, MTT, municipalidades, Carabineros.
- Tipo de vehículo: automóvil o camioneta particular hasta 3.500 kg.

## Licencia

- Clase **B** (no profesional), Ley 18.290 Art. 12.
- Edad mínima: 18 años (Art. 13).
- Habilita vehículos de 3 o más ruedas, hasta 9 asientos o carga hasta 3.500 kg.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Cinturón | Ley 18.290, Art. 79 | Obligatorio en asientos delanteros y traseros según año. | Exigir cinturón antes de partir. |
| Retención infantil | Ley 20.904 (Art. 75) | Silla para ninos hasta 8 años; menores de 12 atrás. | Escenario con pasajeros infantiles. |
| Documentos | Ley 18.290 / Ley 18.490 | Padrón, permiso de circulación, revisión técnica, SOAP. | Chequeo previo simulado. |
| Velocidad urbana | Ley 21.103 | 50 km/h general. | Límite del escenario urbano. |
| Alcohol | Ley 20.770 (Ley Emilia) | Sanciones por conducir bajo la influencia del alcohol. | Modo educativo sobre consecuencias. |

## Reglas de seguridad

- Uso obligatorio de cinturón en todos los asientos ocupados.
- Respetar señales, semaforos y prioridades de paso.
- Mantener distancia de seguimiento y velocidad prudente.
- No usar el teléfono mientras se conduce.

## Restricciones

- Edad mínima 18 años para licencia clase B.
- Menores de 12 años deben viajar en el asiento trasero.
- Zonas con límites y restricciones según señalización municipal.

## Notas para simulación

- Modelar cinturón, retención infantil y respeto de señales.
- Usar avisos educativos ante infracciones.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Licencia, Requisitos y elementos de seguridad y Reglas de seguridad** a **interrumpir la cadena que podría producir perder estabilidad por combinar exceso de velocidad, giro y frenado tardío**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «perder estabilidad por combinar exceso de velocidad, giro y frenado tardío» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Automóviles.

Esta clase se conecta con el resto del curso mediante **transferencia de carga y reparto del círculo de adherencia entre frenar, girar y acelerar**. El hilo de
seguridad consiste en reconocer a tiempo **perder estabilidad por combinar exceso de velocidad, giro y frenado tardío** y poder justificar la decisión
**crear margen de detención y dosificar dirección y freno según la superficie**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → transmisión → diferencial → ruedas motrices**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) aporta marco legal chileno;
[Manuales para conductores](https://www.conaset.cl/manuales/) se usa para formación vial y seguridad. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **perder estabilidad por combinar exceso de velocidad, giro y frenado tardío** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **crear margen de detención y dosificar dirección y freno según la superficie** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **perder estabilidad por combinar exceso de velocidad, giro y frenado tardío**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Automóviles; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [CL-CONASET](https://www.conaset.cl/manuales/): Manuales para conductores, CONASET. Uso: formación vial y seguridad.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-automovil.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-automovil.md)
