# 🎛️ Mandos e instrumentos del caza estelar

[🏠 Inicio](../../../README.md) · [🛸 Curso: Caza estelar](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puesto de mando de un caza estelar realista se parece más a la cabina de una
nave espacial que a la de un avión. Como la nave se mueve en tres dimensiones y
sin rozamiento, el piloto no solo "gira": controla por separado la orientación
(hacia donde apunta) y la traslación (hacia donde se desplaza). Esa separación
es la gran diferencia con conducir un avión.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano derecha | Palanca de orientación | Joystick 3 ejes | Rotar cabeceo, alabeo y guiñada con RCS | Alta | No cambia el rumbo por si sola. |
| Mano izquierda | Palanca de traslación | Mando 3 ejes | Empujar la nave arriba, abajo o de lado | Alta | Usa RCS de traslación. |
| Mano izquierda | Acelerador principal | Palanca lineal | Regular empuje del motor principal | Alta | Cambia la velocidad, no la mantiene. |
| Panel central | Gestión de energía | Botonera | Repartir energía entre sistemas | Media | Motores, sensores, armamento. |
| Panel derecho | Control de armamento | Botones y gatillo | Preparar y disparar | Media | Puntería asistida por computadora. |
| Panel izquierdo | Modo de vuelo | Selector | Elegir asistencia de la computadora | Media | Incluye freno de rotación automático. |
| Consola | Instrumentos | Pantallas | Mostrar estado y sensores | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Vector de velocidad | Dirección y módulo del movimiento | m/s | Alta | Puede diferir de hacia donde apunta la nave. |
| Indicador de orientación | Hacia donde apunta la nave | grados | Alta | Cabeceo, alabeo y guiñada. |
| Presupuesto de maniobra | Delta-v restante | m/s | Alta | Depende del propelente que queda. |
| Nivel de propelente | Propelente restante | porcentaje | Alta | Sin propelente no hay maniobra. |
| Temperatura | Calor acumulado | grados | Media | Se disipa lento por radiadores. |
| Sensores de largo alcance | Objetos lejanos | distancia | Alta | El combate real es a gran distancia. |

## Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Empuje adelante | Flecha arriba | Gatillo derecho | Acelera, no fija una velocidad. |
| Rotar cabeceo | W y S | Stick derecho vertical | Apunta la nariz arriba o abajo. |
| Rotar guiñada | A y D | Stick derecho horizontal | Apunta la nariz a los lados. |
| Rotar alabeo | Q y E | Botones laterales | Gira la nave sobre su eje. |
| Trasladar lateral | J y L | Stick izquierdo | Desplaza sin cambiar orientación. |
| Freno de rotación | Barra espaciadora | Botón central | Aplica RCS para dejar de girar. |
| Disparar | Ctrl | Gatillo izquierdo | Con puntería asistida. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En reposo | Nave sin empuje, puede girar sobre su eje | Vector de velocidad casi cero | Orientar, planificar maniobra. |
| En impulso | Motor principal encendido | Acelerador activo | Cambiar velocidad, orientar. |
| Deriva | Sin motor, mantiene velocidad | Velocidad constante | Orientar con RCS, apuntar. |
| Emergencia | Falla o poco propelente | Alerta de delta-v | Ahorrar propelente, estabilizar. |

## Observaciones ergonomicas

- La interfaz debe mostrar a la vez hacia donde apunta la nave y hacia donde se
  mueve, porque en el vacío no coinciden.
- El presupuesto de maniobra (delta-v) es tan importante como el combustible en
  un vehículo terrestre: cuando se agota, ya no hay como maniobrar.
- El freno de rotación debe ser evidente: la nave no deja de girar sola.
- Conviene un modo de asistencia para principiantes que evite gastar propelente
  de forma innecesaria.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-caza-estelar.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-caza-estelar.md)
