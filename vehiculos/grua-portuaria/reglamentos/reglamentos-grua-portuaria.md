<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: GRUAPORTUARI-08
curso: grua-portuaria
titulo: "Reglamentos de la grúa portuaria (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: GRUAPORTUARI-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Grúa portuaria."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúa portuaria."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos de la grúa portuaria (Chile)

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad competente y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección
1.7 (Maquinaria de izaje fija).

## Ámbito

- País: Chile.
- Marco base: seguridad laboral, no Ley de Tránsito.
- Autoridad: Dirección del Trabajo y mutuales (seguridad laboral); en el recinto
  portuario, además, la Autoridad Marítima (DIRECTEMAR) y la autoridad del puerto.
- Tipo de vehículo: grúa fija de izaje sobre rieles del muelle.

## Habilitación y certificación

- Las grúas fijas **no circulan por vía pública** y **no requieren licencia de
  conducir**.
- La operación la realiza personal **certificado/competente**, con formación
  específica en el equipo.
- Se trabaja con **plan de izaje**, **señalero (rigger)** y **área de exclusión**.
- El detalle de certificación del operador está **(por confirmar)** en el marco
  legal, sección 1.7.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Seguro de accidentes | Ley 16.744 | Seguro social contra accidentes del trabajo. | Contexto de operación segura del escenario. |
| Condiciones de trabajo | D.S. 594 (MINSAL) | Condiciones sanitarias y ambientales básicas. | Reglas de entorno y jornada del escenario. |
| Operador competente | Seguridad laboral | Personal certificado para el equipo (por confirmar). | Modo habilitación del operador. |
| Plan de izaje | Buenas prácticas de izaje | Límites de carga, radios, secuencia. | Modelo de límite de carga y ciclo. |
| Señalero y exclusión | Prevención de riesgos | Rigger y área libre de personas. | Escenario con área de exclusión. |
| Ámbito portuario | Autoridad Marítima y del puerto | Normas del recinto portuario. | Reglas propias del terminal. |

## Reglas de seguridad

- Verificar límite de carga y estado del spreader antes de izar.
- Respetar el límite de viento del anemómetro; detener la operación si se supera.
- Delimitar el área de exclusión y controlar la presencia de personas en tierra.
- Coordinar cada movimiento con el señalero y con el flujo de camiones.
- No izar sin los twist-locks trabados ni con la carga mal calzada.

## Restricciones

- Operación solo por personal certificado/competente (detalle por confirmar).
- Operación según manual del fabricante y límites del equipo.
- Cumplimiento de las normas del recinto portuario y de la Autoridad Marítima.

## Notas para simulación

- El núcleo educativo es la seguridad del izaje: límite de carga, viento y área de exclusión.
- Modelar la coordinación con el señalero y con los camiones.
- Usar avisos educativos en vez de castigos frustrantes.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Habilitación y certificación, Requisitos y elementos de seguridad y Reglas de seguridad** a **interrumpir la cadena que podría producir oscilación, enganche incompleto o ingreso de personas al área de caída**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «oscilación, enganche incompleto o ingreso de personas al área de caída» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Grúa portuaria.

Esta clase se conecta con el resto del curso mediante **control del péndulo y productividad sin superar límites estructurales ni de viento**. El hilo de
seguridad consiste en reconocer a tiempo **oscilación, enganche incompleto o ingreso de personas al área de caída** y poder justificar la decisión
**detener o suavizar el ciclo según viento, señalización y estabilidad de la carga**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **alimentación → accionamientos → carro y cables → spreader y contenedor**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Crane, Derrick and Hoist Safety](https://www.osha.gov/cranes-derricks) aporta izaje, riesgos y controles;
[Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) se usa para navegación, SOLAS, COLREG y STCW. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **oscilación, enganche incompleto o ingreso de personas al área de caída** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **detener o suavizar el ciclo según viento, señalización y estabilidad de la carga** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **oscilación, enganche incompleto o ingreso de personas al área de caída**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Grúa portuaria; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua-portuaria.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-grua-portuaria.md)
