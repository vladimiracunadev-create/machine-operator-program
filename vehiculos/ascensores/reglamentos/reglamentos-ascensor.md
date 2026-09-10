<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: ASCENSORES-08
curso: ascensores
titulo: "Reglamentos del ascensor (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: ASCENSORES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Ascensores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Ascensores."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del ascensor (Chile)

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
instalar, mantener o inspeccionar se debe consultar la autoridad y la normativa
vigente. El ascensor es maquinaria fija: **no** circula por vía pública ni
requiere licencia de conducir. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección
1.8 (ascensores).

## Ámbito

- País: Chile.
- Ley base: Ley 20.296 (instalación, mantención e inspección de ascensores y
  similares).
- Norma complementaria: Ordenanza General de Urbanismo y Construcciones (OGUC).
- Autoridad: municipalidades (Dirección de Obras) fiscalizan; organismos y
  empresas autorizadas certifican y mantienen.
- Tipo de vehículo: transporte vertical fijo.

## Habilitación, mantención e inspección

- No se necesita licencia de conducir: el ascensor no circula por vía pública.
- La instalación y la mantención las realiza personal **competente** de empresas
  autorizadas.
- La mantención es **periódica** y obligatoria.
- La **certificación** la emite un organismo autorizado.
- La fiscalización recae en la municipalidad (Dirección de Obras).
- Los plazos y detalles exactos están por confirmar (ver marco legal).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Mantención periódica | Ley 20.296 | Mantención por empresa competente. | Modo mantención en el escenario. |
| Certificación | Ley 20.296 | Certificado por organismo autorizado. | Estado certificado del equipo. |
| Fiscalización | Ley 20.296 / OGUC | Control municipal. | Chequeo de vigencia simulado. |
| Freno de seguridad | Normativa técnica | Gobernador y paracaídas operativos. | Modelo de protección ante exceso. |
| Sobrecarga | Normativa técnica | Impedir marcha sobrecargado. | Bloqueo por sobrecarga. |
| Accesibilidad | OGUC | Braille, voz y espacio adecuado. | Interfaz accesible del escenario. |

## Reglas de seguridad

- Cumplir la mantención periódica y conservar la certificación vigente.
- No usar el ascensor fuera de servicio ni forzar las puertas.
- Respetar la carga máxima indicada en la cabina.
- Mantener operativos alarma e intercomunicador.
- Ante emergencia del edificio (incendio), usar la escalera según señalización.

## Restricciones

- No circula por vía pública: sin licencia de conducir.
- Operación y mantención según manual del fabricante y personal competente.
- Modo inspección solo para técnicos autorizados.

## Notas para simulación

- El núcleo educativo es la seguridad: contrapeso, freno de seguridad y sobrecarga.
- Modelar mantención, certificación y estado de servicio como parte del escenario.
- Marcar como "(por confirmar)" los plazos exactos de mantención e inspección.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Habilitación, mantención e inspección, Requisitos y elementos de seguridad y Reglas de seguridad** a **interrumpir la cadena que podría producir movimiento con puertas inseguras, mala nivelación o pérdida de tracción**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «movimiento con puertas inseguras, mala nivelación o pérdida de tracción» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Ascensores.

Esta clase se conecta con el resto del curso mediante **equilibrio de masas y control de aceleración, velocidad, nivelación y frenado**. El hilo de
seguridad consiste en reconocer a tiempo **movimiento con puertas inseguras, mala nivelación o pérdida de tracción** y poder justificar la decisión
**verificar enclavamientos y estado antes de autorizar el movimiento**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → polea tractora → cables → cabina y contrapeso**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [1917.116 Elevators and Escalators](https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116) aporta inspección y riesgos de transporte vertical;
[Vehicle Safety](https://www.nhtsa.gov/vehicle-safety) se usa para seguridad de vehículos terrestres. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **movimiento con puertas inseguras, mala nivelación o pérdida de tracción** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **verificar enclavamientos y estado antes de autorizar el movimiento** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **movimiento con puertas inseguras, mala nivelación o pérdida de tracción**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Ascensores; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-ELEVATORS](https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116): 1917.116 Elevators and Escalators, OSHA. Uso: inspección y riesgos de transporte vertical.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-ascensor.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-ascensor.md)
