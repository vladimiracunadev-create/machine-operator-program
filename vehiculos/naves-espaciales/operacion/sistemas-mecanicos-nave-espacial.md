# 🔧 Sistemas mecanicos de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🔧 Sistemas mecanicos

Este modulo abre la nave por dentro. Explica cada sistema, como funciona y como se
conecta con los demas, distinguiendo ciencia real de ficcion. Es la base tecnica
para entender los mandos (Modulo 4) y la fisica orbital (Modulo 5).

```mermaid
flowchart LR
    subgraph Propulsion
        Prop[Propelente] --> Motor[Motor cohete]
        Motor --> Tobera[Tobera]
    end
    subgraph Estructura
        Etapas[Etapas]
        Escudo[Escudo termico]
    end
    subgraph Soporte
        Vital[Soporte vital]
        Energia[Energia]
    end
    subgraph Control
        RCS[Propulsores RCS]
    end
    Tobera --> Empuje[Empuje]
    Empuje --> Etapas
    Energia --> Vital
    Energia --> RCS
```

---

## 1. 🔥 Propulsion cohete

El motor cohete impulsa la nave expulsando gases a gran velocidad. A diferencia de
un avion, **no** necesita aire: lleva su propio oxidante.

```mermaid
flowchart LR
    Comb[Combustible] --> Camara[Camara de combustion]
    Oxid[Oxidante] --> Camara
    Camara --> Gases[Gases a alta presion]
    Gases --> Tobera[Tobera]
    Tobera --> Empuje[Empuje hacia adelante]
```

| Componente | Funcion |
| --- | --- |
| Combustible | Materia que se quema o expulsa. |
| Oxidante | Aporta el oxigeno para quemar sin aire externo. |
| Camara de combustion | Donde se quema la mezcla y sube la presion. |
| Tobera | Acelera los gases y convierte presion en empuje. |
| Presupuesto de delta-v | Cambio total de velocidad que la nave puede lograr. |

- **Propulsion quimica** (real): gran empuje, ideal para despegar.
- **Propulsion electrica / ionica** (real): poco empuje, muy eficiente, para el espacio.
- **Propulsion de ficcion**: motores de "curvatura" y similares, solo como escenario.

---

## 2. 🪜 Etapas y separacion

Un cohete se divide en etapas para no cargar peso muerto. Cada etapa se separa al
agotarse.

```mermaid
flowchart TD
    Total[Cohete completo] --> E1[Etapa 1: gran empuje]
    E1 -->|se agota y separa| E2[Etapa 2: empuje en altura]
    E2 -->|se agota y separa| Carga[Carga util en orbita]
```

| Elemento | Funcion |
| --- | --- |
| Etapa inferior | Vence la gravedad y el aire densos del despegue. |
| Etapa superior | Da la velocidad final para la orbita. |
| Separacion | Suelta la masa vacia para ganar eficiencia. |
| Carga util | Lo que se pone en orbita (satelite, capsula). |

---

## 3. 🧑‍🚀 Soporte vital

Mantiene a la tripulacion viva donde no hay aire ni presion.

| Subsistema | Funcion |
| --- | --- |
| Aire y presion | Provee oxigeno y mantiene la cabina presurizada. |
| Control de CO2 | Retira el dioxido de carbono que exhala la tripulacion. |
| Agua | Almacena y a veces recicla el agua. |
| Control termico | Regula la temperatura interior. |
| Residuos | Gestiona los desechos en microgravedad. |

En misiones largas, reciclar aire y agua es clave: no hay como reabastecerse.

---

## 4. 🔋 Energia

Alimenta todos los sistemas de a bordo.

- **Paneles solares** (real): convierten la luz del Sol en electricidad.
- **Baterias**: almacenan energia para la fase de sombra.
- **Pilas de combustible**: generan electricidad y agua como subproducto.
- **Generadores nucleares** (real, en sondas lejanas): energia donde el Sol es debil.

---

## 5. 🎯 Control de actitud

Orienta la nave en el espacio, donde no hay aire para usar timones.

```mermaid
flowchart LR
    Orden[Orden de giro] --> RCS[Propulsores RCS]
    Orden --> Ruedas[Ruedas de reaccion]
    RCS --> Giro[Cambio de orientacion]
    Ruedas --> Giro
    Giro --> Apunta[Nave apunta al objetivo]
```

| Sistema | Funcion |
| --- | --- |
| Propulsores RCS | Pequenos chorros que giran o trasladan la nave. |
| Ruedas de reaccion | Giran masas internas para orientar sin gastar propelente. |
| Sensores de actitud | Estrellas, Sol y giroscopos indican la orientacion. |
| Escudo termico | Protege en la reentrada, no es control pero es estructura clave. |

---

## 🔁 Como se conecta todo

1. La **propulsion** da el empuje para despegar y maniobrar.
2. Las **etapas** sueltan peso muerto para llegar a la **orbita**.
3. El **soporte vital** mantiene viva a la tripulacion.
4. La **energia** alimenta todos los sistemas.
5. El **control de actitud** orienta la nave sin aire.
6. El **escudo termico** protege en la **reentrada**.

Con esto entendido, el [Modulo 4: Mandos](../mandos/manual-mandos-nave-espacial.md)
muestra como la tripulacion opera estos sistemas.

---

[⬅️ Anterior: Caracteristicas](caracteristicas-nave-espacial.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-nave-espacial.md)
