---
tipo_documento: clase
clase: 4
codigo: PORTAVIONES-04
curso: portaviones
titulo: "Sistemas mecánicos del portaviones"
modalidad: "teórica aplicada"
duracion_minutos: 90
nivel: introductorio
prerrequisito: PORTAVIONES-03
competencia: "comprension_de_sistemas"
resultados_aprendizaje:
  - "Explicar Casco y flotación, Propulsión, Gobierno y timón y Cubierta de vuelo y hangar (nivel divulgativo) con vocabulario propio de Portaviones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Portaviones."
evidencia: "Esquema con flujos de energía, materia o información anotados."
criterio_aprobacion: "Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🔧 Sistemas mecánicos del portaviones

[🏠 Inicio](../../../README.md) · [🛳️ Curso: Portaviones](../README.md) · 🔧 Sistemas mecánicos

Este módulo describe, **solo con física pública y a nivel divulgativo**, como
flota, avanza, gobierna y opera su cubierta un portaviones. No incluye sistemas
de armas, táctica ni datos sensibles. Es la base para entender los mandos
(Módulo 5) y la física de la navegación (Módulo 6).

```mermaid
flowchart LR
    subgraph Propulsion
        M[Planta propulsora] --> Ej[Línea de ejes] --> H[Hélices]
    end
    subgraph Gobierno
        Ti[Timón] --> Pa[Pala del timón]
    end
    subgraph Cubierta
        Cv[Cubierta de vuelo] --- Ha[Hangar]
        Ha --- As[Ascensores]
    end
    H --> Empuje[Empuje]
    Pa --> Rumbo[Rumbo]
    Cv --> Logistica[Logística de cubierta]
```

---

## 1. 🚢 Casco y flotación

El casco estanco sostiene un buque enorme por flotación, con la cubierta como
techo estructural.

- **Reserva de flotabilidad**: gran volumen estanco por encima de la flotación.
- **Compartimentación**: mamparos que dividen el casco para limitar inundaciones.
- **Estabilidad**: el peso alto de la cubierta y la isla se compensa con lastre.

| Parte | Función | Efecto en el buque |
| --- | --- | --- |
| Quilla | Eje estructural inferior | Rigidez y estabilidad. |
| Mamparos | Dividen el casco | Contienen inundaciones. |
| Cubierta de vuelo | Techo y zona de trabajo | Peso alto que afecta estabilidad. |
| Isla | Superestructura lateral | Aloja el puente. |

---

## 2. 🔧 Propulsión

Convierte energía en empuje para mover una masa enorme.

```mermaid
flowchart LR
    Energia[Energía / calderas] --> Planta[Planta propulsora]
    Planta --> Eje[Línea de ejes]
    Eje --> Helice[Hélices]
    Helice -->|empuja agua atrás| Empuje[Empuje adelante]
```

- **Planta propulsora**: genera la potencia; varios ejes y hélices.
- **Línea de ejes**: transmite el giro a las hélices.
- **Hélices**: empujan agua hacia atrás y, por reacción, mueven el buque.
- **Viento sobre cubierta**: navegar contra el viento aumenta el viento relativo
  sobre la cubierta, concepto útil para las operaciones de vuelo.

---

## 3. ⚙️ Gobierno y timón

- **Pala del timón**: al girar desvia el agua y hace rotar el buque.
- **Servomotor**: mueve la pala con la fuerza necesaria para la gran masa.
- **Inercia**: por su tamaño, el giro es muy amplio y lento.

---

## 4. 🛫 Cubierta de vuelo y hangar (nivel divulgativo)

La cubierta de vuelo y el hangar son el rasgo distintivo. Se describen solo como
logística y seguridad general, sin detalle operativo sensible.

- **Cubierta de vuelo**: superficie plana donde se estacionan y mueven aeronaves.
- **Cubierta angulada**: separa las zonas de despegue y aterrizaje para más
  seguridad.
- **Hangar**: espacio interior bajo cubierta para guardar y mantener aeronaves.
- **Ascensores**: plataformas que suben y bajan aeronaves entre hangar y cubierta.

| Elemento | Función | Nota divulgativa |
| --- | --- | --- |
| Cubierta de vuelo | Operar aeronaves | Zona de trabajo abierta. |
| Cubierta angulada | Separar operaciones | Mejora la seguridad. |
| Hangar | Guardar aeronaves | Bajo la cubierta. |
| Ascensores | Mover aeronaves | Conectan hangar y cubierta. |
| Isla | Control y observación | Visión de la cubierta. |

---

## 5. ⚖️ Estabilidad y flotabilidad

| Concepto | Definición | Riesgo si falla |
| --- | --- | --- |
| Centro de gravedad (G) | Punto donde actua el peso total. | Muy alto: inestable. |
| Metacentro (M) | Referencia de estabilidad al escorar. | G sobre M: riesgo de vuelco. |
| Escora | Inclinación transversal. | Excesiva: peligrosa en cubierta. |
| Lastre | Agua de ajuste de peso. | Mal manejo: inestabilidad. |
| Compartimentación | Zonas estancas. | Limita inundaciones. |

---

## 🔁 Cómo se conecta todo

1. El **casco** aporta flotación y sostiene la **cubierta**.
2. La **planta propulsora** mueve las **hélices** para avanzar.
3. El **timón** desvia el agua para cambiar el rumbo.
4. La **cubierta y el hangar** organizan la logística a nivel general.
5. El **lastre** y la **compartimentación** cuidan la estabilidad.

Con esto entendido, el
[Módulo 5: Mandos](../mandos/manual-mandos-portaviones.md) describe, a nivel
educativo, como se navega el buque desde el puente.

## 🎓 Cierre de clase

- **Actividad:** Dibuja un esquema funcional de Portaviones que conecte Casco y flotación, Propulsión, Gobierno y timón y Cubierta de vuelo y hangar (nivel divulgativo); después predice el efecto de una falla simulada.
- **Evidencia:** Esquema con flujos de energía, materia o información anotados.
- **Criterio de aprobación:** Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-NHHC-SHIPS](https://www.history.navy.mil/browse-by-topic/ships.html): Ships, Naval History and Heritage Command. Uso: historia pública de buques militares.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-portaviones.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-portaviones.md)
