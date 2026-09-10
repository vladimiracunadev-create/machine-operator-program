<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: AVIONESPEQUE-03
curso: aviones-pequenos
titulo: "Modelos y variantes del avión pequeño"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: AVIONESPEQUE-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Aviones pequeños."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones pequeños."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del avión pequeño

[🏠 Inicio](../../../README.md) · [🛩️ Curso: Aviones pequeños](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-avion-pequeno.md) ya dijo qué tipos de
avión pequeño existen y para qué sirve cada uno. Esta clase responde a lo
siguiente: **no todos se pilotan igual**, y esa diferencia no es de matiz. Cambia
qué mandos tiene la máquina y, por tanto, qué debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** "Un avión pequeño" no es una sola
> máquina desde el punto de vista del mando. Un turismo con tren retráctil y
> hélice de paso variable tiene dos palancas que en un monomotor de escuela **no
> existen**: no son las mismas más difíciles, es que no están. Un simulador que
> presente un solo esquema de control está representando un avión concreto aunque
> diga representarlos todos.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-avion-pequeno.md) describe una consola con
tres mandos de motor: **acelerador, mezcla y flaps**. No hay palanca de hélice ni
selector de tren. El [Clase 9](../simulacion/diseno-simulador-avion-pequeno.md)
expone una variable `Potencia del motor` de `0-100%` como único parámetro de
propulsión. Ambos describen un avión de **hélice de paso fijo, tren fijo y un
solo motor**: el monomotor de escuela del Clase 2.

En cuanto el modelo lleva hélice de paso variable, ese `0-100%` deja de bastar:
la potencia pasa a ser un par de valores —presión de admisión y rpm— que el
piloto ajusta con dos palancas distintas, y el tacómetro deja de seguir al
acelerador. Y en cuanto el tren es retráctil, aparece un mando con estado propio
que el Clase 9 no tiene: la posición del tren no es un ajuste, es una condición
del aterrizaje. Si el simulador se construye sobre el esquema de escuela y luego
se le "añade" un bimotor de turismo, el resultado es un bimotor con una sola
palanca de gases, que no existe.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia al pilotarlo |
| --- | --- |
| Monomotor de escuela | La referencia del curso: estable, perdonador y con la respuesta más previsible de la familia. |
| Ultraligero | Muy liviano: el viento deja de ser una corrección y pasa a ser el factor dominante de la trayectoria. |
| Deportivo ligero | Moderno y simple, cercano al de escuela; el mando suele ser bastón en vez de yugo, con la mano de potencia siempre disponible. |
| Turismo monomotor | Vuela más rápido y con más autonomía: el piloto gestiona configuración —tren, hélice, mezcla— además de volar. |
| Bimotor ligero | Con los dos motores dando lo mismo se parece a un monomotor; en cuanto uno falla, el empuje es asimétrico y la guiñada deja de ser una coordinación y pasa a ser una carga sostenida. |
| Anfibio / hidroavión | El "suelo" cambia de naturaleza: sobre agua no hay pista alineada ni frenos de rueda, y la superficie misma se mueve. |
| Tren de patín de cola (variante de varios modelos) | El rodaje se invierte: el avión tiende a irse de cola y el piloto lo corrige activamente con pedales todo el tiempo. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Monomotor de escuela, Deportivo ligero | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Cambian los rangos, no los controles. |
| Ultraligero | El mando de vuelo es bastón en lugar de yugo; la consola es la más reducida del curso. | Menos que gestionar, pero cada entrada pesa más en el resultado. |
| Turismo monomotor (paso variable) | **Aparece** la palanca de hélice, un tercer mando de consola entre acelerador y mezcla. | La potencia deja de fijarse con un solo control, y el tacómetro deja de depender del acelerador. |
| Turismo monomotor (tren retráctil) | **Aparece** el selector de tren, con posición propia y aviso asociado. | Nuevo mando de estado: recogerlo y sacarlo son pasos obligados del despegue y la aproximación. |
| Bimotor ligero | **Se duplican** acelerador, mezcla y hélice; **aparecen** los mandos de selección por motor. | Un solo eje de "potencia" ya no representa la consola: son dos conjuntos que pueden diferir. |
| Anfibio / hidroavión | Sobre flotadores **desaparecen** los frenos de las puntas de los pedales. En el anfibio **aparece** el selector de tren, con la posición correcta dependiendo de la superficie. | El pedal pierde su segunda función en agua; en el anfibio el mismo mando significa cosas opuestas según dónde se ameriza o aterriza. |
| Variante de patín de cola | No aparece ningún mando, pero los pedales dejan de ser un control de coordinación en tierra y pasan a ser un control continuo. | El rodaje deja de ser una fase pasiva del simulador. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-avion-pequeno.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Monomotor de escuela | Ninguna: es el caso base. | El del Clase 5. |
| Ultraligero | `Viento` deja de ser una corrección de rumbo y pasa a pesar en el cálculo como el resto de fuerzas. `Velocidad (IAS)` y `Altitud` reducen su rango útil. | El mismo, con bastón y consola mínima. |
| Deportivo ligero | Ninguna estructural: `Velocidad (IAS)` y `Combustible` ajustan rango. | El mismo. |
| Turismo monomotor (paso variable) | `Potencia del motor` **deja de ser un escalar** `0-100%`: se desdobla en potencia demandada y régimen de hélice, que el piloto fija por separado. | Tres mandos de consola; el tacómetro pasa a ser una lectura gobernada, no un reflejo del acelerador. |
| Turismo monomotor (tren retráctil) | **Aparece** una variable de estado del tren (recogido / extendido / en tránsito) que el Clase 9 no contempla, y que entra en `Resistencia` y en la validación del aterrizaje. | El mismo, más un mando discreto con consecuencia irreversible dentro de la partida. |
| Bimotor ligero | `Potencia del motor` **pasa a ser una por motor**; `Combustible` se reparte por lado y el desbalance importa. La `Actitud` deja de depender solo de los mandos de vuelo: la asimetría de empuje la mueve. | Consola duplicada; la guiñada pasa de coordinación puntual a entrada sostenida. |
| Anfibio / hidroavión | `Velocidad (IAS)` gana una fase de agua antes del despegue; el `Viento` actúa además sobre la superficie. La frenada en tierra **desaparece** del modelo cuando opera sobre flotadores. | Sin frenos de pedal en agua; con selector de tren en el anfibio. |
| Variante de patín de cola | La guiñada en tierra deja de ser un valor estable y pasa a ser una variable que diverge sin corrección del piloto. | El mismo, con el rodaje modelado como fase activa. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Hel{¿Hélice de paso<br/>fijo o variable?}
    Hel -- Fijo --> Esc[Consola de escuela:<br/>acelerador y mezcla]
    Hel -- Variable --> Var[Consola ampliada:<br/>acelerador, hélice y mezcla]
    Esc --> V1[Potencia como escalar 0-100%]
    Var --> V2[Potencia desdoblada:<br/>demanda y régimen]
    Modelo --> Tren{¿Tren fijo<br/>o retráctil?}
    Tren -- Fijo --> Sin[Sin mando de tren:<br/>nada que olvidar]
    Tren -- Retráctil --> Con[Mando de tren con estado<br/>y aviso en aproximación]
    Modelo --> Rod{¿Rueda de morro<br/>o patín de cola?}
    Rod -- Rueda de morro --> Pas[Rodaje estable:<br/>pedales para corregir]
    Rod -- Patín de cola --> Act[Rodaje activo:<br/>pedales todo el tiempo]
    Modelo --> Mot{¿Uno o dos<br/>motores?}
    Mot -- Uno --> Sim[Un juego de mandos de motor]
    Mot -- Dos --> Dob[Mandos duplicados<br/>y empuje asimétrico posible]
```

---

## ⚠️ Qué modelos no comparten simulador

Tres familias no se resuelven con un ajuste de parámetros, porque su esquema de
control es otro:

- **El bimotor ligero** frente al resto: no tiene una consola más grande, tiene
  dos consolas. `Potencia del motor` deja de ser una variable y pasa a ser dos, y
  la diferencia entre ambas produce una fuerza que ningún mando de vuelo del
  Clase 5 estaba pensado para compensar de forma continua.
- **El turismo con paso variable y tren retráctil** frente al de escuela: añade
  dos mandos que no existen en el mapa del Clase 5 y una variable de estado que
  no existe en el Clase 9. Es un puesto de mando distinto, no un avión más
  rápido.
- **El hidroavión de flotadores** frente a los de rueda: le falta una entrada
  —los frenos en las puntas de los pedales— y le sobra una fase, la del agua, que
  el ciclo básico del Clase 9 no recorre. En el anfibio el problema se agrava:
  el mismo mando de tren tiene la posición correcta invertida según la superficie.

El resto de modelos sí caben en un mismo simulador ajustando rangos, tal como
plantean los [niveles de realismo](../../../docs/03-niveles-de-realismo.md): en
el nivel 1 casi todos se comportan igual, y las diferencias emergen a medida que
el nivel sube. La variante de patín de cola es el caso intermedio: comparte
mandos con el de escuela, pero solo se distingue de él si el simulador modela el
rodaje como algo más que un traslado hasta la pista.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar entrenador de ala alta frente a turismo de ala baja frente al mismo encargo**?

### Explicación razonada

Las variantes «entrenador de ala alta frente a turismo de ala baja» resuelven prioridades distintas. Una comparación profesional sigue la cadena motor → hélice → flujo de aire → alas y mandos: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **balance entre sustentación, peso, empuje y resistencia dentro de una envolvente limitada**. El hilo de
seguridad consiste en reconocer a tiempo **pérdida aerodinámica o salida de pista por velocidad y trayectoria inestables** y poder justificar la decisión
**estabilizar aproximación y frustrar si no se cumplen criterios antes del umbral**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → hélice → flujo de aire → alas y mandos**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Aviation Handbooks and Manuals](https://www.faa.gov/regulations_policies/handbooks_manuals) aporta aerodinámica, sistemas y operación;
[Normativa aeronáutica](https://www.dgac.gob.cl/normativa/) se usa para marco aeronáutico chileno. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **aproximación con viento cruzado y pista corta**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **motor** hasta **alas y mandos**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **motor → hélice → flujo de aire → alas y mandos** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «aproximación con viento cruzado y pista corta» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Aviones pequeños mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-avion-pequeno.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-avion-pequeno.md)
