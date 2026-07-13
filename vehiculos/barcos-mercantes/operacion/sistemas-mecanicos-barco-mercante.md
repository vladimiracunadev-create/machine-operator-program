# 🔧 Sistemas mecanicos del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🔧 Sistemas mecanicos

Este modulo abre el buque por dentro. Explica cada sistema, como funciona y como
se conecta con los demas. Es la base tecnica para entender los mandos (Modulo 4)
y la fisica de la navegacion (Modulo 5).

```mermaid
flowchart LR
    subgraph Propulsion
        M[Motor principal] --> Ej[Linea de ejes] --> H[Helice]
    end
    subgraph Gobierno
        Ti[Timon] --> Pa[Pala del timon]
    end
    subgraph Estructura
        Ca[Casco] --- La[Lastre]
        Ca --- Bo[Bodegas / tanques]
    end
    H --> Empuje[Empuje]
    Pa --> Rumbo[Rumbo]
    La --> Estabilidad[Estabilidad]
```

---

## 1. 🚢 Casco

El casco es la estructura estanca que da flotacion, resistencia y forma
hidrodinamica. Todo el buque se construye alrededor de el.

- **Obra viva**: parte sumergida; su forma define resistencia al avance.
- **Obra muerta**: parte sobre la linea de flotacion.
- **Doble casco / doble fondo**: proteccion ante averias y espacio de lastre.
- **Mamparos estancos**: dividen el casco en compartimentos para limitar
  inundaciones.

| Parte | Funcion | Efecto en el buque |
| --- | --- | --- |
| Proa | Corta el agua | Menor resistencia al avance. |
| Popa | Aloja timon y helice | Gobierno y propulsion. |
| Quilla | Eje estructural inferior | Rigidez y estabilidad. |
| Francobordo | Altura hasta cubierta | Reserva de flotabilidad. |
| Calado | Profundidad sumergida | Limita puertos y canales. |

---

## 2. 🔧 Propulsion

Convierte energia (combustible o electricidad) en empuje para avanzar.

```mermaid
flowchart LR
    Combustible[Combustible] --> Motor[Motor principal diesel]
    Motor --> Eje[Linea de ejes]
    Eje --> Helice[Helice]
    Helice -->|empuja agua atras| Empuje[Empuje adelante]
```

- **Motor principal**: normalmente un motor diesel lento de gran tamano acoplado
  directo al eje, o una planta diesel-electrica.
- **Linea de ejes**: transmite el giro del motor a la helice.
- **Helice**: al empujar agua hacia atras, genera empuje hacia adelante
  (tercera ley de Newton). Puede ser de paso fijo o de paso variable.
- **Propulsores auxiliares**: los de proa (bow thruster) ayudan a maniobrar en
  puerto a baja velocidad.

| Componente | Funcion | Nota |
| --- | --- | --- |
| Motor principal | Genera potencia | Diesel lento, muy eficiente. |
| Reductor | Adapta revoluciones | No siempre presente. |
| Linea de ejes | Transmite giro | Atraviesa el casco por la bocina. |
| Helice | Convierte giro en empuje | Paso fijo o variable. |
| Thruster de proa | Maniobra en puerto | Movimiento lateral a baja velocidad. |

---

## 3. ⚙️ Gobierno y timon

El gobierno cambia el rumbo desviando el flujo de agua en la popa.

```mermaid
flowchart TD
    Rueda[Rueda de gobierno] --> Piloto[Piloto automatico / servo]
    Piloto --> Servo[Servomotor del timon]
    Servo --> Pala[Pala del timon]
    Pala -->|desvia el agua| Giro[Cambio de rumbo]
```

- **Pala del timon**: al girar, desvia el flujo de agua y genera una fuerza que
  hace rotar el buque.
- **Servomotor**: mueve la pala con fuerza hidraulica siguiendo la orden del
  puente.
- **Efecto de la velocidad**: el timon casi no responde con el buque parado;
  necesita flujo de agua para gobernar.

---

## 4. 📦 Carga, estiba y estabilidad

El buque mercante existe para transportar carga con seguridad. La forma de
cargar afecta directamente la estabilidad.

- **Bodegas y tanques**: espacios donde se estiba la carga (seca o liquida).
- **Estiba**: distribucion de la carga para equilibrar el buque y evitar
  esfuerzos excesivos en el casco.
- **Lastre**: agua que se toma o descarga para ajustar calado y estabilidad
  cuando el buque va vacio o parcialmente cargado.
- **Metacentro y centro de gravedad**: su posicion relativa define si el buque
  es estable y vuelve a la vertical tras una escora.

| Concepto | Definicion | Riesgo si falla |
| --- | --- | --- |
| Centro de gravedad (G) | Punto donde actua el peso total. | Muy alto: buque inestable. |
| Metacentro (M) | Punto de equilibrio al escorar. | G sobre M: puede volcar. |
| Escora | Inclinacion transversal. | Excesiva: perdida de carga. |
| Asiento (trimado) | Diferencia de calado proa-popa. | Mal asiento: mal gobierno. |
| Lastre | Agua de ajuste de peso. | Mal manejo: inestabilidad. |

---

## 5. 🔩 Sistemas auxiliares

- **Generadores**: producen la electricidad de a bordo.
- **Sistema de achique**: extrae agua que entra al casco.
- **Sistema contraincendios**: bombas, detectores y extincion.
- **Fondeo**: anclas y cadenas para inmovilizar el buque.
- **Amarre**: cabos y cabrestantes para atracar en muelle.

---

## 🔁 Como se conecta todo

1. El **motor principal** genera potencia.
2. La **linea de ejes** la lleva a la **helice**, que produce empuje.
3. El **timon** desvia el agua en popa para cambiar el rumbo.
4. El **casco** aporta flotacion y aloja **carga y lastre**.
5. La **estiba y el lastre** mantienen la estabilidad.
6. Los **sistemas auxiliares** dan energia y seguridad.

Con esto entendido, el
[Modulo 4: Mandos](../mandos/manual-mandos-barco-mercante.md) muestra como la
tripulacion opera cada uno de estos sistemas desde el puente.

---

[⬅️ Anterior: Caracteristicas](caracteristicas-barco-mercante.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-barco-mercante.md)
