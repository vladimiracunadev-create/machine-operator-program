# 🧪 Principios y operacion de la grua portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grua portuaria](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formacion certificada del operador
ni el manual del fabricante. Describe como se opera una grua portico en
simulacion y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Estabilidad del portico**: la grua se apoya en dos rieles del muelle; su peso
  propio y su anclaje mantienen el equilibrio aunque la pluma se proyecte sobre el
  agua. El punto de vuelco es la linea del riel del lado de la carga.
- **Limites de carga**: el spreader y la grua tienen una carga maxima. El peso del
  contenedor mas el del spreader nunca debe superar ese limite.
- **Control del balanceo**: la carga cuelga como un pendulo; todo arranque o
  frenado brusco del trolley la hace bambolear. El anti-sway y los movimientos
  suaves mantienen la carga quieta.
- **Precision de posicionamiento**: el exito del ciclo depende de encajar el
  contenedor en su celda o sobre el camion sin golpear las guias.
- **Ciclo repetitivo**: la productividad se logra repitiendo un mismo ciclo de
  forma estable y segura, no con velocidad puntual.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Cables, spreader, twist-locks, anemometro, frenos. |
| Energizado | Poner la grua en servicio | Alimentacion conectada, instrumentos activos. |
| Posicionamiento | Alinear con la bahia | Gantry a la bodega, pluma en horizontal. |
| Enganche | Tomar el contenedor | Trolley sobre la celda, bajar spreader, trabar twist-locks. |
| Izaje y traslado | Mover la carga | Izar con anti-sway, trasladar el trolley al muelle. |
| Deposito | Dejar la carga | Bajar sobre camion o acopio, liberar twist-locks. |
| Cierre | Dejar segura | Pluma arriba, frenos de riel, grua asegurada. |

## Control del balanceo: idea general

1. Iniciar el movimiento del trolley de forma **suave**, sin tirones.
2. Mantener el **anti-sway** activo durante el traslado de la carga.
3. Anticipar el frenado para que el contenedor llegue quieto al punto de apoyo.
4. Bajar la carga con velocidad reducida en el tramo final.
5. Confirmar el asiento del contenedor antes de liberar los twist-locks.

## Errores comunes que la simulacion puede ensenar a evitar

- Arrancar o frenar el trolley de golpe y provocar balanceo de la carga.
- Izar sin confirmar que los twist-locks estan trabados.
- Operar con viento por sobre el limite del anemometro.
- Superar el limite de carga sumando el peso del spreader.
- Bajar el contenedor rapido y golpear las guias de la celda.
- Descuidar el area de exclusion y al personal en tierra.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: posicionar, izar, trasladar y depositar un contenedor.
- **Nivel 2 (simplificado)**: agregar balanceo de la carga, limite de carga y viento.
- **Nivel 3 (tecnico)**: sumar anti-sway, enclavamientos, precision de celda y
  ciclo cronometrado.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-grua-portuaria.md) · [➡️ Siguiente: Entornos de trabajo](entornos-grua-portuaria.md)
