# 🎛️ Mandos e instrumentos del Nautilus

[🏠 Inicio](../../../README.md) · [🐙 Curso: Nautilus](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; el Nautilus de Julio Verne (1870) es de dominio publico; otros derechos pertenecen a sus titulares.

## Vista general

El puesto de mando de un submarino imaginado como el Nautilus se organiza
alrededor de tres decisiones: cuanto lastre llevar, hacia donde apuntar y a que
velocidad avanzar. A diferencia de un vehiculo terrestre, aqui el control de la
profundidad es tan importante como el del rumbo, y todo se hace sin ver el
exterior salvo por ventanas o instrumentos.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Panel de lastre | Valvulas de inundacion | Palanca | Dejar entrar agua para sumergir | Alta | Aumenta el peso de la nave. |
| Panel de lastre | Purga de aire comprimido | Palanca | Expulsar agua para emerger | Alta | Reduce el peso de la nave. |
| Puesto de gobierno | Timon de direccion | Rueda | Girar a babor o estribor | Alta | Rumbo horizontal. |
| Puesto de gobierno | Timones de profundidad | Palanca | Inclinar arriba o abajo | Alta | Ajuste fino de profundidad. |
| Consola de energia | Regulador de propulsion | Mando | Regular la potencia de la helice | Alta | Controla la velocidad. |
| Consola de energia | Corte general | Boton | Detener la propulsion | Alta | Parada de seguridad. |
| Soporte vital | Renovacion de aire | Valvula | Ventilar y reponer oxigeno | Alta | Vital en inmersiones largas. |
| Observacion | Iluminacion exterior | Interruptor | Alumbrar el entorno | Media | Util en aguas oscuras. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Profundimetro | Profundidad actual | metros | Alta | Clave para no pasar el limite del casco. |
| Manometro | Presion exterior | atmosferas | Alta | Sube con la profundidad. |
| Indicador de flotabilidad | Peso frente a empuje | relativa | Alta | Muestra si la nave sube o baja. |
| Brujula | Rumbo | grados | Alta | Orientacion horizontal. |
| Corredera | Velocidad de avance | nudos | Media | Ayuda a estimar distancia. |
| Nivel de aire | Oxigeno disponible | fraccion | Alta | Limite real de la inmersion. |
| Carga de energia | Energia restante | fraccion | Alta | Define la autonomia. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Inundar lastre | Tecla F | Gatillo izquierdo | Boton bajar | Sumerge la nave, progresivo. |
| Purgar lastre | Tecla R | Gatillo derecho | Boton subir | Emerge la nave, progresivo. |
| Timon izquierda | Flecha izquierda | Stick izquierdo | Deslizar izquierda | Gira a babor. |
| Timon derecha | Flecha derecha | Stick derecho | Deslizar derecha | Gira a estribor. |
| Morro arriba | Flecha arriba | Cruceta arriba | Boton proa arriba | Timones de profundidad. |
| Morro abajo | Flecha abajo | Cruceta abajo | Boton proa abajo | Timones de profundidad. |
| Acelerar | Tecla W | Boton A | Zona derecha | Mas potencia a la helice. |
| Ventilar aire | Tecla V | Boton lateral | Boton aire | Solo posible en superficie. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En superficie | Flota, aire renovable | Profundimetro en cero | Ventilar, inundar lastre, navegar. |
| Sumergiendo | Ganando profundidad | Profundidad en aumento | Ajustar timones, vigilar presion. |
| A media agua | Flotabilidad neutra | Profundidad estable | Navegar, girar, acelerar. |
| Emergiendo | Perdiendo profundidad | Profundidad en descenso | Purgar lastre, controlar ascenso. |
| Emergencia | Riesgo o falla | Testigos de alerta | Purgar lastre, cortar propulsion. |

## Observaciones ergonomicas

- El profundimetro y el manometro deben verse siempre: marcan el limite fisico.
- El nivel de aire debe estar visible para no olvidar la autonomia respirable.
- La purga de lastre de emergencia tiene que ser accesible y reconocible.
- La interfaz debe dejar claro que ventilar el aire solo es posible en la
  superficie, no sumergido.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-nautilus.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-nautilus.md)
