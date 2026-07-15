# 🎛️ Mandos e instrumentos del ascensor

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · 🎛️ Mandos

## Vista general

El ascensor no tiene un "conductor": el usuario pide un viaje y el controlador lo
ejecuta. Los mandos se reparten entre la botonera de piso (llamada), la botonera
de cabina (destino) y los indicadores. Un técnico usa además controles de
mantención que no están al alcance del público.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Piso | Botón de llamada | Pulsador | Pedir la cabina en un sentido | Alta | Sube o baja según necesidad. |
| Cabina | Botones de piso | Pulsadores | Elegir destino | Alta | Uno por planta. |
| Cabina | Botón de apertura | Pulsador | Mantener puerta abierta | Media | Comodidad y seguridad. |
| Cabina | Botón de cierre | Pulsador | Adelantar el cierre | Baja | Acelera el viaje. |
| Cabina | Botón de alarma | Pulsador | Pedir ayuda | Alta | Comunicación con conserjería. |
| Cabina | Parada de emergencia | Pulsador | Detener el equipo | Alta | Uso solo ante riesgo. |
| Cabina | Intercomunicador | Botón | Hablar con el exterior | Alta | Requisito de seguridad. |
| Técnico | Modo inspección | Llave o selector | Operar en mantención | Alta | Solo personal competente. |

## Instrumentos e indicadores

| Instrumento | Muestra | Formato | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Indicador de posición | Piso actual | número/letra | Alta | En cabina y en pisos. |
| Flechas de sentido | Sube o baja | flecha | Alta | Orientan al usuario. |
| Indicador de sobrecarga | Exceso de peso | luz/sonido | Alta | Impide arrancar sobrecargado. |
| Indicador de puerta | Puerta abierta o cerrada | luz | Media | Estado del acceso. |
| Testigo de fuera de servicio | Equipo detenido | luz/cartel | Alta | Avisa mantención o falla. |

## Entradas de simulación

| Acción | Teclado | Controlador | Pantalla táctil | Comentarios |
| --- | --- | --- | --- | --- |
| Llamar en piso | Tecla arriba/abajo | Botón asignado | Botón de llamada | Define sentido. |
| Elegir destino | Teclas numéricas | Cruceta | Botones de piso | Uno por planta. |
| Abrir puerta | Tecla O | Botón | Botón apertura | Mantiene abierto. |
| Cerrar puerta | Tecla C | Botón | Botón cierre | Adelanta el cierre. |
| Alarma | Tecla A | Botón | Botón alarma | Pide ayuda. |
| Parada de emergencia | Tecla E | Botón | Botón parada | Solo ante riesgo. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Reposo | Cabina detenida en un piso | Posición fija | Recibir llamada. |
| Viajando | Cabina en movimiento | Flechas y posición | Continuar hasta destino. |
| En parada | Puerta abierta en piso | Puerta abierta | Entrar, salir, elegir destino. |
| Sobrecarga | Exceso de peso | Alerta de sobrecarga | No arranca; reducir carga. |
| Fuera de servicio | Mantención o falla | Cartel y testigo | Solo modo inspección técnico. |

## Observaciones ergonomicas

- El indicador de posición y las flechas deben verse siempre con claridad.
- La botonera debe ser accesible, con marcas en relieve y braille.
- Alarma e intercomunicador deben ser inconfundibles y funcionar sin energía
  normal.
- El modo inspección es solo para personal competente; la simulación debe
  distinguirlo del uso público.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-ascensor.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-ascensor.md)
