# 🎛️ Mandos e instrumentos del camión

[🏠 Inicio](../../../README.md) · [🚛 Curso: Camiones](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando del camión es una cabina alta que ofrece amplia visión de la
vía. El conductor opera con volante y pedales como en un automóvil, pero suma
controles propios de la carga pesada: freno de motor, retarder, freno de
estacionamiento por válvula y, en articulados, el mando del semirremolque. El
tablero vigila la presión de aire, algo que en un auto no existe.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Volante | Dirección | Volante asistido | Orientar el eje delantero | Alta | Radio de giro amplio y barrido trasero. |
| Pie derecho | Acelerador | Pedal | Regular el par del motor | Alta | Progresivo, gestiona consumo. |
| Pie central | Freno de servicio | Pedal | Frenar por aire | Alta | Modula toda la combinación de frenos. |
| Pie izquierdo | Embrague | Pedal | Desacoplar motor y caja | Alta | Ausente en cajas automatizadas. |
| Palanca / botones | Cambio de marchas | Palanca o selector | Elegir relación | Alta | Con gama alta/baja y splitter. |
| Columna / palanca | Freno de motor y retarder | Palanca escalonada | Frenar sin fricción | Alta | Clave en pendientes largas. |
| Tablero | Freno de estacionamiento | Válvula de tiro | Bloquear por muelle | Alta | Se aplica al detener. |
| Tablero | Bloqueo de diferencial | Botón | Igualar giro de ejes | Media | Para piso resbaladizo o barro. |
| Consola | Mando del semirremolque | Palanca de mano | Frenar solo el semi | Media | Ayuda a estirar el conjunto. |
| Tablero | Luces, señales y bocina | Botones y palancas | Señalizar y alumbrar | Media | Incluye bocina de aire. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad | km/h | Alta | Central para circular seguro. |
| Tacómetro | Régimen del motor | rpm | Alta | Guía la elección de marcha diesel. |
| Manómetro de aire | Presión de frenos | bar | Alta | Doble aguja por circuitos separados. |
| Temperatura del motor | Calor del refrigerante | grados | Alta | Vigila esfuerzo en pendiente. |
| Nivel de combustible | Diesel restante | fracción | Alta | Autonomía en ruta larga. |
| Nivel de AdBlue | Reactivo SCR | fracción | Media | Necesario para emisiones legales. |
| Testigos | Estado de sistemas | luz | Alta | ABS, freno, motor, baja presión. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Progresivo, cuida el consumo. |
| Frenar servicio | Flecha abajo | Gatillo izquierdo | Botón freno | Modula toda la frenada. |
| Freno de motor / retarder | Tecla B | Cruceta abajo | Botón retarder | Escalonado en varios niveles. |
| Embragar | Shift | Botón lateral | Botón embrague | Ausente en caja automatizada. |
| Subir marcha | E | Cruceta arriba | Botón más | Con gama y splitter. |
| Bajar marcha | Q | Cruceta abajo | Botón menos | Reducir antes de pendiente. |
| Freno de estacionamiento | Tecla P | Botón dedicado | Válvula en pantalla | Bloquea por muelle. |
| Girar | Flechas izq/der | Stick izquierdo | Volante en pantalla | Considerar barrido trasero. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido, sin presión | Tablero off | Encender, cargar aire. |
| Cargando aire | Motor en marcha, subiendo presión | Manómetro subiendo | Esperar presión mínima. |
| Preparado | Presión normal, detenido | Presión en verde | Soltar estacionamiento, meter marcha. |
| En movimiento | Circulando con carga | Velocímetro activo | Acelerar, frenar, cambiar, girar. |
| Emergencia | Riesgo o falla | Testigos de alerta | Frenar, orillar, aplicar retarder. |

## Observaciones ergonomicas

- El manómetro de aire debe verse siempre; la baja presión es crítica.
- El freno de motor y el retarder deben quedar a mano para usarlos en descensos.
- La cabina alta amplia la visión pero crea puntos ciegos cercanos y laterales.
- La interfaz de simulación debería impedir circular sin presión mínima de aire y
  advertir del barrido trasero al girar con semirremolque.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-camion.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-camion.md)
