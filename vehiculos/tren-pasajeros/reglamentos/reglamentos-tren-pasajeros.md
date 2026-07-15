# ⚖️ Reglamentos del tren de pasajeros (Chile)

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad de transporte y la ley vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
sección 1.6 (Ferroviario).

## Ámbito

- País: Chile.
- Ley base: Ley General de Ferrocarriles (número y fecha por confirmar).
- Operador estatal histórico: Empresa de los Ferrocarriles del Estado (EFE).
- Autoridad reguladora: Ministerio de Transportes (MTT).
- Tipo de vehículo: tren de pasajeros sobre red ferroviaria.

## Habilitación del personal de conducción

A diferencia de un vehículo de vía pública, el tren **no** se opera con una
licencia de conducir común. El personal de conducción, el maquinista, requiere
una **habilitación o certificación específica del operador** ferroviario.

- No aplica licencia de conducir de vía pública (clases A, B o C).
- La habilitación la define el operador (EFE) según su normativa interna.
- El régimen exacto de habilitación de maquinistas queda **por confirmar** en la
  fuente oficial.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Marco ferroviario | Ley General de Ferrocarriles (por confirmar) | Base legal del transporte por ferrocarril. | Reglas generales del escenario. |
| Habilitación del maquinista | Certificación del operador (por confirmar) | Personal de conducción habilitado por EFE. | Requisito previo antes de operar. |
| Señalización y ATP | Normativa del sector (por confirmar) | Respetar señales y límites del ATP. | Control de velocidad por señal. |
| Pasos a nivel | Normativa del sector (por confirmar) | Advertir y proteger cruces con carretera. | Escenarios de paso a nivel. |
| Ancho de vía | Estandar de la red (por confirmar) | Trocha compatible con el material. | Parámetro fijo del escenario. |

## Reglas de seguridad

- Operar solo con habilitación vigente del operador.
- Respetar en todo momento las señales de vía y los límites del ATP.
- Advertir con el silbato en pasos a nivel y al aproximarse a andenes.
- Verificar la presión de freno y el enclavamiento de puertas antes de arrancar.
- Comunicar por radio cualquier incidencia al puesto de control.

## Restricciones

- Circulación solo por vías autorizadas y según el horario del servicio.
- Velocidad limitada por la señalización y el ATP de cada tramo.
- Distancias mínimas entre trenes garantizadas por el bloqueo por tramos.

## Notas para simulación

- Modelar señales, ATP, pasos a nivel y paradas en andén.
- Representar la habilitación del maquinista como requisito previo del escenario.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Enlazar el marco a [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md)
  sección 1.6 y a los datos por reconfirmar. Fuente institucional: efe.cl.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-pasajeros.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tren-pasajeros.md)
