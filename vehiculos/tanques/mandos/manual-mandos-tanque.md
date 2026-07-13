# 🎛️ Mandos e instrumentos del tanque (marco publico)

[🏠 Inicio](../../../README.md) · [🪖 Curso: Tanques](../README.md) · 🎛️ Mandos

## Vista general

Este modulo describe **solo el puesto del conductor** a nivel general educativo:
como se mueve el vehiculo. No trata puestos ni sistemas de combate, en linea con
[`docs/04-seguridad-y-limites.md`](../../../docs/04-seguridad-y-limites.md). El
conductor gobierna motor, transmision y direccion diferencial, guiado por
instrumentos de movilidad.

## Mapa de controles de conduccion

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Manos | Direccion | Palancas o volante | Variar velocidad de cada oruga | Alta | Direccion diferencial. |
| Pies | Acelerador | Pedal | Regular potencia del motor | Alta | Progresivo. |
| Pies | Freno | Pedal | Reducir velocidad | Alta | Frena ambas orugas. |
| Mano | Cambio de marcha | Palanca o selector | Adaptar fuerza y velocidad | Alta | Segun transmision. |
| Panel | Arranque y paro | Botones | Encender o apagar motor | Alta | Incluye corte del motor. |
| Panel | Luces | Interruptores | Iluminacion de marcha | Media | Conduccion de dia y noche. |
| Puesto | Escotilla | Palanca | Abrir o cerrar la posicion | Media | Conduccion abierta o cerrada. |

## Instrumentos de movilidad

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocimetro | Velocidad | km/h | Alta | Para marcha segura. |
| Tacometro | Regimen del motor | rpm | Media | Ayuda a elegir la marcha. |
| Temperatura del motor | Estado termico | grados | Alta | Evita sobrecalentar. |
| Nivel de combustible | Combustible restante | fraccion | Alta | Autonomia. |
| Presion de aceite | Lubricacion | bar | Media | Fiabilidad del motor. |
| Testigos | Estado de sistemas | luz | Alta | Alertas de conduccion. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Progresivo. |
| Frenar | Flecha abajo | Gatillo izquierdo | Frena ambas orugas. |
| Girar izquierda | Flecha izquierda | Stick izquierdo | Reduce la oruga izquierda. |
| Girar derecha | Flecha derecha | Stick derecho | Reduce la oruga derecha. |
| Cambiar marcha | E / Q | Cruceta | Subir o bajar segun transmision. |
| Luces | Tecla L | Boton asignado | Dia o noche. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Panel off | Encender. |
| Preparado | Motor encendido, detenido | Testigos normales | Meter marcha, avanzar. |
| En movimiento | Avanzando en terreno | Velocimetro activo | Acelerar, frenar, girar. |
| Obstaculo | Pendiente o zanja | Alerta de inclinacion | Reducir, elegir linea. |
| Alerta | Falla o riesgo | Testigos de alerta | Detener, revisar. |

## Observaciones ergonomicas

- Velocimetro, temperatura y combustible deben verse siempre.
- La direccion diferencial debe sentirse clara: girar es variar cada oruga.
- El corte de motor debe ser accesible y reconocible.
- La simulacion se limita a la conduccion; no representa sistemas sensibles.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-tanque.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-tanque.md)
