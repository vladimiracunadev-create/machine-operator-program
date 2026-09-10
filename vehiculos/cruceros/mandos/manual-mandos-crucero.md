---
tipo_documento: clase
clase: 5
codigo: CRUCEROS-05
curso: cruceros
titulo: "Mandos e instrumentos del crucero"
modalidad: "taller de simulación"
duracion_minutos: 60
nivel: introductorio
prerrequisito: CRUCEROS-04
competencia: "lectura_y_mando"
resultados_aprendizaje:
  - "Explicar controles, instrumentos, entradas y estados del sistema con vocabulario propio de Cruceros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Cruceros."
evidencia: "Mapa de mandos y resolución de dos estados del tablero."
criterio_aprobacion: "Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎛️ Mandos e instrumentos del crucero

[🏠 Inicio](../../../README.md) · [⛴️ Curso: Cruceros](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un crucero es el **puente de gobierno**, una consola ancha
y elevada con visión panorámica y alas laterales que sobresalen del casco para
maniobrar en puerto. Desde allí el oficial de guardia gobierna con palancas de
pod, ordena la propulsión, vigila la navegación con radar, ECDIS y GPS, y
supervisa la seguridad del pasaje. Muchos mandos son ordenes coordinadas por una
tripulación numerosa.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Consola central | Palancas de propulsión (pods) | Palancas | Regular empuje y orientación | Alta | Combinan avance y gobierno. |
| Consola central | Timón / rueda de gobierno | Rueda o palanca | Cambiar el rumbo | Alta | En buques con timones clásicos. |
| Consola central | Piloto automático | Selector | Mantener rumbo fijo | Media | Libera al timonel en travesía. |
| Consola central | Joystick de maniobra | Mando integrado | Mover el buque en cualquier dirección | Alta | Combina pods y thrusters en puerto. |
| Consola lateral | Propulsores de proa | Mando lateral | Maniobra en puerto | Media | Movimiento lateral a baja velocidad. |
| Consola | Control de estabilizadores | Selector | Desplegar aletas | Media | Reduce el balance del pasaje. |
| Consola | Bocina / señales acústicas | Botón | Señalizar maniobras | Alta | Reglamentada por COLREG. |
| Consola | Luces de navegación | Interruptores | Ser visto de noche | Alta | Configuración según COLREG. |
| Consola | Alarma general y megafonia | Panel | Alertar y dirigir al pasaje | Alta | Clave en evacuación. |
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
| Indicador de pods | Empuje y ángulo de cada pod | grados / % | Alta | Confirma la orden de propulsión. |
| Panel de estabilizadores | Estado de las aletas | desplegado/retraído | Media | Confort del pasaje. |
| Panel de seguridad | Incendios, puertas estancas, botes | estado | Alta | Supervisión de emergencia. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Cambiar rumbo | Flechas izq/der | Stick izquierdo | Rueda táctil | Respuesta con inercia. |
| Ajustar empuje | Flechas arriba/abajo | Gatillos | Palancas de pod | Escalonado y progresivo. |
| Orientar pods | Teclas Q/E | Stick derecho | Diales de pod | Solo con propulsión por pods. |
| Maniobra lateral | Teclas A/D | Cruceta lateral | Joystick de maniobra | Solo a baja velocidad. |
| Piloto automático | Tecla H | Botón dedicado | Interruptor | Mantiene rumbo fijo. |
| Estabilizadores | Tecla T | Botón | Interruptor | Despliega o retrae aletas. |
| Señal acústica | Barra espaciadora | Botón R1 | Botón bocina | Según maniobra COLREG. |
| Alarma general | Tecla G | Botón protegido | Botón protegido | Inicia procedimiento de muster. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Atracado | En muelle, amarrado | Máquina parada | Embarcar pasaje, preparar zarpe. |
| Maniobra | Entrando o saliendo de puerto | Thruster activo | Gobierno fino, baja velocidad. |
| Navegación | En travesía entre escalas | Piloto automático | Rumbo, vigilancia, guardias. |
| Fondeado | Al ancla frente a puerto | Ancla desplegada | Tender de pasaje, vigilar garreo. |
| Emergencia | Riesgo o falla | Alarma general | Muster, evacuación, achique, auxilio. |

## Observaciones ergonomicas

- El puente debe tener visión panorámica de 360 grados en lo posible.
- El radar, el ECDIS y el indicador de rumbo deben verse en todo momento.
- Las palancas de pod deben mostrar con claridad empuje y orientación de cada unidad.
- El panel de seguridad (incendios, puertas estancas, botes) debe ser visible y priorizado.
- La simulación debe reflejar el retardo entre la orden y la respuesta del buque.
- La alarma general y la megafonia deben estar protegidas contra accionamiento accidental.

## 🎓 Cierre de clase

- **Actividad:** Recorre el puesto de mando simulado de Cruceros: localiza los controles de controles, instrumentos, entradas y estados del sistema y asocia cada indicación con una decisión.
- **Evidencia:** Mapa de mandos y resolución de dos estados del tablero.
- **Criterio de aprobación:** Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [IMO-COLREG](https://www.imo.org/en/about/conventions/pages/colreg.aspx): Collision Regulations, International Maritime Organization. Uso: prevención de abordajes.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-crucero.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-crucero.md)
