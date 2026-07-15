# 🎛️ Mandos e instrumentos del avión pequeño

[🏠 Inicio](../../../README.md) · [🛩️ Curso: Aviones pequeños](../README.md) · 🎛️ Mandos

## Vista general

La cabina de un avión pequeño concentra los mandos de vuelo, los mandos de motor y
el panel de instrumentos. El piloto vuela con las dos manos y los dos pies: el
yugo controla cabeceo y alabeo, los pedales controlan la guiñada y los frenos, y
la mano libre gestiona potencia, mezcla y flaps. El panel al frente muestra el
estado del vuelo.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Frente | Yugo o bastón | Volante / palanca | Cabeceo y alabeo | Alta | Adelante-atras cabecea; giro alabea. |
| Piso | Pedales de timón | Pedales | Guiñada y coordinación | Alta | También accionan los frenos. |
| Consola | Acelerador (throttle) | Palanca | Regular potencia del motor | Alta | Controla el empuje. |
| Consola | Mezcla (mixture) | Palanca | Proporción aire-combustible | Alta | Se empobrece con la altitud. |
| Consola | Flaps | Palanca / selector | Sustentación y resistencia | Media | Para despegue y aterrizaje. |
| Consola | Compensador (trim) | Rueda / botón | Aliviar fuerza en el yugo | Media | Estabiliza la actitud elegida. |
| Panel | Interruptores eléctricos | Botones | Luces, bombas, avionica | Media | Encendido por checklist. |
| Panel | Magnetos y arranque | Llave | Encender y apagar el motor | Alta | Prueba de magnetos previa. |
| Panel | Radio y transponder | Teclado | Comunicar y ser visto en radar | Alta | Frecuencias y código asignado. |
| Panel | Instrumentos | Relojes / pantalla | Mostrar estado del vuelo | Alta | Ver sección de instrumentos. |

## Instrumentos de vuelo

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Anemómetro (velocidad) | Velocidad respecto al aire | nudos | Alta | Clave para evitar la pérdida. |
| Altímetro | Altitud sobre el nivel de referencia | pies | Alta | Se ajusta con la presión local. |
| Variómetro | Velocidad vertical | pies/min | Media | Muestra ascenso o descenso. |
| Horizonte artificial | Actitud (cabeceo y alabeo) | grados | Alta | Referencia sin ver el exterior. |
| Indicador de rumbo | Dirección de la nariz | grados | Alta | Se alinea con la brújula. |
| Coordinador de viraje | Ritmo de viraje y coordinación | - | Media | La bolita indica vuelo coordinado. |
| Tacómetro | Régimen del motor / hélice | rpm | Media | Ayuda a ajustar potencia. |
| Instrumentos de motor | Aceite, combustible, temperatura | varias | Alta | Vigilan la salud del motor. |

## Entradas de simulación

| Acción | Teclado | Controlador | Palanca de vuelo | Comentarios |
| --- | --- | --- | --- | --- |
| Cabecear | Flechas arriba/abajo | Stick eje Y | Adelante-atras | Sube o baja el morro. |
| Alabear | Flechas izq/der | Stick eje X | Giro lateral | Inclina las alas. |
| Guiñar | Teclas Z / X | Gatillos / pedales | Pedales | Coordina el viraje. |
| Potencia | Teclas F2 / F3 | Gatillo derecho | Throttle | Sube o baja el empuje. |
| Flaps | Tecla F | Botón | Selector de flaps | Por etapas. |
| Trim | Teclas coma / punto | Cruceta | Rueda de trim | Alivia la fuerza sostenida. |
| Frenos | Tecla B | Botón | Punta de pedales | Solo en tierra. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En tierra apagado | Motor detenido | Panel sin energía | Checklist, encender sistemas. |
| Motor en marcha | Rodando o detenido en tierra | Tacómetro activo | Rodar, alinear, despegar. |
| En vuelo | Aeronave volando | Anemómetro y altímetro activos | Ascender, virar, crucero, descender. |
| Aproximación | Preparando aterrizaje | Flaps y velocidad de aproximación | Configurar, alinear, aterrizar. |
| Emergencia | Falla o riesgo | Testigos de alerta | Aplicar checklist de emergencia. |

## Observaciones ergonomicas

- El anemómetro y el altímetro deben verse siempre; son críticos para la seguridad.
- El horizonte artificial es la referencia principal si no se ve el exterior.
- El acelerador, la mezcla y los flaps deben quedar bien diferenciados al tacto.
- El corte de motor y los magnetos deben ser accesibles y reconocibles.
- La interfaz de simulación debería guiar el uso de checklist en cada fase.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-avion-pequeno.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-avion-pequeno.md)
