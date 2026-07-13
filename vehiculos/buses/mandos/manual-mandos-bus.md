# 🎛️ Mandos e instrumentos del bus

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un bus es amplio y ergonomico, pensado para largas
jornadas. El conductor va sentado frente a un volante grande de direccion
asistida, con pedales al estilo automovil (sin embrague en cajas automaticas),
un selector de marchas, el control de puertas al alcance de la mano y un tablero
que incluye la presion de aire del sistema neumatico.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Pie derecho | Acelerador | Pedal | Regular potencia del motor | Alta | Progresivo, con carga en mente. |
| Pie derecho | Freno de servicio | Pedal | Frenar por sistema neumatico | Alta | Modular para no desestabilizar de pie. |
| Columna | Volante | Volante | Dirigir el bus | Alta | Direccion asistida, giros amplios. |
| Consola | Selector de transmision | Palanca o botonera | Elegir D, N, R | Alta | Automatica, sin embrague. |
| Consola | Retardador | Palanca o pedal | Freno auxiliar sin friccion | Alta | Escalonado, para descensos largos. |
| Panel puerta | Control de puertas | Botones | Abrir y cerrar puertas | Alta | Con enclavamiento de marcha. |
| Consola | Kneeling (arrodillamiento) | Boton | Bajar el lado de la puerta | Media | Facilita el ascenso accesible. |
| Consola | Rampa | Boton | Desplegar rampa de accesibilidad | Media | Para sillas de ruedas. |
| Tablero | Freno de estacionamiento | Valvula/boton | Aplicar freno de muelle | Alta | Obligatorio al detener y estacionar. |
| Columna | Luces e intermitentes | Palanca | Senalizar y alumbrar | Media | Incluye luces de parada. |
| Volante | Bocina | Boton | Advertir | Media | Uso de seguridad. |
| Tablero | Instrumentos | Panel | Mostrar estado | Alta | Ver seccion de instrumentos. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocimetro | Velocidad | km/h | Alta | Central para circulacion segura. |
| Manometro de aire | Presion del sistema neumatico | bar/psi | Alta | No arrancar bajo el minimo. |
| Tacometro | Regimen del motor | rpm | Media | Ayuda en pendientes y freno motor. |
| Temperatura motor | Estado termico | grados | Media | Vigila sobrecalentamiento. |
| Nivel de combustible | Combustible o carga | fraccion/% | Alta | Diesel, gas o bateria. |
| Testigos | Estado de sistemas | luz | Alta | Puertas, ABS, presion baja, retardador. |
| Indicador de puertas | Puertas abiertas/cerradas | luz | Alta | Ligado al enclavamiento de marcha. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Progresivo, con inercia de carga. |
| Frenar | Flecha abajo | Gatillo izquierdo | Boton freno | Modular para pasajeros de pie. |
| Retardador | Tecla R | Boton lateral | Boton retardador | Escalonado, sin desgaste. |
| Girar | Flechas izq/der | Stick izquierdo | Inclinar dispositivo | Anticipar el barrido trasero. |
| Cambiar D/N/R | Teclas D/N/R | Cruceta | Botones D/N/R | Automatica, sin embrague. |
| Abrir puertas | Tecla O | Boton A | Boton puertas | Solo con el bus detenido. |
| Cerrar puertas | Tecla C | Boton B | Boton puertas | Verificar sensores antes. |
| Kneeling | Tecla K | Boton inferior | Boton kneeling | Baja el lado de la puerta. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido, sin presion | Tablero off | Encender, esperar carga de aire. |
| Cargando aire | Motor en marcha, subiendo presion | Alarma de presion baja | Esperar rango normal antes de mover. |
| Preparado | Presion normal, detenido | Manometro en verde | Soltar freno, abrir puertas, seleccionar D. |
| En servicio | Circulando con pasajeros | Velocimetro activo | Acelerar, frenar, girar, parar en paradas. |
| En parada | Detenido con puertas abiertas | Testigo de puertas | Ascenso/descenso; marcha enclavada. |
| Emergencia | Riesgo o falla | Testigos de alerta | Frenar, orillar, freno de estacionamiento. |

## Observaciones ergonomicas

- El velocimetro y el manometro de aire deben verse siempre.
- El control de puertas debe estar claramente separado del resto para evitar
  aperturas accidentales en marcha.
- El enclavamiento de marcha con puertas abiertas es una salvaguarda clave: la
  interfaz debe impedir avanzar con puertas abiertas en niveles realistas.
- El retardador conviene representarlo escalonado, para ensenar a frenar
  descensos largos sin castigar los frenos de servicio.
- La suavidad del frenado debe premiarse: los pasajeros de pie penalizan las
  maniobras bruscas.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-bus.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-bus.md)
