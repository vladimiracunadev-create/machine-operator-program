# 🔧 Sistemas mecánicos de la grúa portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · 🔧 Sistemas mecánicos

Este módulo abre la grúa pórtico por dentro y es el corazón del curso. Explica
como se sostiene la estructura sobre los rieles del muelle, como el trolley lleva
el spreader hasta el contenedor y cómo se mueve cada eje del izaje. Es la base
técnica para entender los mandos (Módulo 5) y los principios de operación
(Módulo 6).

```mermaid
flowchart LR
    subgraph Estructura
        Ri[Rieles del muelle] --- Pa[Patas del pórtico]
        Pa --- Vi[Viga principal]
        Vi --- Bo[Pluma boom]
    end
    subgraph Movimiento
        Ga[Gantry sobre rieles]
        Tr[Trolley carro]
    end
    subgraph Izaje
        Ho[Cabrestante de izaje] --- Sp[Spreader]
        Sp --- Cn[Contenedor]
    end
    Vi --> Tr
    Tr --> Ho
    Ri --> Ga
    AS[Anti-sway] -. estabiliza .-> Sp
    LMS[Límites y enclavamientos] -. vigila .-> Ho
```

---

## 1. 🏗️ Estructura del pórtico

El pórtico ship-to-shore es una gran estructura de acero con forma de marco. Se
apoya sobre patas que descansan en bogies con ruedas sobre los rieles del muelle,
y una viga horizontal en altura que cruza desde tierra hasta sobre el agua. Sobre
esa viga corre el trolley.

| Elemento | Función |
| --- | --- |
| Patas y bogies | Sostienen el pórtico y ruedan sobre los rieles del muelle. |
| Viga principal | Camino horizontal por donde corre el trolley. |
| Pluma boom | Prolongación de la viga que se proyecta sobre el buque. |
| Pórtico trasero | Lado de tierra, sobre el muelle y los camiones. |
| Tirantes y torre | Sostienen la viga y la pluma desde arriba. |

La pluma se abate: se levanta a posición vertical cuando la grúa no opera o para
dejar pasar el buque, y se baja a horizontal para trabajar sobre las bodegas. Al
apoyarse en dos rieles paralelos, el punto de vuelco de la grúa es la línea del
riel del lado de la carga; el peso propio de la estructura y su anclaje mantienen
el equilibrio sobre el agua.

---

## 2. 🛤️ Traslación sobre rieles: gantry, trolley y boom

La grúa tiene tres traslaciones principales, cada una en un eje distinto. Es útil
distinguirlas porque los mandos (Módulo 5) las controlan por separado.

```mermaid
flowchart TD
    Gantry[Gantry: pórtico sobre rieles] -->|posiciona frente a la bodega| Buque[Bahía del buque]
    Trolley[Trolley: carro sobre la viga] -->|acerca o aleja del agua| Punto[Punto de izaje]
    Boom[Boom: pluma abatible] -->|libera o cubre el buque| Vano[Vano sobre el buque]
    Hoist[Hoist: izaje vertical] -->|sube y baja| Spreader[Spreader]
```

| Traslación | Eje | Que mueve | Cuando se usa |
| --- | --- | --- | --- |
| Gantry | A lo largo del muelle | Todo el pórtico sobre los rieles | Para alinear la grúa con otra bahía del buque. |
| Trolley | Perpendicular al muelle | El carro sobre la viga | Para acercar o alejar la carga del agua. |
| Boom | Vertical, abatible | La pluma sobre el buque | Para liberar el gabarito del buque al maniobrar. |
| Hoist | Vertical | El spreader y la carga | Para subir y bajar el contenedor. |

- **Gantry (traslación del pórtico)**: motores en los bogies mueven la grúa
  completa por los rieles, con velocidad baja y frenos de riel para fijarla.
- **Trolley (traslación del carro)**: el carro corre por la viga llevando el
  spreader entre el buque y el muelle; define el alcance horizontal del izaje.
- **Boom (abatimiento de la pluma)**: cabrestantes o cilindros levantan la pluma
  a vertical para el paso del buque y la bajan a horizontal para operar.

---

## 3. 🚋 Trolley y spreader

El trolley es el carro que corre por la viga; suele llevar la cabina del operador
mirando hacia abajo. Del trolley cuelga el spreader mediante el cable de izaje.

```mermaid
flowchart TD
    Carro[Trolley carro] --> Cables[Cables de izaje]
    Cables --> Spreader[Spreader telescópico]
    Spreader --> Twist[Twist-locks en 4 esquinas]
    Twist --> Contenedor[Contenedor ISO]
    Carro -. lleva .-> Cabina[Cabina del operador]
```

- **Spreader telescópico**: marco que se extiende o recoge para ajustarse a 20,
  40 o 45 pies de contenedor.
- **Twist-locks**: cuatro pernos giratorios que entran en las esquinas del
  contenedor y giran para trabar o liberar la carga.
- **Flippers / guías**: patas guía en las esquinas del spreader que centran la
  caja al descender.
- **Cabina en el trolley**: el operador viaja con el carro y mira hacia abajo el
  punto de izaje, lo que da visión directa sobre el contenedor.

| Parámetro del spreader | Que es | Efecto |
| --- | --- | --- |
| Longitud | Extensión telescópica en pies | Debe coincidir con el contenedor a tomar. |
| Peso propio | Masa del spreader | Se suma a la carga que ve el izaje. |
| Estado de twist-locks | Trabado o liberado | Habilita o impide el izaje seguro. |
| Sensores de asiento | Confirman apoyo en las 4 esquinas | Evitan izar mal calzado. |

---

## 4. ⚙️ Cabrestantes: hoist, trolley y gantry

Los movimientos se accionan con cabrestantes y motores eléctricos. El de izaje
(hoist) sube y baja el spreader; el de traslación del carro (trolley) lo desplaza
por la viga; el de traslación del pórtico (gantry) mueve la grúa por los rieles.

| Cabrestante / accionamiento | Que mueve | Dirección | Nota |
| --- | --- | --- | --- |
| Hoist de izaje | Spreader y contenedor | Vertical | Enrolla los cables desde el trolley. |
| Traslación del trolley | Carro sobre la viga | Horizontal, hacia el agua | Define el alcance del izaje. |
| Traslación del gantry | Pórtico sobre rieles | A lo largo del muelle | Reposiciona toda la grúa. |
| Abatimiento de boom | Pluma | Vertical, abatible | Levanta o baja la pluma. |

El izaje usa varios ramales de cable que pasan por poleas entre el trolley y el
spreader, repartiendo el peso del contenedor. La velocidad de cada motor la regula
el operador con los joysticks, de forma proporcional al desplazamiento del mando.

---

## 5. 📦 Contenedores, celdas y apilado

La carga que maneja la grúa está normalizada, lo que permite un ciclo repetitivo.
Conocer sus dimensiones y cómo se apila ayuda a entender el posicionamiento.

| Concepto | Descripción |
| --- | --- |
| TEU | Contenedor de 20 pies; unidad de medida del tráfico. |
| FEU | Contenedor de 40 pies; equivale a 2 TEU. |
| Esquinas ISO | Cuatro cajas de esquina normalizadas donde engancha el spreader. |
| Celdas del buque | Guías verticales en las bodegas que alinean el apilado. |
| Alturas de apilado | Los contenedores se apilan varios niveles en bodega y cubierta. |
| Bloque de patio | Agrupación de contenedores apilados en el terminal. |

El buque portacontenedores tiene celdas guía que reciben la caja y la centran al
bajar; en cubierta los contenedores se aseguran con twist-locks y barras. El
operador debe posicionar el spreader con precisión para que la caja entre en su
celda sin golpear las guías.

---

## 6. ⚡ Accionamiento eléctrico y anti-sway

La grúa STS moderna es eléctrica: recibe energía desde el muelle por un carrete de
cable o una barra colectora y alimenta los motores de cada movimiento. No lleva
combustible a bordo.

```mermaid
flowchart LR
    Red[Red del muelle] --> Cable[Carrete de cable]
    Cable --> Tablero[Tablero de potencia]
    Tablero --> MHoist[Motor de izaje]
    Tablero --> MTrolley[Motor del trolley]
    Tablero --> MGantry[Motores del gantry]
    Tablero --> MBoom[Motor de la pluma]
    AntiSway[Anti-sway] -. corrige .-> MTrolley
    AntiSway -. corrige .-> MHoist
```

| Componente | Función |
| --- | --- |
| Alimentación del muelle | Entrega energía eléctrica a la grúa sin combustible a bordo. |
| Carrete de cable | Enrolla el cable de energía mientras la grúa se traslada. |
| Tablero de potencia | Distribuye energía a cada motor de movimiento. |
| Variadores | Regulan velocidad y par de los motores eléctricos. |
| Sistema anti-sway | Ajusta el trolley y el izaje para frenar el balanceo de la carga. |

El **anti-sway** (anti-balanceo) mide u anticipa el bamboleo del contenedor
colgado y corrige los movimientos del trolley y del izaje para que la carga
llegue quieta al punto de apoyo. Reduce el tiempo de posicionamiento y evita
golpes contra el buque o las guías.

---

## 7. 🔒 Enclavamientos, límites de carga y seguridad

La grúa incorpora enclavamientos y límites que impiden maniobras inseguras. Son
la base del modelo de seguridad que la simulación debe representar.

| Dispositivo | Que hace |
| --- | --- |
| Límite de carga | Impide izar por encima de la capacidad del spreader y de la grúa. |
| Fin de carrera de izaje | Detiene el spreader antes del tope superior o del suelo. |
| Fin de carrera de trolley | Frena el carro en los extremos de la viga. |
| Sensor de twist-locks | Solo habilita el izaje con la carga trabada. |
| Anemómetro y límite de viento | Detiene la operación si el viento supera el límite. |
| Frenos de riel y anclaje | Fijan la grúa contra el desplazamiento por viento. |
| Parada de emergencia | Corta todos los movimientos de inmediato. |

Además de proteger la máquina, estos límites protegen al personal en tierra: la
grúa no debe izar sin la carga bien trabada, ni mover el contenedor si el viento
excede el umbral operacional.

---

## 🔁 Ciclo de descarga buque a muelle

El trabajo de la grúa es un ciclo repetitivo. Un ciclo típico de descarga sigue
estos pasos:

1. El **gantry** posiciona la grúa frente a la bahía del buque a descargar.
2. El **trolley** lleva el spreader sobre la celda del contenedor objetivo.
3. El **hoist** baja el spreader y los **twist-locks** traban el contenedor.
4. El hoist iza el contenedor fuera de la celda, con **anti-sway** activo.
5. El trolley traslada la carga desde el buque hacia el muelle.
6. El hoist baja el contenedor sobre el camión o la zona de acopio.
7. Los twist-locks liberan la caja y el spreader sube vacío.
8. La grúa repite el ciclo con el siguiente contenedor.

Con esto entendido, el [Módulo 5: Mandos](../mandos/manual-mandos-grua-portuaria.md)
muestra como el operador acciona cada uno de estos sistemas.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-grua-portuaria.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-grua-portuaria.md)
