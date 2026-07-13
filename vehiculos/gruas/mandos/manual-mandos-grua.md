# 🎛️ Mandos e instrumentos de la grua

[🏠 Inicio](../../../README.md) · [🏗️ Curso: Gruas](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de una grua es una cabina giratoria montada sobre la
superestructura. El operador controla casi todo con dos joysticks
electrohidraulicos proporcionales, palancas para los estabilizadores y una
consola de instrumentos donde el LMI ocupa el lugar central. A diferencia de un
vehiculo de calle, aqui la prioridad no es la velocidad sino la precision y el
control del momento de carga.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Joystick izquierdo | Elevacion de pluma | Joystick proporcional | Subir y bajar el angulo de la pluma | Alta | Subir el angulo reduce el radio. |
| Joystick izquierdo | Giro / swing | Joystick proporcional | Rotar la superestructura | Alta | Movimiento suave para no balancear la carga. |
| Joystick derecho | Telescopico | Joystick proporcional | Extender o recoger la pluma | Alta | Extender aumenta el radio y baja la capacidad. |
| Joystick derecho | Cabrestante | Joystick proporcional | Subir o bajar el gancho | Alta | Controla el izaje vertical de la carga. |
| Consola lateral | Estabilizadores | Palancas | Extender y apoyar outriggers | Alta | Se opera con la grua detenida antes de izar. |
| Consola | Parada de emergencia | Boton hongo | Cortar todos los movimientos | Alta | Detiene la operacion de inmediato. |
| Consola | Bloqueo de giro | Palanca | Fijar la superestructura | Media | Se usa al desplazar o transportar. |
| Consola | Bocina y senales | Boton | Advertir a personal en tierra | Media | Coordinacion con el senalero. |
| Cabina | Instrumentos y LMI | Pantalla | Mostrar estado de izaje | Alta | Ver seccion de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| LMI (momento de carga) | Momento actual vs maximo | % y t·m | Alta | Corazon de la seguridad; avisa y corta. |
| Indicador de carga | Peso izado | t | Alta | Peso real en el gancho. |
| Angulo de pluma | Inclinacion de la pluma | grados | Alta | Relacionado con el radio. |
| Radio de trabajo | Distancia del eje al gancho | m | Alta | Parametro clave de la tabla de carga. |
| Longitud de pluma | Extension telescopica | m | Alta | Define la tabla aplicable. |
| Anemometro | Velocidad del viento | km/h o m/s | Alta | El viento reduce el limite de izaje. |
| Nivel de burbuja | Nivelacion de la maquina | grados | Alta | Confirma base estabilizada. |
| Altura de gancho | Posicion vertical del gancho | m | Media | Evita el contacto y el fin de carrera. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Elevar pluma | Flechas arriba/abajo | Stick izquierdo vertical | Zona pluma | Proporcional, no on/off. |
| Girar superestructura | Flechas izq/der | Stick izquierdo horizontal | Zona giro | Movimiento suave para no balancear. |
| Telescopiar | Teclas R/F | Stick derecho vertical | Zona telescopico | Extender baja la capacidad. |
| Subir/bajar gancho | Teclas W/S | Stick derecho horizontal | Zona winch | Controla el izaje vertical. |
| Estabilizadores | Tecla O | Botones laterales | Panel outriggers | Solo con grua detenida. |
| Parada de emergencia | Barra espaciadora | Boton dedicado | Boton rojo | Corta todos los movimientos. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Consola off | Encender, planificar. |
| No estabilizado | Encendida, sin outriggers | Alerta de nivel | Extender estabilizadores. |
| Estabilizado | Base apoyada y nivelada | Nivel en verde | Habilitar izaje. |
| Izando | Levantando o moviendo carga | LMI activo | Elevar, girar, telescopiar, gancho. |
| Emergencia | LMI en limite o falla | Alarma y luz roja | Parar, reducir radio, bajar carga. |

## Observaciones ergonomicas y de seguridad

- El LMI debe estar siempre visible y ser el primer instrumento en el campo de vision.
- Los joysticks proporcionales evitan movimientos bruscos que balancean la carga.
- El sistema debe impedir el izaje si la grua no esta estabilizada y nivelada.
- La parada de emergencia debe ser grande, roja y accesible sin mirar.
- En simulacion conviene mostrar el radio y el porcentaje de capacidad de forma
  continua, para que el usuario relacione cada movimiento con la estabilidad.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-grua.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-grua.md)
