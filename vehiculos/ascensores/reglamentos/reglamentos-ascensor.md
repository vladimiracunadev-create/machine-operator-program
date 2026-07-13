# ⚖️ Reglamentos del ascensor (Chile)

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseno de simulacion. Las normas reales cambian; para
instalar, mantener o inspeccionar se debe consultar la autoridad y la normativa
vigente. El ascensor es maquinaria fija: **no** circula por via publica ni
requiere licencia de conducir. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), seccion
1.8 (ascensores).

## Ambito

- Pais: Chile.
- Ley base: Ley 20.296 (instalacion, mantencion e inspeccion de ascensores y
  similares).
- Norma complementaria: Ordenanza General de Urbanismo y Construcciones (OGUC).
- Autoridad: municipalidades (Direccion de Obras) fiscalizan; organismos y
  empresas autorizadas certifican y mantienen.
- Tipo de vehiculo: transporte vertical fijo.

## Habilitacion, mantencion e inspeccion

- No se necesita licencia de conducir: el ascensor no circula por via publica.
- La instalacion y la mantencion las realiza personal **competente** de empresas
  autorizadas.
- La mantencion es **periodica** y obligatoria.
- La **certificacion** la emite un organismo autorizado.
- La fiscalizacion recae en la municipalidad (Direccion de Obras).
- Los plazos y detalles exactos estan por confirmar (ver marco legal).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Mantencion periodica | Ley 20.296 | Mantencion por empresa competente. | Modo mantencion en el escenario. |
| Certificacion | Ley 20.296 | Certificado por organismo autorizado. | Estado certificado del equipo. |
| Fiscalizacion | Ley 20.296 / OGUC | Control municipal. | Chequeo de vigencia simulado. |
| Freno de seguridad | Normativa tecnica | Gobernador y paracaidas operativos. | Modelo de proteccion ante exceso. |
| Sobrecarga | Normativa tecnica | Impedir marcha sobrecargado. | Bloqueo por sobrecarga. |
| Accesibilidad | OGUC | Braille, voz y espacio adecuado. | Interfaz accesible del escenario. |

## Reglas de seguridad

- Cumplir la mantencion periodica y conservar la certificacion vigente.
- No usar el ascensor fuera de servicio ni forzar las puertas.
- Respetar la carga maxima indicada en la cabina.
- Mantener operativos alarma e intercomunicador.
- Ante emergencia del edificio (incendio), usar la escalera segun senalizacion.

## Restricciones

- No circula por via publica: sin licencia de conducir.
- Operacion y mantencion segun manual del fabricante y personal competente.
- Modo inspeccion solo para tecnicos autorizados.

## Notas para simulacion

- El nucleo educativo es la seguridad: contrapeso, freno de seguridad y sobrecarga.
- Modelar mantencion, certificacion y estado de servicio como parte del escenario.
- Marcar como "(por confirmar)" los plazos exactos de mantencion e inspeccion.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-ascensor.md) · [➡️ Siguiente: Diseno de simulacion](../simulacion/diseno-simulador-ascensor.md)
