# 🎛️ Mandos e instrumentos del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un buque mercante es el **puente** (o puente de gobierno),
ubicado en alto para tener buena visibilidad. Desde allí el oficial de guardia
gobierna el rumbo, ordena la potencia a la máquina y vigila la navegación con
radar, GPS y cartas electrónicas. A diferencia de una moto, muchos mandos son
ordenes coordinadas por una tripulación.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Consola central | Timón / rueda de gobierno | Rueda o palanca | Cambiar el rumbo | Alta | Actua sobre la pala del timón. |
| Consola central | Telégrafo de máquina | Palanca de rango | Ordenar potencia y sentido | Alta | Avante, atrás, parado. |
| Consola central | Piloto automático | Selector | Mantener rumbo fijo | Media | Libera al timonel en travesía. |
| Consola lateral | Propulsor de proa | Mando lateral | Maniobra en puerto | Media | Movimiento lateral a baja velocidad. |
| Consola | Control de paso de hélice | Mando | Ajustar empuje | Media | Solo en hélice de paso variable. |
| Consola | Bocina / señales acústicas | Botón | Señalizar maniobras | Alta | Reglamentada por COLREG. |
| Consola | Luces de navegación | Interruptores | Ser visto de noche | Alta | Configuración según COLREG. |
| Consola | Alarmas y comunicaciones | Panel / radio | Seguridad y coordinación | Alta | VHF, GMDSS. |
| Alas del puente | Mandos repetidos | Duplicados | Maniobrar atracando | Media | Visión directa del costado. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Giroscópica / compás | Rumbo | grados | Alta | Referencia de dirección. |
| Corredera | Velocidad respecto al agua | nudos | Alta | Central para navegar. |
| Radar / ARPA | Otros buques y costa | millas | Alta | Prevención de abordajes. |
| GPS | Posición | lat/long | Alta | Ubicación precisa. |
| ECDIS | Carta electrónica | derrota | Alta | Sustituye cartas de papel. |
| Ecosonda | Profundidad bajo la quilla | metros | Alta | Evita varar. |
| Indicador de timón | Ángulo de la pala | grados | Media | Confirma la orden de gobierno. |
| Indicador de RPM | Régimen del motor | rpm | Media | Estado de la propulsión. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda táctil | Respuesta lenta por inercia. |
| Ordenar avante | Flecha arriba | Gatillo derecho | Palanca telégrafo | Escalonado por regímenes. |
| Ordenar atrás | Flecha abajo | Gatillo izquierdo | Palanca telégrafo | Detención muy progresiva. |
| Parar máquina | Tecla P | Botón central | Botón parado | Ordena régimen cero. |
| Thruster de proa | Teclas A/D | Cruceta lateral | Botones laterales | Solo a baja velocidad. |
| Piloto automático | Tecla H | Botón dedicado | Interruptor | Mantiene rumbo fijo. |
| Señal acústica | Barra espaciadora | Botón R1 | Botón bocina | Según maniobra COLREG. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Atracado | En muelle, amarrado | Máquina parada | Preparar zarpe, revisar sistemas. |
| Maniobra | Entrando o saliendo de puerto | Thruster activo | Gobierno fino, baja velocidad. |
| Navegación | En travesía | Piloto automático | Rumbo, vigilancia, guardias. |
| Fondeado | Al ancla, sin muelle | Ancla desplegada | Vigilar garreo, guardia. |
| Emergencia | Riesgo o falla | Alarmas activas | Maniobra evasiva, achique, auxilio. |

## Observaciones ergonomicas

- El puente debe tener visión panorámica de 360 grados en lo posible.
- El radar, el ECDIS y el indicador de rumbo deben verse en todo momento.
- El telégrafo debe dejar claro el sentido (avante/atrás) y el régimen actual.
- La simulación debe reflejar el retardo entre la orden y la respuesta del buque.
- Las señales acústicas y luminosas deben seguir el COLREG para ser educativas.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-barco-mercante.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-barco-mercante.md)
