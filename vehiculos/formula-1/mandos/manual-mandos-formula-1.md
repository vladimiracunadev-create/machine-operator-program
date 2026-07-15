# 🎛️ Mandos e instrumentos de la Fórmula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · 🎛️ Mandos

## Vista general

El puesto de mando de un monoplaza se concentra en el volante y en los pedales.
El volante es una computadora: reune dirección, cambios, pantalla de datos y
decenas de ajustes. El piloto va tumbado dentro del monocasco, con los pies casi
al mismo nivel que las manos y la cabeza fija por el arco de protección.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Volante | Dirección | Giro | Orientar ruedas delanteras | Alta | Recorrido corto y muy directo. |
| Volante detrás | Leva de subir marcha | Leva derecha | Subir de marcha | Alta | Secuencial, sin embrague en marcha. |
| Volante detrás | Leva de bajar marcha | Leva izquierda | Reducir de marcha | Alta | Ayuda a la frenada. |
| Volante detrás | Levas de embrague | Levas dobles | Embragar en salida | Alta | Solo para arrancar y en boxes. |
| Volante | Botón DRS | Botón | Abrir aleron trasero | Alta | Solo en zonas permitidas. |
| Volante | Botón de radio | Botón | Hablar con el equipo | Media | Comunicación con el muro. |
| Volante | Botón de impulso ERS | Botón | Solicitar entrega eléctrica | Alta | Gestión de energía por vuelta. |
| Volante | Ruletas de ajuste | Selectores | Reparto de frenada, mezcla, diferencial | Alta | Cambian el comportamiento en pista. |
| Volante | Limitador de boxes | Botón | Limitar velocidad en el pit lane | Alta | Obligatorio en boxes. |
| Piso | Pedal de acelerador | Pedal | Regular potencia | Alta | Muy progresivo. |
| Piso | Pedal de freno | Pedal | Frenar | Alta | Esfuerzo alto, gran precisión. |

## Instrumentos principales

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Pantalla del volante | Datos de vuelta y coche | varios | Alta | Configurable por página. |
| Marcha actual | Marcha engranada | número/N | Alta | Siempre visible. |
| Luces de cambio | Momento de cambiar | luces LED | Alta | Guian el cambio óptimo. |
| Delta de tiempo | Diferencia con referencia | segundos | Alta | Sabe si gana o pierde tiempo. |
| Estado de energía ERS | Carga y despliegue | porcentaje | Alta | Clave para la gestión de batería. |
| Temperaturas | Neumáticos, frenos, motor | grados | Alta | Ventanas de funcionamiento. |
| Presiones | Neumáticos y aceite | bar | Media | Vigilancia de fiabilidad. |

## Entradas de simulación

| Acción | Teclado | Controlador | Volante de sim | Comentarios |
| --- | --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Pedal acelerador | Progresivo, controla tracción. |
| Frenar | Flecha abajo | Gatillo izquierdo | Pedal de freno | Modula fuerza y evita bloqueo. |
| Subir marcha | E | Leva derecha | Leva derecha | Secuencial. |
| Bajar marcha | Q | Leva izquierda | Leva izquierda | Reducir antes de curva. |
| Girar | Flechas izq/der | Stick izquierdo | Giro del volante | Recorrido corto. |
| DRS | Tecla D | Botón asignado | Botón DRS | Solo en zona DRS. |
| Impulso ERS | Tecla Espacio | Botón asignado | Botón ERS | Gestión de energía. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Detenido | En boxes o parrilla | Pantalla en modo garaje | Encender, calibrar, salir. |
| En pista | Rodando en el trazado | Delta y marcha activos | Acelerar, frenar, cambiar, DRS. |
| Vuelta rápida | Buscando mejor tiempo | Luces de cambio y delta | Gestionar energía y neumáticos. |
| Boxes | Parada técnica | Limitador activo | Limitar velocidad, cambiar gomas. |
| Bandera / alerta | Precaución en pista | Testigos y radio | Levantar, respetar bandera. |

## Observaciones ergonomicas

- La pantalla del volante debe priorizar marcha, delta y estado de energía.
- El limitador de boxes debe ser inconfundible para no exceder el límite.
- Reparto de frenada y modos de energía son ajustes frecuentes: la interfaz de
  simulación debe hacerlos accesibles sin distraer del pilotaje.
- El DRS solo debe habilitarse cuando la simulación permite la zona.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-formula-1.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-formula-1.md)
