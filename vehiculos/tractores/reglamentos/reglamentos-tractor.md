# ⚖️ Reglamentos del tractor (Chile)

[🏠 Inicio](../../../README.md) · [🚜 Curso: Tractores](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
circular se deben consultar la autoridad de tránsito y la ley vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito) para la circulación en vía pública;
  normativa laboral y de prevención para el trabajo agrícola.
- Autoridad: MTT y municipalidades (tránsito y licencias); Carabineros
  (fiscalización); mutuales y Dirección del Trabajo (seguridad laboral).
- Tipo de vehículo: tractor agrícola, maquinaria automotriz autopropulsada.

## Licencia

- Clase **D** (especial) para maquinaria automotriz, Ley 18.290 Art. 12.
- La clase D habilita para operar tractores, grúas, cargadores,
  retroexcavadoras y maquinaria similar.
- Edad mínima: 18 años (Art. 13).
- El examen práctico se rinde sobre el tipo de maquinaria a operar.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Licencia de maquinaria | Ley 18.290, Art. 12 | Clase D para operar el tractor. | Modo licencia por tipo de máquina. |
| Estructura antivuelco (ROPS) | Normativa de prevención laboral | Arco o cabina de protección contra vuelco. | Estado del ROPS y del cinturón. |
| Cinturón de seguridad | Prevención y Ley 18.290 | Obligatorio dentro del ROPS. | Chequeo previo simulado. |
| Protector de la PTO | Normativa de prevención | Cubierta del eje de toma de fuerza. | Bloqueo si falta el protector. |
| Circulación en vía pública | Ley 18.290 | Luces, señalización y velocidad reducida. | Reglas de tránsito al trasladarse. |
| Traslado de aperos | Ley 18.290 y Vialidad | Señalización de carga ancha o larga. | Escenario de traslado por camino. |

## Documentos obligatorios

| Documento | Para que sirve |
| --- | --- |
| Licencia clase D | Habilita para operar maquinaria automotriz. |
| Padrón | Acredita inscripción del vehículo, si circula por vía pública. |
| Permiso de circulación | Requerido para circular por caminos públicos. |
| SOAP | Seguro obligatorio de accidentes personales para vía pública. |
| Registro de mantenimiento | Respalda el estado seguro de la máquina. |

## Reglas de seguridad

- Operar siempre con la estructura antivuelco (ROPS) y el cinturón puesto.
- Mantener el protector de la PTO y nunca acercarse con el eje en marcha.
- Subir y bajar pendientes en línea recta, evitando giros bruscos.
- Enganchar el tiro desde la barra baja, nunca por encima del eje trasero.
- Señalizar y usar luces al circular por camino público.
- Impedir que otras personas suban o esten cerca durante el trabajo.

## Restricciones

- Licencia especial clase D.
- Velocidad reducida en vía pública y prioridad a la señalización.
- El traslado de aperos anchos o largos requiere señalización especial.

## Notas para simulación

- El núcleo educativo es la estabilidad y la seguridad con la PTO.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar el vuelco en pendiente y el atrapamiento de la PTO como riesgos claros.
- Registrar cada norma usada en
  [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tractor.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tractor.md)
