# 🎛️ Mandos e instrumentos del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando del tren es la cabina del maquinista, ubicada en el extremo de
la composicion. A diferencia de un auto, el maquinista no dirige la trayectoria:
la via lo hace. Su trabajo es regular la traccion y el freno, vigilar la
senalizacion y respetar las velocidades. El control central suele ser un
manipulador que combina traccion y freno, o dos palancas separadas.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Pupitre | Manipulador de traccion | Palanca | Regular la fuerza de traccion | Alta | Puede ir combinado con el freno. |
| Pupitre | Manipulador de freno | Palanca | Regular el freno de servicio | Alta | Neumatico y dinamico combinados. |
| Pupitre | Palanca inversora | Selector | Elegir sentido de marcha | Alta | Adelante, neutro o atras. |
| Pupitre | Freno de emergencia | Mando | Detencion maxima | Alta | Aplica todo el freno disponible. |
| Piso o pupitre | Hombre muerto | Pedal o boton | Detectar al maquinista activo | Alta | Frena el tren si se suelta. |
| Pupitre | Vigilante | Boton | Confirmar atencion | Alta | Exige respuesta periodica. |
| Pupitre | Areneros | Boton | Soltar arena al riel | Media | Mejora la adherencia. |
| Pupitre | Bocina o silbato | Boton | Advertir | Media | Uso en pasos a nivel y andenes. |
| Pupitre | Mando de puertas | Boton | Abrir y cerrar puertas | Alta | Con enclavamiento de marcha. |
| Pupitre | Radio tren-tierra | Equipo | Comunicar con control | Alta | Coordinacion con el puesto central. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocimetro | Velocidad del tren | km/h | Alta | Central para respetar limites. |
| Manometro de freno | Presion de la tuberia de freno | bar | Alta | Vigila el sistema neumatico. |
| Indicador de tension de linea | Tension de la catenaria | kV | Alta | Confirma alimentacion electrica. |
| Amperimetro de traccion | Corriente de traccion | A | Media | Ayuda a dosificar el esfuerzo. |
| Panel ATP | Limite y estado de la senal | luz/numero | Alta | Repite la senal en cabina. |
| Testigos | Estado de sistemas | luz | Alta | Puertas, freno, hombre muerto. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Aplicar traccion | Flecha arriba | Gatillo derecho | Palanca traccion | Progresivo, no on/off. |
| Aplicar freno | Flecha abajo | Gatillo izquierdo | Palanca freno | Modula la fuerza. |
| Freno de emergencia | Barra espaciadora | Boton rojo | Boton emergencia | Detencion maxima. |
| Cambiar sentido | R | Boton lateral | Selector inversor | Adelante, neutro, atras. |
| Confirmar vigilante | V | Boton superior | Boton vigilante | Respuesta periodica. |
| Arenado | S | Cruceta abajo | Boton arena | Mejora adherencia. |
| Abrir o cerrar puertas | P | Cruceta arriba | Boton puertas | Solo con tren detenido. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Cabina sin energia | Panel off | Encender, revisar sistemas. |
| Preparado | Cabina activa, detenido | Tension de linea presente | Cerrar puertas, seleccionar sentido. |
| En marcha | Circulando | Velocimetro activo | Aplicar traccion, frenar, vigilar senal. |
| Emergencia | Riesgo o falla | Testigos de alerta | Freno de emergencia, avisar por radio. |

## Observaciones ergonomicas

- El velocimetro y el panel ATP deben verse siempre desde la posicion normal.
- El hombre muerto y el vigilante son dispositivos de seguridad: la simulacion
  debe representarlos como confirmaciones periodicas, no como estorbos.
- El freno de emergencia debe ser accesible y reconocible al instante.
- El mando de puertas debe estar enclavado para no abrir con el tren en marcha.
- En niveles de realismo altos, la interfaz deberia exigir presion de freno
  suficiente antes de autorizar la marcha.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-tren-pasajeros.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-tren-pasajeros.md)
