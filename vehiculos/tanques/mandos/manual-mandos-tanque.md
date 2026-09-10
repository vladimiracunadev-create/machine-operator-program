---
tipo_documento: clase
clase: 5
codigo: TANQUES-05
curso: tanques
titulo: "Mandos e instrumentos del tanque (marco público)"
modalidad: "taller de simulación"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TANQUES-04
competencia: "lectura_y_mando"
resultados_aprendizaje:
  - "Explicar controles, instrumentos, entradas y estados del sistema con vocabulario propio de Tanques."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tanques."
evidencia: "Mapa de mandos y resolución de dos estados del tablero."
criterio_aprobacion: "Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

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

## 🎓 Cierre de clase

- **Actividad:** Recorre el puesto de mando simulado de Tanques: localiza los controles de controles, instrumentos, entradas y estados del sistema y asocia cada indicación con una decisión.
- **Evidencia:** Mapa de mandos y resolución de dos estados del tablero.
- **Criterio de aprobación:** Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [TANK-MUSEUM](https://tankmuseum.org/tank-nuts/tank-collection): Tank Collection, The Tank Museum. Uso: historia pública de vehículos blindados.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-tanque.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-tanque.md)
