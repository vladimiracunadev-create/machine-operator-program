# 🎛️ Mandos e instrumentos de la grua torre

[🏠 Inicio](../../../README.md) · [🗼 Curso: Grua torre](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de una grua torre puede ser una cabina en lo alto del mastil,
junto a la corona de giro, o un mando a distancia por radio operado desde tierra.
El operador controla el izaje, la traslacion del carro y el giro con palancas
proporcionales, y vigila una consola donde el limitador de momento y el
anemometro ocupan el lugar central. La prioridad no es la velocidad sino la
precision y el control del momento de carga. En tierra un senalero (rigger)
coordina por radio o con gestos.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Palanca izquierda | Izaje | Palanca proporcional | Subir y bajar el gancho | Alta | Izaje lento para controlar el pendulo. |
| Palanca izquierda | Giro / orientacion | Palanca proporcional | Rotar la superestructura | Alta | Movimiento suave para no balancear la carga. |
| Palanca derecha | Traslacion del carro | Palanca proporcional | Mover el carro por la pluma | Alta | Alejar el carro baja la capacidad. |
| Consola | Limitador de momento | Sistema | Cortar movimientos que superan el momento | Alta | Corazon de la seguridad. |
| Consola | Anemometro | Indicador | Mostrar la velocidad del viento | Alta | Fija el limite de servicio. |
| Consola | Parada de emergencia | Boton hongo | Cortar todos los movimientos | Alta | Detiene la operacion de inmediato. |
| Consola | Freno de giro | Palanca | Fijar o liberar la orientacion | Media | Se libera en veleta fuera de servicio. |
| Consola | Bocina y senales | Boton | Advertir al personal en tierra | Media | Coordinacion con el senalero. |
| Cabina o radio | Instrumentos | Pantalla | Mostrar estado de izaje | Alta | Ver seccion de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Limitador de momento | Momento actual vs maximo | % y t·m | Alta | Avisa y corta antes del vuelco. |
| Indicador de carga | Peso izado | t | Alta | Peso real en el gancho. |
| Radio de trabajo | Distancia del eje al gancho | m | Alta | Parametro clave de la tabla de carga. |
| Altura de gancho | Posicion vertical del gancho | m | Media | Evita el fin de carrera y el contacto. |
| Anemometro | Velocidad del viento | km/h o m/s | Alta | El viento reduce o detiene el izaje. |
| Angulo de giro | Orientacion de la pluma | grados | Media | Ubica la carga sobre la obra. |
| Nivel de la base | Nivelacion del mastil | grados | Alta | Confirma base estabilizada. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Subir/bajar gancho | Teclas W/S | Stick izquierdo vertical | Zona izaje | Proporcional, izaje lento. |
| Girar superestructura | Flechas izq/der | Stick izquierdo horizontal | Zona giro | Movimiento suave para no balancear. |
| Trasladar carro | Teclas R/F | Stick derecho vertical | Zona carro | Alejar baja la capacidad. |
| Freno de giro | Tecla G | Boton lateral | Panel giro | Liberar para veleta. |
| Parada de emergencia | Barra espaciadora | Boton dedicado | Boton rojo | Corta todos los movimientos. |
| Consultar viento | Tecla V | Boton info | Panel anemometro | Decide si se puede izar. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Fuera de servicio | Detenida, giro en veleta | Freno de giro liberado | Poner en servicio si el viento baja. |
| Preparada | Encendida y nivelada | Nivel en verde | Habilitar izaje. |
| Izando | Levantando o moviendo carga | Limitador activo | Izar, girar, trasladar carro. |
| Viento alto | Viento sobre el limite | Alarma de anemometro | Bajar carga, pasar a veleta. |
| Emergencia | Limitador en tope o falla | Alarma y luz roja | Parar, reducir radio, bajar carga. |

## Observaciones ergonomicas y de seguridad

- El limitador de momento debe estar siempre visible y ser el primer instrumento del campo de vision.
- Las palancas proporcionales evitan movimientos bruscos que balancean la carga.
- El sistema debe impedir el izaje si la grua no esta nivelada o si el viento supera el limite.
- La parada de emergencia debe ser grande, roja y accesible sin mirar.
- En simulacion conviene mostrar el radio y el porcentaje de capacidad de forma
  continua, para que el usuario relacione cada movimiento con la estabilidad.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-grua-torre.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-grua-torre.md)
