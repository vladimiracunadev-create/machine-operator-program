# 🔧 Sistemas mecánicos del Nautilus

[🏠 Inicio](../../../README.md) · [🐙 Curso: Nautilus](../README.md) · 🔧 Sistemas mecánicos

> ⚖️ Material educativo original; el Nautilus de Julio Verne (1870) es de dominio público; otros derechos pertenecen a sus titulares.

Este módulo abre el Nautilus por dentro. Explica cada sistema imaginado por
Verne y lo compara con la física real del submarino moderno. La sorpresa es que
gran parte de lo que la novela describio coincide con la ingeniería que se
desarrollo después. Es la base técnica para entender los mandos (Módulo 4) y la
física de operación (Módulo 5).

```mermaid
flowchart LR
    subgraph Flotacion
        L[Tanques de lastre] --> B[Flotabilidad]
    end
    subgraph Estructura
        C[Casco resistente] --- P[Resiste presión]
    end
    subgraph Propulsion
        E[Energía eléctrica] --> H[Hélice]
    end
    subgraph Vida
        A[Renovación de aire]
    end
    B --> Navega[Navegación]
    H --> Navega
    P --> Navega
    A --> Navega
```

---

## 1. 🌊 Flotabilidad y tanques de lastre

El corazón de cualquier submarino es el control de la flotabilidad. Aquí Verne
acerto de lleno.

### Principio de Arquímedes

Todo cuerpo sumergido recibe un empuje hacia arriba igual al peso del agua que
desplaza. Si el peso de la nave es **menor** que ese empuje, sube; si es
**mayor**, baja; si son iguales, queda en equilibrio a media agua. Un submarino
no cambia su volumen, así que juega con su peso: para eso sirven los tanques de
lastre.

### Cómo funcionan los tanques

```mermaid
flowchart TD
    Emerger[Emerger] --> Vaciar[Expulsar agua con aire]
    Vaciar --> Ligero[La nave pesa menos]
    Ligero --> Sube[Empuje mayor que peso: sube]
    Sumergir[Sumergir] --> Llenar[Dejar entrar agua]
    Llenar --> Pesada[La nave pesa más]
    Pesada --> Baja[Peso mayor que empuje: baja]
```

- Para **sumergir**, se abren válvulas y el agua entra en los tanques: la nave
  gana peso y se hunde.
- Para **emerger**, se inyecta aire comprimido que expulsa el agua: la nave
  pierde peso y sube.
- Para navegar a **profundidad constante**, se busca la flotabilidad neutra y se
  ajusta con los timones de profundidad mientras la nave avanza.

### Ficción frente a realidad

| Tema | Lo que imagino Verne | Física e ingeniería real |
| --- | --- | --- |
| Sumergir y emerger | Llenar y vaciar depósitos de agua | Idéntico: tanques de lastre reales. |
| Flotabilidad neutra | Equilibrar peso y empuje a media agua | Concepto central del submarinismo. |
| Control fino | Ajuste de profundidad a voluntad | Se combina lastre y timones de buceo. |

---

## 2. 🛡️ Casco y presión en profundidad

### Por  qué aumenta la presión

Cada metro de agua sobre la nave añade peso encima. Por eso la presión crece de
forma continua con la profundidad: aproximadamente una atmósfera adicional cada
diez metros. A gran profundidad, el agua aprieta el casco con una fuerza
enorme desde todas direcciones.

### El casco resistente

Verne intuyo que la nave debía ser muy robusta para soportar esas
profundidades, e imagino un casco fuerte, de metal, capaz de resistir ese
abrazo del océano. La ingeniería real confirma la idea: los submarinos usan un
**casco de presión** de forma redondeada, casi cilíndrica o esférica, porque
esa geometría reparte la carga y evita puntos débiles.

| Tema | Lo que imagino Verne | Física e ingeniería real |
| --- | --- | --- |
| Presión con profundidad | La nave sufre más cuanto más baja | Sube cerca de 1 atmósfera cada 10 m. |
| Casco fuerte de metal | Estructura robusta contra el agua | Casco de presión de acero o titanio. |
| Forma de la nave | Cuerpo alargado y redondeado | Formas curvas reparten mejor la carga. |
| Límite de profundidad | Profundidades extremas alcanzables | Existe una profundidad de aplastamiento. |

Aquí aparece una diferencia importante: la novela sugiere profundidades muy
grandes con gran libertad, mientras que en la realidad cada casco tiene una
**profundidad límite** más allá de la cual la presión lo aplastaria.

---

## 3. ⚡ Energía

Verne fue especialmente visionario al elegir la **electricidad** como fuente de
energía, en una época dominada por el vapor y el carbón. En la novela, la nave
obtiene esa electricidad del propio mar, con ideas cercanas a las baterías que
usan sodio y otros elementos presentes en el agua salada.

| Tema | Lo que imagino Verne | Física e ingeniería real |
| --- | --- | --- |
| Energía eléctrica | Todo funciona con electricidad | Los submarinos modernos dependen de ella. |
| Energía del mar | Extraer energía del agua salada | Existen baterías y celdas basadas en sodio. |
| Sin repostar carbón | Autonomía sin puertos | Los reactores nucleares dan gran autonomía. |
| Motor limpio y silencioso | Propulsión sin humo | El motor eléctrico es silencioso y limpio. |

La intuición de fondo, una nave que no depende de quemar combustible en cada
viaje, se cumplio decadas después con la propulsión nuclear, aunque por un
camino técnico distinto al que describio la novela.

---

## 4. 🌀 Propulsión y navegación

- **Propulsión**: la energía eléctrica mueve una hélice en la popa que empuja
  la nave hacia adelante. Es exactamente el esquema de un submarino real de
  motor eléctrico.
- **Dirección horizontal**: un timón vertical, como el de un barco, hace girar
  la nave a babor o estribor.
- **Dirección vertical**: timones de profundidad, unas aletas horizontales, que
  inclinan la nave hacia arriba o hacia abajo mientras avanza.
- **Navegación**: instrumentos para conocer rumbo, velocidad y profundidad, más
  observación directa del entorno.

---

## 5. 💨 Soporte vital y renovación del aire

El límite real de vivir bajo el agua no es la presión, sino el **aire
respirable**. Las personas consumen oxígeno y producen dioxido de carbono, que
se vuelve tóxico si se acumula. Verne fue consciente de esto: en la novela la
nave sube periódicamente a renovar el aire y almacena reservas para permanecer
sumergida.

| Tema | Lo que imagino Verne | Física e ingeniería real |
| --- | --- | --- |
| Consumo de oxígeno | El aire se agota con el tiempo | Cierto: hay que reponer oxígeno. |
| Aire viciado | El dioxido de carbono es un peligro | Debe retirarse para poder respirar. |
| Reservas de aire | Guardar aire a presión a bordo | Se usan tanques y generadores de oxígeno. |
| Subir a ventilar | Renovar el aire en superficie | Los submarinos clásicos lo hacían así. |

---

## 🔁 Cómo se conecta todo

1. Los **tanques de lastre** deciden si la nave sube, baja o se queda.
2. El **casco resistente** permite bajar sin ser aplastado por la presión.
3. La **energía eléctrica** alimenta motores y sistemas de a bordo.
4. La **hélice y los timones** dan movimiento y rumbo.
5. El **soporte vital** mantiene el aire respirable y las reservas.

Con esto claro, el [Módulo 4: Mandos](../mandos/manual-mandos-nautilus.md)
muestra cómo la tripulación opera cada uno de estos sistemas.

---

[⬅️ Anterior: Características](caracteristicas-nautilus.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-nautilus.md)
