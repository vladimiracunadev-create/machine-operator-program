# 🎛️ Mandos e instrumentos del automóvil

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automóviles](../README.md) · 🎛️ Mandos

## Vista general

El puesto de conducción de un automóvil reune el volante, los pedales, la palanca
selectora y un conjunto de mandos secundarios al alcance de la mano. A diferencia
de una moto, el conductor va sentado y protegido, y opera la dirección con ambas
manos sobre el volante y la propulsión y frenado con los pies. El tablero, hoy
digital o mixto, se ubica frente al conductor.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Volante | Volante | Aro giratorio | Orientar las ruedas delanteras | Alta | Se maneja con ambas manos. |
| Pie derecho | Acelerador | Pedal | Regular potencia del motor | Alta | Progresivo, no on/off. |
| Pie derecho | Freno | Pedal | Reducir velocidad | Alta | Modula la fuerza de frenado. |
| Pie izquierdo | Embrague | Pedal | Desconectar motor y caja | Alta | Solo en transmisión manual. |
| Consola | Palanca selectora | Palanca | Elegir marcha o modo (P R N D) | Alta | Manual o automática. |
| Consola | Freno de mano | Palanca / botón | Inmovilizar detenido | Media | Mecánico o eléctrico (EPB). |
| Volante izq | Luces e intermitentes | Palanca | Señalizar y alumbrar | Media | Cruce, carretera y giros. |
| Volante der | Limpiaparabrisas | Palanca | Limpiar el vidrio | Media | Con lluvia o suciedad. |
| Volante | Bocina | Botón | Advertir | Media | Uso de seguridad. |
| Tablero | Climatización | Perillas / pantalla | Regular temperatura | Baja | Confort y desempano. |
| Tablero | Instrumentos | Pantalla | Mostrar estado | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad | km/h | Alta | Central para circular seguro. |
| Tacómetro | Régimen del motor | rpm | Media | Ayuda a elegir la marcha. |
| Indicador de marcha | Marcha o modo actual | P R N D / número | Media | Común en cajas automáticas. |
| Nivel de combustible | Energía restante | fracción / % | Alta | Incluye autonomía estimada. |
| Temperatura motor | Estado térmico | grados | Media | Alerta de sobrecalentamiento. |
| Testigos | Estado de sistemas | luz | Alta | Aceite, ABS, airbag, cinturón. |
| Odómetro | Distancia recorrida | km | Baja | Total y parcial. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Progresivo, no on/off. |
| Frenar | Flecha abajo | Gatillo izquierdo | Botón freno | Modula la fuerza. |
| Embragar | Shift | Botón lateral | Botón embrague | Solo en modo manual. |
| Girar | Flechas izq/der | Stick izquierdo | Inclinar / arrastrar | Proporcional al ángulo. |
| Cambiar marcha | E / Q | Cruceta arriba/abajo | Botones +/- | Manual o modo D. |
| Luces / intermitentes | Tecla L | Cruceta lateral | Botón luces | Señalizar maniobras. |
| Freno de mano | Barra espacio | Botón inferior | Botón freno mano | Al detenerse o estacionar. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Tablero off | Encender, ajustar posición. |
| Preparado | Motor encendido, detenido | Testigos activos | Poner marcha, soltar freno. |
| En movimiento | Circulando | Velocímetro activo | Acelerar, frenar, girar, cambiar. |
| Emergencia | Riesgo o falla | Testigos de alerta | Frenar, orillar, encender balizas. |

## Observaciones ergonomicas

- El velocímetro y los testigos deben verse siempre sin apartar la vista del camino.
- Acelerador y freno comparten el pie derecho: la interfaz debe dejar claro que no
  se accionan a la vez.
- El freno de mano y las balizas deben ser accesibles y reconocibles.
- La interfaz de simulación debería exigir el cinturón antes de partir y penalizar
  el uso del teléfono en los niveles de realismo más altos.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-automovil.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-automovil.md)
