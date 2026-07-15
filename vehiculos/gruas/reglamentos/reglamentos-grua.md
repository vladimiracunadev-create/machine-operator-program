# ⚖️ Reglamentos de la grúa (Chile)

[🏠 Inicio](../../../README.md) · [🏗️ Curso: Grúas](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito) para circulación; normativa laboral y
  de seguridad para la operación como maquinaria.
- Autoridad: MTT y municipalidades (tránsito); Dirección del Trabajo y mutuales
  (seguridad laboral); Dirección de Vialidad MOP (cargas sobredimensionadas).
- Tipo de vehículo: grúa / maquinaria automotriz autopropulsada.

## Licencia

- Clase **D** (especial) para maquinaria automotriz, Ley 18.290 Art. 12.
- Edad mínima: 18 años.
- El examen práctico se rinde sobre la maquinaria específica a operar.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Licencia de maquinaria | Ley 18.290, Art. 12 | Clase D para operar la grúa. | Modo licencia por tipo de máquina. |
| Circulación en vía pública | Ley 18.290 | Cumplir señalización y límites. | Reglas de tránsito al desplazarse. |
| Cargas anchas o pesadas | Dirección de Vialidad (MOP) | Autorización y señalización especial. | Escenario de transporte especial. |
| Seguridad de izaje | Normativa laboral y de prevención | Límites de carga, radios, estabilidad. | Modelo de estabilidad y momento de carga. |

## Reglas de seguridad

- Verificar tablas de carga, radio y contrapeso antes de izar.
- Nivelar y estabilizar la máquina (estabilizadores) antes de operar.
- Delimitar el área de trabajo y controlar la presencia de personas.
- No exceder los límites de carga según el ángulo y el alcance.

## Restricciones

- Licencia especial clase D.
- Operación según manual del fabricante y límites de la máquina.
- Permisos adicionales para circular con sobredimensión.

## Notas para simulación

- El núcleo educativo es la estabilidad: momento de carga, radio y contrapeso.
- Modelar el área de exclusión y la señalización.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-grua.md)
