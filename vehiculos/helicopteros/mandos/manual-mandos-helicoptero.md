# 🎛️ Mandos e instrumentos del helicóptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · 🎛️ Mandos

## Vista general

La cabina de un helicóptero exige coordinar las dos manos y los dos pies a la vez.
La mano izquierda opera la palanca de colectivo, con el mando de gas integrado; la
mano derecha lleva la palanca cíclica; los dos pies actuan sobre los pedales del
rotor de cola. El panel al frente muestra el estado del vuelo, del motor y de la
transmisión. Es un vehículo de equilibrio constante entre potencia, sustentación y
anti-par.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano izquierda | Colectivo | Palanca | Subir o bajar el paso de todas las palas | Alta | Controla la sustentación total. |
| Mano izquierda | Mando de gas | Puño giratorio | Ajustar la potencia del motor | Alta | Integrado en el colectivo. |
| Mano derecha | Cíclico | Palanca central | Inclinar el disco rotor | Alta | Traslada el helicóptero. |
| Ambos pies | Pedales | Pedales | Cambiar el paso del rotor de cola | Alta | Controlan la guiñada y el anti-par. |
| Panel | Instrumentos de vuelo | Relojes / pantalla | Mostrar estado del vuelo | Alta | Ver sección de instrumentos. |
| Panel | Instrumentos de motor | Relojes / pantalla | Presión y temperatura | Alta | Vigilan la salud del motor. |
| Panel | Instrumentos de transmisión | Relojes / pantalla | Presión y temperatura de caja | Alta | Críticos por la carga del rotor. |
| Panel | Rotor RPM | Indicador | Régimen del rotor y del motor | Alta | Debe mantenerse en su rango. |
| Panel | Interruptores eléctricos | Botones | Luces, bombas, avionica | Media | Encendido por checklist. |
| Panel | Radio y transponder | Teclado | Comunicar y ser visto en radar | Alta | Frecuencias y código asignado. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Anemómetro (velocidad) | Velocidad respecto al aire | nudos | Alta | Menos útil en vuelo estacionario. |
| Altímetro | Altitud sobre el nivel de referencia | pies | Alta | Se ajusta con la presión local. |
| Variómetro | Velocidad vertical | pies/min | Alta | Clave en ascenso y descenso vertical. |
| Horizonte artificial | Actitud (cabeceo y alabeo) | grados | Alta | Referencia sin ver el exterior. |
| Indicador de rumbo | Dirección de la nariz | grados | Alta | Se alinea con la brújula. |
| Rotor RPM | Régimen del rotor y del motor | rpm | Alta | Vital; fuera de rango es peligroso. |
| Presión y temperatura de motor | Salud del motor | varias | Alta | Aceite y temperatura de gases. |
| Presión y temperatura de transmisión | Salud de la caja reductora | varias | Alta | La transmisión es punto crítico. |

## Entradas de simulación

| Acción | Teclado | Controlador | Palanca de vuelo | Comentarios |
| --- | --- | --- | --- | --- |
| Colectivo arriba/abajo | Teclas F2 / F3 | Gatillo izquierdo | Palanca de colectivo | Sube o baja la sustentación. |
| Cíclico adelante/atrás | Flechas arriba/abajo | Stick eje Y | Adelante-atrás | Avanza o retrocede. |
| Cíclico izq/der | Flechas izq/der | Stick eje X | Giro lateral | Se desplaza de lado. |
| Guiñada | Teclas Z / X | Pedales | Pedales | Gira la nariz; ajusta anti-par. |
| Gas / potencia | Teclas + / - | Rueda | Puño del colectivo | Ajusta la potencia del motor. |
| Arranque de rotor | Tecla I | Botón | Secuencia de arranque | Según checklist. |
| Freno de rotor | Tecla B | Botón | Palanca de freno | Solo con rotor detenido en tierra. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En tierra apagado | Rotor detenido | Panel sin energía | Checklist, encender sistemas. |
| Rotor en marcha | Motor y rotor girando en tierra | Rotor RPM en rango | Estabilizar, prepararse para despegar. |
| Vuelo estacionario | Sostenido sobre un punto | Variómetro cerca de cero | Trasladar, ascender, girar. |
| En vuelo | Desplazamiento en crucero | Anemómetro y altímetro activos | Ascender, virar, crucero, descender. |
| Aproximación | Preparando aterrizaje | Descenso controlado | Reducir velocidad, estacionario, posar. |
| Emergencia | Falla o riesgo | Testigos de alerta | Autorrotación o checklist de emergencia. |

## Observaciones ergonomicas

- El rotor RPM y el horizonte artificial deben verse siempre; son críticos.
- Colectivo, cíclico y pedales se coordinan de forma continua: la interfaz debe
  mostrar como un mando afecta a los otros.
- Al subir colectivo aumenta el par, por lo que suele acompanarse con pedal.
- Los instrumentos de transmisión deben ser visibles y fácilmente reconocibles.
- La interfaz de simulación debería guiar el uso de checklist en cada fase.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-helicoptero.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-helicoptero.md)
