# 🧪 Principios y operacion de la estacion espacial

[🏠 Inicio](../../../README.md) · [🛰️ Curso: Estacion espacial (ISS)](../README.md) · 🧪 Principios

Documento general y educativo. Describe como se opera una estacion espacial en
simulacion y que principios fisicos conviene representar. Todo es **ciencia
real**: la microgravedad y la orbita se modelan con rigor.

## Principios de funcionamiento

- **Orbita baja**: la estacion cae de forma continua alrededor de la Tierra a unos
  400 km de altura (aproximado), dando una vuelta en poco mas de una hora y media.
- **Microgravedad**: no es ausencia de gravedad, sino caida libre; por eso todo
  flota dentro de la estacion.
- **Ciclo de luz y sombra**: en cada vuelta la estacion pasa por dia y noche, lo
  que obliga a guardar energia en baterias.
- **Rozamiento residual**: el aire muy tenue a esa altura frena poco a poco la
  estacion, que debe elevar su orbita cada cierto tiempo.
- **Soporte vital de ciclo cerrado**: aire y agua se reciclan porque reabastecer
  desde la Tierra es caro y lento.

## La microgravedad en una idea

```mermaid
flowchart LR
    Cae[La estacion cae hacia la Tierra] --> Avanza[Pero avanza muy rapido de lado]
    Avanza --> Curva[La Tierra se curva bajo ella]
    Curva --> Orbita[Cae sin tocar el suelo: orbita]
    Orbita --> Flota[Todo dentro cae igual y parece flotar]
```

La tripulacion no flota porque "no haya gravedad", sino porque la estacion y todo
lo que hay dentro caen juntos en la misma orbita.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Operacion diaria | Ciencia y vida a bordo | Rutina, ejercicio, mantenimiento. |
| Acoplamiento | Llega una nave | Aproximacion lenta, captura o acople. |
| Reabastecimiento | Traspaso de carga | Agua, aire, comida, equipos. |
| Caminata espacial | Trabajo en el exterior | Traje, esclusa, sujeciones. |
| Ajuste de orbita | Elevar la altura | Empuje de una nave acoplada. |
| Relevo de tripulacion | Cambio de personas | Traspaso de tareas y despedida de la nave. |

## Vida en microgravedad: idea general

1. Todo debe sujetarse: objetos, personas y liquidos flotan.
2. El agua no cae; se maneja con cuidado para no danar equipos.
3. El cuerpo pierde musculo y hueso, por eso se hace ejercicio a diario.
4. Dormir es amarrarse a un saco para no chocar con las paredes.
5. Cada tarea usa asideros y anclajes para trabajar sin flotar a la deriva.

## Errores comunes que la simulacion puede ensenar a evitar

- Pensar que en orbita "no hay gravedad" en vez de caida libre.
- Olvidar que la estacion pierde altura y necesita reimpulso.
- No administrar la energia en la fase de sombra.
- Descuidar el reciclaje de aire y agua en misiones largas.
- Aproximar una nave demasiado rapido al acoplar.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: entender la vida a bordo y la microgravedad de forma guiada.
- **Nivel 2 (simplificado)**: agregar energia solar, ciclo de sombra y recursos vitales.
- **Nivel 3 (tecnico)**: sumar acoplamiento preciso, reimpulso de orbita y EVA.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-estacion-espacial.md) · [➡️ Siguiente: Entornos de trabajo](entornos-estacion-espacial.md)
