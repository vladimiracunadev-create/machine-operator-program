# 🎛️ Mandos e instrumentos de la nave de exploracion

[🏠 Inicio](../../../README.md) · [🌌 Curso: Nave de exploracion](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Este modulo describe, de forma generica y original, el puesto de mando de una
nave de exploracion imaginaria y como cada control se relaciona con la fisica
que ya vimos. No reproducimos consolas ni disenos oficiales: son roles y
funciones conceptuales, utiles ademas para pensar un simulador.

## 🧑‍🚀 El puente de mando

El puente reune a las personas que operan los sistemas. La idea de fondo es
sencilla: cada control traduce una decision humana en una orden para un sistema
fisico, y cada instrumento devuelve informacion medida por sensores.

## Controles principales

| Control | Funcion | Sistema que opera |
| --- | --- | --- |
| Palanca de propulsion subluminica | Ajusta el empuje realista | Motor subluminico. |
| Selector de impulso | Activa el viaje rapido imaginario | Impulso superluminico. |
| Timon de rumbo | Fija direccion y orientacion | Control de actitud. |
| Regulador de energia | Reparte potencia entre sistemas | Reactor. |
| Mando de sensores | Orienta y enfoca la observacion | Sensores. |
| Control de soporte vital | Ajusta aire, agua y temperatura | Soporte vital. |

## Instrumentos del tablero

| Instrumento | Que muestra | Base fisica |
| --- | --- | --- |
| Indicador de velocidad | Fraccion de la velocidad de la luz | Real. |
| Reloj doble | Tiempo a bordo y tiempo externo | Dilatacion temporal real. |
| Mapa estelar | Distancias en anios luz | Real. |
| Nivel de energia | Reserva del reactor | Real en concepto. |
| Estado del impulso | Si el viaje rapido esta activo | Imaginario. |
| Alerta de radiacion | Riesgo del entorno | Real. |

## Flujo de una orden

Cuando la tripulacion decide moverse, la orden pasa del control al sistema y el
resultado vuelve como lectura en el tablero. Ese ciclo de mando y respuesta es
justo lo que un simulador debe modelar.

## Entradas de simulacion

| Entrada | Tipo | Rango | Efecto principal |
| --- | --- | --- | --- |
| Empuje subluminico | numerica | 0-100% | Aceleracion realista. |
| Activar impulso | booleana | si / no | Cambia a modo viaje rapido. |
| Rumbo | numerica | 0-360 grados | Direccion de la nave. |
| Reparto de energia | numerica | 0-100% por sistema | Prioridad de potencia. |
| Enfoque de sensores | discreta | corto / medio / largo | Alcance de observacion. |
| Nivel de soporte vital | numerica | 0-100% | Confort y seguridad a bordo. |

## Puente hacia los principios

Ya sabemos que controles existen. El siguiente modulo explica que decisiones son
fisicamente posibles, cuales no y por que, comparando ficcion y realidad.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-nave-exploracion.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-nave-exploracion.md)
