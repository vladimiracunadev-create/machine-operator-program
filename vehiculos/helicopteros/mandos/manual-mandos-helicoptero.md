# 🎛️ Mandos e instrumentos del helicoptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicopteros](../README.md) · 🎛️ Mandos

## Vista general

La cabina de un helicoptero exige coordinar las dos manos y los dos pies a la vez.
La mano izquierda opera la palanca de colectivo, con el mando de gas integrado; la
mano derecha lleva la palanca ciclica; los dos pies actuan sobre los pedales del
rotor de cola. El panel al frente muestra el estado del vuelo, del motor y de la
transmision. Es un vehiculo de equilibrio constante entre potencia, sustentacion y
anti-par.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano izquierda | Colectivo | Palanca | Subir o bajar el paso de todas las palas | Alta | Controla la sustentacion total. |
| Mano izquierda | Mando de gas | Puno giratorio | Ajustar la potencia del motor | Alta | Integrado en el colectivo. |
| Mano derecha | Ciclico | Palanca central | Inclinar el disco rotor | Alta | Traslada el helicoptero. |
| Ambos pies | Pedales | Pedales | Cambiar el paso del rotor de cola | Alta | Controlan la guinada y el anti-par. |
| Panel | Instrumentos de vuelo | Relojes / pantalla | Mostrar estado del vuelo | Alta | Ver seccion de instrumentos. |
| Panel | Instrumentos de motor | Relojes / pantalla | Presion y temperatura | Alta | Vigilan la salud del motor. |
| Panel | Instrumentos de transmision | Relojes / pantalla | Presion y temperatura de caja | Alta | Criticos por la carga del rotor. |
| Panel | Rotor RPM | Indicador | Regimen del rotor y del motor | Alta | Debe mantenerse en su rango. |
| Panel | Interruptores electricos | Botones | Luces, bombas, avionica | Media | Encendido por checklist. |
| Panel | Radio y transponder | Teclado | Comunicar y ser visto en radar | Alta | Frecuencias y codigo asignado. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Anemometro (velocidad) | Velocidad respecto al aire | nudos | Alta | Menos util en vuelo estacionario. |
| Altimetro | Altitud sobre el nivel de referencia | pies | Alta | Se ajusta con la presion local. |
| Variometro | Velocidad vertical | pies/min | Alta | Clave en ascenso y descenso vertical. |
| Horizonte artificial | Actitud (cabeceo y alabeo) | grados | Alta | Referencia sin ver el exterior. |
| Indicador de rumbo | Direccion de la nariz | grados | Alta | Se alinea con la brujula. |
| Rotor RPM | Regimen del rotor y del motor | rpm | Alta | Vital; fuera de rango es peligroso. |
| Presion y temperatura de motor | Salud del motor | varias | Alta | Aceite y temperatura de gases. |
| Presion y temperatura de transmision | Salud de la caja reductora | varias | Alta | La transmision es punto critico. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Palanca de vuelo | Comentarios |
| --- | --- | --- | --- | --- |
| Colectivo arriba/abajo | Teclas F2 / F3 | Gatillo izquierdo | Palanca de colectivo | Sube o baja la sustentacion. |
| Ciclico adelante/atras | Flechas arriba/abajo | Stick eje Y | Adelante-atras | Avanza o retrocede. |
| Ciclico izq/der | Flechas izq/der | Stick eje X | Giro lateral | Se desplaza de lado. |
| Guinada | Teclas Z / X | Pedales | Pedales | Gira la nariz; ajusta anti-par. |
| Gas / potencia | Teclas + / - | Rueda | Puno del colectivo | Ajusta la potencia del motor. |
| Arranque de rotor | Tecla I | Boton | Secuencia de arranque | Segun checklist. |
| Freno de rotor | Tecla B | Boton | Palanca de freno | Solo con rotor detenido en tierra. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En tierra apagado | Rotor detenido | Panel sin energia | Checklist, encender sistemas. |
| Rotor en marcha | Motor y rotor girando en tierra | Rotor RPM en rango | Estabilizar, prepararse para despegar. |
| Vuelo estacionario | Sostenido sobre un punto | Variometro cerca de cero | Trasladar, ascender, girar. |
| En vuelo | Desplazamiento en crucero | Anemometro y altimetro activos | Ascender, virar, crucero, descender. |
| Aproximacion | Preparando aterrizaje | Descenso controlado | Reducir velocidad, estacionario, posar. |
| Emergencia | Falla o riesgo | Testigos de alerta | Autorrotacion o checklist de emergencia. |

## Observaciones ergonomicas

- El rotor RPM y el horizonte artificial deben verse siempre; son criticos.
- Colectivo, ciclico y pedales se coordinan de forma continua: la interfaz debe
  mostrar como un mando afecta a los otros.
- Al subir colectivo aumenta el par, por lo que suele acompanarse con pedal.
- Los instrumentos de transmision deben ser visibles y facilmente reconocibles.
- La interfaz de simulacion deberia guiar el uso de checklist en cada fase.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-helicoptero.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-helicoptero.md)
