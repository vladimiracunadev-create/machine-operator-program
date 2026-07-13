# 🎛️ Mandos e instrumentos del automovil

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automoviles](../README.md) · 🎛️ Mandos

## Vista general

El puesto de conduccion de un automovil reune el volante, los pedales, la palanca
selectora y un conjunto de mandos secundarios al alcance de la mano. A diferencia
de una moto, el conductor va sentado y protegido, y opera la direccion con ambas
manos sobre el volante y la propulsion y frenado con los pies. El tablero, hoy
digital o mixto, se ubica frente al conductor.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Volante | Volante | Aro giratorio | Orientar las ruedas delanteras | Alta | Se maneja con ambas manos. |
| Pie derecho | Acelerador | Pedal | Regular potencia del motor | Alta | Progresivo, no on/off. |
| Pie derecho | Freno | Pedal | Reducir velocidad | Alta | Modula la fuerza de frenado. |
| Pie izquierdo | Embrague | Pedal | Desconectar motor y caja | Alta | Solo en transmision manual. |
| Consola | Palanca selectora | Palanca | Elegir marcha o modo (P R N D) | Alta | Manual o automatica. |
| Consola | Freno de mano | Palanca / boton | Inmovilizar detenido | Media | Mecanico o electrico (EPB). |
| Volante izq | Luces e intermitentes | Palanca | Senalizar y alumbrar | Media | Cruce, carretera y giros. |
| Volante der | Limpiaparabrisas | Palanca | Limpiar el vidrio | Media | Con lluvia o suciedad. |
| Volante | Bocina | Boton | Advertir | Media | Uso de seguridad. |
| Tablero | Climatizacion | Perillas / pantalla | Regular temperatura | Baja | Confort y desempano. |
| Tablero | Instrumentos | Pantalla | Mostrar estado | Alta | Ver seccion de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocimetro | Velocidad | km/h | Alta | Central para circular seguro. |
| Tacometro | Regimen del motor | rpm | Media | Ayuda a elegir la marcha. |
| Indicador de marcha | Marcha o modo actual | P R N D / numero | Media | Comun en cajas automaticas. |
| Nivel de combustible | Energia restante | fraccion / % | Alta | Incluye autonomia estimada. |
| Temperatura motor | Estado termico | grados | Media | Alerta de sobrecalentamiento. |
| Testigos | Estado de sistemas | luz | Alta | Aceite, ABS, airbag, cinturon. |
| Odometro | Distancia recorrida | km | Baja | Total y parcial. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Progresivo, no on/off. |
| Frenar | Flecha abajo | Gatillo izquierdo | Boton freno | Modula la fuerza. |
| Embragar | Shift | Boton lateral | Boton embrague | Solo en modo manual. |
| Girar | Flechas izq/der | Stick izquierdo | Inclinar / arrastrar | Proporcional al angulo. |
| Cambiar marcha | E / Q | Cruceta arriba/abajo | Botones +/- | Manual o modo D. |
| Luces / intermitentes | Tecla L | Cruceta lateral | Boton luces | Senalizar maniobras. |
| Freno de mano | Barra espacio | Boton inferior | Boton freno mano | Al detenerse o estacionar. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Tablero off | Encender, ajustar posicion. |
| Preparado | Motor encendido, detenido | Testigos activos | Poner marcha, soltar freno. |
| En movimiento | Circulando | Velocimetro activo | Acelerar, frenar, girar, cambiar. |
| Emergencia | Riesgo o falla | Testigos de alerta | Frenar, orillar, encender balizas. |

## Observaciones ergonomicas

- El velocimetro y los testigos deben verse siempre sin apartar la vista del camino.
- Acelerador y freno comparten el pie derecho: la interfaz debe dejar claro que no
  se accionan a la vez.
- El freno de mano y las balizas deben ser accesibles y reconocibles.
- La interfaz de simulacion deberia exigir el cinturon antes de partir y penalizar
  el uso del telefono en los niveles de realismo mas altos.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-automovil.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-automovil.md)
