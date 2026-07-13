# 🧪 Principios y operacion de la grua torre

[🏠 Inicio](../../../README.md) · [🗼 Curso: Grua torre](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formacion certificada del operador
ni el manual del fabricante. Describe como se opera una grua torre en simulacion
y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Equilibrio de momentos**: la carga por su radio genera un momento que el
  contrapeso de la contrapluma equilibra sobre el eje de la torre.
- **Estabilidad de la base**: la base anclada y nivelada resiste el vuelco; una
  base mal apoyada o inclinada reduce la seguridad.
- **Momento y radio**: cuanto mas lejos del eje esta el carro, mayor es el
  momento y menor el peso admisible.
- **Limite de viento**: el viento empuja la carga y la estructura; por encima de
  un umbral la grua no puede operar.
- **Control del pendulo**: la carga colgada oscila; el izaje y el giro lentos
  evitan que el pendulo se vuelva peligroso.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Base, cables, limitadores, anemometro, area libre. |
| Puesta en servicio | Habilitar la grua | Nivel correcto, freno de giro, viento bajo el limite. |
| Enganche | Amarrar la carga | Eslingas correctas, senalero listo, radio segura. |
| Izaje | Levantar la carga | Izaje lento, vigilar el limitador y el radio. |
| Traslado y giro | Llevar la carga | Giro suave, controlar el pendulo, area despejada. |
| Descenso | Depositar la carga | Bajada lenta, guiar con el senalero. |
| Cierre | Dejar segura | Gancho arriba, freno de giro liberado, veleta. |

## Izaje seguro: idea general

1. Confirmar el **peso** y el **radio** contra la tabla de carga antes de izar.
2. Coordinar con el **senalero** por radio o gestos.
3. Tensar el cable despacio y despegar la carga sin tirones.
4. Girar y trasladar el carro con movimientos suaves para no balancear.
5. Depositar la carga lento y liberar el gancho con seguridad.

## Errores comunes que la simulacion puede ensenar a evitar

- Izar sin comprobar el peso y el radio contra la tabla de carga.
- Alejar el carro sin notar que la capacidad baja.
- Operar con viento por encima del limite de servicio.
- Girar de golpe y provocar un pendulo peligroso.
- Dejar la grua fuera de servicio con el giro frenado en vez de veleta.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: izar, girar, trasladar el carro y respetar el limitador.
- **Nivel 2 (simplificado)**: agregar momento de carga, radio y limite de viento.
- **Nivel 3 (tecnico)**: sumar pendulo de la carga, trepado y arriostramiento.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-grua-torre.md) · [➡️ Siguiente: Entornos de trabajo](entornos-grua-torre.md)
