# 🎛️ Mandos e instrumentos del teletransportador

[🏠 Inicio](../../../README.md) · [🌀 Curso: Teletransportador](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puesto de mando de un teletransportador realista se parece más a la consola
de un centro de datos que al panel de una nave. Como el aparato no mueve
materia sino que mide, transmite y reconstruye información, el operador no
"conduce": gestiona por separado el escaneo del origen, el canal de
transmisión y la reconstrucción en destino. Esa separación es la gran
diferencia con imaginar un simple botón de "enviar".

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano derecha | Selector de origen | Perilla | Elegir el objeto a escanear | Alta | Define el volumen de datos. |
| Mano izquierda | Ajuste de resolución | Palanca lineal | Regular el detalle del escaneo | Alta | Más detalle, más información. |
| Panel central | Gestión de energía | Botonera | Repartir energía entre etapas | Alta | Escaneo, canal y reconstrucción. |
| Panel derecho | Control del canal | Botones | Abrir y cerrar la transmisión | Alta | Limitada por la velocidad de la luz. |
| Panel izquierdo | Modo de proceso | Selector | Elegir copia o transferencia | Media | Afecta al problema del duplicado. |
| Panel superior | Confirmación de destino | Interruptor | Autorizar la reconstrucción | Alta | Requiere materia local disponible. |
| Consola | Instrumentos | Pantallas | Mostrar estado del proceso | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Volumen de datos | Información del patrón leído | bits | Alta | Crece muchísimo con el detalle. |
| Progreso del canal | Fracción transmitida | porcentaje | Alta | Limitado por la velocidad de la luz. |
| Energía acumulada | Energía usada en el proceso | julios | Alta | Escala colosal por masa-energía. |
| Integridad del patrón | Errores detectados | tasa | Alta | Un error sería grave en destino. |
| Materia local | Reserva en el destino | porcentaje | Alta | Sin materia no hay reconstrucción. |
| Estado del original | Intacto, medido o borrado | discreto | Alta | Clave para el problema del duplicado. |

## Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Iniciar escaneo | Flecha arriba | Gatillo derecho | Empieza a leer el patrón. |
| Subir resolución | W y S | Stick derecho vertical | Más detalle, más datos. |
| Abrir canal | A y D | Stick derecho horizontal | Transmite la información. |
| Elegir modo | Q y E | Botones laterales | Copia o transferencia de estado. |
| Cargar materia | J y L | Stick izquierdo | Prepara la reserva de destino. |
| Confirmar destino | Barra espaciadora | Botón central | Autoriza la reconstrucción. |
| Abortar proceso | Ctrl | Gatillo izquierdo | Detiene y protege el original. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En espera | Aparato listo, sin proceso activo | Volumen de datos en cero | Elegir origen, ajustar resolución. |
| Escaneando | Leyendo el patrón del origen | Volumen de datos subiendo | Ajustar detalle, abortar. |
| Transmitiendo | Enviando información por el canal | Progreso del canal activo | Vigilar integridad, abortar. |
| Reconstruyendo | Ensamblando materia en destino | Materia local bajando | Confirmar o abortar. |
| Emergencia | Falla, error o falta de materia | Alerta de integridad | Proteger el original, estabilizar. |

## Observaciones ergonomicas

- La interfaz debe mostrar a la vez cuanta información falta por transmitir y
  cuanta energía lleva gastada, porque ambas escalas son enormes.
- El estado del original es tan importante como el progreso del destino: de el
  depende si hay copia, traslado o duplicado.
- El aborto debe ser evidente y seguro: nunca dejar un patrón a medias en
  destino sin proteger el objeto de origen.
- Conviene un modo de asistencia para principiantes que explique cada límite
  físico al activarse (datos, energía, no clonación).

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-teletransportador.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-teletransportador.md)
