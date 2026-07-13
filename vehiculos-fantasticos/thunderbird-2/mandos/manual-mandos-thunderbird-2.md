# 🎛️ Mandos e instrumentos del Thunderbird 2

[🏠 Inicio](../../../README.md) · [📦 Curso: Thunderbird 2](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puesto de mando de un transporte pesado modular realista se parece mas a la
cabina de una gran aeronave de carga que a la de un vehiculo ligero. Como el
peso cambia en cada mision, el piloto no solo conduce: vigila la carga, el
reparto de peso y el margen de empuje. Esa atencion al peso es la gran
diferencia con conducir un vehiculo vacio.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano derecha | Palanca de vuelo | Joystick 3 ejes | Guiar cabeceo, alabeo y rumbo | Alta | Responde mas lento con carga pesada. |
| Mano izquierda | Acelerador principal | Palanca lineal | Regular empuje de los motores | Alta | El empuje debe superar el peso total. |
| Panel central | Gestion de carga | Botonera | Anclar y soltar el modulo | Alta | Requiere verificar los cierres. |
| Panel central | Reparto de peso | Selector | Ajustar donde apoya la carga | Media | Mantiene el centro de masa estable. |
| Panel derecho | Control de tren | Botones | Desplegar y recoger apoyos | Media | Dimensionado al peso maximo. |
| Panel izquierdo | Modo de vuelo | Selector | Elegir asistencia de la computadora | Media | Incluye limite de carga segura. |
| Consola | Instrumentos | Pantallas | Mostrar estado y carga | Alta | Ver seccion de instrumentos. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Peso total | Masa del conjunto cargado | toneladas | Alta | Vehiculo mas estructura mas modulo. |
| Margen de empuje | Empuje frente al peso | porcentaje | Alta | Si baja de cero, no despega. |
| Centro de masa | Posicion del equilibrio | ejes | Alta | Debe quedar en la zona segura. |
| Estado de anclajes | Cierres del modulo | luces | Alta | Sin todos firmes no se mueve carga. |
| Nivel de combustible | Combustible restante | porcentaje | Alta | Es masa que tambien hay que mover. |
| Carga en cada apoyo | Peso por pata o rueda | toneladas | Media | Evita hundir o romper un apoyo. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Aumentar empuje | Flecha arriba | Gatillo derecho | Necesario para elevar mas carga. |
| Cabecear | W y S | Stick derecho vertical | Mas lento cuanto mas peso. |
| Virar rumbo | A y D | Stick derecho horizontal | Requiere anticipacion con carga. |
| Alabeo | Q y E | Botones laterales | Inclina el conjunto sobre su eje. |
| Anclar modulo | Tecla G | Boton X | Solo con el vehiculo posado y alineado. |
| Soltar modulo | Tecla H | Boton Y | Verificar antes que el modulo apoye. |
| Desplegar tren | Barra espaciadora | Boton central | Antes de tocar el suelo cargado. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| Vacio | Sin modulo, minima masa | Peso total bajo | Volar agil, ir a recoger carga. |
| Cargando | Anclando o soltando modulo | Anclajes en proceso | Alinear, cerrar, verificar. |
| Cargado | Modulo fijado y en marcha | Peso total alto | Volar con margen de empuje justo. |
| Emergencia | Sobrepeso o anclaje suelto | Alerta de carga | Soltar carga, estabilizar el centro. |

## Observaciones ergonomicas

- La interfaz debe mostrar a la vez el peso total y el margen de empuje, porque
  con carga el limite de despegue esta muy cerca.
- El centro de masa es tan importante como el combustible: si se desvia, el
  vehiculo se vuelve dificil de controlar.
- El estado de los anclajes debe ser evidente: mover carga mal fijada es
  peligroso.
- Conviene un modo de asistencia que avise antes de superar la carga segura.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-thunderbird-2.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-thunderbird-2.md)
