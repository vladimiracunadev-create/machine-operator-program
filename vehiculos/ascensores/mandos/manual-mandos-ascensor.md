# 🎛️ Mandos e instrumentos del ascensor

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · 🎛️ Mandos

## Vista general

El ascensor no tiene un "conductor": el usuario pide un viaje y el controlador lo
ejecuta. Los mandos se reparten entre la botonera de piso (llamada), la botonera
de cabina (destino) y los indicadores. Un tecnico usa ademas controles de
mantencion que no estan al alcance del publico.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Piso | Boton de llamada | Pulsador | Pedir la cabina en un sentido | Alta | Sube o baja segun necesidad. |
| Cabina | Botones de piso | Pulsadores | Elegir destino | Alta | Uno por planta. |
| Cabina | Boton de apertura | Pulsador | Mantener puerta abierta | Media | Comodidad y seguridad. |
| Cabina | Boton de cierre | Pulsador | Adelantar el cierre | Baja | Acelera el viaje. |
| Cabina | Boton de alarma | Pulsador | Pedir ayuda | Alta | Comunicacion con conserjeria. |
| Cabina | Parada de emergencia | Pulsador | Detener el equipo | Alta | Uso solo ante riesgo. |
| Cabina | Intercomunicador | Boton | Hablar con el exterior | Alta | Requisito de seguridad. |
| Tecnico | Modo inspeccion | Llave o selector | Operar en mantencion | Alta | Solo personal competente. |

## Instrumentos e indicadores

| Instrumento | Muestra | Formato | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Indicador de posicion | Piso actual | numero/letra | Alta | En cabina y en pisos. |
| Flechas de sentido | Sube o baja | flecha | Alta | Orientan al usuario. |
| Indicador de sobrecarga | Exceso de peso | luz/sonido | Alta | Impide arrancar sobrecargado. |
| Indicador de puerta | Puerta abierta o cerrada | luz | Media | Estado del acceso. |
| Testigo de fuera de servicio | Equipo detenido | luz/cartel | Alta | Avisa mantencion o falla. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Pantalla tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Llamar en piso | Tecla arriba/abajo | Boton asignado | Boton de llamada | Define sentido. |
| Elegir destino | Teclas numericas | Cruceta | Botones de piso | Uno por planta. |
| Abrir puerta | Tecla O | Boton | Boton apertura | Mantiene abierto. |
| Cerrar puerta | Tecla C | Boton | Boton cierre | Adelanta el cierre. |
| Alarma | Tecla A | Boton | Boton alarma | Pide ayuda. |
| Parada de emergencia | Tecla E | Boton | Boton parada | Solo ante riesgo. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Reposo | Cabina detenida en un piso | Posicion fija | Recibir llamada. |
| Viajando | Cabina en movimiento | Flechas y posicion | Continuar hasta destino. |
| En parada | Puerta abierta en piso | Puerta abierta | Entrar, salir, elegir destino. |
| Sobrecarga | Exceso de peso | Alerta de sobrecarga | No arranca; reducir carga. |
| Fuera de servicio | Mantencion o falla | Cartel y testigo | Solo modo inspeccion tecnico. |

## Observaciones ergonomicas

- El indicador de posicion y las flechas deben verse siempre con claridad.
- La botonera debe ser accesible, con marcas en relieve y braille.
- Alarma e intercomunicador deben ser inconfundibles y funcionar sin energia
  normal.
- El modo inspeccion es solo para personal competente; la simulacion debe
  distinguirlo del uso publico.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-ascensor.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-ascensor.md)
