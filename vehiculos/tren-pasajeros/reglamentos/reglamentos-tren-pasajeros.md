# ⚖️ Reglamentos del tren de pasajeros (Chile)

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseno de simulacion. Las normas reales cambian; para
operar se deben consultar la autoridad de transporte y la ley vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
seccion 1.6 (Ferroviario).

## Ambito

- Pais: Chile.
- Ley base: Ley General de Ferrocarriles (numero y fecha por confirmar).
- Operador estatal historico: Empresa de los Ferrocarriles del Estado (EFE).
- Autoridad reguladora: Ministerio de Transportes (MTT).
- Tipo de vehiculo: tren de pasajeros sobre red ferroviaria.

## Habilitacion del personal de conduccion

A diferencia de un vehiculo de via publica, el tren **no** se opera con una
licencia de conducir comun. El personal de conduccion, el maquinista, requiere
una **habilitacion o certificacion especifica del operador** ferroviario.

- No aplica licencia de conducir de via publica (clases A, B o C).
- La habilitacion la define el operador (EFE) segun su normativa interna.
- El regimen exacto de habilitacion de maquinistas queda **por confirmar** en la
  fuente oficial.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Marco ferroviario | Ley General de Ferrocarriles (por confirmar) | Base legal del transporte por ferrocarril. | Reglas generales del escenario. |
| Habilitacion del maquinista | Certificacion del operador (por confirmar) | Personal de conduccion habilitado por EFE. | Requisito previo antes de operar. |
| Senalizacion y ATP | Normativa del sector (por confirmar) | Respetar senales y limites del ATP. | Control de velocidad por senal. |
| Pasos a nivel | Normativa del sector (por confirmar) | Advertir y proteger cruces con carretera. | Escenarios de paso a nivel. |
| Ancho de via | Estandar de la red (por confirmar) | Trocha compatible con el material. | Parametro fijo del escenario. |

## Reglas de seguridad

- Operar solo con habilitacion vigente del operador.
- Respetar en todo momento las senales de via y los limites del ATP.
- Advertir con el silbato en pasos a nivel y al aproximarse a andenes.
- Verificar la presion de freno y el enclavamiento de puertas antes de arrancar.
- Comunicar por radio cualquier incidencia al puesto de control.

## Restricciones

- Circulacion solo por vias autorizadas y segun el horario del servicio.
- Velocidad limitada por la senalizacion y el ATP de cada tramo.
- Distancias minimas entre trenes garantizadas por el bloqueo por tramos.

## Notas para simulacion

- Modelar senales, ATP, pasos a nivel y paradas en anden.
- Representar la habilitacion del maquinista como requisito previo del escenario.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Enlazar el marco a [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md)
  seccion 1.6 y a los datos por reconfirmar. Fuente institucional: efe.cl.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-pasajeros.md) · [➡️ Siguiente: Diseno de simulacion](../simulacion/diseno-simulador-tren-pasajeros.md)
