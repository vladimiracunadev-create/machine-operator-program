# 🎛️ Mandos e instrumentos de la grúa torre

[🏠 Inicio](../../../README.md) · [🗼 Curso: Grúa torre](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de una grúa torre puede ser una cabina en lo alto del mástil,
junto a la corona de giro, o un mando a distancia por radio operado desde tierra.
El operador controla el izaje, la traslación del carro y el giro con palancas
proporcionales, y vigila una consola donde el limitador de momento y el
anemómetro ocupan el lugar central. La prioridad no es la velocidad sino la
precisión y el control del momento de carga. En tierra un señalero (rigger)
coordina por radio o con gestos.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Palanca izquierda | Izaje | Palanca proporcional | Subir y bajar el gancho | Alta | Izaje lento para controlar el péndulo. |
| Palanca izquierda | Giro / orientación | Palanca proporcional | Rotar la superestructura | Alta | Movimiento suave para no balancear la carga. |
| Palanca derecha | Traslación del carro | Palanca proporcional | Mover el carro por la pluma | Alta | Alejar el carro baja la capacidad. |
| Consola | Limitador de momento | Sistema | Cortar movimientos que superan el momento | Alta | Corazón de la seguridad. |
| Consola | Anemómetro | Indicador | Mostrar la velocidad del viento | Alta | Fija el límite de servicio. |
| Consola | Parada de emergencia | Botón hongo | Cortar todos los movimientos | Alta | Detiene la operación de inmediato. |
| Consola | Freno de giro | Palanca | Fijar o liberar la orientación | Media | Se libera en veleta fuera de servicio. |
| Consola | Bocina y señales | Botón | Advertir al personal en tierra | Media | Coordinación con el señalero. |
| Cabina o radio | Instrumentos | Pantalla | Mostrar estado de izaje | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Limitador de momento | Momento actual vs máximo | % y t·m | Alta | Avisa y corta antes del vuelco. |
| Indicador de carga | Peso izado | t | Alta | Peso real en el gancho. |
| Radio de trabajo | Distancia del eje al gancho | m | Alta | Parámetro clave de la tabla de carga. |
| Altura de gancho | Posición vertical del gancho | m | Media | Evita el fin de carrera y el contacto. |
| Anemómetro | Velocidad del viento | km/h o m/s | Alta | El viento reduce o detiene el izaje. |
| Ángulo de giro | Orientación de la pluma | grados | Media | Ubica la carga sobre la obra. |
| Nivel de la base | Nivelación del mástil | grados | Alta | Confirma base estabilizada. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Subir/bajar gancho | Teclas W/S | Stick izquierdo vertical | Zona izaje | Proporcional, izaje lento. |
| Girar superestructura | Flechas izq/der | Stick izquierdo horizontal | Zona giro | Movimiento suave para no balancear. |
| Trasladar carro | Teclas R/F | Stick derecho vertical | Zona carro | Alejar baja la capacidad. |
| Freno de giro | Tecla G | Botón lateral | Panel giro | Liberar para veleta. |
| Parada de emergencia | Barra espaciadora | Botón dedicado | Botón rojo | Corta todos los movimientos. |
| Consultar viento | Tecla V | Botón info | Panel anemómetro | Decide si se puede izar. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Fuera de servicio | Detenida, giro en veleta | Freno de giro liberado | Poner en servicio si el viento baja. |
| Preparada | Encendida y nivelada | Nivel en verde | Habilitar izaje. |
| Izando | Levantando o moviendo carga | Limitador activo | Izar, girar, trasladar carro. |
| Viento alto | Viento sobre el límite | Alarma de anemómetro | Bajar carga, pasar a veleta. |
| Emergencia | Limitador en tope o falla | Alarma y luz roja | Parar, reducir radio, bajar carga. |

## Observaciones ergonomicas y de seguridad

- El limitador de momento debe estar siempre visible y ser el primer instrumento del campo de visión.
- Las palancas proporcionales evitan movimientos bruscos que balancean la carga.
- El sistema debe impedir el izaje si la grúa no está nivelada o si el viento supera el límite.
- La parada de emergencia debe ser grande, roja y accesible sin mirar.
- En simulación conviene mostrar el radio y el porcentaje de capacidad de forma
  continua, para que el usuario relacione cada movimiento con la estabilidad.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-torre.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-grua-torre.md)
