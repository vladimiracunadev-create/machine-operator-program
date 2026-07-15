# 🎛️ Mandos e instrumentos del bus

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un bus es amplio y ergonomico, pensado para largas
jornadas. El conductor va sentado frente a un volante grande de dirección
asistida, con pedales al estilo automóvil (sin embrague en cajas automáticas),
un selector de marchas, el control de puertas al alcance de la mano y un tablero
que incluye la presión de aire del sistema neumático.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Pie derecho | Acelerador | Pedal | Regular potencia del motor | Alta | Progresivo, con carga en mente. |
| Pie derecho | Freno de servicio | Pedal | Frenar por sistema neumático | Alta | Modular para no desestabilizar de pie. |
| Columna | Volante | Volante | Dirigir el bus | Alta | Dirección asistida, giros amplios. |
| Consola | Selector de transmisión | Palanca o botonera | Elegir D, N, R | Alta | Automática, sin embrague. |
| Consola | Retardador | Palanca o pedal | Freno auxiliar sin fricción | Alta | Escalonado, para descensos largos. |
| Panel puerta | Control de puertas | Botones | Abrir y cerrar puertas | Alta | Con enclavamiento de marcha. |
| Consola | Kneeling (arrodillamiento) | Botón | Bajar el lado de la puerta | Media | Facilita el ascenso accesible. |
| Consola | Rampa | Botón | Desplegar rampa de accesibilidad | Media | Para sillas de ruedas. |
| Tablero | Freno de estacionamiento | Válvula/botón | Aplicar freno de muelle | Alta | Obligatorio al detener y estacionar. |
| Columna | Luces e intermitentes | Palanca | Señalizar y alumbrar | Media | Incluye luces de parada. |
| Volante | Bocina | Botón | Advertir | Media | Uso de seguridad. |
| Tablero | Instrumentos | Panel | Mostrar estado | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad | km/h | Alta | Central para circulación segura. |
| Manómetro de aire | Presión del sistema neumático | bar/psi | Alta | No arrancar bajo el mínimo. |
| Tacómetro | Régimen del motor | rpm | Media | Ayuda en pendientes y freno motor. |
| Temperatura motor | Estado térmico | grados | Media | Vigila sobrecalentamiento. |
| Nivel de combustible | Combustible o carga | fracción/% | Alta | Diesel, gas o batería. |
| Testigos | Estado de sistemas | luz | Alta | Puertas, ABS, presión baja, retardador. |
| Indicador de puertas | Puertas abiertas/cerradas | luz | Alta | Ligado al enclavamiento de marcha. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Progresivo, con inercia de carga. |
| Frenar | Flecha abajo | Gatillo izquierdo | Botón freno | Modular para pasajeros de pie. |
| Retardador | Tecla R | Botón lateral | Botón retardador | Escalonado, sin desgaste. |
| Girar | Flechas izq/der | Stick izquierdo | Inclinar dispositivo | Anticipar el barrido trasero. |
| Cambiar D/N/R | Teclas D/N/R | Cruceta | Botones D/N/R | Automática, sin embrague. |
| Abrir puertas | Tecla O | Botón A | Botón puertas | Solo con el bus detenido. |
| Cerrar puertas | Tecla C | Botón B | Botón puertas | Verificar sensores antes. |
| Kneeling | Tecla K | Botón inferior | Botón kneeling | Baja el lado de la puerta. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido, sin presión | Tablero off | Encender, esperar carga de aire. |
| Cargando aire | Motor en marcha, subiendo presión | Alarma de presión baja | Esperar rango normal antes de mover. |
| Preparado | Presión normal, detenido | Manómetro en verde | Soltar freno, abrir puertas, seleccionar D. |
| En servicio | Circulando con pasajeros | Velocímetro activo | Acelerar, frenar, girar, parar en paradas. |
| En parada | Detenido con puertas abiertas | Testigo de puertas | Ascenso/descenso; marcha enclavada. |
| Emergencia | Riesgo o falla | Testigos de alerta | Frenar, orillar, freno de estacionamiento. |

## Observaciones ergonomicas

- El velocímetro y el manómetro de aire deben verse siempre.
- El control de puertas debe estar claramente separado del resto para evitar
  aperturas accidentales en marcha.
- El enclavamiento de marcha con puertas abiertas es una salvaguarda clave: la
  interfaz debe impedir avanzar con puertas abiertas en niveles realistas.
- El retardador conviene representarlo escalonado, para enseñar a frenar
  descensos largos sin castigar los frenos de servicio.
- La suavidad del frenado debe premiarse: los pasajeros de pie penalizan las
  maniobras bruscas.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-bus.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-bus.md)
