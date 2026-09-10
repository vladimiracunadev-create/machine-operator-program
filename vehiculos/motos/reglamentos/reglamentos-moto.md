<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: MOTOS-08
curso: motos
titulo: "Reglamentos de la moto (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: MOTOS-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Motocicletas."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Motocicletas."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos de la moto (Chile)

[🏠 Inicio](../../../README.md) · [🏍️ Curso: Motos](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
circular se deben consultar la autoridad de tránsito y la ley vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito).
- Autoridad: CONASET, MTT, municipalidades (licencias) y Carabineros
  (fiscalización).
- Tipo de vehículo: motocicleta de vía pública.

## Licencia

- Clase **C** (no profesional), Ley 18.290 Art. 12.
- Edad mínima: 18 años (Art. 13).
- La licencia habilita motocicletas, motonetas y bicimotos.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Casco | Ley 18.290, Art. 84 | Obligatorio para conductor y acompañante. | Advertir o bloquear el arranque sin casco. |
| Luces | Ley 18.290 | Uso de luces según norma. | Estado de luces en el tablero. |
| Documentos | Ley 18.290 / Ley 18.490 | Padrón, permiso de circulación, revisión técnica, SOAP. | Chequeo previo simulado. |
| Velocidad urbana | Ley 21.103 | 50 km/h general. | Límite del escenario urbano. |
| Convivencia vial | Ley 21.088 | Distancia y respeto a usuarios vulnerables. | Reglas de tráfico del escenario. |

## Reglas de seguridad

- Usar siempre casco homologado y protección adecuada.
- Encender luces y señalizar cada maniobra con anticipación.
- Mantener distancia y velocidad prudente.
- Adaptar la conducción a lluvia, viento o baja visibilidad.
- No circular entre vehículos de forma imprudente.

## Restricciones

- Edad mínima 18 años para licencia clase C.
- Acompañante solo si la moto lo permite y con casco.
- Zonas o vías con restricciones específicas según señalización.

## Notas para simulación

- Representar casco y señalización como habitos correctos.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Ajustar los límites de velocidad al escenario.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Licencia, Requisitos y elementos de seguridad y Reglas de seguridad** a **interrumpir la cadena que podría producir agotar adherencia por frenar o acelerar bruscamente con la moto inclinada**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «agotar adherencia por frenar o acelerar bruscamente con la moto inclinada» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Motocicletas.

Esta clase se conecta con el resto del curso mediante **equilibrio entre inclinación, velocidad, radio y adherencia disponible**. El hilo de
seguridad consiste en reconocer a tiempo **agotar adherencia por frenar o acelerar bruscamente con la moto inclinada** y poder justificar la decisión
**ajustar velocidad, trayectoria y suavidad de los mandos antes de inclinar**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → embrague y caja → transmisión final → neumático trasero**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) aporta marco legal chileno;
[Manuales para conductores](https://www.conaset.cl/manuales/) se usa para formación vial y seguridad. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **agotar adherencia por frenar o acelerar bruscamente con la moto inclinada** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **ajustar velocidad, trayectoria y suavidad de los mandos antes de inclinar** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **agotar adherencia por frenar o acelerar bruscamente con la moto inclinada**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Motocicletas; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [CL-CONASET](https://www.conaset.cl/manuales/): Manuales para conductores, CONASET. Uso: formación vial y seguridad.
- [US-NHTSA-MOTO](https://www.nhtsa.gov/road-safety/motorcycles): Motorcycle Safety, NHTSA. Uso: riesgos, equipo y conducción segura.
- [MSF-BRC](https://msf-usa.org/library/): Motorcycle Safety Foundation Library, MSF. Uso: formación inicial y ejercicios.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-moto.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-moto.md)
