# 🎛️ Mandos e instrumentos del caza transformable

[🏠 Inicio](../../../README.md) · [🤖 Curso: Caza transformable](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

¿Cómo se pilota una máquina que cambia de forma? Este módulo describe, de manera
genérica y original, el puesto de mando imaginado y cómo se traduce en entradas
de simulación. La gran diferencia con un avión normal es que hay un control más:
el de cambio de modo.

---

## 🎯 Puesto de mando

El piloto se ubica en una cabina que debe seguir siendo utilizable en los tres
modos. Eso plantea un reto de diseño: los mandos que sirven para volar (palanca,
acelerador, pedales) conviven con los que sirven para caminar o manipular en modo
humanoide.

---

## Controles y su función

| Control | Modo principal | Función |
| --- | --- | --- |
| Palanca de vuelo | Caza | Controla cabeceo y alabeo en el aire. |
| Acelerador | Caza e intermedio | Regula el empuje de los motores. |
| Pedales | Caza | Controla la guiñada (giro sobre el eje vertical). |
| Selector de modo | Todos | Ordena la transformación entre formas. |
| Mando de extremidades | Humanoide | Coordina brazos y piernas. |
| Freno o punto de apoyo | Intermedio y humanoide | Estabiliza al tocar el suelo. |
| Panel de estado | Todos | Muestra la fase de transformación. |

---

## Instrumentos del tablero

| Instrumento | Que informa | Por qué importa |
| --- | --- | --- |
| Indicador de modo | Forma actual y transición | Evita cambiar de modo en mal momento. |
| Horizonte artificial | Actitud respecto al suelo | Clave en modo caza e intermedio. |
| Centro de masa | Posición del punto de equilibrio | Avisa de inestabilidad al transformar. |
| Energía disponible | Reserva para motores y actuadores | La transformación consume mucha. |
| Cargas estructurales | Esfuerzo en juntas críticas | Previene forzar el mecanismo. |
| Velocidad | Rapidez respecto al aire o al suelo | Limita cuando es seguro transformar. |

---

## Entradas de simulación

Para modelar el pilotaje en un simulador educativo, cada control se convierte en
una entrada con un rango definido. Incluimos de forma explícita el control de
cambio de modo.

| Entrada | Tipo | Rango | Efecto en el modelo |
| --- | --- | --- | --- |
| Empuje | numérica | 0-100% | Acelera o frena la máquina. |
| Cabeceo | numérica | -100..100 | Sube o baja el morro en vuelo. |
| Alabeo | numérica | -100..100 | Inclina hacia los lados. |
| Guiñada | numérica | -100..100 | Gira sobre el eje vertical. |
| Cambio de modo | discreta | caza, intermedio, humanoide | Lanza la secuencia de transformación. |
| Extremidades | numérica | -100..100 | Mueve brazos y piernas en el suelo. |
| Freno o apoyo | numérica | 0-100% | Estabiliza al contactar la superficie. |

---

## Buenas prácticas de pilotaje

- Verificar velocidad y energía antes de ordenar un cambio de modo.
- No transformar en plena maniobra brusca: el centro de masa se mueve.
- Vigilar las cargas estructurales para no forzar las juntas.
- Usar el modo intermedio como transición controlada, no como atajo.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-caza-transformable.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-caza-transformable.md)
