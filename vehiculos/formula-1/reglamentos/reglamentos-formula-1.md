# ⚖️ Reglamentos de la Fórmula 1 (FIA)

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. La Fórmula 1 **no** se rige por
la ley de tránsito: es una competición regulada por la FIA. Las normas cambian
cada temporada; para datos oficiales hay que consultar el reglamento vigente.
Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección
1.9 (Fórmula 1).

## Ámbito

- Tipo de vehículo: monoplaza de competición, no circula por vía pública.
- Autoridad: FIA (Federación Internacional del Automóvil).
- No requiere licencia de conducir común: exige una superlicencia deportiva de
  la FIA para pilotar en el campeonato.
- En Chile, el automovilismo deportivo se organiza por la federación nacional del
  automovilismo.

## Los dos reglamentos

| Reglamento | Que regula | Ejemplos |
| --- | --- | --- |
| Deportivo | Como se compite | Formato de fin de semana, puntos, banderas, penalizaciones. |
| Técnico | Como es el coche | Dimensiones, peso mínimo, unidad de potencia, seguridad. |

## Reglamento deportivo (resumen educativo)

- **Formato**: entrenamientos, clasificación y carrera.
- **Banderas**: comunican estado de pista (peligro, adelantamiento, fin).
- **Coche de seguridad**: neutraliza la carrera ante un incidente.
- **Penalizaciones**: por tiempo o posiciones ante infracciones.
- **Parque cerrado**: limita los cambios al coche tras la clasificación.

## Reglamento técnico (resumen educativo)

| Tema | Idea general | Aplicación en simulación |
| --- | --- | --- |
| Peso mínimo | El coche no puede bajar de un peso definido. | Parámetro fijo del modelo. |
| Unidad de potencia | Número de componentes limitado por temporada. | Gestión de fiabilidad. |
| Aerodinámica | Superficies y fondo dentro de un reglamento. | Reglaje de carga acotado. |
| Seguridad | Monocasco, halo, pruebas de choque. | Contexto de protección del piloto. |
| Combustible | Cantidad y flujo máximos regulados. | Gestión de consumo por vuelta. |

## Seguridad del piloto

- Monocasco de carbono, cinturones de seguridad y sistema HANS.
- Arco de protección halo sobre la cabeza.
- Casco homologado y traje ignífugo.
- Barreras, escapatorias y sistemas de extracción en el circuito.

## Notas para simulación

- Representar banderas y coche de seguridad como reglas del escenario.
- Usar penalizaciones educativas (avisos, tiempo) en vez de castigos frustrantes.
- Modelar límites técnicos como parámetros (peso, energía, consumo).
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-formula-1.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-formula-1.md)
