# 🎛️ Mandos e instrumentos del portaviones

[🏠 Inicio](../../../README.md) · [🛳️ Curso: Portaviones](../README.md) · 🎛️ Mandos

## Vista general

Este modulo describe, **a nivel educativo y solo para simulacion**, el puente de
navegacion de un portaviones (ubicado en la isla lateral). No representa
operacion militar real ni sistemas de armas: se limita al gobierno, la
propulsion, la navegacion y la coordinacion general de cubierta a nivel
divulgativo.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puente (isla) | Timon / rueda de gobierno | Rueda o palanca | Cambiar el rumbo | Alta | Actua sobre la pala del timon. |
| Puente | Telegrafo de maquina | Palanca de rango | Ordenar potencia y sentido | Alta | Avante, atras, parado. |
| Puente | Piloto de rumbo | Selector | Mantener rumbo fijo | Media | Para travesia sostenida. |
| Puente | Comunicaciones internas | Panel | Coordinar la tripulacion | Media | Ordenes de navegacion. |
| Control de cubierta | Estado de cubierta | Panel simulado | Coordinar movimientos | Media | Solo logistica general. |
| Puente | Senales acusticas | Boton | Senalizar maniobras | Alta | Segun reglas de navegacion. |
| Puente | Luces de navegacion | Interruptores | Ser visto de noche | Alta | Configuracion COLREG. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Compas / giroscopica | Rumbo | grados | Alta | Referencia de direccion. |
| Corredera | Velocidad respecto al agua | nudos | Alta | Central para navegar. |
| Anemometro | Viento sobre cubierta | nudos | Alta | Relevante en operaciones de vuelo. |
| Indicador de timon | Angulo de la pala | grados | Media | Confirma la orden. |
| Inclinometro | Escora | grados | Alta | Estabilidad y seguridad en cubierta. |
| Sonda | Profundidad bajo la quilla | metros | Alta | Evita varar. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda tactil | Respuesta lenta por inercia. |
| Ordenar avante | Flecha arriba | Gatillo derecho | Palanca telegrafo | Escalonado por regimenes. |
| Ordenar atras | Flecha abajo | Gatillo izquierdo | Palanca telegrafo | Detencion muy progresiva. |
| Parar maquina | Tecla P | Boton central | Boton parado | Ordena regimen cero. |
| Mantener rumbo | Tecla H | Boton dedicado | Interruptor | Piloto de rumbo. |
| Rumbo al viento | Tecla W | Boton dedicado | Boton viento | Alinear con el viento relativo. |
| Senal acustica | Barra espaciadora | Boton R1 | Boton bocina | Segun maniobra. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Atracado | En muelle, amarrado | Maquina parada | Preparar zarpe, revisar sistemas. |
| Maniobra | Entrando o saliendo de puerto | Baja velocidad | Gobierno fino, senales. |
| Navegacion | En travesia | Piloto de rumbo | Rumbo, vigilancia, guardias. |
| Cubierta activa | Coordinacion de cubierta | Estado de cubierta | Rumbo al viento, logistica general. |
| Emergencia | Riesgo o via de agua | Alarmas activas | Achique, contrainundacion, auxilio. |

## Observaciones ergonomicas

- La isla debe ofrecer vision de la cubierta y del entorno.
- El rumbo, la velocidad, el viento y la escora deben verse en todo momento.
- La simulacion debe reflejar el gran retardo entre orden y respuesta.
- Toda la interfaz debe dejar claro que es una **simulacion educativa**, no
  operacion real ni entrenamiento militar.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-portaviones.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-portaviones.md)
