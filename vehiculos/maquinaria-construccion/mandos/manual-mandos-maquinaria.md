# 🎛️ Mandos e instrumentos de la maquinaria de construcción

[🏠 Inicio](../../../README.md) · [🚧 Curso: Maquinaria de construcción](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de la maquinaria de construcción se organiza en torno a dos
**joysticks** que controlan el brazo, el cucharón y el giro, más pedales y
palancas para la traslación. A diferencia de un vehículo de transporte, aquí casi
todo el trabajo se hace con la máquina detenida y el foco está en coordinar los
movimientos hidráulicos. La cabina protege con estructuras ROPS y FOPS.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano izquierda | Joystick izquierdo | Palanca proporcional | Giro y balancín | Alta | Combina rotación y acercar el brazo. |
| Mano derecha | Joystick derecho | Palanca proporcional | Pluma y cucharón | Alta | Sube el brazo y cierra el cucharón. |
| Pies | Pedales de traslación | Pedales o palancas | Mover cada oruga | Alta | Giro diferencial de la máquina. |
| Consola | Acelerador del motor | Dial o palanca | Fijar régimen de trabajo | Alta | Se mantiene constante en faena. |
| Consola | Bloqueo hidráulico | Palanca de seguridad | Anular los mandos | Alta | Se baja al subir o bajar de la cabina. |
| Consola | Herramienta auxiliar | Botón o rueda | Martillo, pinza u otra | Media | Según el implemento montado. |
| Cabina | Luces y bocina | Botones | Alumbrar y advertir | Media | Bocina y alarma de retroceso. |
| Cabina | Cámaras | Pantalla | Ver puntos ciegos | Media | Visión trasera y lateral. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Tacómetro | Régimen del motor | rpm | Alta | Guía el régimen de trabajo. |
| Temperatura hidráulica | Calor del aceite | grados | Alta | El aceite caliente pierde eficacia. |
| Temperatura del motor | Calor del refrigerante | grados | Alta | Vigila el esfuerzo continuo. |
| Presión hidráulica | Empuje del sistema | bar | Alta | Fuerza disponible de trabajo. |
| Nivel de combustible | Diesel restante | fracción | Alta | Autonomía de la jornada. |
| Cuentahoras | Horas de trabajo | horas | Alta | Base del mantenimiento. |
| Testigos | Estado de sistemas | luz | Alta | Filtros, carga, freno, alertas. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Subir/bajar pluma | W / S | Stick derecho vertical | Deslizar vertical | Proporcional a lo desplazado. |
| Abrir/cerrar cucharón | A / D | Stick derecho horizontal | Deslizar horizontal | Llena y descarga el cucharón. |
| Acercar/alejar balancín | R / F | Stick izquierdo vertical | Deslizar vertical | Extiende y recoge el brazo. |
| Girar superestructura | Q / E | Stick izquierdo horizontal | Deslizar horizontal | Rota 360 grados. |
| Trasladar | Flechas | Gatillos | Botones de oruga | Giro diferencial. |
| Bloqueo hidráulico | Tecla L | Botón dedicado | Interruptor | Anula mandos al entrar o salir. |
| Herramienta auxiliar | Tecla T | Botón | Botón implemento | Martillo, pinza u otro. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Apagado | Motor detenido | Tablero off | Encender, inspeccionar. |
| Preparado | Motor en marcha, mandos bloqueados | Bloqueo activo | Desbloquear para operar. |
| Trasladando | Moviendose por la faena | Traslación activa | Avanzar, girar, posicionar. |
| Trabajando | Excavando o empujando | Hidráulica en carga | Coordinar brazo, cucharón y giro. |
| Emergencia | Riesgo o falla | Testigos de alerta | Bloquear mandos, bajar carga, detener. |

## Observaciones ergonomicas

- Los dos joysticks deben responder de forma proporcional y previsible.
- El bloqueo hidráulico debe accionarse siempre al subir o bajar de la cabina.
- Las cámaras y espejos son esenciales por los grandes puntos ciegos.
- La interfaz de simulación debería advertir el acercamiento al límite de vuelco y
  la presencia de personas en el radio de giro.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-maquinaria.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-maquinaria.md)
