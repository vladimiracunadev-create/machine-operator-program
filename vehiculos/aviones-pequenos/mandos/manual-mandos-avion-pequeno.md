# 🎛️ Mandos e instrumentos del avion pequeno

[🏠 Inicio](../../../README.md) · [🛩️ Curso: Aviones pequenos](../README.md) · 🎛️ Mandos

## Vista general

La cabina de un avion pequeno concentra los mandos de vuelo, los mandos de motor y
el panel de instrumentos. El piloto vuela con las dos manos y los dos pies: el
yugo controla cabeceo y alabeo, los pedales controlan la guinada y los frenos, y
la mano libre gestiona potencia, mezcla y flaps. El panel al frente muestra el
estado del vuelo.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Frente | Yugo o baston | Volante / palanca | Cabeceo y alabeo | Alta | Adelante-atras cabecea; giro alabea. |
| Piso | Pedales de timon | Pedales | Guinada y coordinacion | Alta | Tambien accionan los frenos. |
| Consola | Acelerador (throttle) | Palanca | Regular potencia del motor | Alta | Controla el empuje. |
| Consola | Mezcla (mixture) | Palanca | Proporcion aire-combustible | Alta | Se empobrece con la altitud. |
| Consola | Flaps | Palanca / selector | Sustentacion y resistencia | Media | Para despegue y aterrizaje. |
| Consola | Compensador (trim) | Rueda / boton | Aliviar fuerza en el yugo | Media | Estabiliza la actitud elegida. |
| Panel | Interruptores electricos | Botones | Luces, bombas, avionica | Media | Encendido por checklist. |
| Panel | Magnetos y arranque | Llave | Encender y apagar el motor | Alta | Prueba de magnetos previa. |
| Panel | Radio y transponder | Teclado | Comunicar y ser visto en radar | Alta | Frecuencias y codigo asignado. |
| Panel | Instrumentos | Relojes / pantalla | Mostrar estado del vuelo | Alta | Ver seccion de instrumentos. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Anemometro (velocidad) | Velocidad respecto al aire | nudos | Alta | Clave para evitar la perdida. |
| Altimetro | Altitud sobre el nivel de referencia | pies | Alta | Se ajusta con la presion local. |
| Variometro | Velocidad vertical | pies/min | Media | Muestra ascenso o descenso. |
| Horizonte artificial | Actitud (cabeceo y alabeo) | grados | Alta | Referencia sin ver el exterior. |
| Indicador de rumbo | Direccion de la nariz | grados | Alta | Se alinea con la brujula. |
| Coordinador de viraje | Ritmo de viraje y coordinacion | - | Media | La bolita indica vuelo coordinado. |
| Tacometro | Regimen del motor / helice | rpm | Media | Ayuda a ajustar potencia. |
| Instrumentos de motor | Aceite, combustible, temperatura | varias | Alta | Vigilan la salud del motor. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Palanca de vuelo | Comentarios |
| --- | --- | --- | --- | --- |
| Cabecear | Flechas arriba/abajo | Stick eje Y | Adelante-atras | Sube o baja el morro. |
| Alabear | Flechas izq/der | Stick eje X | Giro lateral | Inclina las alas. |
| Guinar | Teclas Z / X | Gatillos / pedales | Pedales | Coordina el viraje. |
| Potencia | Teclas F2 / F3 | Gatillo derecho | Throttle | Sube o baja el empuje. |
| Flaps | Tecla F | Boton | Selector de flaps | Por etapas. |
| Trim | Teclas coma / punto | Cruceta | Rueda de trim | Alivia la fuerza sostenida. |
| Frenos | Tecla B | Boton | Punta de pedales | Solo en tierra. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En tierra apagado | Motor detenido | Panel sin energia | Checklist, encender sistemas. |
| Motor en marcha | Rodando o detenido en tierra | Tacometro activo | Rodar, alinear, despegar. |
| En vuelo | Aeronave volando | Anemometro y altimetro activos | Ascender, virar, crucero, descender. |
| Aproximacion | Preparando aterrizaje | Flaps y velocidad de aproximacion | Configurar, alinear, aterrizar. |
| Emergencia | Falla o riesgo | Testigos de alerta | Aplicar checklist de emergencia. |

## Observaciones ergonomicas

- El anemometro y el altimetro deben verse siempre; son criticos para la seguridad.
- El horizonte artificial es la referencia principal si no se ve el exterior.
- El acelerador, la mezcla y los flaps deben quedar bien diferenciados al tacto.
- El corte de motor y los magnetos deben ser accesibles y reconocibles.
- La interfaz de simulacion deberia guiar el uso de checklist en cada fase.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-avion-pequeno.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-avion-pequeno.md)
