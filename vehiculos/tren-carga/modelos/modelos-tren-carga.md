<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: TRENCARGA-03
curso: tren-carga
titulo: "Modelos y variantes del tren de carga"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRENCARGA-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Tren de carga."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de carga."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-tren-carga.md) ya dijo qué tipos de
locomotora y de vagón existen y qué composiciones se arman con ellos. Este
módulo responde a otra cosa: **no todos los trenes se conducen igual**, y esa
diferencia no es de matiz. Cambia qué mandos tiene la cabina y, por tanto, qué
debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** "Un tren de carga" no es una sola
> máquina desde el punto de vista del mando. En un tren corto, la radio sirve
> para hablar; en un tren largo con locomotoras distribuidas, la radio **es**
> parte del mando de tracción: el manipulador no aplica fuerza en un punto,
> sino en varios a la vez. Un simulador que presente un solo esquema de control
> está representando un tren concreto aunque diga representarlos todos.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-tren-carga.md) describe un puesto con
manipulador de tracción, freno automático, freno independiente, freno dinámico,
inversor, arenado y radio. El [Clase 9](../simulacion/diseno-simulador-tren-carga.md)
expone variables como `Esfuerzo de tracción`, `Fuerza longitudinal` y
`Adherencia rueda-riel`. Ambos describen, sin decirlo, un tren **diesel-eléctrico
con locomotoras remotas**.

Cambia la fuente de energía y el freno dinámico deja de disipar calor en
resistencias para devolver energía a la catenaria: el mando se parece, pero la
consecuencia energética es opuesta. Cambia la longitud del tren y la
`Fuerza longitudinal` deja de tener un punto de aplicación para tener varios,
repartidos a lo largo de la composición. Si el simulador se construye sobre el
esquema del tren corto y luego se le "añaden" locomotoras remotas, el resultado
es un tren largo cuyas fuerzas internas nacen todas del enganche delantero, que
es justamente lo que el *distributed power* existe para evitar.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia al conducirlo |
| --- | --- |
| Diesel-eléctrica | La referencia del curso: potencia a bordo, autonomía en cualquier vía, el motor diesel gira a régimen casi constante y la fuerza se dosifica con el control eléctrico. |
| Eléctrica por catenaria | Más potencia disponible desde el arranque, pero la máquina depende de la línea: fuera del tramo electrificado no hay tracción posible. |
| Tren corto (una locomotora líder) | Toda la fuerza entra por el enganche delantero. El tren se estira y se comprime como una sola cadena; el arranque progresivo lo resuelve casi todo. |
| Tren largo con locomotoras distribuidas | El esfuerzo entra en varios puntos. Hay que pensar el tren por tramos: uno puede estar en tensión mientras otro sigue comprimido. |
| Tren unitario | Masa homogénea de punta a punta: el tren responde de forma previsible y las fuerzas se reparten de manera pareja. |
| Tren mixto | Vagones de distinto tipo y peso: el comportamiento cambia según dónde quedó lo pesado en el orden de la composición. |
| Maniobras en patio | Velocidades bajas, tren en armado y longitud cambiante: la máquina se mueve más de lo que arrastra. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Diesel-eléctrica | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Es el caso base del curso. |
| Eléctrica por catenaria | **Desaparece** el motor diesel como sistema a bordo y **aparece** el pantógrafo como condición de la tracción. El freno dinámico pasa a ser regenerativo. | El mismo gesto de freno dinámico devuelve energía a la catenaria en vez de disiparla; sin línea, el manipulador de tracción no manda nada. |
| Tren corto (una locomotora líder) | **Desaparece** el mando de las remotas: la radio queda solo como enlace con el control. | El manipulador de tracción aplica fuerza en un único punto del tren. |
| Tren largo con locomotoras distribuidas | La radio **se convierte** en parte del mando de tracción: replica el manipulador en las locomotoras remotas. | Un mando de comunicación pasa a ser un mando de fuerza; hay testigos de estado de remotas que vigilar. |
| Tren unitario | Ninguno: cambian los rangos, no los controles. | El arenado y el freno se dosifican igual en toda la composición. |
| Tren mixto | Ninguno, pero el freno automático **deja de actuar de forma pareja** sobre vagones de masa muy distinta. | El mismo movimiento de palanca da un resultado desigual a lo largo del tren. |
| Maniobras en patio | El **freno independiente** pasa de ajuste fino a mando principal; el **inversor** se usa constantemente. | El freno automático de tren deja de ser el recurso habitual. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-tren-carga.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Diesel-eléctrica | Ninguna: es el caso base. | El del Clase 5. |
| Eléctrica por catenaria | `Esfuerzo de tracción` pasa a depender de la línea disponible además de la `Adherencia rueda-riel`. La energía del freno dinámico deja de disiparse y se devuelve. | El mismo, con el pantógrafo y el tramo electrificado como condición previa. |
| Tren corto (una locomotora líder) | `Fuerza longitudinal` **se simplifica**: un solo origen de tracción, tensión y compresión encadenadas desde el frente. | Sin entrada de mando a remotas. |
| Tren largo con locomotoras distribuidas | `Fuerza longitudinal` **deja de ser un valor** y pasa a ser una distribución por tramos. `Masa total` se reparte entre varios puntos de tracción. | Manipulador que actúa en varios puntos vía radio; testigos de remotas. |
| Tren unitario | `Masa total` es homogénea por vagón: el reparto se calcula una vez. | El mismo. |
| Tren mixto | `Masa total` **deja de ser uniforme** y se vuelve un perfil según el orden de vagones; `Fuerza longitudinal` depende de ese orden. | El mismo. |
| Maniobras en patio | `Velocidad` reduce mucho su rango útil. `Masa total` **deja de ser fija** y cambia durante la partida al enganchar y desenganchar. | Freno independiente como mando primario; inversor de uso continuo. |
| Cualquiera con riel húmedo | `Adherencia rueda-riel` baja y el arenado gana peso en el cálculo. | El mismo, con más advertencia de patinaje. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Larg{¿Lleva locomotoras<br/>remotas?}
    Larg -- No --> Corto[Esquema de tren corto:<br/>un punto de tracción,<br/>radio solo comunica]
    Larg -- Sí --> Largo[Esquema distribuido:<br/>varios puntos de tracción,<br/>radio manda fuerza]
    Corto --> Var1[Fuerza longitudinal<br/>como cadena única]
    Largo --> Var2[Fuerza longitudinal<br/>repartida por tramos]
    Modelo --> Energia{¿Diesel-eléctrica<br/>o catenaria?}
    Energia -- Diesel-eléctrica --> Dies[Autonomía en toda la vía,<br/>dinámico a resistencias]
    Energia -- Catenaria --> Elec[Tramo electrificado obligatorio,<br/>freno regenerativo]
    Modelo --> Comp{¿Unitario o mixto?}
    Comp -- Unitario --> Homo[Masa homogénea:<br/>reparto previsible]
    Comp -- Mixto --> Hete[Masa por perfil:<br/>depende del orden]
```

---

## ⚠️ Qué modelos no comparten simulador

Tres familias no se resuelven con un ajuste de parámetros, porque su esquema de
control es otro:

- **El tren largo con locomotoras distribuidas** frente al tren corto: la radio
  deja de ser un enlace y pasa a ser un mando de fuerza, y `Fuerza longitudinal`
  deja de ser una cadena para volverse un reparto por tramos. Es un modo de
  control distinto, no una dificultad distinta.
- **La eléctrica por catenaria** frente a la diesel-eléctrica: la tracción queda
  condicionada por la infraestructura de la vía, no solo por la adherencia, y el
  freno dinámico cambia de destino energético. El mando se ve igual y hace otra
  cosa.
- **Las maniobras en patio** frente a la marcha en corredor: `Masa total` tiene
  que ser una variable viva durante la partida, no una constante que se fija al
  empezar, y el freno independiente desplaza al automático como mando principal.

El tren unitario y el tren mixto sí caben en un mismo simulador ajustando el
perfil de masa, tal como plantean los
[niveles de realismo](../../../docs/03-niveles-de-realismo.md): en el nivel 1
casi todos se comportan igual, y las diferencias emergen a medida que el nivel
sube. Los propios [Módulos 6](../operacion/principios-tren-carga.md) y
[9](../simulacion/diseno-simulador-tren-carga.md) sitúan las fuerzas
longitudinales y el *distributed power* en el nivel 3, que es exactamente donde
estos modelos dejan de ser el mismo tren.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar carga unitaria frente a carga mixta frente al mismo encargo**?

### Explicación razonada

Las variantes «carga unitaria frente a carga mixta» resuelven prioridades distintas. Una comparación profesional sigue la cadena locomotora → generador y tracción → enganches → rueda-carril: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **fuerzas longitudinales del tren y propagación del freno neumático**. El hilo de
seguridad consiste en reconocer a tiempo **rotura de enganche, patinaje o compresión excesiva del convoy** y poder justificar la decisión
**aplicar potencia y freno de modo gradual considerando la longitud completa**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **locomotora → generador y tracción → enganches → rueda-carril**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Railroad Operating Practices](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0) aporta operación, señalización y competencias ferroviarias;
[Human Factors: Tasks and Demands](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands) se usa para factores humanos y carga de trabajo. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **arranque de un tren largo en rampa con holguras entre enganches**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **locomotora** hasta **rueda-carril**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **locomotora → generador y tracción → enganches → rueda-carril** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «arranque de un tren largo en rampa con holguras entre enganches» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Tren de carga mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-tren-carga.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-carga.md)
