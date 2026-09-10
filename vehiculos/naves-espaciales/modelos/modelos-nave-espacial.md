<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: NAVESESPACIA-03
curso: naves-espaciales
titulo: "Modelos y variantes de la nave espacial"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: NAVESESPACIA-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Naves espaciales."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Naves espaciales."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-nave-espacial.md) ya dijo qué tipos de
nave espacial existen y para qué sirve cada uno. Esta clase responde a lo
siguiente: **no todas se manejan igual**, y esa diferencia no es de matiz. Cambia
qué mandos tiene la máquina y, por tanto, qué debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** "Una nave espacial" no es una sola
> máquina desde el punto de vista del mando. Un satélite no tiene tripulación a
> bordo: no es que sus mandos sean más simples, es que **la cabina no existe** y
> el soporte vital tampoco. Un simulador que presente un solo puesto de pilotaje
> está representando una nave tripulada aunque diga representarlas todas.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-nave-espacial.md) describe una cabina con
control de actitud, control de empuje, panel de soporte vital y una radio que
mantiene el contacto con control. El
[Clase 9](../simulacion/diseno-simulador-nave-espacial.md) expone una variable
`Recursos vitales` que afecta a la tripulación. Ambos describen una nave
**tripulada y en órbita terrestre**.

En un satélite no hay nadie a bordo que accione esa consola: quien manda está en
tierra, y la variable `Recursos vitales` no tiene a quién afectar. En una sonda
interplanetaria el problema se agrava, porque la radio del Clase 5 —la que
avisa de que hay retardo a gran distancia— deja de ser un mando de apoyo y pasa
a ser **el único mando**, con una demora que impide corregir en tiempo real. Si
el simulador se construye sobre el esquema tripulado y luego se le "añade" una
sonda, el resultado es una sonda pilotada al instante desde una cabina, que no
existe.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia en su operación |
| --- | --- |
| Cápsula tripulada | La referencia del curso: tripulación a bordo, misión corta, ciclo completo de lanzamiento, órbita y reentrada. |
| Cohete lanzador | Solo vive las fases de ascenso y separación de etapas: su masa cae por escalones y nunca llega a operar en órbita como nave. |
| Estación espacial | No maniobra para llegar: ya está. La operación es de larga duración y el soporte vital deja de ser un consumo para volverse un ciclo que hay que reciclar. |
| Satélite | Nadie a bordo. La operación se reduce a mantener la actitud, apuntar y administrar energía entre sol y sombra. |
| Sonda interplanetaria | El retardo de la comunicación obliga a operar por secuencias programadas: se ordena lo que se hará, no lo que se está haciendo. |
| Nave de ficción | Su operación la fija el escenario, no la física orbital, y por eso debe ir siempre etiquetada como ficción. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Cápsula tripulada | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Cambian los rangos y las fases, no los controles. |
| Cohete lanzador | **Desaparecen** el acoplamiento y la navegación orbital fina; el control de empuje y la separación de etapas concentran todo. | El puesto se reduce a guiar el ascenso; no hay maniobra que planificar. |
| Estación espacial | **Desaparece** el control de empuje como maniobra habitual. El soporte vital **asciende** de lectura a mando central. | Se opera un hábitat, no un vehículo: se gestiona, no se pilota. |
| Satélite | **Desaparecen** el soporte vital y todo el puesto de cabina. Las comunicaciones **se convierten** en el mando único, desde tierra. | Sin nadie a bordo no hay ergonomía de cabina que diseñar: hay una consola remota. |
| Sonda interplanetaria | **Desaparece** el mando en tiempo real. Las comunicaciones traen un retardo que **inserta** una planificación previa entre la orden y el efecto. | No se corrige lo que se ve: se ve lo que ya ocurrió. Es otro modo de control. |
| Nave de ficción | **Aparecen** los mandos que el escenario invente. | Deben quedar separados de los reales con etiquetas claras. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-nave-espacial.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Cápsula tripulada | Ninguna: es el caso base. | El del Clase 5. |
| Cohete lanzador | `Altitud orbital` y `Velocidad orbital` solo recorren el tramo de ascenso. `Propelente` se consume por etapas, no de forma continua. `Temperatura del escudo` no interviene. | El mismo, recortado: empuje y actitud, sin acoplamiento. |
| Estación espacial | `Delta-v disponible` pierde peso: casi no maniobra. `Recursos vitales` pasa de consumo a ciclo de reciclaje y se vuelve la variable dominante. | El mismo, con el soporte vital al centro. |
| Satélite | `Recursos vitales` **se elimina**: no hay tripulación. `Temperatura del escudo` **desaparece**: no reentra. `Actitud` y la energía disponible pasan a ser el juego entero. | Sin cabina: consola remota, sin entrada de soporte vital. |
| Sonda interplanetaria | `Recursos vitales` **se elimina**. `Delta-v disponible` se planifica con años de antelación y `Actitud` se ordena, no se corrige. **Aparece** el retardo de comunicación como variable propia. | Sin control en tiempo real: se envían secuencias y se espera. |
| Nave de ficción | `Modo ciencia/ficción` pasa a `ficción` y libera las reglas físicas del resto. | El que el escenario defina, siempre etiquetado. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Trip{¿Hay tripulación<br/>a bordo?}
    Trip -- Sí --> Cabina[Esquema de cabina:<br/>actitud, empuje,<br/>soporte vital]
    Trip -- No --> Remoto[Esquema remoto:<br/>consola en tierra,<br/>sin soporte vital]
    Cabina --> Var1[Simulador con variable<br/>Recursos vitales]
    Remoto --> Var2[Simulador sin variable<br/>Recursos vitales]
    Remoto --> Dist{¿Retardo de<br/>comunicación?}
    Dist -- Corto --> Directo[Órdenes casi inmediatas]
    Dist -- Largo --> Secuencia[Secuencias programadas:<br/>sin corrección en vivo]
    Modelo --> Fis{¿Ciencia o ficción?}
    Fis -- Ciencia --> Real[Física orbital<br/>y delta-v limitado]
    Fis -- Ficción --> Fic[Reglas del escenario,<br/>etiquetadas como ficción]
```

---

## ⚠️ Qué modelos no comparten simulador

Tres familias no se resuelven con un ajuste de parámetros, porque su esquema de
control es otro:

- **El satélite** frente a la cápsula: no falta un mando, falta el puesto entero.
  Sin tripulación a bordo desaparecen el soporte vital y la ergonomía de cabina,
  y el control se muda a una consola remota. Es un modo de control distinto, no
  una dificultad distinta.
- **La sonda interplanetaria** frente a todo lo demás: el retardo rompe el lazo
  entre ver y corregir. El ciclo del Clase 9 —leer la entrada del usuario y
  actualizar el estado— deja de cerrarse en el mismo instante, y eso no es un
  parámetro: es otra arquitectura.
- **La nave de ficción** frente a las reales: no comparte las reglas físicas, así
  que tampoco puede compartir el motor que las calcula sin marcar la frontera.

El cohete lanzador y la estación espacial sí caben en el mismo simulador que la
cápsula ajustando fases y rangos, tal como plantean los
[niveles de realismo](../../../docs/03-niveles-de-realismo.md): en el nivel 1 la
operación guiada los acerca, y las diferencias emergen a medida que el nivel
sube.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar cápsula tripulada frente a sonda robótica frente al mismo encargo**?

### Explicación razonada

Las variantes «cápsula tripulada frente a sonda robótica» resuelven prioridades distintas. Una comparación profesional sigue la cadena fuente de energía → propulsión → navegación y control → órbita o trayectoria: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **pequeños cambios de velocidad producen cambios acumulativos de órbita y ventanas de encuentro**. El hilo de
seguridad consiste en reconocer a tiempo **colisión o imposibilidad de retirada por quemado mal orientado o tardío** y poder justificar la decisión
**verificar marco de referencia, ventana, delta-v y opción de aborto antes del encendido**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **fuente de energía → propulsión → navegación y control → órbita o trayectoria**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Spaceships and Rockets](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/) aporta naves, sistemas y misiones;
[Space Law Treaties and Principles](https://www.unoosa.org/oosa/SpaceLaw/treaties.html) se usa para derecho espacial internacional. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **maniobra de aproximación orbital con combustible de reserva limitado**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **fuente de energía** hasta **órbita o trayectoria**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **fuente de energía → propulsión → navegación y control → órbita o trayectoria** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «maniobra de aproximación orbital con combustible de reserva limitado» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Naves espaciales mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-nave-espacial.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-espacial.md)
</content>
</invoke>
