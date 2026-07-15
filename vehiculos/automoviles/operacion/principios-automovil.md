# 🧪 Principios y operación del automóvil

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automóviles](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye un curso de conducción certificado ni
el manual del fabricante. Describe cómo se opera un automóvil en simulación y que
principios físicos conviene representar.

## Principios de funcionamiento

- **Tracción**: el motor entrega par a las ruedas motrices a través de la
  transmisión y el diferencial. El acelerador regula esa entrega.
- **Dirección**: al girar el volante, las ruedas delanteras cambian su ángulo y
  el auto describe una curva; el radio depende del ángulo y de la velocidad.
- **Transferencia de peso**: al frenar el peso va hacia adelante, al acelerar
  hacia atrás y al girar hacia el exterior de la curva. Esto cambia el agarre de
  cada rueda.
- **Frenado**: los frenos convierten el movimiento en calor; los delanteros
  aportan más capacidad porque reciben más peso al frenar.
- **Adherencia**: el agarre de los cuatro neumáticos limita cuanta aceleración,
  frenado y giro son posibles antes de deslizar (subviraje o sobreviraje).

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión básica | Neumáticos, luces, frenos, combustible, espejos. |
| Arranque | Encender el motor | Freno pisado, palanca en P o N, cinturón puesto. |
| Puesta en marcha | Iniciar movimiento | Meter marcha, soltar freno, acelerar suave. |
| Conducción | Circular con seguridad | Mirar lejos, mantener distancia, respetar límites. |
| Maniobras | Curvas y cambios | Frenar antes de la curva, girar suave, acelerar a la salida. |
| Detención | Parar de forma segura | Frenar progresivo, dejar en P o punto muerto. |
| Cierre | Dejar seguro | Freno de mano, motor apagado, luces off. |

## Curvas: idea general

1. Ajustar la velocidad **antes** de entrar a la curva.
2. Mirar hacia la salida, no al capo.
3. Trazar suave y progresivo, sin movimientos bruscos del volante.
4. Mantener o abrir levemente el acelerador dentro de la curva.
5. Enderezar y acelerar a la salida.

## Errores comunes que la simulación puede enseñar a evitar

- Frenar dentro de la curva en vez de antes de entrar.
- Girar el volante de golpe y provocar pérdida de agarre.
- Ignorar la transferencia de peso al frenar o acelerar.
- Seguir demasiado cerca del vehículo de adelante.
- No adaptar la velocidad al piso mojado o a la baja visibilidad.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar, girar y respetar señales.
- **Nivel 2 (simplificado)**: agregar inercia, transferencia de peso y límite de
  adherencia.
- **Nivel 3 (técnico)**: sumar embrague, marchas, subviraje/sobreviraje y frenada
  con ABS.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-automovil.md) · [➡️ Siguiente: Entornos de trabajo](entornos-automovil.md)
