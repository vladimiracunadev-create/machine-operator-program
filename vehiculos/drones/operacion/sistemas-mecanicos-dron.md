# 🔧 Sistemas mecánicos del dron

[🏠 Inicio](../../../README.md) · [🕹️ Curso: Drones](../README.md) · 🔧 Sistemas mecánicos

Este módulo abre el dron por dentro. Explica cada sistema, como funciona y como
se conecta con los demás. Es la base técnica para entender los mandos (Módulo 4)
y la física del vuelo (Módulo 5). El foco es el multirotor, el tipo más común.

```mermaid
flowchart LR
    subgraph Energia
        Bat[Batería LiPo] --> PDB[Distribución de energía]
    end
    subgraph Propulsion
        ESC[Controladores ESC] --> Mot[Motores brushless]
        Mot --> Hel[Hélices]
    end
    subgraph Cerebro
        FC[Controladora de vuelo]
        IMU[IMU]
        GPS[GPS]
    end
    subgraph Enlace
        RX[Receptor]
        Tel[Telemetría]
    end
    PDB --> ESC
    PDB --> FC
    FC --> ESC
    IMU --> FC
    GPS --> FC
    RX --> FC
    FC --> Tel
    Hel --> Empuje[Sustentación y empuje]
```

---

## 1. ⚙️ Motores brushless y ESC

El multirotor se mueve variando la velocidad de giro de cada rotor. Los motores
son **brushless** (sin escobillas): giran gracias a un campo magnético controlado
electronicamente, sin contacto que se desgaste, lo que les da alta eficiencia y
respuesta rápida.

Cada motor necesita un **ESC** (controlador electrónico de velocidad). El ESC
recibe una orden de la controladora y entrega a su motor la corriente justa para
girar al régimen pedido. En un cuadricoptero hay cuatro motores y cuatro ESC.

```mermaid
flowchart LR
    FC[Controladora de vuelo] --> ESC1[ESC 1]
    FC --> ESC2[ESC 2]
    FC --> ESC3[ESC 3]
    FC --> ESC4[ESC 4]
    ESC1 --> M1[Motor 1]
    ESC2 --> M2[Motor 2]
    ESC3 --> M3[Motor 3]
    ESC4 --> M4[Motor 4]
```

| Componente | Función | Parámetro clave |
| --- | --- | --- |
| Motor brushless | Transforma energía eléctrica en giro. | KV: rpm por voltio aplicado. |
| ESC | Regula la corriente de cada motor. | Amperaje máximo que soporta. |
| Distribución de energía | Reparte la batería a los ESC. | Corriente total del conjunto. |

---

## 2. 🌀 Hélices y empuje

Cada motor mueve una **hélice** de paso fijo que, al girar, empuja aire hacia
abajo y genera empuje hacia arriba. La suma de los cuatro empujes sostiene el
dron. Para mantener el equilibrio, las hélices giran en sentidos alternos: dos en
sentido horario y dos en sentido antihorario, de modo que sus pares se cancelan.

| Concepto | Descripción |
| --- | --- |
| Empuje | Fuerza vertical que genera cada hélice al girar. |
| Paso | Ángulo de la pala; en multirotor es fijo, el control es por rpm. |
| Sentido de giro | Alternado para cancelar el par y no girar sobre si mismo. |
| Diámetro | Hélice mayor mueve más aire; motor y ESC deben acompañar. |

---

## 3. 🎚️ Control por variación de rpm

El multirotor no tiene superficies móviles: **todo el control nace de variar la
velocidad de cada rotor**. La controladora sube o baja el empuje de rotores
concretos para inclinar o girar el aparato.

```mermaid
flowchart TD
    Orden[Orden del piloto] --> FC[Controladora]
    FC --> Sube[Sube rpm de unos rotores]
    FC --> Baja[Baja rpm de otros rotores]
    Sube --> Dif[Diferencia de empuje]
    Baja --> Dif
    Dif --> Mov[Cabeceo, alabeo o guiñada]
```

| Movimiento | Que hace | Como se logra por rpm |
| --- | --- | --- |
| Ascenso / descenso | Sube o baja en vertical. | Sube o baja el rpm de los cuatro rotores por igual. |
| Cabeceo (pitch) | Inclina adelante o atrás para avanzar. | Más empuje atrás y menos adelante, o al revés. |
| Alabeo (roll) | Inclina a un lado para desplazarse. | Más empuje de un lado y menos del otro. |
| Guiñada (yaw) | Gira la nariz a izquierda o derecha. | Desequilibra el par: más rpm a los rotores de un sentido de giro. |

La guiñada se logra aprovechando que unas hélices giran horario y otras
antihorario: al acelerar el par de rotores que giran en un sentido y frenar los
del otro, aparece un par neto que rota el dron sobre su eje vertical.

---

## 4. 🔋 Batería LiPo y autonomía

La energía viene de una **batería de polimero de litio (LiPo)**, elegida por su
alta densidad de energía y su capacidad de entregar mucha corriente. Define,
junto con el peso, cuantos minutos vuela el dron.

| Parámetro | Significado | Efecto |
| --- | --- | --- |
| Capacidad | Energía almacenada, en mAh. | Más capacidad, más autonomía y más peso. |
| Celdas | Número de celdas en serie, notado S. | Fija el voltaje; 4S es típico en consumo. |
| Tasa de descarga | Corriente máxima, notada C. | Debe cubrir el pico de los motores. |
| Autonomía | Minutos de vuelo útiles. | Suele estar entre 10 y 40 minutos. |

Volar por debajo de un voltaje mínimo dana la LiPo; por eso la controladora vigila
la carga y activa avisos o el retorno automático cuando queda poca energía.

---

## 5. 🧠 Controladora de vuelo, IMU y GPS

La **controladora de vuelo** es el cerebro del dron. Lee sus sensores muchas veces
por segundo y ajusta el rpm de cada motor para mantener la actitud que pide el
piloto.

| Sensor | Que mide | Para que sirve |
| --- | --- | --- |
| IMU | Aceleraciones y giros en los tres ejes. | Conocer la actitud y estabilizar. |
| Giróscopo | Velocidad de rotación. | Corregir cabeceo, alabeo y guiñada. |
| Acelerómetro | Aceleración y dirección de la gravedad. | Saber que es "arriba". |
| Barómetro | Presión del aire. | Estimar y mantener la altura. |
| GPS | Posición y velocidad sobre el terreno. | Mantener el punto y navegar por waypoints. |
| Brújula | Rumbo magnético. | Orientar la navegación y el retorno. |

La **IMU** combina giróscopo y acelerómetro y es imprescindible incluso para el
vuelo más básico. El **GPS** no es obligatorio para volar, pero habilita el vuelo
estacionario preciso, la navegación automática y el retorno a casa.

---

## 6. 📡 Enlace de radio y telemetría

El dron se comunica con tierra por radio. Hay dos flujos:

```mermaid
flowchart LR
    Radio[Radiocontrol] -->|ordenes| RX[Receptor a bordo]
    RX --> FC[Controladora]
    FC -->|telemetría| TX[Emisor a bordo]
    TX --> Estacion[Estación de tierra]
    Cam[Cámara] -->|video| Estacion
```

- **Enlace de mando**: del radiocontrol al receptor; lleva las ordenes del piloto.
- **Telemetría**: del dron a la estación; informa batería, altura, posición y modo.
- **Enlace de video**: transmite la imagen de la cámara en tiempo casi real.

| Enlace | Dirección | Contenido |
| --- | --- | --- |
| Mando | Tierra a dron | Ordenes de los sticks y de los modos. |
| Telemetría | Dron a tierra | Estado del vuelo y de los sistemas. |
| Video | Dron a tierra | Imagen de la cámara para el piloto. |

Si el enlace de mando se pierde, la controladora activa un **fail-safe** para no
quedar sin control (ver sección 8).

---

## 7. 📷 Cámara y gimbal

Muchos drones llevan una **cámara** montada en un **gimbal**: un soporte con
motores que compensa los movimientos del dron para que la imagen salga estable.

| Elemento | Función |
| --- | --- |
| Cámara | Captura foto y video; también sirve para pilotar en vista FPV. |
| Gimbal | Estabiliza la cámara compensando cabeceo, alabeo y guiñada. |
| Sensores extra | Cámaras multiespectrales o térmicas para agricultura e inspección. |

El gimbal separa el movimiento del dron del de la cámara: aunque el dron corrija
su actitud, la imagen se mantiene nivelada.

---

## 8. 🛟 Fail-safe y retorno a casa

El dron incluye protecciones automáticas para reaccionar ante fallos sin que el
piloto tenga que resolver todo a mano.

| Protección | Cuando actua | Que hace |
| --- | --- | --- |
| Return to home | Pérdida de enlace o poca batería. | Vuelve al punto de despegue y aterriza. |
| Aviso de batería baja | Voltaje o carga por debajo del umbral. | Alerta y, si sigue bajando, fuerza el retorno. |
| Fail-safe de enlace | Se pierde la señal de mando. | Mantiene posición o inicia el retorno. |
| Límite geográfico | Zona restringida o distancia máxima. | Frena o impide entrar a la zona. |

El **retorno a casa (RTH)** depende del GPS: guarda el punto de despegue como
"casa" y, al activarse, sube a una altura segura, vuela hasta ese punto y baja.

---

## 🔁 Cómo se conecta todo

1. La **batería LiPo** alimenta los ESC y la controladora.
2. La **controladora** lee la **IMU** y el **GPS** y decide el rpm de cada motor.
3. Los **ESC** ajustan los **motores brushless** y sus **hélices**.
4. La **diferencia de empuje** entre rotores produce cabeceo, alabeo y guiñada.
5. El **enlace de radio** trae las ordenes y devuelve la **telemetría** y el video.
6. El **fail-safe** protege el vuelo si falla el enlace o baja la batería.

Con esto entendido, el [Módulo 4: Mandos](../mandos/manual-mandos-dron.md) muestra
como el piloto opera cada uno de estos sistemas.

---

[⬅️ Anterior: Características](caracteristicas-dron.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-dron.md)
