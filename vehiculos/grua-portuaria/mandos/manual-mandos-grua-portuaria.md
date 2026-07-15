# 🎛️ Mandos e instrumentos de la grúa portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de una grúa pórtico ship-to-shore es una cabina que suele ir
montada en el trolley, mirando hacia abajo el punto de izaje. El operador
controla los movimientos con dos joysticks proporcionales, apoyados en pedales y
botonera para el spreader, mientras vigila una consola de instrumentos con la
carga, la posición y el viento. A diferencia de un vehículo de calle, aquí la
prioridad no es la velocidad sino la precisión del posicionamiento y el control
del balanceo de la carga.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Joystick izquierdo | Traslación del trolley | Joystick proporcional | Mover el carro entre buque y muelle | Alta | Define el alcance horizontal del izaje. |
| Joystick izquierdo | Traslación del gantry | Joystick proporcional | Mover el pórtico sobre los rieles | Alta | Reposiciona la grúa frente a otra bahía. |
| Joystick derecho | Izaje hoist | Joystick proporcional | Subir y bajar el spreader | Alta | Controla el izaje vertical de la carga. |
| Joystick derecho | Anti-sway | Botón o modo | Activar el control de balanceo | Alta | Estabiliza el contenedor colgado. |
| Botonera | Spreader bajar/subir twist-locks | Botones | Trabar y liberar el contenedor | Alta | Solo iza con la carga trabada. |
| Botonera | Telescopiado del spreader | Botones | Ajustar a 20, 40 o 45 pies | Alta | Debe coincidir con el contenedor. |
| Consola | Abatimiento de la pluma | Palanca | Subir o bajar el boom | Media | Se opera con la grúa sin carga. |
| Consola | Parada de emergencia | Botón hongo | Cortar todos los movimientos | Alta | Detiene la operación de inmediato. |
| Cabina | Instrumentos y cámaras | Pantalla | Mostrar estado y vistas | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Indicador de carga | Peso izado por el spreader | t | Alta | Debe respetar el límite de la grúa. |
| Límite de carga | Carga actual vs máxima | % | Alta | Avisa y corta al acercarse al límite. |
| Posición del trolley | Distancia del carro sobre la viga | m | Alta | Ubica el punto de izaje. |
| Altura del spreader | Posición vertical del izaje | m | Alta | Evita topes y colisiones. |
| Estado de twist-locks | Trabado o liberado | luz | Alta | Habilita o impide el izaje. |
| Anemómetro | Velocidad del viento | km/h o m/s | Alta | El viento define el límite operacional. |
| Posición del gantry | Ubicación en el muelle | m o bahía | Media | Alinea la grúa con la bodega. |
| Cámaras | Vistas del spreader y del apoyo | imagen | Alta | Apoyan el posicionamiento fino. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Trasladar trolley | Flechas izq/der | Stick izquierdo horizontal | Zona trolley | Proporcional, no on/off. |
| Trasladar gantry | Teclas A/D | Stick izquierdo vertical | Zona gantry | Movimiento lento sobre rieles. |
| Izar o bajar | Flechas arriba/abajo | Stick derecho vertical | Zona hoist | Controla el izaje vertical. |
| Trabar twist-locks | Tecla T | Botón derecho | Botón spreader | Requerido para izar. |
| Telescopiar spreader | Teclas R/F | Cruceta | Panel spreader | Ajusta a la longitud del contenedor. |
| Activar anti-sway | Tecla Z | Botón lateral | Botón anti-sway | Estabiliza el balanceo. |
| Parada de emergencia | Barra espaciadora | Botón dedicado | Botón rojo | Corta todos los movimientos. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Grúa sin energía | Consola off | Encender, planificar. |
| Preparada | Energizada, pluma abajo | Instrumentos activos | Posicionar gantry y trolley. |
| Enganchando | Spreader sobre el contenedor | Sensores de asiento | Trabar twist-locks. |
| Izando | Levantando o moviendo carga | Carga y anti-sway activos | Izar, trasladar, posicionar. |
| Emergencia | Sobrecarga, viento o falla | Alarma y luz roja | Parar, bajar carga, asegurar. |

## Observaciones ergonomicas y de seguridad

- El indicador de carga y el anemómetro deben estar siempre visibles en la cabina.
- Los joysticks proporcionales evitan movimientos bruscos que balancean la carga.
- El sistema debe impedir el izaje si los twist-locks no están trabados.
- La cabina en el trolley da visión directa hacia abajo, apoyada por cámaras.
- La parada de emergencia debe ser grande, roja y accesible sin mirar.
- En simulación conviene mostrar la posición del trolley y el estado del spreader
  de forma continua, para que el usuario relacione cada movimiento con la carga.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-portuaria.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-grua-portuaria.md)
