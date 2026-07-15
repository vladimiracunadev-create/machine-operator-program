# 🎛️ Mandos e instrumentos del submarino

[🏠 Inicio](../../../README.md) · [🌊 Curso: Submarinos](../README.md) · 🎛️ Mandos

## Vista general

Este módulo describe, **a nivel educativo y solo para simulación**, el puesto de
control de un submarino. No representa operación militar real ni sistemas de
armas: se limita a la flotabilidad, el gobierno en profundidad, la propulsión y
los instrumentos básicos. El control se concentra en un puesto central donde la
tripulación coordina rumbo, profundidad y lastre.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puesto central | Timón vertical | Rueda o palanca | Cambiar el rumbo | Alta | Gobierno horizontal. |
| Puesto central | Planos de inmersión | Palancas | Ajustar ángulo y profundidad | Alta | Control fino en movimiento. |
| Puesto central | Control de lastre | Panel | Inundar o purgar tanques | Alta | Flotabilidad general. |
| Puesto central | Telégrafo / control de máquina | Palanca | Ordenar potencia | Alta | Avante, atrás, parado. |
| Puesto central | Aire comprimido | Válvulas | Emerger de emergencia | Alta | Concepto de seguridad. |
| Puesto central | Comunicaciones internas | Panel | Coordinar la tripulación | Media | Ordenes de maniobra. |
| Puesto central | Alarmas | Panel | Avisar fallas | Alta | Presión, energía, aire. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Profundímetro | Profundidad | metros | Alta | Central en inmersión. |
| Manómetro | Presión externa | atmósferas | Alta | Crece con la profundidad. |
| Compás / giroscópica | Rumbo | grados | Alta | Referencia de dirección. |
| Indicador de lastre | Estado de tanques | fracción | Alta | Agua o aire en tanques. |
| Inclinómetro | Ángulo de cabeceo | grados | Alta | Control de la inmersión. |
| Nivel de oxígeno | Aire respirable | porcentaje | Alta | Soporte vital. |
| Carga de batería | Energía disponible | porcentaje | Alta | Autonomía sumergido. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda táctil | Timón vertical. |
| Sumergir | Tecla S | Gatillo izquierdo | Botón descenso | Inunda lastre / planos abajo. |
| Emerger | Tecla W | Gatillo derecho | Botón ascenso | Purga lastre / planos arriba. |
| Ajustar profundidad | Flechas arriba/abajo | Stick derecho | Deslizador | Planos de inmersión. |
| Ordenar avante | Tecla E | Cruceta arriba | Palanca telégrafo | Escalonado por regímenes. |
| Parar máquina | Tecla P | Botón central | Botón parado | Régimen cero. |
| Emersión de emergencia | Barra espaciadora | Botón R1 | Botón emergencia | Aire comprimido a tanques. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Superficie | Flotando, escotillas usables | Profundidad cero | Cargar batería, ventilar. |
| Inmersión | Sumergiendo | Lastre inundandose | Ajustar planos y cota. |
| En cota | Navegando sumergido | Profundidad estable | Rumbo, velocidad, vigilancia. |
| Emersión | Subiendo a superficie | Lastre purgandose | Controlar ascenso. |
| Emergencia | Falla o riesgo | Alarmas activas | Emersión de emergencia, achique. |

## Observaciones ergonomicas

- La profundidad, la presión y el rumbo deben verse en todo momento.
- El control de lastre y los planos deben distinguirse con claridad.
- El nivel de oxígeno y la carga de batería deben estar siempre visibles.
- La emersión de emergencia debe ser un control accesible y reconocible.
- Toda la interfaz debe dejar claro que es una **simulación educativa**, no
  operación real ni entrenamiento militar.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-submarino.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-submarino.md)
