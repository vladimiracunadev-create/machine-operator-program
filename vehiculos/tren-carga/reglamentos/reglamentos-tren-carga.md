# ⚖️ Reglamentos del tren de carga (Chile)

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseno de simulacion. Las normas reales cambian; para
operar se deben consultar la autoridad ferroviaria y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), seccion 1.6 (Ferroviario).

## Ambito

- Pais: Chile.
- Ley base: Ley General de Ferrocarriles (numero y fecha por confirmar).
- Autoridad: EFE como dueno de la infraestructura y operador estatal historico, y
  MTT en el rol regulador del sector.
- Tipo de vehiculo: tren de carga sobre la red ferroviaria.

## Habilitacion y certificacion del maquinista

El ferrocarril no usa una licencia de via publica como los vehiculos de carretera,
porque no circula por caminos abiertos sino sobre una via ferrea controlada. En su
lugar se exige la **habilitacion o certificacion de maquinista** (requisitos exactos
por confirmar), otorgada segun la normativa del sector y del operador.

- No hay licencia de conducir de via publica para el tren.
- El maquinista requiere habilitacion o certificacion especifica (por confirmar).
- Los operadores de carga privados que usan la red operan sobre la infraestructura
  de EFE (regimen y nombres por confirmar).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Habilitacion de maquinista | Marco ferroviario (por confirmar) | Certificacion vigente para conducir. | Modo habilitacion antes de operar. |
| Carga por eje | Marco ferroviario (por confirmar) | No exceder el peso por eje que admite la via. | Control de carga y reparto por eje. |
| Senalizacion de via | Marco ferroviario (por confirmar) | Obedecer senales de circulacion y velocidad. | Reglas de senal en el escenario. |
| Pasos a nivel | Marco ferroviario (por confirmar) | Bocina y prioridad segun la senalizacion. | Advertencia sonora obligatoria. |
| Freno del tren | Marco ferroviario (por confirmar) | Tuberia de freno operativa en toda la composicion. | Chequeo previo simulado de freno. |
| Ancho de via / trocha | Marco ferroviario (por confirmar) | Material compatible con la trocha de la ruta. | Coherencia de trocha en el escenario. |

## Reglas de seguridad

- Verificar la presion de la tuberia de freno antes de mover el tren.
- Respetar el peso por eje y el reparto de carga que admite la via.
- Obedecer siempre la senalizacion y los limites de velocidad de la via.
- Usar bocina y maxima atencion al aproximarse a un paso a nivel.
- Anticipar la larga distancia de frenado por la gran masa del tren.

## Restricciones

- Habilitacion o certificacion de maquinista vigente (por confirmar).
- Circulacion sujeta a la senalizacion y a la gestion de la via.
- Cargas o composiciones especiales requieren autorizacion del operador y de EFE
  (por confirmar).

## Notas para simulacion

- El nucleo educativo es la gestion de masa: distancia de frenado, adherencia y
  fuerzas longitudinales del tren.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar la baja presion de la tuberia de freno como condicion que impide circular.
- Citar solo numeros de ley confirmados en `docs/07-marco-legal-chile.md`; el resto
  se marca como por confirmar. Fuente institucional: efe.cl.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-carga.md) · [➡️ Siguiente: Diseno de simulacion](../simulacion/diseno-simulador-tren-carga.md)
