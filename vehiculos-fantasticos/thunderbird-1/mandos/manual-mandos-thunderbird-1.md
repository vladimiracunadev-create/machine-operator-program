# 🎛️ Mandos e instrumentos de Thunderbird 1

[🏠 Inicio](../../../README.md) · [⚡ Curso: Thunderbird 1](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puesto de mando de un vehículo de respuesta rápida realista debe controlar
dos cosas a la vez: la potencia del motor que sostiene y eleva la nave, y la
orientación del chorro que decide si sube, flota o avanza. Esa combinación es la
gran diferencia con pilotar un avión normal, que solo se apoya en sus alas.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano izquierda | Palanca de potencia | Palanca lineal | Regular el empuje del motor | Alta | Decide si sube, flota o baja. |
| Mano derecha | Mando de toberas | Joystick 2 ejes | Inclinar el chorro del motor | Alta | Controla la transición vertical a horizontal. |
| Mano derecha | Palanca de actitud | Joystick 3 ejes | Ajustar cabeceo, alabeo y guiñada | Alta | Mantiene la nave nivelada al flotar. |
| Panel central | Gestión de energía | Botonera | Repartir energía entre sistemas | Media | Motor, sensores y servicios. |
| Panel derecho | Modo de vuelo | Selector | Elegir vertical, transición o crucero | Alta | Cambia como responden los mandos. |
| Panel izquierdo | Asistencia | Selector | Activar estabilización automática | Media | Ayuda a flotar sin oscilar. |
| Consola | Instrumentos | Pantallas | Mostrar estado y sensores | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Empuje relativo | Empuje frente al peso | porcentaje | Alta | Por encima de cien la nave sube. |
| Altura | Distancia al suelo | metros | Alta | Clave durante despegue y aterrizaje. |
| Velocidad horizontal | Avance hacia adelante | m/s | Alta | Cuando sube, las alas ayudan. |
| Ángulo de toberas | Inclinación del chorro | grados | Alta | Marca el grado de transición. |
| Nivel de combustible | Propelente restante | porcentaje | Alta | Flotar lo consume muy rápido. |
| Temperatura del motor | Calor acumulado | grados | Media | Limita el empuje sostenido. |

## Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Subir potencia | Flecha arriba | Gatillo derecho | Aumenta el empuje del motor. |
| Bajar potencia | Flecha abajo | Gatillo izquierdo | Reduce el empuje, la nave desciende. |
| Inclinar toberas | W y S | Stick derecho vertical | Pasa de vertical a horizontal. |
| Guiñada | A y D | Stick derecho horizontal | Apunta la nariz a los lados. |
| Alabeo | Q y E | Botones laterales | Nivela la nave sobre su eje. |
| Estabilizar | Barra espaciadora | Botón central | Mantiene el vuelo estacionario. |
| Cambiar modo | Tecla M | Botón de modo | Vertical, transición o crucero. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En tierra | Nave posada, motor al mínimo | Empuje bajo el peso | Encender motor, planificar despegue. |
| Estacionario | Flota a altura constante | Empuje igual al peso | Ajustar altura, iniciar transición. |
| Transición | Pasa de vertical a horizontal | Toberas inclinandose | Ganar velocidad, aliviar el motor. |
| Crucero | Vuela rápido apoyada en las alas | Velocidad horizontal alta | Avanzar, vigilar combustible. |
| Emergencia | Falla o poco combustible | Alerta de nivel bajo | Ahorrar potencia, aterrizar. |

## Observaciones ergonomicas

- La interfaz debe mostrar a la vez el empuje relativo al peso y la altura,
  porque de esa relación depende que la nave suba, flote o baje.
- El combustible es tan crítico como en un cohete: flotar lo consume muy rápido,
  así que conviene alertar pronto del nivel bajo.
- La transición debe ser gradual y clara: inclinar el chorro de golpe puede
  hacer perder altura antes de ganar velocidad.
- Conviene un modo de asistencia para principiantes que estabilice el vuelo
  estacionario y evite oscilaciones.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-thunderbird-1.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-thunderbird-1.md)
