<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: NAUTILUS-03
curso: nautilus
titulo: "Modelos y variantes del Nautilus"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: NAUTILUS-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Nautilus."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Nautilus."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del Nautilus

[🏠 Inicio](../../../README.md) · [🐙 Curso: Nautilus](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-nautilus.md) ya dijo qué es el
Nautilus, qué forma tiene y qué sabe hacer. Esta clase responde a lo siguiente:
**el Nautilus no es una familia de naves, es una sola**. No hay variantes que
comparar entre sí. Lo que sí se puede comparar, y es donde está la lección, es el
Nautilus frente a los submarinos que existían de verdad en su época y frente a
los que existen hoy. Ahí sí cambia qué mandos hay en el puesto, y por tanto qué
debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** El Nautilus es una nave de ficción,
> imaginada por Julio Verne en 1870 y hoy en dominio público. Inventarle
> versiones sería inventar datos, así que este módulo no lo hace. En su lugar usa
> el eje honesto que el propio curso ya tiene abierto desde el
> [Clase 1](../historia/historia-nautilus.md): la nave imaginada, los
> sumergibles reales de su siglo y el submarino moderno. Un simulador que
> presente un solo esquema de control está representando **una** de esas
> máquinas, aunque diga representar "un submarino".

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-nautilus.md) describe un puesto con panel
de lastre, timón de dirección, timones de profundidad y una **consola de
energía** con regulador de propulsión eléctrica. El
[Clase 9](../simulacion/diseno-simulador-nautilus.md) expone una variable
`Energía` con rango `0-100%` y una variable `Modo ciencia/ficción`. Ambos
describen al Nautilus **de la novela**.

Ese puesto no es el de un sumergible de 1870. El [Clase 1](../historia/historia-nautilus.md)
sitúa en 1863 los primeros submarinos de propulsión mecánica y recuerda que Verne
escribió cuando "casi todo funcionaba a vapor": la consola de energía eléctrica
del Clase 5 no tenía dónde existir. Y tampoco es el de un submarino moderno: el
[Clase 4](../operacion/sistemas-mecanicos-nautilus.md) señala que hoy se usan
generadores de oxígeno a bordo, mientras que la válvula de renovación de aire del
Nautilus solo funciona en superficie.

Si el simulador se construye sobre el puesto del Clase 5 y luego se le "añade"
un sumergible de 1776, el resultado es un sumergible de 1776 con regulador
eléctrico, que nunca existió.

---

## 🗂️ Qué cambia en el manejo

| Modelo o variante | Qué cambia al gobernarlo |
| --- | --- |
| Nautilus, modo ficción | La referencia del curso. Sumerge y emerge de forma controlada siempre, el casco aguanta la profundidad que pida la aventura y la energía parece inagotable ([Clase 8](../reglamentos/reglas-universo-nautilus.md)). |
| Nautilus, modo ciencia | La misma nave, pero la profundidad tiene un límite de aplastamiento y el aire y la energía se agotan. El piloto deja de explorar y empieza a administrar. |
| Sumergible de remos (1620) | Solo hay casco que baja y sube; el curso no le atribuye más. El avance depende de la fuerza humana, así que no se "gobierna" un rumbo, se rema. |
| Sumergible de lastre, una plaza (1776) | Aparece el lastre de agua para sumergir, pero una sola persona hace todo. No hay reparto de tareas entre gobierno, lastre y energía. |
| Submarino de propulsión mecánica (1863) | Motor en lugar de fuerza humana: por primera vez la velocidad es una decisión y no un esfuerzo. Autonomía muy corta. |
| Submarino de motor y batería (1900-1918) | Doble propulsión y autonomía real limitada: la superficie deja de ser un lugar al que subir a voluntad y pasa a ser una necesidad periódica. |
| Submarino nuclear (1954-hoy) | Gran autonomía, como intuyó la ficción. Subir a ventilar deja de marcar el ritmo de la misión; el límite se corre hacia la tripulación. |

---

## 🎛️ Qué cambia en el mando

| Modelo o variante | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Nautilus, modo ficción y modo ciencia | Ninguno: el mapa de controles del Clase 5 aplica tal cual en ambos. | Cambian los límites y los avisos, no los controles. El modo no toca el puesto, toca la física. |
| Sumergible de remos (1620) | **Desaparece** todo salvo el casco: sin panel de lastre documentado, sin consola de energía, sin timones. | No hay puesto de mando que simular; hay un casco y personas remando. |
| Sumergible de lastre, una plaza (1776) | **Aparece** el lastre de agua. Siguen sin existir la consola de energía y la iluminación exterior. | Se puede sumergir, pero no se puede alumbrar ni regular potencia: navegar a ciegas es la condición normal. |
| Submarino de propulsión mecánica (1863) | **Aparece** un mando de propulsión, pero **mecánico**, no la consola eléctrica del Clase 5. | La velocidad ya es un mando; la energía todavía no es un instrumento que vigilar. |
| Submarino de motor y batería (1900-1918) | **Aparece** la gestión de dos fuentes de propulsión, que el puesto del Nautilus no contempla. | El piloto elige fuente, algo que el Clase 5 nunca le pide: allí la energía es una sola. |
| Submarino nuclear (1954-hoy) | **Desaparece** la atadura de la válvula de renovación de aire a la superficie: el Clase 4 registra generadores de oxígeno a bordo. | La acción "Ventilar aire", que el Clase 5 marca como "solo posible en superficie", deja de ser el reloj de la inmersión. |
| Todos los reales, frente al Nautilus | **Falta** en el Nautilus cualquier mando de detección: ante la oscuridad total del [Clase 7](../operacion/entornos-nautilus.md), su única respuesta es el interruptor de iluminación exterior. | El riesgo de choque contra el relieve del fondo queda sin instrumento propio: se ve o no se ve. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-nautilus.md):

| Modelo o variante | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Nautilus, modo ficción | `Modo ciencia/ficción` = ficción. `Aire respirable` y `Energía` dejan de ser restrictivos y `Profundidad` usa todo su rango. | El del Clase 5. |
| Nautilus, modo ciencia | `Modo ciencia/ficción` = ciencia. `Presión exterior` limita `Profundidad`; `Aire respirable` y `Energía` se consumen de verdad. | El del Clase 5, con avisos activos. |
| Sumergible de remos (1620) | `Energía` **desaparece** como recurso de a bordo y `Velocidad` deja de depender de un mando. `Lastre` no está documentado. | Sin puesto: no hay esquema de control que compartir. |
| Sumergible de lastre, una plaza (1776) | Quedan `Lastre`, `Flotabilidad neta` y `Profundidad`. `Energía` y `Velocidad` **se eliminan**. | Solo el panel de lastre; sin consola de energía. |
| Submarino de propulsión mecánica (1863) | Vuelve `Velocidad`, pero `Energía` no es eléctrica y su rango útil es mucho más corto. | Panel de lastre más propulsión mecánica. |
| Submarino de motor y batería (1900-1918) | `Energía` **se desdobla** en dos fuentes y `Aire respirable` marca el ritmo: la superficie es obligatoria. | El del Clase 5 más una entrada de selección de fuente. |
| Submarino nuclear (1954-hoy) | `Energía` deja de ser el límite práctico y `Aire respirable` se repone sumergido: ninguna de las dos fuerza subir. | El del Clase 5 sin la atadura de "ventilar solo en superficie". |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Lastre{¿Tiene panel<br/>de lastre?}
    Lastre -- No --> Casco[Sin puesto:<br/>solo casco que<br/>sube y baja]
    Lastre -- Sí --> Energia{¿Tiene consola<br/>de energía?}
    Energia -- No --> Ciego[Esquema mínimo:<br/>lastre y timones,<br/>sin luz ni potencia]
    Energia -- Sí --> Puesto[Esquema del Clase 5:<br/>lastre, timones,<br/>propulsión, luz]
    Puesto --> Aire{¿El aire se repone<br/>solo en superficie?}
    Aire -- Sí --> Reloj[Aire respirable<br/>marca el ritmo<br/>de la inmersión]
    Aire -- No --> Libre[Sin obligación<br/>de subir a ventilar]
    Puesto --> Modo{¿Modo ciencia<br/>o ficción?}
    Modo -- Ciencia --> Limite[Presión y consumo<br/>limitan la profundidad]
    Modo -- Ficción --> Aventura[Profundidad libre,<br/>autonomía casi<br/>ilimitada]
```

---

## ⚠️ Qué modelos no comparten simulador

Tres casos no se resuelven ajustando parámetros, porque su esquema de control es
otro:

- **Los sumergibles anteriores a la novela** (1620 y 1776) frente al Nautilus:
  no les falta potencia, les falta el puesto entero. Sin consola de energía no
  hay regulador de propulsión ni iluminación exterior, y sin iluminación el
  entorno de gran profundidad del Clase 7 deja de ser jugable. Es otra máquina,
  no una versión modesta de la misma.
- **El submarino de motor y batería** frente al Nautilus: obliga a que `Energía`
  sea dos recursos y no uno, y a que el piloto elija entre ellos. El puesto del
  Clase 5 no tiene esa entrada.
- **El submarino nuclear** frente al Nautilus: rompe la regla que sostiene todo
  el diseño de la inmersión, que ventilar solo se puede en superficie. Quitarla
  no hace la partida más fácil: la deja sin reloj.

En cambio, los dos **modos** del Nautilus sí comparten simulador, y por diseño:
el Clase 9 los resuelve con la variable `Modo ciencia/ficción` sobre el mismo
puesto de mando. Esa gradación es la misma idea que plantean los
[niveles de realismo](../../../docs/03-niveles-de-realismo.md): en el nivel 1
basta con sumergir, emerger y vigilar la profundidad, y las diferencias emergen a
medida que el nivel sube.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar Nautilus literario frente a submarino moderno frente al mismo encargo**?

### Explicación razonada

Las variantes «Nautilus literario frente a submarino moderno» resuelven prioridades distintas. Una comparación profesional sigue la cadena energía descrita en la obra → motor → hélice → casco y timones: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **lectura doble: tecnología imaginada por Verne y principios reales de flotabilidad y presión**. El hilo de
seguridad consiste en reconocer a tiempo **colisión o exceso de profundidad al tomar la descripción literaria como procedimiento real** y poder justificar la decisión
**citar el canon y contrastar cada maniobra con física y navegación reales**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **energía descrita en la obra → motor → hélice → casco y timones**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Twenty Thousand Leagues under the Sea](https://www.gutenberg.org/ebooks/164) aporta obra primaria en dominio público;
[Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) se usa para navegación, SOLAS, COLREG y STCW. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **inmersión narrativa cerca de relieve submarino**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **energía descrita en la obra** hasta **casco y timones**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **energía descrita en la obra → motor → hélice → casco y timones** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «inmersión narrativa cerca de relieve submarino» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Nautilus mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [GUTENBERG-20000](https://www.gutenberg.org/ebooks/164): Twenty Thousand Leagues under the Sea, Project Gutenberg. Uso: obra primaria en dominio público.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-nautilus.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-nautilus.md)
