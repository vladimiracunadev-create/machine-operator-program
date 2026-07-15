# 🧪 Principios y operación de la estación espacial

[🏠 Inicio](../../../README.md) · [🛰️ Curso: Estación espacial (ISS)](../README.md) · 🧪 Principios

Documento general y educativo. Describe cómo se opera una estación espacial en
simulación y que principios físicos conviene representar. Todo es **ciencia
real**: la microgravedad y la órbita se modelan con rigor.

## Principios de funcionamiento

- **Órbita baja**: la estación cae de forma continua alrededor de la Tierra a unos
  400 km de altura (aproximado), dando una vuelta en poco más de una hora y media.
- **Microgravedad**: no es ausencia de gravedad, sino caída libre; por eso todo
  flota dentro de la estación.
- **Ciclo de luz y sombra**: en cada vuelta la estación pasa por día y noche, lo
  que obliga a guardar energía en baterías.
- **Rozamiento residual**: el aire muy tenue a esa altura frena poco a poco la
  estación, que debe elevar su órbita cada cierto tiempo.
- **Soporte vital de ciclo cerrado**: aire y agua se reciclan porque reabastecer
  desde la Tierra es caro y lento.

## La microgravedad en una idea

```mermaid
flowchart LR
    Cae[La estación cae hacia la Tierra] --> Avanza[Pero avanza muy rápido de lado]
    Avanza --> Curva[La Tierra se curva bajo ella]
    Curva --> Orbita[Cae sin tocar el suelo: órbita]
    Orbita --> Flota[Todo dentro cae igual y parece flotar]
```

La tripulación no flota porque "no haya gravedad", sino porque la estación y todo
lo que hay dentro caen juntos en la misma órbita.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Operación diaria | Ciencia y vida a bordo | Rutina, ejercicio, mantenimiento. |
| Acoplamiento | Llega una nave | Aproximación lenta, captura o acople. |
| Reabastecimiento | Traspaso de carga | Agua, aire, comida, equipos. |
| Caminata espacial | Trabajo en el exterior | Traje, esclusa, sujeciones. |
| Ajuste de órbita | Elevar la altura | Empuje de una nave acoplada. |
| Relevo de tripulación | Cambio de personas | Traspaso de tareas y despedida de la nave. |

## Vida en microgravedad: idea general

1. Todo debe sujetarse: objetos, personas y líquidos flotan.
2. El agua no cae; se maneja con cuidado para no dañar equipos.
3. El cuerpo pierde músculo y hueso, por eso se hace ejercicio a diario.
4. Dormir es amarrarse a un saco para no chocar con las paredes.
5. Cada tarea usa asideros y anclajes para trabajar sin flotar a la deriva.

## Errores comunes que la simulación puede enseñar a evitar

- Pensar que en órbita "no hay gravedad" en vez de caída libre.
- Olvidar que la estación pierde altura y necesita reimpulso.
- No administrar la energía en la fase de sombra.
- Descuidar el reciclaje de aire y agua en misiones largas.
- Aproximar una nave demasiado rápido al acoplar.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: entender la vida a bordo y la microgravedad de forma guiada.
- **Nivel 2 (simplificado)**: agregar energía solar, ciclo de sombra y recursos vitales.
- **Nivel 3 (técnico)**: sumar acoplamiento preciso, reimpulso de órbita y EVA.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-estacion-espacial.md) · [➡️ Siguiente: Entornos de trabajo](entornos-estacion-espacial.md)
