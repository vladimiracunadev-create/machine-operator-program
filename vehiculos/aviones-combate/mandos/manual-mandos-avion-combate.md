# 🎛️ Mandos e instrumentos del avion de combate

[🏠 Inicio](../../../README.md) · [✈️ Curso: Aviones de combate](../README.md) · 🎛️ Mandos

## Vista general

La cabina de un avion de combate concentra los mandos de vuelo, el control de
potencia y las pantallas de vuelo. Este modulo describe **solo** los mandos
generales de vuelo, no sistemas de mision ni de armas. El piloto vuela con la
palanca (cabeceo y alabeo), los pedales (guinada) y el acelerador (empuje),
apoyado en instrumentos de pantalla y un HUD frontal.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Central / lateral | Palanca de mando | Baston | Cabeceo y alabeo | Alta | Manda las superficies via fly-by-wire. |
| Piso | Pedales de timon | Pedales | Guinada y frenos | Alta | Coordinan el viraje y frenan en tierra. |
| Consola | Acelerador (throttle) | Palanca | Regular empuje | Alta | Puede tener detente de posquemador. |
| Panel | Tren de aterrizaje | Palanca | Subir o bajar el tren | Media | Retractil en vuelo. |
| Panel | Aerofrenos / flaps | Selector | Ajustar resistencia y sustentacion | Media | Para maniobra y aproximacion. |
| Panel | Pantallas multifuncion | Botones | Mostrar datos de vuelo | Alta | Configurables por el piloto. |
| Panel | Comunicaciones | Teclado | Radio (uso general) | Media | En simulacion, no sensible. |
| Cabina | Sistema de oxigeno | Mando | Soporte a gran altitud | Alta | Parte del equipo de vuelo. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocidad | Velocidad respecto al aire | nudos / Mach | Alta | A alta velocidad se usa el numero de Mach. |
| Altimetro | Altitud | pies | Alta | Critico a gran altura. |
| Horizonte / actitud | Cabeceo y alabeo | grados | Alta | Referencia principal del vuelo. |
| Indicador de rumbo | Direccion de la nariz | grados | Alta | Para navegar. |
| Acelerometro (G) | Carga de maniobra | G | Alta | Muestra el esfuerzo estructural y fisico. |
| Instrumentos de motor | Empuje, temperatura, combustible | varias | Alta | Vigilan la salud del motor. |
| HUD | Datos de vuelo al frente | varias | Alta | Permite volar sin mirar abajo. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Palanca de vuelo | Comentarios |
| --- | --- | --- | --- | --- |
| Cabecear | Flechas arriba/abajo | Stick eje Y | Adelante-atras | Sube o baja el morro. |
| Alabear | Flechas izq/der | Stick eje X | Giro lateral | Inclina las alas. |
| Guinar | Teclas Z / X | Gatillos / pedales | Pedales | Coordina el viraje. |
| Empuje | Teclas F2 / F3 | Gatillo derecho | Throttle | Sube o baja el empuje. |
| Posquemador | Tecla Shift | Boton | Detente del throttle | Empuje extra puntual. |
| Tren | Tecla G | Boton | Palanca de tren | Solo a baja velocidad. |
| Aerofrenos | Tecla B | Boton | Selector | Reduce la velocidad. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En tierra apagado | Motor detenido | Pantallas sin energia | Checklist, encender sistemas. |
| Motor en marcha | En tierra con motor activo | Instrumentos de motor activos | Rodar, alinear, despegar. |
| En vuelo | Aeronave volando | Velocidad y altitud activas | Ascender, virar, crucero, descender. |
| Maniobra | Vuelo con cargas G | Acelerometro elevado | Controlar G, mantener energia. |
| Aproximacion | Preparando aterrizaje | Tren y aerofrenos | Configurar, alinear, aterrizar. |
| Emergencia | Falla o riesgo | Alertas activas | Aplicar checklist de emergencia. |

## Observaciones ergonomicas

- El HUD y la velocidad deben verse sin bajar la vista.
- El acelerometro ayuda a no exceder las cargas G seguras.
- La palanca y los pedales deben responder de forma suave con fly-by-wire.
- El corte de motor y el tren deben ser accesibles y reconocibles.
- La interfaz de simulacion enfatiza la fisica del vuelo, no sistemas sensibles.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-avion-combate.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-avion-combate.md)
