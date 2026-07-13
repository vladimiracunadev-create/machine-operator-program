# 🎛️ Mandos e instrumentos del caza transformable

[🏠 Inicio](../../../README.md) · [🤖 Curso: Caza transformable](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Como se pilota una maquina que cambia de forma? Este modulo describe, de manera
generica y original, el puesto de mando imaginado y como se traduce en entradas
de simulacion. La gran diferencia con un avion normal es que hay un control mas:
el de cambio de modo.

---

## 🎯 Puesto de mando

El piloto se ubica en una cabina que debe seguir siendo utilizable en los tres
modos. Eso plantea un reto de diseno: los mandos que sirven para volar (palanca,
acelerador, pedales) conviven con los que sirven para caminar o manipular en modo
humanoide.

---

## Controles y su funcion

| Control | Modo principal | Funcion |
| --- | --- | --- |
| Palanca de vuelo | Caza | Controla cabeceo y alabeo en el aire. |
| Acelerador | Caza e intermedio | Regula el empuje de los motores. |
| Pedales | Caza | Controla la guinada (giro sobre el eje vertical). |
| Selector de modo | Todos | Ordena la transformacion entre formas. |
| Mando de extremidades | Humanoide | Coordina brazos y piernas. |
| Freno o punto de apoyo | Intermedio y humanoide | Estabiliza al tocar el suelo. |
| Panel de estado | Todos | Muestra la fase de transformacion. |

---

## Instrumentos del tablero

| Instrumento | Que informa | Por que importa |
| --- | --- | --- |
| Indicador de modo | Forma actual y transicion | Evita cambiar de modo en mal momento. |
| Horizonte artificial | Actitud respecto al suelo | Clave en modo caza e intermedio. |
| Centro de masa | Posicion del punto de equilibrio | Avisa de inestabilidad al transformar. |
| Energia disponible | Reserva para motores y actuadores | La transformacion consume mucha. |
| Cargas estructurales | Esfuerzo en juntas criticas | Previene forzar el mecanismo. |
| Velocidad | Rapidez respecto al aire o al suelo | Limita cuando es seguro transformar. |

---

## Entradas de simulacion

Para modelar el pilotaje en un simulador educativo, cada control se convierte en
una entrada con un rango definido. Incluimos de forma explicita el control de
cambio de modo.

| Entrada | Tipo | Rango | Efecto en el modelo |
| --- | --- | --- | --- |
| Empuje | numerica | 0-100% | Acelera o frena la maquina. |
| Cabeceo | numerica | -100..100 | Sube o baja el morro en vuelo. |
| Alabeo | numerica | -100..100 | Inclina hacia los lados. |
| Guinada | numerica | -100..100 | Gira sobre el eje vertical. |
| Cambio de modo | discreta | caza, intermedio, humanoide | Lanza la secuencia de transformacion. |
| Extremidades | numerica | -100..100 | Mueve brazos y piernas en el suelo. |
| Freno o apoyo | numerica | 0-100% | Estabiliza al contactar la superficie. |

---

## Buenas practicas de pilotaje

- Verificar velocidad y energia antes de ordenar un cambio de modo.
- No transformar en plena maniobra brusca: el centro de masa se mueve.
- Vigilar las cargas estructurales para no forzar las juntas.
- Usar el modo intermedio como transicion controlada, no como atajo.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-caza-transformable.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-caza-transformable.md)
