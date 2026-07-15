# 🧪 Principios y operación del dron

[🏠 Inicio](../../../README.md) · [🕹️ Curso: Drones](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye una formación de piloto de RPAS
certificada ni el manual del fabricante. Describe cómo se opera un dron en
simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Sustentación por rotores**: cada hélice empuja aire hacia abajo y genera
  empuje hacia arriba; la suma de todos los rotores sostiene el dron.
- **Control por diferencia de empuje**: el multirotor no tiene superficies
  móviles; cabecea, alabea y guina variando el rpm de rotores concretos.
- **Estabilidad por control activo**: el dron no es estable por si mismo; la
  controladora corrige la actitud muchas veces por segundo con ayuda de la IMU.
- **Guiñada por par**: al acelerar los rotores que giran en un sentido y frenar
  los del otro, aparece un par neto que rota el dron sobre su eje vertical.
- **Autonomía y peso**: la batería limita el tiempo de vuelo; más carga exige más
  empuje y reduce los minutos disponibles.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión básica | Hélices, batería, GPS, enlace, firmware, zona permitida. |
| Armado | Preparar los motores | Confirmar modo, satélites suficientes, área despejada. |
| Despegue | Elevarse en vertical | Subir throttle suave, verificar estabilidad. |
| Misión | Volar y capturar datos | Mantener enlace, vigilar batería y distancia. |
| Retorno | Volver al punto de casa | Manual o automático; subir a altura segura. |
| Aterrizaje | Posarse con suavidad | Descenso controlado, desarmar motores. |

## Vuelo estacionario: idea general

1. Ajustar el **throttle** para que el empuje iguale el peso.
2. Dejar que el modo GPS **mantenga el punto** con pequeñas correcciones.
3. Usar cabeceo y alabeo con movimientos suaves para no derivar.
4. Vigilar **batería, altura y distancia** en la estación.
5. Corregir de forma continua: el viento empuja y hay que compensarlo.

## Errores comunes que la simulación puede enseñar a evitar

- Despegar con pocos satélites y perder el mantenimiento de posición.
- Alejarse hasta el límite del enlace de radio.
- Ignorar el aviso de batería baja y quedarse sin energía en el aire.
- Volar con viento fuerte que supera el empuje disponible.
- Sobrecontrolar los sticks y provocar oscilaciones.
- Olvidar revisar la zona: volar cerca de un aeropuerto o sobre personas.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: despegar, mantener el hover, trasladar y aterrizar.
- **Nivel 2 (simplificado)**: agregar viento, autonomía de batería y límite de enlace.
- **Nivel 3 (técnico)**: sumar modos de vuelo, pérdida de GPS y fail-safe.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-dron.md) · [➡️ Siguiente: Entornos de trabajo](entornos-dron.md)
