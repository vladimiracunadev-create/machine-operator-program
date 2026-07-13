# 🎛️ Mandos e instrumentos del submarino

[🏠 Inicio](../../../README.md) · [🌊 Curso: Submarinos](../README.md) · 🎛️ Mandos

## Vista general

Este modulo describe, **a nivel educativo y solo para simulacion**, el puesto de
control de un submarino. No representa operacion militar real ni sistemas de
armas: se limita a la flotabilidad, el gobierno en profundidad, la propulsion y
los instrumentos basicos. El control se concentra en un puesto central donde la
tripulacion coordina rumbo, profundidad y lastre.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puesto central | Timon vertical | Rueda o palanca | Cambiar el rumbo | Alta | Gobierno horizontal. |
| Puesto central | Planos de inmersion | Palancas | Ajustar angulo y profundidad | Alta | Control fino en movimiento. |
| Puesto central | Control de lastre | Panel | Inundar o purgar tanques | Alta | Flotabilidad general. |
| Puesto central | Telegrafo / control de maquina | Palanca | Ordenar potencia | Alta | Avante, atras, parado. |
| Puesto central | Aire comprimido | Valvulas | Emerger de emergencia | Alta | Concepto de seguridad. |
| Puesto central | Comunicaciones internas | Panel | Coordinar la tripulacion | Media | Ordenes de maniobra. |
| Puesto central | Alarmas | Panel | Avisar fallas | Alta | Presion, energia, aire. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Profundimetro | Profundidad | metros | Alta | Central en inmersion. |
| Manometro | Presion externa | atmosferas | Alta | Crece con la profundidad. |
| Compas / giroscopica | Rumbo | grados | Alta | Referencia de direccion. |
| Indicador de lastre | Estado de tanques | fraccion | Alta | Agua o aire en tanques. |
| Inclinometro | Angulo de cabeceo | grados | Alta | Control de la inmersion. |
| Nivel de oxigeno | Aire respirable | porcentaje | Alta | Soporte vital. |
| Carga de bateria | Energia disponible | porcentaje | Alta | Autonomia sumergido. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda tactil | Timon vertical. |
| Sumergir | Tecla S | Gatillo izquierdo | Boton descenso | Inunda lastre / planos abajo. |
| Emerger | Tecla W | Gatillo derecho | Boton ascenso | Purga lastre / planos arriba. |
| Ajustar profundidad | Flechas arriba/abajo | Stick derecho | Deslizador | Planos de inmersion. |
| Ordenar avante | Tecla E | Cruceta arriba | Palanca telegrafo | Escalonado por regimenes. |
| Parar maquina | Tecla P | Boton central | Boton parado | Regimen cero. |
| Emersion de emergencia | Barra espaciadora | Boton R1 | Boton emergencia | Aire comprimido a tanques. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Superficie | Flotando, escotillas usables | Profundidad cero | Cargar bateria, ventilar. |
| Inmersion | Sumergiendo | Lastre inundandose | Ajustar planos y cota. |
| En cota | Navegando sumergido | Profundidad estable | Rumbo, velocidad, vigilancia. |
| Emersion | Subiendo a superficie | Lastre purgandose | Controlar ascenso. |
| Emergencia | Falla o riesgo | Alarmas activas | Emersion de emergencia, achique. |

## Observaciones ergonomicas

- La profundidad, la presion y el rumbo deben verse en todo momento.
- El control de lastre y los planos deben distinguirse con claridad.
- El nivel de oxigeno y la carga de bateria deben estar siempre visibles.
- La emersion de emergencia debe ser un control accesible y reconocible.
- Toda la interfaz debe dejar claro que es una **simulacion educativa**, no
  operacion real ni entrenamiento militar.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-submarino.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-submarino.md)
