# ⚖️ Reglamentos de la Formula 1 (FIA)

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Formula 1](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseno de simulacion. La Formula 1 **no** se rige por
la ley de transito: es una competicion regulada por la FIA. Las normas cambian
cada temporada; para datos oficiales hay que consultar el reglamento vigente.
Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), seccion
1.9 (Formula 1).

## Ambito

- Tipo de vehiculo: monoplaza de competicion, no circula por via publica.
- Autoridad: FIA (Federacion Internacional del Automovil).
- No requiere licencia de conducir comun: exige una superlicencia deportiva de
  la FIA para pilotar en el campeonato.
- En Chile, el automovilismo deportivo se organiza por la federacion nacional del
  automovilismo.

## Los dos reglamentos

| Reglamento | Que regula | Ejemplos |
| --- | --- | --- |
| Deportivo | Como se compite | Formato de fin de semana, puntos, banderas, penalizaciones. |
| Tecnico | Como es el coche | Dimensiones, peso minimo, unidad de potencia, seguridad. |

## Reglamento deportivo (resumen educativo)

- **Formato**: entrenamientos, clasificacion y carrera.
- **Banderas**: comunican estado de pista (peligro, adelantamiento, fin).
- **Coche de seguridad**: neutraliza la carrera ante un incidente.
- **Penalizaciones**: por tiempo o posiciones ante infracciones.
- **Parque cerrado**: limita los cambios al coche tras la clasificacion.

## Reglamento tecnico (resumen educativo)

| Tema | Idea general | Aplicacion en simulacion |
| --- | --- | --- |
| Peso minimo | El coche no puede bajar de un peso definido. | Parametro fijo del modelo. |
| Unidad de potencia | Numero de componentes limitado por temporada. | Gestion de fiabilidad. |
| Aerodinamica | Superficies y fondo dentro de un reglamento. | Reglaje de carga acotado. |
| Seguridad | Monocasco, halo, pruebas de choque. | Contexto de proteccion del piloto. |
| Combustible | Cantidad y flujo maximos regulados. | Gestion de consumo por vuelta. |

## Seguridad del piloto

- Monocasco de carbono, cinturones de seguridad y sistema HANS.
- Arco de proteccion halo sobre la cabeza.
- Casco homologado y traje ignifugo.
- Barreras, escapatorias y sistemas de extraccion en el circuito.

## Notas para simulacion

- Representar banderas y coche de seguridad como reglas del escenario.
- Usar penalizaciones educativas (avisos, tiempo) en vez de castigos frustrantes.
- Modelar limites tecnicos como parametros (peso, energia, consumo).
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-formula-1.md) · [➡️ Siguiente: Diseno de simulacion](../simulacion/diseno-simulador-formula-1.md)
