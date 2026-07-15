# 🎛️ Mandos e instrumentos del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 🎛️ Mandos

## Vista general

El puesto del maquinista va en la cabina de la locomotora lider. Desde ahí se
controla la tracción de todo el tren, incluidas las locomotoras remotas por
radio, y el frenado de toda la composición. A diferencia de un vehículo de
carretera, el maquinista no dirige la trayectoria (la vía es fija): gestiona
fuerza, freno y velocidad sobre una ruta senalizada.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puesto central | Manipulador de tracción | Palanca | Regular fuerza de los motores | Alta | Manda también a las locomotoras remotas. |
| Puesto central | Freno automático | Palanca | Frenar todo el tren por la tubería de aire | Alta | Actua en locomotora y vagones. |
| Puesto central | Freno independiente | Palanca | Frenar solo la locomotora | Alta | Útil en maniobras y ajustes finos. |
| Puesto central | Inversor | Palanca | Elegir sentido de marcha | Alta | Adelante, neutro o atrás. |
| Puesto central | Freno dinámico | Palanca o modo | Retener con los motores | Alta | Ahorra zapatas en descensos. |
| Pedal / botón | Hombre muerto / vigilante | Pedal o botón | Confirmar que el maquinista está atento | Alta | Si no se atiende, frena solo. |
| Consola | Control de patinaje / arenado | Botón | Lanzar arena y limitar patinaje | Media | Mejora la adherencia al arrancar. |
| Consola | Radio | Equipo | Comunicar y mandar remotas | Alta | Enlace con control y otras locomotoras. |
| Consola | Bocina y silbato | Botón | Advertir en pasos a nivel | Alta | Uso obligatorio de seguridad. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad del tren | km/h | Alta | Central para respetar límites de vía. |
| Manómetro de tubería de freno | Presión de la tubería de freno | bar | Alta | Vigila el frenado de todo el tren. |
| Amperímetro de tracción | Corriente en los motores | amperios | Alta | Indica el esfuerzo y el riesgo de patinaje. |
| Indicador de esfuerzo de tracción | Fuerza aplicada | referencia | Media | Ayuda a dosificar el arranque. |
| Testigos | Estado de sistemas | luz | Alta | Patinaje, hombre muerto, remotas, freno. |
| Odómetro | Distancia recorrida | km | Baja | Control de recorrido y punto kilométrico. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Aplicar tracción | Flecha arriba | Gatillo derecho | Palanca de tracción | Progresivo, cuidando el patinaje. |
| Freno automático | Tecla J | Gatillo izquierdo | Palanca de freno tren | Frena toda la composición. |
| Freno independiente | Tecla K | Botón inferior | Palanca de freno loco | Solo la locomotora. |
| Freno dinámico | Tecla D | Botón lateral | Modo dinámico | Retiene sin desgaste. |
| Invertir sentido | Tecla R | Cruceta arriba/abajo | Selector de sentido | Adelante, neutro o atrás. |
| Arenado | Tecla S | Botón frontal | Botón de arena | Sube la adherencia al arrancar. |
| Vigilante / hombre muerto | Barra espacio | Botón de confirmación | Botón de atención | Confirmar de forma periódica. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Detenido | Tren parado con freno aplicado | Presión de tubería baja | Cargar aire, soltar freno, aplicar tracción. |
| Preparado | Aire cargado, listo para partir | Manómetro en rango | Aplicar tracción, arenar. |
| En marcha | Tren circulando | Velocímetro activo | Traccionar, frenar, usar dinámico. |
| Frenando | Reduciendo velocidad | Manómetro descendiendo | Modular freno, arenar, detener. |
| Emergencia | Riesgo o falla | Testigos de alerta | Freno de emergencia, avisar por radio. |

## Observaciones ergonomicas

- El velocímetro, el manómetro de tubería de freno y el amperímetro deben verse siempre.
- El manipulador de tracción y el freno automático conviven en el puesto central: la
  interfaz debe dejar claro que no se aplican fuerza y freno a la vez sin control.
- El hombre muerto o vigilante debe ser accesible y su alarma reconocible.
- La interfaz de simulación debería advertir el patinaje y sugerir arenado en los
  niveles de realismo más altos.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-carga.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-tren-carga.md)
