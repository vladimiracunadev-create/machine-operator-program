# 🎛️ Mandos e instrumentos del teletransportador

[🏠 Inicio](../../../README.md) · [🌀 Curso: Teletransportador](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puesto de mando de un teletransportador realista se parece mas a la consola
de un centro de datos que al panel de una nave. Como el aparato no mueve
materia sino que mide, transmite y reconstruye informacion, el operador no
"conduce": gestiona por separado el escaneo del origen, el canal de
transmision y la reconstruccion en destino. Esa separacion es la gran
diferencia con imaginar un simple boton de "enviar".

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano derecha | Selector de origen | Perilla | Elegir el objeto a escanear | Alta | Define el volumen de datos. |
| Mano izquierda | Ajuste de resolucion | Palanca lineal | Regular el detalle del escaneo | Alta | Mas detalle, mas informacion. |
| Panel central | Gestion de energia | Botonera | Repartir energia entre etapas | Alta | Escaneo, canal y reconstruccion. |
| Panel derecho | Control del canal | Botones | Abrir y cerrar la transmision | Alta | Limitada por la velocidad de la luz. |
| Panel izquierdo | Modo de proceso | Selector | Elegir copia o transferencia | Media | Afecta al problema del duplicado. |
| Panel superior | Confirmacion de destino | Interruptor | Autorizar la reconstruccion | Alta | Requiere materia local disponible. |
| Consola | Instrumentos | Pantallas | Mostrar estado del proceso | Alta | Ver seccion de instrumentos. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Volumen de datos | Informacion del patron leido | bits | Alta | Crece muchisimo con el detalle. |
| Progreso del canal | Fraccion transmitida | porcentaje | Alta | Limitado por la velocidad de la luz. |
| Energia acumulada | Energia usada en el proceso | julios | Alta | Escala colosal por masa-energia. |
| Integridad del patron | Errores detectados | tasa | Alta | Un error seria grave en destino. |
| Materia local | Reserva en el destino | porcentaje | Alta | Sin materia no hay reconstruccion. |
| Estado del original | Intacto, medido o borrado | discreto | Alta | Clave para el problema del duplicado. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Iniciar escaneo | Flecha arriba | Gatillo derecho | Empieza a leer el patron. |
| Subir resolucion | W y S | Stick derecho vertical | Mas detalle, mas datos. |
| Abrir canal | A y D | Stick derecho horizontal | Transmite la informacion. |
| Elegir modo | Q y E | Botones laterales | Copia o transferencia de estado. |
| Cargar materia | J y L | Stick izquierdo | Prepara la reserva de destino. |
| Confirmar destino | Barra espaciadora | Boton central | Autoriza la reconstruccion. |
| Abortar proceso | Ctrl | Gatillo izquierdo | Detiene y protege el original. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En espera | Aparato listo, sin proceso activo | Volumen de datos en cero | Elegir origen, ajustar resolucion. |
| Escaneando | Leyendo el patron del origen | Volumen de datos subiendo | Ajustar detalle, abortar. |
| Transmitiendo | Enviando informacion por el canal | Progreso del canal activo | Vigilar integridad, abortar. |
| Reconstruyendo | Ensamblando materia en destino | Materia local bajando | Confirmar o abortar. |
| Emergencia | Falla, error o falta de materia | Alerta de integridad | Proteger el original, estabilizar. |

## Observaciones ergonomicas

- La interfaz debe mostrar a la vez cuanta informacion falta por transmitir y
  cuanta energia lleva gastada, porque ambas escalas son enormes.
- El estado del original es tan importante como el progreso del destino: de el
  depende si hay copia, traslado o duplicado.
- El aborto debe ser evidente y seguro: nunca dejar un patron a medias en
  destino sin proteger el objeto de origen.
- Conviene un modo de asistencia para principiantes que explique cada limite
  fisico al activarse (datos, energia, no clonacion).

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-teletransportador.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-teletransportador.md)
