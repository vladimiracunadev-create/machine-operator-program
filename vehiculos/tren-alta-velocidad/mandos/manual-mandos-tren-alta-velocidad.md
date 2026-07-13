# 🎛️ Mandos e instrumentos del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un tren de alta velocidad es la cabina del maquinista, en
cabeza del tren. A diferencia de un vehiculo de carretera, no hay volante: la
ruta la fija la via. El maquinista controla sobre todo la **traccion y el freno**
mediante un manipulador, vigila la **pantalla de senalizacion en cabina** (DMI de
ETCS) y confirma su atencion con el dispositivo de hombre muerto o vigilante.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Pupitre central | Manipulador de traccion/freno | Palanca | Regular traccion y frenado | Alta | Controla la marcha sin volante. |
| Pupitre | Freno de emergencia | Palanca / boton | Detencion maxima | Alta | Aplica todos los frenos disponibles. |
| Piso o pupitre | Hombre muerto / vigilante | Pedal o boton | Confirmar atencion del maquinista | Alta | Si no se confirma, frena solo. |
| Pupitre | Pantografo | Boton | Subir o bajar el pantografo | Alta | Necesario para tomar corriente. |
| Pupitre | Puertas | Boton | Abrir y cerrar puertas en estacion | Media | Enclavamiento con la marcha. |
| Pupitre | Bocina / silbato | Boton | Advertir | Media | Uso de seguridad en la via. |
| Pupitre | Radio de tren | Consola | Comunicar con control | Alta | Contacto con el puesto de control. |
| Pupitre | Limpiaparabrisas y luces | Botones | Visibilidad | Media | Frontales y de gabarito. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocimetro | Velocidad real | km/h | Alta | Central para respetar limites. |
| DMI de ETCS | Velocidad objetivo y limites | km/h | Alta | Pantalla de senalizacion en cabina. |
| Tension de linea | Estado de la catenaria | kV | Alta | Avisa si falta tension. |
| Esfuerzo de traccion/freno | Fuerza aplicada | porcentaje | Media | Muestra cuanto se pide al tren. |
| Presion de freno | Estado del freno neumatico | bar | Alta | Clave para la frenada final. |
| Testigos | Estado de sistemas | luz | Alta | Puertas, pantografo, freno, alarmas. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Aplicar traccion | Flecha arriba | Gatillo derecho | Zona traccion | Progresivo, no on/off. |
| Aplicar freno | Flecha abajo | Gatillo izquierdo | Zona freno | Modula la fuerza de frenado. |
| Freno de emergencia | Barra espaciadora | Boton dedicado | Boton rojo | Aplica todos los frenos. |
| Confirmar vigilante | Tecla V | Boton lateral | Boton vigilante | Evita el frenado automatico. |
| Subir pantografo | Tecla P | Cruceta arriba | Boton pantografo | Necesario antes de traccionar. |
| Abrir/cerrar puertas | Tecla O | Boton inferior | Boton puertas | Solo detenido en estacion. |
| Bocina | Tecla B | Boton superior | Boton bocina | Advertencia en la via. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Tren sin energia | Pupitre off | Subir pantografo, encender. |
| Preparado | Con tension, detenido | Tension de linea presente | Confirmar vigilante, aplicar traccion. |
| En movimiento | Circulando | Velocimetro y DMI activos | Traccionar, frenar, respetar objetivo. |
| Emergencia | Riesgo o falla | Testigos de alerta | Freno de emergencia, contactar control. |

## Observaciones ergonomicas

- El velocimetro y el DMI deben verse siempre y sin ambiguedad.
- El manipulador de traccion/freno debe distinguir con claridad ambas zonas.
- El dispositivo de hombre muerto no debe ser molesto pero si constante.
- El freno de emergencia debe ser accesible y reconocible al instante.
- La interfaz de simulacion deberia aplicar el frenado automatico si no se
  confirma el vigilante o si se supera la velocidad objetivo del DMI.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-tren-alta-velocidad.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-tren-alta-velocidad.md)
