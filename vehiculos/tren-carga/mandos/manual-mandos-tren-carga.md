# 🎛️ Mandos e instrumentos del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 🎛️ Mandos

## Vista general

El puesto del maquinista va en la cabina de la locomotora lider. Desde ahi se
controla la traccion de todo el tren, incluidas las locomotoras remotas por
radio, y el frenado de toda la composicion. A diferencia de un vehiculo de
carretera, el maquinista no dirige la trayectoria (la via es fija): gestiona
fuerza, freno y velocidad sobre una ruta senalizada.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puesto central | Manipulador de traccion | Palanca | Regular fuerza de los motores | Alta | Manda tambien a las locomotoras remotas. |
| Puesto central | Freno automatico | Palanca | Frenar todo el tren por la tuberia de aire | Alta | Actua en locomotora y vagones. |
| Puesto central | Freno independiente | Palanca | Frenar solo la locomotora | Alta | Util en maniobras y ajustes finos. |
| Puesto central | Inversor | Palanca | Elegir sentido de marcha | Alta | Adelante, neutro o atras. |
| Puesto central | Freno dinamico | Palanca o modo | Retener con los motores | Alta | Ahorra zapatas en descensos. |
| Pedal / boton | Hombre muerto / vigilante | Pedal o boton | Confirmar que el maquinista esta atento | Alta | Si no se atiende, frena solo. |
| Consola | Control de patinaje / arenado | Boton | Lanzar arena y limitar patinaje | Media | Mejora la adherencia al arrancar. |
| Consola | Radio | Equipo | Comunicar y mandar remotas | Alta | Enlace con control y otras locomotoras. |
| Consola | Bocina y silbato | Boton | Advertir en pasos a nivel | Alta | Uso obligatorio de seguridad. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocimetro | Velocidad del tren | km/h | Alta | Central para respetar limites de via. |
| Manometro de tuberia de freno | Presion de la tuberia de freno | bar | Alta | Vigila el frenado de todo el tren. |
| Amperimetro de traccion | Corriente en los motores | amperios | Alta | Indica el esfuerzo y el riesgo de patinaje. |
| Indicador de esfuerzo de traccion | Fuerza aplicada | referencia | Media | Ayuda a dosificar el arranque. |
| Testigos | Estado de sistemas | luz | Alta | Patinaje, hombre muerto, remotas, freno. |
| Odometro | Distancia recorrida | km | Baja | Control de recorrido y punto kilometrico. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Aplicar traccion | Flecha arriba | Gatillo derecho | Palanca de traccion | Progresivo, cuidando el patinaje. |
| Freno automatico | Tecla J | Gatillo izquierdo | Palanca de freno tren | Frena toda la composicion. |
| Freno independiente | Tecla K | Boton inferior | Palanca de freno loco | Solo la locomotora. |
| Freno dinamico | Tecla D | Boton lateral | Modo dinamico | Retiene sin desgaste. |
| Invertir sentido | Tecla R | Cruceta arriba/abajo | Selector de sentido | Adelante, neutro o atras. |
| Arenado | Tecla S | Boton frontal | Boton de arena | Sube la adherencia al arrancar. |
| Vigilante / hombre muerto | Barra espacio | Boton de confirmacion | Boton de atencion | Confirmar de forma periodica. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Detenido | Tren parado con freno aplicado | Presion de tuberia baja | Cargar aire, soltar freno, aplicar traccion. |
| Preparado | Aire cargado, listo para partir | Manometro en rango | Aplicar traccion, arenar. |
| En marcha | Tren circulando | Velocimetro activo | Traccionar, frenar, usar dinamico. |
| Frenando | Reduciendo velocidad | Manometro descendiendo | Modular freno, arenar, detener. |
| Emergencia | Riesgo o falla | Testigos de alerta | Freno de emergencia, avisar por radio. |

## Observaciones ergonomicas

- El velocimetro, el manometro de tuberia de freno y el amperimetro deben verse siempre.
- El manipulador de traccion y el freno automatico conviven en el puesto central: la
  interfaz debe dejar claro que no se aplican fuerza y freno a la vez sin control.
- El hombre muerto o vigilante debe ser accesible y su alarma reconocible.
- La interfaz de simulacion deberia advertir el patinaje y sugerir arenado en los
  niveles de realismo mas altos.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-tren-carga.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-tren-carga.md)
