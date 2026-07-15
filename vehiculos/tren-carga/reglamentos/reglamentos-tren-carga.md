# ⚖️ Reglamentos del tren de carga (Chile)

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad ferroviaria y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección 1.6 (Ferroviario).

## Ámbito

- País: Chile.
- Ley base: Ley General de Ferrocarriles (número y fecha por confirmar).
- Autoridad: EFE como dueño de la infraestructura y operador estatal histórico, y
  MTT en el rol regulador del sector.
- Tipo de vehículo: tren de carga sobre la red ferroviaria.

## Habilitación y certificación del maquinista

El ferrocarril no usa una licencia de vía pública como los vehículos de carretera,
porque no circula por caminos abiertos sino sobre una vía férrea controlada. En su
lugar se exige la **habilitación o certificación de maquinista** (requisitos exactos
por confirmar), otorgada según la normativa del sector y del operador.

- No hay licencia de conducir de vía pública para el tren.
- El maquinista requiere habilitación o certificación específica (por confirmar).
- Los operadores de carga privados que usan la red operan sobre la infraestructura
  de EFE (régimen y nombres por confirmar).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Habilitación de maquinista | Marco ferroviario (por confirmar) | Certificación vigente para conducir. | Modo habilitación antes de operar. |
| Carga por eje | Marco ferroviario (por confirmar) | No exceder el peso por eje que admite la vía. | Control de carga y reparto por eje. |
| Señalización de vía | Marco ferroviario (por confirmar) | Obedecer señales de circulación y velocidad. | Reglas de señal en el escenario. |
| Pasos a nivel | Marco ferroviario (por confirmar) | Bocina y prioridad según la señalización. | Advertencia sonora obligatoria. |
| Freno del tren | Marco ferroviario (por confirmar) | Tubería de freno operativa en toda la composición. | Chequeo previo simulado de freno. |
| Ancho de vía / trocha | Marco ferroviario (por confirmar) | Material compatible con la trocha de la ruta. | Coherencia de trocha en el escenario. |

## Reglas de seguridad

- Verificar la presión de la tubería de freno antes de mover el tren.
- Respetar el peso por eje y el reparto de carga que admite la vía.
- Obedecer siempre la señalización y los límites de velocidad de la vía.
- Usar bocina y máxima atención al aproximarse a un paso a nivel.
- Anticipar la larga distancia de frenado por la gran masa del tren.

## Restricciones

- Habilitación o certificación de maquinista vigente (por confirmar).
- Circulación sujeta a la señalización y a la gestión de la vía.
- Cargas o composiciones especiales requieren autorización del operador y de EFE
  (por confirmar).

## Notas para simulación

- El núcleo educativo es la gestión de masa: distancia de frenado, adherencia y
  fuerzas longitudinales del tren.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar la baja presión de la tubería de freno como condición que impide circular.
- Citar solo números de ley confirmados en `docs/07-marco-legal-chile.md`; el resto
  se marca como por confirmar. Fuente institucional: efe.cl.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-carga.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tren-carga.md)
