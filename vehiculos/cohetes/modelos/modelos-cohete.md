<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: COHETES-03
curso: cohetes
titulo: "Modelos y variantes del cohete"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: COHETES-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Cohetes."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Cohetes."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del cohete

[🏠 Inicio](../../../README.md) · [🚀 Curso: Cohetes](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-cohete.md) ya dijo qué tipos de cohete
existen y para qué sirve cada uno. Esta clase responde a lo siguiente: **no
todos se operan igual**, y esa diferencia no es de matiz. Cambia qué mandos tiene
la máquina y, por tanto, qué debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** "Un cohete" no es una sola máquina desde
> el punto de vista del mando. Un motor sólido no se apaga ni se regula: no es
> que sea más difícil de dosificar, es que **el mando de empuje no existe**. Un
> simulador que presente un solo esquema de control está representando un cohete
> concreto aunque diga representarlos todos.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-cohete.md) describe unas entradas de
simulación con `Regular empuje` en Shift y Ctrl y `Retornar propulsor` en la
tecla R. El [Clase 9](../simulacion/diseno-simulador-cohete.md) expone una
variable `Empuje` con rango `0-100 porciento` y una `Reserva de aterrizaje`.
Ambos describen un cohete **de motor líquido y primera etapa recuperable**.

En un cohete de motor sólido, esas teclas no tienen nada que ajustar: el
[Clase 4](../operacion/sistemas-mecanicos-cohete.md) es explícito en que el
empuje no se regula y el motor no se apaga a voluntad una vez encendido. Y en un
lanzador desechable, la tecla R no manda sobre nada: la fase de retorno del
propulsor no ocurre. Si el simulador se construye sobre el esquema líquido y
recuperable y luego se le "añaden" las demás variantes, el resultado es un
propulsor sólido con acelerador, que no existe.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia en su operación |
| --- | --- |
| Lanzador mediano | La referencia del curso: ascenso por etapas, giro gradual e inserción orbital con margen de decisión. |
| Lanzador ligero | Menos etapas y menos margen: cada segundo de propelente cuenta y el momento de separación se estrecha. |
| Lanzador pesado | Más etapas y más masa: el empuje inicial es enorme y el esfuerzo estructural manda sobre el ritmo del ascenso. |
| De motor líquido | El empuje se dosifica durante todo el vuelo: se puede aliviar la estructura y apagar antes de agotar el tanque. |
| De motor sólido | Una vez encendido, el vuelo está comprometido: solo queda orientar y esperar a que el propelente se agote. |
| Desechable | El vuelo termina en la inserción orbital: todo el propelente se puede gastar en subir. |
| Recuperable | Aparece una fase posterior: hay que guardar propelente para el retorno y volar el ascenso pensando en el aterrizaje. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Lanzador ligero, mediano, pesado | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Cambian los rangos y los tiempos, no los controles. |
| De motor líquido | Ninguno: es el caso para el que está escrito el Clase 5. | `Regular empuje` y el apagado ordenado están disponibles. |
| De motor sólido | **Desaparecen** `Regular empuje` y el apagado de motores. `Separar etapa` deja de ser una decisión y se vuelve consecuencia del agotamiento. | Del despegue solo quedan `Orientar el cohete` y `Abortar`; el corte de emergencia no puede apagar el motor, solo salvar la carga. |
| Desechable | **Desaparece** `Retornar propulsor`. | Tras la separación no hay nada que pilotar abajo: la etapa se pierde. |
| Recuperable | **Aparece** `Retornar propulsor` con los encendidos de reentrada y aterrizaje. | El mismo mando de empuje se usa dos veces en el mismo vuelo, con objetivos opuestos. |
| Tripulado (cápsula) | **Aparecen** el panel de tripulación y la palanca de aborto. | El aborto deja de ser solo una orden de tierra y pasa a tener prioridad a bordo. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-cohete.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Lanzador mediano | Ninguna: es el caso base. | El del Clase 5. |
| Lanzador ligero | `Propelente` y `Masa total` reducen su rango; `Altitud` y `Velocidad horizontal` se acotan a órbita baja. | El mismo, con menos tolerancia al error. |
| Lanzador pesado | `Masa total` y `Estado de etapas` amplían rango; `Ángulo de ascenso` pesa más por el esfuerzo estructural. | El mismo, con respuesta más lenta. |
| De motor líquido | Ninguna: `Empuje` es la variable regulable que el módulo asume. | El del Clase 5. |
| De motor sólido | `Empuje` **deja de ser numérica** y pasa a discreta: encendido o agotado. `Propelente` deja de ser una entrada del usuario y solo se consume. | Sin entrada de empuje ni de apagado; solo actitud y aborto. |
| Desechable | `Reserva de aterrizaje` **se elimina**. `Estado de etapas` termina en separada, sin retorno. | Sin entrada de retorno del propulsor. |
| Recuperable | `Reserva de aterrizaje` **se activa** y compite con `Propelente` durante el ascenso. | El del Clase 5, con una segunda fase de guiado tras la separación. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Prop{¿Propelente líquido<br/>o sólido?}
    Prop -- Líquido --> Regulable[Esquema regulable:<br/>empuje ajustable,<br/>apagado y reencendido]
    Prop -- Sólido --> Fijo[Esquema fijo:<br/>sin mando de empuje,<br/>solo actitud y aborto]
    Regulable --> Var1[Simulador con Empuje numérico]
    Fijo --> Var2[Simulador con Empuje discreto]
    Modelo --> Reuso{¿Desechable<br/>o recuperable?}
    Reuso -- Desechable --> Una[Una sola fase:<br/>sin Reserva de aterrizaje]
    Reuso -- Recuperable --> Dos[Dos fases:<br/>reserva guardada<br/>y retorno guiado]
```

---

## ⚠️ Qué modelos no comparten simulador

Dos familias no se resuelven con un ajuste de parámetros, porque su esquema de
control es otro:

- **El cohete de motor sólido** frente al líquido: falta la entrada de empuje y
  la variable que la recoge cambia de tipo. Es un modo de control distinto, no
  una dificultad distinta.
- **El lanzador recuperable** frente al desechable: añade una fase completa de
  vuelo tras la separación y obliga a que la reserva de aterrizaje sea una
  decisión viva durante el ascenso, no una constante que se fija al empezar.

El resto de modelos sí caben en un mismo simulador ajustando rangos, tal como
plantean los [niveles de realismo](../../../docs/03-niveles-de-realismo.md): en
el nivel 1 casi todos se comportan igual, y las diferencias emergen a medida que
el nivel sube; el retorno del propulsor, de hecho, solo aparece en el nivel 3.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar cohete de combustible líquido frente a sólido frente al mismo encargo**?

### Explicación razonada

Las variantes «cohete de combustible líquido frente a sólido» resuelven prioridades distintas. Una comparación profesional sigue la cadena propelentes → cámara → tobera → empuje y trayectoria: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **la aceleración depende de empuje menos peso y resistencia, mientras la masa disminuye**. El hilo de
seguridad consiste en reconocer a tiempo **inestabilidad, desviación o cargas excesivas durante máxima presión dinámica** y poder justificar la decisión
**evaluar trayectoria, estabilidad y condiciones de aborto antes del lanzamiento**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **propelentes → cámara → tobera → empuje y trayectoria**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Rockets Educator Guide](https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf) aporta propulsión, estabilidad y trayectoria;
[Space Law Treaties and Principles](https://www.unoosa.org/oosa/SpaceLaw/treaties.html) se usa para derecho espacial internacional. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **ascenso educativo con cambio de etapa y viento en altura**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **propelentes** hasta **empuje y trayectoria**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **propelentes → cámara → tobera → empuje y trayectoria** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «ascenso educativo con cambio de etapa y viento en altura» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Cohetes mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-ROCKETS](https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf): Rockets Educator Guide, NASA. Uso: propulsión, estabilidad y trayectoria.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-cohete.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-cohete.md)
