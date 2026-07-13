# 🎛️ Mandos e instrumentos de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🎛️ Mandos

## Vista general

La cabina de una nave espacial concentra el control de actitud, el control de
empuje, la energia, la navegacion y el soporte vital. A diferencia de un avion, no
hay superficies aerodinamicas: la orientacion se logra con propulsores y ruedas de
reaccion. Los paneles muestran orbita, recursos y estado de los sistemas.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Consola | Control de actitud | Palanca / botones | Orientar la nave | Alta | Acciona propulsores RCS. |
| Consola | Control de empuje | Palanca | Encender el motor principal | Alta | Para maniobras orbitales. |
| Panel | Panel de energia | Interruptores | Gestionar potencia | Alta | Reparte energia entre sistemas. |
| Panel | Navegacion | Teclado / pantalla | Calcular maniobras | Alta | Muestra orbita y objetivo. |
| Panel | Soporte vital | Mandos / lecturas | Aire, agua, CO2, temperatura | Alta | Vital en misiones largas. |
| Panel | Acoplamiento | Palanca fina | Unir con otra nave o estacion | Media | Maniobra lenta y precisa. |
| Panel | Comunicaciones | Radio | Contacto con control | Media | Con retardo a gran distancia. |
| Panel | Alarmas | Luces / sonido | Avisar fallas | Alta | Presion, energia, temperatura. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Indicador de orbita | Forma y altura de la orbita | km | Alta | Muestra apogeo y perigeo. |
| Delta-v disponible | Capacidad de maniobra restante | m/s | Alta | Depende del propelente. |
| Actitud | Orientacion de la nave | grados | Alta | Referencia para apuntar. |
| Velocidad relativa | Respecto a un objetivo | m/s | Alta | Clave en acoplamiento. |
| Recursos vitales | Oxigeno, CO2, agua, energia | varias | Alta | Estado del soporte vital. |
| Temperatura | Interior y escudo | grados | Alta | Critica en la reentrada. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Panel tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Girar (actitud) | Teclas WASDQE | Stick derecho | Zona de actitud | Cabecear, guinar, rolar. |
| Trasladar (RCS) | Teclas IJKL | Stick izquierdo | Zona de traslacion | Movimiento fino en acoplamiento. |
| Empuje principal | Shift / Ctrl | Gatillos | Barra de empuje | Para maniobras orbitales. |
| Planificar maniobra | Tecla M | Boton | Editor de nodos | Ajusta delta-v y momento. |
| Gestionar energia | Tecla P | Cruceta | Panel de energia | Reparte potencia. |
| Soporte vital | Tecla L | Boton | Panel vital | Revisa aire, agua, CO2. |
| Acoplar | Tecla espacio | Boton | Boton de captura | Alinear y unir suave. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En plataforma | Antes del lanzamiento | Checklist en pantalla | Revisar sistemas, encender. |
| Ascenso | Subiendo a la orbita | Empuje y velocidad activos | Guiar, separar etapas. |
| En orbita | Vuelo orbital estable | Indicador de orbita activo | Maniobrar, acoplar, operar. |
| Maniobra | Cambio de orbita | Delta-v en uso | Encender motor, controlar actitud. |
| Reentrada | Regreso a la atmosfera | Temperatura del escudo | Orientar escudo, controlar descenso. |
| Emergencia | Falla o riesgo | Alarmas activas | Aislar falla, aplicar checklist. |

## Observaciones ergonomicas

- El delta-v disponible y los recursos vitales deben verse siempre.
- Los controles de actitud y traslacion deben distinguirse con claridad.
- Las alarmas de presion, energia y temperatura deben ser inconfundibles.
- El acoplamiento exige controles finos y una vista clara del objetivo.
- La interfaz debe separar lo real de lo ficticio con etiquetas claras.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-nave-espacial.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-nave-espacial.md)
