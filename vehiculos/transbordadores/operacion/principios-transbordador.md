# 🧪 Principios y operación del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🧪 Principios

Documento general y educativo. Describe cómo se opera un transbordador en
simulación y que principios físicos conviene representar. Todo es **ciencia
real**: la física del ascenso, la órbita y el planeo se modela con rigor.

## Principios de funcionamiento

- **Despegue de cohete**: propulsores y motores dan el empuje para vencer la
  gravedad y ganar velocidad orbital.
- **Vuelo orbital**: en órbita la nave cae de forma continua alrededor de la
  Tierra; la tripulación y los objetos flotan en microgravedad.
- **Reentrada**: al frenar y bajar, el aire genera un calor enorme; el escudo
  térmico protege la estructura y la orientación debe ser exacta.
- **Planeo sin motor**: en el descenso final la nave no tiene empuje, solo la
  aerodinámica de sus alas. Cada aterrizaje es un único intento.
- **Energía del descenso**: la altura y la velocidad son el "combustible" del
  planeo; hay que administrarlas para llegar a la pista.

## La reentrada en una idea

```mermaid
flowchart LR
    Frena[Encender motor a contramano] --> Baja[La nave baja de la órbita]
    Baja --> Aire[Encuentra aire cada vez más denso]
    Aire --> Calor[El roce genera calor]
    Calor --> Escudo[El escudo protege por delante]
    Escudo --> Planeo[La nave planea a la pista]
```

Reingresar no es "caer": la nave llega muy rápido y debe frenar contra el aire de
forma controlada, con el escudo al frente y un ángulo correcto, ni muy plano ni
muy pronunciado.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Prelanzamiento | Revisión y cuenta atrás | Checklist, propelente, clima. |
| Despegue | Subida con propulsores | Empuje mayor que el peso. |
| Ascenso y separación | Soltar propulsores y tanque | Momento justo de cada separación. |
| Órbita | Cumplir la misión | Desplegar carga, ciencia, acoplar. |
| Desorbitación | Frenar para volver | Encender motor en el punto correcto. |
| Reentrada | Regreso con calor | Escudo por delante, ángulo correcto. |
| Planeo y aterrizaje | Descenso sin motor | Administrar altura y velocidad. |

## Aterrizaje sin motor: idea general

1. La nave llega a la atmósfera con mucha energía de altura y velocidad.
2. Las alas generan sustentación cuando el aire es denso.
3. Se controla el planeo con palanca y timones, sin empuje.
4. Se administra la energía para no quedar corto ni largo de la pista.
5. Se despliega el tren y se frena, con un único intento.

## Errores comunes que la simulación puede enseñar a evitar

- Reingresar con el escudo mal orientado.
- Elegir un ángulo de reentrada muy plano (rebota) o muy pronunciado (calor extremo).
- Gastar la energía del planeo demasiado pronto y no llegar a la pista.
- Olvidar desplegar el tren de aterrizaje a tiempo.
- Pensar que se puede "acelerar" en el descenso final, cuando no hay motor.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: despegar, orbitar y aterrizar de forma guiada.
- **Nivel 2 (simplificado)**: agregar órbita, ángulo de reentrada y planeo.
- **Nivel 3 (técnico)**: sumar separaciones, gestión de energía y aterrizaje de un solo intento.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-transbordador.md) · [➡️ Siguiente: Entornos de trabajo](entornos-transbordador.md)
