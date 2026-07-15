# 🧪 Principios y operación de la maquinaria de construcción

[🏠 Inicio](../../../README.md) · [🚧 Curso: Maquinaria de construcción](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la capacitación de operador
certificada ni el manual del fabricante. Describe cómo se opera la maquinaria en
simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Fuerza hidráulica**: el motor mueve una bomba que genera presión; esa presión
  se convierte en fuerza en cilindros y motores. A mayor presión y área, más
  fuerza de excavación o empuje.
- **Movimiento proporcional**: la velocidad de cada actuador depende de cuanto se
  mueve el joystick, lo que permite trabajo fino y combinado.
- **Estabilidad por momentos**: la máquina vuelca si el momento de la carga (peso
  por alcance) supera el momento resistente de su base y contrapeso.
- **Reparto de peso**: las orugas distribuyen el peso en el suelo; en terreno
  blando esto evita el hundimiento y mejora la estabilidad.
- **Ciclo de trabajo**: excavar, girar, descargar y volver forman un ciclo
  repetitivo cuya eficiencia depende de la coordinación del operador.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión de la máquina y el frente | Aceite, fugas, orugas, terreno firme. |
| Posicionamiento | Ubicar la máquina | Base nivelada, distancia al camión y a la zanja. |
| Excavación / empuje | Trabajar el material | Coordinar brazo, cucharón o hoja. |
| Giro y descarga | Llevar el material | Girar hacia la zona estable, descargar controlado. |
| Traslado | Reubicarse en la faena | Bloqueo de mandos liberado, ruta despejada. |
| Cierre | Dejar la máquina segura | Cucharón apoyado, mandos bloqueados, motor apagado. |

## Estabilidad y cargas: idea general

1. Trabajar sobre **terreno nivelado y firme** siempre que sea posible.
2. No extender el brazo con carga más allá de lo necesario.
3. Girar y descargar hacia el lado más estable de la máquina.
4. Mantener el cucharón bajo y cerca del cuerpo al trasladarse.
5. Vigilar el margen frente al vuelco al aumentar el alcance.

## Errores comunes que la simulación puede enseñar a evitar

- Excavar o cargar con la máquina inclinada en terreno que cede.
- Extender el brazo con carga hasta acercarse al vuelco lateral.
- Trasladarse con el cucharón en alto y perder estabilidad.
- Girar hacia una zona con personas dentro del radio de trabajo.
- Ignorar la temperatura del aceite hidráulico en faena larga.
- Subir o bajar de la cabina sin bloquear los mandos.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: mover el brazo, llenar el cucharón y descargar.
- **Nivel 2 (simplificado)**: agregar traslación, giro y estabilidad básica.
- **Nivel 3 (técnico)**: sumar hidráulica proporcional, momento de carga, límite
  de vuelco y coordinación del ciclo completo.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md)
para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-maquinaria.md) · [➡️ Siguiente: Entornos de trabajo](entornos-maquinaria.md)
