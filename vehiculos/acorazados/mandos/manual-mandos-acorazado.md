---
tipo_documento: clase
clase: 5
codigo: ACORAZADOS-05
curso: acorazados
titulo: "Mandos e instrumentos del acorazado"
modalidad: "taller de simulación"
duracion_minutos: 60
nivel: introductorio
prerrequisito: ACORAZADOS-04
competencia: "lectura_y_mando"
resultados_aprendizaje:
  - "Explicar controles, instrumentos, entradas y estados del sistema con vocabulario propio de Acorazados."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Acorazados."
evidencia: "Mapa de mandos y resolución de dos estados del tablero."
criterio_aprobacion: "Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

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

## 🎓 Cierre de clase

- **Actividad:** Recorre el puesto de mando simulado de Acorazados: localiza los controles de controles, instrumentos, entradas y estados del sistema y asocia cada indicación con una decisión.
- **Evidencia:** Mapa de mandos y resolución de dos estados del tablero.
- **Criterio de aprobación:** Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-NHHC-SHIPS](https://www.history.navy.mil/browse-by-topic/ships.html): Ships, Naval History and Heritage Command. Uso: historia pública de buques militares.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-acorazado.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-acorazado.md)
