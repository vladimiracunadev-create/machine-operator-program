# 🎛️ Mandos e instrumentos de la moto

[🏠 Inicio](../../../README.md) · [🏍️ Curso: Motos](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de una motocicleta se concentra en el manillar y en los
apoyos para pies. A diferencia de un automóvil, casi todos los controles se
operan con las manos y los pies sin soltar la posición de conducción. El
tablero, hoy digital o mixto, se ubica al centro sobre la horquilla.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puño derecho | Acelerador | Puño giratorio | Regular potencia del motor | Alta | Se acciona girando hacia el conductor. |
| Puño derecho | Freno delantero | Maneta | Frenar rueda delantera | Alta | Aporta la mayor capacidad de frenado. |
| Puño izquierdo | Embrague | Maneta | Desconectar motor y transmisión | Alta | Necesario para cambiar de marcha. |
| Pie derecho | Freno trasero | Pedal | Frenar rueda trasera | Alta | Estabiliza y complementa al delantero. |
| Pie izquierdo | Cambio de marchas | Palanca | Subir o bajar de marcha | Alta | Patrón típico 1-N-2-3-4-5-6. |
| Manillar izquierdo | Luces e intermitentes | Botones | Señalizar y alumbrar | Media | Incluye luces de cruce y carretera. |
| Manillar izquierdo | Bocina | Botón | Advertir | Media | Uso de seguridad. |
| Manillar derecho | Arranque y paro | Botones | Encender o cortar motor | Alta | Incluye corte de emergencia. |
| Tablero | Instrumentos | Pantalla | Mostrar estado | Alta | Ver sección de instrumentos. |
| Lateral | Caballete | Palanca | Estacionar | Baja | Puede tener corte de encendido asociado. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad | km/h | Alta | Central para circulación segura. |
| Tacómetro | Régimen del motor | rpm | Media | Ayuda a elegir la marcha. |
| Indicador de marcha | Marcha actual | número/N | Media | Común en modelos modernos. |
| Nivel de combustible | Combustible restante | fracción | Alta | Puede incluir reserva. |
| Testigos | Estado de sistemas | luz | Alta | Aceite, neutro, intermitentes, ABS. |
| Odómetro | Distancia recorrida | km | Baja | Total y parcial. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Zona derecha | Progresivo, no on/off. |
| Frenar delante | Tecla J | Gatillo izquierdo | Botón freno | Modula fuerza. |
| Frenar detrás | Tecla K | Botón inferior | Botón freno trasero | Complementa al delantero. |
| Embragar | Shift | Botón lateral | Botón embrague | Requerido para cambiar. |
| Subir marcha | E | Cruceta arriba | Botón más | Con embrague en niveles altos. |
| Bajar marcha | Q | Cruceta abajo | Botón menos | Reducir antes de curva. |
| Girar | Flechas izq/der | Stick izquierdo | Inclinación | Combina giro e inclinación. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Tablero off | Encender, mover en punto muerto. |
| Preparado | Motor encendido, detenida | Testigo de neutro | Embragar, meter primera. |
| En movimiento | Circulando | Velocímetro activo | Acelerar, frenar, cambiar, girar. |
| Emergencia | Riesgo o falla | Testigos de alerta | Frenar, orillar, cortar motor. |

## Observaciones ergonomicas

- El velocímetro y los testigos deben verse siempre.
- Acelerador y freno delantero conviven en la mano derecha: la interfaz debe
  dejar claro que no se accionan a la vez con la misma intensidad.
- El corte de motor de emergencia debe ser accesible y reconocible.
- La interfaz de simulación debería prevenir cambios de marcha sin embrague en
  los niveles de realismo más altos.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-moto.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-moto.md)
