# 🎛️ Mandos e instrumentos del avión de combate

[🏠 Inicio](../../../README.md) · [✈️ Curso: Aviones de combate](../README.md) · 🎛️ Mandos

## Vista general

La cabina de un avión de combate concentra los mandos de vuelo, el control de
potencia y las pantallas de vuelo. Este módulo describe **solo** los mandos
generales de vuelo, no sistemas de misión ni de armas. El piloto vuela con la
palanca (cabeceo y alabeo), los pedales (guiñada) y el acelerador (empuje),
apoyado en instrumentos de pantalla y un HUD frontal.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Central / lateral | Palanca de mando | Bastón | Cabeceo y alabeo | Alta | Manda las superficies vía fly-by-wire. |
| Piso | Pedales de timón | Pedales | Guiñada y frenos | Alta | Coordinan el viraje y frenan en tierra. |
| Consola | Acelerador (throttle) | Palanca | Regular empuje | Alta | Puede tener detente de posquemador. |
| Panel | Tren de aterrizaje | Palanca | Subir o bajar el tren | Media | Retráctil en vuelo. |
| Panel | Aerofrenos / flaps | Selector | Ajustar resistencia y sustentación | Media | Para maniobra y aproximación. |
| Panel | Pantallas multifunción | Botones | Mostrar datos de vuelo | Alta | Configurables por el piloto. |
| Panel | Comunicaciones | Teclado | Radio (uso general) | Media | En simulación, no sensible. |
| Cabina | Sistema de oxígeno | Mando | Soporte a gran altitud | Alta | Parte del equipo de vuelo. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocidad | Velocidad respecto al aire | nudos / Mach | Alta | A alta velocidad se usa el número de Mach. |
| Altímetro | Altitud | pies | Alta | Crítico a gran altura. |
| Horizonte / actitud | Cabeceo y alabeo | grados | Alta | Referencia principal del vuelo. |
| Indicador de rumbo | Dirección de la nariz | grados | Alta | Para navegar. |
| Acelerómetro (G) | Carga de maniobra | G | Alta | Muestra el esfuerzo estructural y físico. |
| Instrumentos de motor | Empuje, temperatura, combustible | varias | Alta | Vigilan la salud del motor. |
| HUD | Datos de vuelo al frente | varias | Alta | Permite volar sin mirar abajo. |

## Entradas de simulación

| Acción | Teclado | Controlador | Palanca de vuelo | Comentarios |
| --- | --- | --- | --- | --- |
| Cabecear | Flechas arriba/abajo | Stick eje Y | Adelante-atrás | Sube o baja el morro. |
| Alabear | Flechas izq/der | Stick eje X | Giro lateral | Inclina las alas. |
| Guiñar | Teclas Z / X | Gatillos / pedales | Pedales | Coordina el viraje. |
| Empuje | Teclas F2 / F3 | Gatillo derecho | Throttle | Sube o baja el empuje. |
| Posquemador | Tecla Shift | Botón | Detente del throttle | Empuje extra puntual. |
| Tren | Tecla G | Botón | Palanca de tren | Solo a baja velocidad. |
| Aerofrenos | Tecla B | Botón | Selector | Reduce la velocidad. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En tierra apagado | Motor detenido | Pantallas sin energía | Checklist, encender sistemas. |
| Motor en marcha | En tierra con motor activo | Instrumentos de motor activos | Rodar, alinear, despegar. |
| En vuelo | Aeronave volando | Velocidad y altitud activas | Ascender, virar, crucero, descender. |
| Maniobra | Vuelo con cargas G | Acelerómetro elevado | Controlar G, mantener energía. |
| Aproximación | Preparando aterrizaje | Tren y aerofrenos | Configurar, alinear, aterrizar. |
| Emergencia | Falla o riesgo | Alertas activas | Aplicar checklist de emergencia. |

## Observaciones ergonomicas

- El HUD y la velocidad deben verse sin bajar la vista.
- El acelerómetro ayuda a no exceder las cargas G seguras.
- La palanca y los pedales deben responder de forma suave con fly-by-wire.
- El corte de motor y el tren deben ser accesibles y reconocibles.
- La interfaz de simulación enfatiza la física del vuelo, no sistemas sensibles.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-avion-combate.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-avion-combate.md)
