# 🎛️ Mandos e instrumentos de la Formula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Formula 1](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un monoplaza se concentra en el volante y en los pedales.
El volante es una computadora: reune direccion, cambios, pantalla de datos y
decenas de ajustes. El piloto va tumbado dentro del monocasco, con los pies casi
al mismo nivel que las manos y la cabeza fija por el arco de proteccion.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Volante | Direccion | Giro | Orientar ruedas delanteras | Alta | Recorrido corto y muy directo. |
| Volante detras | Leva de subir marcha | Leva derecha | Subir de marcha | Alta | Secuencial, sin embrague en marcha. |
| Volante detras | Leva de bajar marcha | Leva izquierda | Reducir de marcha | Alta | Ayuda a la frenada. |
| Volante detras | Levas de embrague | Levas dobles | Embragar en salida | Alta | Solo para arrancar y en boxes. |
| Volante | Boton DRS | Boton | Abrir aleron trasero | Alta | Solo en zonas permitidas. |
| Volante | Boton de radio | Boton | Hablar con el equipo | Media | Comunicacion con el muro. |
| Volante | Boton de impulso ERS | Boton | Solicitar entrega electrica | Alta | Gestion de energia por vuelta. |
| Volante | Ruletas de ajuste | Selectores | Reparto de frenada, mezcla, diferencial | Alta | Cambian el comportamiento en pista. |
| Volante | Limitador de boxes | Boton | Limitar velocidad en el pit lane | Alta | Obligatorio en boxes. |
| Piso | Pedal de acelerador | Pedal | Regular potencia | Alta | Muy progresivo. |
| Piso | Pedal de freno | Pedal | Frenar | Alta | Esfuerzo alto, gran precision. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Pantalla del volante | Datos de vuelta y coche | varios | Alta | Configurable por pagina. |
| Marcha actual | Marcha engranada | numero/N | Alta | Siempre visible. |
| Luces de cambio | Momento de cambiar | luces LED | Alta | Guian el cambio optimo. |
| Delta de tiempo | Diferencia con referencia | segundos | Alta | Sabe si gana o pierde tiempo. |
| Estado de energia ERS | Carga y despliegue | porcentaje | Alta | Clave para la gestion de bateria. |
| Temperaturas | Neumaticos, frenos, motor | grados | Alta | Ventanas de funcionamiento. |
| Presiones | Neumaticos y aceite | bar | Media | Vigilancia de fiabilidad. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Volante de sim | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Pedal acelerador | Progresivo, controla traccion. |
| Frenar | Flecha abajo | Gatillo izquierdo | Pedal de freno | Modula fuerza y evita bloqueo. |
| Subir marcha | E | Leva derecha | Leva derecha | Secuencial. |
| Bajar marcha | Q | Leva izquierda | Leva izquierda | Reducir antes de curva. |
| Girar | Flechas izq/der | Stick izquierdo | Giro del volante | Recorrido corto. |
| DRS | Tecla D | Boton asignado | Boton DRS | Solo en zona DRS. |
| Impulso ERS | Tecla Espacio | Boton asignado | Boton ERS | Gestion de energia. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Detenido | En boxes o parrilla | Pantalla en modo garaje | Encender, calibrar, salir. |
| En pista | Rodando en el trazado | Delta y marcha activos | Acelerar, frenar, cambiar, DRS. |
| Vuelta rapida | Buscando mejor tiempo | Luces de cambio y delta | Gestionar energia y neumaticos. |
| Boxes | Parada tecnica | Limitador activo | Limitar velocidad, cambiar gomas. |
| Bandera / alerta | Precaucion en pista | Testigos y radio | Levantar, respetar bandera. |

## Observaciones ergonomicas

- La pantalla del volante debe priorizar marcha, delta y estado de energia.
- El limitador de boxes debe ser inconfundible para no exceder el limite.
- Reparto de frenada y modos de energia son ajustes frecuentes: la interfaz de
  simulacion debe hacerlos accesibles sin distraer del pilotaje.
- El DRS solo debe habilitarse cuando la simulacion permite la zona.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-formula-1.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-formula-1.md)
