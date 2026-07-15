# 🎛️ Mandos e instrumentos del tanque (marco público)

[🏠 Inicio](../../../README.md) · [🪖 Curso: Tanques](../README.md) · 🎛️ Mandos

## Vista general

Este módulo describe **solo el puesto del conductor** a nivel general educativo:
cómo se mueve el vehículo. No trata puestos ni sistemas de combate, en línea con
[`docs/04-seguridad-y-limites.md`](../../../docs/04-seguridad-y-limites.md). El
conductor gobierna motor, transmisión y dirección diferencial, guiado por
instrumentos de movilidad.

## Mapa de controles de conducción

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Manos | Dirección | Palancas o volante | Variar velocidad de cada oruga | Alta | Dirección diferencial. |
| Pies | Acelerador | Pedal | Regular potencia del motor | Alta | Progresivo. |
| Pies | Freno | Pedal | Reducir velocidad | Alta | Frena ambas orugas. |
| Mano | Cambio de marcha | Palanca o selector | Adaptar fuerza y velocidad | Alta | Según transmisión. |
| Panel | Arranque y paro | Botones | Encender o apagar motor | Alta | Incluye corte del motor. |
| Panel | Luces | Interruptores | Iluminación de marcha | Media | Conducción de día y noche. |
| Puesto | Escotilla | Palanca | Abrir o cerrar la posición | Media | Conducción abierta o cerrada. |

## Instrumentos de movilidad

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocímetro | Velocidad | km/h | Alta | Para marcha segura. |
| Tacómetro | Régimen del motor | rpm | Media | Ayuda a elegir la marcha. |
| Temperatura del motor | Estado térmico | grados | Alta | Evita sobrecalentar. |
| Nivel de combustible | Combustible restante | fracción | Alta | Autonomía. |
| Presión de aceite | Lubricación | bar | Media | Fiabilidad del motor. |
| Testigos | Estado de sistemas | luz | Alta | Alertas de conducción. |

## Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Progresivo. |
| Frenar | Flecha abajo | Gatillo izquierdo | Frena ambas orugas. |
| Girar izquierda | Flecha izquierda | Stick izquierdo | Reduce la oruga izquierda. |
| Girar derecha | Flecha derecha | Stick derecho | Reduce la oruga derecha. |
| Cambiar marcha | E / Q | Cruceta | Subir o bajar según transmisión. |
| Luces | Tecla L | Botón asignado | Día o noche. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Panel off | Encender. |
| Preparado | Motor encendido, detenido | Testigos normales | Meter marcha, avanzar. |
| En movimiento | Avanzando en terreno | Velocímetro activo | Acelerar, frenar, girar. |
| Obstáculo | Pendiente o zanja | Alerta de inclinación | Reducir, elegir línea. |
| Alerta | Falla o riesgo | Testigos de alerta | Detener, revisar. |

## Observaciones ergonomicas

- Velocímetro, temperatura y combustible deben verse siempre.
- La dirección diferencial debe sentirse clara: girar es variar cada oruga.
- El corte de motor debe ser accesible y reconocible.
- La simulación se limita a la conducción; no representa sistemas sensibles.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-tanque.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-tanque.md)
