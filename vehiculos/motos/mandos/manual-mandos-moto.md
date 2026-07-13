# Manual de mandos: moto

## Vista general

El puesto de mando de una motocicleta se concentra en el manillar y en los
apoyos para pies. A diferencia de un automovil, casi todos los controles se
operan con las manos y los pies sin soltar la posicion de conduccion. El
tablero, hoy digital o mixto, se ubica al centro sobre la horquilla.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puno derecho | Acelerador | Puno giratorio | Regular potencia del motor | Alta | Se acciona girando hacia el conductor. |
| Puno derecho | Freno delantero | Maneta | Frenar rueda delantera | Alta | Aporta la mayor capacidad de frenado. |
| Puno izquierdo | Embrague | Maneta | Desconectar motor y transmision | Alta | Necesario para cambiar de marcha. |
| Pie derecho | Freno trasero | Pedal | Frenar rueda trasera | Alta | Estabiliza y complementa al delantero. |
| Pie izquierdo | Cambio de marchas | Palanca | Subir o bajar de marcha | Alta | Patron tipico 1-N-2-3-4-5-6. |
| Manillar izquierdo | Luces e intermitentes | Botones | Senalizar y alumbrar | Media | Incluye luces de cruce y carretera. |
| Manillar izquierdo | Bocina | Boton | Advertir | Media | Uso de seguridad. |
| Manillar derecho | Arranque y paro | Botones | Encender o cortar motor | Alta | Incluye corte de emergencia. |
| Tablero | Instrumentos | Pantalla | Mostrar estado | Alta | Ver seccion de instrumentos. |
| Lateral | Caballete | Palanca | Estacionar | Baja | Puede tener corte de encendido asociado. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocimetro | Velocidad | km/h | Alta | Central para circulacion segura. |
| Tacometro | Regimen del motor | rpm | Media | Ayuda a elegir la marcha. |
| Indicador de marcha | Marcha actual | numero/N | Media | Comun en modelos modernos. |
| Nivel de combustible | Combustible restante | fraccion | Alta | Puede incluir reserva. |
| Testigos | Estado de sistemas | luz | Alta | Aceite, neutro, intermitentes, ABS. |
| Odometro | Distancia recorrida | km | Baja | Total y parcial. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Progresivo, no on/off. |
| Frenar delante | Tecla J | Gatillo izquierdo | Boton freno | Modula fuerza. |
| Frenar detras | Tecla K | Boton inferior | Boton freno trasero | Complementa al delantero. |
| Embragar | Shift | Boton lateral | Boton embrague | Requerido para cambiar. |
| Subir marcha | E | Cruceta arriba | Boton mas | Con embrague en niveles altos. |
| Bajar marcha | Q | Cruceta abajo | Boton menos | Reducir antes de curva. |
| Girar | Flechas izq/der | Stick izquierdo | Inclinacion | Combina giro e inclinacion. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Tablero off | Encender, mover en punto muerto. |
| Preparado | Motor encendido, detenida | Testigo de neutro | Embragar, meter primera. |
| En movimiento | Circulando | Velocimetro activo | Acelerar, frenar, cambiar, girar. |
| Emergencia | Riesgo o falla | Testigos de alerta | Frenar, orillar, cortar motor. |

## Observaciones ergonomicas

- El velocimetro y los testigos deben verse siempre.
- Acelerador y freno delantero conviven en la mano derecha: la interfaz debe
  dejar claro que no se accionan a la vez con la misma intensidad.
- El corte de motor de emergencia debe ser accesible y reconocible.
- La interfaz de simulacion deberia prevenir cambios de marcha sin embrague en
  los niveles de realismo mas altos.
