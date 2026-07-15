# 🎛️ Mandos e instrumentos de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🎛️ Mandos

## Vista general

La cabina de una nave espacial concentra el control de actitud, el control de
empuje, la energía, la navegación y el soporte vital. A diferencia de un avión, no
hay superficies aerodinámicas: la orientación se logra con propulsores y ruedas de
reacción. Los paneles muestran órbita, recursos y estado de los sistemas.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Consola | Control de actitud | Palanca / botones | Orientar la nave | Alta | Acciona propulsores RCS. |
| Consola | Control de empuje | Palanca | Encender el motor principal | Alta | Para maniobras orbitales. |
| Panel | Panel de energía | Interruptores | Gestionar potencia | Alta | Reparte energía entre sistemas. |
| Panel | Navegación | Teclado / pantalla | Calcular maniobras | Alta | Muestra órbita y objetivo. |
| Panel | Soporte vital | Mandos / lecturas | Aire, agua, CO2, temperatura | Alta | Vital en misiones largas. |
| Panel | Acoplamiento | Palanca fina | Unir con otra nave o estación | Media | Maniobra lenta y precisa. |
| Panel | Comunicaciones | Radio | Contacto con control | Media | Con retardo a gran distancia. |
| Panel | Alarmas | Luces / sonido | Avisar fallas | Alta | Presión, energía, temperatura. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Indicador de órbita | Forma y altura de la órbita | km | Alta | Muestra apogeo y perigeo. |
| Delta-v disponible | Capacidad de maniobra restante | m/s | Alta | Depende del propelente. |
| Actitud | Orientación de la nave | grados | Alta | Referencia para apuntar. |
| Velocidad relativa | Respecto a un objetivo | m/s | Alta | Clave en acoplamiento. |
| Recursos vitales | Oxígeno, CO2, agua, energía | varias | Alta | Estado del soporte vital. |
| Temperatura | Interior y escudo | grados | Alta | Crítica en la reentrada. |

## Entradas de simulación

| Acción | Teclado | Controlador | Panel táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Girar (actitud) | Teclas WASDQE | Stick derecho | Zona de actitud | Cabecear, guiñar, rolar. |
| Trasladar (RCS) | Teclas IJKL | Stick izquierdo | Zona de traslación | Movimiento fino en acoplamiento. |
| Empuje principal | Shift / Ctrl | Gatillos | Barra de empuje | Para maniobras orbitales. |
| Planificar maniobra | Tecla M | Botón | Editor de nodos | Ajusta delta-v y momento. |
| Gestionar energía | Tecla P | Cruceta | Panel de energía | Reparte potencia. |
| Soporte vital | Tecla L | Botón | Panel vital | Revisa aire, agua, CO2. |
| Acoplar | Tecla espacio | Botón | Botón de captura | Alinear y unir suave. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En plataforma | Antes del lanzamiento | Checklist en pantalla | Revisar sistemas, encender. |
| Ascenso | Subiendo a la órbita | Empuje y velocidad activos | Guiar, separar etapas. |
| En órbita | Vuelo orbital estable | Indicador de órbita activo | Maniobrar, acoplar, operar. |
| Maniobra | Cambio de órbita | Delta-v en uso | Encender motor, controlar actitud. |
| Reentrada | Regreso a la atmósfera | Temperatura del escudo | Orientar escudo, controlar descenso. |
| Emergencia | Falla o riesgo | Alarmas activas | Aislar falla, aplicar checklist. |

## Observaciones ergonomicas

- El delta-v disponible y los recursos vitales deben verse siempre.
- Los controles de actitud y traslación deben distinguirse con claridad.
- Las alarmas de presión, energía y temperatura deben ser inconfundibles.
- El acoplamiento exige controles finos y una vista clara del objetivo.
- La interfaz debe separar lo real de lo ficticio con etiquetas claras.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-espacial.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-nave-espacial.md)
