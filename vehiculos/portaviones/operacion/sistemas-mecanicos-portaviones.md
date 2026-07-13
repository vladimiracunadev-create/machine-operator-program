# 🔧 Sistemas mecanicos del portaviones

[🏠 Inicio](../../../README.md) · [🛳️ Curso: Portaviones](../README.md) · 🔧 Sistemas mecanicos

Este modulo describe, **solo con fisica publica y a nivel divulgativo**, como
flota, avanza, gobierna y opera su cubierta un portaviones. No incluye sistemas
de armas, tactica ni datos sensibles. Es la base para entender los mandos
(Modulo 4) y la fisica de la navegacion (Modulo 5).

```mermaid
flowchart LR
    subgraph Propulsion
        M[Planta propulsora] --> Ej[Linea de ejes] --> H[Helices]
    end
    subgraph Gobierno
        Ti[Timon] --> Pa[Pala del timon]
    end
    subgraph Cubierta
        Cv[Cubierta de vuelo] --- Ha[Hangar]
        Ha --- As[Ascensores]
    end
    H --> Empuje[Empuje]
    Pa --> Rumbo[Rumbo]
    Cv --> Logistica[Logistica de cubierta]
```

---

## 1. 🚢 Casco y flotacion

El casco estanco sostiene un buque enorme por flotacion, con la cubierta como
techo estructural.

- **Reserva de flotabilidad**: gran volumen estanco por encima de la flotacion.
- **Compartimentacion**: mamparos que dividen el casco para limitar inundaciones.
- **Estabilidad**: el peso alto de la cubierta y la isla se compensa con lastre.

| Parte | Funcion | Efecto en el buque |
| --- | --- | --- |
| Quilla | Eje estructural inferior | Rigidez y estabilidad. |
| Mamparos | Dividen el casco | Contienen inundaciones. |
| Cubierta de vuelo | Techo y zona de trabajo | Peso alto que afecta estabilidad. |
| Isla | Superestructura lateral | Aloja el puente. |

---

## 2. 🔧 Propulsion

Convierte energia en empuje para mover una masa enorme.

```mermaid
flowchart LR
    Energia[Energia / calderas] --> Planta[Planta propulsora]
    Planta --> Eje[Linea de ejes]
    Eje --> Helice[Helices]
    Helice -->|empuja agua atras| Empuje[Empuje adelante]
```

- **Planta propulsora**: genera la potencia; varios ejes y helices.
- **Linea de ejes**: transmite el giro a las helices.
- **Helices**: empujan agua hacia atras y, por reaccion, mueven el buque.
- **Viento sobre cubierta**: navegar contra el viento aumenta el viento relativo
  sobre la cubierta, concepto util para las operaciones de vuelo.

---

## 3. ⚙️ Gobierno y timon

- **Pala del timon**: al girar desvia el agua y hace rotar el buque.
- **Servomotor**: mueve la pala con la fuerza necesaria para la gran masa.
- **Inercia**: por su tamano, el giro es muy amplio y lento.

---

## 4. 🛫 Cubierta de vuelo y hangar (nivel divulgativo)

La cubierta de vuelo y el hangar son el rasgo distintivo. Se describen solo como
logistica y seguridad general, sin detalle operativo sensible.

- **Cubierta de vuelo**: superficie plana donde se estacionan y mueven aeronaves.
- **Cubierta angulada**: separa las zonas de despegue y aterrizaje para mas
  seguridad.
- **Hangar**: espacio interior bajo cubierta para guardar y mantener aeronaves.
- **Ascensores**: plataformas que suben y bajan aeronaves entre hangar y cubierta.

| Elemento | Funcion | Nota divulgativa |
| --- | --- | --- |
| Cubierta de vuelo | Operar aeronaves | Zona de trabajo abierta. |
| Cubierta angulada | Separar operaciones | Mejora la seguridad. |
| Hangar | Guardar aeronaves | Bajo la cubierta. |
| Ascensores | Mover aeronaves | Conectan hangar y cubierta. |
| Isla | Control y observacion | Vision de la cubierta. |

---

## 5. ⚖️ Estabilidad y flotabilidad

| Concepto | Definicion | Riesgo si falla |
| --- | --- | --- |
| Centro de gravedad (G) | Punto donde actua el peso total. | Muy alto: inestable. |
| Metacentro (M) | Referencia de estabilidad al escorar. | G sobre M: riesgo de vuelco. |
| Escora | Inclinacion transversal. | Excesiva: peligrosa en cubierta. |
| Lastre | Agua de ajuste de peso. | Mal manejo: inestabilidad. |
| Compartimentacion | Zonas estancas. | Limita inundaciones. |

---

## 🔁 Como se conecta todo

1. El **casco** aporta flotacion y sostiene la **cubierta**.
2. La **planta propulsora** mueve las **helices** para avanzar.
3. El **timon** desvia el agua para cambiar el rumbo.
4. La **cubierta y el hangar** organizan la logistica a nivel general.
5. El **lastre** y la **compartimentacion** cuidan la estabilidad.

Con esto entendido, el
[Modulo 4: Mandos](../mandos/manual-mandos-portaviones.md) describe, a nivel
educativo, como se navega el buque desde el puente.

---

[⬅️ Anterior: Caracteristicas](caracteristicas-portaviones.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-portaviones.md)
