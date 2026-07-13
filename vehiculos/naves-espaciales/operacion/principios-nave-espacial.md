# 🧪 Principios y operacion de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🧪 Principios

Documento general y educativo. Describe como se opera una nave espacial en
simulacion y que principios fisicos conviene representar, distinguiendo siempre la
ciencia real de la ficcion.

## Principios de funcionamiento

- **Propulsion por reaccion**: la nave avanza expulsando masa; vale la tercera ley
  de Newton y **no** necesita aire.
- **Orbita**: estar en orbita es caer de forma continua alrededor de la Tierra sin
  chocar, porque se avanza lo bastante rapido de lado.
- **Microgravedad**: en caida libre todo "flota"; no es ausencia de gravedad.
- **Delta-v**: cada maniobra gasta un presupuesto limitado de cambio de velocidad.
- **Reentrada**: al volver, la friccion con el aire genera calor; el escudo protege.

## La orbita en una idea

```mermaid
flowchart LR
    Lanza[Lanzar rapido de lado] --> Cae[La nave cae hacia la Tierra]
    Cae --> Curva[La Tierra se curva bajo la nave]
    Curva --> Orbita[Cae sin tocar el suelo: orbita]
```

Si se lanza un objeto lo bastante rapido en horizontal, cae hacia la Tierra pero
la superficie se curva a la misma tasa: nunca llega al suelo. Eso es una orbita.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Prelanzamiento | Revision y cuenta atras | Checklist, propelente, sistemas vitales. |
| Lanzamiento | Despegue con gran empuje | Vencer gravedad y atmosfera densa. |
| Ascenso y etapas | Ganar velocidad orbital | Separar etapas al agotarse. |
| Insercion orbital | Alcanzar orbita estable | Velocidad de lado suficiente. |
| Operacion en orbita | Cumplir la mision | Maniobras, acoplamiento, ciencia. |
| Desorbitacion | Salir de la orbita | Frenar con el motor en el momento justo. |
| Reentrada | Volver a la atmosfera | Orientar el escudo, soportar el calor. |
| Aterrizaje / amerizaje | Tocar tierra o mar | Paracaidas o descenso propulsado. |

## Maniobra orbital: idea general

1. Toda maniobra cambia la orbita gastando **delta-v**.
2. Encender el motor a favor del movimiento sube la orbita opuesta.
3. Encenderlo en contra la baja; asi se frena para reentrar.
4. El momento (donde en la orbita) importa tanto como la cantidad.
5. Sin propelente no hay maniobra: se planifica el presupuesto.

## Errores comunes que la simulacion puede ensenar a evitar

- Pensar que en orbita "no hay gravedad" en vez de caida libre.
- Gastar todo el delta-v sin reserva para volver.
- Reentrar con mala orientacion del escudo termico.
- Ignorar el consumo de aire, agua y energia en misiones largas.
- Confundir capacidades reales con recursos de ficcion.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: lanzar, llegar a orbita y reentrar de forma guiada.
- **Nivel 2 (simplificado)**: agregar delta-v, orbitas y microgravedad.
- **Nivel 3 (tecnico)**: sumar planificacion de maniobras, acoplamiento y recursos.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-nave-espacial.md) · [➡️ Siguiente: Entornos de trabajo](entornos-nave-espacial.md)
