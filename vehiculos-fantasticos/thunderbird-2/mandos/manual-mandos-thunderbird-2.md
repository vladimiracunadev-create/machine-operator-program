# 🎛️ Mandos e instrumentos del Thunderbird 2

[🏠 Inicio](../../../README.md) · [📦 Curso: Thunderbird 2](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puesto de mando de un transporte pesado modular realista se parece más a la
cabina de una gran aeronave de carga que a la de un vehículo ligero. Como el
peso cambia en cada misión, el piloto no solo conduce: vigila la carga, el
reparto de peso y el margen de empuje. Esa atención al peso es la gran
diferencia con conducir un vehículo vacío.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano derecha | Palanca de vuelo | Joystick 3 ejes | Guiar cabeceo, alabeo y rumbo | Alta | Responde más lento con carga pesada. |
| Mano izquierda | Acelerador principal | Palanca lineal | Regular empuje de los motores | Alta | El empuje debe superar el peso total. |
| Panel central | Gestión de carga | Botonera | Anclar y soltar el módulo | Alta | Requiere verificar los cierres. |
| Panel central | Reparto de peso | Selector | Ajustar donde apoya la carga | Media | Mantiene el centro de masa estable. |
| Panel derecho | Control de tren | Botones | Desplegar y recoger apoyos | Media | Dimensionado al peso máximo. |
| Panel izquierdo | Modo de vuelo | Selector | Elegir asistencia de la computadora | Media | Incluye límite de carga segura. |
| Consola | Instrumentos | Pantallas | Mostrar estado y carga | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Peso total | Masa del conjunto cargado | toneladas | Alta | Vehículo más estructura más módulo. |
| Margen de empuje | Empuje frente al peso | porcentaje | Alta | Si baja de cero, no despega. |
| Centro de masa | Posición del equilibrio | ejes | Alta | Debe quedar en la zona segura. |
| Estado de anclajes | Cierres del módulo | luces | Alta | Sin todos firmes no se mueve carga. |
| Nivel de combustible | Combustible restante | porcentaje | Alta | Es masa que también hay que mover. |
| Carga en cada apoyo | Peso por pata o rueda | toneladas | Media | Evita hundir o romper un apoyo. |

## Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Aumentar empuje | Flecha arriba | Gatillo derecho | Necesario para elevar más carga. |
| Cabecear | W y S | Stick derecho vertical | Más lento cuanto más peso. |
| Virar rumbo | A y D | Stick derecho horizontal | Requiere anticipación con carga. |
| Alabeo | Q y E | Botones laterales | Inclina el conjunto sobre su eje. |
| Anclar módulo | Tecla G | Botón X | Solo con el vehículo posado y alineado. |
| Soltar módulo | Tecla H | Botón Y | Verificar antes que el módulo apoye. |
| Desplegar tren | Barra espaciadora | Botón central | Antes de tocar el suelo cargado. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Vacío | Sin módulo, mínima masa | Peso total bajo | Volar ágil, ir a recoger carga. |
| Cargando | Anclando o soltando módulo | Anclajes en proceso | Alinear, cerrar, verificar. |
| Cargado | Módulo fijado y en marcha | Peso total alto | Volar con margen de empuje justo. |
| Emergencia | Sobrepeso o anclaje suelto | Alerta de carga | Soltar carga, estabilizar el centro. |

## Observaciones ergonomicas

- La interfaz debe mostrar a la vez el peso total y el margen de empuje, porque
  con carga el límite de despegue está muy cerca.
- El centro de masa es tan importante como el combustible: si se desvia, el
  vehículo se vuelve difícil de controlar.
- El estado de los anclajes debe ser evidente: mover carga mal fijada es
  peligroso.
- Conviene un modo de asistencia que avise antes de superar la carga segura.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-thunderbird-2.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-thunderbird-2.md)
