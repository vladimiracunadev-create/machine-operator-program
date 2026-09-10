<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: ASCENSORES-03
curso: ascensores
titulo: "Modelos y variantes del ascensor"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: ASCENSORES-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Ascensores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Ascensores."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del ascensor

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-ascensor.md) ya dijo qué tipos de
ascensor existen y para qué sirve cada uno. Esta clase responde a otra cosa:
**no todos se manejan igual**, y esa diferencia no es de matiz. Cambia qué
mandos tiene la máquina y, por tanto, qué debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** En el ascensor el "operador" habitual es
> el pasajero, y quien conduce de verdad es el cuadro de maniobra. Por eso los
> modelos casi no tocan la botonera pública: lo que cambian es la física que hay
> detrás del botón y el mando técnico que la gobierna. Un simulador que dé por
> supuesto un contrapeso y una polea de tracción está representando un ascensor
> de tracción, aunque diga representarlos todos.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-ascensor.md) describe un mapa de controles
con un **modo inspección**, accionado por llave o selector, reservado a personal
competente. El [Clase 9](../simulacion/diseno-simulador-ascensor.md) expone una
variable `Contrapeso` de tipo numérica y rango fijo, que "equilibra la cabina", y
una variable `Velocidad de descenso` derivada que "dispara el gobernador". Las
tres piezas describen un ascensor **de tracción con cuarto de máquinas**.

En un ascensor hidráulico no hay contrapeso que equilibre nada: el Clase 2 lo
dice sin rodeos, es "pistón; sin contrapeso en altura". La variable `Contrapeso`
no tiene un valor menor ni distinto: no tiene nada que representar. Y en uno sin
cuarto de máquinas el modo inspección deja de vivir en una sala superior porque
esa sala no existe. Si el simulador se construye sobre el caso de tracción con
sala y luego se le "añade" el hidráulico, el resultado es un hidráulico con
contrapeso, que no existe.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia en su operación |
| --- | --- |
| Tracción con cuarto de máquinas | La referencia del curso: contrapeso, tracción por fricción y grupo tractor en sala superior, accesible sin entrar al hueco. |
| Tracción sin cuarto de máquinas | Mismo principio de fricción y contrapeso, pero el motor compacto vive dentro del hueco: toda intervención técnica pasa por el hueco o por un armario de maniobra. |
| Hidráulico | Sube empujado por el pistón y baja por su propio peso liberando fluido. Sin contrapeso, el esfuerzo no es la diferencia de masas sino la carga completa. Propio de edificios bajos. |
| De pasajeros | El uso lo marcan personas que entran y salen: manda el confort, la nivelación precisa y la maniobra colectiva. |
| De carga | La cabina robusta y la gran capacidad hacen que la carga trabaje cerca del límite nominal, no lejos de él. La sobrecarga deja de ser un caso raro. |
| Panorámico | Mecánicamente es un ascensor de tracción; lo que cambia es la cabina con vista y el foco estético, no el manejo. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Tracción con cuarto de máquinas | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Es el caso de referencia. |
| Tracción sin cuarto de máquinas | Ninguno para el pasajero. El **modo inspección se muda**: sin sala, el selector se opera junto al hueco. | El mando técnico cambia de sitio y de contexto de riesgo, no de función. |
| Hidráulico | Ninguno para el pasajero. **Desaparece** el mando que se apoya en el grupo tractor de polea; el descenso lo gobierna el fluido. | La botonera es idéntica y detrás hay otra máquina: el mando público deja de informar del modelo. |
| De pasajeros | Ninguno: botón de apertura, cierre, alarma e intercomunicador tal como los lista el Clase 5. | Es el uso para el que está pensada la botonera. |
| De carga | El **indicador de sobrecarga** y el **botón de apertura** pasan de accesorios a mandos centrales durante la carga. | No aparece un control nuevo; cambia cuál es el control que se usa todo el rato. |
| Panorámico | Ninguno. | El mapa de controles no distingue este modelo. |

El hallazgo incómodo es este: **ningún modelo cambia la botonera del pasajero**.
Todos comparten llamada, destino, apertura, cierre, alarma y parada de
emergencia. Lo que cambia de modelo a modelo es el mando técnico —el modo
inspección— y el cuadro de maniobra al que ese mando accede. En una moto el
modelo se ve en el manillar; en un ascensor no se ve desde la cabina.

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-ascensor.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Tracción con cuarto de máquinas | Ninguna: es el caso base. | El del Clase 5. |
| Tracción sin cuarto de máquinas | `Estado de servicio` cambia de significado: pasar a `inspección` implica intervenir el hueco, no una sala aparte. | El mismo, con el modo inspección reubicado. |
| Hidráulico | `Contrapeso` **se elimina**. `Velocidad de descenso` deja de depender del gobernador y pasa a depender del fluido. `Velocidad` reduce su rango útil. | Sin contrapeso ni gobernador de polea; el descenso es el caso a modelar. |
| De pasajeros | `Cola de llamadas` es la variable protagonista: maniobra colectiva con paradas frecuentes. `Carga` se mueve lejos del límite. | El mismo. |
| De carga | `Carga` **deja de ser un margen y pasa a ser la restricción**: el estado de sobrecarga es habitual. `Estado de puerta` domina el ciclo. | El mismo, con el ciclo dominado por la carga y la puerta. |
| Panorámico | Ninguna. | El mismo. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Tipo{¿Tracción o hidráulico?}
    Tipo -- Tracción --> Contra[Esquema con contrapeso:<br/>fricción en polea,<br/>gobernador y freno de seguridad]
    Tipo -- Hidráulico --> Piston[Esquema con pistón:<br/>sin contrapeso,<br/>descenso por fluido]
    Contra --> Var1[Simulador con variable Contrapeso]
    Piston --> Var2[Simulador sin variable Contrapeso]
    Modelo --> Sala{¿Hay cuarto de máquinas?}
    Sala -- Sí --> Insp1[Modo inspección<br/>desde sala superior]
    Sala -- No --> Insp2[Modo inspección<br/>junto al hueco]
    Modelo --> Uso{¿Pasajeros o carga?}
    Uso -- Pasajeros --> Cola[Cola de llamadas<br/>como variable central]
    Uso -- Carga --> Peso[Carga en el límite<br/>y sobrecarga habitual]
```

---

## ⚠️ Qué modelos no comparten simulador

Dos casos no se resuelven con un ajuste de parámetros, porque el modelo físico o
el esquema de control es otro:

- **El hidráulico** frente a los de tracción: desaparece una variable
  (`Contrapeso`) y otra (`Velocidad de descenso`) cambia de causa. El equilibrio
  con contrapeso y la tracción por fricción, los dos primeros principios del
  [Clase 6](../operacion/principios-ascensor.md), sencillamente no aplican. No
  es un ascensor más lento: es otra máquina bajo la misma botonera.
- **El de carga** frente al de pasajeros: obliga a que la sobrecarga sea un
  estado de trabajo normal y no una excepción. El ciclo pasa a girar en torno a
  la carga y la puerta, no en torno a la cola de llamadas.

El resto de modelos sí caben en un mismo simulador ajustando rangos, tal como
plantean los [niveles de realismo](../../../docs/03-niveles-de-realismo.md): en
el nivel 1 todos se comportan igual, porque llamar, viajar y abrir la puerta es
idéntico en cualquiera de ellos. Las diferencias solo emergen en el nivel 2,
cuando entra el contrapeso, y en el nivel 3, cuando entran el gobernador, el
freno de seguridad y el modo inspección.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar ascensor de tracción frente a ascensor hidráulico frente al mismo encargo**?

### Explicación razonada

Las variantes «ascensor de tracción frente a ascensor hidráulico» resuelven prioridades distintas. Una comparación profesional sigue la cadena motor → polea tractora → cables → cabina y contrapeso: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **equilibrio de masas y control de aceleración, velocidad, nivelación y frenado**. El hilo de
seguridad consiste en reconocer a tiempo **movimiento con puertas inseguras, mala nivelación o pérdida de tracción** y poder justificar la decisión
**verificar enclavamientos y estado antes de autorizar el movimiento**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → polea tractora → cables → cabina y contrapeso**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [1917.116 Elevators and Escalators](https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116) aporta inspección y riesgos de transporte vertical;
[Vehicle Safety](https://www.nhtsa.gov/vehicle-safety) se usa para seguridad de vehículos terrestres. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **viaje con carga variable seguido de una orden de parada en piso**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **motor** hasta **cabina y contrapeso**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **motor → polea tractora → cables → cabina y contrapeso** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «viaje con carga variable seguido de una orden de parada en piso» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Ascensores mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-ELEVATORS](https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116): 1917.116 Elevators and Escalators, OSHA. Uso: inspección y riesgos de transporte vertical.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-ascensor.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-ascensor.md)
</content>
</invoke>
