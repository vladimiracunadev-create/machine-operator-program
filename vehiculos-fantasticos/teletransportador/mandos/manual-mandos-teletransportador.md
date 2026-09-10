---
tipo_documento: clase
clase: 5
codigo: TELETRANSPOR-05
curso: teletransportador
titulo: "Mandos e instrumentos del teletransportador"
modalidad: "taller de simulación"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TELETRANSPOR-04
competencia: "lectura_y_mando"
resultados_aprendizaje:
  - "Explicar controles, instrumentos, entradas y estados del sistema con vocabulario propio de Teletransportador."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Teletransportador."
evidencia: "Mapa de mandos y resolución de dos estados del tablero."
criterio_aprobacion: "Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

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

## 🎓 Cierre de clase

- **Actividad:** Recorre el puesto de mando simulado de Teletransportador: localiza los controles de controles, instrumentos, entradas y estados del sistema y asocia cada indicación con una decisión.
- **Evidencia:** Mapa de mandos y resolución de dos estados del tablero.
- **Criterio de aprobación:** Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [STARTREK-DATABASE](https://www.startrek.com/database): Star Trek Database, Paramount. Uso: canon narrativo y tecnologías de ficción.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-teletransportador.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-teletransportador.md)
