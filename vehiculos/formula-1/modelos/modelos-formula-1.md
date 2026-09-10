<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: FORMULA1-03
curso: formula-1
titulo: "Modelos y variantes del Fórmula 1"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: FORMULA1-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Fórmula 1."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Fórmula 1."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del Fórmula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-formula-1.md) ya dijo qué familias de
monoplaza existen: las que define el reglamento (actual e histórico) y las que
define el reglaje (alta carga, baja carga, lluvia). Esta clase responde a algo
distinto: **no todas se pilotan igual**, y esa diferencia no es de matiz. Cambia
qué mandos tiene la máquina y, por tanto, qué debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** "Un Fórmula 1" no es una sola máquina
> desde el punto de vista del mando. Un monoplaza histórico no tiene botón de
> impulso ERS: no es que lo tenga más simple, es que **no existe**, porque no
> hay hibridación que gestionar. Un simulador que presente un solo esquema de
> control está representando un monoplaza concreto aunque diga representarlos
> todos.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-formula-1.md) describe un puesto de mando
con un **botón de impulso ERS** en el volante, de prioridad alta, cuya función
es "solicitar entrega eléctrica" y cuya nota dice "gestión de energía por
vuelta". El [Clase 9](../simulacion/diseno-simulador-formula-1.md) expone una
variable `Energía ERS` con rango `0-100%`, que afecta al impulso disponible y
que "se gasta y recupera por vuelta". Ambos describen un monoplaza **híbrido**:
el del campeonato vigente.

En un monoplaza histórico, que el Clase 2 define con "motores atmosféricos, sin
hibridación", ese botón no manda nada. Y la variable `Energía ERS` sencillamente
no tiene valores que tomar. Si el simulador se construye sobre el esquema
híbrido y luego se le "añade" un histórico, el resultado es un monoplaza
atmosférico con ERS, que no existe.

Lo mismo pasa, en menor escala, con el reglaje: el reglaje de lluvia no quita
mandos, pero mueve dos variables (`Adherencia` y `Temperatura de gomas`) fuera
del rango con el que el resto del curso razona.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia al conducirlo |
| --- | --- |
| Monoplaza actual | La referencia del curso: efecto suelo, unidad híbrida V6 turbo y gestión de energía por vuelta. Todo el Clase 6 está escrito sobre él. |
| Monoplaza histórico | Sin hibridación que administrar, la atención se libera hacia la trazada y la frenada. La carga aerodinámica es menor o inexistente según la era: la velocidad de paso por curva no crece con la velocidad como en el actual. |
| Alta carga aerodinámica | Máximo agarre en curva: se puede girar más rápido, pero la resistencia castiga la recta. El coche depende de mantener velocidad, no de recuperarla. |
| Baja carga aerodinámica | Más velocidad punta y menos agarre en apoyo: la frenada se alarga y el vértice exige más precisión. |
| Reglaje de lluvia | Neumáticos de lluvia y menos potencia aplicada. La adherencia deja de ser un valor estable de asfalto seco y el error se paga antes. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Monoplaza actual | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Es el caso base del curso. |
| Monoplaza histórico | **Desaparece** el botón de impulso ERS: sin hibridación no hay entrega eléctrica que solicitar. La ruleta de mezcla y el estado de energía del tablero se quedan sin contenido. | El piloto pierde una decisión estratégica por vuelta. La pantalla del volante, que el Clase 5 pide priorizar en "marcha, delta y estado de energía", queda con dos de tres. |
| Alta carga / baja carga | Ninguno: cambian los valores de reglaje, no los controles. | El botón DRS pesa mucho más en baja carga, donde la recta es el terreno de juego. |
| Reglaje de lluvia | Ninguno **desaparece**, pero el DRS deja de estar disponible cuando la dirección de carrera no lo habilita, tal como pide el propio Clase 5. | Un mando de prioridad alta se vuelve inerte sin que el piloto lo decida. |
| Todos | Las **ruletas de ajuste** (reparto de frenada, mezcla, diferencial) no cambian de sitio, pero cambian de peso según el modelo. | No es un mando nuevo, pero altera el resultado de todos los demás. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-formula-1.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Monoplaza actual | Ninguna: es el caso base. | El del Clase 5. |
| Monoplaza histórico | `Energía ERS` **se elimina**: sin hibridación no hay carga que gastar ni recuperar. `Carga aerodinámica` reduce su rango o desaparece según la era del Clase 1. `Combustible` sigue pesando, pero deja de estar acotado por el flujo regulado del reglamento actual. | Sin entrada de impulso ERS; la gestión de energía sale del ciclo básico. |
| Alta carga aerodinámica | `Carga aerodinámica` se fija en el extremo alto; `Velocidad` recorta su techo por resistencia. | El mismo. |
| Baja carga aerodinámica | `Carga aerodinámica` se fija en el extremo bajo; `Velocidad` alcanza el techo del rango y `Adherencia` importa más en apoyo. | El mismo, con el DRS como recurso central. |
| Reglaje de lluvia | `Adherencia` deja de ser un valor de asfalto seco y baja de forma sostenida. `Temperatura de gomas` cambia de ventana: el problema pasa de sobrecalentar a no llegar a temperatura. `Desgaste de gomas` sigue otra curva. | El mismo, con el DRS deshabilitado por el escenario. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Regl{¿Reglamento actual<br/>o histórico?}
    Regl -- Actual --> Hibrido[Esquema híbrido:<br/>botón ERS, ruleta de mezcla,<br/>estado de energía en pantalla]
    Regl -- Histórico --> Atmo[Esquema atmosférico:<br/>sin botón ERS,<br/>sin gestión de energía]
    Hibrido --> Var1[Simulador con variable Energía ERS]
    Atmo --> Var2[Simulador sin variable Energía ERS]
    Modelo --> Reglaje{¿Qué reglaje?}
    Reglaje -- Alta carga --> AltaC[Carga alta:<br/>agarre en curva,<br/>techo de velocidad menor]
    Reglaje -- Baja carga --> BajaC[Carga baja:<br/>velocidad punta,<br/>DRS decisivo]
    Reglaje -- Lluvia --> Lluv[Adherencia baja,<br/>otra ventana térmica,<br/>DRS deshabilitado]
```

---

## ⚠️ Qué modelos no comparten simulador

Un solo modelo no se resuelve con un ajuste de parámetros, porque su esquema de
control es otro:

- **El monoplaza histórico** frente al resto: falta una entrada de prioridad
  alta y desaparece una variable entera del Clase 9. La gestión de energía deja
  de ser un paso del ciclo básico, no un paso más barato. Es un modo de control
  distinto, no una dificultad distinta.

Las tres configuraciones de reglaje sí caben en un mismo simulador ajustando
rangos, porque comparten volante, pedales y variables:

- **Alta y baja carga** solo mueven `Carga aerodinámica` y el techo de
  `Velocidad`.
- **El reglaje de lluvia** mueve `Adherencia` y `Temperatura de gomas`, y apaga
  el DRS desde el escenario, no desde el modelo del coche.

Esto encaja con los [niveles de realismo](../../../docs/03-niveles-de-realismo.md)
que recoge el [Clase 6](../operacion/principios-formula-1.md): en el nivel 1
todos los reglajes se comportan casi igual, la carga aerodinámica y la
adherencia aparecen en el nivel 2, y la gestión de energía ERS —lo único que
separa de verdad al histórico del actual— no llega hasta el nivel 3.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar configuración de alta carga frente a baja carga aerodinámica frente al mismo encargo**?

### Explicación razonada

Las variantes «configuración de alta carga frente a baja carga aerodinámica» resuelven prioridades distintas. Una comparación profesional sigue la cadena unidad de potencia → caja secuencial → diferencial → neumáticos: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **interacción entre carga aerodinámica, temperatura del neumático y balance del monoplaza**. El hilo de
seguridad consiste en reconocer a tiempo **sobrepasar el agarre disponible al cambiar el balance con freno, volante o acelerador** y poder justificar la decisión
**sacrificar velocidad de entrada para conservar estabilidad y tracción de salida**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **unidad de potencia → caja secuencial → diferencial → neumáticos**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Formula 1 Regulations](https://www.fia.com/regulations/formula-1) aporta reglamento, arquitectura y seguridad de Fórmula 1;
[Vehicle Safety](https://www.nhtsa.gov/vehicle-safety) se usa para seguridad de vehículos terrestres. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **entrada y salida de una curva rápida durante una tanda con neumáticos degradados**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **unidad de potencia** hasta **neumáticos**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **unidad de potencia → caja secuencial → diferencial → neumáticos** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «entrada y salida de una curva rápida durante una tanda con neumáticos degradados» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Fórmula 1 mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [FIA-F1-2026](https://www.fia.com/regulations/formula-1): Formula 1 Regulations, FIA. Uso: reglamento, arquitectura y seguridad de Fórmula 1.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-formula-1.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-formula-1.md)
