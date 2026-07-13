# 🧪 Principios y operacion del automovil

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automoviles](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye un curso de conduccion certificado ni
el manual del fabricante. Describe como se opera un automovil en simulacion y que
principios fisicos conviene representar.

## Principios de funcionamiento

- **Traccion**: el motor entrega par a las ruedas motrices a traves de la
  transmision y el diferencial. El acelerador regula esa entrega.
- **Direccion**: al girar el volante, las ruedas delanteras cambian su angulo y
  el auto describe una curva; el radio depende del angulo y de la velocidad.
- **Transferencia de peso**: al frenar el peso va hacia adelante, al acelerar
  hacia atras y al girar hacia el exterior de la curva. Esto cambia el agarre de
  cada rueda.
- **Frenado**: los frenos convierten el movimiento en calor; los delanteros
  aportan mas capacidad porque reciben mas peso al frenar.
- **Adherencia**: el agarre de los cuatro neumaticos limita cuanta aceleracion,
  frenado y giro son posibles antes de deslizar (subviraje o sobreviraje).

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Neumaticos, luces, frenos, combustible, espejos. |
| Arranque | Encender el motor | Freno pisado, palanca en P o N, cinturon puesto. |
| Puesta en marcha | Iniciar movimiento | Meter marcha, soltar freno, acelerar suave. |
| Conduccion | Circular con seguridad | Mirar lejos, mantener distancia, respetar limites. |
| Maniobras | Curvas y cambios | Frenar antes de la curva, girar suave, acelerar a la salida. |
| Detencion | Parar de forma segura | Frenar progresivo, dejar en P o punto muerto. |
| Cierre | Dejar seguro | Freno de mano, motor apagado, luces off. |

## Curvas: idea general

1. Ajustar la velocidad **antes** de entrar a la curva.
2. Mirar hacia la salida, no al capo.
3. Trazar suave y progresivo, sin movimientos bruscos del volante.
4. Mantener o abrir levemente el acelerador dentro de la curva.
5. Enderezar y acelerar a la salida.

## Errores comunes que la simulacion puede ensenar a evitar

- Frenar dentro de la curva en vez de antes de entrar.
- Girar el volante de golpe y provocar perdida de agarre.
- Ignorar la transferencia de peso al frenar o acelerar.
- Seguir demasiado cerca del vehiculo de adelante.
- No adaptar la velocidad al piso mojado o a la baja visibilidad.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar, girar y respetar senales.
- **Nivel 2 (simplificado)**: agregar inercia, transferencia de peso y limite de
  adherencia.
- **Nivel 3 (tecnico)**: sumar embrague, marchas, subviraje/sobreviraje y frenada
  con ABS.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-automovil.md) · [➡️ Siguiente: Entornos de trabajo](entornos-automovil.md)
