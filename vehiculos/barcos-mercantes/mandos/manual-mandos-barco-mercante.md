# 🎛️ Mandos e instrumentos del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un buque mercante es el **puente** (o puente de gobierno),
ubicado en alto para tener buena visibilidad. Desde alli el oficial de guardia
gobierna el rumbo, ordena la potencia a la maquina y vigila la navegacion con
radar, GPS y cartas electronicas. A diferencia de una moto, muchos mandos son
ordenes coordinadas por una tripulacion.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Consola central | Timon / rueda de gobierno | Rueda o palanca | Cambiar el rumbo | Alta | Actua sobre la pala del timon. |
| Consola central | Telegrafo de maquina | Palanca de rango | Ordenar potencia y sentido | Alta | Avante, atras, parado. |
| Consola central | Piloto automatico | Selector | Mantener rumbo fijo | Media | Libera al timonel en travesia. |
| Consola lateral | Propulsor de proa | Mando lateral | Maniobra en puerto | Media | Movimiento lateral a baja velocidad. |
| Consola | Control de paso de helice | Mando | Ajustar empuje | Media | Solo en helice de paso variable. |
| Consola | Bocina / senales acusticas | Boton | Senalizar maniobras | Alta | Reglamentada por COLREG. |
| Consola | Luces de navegacion | Interruptores | Ser visto de noche | Alta | Configuracion segun COLREG. |
| Consola | Alarmas y comunicaciones | Panel / radio | Seguridad y coordinacion | Alta | VHF, GMDSS. |
| Alas del puente | Mandos repetidos | Duplicados | Maniobrar atracando | Media | Vision directa del costado. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Giroscopica / compas | Rumbo | grados | Alta | Referencia de direccion. |
| Corredera | Velocidad respecto al agua | nudos | Alta | Central para navegar. |
| Radar / ARPA | Otros buques y costa | millas | Alta | Prevencion de abordajes. |
| GPS | Posicion | lat/long | Alta | Ubicacion precisa. |
| ECDIS | Carta electronica | derrota | Alta | Sustituye cartas de papel. |
| Ecosonda | Profundidad bajo la quilla | metros | Alta | Evita varar. |
| Indicador de timon | Angulo de la pala | grados | Media | Confirma la orden de gobierno. |
| Indicador de RPM | Regimen del motor | rpm | Media | Estado de la propulsion. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda tactil | Respuesta lenta por inercia. |
| Ordenar avante | Flecha arriba | Gatillo derecho | Palanca telegrafo | Escalonado por regimenes. |
| Ordenar atras | Flecha abajo | Gatillo izquierdo | Palanca telegrafo | Detencion muy progresiva. |
| Parar maquina | Tecla P | Boton central | Boton parado | Ordena regimen cero. |
| Thruster de proa | Teclas A/D | Cruceta lateral | Botones laterales | Solo a baja velocidad. |
| Piloto automatico | Tecla H | Boton dedicado | Interruptor | Mantiene rumbo fijo. |
| Senal acustica | Barra espaciadora | Boton R1 | Boton bocina | Segun maniobra COLREG. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Atracado | En muelle, amarrado | Maquina parada | Preparar zarpe, revisar sistemas. |
| Maniobra | Entrando o saliendo de puerto | Thruster activo | Gobierno fino, baja velocidad. |
| Navegacion | En travesia | Piloto automatico | Rumbo, vigilancia, guardias. |
| Fondeado | Al ancla, sin muelle | Ancla desplegada | Vigilar garreo, guardia. |
| Emergencia | Riesgo o falla | Alarmas activas | Maniobra evasiva, achique, auxilio. |

## Observaciones ergonomicas

- El puente debe tener vision panoramica de 360 grados en lo posible.
- El radar, el ECDIS y el indicador de rumbo deben verse en todo momento.
- El telegrafo debe dejar claro el sentido (avante/atras) y el regimen actual.
- La simulacion debe reflejar el retardo entre la orden y la respuesta del buque.
- Las senales acusticas y luminosas deben seguir el COLREG para ser educativas.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-barco-mercante.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-barco-mercante.md)
