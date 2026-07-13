# 🔧 Sistemas mecanicos del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🔧 Sistemas mecanicos

Este modulo abre el transbordador por dentro. Explica cada sistema, como funciona
y como se conecta con los demas. Es la base tecnica para entender los mandos
(Modulo 4) y la fisica del planeo (Modulo 5). Todo es **ciencia real**.

```mermaid
flowchart LR
    subgraph Despegue
        Tanque[Tanque externo] --> Motores[Motores del orbitador]
        Propulsores[Propulsores laterales] --> EmpujeD[Empuje de despegue]
        Motores --> EmpujeD
    end
    subgraph Orbitador
        Cabina[Cabina]
        Bahia[Bahia de carga]
        RCS[Propulsores RCS]
    end
    subgraph Reentrada
        Escudo[Escudo termico]
        Alas[Alas y timones]
    end
    EmpujeD --> Orbita[Orbita]
    Orbita --> Escudo
    Escudo --> Alas
```

---

## 1. 🚀 Grupo de despegue

El transbordador sube gracias a tres sistemas que trabajan juntos al despegar.

```mermaid
flowchart LR
    Propulsores[Propulsores laterales] --> Sube[Empuje inicial fuerte]
    Tanque[Tanque externo] --> Motores[Motores del orbitador]
    Motores --> Sube
    Sube --> Separa1[Se separan los propulsores]
    Separa1 --> Separa2[Se suelta el tanque externo]
    Separa2 --> Orbita[Orbitador en orbita]
```

| Componente | Funcion |
| --- | --- |
| Propulsores laterales | Dan gran empuje en los primeros minutos, luego se separan. |
| Tanque externo | Guarda el propelente que usan los motores del orbitador. |
| Motores del orbitador | Queman el propelente del tanque durante el ascenso. |
| Sistema de separacion | Suelta primero los propulsores y luego el tanque. |

---

## 2. 🛰️ Orbitador

Es la nave alada que lleva a la tripulacion y la carga, y la unica parte que
regresa entera.

| Subsistema | Funcion |
| --- | --- |
| Cabina | Puesto de la tripulacion, presurizado. |
| Bahia de carga | Espacio con puertas para desplegar cargas. |
| Brazo robotico | Manipula satelites y modulos en orbita. |
| Propulsores RCS | Orientan y trasladan la nave en el espacio. |
| Motores de maniobra | Cambian la orbita y frenan para desorbitar. |

---

## 3. 🛡️ Escudo termico

Al reingresar, el aire frena la nave y genera un calor enorme. El escudo protege
la estructura.

- **Losetas ceramicas**: cubren las zonas mas calientes de la panza y las alas.
- **Mantas flexibles**: protegen zonas de calor moderado.
- **Borde de ataque reforzado**: soporta las temperaturas mas altas.
- **Regla clave**: la nave debe reingresar con el escudo por delante, no las alas.

---

## 4. 🪽 Alas, timones y tren de aterrizaje

En el regreso, el orbitador deja de ser nave y se comporta como planeador.

```mermaid
flowchart LR
    Aire[Aire cada vez mas denso] --> Alas[Alas generan sustentacion]
    Alas --> Planea[La nave planea sin motor]
    Timon[Timon y elevones] --> Controla[Controla el rumbo y el descenso]
    Planea --> Pista[Aproximacion a la pista]
    Tren[Tren de aterrizaje] --> Toca[Toca y frena en pista]
```

| Sistema | Funcion |
| --- | --- |
| Alas | Generan sustentacion para planear en el aire denso. |
| Elevones | Superficies que combinan control de cabeceo y alabeo. |
| Timon de direccion | Ayuda a orientar la nave y frenar en la pista. |
| Tren de aterrizaje | Se despliega para el toque final en pista. |
| Paracaidas de frenado | Reduce la velocidad tras tocar tierra. |

---

## 5. 🔋 Energia y soporte vital

Mientras trabaja en orbita, el orbitador debe mantener con vida a su tripulacion.

- **Pilas de combustible**: generan electricidad y agua como subproducto.
- **Control de aire**: provee oxigeno y retira el dioxido de carbono.
- **Control termico**: radiadores que expulsan el calor sobrante al espacio.
- **Agua y residuos**: se gestionan para la duracion de la mision.

---

## 🔁 Como se conecta todo

1. El **grupo de despegue** lleva el orbitador a la orbita.
2. El **orbitador** trabaja en el espacio con su cabina y su bahia de carga.
3. El **escudo termico** protege a la nave al reingresar.
4. Las **alas y timones** convierten la reentrada en un planeo controlado.
5. El **tren de aterrizaje** cierra la mision con un toque en pista.

Con esto entendido, el [Modulo 4: Mandos](../mandos/manual-mandos-transbordador.md)
muestra como la tripulacion opera estos sistemas.

---

[⬅️ Anterior: Caracteristicas](caracteristicas-transbordador.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-transbordador.md)
