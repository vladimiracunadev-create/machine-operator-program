<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: TRENPASAJERO-03
curso: tren-pasajeros
titulo: "Modelos y variantes del tren de pasajeros"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRENPASAJERO-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Tren de pasajeros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de pasajeros."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-tren-pasajeros.md) ya dijo qué tipos de
tren de pasajeros existen y para qué sirve cada uno. Esta clase responde a lo
siguiente: **no todos se manejan igual**, y esa diferencia no es de matiz. Cambia
qué mandos tiene la máquina y, por tanto, qué debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** "Un tren" no es una sola máquina desde el
> punto de vista del mando. En un metro automático no hay manipulador de tracción
> que empujar: no es que sea más fácil de conducir, es que **no hay maquinista
> conduciendo**. Un simulador que presente un solo esquema de control está
> representando un tren concreto aunque diga representarlos todos.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-tren-pasajeros.md) describe un puesto de
mando con **manipulador de tracción** y **manipulador de freno** en el pupitre, un
**hombre muerto** que frena el tren si el maquinista lo suelta y un **panel ATP**
que repite la señal. El [Clase 9](../simulacion/diseno-simulador-tren-pasajeros.md)
expone una variable `Tracción aplicada` con rango `0-100%` que el usuario dosifica.
Ambos describen un tren **conducido por un maquinista**.

En un metro automático (ATC) esa `Tracción aplicada` no es una entrada del usuario:
es una salida del sistema, calculada contra el perfil de velocidad. El hombre
muerto tampoco tiene a quién vigilar. Si el simulador se construye sobre el esquema
con maquinista y luego se le "añade" el metro automático, el resultado es un metro
automático con hombre muerto, que no existe.

La segunda bisagra es dónde vive la tracción. El
[Clase 4](../operacion/sistemas-mecanicos-tren-pasajeros.md) explica que la
adherencia depende del **peso por eje**: más carga sobre el eje, más agarre
disponible. En una EMU casi todos los ejes son motrices y el peso se reparte; en un
interurbano de locomotora más coches, toda la tracción sale de los ejes de la
locomotora y arrastra un remolque muerto. `Adherencia` deja de ser un valor único
del tren y pasa a ser un valor del bogie que tracciona.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia al conducirlo |
| --- | --- |
| Regional EMU | La referencia del curso: tracción distribuida en varios coches, arranque y frenada firmes, patinaje poco probable. |
| Metro / subterráneo | Recorrido corto entre paradas y alta frecuencia: la parada en andén domina la jornada. Con ATC, el maquinista supervisa en vez de conducir. |
| Suburbano / cercanías | Paradas frecuentes con masa que cambia en cada andén: el mismo tren frena distinto lleno que vacío. |
| Tren-tram | Circula en calle y en línea férrea: alterna la marcha por señal con la marcha a la vista, y el entorno deja de ser exclusivo. |
| Interurbano (locomotora más coches) | Toda la tracción sale de un extremo y arrastra la composición: el arranque es más propenso al patinaje y exige arenado. |
| Regional diesel-eléctrico | Sin catenaria: la energía es de a bordo y no hay línea a la que devolver el freno regenerativo. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Regional EMU, Suburbano, Interurbano | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Cambian los rangos y la dosificación, no los controles. |
| Metro automático (ATC) | **Desaparecen** el manipulador de tracción, el manipulador de freno y el hombre muerto. **Queda** el mando de puertas, el freno de emergencia y la radio tren-tierra. | El usuario deja de conducir y pasa a supervisar y despachar. Es otro modo de control, no otra dificultad. |
| Metro con maquinista | Ninguno desaparece, pero el **panel ATP** manda sobre el manipulador. | La señal deja de ser información y pasa a ser un límite duro. |
| Tren-tram | **Aparece** la marcha a la vista junto a la señal. | El panel ATP deja de ser la única autoridad: el maquinista vuelve a mirar el camino. |
| Regional diesel-eléctrico | **Desaparece** el indicador de tensión de línea de la catenaria. El freno dinámico deja de ser regenerativo. | Un instrumento de alta importancia del Clase 5 queda sin señal que mostrar. |
| Interurbano | **Sube de prioridad** el arenero: pasa de ayuda ocasional a mando de arranque. | El botón de arena entra en el ciclo normal, no solo en riel húmedo. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-tren-pasajeros.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Regional EMU | Ninguna: es el caso base. | El del Clase 5. |
| Metro automático (ATC) | `Tracción aplicada` y `Freno aplicado` **dejan de ser entradas** y pasan a ser salidas calculadas contra `Estado de la señal`. | Sin manipuladores ni hombre muerto: solo puertas, emergencia y radio. |
| Metro con maquinista | `Velocidad` **reduce** su rango útil frente a los 0-160 km/h del caso base; `Estado de la señal` gobierna el ciclo. | El mismo, con el ATP como techo permanente. |
| Suburbano / cercanías | `Masa del tren` deja de ser `fijo + pasajeros` al empezar y pasa a variar en cada andén durante la partida. | El mismo. |
| Tren-tram | `Estado de la señal` deja de ser la única restricción: se suma el entorno de calle. | El mismo, con marcha a la vista añadida. |
| Interurbano | `Adherencia` deja de ser un valor del tren y pasa a calcularse sobre los ejes motrices de la locomotora; `Masa del tren` crece frente a los ejes que traccionan. | El mismo, con arenado en el arranque. |
| Regional diesel-eléctrico | La tensión de línea **desaparece** del cuadro de instrumentos; el freno dinámico disipa en vez de devolver. `Presión de freno` no cambia. | El mismo. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Cond{¿Conduce un maquinista?}
    Cond -- Sí --> Manual[Esquema con maquinista:<br/>manipuladores, hombre muerto,<br/>vigilante]
    Cond -- No, ATC --> Auto[Esquema automático:<br/>sin manipuladores,<br/>puertas y emergencia]
    Manual --> Var1[Tracción y freno<br/>como entradas]
    Auto --> Var2[Tracción y freno<br/>como salidas del ATC]
    Modelo --> Trac{¿Tracción distribuida<br/>o concentrada?}
    Trac -- EMU distribuida --> Rep[Adherencia repartida<br/>en muchos ejes motrices]
    Trac -- Locomotora --> Con[Adherencia limitada<br/>a la locomotora,<br/>arenado al arrancar]
    Modelo --> Ener{¿Catenaria o diesel?}
    Ener -- Catenaria --> Regen[Tensión de línea<br/>y freno regenerativo]
    Ener -- Diesel --> Bordo[Energía de a bordo,<br/>freno dinámico disipativo]
```

---

## ⚠️ Qué modelos no comparten simulador

Dos familias no se resuelven con un ajuste de parámetros, porque su esquema de
control es otro:

- **El metro automático** frente al resto: faltan los dos manipuladores y el hombre
  muerto, y las dos variables centrales cambian de sentido, de entrada del usuario
  a salida del sistema. Lo que el usuario aprende ahí es supervisar y despachar, no
  conducir. Es un modo de control distinto, no una dificultad distinta.
- **El suburbano con masa variable** frente a los demás: obliga a que `Masa del
  tren` sea una variable viva que cambia en cada andén, no una constante que se
  fija al empezar la partida.

El resto de modelos sí caben en un mismo simulador ajustando rangos, tal como
plantean los [niveles de realismo](../../../docs/03-niveles-de-realismo.md): en el
nivel 1 casi todos se comportan igual, y las diferencias de tracción distribuida,
adherencia y arenado emergen a medida que el nivel sube.

Queda **por confirmar** el ancho de vía de la red chilena, tal como advierten el
[Clase 4](../operacion/sistemas-mecanicos-tren-pasajeros.md) y el
[Clase 9](../simulacion/diseno-simulador-tren-pasajeros.md). Mientras no se
confirme en la fuente oficial, ningún modelo de este cuadro debería fijar valores
por defecto de vía.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar unidad eléctrica múltiple frente a tren remolcado frente al mismo encargo**?

### Explicación razonada

Las variantes «unidad eléctrica múltiple frente a tren remolcado» resuelven prioridades distintas. Una comparación profesional sigue la cadena captación o motor → convertidor de tracción → motores de eje → rueda-carril: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **adherencia rueda-carril, curva de frenado y cumplimiento de señales**. El hilo de
seguridad consiste en reconocer a tiempo **rebasar el punto de parada o comprometer la comodidad por frenar tarde** y poder justificar la decisión
**anticipar la frenada según señal, pendiente, adherencia y carga**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **captación o motor → convertidor de tracción → motores de eje → rueda-carril**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Railroad Operating Practices](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0) aporta operación, señalización y competencias ferroviarias;
[Human Factors: Tasks and Demands](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands) se usa para factores humanos y carga de trabajo. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **aproximación a estación con lluvia y alta ocupación**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **captación o motor** hasta **rueda-carril**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **captación o motor → convertidor de tracción → motores de eje → rueda-carril** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «aproximación a estación con lluvia y alta ocupación» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Tren de pasajeros mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-tren-pasajeros.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-pasajeros.md)
