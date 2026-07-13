# 🧪 Principios y operacion del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🧪 Principios

Documento general y educativo. Describe como se opera un transbordador en
simulacion y que principios fisicos conviene representar. Todo es **ciencia
real**: la fisica del ascenso, la orbita y el planeo se modela con rigor.

## Principios de funcionamiento

- **Despegue de cohete**: propulsores y motores dan el empuje para vencer la
  gravedad y ganar velocidad orbital.
- **Vuelo orbital**: en orbita la nave cae de forma continua alrededor de la
  Tierra; la tripulacion y los objetos flotan en microgravedad.
- **Reentrada**: al frenar y bajar, el aire genera un calor enorme; el escudo
  termico protege la estructura y la orientacion debe ser exacta.
- **Planeo sin motor**: en el descenso final la nave no tiene empuje, solo la
  aerodinamica de sus alas. Cada aterrizaje es un unico intento.
- **Energia del descenso**: la altura y la velocidad son el "combustible" del
  planeo; hay que administrarlas para llegar a la pista.

## La reentrada en una idea

```mermaid
flowchart LR
    Frena[Encender motor a contramano] --> Baja[La nave baja de la orbita]
    Baja --> Aire[Encuentra aire cada vez mas denso]
    Aire --> Calor[El roce genera calor]
    Calor --> Escudo[El escudo protege por delante]
    Escudo --> Planeo[La nave planea a la pista]
```

Reingresar no es "caer": la nave llega muy rapido y debe frenar contra el aire de
forma controlada, con el escudo al frente y un angulo correcto, ni muy plano ni
muy pronunciado.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Prelanzamiento | Revision y cuenta atras | Checklist, propelente, clima. |
| Despegue | Subida con propulsores | Empuje mayor que el peso. |
| Ascenso y separacion | Soltar propulsores y tanque | Momento justo de cada separacion. |
| Orbita | Cumplir la mision | Desplegar carga, ciencia, acoplar. |
| Desorbitacion | Frenar para volver | Encender motor en el punto correcto. |
| Reentrada | Regreso con calor | Escudo por delante, angulo correcto. |
| Planeo y aterrizaje | Descenso sin motor | Administrar altura y velocidad. |

## Aterrizaje sin motor: idea general

1. La nave llega a la atmosfera con mucha energia de altura y velocidad.
2. Las alas generan sustentacion cuando el aire es denso.
3. Se controla el planeo con palanca y timones, sin empuje.
4. Se administra la energia para no quedar corto ni largo de la pista.
5. Se despliega el tren y se frena, con un unico intento.

## Errores comunes que la simulacion puede ensenar a evitar

- Reingresar con el escudo mal orientado.
- Elegir un angulo de reentrada muy plano (rebota) o muy pronunciado (calor extremo).
- Gastar la energia del planeo demasiado pronto y no llegar a la pista.
- Olvidar desplegar el tren de aterrizaje a tiempo.
- Pensar que se puede "acelerar" en el descenso final, cuando no hay motor.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: despegar, orbitar y aterrizar de forma guiada.
- **Nivel 2 (simplificado)**: agregar orbita, angulo de reentrada y planeo.
- **Nivel 3 (tecnico)**: sumar separaciones, gestion de energia y aterrizaje de un solo intento.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-transbordador.md) · [➡️ Siguiente: Entornos de trabajo](entornos-transbordador.md)
