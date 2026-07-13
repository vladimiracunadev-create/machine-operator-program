# 🧪 Principios y operacion del tanque (marco publico)

[🏠 Inicio](../../../README.md) · [🪖 Curso: Tanques](../README.md) · 🧪 Principios

Documento general y educativo, **solo de movilidad**. No sustituye formacion real
ni trata contenido sensible, en linea con
[`docs/04-seguridad-y-limites.md`](../../../docs/04-seguridad-y-limites.md).
Describe como se mueve el vehiculo en simulacion y que fisica conviene
representar.

## Principios de movilidad

- **Propulsion**: el motor entrega par a la rueda motriz, que mueve la cadena de
  oruga; el acelerador regula esa entrega.
- **Direccion diferencial**: el vehiculo gira variando la velocidad de cada
  oruga, no orientando ruedas.
- **Reparto de presion**: al apoyar el peso en una gran superficie, el vehiculo
  avanza por terreno blando sin hundirse.
- **Relacion potencia/peso**: define la aceleracion y la capacidad de subir
  pendientes con mucha masa.
- **Adherencia**: la oruga limita cuanta fuerza se puede aplicar antes de patinar
  en barro, roca o hielo.

## Fases de operacion (movilidad)

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Orugas, tension, combustible, niveles. |
| Arranque | Encender el motor | Punto muerto, testigos normales. |
| Puesta en marcha | Iniciar avance | Marcha corta, acelerar suave. |
| Marcha | Avanzar por terreno | Elegir linea, mantener regimen adecuado. |
| Obstaculos | Pendiente, zanja, barro | Reducir, aproximar de frente, control fino. |
| Detencion | Parar de forma segura | Frenar progresivo, dejar en marcha o freno. |
| Cierre | Dejar seguro | Motor apagado, freno puesto. |

## Superar un obstaculo: idea general

1. Aproximarse de frente y a baja velocidad.
2. Elegir una marcha corta para tener fuerza.
3. Mantener el acelerador constante sin golpes.
4. Cuidar el angulo para no perder apoyo de las orugas.
5. Recuperar velocidad una vez superado el obstaculo.

## Errores comunes que la simulacion puede ensenar a evitar

- Girar de forma brusca y perder tension o apoyo de la oruga.
- Subir una pendiente en marcha larga sin fuerza suficiente.
- Acelerar de golpe en barro y hacer patinar las orugas.
- Ignorar la temperatura del motor con mucha carga.
- Abordar un obstaculo en angulo y descarrilar una oruga.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: avanzar, frenar y girar por direccion diferencial.
- **Nivel 2 (simplificado)**: agregar inercia, pendientes y limite de adherencia.
- **Nivel 3 (tecnico)**: sumar marchas, potencia/peso y presion sobre el suelo.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-tanque.md) · [➡️ Siguiente: Entornos de trabajo](entornos-tanque.md)
