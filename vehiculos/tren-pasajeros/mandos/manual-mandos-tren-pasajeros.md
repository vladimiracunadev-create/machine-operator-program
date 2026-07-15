# 🎛️ Mandos e instrumentos del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando del tren es la cabina del maquinista, ubicada en el extremo de
la composición. A diferencia de un auto, el maquinista no dirige la trayectoria:
la vía lo hace. Su trabajo es regular la tracción y el freno, vigilar la
señalización y respetar las velocidades. El control central suele ser un
manipulador que combina tracción y freno, o dos palancas separadas.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Pupitre | Manipulador de tracción | Palanca | Regular la fuerza de tracción | Alta | Puede ir combinado con el freno. |
| Pupitre | Manipulador de freno | Palanca | Regular el freno de servicio | Alta | Neumático y dinámico combinados. |
| Pupitre | Palanca inversora | Selector | Elegir sentido de marcha | Alta | Adelante, neutro o atrás. |
| Pupitre | Freno de emergencia | Mando | Detención máxima | Alta | Aplica todo el freno disponible. |
| Piso o pupitre | Hombre muerto | Pedal o botón | Detectar al maquinista activo | Alta | Frena el tren si se suelta. |
| Pupitre | Vigilante | Botón | Confirmar atención | Alta | Exige respuesta periódica. |
| Pupitre | Areneros | Botón | Soltar arena al riel | Media | Mejora la adherencia. |
| Pupitre | Bocina o silbato | Botón | Advertir | Media | Uso en pasos a nivel y andenes. |
| Pupitre | Mando de puertas | Botón | Abrir y cerrar puertas | Alta | Con enclavamiento de marcha. |
| Pupitre | Radio tren-tierra | Equipo | Comunicar con control | Alta | Coordinación con el puesto central. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad del tren | km/h | Alta | Central para respetar límites. |
| Manómetro de freno | Presión de la tubería de freno | bar | Alta | Vigila el sistema neumático. |
| Indicador de tensión de línea | Tensión de la catenaria | kV | Alta | Confirma alimentación eléctrica. |
| Amperímetro de tracción | Corriente de tracción | A | Media | Ayuda a dosificar el esfuerzo. |
| Panel ATP | Límite y estado de la señal | luz/número | Alta | Repite la señal en cabina. |
| Testigos | Estado de sistemas | luz | Alta | Puertas, freno, hombre muerto. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Aplicar tracción | Flecha arriba | Gatillo derecho | Palanca tracción | Progresivo, no on/off. |
| Aplicar freno | Flecha abajo | Gatillo izquierdo | Palanca freno | Modula la fuerza. |
| Freno de emergencia | Barra espaciadora | Botón rojo | Botón emergencia | Detención máxima. |
| Cambiar sentido | R | Botón lateral | Selector inversor | Adelante, neutro, atrás. |
| Confirmar vigilante | V | Botón superior | Botón vigilante | Respuesta periódica. |
| Arenado | S | Cruceta abajo | Botón arena | Mejora adherencia. |
| Abrir o cerrar puertas | P | Cruceta arriba | Botón puertas | Solo con tren detenido. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Cabina sin energía | Panel off | Encender, revisar sistemas. |
| Preparado | Cabina activa, detenido | Tensión de línea presente | Cerrar puertas, seleccionar sentido. |
| En marcha | Circulando | Velocímetro activo | Aplicar tracción, frenar, vigilar señal. |
| Emergencia | Riesgo o falla | Testigos de alerta | Freno de emergencia, avisar por radio. |

## Observaciones ergonomicas

- El velocímetro y el panel ATP deben verse siempre desde la posición normal.
- El hombre muerto y el vigilante son dispositivos de seguridad: la simulación
  debe representarlos como confirmaciones periódicas, no como estorbos.
- El freno de emergencia debe ser accesible y reconocible al instante.
- El mando de puertas debe estar enclavado para no abrir con el tren en marcha.
- En niveles de realismo altos, la interfaz debería exigir presión de freno
  suficiente antes de autorizar la marcha.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-pasajeros.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-tren-pasajeros.md)
