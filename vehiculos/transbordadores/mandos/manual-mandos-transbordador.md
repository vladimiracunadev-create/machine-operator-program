# 🎛️ Mandos e instrumentos del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🎛️ Mandos

## Vista general

La cabina del orbitador combina lo mejor de una nave espacial y de un avion.
Durante el ascenso y la orbita, la tripulacion controla el empuje, la actitud y
los sistemas como en una nave; en la reentrada y el aterrizaje, usa palanca y
timones como en un planeador. Los paneles muestran la orbita, los recursos y,
sobre todo, el estado del escudo termico y la trayectoria de descenso.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Consola | Control de actitud | Palanca | Orientar la nave en orbita | Alta | Acciona propulsores RCS. |
| Consola | Control de empuje | Palanca | Motores de maniobra | Alta | Para cambiar de orbita y desorbitar. |
| Cabina | Palanca de vuelo | Baston | Controlar el planeo | Alta | Se usa en la reentrada y el aterrizaje. |
| Cabina | Pedales de timon | Pedales | Direccion y frenado en pista | Alta | Como en un avion. |
| Panel | Bahia de carga | Interruptores | Abrir puertas y mover brazo | Media | Solo en orbita. |
| Panel | Energia y soporte vital | Mandos | Gestionar aire, agua, potencia | Alta | Vital durante la mision. |
| Panel | Tren de aterrizaje | Palanca | Desplegar el tren | Alta | Antes de tocar la pista. |
| Panel | Alarmas | Luces y sonido | Avisar fallas | Alta | Presion, escudo, energia. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Indicador de orbita | Forma y altura de la orbita | km | Alta | Apogeo y perigeo. |
| Actitud | Orientacion de la nave | grados | Alta | Clave para apuntar el escudo. |
| Velocidad | Rapidez de la nave | m/s o km/h | Alta | Muy alta en orbita, baja al aterrizar. |
| Angulo de reentrada | Inclinacion de descenso | grados | Alta | Ni muy plano ni muy vertical. |
| Temperatura del escudo | Calor en la panza y bordes | grados | Alta | Critica en la reentrada. |
| Senda de planeo | Trayectoria hacia la pista | grafico | Alta | Guia el descenso sin motor. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Panel tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Orientar en orbita | Teclas WASDQE | Stick derecho | Zona de actitud | Cabecear, guinar, rolar. |
| Empuje de maniobra | Shift y Ctrl | Gatillos | Barra de empuje | Cambiar orbita o desorbitar. |
| Apuntar el escudo | Tecla B | Boton | Modo reentrada | Escudo por delante. |
| Controlar el planeo | Flechas | Stick de vuelo | Palanca virtual | Cabeceo y alabeo sin motor. |
| Timon y frenos | Teclas Z y X | Gatillos | Pedales | Direccion y frenado en pista. |
| Desplegar tren | Tecla G | Boton | Boton de tren | Antes del toque. |
| Abrir bahia | Tecla O | Boton | Panel de carga | Solo en orbita. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En plataforma | Antes del despegue | Checklist en pantalla | Revisar sistemas, iniciar cuenta. |
| Ascenso | Subiendo con propulsores | Empuje y velocidad activos | Guiar, separar propulsores y tanque. |
| En orbita | Vuelo orbital estable | Indicador de orbita activo | Maniobrar, abrir bahia, operar carga. |
| Desorbitacion | Frenado para volver | Delta-v en uso | Encender motor, apuntar escudo. |
| Reentrada | Regreso con calor | Temperatura del escudo | Mantener angulo, orientar el escudo. |
| Planeo y aterrizaje | Descenso sin motor | Senda de planeo | Controlar palanca, timon, tren, frenos. |

## Observaciones ergonomicas

- La temperatura del escudo y el angulo de reentrada deben verse siempre.
- El paso de "nave" a "planeador" debe quedar claro en la interfaz.
- La senda de planeo debe guiar al usuario en el aterrizaje sin motor.
- Las alarmas del escudo y de la energia deben ser inconfundibles.
- Debe recordarse que en el descenso final no hay motor para corregir.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-transbordador.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-transbordador.md)
