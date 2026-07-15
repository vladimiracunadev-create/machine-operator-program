# 🔧 Sistemas mecánicos del tractor

[🏠 Inicio](../../../README.md) · [🚜 Curso: Tractores](../README.md) · 🔧 Sistemas mecánicos

Este módulo abre el tractor por dentro y es el corazón del curso. Explica cada
sistema, como funciona y cómo se conecta con los demás, con foco en la toma de
fuerza, el enganche de tres puntos, la hidráulica y la estabilidad. Es la base
técnica para entender los mandos (Módulo 5) y la física del trabajo (Módulo 6).

```mermaid
flowchart LR
    subgraph Motriz
        M[Motor diesel] --> Em[Embrague] --> Cx[Caja de cambios] --> Di[Diferencial] --> Rt[Ruedas traseras]
    end
    subgraph Trabajo
        PTO[Toma de fuerza PTO] --> Ap[Apero accionado]
        Bo[Bomba hidráulica] --> Vl[Válvulas] --> Tp[Enganche tres puntos]
    end
    subgraph Estabilidad
        La[Lastre] --- Cg[Centro de gravedad]
    end
    M --> PTO
    M --> Bo
```

---

## 1. ⚙️ Motor diesel

El tractor usa un **motor diesel** por su alto par a bajas vueltas y su bajo
consumo, ideal para tirar de aperos durante horas. A diferencia de un automóvil,
el tractor trabaja largos periodos a régimen constante, moviendo la PTO o
traccionando bajo carga.

```mermaid
flowchart LR
    A[1. Admisión, entra aire] --> B[2. Compresión, sube presión y calor]
    B --> C[3. Inyección y combustión, empuje]
    C --> D[4. Escape, salen gases]
    D --> A
```

| Parámetro | Efecto en el tractor |
| --- | --- |
| Par (torque) | Fuerza de tiro y de arrastre de aperos pesados. |
| Potencia (kW/CV) | Capacidad de mantener el trabajo bajo carga. |
| Régimen de PTO | Vueltas del motor que dan las 540 o 1000 rpm de la PTO. |
| Consumo | Determina la autonomía en una jornada de campo. |

Sistemas de apoyo: inyección diesel, refrigeración por líquido, filtrado
reforzado de aire (mucho polvo en el campo) y, en modelos modernos,
postratamiento de gases.

---

## 2. 🔩 Toma de fuerza (PTO)

La **toma de fuerza** o Power Take-Off es un eje estriado que sale del tractor y
transmite la potencia del motor directamente al apero: una segadora, una bomba,
un remolque esparcidor. Es lo que diferencia al tractor de un simple vehículo de
tiro.

```mermaid
flowchart LR
    Motor[Motor] --> EmbraguePTO[Embrague de PTO]
    EmbraguePTO --> EjePTO[Eje estriado PTO]
    EjePTO --> Cardan[Cardan del apero]
    Cardan --> Apero[Apero accionado]
    Protector[Protector del eje] -. cubre .-> Cardan
```

| Concepto | Descripción |
| --- | --- |
| Régimen normalizado | 540 rpm o 1000 rpm según el apero. |
| Embrague de PTO | Conecta y desconecta el eje sin detener el tractor. |
| Cardan con junta | Transmite el giro al apero permitiendo movimiento. |
| Protector | Cubierta que evita el atrapamiento; nunca debe faltar. |

Seguridad crítica: el eje de la PTO gira a gran velocidad y ha causado accidentes
graves por atrapamiento de ropa. El protector debe estar siempre colocado y el
operador nunca debe acercarse con la PTO en marcha.

---

## 3. 🔺 Enganche de tres puntos e hidráulica

El **enganche de tres puntos** es un triángulo formado por dos brazos inferiores
y un brazo superior (tercer punto) que sujeta el apero montado. La hidráulica
sube y baja ese enganche, controlando la profundidad de trabajo.

```mermaid
flowchart TD
    Tanque[Depósito de aceite] --> Bomba[Bomba hidráulica]
    Motor[Motor] --> Bomba
    Bomba --> Valvulas[Válvulas de control]
    Valvulas --> Cilindro[Cilindro de elevación]
    Cilindro --> Brazos[Brazos inferiores]
    Brazos --> Apero[Apero montado]
    Superior[Tercer punto superior] --> Apero
    Valvulas --> Externa[Salidas hidráulicas externas]
```

| Elemento | Función |
| --- | --- |
| Brazos inferiores | Sostienen el apero y transmiten el tiro. |
| Tercer punto | Fija el ángulo del apero y su inclinación. |
| Cilindro hidráulico | Sube y baja el enganche para regular la profundidad. |
| Control de esfuerzo | Ajusta la altura según la resistencia del suelo. |
| Salidas externas | Alimentan cilindros de aperos remolcados. |

- **Transferencia de peso**: al levantar un apero de tiro, parte de su peso se
  traslada a las ruedas traseras del tractor y mejora el agarre.
- **Control de posición**: mantiene el apero a una altura fija.
- **Control de esfuerzo**: sube el apero cuando la resistencia del suelo aumenta,
  evitando que el motor se ahogue y regulando la tracción.

---

## 4. 🔗 Transmisión y tracción

La transmisión adapta el par del motor a la velocidad de trabajo, que suele ser
muy baja (labranza) o moderada (transporte). El agarre depende de las ruedas y
del reparto de peso.

| Elemento | Función | Nota |
| --- | --- | --- |
| Caja de cambios | Muchas relaciones para cada labor. | A veces con gamas y superreductora. |
| Diferencial | Reparte giro entre ruedas en curva. | Permite girar sin arrastrar. |
| Bloqueo de diferencial | Iguala el giro de ambas ruedas. | Para salir del barro o patinaje. |
| Doble tracción (4x4) | Tracciona también el eje delantero. | Más agarre en suelo blando o pendiente. |
| Ruedas traseras grandes | Aumentan el área de contacto y el agarre. | Se lastran con agua o pesos. |

- **Patinaje**: si las ruedas giran más que el avance, se pierde tracción. Un
  poco de patinaje es normal; demasiado desperdicia potencia y dana el suelo.
- **Neumáticos de barra (tacos)**: el dibujo profundo agarra la tierra blanda.

---

## 5. ⚖️ Lastre y estabilidad en pendiente

El tractor tiene un centro de gravedad relativamente alto y una vía estrecha, lo
que lo hace **sensible al vuelco**, sobre todo lateral en pendiente. El lastre y
la conducción prudente son la defensa principal.

```mermaid
flowchart LR
    Lastre[Lastre delantero y en ruedas] --> Agarre[Más agarre y equilibrio]
    Pendiente[Pendiente lateral] --> Riesgo[Riesgo de vuelco lateral]
    Agarre --> Estable[Operación estable]
    Riesgo --> Prudencia[Bajar velocidad y evitar giros bruscos]
    Prudencia --> Estable
```

| Concepto | Descripción |
| --- | --- |
| Lastre delantero | Contrapesos que equilibran un apero trasero pesado. |
| Lastre en ruedas | Agua o pesos que bajan el centro de gravedad y dan agarre. |
| Vía | Ancho entre ruedas; más ancha, más estable. |
| Centro de gravedad | Cuanto más bajo, menor riesgo de vuelco. |
| Estructura antivuelco (ROPS) | Arco o cabina que protege si el tractor vuelca. |
| Cinturón | Mantiene al operador dentro de la zona protegida por el ROPS. |

Reglas básicas de estabilidad:

- Subir y bajar pendientes **en línea recta**, no en diagonal.
- Evitar giros bruscos y frenadas de una sola rueda en pendiente.
- No enganchar cargas de tiro por encima del eje trasero: eso favorece el vuelco
  hacia atrás. El tiro siempre desde la barra de tiro baja.
- Usar siempre el ROPS y el cinturón.

---

## 6. 🛠️ Aperos

Los aperos son los implementos que el tractor arrastra o acciona. Definen la
labor y cómo se transmite la fuerza.

| Apero | Como recibe la fuerza | Labor |
| --- | --- | --- |
| Arado / rastra | Por tiro desde el enganche | Preparar el suelo. |
| Sembradora | Tiro + PTO o hidráulica | Depositar semilla. |
| Segadora / rotativa | Por la PTO | Cortar forraje o maleza. |
| Esparcidor | Por la PTO | Distribuir abono o semilla. |
| Pala cargadora frontal | Por la hidráulica | Cargar y mover material. |
| Remolque | Por tiro desde la barra | Transportar carga. |

---

## 🔁 Cómo se conecta todo

1. El **motor diesel** entrega mucho par a bajas vueltas.
2. La **caja** y el **diferencial** llevan la tracción a las ruedas grandes.
3. La **toma de fuerza** transmite potencia directa a los aperos accionados.
4. La **bomba hidráulica** alimenta el enganche de tres puntos y las salidas externas.
5. El **enganche** sube, baja y controla la profundidad del apero montado.
6. El **lastre** y la conducción prudente mantienen la estabilidad en pendiente.

Con esto entendido, el [Módulo 5: Mandos](../mandos/manual-mandos-tractor.md)
muestra como el operador acciona cada uno de estos sistemas.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-tractor.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-tractor.md)
