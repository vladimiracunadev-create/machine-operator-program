# 🎛️ Mandos e instrumentos del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un tren de alta velocidad es la cabina del maquinista, en
cabeza del tren. A diferencia de un vehículo de carretera, no hay volante: la
ruta la fija la vía. El maquinista controla sobre todo la **tracción y el freno**
mediante un manipulador, vigila la **pantalla de señalización en cabina** (DMI de
ETCS) y confirma su atención con el dispositivo de hombre muerto o vigilante.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Pupitre central | Manipulador de tracción/freno | Palanca | Regular tracción y frenado | Alta | Controla la marcha sin volante. |
| Pupitre | Freno de emergencia | Palanca / botón | Detención máxima | Alta | Aplica todos los frenos disponibles. |
| Piso o pupitre | Hombre muerto / vigilante | Pedal o botón | Confirmar atención del maquinista | Alta | Si no se confirma, frena solo. |
| Pupitre | Pantógrafo | Botón | Subir o bajar el pantógrafo | Alta | Necesario para tomar corriente. |
| Pupitre | Puertas | Botón | Abrir y cerrar puertas en estación | Media | Enclavamiento con la marcha. |
| Pupitre | Bocina / silbato | Botón | Advertir | Media | Uso de seguridad en la vía. |
| Pupitre | Radio de tren | Consola | Comunicar con control | Alta | Contacto con el puesto de control. |
| Pupitre | Limpiaparabrisas y luces | Botones | Visibilidad | Media | Frontales y de gabarito. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad real | km/h | Alta | Central para respetar límites. |
| DMI de ETCS | Velocidad objetivo y límites | km/h | Alta | Pantalla de señalización en cabina. |
| Tensión de línea | Estado de la catenaria | kV | Alta | Avisa si falta tensión. |
| Esfuerzo de tracción/freno | Fuerza aplicada | porcentaje | Media | Muestra cuanto se pide al tren. |
| Presión de freno | Estado del freno neumático | bar | Alta | Clave para la frenada final. |
| Testigos | Estado de sistemas | luz | Alta | Puertas, pantógrafo, freno, alarmas. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Aplicar tracción | Flecha arriba | Gatillo derecho | Zona tracción | Progresivo, no on/off. |
| Aplicar freno | Flecha abajo | Gatillo izquierdo | Zona freno | Modula la fuerza de frenado. |
| Freno de emergencia | Barra espaciadora | Botón dedicado | Botón rojo | Aplica todos los frenos. |
| Confirmar vigilante | Tecla V | Botón lateral | Botón vigilante | Evita el frenado automático. |
| Subir pantógrafo | Tecla P | Cruceta arriba | Botón pantógrafo | Necesario antes de traccionar. |
| Abrir/cerrar puertas | Tecla O | Botón inferior | Botón puertas | Solo detenido en estación. |
| Bocina | Tecla B | Botón superior | Botón bocina | Advertencia en la vía. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Tren sin energía | Pupitre off | Subir pantógrafo, encender. |
| Preparado | Con tensión, detenido | Tensión de línea presente | Confirmar vigilante, aplicar tracción. |
| En movimiento | Circulando | Velocímetro y DMI activos | Traccionar, frenar, respetar objetivo. |
| Emergencia | Riesgo o falla | Testigos de alerta | Freno de emergencia, contactar control. |

## Observaciones ergonomicas

- El velocímetro y el DMI deben verse siempre y sin ambiguedad.
- El manipulador de tracción/freno debe distinguir con claridad ambas zonas.
- El dispositivo de hombre muerto no debe ser molesto pero si constante.
- El freno de emergencia debe ser accesible y reconocible al instante.
- La interfaz de simulación debería aplicar el frenado automático si no se
  confirma el vigilante o si se supera la velocidad objetivo del DMI.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-alta-velocidad.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-tren-alta-velocidad.md)
