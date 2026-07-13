# Reglamentos: grua (Chile)

Referencia educativa y de diseno de simulacion. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ambito

- Pais: Chile.
- Ley base: Ley 18.290 (Ley de Transito) para circulacion; normativa laboral y
  de seguridad para la operacion como maquinaria.
- Autoridad: MTT y municipalidades (transito); Direccion del Trabajo y mutuales
  (seguridad laboral); Direccion de Vialidad MOP (cargas sobredimensionadas).
- Tipo de vehiculo: grua / maquinaria automotriz autopropulsada.

## Licencia

- Clase **D** (especial) para maquinaria automotriz, Ley 18.290 Art. 12.
- Edad minima: 18 anos.
- El examen practico se rinde sobre la maquinaria especifica a operar.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Licencia de maquinaria | Ley 18.290, Art. 12 | Clase D para operar la grua. | Modo licencia por tipo de maquina. |
| Circulacion en via publica | Ley 18.290 | Cumplir senalizacion y limites. | Reglas de transito al desplazarse. |
| Cargas anchas o pesadas | Direccion de Vialidad (MOP) | Autorizacion y senalizacion especial. | Escenario de transporte especial. |
| Seguridad de izaje | Normativa laboral y de prevencion | Limites de carga, radios, estabilidad. | Modelo de estabilidad y momento de carga. |

## Reglas de seguridad

- Verificar tablas de carga, radio y contrapeso antes de izar.
- Nivelar y estabilizar la maquina (estabilizadores) antes de operar.
- Delimitar el area de trabajo y controlar la presencia de personas.
- No exceder los limites de carga segun el angulo y el alcance.

## Restricciones

- Licencia especial clase D.
- Operacion segun manual del fabricante y limites de la maquina.
- Permisos adicionales para circular con sobredimension.

## Notas para simulacion

- El nucleo educativo es la estabilidad: momento de carga, radio y contrapeso.
- Modelar el area de exclusion y la senalizacion.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).
