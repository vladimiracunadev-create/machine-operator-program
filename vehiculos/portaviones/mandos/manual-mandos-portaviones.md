# 🎛️ Mandos e instrumentos del portaviones

[🏠 Inicio](../../../README.md) · [🛳️ Curso: Portaviones](../README.md) · 🎛️ Mandos

## Vista general

Este módulo describe, **a nivel educativo y solo para simulación**, el puente de
navegación de un portaviones (ubicado en la isla lateral). No representa
operación militar real ni sistemas de armas: se limita al gobierno, la
propulsión, la navegación y la coordinación general de cubierta a nivel
divulgativo.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puente (isla) | Timón / rueda de gobierno | Rueda o palanca | Cambiar el rumbo | Alta | Actua sobre la pala del timón. |
| Puente | Telégrafo de máquina | Palanca de rango | Ordenar potencia y sentido | Alta | Avante, atrás, parado. |
| Puente | Piloto de rumbo | Selector | Mantener rumbo fijo | Media | Para travesía sostenida. |
| Puente | Comunicaciones internas | Panel | Coordinar la tripulación | Media | Ordenes de navegación. |
| Control de cubierta | Estado de cubierta | Panel simulado | Coordinar movimientos | Media | Solo logística general. |
| Puente | Señales acústicas | Botón | Señalizar maniobras | Alta | Según reglas de navegación. |
| Puente | Luces de navegación | Interruptores | Ser visto de noche | Alta | Configuración COLREG. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Compás / giroscópica | Rumbo | grados | Alta | Referencia de dirección. |
| Corredera | Velocidad respecto al agua | nudos | Alta | Central para navegar. |
| Anemómetro | Viento sobre cubierta | nudos | Alta | Relevante en operaciones de vuelo. |
| Indicador de timón | Ángulo de la pala | grados | Media | Confirma la orden. |
| Inclinómetro | Escora | grados | Alta | Estabilidad y seguridad en cubierta. |
| Sonda | Profundidad bajo la quilla | metros | Alta | Evita varar. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda táctil | Respuesta lenta por inercia. |
| Ordenar avante | Flecha arriba | Gatillo derecho | Palanca telégrafo | Escalonado por regímenes. |
| Ordenar atrás | Flecha abajo | Gatillo izquierdo | Palanca telégrafo | Detención muy progresiva. |
| Parar máquina | Tecla P | Botón central | Botón parado | Ordena régimen cero. |
| Mantener rumbo | Tecla H | Botón dedicado | Interruptor | Piloto de rumbo. |
| Rumbo al viento | Tecla W | Botón dedicado | Botón viento | Alinear con el viento relativo. |
| Señal acústica | Barra espaciadora | Botón R1 | Botón bocina | Según maniobra. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Atracado | En muelle, amarrado | Máquina parada | Preparar zarpe, revisar sistemas. |
| Maniobra | Entrando o saliendo de puerto | Baja velocidad | Gobierno fino, señales. |
| Navegación | En travesía | Piloto de rumbo | Rumbo, vigilancia, guardias. |
| Cubierta activa | Coordinación de cubierta | Estado de cubierta | Rumbo al viento, logística general. |
| Emergencia | Riesgo o vía de agua | Alarmas activas | Achique, contrainundación, auxilio. |

## Observaciones ergonomicas

- La isla debe ofrecer visión de la cubierta y del entorno.
- El rumbo, la velocidad, el viento y la escora deben verse en todo momento.
- La simulación debe reflejar el gran retardo entre orden y respuesta.
- Toda la interfaz debe dejar claro que es una **simulación educativa**, no
  operación real ni entrenamiento militar.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-portaviones.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-portaviones.md)
