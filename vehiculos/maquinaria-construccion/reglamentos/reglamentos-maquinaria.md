---
tipo_documento: clase
clase: 8
codigo: MAQUINARIACO-08
curso: maquinaria-construccion
titulo: "Reglamentos de la maquinaria de construcción (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: MAQUINARIACO-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Maquinaria de construcción."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Maquinaria de construcción."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos de la maquinaria de construcción (Chile)

[🏠 Inicio](../../../README.md) · [🚧 Curso: Maquinaria de construcción](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar y circular se deben consultar la autoridad de tránsito y la ley vigente.
Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito) para la circulación; normativa laboral y
  de prevención de riesgos para la operación en faena.
- Autoridad: MTT y municipalidades (tránsito y licencias); Carabineros
  (fiscalización); Dirección del Trabajo y mutuales (seguridad laboral).
- Tipo de vehículo: maquinaria automotriz de construcción autopropulsada.

## Licencia

- Clase **D** (especial) para maquinaria automotriz, Ley 18.290 Art. 12.
- La clase D habilita para operar cargadores, retroexcavadoras, excavadoras,
  bulldozer, motoniveladoras y maquinaria similar.
- Edad mínima: 18 años (Art. 13).
- El examen práctico se rinde sobre el tipo de maquinaria a operar.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Licencia de maquinaria | Ley 18.290, Art. 12 | Clase D para operar la máquina. | Modo licencia por tipo de máquina. |
| Estructura ROPS/FOPS | Normativa de prevención laboral | Protección contra vuelco y caída de objetos. | Estado de la cabina y cinturón. |
| Zona de exclusión | Normativa de prevención | Radio de trabajo sin personas. | Modelo de radio y presencia de personas. |
| Señalización de faena | Normativa laboral y de obra | Señaleros, barreras y alarmas. | Escenario de faena con señaleros. |
| Circulación en vía pública | Ley 18.290 | Traslado con señalización y velocidad reducida. | Reglas de tránsito al trasladarse. |
| Transporte de la máquina | Ley 18.290 y Vialidad | Traslado en camión cama baja si procede. | Escenario de traslado entre faenas. |

## Documentos obligatorios

| Documento | Para que sirve |
| --- | --- |
| Licencia clase D | Habilita para operar maquinaria automotriz. |
| Registro de operador | Respalda la capacitación en la máquina específica. |
| Mantenimiento al día | Acredita el estado seguro de la máquina. |
| Permiso de circulación y SOAP | Requeridos si la máquina circula por vía pública. |
| Plan de prevención de la obra | Define las reglas de seguridad de la faena. |

## Reglas de seguridad

- Operar siempre con la cabina ROPS/FOPS y el cinturón puesto.
- Mantener el radio de trabajo como zona de exclusión sin personas.
- Bloquear los mandos hidráulicos al subir o bajar de la cabina.
- Trabajar sobre terreno nivelado y firme; vigilar taludes y el vuelco.
- Usar bocina y alarma de retroceso y apoyarse en señaleros.
- Coordinar el movimiento con camiones y otras máquinas de la faena.

## Restricciones

- Licencia especial clase D.
- Operación según el manual del fabricante y los límites de la máquina.
- Circulación o traslado por vía pública con señalización y autorización.

## Notas para simulación

- El núcleo educativo es la estabilidad frente al vuelco y la zona de exclusión.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar el radio de trabajo, la presencia de personas y el límite de vuelco.
- Registrar cada norma usada en
  [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Maquinaria de construcción; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CONSTRUCTION](https://www.osha.gov/construction): Construction Industry, OSHA. Uso: maquinaria y seguridad de obra.
- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-maquinaria.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-maquinaria.md)
