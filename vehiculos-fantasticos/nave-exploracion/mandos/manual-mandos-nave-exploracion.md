# 🎛️ Mandos e instrumentos de la nave de exploración

[🏠 Inicio](../../../README.md) · [🌌 Curso: Nave de exploración](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Este módulo describe, de forma genérica y original, el puesto de mando de una
nave de exploración imaginaria y como cada control se relaciona con la física
que ya vimos. No reproducimos consolas ni diseños oficiales: son roles y
funciones conceptuales, útiles además para pensar un simulador.

## 🧑‍🚀 El puente de mando

El puente reune a las personas que operan los sistemas. La idea de fondo es
sencilla: cada control traduce una decisión humana en una orden para un sistema
físico, y cada instrumento devuelve información medida por sensores.

## Controles principales

| Control | Función | Sistema que opera |
| --- | --- | --- |
| Palanca de propulsión subluminica | Ajusta el empuje realista | Motor subluminico. |
| Selector de impulso | Activa el viaje rápido imaginario | Impulso superluminico. |
| Timón de rumbo | Fija dirección y orientación | Control de actitud. |
| Regulador de energía | Reparte potencia entre sistemas | Reactor. |
| Mando de sensores | Orienta y enfoca la observación | Sensores. |
| Control de soporte vital | Ajusta aire, agua y temperatura | Soporte vital. |

## Instrumentos del tablero

| Instrumento | Que muestra | Base física |
| --- | --- | --- |
| Indicador de velocidad | Fracción de la velocidad de la luz | Real. |
| Reloj doble | Tiempo a bordo y tiempo externo | Dilatación temporal real. |
| Mapa estelar | Distancias en años luz | Real. |
| Nivel de energía | Reserva del reactor | Real en concepto. |
| Estado del impulso | Si el viaje rápido está activo | Imaginario. |
| Alerta de radiación | Riesgo del entorno | Real. |

## Flujo de una orden

Cuando la tripulación decide moverse, la orden pasa del control al sistema y el
resultado vuelve como lectura en el tablero. Ese ciclo de mando y respuesta es
justo lo que un simulador debe modelar.

## Entradas de simulación

| Entrada | Tipo | Rango | Efecto principal |
| --- | --- | --- | --- |
| Empuje subluminico | numérica | 0-100% | Aceleración realista. |
| Activar impulso | booleana | si / no | Cambia a modo viaje rápido. |
| Rumbo | numérica | 0-360 grados | Dirección de la nave. |
| Reparto de energía | numérica | 0-100% por sistema | Prioridad de potencia. |
| Enfoque de sensores | discreta | corto / medio / largo | Alcance de observación. |
| Nivel de soporte vital | numérica | 0-100% | Confort y seguridad a bordo. |

## Puente hacia los principios

Ya sabemos que controles existen. El siguiente módulo explica que decisiones son
físicamente posibles, cuales no y por  qué, comparando ficción y realidad.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-exploracion.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-nave-exploracion.md)
