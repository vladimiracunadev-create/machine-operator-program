# 🎛️ Mandos e instrumentos del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🎛️ Mandos

## Vista general

La cabina del orbitador combina lo mejor de una nave espacial y de un avión.
Durante el ascenso y la órbita, la tripulación controla el empuje, la actitud y
los sistemas como en una nave; en la reentrada y el aterrizaje, usa palanca y
timones como en un planeador. Los paneles muestran la órbita, los recursos y,
sobre todo, el estado del escudo térmico y la trayectoria de descenso.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Consola | Control de actitud | Palanca | Orientar la nave en órbita | Alta | Acciona propulsores RCS. |
| Consola | Control de empuje | Palanca | Motores de maniobra | Alta | Para cambiar de órbita y desorbitar. |
| Cabina | Palanca de vuelo | Bastón | Controlar el planeo | Alta | Se usa en la reentrada y el aterrizaje. |
| Cabina | Pedales de timón | Pedales | Dirección y frenado en pista | Alta | Como en un avión. |
| Panel | Bahía de carga | Interruptores | Abrir puertas y mover brazo | Media | Solo en órbita. |
| Panel | Energía y soporte vital | Mandos | Gestionar aire, agua, potencia | Alta | Vital durante la misión. |
| Panel | Tren de aterrizaje | Palanca | Desplegar el tren | Alta | Antes de tocar la pista. |
| Panel | Alarmas | Luces y sonido | Avisar fallas | Alta | Presión, escudo, energía. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Indicador de órbita | Forma y altura de la órbita | km | Alta | Apogeo y perigeo. |
| Actitud | Orientación de la nave | grados | Alta | Clave para apuntar el escudo. |
| Velocidad | Rapidez de la nave | m/s o km/h | Alta | Muy alta en órbita, baja al aterrizar. |
| Ángulo de reentrada | Inclinación de descenso | grados | Alta | Ni muy plano ni muy vertical. |
| Temperatura del escudo | Calor en la panza y bordes | grados | Alta | Crítica en la reentrada. |
| Senda de planeo | Trayectoria hacia la pista | gráfico | Alta | Guía el descenso sin motor. |

## Entradas de simulación

| Acción | Teclado | Controlador | Panel táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Orientar en órbita | Teclas WASDQE | Stick derecho | Zona de actitud | Cabecear, guiñar, rolar. |
| Empuje de maniobra | Shift y Ctrl | Gatillos | Barra de empuje | Cambiar órbita o desorbitar. |
| Apuntar el escudo | Tecla B | Botón | Modo reentrada | Escudo por delante. |
| Controlar el planeo | Flechas | Stick de vuelo | Palanca virtual | Cabeceo y alabeo sin motor. |
| Timón y frenos | Teclas Z y X | Gatillos | Pedales | Dirección y frenado en pista. |
| Desplegar tren | Tecla G | Botón | Botón de tren | Antes del toque. |
| Abrir bahía | Tecla O | Botón | Panel de carga | Solo en órbita. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En plataforma | Antes del despegue | Checklist en pantalla | Revisar sistemas, iniciar cuenta. |
| Ascenso | Subiendo con propulsores | Empuje y velocidad activos | Guiar, separar propulsores y tanque. |
| En órbita | Vuelo orbital estable | Indicador de órbita activo | Maniobrar, abrir bahía, operar carga. |
| Desorbitación | Frenado para volver | Delta-v en uso | Encender motor, apuntar escudo. |
| Reentrada | Regreso con calor | Temperatura del escudo | Mantener ángulo, orientar el escudo. |
| Planeo y aterrizaje | Descenso sin motor | Senda de planeo | Controlar palanca, timón, tren, frenos. |

## Observaciones ergonomicas

- La temperatura del escudo y el ángulo de reentrada deben verse siempre.
- El paso de "nave" a "planeador" debe quedar claro en la interfaz.
- La senda de planeo debe guiar al usuario en el aterrizaje sin motor.
- Las alarmas del escudo y de la energía deben ser inconfundibles.
- Debe recordarse que en el descenso final no hay motor para corregir.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-transbordador.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-transbordador.md)
