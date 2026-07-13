# 🎛️ Mandos e instrumentos del acorazado

[🏠 Inicio](../../../README.md) · [🛡️ Curso: Acorazados](../README.md) · 🎛️ Mandos

## Vista general

Este modulo describe, **a nivel educativo y solo para simulacion**, el puente de
navegacion de un gran buque. No representa operacion militar real ni incluye
sistemas de combate: se limita al gobierno, la propulsion y la navegacion, igual
que en cualquier buque de gran porte. El puente se ubica en alto para tener buena
visibilidad.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puente | Timon / rueda de gobierno | Rueda o palanca | Cambiar el rumbo | Alta | Actua sobre la pala del timon. |
| Puente | Telegrafo de maquina | Palanca de rango | Ordenar potencia y sentido | Alta | Avante, atras, parado. |
| Puente | Piloto de rumbo | Selector | Mantener rumbo fijo | Media | Para travesia sostenida. |
| Puente | Comunicaciones internas | Panel | Coordinar la tripulacion | Media | Ordenes de navegacion. |
| Puente | Senales acusticas | Boton | Senalizar maniobras | Alta | Segun reglas de navegacion. |
| Puente | Luces de navegacion | Interruptores | Ser visto de noche | Alta | Configuracion COLREG. |
| Puente | Control de flotabilidad | Panel simulado | Gestionar lastre y achique | Alta | Concepto de seguridad, no combate. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Compas / giroscopica | Rumbo | grados | Alta | Referencia de direccion. |
| Corredera | Velocidad respecto al agua | nudos | Alta | Central para navegar. |
| Indicador de timon | Angulo de la pala | grados | Media | Confirma la orden. |
| Indicador de maquina | Regimen de propulsion | rpm | Media | Estado de la planta. |
| Inclinometro | Escora | grados | Alta | Vigila estabilidad. |
| Sonda | Profundidad bajo la quilla | metros | Alta | Evita varar. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda tactil | Respuesta lenta por inercia. |
| Ordenar avante | Flecha arriba | Gatillo derecho | Palanca telegrafo | Escalonado por regimenes. |
| Ordenar atras | Flecha abajo | Gatillo izquierdo | Palanca telegrafo | Detencion muy progresiva. |
| Parar maquina | Tecla P | Boton central | Boton parado | Ordena regimen cero. |
| Mantener rumbo | Tecla H | Boton dedicado | Interruptor | Piloto de rumbo. |
| Senal acustica | Barra espaciadora | Boton R1 | Boton bocina | Segun maniobra. |
| Ajustar lastre | Teclas L | Cruceta | Panel flotabilidad | Concepto de estabilidad. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Atracado | En muelle, amarrado | Maquina parada | Preparar zarpe, revisar sistemas. |
| Maniobra | Entrando o saliendo de puerto | Baja velocidad | Gobierno fino, senales. |
| Navegacion | En travesia | Piloto de rumbo | Rumbo, vigilancia, guardias. |
| Fondeado | Al ancla | Ancla desplegada | Vigilar garreo, guardia. |
| Emergencia | Riesgo o via de agua | Alarmas activas | Achique, contrainundacion, auxilio. |

## Observaciones ergonomicas

- El puente debe ofrecer buena vision del entorno y del propio buque.
- El rumbo, la velocidad y la escora deben verse en todo momento.
- La simulacion debe reflejar el gran retardo entre orden y respuesta.
- Toda la interfaz debe dejar claro que es una **simulacion educativa**, no
  operacion real ni entrenamiento militar.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-acorazado.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-acorazado.md)
