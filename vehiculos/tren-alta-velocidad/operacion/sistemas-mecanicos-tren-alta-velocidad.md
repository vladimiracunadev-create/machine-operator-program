<!-- clase-meta
tipo_documento: clase
clase: 4
codigo: TRENALTAVELO-04
curso: tren-alta-velocidad
titulo: "Sistemas mecánicos del tren de alta velocidad"
modalidad: "teórica aplicada"
duracion_minutos: 90
nivel: introductorio
prerrequisito: TRENALTAVELO-03
competencia: "comprension_de_sistemas"
resultados_aprendizaje:
  - "Explicar Tracción eléctrica de alta potencia, Bogies y ruedas de pestaña, Frenado de gran masa a alta velocidad y Aerodinámica con vocabulario propio de Tren de alta velocidad."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de alta velocidad."
evidencia: "Esquema con flujos de energía, materia o información anotados."
criterio_aprobacion: "Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🔧 Sistemas mecánicos del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 🔧 Sistemas mecánicos

Esta clase abre el tren de alta velocidad por dentro. Explica cada sistema, como
funciona y cómo se conecta con los demás, con foco en la tracción eléctrica de
alta potencia, el frenado de gran masa, la aerodinámica y la vía dedicada. Es la
base técnica para entender los mandos (Clase 5) y la física (Clase 6).

```mermaid
flowchart LR
    subgraph Alimentacion
        Cat[Catenaria alta tensión] --> Pan[Pantógrafo único]
        Pan --> Tr[Transformador]
        Tr --> Conv[Convertidores]
    end
    subgraph Traccion
        Conv --> Mot[Motores repartidos EMU]
        Mot --> Bog[Bogies motores]
    end
    subgraph Rodante
        Bog --- Rue[Ruedas de pestaña]
        Rue --- Riel[Riel de vía dedicada]
    end
    subgraph Frenado
        Reg[Freno regenerativo]
        Neu[Freno neumático]
        Fou[Freno de Foucault]
    end
    Reg -. frena .-> Bog
    Neu -. frena .-> Rue
    Fou -. frena .-> Riel
```

---

## 1. ⚡ Tracción eléctrica de alta potencia

El tren no lleva combustible a bordo: toma energía eléctrica de la **catenaria de
alta tensión** mediante un **pantógrafo único** en contacto con el cable. A alta
velocidad se usa un solo pantógrafo activo para reducir el arco eléctrico y el
ruido aerodinámico.

```mermaid
flowchart LR
    Catenaria[Catenaria alta tensión] --> Pantografo[Pantógrafo único]
    Pantografo --> Transformador[Transformador principal]
    Transformador --> Convertidor[Convertidores de potencia]
    Convertidor --> Motores[Motores de tracción]
    Motores --> Ejes[Ejes de bogies motores]
```

| Componente | Función |
| --- | --- |
| Catenaria | Cable aéreo que lleva la alta tensión a lo largo de la vía. |
| Pantógrafo | Brazo articulado que roza la catenaria y capta la corriente. |
| Transformador | Adapta la tensión de línea a la del tren. |
| Convertidores | Regulan la energía entregada a los motores. |
| Motores de tracción | Convierten la electricidad en giro de los ejes. |

- **Tracción distribuida (EMU)**: los motores se reparten en varios coches. Esto
  mejora la adherencia (más ejes motores) y reparte el esfuerzo.
- **Tracción concentrada**: la potencia se concentra en una locomotora en cabeza
  (y a veces en cola) que remolca coches sin motor.
- **Tensión exacta de línea para Chile**: por confirmar, al no existir red de
  alta velocidad comercial.

---

## 2. 🛞 Bogies y ruedas de pestaña

El **bogie** es el carro con ejes, ruedas y suspensión sobre el que se apoya cada
coche. Las **ruedas de pestaña** guian el tren sobre el riel: la pestaña interior
impide que la rueda se salga y el perfil cónico ayuda a centrar el eje.

| Elemento | Función |
| --- | --- |
| Bogie | Estructura con ejes y suspensión bajo cada coche. |
| Rueda de pestaña | Rueda con reborde que se mantiene sobre el riel. |
| Perfil cónico | Centra el eje y ayuda a tomar curvas. |
| Suspensión primaria | Une eje y bogie, filtra irregularidades del riel. |
| Suspensión secundaria | Une bogie y coche, da confort al pasajero. |

- **Adherencia rueda-riel**: el contacto acero contra acero tiene poca fricción,
  por eso repartir motores (EMU) ayuda a no patinar al acelerar.
- **Estabilidad**: a alta velocidad los bogies deben evitar la oscilación
  llamada movimiento de lazo, con amortiguadores especiales.

---

## 3. 🛑 Frenado de gran masa a alta velocidad

Detener un tren de alta velocidad exige combinar varios frenos, porque la energía
cinética es enorme y la distancia de frenado se mide en kilómetros. El freno solo
de fricción no basta ni disiparía el calor con seguridad.

```mermaid
flowchart TD
    Mando[Manipulador de freno] --> Gestion[Gestión de frenado]
    Gestion --> Regen[Freno regenerativo]
    Gestion --> Dinamico[Freno dinámico]
    Gestion --> Neumatico[Freno neumático]
    Gestion --> Foucault[Freno de Foucault / eddy]
    Regen --> Red[Devuelve energía a la catenaria]
    Dinamico --> Calor[Disipa como calor]
    Neumatico --> Zapata[Zapatas y discos en ruedas]
    Foucault --> Riel[Frena sin contacto sobre el riel]
```

| Tipo de freno | Como funciona | Nota |
| --- | --- | --- |
| Regenerativo | El motor actua como generador y devuelve energía a la línea. | Ahorra energía y frena sin desgaste. |
| Dinámico | El motor genera electricidad que se disipa como calor. | Útil cuando la línea no admite regeneración. |
| Neumático | Aire comprimido aprieta zapatas o discos en las ruedas. | Freno de fricción clásico, para baja velocidad y parada. |
| Foucault / eddy | Corrientes inducidas frenan sobre el riel sin contacto. | Sin desgaste; útil a alta velocidad. |

- El **freno regenerativo** y el **dinámico** hacen la mayor parte del trabajo a
  alta velocidad; el **neumático** completa la detención final.
- El **freno de Foucault** (corrientes de Foucault o eddy) frena sin tocar la
  rueda, lo que reduce el desgaste en frenadas fuertes.

---

## 4. 🌬️ Aerodinámica

Por encima de 250 km/h la **resistencia del aire domina** sobre las demás fuerzas
de oposición. Por eso la forma del tren importa tanto como su potencia.

| Aspecto aerodinámico | Efecto |
| --- | --- |
| Forma de nariz | Una nariz larga reduce la resistencia y la onda de presión. |
| Resistencia del aire | Crece con el cuadrado de la velocidad; domina a alta velocidad. |
| Ruido | El flujo de aire y el pantógrafo generan ruido que se busca reducir. |
| Túneles | Al entrar a un túnel se crea una onda de presión y un estampido de salida. |
| Onda de presión | La nariz alargada suaviza el golpe de presión al cruzarse trenes o entrar a túneles. |

- La resistencia aerodinámica obliga a carenar bajos, juntas entre coches y el
  propio pantógrafo.
- En **túneles largos** la sección del túnel y la forma del tren definen el
  confort de oidos de los pasajeros.

---

## 5. 🛤️ Vía dedicada y ancho de vía

La alta velocidad necesita una **línea de gran velocidad (LGV)** construida para
ese fin. No comparte los cruces ni las curvas cerradas de una red convencional.

| Elemento de vía | Función |
| --- | --- |
| Radios de curva amplios | Permiten mantener alta velocidad sin fuerza lateral excesiva. |
| Peralte | La vía se inclina en curva para compensar la fuerza centrífuga. |
| Sin pasos a nivel | Elimina cruces con carreteras, principal fuente de riesgo. |
| Vía dedicada (LGV) | Trazado exclusivo para alta velocidad. |
| Ancho de vía | Trocha internacional como referencia; valor exacto para Chile por confirmar. |

- Los **radios de curva amplios** y el **peralte** permiten tomar curvas sin que
  el pasajero sienta fuerza lateral molesta.
- El **ancho de vía** de referencia es la trocha internacional; el valor exacto
  aplicable a Chile queda por confirmar.

---

## 6. 📡 Señalización en cabina ETCS/ERTMS

A alta velocidad el maquinista **no puede leer señales laterales**: pasan
demasiado rápido. La información de circulación se muestra dentro de la cabina.

```mermaid
flowchart LR
    Via[Balizas y vía] --> Tren[Equipo embarcado ETCS]
    Tren --> DMI[Pantalla DMI en cabina]
    DMI --> Maquinista[Maquinista]
    Maquinista -. respeta .-> Objetivo[Velocidad objetivo]
    Tren -. supervisa .-> Freno[Freno automático si excede]
```

| Elemento | Función |
| --- | --- |
| ETCS | Sistema europeo de control del tren embarcado. |
| ERTMS | Marco que integra ETCS y comunicaciones. |
| DMI | Pantalla en cabina que muestra la velocidad objetivo. |
| Balizas | Puntos en la vía que informan al tren su posición y límites. |
| Supervisión | Si el tren excede el límite, el sistema frena solo. |

La señalización embarcada supervisa la velocidad y aplica el freno de forma
automática si el maquinista no respeta el límite, lo que es imprescindible a esa
velocidad.

---

## 🔁 Cómo se conecta todo

1. El **pantógrafo** capta la energía de la **catenaria** de alta tensión.
2. El **transformador** y los **convertidores** la adaptan a los **motores**.
3. Los **motores repartidos** mueven los **bogies** y las **ruedas de pestaña**.
4. La **vía dedicada** con curvas amplias y peralte permite mantener la velocidad.
5. La **aerodinámica** reduce la resistencia del aire, que domina a alta velocidad.
6. El **frenado combinado** (regenerativo, dinámico, neumático y de Foucault) detiene la gran masa.
7. La **señalización en cabina** ETCS/ERTMS informa y supervisa la velocidad objetivo.

Con esto entendido, el [Clase 5: Mandos](../mandos/manual-mandos-tren-alta-velocidad.md)
muestra como el maquinista opera cada uno de estos sistemas.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Tracción eléctrica de alta potencia, Bogies y ruedas de pestaña, Frenado de gran masa a alta velocidad y Aerodinámica** a **seguir una alteración desde catenaria hasta rueda-carril durante reducción de velocidad previa a una zona de viento lateral**?

### Explicación razonada

El funcionamiento puede leerse como una cadena causal: catenaria entrega o transforma energía; electrónica de potencia la adapta; motores distribuidos la transmite o gobierna; y rueda-carril produce el efecto observable. La cadena no es lineal en sentido estricto: sensores, estructura y operador cierran el lazo. Si un eslabón se degrada, la señal importante es cómo cambia el estado de rueda-carril y qué margen queda.

```mermaid
flowchart LR
    A["catenaria"] --> B["electrónica de potencia"] --> C["motores distribuidos"] --> D["rueda-carril"]
    D -. respuesta observable .-> O["operador o control"]
    O -. orden y verificación .-> A
```

Esta clase se conecta con el resto del curso mediante **estabilidad dinámica y crecimiento de la energía con el cuadrado de la velocidad**. El hilo de
seguridad consiste en reconocer a tiempo **perder margen por interpretar tarde una restricción a velocidad elevada** y poder justificar la decisión
**cumplir la curva de frenado con anticipación y sin correcciones bruscas**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **catenaria → electrónica de potencia → motores distribuidos → rueda-carril**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Railroad Operating Practices](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0) aporta operación, señalización y competencias ferroviarias;
[Human Factors: Tasks and Demands](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands) se usa para factores humanos y carga de trabajo. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Entrada:** identifica el estado inicial de **catenaria** durante **reducción de velocidad previa a una zona de viento lateral**.
2. **Transformación:** explica qué hacen **electrónica de potencia** y **motores distribuidos**, y qué magnitud cambia en cada paso.
3. **Salida:** comprueba el efecto esperado en **rueda-carril** y busca una desviación temprana.
4. **Falla razonada:** si aparece **perder margen por interpretar tarde una restricción a velocidad elevada**, retrocede por la cadena antes de ordenar otra acción.

### Comprueba tu comprensión

1. Si se degrada **electrónica de potencia**, ¿qué efecto esperarías primero en **motores distribuidos** y después en **rueda-carril**?
2. ¿Qué observación ayudaría a diferenciar una falla de **catenaria** de una falla de **motores distribuidos**?
3. ¿Por qué una segunda orden podría agravar **perder margen por interpretar tarde una restricción a velocidad elevada**?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Dibuja un esquema funcional de Tren de alta velocidad que conecte Tracción eléctrica de alta potencia, Bogies y ruedas de pestaña, Frenado de gran masa a alta velocidad y Aerodinámica; después predice el efecto de una falla simulada.
- **Evidencia:** Esquema con flujos de energía, materia o información anotados.
- **Criterio de aprobación:** Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-tren-alta-velocidad.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-tren-alta-velocidad.md)
