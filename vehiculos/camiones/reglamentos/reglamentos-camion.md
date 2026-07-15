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

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-camion.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-camion.md)
