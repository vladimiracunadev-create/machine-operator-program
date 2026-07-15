# 🧪 Principios y operación de la grúa portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formación certificada del operador
ni el manual del fabricante. Describe cómo se opera una grúa pórtico en
simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Estabilidad del pórtico**: la grúa se apoya en dos rieles del muelle; su peso
  propio y su anclaje mantienen el equilibrio aunque la pluma se proyecte sobre el
  agua. El punto de vuelco es la línea del riel del lado de la carga.
- **Límites de carga**: el spreader y la grúa tienen una carga máxima. El peso del
  contenedor más el del spreader nunca debe superar ese límite.
- **Control del balanceo**: la carga cuelga como un péndulo; todo arranque o
  frenado brusco del trolley la hace bambolear. El anti-sway y los movimientos
  suaves mantienen la carga quieta.
- **Precisión de posicionamiento**: el éxito del ciclo depende de encajar el
  contenedor en su celda o sobre el camión sin golpear las guías.
- **Ciclo repetitivo**: la productividad se logra repitiendo un mismo ciclo de
  forma estable y segura, no con velocidad puntual.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión básica | Cables, spreader, twist-locks, anemómetro, frenos. |
| Energizado | Poner la grúa en servicio | Alimentación conectada, instrumentos activos. |
| Posicionamiento | Alinear con la bahía | Gantry a la bodega, pluma en horizontal. |
| Enganche | Tomar el contenedor | Trolley sobre la celda, bajar spreader, trabar twist-locks. |
| Izaje y traslado | Mover la carga | Izar con anti-sway, trasladar el trolley al muelle. |
| Depósito | Dejar la carga | Bajar sobre camión o acopio, liberar twist-locks. |
| Cierre | Dejar segura | Pluma arriba, frenos de riel, grúa asegurada. |

## Control del balanceo: idea general

1. Iniciar el movimiento del trolley de forma **suave**, sin tirones.
2. Mantener el **anti-sway** activo durante el traslado de la carga.
3. Anticipar el frenado para que el contenedor llegue quieto al punto de apoyo.
4. Bajar la carga con velocidad reducida en el tramo final.
5. Confirmar el asiento del contenedor antes de liberar los twist-locks.

## Errores comunes que la simulación puede enseñar a evitar

- Arrancar o frenar el trolley de golpe y provocar balanceo de la carga.
- Izar sin confirmar que los twist-locks están trabados.
- Operar con viento por sobre el límite del anemómetro.
- Superar el límite de carga sumando el peso del spreader.
- Bajar el contenedor rápido y golpear las guías de la celda.
- Descuidar el área de exclusión y al personal en tierra.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: posicionar, izar, trasladar y depositar un contenedor.
- **Nivel 2 (simplificado)**: agregar balanceo de la carga, límite de carga y viento.
- **Nivel 3 (técnico)**: sumar anti-sway, enclavamientos, precisión de celda y
  ciclo cronometrado.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-grua-portuaria.md) · [➡️ Siguiente: Entornos de trabajo](entornos-grua-portuaria.md)
