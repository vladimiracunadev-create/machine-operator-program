# 🧪 Principios y operación del camión

[🏠 Inicio](../../../README.md) · [🚛 Curso: Camiones](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye un curso de conducción profesional
ni el manual del fabricante. Describe cómo se opera un camión en simulación y que
principios físicos conviene representar.

## Principios de funcionamiento

- **Propulsión**: el motor diesel entrega mucho par a bajas vueltas, que la caja
  multimarcha adapta a la carga y a la pendiente.
- **Masa e inercia**: un camión cargado tiene enorme inercia; tarda mucho más en
  acelerar y en detenerse que un automóvil.
- **Frenado por energía**: la energía cinética crece con la masa y con el
  cuadrado de la velocidad, por eso se combinan frenos de servicio, de motor y
  retarder para no recalentar.
- **Reparto de peso**: la carga debe repartirse por eje; un mal reparto reduce
  agarre delantero, alarga el frenado o sobrecarga un eje.
- **Estabilidad**: un centro de gravedad alto (cisterna, carga apilada) aumenta
  el riesgo de vuelco en curva; la velocidad de paso debe reducirse.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión del vehículo y la carga | Neumáticos, luces, presión de aire, amarre de carga. |
| Carga de aire | Subir la presión del sistema | Esperar el rango normal antes de mover. |
| Arranque | Iniciar movimiento | Soltar estacionamiento, marcha corta, soltar embrague suave. |
| Conducción | Circular con seguridad | Anticipar, mantener gran distancia, vigilar puntos ciegos. |
| Pendientes | Subir y bajar cargado | Marcha adecuada, freno de motor y retarder en bajada. |
| Maniobras | Girar y estacionar | Considerar barrido trasero y espacio del semirremolque. |
| Detención | Parar de forma segura | Frenar progresivo, aplicar estacionamiento, calzar si procede. |

## Pendientes: idea general

1. Elegir la marcha **antes** de la bajada, no durante.
2. Usar freno de motor y retarder para mantener la velocidad.
3. Reservar el freno de servicio para ajustes puntuales, no continuos.
4. En subida, no dejar caer el régimen: reducir a tiempo para no perder impulso.
5. Vigilar la temperatura del motor y de los frenos.

## Errores comunes que la simulación puede enseñar a evitar

- Bajar una pendiente larga usando solo el freno de servicio (riesgo de fading).
- Subestimar la distancia de frenado con el camión cargado.
- Girar demasiado cerca de un obstáculo e ignorar el barrido trasero.
- Circular con presión de aire insuficiente.
- Cargar mal el vehículo y superar el límite de un eje.
- Entrar a una curva con carga alta a demasiada velocidad.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar, girar y respetar señales con carga.
- **Nivel 2 (simplificado)**: agregar inercia por masa, distancia de frenado y
  distribución básica de la carga.
- **Nivel 3 (técnico)**: sumar caja multimarcha, freno de motor y retarder,
  presión de aire, reparto por eje y articulación del semirremolque.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md)
para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-camion.md) · [➡️ Siguiente: Entornos de trabajo](entornos-camion.md)
