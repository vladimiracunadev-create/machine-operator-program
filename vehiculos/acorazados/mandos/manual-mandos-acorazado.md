# 🎛️ Mandos e instrumentos del acorazado

[🏠 Inicio](../../../README.md) · [🛡️ Curso: Acorazados](../README.md) · 🎛️ Mandos

## Vista general

Este módulo describe, **a nivel educativo y solo para simulación**, el puente de
navegación de un gran buque. No representa operación militar real ni incluye
sistemas de combate: se limita al gobierno, la propulsión y la navegación, igual
que en cualquier buque de gran porte. El puente se ubica en alto para tener buena
visibilidad.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puente | Timón / rueda de gobierno | Rueda o palanca | Cambiar el rumbo | Alta | Actua sobre la pala del timón. |
| Puente | Telégrafo de máquina | Palanca de rango | Ordenar potencia y sentido | Alta | Avante, atrás, parado. |
| Puente | Piloto de rumbo | Selector | Mantener rumbo fijo | Media | Para travesía sostenida. |
| Puente | Comunicaciones internas | Panel | Coordinar la tripulación | Media | Ordenes de navegación. |
| Puente | Señales acústicas | Botón | Señalizar maniobras | Alta | Según reglas de navegación. |
| Puente | Luces de navegación | Interruptores | Ser visto de noche | Alta | Configuración COLREG. |
| Puente | Control de flotabilidad | Panel simulado | Gestionar lastre y achique | Alta | Concepto de seguridad, no combate. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Compás / giroscópica | Rumbo | grados | Alta | Referencia de dirección. |
| Corredera | Velocidad respecto al agua | nudos | Alta | Central para navegar. |
| Indicador de timón | Ángulo de la pala | grados | Media | Confirma la orden. |
| Indicador de máquina | Régimen de propulsión | rpm | Media | Estado de la planta. |
| Inclinómetro | Escora | grados | Alta | Vigila estabilidad. |
| Sonda | Profundidad bajo la quilla | metros | Alta | Evita varar. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda táctil | Respuesta lenta por inercia. |
| Ordenar avante | Flecha arriba | Gatillo derecho | Palanca telégrafo | Escalonado por regímenes. |
| Ordenar atrás | Flecha abajo | Gatillo izquierdo | Palanca telégrafo | Detención muy progresiva. |
| Parar máquina | Tecla P | Botón central | Botón parado | Ordena régimen cero. |
| Mantener rumbo | Tecla H | Botón dedicado | Interruptor | Piloto de rumbo. |
| Señal acústica | Barra espaciadora | Botón R1 | Botón bocina | Según maniobra. |
| Ajustar lastre | Teclas L | Cruceta | Panel flotabilidad | Concepto de estabilidad. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Atracado | En muelle, amarrado | Máquina parada | Preparar zarpe, revisar sistemas. |
| Maniobra | Entrando o saliendo de puerto | Baja velocidad | Gobierno fino, señales. |
| Navegación | En travesía | Piloto de rumbo | Rumbo, vigilancia, guardias. |
| Fondeado | Al ancla | Ancla desplegada | Vigilar garreo, guardia. |
| Emergencia | Riesgo o vía de agua | Alarmas activas | Achique, contrainundación, auxilio. |

## Observaciones ergonomicas

- El puente debe ofrecer buena visión del entorno y del propio buque.
- El rumbo, la velocidad y la escora deben verse en todo momento.
- La simulación debe reflejar el gran retardo entre orden y respuesta.
- Toda la interfaz debe dejar claro que es una **simulación educativa**, no
  operación real ni entrenamiento militar.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-acorazado.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-acorazado.md)
