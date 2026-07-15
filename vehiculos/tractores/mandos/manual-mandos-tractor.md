# 🎛️ Mandos e instrumentos del tractor

[🏠 Inicio](../../../README.md) · [🚜 Curso: Tractores](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando del tractor combina los controles de conducción con los de
trabajo. Además del volante y los pedales, el operador dispone de mandos para la
toma de fuerza, la hidráulica del enganche de tres puntos y las salidas
hidráulicas externas. La cabina moderna incluye estructura antivuelco (ROPS) y
cinturón, elementos de seguridad centrales.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Volante | Dirección | Volante asistido | Orientar el eje delantero | Alta | Radio de giro corto para maniobrar. |
| Pie derecho | Acelerador | Pedal | Regular el par del motor | Alta | Suele haber también acelerador de mano. |
| Pie | Frenos independientes | Dos pedales | Frenar cada rueda trasera | Alta | Se unen para frenar en carretera. |
| Pie izquierdo | Embrague | Pedal | Desacoplar motor y caja | Alta | Para cambiar y para arrancar. |
| Palanca | Cambio de marchas y gamas | Palancas | Elegir relación y superreductora | Alta | Muchas relaciones de trabajo. |
| Palanca | Mando de la PTO | Palanca o botón | Conectar la toma de fuerza | Alta | Elegir 540 o 1000 rpm. |
| Palanca | Enganche de tres puntos | Palanca de posición | Subir y bajar el apero | Alta | Control de posición o de esfuerzo. |
| Consola | Salidas hidráulicas | Palancas | Alimentar aperos externos | Media | Para cilindros del apero. |
| Tablero | Bloqueo de diferencial | Pedal o botón | Igualar giro de ruedas | Media | Para barro o patinaje. |
| Tablero | Doble tracción | Botón | Traccionar el eje delantero | Media | Más agarre cuando se necesita. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Tacómetro | Régimen del motor | rpm | Alta | Marca el régimen de PTO (540/1000). |
| Cuentahoras | Horas de trabajo | horas | Alta | Base del mantenimiento, no del odómetro. |
| Temperatura del motor | Calor del refrigerante | grados | Alta | Vigila esfuerzo continuo. |
| Presión de aceite | Lubricación | testigo/bar | Alta | Crítica en trabajo prolongado. |
| Nivel de combustible | Diesel restante | fracción | Alta | Autonomía de la jornada. |
| Testigos | Estado de sistemas | luz | Alta | Freno de mano, carga, filtros. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Con opción de acelerador de mano. |
| Frenar | Flecha abajo | Gatillo izquierdo | Botón freno | Frenos unidos en carretera. |
| Embragar | Shift | Botón lateral | Botón embrague | Para cambiar de marcha. |
| Cambiar marcha | E / Q | Cruceta | Botones más/menos | Con gamas y superreductora. |
| Conectar PTO | Tecla T | Botón dedicado | Botón PTO | Elegir régimen normalizado. |
| Subir/bajar apero | R / F | Cruceta arriba/abajo | Palanca en pantalla | Control de posición o esfuerzo. |
| Doble tracción | Tecla 4 | Botón | Botón 4x4 | Activa el eje delantero. |
| Girar | Flechas izq/der | Stick izquierdo | Volante en pantalla | Radio de giro corto. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Tablero off | Encender, revisar aperos. |
| Preparado | Motor en marcha, detenido | Testigos en verde | Meter marcha, conectar PTO. |
| Traslado | Circulando sin trabajar | Marcha de transporte | Conducir, girar, frenar. |
| Trabajando | Apero en acción | PTO o hidráulica activas | Regular profundidad y avance. |
| Emergencia | Riesgo o falla | Testigos de alerta | Desconectar PTO, frenar, detener. |

## Observaciones ergonomicas

- El tacómetro con marcas de PTO debe verse siempre para mantener el régimen.
- El mando de la PTO debe ser inconfundible y fácil de desconectar.
- El asiento con suspensión y el cinturón dentro del ROPS son claves de seguridad.
- La interfaz de simulación debería advertir el vuelco al girar en pendiente y
  bloquear el trabajo con la PTO si alguien está en la zona de riesgo.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-tractor.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-tractor.md)
