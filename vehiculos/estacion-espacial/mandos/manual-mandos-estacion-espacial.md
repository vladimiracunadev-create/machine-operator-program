# 🎛️ Mandos e instrumentos de la estacion espacial

[🏠 Inicio](../../../README.md) · [🛰️ Curso: Estacion espacial (ISS)](../README.md) · 🎛️ Mandos

## Vista general

La estacion espacial no se "pilota" como una nave: se **opera**. La tripulacion a
bordo trabaja en estaciones de trabajo y paneles de sistema, mientras varios
**centros de control** en tierra vigilan la telemetria y coordinan las tareas. La
estacion mantiene su orbita y su orientacion de forma casi automatica; el trabajo
humano se centra en la ciencia, el mantenimiento, el acoplamiento y las EVA.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| A bordo | Panel de soporte vital | Mandos y lecturas | Aire, agua, CO2, temperatura | Alta | Vital cada dia. |
| A bordo | Panel de energia | Interruptores | Repartir potencia | Alta | Gestiona paneles y baterias. |
| A bordo | Estacion de brazo robotico | Palancas y pantallas | Mover el brazo | Alta | Captura naves y cargas. |
| A bordo | Control de acoplamiento | Pantallas | Vigilar la aproximacion | Alta | Encuentro lento y preciso. |
| A bordo | Esclusa de EVA | Mandos | Preparar caminatas | Alta | Presion y trajes. |
| A bordo | Comunicaciones | Radio | Contacto con tierra | Media | Enlace con el centro de control. |
| Tierra | Consolas de control | Telemetria | Vigilar todos los sistemas | Alta | Varios centros por pais socio. |
| A bordo y tierra | Alarmas | Luces y sonido | Avisar fallas | Alta | Fuego, presion, energia. |

## Instrumentos y telemetria

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Altitud orbital | Altura sobre la Tierra | km | Alta | Ronda los 400 km (aproximado). |
| Recursos vitales | Oxigeno, CO2, agua | varias | Alta | Estado del soporte vital. |
| Energia disponible | Carga de baterias y paneles | porcentaje | Alta | Sube al Sol, baja en sombra. |
| Temperatura interior | Ambiente de los modulos | grados | Alta | La regula el control termico. |
| Orientacion | Actitud de la estacion | grados | Media | Casi siempre automatica. |
| Estado de puertos | Libre u ocupado | discreto | Alta | Para recibir naves. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Panel tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Revisar soporte vital | Tecla L | Boton | Panel vital | Aire, agua, CO2. |
| Gestionar energia | Tecla P | Cruceta | Panel de energia | Reparte potencia. |
| Operar brazo robotico | Teclas WASDQE | Sticks | Estacion de brazo | Mueve cargas y captura naves. |
| Guiar acoplamiento | Flechas | Stick | Zona de acople | Aproximacion lenta. |
| Preparar EVA | Tecla V | Boton | Panel de esclusa | Presion y traje. |
| Atender alarma | Tecla espacio | Boton | Boton de alarma | Aislar la falla. |
| Comunicar con tierra | Tecla T | Boton | Radio | Coordinar tareas. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Operacion normal | Estacion estable en orbita | Sistemas en verde | Ciencia, mantenimiento, ejercicio. |
| Acoplamiento | Llega una nave | Datos de aproximacion | Guiar acople, capturar con el brazo. |
| Reabastecimiento | Traspaso de carga | Puerto ocupado | Descargar agua, aire, comida, equipos. |
| Caminata espacial | Tripulacion en el exterior | Estado de esclusa y traje | Instalar o reparar equipos. |
| Ajuste de orbita | Correccion de altura | Empuje de una nave acoplada | Elevar la orbita. |
| Emergencia | Fuego, fuga o falla | Alarmas activas | Aislar, cerrar modulo, aplicar checklist. |

## Observaciones ergonomicas

- Los recursos vitales y la energia deben verse siempre de un vistazo.
- Las alarmas de fuego, presion y fuga deben ser inconfundibles.
- El control del brazo robotico exige vistas claras y movimientos suaves.
- La interfaz debe recordar que la estacion se opera en equipo con tierra.
- La preparacion de una EVA debe seguir una lista de pasos ordenada.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-estacion-espacial.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-estacion-espacial.md)
